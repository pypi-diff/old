# Comparing `tmp/tencentcloud-sdk-python-3.0.98.tar.gz` & `tmp/tencentcloud-sdk-python-3.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tencentcloud-sdk-python-3.0.98.tar", last modified: Fri Oct 25 09:33:25 2019, max compression
+gzip compressed data, was "dist/tencentcloud-sdk-python-3.0.99.tar", last modified: Mon Oct 28 08:59:43 2019, max compression
```

## Comparing `tencentcloud-sdk-python-3.0.98.tar` & `tencentcloud-sdk-python-3.0.99.tar`

### file list

```diff
@@ -1,617 +1,633 @@
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/
--rw-rw-rw-   0 root         (0) root         (0)       67 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)    11351 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/LICENSE
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/
--rw-rw-rw-   0 root         (0) root         (0)      677 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/lb.py
--rw-rw-rw-   0 root         (0) root         (0)      687 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/monitor.py
--rw-rw-rw-   0 root         (0) root         (0)      689 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/partners.py
--rw-rw-rw-   0 root         (0) root         (0)      687 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/scaling.py
--rw-rw-rw-   0 root         (0) root         (0)      680 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/sec.py
--rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/trade.py
--rw-rw-rw-   0 root         (0) root         (0)      693 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/cloudaudit.py
--rw-rw-rw-   0 root         (0) root         (0)      687 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/account.py
--rw-rw-rw-   0 root         (0) root         (0)      691 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/feecenter.py
--rw-rw-rw-   0 root         (0) root         (0)      717 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/scf.py
--rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/eip.py
--rw-rw-rw-   0 root         (0) root         (0)      776 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/emr.py
--rw-rw-rw-   0 root         (0) root         (0)      681 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/cmem.py
--rw-rw-rw-   0 root         (0) root         (0)      802 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/athena.py
--rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/bgpip.py
--rw-rw-rw-   0 root         (0) root         (0)      685 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/market.py
--rw-rw-rw-   0 root         (0) root         (0)      693 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/apigateway.py
--rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/bmvpc.py
--rw-rw-rw-   0 root         (0) root         (0)      689 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/snapshot.py
--rw-rw-rw-   0 root         (0) root         (0)     5487 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/base.py
--rw-rw-rw-   0 root         (0) root         (0)      785 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/tmt.py
--rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/redis.py
--rw-rw-rw-   0 root         (0) root         (0)     1346 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/cdn.py
--rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/tdsql.py
--rw-rw-rw-   0 root         (0) root         (0)      780 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/sts.py
--rw-rw-rw-   0 root         (0) root         (0)      685 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/wenzhi.py
--rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/vod.py
--rw-rw-rw-   0 root         (0) root         (0)      685 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/yunsou.py
--rw-rw-rw-   0 root         (0) root         (0)      681 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/bmlb.py
--rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/cdb.py
--rw-rw-rw-   0 root         (0) root         (0)      787 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/ccr.py
--rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/vpc.py
--rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/image.py
--rw-rw-rw-   0 root         (0) root         (0)      681 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/live.py
--rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/ccs.py
--rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/batch.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/cvm.py
--rw-rw-rw-   0 root         (0) root         (0)      811 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/dc.py
--rw-rw-rw-   0 root         (0) root         (0)      793 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/tbaas.py
--rw-rw-rw-   0 root         (0) root         (0)      681 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/bill.py
--rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/dfw.py
--rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/cns.py
--rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/cbs.py
--rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/bmeip.py
--rw-rw-rw-   0 root         (0) root         (0)      677 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/modules/bm.py
--rw-rw-rw-   0 root         (0) root         (0)     6751 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/qcloudapi.py
--rw-rw-rw-   0 root         (0) root         (0)       23 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/common/
--rw-rw-rw-   0 root         (0) root         (0)     1378 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/common/api_exception.py
--rw-rw-rw-   0 root         (0) root         (0)     1197 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/common/sign.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/common/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     5077 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/QcloudApi/common/request.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/captcha/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/captcha/v20190722/
--rw-rw-rw-   0 root         (0) root         (0)     4674 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/captcha/v20190722/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/captcha/v20190722/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2187 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/captcha/v20190722/captcha_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/captcha/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/kms/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/kms/v20190118/
--rw-rw-rw-   0 root         (0) root         (0)    37259 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/kms/v20190118/models.py
--rw-rw-rw-   0 root         (0) root         (0)    30543 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/kms/v20190118/kms_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/kms/v20190118/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/kms/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/faceid/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/faceid/v20180301/
--rw-rw-rw-   0 root         (0) root         (0)    29855 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/faceid/v20180301/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/faceid/v20180301/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    17237 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/faceid/v20180301/faceid_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/faceid/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/chdfs/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/chdfs/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/chdfs/v20190718/
--rw-rw-rw-   0 root         (0) root         (0)    22009 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/chdfs/v20190718/chdfs_client.py
--rw-rw-rw-   0 root         (0) root         (0)    28153 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/chdfs/v20190718/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/chdfs/v20190718/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/clb/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/clb/v20180317/
--rw-rw-rw-   0 root         (0) root         (0)   119469 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/clb/v20180317/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/clb/v20180317/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    52029 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/clb/v20180317/clb_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/clb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bizlive/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bizlive/v20190313/
--rw-rw-rw-   0 root         (0) root         (0)     6186 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bizlive/v20190313/models.py
--rw-rw-rw-   0 root         (0) root         (0)     4630 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bizlive/v20190313/bizlive_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bizlive/v20190313/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bizlive/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmvpc/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmvpc/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmvpc/v20180625/
--rw-rw-rw-   0 root         (0) root         (0)   127910 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmvpc/v20180625/models.py
--rw-rw-rw-   0 root         (0) root         (0)    76562 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmvpc/v20180625/bmvpc_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmvpc/v20180625/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ds/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ds/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ds/v20180523/
--rw-rw-rw-   0 root         (0) root         (0)    17206 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ds/v20180523/ds_client.py
--rw-rw-rw-   0 root         (0) root         (0)    25275 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ds/v20180523/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ds/v20180523/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cam/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cam/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cam/v20190116/
--rw-rw-rw-   0 root         (0) root         (0)    73511 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cam/v20190116/models.py
--rw-rw-rw-   0 root         (0) root         (0)    51349 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cam/v20190116/cam_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cam/v20190116/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/drm/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/drm/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/drm/v20181115/
--rw-rw-rw-   0 root         (0) root         (0)    20236 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/drm/v20181115/models.py
--rw-rw-rw-   0 root         (0) root         (0)    10052 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/drm/v20181115/drm_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/drm/v20181115/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/live/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/live/v20180801/
--rw-rw-rw-   0 root         (0) root         (0)   121972 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/live/v20180801/live_client.py
--rw-rw-rw-   0 root         (0) root         (0)   216809 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/live/v20180801/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/live/v20180801/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/live/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iai/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iai/v20180301/
--rw-rw-rw-   0 root         (0) root         (0)    32286 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iai/v20180301/iai_client.py
--rw-rw-rw-   0 root         (0) root         (0)    66647 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iai/v20180301/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iai/v20180301/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iai/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iotexplorer/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iotexplorer/v20190423/
--rw-rw-rw-   0 root         (0) root         (0)    27515 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iotexplorer/v20190423/iotexplorer_client.py
--rw-rw-rw-   0 root         (0) root         (0)    43033 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iotexplorer/v20190423/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iotexplorer/v20190423/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iotexplorer/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tiems/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tiems/v20190416/
--rw-rw-rw-   0 root         (0) root         (0)    24632 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tiems/v20190416/models.py
--rw-rw-rw-   0 root         (0) root         (0)    10230 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tiems/v20190416/tiems_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tiems/v20190416/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tiems/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/partners/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/partners/v20180321/
--rw-rw-rw-   0 root         (0) root         (0)    40079 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/partners/v20180321/models.py
--rw-rw-rw-   0 root         (0) root         (0)    18158 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/partners/v20180321/partners_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/partners/v20180321/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/partners/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/habo/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/habo/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/habo/v20181203/
--rw-rw-rw-   0 root         (0) root         (0)     3714 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/habo/v20181203/models.py
--rw-rw-rw-   0 root         (0) root         (0)     3356 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/habo/v20181203/habo_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/habo/v20181203/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/sqlserver/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/sqlserver/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/sqlserver/v20180328/
--rw-rw-rw-   0 root         (0) root         (0)    94601 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/sqlserver/v20180328/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/sqlserver/v20180328/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    49632 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/sqlserver/v20180328/sqlserver_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/youmall/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/youmall/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/youmall/v20180228/
--rw-rw-rw-   0 root         (0) root         (0)    95293 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/youmall/v20180228/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/youmall/v20180228/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    40451 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/youmall/v20180228/youmall_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tav/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tav/v20190118/
--rw-rw-rw-   0 root         (0) root         (0)     7391 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tav/v20190118/models.py
--rw-rw-rw-   0 root         (0) root         (0)     5530 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tav/v20190118/tav_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tav/v20190118/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tav/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmlb/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmlb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmlb/v20180625/
--rw-rw-rw-   0 root         (0) root         (0)   174774 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmlb/v20180625/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmlb/v20180625/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    61421 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmlb/v20180625/bmlb_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/hcm/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/hcm/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/hcm/v20181106/
--rw-rw-rw-   0 root         (0) root         (0)     5686 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/hcm/v20181106/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/hcm/v20181106/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2215 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/hcm/v20181106/hcm_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tci/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tci/v20190318/
--rw-rw-rw-   0 root         (0) root         (0)   149539 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tci/v20190318/models.py
--rw-rw-rw-   0 root         (0) root         (0)    56015 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tci/v20190318/tci_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tci/v20190318/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tci/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbaas/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbaas/v20180416/
--rw-rw-rw-   0 root         (0) root         (0)    40276 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbaas/v20180416/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbaas/v20180416/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    17269 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbaas/v20180416/tbaas_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbaas/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tics/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tics/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tics/v20181115/
--rw-rw-rw-   0 root         (0) root         (0)     6051 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tics/v20181115/tics_client.py
--rw-rw-rw-   0 root         (0) root         (0)    15988 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tics/v20181115/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tics/v20181115/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bri/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bri/v20190328/
--rw-rw-rw-   0 root         (0) root         (0)     6081 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bri/v20190328/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bri/v20190328/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2565 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bri/v20190328/bri_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bri/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ticm/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ticm/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ticm/v20181127/
--rw-rw-rw-   0 root         (0) root         (0)    13649 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ticm/v20181127/models.py
--rw-rw-rw-   0 root         (0) root         (0)     2307 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ticm/v20181127/ticm_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ticm/v20181127/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/billing/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/billing/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/billing/v20180709/
--rw-rw-rw-   0 root         (0) root         (0)    52267 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/billing/v20180709/models.py
--rw-rw-rw-   0 root         (0) root         (0)    14333 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/billing/v20180709/billing_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/billing/v20180709/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cloudaudit/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cloudaudit/v20190319/
--rw-rw-rw-   0 root         (0) root         (0)    15282 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cloudaudit/v20190319/cloudaudit_client.py
--rw-rw-rw-   0 root         (0) root         (0)    27628 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cloudaudit/v20190319/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cloudaudit/v20190319/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cloudaudit/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cws/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cws/v20180312/
--rw-rw-rw-   0 root         (0) root         (0)    46637 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cws/v20180312/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cws/v20180312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    24051 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cws/v20180312/cws_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cws/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ic/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ic/v20190307/
--rw-rw-rw-   0 root         (0) root         (0)    15283 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ic/v20190307/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ic/v20190307/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     6605 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ic/v20190307/ic_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ic/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbp/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbp/v20190311/
--rw-rw-rw-   0 root         (0) root         (0)    11765 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbp/v20190311/models.py
--rw-rw-rw-   0 root         (0) root         (0)     4464 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbp/v20190311/tbp_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbp/v20190311/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbp/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbp/v20190627/
--rw-rw-rw-   0 root         (0) root         (0)    11133 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbp/v20190627/models.py
--rw-rw-rw-   0 root         (0) root         (0)     3247 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbp/v20190627/tbp_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbp/v20190627/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tiia/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tiia/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tiia/v20190529/
--rw-rw-rw-   0 root         (0) root         (0)    34751 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tiia/v20190529/models.py
--rw-rw-rw-   0 root         (0) root         (0)    10233 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tiia/v20190529/tiia_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tiia/v20190529/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/msp/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/msp/v20180319/
--rw-rw-rw-   0 root         (0) root         (0)     9388 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/msp/v20180319/msp_client.py
--rw-rw-rw-   0 root         (0) root         (0)    16478 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/msp/v20180319/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/msp/v20180319/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/msp/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ms/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ms/v20180408/
--rw-rw-rw-   0 root         (0) root         (0)    57336 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ms/v20180408/models.py
--rw-rw-rw-   0 root         (0) root         (0)    19959 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ms/v20180408/ms_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ms/v20180408/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ms/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cis/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cis/v20180408/
--rw-rw-rw-   0 root         (0) root         (0)    20158 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cis/v20180408/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cis/v20180408/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     9728 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cis/v20180408/cis_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cis/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bm/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bm/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bm/v20180423/
--rw-rw-rw-   0 root         (0) root         (0)   129729 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bm/v20180423/models.py
--rw-rw-rw-   0 root         (0) root         (0)    62154 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bm/v20180423/bm_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bm/v20180423/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbm/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbm/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbm/v20180129/
--rw-rw-rw-   0 root         (0) root         (0)    27606 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbm/v20180129/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbm/v20180129/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    13039 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tbm/v20180129/tbm_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cds/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cds/v20180420/
--rw-rw-rw-   0 root         (0) root         (0)     7361 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cds/v20180420/cds_client.py
--rw-rw-rw-   0 root         (0) root         (0)    11833 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cds/v20180420/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cds/v20180420/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cds/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cr/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cr/v20180321/
--rw-rw-rw-   0 root         (0) root         (0)    24599 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cr/v20180321/models.py
--rw-rw-rw-   0 root         (0) root         (0)    13876 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cr/v20180321/cr_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cr/v20180321/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cr/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cdn/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cdn/v20180606/
--rw-rw-rw-   0 root         (0) root         (0)    46334 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cdn/v20180606/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cdn/v20180606/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    21336 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cdn/v20180606/cdn_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cdn/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/gaap/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/gaap/v20180529/
--rw-rw-rw-   0 root         (0) root         (0)   187297 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/gaap/v20180529/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/gaap/v20180529/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    97555 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/gaap/v20180529/gaap_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/gaap/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/trtc/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/trtc/v20190722/
--rw-rw-rw-   0 root         (0) root         (0)     2635 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/trtc/v20190722/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/trtc/v20190722/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     3504 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/trtc/v20190722/trtc_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/trtc/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tts/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tts/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tts/v20190823/
--rw-rw-rw-   0 root         (0) root         (0)     4159 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tts/v20190823/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tts/v20190823/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2497 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tts/v20190823/tts_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/scf/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/scf/v20180416/
--rw-rw-rw-   0 root         (0) root         (0)    61599 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/scf/v20180416/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/scf/v20180416/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    22525 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/scf/v20180416/scf_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/scf/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/postgres/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/postgres/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)    32968 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/postgres/v20170312/postgres_client.py
--rw-rw-rw-   0 root         (0) root         (0)    61242 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/postgres/v20170312/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/postgres/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/postgres/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cdb/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cdb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cdb/v20170320/
--rw-rw-rw-   0 root         (0) root         (0)   206477 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cdb/v20170320/models.py
--rw-rw-rw-   0 root         (0) root         (0)    99356 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cdb/v20170320/cdb_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cdb/v20170320/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ocr/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ocr/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ocr/v20181119/
--rw-rw-rw-   0 root         (0) root         (0)   137607 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ocr/v20181119/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ocr/v20181119/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    60811 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ocr/v20181119/ocr_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/asr/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/asr/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/asr/v20190614/
--rw-rw-rw-   0 root         (0) root         (0)     5958 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/asr/v20190614/asr_client.py
--rw-rw-rw-   0 root         (0) root         (0)     9594 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/asr/v20190614/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/asr/v20190614/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mariadb/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mariadb/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)   105039 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mariadb/v20170312/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mariadb/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    49657 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mariadb/v20170312/mariadb_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mariadb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/sts/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/sts/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/sts/v20180813/
--rw-rw-rw-   0 root         (0) root         (0)     8051 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/sts/v20180813/models.py
--rw-rw-rw-   0 root         (0) root         (0)     4504 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/sts/v20180813/sts_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/sts/v20180813/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dts/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dts/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dts/v20180330/
--rw-rw-rw-   0 root         (0) root         (0)    49379 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dts/v20180330/models.py
--rw-rw-rw-   0 root         (0) root         (0)    24662 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dts/v20180330/dts_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dts/v20180330/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/aai/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/aai/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/aai/v20180522/
--rw-rw-rw-   0 root         (0) root         (0)     6632 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/aai/v20180522/aai_client.py
--rw-rw-rw-   0 root         (0) root         (0)    11875 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/aai/v20180522/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/aai/v20180522/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ecc/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ecc/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ecc/v20181213/
--rw-rw-rw-   0 root         (0) root         (0)    17322 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ecc/v20181213/models.py
--rw-rw-rw-   0 root         (0) root         (0)     4399 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ecc/v20181213/ecc_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/ecc/v20181213/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmeip/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmeip/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmeip/v20180625/
--rw-rw-rw-   0 root         (0) root         (0)    34618 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmeip/v20180625/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmeip/v20180625/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    22632 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/bmeip/v20180625/bmeip_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mps/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mps/v20190612/
--rw-rw-rw-   0 root         (0) root         (0)   177216 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mps/v20190612/models.py
--rw-rw-rw-   0 root         (0) root         (0)    45651 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mps/v20190612/mps_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mps/v20190612/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mps/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      629 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/soe/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/soe/v20180724/
--rw-rw-rw-   0 root         (0) root         (0)    34571 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/soe/v20180724/models.py
--rw-rw-rw-   0 root         (0) root         (0)     6826 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/soe/v20180724/soe_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/soe/v20180724/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/soe/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cvm/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cvm/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)   100489 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cvm/v20170312/cvm_client.py
--rw-rw-rw-   0 root         (0) root         (0)   213843 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cvm/v20170312/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cvm/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cvm/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/yunsou/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/yunsou/v20180504/
--rw-rw-rw-   0 root         (0) root         (0)     3289 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/yunsou/v20180504/yunsou_client.py
--rw-rw-rw-   0 root         (0) root         (0)     6794 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/yunsou/v20180504/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/yunsou/v20180504/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/yunsou/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/batch/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/batch/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)    36548 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/batch/v20170312/batch_client.py
--rw-rw-rw-   0 root         (0) root         (0)   134458 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/batch/v20170312/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/batch/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/batch/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dcdb/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dcdb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dcdb/v20180411/
--rw-rw-rw-   0 root         (0) root         (0)    93875 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dcdb/v20180411/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dcdb/v20180411/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    43090 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dcdb/v20180411/dcdb_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/redis/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/redis/v20180412/
--rw-rw-rw-   0 root         (0) root         (0)    85220 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/redis/v20180412/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/redis/v20180412/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    38102 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/redis/v20180412/redis_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/redis/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/vpc/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/vpc/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)   351207 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/vpc/v20170312/models.py
--rw-rw-rw-   0 root         (0) root         (0)   224661 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/vpc/v20170312/vpc_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/vpc/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/vpc/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cbs/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cbs/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)    91580 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cbs/v20170312/models.py
--rw-rw-rw-   0 root         (0) root         (0)    48059 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cbs/v20170312/cbs_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cbs/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cbs/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tia/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tia/v20180226/
--rw-rw-rw-   0 root         (0) root         (0)    27208 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tia/v20180226/models.py
--rw-rw-rw-   0 root         (0) root         (0)    13551 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tia/v20180226/tia_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tia/v20180226/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tia/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/autoscaling/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/autoscaling/v20180419/
--rw-rw-rw-   0 root         (0) root         (0)   153145 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/autoscaling/v20180419/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/autoscaling/v20180419/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    59326 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/autoscaling/v20180419/autoscaling_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/autoscaling/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/facefusion/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/facefusion/v20181201/
--rw-rw-rw-   0 root         (0) root         (0)     3621 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/facefusion/v20181201/facefusion_client.py
--rw-rw-rw-   0 root         (0) root         (0)    10150 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/facefusion/v20181201/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/facefusion/v20181201/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/facefusion/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/yunjing/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/yunjing/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/yunjing/v20180228/
--rw-rw-rw-   0 root         (0) root         (0)   126882 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/yunjing/v20180228/models.py
--rw-rw-rw-   0 root         (0) root         (0)    74383 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/yunjing/v20180228/yunjing_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/yunjing/v20180228/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/vod/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/vod/v20180717/
--rw-rw-rw-   0 root         (0) root         (0)   112500 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/vod/v20180717/vod_client.py
--rw-rw-rw-   0 root         (0) root         (0)   571041 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/vod/v20180717/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/vod/v20180717/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/vod/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mongodb/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mongodb/v20180408/
--rw-rw-rw-   0 root         (0) root         (0)    40960 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mongodb/v20180408/models.py
--rw-rw-rw-   0 root         (0) root         (0)    17355 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mongodb/v20180408/mongodb_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mongodb/v20180408/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/mongodb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cim/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cim/v20190318/
--rw-rw-rw-   0 root         (0) root         (0)     1423 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cim/v20190318/models.py
--rw-rw-rw-   0 root         (0) root         (0)     2162 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cim/v20190318/cim_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cim/v20190318/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cim/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/wss/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/wss/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/wss/v20180426/
--rw-rw-rw-   0 root         (0) root         (0)    13764 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/wss/v20180426/models.py
--rw-rw-rw-   0 root         (0) root         (0)     4452 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/wss/v20180426/wss_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/wss/v20180426/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/exception/
--rw-rw-rw-   0 root         (0) root         (0)      760 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/exception/tencent_cloud_sdk_exception.py
--rw-rw-rw-   0 root         (0) root         (0)       25 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/exception/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1557 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/sign.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    11870 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/abstract_client.py
--rw-rw-rw-   0 root         (0) root         (0)     1984 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/abstract_model.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/profile/
--rw-rw-rw-   0 root         (0) root         (0)     1405 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/profile/http_profile.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/profile/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1636 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/profile/client_profile.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/http/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/http/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     4973 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/http/request.py
--rw-rw-rw-   0 root         (0) root         (0)     2036 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/common/credential.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dc/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dc/v20180410/
--rw-rw-rw-   0 root         (0) root         (0)    14541 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dc/v20180410/dc_client.py
--rw-rw-rw-   0 root         (0) root         (0)    37127 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dc/v20180410/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dc/v20180410/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/dc/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/gme/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/gme/v20180711/
--rw-rw-rw-   0 root         (0) root         (0)    18270 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/gme/v20180711/models.py
--rw-rw-rw-   0 root         (0) root         (0)    12302 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/gme/v20180711/gme_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/gme/v20180711/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/gme/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/nlp/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/nlp/v20190408/
--rw-rw-rw-   0 root         (0) root         (0)    25716 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/nlp/v20190408/models.py
--rw-rw-rw-   0 root         (0) root         (0)    25668 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/nlp/v20190408/nlp_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/nlp/v20190408/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/nlp/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iotcloud/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iotcloud/v20180614/
--rw-rw-rw-   0 root         (0) root         (0)    41909 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iotcloud/v20180614/iotcloud_client.py
--rw-rw-rw-   0 root         (0) root         (0)    72050 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iotcloud/v20180614/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iotcloud/v20180614/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iotcloud/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iot/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iot/v20180123/
--rw-rw-rw-   0 root         (0) root         (0)    53839 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iot/v20180123/iot_client.py
--rw-rw-rw-   0 root         (0) root         (0)    86687 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iot/v20180123/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iot/v20180123/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iot/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tkgdq/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tkgdq/v20190411/
--rw-rw-rw-   0 root         (0) root         (0)     5037 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tkgdq/v20190411/tkgdq_client.py
--rw-rw-rw-   0 root         (0) root         (0)     7149 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tkgdq/v20190411/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tkgdq/v20190411/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tkgdq/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tmt/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tmt/v20180321/
--rw-rw-rw-   0 root         (0) root         (0)    12938 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tmt/v20180321/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tmt/v20180321/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     6972 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tmt/v20180321/tmt_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tmt/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cms/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cms/v20190321/
--rw-rw-rw-   0 root         (0) root         (0)    35530 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cms/v20190321/models.py
--rw-rw-rw-   0 root         (0) root         (0)    17364 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cms/v20190321/cms_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cms/v20190321/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cms/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tcb/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tcb/v20180608/
--rw-rw-rw-   0 root         (0) root         (0)    10353 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tcb/v20180608/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tcb/v20180608/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     5656 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tcb/v20180608/tcb_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tcb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tke/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tke/v20180525/
--rw-rw-rw-   0 root         (0) root         (0)    22361 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tke/v20180525/tke_client.py
--rw-rw-rw-   0 root         (0) root         (0)    63950 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tke/v20180525/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tke/v20180525/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tke/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/emr/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/emr/v20190103/
--rw-rw-rw-   0 root         (0) root         (0)    47110 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/emr/v20190103/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/emr/v20190103/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    11599 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/emr/v20190103/emr_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/emr/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tag/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tag/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tag/v20180813/
--rw-rw-rw-   0 root         (0) root         (0)    22955 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tag/v20180813/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tag/v20180813/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    14044 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tag/v20180813/tag_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/es/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/es/v20180416/
--rw-rw-rw-   0 root         (0) root         (0)    12324 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/es/v20180416/es_client.py
--rw-rw-rw-   0 root         (0) root         (0)    41323 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/es/v20180416/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/es/v20180416/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/es/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cfs/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cfs/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cfs/v20190719/
--rw-rw-rw-   0 root         (0) root         (0)    40017 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cfs/v20190719/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cfs/v20190719/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    23986 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/cfs/v20190719/cfs_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tsf/
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tsf/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tsf/v20180326/
--rw-rw-rw-   0 root         (0) root         (0)    80120 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tsf/v20180326/tsf_client.py
--rw-rw-rw-   0 root         (0) root         (0)   185441 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tsf/v20180326/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/tsf/v20180326/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/monitor/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/monitor/v20180724/
--rw-rw-rw-   0 root         (0) root         (0)     3652 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/monitor/v20180724/monitor_client.py
--rw-rw-rw-   0 root         (0) root         (0)    10105 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/monitor/v20180724/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/monitor/v20180724/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/monitor/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iottid/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iottid/v20190411/
--rw-rw-rw-   0 root         (0) root         (0)    12672 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iottid/v20190411/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iottid/v20190411/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    11743 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iottid/v20190411/iottid_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:33:07.000000 tencentcloud-sdk-python-3.0.98/tencentcloud/iottid/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1240 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/setup.py
--rw-rw-rw-   0 root         (0) root         (0)     1762 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)       65 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/MANIFEST.in
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud_sdk_python.egg-info/
--rw-rw-rw-   0 root         (0) root         (0)     1762 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud_sdk_python.egg-info/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)    15644 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud_sdk_python.egg-info/SOURCES.txt
--rw-rw-rw-   0 root         (0) root         (0)       23 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud_sdk_python.egg-info/top_level.txt
--rw-rw-rw-   0 root         (0) root         (0)        1 2019-10-25 09:33:25.000000 tencentcloud-sdk-python-3.0.98/tencentcloud_sdk_python.egg-info/dependency_links.txt
--rw-rw-rw-   0 root         (0) root         (0)      661 2019-10-25 09:33:06.000000 tencentcloud-sdk-python-3.0.98/README.rst
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/
+-rw-rw-rw-   0 root         (0) root         (0)       67 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)    11351 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/LICENSE
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/
+-rw-rw-rw-   0 root         (0) root         (0)      677 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/lb.py
+-rw-rw-rw-   0 root         (0) root         (0)      687 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/monitor.py
+-rw-rw-rw-   0 root         (0) root         (0)      689 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/partners.py
+-rw-rw-rw-   0 root         (0) root         (0)      687 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/scaling.py
+-rw-rw-rw-   0 root         (0) root         (0)      680 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/sec.py
+-rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/trade.py
+-rw-rw-rw-   0 root         (0) root         (0)      693 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/cloudaudit.py
+-rw-rw-rw-   0 root         (0) root         (0)      687 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/account.py
+-rw-rw-rw-   0 root         (0) root         (0)      691 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/feecenter.py
+-rw-rw-rw-   0 root         (0) root         (0)      717 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/scf.py
+-rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/eip.py
+-rw-rw-rw-   0 root         (0) root         (0)      776 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/emr.py
+-rw-rw-rw-   0 root         (0) root         (0)      681 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/cmem.py
+-rw-rw-rw-   0 root         (0) root         (0)      802 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/athena.py
+-rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/bgpip.py
+-rw-rw-rw-   0 root         (0) root         (0)      685 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/market.py
+-rw-rw-rw-   0 root         (0) root         (0)      693 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/apigateway.py
+-rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/bmvpc.py
+-rw-rw-rw-   0 root         (0) root         (0)      689 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/snapshot.py
+-rw-rw-rw-   0 root         (0) root         (0)     5487 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/base.py
+-rw-rw-rw-   0 root         (0) root         (0)      785 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/tmt.py
+-rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/redis.py
+-rw-rw-rw-   0 root         (0) root         (0)     1346 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/cdn.py
+-rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/tdsql.py
+-rw-rw-rw-   0 root         (0) root         (0)      780 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/sts.py
+-rw-rw-rw-   0 root         (0) root         (0)      685 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/wenzhi.py
+-rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/vod.py
+-rw-rw-rw-   0 root         (0) root         (0)      685 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/yunsou.py
+-rw-rw-rw-   0 root         (0) root         (0)      681 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/bmlb.py
+-rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/cdb.py
+-rw-rw-rw-   0 root         (0) root         (0)      787 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/ccr.py
+-rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/vpc.py
+-rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/image.py
+-rw-rw-rw-   0 root         (0) root         (0)      681 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/live.py
+-rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/ccs.py
+-rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/batch.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/cvm.py
+-rw-rw-rw-   0 root         (0) root         (0)      811 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/dc.py
+-rw-rw-rw-   0 root         (0) root         (0)      793 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/tbaas.py
+-rw-rw-rw-   0 root         (0) root         (0)      681 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/bill.py
+-rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/dfw.py
+-rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/cns.py
+-rw-rw-rw-   0 root         (0) root         (0)      679 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/cbs.py
+-rw-rw-rw-   0 root         (0) root         (0)      683 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/bmeip.py
+-rw-rw-rw-   0 root         (0) root         (0)      677 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/modules/bm.py
+-rw-rw-rw-   0 root         (0) root         (0)     6751 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/qcloudapi.py
+-rw-rw-rw-   0 root         (0) root         (0)       23 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/common/
+-rw-rw-rw-   0 root         (0) root         (0)     1378 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/common/api_exception.py
+-rw-rw-rw-   0 root         (0) root         (0)     1197 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/common/sign.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/common/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     5077 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/QcloudApi/common/request.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/captcha/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/captcha/v20190722/
+-rw-rw-rw-   0 root         (0) root         (0)     4674 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/captcha/v20190722/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/captcha/v20190722/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2187 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/captcha/v20190722/captcha_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/captcha/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/kms/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/kms/v20190118/
+-rw-rw-rw-   0 root         (0) root         (0)    38352 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/kms/v20190118/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    31689 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/kms/v20190118/kms_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/kms/v20190118/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/kms/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/faceid/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/faceid/v20180301/
+-rw-rw-rw-   0 root         (0) root         (0)    29855 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/faceid/v20180301/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/faceid/v20180301/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    17237 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/faceid/v20180301/faceid_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/faceid/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/chdfs/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/chdfs/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/chdfs/v20190718/
+-rw-rw-rw-   0 root         (0) root         (0)    22009 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/chdfs/v20190718/chdfs_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    28153 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/chdfs/v20190718/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/chdfs/v20190718/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/clb/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/clb/v20180317/
+-rw-rw-rw-   0 root         (0) root         (0)   119469 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/clb/v20180317/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/clb/v20180317/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    52029 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/clb/v20180317/clb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/clb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bizlive/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bizlive/v20190313/
+-rw-rw-rw-   0 root         (0) root         (0)     6186 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bizlive/v20190313/models.py
+-rw-rw-rw-   0 root         (0) root         (0)     4630 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bizlive/v20190313/bizlive_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bizlive/v20190313/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bizlive/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmvpc/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmvpc/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmvpc/v20180625/
+-rw-rw-rw-   0 root         (0) root         (0)   127910 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmvpc/v20180625/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    76562 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmvpc/v20180625/bmvpc_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmvpc/v20180625/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/organization/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/organization/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/organization/v20181225/
+-rw-rw-rw-   0 root         (0) root         (0)    25450 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/organization/v20181225/organization_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    24942 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/organization/v20181225/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/organization/v20181225/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ds/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ds/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ds/v20180523/
+-rw-rw-rw-   0 root         (0) root         (0)    17206 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ds/v20180523/ds_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    25275 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ds/v20180523/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ds/v20180523/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cam/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cam/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cam/v20190116/
+-rw-rw-rw-   0 root         (0) root         (0)    73511 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cam/v20190116/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    51349 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cam/v20190116/cam_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cam/v20190116/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/drm/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/drm/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/drm/v20181115/
+-rw-rw-rw-   0 root         (0) root         (0)    20236 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/drm/v20181115/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    10052 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/drm/v20181115/drm_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/drm/v20181115/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/live/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/live/v20180801/
+-rw-rw-rw-   0 root         (0) root         (0)   122135 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/live/v20180801/live_client.py
+-rw-rw-rw-   0 root         (0) root         (0)   217738 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/live/v20180801/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/live/v20180801/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/live/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iai/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iai/v20180301/
+-rw-rw-rw-   0 root         (0) root         (0)    32286 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iai/v20180301/iai_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    66647 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iai/v20180301/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iai/v20180301/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iai/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iotexplorer/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iotexplorer/v20190423/
+-rw-rw-rw-   0 root         (0) root         (0)    27515 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iotexplorer/v20190423/iotexplorer_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    43033 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iotexplorer/v20190423/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iotexplorer/v20190423/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iotexplorer/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tiems/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tiems/v20190416/
+-rw-rw-rw-   0 root         (0) root         (0)    24632 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tiems/v20190416/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    10230 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tiems/v20190416/tiems_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tiems/v20190416/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tiems/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/partners/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/partners/v20180321/
+-rw-rw-rw-   0 root         (0) root         (0)    40079 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/partners/v20180321/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    18158 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/partners/v20180321/partners_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/partners/v20180321/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/partners/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/habo/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/habo/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/habo/v20181203/
+-rw-rw-rw-   0 root         (0) root         (0)     3714 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/habo/v20181203/models.py
+-rw-rw-rw-   0 root         (0) root         (0)     3356 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/habo/v20181203/habo_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/habo/v20181203/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sqlserver/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sqlserver/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sqlserver/v20180328/
+-rw-rw-rw-   0 root         (0) root         (0)    94601 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sqlserver/v20180328/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sqlserver/v20180328/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    49632 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sqlserver/v20180328/sqlserver_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/youmall/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/youmall/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/youmall/v20180228/
+-rw-rw-rw-   0 root         (0) root         (0)    95293 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/youmall/v20180228/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/youmall/v20180228/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    40451 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/youmall/v20180228/youmall_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tav/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tav/v20190118/
+-rw-rw-rw-   0 root         (0) root         (0)     7391 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tav/v20190118/models.py
+-rw-rw-rw-   0 root         (0) root         (0)     5530 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tav/v20190118/tav_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tav/v20190118/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tav/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmlb/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmlb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmlb/v20180625/
+-rw-rw-rw-   0 root         (0) root         (0)   174774 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmlb/v20180625/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmlb/v20180625/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    61421 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmlb/v20180625/bmlb_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/hcm/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/hcm/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/hcm/v20181106/
+-rw-rw-rw-   0 root         (0) root         (0)     5686 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/hcm/v20181106/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/hcm/v20181106/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2215 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/hcm/v20181106/hcm_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tci/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tci/v20190318/
+-rw-rw-rw-   0 root         (0) root         (0)   152989 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tci/v20190318/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    56015 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tci/v20190318/tci_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tci/v20190318/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tci/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbaas/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbaas/v20180416/
+-rw-rw-rw-   0 root         (0) root         (0)    40276 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbaas/v20180416/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbaas/v20180416/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    17269 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbaas/v20180416/tbaas_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbaas/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tics/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tics/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tics/v20181115/
+-rw-rw-rw-   0 root         (0) root         (0)     6051 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tics/v20181115/tics_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    15988 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tics/v20181115/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tics/v20181115/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bri/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bri/v20190328/
+-rw-rw-rw-   0 root         (0) root         (0)     6081 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bri/v20190328/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bri/v20190328/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2565 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bri/v20190328/bri_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bri/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ticm/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ticm/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ticm/v20181127/
+-rw-rw-rw-   0 root         (0) root         (0)    13649 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ticm/v20181127/models.py
+-rw-rw-rw-   0 root         (0) root         (0)     2307 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ticm/v20181127/ticm_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ticm/v20181127/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/billing/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/billing/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/billing/v20180709/
+-rw-rw-rw-   0 root         (0) root         (0)    52267 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/billing/v20180709/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    14333 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/billing/v20180709/billing_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/billing/v20180709/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cloudaudit/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cloudaudit/v20190319/
+-rw-rw-rw-   0 root         (0) root         (0)    15282 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cloudaudit/v20190319/cloudaudit_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    27628 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cloudaudit/v20190319/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cloudaudit/v20190319/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cloudaudit/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cws/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cws/v20180312/
+-rw-rw-rw-   0 root         (0) root         (0)    46637 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cws/v20180312/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cws/v20180312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    24051 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cws/v20180312/cws_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cws/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ic/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ic/v20190307/
+-rw-rw-rw-   0 root         (0) root         (0)    15283 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ic/v20190307/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ic/v20190307/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     6605 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ic/v20190307/ic_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ic/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbp/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbp/v20190311/
+-rw-rw-rw-   0 root         (0) root         (0)    11765 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbp/v20190311/models.py
+-rw-rw-rw-   0 root         (0) root         (0)     4464 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbp/v20190311/tbp_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbp/v20190311/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbp/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbp/v20190627/
+-rw-rw-rw-   0 root         (0) root         (0)    11354 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbp/v20190627/models.py
+-rw-rw-rw-   0 root         (0) root         (0)     3247 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbp/v20190627/tbp_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbp/v20190627/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tiia/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tiia/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tiia/v20190529/
+-rw-rw-rw-   0 root         (0) root         (0)    34751 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tiia/v20190529/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    10233 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tiia/v20190529/tiia_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tiia/v20190529/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/msp/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/msp/v20180319/
+-rw-rw-rw-   0 root         (0) root         (0)     9388 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/msp/v20180319/msp_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    16478 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/msp/v20180319/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/msp/v20180319/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/msp/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ms/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ms/v20180408/
+-rw-rw-rw-   0 root         (0) root         (0)    57336 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ms/v20180408/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    19959 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ms/v20180408/ms_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ms/v20180408/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ms/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cis/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cis/v20180408/
+-rw-rw-rw-   0 root         (0) root         (0)    20158 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cis/v20180408/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cis/v20180408/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     9728 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cis/v20180408/cis_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cis/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bm/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bm/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bm/v20180423/
+-rw-rw-rw-   0 root         (0) root         (0)   129729 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bm/v20180423/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    62154 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bm/v20180423/bm_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bm/v20180423/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbm/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbm/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbm/v20180129/
+-rw-rw-rw-   0 root         (0) root         (0)    27606 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbm/v20180129/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbm/v20180129/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    13039 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tbm/v20180129/tbm_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cds/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cds/v20180420/
+-rw-rw-rw-   0 root         (0) root         (0)     7361 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cds/v20180420/cds_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    11833 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cds/v20180420/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cds/v20180420/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cds/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cr/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cr/v20180321/
+-rw-rw-rw-   0 root         (0) root         (0)    24599 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cr/v20180321/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    13876 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cr/v20180321/cr_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cr/v20180321/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cr/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cdn/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cdn/v20180606/
+-rw-rw-rw-   0 root         (0) root         (0)    46334 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cdn/v20180606/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cdn/v20180606/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    21336 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cdn/v20180606/cdn_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cdn/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/gaap/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/gaap/v20180529/
+-rw-rw-rw-   0 root         (0) root         (0)   187297 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/gaap/v20180529/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/gaap/v20180529/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    97555 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/gaap/v20180529/gaap_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/gaap/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/trtc/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/trtc/v20190722/
+-rw-rw-rw-   0 root         (0) root         (0)     2635 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/trtc/v20190722/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/trtc/v20190722/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     3504 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/trtc/v20190722/trtc_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/trtc/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tts/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tts/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tts/v20190823/
+-rw-rw-rw-   0 root         (0) root         (0)     4159 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tts/v20190823/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tts/v20190823/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2497 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tts/v20190823/tts_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/scf/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/scf/v20180416/
+-rw-rw-rw-   0 root         (0) root         (0)    61599 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/scf/v20180416/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/scf/v20180416/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    22525 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/scf/v20180416/scf_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/scf/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/postgres/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/postgres/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)    32968 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/postgres/v20170312/postgres_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    61242 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/postgres/v20170312/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/postgres/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/postgres/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cdb/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cdb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cdb/v20170320/
+-rw-rw-rw-   0 root         (0) root         (0)   215359 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cdb/v20170320/models.py
+-rw-rw-rw-   0 root         (0) root         (0)   104231 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cdb/v20170320/cdb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cdb/v20170320/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ocr/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ocr/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ocr/v20181119/
+-rw-rw-rw-   0 root         (0) root         (0)   137607 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ocr/v20181119/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ocr/v20181119/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    60811 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ocr/v20181119/ocr_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/asr/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/asr/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/asr/v20190614/
+-rw-rw-rw-   0 root         (0) root         (0)     5999 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/asr/v20190614/asr_client.py
+-rw-rw-rw-   0 root         (0) root         (0)     9751 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/asr/v20190614/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/asr/v20190614/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mariadb/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mariadb/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)   105039 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mariadb/v20170312/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mariadb/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    49657 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mariadb/v20170312/mariadb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mariadb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sts/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sts/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sts/v20180813/
+-rw-rw-rw-   0 root         (0) root         (0)     8051 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sts/v20180813/models.py
+-rw-rw-rw-   0 root         (0) root         (0)     4504 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sts/v20180813/sts_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sts/v20180813/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dts/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dts/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dts/v20180330/
+-rw-rw-rw-   0 root         (0) root         (0)    49379 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dts/v20180330/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    24662 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dts/v20180330/dts_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dts/v20180330/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/aai/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/aai/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/aai/v20180522/
+-rw-rw-rw-   0 root         (0) root         (0)     6632 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/aai/v20180522/aai_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    11875 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/aai/v20180522/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/aai/v20180522/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ecc/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ecc/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ecc/v20181213/
+-rw-rw-rw-   0 root         (0) root         (0)    17322 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ecc/v20181213/models.py
+-rw-rw-rw-   0 root         (0) root         (0)     4399 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ecc/v20181213/ecc_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/ecc/v20181213/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmeip/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmeip/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmeip/v20180625/
+-rw-rw-rw-   0 root         (0) root         (0)    34618 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmeip/v20180625/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmeip/v20180625/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    22632 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/bmeip/v20180625/bmeip_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mps/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mps/v20190612/
+-rw-rw-rw-   0 root         (0) root         (0)   177216 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mps/v20190612/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    45651 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mps/v20190612/mps_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mps/v20190612/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mps/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      629 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/soe/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/soe/v20180724/
+-rw-rw-rw-   0 root         (0) root         (0)    34571 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/soe/v20180724/models.py
+-rw-rw-rw-   0 root         (0) root         (0)     6826 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/soe/v20180724/soe_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/soe/v20180724/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/soe/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cvm/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cvm/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)   100489 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cvm/v20170312/cvm_client.py
+-rw-rw-rw-   0 root         (0) root         (0)   213843 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cvm/v20170312/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cvm/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cvm/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/yunsou/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/yunsou/v20180504/
+-rw-rw-rw-   0 root         (0) root         (0)     3289 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/yunsou/v20180504/yunsou_client.py
+-rw-rw-rw-   0 root         (0) root         (0)     6794 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/yunsou/v20180504/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/yunsou/v20180504/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/yunsou/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/batch/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/batch/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)    36548 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/batch/v20170312/batch_client.py
+-rw-rw-rw-   0 root         (0) root         (0)   134458 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/batch/v20170312/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/batch/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/batch/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dcdb/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dcdb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dcdb/v20180411/
+-rw-rw-rw-   0 root         (0) root         (0)    93875 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dcdb/v20180411/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dcdb/v20180411/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    43090 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dcdb/v20180411/dcdb_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/redis/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/redis/v20180412/
+-rw-rw-rw-   0 root         (0) root         (0)    85220 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/redis/v20180412/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/redis/v20180412/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    38102 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/redis/v20180412/redis_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/redis/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/vpc/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/vpc/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)   370533 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/vpc/v20170312/models.py
+-rw-rw-rw-   0 root         (0) root         (0)   231892 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/vpc/v20170312/vpc_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/vpc/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/vpc/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cbs/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cbs/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)    91580 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cbs/v20170312/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    48059 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cbs/v20170312/cbs_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cbs/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cbs/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tia/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tia/v20180226/
+-rw-rw-rw-   0 root         (0) root         (0)    27208 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tia/v20180226/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    13551 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tia/v20180226/tia_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tia/v20180226/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tia/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/autoscaling/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/autoscaling/v20180419/
+-rw-rw-rw-   0 root         (0) root         (0)   153145 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/autoscaling/v20180419/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/autoscaling/v20180419/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    59326 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/autoscaling/v20180419/autoscaling_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/autoscaling/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/facefusion/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/facefusion/v20181201/
+-rw-rw-rw-   0 root         (0) root         (0)     4145 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/facefusion/v20181201/facefusion_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    10135 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/facefusion/v20181201/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/facefusion/v20181201/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/facefusion/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/yunjing/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/yunjing/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/yunjing/v20180228/
+-rw-rw-rw-   0 root         (0) root         (0)   126882 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/yunjing/v20180228/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    74383 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/yunjing/v20180228/yunjing_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/yunjing/v20180228/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/vod/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/vod/v20180717/
+-rw-rw-rw-   0 root         (0) root         (0)   112473 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/vod/v20180717/vod_client.py
+-rw-rw-rw-   0 root         (0) root         (0)   574326 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/vod/v20180717/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/vod/v20180717/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/vod/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mongodb/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mongodb/v20180408/
+-rw-rw-rw-   0 root         (0) root         (0)    40960 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mongodb/v20180408/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    17355 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mongodb/v20180408/mongodb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mongodb/v20180408/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mongodb/v20190725/
+-rw-rw-rw-   0 root         (0) root         (0)    43341 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mongodb/v20190725/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    16620 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mongodb/v20190725/mongodb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mongodb/v20190725/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/mongodb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sms/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sms/v20190711/
+-rw-rw-rw-   0 root         (0) root         (0)     6995 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sms/v20190711/sms_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    15498 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sms/v20190711/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sms/v20190711/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/sms/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cim/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cim/v20190318/
+-rw-rw-rw-   0 root         (0) root         (0)     1423 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cim/v20190318/models.py
+-rw-rw-rw-   0 root         (0) root         (0)     2162 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cim/v20190318/cim_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cim/v20190318/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cim/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/wss/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/wss/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/wss/v20180426/
+-rw-rw-rw-   0 root         (0) root         (0)    13764 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/wss/v20180426/models.py
+-rw-rw-rw-   0 root         (0) root         (0)     4452 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/wss/v20180426/wss_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/wss/v20180426/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/exception/
+-rw-rw-rw-   0 root         (0) root         (0)      760 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/exception/tencent_cloud_sdk_exception.py
+-rw-rw-rw-   0 root         (0) root         (0)       25 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/exception/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1557 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/sign.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    11870 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/abstract_client.py
+-rw-rw-rw-   0 root         (0) root         (0)     1984 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/abstract_model.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/profile/
+-rw-rw-rw-   0 root         (0) root         (0)     1405 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/profile/http_profile.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/profile/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1636 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/profile/client_profile.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/http/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/http/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     4973 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/http/request.py
+-rw-rw-rw-   0 root         (0) root         (0)     2036 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/common/credential.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dc/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dc/v20180410/
+-rw-rw-rw-   0 root         (0) root         (0)    14541 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dc/v20180410/dc_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    37127 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dc/v20180410/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dc/v20180410/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/dc/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/gme/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/gme/v20180711/
+-rw-rw-rw-   0 root         (0) root         (0)    31526 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/gme/v20180711/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    16300 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/gme/v20180711/gme_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/gme/v20180711/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/gme/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/nlp/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/nlp/v20190408/
+-rw-rw-rw-   0 root         (0) root         (0)    25716 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/nlp/v20190408/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    25668 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/nlp/v20190408/nlp_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/nlp/v20190408/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/nlp/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iotcloud/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iotcloud/v20180614/
+-rw-rw-rw-   0 root         (0) root         (0)    41909 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iotcloud/v20180614/iotcloud_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    72050 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iotcloud/v20180614/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iotcloud/v20180614/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iotcloud/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iot/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iot/v20180123/
+-rw-rw-rw-   0 root         (0) root         (0)    53839 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iot/v20180123/iot_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    86687 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iot/v20180123/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iot/v20180123/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iot/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tkgdq/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tkgdq/v20190411/
+-rw-rw-rw-   0 root         (0) root         (0)     5037 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tkgdq/v20190411/tkgdq_client.py
+-rw-rw-rw-   0 root         (0) root         (0)     7149 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tkgdq/v20190411/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tkgdq/v20190411/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tkgdq/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tmt/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tmt/v20180321/
+-rw-rw-rw-   0 root         (0) root         (0)    12938 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tmt/v20180321/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tmt/v20180321/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     6972 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tmt/v20180321/tmt_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tmt/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cms/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cms/v20190321/
+-rw-rw-rw-   0 root         (0) root         (0)    35530 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cms/v20190321/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    17364 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cms/v20190321/cms_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cms/v20190321/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cms/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tcb/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tcb/v20180608/
+-rw-rw-rw-   0 root         (0) root         (0)    10353 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tcb/v20180608/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tcb/v20180608/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     5656 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tcb/v20180608/tcb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tcb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tke/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tke/v20180525/
+-rw-rw-rw-   0 root         (0) root         (0)    22361 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tke/v20180525/tke_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    63950 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tke/v20180525/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tke/v20180525/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tke/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/emr/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/emr/v20190103/
+-rw-rw-rw-   0 root         (0) root         (0)    47110 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/emr/v20190103/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/emr/v20190103/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    11599 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/emr/v20190103/emr_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/emr/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tag/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tag/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tag/v20180813/
+-rw-rw-rw-   0 root         (0) root         (0)    22955 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tag/v20180813/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tag/v20180813/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    14044 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tag/v20180813/tag_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/es/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/es/v20180416/
+-rw-rw-rw-   0 root         (0) root         (0)    12324 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/es/v20180416/es_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    41323 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/es/v20180416/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/es/v20180416/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/es/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cfs/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cfs/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cfs/v20190719/
+-rw-rw-rw-   0 root         (0) root         (0)    40017 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cfs/v20190719/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cfs/v20190719/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    23986 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/cfs/v20190719/cfs_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tsf/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tsf/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tsf/v20180326/
+-rw-rw-rw-   0 root         (0) root         (0)    80120 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tsf/v20180326/tsf_client.py
+-rw-rw-rw-   0 root         (0) root         (0)   185441 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tsf/v20180326/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/tsf/v20180326/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/monitor/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/monitor/v20180724/
+-rw-rw-rw-   0 root         (0) root         (0)     3652 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/monitor/v20180724/monitor_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    10105 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/monitor/v20180724/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/monitor/v20180724/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/monitor/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iottid/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iottid/v20190411/
+-rw-rw-rw-   0 root         (0) root         (0)    12672 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iottid/v20190411/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iottid/v20190411/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    11743 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iottid/v20190411/iottid_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:59:30.000000 tencentcloud-sdk-python-3.0.99/tencentcloud/iottid/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1240 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/setup.py
+-rw-rw-rw-   0 root         (0) root         (0)     1762 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)       65 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/MANIFEST.in
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud_sdk_python.egg-info/
+-rw-rw-rw-   0 root         (0) root         (0)     1762 2019-10-28 08:59:42.000000 tencentcloud-sdk-python-3.0.99/tencentcloud_sdk_python.egg-info/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)    16114 2019-10-28 08:59:43.000000 tencentcloud-sdk-python-3.0.99/tencentcloud_sdk_python.egg-info/SOURCES.txt
+-rw-rw-rw-   0 root         (0) root         (0)       23 2019-10-28 08:59:42.000000 tencentcloud-sdk-python-3.0.99/tencentcloud_sdk_python.egg-info/top_level.txt
+-rw-rw-rw-   0 root         (0) root         (0)        1 2019-10-28 08:59:42.000000 tencentcloud-sdk-python-3.0.99/tencentcloud_sdk_python.egg-info/dependency_links.txt
+-rw-rw-rw-   0 root         (0) root         (0)      661 2019-10-28 08:59:28.000000 tencentcloud-sdk-python-3.0.99/README.rst
```

### Comparing `tencentcloud-sdk-python-3.0.98/LICENSE` & `tencentcloud-sdk-python-3.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/lb.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/lb.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/monitor.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/monitor.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/partners.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/partners.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/scaling.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/scaling.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/sec.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/sec.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/trade.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/trade.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/cloudaudit.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/cloudaudit.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/account.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/account.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/feecenter.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/feecenter.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/scf.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/scf.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/eip.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/eip.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/emr.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/emr.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/cmem.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/cmem.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/athena.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/athena.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/bgpip.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/bgpip.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/market.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/market.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/apigateway.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/apigateway.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/bmvpc.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/bmvpc.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/snapshot.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/snapshot.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/base.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/base.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/tmt.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/tmt.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/redis.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/redis.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/cdn.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/cdn.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/tdsql.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/tdsql.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/sts.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/sts.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/wenzhi.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/wenzhi.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/vod.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/vod.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/yunsou.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/yunsou.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/bmlb.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/bmlb.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/cdb.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/cdb.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/ccr.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/ccr.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/vpc.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/vpc.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/image.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/image.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/live.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/live.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/ccs.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/ccs.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/batch.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/batch.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/cvm.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/cvm.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/dc.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/dc.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/tbaas.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/tbaas.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/bill.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/bill.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/dfw.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/dfw.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/cns.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/cns.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/cbs.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/cbs.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/bmeip.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/bmeip.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/modules/bm.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/modules/bm.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/qcloudapi.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/qcloudapi.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/common/api_exception.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/common/api_exception.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/common/sign.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/common/sign.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/QcloudApi/common/request.py` & `tencentcloud-sdk-python-3.0.99/QcloudApi/common/request.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/captcha/v20190722/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/captcha/v20190722/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/captcha/v20190722/captcha_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/captcha/v20190722/captcha_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/kms/v20190118/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/kms/v20190118/models.py`

 * *Files 1% similar despite different names*

```diff
@@ -598,14 +598,52 @@
     def _deserialize(self, params):
         self.KeyId = params.get("KeyId")
         self.Plaintext = params.get("Plaintext")
         self.CiphertextBlob = params.get("CiphertextBlob")
         self.RequestId = params.get("RequestId")
 
 
+class GenerateRandomRequest(AbstractModel):
+    """GenerateRandom请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param NumberOfBytes: 生成的随机数的长度。最小值为1， 最大值为1024。
+        :type NumberOfBytes: int
+        """
+        self.NumberOfBytes = None
+
+
+    def _deserialize(self, params):
+        self.NumberOfBytes = params.get("NumberOfBytes")
+
+
+class GenerateRandomResponse(AbstractModel):
+    """GenerateRandom返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param Plaintext: 生成的随机数的明文，该明文使用base64编码，用户需要使用base64解码得到明文。
+        :type Plaintext: str
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.Plaintext = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.Plaintext = params.get("Plaintext")
+        self.RequestId = params.get("RequestId")
+
+
 class GetKeyRotationStatusRequest(AbstractModel):
     """GetKeyRotationStatus请求参数结构体
 
     """
 
     def __init__(self):
         """
@@ -739,15 +777,15 @@
         """
         :param EncryptedKeyMaterial: 使用GetParametersForImport 返回的PublicKey加密后的密钥材料base64编码。对于国密版本region的KMS，导入的密钥材料长度要求为 128 bit，FIPS版本region的KMS， 导入的密钥材料长度要求为 256 bit。
         :type EncryptedKeyMaterial: str
         :param ImportToken: 通过调用GetParametersForImport获得的导入令牌。
         :type ImportToken: str
         :param KeyId: 指定导入密钥材料的CMK，需要和GetParametersForImport 指定的CMK相同。
         :type KeyId: str
-        :param ValidTo: 密钥材料过期时间 unix 时间戳，不指定或者 0 表示密钥材料不会过期，若指定过期时间，需要大于当前时间点。
+        :param ValidTo: 密钥材料过期时间 unix 时间戳，不指定或者 0 表示密钥材料不会过期，若指定过期时间，需要大于当前时间点，最大支持 2147443200。
         :type ValidTo: int
         """
         self.EncryptedKeyMaterial = None
         self.ImportToken = None
         self.KeyId = None
         self.ValidTo = None
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/kms/v20190118/kms_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/kms/v20190118/kms_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -413,14 +413,42 @@
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
+    def GenerateRandom(self, request):
+        """随机数生成接口。
+
+        :param request: 调用GenerateRandom所需参数的结构体。
+        :type request: :class:`tencentcloud.kms.v20190118.models.GenerateRandomRequest`
+        :rtype: :class:`tencentcloud.kms.v20190118.models.GenerateRandomResponse`
+
+        """
+        try:
+            params = request._serialize()
+            body = self.call("GenerateRandom", params)
+            response = json.loads(body)
+            if "Error" not in response["Response"]:
+                model = models.GenerateRandomResponse()
+                model._deserialize(response["Response"])
+                return model
+            else:
+                code = response["Response"]["Error"]["Code"]
+                message = response["Response"]["Error"]["Message"]
+                reqid = response["Response"]["RequestId"]
+                raise TencentCloudSDKException(code, message, reqid)
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
     def GetKeyRotationStatus(self, request):
         """查询指定的CMK是否开启了密钥轮换功能。
 
         :param request: 调用GetKeyRotationStatus所需参数的结构体。
         :type request: :class:`tencentcloud.kms.v20190118.models.GetKeyRotationStatusRequest`
         :rtype: :class:`tencentcloud.kms.v20190118.models.GetKeyRotationStatusResponse`
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/faceid/v20180301/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/faceid/v20180301/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/faceid/v20180301/faceid_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/faceid/v20180301/faceid_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/chdfs/v20190718/chdfs_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/chdfs/v20190718/chdfs_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/chdfs/v20190718/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/chdfs/v20190718/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/clb/v20180317/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/clb/v20180317/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/clb/v20180317/clb_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/clb/v20180317/clb_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/bizlive/v20190313/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/bizlive/v20190313/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/bizlive/v20190313/bizlive_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/bizlive/v20190313/bizlive_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/bmvpc/v20180625/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/bmvpc/v20180625/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/bmvpc/v20180625/bmvpc_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/bmvpc/v20180625/bmvpc_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/ds/v20180523/ds_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/ds/v20180523/ds_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/ds/v20180523/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/ds/v20180523/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cam/v20190116/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cam/v20190116/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cam/v20190116/cam_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cam/v20190116/cam_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/drm/v20181115/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/drm/v20181115/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/drm/v20181115/drm_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/drm/v20181115/drm_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/live/v20180801/live_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/live/v20180801/live_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -609,15 +609,15 @@
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
     def DeleteLiveRecord(self, request):
-        """用于删除录制任务。
+        """注：DeleteLiveRecord 接口仅用于删除录制任务记录，不具备停止录制的功能，也不能删除正在进行中的录制。如果需要停止录制任务，请使用终止录制[StopLiveRecord](/document/product/267/30146) 接口。
 
         :param request: 调用DeleteLiveRecord所需参数的结构体。
         :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordRequest`
         :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordResponse`
 
         """
         try:
@@ -1677,16 +1677,15 @@
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
     def DescribeLiveTranscodeDetailInfo(self, request):
-        """支持查询某天的转码详细信息。
-        注意：当前只支持查询近30天内某天的详细数据。
+        """支持查询某天或某段时间的转码详细信息。
 
         :param request: 调用DescribeLiveTranscodeDetailInfo所需参数的结构体。
         :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeDetailInfoRequest`
         :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeDetailInfoResponse`
 
         """
         try:
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/live/v20180801/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/live/v20180801/models.py`

 * *Files 0% similar despite different names*

```diff
@@ -3325,42 +3325,54 @@
 class DescribeLiveTranscodeDetailInfoRequest(AbstractModel):
     """DescribeLiveTranscodeDetailInfo请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param DayTime: 起始时间，北京时间，
-格式：yyyymmdd。
-注意：当前只支持查询近30天内某天的详细数据。
-        :type DayTime: str
         :param PushDomain: 推流域名。
         :type PushDomain: str
         :param StreamName: 流名称。
         :type StreamName: str
+        :param DayTime: 查询时间，北京时间，
+格式：yyyymmdd。
+注意：支持查询近3个月内某天的详细数据。
+        :type DayTime: str
         :param PageNum: 页数，默认1，
 不超过100页。
         :type PageNum: int
         :param PageSize: 每页个数，默认20，
 范围：[10,1000]。
         :type PageSize: int
+        :param StartDayTime: 起始天时间，北京时间，
+格式：yyyymmdd。
+注意：支持查询近3个月内的详细数据。
+        :type StartDayTime: str
+        :param EndDayTime: 结束天时间，北京时间，
+格式：yyyymmdd。
+注意：支持查询近3个月内的详细数据，注意DayTime 与（StartDayTime，EndDayTime）必须要传一个，如果都传，会以DayTime为准 。
+        :type EndDayTime: str
         """
-        self.DayTime = None
         self.PushDomain = None
         self.StreamName = None
+        self.DayTime = None
         self.PageNum = None
         self.PageSize = None
+        self.StartDayTime = None
+        self.EndDayTime = None
 
 
     def _deserialize(self, params):
-        self.DayTime = params.get("DayTime")
         self.PushDomain = params.get("PushDomain")
         self.StreamName = params.get("StreamName")
+        self.DayTime = params.get("DayTime")
         self.PageNum = params.get("PageNum")
         self.PageSize = params.get("PageSize")
+        self.StartDayTime = params.get("StartDayTime")
+        self.EndDayTime = params.get("EndDayTime")
 
 
 class DescribeLiveTranscodeDetailInfoResponse(AbstractModel):
     """DescribeLiveTranscodeDetailInfo返回参数结构体
 
     """
 
@@ -4725,21 +4737,21 @@
 
     """
 
     def __init__(self):
         """
         :param AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
         :type AppName: str
-        :param DomainName: 您的加速域名。
+        :param DomainName: 您的推流域名。
         :type DomainName: str
         :param StreamName: 流名称。
         :type StreamName: str
         :param ResumeTime: 恢复流的时间。UTC 格式，例如：2018-11-29T19:00:00Z。
 注意：
-1. 默认禁播90天，且最长支持禁播90天。
+1. 默认禁播7天，且最长支持禁播90天。
 2. 北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
         :type ResumeTime: str
         :param Reason: 禁推原因。
 注明：请务必填写禁推原因，防止误操作。
 长度限制：2048字节。
         :type Reason: str
         """
@@ -5669,15 +5681,15 @@
         self.Enable = params.get("Enable")
         self.AuthKey = params.get("AuthKey")
         self.AuthDelta = params.get("AuthDelta")
         self.AuthBackKey = params.get("AuthBackKey")
 
 
 class PlayCodeTotalInfo(AbstractModel):
-    """各状态码的总次数，暂时支持400,403,404,500,502,503,504
+    """各状态码的总次数，支持大多数的http协议返回码
 
     """
 
     def __init__(self):
         """
         :param Code: HTTP code，可选值包括400,403,404,500,502,503,504
         :type Code: str
@@ -5772,40 +5784,48 @@
 
     def __init__(self):
         """
         :param ProvinceName: 省份。
         :type ProvinceName: str
         :param IspName: 运营商。
         :type IspName: str
+        :param Code2xx: 错误码为2开头的次数。
+        :type Code2xx: int
+        :param Code3xx: 错误码为3开头的次数。
+        :type Code3xx: int
         :param Code4xx: 错误码为4开头的次数。
         :type Code4xx: int
         :param Code5xx: 错误码为5开头的次数。
         :type Code5xx: int
         """
         self.ProvinceName = None
         self.IspName = None
+        self.Code2xx = None
+        self.Code3xx = None
         self.Code4xx = None
         self.Code5xx = None
 
 
     def _deserialize(self, params):
         self.ProvinceName = params.get("ProvinceName")
         self.IspName = params.get("IspName")
+        self.Code2xx = params.get("Code2xx")
+        self.Code3xx = params.get("Code3xx")
         self.Code4xx = params.get("Code4xx")
         self.Code5xx = params.get("Code5xx")
 
 
 class ProIspPlaySumInfo(AbstractModel):
     """获取省份/运营商的播放信息
 
     """
 
     def __init__(self):
         """
-        :param Name: 省份/运营商。
+        :param Name: 省份/运营商/国家或地区。
         :type Name: str
         :param TotalFlux: 总流量，单位：MB。
         :type TotalFlux: float
         :param TotalRequest: 总请求数。
         :type TotalRequest: int
         :param AvgFluxPerSecond: 平均下载流量，单位：MB/s
         :type AvgFluxPerSecond: float
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/iai/v20180301/iai_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/iai/v20180301/iai_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/iai/v20180301/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/iai/v20180301/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/iotexplorer/v20190423/iotexplorer_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/iotexplorer/v20190423/iotexplorer_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/iotexplorer/v20190423/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/iotexplorer/v20190423/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tiems/v20190416/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tiems/v20190416/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tiems/v20190416/tiems_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tiems/v20190416/tiems_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/partners/v20180321/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/partners/v20180321/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/partners/v20180321/partners_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/partners/v20180321/partners_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/habo/v20181203/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/habo/v20181203/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/habo/v20181203/habo_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/habo/v20181203/habo_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/sqlserver/v20180328/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/sqlserver/v20180328/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/sqlserver/v20180328/sqlserver_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/sqlserver/v20180328/sqlserver_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/youmall/v20180228/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/youmall/v20180228/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/youmall/v20180228/youmall_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/youmall/v20180228/youmall_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tav/v20190118/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tav/v20190118/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tav/v20190118/tav_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tav/v20190118/tav_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/bmlb/v20180625/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/bmlb/v20180625/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/bmlb/v20180625/bmlb_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/bmlb/v20180625/bmlb_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/hcm/v20181106/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/hcm/v20181106/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/hcm/v20181106/hcm_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/hcm/v20181106/hcm_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tci/v20190318/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tci/v20190318/models.py`

 * *Files 1% similar despite different names*

```diff
@@ -140,14 +140,35 @@
         self.MuteDuration = params.get("MuteDuration")
         self.SoundDuration = params.get("SoundDuration")
         self.TotalDuration = params.get("TotalDuration")
         self.VadNum = params.get("VadNum")
         self.WordNum = params.get("WordNum")
 
 
+class AbsenceInfo(AbstractModel):
+    """缺勤人员信息
+
+    """
+
+    def __init__(self):
+        """
+        :param LibraryIds: 识别到的人员所在的库id
+        :type LibraryIds: str
+        :param PersonId: 识别到的人员id
+        :type PersonId: str
+        """
+        self.LibraryIds = None
+        self.PersonId = None
+
+
+    def _deserialize(self, params):
+        self.LibraryIds = params.get("LibraryIds")
+        self.PersonId = params.get("PersonId")
+
+
 class ActionCountStatistic(AbstractModel):
     """数量统计结果
 
     """
 
     def __init__(self):
         """
@@ -317,14 +338,44 @@
 
 
     def _deserialize(self, params):
         self.Confidence = params.get("Confidence")
         self.Type = params.get("Type")
 
 
+class AllMuteSlice(AbstractModel):
+    """如果请求中开启了静音检测开关，则会返回所有的静音片段（静音时长超过阈值的片段）。
+
+    """
+
+    def __init__(self):
+        """
+        :param MuteSlice: 所有静音片段。
+        :type MuteSlice: list of MuteSlice
+        :param MuteRatio: 静音时长占比。
+        :type MuteRatio: float
+        :param TotalMuteDuration: 静音总时长。
+        :type TotalMuteDuration: int
+        """
+        self.MuteSlice = None
+        self.MuteRatio = None
+        self.TotalMuteDuration = None
+
+
+    def _deserialize(self, params):
+        if params.get("MuteSlice") is not None:
+            self.MuteSlice = []
+            for item in params.get("MuteSlice"):
+                obj = MuteSlice()
+                obj._deserialize(item)
+                self.MuteSlice.append(obj)
+        self.MuteRatio = params.get("MuteRatio")
+        self.TotalMuteDuration = params.get("TotalMuteDuration")
+
+
 class AttendanceInfo(AbstractModel):
     """识别到的人员信息
 
     """
 
     def __init__(self):
         """
@@ -1041,33 +1092,42 @@
 class DescribeAttendanceResultResponse(AbstractModel):
     """DescribeAttendanceResult返回参数结构体
 
     """
 
     def __init__(self):
         """
+        :param AbsenceSetInLibs: 缺失人员的ID列表(只针对请求中的libids字段)
+        :type AbsenceSetInLibs: list of AbsenceInfo
         :param AttendanceSet: 确定出勤人员列表
         :type AttendanceSet: list of AttendanceInfo
         :param SuspectedSet: 疑似出勤人员列表
         :type SuspectedSet: list of SuspectedInfo
-        :param AbsenceSet: 缺失人员的ID列表
+        :param AbsenceSet: 缺失人员的ID列表(只针对请求中的personids字段)
         :type AbsenceSet: list of str
         :param Progress: 请求处理进度
         :type Progress: int
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
+        self.AbsenceSetInLibs = None
         self.AttendanceSet = None
         self.SuspectedSet = None
         self.AbsenceSet = None
         self.Progress = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
+        if params.get("AbsenceSetInLibs") is not None:
+            self.AbsenceSetInLibs = []
+            for item in params.get("AbsenceSetInLibs"):
+                obj = AbsenceInfo()
+                obj._deserialize(item)
+                self.AbsenceSetInLibs.append(obj)
         if params.get("AttendanceSet") is not None:
             self.AttendanceSet = []
             for item in params.get("AttendanceSet"):
                 obj = AttendanceInfo()
                 obj._deserialize(item)
                 self.AttendanceSet.append(obj)
         if params.get("SuspectedSet") is not None:
@@ -1109,14 +1169,16 @@
 class DescribeAudioTaskResponse(AbstractModel):
     """DescribeAudioTask返回参数结构体
 
     """
 
     def __init__(self):
         """
+        :param AllMuteSlice: 如果请求中开启了静音检测开关，则会返回所有的静音片段（静音时长超过阈值的片段）。
+        :type AllMuteSlice: :class:`tencentcloud.tci.v20190318.models.AllMuteSlice`
         :param AsrStat: 返回的当前音频的统计信息。当进度为100时返回。
         :type AsrStat: :class:`tencentcloud.tci.v20190318.models.ASRStat`
         :param Texts: 返回当前音频流的详细信息，如果是流模式，返回的是对应流的详细信息，如果是 URL模式，返回的是查询的那一段seq对应的音频的详细信息。
         :type Texts: list of WholeTextItem
         :param VocabAnalysisDetailInfo: 返回词汇库中的单词出现的详细时间信息。
         :type VocabAnalysisDetailInfo: list of VocabDetailInfomation
         :param VocabAnalysisStatInfo: 返回词汇库中的单词出现的次数信息。
@@ -1128,26 +1190,30 @@
         :param Progress: 返回的当前处理进度。
         :type Progress: float
         :param TotalCount: 结果总数
         :type TotalCount: int
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
+        self.AllMuteSlice = None
         self.AsrStat = None
         self.Texts = None
         self.VocabAnalysisDetailInfo = None
         self.VocabAnalysisStatInfo = None
         self.AllTexts = None
         self.JobId = None
         self.Progress = None
         self.TotalCount = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
+        if params.get("AllMuteSlice") is not None:
+            self.AllMuteSlice = AllMuteSlice()
+            self.AllMuteSlice._deserialize(params.get("AllMuteSlice"))
         if params.get("AsrStat") is not None:
             self.AsrStat = ASRStat()
             self.AsrStat._deserialize(params.get("AsrStat"))
         if params.get("Texts") is not None:
             self.Texts = []
             for item in params.get("Texts"):
                 obj = WholeTextItem()
@@ -2075,28 +2141,32 @@
 
     def __init__(self):
         """
         :param EnableAllText: 输出全部文本标识，当该值设置为true时，会输出当前音频的全部文本
         :type EnableAllText: bool
         :param EnableKeyword: 输出关键词信息标识，当该值设置为true时，会输出当前音频的关键词信息。
         :type EnableKeyword: bool
+        :param EnableMuteDetect: 静音检测标识，当设置为 true 时，需要设置静音时间阈值字段mute_threshold，统计结果中会返回静音片段。
+        :type EnableMuteDetect: bool
         :param EnableVadInfo: 输出音频统计信息标识，当设置为 true 时，任务查询结果会输出音频的统计信息（AsrStat）
         :type EnableVadInfo: bool
         :param EnableVolume: 输出音频音量信息标识，当设置为 true 时，会输出当前音频音量信息。
         :type EnableVolume: bool
         """
         self.EnableAllText = None
         self.EnableKeyword = None
+        self.EnableMuteDetect = None
         self.EnableVadInfo = None
         self.EnableVolume = None
 
 
     def _deserialize(self, params):
         self.EnableAllText = params.get("EnableAllText")
         self.EnableKeyword = params.get("EnableKeyword")
+        self.EnableMuteDetect = params.get("EnableMuteDetect")
         self.EnableVadInfo = params.get("EnableVadInfo")
         self.EnableVolume = params.get("EnableVolume")
 
 
 class GestureResult(AbstractModel):
     """GestureResult
 
@@ -2735,14 +2805,35 @@
                 self.FaceInfoSet.append(obj)
         self.LibraryId = params.get("LibraryId")
         self.PersonId = params.get("PersonId")
         self.PersonName = params.get("PersonName")
         self.RequestId = params.get("RequestId")
 
 
+class MuteSlice(AbstractModel):
+    """所有静音片段。
+
+    """
+
+    def __init__(self):
+        """
+        :param MuteBtm: 起始时间。
+        :type MuteBtm: int
+        :param MuteEtm: 终止时间。
+        :type MuteEtm: int
+        """
+        self.MuteBtm = None
+        self.MuteEtm = None
+
+
+    def _deserialize(self, params):
+        self.MuteBtm = params.get("MuteBtm")
+        self.MuteEtm = params.get("MuteEtm")
+
+
 class Person(AbstractModel):
     """人员描述
 
     """
 
     def __init__(self):
         """
@@ -3034,35 +3125,39 @@
         :type VoiceEncodeType: int
         :param VoiceFileType: 语音文件类型 1:raw, 2:wav, 3:mp3，10:视频（三种音频格式目前仅支持16k采样率16bit）
         :type VoiceFileType: int
         :param Functions: 功能开关列表，表示是否需要打开相应的功能，返回相应的信息
         :type Functions: :class:`tencentcloud.tci.v20190318.models.Function`
         :param FileType: 视频文件类型，默认点播，直播填 live_url
         :type FileType: str
+        :param MuteThreshold: 静音阈值设置，如果静音检测开关开启，则静音时间超过这个阈值认为是静音片段，在结果中会返回, 没给的话默认值为3s
+        :type MuteThreshold: int
         :param VocabLibNameList: 识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析
         :type VocabLibNameList: list of str
         """
         self.Lang = None
         self.Url = None
         self.VoiceEncodeType = None
         self.VoiceFileType = None
         self.Functions = None
         self.FileType = None
+        self.MuteThreshold = None
         self.VocabLibNameList = None
 
 
     def _deserialize(self, params):
         self.Lang = params.get("Lang")
         self.Url = params.get("Url")
         self.VoiceEncodeType = params.get("VoiceEncodeType")
         self.VoiceFileType = params.get("VoiceFileType")
         if params.get("Functions") is not None:
             self.Functions = Function()
             self.Functions._deserialize(params.get("Functions"))
         self.FileType = params.get("FileType")
+        self.MuteThreshold = params.get("MuteThreshold")
         self.VocabLibNameList = params.get("VocabLibNameList")
 
 
 class SubmitAudioTaskResponse(AbstractModel):
     """SubmitAudioTask返回参数结构体
 
     """
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tci/v20190318/tci_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tci/v20190318/tci_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tbaas/v20180416/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tbaas/v20180416/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tbaas/v20180416/tbaas_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tbaas/v20180416/tbaas_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tics/v20181115/tics_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tics/v20181115/tics_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tics/v20181115/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tics/v20181115/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/bri/v20190328/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/bri/v20190328/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/bri/v20190328/bri_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/bri/v20190328/bri_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/ticm/v20181127/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/ticm/v20181127/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/ticm/v20181127/ticm_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/ticm/v20181127/ticm_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/billing/v20180709/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/billing/v20180709/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/billing/v20180709/billing_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/billing/v20180709/billing_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cloudaudit/v20190319/cloudaudit_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cloudaudit/v20190319/cloudaudit_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cloudaudit/v20190319/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cloudaudit/v20190319/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cws/v20180312/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cws/v20180312/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cws/v20180312/cws_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cws/v20180312/cws_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/ic/v20190307/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/ic/v20190307/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/ic/v20190307/ic_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/ic/v20190307/ic_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tbp/v20190311/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tbp/v20190311/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tbp/v20190311/tbp_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tbp/v20190311/tbp_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tbp/v20190627/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tbp/v20190627/models.py`

 * *Files 6% similar despite different names*

```diff
@@ -102,15 +102,15 @@
         :type BotEnv: str
         :param TerminalId: 终端标识，每个终端(或线程)对应一个，区分并发多用户。
         :type TerminalId: str
         :param InputText: 请求的文本。
         :type InputText: str
         :param SessionAttributes: 透传字段，透传给用户自定义的WebService服务。
         :type SessionAttributes: str
-        :param PlatformType: 平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount}。
+        :param PlatformType: 平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount；企业微信: WXWork}。
         :type PlatformType: str
         """
         self.BotId = None
         self.BotEnv = None
         self.TerminalId = None
         self.InputText = None
         self.SessionAttributes = None
@@ -150,15 +150,15 @@
         :type InputText: str
         :param ResponseMessage: 机器人应答。
 注意：此字段可能返回 null，表示取不到有效值。
         :type ResponseMessage: :class:`tencentcloud.tbp.v20190627.models.ResponseMessage`
         :param SessionAttributes: 透传字段，由用户自定义的WebService服务返回。
 注意：此字段可能返回 null，表示取不到有效值。
         :type SessionAttributes: str
-        :param ResultType: 结果类型 {0:未命中机器人; 1:任务型机器人; 2:问答型机器人; 3:闲聊型机器人}
+        :param ResultType: 结果类型 {中间逻辑出错:0; 任务型机器人:1; 问答型机器人:2; 闲聊型机器人:3; 未匹配上，返回预设兜底话术:5; 未匹配上，返回相似问题列表:6}。
 注意：此字段可能返回 null，表示取不到有效值。
         :type ResultType: str
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
         self.DialogStatus = None
         self.BotName = None
@@ -199,15 +199,15 @@
         """
         :param BotId: 机器人标识，用于定义抽象机器人。
         :type BotId: str
         :param BotEnv: 机器人版本，取值"dev"或"release"，{调试版本：dev；线上版本：release}。
         :type BotEnv: str
         :param TerminalId: 终端标识，每个终端(或线程)对应一个，区分并发多用户。
         :type TerminalId: str
-        :param PlatformType: 平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount}。
+        :param PlatformType: 平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount；企业微信: WXWork}。
         :type PlatformType: str
         """
         self.BotId = None
         self.BotEnv = None
         self.TerminalId = None
         self.PlatformType = None
 
@@ -243,15 +243,15 @@
         :type InputText: str
         :param ResponseMessage: 机器人应答。
 注意：此字段可能返回 null，表示取不到有效值。
         :type ResponseMessage: :class:`tencentcloud.tbp.v20190627.models.ResponseMessage`
         :param SessionAttributes: 透传字段，由用户自定义的WebService服务返回。
 注意：此字段可能返回 null，表示取不到有效值。
         :type SessionAttributes: str
-        :param ResultType: 结果类型 {未命中机器人:0; 任务型机器人:1; 问答型机器人:2; 闲聊型机器人:3}。
+        :param ResultType: 结果类型 {中间逻辑出错:0; 任务型机器人:1; 问答型机器人:2; 闲聊型机器人:3; 未匹配上，返回预设兜底话术:5; 未匹配上，返回相似问题列表:6}。
 注意：此字段可能返回 null，表示取不到有效值。
         :type ResultType: str
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
         self.DialogStatus = None
         self.BotName = None
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tbp/v20190627/tbp_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tbp/v20190627/tbp_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tiia/v20190529/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tiia/v20190529/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tiia/v20190529/tiia_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tiia/v20190529/tiia_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/msp/v20180319/msp_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/msp/v20180319/msp_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/msp/v20180319/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/msp/v20180319/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/ms/v20180408/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/ms/v20180408/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/ms/v20180408/ms_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/ms/v20180408/ms_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cis/v20180408/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cis/v20180408/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cis/v20180408/cis_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cis/v20180408/cis_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/bm/v20180423/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/bm/v20180423/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/bm/v20180423/bm_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/bm/v20180423/bm_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tbm/v20180129/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tbm/v20180129/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tbm/v20180129/tbm_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tbm/v20180129/tbm_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cds/v20180420/cds_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cds/v20180420/cds_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cds/v20180420/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cds/v20180420/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cr/v20180321/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cr/v20180321/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cr/v20180321/cr_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cr/v20180321/cr_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cdn/v20180606/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cdn/v20180606/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cdn/v20180606/cdn_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cdn/v20180606/cdn_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/gaap/v20180529/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/gaap/v20180529/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/gaap/v20180529/gaap_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/gaap/v20180529/gaap_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/trtc/v20190722/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/trtc/v20190722/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/trtc/v20190722/trtc_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/trtc/v20190722/trtc_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tts/v20190823/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tts/v20190823/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tts/v20190823/tts_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tts/v20190823/tts_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/scf/v20180416/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/scf/v20180416/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/scf/v20180416/scf_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/scf/v20180416/scf_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/postgres/v20170312/postgres_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/postgres/v20170312/postgres_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/postgres/v20170312/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/postgres/v20170312/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cdb/v20170320/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cdb/v20170320/models.py`

 * *Files 2% similar despite different names*

```diff
@@ -377,14 +377,55 @@
     def _deserialize(self, params):
         self.Database = params.get("Database")
         self.Table = params.get("Table")
         self.Column = params.get("Column")
         self.Privileges = params.get("Privileges")
 
 
+class CommonTimeWindow(AbstractModel):
+    """通用时间窗
+
+    """
+
+    def __init__(self):
+        """
+        :param Monday: 周一的时间窗，格式如： 02:00-06:00
+        :type Monday: str
+        :param Tuesday: 周二的时间窗，格式如： 02:00-06:00
+        :type Tuesday: str
+        :param Wednesday: 周三的时间窗，格式如： 02:00-06:00
+        :type Wednesday: str
+        :param Thursday: 周四的时间窗，格式如： 02:00-06:00
+        :type Thursday: str
+        :param Friday: 周五的时间窗，格式如： 02:00-06:00
+        :type Friday: str
+        :param Saturday: 周六的时间窗，格式如： 02:00-06:00
+        :type Saturday: str
+        :param Sunday: 周日的时间窗，格式如： 02:00-06:00
+        :type Sunday: str
+        """
+        self.Monday = None
+        self.Tuesday = None
+        self.Wednesday = None
+        self.Thursday = None
+        self.Friday = None
+        self.Saturday = None
+        self.Sunday = None
+
+
+    def _deserialize(self, params):
+        self.Monday = params.get("Monday")
+        self.Tuesday = params.get("Tuesday")
+        self.Wednesday = params.get("Wednesday")
+        self.Thursday = params.get("Thursday")
+        self.Friday = params.get("Friday")
+        self.Saturday = params.get("Saturday")
+        self.Sunday = params.get("Sunday")
+
+
 class CreateAccountsRequest(AbstractModel):
     """CreateAccounts请求参数结构体
 
     """
 
     def __init__(self):
         """
@@ -834,14 +875,56 @@
 
     def _deserialize(self, params):
         self.DealIds = params.get("DealIds")
         self.InstanceIds = params.get("InstanceIds")
         self.RequestId = params.get("RequestId")
 
 
+class CreateDeployGroupRequest(AbstractModel):
+    """CreateDeployGroup请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param DeployGroupName: 置放群组名称，最长不能超过60个字符。
+        :type DeployGroupName: str
+        :param Description: 置放群组描述，最长不能超过200个字符。
+        :type Description: str
+        """
+        self.DeployGroupName = None
+        self.Description = None
+
+
+    def _deserialize(self, params):
+        self.DeployGroupName = params.get("DeployGroupName")
+        self.Description = params.get("Description")
+
+
+class CreateDeployGroupResponse(AbstractModel):
+    """CreateDeployGroup返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param DeployGroupId: 置放群组ID
+        :type DeployGroupId: str
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.DeployGroupId = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.DeployGroupId = params.get("DeployGroupId")
+        self.RequestId = params.get("RequestId")
+
+
 class CreateParamTemplateRequest(AbstractModel):
     """CreateParamTemplate请求参数结构体
 
     """
 
     def __init__(self):
         """
@@ -1037,14 +1120,48 @@
         self.RequestId = None
 
 
     def _deserialize(self, params):
         self.RequestId = params.get("RequestId")
 
 
+class DeleteDeployGroupsRequest(AbstractModel):
+    """DeleteDeployGroups请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param DeployGroupIds: 要删除的置放群组 ID 列表。
+        :type DeployGroupIds: list of str
+        """
+        self.DeployGroupIds = None
+
+
+    def _deserialize(self, params):
+        self.DeployGroupIds = params.get("DeployGroupIds")
+
+
+class DeleteDeployGroupsResponse(AbstractModel):
+    """DeleteDeployGroups返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.RequestId = params.get("RequestId")
+
+
 class DeleteParamTemplateRequest(AbstractModel):
     """DeleteParamTemplate请求参数结构体
 
     """
 
     def __init__(self):
         """
@@ -1105,14 +1222,47 @@
         self.RequestId = None
 
 
     def _deserialize(self, params):
         self.RequestId = params.get("RequestId")
 
 
+class DeployGroupInfo(AbstractModel):
+    """置放群组信息
+
+    """
+
+    def __init__(self):
+        """
+        :param DeployGroupId: 置放群组 ID。
+        :type DeployGroupId: str
+        :param DeployGroupName: 置放群组名称。
+        :type DeployGroupName: str
+        :param CreateTime: 创建时间。
+        :type CreateTime: str
+        :param Description: 置放群组描述。
+        :type Description: str
+        :param Quota: 置放群组实例配额。
+        :type Quota: int
+        """
+        self.DeployGroupId = None
+        self.DeployGroupName = None
+        self.CreateTime = None
+        self.Description = None
+        self.Quota = None
+
+
+    def _deserialize(self, params):
+        self.DeployGroupId = params.get("DeployGroupId")
+        self.DeployGroupName = params.get("DeployGroupName")
+        self.CreateTime = params.get("CreateTime")
+        self.Description = params.get("Description")
+        self.Quota = params.get("Quota")
+
+
 class DescribeAccountPrivilegesRequest(AbstractModel):
     """DescribeAccountPrivileges请求参数结构体
 
     """
 
     def __init__(self):
         """
@@ -1258,16 +1408,18 @@
     """DescribeAsyncRequestInfo返回参数结构体
 
     """
 
     def __init__(self):
         """
         :param Status: 任务执行结果。可能的取值：INITIAL - 初始化，RUNNING - 运行中，SUCCESS - 执行成功，FAILED - 执行失败，KILLED - 已终止，REMOVED - 已删除，PAUSED - 终止中。
+注意：此字段可能返回 null，表示取不到有效值。
         :type Status: str
         :param Info: 任务执行信息描述。
+注意：此字段可能返回 null，表示取不到有效值。
         :type Info: str
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
         self.Status = None
         self.Info = None
         self.RequestId = None
@@ -1864,19 +2016,19 @@
         :type WithExCluster: int
         :param ExClusterId: 独享集群 ID。
         :type ExClusterId: str
         :param InstanceIds: 实例 ID。
         :type InstanceIds: list of str
         :param InitFlag: 初始化标记，可取值：0 - 未初始化，1 - 初始化。
         :type InitFlag: int
-        :param WithDr: 是否包含灾备实例，可取值：0 - 不包含，1 - 包含。
+        :param WithDr: 是否包含灾备关系对应的实例，可取值：0 - 不包含，1 - 包含。默认取值为1。如果拉取主实例，则灾备关系的数据在DrInfo字段中， 如果拉取灾备实例， 则灾备关系的数据在MasterInfo字段中。灾备关系中只包含部分基本的数据，详细的数据需要自行调接口拉取。
         :type WithDr: int
-        :param WithRo: 是否包含只读实例，可取值：0 - 不包含，1 - 包含。
+        :param WithRo: 是否包含只读实例，可取值：0 - 不包含，1 - 包含。默认取值为1。
         :type WithRo: int
-        :param WithMaster: 是否包含主实例，可取值：0 - 不包含，1 - 包含。
+        :param WithMaster: 是否包含主实例，可取值：0 - 不包含，1 - 包含。默认取值为1。
         :type WithMaster: int
         """
         self.ProjectId = None
         self.InstanceTypes = None
         self.Vips = None
         self.Status = None
         self.Offset = None
@@ -2261,14 +2413,74 @@
             for item in params.get("Items"):
                 obj = ParameterDetail()
                 obj._deserialize(item)
                 self.Items.append(obj)
         self.RequestId = params.get("RequestId")
 
 
+class DescribeDeployGroupListRequest(AbstractModel):
+    """DescribeDeployGroupList请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param DeployGroupId: 置放群组 ID。
+        :type DeployGroupId: str
+        :param DeployGroupName: 置放群组名称。
+        :type DeployGroupName: str
+        :param Limit: 返回数量，默认为20，最大值为100。
+        :type Limit: int
+        :param Offset: 偏移量，默认为0。
+        :type Offset: int
+        """
+        self.DeployGroupId = None
+        self.DeployGroupName = None
+        self.Limit = None
+        self.Offset = None
+
+
+    def _deserialize(self, params):
+        self.DeployGroupId = params.get("DeployGroupId")
+        self.DeployGroupName = params.get("DeployGroupName")
+        self.Limit = params.get("Limit")
+        self.Offset = params.get("Offset")
+
+
+class DescribeDeployGroupListResponse(AbstractModel):
+    """DescribeDeployGroupList返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param Items: 返回列表。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Items: list of DeployGroupInfo
+        :param Total: 符合条件的记录总数
+        :type Total: int
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.Items = None
+        self.Total = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        if params.get("Items") is not None:
+            self.Items = []
+            for item in params.get("Items"):
+                obj = DeployGroupInfo()
+                obj._deserialize(item)
+                self.Items.append(obj)
+        self.Total = params.get("Total")
+        self.RequestId = params.get("RequestId")
+
+
 class DescribeDeviceMonitorInfoRequest(AbstractModel):
     """DescribeDeviceMonitorInfo请求参数结构体
 
     """
 
     def __init__(self):
         """
@@ -3710,14 +3922,15 @@
     """IsolateDBInstance返回参数结构体
 
     """
 
     def __init__(self):
         """
         :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
+注意：此字段可能返回 null，表示取不到有效值。
         :type AsyncRequestId: str
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
         self.AsyncRequestId = None
         self.RequestId = None
 
@@ -4037,34 +4250,40 @@
 
     def __init__(self):
         """
         :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
         :type InstanceId: str
         :param ExpireDays: 备份文件的保留时间，单位为天。最小值为7天，最大值为732天。
         :type ExpireDays: int
-        :param StartTime: 备份时间范围，格式为：02:00-06:00，起点和终点时间目前限制为整点，目前可以选择的范围为： 00:00-12:00，02:00-06:00，06：00-10：00，10:00-14:00，14:00-18:00，18:00-22:00，22:00-02:00。
+        :param StartTime: (将废弃，建议使用 BackupTimeWindow 参数) 备份时间范围，格式为：02:00-06:00，起点和终点时间目前限制为整点，目前可以选择的范围为： 00:00-12:00，02:00-06:00，06：00-10：00，10:00-14:00，14:00-18:00，18:00-22:00，22:00-02:00。
         :type StartTime: str
         :param BackupMethod: 自动备份方式，仅支持：physical - 物理冷备
         :type BackupMethod: str
         :param BinlogExpireDays: binlog的保留时间，单位为天。最小值为7天，最大值为732天。该值的设置不能大于备份文件的保留时间。
         :type BinlogExpireDays: int
+        :param BackupTimeWindow: 备份时间窗，比如要设置每周二和周日 10:00-14:00之间备份，该参数如下：{"Monday": "", "Tuesday": "10:00-14:00", "Wednesday": "", "Thursday": "", "Friday": "", "Saturday": "", "Sunday": "10:00-14:00"}    （注：可以设置一周的某几天备份，但是每天的备份时间需要设置为相同的时间段。 如果设置了该字段，将忽略StartTime字段的设置）
+        :type BackupTimeWindow: :class:`tencentcloud.cdb.v20170320.models.CommonTimeWindow`
         """
         self.InstanceId = None
         self.ExpireDays = None
         self.StartTime = None
         self.BackupMethod = None
         self.BinlogExpireDays = None
+        self.BackupTimeWindow = None
 
 
     def _deserialize(self, params):
         self.InstanceId = params.get("InstanceId")
         self.ExpireDays = params.get("ExpireDays")
         self.StartTime = params.get("StartTime")
         self.BackupMethod = params.get("BackupMethod")
         self.BinlogExpireDays = params.get("BinlogExpireDays")
+        if params.get("BackupTimeWindow") is not None:
+            self.BackupTimeWindow = CommonTimeWindow()
+            self.BackupTimeWindow._deserialize(params.get("BackupTimeWindow"))
 
 
 class ModifyBackupConfigResponse(AbstractModel):
     """ModifyBackupConfig返回参数结构体
 
     """
 
@@ -4335,14 +4554,56 @@
 
     """
 
     def __init__(self):
         """
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
+        """
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.RequestId = params.get("RequestId")
+
+
+class ModifyNameOrDescByDpIdRequest(AbstractModel):
+    """ModifyNameOrDescByDpId请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param DeployGroupId: 置放群组 ID。
+        :type DeployGroupId: str
+        :param DeployGroupName: 置放群组名称，最长不能超过60个字符。置放群组名和置放群组描述不能都为空。
+        :type DeployGroupName: str
+        :param Description: 置放群组描述，最长不能超过200个字符。置放群组名和置放群组描述不能都为空。
+        :type Description: str
+        """
+        self.DeployGroupId = None
+        self.DeployGroupName = None
+        self.Description = None
+
+
+    def _deserialize(self, params):
+        self.DeployGroupId = params.get("DeployGroupId")
+        self.DeployGroupName = params.get("DeployGroupName")
+        self.Description = params.get("Description")
+
+
+class ModifyNameOrDescByDpIdResponse(AbstractModel):
+    """ModifyNameOrDescByDpId返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
         """
         self.RequestId = None
 
 
     def _deserialize(self, params):
         self.RequestId = params.get("RequestId")
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cdb/v20170320/cdb_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cdb/v20170320/cdb_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -263,14 +263,42 @@
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
+    def CreateDeployGroup(self, request):
+        """创建放置实例的置放群组
+
+        :param request: 调用CreateDeployGroup所需参数的结构体。
+        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateDeployGroupRequest`
+        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateDeployGroupResponse`
+
+        """
+        try:
+            params = request._serialize()
+            body = self.call("CreateDeployGroup", params)
+            response = json.loads(body)
+            if "Error" not in response["Response"]:
+                model = models.CreateDeployGroupResponse()
+                model._deserialize(response["Response"])
+                return model
+            else:
+                code = response["Response"]["Error"]["Code"]
+                message = response["Response"]["Error"]["Message"]
+                reqid = response["Response"]["RequestId"]
+                raise TencentCloudSDKException(code, message, reqid)
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
     def CreateParamTemplate(self, request):
         """该接口（CreateParamTemplate）用于创建参数模板。
 
         :param request: 调用CreateParamTemplate所需参数的结构体。
         :type request: :class:`tencentcloud.cdb.v20170320.models.CreateParamTemplateRequest`
         :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateParamTemplateResponse`
 
@@ -347,14 +375,42 @@
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
+    def DeleteDeployGroups(self, request):
+        """根据置放群组ID删除置放群组（置放群组中有资源存在时不能删除该置放群组）
+
+        :param request: 调用DeleteDeployGroups所需参数的结构体。
+        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteDeployGroupsRequest`
+        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteDeployGroupsResponse`
+
+        """
+        try:
+            params = request._serialize()
+            body = self.call("DeleteDeployGroups", params)
+            response = json.loads(body)
+            if "Error" not in response["Response"]:
+                model = models.DeleteDeployGroupsResponse()
+                model._deserialize(response["Response"])
+                return model
+            else:
+                code = response["Response"]["Error"]["Code"]
+                message = response["Response"]["Error"]["Message"]
+                reqid = response["Response"]["RequestId"]
+                raise TencentCloudSDKException(code, message, reqid)
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
     def DeleteParamTemplate(self, request):
         """该接口（DeleteParamTemplate）用于删除参数模板。
 
         :param request: 调用DeleteParamTemplate所需参数的结构体。
         :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteParamTemplateRequest`
         :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteParamTemplateResponse`
 
@@ -969,14 +1025,42 @@
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
+    def DescribeDeployGroupList(self, request):
+        """根据置放群组 ID 或置放群组名称查询置放群组列表
+
+        :param request: 调用DescribeDeployGroupList所需参数的结构体。
+        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDeployGroupListRequest`
+        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDeployGroupListResponse`
+
+        """
+        try:
+            params = request._serialize()
+            body = self.call("DescribeDeployGroupList", params)
+            response = json.loads(body)
+            if "Error" not in response["Response"]:
+                model = models.DescribeDeployGroupListResponse()
+                model._deserialize(response["Response"])
+                return model
+            else:
+                code = response["Response"]["Error"]["Code"]
+                message = response["Response"]["Error"]["Message"]
+                reqid = response["Response"]["RequestId"]
+                raise TencentCloudSDKException(code, message, reqid)
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
     def DescribeDeviceMonitorInfo(self, request):
         """本接口（DescribeDeviceMonitorInfo）用于查询云数据库物理机当天的监控信息，暂只支持内存488G、硬盘6T的实例查询。
 
         :param request: 调用DescribeDeviceMonitorInfo所需参数的结构体。
         :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDeviceMonitorInfoRequest`
         :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDeviceMonitorInfoResponse`
 
@@ -1774,14 +1858,42 @@
                 model._deserialize(response["Response"])
                 return model
             else:
                 code = response["Response"]["Error"]["Code"]
                 message = response["Response"]["Error"]["Message"]
                 reqid = response["Response"]["RequestId"]
                 raise TencentCloudSDKException(code, message, reqid)
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
+    def ModifyNameOrDescByDpId(self, request):
+        """修改置放群组的名称或者描述
+
+        :param request: 调用ModifyNameOrDescByDpId所需参数的结构体。
+        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyNameOrDescByDpIdRequest`
+        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyNameOrDescByDpIdResponse`
+
+        """
+        try:
+            params = request._serialize()
+            body = self.call("ModifyNameOrDescByDpId", params)
+            response = json.loads(body)
+            if "Error" not in response["Response"]:
+                model = models.ModifyNameOrDescByDpIdResponse()
+                model._deserialize(response["Response"])
+                return model
+            else:
+                code = response["Response"]["Error"]["Code"]
+                message = response["Response"]["Error"]["Message"]
+                reqid = response["Response"]["RequestId"]
+                raise TencentCloudSDKException(code, message, reqid)
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/ocr/v20181119/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/ocr/v20181119/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/ocr/v20181119/ocr_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/ocr/v20181119/ocr_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/asr/v20190614/asr_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/asr/v20190614/asr_client.py`

 * *Files 6% similar despite different names*

```diff
@@ -23,20 +23,18 @@
 class AsrClient(AbstractClient):
     _apiVersion = '2019-06-14'
     _endpoint = 'asr.tencentcloudapi.com'
 
 
     def CreateRecTask(self, request):
         """本接口服务对录音时长1小时以内的录音文件进行识别，异步返回识别全部结果。
-        <br>• 支持回调或轮询的方式获取结果，轮询方式请参考“录音文件识别结果查询”。
+        <br>• 支持回调或轮询的方式获取结果，结果获取请参考[ 录音文件识别结果查询](https://cloud.tencent.com/document/product/1093/37822)。
         <br>• 支持语音 URL 和本地语音文件两种请求方式。
         <br>• 接口是 HTTP RESTful 形式
 
-        在使用该接口前，需要在 [语音识别控制台](https://console.cloud.tencent.com/asr) 开通服务，并进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi) 新建密钥，<br>生成 AppID、SecretID 和 SecretKey ，用于 API 调用时生成签名，签名将用来进行接口鉴权。
-
         :param request: 调用CreateRecTask所需参数的结构体。
         :type request: :class:`tencentcloud.asr.v20190614.models.CreateRecTaskRequest`
         :rtype: :class:`tencentcloud.asr.v20190614.models.CreateRecTaskResponse`
 
         """
         try:
             params = request._serialize()
@@ -55,15 +53,17 @@
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
     def DescribeTaskStatus(self, request):
-        """本接口需要配合录音文件识别请求接口使用，单独使用无效。在调用录音文件识别接口后，可以在本接口传入TaskID来轮询识别结果。
+        """在调用录音文件识别请求接口后，有回调和轮询两种方式获取识别结果。
+        <br>• 当采用回调方式时，识别完成后会将结果通过 POST 请求的形式通知到用户在请求时填写的回调 URL，具体请参见[ 录音识别结果回调 ](https://cloud.tencent.com/document/product/1093/37139#callback)。
+        <br>• 当采用轮询方式时，需要主动提交任务ID来轮询识别结果，共有任务成功、等待、执行中和失败四种结果，具体信息请参见下文说明。
 
         :param request: 调用DescribeTaskStatus所需参数的结构体。
         :type request: :class:`tencentcloud.asr.v20190614.models.DescribeTaskStatusRequest`
         :rtype: :class:`tencentcloud.asr.v20190614.models.DescribeTaskStatusResponse`
 
         """
         try:
@@ -84,15 +84,15 @@
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
     def SentenceRecognition(self, request):
         """本接口用于对60秒之内的短音频文件进行识别。
-        <br>•   支持中文普通话、英语、粤语和带有一定方言口音的中文普通话识别。
+        <br>•   支持中文普通话、英语、粤语。
         <br>•   支持本地语音文件上传和语音URL上传两种请求方式。
         <br>•   音频格式支持wav、mp3；采样率支持8000Hz或者16000Hz；采样精度支持16bits；声道支持单声道。
         <br>•   当音频文件通过请求中body内容上传时，请求大小不能超过600KB；当音频以URL方式传输时，音频时长不可超过60s。
         <br>•   所有请求参数放在POST请求的body中，编码类型采用x-www-form-urlencoded，参数进行urlencode编码后传输。
 
         :param request: 调用SentenceRecognition所需参数的结构体。
         :type request: :class:`tencentcloud.asr.v20190614.models.SentenceRecognitionRequest`
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/asr/v20190614/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/asr/v20190614/models.py`

 * *Files 4% similar despite different names*

```diff
@@ -19,23 +19,26 @@
 class CreateRecTaskRequest(AbstractModel):
     """CreateRecTask请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param EngineModelType: 引擎类型。8k_0：电话 8k 通用模型；16k_0：16k 通用模型；8k_6: 电话场景下单声道话者分离模型。
+        :param EngineModelType: 引擎类型。
+8k_0：电话 8k 通用模型；
+16k_0：16k 通用模型；
+8k_6: 电话场景下单声道话者分离模型。
         :type EngineModelType: str
         :param ChannelNum: 语音声道数。1：单声道；2：双声道（仅在电话 8k 通用模型下支持）。
         :type ChannelNum: int
         :param ResTextFormat: 识别结果文本编码方式。0：UTF-8。
         :type ResTextFormat: int
         :param SourceType: 语音数据来源。0：语音 URL；1：语音数据（post body）。
         :type SourceType: int
-        :param CallbackUrl: 回调 URL，用户自行搭建的用于接收识别结果的服务器地址， 长度小于2048字节。
+        :param CallbackUrl: 回调 URL，用户自行搭建的用于接收识别结果的服务器地址， 长度小于2048字节。如果用户使用回调方式获取识别结果，需提交该参数；如果用户使用轮询方式获取识别结果，则无需提交该参数。
         :type CallbackUrl: str
         :param Url: 语音的URL地址，需要公网可下载。长度小于2048字节，当 source_type 值为 0 时须填写该字段，为 1 时不需要填写。注意：请确保录音文件时长在一个小时之内，否则可能识别失败。请保证文件的下载速度，否则可能下载失败。
         :type Url: str
         :param Data: 语音数据，当SourceType 值为1时必须填写，为0可不写。要base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频数据要小于5MB。
         :type Data: str
         :param DataLen: 数据长度，当 SourceType 值为1时必须填写，为0可不写（此数据长度为数据未进行base64编码时的数据长度）。
         :type DataLen: int
@@ -131,15 +134,19 @@
 
     def __init__(self):
         """
         :param ProjectId: 腾讯云项目 ID，可填 0，总长度不超过 1024 字节。
         :type ProjectId: int
         :param SubServiceType: 子服务类型。2： 一句话识别。
         :type SubServiceType: int
-        :param EngSerViceType: 引擎类型。8k：电话 8k 中文普通话通用；16k：16k 中文普通话通用；16k_en：16k 英语；16k_ca：16k 粤语。
+        :param EngSerViceType: 引擎类型。
+8k：电话 8k 中文普通话通用；
+16k：16k 中文普通话通用；
+16k_en：16k 英语；
+16k_ca：16k 粤语。
         :type EngSerViceType: str
         :param SourceType: 语音数据来源。0：语音 URL；1：语音数据（post body）。
         :type SourceType: int
         :param VoiceFormat: 识别音频的音频格式。mp3、wav。
         :type VoiceFormat: str
         :param UsrAudioKey: 用户端对此任务的唯一标识，用户自助生成，用于用户查找识别结果。
         :type UsrAudioKey: str
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/mariadb/v20170312/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/mariadb/v20170312/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/mariadb/v20170312/mariadb_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/mariadb/v20170312/mariadb_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/sts/v20180813/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/sts/v20180813/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/sts/v20180813/sts_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/sts/v20180813/sts_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/dts/v20180330/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/dts/v20180330/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/dts/v20180330/dts_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/dts/v20180330/dts_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/aai/v20180522/aai_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/aai/v20180522/aai_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/aai/v20180522/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/aai/v20180522/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/ecc/v20181213/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/ecc/v20181213/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/ecc/v20181213/ecc_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/ecc/v20181213/ecc_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/bmeip/v20180625/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/bmeip/v20180625/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/bmeip/v20180625/bmeip_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/bmeip/v20180625/bmeip_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/mps/v20190612/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/mps/v20190612/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/mps/v20190612/mps_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/mps/v20190612/mps_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/__init__.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -10,8 +10,8 @@
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 
-__version__ = '3.0.98'
+__version__ = '3.0.99'
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/soe/v20180724/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/soe/v20180724/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/soe/v20180724/soe_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/soe/v20180724/soe_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cvm/v20170312/cvm_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cvm/v20170312/cvm_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cvm/v20170312/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cvm/v20170312/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/yunsou/v20180504/yunsou_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/yunsou/v20180504/yunsou_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/yunsou/v20180504/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/yunsou/v20180504/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/batch/v20170312/batch_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/batch/v20170312/batch_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/batch/v20170312/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/batch/v20170312/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/dcdb/v20180411/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/dcdb/v20180411/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/dcdb/v20180411/dcdb_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/dcdb/v20180411/dcdb_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/redis/v20180412/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/redis/v20180412/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/redis/v20180412/redis_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/redis/v20180412/redis_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/vpc/v20170312/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/vpc/v20170312/models.py`

 * *Files 4% similar despite different names*

```diff
@@ -1131,14 +1131,91 @@
         self.InstanceName = params.get("InstanceName")
         self.InstanceRegion = params.get("InstanceRegion")
         self.UpdateTime = params.get("UpdateTime")
         self.Enabled = params.get("Enabled")
         self.InstanceUin = params.get("InstanceUin")
 
 
+class CheckNetDetectStateRequest(AbstractModel):
+    """CheckNetDetectState请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param DetectDestinationIp: 探测目的IPv4地址数组，最多两个。
+        :type DetectDestinationIp: list of str
+        :param NextHopType: 下一跳类型，目前我们支持的类型有：
+VPN：VPN网关；
+DIRECTCONNECT：专线网关；
+PEERCONNECTION：对等连接；
+NAT：NAT网关；
+NORMAL_CVM：普通云主机；
+        :type NextHopType: str
+        :param NextHopDestination: 下一跳目的网关，取值与“下一跳类型”相关：
+下一跳类型为VPN，取值VPN网关ID，形如：vpngw-12345678；
+下一跳类型为DIRECTCONNECT，取值专线网关ID，形如：dcg-12345678；
+下一跳类型为PEERCONNECTION，取值对等连接ID，形如：pcx-12345678；
+下一跳类型为NAT，取值Nat网关，形如：nat-12345678；
+下一跳类型为NORMAL_CVM，取值云主机IPv4地址，形如：10.0.0.12；
+        :type NextHopDestination: str
+        :param NetDetectId: 网络探测实例ID。形如：netd-12345678。
+        :type NetDetectId: str
+        :param VpcId: `VPC`实例`ID`。形如：`vpc-12345678`
+        :type VpcId: str
+        :param SubnetId: 子网实例ID。形如：subnet-12345678。
+        :type SubnetId: str
+        :param NetDetectName: 网络探测名称，最大长度不能超过60个字节。
+        :type NetDetectName: str
+        """
+        self.DetectDestinationIp = None
+        self.NextHopType = None
+        self.NextHopDestination = None
+        self.NetDetectId = None
+        self.VpcId = None
+        self.SubnetId = None
+        self.NetDetectName = None
+
+
+    def _deserialize(self, params):
+        self.DetectDestinationIp = params.get("DetectDestinationIp")
+        self.NextHopType = params.get("NextHopType")
+        self.NextHopDestination = params.get("NextHopDestination")
+        self.NetDetectId = params.get("NetDetectId")
+        self.VpcId = params.get("VpcId")
+        self.SubnetId = params.get("SubnetId")
+        self.NetDetectName = params.get("NetDetectName")
+
+
+class CheckNetDetectStateResponse(AbstractModel):
+    """CheckNetDetectState返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param NetDetectIpStateSet: 网络探测验证结果对象数组。
+        :type NetDetectIpStateSet: list of NetDetectIpState
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.NetDetectIpStateSet = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        if params.get("NetDetectIpStateSet") is not None:
+            self.NetDetectIpStateSet = []
+            for item in params.get("NetDetectIpStateSet"):
+                obj = NetDetectIpState()
+                obj._deserialize(item)
+                self.NetDetectIpStateSet.append(obj)
+        self.RequestId = params.get("RequestId")
+
+
 class ClassicLinkInstance(AbstractModel):
     """私有网络和基础网络互通设备
 
     """
 
     def __init__(self):
         """
@@ -1821,14 +1898,88 @@
                 obj = NatGateway()
                 obj._deserialize(item)
                 self.NatGatewaySet.append(obj)
         self.TotalCount = params.get("TotalCount")
         self.RequestId = params.get("RequestId")
 
 
+class CreateNetDetectRequest(AbstractModel):
+    """CreateNetDetect请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param VpcId: `VPC`实例`ID`。形如：`vpc-12345678`
+        :type VpcId: str
+        :param SubnetId: 子网实例ID。形如：subnet-12345678。
+        :type SubnetId: str
+        :param NetDetectName: 网络探测名称，最大长度不能超过60个字节。
+        :type NetDetectName: str
+        :param DetectDestinationIp: 探测目的IPv4地址数组。最多两个。
+        :type DetectDestinationIp: list of str
+        :param NextHopType: 下一跳类型，目前我们支持的类型有：
+VPN：VPN网关；
+DIRECTCONNECT：专线网关；
+PEERCONNECTION：对等连接；
+NAT：NAT网关；
+NORMAL_CVM：普通云主机；
+        :type NextHopType: str
+        :param NextHopDestination: 下一跳目的网关，取值与“下一跳类型”相关：
+下一跳类型为VPN，取值VPN网关ID，形如：vpngw-12345678；
+下一跳类型为DIRECTCONNECT，取值专线网关ID，形如：dcg-12345678；
+下一跳类型为PEERCONNECTION，取值对等连接ID，形如：pcx-12345678；
+下一跳类型为NAT，取值Nat网关，形如：nat-12345678；
+下一跳类型为NORMAL_CVM，取值云主机IPv4地址，形如：10.0.0.12；
+        :type NextHopDestination: str
+        :param NetDetectDescription: 网络探测描述。
+        :type NetDetectDescription: str
+        """
+        self.VpcId = None
+        self.SubnetId = None
+        self.NetDetectName = None
+        self.DetectDestinationIp = None
+        self.NextHopType = None
+        self.NextHopDestination = None
+        self.NetDetectDescription = None
+
+
+    def _deserialize(self, params):
+        self.VpcId = params.get("VpcId")
+        self.SubnetId = params.get("SubnetId")
+        self.NetDetectName = params.get("NetDetectName")
+        self.DetectDestinationIp = params.get("DetectDestinationIp")
+        self.NextHopType = params.get("NextHopType")
+        self.NextHopDestination = params.get("NextHopDestination")
+        self.NetDetectDescription = params.get("NetDetectDescription")
+
+
+class CreateNetDetectResponse(AbstractModel):
+    """CreateNetDetect返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param NetDetect: 网络探测（NetDetect）对象。
+        :type NetDetect: :class:`tencentcloud.vpc.v20170312.models.NetDetect`
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.NetDetect = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        if params.get("NetDetect") is not None:
+            self.NetDetect = NetDetect()
+            self.NetDetect._deserialize(params.get("NetDetect"))
+        self.RequestId = params.get("RequestId")
+
+
 class CreateNetworkInterfaceRequest(AbstractModel):
     """CreateNetworkInterface请求参数结构体
 
     """
 
     def __init__(self):
         """
@@ -2965,14 +3116,48 @@
         self.RequestId = None
 
 
     def _deserialize(self, params):
         self.RequestId = params.get("RequestId")
 
 
+class DeleteNetDetectRequest(AbstractModel):
+    """DeleteNetDetect请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param NetDetectId: 网络探测实例`ID`。形如：`netd-12345678`
+        :type NetDetectId: str
+        """
+        self.NetDetectId = None
+
+
+    def _deserialize(self, params):
+        self.NetDetectId = params.get("NetDetectId")
+
+
+class DeleteNetDetectResponse(AbstractModel):
+    """DeleteNetDetect返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.RequestId = params.get("RequestId")
+
+
 class DeleteNetworkInterfaceRequest(AbstractModel):
     """DeleteNetworkInterface请求参数结构体
 
     """
 
     def __init__(self):
         """
@@ -4821,14 +5006,151 @@
                 obj = NatGateway()
                 obj._deserialize(item)
                 self.NatGatewaySet.append(obj)
         self.TotalCount = params.get("TotalCount")
         self.RequestId = params.get("RequestId")
 
 
+class DescribeNetDetectStatesRequest(AbstractModel):
+    """DescribeNetDetectStates请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param NetDetectIds: 网络探测实例`ID`数组。形如：[`netd-12345678`]
+        :type NetDetectIds: list of str
+        :param Filters: 过滤条件，参数不支持同时指定NetDetectIds和Filters。
+<li>net-detect-id - String - （过滤条件）网络探测实例ID，形如：netd-12345678</li>
+        :type Filters: list of Filter
+        :param Offset: 偏移量，默认为0。
+        :type Offset: int
+        :param Limit: 返回数量，默认为20，最大值为100。
+        :type Limit: int
+        """
+        self.NetDetectIds = None
+        self.Filters = None
+        self.Offset = None
+        self.Limit = None
+
+
+    def _deserialize(self, params):
+        self.NetDetectIds = params.get("NetDetectIds")
+        if params.get("Filters") is not None:
+            self.Filters = []
+            for item in params.get("Filters"):
+                obj = Filter()
+                obj._deserialize(item)
+                self.Filters.append(obj)
+        self.Offset = params.get("Offset")
+        self.Limit = params.get("Limit")
+
+
+class DescribeNetDetectStatesResponse(AbstractModel):
+    """DescribeNetDetectStates返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param NetDetectStateSet: 符合条件的网络探测验证结果对象数组。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type NetDetectStateSet: list of NetDetectState
+        :param TotalCount: 符合条件的网络探测验证结果对象数量。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type TotalCount: int
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.NetDetectStateSet = None
+        self.TotalCount = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        if params.get("NetDetectStateSet") is not None:
+            self.NetDetectStateSet = []
+            for item in params.get("NetDetectStateSet"):
+                obj = NetDetectState()
+                obj._deserialize(item)
+                self.NetDetectStateSet.append(obj)
+        self.TotalCount = params.get("TotalCount")
+        self.RequestId = params.get("RequestId")
+
+
+class DescribeNetDetectsRequest(AbstractModel):
+    """DescribeNetDetects请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param NetDetectIds: 网络探测实例`ID`数组。形如：[`netd-12345678`]
+        :type NetDetectIds: list of str
+        :param Filters: 过滤条件，参数不支持同时指定NetDetectIds和Filters。
+<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-12345678</li>
+<li>net-detect-id - String - （过滤条件）网络探测实例ID，形如：netd-12345678</li>
+<li>subnet-id - String - （过滤条件）子网实例ID，形如：subnet-12345678</li>
+<li>net-detect-name - String - （过滤条件）网络探测名称</li>
+        :type Filters: list of Filter
+        :param Offset: 偏移量，默认为0。
+        :type Offset: int
+        :param Limit: 返回数量，默认为20，最大值为100。
+        :type Limit: int
+        """
+        self.NetDetectIds = None
+        self.Filters = None
+        self.Offset = None
+        self.Limit = None
+
+
+    def _deserialize(self, params):
+        self.NetDetectIds = params.get("NetDetectIds")
+        if params.get("Filters") is not None:
+            self.Filters = []
+            for item in params.get("Filters"):
+                obj = Filter()
+                obj._deserialize(item)
+                self.Filters.append(obj)
+        self.Offset = params.get("Offset")
+        self.Limit = params.get("Limit")
+
+
+class DescribeNetDetectsResponse(AbstractModel):
+    """DescribeNetDetects返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param NetDetectSet: 符合条件的网络探测对象数组。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type NetDetectSet: list of NetDetect
+        :param TotalCount: 符合条件的网络探测对象数量。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type TotalCount: int
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.NetDetectSet = None
+        self.TotalCount = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        if params.get("NetDetectSet") is not None:
+            self.NetDetectSet = []
+            for item in params.get("NetDetectSet"):
+                obj = NetDetect()
+                obj._deserialize(item)
+                self.NetDetectSet.append(obj)
+        self.TotalCount = params.get("TotalCount")
+        self.RequestId = params.get("RequestId")
+
+
 class DescribeNetworkInterfaceLimitRequest(AbstractModel):
     """DescribeNetworkInterfaceLimit请求参数结构体
 
     """
 
     def __init__(self):
         """
@@ -7773,14 +8095,78 @@
         self.RequestId = None
 
 
     def _deserialize(self, params):
         self.RequestId = params.get("RequestId")
 
 
+class ModifyNetDetectRequest(AbstractModel):
+    """ModifyNetDetect请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param NetDetectId: 网络探测实例`ID`。形如：`netd-12345678`
+        :type NetDetectId: str
+        :param NetDetectName: 网络探测名称，最大长度不能超过60个字节。
+        :type NetDetectName: str
+        :param DetectDestinationIp: 探测目的IPv4地址数组，最多两个。
+        :type DetectDestinationIp: list of str
+        :param NextHopType: 下一跳类型，目前我们支持的类型有：
+VPN：VPN网关；
+DIRECTCONNECT：专线网关；
+PEERCONNECTION：对等连接；
+NAT：NAT网关；
+NORMAL_CVM：普通云主机；
+        :type NextHopType: str
+        :param NextHopDestination: 下一跳目的网关，取值与“下一跳类型”相关：
+下一跳类型为VPN，取值VPN网关ID，形如：vpngw-12345678；
+下一跳类型为DIRECTCONNECT，取值专线网关ID，形如：dcg-12345678；
+下一跳类型为PEERCONNECTION，取值对等连接ID，形如：pcx-12345678；
+下一跳类型为NAT，取值Nat网关，形如：nat-12345678；
+下一跳类型为NORMAL_CVM，取值云主机IPv4地址，形如：10.0.0.12；
+        :type NextHopDestination: str
+        :param NetDetectDescription: 网络探测描述。
+        :type NetDetectDescription: str
+        """
+        self.NetDetectId = None
+        self.NetDetectName = None
+        self.DetectDestinationIp = None
+        self.NextHopType = None
+        self.NextHopDestination = None
+        self.NetDetectDescription = None
+
+
+    def _deserialize(self, params):
+        self.NetDetectId = params.get("NetDetectId")
+        self.NetDetectName = params.get("NetDetectName")
+        self.DetectDestinationIp = params.get("DetectDestinationIp")
+        self.NextHopType = params.get("NextHopType")
+        self.NextHopDestination = params.get("NextHopDestination")
+        self.NetDetectDescription = params.get("NetDetectDescription")
+
+
+class ModifyNetDetectResponse(AbstractModel):
+    """ModifyNetDetect返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.RequestId = params.get("RequestId")
+
+
 class ModifyNetworkInterfaceAttributeRequest(AbstractModel):
     """ModifyNetworkInterfaceAttribute请求参数结构体
 
     """
 
     def __init__(self):
         """
@@ -8409,14 +8795,152 @@
         self.PrivatePort = params.get("PrivatePort")
         self.Description = params.get("Description")
         self.NatGatewayId = params.get("NatGatewayId")
         self.VpcId = params.get("VpcId")
         self.CreatedTime = params.get("CreatedTime")
 
 
+class NetDetect(AbstractModel):
+    """网络探测对象。
+
+    """
+
+    def __init__(self):
+        """
+        :param VpcId: `VPC`实例`ID`。形如：`vpc-12345678`
+        :type VpcId: str
+        :param VpcName: `VPC`实例名称。
+        :type VpcName: str
+        :param SubnetId: 子网实例ID。形如：subnet-12345678。
+        :type SubnetId: str
+        :param SubnetName: 子网实例名称。
+        :type SubnetName: str
+        :param NetDetectId: 网络探测实例ID。形如：netd-12345678。
+        :type NetDetectId: str
+        :param NetDetectName: 网络探测名称，最大长度不能超过60个字节。
+        :type NetDetectName: str
+        :param DetectDestinationIp: 探测目的IPv4地址数组，最多两个。
+        :type DetectDestinationIp: list of str
+        :param DetectSourceIp: 系统自动分配的探测源IPv4数组。长度为2。
+        :type DetectSourceIp: list of str
+        :param NextHopType: 下一跳类型，目前我们支持的类型有：
+VPN：VPN网关；
+DIRECTCONNECT：专线网关；
+PEERCONNECTION：对等连接；
+NAT：NAT网关；
+NORMAL_CVM：普通云主机；
+        :type NextHopType: str
+        :param NextHopDestination: 下一跳目的网关，取值与“下一跳类型”相关：
+下一跳类型为VPN，取值VPN网关ID，形如：vpngw-12345678；
+下一跳类型为DIRECTCONNECT，取值专线网关ID，形如：dcg-12345678；
+下一跳类型为PEERCONNECTION，取值对等连接ID，形如：pcx-12345678；
+下一跳类型为NAT，取值Nat网关，形如：nat-12345678；
+下一跳类型为NORMAL_CVM，取值云主机IPv4地址，形如：10.0.0.12；
+        :type NextHopDestination: str
+        :param NextHopName: 下一跳网关名称。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type NextHopName: str
+        :param NetDetectDescription: 网络探测描述。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type NetDetectDescription: str
+        :param CreateTime: 创建时间。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type CreateTime: str
+        """
+        self.VpcId = None
+        self.VpcName = None
+        self.SubnetId = None
+        self.SubnetName = None
+        self.NetDetectId = None
+        self.NetDetectName = None
+        self.DetectDestinationIp = None
+        self.DetectSourceIp = None
+        self.NextHopType = None
+        self.NextHopDestination = None
+        self.NextHopName = None
+        self.NetDetectDescription = None
+        self.CreateTime = None
+
+
+    def _deserialize(self, params):
+        self.VpcId = params.get("VpcId")
+        self.VpcName = params.get("VpcName")
+        self.SubnetId = params.get("SubnetId")
+        self.SubnetName = params.get("SubnetName")
+        self.NetDetectId = params.get("NetDetectId")
+        self.NetDetectName = params.get("NetDetectName")
+        self.DetectDestinationIp = params.get("DetectDestinationIp")
+        self.DetectSourceIp = params.get("DetectSourceIp")
+        self.NextHopType = params.get("NextHopType")
+        self.NextHopDestination = params.get("NextHopDestination")
+        self.NextHopName = params.get("NextHopName")
+        self.NetDetectDescription = params.get("NetDetectDescription")
+        self.CreateTime = params.get("CreateTime")
+
+
+class NetDetectIpState(AbstractModel):
+    """网络探测目的IP的验证结果。
+
+    """
+
+    def __init__(self):
+        """
+        :param DetectDestinationIp: 探测目的IPv4地址。
+        :type DetectDestinationIp: str
+        :param State: 探测结果。
+0：成功；
+-1：查询不到路由丢包；
+-2：外出ACL丢包；
+-3：IN ACL丢包；
+-4：其他错误；
+        :type State: int
+        :param Delay: 时延，单位毫秒
+        :type Delay: int
+        :param PacketLossRate: 丢包率
+        :type PacketLossRate: int
+        """
+        self.DetectDestinationIp = None
+        self.State = None
+        self.Delay = None
+        self.PacketLossRate = None
+
+
+    def _deserialize(self, params):
+        self.DetectDestinationIp = params.get("DetectDestinationIp")
+        self.State = params.get("State")
+        self.Delay = params.get("Delay")
+        self.PacketLossRate = params.get("PacketLossRate")
+
+
+class NetDetectState(AbstractModel):
+    """网络探测验证结果。
+
+    """
+
+    def __init__(self):
+        """
+        :param NetDetectId: 网络探测实例ID。形如：netd-12345678。
+        :type NetDetectId: str
+        :param NetDetectIpStateSet: 网络探测目的IP验证结果对象数组。
+        :type NetDetectIpStateSet: list of NetDetectIpState
+        """
+        self.NetDetectId = None
+        self.NetDetectIpStateSet = None
+
+
+    def _deserialize(self, params):
+        self.NetDetectId = params.get("NetDetectId")
+        if params.get("NetDetectIpStateSet") is not None:
+            self.NetDetectIpStateSet = []
+            for item in params.get("NetDetectIpStateSet"):
+                obj = NetDetectIpState()
+                obj._deserialize(item)
+                self.NetDetectIpStateSet.append(obj)
+
+
 class NetworkInterface(AbstractModel):
     """弹性网卡
 
     """
 
     def __init__(self):
         """
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/vpc/v20170312/vpc_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/vpc/v20170312/vpc_client.py`

 * *Files 2% similar despite different names*

```diff
@@ -415,14 +415,42 @@
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
+    def CheckNetDetectState(self, request):
+        """本接口(CheckNetDetectState)用于验证网络探测。
+
+        :param request: 调用CheckNetDetectState所需参数的结构体。
+        :type request: :class:`tencentcloud.vpc.v20170312.models.CheckNetDetectStateRequest`
+        :rtype: :class:`tencentcloud.vpc.v20170312.models.CheckNetDetectStateResponse`
+
+        """
+        try:
+            params = request._serialize()
+            body = self.call("CheckNetDetectState", params)
+            response = json.loads(body)
+            if "Error" not in response["Response"]:
+                model = models.CheckNetDetectStateResponse()
+                model._deserialize(response["Response"])
+                return model
+            else:
+                code = response["Response"]["Error"]["Code"]
+                message = response["Response"]["Error"]["Message"]
+                reqid = response["Response"]["RequestId"]
+                raise TencentCloudSDKException(code, message, reqid)
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
     def CreateAddressTemplate(self, request):
         """本接口（CreateAddressTemplate）用于创建IP地址模版
 
         :param request: 调用CreateAddressTemplate所需参数的结构体。
         :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateRequest`
         :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateResponse`
 
@@ -789,14 +817,42 @@
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
+    def CreateNetDetect(self, request):
+        """本接口(CreateNetDetect)用于创建网络探测。
+
+        :param request: 调用CreateNetDetect所需参数的结构体。
+        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetDetectRequest`
+        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetDetectResponse`
+
+        """
+        try:
+            params = request._serialize()
+            body = self.call("CreateNetDetect", params)
+            response = json.loads(body)
+            if "Error" not in response["Response"]:
+                model = models.CreateNetDetectResponse()
+                model._deserialize(response["Response"])
+                return model
+            else:
+                code = response["Response"]["Error"]["Code"]
+                message = response["Response"]["Error"]["Message"]
+                reqid = response["Response"]["RequestId"]
+                raise TencentCloudSDKException(code, message, reqid)
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
     def CreateNetworkInterface(self, request):
         """本接口（CreateNetworkInterface）用于创建弹性网卡。
         * 创建弹性网卡时可以指定内网IP，并且可以指定一个主IP，指定的内网IP必须在弹性网卡所在子网内，而且不能被占用。
         * 创建弹性网卡时可以指定需要申请的内网IP数量，系统会随机生成内网IP地址。
         * 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href="/document/product/576/18527">弹性网卡使用限制</a>。
         * 创建弹性网卡同时可以绑定已有安全组。
 
@@ -1498,14 +1554,42 @@
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
+    def DeleteNetDetect(self, request):
+        """本接口(DeleteNetDetect)用于删除网络探测实例。
+
+        :param request: 调用DeleteNetDetect所需参数的结构体。
+        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetDetectRequest`
+        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetDetectResponse`
+
+        """
+        try:
+            params = request._serialize()
+            body = self.call("DeleteNetDetect", params)
+            response = json.loads(body)
+            if "Error" not in response["Response"]:
+                model = models.DeleteNetDetectResponse()
+                model._deserialize(response["Response"])
+                return model
+            else:
+                code = response["Response"]["Error"]["Code"]
+                message = response["Response"]["Error"]["Message"]
+                reqid = response["Response"]["RequestId"]
+                raise TencentCloudSDKException(code, message, reqid)
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
     def DeleteNetworkInterface(self, request):
         """本接口（DeleteNetworkInterface）用于删除弹性网卡。
         * 弹性网卡上绑定了云主机时，不能被删除。
         * 删除指定弹性网卡，弹性网卡必须先和子机解绑才能删除。删除之后弹性网卡上所有内网IP都将被退还。
 
         :param request: 调用DeleteNetworkInterface所需参数的结构体。
         :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkInterfaceRequest`
@@ -2491,14 +2575,70 @@
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
+    def DescribeNetDetectStates(self, request):
+        """本接口(DescribeNetDetectStates)用于查询网络探测验证结果列表。
+
+        :param request: 调用DescribeNetDetectStates所需参数的结构体。
+        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectStatesRequest`
+        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectStatesResponse`
+
+        """
+        try:
+            params = request._serialize()
+            body = self.call("DescribeNetDetectStates", params)
+            response = json.loads(body)
+            if "Error" not in response["Response"]:
+                model = models.DescribeNetDetectStatesResponse()
+                model._deserialize(response["Response"])
+                return model
+            else:
+                code = response["Response"]["Error"]["Code"]
+                message = response["Response"]["Error"]["Message"]
+                reqid = response["Response"]["RequestId"]
+                raise TencentCloudSDKException(code, message, reqid)
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
+    def DescribeNetDetects(self, request):
+        """本接口（DescribeNetDetects）用于查询网络探测列表。
+
+        :param request: 调用DescribeNetDetects所需参数的结构体。
+        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectsRequest`
+        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectsResponse`
+
+        """
+        try:
+            params = request._serialize()
+            body = self.call("DescribeNetDetects", params)
+            response = json.loads(body)
+            if "Error" not in response["Response"]:
+                model = models.DescribeNetDetectsResponse()
+                model._deserialize(response["Response"])
+                return model
+            else:
+                code = response["Response"]["Error"]["Code"]
+                message = response["Response"]["Error"]["Message"]
+                reqid = response["Response"]["RequestId"]
+                raise TencentCloudSDKException(code, message, reqid)
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
     def DescribeNetworkInterfaceLimit(self, request):
         """本接口（DescribeNetworkInterfaceLimit）根据CVM实例ID查询弹性网卡配额，返回该CVM实例能绑定的弹性网卡配额，以及每个弹性网卡可以分配的ip配额
 
         :param request: 调用DescribeNetworkInterfaceLimit所需参数的结构体。
         :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfaceLimitRequest`
         :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfaceLimitResponse`
 
@@ -3842,14 +3982,42 @@
                 model._deserialize(response["Response"])
                 return model
             else:
                 code = response["Response"]["Error"]["Code"]
                 message = response["Response"]["Error"]["Message"]
                 reqid = response["Response"]["RequestId"]
                 raise TencentCloudSDKException(code, message, reqid)
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
+    def ModifyNetDetect(self, request):
+        """本接口(ModifyNetDetect)用于修改网络探测参数。
+
+        :param request: 调用ModifyNetDetect所需参数的结构体。
+        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetDetectRequest`
+        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetDetectResponse`
+
+        """
+        try:
+            params = request._serialize()
+            body = self.call("ModifyNetDetect", params)
+            response = json.loads(body)
+            if "Error" not in response["Response"]:
+                model = models.ModifyNetDetectResponse()
+                model._deserialize(response["Response"])
+                return model
+            else:
+                code = response["Response"]["Error"]["Code"]
+                message = response["Response"]["Error"]["Message"]
+                reqid = response["Response"]["RequestId"]
+                raise TencentCloudSDKException(code, message, reqid)
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cbs/v20170312/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cbs/v20170312/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cbs/v20170312/cbs_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cbs/v20170312/cbs_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tia/v20180226/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tia/v20180226/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tia/v20180226/tia_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tia/v20180226/tia_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/autoscaling/v20180419/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/autoscaling/v20180419/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/autoscaling/v20180419/autoscaling_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/autoscaling/v20180419/autoscaling_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/facefusion/v20181201/facefusion_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/facefusion/v20181201/facefusion_client.py`

 * *Files 14% similar despite different names*

```diff
@@ -52,15 +52,19 @@
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
     def FuseFace(self, request):
-        """选脸融合
+        """本接口用于单脸、多脸融合，用户上传人脸图片，获取与模板融合后的人脸图片。查看 <a href="https://cloud.tencent.com/document/product/670/38247" target="_blank">选脸融合接入指引</a>。
+
+        未发布的活动请求频率限制为1次/秒，已发布的活动请求频率限制50次/秒。如有需要提高活动的请求频率限制，请在控制台中申请。
+        >
+        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
 
         :param request: 调用FuseFace所需参数的结构体。
         :type request: :class:`tencentcloud.facefusion.v20181201.models.FuseFaceRequest`
         :rtype: :class:`tencentcloud.facefusion.v20181201.models.FuseFaceResponse`
 
         """
         try:
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/facefusion/v20181201/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/facefusion/v20181201/models.py`

 * *Files 0% similar despite different names*

```diff
@@ -58,15 +58,15 @@
 
     """
 
     def __init__(self):
         """
         :param Image: RspImgType 为 url 时，返回结果的 url， RspImgType 为 base64 时返回 base64 数据。当前仅支持 url 方式，base64 方式后期开放。
         :type Image: str
-        :param ReviewResultSet: 鉴黄鉴政结果
+        :param ReviewResultSet: 鉴政结果
         :type ReviewResultSet: list of FuseFaceReviewResult
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
         self.Image = None
         self.ReviewResultSet = None
         self.RequestId = None
@@ -121,15 +121,15 @@
         """
         :param ProjectId: 活动 ID，请在人脸融合控制台查看。
         :type ProjectId: str
         :param ModelId: 素材 ID，请在人脸融合控制台查看。
         :type ModelId: str
         :param RspImgType: 返回图像方式（url 或 base64) ，二选一。url有效期为30天。
         :type RspImgType: str
-        :param MergeInfos: 人脸图片和待被融合的素材模板图的人脸位置信息。
+        :param MergeInfos: 用户人脸图片、素材模板图的人脸位置信息。
         :type MergeInfos: list of MergeInfo
         :param FuseProfileDegree: 脸型融合比例，数值越高，融合后的脸型越像素材人物。取值范围[0,100] 
 若此参数不填写，则使用人脸融合控制台中脸型参数数值。
         :type FuseProfileDegree: int
         :param FuseFaceDegree: 五官融合比例，数值越高，融合后的五官越像素材人物。取值范围[0,100] 
 若此参数不填写，则使用人脸融合控制台中五官参数数值。
         :type FuseFaceDegree: int
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/yunjing/v20180228/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/yunjing/v20180228/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/yunjing/v20180228/yunjing_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/yunjing/v20180228/yunjing_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/vod/v20180717/vod_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/vod/v20180717/vod_client.py`

 * *Files 1% similar despite different names*

```diff
@@ -1159,23 +1159,23 @@
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
     def DescribeMediaInfos(self, request):
-        """1. 该接口可以获取多个视频的多种信息，包括：
-            1. 基础信息（basicInfo）：包括视频名称、分类、播放地址、封面图片等。
+        """1. 该接口可以获取多个媒体文件的多种信息，包括：
+            1. 基础信息（basicInfo）：包括媒体名称、分类、播放地址、封面图片等。
             2. 元信息（metaData）：包括大小、时长、视频流信息、音频流信息等。
-            3. 转码结果信息（transcodeInfo）：包括该视频转码生成的各种码率的视频的地址、规格、码率、分辨率等。
-            4. 转动图结果信息（animatedGraphicsInfo）：对视频转动图（如 gif）后，动图相关信息。
-            5. 采样截图信息（sampleSnapshotInfo）：对视频采样截图后，相关截图信息。
-            6. 雪碧图信息（imageSpriteInfo）：对视频截取雪碧图之后，雪碧图的相关信息。
-            7. 指定时间点截图信息（snapshotByTimeOffsetInfo）：对视频依照指定时间点截图后，各个截图的信息。
-            8. 视频打点信息（keyFrameDescInfo）：对视频设置的各个打点信息。
+            3. 转码结果信息（transcodeInfo）：包括该媒体转码生成的各种规格的媒体地址、视频流参数、音频流参数等。
+            4. 转动图结果信息（animatedGraphicsInfo）：对视频转动图（如 gif）后的动图信息。
+            5. 采样截图信息（sampleSnapshotInfo）：对视频采样截图后的截图信息。
+            6. 雪碧图信息（imageSpriteInfo）：对视频截取雪碧图后的雪碧图信息。
+            7. 指定时间点截图信息（snapshotByTimeOffsetInfo）：对视频依照指定时间点截图后，的截图信息。
+            8. 视频打点信息（keyFrameDescInfo）：对视频设置的打点信息。
             9. 转自适应码流信息（adaptiveDynamicStreamingInfo）：包括规格、加密类型、打包格式等相关信息。
         2. 可以指定回包只返回部分信息。
 
         :param request: 调用DescribeMediaInfos所需参数的结构体。
         :type request: :class:`tencentcloud.vod.v20180717.models.DescribeMediaInfosRequest`
         :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeMediaInfosResponse`
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/vod/v20180717/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/vod/v20180717/models.py`

 * *Files 0% similar despite different names*

```diff
@@ -8583,15 +8583,15 @@
         :param AreaCoordSet: 嫌疑文字出现的区域坐标 (像素级)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。
 注意：此字段可能返回 null，表示取不到有效值。
         :type AreaCoordSet: list of int
         :param Url: 嫌疑图片 URL （图片不会永久存储，到达
 PicUrlExpireTime 时间点后图片将被删除）。
         :type Url: str
         :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
-        :type PicUrlExpireTime: int
+        :type PicUrlExpireTime: str
         """
         self.StartTimeOffset = None
         self.EndTimeOffset = None
         self.Confidence = None
         self.Suggestion = None
         self.KeywordSet = None
         self.AreaCoordSet = None
@@ -11927,25 +11927,29 @@
         :type AiContentReviewTask: :class:`tencentcloud.vod.v20180717.models.AiContentReviewTaskInput`
         :param AiAnalysisTask: AI 智能内容分析类型任务参数。
 注意：此字段可能返回 null，表示取不到有效值。
         :type AiAnalysisTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskInput`
         :param AiRecognitionTask: AI 内容识别类型任务参数。
 注意：此字段可能返回 null，表示取不到有效值。
         :type AiRecognitionTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskInput`
+        :param MiniProgramPublishTask: 微信小程序发布任务参数。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type MiniProgramPublishTask: :class:`tencentcloud.vod.v20180717.models.WechatMiniProgramPublishTaskInput`
         :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
         :type CreateTime: str
         :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
         :type UpdateTime: str
         """
         self.Name = None
         self.Type = None
         self.MediaProcessTask = None
         self.AiContentReviewTask = None
         self.AiAnalysisTask = None
         self.AiRecognitionTask = None
+        self.MiniProgramPublishTask = None
         self.CreateTime = None
         self.UpdateTime = None
 
 
     def _deserialize(self, params):
         self.Name = params.get("Name")
         self.Type = params.get("Type")
@@ -11957,14 +11961,17 @@
             self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
         if params.get("AiAnalysisTask") is not None:
             self.AiAnalysisTask = AiAnalysisTaskInput()
             self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
         if params.get("AiRecognitionTask") is not None:
             self.AiRecognitionTask = AiRecognitionTaskInput()
             self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
+        if params.get("MiniProgramPublishTask") is not None:
+            self.MiniProgramPublishTask = WechatMiniProgramPublishTaskInput()
+            self.MiniProgramPublishTask._deserialize(params.get("MiniProgramPublishTask"))
         self.CreateTime = params.get("CreateTime")
         self.UpdateTime = params.get("UpdateTime")
 
 
 class ProcessMediaByProcedureRequest(AbstractModel):
     """ProcessMediaByProcedure请求参数结构体
 
@@ -12114,15 +12121,15 @@
 class ProcessMediaRequest(AbstractModel):
     """ProcessMedia请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param FileId: 媒体文件 ID。
+        :param FileId: 媒体文件 ID，即该文件在云点播上的全局唯一标识符，在上传成功后由云点播后台分配。可以在 [视频上传完成事件通知](/document/product/266/7830) 或 [云点播控制台](https://console.cloud.tencent.com/vod/media) 获取该字段。
         :type FileId: str
         :param MediaProcessTask: 视频处理类型任务参数。
         :type MediaProcessTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskInput`
         :param AiContentReviewTask: 视频内容审核类型任务参数。
         :type AiContentReviewTask: :class:`tencentcloud.vod.v20180717.models.AiContentReviewTaskInput`
         :param AiAnalysisTask: 视频内容分析类型任务参数。
         :type AiAnalysisTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskInput`
@@ -13116,22 +13123,33 @@
 <li>当字符串以 W% 结尾，表示水印 Height 为视频宽度的百分比大小，如 10W% 表示 Height 为视频宽度的 10%；</li>
 <li>当字符串以 H% 结尾，表示水印 Height 为视频高度的百分比大小，如 10H% 表示 Height 为视频高度的 10%；</li>
 <li>当字符串以 S% 结尾，表示水印 Height 为视频短边的百分比大小，如 10S% 表示 Height 为视频短边的 10%；</li>
 <li>当字符串以 L% 结尾，表示水印 Height 为视频长边的百分比大小，如 10L% 表示 Height 为视频长边的 10%；</li>
 <li>当字符串以 % 结尾时，含义同 H%。
 默认值为 0px。
         :type Height: str
+        :param CycleConfig: 水印周期配置，用于配置水印周期性地显示与隐藏。
+主要使用场景是：为了视频防遮标，在视频多个地方设置水印，这些水印按固定顺序周期性地显示与隐藏。
+比如，设置 A、B、C、D 4 个水印分别位于视频的左上角、右上角、右下角、左下角处，视频开始时，{ A 显示 5 秒 -> B 显示 5 秒 -> C 显示 5 秒 -> D 显示 5 秒 } -> A 显示 5 秒 -> B 显示 5 秒 -> ...，任何时刻只显示一处水印。
+花括号 {} 表示由 A、B、C、D 4 个水印组成的大周期，可以看出每个大周期持续 20 秒。
+可以看出，A、B、C、D 都是周期性地显示 5 秒、隐藏 15 秒，且四者有固定的显示顺序。
+此配置项即用来描述单个水印的周期配置。
+        :type CycleConfig: :class:`tencentcloud.vod.v20180717.models.WatermarkCycleConfigForUpdate`
         """
         self.Width = None
         self.Height = None
+        self.CycleConfig = None
 
 
     def _deserialize(self, params):
         self.Width = params.get("Width")
         self.Height = params.get("Height")
+        if params.get("CycleConfig") is not None:
+            self.CycleConfig = WatermarkCycleConfigForUpdate()
+            self.CycleConfig._deserialize(params.get("CycleConfig"))
 
 
 class TEHDConfig(AbstractModel):
     """极速高清参数配置。
 
     """
 
@@ -14283,14 +14301,40 @@
         self.Width = params.get("Width")
         self.Height = params.get("Height")
         self.FillType = params.get("FillType")
         self.CreateTime = params.get("CreateTime")
         self.UpdateTime = params.get("UpdateTime")
 
 
+class WatermarkCycleConfigForUpdate(AbstractModel):
+    """水印周期配置。
+
+    """
+
+    def __init__(self):
+        """
+        :param StartTime: 水印在视频里第一次出现的播放时间点，单位：秒。
+        :type StartTime: float
+        :param DisplayDuration: 在一个水印周期内，水印显示的持续时间，单位：秒。
+        :type DisplayDuration: float
+        :param CycleDuration: 一个水印周期的持续时间，单位：秒。
+填 0 表示水印只持续一个水印周期（即在整个视频里只显示 DisplayDuration 秒）。
+        :type CycleDuration: float
+        """
+        self.StartTime = None
+        self.DisplayDuration = None
+        self.CycleDuration = None
+
+
+    def _deserialize(self, params):
+        self.StartTime = params.get("StartTime")
+        self.DisplayDuration = params.get("DisplayDuration")
+        self.CycleDuration = params.get("CycleDuration")
+
+
 class WatermarkInput(AbstractModel):
     """视频处理任务中的水印参数类型
 
     """
 
     def __init__(self):
         """
@@ -14486,14 +14530,31 @@
         self.ErrCode = params.get("ErrCode")
         self.Message = params.get("Message")
         self.FileId = params.get("FileId")
         self.SourceDefinition = params.get("SourceDefinition")
         self.PublishResult = params.get("PublishResult")
 
 
+class WechatMiniProgramPublishTaskInput(AbstractModel):
+    """微信小程序发布任务类型
+
+    """
+
+    def __init__(self):
+        """
+        :param SourceDefinition: 发布视频所对应的转码模板 ID，为 0 代表原始视频。
+        :type SourceDefinition: int
+        """
+        self.SourceDefinition = None
+
+
+    def _deserialize(self, params):
+        self.SourceDefinition = params.get("SourceDefinition")
+
+
 class WechatPublishTask(AbstractModel):
     """微信发布任务信息
 
     """
 
     def __init__(self):
         """
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/mongodb/v20180408/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/mongodb/v20180408/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/mongodb/v20180408/mongodb_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/mongodb/v20180408/mongodb_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cim/v20190318/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cim/v20190318/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cim/v20190318/cim_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cim/v20190318/cim_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/wss/v20180426/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/wss/v20180426/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/wss/v20180426/wss_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/wss/v20180426/wss_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/common/exception/tencent_cloud_sdk_exception.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/common/exception/tencent_cloud_sdk_exception.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/common/sign.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/common/sign.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/common/abstract_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/common/abstract_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/common/abstract_model.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/common/abstract_model.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/common/profile/http_profile.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/common/profile/http_profile.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/common/profile/client_profile.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/common/profile/client_profile.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/common/http/request.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/common/http/request.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/common/credential.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/common/credential.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/dc/v20180410/dc_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/dc/v20180410/dc_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/dc/v20180410/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/dc/v20180410/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/gme/v20180711/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/nlp/v20190408/models.py`

 * *Files 22% similar despite different names*

```diff
@@ -12,555 +12,917 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 from tencentcloud.common.abstract_model import AbstractModel
 
 
-class DescribeFilterResultListRequest(AbstractModel):
-    """DescribeFilterResultList请求参数结构体
+class AutoSummarizationRequest(AbstractModel):
+    """AutoSummarization请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param BizId: 应用ID
-        :type BizId: int
-        :param StartDate: 开始时间，格式为 年-月-日，如: 2018-07-11
-        :type StartDate: str
-        :param EndDate: 结束时间，格式为 年-月-日，如: 2018-07-11
-        :type EndDate: str
-        :param Offset: 偏移量，默认值为0。
-        :type Offset: int
-        :param Limit: 返回数量，默认值为10，最大值为100。
-        :type Limit: int
+        :param Text: 待处理的文本（仅支持UTF-8格式，不超过2000字）
+        :type Text: str
+        :param Length: 指定摘要的长度（默认值为200）
+注：为保证摘要的可读性，最终生成的摘要长度并不会严格遵循这个值，会有略微的浮动
+        :type Length: int
         """
-        self.BizId = None
-        self.StartDate = None
-        self.EndDate = None
-        self.Offset = None
-        self.Limit = None
+        self.Text = None
+        self.Length = None
 
 
     def _deserialize(self, params):
-        self.BizId = params.get("BizId")
-        self.StartDate = params.get("StartDate")
-        self.EndDate = params.get("EndDate")
-        self.Offset = params.get("Offset")
-        self.Limit = params.get("Limit")
+        self.Text = params.get("Text")
+        self.Length = params.get("Length")
 
 
-class DescribeFilterResultListResponse(AbstractModel):
-    """DescribeFilterResultList返回参数结构体
+class AutoSummarizationResponse(AbstractModel):
+    """AutoSummarization返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TotalCount: 过滤结果总数
-注意：此字段可能返回 null，表示取不到有效值。
-        :type TotalCount: int
-        :param Data: 当前分页过滤结果列表
-注意：此字段可能返回 null，表示取不到有效值。
-        :type Data: list of VoiceFilterInfo
+        :param Summary: 文本摘要结果
+        :type Summary: str
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.TotalCount = None
-        self.Data = None
+        self.Summary = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.TotalCount = params.get("TotalCount")
-        if params.get("Data") is not None:
-            self.Data = []
-            for item in params.get("Data"):
-                obj = VoiceFilterInfo()
-                obj._deserialize(item)
-                self.Data.append(obj)
+        self.Summary = params.get("Summary")
         self.RequestId = params.get("RequestId")
 
 
-class DescribeFilterResultRequest(AbstractModel):
-    """DescribeFilterResult请求参数结构体
+class CCIToken(AbstractModel):
+    """文本纠错结果
+
+    """
+
+    def __init__(self):
+        """
+        :param BeginOffset: 错别字的起始位置，从0开始
+        :type BeginOffset: int
+        :param CorrectWord: 错别字纠错结果
+        :type CorrectWord: str
+        :param Word: 错别字内容
+        :type Word: str
+        """
+        self.BeginOffset = None
+        self.CorrectWord = None
+        self.Word = None
+
+
+    def _deserialize(self, params):
+        self.BeginOffset = params.get("BeginOffset")
+        self.CorrectWord = params.get("CorrectWord")
+        self.Word = params.get("Word")
+
+
+class ClassificationResult(AbstractModel):
+    """文本分类结果
+
+    """
+
+    def __init__(self):
+        """
+        :param FirstClassName: 一级分类名称
+        :type FirstClassName: str
+        :param FirstClassProbability: 一级分类概率
+        :type FirstClassProbability: float
+        :param SecondClassName: 二级分类名称
+        :type SecondClassName: str
+        :param SecondClassProbability: 二级分类概率
+        :type SecondClassProbability: float
+        """
+        self.FirstClassName = None
+        self.FirstClassProbability = None
+        self.SecondClassName = None
+        self.SecondClassProbability = None
+
+
+    def _deserialize(self, params):
+        self.FirstClassName = params.get("FirstClassName")
+        self.FirstClassProbability = params.get("FirstClassProbability")
+        self.SecondClassName = params.get("SecondClassName")
+        self.SecondClassProbability = params.get("SecondClassProbability")
+
+
+class ContentApprovalRequest(AbstractModel):
+    """ContentApproval请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param BizId: 应用ID
-        :type BizId: int
-        :param FileId: 文件ID
-        :type FileId: str
+        :param Text: 待审核的文本（仅支持UTF-8格式，不超过2000字）
+        :type Text: str
         """
-        self.BizId = None
-        self.FileId = None
+        self.Text = None
 
 
     def _deserialize(self, params):
-        self.BizId = params.get("BizId")
-        self.FileId = params.get("FileId")
+        self.Text = params.get("Text")
 
 
-class DescribeFilterResultResponse(AbstractModel):
-    """DescribeFilterResult返回参数结构体
+class ContentApprovalResponse(AbstractModel):
+    """ContentApproval返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Data: 过滤结果
-注意：此字段可能返回 null，表示取不到有效值。
-        :type Data: :class:`tencentcloud.gme.v20180711.models.VoiceFilterInfo`
+        :param EvilFlag: 文本是否恶意：
+0、正常；
+1、恶意；
+2、可疑送审
+        :type EvilFlag: int
+        :param EvilKeywords: 恶意关键词组
+        :type EvilKeywords: list of str
+        :param EvilType: 文本恶意类型：
+0、正常；
+1、政治；
+2、色情；
+3、辱骂/低俗；
+4、暴恐/毒品；
+5、广告/灌水；
+6、迷信/邪教；
+7、其他违法（如跨站追杀/恶意竞争等）；
+8、综合
+        :type EvilType: int
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.Data = None
+        self.EvilFlag = None
+        self.EvilKeywords = None
+        self.EvilType = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        if params.get("Data") is not None:
-            self.Data = VoiceFilterInfo()
-            self.Data._deserialize(params.get("Data"))
+        self.EvilFlag = params.get("EvilFlag")
+        self.EvilKeywords = params.get("EvilKeywords")
+        self.EvilType = params.get("EvilType")
         self.RequestId = params.get("RequestId")
 
 
-class DescribeScanResult(AbstractModel):
-    """语音检测结果返回
+class DependencyParsingRequest(AbstractModel):
+    """DependencyParsing请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param Text: 待分析的文本（仅支持UTF-8格式，不超过200字）
+        :type Text: str
+        """
+        self.Text = None
+
+
+    def _deserialize(self, params):
+        self.Text = params.get("Text")
+
+
+class DependencyParsingResponse(AbstractModel):
+    """DependencyParsing返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Code: 业务返回码
-        :type Code: int
-        :param DataId: 数据唯一 ID
-        :type DataId: str
-        :param ScanFinishTime: 检测完成的时间戳
-        :type ScanFinishTime: int
-        :param HitFlag: 是否违规
-        :type HitFlag: bool
-        :param Live: 是否为流
-        :type Live: bool
-        :param Msg: 业务返回描述
-注意：此字段可能返回 null，表示取不到有效值。
-        :type Msg: str
-        :param ScanPiece: 检测结果，Code 为 0 时返回
-注意：此字段可能返回 null，表示取不到有效值。
-        :type ScanPiece: list of ScanPiece
-        :param ScanStartTime: 提交检测的时间戳
-        :type ScanStartTime: int
-        :param Scenes: 语音检测场景，对应请求时的 Scene
-        :type Scenes: list of str
-        :param TaskId: 语音检测任务 ID，由后台分配
-        :type TaskId: str
-        :param Url: 文件或接流地址
-        :type Url: str
-        :param Status: 检测任务执行结果状态，分别为：
-<li>Start: 任务开始</li>
-<li>Success: 成功结束</li>
-<li>Error: 异常</li>
-        :type Status: str
+        :param DpTokens: 句法依存分析结果，其中句法依存关系的类型包括：
+<li>主谓关系，eg: 我送她一束花 (我 <-- 送)
+<li>动宾关系，eg: 我送她一束花 (送 --> 花)
+<li>间宾关系，eg: 我送她一束花 (送 --> 她)
+<li>前置宾语，eg: 他什么书都读 (书 <-- 读)
+<li>兼语，eg: 他请我吃饭 (请 --> 我)
+<li>定中关系，eg: 红苹果 (红 <-- 苹果)
+<li>状中结构，eg: 非常美丽 (非常 <-- 美丽)
+<li>动补结构，eg: 做完了作业 (做 --> 完)
+<li>并列关系，eg: 大山和大海 (大山 --> 大海)
+<li>介宾关系，eg: 在贸易区内 (在 --> 内)
+<li>左附加关系，eg: 大山和大海 (和 <-- 大海)
+<li>右附加关系，eg: 孩子们 (孩子 --> 们)
+<li>独立结构，eg: 两个单句在结构上彼此独立
+<li>标点符号，eg: 。
+<li>核心关系，eg: 整个句子的核心
+        :type DpTokens: list of DpToken
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
         """
-        self.Code = None
-        self.DataId = None
-        self.ScanFinishTime = None
-        self.HitFlag = None
-        self.Live = None
-        self.Msg = None
-        self.ScanPiece = None
-        self.ScanStartTime = None
-        self.Scenes = None
-        self.TaskId = None
-        self.Url = None
-        self.Status = None
+        self.DpTokens = None
+        self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.Code = params.get("Code")
-        self.DataId = params.get("DataId")
-        self.ScanFinishTime = params.get("ScanFinishTime")
-        self.HitFlag = params.get("HitFlag")
-        self.Live = params.get("Live")
-        self.Msg = params.get("Msg")
-        if params.get("ScanPiece") is not None:
-            self.ScanPiece = []
-            for item in params.get("ScanPiece"):
-                obj = ScanPiece()
+        if params.get("DpTokens") is not None:
+            self.DpTokens = []
+            for item in params.get("DpTokens"):
+                obj = DpToken()
                 obj._deserialize(item)
-                self.ScanPiece.append(obj)
-        self.ScanStartTime = params.get("ScanStartTime")
-        self.Scenes = params.get("Scenes")
-        self.TaskId = params.get("TaskId")
-        self.Url = params.get("Url")
-        self.Status = params.get("Status")
+                self.DpTokens.append(obj)
+        self.RequestId = params.get("RequestId")
+
+
+class DpToken(AbstractModel):
+    """句法依存分析结果，包括基础词，基础词的序号，当前词父节点的序号，句法依存关系的类型
+
+    """
+
+    def __init__(self):
+        """
+        :param HeadId: 当前词父节点的序号
+        :type HeadId: int
+        :param Id: 基础词的序号
+        :type Id: int
+        :param Relation: 句法依存关系的类型
+        :type Relation: str
+        :param Word: 基础词
+        :type Word: str
+        """
+        self.HeadId = None
+        self.Id = None
+        self.Relation = None
+        self.Word = None
+
+
+    def _deserialize(self, params):
+        self.HeadId = params.get("HeadId")
+        self.Id = params.get("Id")
+        self.Relation = params.get("Relation")
+        self.Word = params.get("Word")
+
+
+class EvilToken(AbstractModel):
+    """文本审核结果
+
+    """
+
+    def __init__(self):
+        """
+        :param EvilFlag: 文本是否恶意：
+0、正常；
+1、恶意；
+2、可疑送审
+        :type EvilFlag: int
+        :param EvilKeywords: 恶意关键词组
+        :type EvilKeywords: list of str
+        :param EvilType: 文本恶意类型：
+0、正常；
+1、政治；
+2、色情；
+3、辱骂/低俗；
+4、暴恐/毒品；
+5、广告/灌水；
+6、迷信/邪教；
+7、其他违法（如跨站追杀/恶意竞争等）；
+8、综合
+        :type EvilType: int
+        """
+        self.EvilFlag = None
+        self.EvilKeywords = None
+        self.EvilType = None
+
+
+    def _deserialize(self, params):
+        self.EvilFlag = params.get("EvilFlag")
+        self.EvilKeywords = params.get("EvilKeywords")
+        self.EvilType = params.get("EvilType")
+
+
+class Keyword(AbstractModel):
+    """关键词提取结果
+
+    """
+
+    def __init__(self):
+        """
+        :param Score: 权重
+        :type Score: float
+        :param Word: 关键词
+        :type Word: str
+        """
+        self.Score = None
+        self.Word = None
 
 
-class DescribeScanResultListRequest(AbstractModel):
-    """DescribeScanResultList请求参数结构体
+    def _deserialize(self, params):
+        self.Score = params.get("Score")
+        self.Word = params.get("Word")
+
+
+class KeywordsExtractionRequest(AbstractModel):
+    """KeywordsExtraction请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param BizId: 应用 ID，在控制台统一创建。
-        :type BizId: int
-        :param TaskIdList: 查询的任务 ID 列表，任务 ID 列表最多支持 100 个。
-        :type TaskIdList: list of str
+        :param Text: 待处理的文本（仅支持UTF-8格式，不超过2000字）
+        :type Text: str
+        :param Num: 指定关键词个数上限（默认值为5）
+        :type Num: int
         """
-        self.BizId = None
-        self.TaskIdList = None
+        self.Text = None
+        self.Num = None
 
 
     def _deserialize(self, params):
-        self.BizId = params.get("BizId")
-        self.TaskIdList = params.get("TaskIdList")
+        self.Text = params.get("Text")
+        self.Num = params.get("Num")
 
 
-class DescribeScanResultListResponse(AbstractModel):
-    """DescribeScanResultList返回参数结构体
+class KeywordsExtractionResponse(AbstractModel):
+    """KeywordsExtraction返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Data: 要查询的语音检测任务的结果
-注意：此字段可能返回 null，表示取不到有效值。
-        :type Data: list of DescribeScanResult
+        :param Keywords: 关键词提取结果
+        :type Keywords: list of Keyword
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.Data = None
+        self.Keywords = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        if params.get("Data") is not None:
-            self.Data = []
-            for item in params.get("Data"):
-                obj = DescribeScanResult()
+        if params.get("Keywords") is not None:
+            self.Keywords = []
+            for item in params.get("Keywords"):
+                obj = Keyword()
                 obj._deserialize(item)
-                self.Data.append(obj)
+                self.Keywords.append(obj)
         self.RequestId = params.get("RequestId")
 
 
-class ScanDetail(AbstractModel):
-    """语音检测详情
+class LexicalAnalysisRequest(AbstractModel):
+    """LexicalAnalysis请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Label: 违规场景，参照Label定义
-        :type Label: str
-        :param Rate: 该场景下概率[0.00,100.00],分值越大违规概率越高
-        :type Rate: str
-        :param KeyWord: 违规关键字
-        :type KeyWord: str
-        :param StartTime: 关键字在音频的开始时间，从0开始的偏移量，单位为毫秒
-        :type StartTime: int
-        :param EndTime: 关键字在音频的结束时间，从0开始的偏移量,，单位为毫秒
-        :type EndTime: int
+        :param Text: 待分析的文本（仅支持UTF-8格式，不超过500字）
+        :type Text: str
+        :param Flag: 词法分析模式（默认取1值）：
+1、高精度（具备混合粒度分词能力）；
+2、高性能；
+        :type Flag: int
         """
-        self.Label = None
-        self.Rate = None
-        self.KeyWord = None
-        self.StartTime = None
-        self.EndTime = None
+        self.Text = None
+        self.Flag = None
 
 
     def _deserialize(self, params):
-        self.Label = params.get("Label")
-        self.Rate = params.get("Rate")
-        self.KeyWord = params.get("KeyWord")
-        self.StartTime = params.get("StartTime")
-        self.EndTime = params.get("EndTime")
+        self.Text = params.get("Text")
+        self.Flag = params.get("Flag")
 
 
-class ScanPiece(AbstractModel):
-    """语音检测结果，Code 为 0 时返回
+class LexicalAnalysisResponse(AbstractModel):
+    """LexicalAnalysis返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param DumpUrl: 流检测时返回，音频转存地址，保留30min
-注意：此字段可能返回 null，表示取不到有效值。
-        :type DumpUrl: str
-        :param HitFlag: 是否违规
-        :type HitFlag: bool
-        :param MainType: 违规主要类型
-注意：此字段可能返回 null，表示取不到有效值。
-        :type MainType: str
-        :param ScanDetail: 语音检测详情
-        :type ScanDetail: list of ScanDetail
-        :param RoomId: gme实时语音房间id，透传任务传入时的RoomId
-注意：此字段可能返回 null，表示取不到有效值。
-        :type RoomId: str
-        :param OpenId: gme实时语音用户id，透传任务传入时的OpenId
-注意：此字段可能返回 null，表示取不到有效值。
-        :type OpenId: str
+        :param NerTokens: 命名实体识别结果。取值范围：
+<li>PER：表示人名</li>
+<li>LOC：表示地名</li>
+<li>ORG：表示机构团体名</li>
+        :type NerTokens: list of NerToken
+        :param PosTokens: 分词&词性标注结果（词性表请参见附录）
+        :type PosTokens: list of PosToken
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
         """
-        self.DumpUrl = None
-        self.HitFlag = None
-        self.MainType = None
-        self.ScanDetail = None
-        self.RoomId = None
-        self.OpenId = None
+        self.NerTokens = None
+        self.PosTokens = None
+        self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.DumpUrl = params.get("DumpUrl")
-        self.HitFlag = params.get("HitFlag")
-        self.MainType = params.get("MainType")
-        if params.get("ScanDetail") is not None:
-            self.ScanDetail = []
-            for item in params.get("ScanDetail"):
-                obj = ScanDetail()
+        if params.get("NerTokens") is not None:
+            self.NerTokens = []
+            for item in params.get("NerTokens"):
+                obj = NerToken()
+                obj._deserialize(item)
+                self.NerTokens.append(obj)
+        if params.get("PosTokens") is not None:
+            self.PosTokens = []
+            for item in params.get("PosTokens"):
+                obj = PosToken()
                 obj._deserialize(item)
-                self.ScanDetail.append(obj)
-        self.RoomId = params.get("RoomId")
-        self.OpenId = params.get("OpenId")
+                self.PosTokens.append(obj)
+        self.RequestId = params.get("RequestId")
 
 
-class ScanVoiceRequest(AbstractModel):
-    """ScanVoice请求参数结构体
+class NerToken(AbstractModel):
+    """命名实体识别结果
 
     """
 
     def __init__(self):
         """
-        :param BizId: 应用ID，登录控制台创建应用得到的AppID。
-        :type BizId: int
-        :param Scenes: 语音检测场景，参数值目前要求为 default。 预留场景设置： 谩骂、色情、涉政、广告、暴恐、违禁等场景，<a href="#Label_Value">具体取值见上述 Label 说明。</a>
-        :type Scenes: list of str
-        :param Live: 是否为直播流。值为 false 时表示普通语音文件检测；为 true 时表示语音流检测。
-        :type Live: bool
-        :param Tasks: 语音检测任务列表，列表最多支持100个检测任务。结构体中包含：
-<li>DataId：数据的唯一ID</li>
-<li>Url：数据文件的url，为 urlencode 编码，流式则为拉流地址</li>
-        :type Tasks: list of Task
-        :param Callback: 异步检测结果回调地址，具体见上述<a href="#Callback_Declare">回调相关说明</a>。（说明：该字段为空时，必须通过接口(查询语音检测结果)获取检测结果）。
-        :type Callback: str
+        :param BeginOffset: 起始位置
+        :type BeginOffset: int
+        :param Length: 长度
+        :type Length: int
+        :param Type: 命名实体类型
+        :type Type: str
+        :param Word: 基础词
+        :type Word: str
         """
-        self.BizId = None
-        self.Scenes = None
-        self.Live = None
-        self.Tasks = None
-        self.Callback = None
+        self.BeginOffset = None
+        self.Length = None
+        self.Type = None
+        self.Word = None
 
 
     def _deserialize(self, params):
-        self.BizId = params.get("BizId")
-        self.Scenes = params.get("Scenes")
-        self.Live = params.get("Live")
-        if params.get("Tasks") is not None:
-            self.Tasks = []
-            for item in params.get("Tasks"):
-                obj = Task()
-                obj._deserialize(item)
-                self.Tasks.append(obj)
-        self.Callback = params.get("Callback")
+        self.BeginOffset = params.get("BeginOffset")
+        self.Length = params.get("Length")
+        self.Type = params.get("Type")
+        self.Word = params.get("Word")
+
+
+class PosToken(AbstractModel):
+    """分词&词性标注结果
+
+    """
+
+    def __init__(self):
+        """
+        :param BeginOffset: 起始位置
+        :type BeginOffset: int
+        :param Length: 长度
+        :type Length: int
+        :param Pos: 词性
+        :type Pos: str
+        :param Word: 基础词
+        :type Word: str
+        """
+        self.BeginOffset = None
+        self.Length = None
+        self.Pos = None
+        self.Word = None
+
+
+    def _deserialize(self, params):
+        self.BeginOffset = params.get("BeginOffset")
+        self.Length = params.get("Length")
+        self.Pos = params.get("Pos")
+        self.Word = params.get("Word")
+
+
+class SensitiveWordsRecognitionRequest(AbstractModel):
+    """SensitiveWordsRecognition请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param Text: 待识别的文本（仅支持UTF-8格式，不超过2000字）
+        :type Text: str
+        """
+        self.Text = None
+
+
+    def _deserialize(self, params):
+        self.Text = params.get("Text")
+
+
+class SensitiveWordsRecognitionResponse(AbstractModel):
+    """SensitiveWordsRecognition返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param SensitiveWords: 敏感词数组
+        :type SensitiveWords: list of str
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.SensitiveWords = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.SensitiveWords = params.get("SensitiveWords")
+        self.RequestId = params.get("RequestId")
+
+
+class SentenceEmbeddingRequest(AbstractModel):
+    """SentenceEmbedding请求参数结构体
+
+    """
 
+    def __init__(self):
+        """
+        :param Text: 输入的文本（仅支持UTF-8格式，不超过500字）
+        :type Text: str
+        """
+        self.Text = None
 
-class ScanVoiceResponse(AbstractModel):
-    """ScanVoice返回参数结构体
+
+    def _deserialize(self, params):
+        self.Text = params.get("Text")
+
+
+class SentenceEmbeddingResponse(AbstractModel):
+    """SentenceEmbedding返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Data: 语音检测返回。Data 字段是 JSON 数组，每一个元素包含：<li>DataId： 请求中对应的 DataId。</li>
-<li>TaskID ：该检测任务的 ID，用于轮询语音检测结果。</li>
-        :type Data: list of ScanVoiceResult
+        :param Dimension: 句向量的维度
+        :type Dimension: int
+        :param Vector: 句向量数组
+        :type Vector: list of float
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.Data = None
+        self.Dimension = None
+        self.Vector = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        if params.get("Data") is not None:
-            self.Data = []
-            for item in params.get("Data"):
-                obj = ScanVoiceResult()
+        self.Dimension = params.get("Dimension")
+        self.Vector = params.get("Vector")
+        self.RequestId = params.get("RequestId")
+
+
+class SentenceSimilarityRequest(AbstractModel):
+    """SentenceSimilarity请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param SrcText: 计算相似度的源句子（仅支持UTF-8格式，不超过500字）
+        :type SrcText: str
+        :param TargetText: 计算相似度的目标句子（仅支持UTF-8格式，不超过500字）
+        :type TargetText: str
+        """
+        self.SrcText = None
+        self.TargetText = None
+
+
+    def _deserialize(self, params):
+        self.SrcText = params.get("SrcText")
+        self.TargetText = params.get("TargetText")
+
+
+class SentenceSimilarityResponse(AbstractModel):
+    """SentenceSimilarity返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param Similarity: 两个文本的相似度
+        :type Similarity: float
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.Similarity = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.Similarity = params.get("Similarity")
+        self.RequestId = params.get("RequestId")
+
+
+class SentimentAnalysisRequest(AbstractModel):
+    """SentimentAnalysis请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param Text: 待分析的文本（仅支持UTF-8格式，不超过200字）
+        :type Text: str
+        :param Flag: 文本所属类型（默认取4值）：
+1、电商
+2、APP
+3、美食
+4、酒店和其他
+        :type Flag: int
+        """
+        self.Text = None
+        self.Flag = None
+
+
+    def _deserialize(self, params):
+        self.Text = params.get("Text")
+        self.Flag = params.get("Flag")
+
+
+class SentimentAnalysisResponse(AbstractModel):
+    """SentimentAnalysis返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param Negative: 负面情感概率
+        :type Negative: float
+        :param Positive: 正面情感概率
+        :type Positive: float
+        :param Sentiment: 情感属性
+        :type Sentiment: str
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.Negative = None
+        self.Positive = None
+        self.Sentiment = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.Negative = params.get("Negative")
+        self.Positive = params.get("Positive")
+        self.Sentiment = params.get("Sentiment")
+        self.RequestId = params.get("RequestId")
+
+
+class SimilarWordsRequest(AbstractModel):
+    """SimilarWords请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param Text: 输入的词语（仅支持UTF-8格式，不超过20字）
+        :type Text: str
+        :param WordNumber: 相似词个数；取值范围：1-200，默认为10；
+        :type WordNumber: int
+        """
+        self.Text = None
+        self.WordNumber = None
+
+
+    def _deserialize(self, params):
+        self.Text = params.get("Text")
+        self.WordNumber = params.get("WordNumber")
+
+
+class SimilarWordsResponse(AbstractModel):
+    """SimilarWords返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param SimilarWords: 相似词数组
+        :type SimilarWords: list of str
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.SimilarWords = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.SimilarWords = params.get("SimilarWords")
+        self.RequestId = params.get("RequestId")
+
+
+class TextApprovalRequest(AbstractModel):
+    """TextApproval请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param Text: 待审核的文本（仅支持UTF-8格式，不超过2000字）
+        :type Text: str
+        :param Flag: 文本审核模式（默认取1值）：
+1、全领域审核
+        :type Flag: int
+        """
+        self.Text = None
+        self.Flag = None
+
+
+    def _deserialize(self, params):
+        self.Text = params.get("Text")
+        self.Flag = params.get("Flag")
+
+
+class TextApprovalResponse(AbstractModel):
+    """TextApproval返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param EvilTokens: 文本审核输出结果
+        :type EvilTokens: list of EvilToken
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.EvilTokens = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        if params.get("EvilTokens") is not None:
+            self.EvilTokens = []
+            for item in params.get("EvilTokens"):
+                obj = EvilToken()
                 obj._deserialize(item)
-                self.Data.append(obj)
+                self.EvilTokens.append(obj)
         self.RequestId = params.get("RequestId")
 
 
-class ScanVoiceResult(AbstractModel):
-    """语音检测返回结果
+class TextClassificationRequest(AbstractModel):
+    """TextClassification请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param DataId: 数据ID
-        :type DataId: str
-        :param TaskId: 任务ID
-        :type TaskId: str
+        :param Text: 待分类的文本（仅支持UTF-8格式，不超过2000字）
+        :type Text: str
+        :param Flag: 领域分类体系（默认取1值）：
+1、通用领域
+2、新闻领域
+        :type Flag: int
         """
-        self.DataId = None
-        self.TaskId = None
+        self.Text = None
+        self.Flag = None
 
 
     def _deserialize(self, params):
-        self.DataId = params.get("DataId")
-        self.TaskId = params.get("TaskId")
+        self.Text = params.get("Text")
+        self.Flag = params.get("Flag")
 
 
-class Task(AbstractModel):
-    """语音检测任务列表
+class TextClassificationResponse(AbstractModel):
+    """TextClassification返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param DataId: 数据的唯一ID
-        :type DataId: str
-        :param Url: 数据文件的url，为 urlencode 编码，流式则为拉流地址
-        :type Url: str
-        :param RoomId: gme实时语音房间id，通过gme实时语音进行语音分析时输入
-        :type RoomId: str
-        :param OpenId: gme实时语音用户id，通过gme实时语音进行语音分析时输入
-        :type OpenId: str
+        :param Classes: 文本分类结果（文本分类映射表请参见附录）
+        :type Classes: list of ClassificationResult
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
         """
-        self.DataId = None
-        self.Url = None
-        self.RoomId = None
-        self.OpenId = None
+        self.Classes = None
+        self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.DataId = params.get("DataId")
-        self.Url = params.get("Url")
-        self.RoomId = params.get("RoomId")
-        self.OpenId = params.get("OpenId")
+        if params.get("Classes") is not None:
+            self.Classes = []
+            for item in params.get("Classes"):
+                obj = ClassificationResult()
+                obj._deserialize(item)
+                self.Classes.append(obj)
+        self.RequestId = params.get("RequestId")
 
 
-class VoiceFilter(AbstractModel):
-    """过滤结果
+class TextCorrectionRequest(AbstractModel):
+    """TextCorrection请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Type: 过滤类型，1：政治，2：色情，3：涉毒，4：谩骂
-注意：此字段可能返回 null，表示取不到有效值。
-        :type Type: int
-        :param Word: 过滤命中关键词
-注意：此字段可能返回 null，表示取不到有效值。
-        :type Word: str
+        :param Text: 待纠错的文本（仅支持UTF-8格式，不超过2000字）
+        :type Text: str
         """
-        self.Type = None
-        self.Word = None
+        self.Text = None
 
 
     def _deserialize(self, params):
-        self.Type = params.get("Type")
-        self.Word = params.get("Word")
+        self.Text = params.get("Text")
 
 
-class VoiceFilterInfo(AbstractModel):
-    """语音文件过滤详情
+class TextCorrectionResponse(AbstractModel):
+    """TextCorrection返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param BizId: 应用id
-注意：此字段可能返回 null，表示取不到有效值。
-        :type BizId: int
-        :param FileId: 文件id，表示文件唯一id
-注意：此字段可能返回 null，表示取不到有效值。
-        :type FileId: str
-        :param FileName: 文件名
-注意：此字段可能返回 null，表示取不到有效值。
-        :type FileName: str
-        :param OpenId: 用户id
-注意：此字段可能返回 null，表示取不到有效值。
-        :type OpenId: str
-        :param Timestamp: 数据创建时间
-注意：此字段可能返回 null，表示取不到有效值。
-        :type Timestamp: str
-        :param Data: 过滤结果列表
-注意：此字段可能返回 null，表示取不到有效值。
-        :type Data: list of VoiceFilter
-        """
-        self.BizId = None
-        self.FileId = None
-        self.FileName = None
-        self.OpenId = None
-        self.Timestamp = None
-        self.Data = None
+        :param CCITokens: 纠错详情
+        :type CCITokens: list of CCIToken
+        :param ResultText: 纠错后的文本
+        :type ResultText: str
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.CCITokens = None
+        self.ResultText = None
+        self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.BizId = params.get("BizId")
-        self.FileId = params.get("FileId")
-        self.FileName = params.get("FileName")
-        self.OpenId = params.get("OpenId")
-        self.Timestamp = params.get("Timestamp")
-        if params.get("Data") is not None:
-            self.Data = []
-            for item in params.get("Data"):
-                obj = VoiceFilter()
+        if params.get("CCITokens") is not None:
+            self.CCITokens = []
+            for item in params.get("CCITokens"):
+                obj = CCIToken()
                 obj._deserialize(item)
-                self.Data.append(obj)
+                self.CCITokens.append(obj)
+        self.ResultText = params.get("ResultText")
+        self.RequestId = params.get("RequestId")
+
+
+class WordEmbeddingRequest(AbstractModel):
+    """WordEmbedding请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param Text: 输入的词语（仅支持UTF-8格式，不超过20字）
+        :type Text: str
+        """
+        self.Text = None
+
+
+    def _deserialize(self, params):
+        self.Text = params.get("Text")
+
+
+class WordEmbeddingResponse(AbstractModel):
+    """WordEmbedding返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param Dimension: 词向量的维度
+        :type Dimension: int
+        :param Vector: 词向量数组
+        :type Vector: list of float
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.Dimension = None
+        self.Vector = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.Dimension = params.get("Dimension")
+        self.Vector = params.get("Vector")
+        self.RequestId = params.get("RequestId")
 
 
-class VoiceFilterRequest(AbstractModel):
-    """VoiceFilter请求参数结构体
+class WordSimilarityRequest(AbstractModel):
+    """WordSimilarity请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param BizId: 应用ID，登录[控制台](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID
-        :type BizId: int
-        :param FileId: 文件ID，表示文件唯一ID
-        :type FileId: str
-        :param FileName: 文件名
-        :type FileName: str
-        :param FileUrl: 文件url，urlencode编码，FileUrl和FileContent二选一
-        :type FileUrl: str
-        :param FileContent: 文件内容，base64编码，FileUrl和FileContent二选一
-        :type FileContent: str
-        :param OpenId: 用户ID
-        :type OpenId: str
+        :param SrcWord: 计算相似度的源词（仅支持UTF-8格式，不超过20字）
+        :type SrcWord: str
+        :param TargetWord: 计算相似度的目标词（仅支持UTF-8格式，不超过20字）
+        :type TargetWord: str
         """
-        self.BizId = None
-        self.FileId = None
-        self.FileName = None
-        self.FileUrl = None
-        self.FileContent = None
-        self.OpenId = None
+        self.SrcWord = None
+        self.TargetWord = None
 
 
     def _deserialize(self, params):
-        self.BizId = params.get("BizId")
-        self.FileId = params.get("FileId")
-        self.FileName = params.get("FileName")
-        self.FileUrl = params.get("FileUrl")
-        self.FileContent = params.get("FileContent")
-        self.OpenId = params.get("OpenId")
+        self.SrcWord = params.get("SrcWord")
+        self.TargetWord = params.get("TargetWord")
 
 
-class VoiceFilterResponse(AbstractModel):
-    """VoiceFilter返回参数结构体
+class WordSimilarityResponse(AbstractModel):
+    """WordSimilarity返回参数结构体
 
     """
 
     def __init__(self):
         """
+        :param Similarity: 两个词语的相似度
+        :type Similarity: float
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
+        self.Similarity = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
+        self.Similarity = params.get("Similarity")
         self.RequestId = params.get("RequestId")
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/gme/v20180711/gme_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/gme/v20180711/gme_client.py`

 * *Files 25% similar despite different names*

```diff
@@ -21,14 +21,70 @@
 
 
 class GmeClient(AbstractClient):
     _apiVersion = '2018-07-11'
     _endpoint = 'gme.tencentcloudapi.com'
 
 
+    def CreateApp(self, request):
+        """本接口(CreateApp)用于创建一个GME应用
+
+        :param request: 调用CreateApp所需参数的结构体。
+        :type request: :class:`tencentcloud.gme.v20180711.models.CreateAppRequest`
+        :rtype: :class:`tencentcloud.gme.v20180711.models.CreateAppResponse`
+
+        """
+        try:
+            params = request._serialize()
+            body = self.call("CreateApp", params)
+            response = json.loads(body)
+            if "Error" not in response["Response"]:
+                model = models.CreateAppResponse()
+                model._deserialize(response["Response"])
+                return model
+            else:
+                code = response["Response"]["Error"]["Code"]
+                message = response["Response"]["Error"]["Message"]
+                reqid = response["Response"]["RequestId"]
+                raise TencentCloudSDKException(code, message, reqid)
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
+    def DescribeAppStatistics(self, request):
+        """本接口(DescribeAppStatistics)用户获取某个GME应用的用量数据。包括实时语音，离线语音，语音过滤等。最长查询周期为最近30天。
+
+        :param request: 调用DescribeAppStatistics所需参数的结构体。
+        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeAppStatisticsRequest`
+        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeAppStatisticsResponse`
+
+        """
+        try:
+            params = request._serialize()
+            body = self.call("DescribeAppStatistics", params)
+            response = json.loads(body)
+            if "Error" not in response["Response"]:
+                model = models.DescribeAppStatisticsResponse()
+                model._deserialize(response["Response"])
+                return model
+            else:
+                code = response["Response"]["Error"]["Code"]
+                message = response["Response"]["Error"]["Message"]
+                reqid = response["Response"]["RequestId"]
+                raise TencentCloudSDKException(code, message, reqid)
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
     def DescribeFilterResult(self, request):
         """根据应用ID和文件ID查询识别结果
 
         :param request: 调用DescribeFilterResult所需参数的结构体。
         :type request: :class:`tencentcloud.gme.v20180711.models.DescribeFilterResultRequest`
         :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeFilterResultResponse`
 
@@ -106,17 +162,50 @@
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
+    def ModifyAppStatus(self, request):
+        """本接口(ModifyAppStatus)用于修改应用总开关状态。
+
+        :param request: 调用ModifyAppStatus所需参数的结构体。
+        :type request: :class:`tencentcloud.gme.v20180711.models.ModifyAppStatusRequest`
+        :rtype: :class:`tencentcloud.gme.v20180711.models.ModifyAppStatusResponse`
+
+        """
+        try:
+            params = request._serialize()
+            body = self.call("ModifyAppStatus", params)
+            response = json.loads(body)
+            if "Error" not in response["Response"]:
+                model = models.ModifyAppStatusResponse()
+                model._deserialize(response["Response"])
+                return model
+            else:
+                code = response["Response"]["Error"]["Code"]
+                message = response["Response"]["Error"]["Message"]
+                reqid = response["Response"]["RequestId"]
+                raise TencentCloudSDKException(code, message, reqid)
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
     def ScanVoice(self, request):
-        """本接口(ScanVoice)用于提交语音检测任务，检测任务列表最多支持100个。
+        """本接口(ScanVoice)用于提交语音检测任务，检测任务列表最多支持100个。使用前请您登录[控制台 - 服务配置](https://console.cloud.tencent.com/gamegme/conf)开启语音分析服务。
         </br></br>
+
+        <h4><b>功能试用说明：</b></h4>
+        <li>打开前往<a href="https://console.cloud.tencent.com/gamegme/tryout">控制台 - 产品试用</a>免费试用语音分析服务。</li>
+        </br>
+
         <h4><b>接口功能说明：</b></h4>
         <li>支持对语音流或语音文件进行检测，判断其中是否包含违规内容。</li>
         <li>支持设置回调地址 Callback 获取检测结果，同时支持通过接口(查询语音检测结果)主动轮询获取检测结果。</li>
         <li>支持场景输入，包括：谩骂、色情、涉政等场景</li>
         <li>支持批量提交检测任务。检测任务列表最多支持100个。</li>
         </br>
         <h4><b>音频文件限制说明：</b></h4>
@@ -148,15 +237,15 @@
         <p>normal:正常文本</p>
         <p>porn:色情</p>
         <p>politics:涉政</p>
         <p>abuse:谩骂</p>
         <p>ad :广告</p>
         <p>terrorism:暴恐</p>
         <p>contraband :违禁</p>
-        <p>customized:自定义词库</p>
+        <p>customized:自定义词库。目前白名单开放，如有需要请<a href="https://cloud.tencent.com/apply/p/8809fjcik56">联系我们</a>。</p>
         </td>
         </tr>
         </tbody>
         </table>
         </br>
         <h4 id="Callback_Declare"><b>回调相关说明：</b></h4>
         <li>如果在请求参数中指定了回调地址参数 Callback，即一个 HTTP(S) 协议接口的 URL，则需要支持 POST 方法，传输数据编码采用 UTF-8。</li>
@@ -185,35 +274,30 @@
         	<ul>
         		<li>使用 HMAC-SH1 算法, 最终结果做 BASE64 编码;</li>
         		<li>签名原文串为 POST+body 的整个json内容(长度以 Content-Length 为准);</li>
         		<li>签名key为应用的 secrectkey，可以通过控制台查看。</li>
         	</ul>
         </ul>
 
-        <ul>
-        <li>
-        回调请求 Body 的字段说明见结构：
-        <a href="https://cloud.tencent.com/document/api/607/35375#DescribeScanResult" target="_blank">DescribeScanResult</a>
-        </li>
-        </ul>
-
-        <li>回调示例如下<font color="red">（详细字段说明见上述表格中 Data 字段说明）</font>：</li>
+        <li>回调示例如下<font color="red">（详细字段说明见结构：
+        <a href="https://cloud.tencent.com/document/api/607/35375#DescribeScanResult" target="_blank">DescribeScanResult</a>）</font>：</li>
         <pre><code>{
         	"Code": 0,
         	"DataId": "1400000000_test_data_id",
         	"ScanFinishTime": 1566720906,
         	"HitFlag": true,
         	"Live": false,
         	"Msg": "",
         	"ScanPiece": [{
         		"DumpUrl": "",
         		"HitFlag": true,
         		"MainType": "abuse",
         		"RoomId": "123",
         		"OpenId": "xxx",
+        		"Info":"",
         		"ScanDetail": [{
         			"EndTime": 1110,
         			"KeyWord": "xxx",
         			"Label": "abuse",
         			"Rate": "90.00",
         			"StartTime": 1110
         		}, {
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/nlp/v20190408/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tag/v20180813/models.py`

 * *Files 24% similar despite different names*

```diff
@@ -12,917 +12,775 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 from tencentcloud.common.abstract_model import AbstractModel
 
 
-class AutoSummarizationRequest(AbstractModel):
-    """AutoSummarization请求参数结构体
+class AddResourceTagRequest(AbstractModel):
+    """AddResourceTag请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Text: 待处理的文本（仅支持UTF-8格式，不超过2000字）
-        :type Text: str
-        :param Length: 指定摘要的长度（默认值为200）
-注：为保证摘要的可读性，最终生成的摘要长度并不会严格遵循这个值，会有略微的浮动
-        :type Length: int
+        :param TagKey: 标签键
+        :type TagKey: str
+        :param TagValue: 标签值
+        :type TagValue: str
+        :param Resource: 资源六段式描述
+        :type Resource: str
         """
-        self.Text = None
-        self.Length = None
+        self.TagKey = None
+        self.TagValue = None
+        self.Resource = None
 
 
     def _deserialize(self, params):
-        self.Text = params.get("Text")
-        self.Length = params.get("Length")
+        self.TagKey = params.get("TagKey")
+        self.TagValue = params.get("TagValue")
+        self.Resource = params.get("Resource")
 
 
-class AutoSummarizationResponse(AbstractModel):
-    """AutoSummarization返回参数结构体
+class AddResourceTagResponse(AbstractModel):
+    """AddResourceTag返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Summary: 文本摘要结果
-        :type Summary: str
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.Summary = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.Summary = params.get("Summary")
         self.RequestId = params.get("RequestId")
 
 
-class CCIToken(AbstractModel):
-    """文本纠错结果
+class CreateTagRequest(AbstractModel):
+    """CreateTag请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param BeginOffset: 错别字的起始位置，从0开始
-        :type BeginOffset: int
-        :param CorrectWord: 错别字纠错结果
-        :type CorrectWord: str
-        :param Word: 错别字内容
-        :type Word: str
+        :param TagKey: 标签键
+        :type TagKey: str
+        :param TagValue: 标签值
+        :type TagValue: str
         """
-        self.BeginOffset = None
-        self.CorrectWord = None
-        self.Word = None
+        self.TagKey = None
+        self.TagValue = None
 
 
     def _deserialize(self, params):
-        self.BeginOffset = params.get("BeginOffset")
-        self.CorrectWord = params.get("CorrectWord")
-        self.Word = params.get("Word")
+        self.TagKey = params.get("TagKey")
+        self.TagValue = params.get("TagValue")
 
 
-class ClassificationResult(AbstractModel):
-    """文本分类结果
+class CreateTagResponse(AbstractModel):
+    """CreateTag返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param FirstClassName: 一级分类名称
-        :type FirstClassName: str
-        :param FirstClassProbability: 一级分类概率
-        :type FirstClassProbability: float
-        :param SecondClassName: 二级分类名称
-        :type SecondClassName: str
-        :param SecondClassProbability: 二级分类概率
-        :type SecondClassProbability: float
-        """
-        self.FirstClassName = None
-        self.FirstClassProbability = None
-        self.SecondClassName = None
-        self.SecondClassProbability = None
-
-
-    def _deserialize(self, params):
-        self.FirstClassName = params.get("FirstClassName")
-        self.FirstClassProbability = params.get("FirstClassProbability")
-        self.SecondClassName = params.get("SecondClassName")
-        self.SecondClassProbability = params.get("SecondClassProbability")
-
-
-class ContentApprovalRequest(AbstractModel):
-    """ContentApproval请求参数结构体
-
-    """
-
-    def __init__(self):
-        """
-        :param Text: 待审核的文本（仅支持UTF-8格式，不超过2000字）
-        :type Text: str
-        """
-        self.Text = None
-
-
-    def _deserialize(self, params):
-        self.Text = params.get("Text")
-
-
-class ContentApprovalResponse(AbstractModel):
-    """ContentApproval返回参数结构体
-
-    """
-
-    def __init__(self):
-        """
-        :param EvilFlag: 文本是否恶意：
-0、正常；
-1、恶意；
-2、可疑送审
-        :type EvilFlag: int
-        :param EvilKeywords: 恶意关键词组
-        :type EvilKeywords: list of str
-        :param EvilType: 文本恶意类型：
-0、正常；
-1、政治；
-2、色情；
-3、辱骂/低俗；
-4、暴恐/毒品；
-5、广告/灌水；
-6、迷信/邪教；
-7、其他违法（如跨站追杀/恶意竞争等）；
-8、综合
-        :type EvilType: int
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.EvilFlag = None
-        self.EvilKeywords = None
-        self.EvilType = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.EvilFlag = params.get("EvilFlag")
-        self.EvilKeywords = params.get("EvilKeywords")
-        self.EvilType = params.get("EvilType")
         self.RequestId = params.get("RequestId")
 
 
-class DependencyParsingRequest(AbstractModel):
-    """DependencyParsing请求参数结构体
+class DeleteResourceTagRequest(AbstractModel):
+    """DeleteResourceTag请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Text: 待分析的文本（仅支持UTF-8格式，不超过200字）
-        :type Text: str
+        :param TagKey: 标签键
+        :type TagKey: str
+        :param Resource: 资源六段式描述
+        :type Resource: str
         """
-        self.Text = None
+        self.TagKey = None
+        self.Resource = None
 
 
     def _deserialize(self, params):
-        self.Text = params.get("Text")
+        self.TagKey = params.get("TagKey")
+        self.Resource = params.get("Resource")
 
 
-class DependencyParsingResponse(AbstractModel):
-    """DependencyParsing返回参数结构体
+class DeleteResourceTagResponse(AbstractModel):
+    """DeleteResourceTag返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param DpTokens: 句法依存分析结果，其中句法依存关系的类型包括：
-<li>主谓关系，eg: 我送她一束花 (我 <-- 送)
-<li>动宾关系，eg: 我送她一束花 (送 --> 花)
-<li>间宾关系，eg: 我送她一束花 (送 --> 她)
-<li>前置宾语，eg: 他什么书都读 (书 <-- 读)
-<li>兼语，eg: 他请我吃饭 (请 --> 我)
-<li>定中关系，eg: 红苹果 (红 <-- 苹果)
-<li>状中结构，eg: 非常美丽 (非常 <-- 美丽)
-<li>动补结构，eg: 做完了作业 (做 --> 完)
-<li>并列关系，eg: 大山和大海 (大山 --> 大海)
-<li>介宾关系，eg: 在贸易区内 (在 --> 内)
-<li>左附加关系，eg: 大山和大海 (和 <-- 大海)
-<li>右附加关系，eg: 孩子们 (孩子 --> 们)
-<li>独立结构，eg: 两个单句在结构上彼此独立
-<li>标点符号，eg: 。
-<li>核心关系，eg: 整个句子的核心
-        :type DpTokens: list of DpToken
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.DpTokens = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        if params.get("DpTokens") is not None:
-            self.DpTokens = []
-            for item in params.get("DpTokens"):
-                obj = DpToken()
-                obj._deserialize(item)
-                self.DpTokens.append(obj)
         self.RequestId = params.get("RequestId")
 
 
-class DpToken(AbstractModel):
-    """句法依存分析结果，包括基础词，基础词的序号，当前词父节点的序号，句法依存关系的类型
+class DeleteTagRequest(AbstractModel):
+    """DeleteTag请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param HeadId: 当前词父节点的序号
-        :type HeadId: int
-        :param Id: 基础词的序号
-        :type Id: int
-        :param Relation: 句法依存关系的类型
-        :type Relation: str
-        :param Word: 基础词
-        :type Word: str
+        :param TagKey: 需要删除的标签键
+        :type TagKey: str
+        :param TagValue: 需要删除的标签值
+        :type TagValue: str
         """
-        self.HeadId = None
-        self.Id = None
-        self.Relation = None
-        self.Word = None
+        self.TagKey = None
+        self.TagValue = None
 
 
     def _deserialize(self, params):
-        self.HeadId = params.get("HeadId")
-        self.Id = params.get("Id")
-        self.Relation = params.get("Relation")
-        self.Word = params.get("Word")
+        self.TagKey = params.get("TagKey")
+        self.TagValue = params.get("TagValue")
 
 
-class EvilToken(AbstractModel):
-    """文本审核结果
+class DeleteTagResponse(AbstractModel):
+    """DeleteTag返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param EvilFlag: 文本是否恶意：
-0、正常；
-1、恶意；
-2、可疑送审
-        :type EvilFlag: int
-        :param EvilKeywords: 恶意关键词组
-        :type EvilKeywords: list of str
-        :param EvilType: 文本恶意类型：
-0、正常；
-1、政治；
-2、色情；
-3、辱骂/低俗；
-4、暴恐/毒品；
-5、广告/灌水；
-6、迷信/邪教；
-7、其他违法（如跨站追杀/恶意竞争等）；
-8、综合
-        :type EvilType: int
-        """
-        self.EvilFlag = None
-        self.EvilKeywords = None
-        self.EvilType = None
-
-
-    def _deserialize(self, params):
-        self.EvilFlag = params.get("EvilFlag")
-        self.EvilKeywords = params.get("EvilKeywords")
-        self.EvilType = params.get("EvilType")
-
-
-class Keyword(AbstractModel):
-    """关键词提取结果
-
-    """
-
-    def __init__(self):
-        """
-        :param Score: 权重
-        :type Score: float
-        :param Word: 关键词
-        :type Word: str
-        """
-        self.Score = None
-        self.Word = None
-
-
-    def _deserialize(self, params):
-        self.Score = params.get("Score")
-        self.Word = params.get("Word")
-
-
-class KeywordsExtractionRequest(AbstractModel):
-    """KeywordsExtraction请求参数结构体
-
-    """
-
-    def __init__(self):
-        """
-        :param Text: 待处理的文本（仅支持UTF-8格式，不超过2000字）
-        :type Text: str
-        :param Num: 指定关键词个数上限（默认值为5）
-        :type Num: int
-        """
-        self.Text = None
-        self.Num = None
-
-
-    def _deserialize(self, params):
-        self.Text = params.get("Text")
-        self.Num = params.get("Num")
-
-
-class KeywordsExtractionResponse(AbstractModel):
-    """KeywordsExtraction返回参数结构体
-
-    """
-
-    def __init__(self):
-        """
-        :param Keywords: 关键词提取结果
-        :type Keywords: list of Keyword
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.Keywords = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        if params.get("Keywords") is not None:
-            self.Keywords = []
-            for item in params.get("Keywords"):
-                obj = Keyword()
-                obj._deserialize(item)
-                self.Keywords.append(obj)
         self.RequestId = params.get("RequestId")
 
 
-class LexicalAnalysisRequest(AbstractModel):
-    """LexicalAnalysis请求参数结构体
+class DescribeResourceTagsByResourceIdsRequest(AbstractModel):
+    """DescribeResourceTagsByResourceIds请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Text: 待分析的文本（仅支持UTF-8格式，不超过500字）
-        :type Text: str
-        :param Flag: 词法分析模式（默认取1值）：
-1、高精度（具备混合粒度分词能力）；
-2、高性能；
-        :type Flag: int
+        :param ServiceType: 业务类型
+        :type ServiceType: str
+        :param ResourcePrefix: 资源前缀
+        :type ResourcePrefix: str
+        :param ResourceIds: 资源唯一标记
+        :type ResourceIds: list of str
+        :param ResourceRegion: 资源所在地域
+        :type ResourceRegion: str
+        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
+        :type Offset: int
+        :param Limit: 每页大小，默认为 15
+        :type Limit: int
         """
-        self.Text = None
-        self.Flag = None
+        self.ServiceType = None
+        self.ResourcePrefix = None
+        self.ResourceIds = None
+        self.ResourceRegion = None
+        self.Offset = None
+        self.Limit = None
 
 
     def _deserialize(self, params):
-        self.Text = params.get("Text")
-        self.Flag = params.get("Flag")
+        self.ServiceType = params.get("ServiceType")
+        self.ResourcePrefix = params.get("ResourcePrefix")
+        self.ResourceIds = params.get("ResourceIds")
+        self.ResourceRegion = params.get("ResourceRegion")
+        self.Offset = params.get("Offset")
+        self.Limit = params.get("Limit")
 
 
-class LexicalAnalysisResponse(AbstractModel):
-    """LexicalAnalysis返回参数结构体
+class DescribeResourceTagsByResourceIdsResponse(AbstractModel):
+    """DescribeResourceTagsByResourceIds返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param NerTokens: 命名实体识别结果。取值范围：
-<li>PER：表示人名</li>
-<li>LOC：表示地名</li>
-<li>ORG：表示机构团体名</li>
-        :type NerTokens: list of NerToken
-        :param PosTokens: 分词&词性标注结果（词性表请参见附录）
-        :type PosTokens: list of PosToken
+        :param TotalCount: 结果总数
+        :type TotalCount: int
+        :param Offset: 数据位移偏量
+        :type Offset: int
+        :param Limit: 每页大小
+        :type Limit: int
+        :param Tags: 标签列表
+        :type Tags: list of TagResource
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.NerTokens = None
-        self.PosTokens = None
+        self.TotalCount = None
+        self.Offset = None
+        self.Limit = None
+        self.Tags = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        if params.get("NerTokens") is not None:
-            self.NerTokens = []
-            for item in params.get("NerTokens"):
-                obj = NerToken()
-                obj._deserialize(item)
-                self.NerTokens.append(obj)
-        if params.get("PosTokens") is not None:
-            self.PosTokens = []
-            for item in params.get("PosTokens"):
-                obj = PosToken()
+        self.TotalCount = params.get("TotalCount")
+        self.Offset = params.get("Offset")
+        self.Limit = params.get("Limit")
+        if params.get("Tags") is not None:
+            self.Tags = []
+            for item in params.get("Tags"):
+                obj = TagResource()
                 obj._deserialize(item)
-                self.PosTokens.append(obj)
+                self.Tags.append(obj)
         self.RequestId = params.get("RequestId")
 
 
-class NerToken(AbstractModel):
-    """命名实体识别结果
-
-    """
-
-    def __init__(self):
-        """
-        :param BeginOffset: 起始位置
-        :type BeginOffset: int
-        :param Length: 长度
-        :type Length: int
-        :param Type: 命名实体类型
-        :type Type: str
-        :param Word: 基础词
-        :type Word: str
-        """
-        self.BeginOffset = None
-        self.Length = None
-        self.Type = None
-        self.Word = None
-
-
-    def _deserialize(self, params):
-        self.BeginOffset = params.get("BeginOffset")
-        self.Length = params.get("Length")
-        self.Type = params.get("Type")
-        self.Word = params.get("Word")
-
-
-class PosToken(AbstractModel):
-    """分词&词性标注结果
-
-    """
-
-    def __init__(self):
-        """
-        :param BeginOffset: 起始位置
-        :type BeginOffset: int
-        :param Length: 长度
-        :type Length: int
-        :param Pos: 词性
-        :type Pos: str
-        :param Word: 基础词
-        :type Word: str
-        """
-        self.BeginOffset = None
-        self.Length = None
-        self.Pos = None
-        self.Word = None
-
-
-    def _deserialize(self, params):
-        self.BeginOffset = params.get("BeginOffset")
-        self.Length = params.get("Length")
-        self.Pos = params.get("Pos")
-        self.Word = params.get("Word")
-
-
-class SensitiveWordsRecognitionRequest(AbstractModel):
-    """SensitiveWordsRecognition请求参数结构体
+class DescribeResourcesByTagsRequest(AbstractModel):
+    """DescribeResourcesByTags请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Text: 待识别的文本（仅支持UTF-8格式，不超过2000字）
-        :type Text: str
+        :param TagFilters: 标签过滤数组
+        :type TagFilters: list of TagFilter
+        :param CreateUin: 创建标签者uin
+        :type CreateUin: int
+        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
+        :type Offset: int
+        :param Limit: 每页大小，默认为 15
+        :type Limit: int
+        :param ResourcePrefix: 资源前缀
+        :type ResourcePrefix: str
+        :param ResourceId: 资源唯一标记
+        :type ResourceId: str
+        :param ResourceRegion: 资源所在地域
+        :type ResourceRegion: str
+        :param ServiceType: 业务类型
+        :type ServiceType: str
         """
-        self.Text = None
+        self.TagFilters = None
+        self.CreateUin = None
+        self.Offset = None
+        self.Limit = None
+        self.ResourcePrefix = None
+        self.ResourceId = None
+        self.ResourceRegion = None
+        self.ServiceType = None
 
 
     def _deserialize(self, params):
-        self.Text = params.get("Text")
+        if params.get("TagFilters") is not None:
+            self.TagFilters = []
+            for item in params.get("TagFilters"):
+                obj = TagFilter()
+                obj._deserialize(item)
+                self.TagFilters.append(obj)
+        self.CreateUin = params.get("CreateUin")
+        self.Offset = params.get("Offset")
+        self.Limit = params.get("Limit")
+        self.ResourcePrefix = params.get("ResourcePrefix")
+        self.ResourceId = params.get("ResourceId")
+        self.ResourceRegion = params.get("ResourceRegion")
+        self.ServiceType = params.get("ServiceType")
 
 
-class SensitiveWordsRecognitionResponse(AbstractModel):
-    """SensitiveWordsRecognition返回参数结构体
+class DescribeResourcesByTagsResponse(AbstractModel):
+    """DescribeResourcesByTags返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param SensitiveWords: 敏感词数组
-        :type SensitiveWords: list of str
+        :param TotalCount: 结果总数
+        :type TotalCount: int
+        :param Offset: 数据位移偏量
+        :type Offset: int
+        :param Limit: 每页大小
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Limit: int
+        :param Rows: 资源标签
+        :type Rows: list of ResourceTag
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.SensitiveWords = None
+        self.TotalCount = None
+        self.Offset = None
+        self.Limit = None
+        self.Rows = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.SensitiveWords = params.get("SensitiveWords")
+        self.TotalCount = params.get("TotalCount")
+        self.Offset = params.get("Offset")
+        self.Limit = params.get("Limit")
+        if params.get("Rows") is not None:
+            self.Rows = []
+            for item in params.get("Rows"):
+                obj = ResourceTag()
+                obj._deserialize(item)
+                self.Rows.append(obj)
         self.RequestId = params.get("RequestId")
 
 
-class SentenceEmbeddingRequest(AbstractModel):
-    """SentenceEmbedding请求参数结构体
+class DescribeTagKeysRequest(AbstractModel):
+    """DescribeTagKeys请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Text: 输入的文本（仅支持UTF-8格式，不超过500字）
-        :type Text: str
+        :param CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
+        :type CreateUin: int
+        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
+        :type Offset: int
+        :param Limit: 每页大小，默认为 15
+        :type Limit: int
         """
-        self.Text = None
+        self.CreateUin = None
+        self.Offset = None
+        self.Limit = None
 
 
     def _deserialize(self, params):
-        self.Text = params.get("Text")
+        self.CreateUin = params.get("CreateUin")
+        self.Offset = params.get("Offset")
+        self.Limit = params.get("Limit")
 
 
-class SentenceEmbeddingResponse(AbstractModel):
-    """SentenceEmbedding返回参数结构体
+class DescribeTagKeysResponse(AbstractModel):
+    """DescribeTagKeys返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Dimension: 句向量的维度
-        :type Dimension: int
-        :param Vector: 句向量数组
-        :type Vector: list of float
+        :param TotalCount: 结果总数
+        :type TotalCount: int
+        :param Offset: 数据位移偏量
+        :type Offset: int
+        :param Limit: 每页大小
+        :type Limit: int
+        :param Tags: 标签列表
+        :type Tags: list of str
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.Dimension = None
-        self.Vector = None
+        self.TotalCount = None
+        self.Offset = None
+        self.Limit = None
+        self.Tags = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.Dimension = params.get("Dimension")
-        self.Vector = params.get("Vector")
+        self.TotalCount = params.get("TotalCount")
+        self.Offset = params.get("Offset")
+        self.Limit = params.get("Limit")
+        self.Tags = params.get("Tags")
         self.RequestId = params.get("RequestId")
 
 
-class SentenceSimilarityRequest(AbstractModel):
-    """SentenceSimilarity请求参数结构体
+class DescribeTagValuesRequest(AbstractModel):
+    """DescribeTagValues请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param SrcText: 计算相似度的源句子（仅支持UTF-8格式，不超过500字）
-        :type SrcText: str
-        :param TargetText: 计算相似度的目标句子（仅支持UTF-8格式，不超过500字）
-        :type TargetText: str
+        :param TagKeys: 标签键列表
+        :type TagKeys: list of str
+        :param CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
+        :type CreateUin: int
+        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
+        :type Offset: int
+        :param Limit: 每页大小，默认为 15
+        :type Limit: int
         """
-        self.SrcText = None
-        self.TargetText = None
+        self.TagKeys = None
+        self.CreateUin = None
+        self.Offset = None
+        self.Limit = None
 
 
     def _deserialize(self, params):
-        self.SrcText = params.get("SrcText")
-        self.TargetText = params.get("TargetText")
+        self.TagKeys = params.get("TagKeys")
+        self.CreateUin = params.get("CreateUin")
+        self.Offset = params.get("Offset")
+        self.Limit = params.get("Limit")
 
 
-class SentenceSimilarityResponse(AbstractModel):
-    """SentenceSimilarity返回参数结构体
+class DescribeTagValuesResponse(AbstractModel):
+    """DescribeTagValues返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Similarity: 两个文本的相似度
-        :type Similarity: float
+        :param TotalCount: 结果总数
+        :type TotalCount: int
+        :param Offset: 数据位移偏量
+        :type Offset: int
+        :param Limit: 每页大小
+        :type Limit: int
+        :param Tags: 标签列表
+        :type Tags: list of Tag
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.Similarity = None
+        self.TotalCount = None
+        self.Offset = None
+        self.Limit = None
+        self.Tags = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.Similarity = params.get("Similarity")
+        self.TotalCount = params.get("TotalCount")
+        self.Offset = params.get("Offset")
+        self.Limit = params.get("Limit")
+        if params.get("Tags") is not None:
+            self.Tags = []
+            for item in params.get("Tags"):
+                obj = Tag()
+                obj._deserialize(item)
+                self.Tags.append(obj)
         self.RequestId = params.get("RequestId")
 
 
-class SentimentAnalysisRequest(AbstractModel):
-    """SentimentAnalysis请求参数结构体
+class DescribeTagsRequest(AbstractModel):
+    """DescribeTags请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Text: 待分析的文本（仅支持UTF-8格式，不超过200字）
-        :type Text: str
-        :param Flag: 文本所属类型（默认取4值）：
-1、电商
-2、APP
-3、美食
-4、酒店和其他
-        :type Flag: int
+        :param TagKey: 标签键,与标签值同时存在或同时不存在，不存在时表示查询该用户所有标签
+        :type TagKey: str
+        :param TagValue: 标签值,与标签键同时存在或同时不存在，不存在时表示查询该用户所有标签
+        :type TagValue: str
+        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
+        :type Offset: int
+        :param Limit: 每页大小，默认为 15
+        :type Limit: int
+        :param CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
+        :type CreateUin: int
         """
-        self.Text = None
-        self.Flag = None
+        self.TagKey = None
+        self.TagValue = None
+        self.Offset = None
+        self.Limit = None
+        self.CreateUin = None
 
 
     def _deserialize(self, params):
-        self.Text = params.get("Text")
-        self.Flag = params.get("Flag")
+        self.TagKey = params.get("TagKey")
+        self.TagValue = params.get("TagValue")
+        self.Offset = params.get("Offset")
+        self.Limit = params.get("Limit")
+        self.CreateUin = params.get("CreateUin")
 
 
-class SentimentAnalysisResponse(AbstractModel):
-    """SentimentAnalysis返回参数结构体
+class DescribeTagsResponse(AbstractModel):
+    """DescribeTags返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Negative: 负面情感概率
-        :type Negative: float
-        :param Positive: 正面情感概率
-        :type Positive: float
-        :param Sentiment: 情感属性
-        :type Sentiment: str
+        :param TotalCount: 结果总数
+        :type TotalCount: int
+        :param Offset: 数据位移偏量
+        :type Offset: int
+        :param Limit: 每页大小
+        :type Limit: int
+        :param Tags: 标签列表
+        :type Tags: list of TagWithDelete
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.Negative = None
-        self.Positive = None
-        self.Sentiment = None
+        self.TotalCount = None
+        self.Offset = None
+        self.Limit = None
+        self.Tags = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.Negative = params.get("Negative")
-        self.Positive = params.get("Positive")
-        self.Sentiment = params.get("Sentiment")
+        self.TotalCount = params.get("TotalCount")
+        self.Offset = params.get("Offset")
+        self.Limit = params.get("Limit")
+        if params.get("Tags") is not None:
+            self.Tags = []
+            for item in params.get("Tags"):
+                obj = TagWithDelete()
+                obj._deserialize(item)
+                self.Tags.append(obj)
         self.RequestId = params.get("RequestId")
 
 
-class SimilarWordsRequest(AbstractModel):
-    """SimilarWords请求参数结构体
+class ModifyResourceTagsRequest(AbstractModel):
+    """ModifyResourceTags请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Text: 输入的词语（仅支持UTF-8格式，不超过20字）
-        :type Text: str
-        :param WordNumber: 相似词个数；取值范围：1-200，默认为10；
-        :type WordNumber: int
+        :param Resource: 资源的六段式描述
+        :type Resource: str
+        :param ReplaceTags: 需要增加或修改的标签集合。如果Resource描述的资源未关联输入的标签键，则增加关联；若已关联，则将该资源关联的键对应的标签值修改为输入值。本接口中ReplaceTags和DeleteTags二者必须存在其一，且二者不能包含相同的标签键
+        :type ReplaceTags: list of Tag
+        :param DeleteTags: 需要解关联的标签集合。本接口中ReplaceTags和DeleteTags二者必须存在其一，且二者不能包含相同的标签键
+        :type DeleteTags: list of TagKeyObject
         """
-        self.Text = None
-        self.WordNumber = None
+        self.Resource = None
+        self.ReplaceTags = None
+        self.DeleteTags = None
 
 
     def _deserialize(self, params):
-        self.Text = params.get("Text")
-        self.WordNumber = params.get("WordNumber")
+        self.Resource = params.get("Resource")
+        if params.get("ReplaceTags") is not None:
+            self.ReplaceTags = []
+            for item in params.get("ReplaceTags"):
+                obj = Tag()
+                obj._deserialize(item)
+                self.ReplaceTags.append(obj)
+        if params.get("DeleteTags") is not None:
+            self.DeleteTags = []
+            for item in params.get("DeleteTags"):
+                obj = TagKeyObject()
+                obj._deserialize(item)
+                self.DeleteTags.append(obj)
 
 
-class SimilarWordsResponse(AbstractModel):
-    """SimilarWords返回参数结构体
+class ModifyResourceTagsResponse(AbstractModel):
+    """ModifyResourceTags返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param SimilarWords: 相似词数组
-        :type SimilarWords: list of str
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.SimilarWords = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.SimilarWords = params.get("SimilarWords")
         self.RequestId = params.get("RequestId")
 
 
-class TextApprovalRequest(AbstractModel):
-    """TextApproval请求参数结构体
+class ResourceTag(AbstractModel):
+    """资源标签
 
     """
 
     def __init__(self):
         """
-        :param Text: 待审核的文本（仅支持UTF-8格式，不超过2000字）
-        :type Text: str
-        :param Flag: 文本审核模式（默认取1值）：
-1、全领域审核
-        :type Flag: int
+        :param ResourceRegion: 资源所在地域
+注意：此字段可能返回 null，表示取不到有效值。
+        :type ResourceRegion: str
+        :param ServiceType: 业务类型
+注意：此字段可能返回 null，表示取不到有效值。
+        :type ServiceType: str
+        :param ResourcePrefix: 资源前缀
+注意：此字段可能返回 null，表示取不到有效值。
+        :type ResourcePrefix: str
+        :param ResourceId: 资源唯一标记
+注意：此字段可能返回 null，表示取不到有效值。
+        :type ResourceId: str
+        :param Tags: 资源标签
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Tags: list of Tag
         """
-        self.Text = None
-        self.Flag = None
+        self.ResourceRegion = None
+        self.ServiceType = None
+        self.ResourcePrefix = None
+        self.ResourceId = None
+        self.Tags = None
 
 
     def _deserialize(self, params):
-        self.Text = params.get("Text")
-        self.Flag = params.get("Flag")
-
-
-class TextApprovalResponse(AbstractModel):
-    """TextApproval返回参数结构体
-
-    """
-
-    def __init__(self):
-        """
-        :param EvilTokens: 文本审核输出结果
-        :type EvilTokens: list of EvilToken
-        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
-        :type RequestId: str
-        """
-        self.EvilTokens = None
-        self.RequestId = None
-
-
-    def _deserialize(self, params):
-        if params.get("EvilTokens") is not None:
-            self.EvilTokens = []
-            for item in params.get("EvilTokens"):
-                obj = EvilToken()
+        self.ResourceRegion = params.get("ResourceRegion")
+        self.ServiceType = params.get("ServiceType")
+        self.ResourcePrefix = params.get("ResourcePrefix")
+        self.ResourceId = params.get("ResourceId")
+        if params.get("Tags") is not None:
+            self.Tags = []
+            for item in params.get("Tags"):
+                obj = Tag()
                 obj._deserialize(item)
-                self.EvilTokens.append(obj)
-        self.RequestId = params.get("RequestId")
+                self.Tags.append(obj)
 
 
-class TextClassificationRequest(AbstractModel):
-    """TextClassification请求参数结构体
+class Tag(AbstractModel):
+    """表示一个标签键值对
 
     """
 
     def __init__(self):
         """
-        :param Text: 待分类的文本（仅支持UTF-8格式，不超过2000字）
-        :type Text: str
-        :param Flag: 领域分类体系（默认取1值）：
-1、通用领域
-2、新闻领域
-        :type Flag: int
+        :param TagKey: 标签键
+        :type TagKey: str
+        :param TagValue: 标签值
+        :type TagValue: str
         """
-        self.Text = None
-        self.Flag = None
+        self.TagKey = None
+        self.TagValue = None
 
 
     def _deserialize(self, params):
-        self.Text = params.get("Text")
-        self.Flag = params.get("Flag")
+        self.TagKey = params.get("TagKey")
+        self.TagValue = params.get("TagValue")
 
 
-class TextClassificationResponse(AbstractModel):
-    """TextClassification返回参数结构体
+class TagFilter(AbstractModel):
+    """tag过滤数组多个是与的关系
 
     """
 
     def __init__(self):
         """
-        :param Classes: 文本分类结果（文本分类映射表请参见附录）
-        :type Classes: list of ClassificationResult
-        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
-        :type RequestId: str
+        :param TagKey: 标签键
+        :type TagKey: str
+        :param TagValue: 标签值数组 多个值的话是或的关系
+        :type TagValue: list of str
         """
-        self.Classes = None
-        self.RequestId = None
+        self.TagKey = None
+        self.TagValue = None
 
 
     def _deserialize(self, params):
-        if params.get("Classes") is not None:
-            self.Classes = []
-            for item in params.get("Classes"):
-                obj = ClassificationResult()
-                obj._deserialize(item)
-                self.Classes.append(obj)
-        self.RequestId = params.get("RequestId")
+        self.TagKey = params.get("TagKey")
+        self.TagValue = params.get("TagValue")
 
 
-class TextCorrectionRequest(AbstractModel):
-    """TextCorrection请求参数结构体
+class TagKeyObject(AbstractModel):
+    """标签键对象
 
     """
 
     def __init__(self):
         """
-        :param Text: 待纠错的文本（仅支持UTF-8格式，不超过2000字）
-        :type Text: str
+        :param TagKey: 标签键
+        :type TagKey: str
         """
-        self.Text = None
+        self.TagKey = None
 
 
     def _deserialize(self, params):
-        self.Text = params.get("Text")
+        self.TagKey = params.get("TagKey")
 
 
-class TextCorrectionResponse(AbstractModel):
-    """TextCorrection返回参数结构体
+class TagResource(AbstractModel):
+    """标签键值对以及资源ID
 
     """
 
     def __init__(self):
         """
-        :param CCITokens: 纠错详情
-        :type CCITokens: list of CCIToken
-        :param ResultText: 纠错后的文本
-        :type ResultText: str
-        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
-        :type RequestId: str
+        :param TagKey: 标签键
+        :type TagKey: str
+        :param TagValue: 标签值
+        :type TagValue: str
+        :param ResourceId: 资源ID
+        :type ResourceId: str
+        :param TagKeyMd5: 标签键MD5值
+        :type TagKeyMd5: str
+        :param TagValueMd5: 标签值MD5值
+        :type TagValueMd5: str
         """
-        self.CCITokens = None
-        self.ResultText = None
-        self.RequestId = None
+        self.TagKey = None
+        self.TagValue = None
+        self.ResourceId = None
+        self.TagKeyMd5 = None
+        self.TagValueMd5 = None
 
 
     def _deserialize(self, params):
-        if params.get("CCITokens") is not None:
-            self.CCITokens = []
-            for item in params.get("CCITokens"):
-                obj = CCIToken()
-                obj._deserialize(item)
-                self.CCITokens.append(obj)
-        self.ResultText = params.get("ResultText")
-        self.RequestId = params.get("RequestId")
+        self.TagKey = params.get("TagKey")
+        self.TagValue = params.get("TagValue")
+        self.ResourceId = params.get("ResourceId")
+        self.TagKeyMd5 = params.get("TagKeyMd5")
+        self.TagValueMd5 = params.get("TagValueMd5")
 
 
-class WordEmbeddingRequest(AbstractModel):
-    """WordEmbedding请求参数结构体
+class TagWithDelete(AbstractModel):
+    """表示一个标签键值对以及是否允许删除
 
     """
 
     def __init__(self):
         """
-        :param Text: 输入的词语（仅支持UTF-8格式，不超过20字）
-        :type Text: str
+        :param TagKey: 标签键
+        :type TagKey: str
+        :param TagValue: 标签值
+        :type TagValue: str
+        :param CanDelete: 是否可以删除
+        :type CanDelete: int
         """
-        self.Text = None
+        self.TagKey = None
+        self.TagValue = None
+        self.CanDelete = None
 
 
     def _deserialize(self, params):
-        self.Text = params.get("Text")
-
-
-class WordEmbeddingResponse(AbstractModel):
-    """WordEmbedding返回参数结构体
-
-    """
-
-    def __init__(self):
-        """
-        :param Dimension: 词向量的维度
-        :type Dimension: int
-        :param Vector: 词向量数组
-        :type Vector: list of float
-        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
-        :type RequestId: str
-        """
-        self.Dimension = None
-        self.Vector = None
-        self.RequestId = None
-
-
-    def _deserialize(self, params):
-        self.Dimension = params.get("Dimension")
-        self.Vector = params.get("Vector")
-        self.RequestId = params.get("RequestId")
+        self.TagKey = params.get("TagKey")
+        self.TagValue = params.get("TagValue")
+        self.CanDelete = params.get("CanDelete")
 
 
-class WordSimilarityRequest(AbstractModel):
-    """WordSimilarity请求参数结构体
+class UpdateResourceTagValueRequest(AbstractModel):
+    """UpdateResourceTagValue请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param SrcWord: 计算相似度的源词（仅支持UTF-8格式，不超过20字）
-        :type SrcWord: str
-        :param TargetWord: 计算相似度的目标词（仅支持UTF-8格式，不超过20字）
-        :type TargetWord: str
+        :param TagKey: 资源关联的标签键
+        :type TagKey: str
+        :param TagValue: 修改后的标签值
+        :type TagValue: str
+        :param Resource: 资源的六段式描述
+        :type Resource: str
         """
-        self.SrcWord = None
-        self.TargetWord = None
+        self.TagKey = None
+        self.TagValue = None
+        self.Resource = None
 
 
     def _deserialize(self, params):
-        self.SrcWord = params.get("SrcWord")
-        self.TargetWord = params.get("TargetWord")
+        self.TagKey = params.get("TagKey")
+        self.TagValue = params.get("TagValue")
+        self.Resource = params.get("Resource")
 
 
-class WordSimilarityResponse(AbstractModel):
-    """WordSimilarity返回参数结构体
+class UpdateResourceTagValueResponse(AbstractModel):
+    """UpdateResourceTagValue返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Similarity: 两个词语的相似度
-        :type Similarity: float
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.Similarity = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.Similarity = params.get("Similarity")
         self.RequestId = params.get("RequestId")
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/nlp/v20190408/nlp_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/nlp/v20190408/nlp_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/iotcloud/v20180614/iotcloud_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/iotcloud/v20180614/iotcloud_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/iotcloud/v20180614/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/iotcloud/v20180614/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/iot/v20180123/iot_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/iot/v20180123/iot_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/iot/v20180123/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/iot/v20180123/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tkgdq/v20190411/tkgdq_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tkgdq/v20190411/tkgdq_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tkgdq/v20190411/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tkgdq/v20190411/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tmt/v20180321/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tmt/v20180321/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tmt/v20180321/tmt_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tmt/v20180321/tmt_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cms/v20190321/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cms/v20190321/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cms/v20190321/cms_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cms/v20190321/cms_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tcb/v20180608/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tcb/v20180608/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tcb/v20180608/tcb_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tcb/v20180608/tcb_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tke/v20180525/tke_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tke/v20180525/tke_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tke/v20180525/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tke/v20180525/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/emr/v20190103/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/emr/v20190103/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/emr/v20190103/emr_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/emr/v20190103/emr_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tag/v20180813/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/organization/v20181225/models.py`

 * *Files 14% similar despite different names*

```diff
@@ -12,41 +12,33 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 from tencentcloud.common.abstract_model import AbstractModel
 
 
-class AddResourceTagRequest(AbstractModel):
-    """AddResourceTag请求参数结构体
+class AcceptOrganizationInvitationRequest(AbstractModel):
+    """AcceptOrganizationInvitation请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TagKey: 标签键
-        :type TagKey: str
-        :param TagValue: 标签值
-        :type TagValue: str
-        :param Resource: 资源六段式描述
-        :type Resource: str
+        :param Id: 邀请ID
+        :type Id: int
         """
-        self.TagKey = None
-        self.TagValue = None
-        self.Resource = None
+        self.Id = None
 
 
     def _deserialize(self, params):
-        self.TagKey = params.get("TagKey")
-        self.TagValue = params.get("TagValue")
-        self.Resource = params.get("Resource")
+        self.Id = params.get("Id")
 
 
-class AddResourceTagResponse(AbstractModel):
-    """AddResourceTag返回参数结构体
+class AcceptOrganizationInvitationResponse(AbstractModel):
+    """AcceptOrganizationInvitation返回参数结构体
 
     """
 
     def __init__(self):
         """
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
@@ -54,75 +46,75 @@
         self.RequestId = None
 
 
     def _deserialize(self, params):
         self.RequestId = params.get("RequestId")
 
 
-class CreateTagRequest(AbstractModel):
-    """CreateTag请求参数结构体
+class AddOrganizationNodeRequest(AbstractModel):
+    """AddOrganizationNode请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TagKey: 标签键
-        :type TagKey: str
-        :param TagValue: 标签值
-        :type TagValue: str
+        :param ParentNodeId: 父组织单元ID
+        :type ParentNodeId: int
+        :param Name: 组织单元名字
+        :type Name: str
         """
-        self.TagKey = None
-        self.TagValue = None
+        self.ParentNodeId = None
+        self.Name = None
 
 
     def _deserialize(self, params):
-        self.TagKey = params.get("TagKey")
-        self.TagValue = params.get("TagValue")
+        self.ParentNodeId = params.get("ParentNodeId")
+        self.Name = params.get("Name")
 
 
-class CreateTagResponse(AbstractModel):
-    """CreateTag返回参数结构体
+class AddOrganizationNodeResponse(AbstractModel):
+    """AddOrganizationNode返回参数结构体
 
     """
 
     def __init__(self):
         """
+        :param NodeId: 组织单元ID
+        :type NodeId: int
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
+        self.NodeId = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
+        self.NodeId = params.get("NodeId")
         self.RequestId = params.get("RequestId")
 
 
-class DeleteResourceTagRequest(AbstractModel):
-    """DeleteResourceTag请求参数结构体
+class CancelOrganizationInvitationRequest(AbstractModel):
+    """CancelOrganizationInvitation请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TagKey: 标签键
-        :type TagKey: str
-        :param Resource: 资源六段式描述
-        :type Resource: str
+        :param Id: 邀请ID
+        :type Id: int
         """
-        self.TagKey = None
-        self.Resource = None
+        self.Id = None
 
 
     def _deserialize(self, params):
-        self.TagKey = params.get("TagKey")
-        self.Resource = params.get("Resource")
+        self.Id = params.get("Id")
 
 
-class DeleteResourceTagResponse(AbstractModel):
-    """DeleteResourceTag返回参数结构体
+class CancelOrganizationInvitationResponse(AbstractModel):
+    """CancelOrganizationInvitation返回参数结构体
 
     """
 
     def __init__(self):
         """
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
@@ -130,449 +122,552 @@
         self.RequestId = None
 
 
     def _deserialize(self, params):
         self.RequestId = params.get("RequestId")
 
 
-class DeleteTagRequest(AbstractModel):
-    """DeleteTag请求参数结构体
+class CreateOrganizationRequest(AbstractModel):
+    """CreateOrganization请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TagKey: 需要删除的标签键
-        :type TagKey: str
-        :param TagValue: 需要删除的标签值
-        :type TagValue: str
+        :param OrgType: 组织类型（目前固定为1）
+        :type OrgType: int
         """
-        self.TagKey = None
-        self.TagValue = None
+        self.OrgType = None
 
 
     def _deserialize(self, params):
-        self.TagKey = params.get("TagKey")
-        self.TagValue = params.get("TagValue")
+        self.OrgType = params.get("OrgType")
 
 
-class DeleteTagResponse(AbstractModel):
-    """DeleteTag返回参数结构体
+class CreateOrganizationResponse(AbstractModel):
+    """CreateOrganization返回参数结构体
 
     """
 
     def __init__(self):
         """
+        :param OrgId: 企业组织ID
+        :type OrgId: int
+        :param Nickname: 创建者昵称
+        :type Nickname: str
+        :param Mail: 创建者邮箱
+        :type Mail: str
+        :param OrgType: 组织类型
+        :type OrgType: int
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
+        self.OrgId = None
+        self.Nickname = None
+        self.Mail = None
+        self.OrgType = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
+        self.OrgId = params.get("OrgId")
+        self.Nickname = params.get("Nickname")
+        self.Mail = params.get("Mail")
+        self.OrgType = params.get("OrgType")
         self.RequestId = params.get("RequestId")
 
 
-class DescribeResourceTagsByResourceIdsRequest(AbstractModel):
-    """DescribeResourceTagsByResourceIds请求参数结构体
+class DeleteOrganizationMemberFromNodeRequest(AbstractModel):
+    """DeleteOrganizationMemberFromNode请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param ServiceType: 业务类型
-        :type ServiceType: str
-        :param ResourcePrefix: 资源前缀
-        :type ResourcePrefix: str
-        :param ResourceIds: 资源唯一标记
-        :type ResourceIds: list of str
-        :param ResourceRegion: 资源所在地域
-        :type ResourceRegion: str
-        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
-        :type Offset: int
-        :param Limit: 每页大小，默认为 15
-        :type Limit: int
+        :param MemberUin: 被删除成员UIN
+        :type MemberUin: int
+        :param NodeId: 组织单元ID
+        :type NodeId: int
         """
-        self.ServiceType = None
-        self.ResourcePrefix = None
-        self.ResourceIds = None
-        self.ResourceRegion = None
-        self.Offset = None
-        self.Limit = None
+        self.MemberUin = None
+        self.NodeId = None
 
 
     def _deserialize(self, params):
-        self.ServiceType = params.get("ServiceType")
-        self.ResourcePrefix = params.get("ResourcePrefix")
-        self.ResourceIds = params.get("ResourceIds")
-        self.ResourceRegion = params.get("ResourceRegion")
-        self.Offset = params.get("Offset")
-        self.Limit = params.get("Limit")
+        self.MemberUin = params.get("MemberUin")
+        self.NodeId = params.get("NodeId")
 
 
-class DescribeResourceTagsByResourceIdsResponse(AbstractModel):
-    """DescribeResourceTagsByResourceIds返回参数结构体
+class DeleteOrganizationMemberFromNodeResponse(AbstractModel):
+    """DeleteOrganizationMemberFromNode返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TotalCount: 结果总数
-        :type TotalCount: int
-        :param Offset: 数据位移偏量
-        :type Offset: int
-        :param Limit: 每页大小
-        :type Limit: int
-        :param Tags: 标签列表
-        :type Tags: list of TagResource
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.TotalCount = None
-        self.Offset = None
-        self.Limit = None
-        self.Tags = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.TotalCount = params.get("TotalCount")
-        self.Offset = params.get("Offset")
-        self.Limit = params.get("Limit")
-        if params.get("Tags") is not None:
-            self.Tags = []
-            for item in params.get("Tags"):
-                obj = TagResource()
-                obj._deserialize(item)
-                self.Tags.append(obj)
         self.RequestId = params.get("RequestId")
 
 
-class DescribeResourcesByTagsRequest(AbstractModel):
-    """DescribeResourcesByTags请求参数结构体
+class DeleteOrganizationMembersRequest(AbstractModel):
+    """DeleteOrganizationMembers请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TagFilters: 标签过滤数组
-        :type TagFilters: list of TagFilter
-        :param CreateUin: 创建标签者uin
-        :type CreateUin: int
-        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
-        :type Offset: int
-        :param Limit: 每页大小，默认为 15
-        :type Limit: int
-        :param ResourcePrefix: 资源前缀
-        :type ResourcePrefix: str
-        :param ResourceId: 资源唯一标记
-        :type ResourceId: str
-        :param ResourceRegion: 资源所在地域
-        :type ResourceRegion: str
-        :param ServiceType: 业务类型
-        :type ServiceType: str
+        :param Uins: 被删除成员的UIN列表
+        :type Uins: list of int non-negative
         """
-        self.TagFilters = None
-        self.CreateUin = None
-        self.Offset = None
-        self.Limit = None
-        self.ResourcePrefix = None
-        self.ResourceId = None
-        self.ResourceRegion = None
-        self.ServiceType = None
+        self.Uins = None
 
 
     def _deserialize(self, params):
-        if params.get("TagFilters") is not None:
-            self.TagFilters = []
-            for item in params.get("TagFilters"):
-                obj = TagFilter()
-                obj._deserialize(item)
-                self.TagFilters.append(obj)
-        self.CreateUin = params.get("CreateUin")
-        self.Offset = params.get("Offset")
-        self.Limit = params.get("Limit")
-        self.ResourcePrefix = params.get("ResourcePrefix")
-        self.ResourceId = params.get("ResourceId")
-        self.ResourceRegion = params.get("ResourceRegion")
-        self.ServiceType = params.get("ServiceType")
+        self.Uins = params.get("Uins")
 
 
-class DescribeResourcesByTagsResponse(AbstractModel):
-    """DescribeResourcesByTags返回参数结构体
+class DeleteOrganizationMembersResponse(AbstractModel):
+    """DeleteOrganizationMembers返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TotalCount: 结果总数
-        :type TotalCount: int
-        :param Offset: 数据位移偏量
-        :type Offset: int
-        :param Limit: 每页大小
-注意：此字段可能返回 null，表示取不到有效值。
-        :type Limit: int
-        :param Rows: 资源标签
-        :type Rows: list of ResourceTag
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
-        self.TotalCount = None
-        self.Offset = None
-        self.Limit = None
-        self.Rows = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.TotalCount = params.get("TotalCount")
-        self.Offset = params.get("Offset")
-        self.Limit = params.get("Limit")
-        if params.get("Rows") is not None:
-            self.Rows = []
-            for item in params.get("Rows"):
-                obj = ResourceTag()
-                obj._deserialize(item)
-                self.Rows.append(obj)
         self.RequestId = params.get("RequestId")
 
 
-class DescribeTagKeysRequest(AbstractModel):
-    """DescribeTagKeys请求参数结构体
+class DeleteOrganizationNodesRequest(AbstractModel):
+    """DeleteOrganizationNodes请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param NodeIds: 组织单元ID列表
+        :type NodeIds: list of int non-negative
+        """
+        self.NodeIds = None
+
+
+    def _deserialize(self, params):
+        self.NodeIds = params.get("NodeIds")
+
+
+class DeleteOrganizationNodesResponse(AbstractModel):
+    """DeleteOrganizationNodes返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.RequestId = params.get("RequestId")
+
+
+class DeleteOrganizationRequest(AbstractModel):
+    """DeleteOrganization请求参数结构体
+
+    """
+
+
+class DeleteOrganizationResponse(AbstractModel):
+    """DeleteOrganization返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.RequestId = params.get("RequestId")
+
+
+class DenyOrganizationInvitationRequest(AbstractModel):
+    """DenyOrganizationInvitation请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param Id: 邀请ID
+        :type Id: int
+        """
+        self.Id = None
+
+
+    def _deserialize(self, params):
+        self.Id = params.get("Id")
+
+
+class DenyOrganizationInvitationResponse(AbstractModel):
+    """DenyOrganizationInvitation返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.RequestId = params.get("RequestId")
+
+
+class GetOrganizationMemberRequest(AbstractModel):
+    """GetOrganizationMember请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param MemberUin: 组织成员UIN
+        :type MemberUin: int
+        """
+        self.MemberUin = None
+
+
+    def _deserialize(self, params):
+        self.MemberUin = params.get("MemberUin")
+
+
+class GetOrganizationMemberResponse(AbstractModel):
+    """GetOrganizationMember返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param Uin: 组织成员UIN
+        :type Uin: int
+        :param Name: 组织成员名称
+        :type Name: str
+        :param Remark: 备注
+        :type Remark: str
+        :param JoinTime: 加入时间
+        :type JoinTime: str
+        :param NodeId: 组织单元ID
+        :type NodeId: int
+        :param NodeName: 组织单元名称
+        :type NodeName: str
+        :param ParentNodeId: 父组织单元ID
+        :type ParentNodeId: int
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.Uin = None
+        self.Name = None
+        self.Remark = None
+        self.JoinTime = None
+        self.NodeId = None
+        self.NodeName = None
+        self.ParentNodeId = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.Uin = params.get("Uin")
+        self.Name = params.get("Name")
+        self.Remark = params.get("Remark")
+        self.JoinTime = params.get("JoinTime")
+        self.NodeId = params.get("NodeId")
+        self.NodeName = params.get("NodeName")
+        self.ParentNodeId = params.get("ParentNodeId")
+        self.RequestId = params.get("RequestId")
+
+
+class GetOrganizationRequest(AbstractModel):
+    """GetOrganization请求参数结构体
+
+    """
+
+
+class GetOrganizationResponse(AbstractModel):
+    """GetOrganization返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
-        :type CreateUin: int
-        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
+        :param OrgId: 企业组织ID
+        :type OrgId: int
+        :param HostUin: 创建者UIN
+        :type HostUin: int
+        :param Nickname: 创建者昵称
+        :type Nickname: str
+        :param Mail: 创建者邮箱
+        :type Mail: str
+        :param OrgType: 企业组织类型
+        :type OrgType: int
+        :param IsEmpty: 是否为空
+        :type IsEmpty: int
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.OrgId = None
+        self.HostUin = None
+        self.Nickname = None
+        self.Mail = None
+        self.OrgType = None
+        self.IsEmpty = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.OrgId = params.get("OrgId")
+        self.HostUin = params.get("HostUin")
+        self.Nickname = params.get("Nickname")
+        self.Mail = params.get("Mail")
+        self.OrgType = params.get("OrgType")
+        self.IsEmpty = params.get("IsEmpty")
+        self.RequestId = params.get("RequestId")
+
+
+class ListOrganizationInvitationsRequest(AbstractModel):
+    """ListOrganizationInvitations请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param Invited: 是否被邀请。1：被邀请，0：发出的邀请
+        :type Invited: int
+        :param Offset: 偏移量
         :type Offset: int
-        :param Limit: 每页大小，默认为 15
+        :param Limit: 限制数目
         :type Limit: int
         """
-        self.CreateUin = None
+        self.Invited = None
         self.Offset = None
         self.Limit = None
 
 
     def _deserialize(self, params):
-        self.CreateUin = params.get("CreateUin")
+        self.Invited = params.get("Invited")
         self.Offset = params.get("Offset")
         self.Limit = params.get("Limit")
 
 
-class DescribeTagKeysResponse(AbstractModel):
-    """DescribeTagKeys返回参数结构体
+class ListOrganizationInvitationsResponse(AbstractModel):
+    """ListOrganizationInvitations返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TotalCount: 结果总数
+        :param Invitations: 邀请信息列表
+        :type Invitations: list of OrgInvitation
+        :param TotalCount: 总数目
         :type TotalCount: int
-        :param Offset: 数据位移偏量
-        :type Offset: int
-        :param Limit: 每页大小
-        :type Limit: int
-        :param Tags: 标签列表
-        :type Tags: list of str
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
+        self.Invitations = None
         self.TotalCount = None
-        self.Offset = None
-        self.Limit = None
-        self.Tags = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
+        if params.get("Invitations") is not None:
+            self.Invitations = []
+            for item in params.get("Invitations"):
+                obj = OrgInvitation()
+                obj._deserialize(item)
+                self.Invitations.append(obj)
         self.TotalCount = params.get("TotalCount")
-        self.Offset = params.get("Offset")
-        self.Limit = params.get("Limit")
-        self.Tags = params.get("Tags")
         self.RequestId = params.get("RequestId")
 
 
-class DescribeTagValuesRequest(AbstractModel):
-    """DescribeTagValues请求参数结构体
+class ListOrganizationMembersRequest(AbstractModel):
+    """ListOrganizationMembers请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TagKeys: 标签键列表
-        :type TagKeys: list of str
-        :param CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
-        :type CreateUin: int
-        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
+        :param Offset: 偏移量
         :type Offset: int
-        :param Limit: 每页大小，默认为 15
+        :param Limit: 限制数目
         :type Limit: int
         """
-        self.TagKeys = None
-        self.CreateUin = None
         self.Offset = None
         self.Limit = None
 
 
     def _deserialize(self, params):
-        self.TagKeys = params.get("TagKeys")
-        self.CreateUin = params.get("CreateUin")
         self.Offset = params.get("Offset")
         self.Limit = params.get("Limit")
 
 
-class DescribeTagValuesResponse(AbstractModel):
-    """DescribeTagValues返回参数结构体
+class ListOrganizationMembersResponse(AbstractModel):
+    """ListOrganizationMembers返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TotalCount: 结果总数
+        :param Members: 成员列表
+        :type Members: list of OrgMember
+        :param TotalCount: 总数目
         :type TotalCount: int
-        :param Offset: 数据位移偏量
-        :type Offset: int
-        :param Limit: 每页大小
-        :type Limit: int
-        :param Tags: 标签列表
-        :type Tags: list of Tag
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
+        self.Members = None
         self.TotalCount = None
-        self.Offset = None
-        self.Limit = None
-        self.Tags = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.TotalCount = params.get("TotalCount")
-        self.Offset = params.get("Offset")
-        self.Limit = params.get("Limit")
-        if params.get("Tags") is not None:
-            self.Tags = []
-            for item in params.get("Tags"):
-                obj = Tag()
+        if params.get("Members") is not None:
+            self.Members = []
+            for item in params.get("Members"):
+                obj = OrgMember()
                 obj._deserialize(item)
-                self.Tags.append(obj)
+                self.Members.append(obj)
+        self.TotalCount = params.get("TotalCount")
         self.RequestId = params.get("RequestId")
 
 
-class DescribeTagsRequest(AbstractModel):
-    """DescribeTags请求参数结构体
+class ListOrganizationNodeMembersRequest(AbstractModel):
+    """ListOrganizationNodeMembers请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TagKey: 标签键,与标签值同时存在或同时不存在，不存在时表示查询该用户所有标签
-        :type TagKey: str
-        :param TagValue: 标签值,与标签键同时存在或同时不存在，不存在时表示查询该用户所有标签
-        :type TagValue: str
-        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
+        :param NodeId: 企业组织单元ID
+        :type NodeId: int
+        :param Offset: 偏移量
         :type Offset: int
-        :param Limit: 每页大小，默认为 15
+        :param Limit: 限制数目
         :type Limit: int
-        :param CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
-        :type CreateUin: int
         """
-        self.TagKey = None
-        self.TagValue = None
+        self.NodeId = None
         self.Offset = None
         self.Limit = None
-        self.CreateUin = None
 
 
     def _deserialize(self, params):
-        self.TagKey = params.get("TagKey")
-        self.TagValue = params.get("TagValue")
+        self.NodeId = params.get("NodeId")
         self.Offset = params.get("Offset")
         self.Limit = params.get("Limit")
-        self.CreateUin = params.get("CreateUin")
 
 
-class DescribeTagsResponse(AbstractModel):
-    """DescribeTags返回参数结构体
+class ListOrganizationNodeMembersResponse(AbstractModel):
+    """ListOrganizationNodeMembers返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TotalCount: 结果总数
+        :param TotalCount: 总数目
         :type TotalCount: int
-        :param Offset: 数据位移偏量
-        :type Offset: int
-        :param Limit: 每页大小
-        :type Limit: int
-        :param Tags: 标签列表
-        :type Tags: list of TagWithDelete
+        :param Members: 成员列表
+        :type Members: list of OrgMember
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
         self.TotalCount = None
-        self.Offset = None
-        self.Limit = None
-        self.Tags = None
+        self.Members = None
         self.RequestId = None
 
 
     def _deserialize(self, params):
         self.TotalCount = params.get("TotalCount")
-        self.Offset = params.get("Offset")
-        self.Limit = params.get("Limit")
-        if params.get("Tags") is not None:
-            self.Tags = []
-            for item in params.get("Tags"):
-                obj = TagWithDelete()
+        if params.get("Members") is not None:
+            self.Members = []
+            for item in params.get("Members"):
+                obj = OrgMember()
                 obj._deserialize(item)
-                self.Tags.append(obj)
+                self.Members.append(obj)
         self.RequestId = params.get("RequestId")
 
 
-class ModifyResourceTagsRequest(AbstractModel):
-    """ModifyResourceTags请求参数结构体
+class ListOrganizationNodesRequest(AbstractModel):
+    """ListOrganizationNodes请求参数结构体
+
+    """
+
+
+class ListOrganizationNodesResponse(AbstractModel):
+    """ListOrganizationNodes返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param Resource: 资源的六段式描述
-        :type Resource: str
-        :param ReplaceTags: 需要增加或修改的标签集合。如果Resource描述的资源未关联输入的标签键，则增加关联；若已关联，则将该资源关联的键对应的标签值修改为输入值。本接口中ReplaceTags和DeleteTags二者必须存在其一，且二者不能包含相同的标签键
-        :type ReplaceTags: list of Tag
-        :param DeleteTags: 需要解关联的标签集合。本接口中ReplaceTags和DeleteTags二者必须存在其一，且二者不能包含相同的标签键
-        :type DeleteTags: list of TagKeyObject
+        :param Nodes: 企业组织单元列表
+        :type Nodes: list of OrgNode
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
         """
-        self.Resource = None
-        self.ReplaceTags = None
-        self.DeleteTags = None
+        self.Nodes = None
+        self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.Resource = params.get("Resource")
-        if params.get("ReplaceTags") is not None:
-            self.ReplaceTags = []
-            for item in params.get("ReplaceTags"):
-                obj = Tag()
+        if params.get("Nodes") is not None:
+            self.Nodes = []
+            for item in params.get("Nodes"):
+                obj = OrgNode()
                 obj._deserialize(item)
-                self.ReplaceTags.append(obj)
-        if params.get("DeleteTags") is not None:
-            self.DeleteTags = []
-            for item in params.get("DeleteTags"):
-                obj = TagKeyObject()
-                obj._deserialize(item)
-                self.DeleteTags.append(obj)
+                self.Nodes.append(obj)
+        self.RequestId = params.get("RequestId")
 
 
-class ModifyResourceTagsResponse(AbstractModel):
-    """ModifyResourceTags返回参数结构体
+class MoveOrganizationMembersToNodeRequest(AbstractModel):
+    """MoveOrganizationMembersToNode请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param NodeId: 组织单元ID
+        :type NodeId: int
+        :param Uins: 成员UIN列表
+        :type Uins: list of int non-negative
+        """
+        self.NodeId = None
+        self.Uins = None
+
+
+    def _deserialize(self, params):
+        self.NodeId = params.get("NodeId")
+        self.Uins = params.get("Uins")
+
+
+class MoveOrganizationMembersToNodeResponse(AbstractModel):
+    """MoveOrganizationMembersToNode返回参数结构体
 
     """
 
     def __init__(self):
         """
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
@@ -580,201 +675,274 @@
         self.RequestId = None
 
 
     def _deserialize(self, params):
         self.RequestId = params.get("RequestId")
 
 
-class ResourceTag(AbstractModel):
-    """资源标签
+class OrgInvitation(AbstractModel):
+    """企业组织邀请
 
     """
 
     def __init__(self):
         """
-        :param ResourceRegion: 资源所在地域
-注意：此字段可能返回 null，表示取不到有效值。
-        :type ResourceRegion: str
-        :param ServiceType: 业务类型
-注意：此字段可能返回 null，表示取不到有效值。
-        :type ServiceType: str
-        :param ResourcePrefix: 资源前缀
-注意：此字段可能返回 null，表示取不到有效值。
-        :type ResourcePrefix: str
-        :param ResourceId: 资源唯一标记
-注意：此字段可能返回 null，表示取不到有效值。
-        :type ResourceId: str
-        :param Tags: 资源标签
-注意：此字段可能返回 null，表示取不到有效值。
-        :type Tags: list of Tag
+        :param Id: 邀请ID
+        :type Id: int
+        :param Uin: 被邀请UIN
+        :type Uin: int
+        :param HostUin: 创建者UIN
+        :type HostUin: int
+        :param HostName: 创建者名称
+        :type HostName: str
+        :param HostMail: 创建者邮箱
+        :type HostMail: str
+        :param Status: 邀请状态。-1：已过期，0：正常，1：已接受，2：已失效，3：已取消
+        :type Status: int
+        :param Name: 名称
+        :type Name: str
+        :param Remark: 备注
+        :type Remark: str
+        :param OrgType: 企业组织类型
+        :type OrgType: int
+        :param InviteTime: 邀请时间
+        :type InviteTime: str
+        :param ExpireTime: 过期时间
+        :type ExpireTime: str
         """
-        self.ResourceRegion = None
-        self.ServiceType = None
-        self.ResourcePrefix = None
-        self.ResourceId = None
-        self.Tags = None
+        self.Id = None
+        self.Uin = None
+        self.HostUin = None
+        self.HostName = None
+        self.HostMail = None
+        self.Status = None
+        self.Name = None
+        self.Remark = None
+        self.OrgType = None
+        self.InviteTime = None
+        self.ExpireTime = None
 
 
     def _deserialize(self, params):
-        self.ResourceRegion = params.get("ResourceRegion")
-        self.ServiceType = params.get("ServiceType")
-        self.ResourcePrefix = params.get("ResourcePrefix")
-        self.ResourceId = params.get("ResourceId")
-        if params.get("Tags") is not None:
-            self.Tags = []
-            for item in params.get("Tags"):
-                obj = Tag()
-                obj._deserialize(item)
-                self.Tags.append(obj)
+        self.Id = params.get("Id")
+        self.Uin = params.get("Uin")
+        self.HostUin = params.get("HostUin")
+        self.HostName = params.get("HostName")
+        self.HostMail = params.get("HostMail")
+        self.Status = params.get("Status")
+        self.Name = params.get("Name")
+        self.Remark = params.get("Remark")
+        self.OrgType = params.get("OrgType")
+        self.InviteTime = params.get("InviteTime")
+        self.ExpireTime = params.get("ExpireTime")
 
 
-class Tag(AbstractModel):
-    """表示一个标签键值对
+class OrgMember(AbstractModel):
+    """企业组织成员
 
     """
 
     def __init__(self):
         """
-        :param TagKey: 标签键
-        :type TagKey: str
-        :param TagValue: 标签值
-        :type TagValue: str
+        :param Uin: UIN
+        :type Uin: int
+        :param Name: 名称
+        :type Name: str
+        :param Remark: 备注
+        :type Remark: str
+        :param JoinTime: 加入时间
+        :type JoinTime: str
         """
-        self.TagKey = None
-        self.TagValue = None
+        self.Uin = None
+        self.Name = None
+        self.Remark = None
+        self.JoinTime = None
 
 
     def _deserialize(self, params):
-        self.TagKey = params.get("TagKey")
-        self.TagValue = params.get("TagValue")
+        self.Uin = params.get("Uin")
+        self.Name = params.get("Name")
+        self.Remark = params.get("Remark")
+        self.JoinTime = params.get("JoinTime")
 
 
-class TagFilter(AbstractModel):
-    """tag过滤数组多个是与的关系
+class OrgNode(AbstractModel):
+    """企业组织单元
 
     """
 
     def __init__(self):
         """
-        :param TagKey: 标签键
-        :type TagKey: str
-        :param TagValue: 标签值数组 多个值的话是或的关系
-        :type TagValue: list of str
+        :param NodeId: 组织单元ID
+        :type NodeId: int
+        :param Name: 名称
+        :type Name: str
+        :param ParentNodeId: 父单元ID
+        :type ParentNodeId: int
+        :param MemberCount: 成员数量
+        :type MemberCount: int
         """
-        self.TagKey = None
-        self.TagValue = None
+        self.NodeId = None
+        self.Name = None
+        self.ParentNodeId = None
+        self.MemberCount = None
 
 
     def _deserialize(self, params):
-        self.TagKey = params.get("TagKey")
-        self.TagValue = params.get("TagValue")
+        self.NodeId = params.get("NodeId")
+        self.Name = params.get("Name")
+        self.ParentNodeId = params.get("ParentNodeId")
+        self.MemberCount = params.get("MemberCount")
 
 
-class TagKeyObject(AbstractModel):
-    """标签键对象
+class QuitOrganizationRequest(AbstractModel):
+    """QuitOrganization请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TagKey: 标签键
-        :type TagKey: str
+        :param OrgId: 企业组织ID
+        :type OrgId: int
         """
-        self.TagKey = None
+        self.OrgId = None
 
 
     def _deserialize(self, params):
-        self.TagKey = params.get("TagKey")
+        self.OrgId = params.get("OrgId")
 
 
-class TagResource(AbstractModel):
-    """标签键值对以及资源ID
+class QuitOrganizationResponse(AbstractModel):
+    """QuitOrganization返回参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TagKey: 标签键
-        :type TagKey: str
-        :param TagValue: 标签值
-        :type TagValue: str
-        :param ResourceId: 资源ID
-        :type ResourceId: str
-        :param TagKeyMd5: 标签键MD5值
-        :type TagKeyMd5: str
-        :param TagValueMd5: 标签值MD5值
-        :type TagValueMd5: str
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
         """
-        self.TagKey = None
-        self.TagValue = None
-        self.ResourceId = None
-        self.TagKeyMd5 = None
-        self.TagValueMd5 = None
+        self.RequestId = None
 
 
     def _deserialize(self, params):
-        self.TagKey = params.get("TagKey")
-        self.TagValue = params.get("TagValue")
-        self.ResourceId = params.get("ResourceId")
-        self.TagKeyMd5 = params.get("TagKeyMd5")
-        self.TagValueMd5 = params.get("TagValueMd5")
+        self.RequestId = params.get("RequestId")
 
 
-class TagWithDelete(AbstractModel):
-    """表示一个标签键值对以及是否允许删除
+class SendOrganizationInvitationRequest(AbstractModel):
+    """SendOrganizationInvitation请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TagKey: 标签键
-        :type TagKey: str
-        :param TagValue: 标签值
-        :type TagValue: str
-        :param CanDelete: 是否可以删除
-        :type CanDelete: int
+        :param InviteUin: 被邀请账户UIN
+        :type InviteUin: int
+        :param Name: 名称
+        :type Name: str
+        :param Remark: 备注
+        :type Remark: str
         """
-        self.TagKey = None
-        self.TagValue = None
-        self.CanDelete = None
+        self.InviteUin = None
+        self.Name = None
+        self.Remark = None
 
 
     def _deserialize(self, params):
-        self.TagKey = params.get("TagKey")
-        self.TagValue = params.get("TagValue")
-        self.CanDelete = params.get("CanDelete")
+        self.InviteUin = params.get("InviteUin")
+        self.Name = params.get("Name")
+        self.Remark = params.get("Remark")
+
+
+class SendOrganizationInvitationResponse(AbstractModel):
+    """SendOrganizationInvitation返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.RequestId = params.get("RequestId")
+
+
+class UpdateOrganizationMemberRequest(AbstractModel):
+    """UpdateOrganizationMember请求参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param MemberUin: 成员UIN
+        :type MemberUin: int
+        :param Name: 名称
+        :type Name: str
+        :param Remark: 备注
+        :type Remark: str
+        """
+        self.MemberUin = None
+        self.Name = None
+        self.Remark = None
+
+
+    def _deserialize(self, params):
+        self.MemberUin = params.get("MemberUin")
+        self.Name = params.get("Name")
+        self.Remark = params.get("Remark")
+
+
+class UpdateOrganizationMemberResponse(AbstractModel):
+    """UpdateOrganizationMember返回参数结构体
+
+    """
+
+    def __init__(self):
+        """
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.RequestId = params.get("RequestId")
 
 
-class UpdateResourceTagValueRequest(AbstractModel):
-    """UpdateResourceTagValue请求参数结构体
+class UpdateOrganizationNodeRequest(AbstractModel):
+    """UpdateOrganizationNode请求参数结构体
 
     """
 
     def __init__(self):
         """
-        :param TagKey: 资源关联的标签键
-        :type TagKey: str
-        :param TagValue: 修改后的标签值
-        :type TagValue: str
-        :param Resource: 资源的六段式描述
-        :type Resource: str
+        :param NodeId: 企业组织单元ID
+        :type NodeId: int
+        :param Name: 名称
+        :type Name: str
+        :param ParentNodeId: 父单元ID
+        :type ParentNodeId: int
         """
-        self.TagKey = None
-        self.TagValue = None
-        self.Resource = None
+        self.NodeId = None
+        self.Name = None
+        self.ParentNodeId = None
 
 
     def _deserialize(self, params):
-        self.TagKey = params.get("TagKey")
-        self.TagValue = params.get("TagValue")
-        self.Resource = params.get("Resource")
+        self.NodeId = params.get("NodeId")
+        self.Name = params.get("Name")
+        self.ParentNodeId = params.get("ParentNodeId")
 
 
-class UpdateResourceTagValueResponse(AbstractModel):
-    """UpdateResourceTagValue返回参数结构体
+class UpdateOrganizationNodeResponse(AbstractModel):
+    """UpdateOrganizationNode返回参数结构体
 
     """
 
     def __init__(self):
         """
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tag/v20180813/tag_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tag/v20180813/tag_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/es/v20180416/es_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/es/v20180416/es_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/es/v20180416/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/es/v20180416/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cfs/v20190719/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cfs/v20190719/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/cfs/v20190719/cfs_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/cfs/v20190719/cfs_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tsf/v20180326/tsf_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tsf/v20180326/tsf_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/tsf/v20180326/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/tsf/v20180326/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/monitor/v20180724/monitor_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/monitor/v20180724/monitor_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/monitor/v20180724/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/monitor/v20180724/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/iottid/v20190411/models.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/iottid/v20190411/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud/iottid/v20190411/iottid_client.py` & `tencentcloud-sdk-python-3.0.99/tencentcloud/iottid/v20190411/iottid_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/setup.py` & `tencentcloud-sdk-python-3.0.99/setup.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-3.0.98/PKG-INFO` & `tencentcloud-sdk-python-3.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: tencentcloud-sdk-python
-Version: 3.0.98
+Version: 3.0.99
 Summary: Tencent Cloud SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Maintainer-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud_sdk_python.egg-info/PKG-INFO` & `tencentcloud-sdk-python-3.0.99/tencentcloud_sdk_python.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: tencentcloud-sdk-python
-Version: 3.0.98
+Version: 3.0.99
 Summary: Tencent Cloud SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Maintainer-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-3.0.98/tencentcloud_sdk_python.egg-info/SOURCES.txt` & `tencentcloud-sdk-python-3.0.99/tencentcloud_sdk_python.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -268,14 +268,17 @@
 tencentcloud/mariadb/v20170312/__init__.py
 tencentcloud/mariadb/v20170312/mariadb_client.py
 tencentcloud/mariadb/v20170312/models.py
 tencentcloud/mongodb/__init__.py
 tencentcloud/mongodb/v20180408/__init__.py
 tencentcloud/mongodb/v20180408/models.py
 tencentcloud/mongodb/v20180408/mongodb_client.py
+tencentcloud/mongodb/v20190725/__init__.py
+tencentcloud/mongodb/v20190725/models.py
+tencentcloud/mongodb/v20190725/mongodb_client.py
 tencentcloud/monitor/__init__.py
 tencentcloud/monitor/v20180724/__init__.py
 tencentcloud/monitor/v20180724/models.py
 tencentcloud/monitor/v20180724/monitor_client.py
 tencentcloud/mps/__init__.py
 tencentcloud/mps/v20190612/__init__.py
 tencentcloud/mps/v20190612/models.py
@@ -292,14 +295,18 @@
 tencentcloud/nlp/v20190408/__init__.py
 tencentcloud/nlp/v20190408/models.py
 tencentcloud/nlp/v20190408/nlp_client.py
 tencentcloud/ocr/__init__.py
 tencentcloud/ocr/v20181119/__init__.py
 tencentcloud/ocr/v20181119/models.py
 tencentcloud/ocr/v20181119/ocr_client.py
+tencentcloud/organization/__init__.py
+tencentcloud/organization/v20181225/__init__.py
+tencentcloud/organization/v20181225/models.py
+tencentcloud/organization/v20181225/organization_client.py
 tencentcloud/partners/__init__.py
 tencentcloud/partners/v20180321/__init__.py
 tencentcloud/partners/v20180321/models.py
 tencentcloud/partners/v20180321/partners_client.py
 tencentcloud/postgres/__init__.py
 tencentcloud/postgres/v20170312/__init__.py
 tencentcloud/postgres/v20170312/models.py
@@ -308,14 +315,18 @@
 tencentcloud/redis/v20180412/__init__.py
 tencentcloud/redis/v20180412/models.py
 tencentcloud/redis/v20180412/redis_client.py
 tencentcloud/scf/__init__.py
 tencentcloud/scf/v20180416/__init__.py
 tencentcloud/scf/v20180416/models.py
 tencentcloud/scf/v20180416/scf_client.py
+tencentcloud/sms/__init__.py
+tencentcloud/sms/v20190711/__init__.py
+tencentcloud/sms/v20190711/models.py
+tencentcloud/sms/v20190711/sms_client.py
 tencentcloud/soe/__init__.py
 tencentcloud/soe/v20180724/__init__.py
 tencentcloud/soe/v20180724/models.py
 tencentcloud/soe/v20180724/soe_client.py
 tencentcloud/sqlserver/__init__.py
 tencentcloud/sqlserver/v20180328/__init__.py
 tencentcloud/sqlserver/v20180328/models.py
```

### Comparing `tencentcloud-sdk-python-3.0.98/README.rst` & `tencentcloud-sdk-python-3.0.99/README.rst`

 * *Files identical despite different names*

