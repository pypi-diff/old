# Comparing `tmp/tccli-3.0.98.1.tar.gz` & `tmp/tccli-3.0.99.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tccli-3.0.98.1.tar", last modified: Fri Oct 25 09:30:52 2019, max compression
+gzip compressed data, was "dist/tccli-3.0.99.1.tar", last modified: Mon Oct 28 08:58:38 2019, max compression
```

## Comparing `tccli-3.0.98.1.tar` & `tccli-3.0.99.1.tar`

### file list

```diff
@@ -1,581 +1,596 @@
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/
--rw-rw-rw-   0 root         (0) root         (0)     3553 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/showHelp.py
--rw-rw-rw-   0 root         (0) root         (0)    10502 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/configure.py
--rw-rw-rw-   0 root         (0) root         (0)      414 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/error_msg.py
--rw-rw-rw-   0 root         (0) root         (0)     1415 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/utils.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/colorama/
--rw-rw-rw-   0 root         (0) root         (0)     2403 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/colorama/ansi.py
--rw-rw-rw-   0 root         (0) root         (0)     5267 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/colorama/win32.py
--rw-rw-rw-   0 root         (0) root         (0)     9490 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/colorama/ansitowin32.py
--rw-rw-rw-   0 root         (0) root         (0)      232 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/colorama/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     5883 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/colorama/winterm.py
--rw-rw-rw-   0 root         (0) root         (0)     1663 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/colorama/initialise.py
--rw-rw-rw-   0 root         (0) root         (0)     4216 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/text.py
--rw-rw-rw-   0 root         (0) root         (0)     3752 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/help_template.py
--rw-rw-rw-   0 root         (0) root         (0)     6365 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/format_output.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/captcha/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/captcha/v20190722/
--rw-rw-rw-   0 root         (0) root         (0)     1299 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/captcha/v20190722/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/captcha/v20190722/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/captcha/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     8063 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/captcha/captcha_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/kms/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/kms/v20190118/
--rw-rw-rw-   0 root         (0) root         (0)    12109 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/kms/v20190118/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/kms/v20190118/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    39872 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/kms/kms_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/kms/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/faceid/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/faceid/v20180301/
--rw-rw-rw-   0 root         (0) root         (0)    10089 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/faceid/v20180301/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/faceid/v20180301/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      221 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/faceid/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    25333 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/faceid/faceid_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/chdfs/
--rw-rw-rw-   0 root         (0) root         (0)    32281 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/chdfs/chdfs_client.py
--rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/chdfs/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/chdfs/v20190718/
--rw-rw-rw-   0 root         (0) root         (0)     5637 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/chdfs/v20190718/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/chdfs/v20190718/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/clb/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/clb/v20180317/
--rw-rw-rw-   0 root         (0) root         (0)    31643 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/clb/v20180317/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/clb/v20180317/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/clb/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    62803 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/clb/clb_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/bizlive/
--rw-rw-rw-   0 root         (0) root         (0)    10730 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bizlive/bizlive_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/bizlive/v20190313/
--rw-rw-rw-   0 root         (0) root         (0)     1805 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bizlive/v20190313/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bizlive/v20190313/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bizlive/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/bmvpc/
--rw-rw-rw-   0 root         (0) root         (0)    97199 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bmvpc/bmvpc_client.py
--rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bmvpc/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/bmvpc/v20180625/
--rw-rw-rw-   0 root         (0) root         (0)    32042 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bmvpc/v20180625/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bmvpc/v20180625/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/ds/
--rw-rw-rw-   0 root         (0) root         (0)    25366 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ds/ds_client.py
--rw-rw-rw-   0 root         (0) root         (0)      197 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ds/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/ds/v20180523/
--rw-rw-rw-   0 root         (0) root         (0)     9899 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ds/v20180523/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ds/v20180523/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cam/
--rw-rw-rw-   0 root         (0) root         (0)    67735 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cam/cam_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cam/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cam/v20190116/
--rw-rw-rw-   0 root         (0) root         (0)    17085 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cam/v20190116/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cam/v20190116/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/drm/
--rw-rw-rw-   0 root         (0) root         (0)    16943 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/drm/drm_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/drm/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/drm/v20181115/
--rw-rw-rw-   0 root         (0) root         (0)     6623 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/drm/v20181115/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/drm/v20181115/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/live/
--rw-rw-rw-   0 root         (0) root         (0)   155194 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/live/live_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/live/v20180801/
--rw-rw-rw-   0 root         (0) root         (0)    60013 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/live/v20180801/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/live/v20180801/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/live/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/iai/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/iai/v20180301/
--rw-rw-rw-   0 root         (0) root         (0)    22717 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iai/v20180301/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iai/v20180301/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    38123 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iai/iai_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iai/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/iotexplorer/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/iotexplorer/v20190423/
--rw-rw-rw-   0 root         (0) root         (0)     7925 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iotexplorer/v20190423/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iotexplorer/v20190423/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    38709 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iotexplorer/iotexplorer_client.py
--rw-rw-rw-   0 root         (0) root         (0)      251 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iotexplorer/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tiems/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tiems/v20190416/
--rw-rw-rw-   0 root         (0) root         (0)     3933 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tiems/v20190416/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tiems/v20190416/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    18282 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tiems/tiems_client.py
--rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tiems/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/partners/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/partners/v20180321/
--rw-rw-rw-   0 root         (0) root         (0)     8268 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/partners/v20180321/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/partners/v20180321/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    28352 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/partners/partners_client.py
--rw-rw-rw-   0 root         (0) root         (0)      233 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/partners/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/habo/
--rw-rw-rw-   0 root         (0) root         (0)     8920 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/habo/habo_client.py
--rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/habo/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/habo/v20181203/
--rw-rw-rw-   0 root         (0) root         (0)      878 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/habo/v20181203/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/habo/v20181203/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/sqlserver/
--rw-rw-rw-   0 root         (0) root         (0)      239 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/sqlserver/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    65530 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/sqlserver/sqlserver_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/sqlserver/v20180328/
--rw-rw-rw-   0 root         (0) root         (0)    19262 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/sqlserver/v20180328/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/sqlserver/v20180328/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/youmall/
--rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/youmall/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/youmall/v20180228/
--rw-rw-rw-   0 root         (0) root         (0)    20738 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/youmall/v20180228/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/youmall/v20180228/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    55906 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/youmall/youmall_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/tav/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/tav/v20190118/
--rw-rw-rw-   0 root         (0) root         (0)     1559 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tav/v20190118/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tav/v20190118/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    11675 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tav/tav_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tav/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/bmlb/
--rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bmlb/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    83988 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bmlb/bmlb_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/bmlb/v20180625/
--rw-rw-rw-   0 root         (0) root         (0)    36563 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bmlb/v20180625/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bmlb/v20180625/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/hcm/
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/hcm/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     7763 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/hcm/hcm_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/hcm/v20181106/
--rw-rw-rw-   0 root         (0) root         (0)     1391 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/hcm/v20181106/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/hcm/v20181106/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tci/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tci/v20190318/
--rw-rw-rw-   0 root         (0) root         (0)    35024 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tci/v20190318/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tci/v20190318/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    70479 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tci/tci_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tci/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/tbaas/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/tbaas/v20180416/
--rw-rw-rw-   0 root         (0) root         (0)    12772 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tbaas/v20180416/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tbaas/v20180416/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tbaas/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    29050 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tbaas/tbaas_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tics/
--rw-rw-rw-   0 root         (0) root         (0)    11812 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tics/tics_client.py
--rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tics/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tics/v20181115/
--rw-rw-rw-   0 root         (0) root         (0)     1896 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tics/v20181115/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tics/v20181115/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/bri/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/bri/v20190328/
--rw-rw-rw-   0 root         (0) root         (0)      762 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bri/v20190328/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bri/v20190328/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bri/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     7542 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bri/bri_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/ticm/
--rw-rw-rw-   0 root         (0) root         (0)     7696 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ticm/ticm_client.py
--rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ticm/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/ticm/v20181127/
--rw-rw-rw-   0 root         (0) root         (0)     1575 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ticm/v20181127/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ticm/v20181127/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/billing/
--rw-rw-rw-   0 root         (0) root         (0)    23297 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/billing/billing_client.py
--rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/billing/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/billing/v20180709/
--rw-rw-rw-   0 root         (0) root         (0)     8218 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/billing/v20180709/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/billing/v20180709/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cloudaudit/
--rw-rw-rw-   0 root         (0) root         (0)    23726 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cloudaudit/cloudaudit_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cloudaudit/v20190319/
--rw-rw-rw-   0 root         (0) root         (0)     7236 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cloudaudit/v20190319/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cloudaudit/v20190319/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      245 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cloudaudit/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cws/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cws/v20180312/
--rw-rw-rw-   0 root         (0) root         (0)     7088 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cws/v20180312/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cws/v20180312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cws/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    33702 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cws/cws_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/ic/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/ic/v20190307/
--rw-rw-rw-   0 root         (0) root         (0)     1358 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ic/v20190307/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ic/v20190307/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      197 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ic/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    13117 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ic/ic_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tbp/
--rw-rw-rw-   0 root         (0) root         (0)    10915 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tbp/tbp_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tbp/v20190311/
--rw-rw-rw-   0 root         (0) root         (0)     2063 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tbp/v20190311/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tbp/v20190311/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tbp/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tbp/v20190627/
--rw-rw-rw-   0 root         (0) root         (0)     1609 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tbp/v20190627/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tbp/v20190627/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tiia/
--rw-rw-rw-   0 root         (0) root         (0)    16006 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tiia/tiia_client.py
--rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tiia/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tiia/v20190529/
--rw-rw-rw-   0 root         (0) root         (0)     7583 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tiia/v20190529/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tiia/v20190529/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/msp/
--rw-rw-rw-   0 root         (0) root         (0)    16783 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/msp/msp_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/msp/v20180319/
--rw-rw-rw-   0 root         (0) root         (0)     3718 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/msp/v20180319/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/msp/v20180319/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/msp/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/ms/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/ms/v20180408/
--rw-rw-rw-   0 root         (0) root         (0)     7067 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ms/v20180408/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ms/v20180408/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    28522 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ms/ms_client.py
--rw-rw-rw-   0 root         (0) root         (0)      197 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ms/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cis/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cis/v20180408/
--rw-rw-rw-   0 root         (0) root         (0)     2992 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cis/v20180408/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cis/v20180408/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cis/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    16612 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cis/cis_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/bm/
--rw-rw-rw-   0 root         (0) root         (0)    83043 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bm/bm_client.py
--rw-rw-rw-   0 root         (0) root         (0)      197 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bm/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/bm/v20180423/
--rw-rw-rw-   0 root         (0) root         (0)    29814 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bm/v20180423/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bm/v20180423/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/tbm/
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tbm/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    19967 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tbm/tbm_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tbm/v20180129/
--rw-rw-rw-   0 root         (0) root         (0)     5108 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tbm/v20180129/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tbm/v20180129/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cds/
--rw-rw-rw-   0 root         (0) root         (0)    13571 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cds/cds_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cds/v20180420/
--rw-rw-rw-   0 root         (0) root         (0)     2050 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cds/v20180420/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cds/v20180420/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cds/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cr/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cr/v20180321/
--rw-rw-rw-   0 root         (0) root         (0)     7856 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cr/v20180321/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cr/v20180321/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    21624 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cr/cr_client.py
--rw-rw-rw-   0 root         (0) root         (0)      197 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cr/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cdn/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cdn/v20180606/
--rw-rw-rw-   0 root         (0) root         (0)    18294 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cdn/v20180606/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cdn/v20180606/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cdn/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    28542 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cdn/cdn_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/gaap/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/gaap/v20180529/
--rw-rw-rw-   0 root         (0) root         (0)    50040 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/gaap/v20180529/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/gaap/v20180529/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/gaap/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   122129 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/gaap/gaap_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/trtc/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/trtc/v20190722/
--rw-rw-rw-   0 root         (0) root         (0)      901 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/trtc/v20190722/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/trtc/v20190722/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/trtc/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     9017 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/trtc/trtc_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tts/
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tts/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tts/v20190823/
--rw-rw-rw-   0 root         (0) root         (0)     2391 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tts/v20190823/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tts/v20190823/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     7976 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tts/tts_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/scf/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/scf/v20180416/
--rw-rw-rw-   0 root         (0) root         (0)    16994 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/scf/v20180416/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/scf/v20180416/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/scf/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    34982 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/scf/scf_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/postgres/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/postgres/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)    14147 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/postgres/v20170312/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/postgres/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    45652 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/postgres/postgres_client.py
--rw-rw-rw-   0 root         (0) root         (0)      233 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/postgres/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cdb/
--rw-rw-rw-   0 root         (0) root         (0)   120940 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cdb/cdb_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cdb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cdb/v20170320/
--rw-rw-rw-   0 root         (0) root         (0)    62273 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cdb/v20170320/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cdb/v20170320/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/ocr/
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ocr/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    69114 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ocr/ocr_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/ocr/v20181119/
--rw-rw-rw-   0 root         (0) root         (0)    51619 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ocr/v20181119/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ocr/v20181119/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/asr/
--rw-rw-rw-   0 root         (0) root         (0)    11054 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/asr/asr_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/asr/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/asr/v20190614/
--rw-rw-rw-   0 root         (0) root         (0)     5385 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/asr/v20190614/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/asr/v20190614/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/mariadb/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/mariadb/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)    27768 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/mariadb/v20170312/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/mariadb/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/mariadb/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    64096 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/mariadb/mariadb_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/sts/
--rw-rw-rw-   0 root         (0) root         (0)    10708 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/sts/sts_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/sts/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/sts/v20180813/
--rw-rw-rw-   0 root         (0) root         (0)     2329 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/sts/v20180813/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/sts/v20180813/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/dts/
--rw-rw-rw-   0 root         (0) root         (0)    31104 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/dts/dts_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/dts/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/dts/v20180330/
--rw-rw-rw-   0 root         (0) root         (0)    13045 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/dts/v20180330/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/dts/v20180330/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/aai/
--rw-rw-rw-   0 root         (0) root         (0)    13190 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/aai/aai_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/aai/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/aai/v20180522/
--rw-rw-rw-   0 root         (0) root         (0)     6956 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/aai/v20180522/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/aai/v20180522/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/ecc/
--rw-rw-rw-   0 root         (0) root         (0)    10945 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ecc/ecc_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ecc/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/ecc/v20181213/
--rw-rw-rw-   0 root         (0) root         (0)     4257 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ecc/v20181213/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/ecc/v20181213/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/bmeip/
--rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bmeip/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/bmeip/v20180625/
--rw-rw-rw-   0 root         (0) root         (0)     7505 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bmeip/v20180625/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bmeip/v20180625/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    33405 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/bmeip/bmeip_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/mps/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/mps/v20190612/
--rw-rw-rw-   0 root         (0) root         (0)    31786 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/mps/v20190612/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/mps/v20190612/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    62649 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/mps/mps_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/mps/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1066 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/services/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/soe/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/soe/v20180724/
--rw-rw-rw-   0 root         (0) root         (0)    12618 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/soe/v20180724/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/soe/v20180724/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    14207 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/soe/soe_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/soe/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cvm/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cvm/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)    95255 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cvm/v20170312/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cvm/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   106509 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cvm/cvm_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cvm/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/yunsou/
--rw-rw-rw-   0 root         (0) root         (0)    10269 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/yunsou/yunsou_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/yunsou/v20180504/
--rw-rw-rw-   0 root         (0) root         (0)     2916 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/yunsou/v20180504/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/yunsou/v20180504/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      221 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/yunsou/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/batch/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/batch/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)    13566 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/batch/v20170312/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/batch/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    47164 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/batch/batch_client.py
--rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/batch/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/dcdb/
--rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/dcdb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/dcdb/v20180411/
--rw-rw-rw-   0 root         (0) root         (0)    24592 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/dcdb/v20180411/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/dcdb/v20180411/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    56729 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/dcdb/dcdb_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/redis/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/redis/v20180412/
--rw-rw-rw-   0 root         (0) root         (0)    16445 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/redis/v20180412/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/redis/v20180412/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/redis/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    53358 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/redis/redis_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/vpc/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/vpc/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)   113648 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/vpc/v20170312/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/vpc/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   254360 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/vpc/vpc_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/vpc/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cbs/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cbs/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)    36719 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cbs/v20170312/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cbs/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    53700 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cbs/cbs_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cbs/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tia/
--rw-rw-rw-   0 root         (0) root         (0)    21272 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tia/tia_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tia/v20180226/
--rw-rw-rw-   0 root         (0) root         (0)     8787 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tia/v20180226/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tia/v20180226/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tia/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/autoscaling/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/autoscaling/v20180419/
--rw-rw-rw-   0 root         (0) root         (0)    55492 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/autoscaling/v20180419/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/autoscaling/v20180419/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      251 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/autoscaling/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    76309 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/autoscaling/autoscaling_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/facefusion/
--rw-rw-rw-   0 root         (0) root         (0)     9465 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/facefusion/facefusion_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/facefusion/v20181201/
--rw-rw-rw-   0 root         (0) root         (0)     2758 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/facefusion/v20181201/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/facefusion/v20181201/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      245 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/facefusion/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/yunjing/
--rw-rw-rw-   0 root         (0) root         (0)    91952 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/yunjing/yunjing_client.py
--rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/yunjing/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/yunjing/v20180228/
--rw-rw-rw-   0 root         (0) root         (0)    23868 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/yunjing/v20180228/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/yunjing/v20180228/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/vod/
--rw-rw-rw-   0 root         (0) root         (0)   139753 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/vod/vod_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/vod/v20180717/
--rw-rw-rw-   0 root         (0) root         (0)    96252 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/vod/v20180717/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/vod/v20180717/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/vod/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/mongodb/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/mongodb/v20180408/
--rw-rw-rw-   0 root         (0) root         (0)    10945 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/mongodb/v20180408/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/mongodb/v20180408/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    26816 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/mongodb/mongodb_client.py
--rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/mongodb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cim/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cim/v20190318/
--rw-rw-rw-   0 root         (0) root         (0)      171 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cim/v20190318/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cim/v20190318/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     7459 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cim/cim_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cim/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/wss/
--rw-rw-rw-   0 root         (0) root         (0)    10701 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/wss/wss_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/wss/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/wss/v20180426/
--rw-rw-rw-   0 root         (0) root         (0)     1909 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/wss/v20180426/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/wss/v20180426/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/dc/
--rw-rw-rw-   0 root         (0) root         (0)    24923 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/dc/dc_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/dc/v20180410/
--rw-rw-rw-   0 root         (0) root         (0)     9220 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/dc/v20180410/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/dc/v20180410/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      197 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/dc/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/gme/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/gme/v20180711/
--rw-rw-rw-   0 root         (0) root         (0)     7964 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/gme/v20180711/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/gme/v20180711/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    13718 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/gme/gme_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/gme/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/nlp/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/nlp/v20190408/
--rw-rw-rw-   0 root         (0) root         (0)    11695 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/nlp/v20190408/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/nlp/v20190408/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    26830 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/nlp/nlp_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/nlp/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/iotcloud/
--rw-rw-rw-   0 root         (0) root         (0)    56451 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iotcloud/iotcloud_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/iotcloud/v20180614/
--rw-rw-rw-   0 root         (0) root         (0)    15424 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iotcloud/v20180614/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iotcloud/v20180614/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      233 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iotcloud/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/iot/
--rw-rw-rw-   0 root         (0) root         (0)    70839 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iot/iot_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/iot/v20180123/
--rw-rw-rw-   0 root         (0) root         (0)    16115 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iot/v20180123/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iot/v20180123/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iot/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tkgdq/
--rw-rw-rw-   0 root         (0) root         (0)    10311 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tkgdq/tkgdq_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tkgdq/v20190411/
--rw-rw-rw-   0 root         (0) root         (0)     1271 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tkgdq/v20190411/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tkgdq/v20190411/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tkgdq/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tmt/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tmt/v20180321/
--rw-rw-rw-   0 root         (0) root         (0)     5618 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tmt/v20180321/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tmt/v20180321/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tmt/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    12382 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tmt/tmt_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cms/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cms/v20190321/
--rw-rw-rw-   0 root         (0) root         (0)     8410 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cms/v20190321/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cms/v20190321/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    22341 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cms/cms_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cms/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tcb/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tcb/v20180608/
--rw-rw-rw-   0 root         (0) root         (0)     1469 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tcb/v20180608/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tcb/v20180608/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tcb/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    11689 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tcb/tcb_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tke/
--rw-rw-rw-   0 root         (0) root         (0)    34035 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tke/tke_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tke/v20180525/
--rw-rw-rw-   0 root         (0) root         (0)    10698 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tke/v20180525/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tke/v20180525/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tke/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/emr/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/emr/v20190103/
--rw-rw-rw-   0 root         (0) root         (0)     7245 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/emr/v20190103/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/emr/v20190103/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/emr/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    22156 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/emr/emr_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/tag/
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tag/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/tag/v20180813/
--rw-rw-rw-   0 root         (0) root         (0)     5629 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tag/v20180813/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tag/v20180813/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    22742 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tag/tag_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/es/
--rw-rw-rw-   0 root         (0) root         (0)    21664 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/es/es_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/es/v20180416/
--rw-rw-rw-   0 root         (0) root         (0)    11423 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/es/v20180416/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/es/v20180416/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      197 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/es/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cfs/
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cfs/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/cfs/v20190719/
--rw-rw-rw-   0 root         (0) root         (0)     8146 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cfs/v20190719/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cfs/v20190719/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    33324 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/cfs/cfs_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tsf/
--rw-rw-rw-   0 root         (0) root         (0)   108316 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tsf/tsf_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tsf/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:52.000000 tccli-3.0.98.1/tccli/services/tsf/v20180326/
--rw-rw-rw-   0 root         (0) root         (0)    30499 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tsf/v20180326/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/tsf/v20180326/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/monitor/
--rw-rw-rw-   0 root         (0) root         (0)     9235 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/monitor/monitor_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/monitor/v20180724/
--rw-rw-rw-   0 root         (0) root         (0)     1491 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/monitor/v20180724/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/monitor/v20180724/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/monitor/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/iottid/
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/services/iottid/v20190411/
--rw-rw-rw-   0 root         (0) root         (0)     2188 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iottid/v20190411/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iottid/v20190411/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      221 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iottid/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    18590 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/services/iottid/iottid_client.py
--rw-rw-rw-   0 root         (0) root         (0)     2466 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/completer.py
--rw-rw-rw-   0 root         (0) root         (0)    14793 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/table.py
--rw-rw-rw-   0 root         (0) root         (0)     2563 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/nice_command.py
--rw-rw-rw-   0 root         (0) root         (0)       26 2019-10-25 09:30:39.000000 tccli-3.0.98.1/tccli/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    26837 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/six.py
--rw-rw-rw-   0 root         (0) root         (0)      353 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/options_define.py
--rw-rw-rw-   0 root         (0) root         (0)     2113 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/main.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli/advance/
--rw-rw-rw-   0 root         (0) root         (0)     2873 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/advance/userConfigHandler.py
--rw-rw-rw-   0 root         (0) root         (0)    11514 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/advance/userProfileHandler.py
--rw-rw-rw-   0 root         (0) root         (0)       23 2019-10-25 09:30:38.000000 tccli-3.0.98.1/tccli/advance/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)       67 2019-10-25 09:30:52.000000 tccli-3.0.98.1/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)     2611 2019-10-25 09:30:38.000000 tccli-3.0.98.1/setup.py
--rw-rw-rw-   0 root         (0) root         (0)      935 2019-10-25 09:30:52.000000 tccli-3.0.98.1/PKG-INFO
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/jmespath/
--rw-rw-rw-   0 root         (0) root         (0)    13111 2019-10-25 09:30:38.000000 tccli-3.0.98.1/jmespath/functions.py
--rw-rw-rw-   0 root         (0) root         (0)     2026 2019-10-25 09:30:38.000000 tccli-3.0.98.1/jmespath/ast.py
--rw-rw-rw-   0 root         (0) root         (0)     4250 2019-10-25 09:30:38.000000 tccli-3.0.98.1/jmespath/exceptions.py
--rw-rw-rw-   0 root         (0) root         (0)     1932 2019-10-25 09:30:38.000000 tccli-3.0.98.1/jmespath/compat.py
--rw-rw-rw-   0 root         (0) root         (0)    19890 2019-10-25 09:30:38.000000 tccli-3.0.98.1/jmespath/parser.py
--rw-rw-rw-   0 root         (0) root         (0)      224 2019-10-25 09:30:38.000000 tccli-3.0.98.1/jmespath/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     7927 2019-10-25 09:30:38.000000 tccli-3.0.98.1/jmespath/visitor.py
--rw-rw-rw-   0 root         (0) root         (0)     5696 2019-10-25 09:30:38.000000 tccli-3.0.98.1/jmespath/lexer.py
--rw-rw-rw-   0 root         (0) root         (0)      298 2019-10-25 09:30:38.000000 tccli-3.0.98.1/MANIFEST.in
-drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli.egg-info/
--rw-rw-rw-   0 root         (0) root         (0)       86 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli.egg-info/entry_points.txt
--rw-rw-rw-   0 root         (0) root         (0)       32 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli.egg-info/requires.txt
--rw-rw-rw-   0 root         (0) root         (0)      935 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli.egg-info/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)    14038 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli.egg-info/SOURCES.txt
--rw-rw-rw-   0 root         (0) root         (0)       15 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli.egg-info/top_level.txt
--rw-rw-rw-   0 root         (0) root         (0)        1 2019-10-25 09:30:51.000000 tccli-3.0.98.1/tccli.egg-info/dependency_links.txt
--rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-25 09:30:38.000000 tccli-3.0.98.1/README.rst
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/
+-rw-rw-rw-   0 root         (0) root         (0)     3553 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/showHelp.py
+-rw-rw-rw-   0 root         (0) root         (0)    10502 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/configure.py
+-rw-rw-rw-   0 root         (0) root         (0)      414 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/error_msg.py
+-rw-rw-rw-   0 root         (0) root         (0)     1415 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/utils.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/colorama/
+-rw-rw-rw-   0 root         (0) root         (0)     2403 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/colorama/ansi.py
+-rw-rw-rw-   0 root         (0) root         (0)     5267 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/colorama/win32.py
+-rw-rw-rw-   0 root         (0) root         (0)     9490 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/colorama/ansitowin32.py
+-rw-rw-rw-   0 root         (0) root         (0)      232 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/colorama/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     5883 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/colorama/winterm.py
+-rw-rw-rw-   0 root         (0) root         (0)     1663 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/colorama/initialise.py
+-rw-rw-rw-   0 root         (0) root         (0)     4216 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/text.py
+-rw-rw-rw-   0 root         (0) root         (0)     3752 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/help_template.py
+-rw-rw-rw-   0 root         (0) root         (0)     6365 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/format_output.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/captcha/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/captcha/v20190722/
+-rw-rw-rw-   0 root         (0) root         (0)     1299 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/captcha/v20190722/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/captcha/v20190722/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/captcha/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     8063 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/captcha/captcha_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/kms/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/kms/v20190118/
+-rw-rw-rw-   0 root         (0) root         (0)    12358 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/kms/v20190118/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/kms/v20190118/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    41239 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/kms/kms_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/kms/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/faceid/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/faceid/v20180301/
+-rw-rw-rw-   0 root         (0) root         (0)    10089 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/faceid/v20180301/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/faceid/v20180301/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      221 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/faceid/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    25333 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/faceid/faceid_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/chdfs/
+-rw-rw-rw-   0 root         (0) root         (0)    32281 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/chdfs/chdfs_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/chdfs/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/chdfs/v20190718/
+-rw-rw-rw-   0 root         (0) root         (0)     5637 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/chdfs/v20190718/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/chdfs/v20190718/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/clb/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/clb/v20180317/
+-rw-rw-rw-   0 root         (0) root         (0)    31643 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/clb/v20180317/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/clb/v20180317/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/clb/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    62803 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/clb/clb_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/bizlive/
+-rw-rw-rw-   0 root         (0) root         (0)    10730 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/bizlive/bizlive_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/bizlive/v20190313/
+-rw-rw-rw-   0 root         (0) root         (0)     1805 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/bizlive/v20190313/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/bizlive/v20190313/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/bizlive/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/bmvpc/
+-rw-rw-rw-   0 root         (0) root         (0)    97199 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bmvpc/bmvpc_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bmvpc/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/bmvpc/v20180625/
+-rw-rw-rw-   0 root         (0) root         (0)    32042 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bmvpc/v20180625/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bmvpc/v20180625/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/organization/
+-rw-rw-rw-   0 root         (0) root         (0)    35165 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/organization/organization_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      257 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/organization/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/organization/v20181225/
+-rw-rw-rw-   0 root         (0) root         (0)     4416 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/organization/v20181225/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/organization/v20181225/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/ds/
+-rw-rw-rw-   0 root         (0) root         (0)    25366 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ds/ds_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      197 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ds/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/ds/v20180523/
+-rw-rw-rw-   0 root         (0) root         (0)     9899 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ds/v20180523/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ds/v20180523/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cam/
+-rw-rw-rw-   0 root         (0) root         (0)    67735 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cam/cam_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cam/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cam/v20190116/
+-rw-rw-rw-   0 root         (0) root         (0)    17085 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cam/v20190116/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cam/v20190116/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/drm/
+-rw-rw-rw-   0 root         (0) root         (0)    16943 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/drm/drm_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/drm/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/drm/v20181115/
+-rw-rw-rw-   0 root         (0) root         (0)     6623 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/drm/v20181115/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/drm/v20181115/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/live/
+-rw-rw-rw-   0 root         (0) root         (0)   155294 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/live/live_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/live/v20180801/
+-rw-rw-rw-   0 root         (0) root         (0)    60634 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/live/v20180801/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/live/v20180801/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/live/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/iai/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/iai/v20180301/
+-rw-rw-rw-   0 root         (0) root         (0)    22717 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iai/v20180301/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iai/v20180301/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    38123 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iai/iai_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iai/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/iotexplorer/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/iotexplorer/v20190423/
+-rw-rw-rw-   0 root         (0) root         (0)     7925 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iotexplorer/v20190423/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iotexplorer/v20190423/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    38709 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iotexplorer/iotexplorer_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      251 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iotexplorer/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tiems/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tiems/v20190416/
+-rw-rw-rw-   0 root         (0) root         (0)     3933 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tiems/v20190416/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tiems/v20190416/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    18282 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tiems/tiems_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tiems/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/partners/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/partners/v20180321/
+-rw-rw-rw-   0 root         (0) root         (0)     8268 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/partners/v20180321/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/partners/v20180321/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    28352 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/partners/partners_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      233 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/partners/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/habo/
+-rw-rw-rw-   0 root         (0) root         (0)     8920 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/habo/habo_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/habo/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/habo/v20181203/
+-rw-rw-rw-   0 root         (0) root         (0)      878 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/habo/v20181203/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/habo/v20181203/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/sqlserver/
+-rw-rw-rw-   0 root         (0) root         (0)      239 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/sqlserver/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    65530 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/sqlserver/sqlserver_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/sqlserver/v20180328/
+-rw-rw-rw-   0 root         (0) root         (0)    19262 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/sqlserver/v20180328/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/sqlserver/v20180328/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/youmall/
+-rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/youmall/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/youmall/v20180228/
+-rw-rw-rw-   0 root         (0) root         (0)    20738 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/youmall/v20180228/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/youmall/v20180228/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    55906 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/youmall/youmall_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tav/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tav/v20190118/
+-rw-rw-rw-   0 root         (0) root         (0)     1559 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tav/v20190118/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tav/v20190118/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    11675 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tav/tav_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tav/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/bmlb/
+-rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bmlb/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    83988 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bmlb/bmlb_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/bmlb/v20180625/
+-rw-rw-rw-   0 root         (0) root         (0)    36563 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bmlb/v20180625/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bmlb/v20180625/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/hcm/
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/hcm/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     7763 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/hcm/hcm_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/hcm/v20181106/
+-rw-rw-rw-   0 root         (0) root         (0)     1391 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/hcm/v20181106/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/hcm/v20181106/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tci/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tci/v20190318/
+-rw-rw-rw-   0 root         (0) root         (0)    35253 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tci/v20190318/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tci/v20190318/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    70548 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tci/tci_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tci/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tbaas/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tbaas/v20180416/
+-rw-rw-rw-   0 root         (0) root         (0)    12772 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tbaas/v20180416/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tbaas/v20180416/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tbaas/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    29050 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tbaas/tbaas_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tics/
+-rw-rw-rw-   0 root         (0) root         (0)    11812 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tics/tics_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tics/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tics/v20181115/
+-rw-rw-rw-   0 root         (0) root         (0)     1896 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tics/v20181115/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tics/v20181115/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/bri/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/bri/v20190328/
+-rw-rw-rw-   0 root         (0) root         (0)      762 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/bri/v20190328/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/bri/v20190328/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/bri/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     7542 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/bri/bri_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/ticm/
+-rw-rw-rw-   0 root         (0) root         (0)     7696 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ticm/ticm_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ticm/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/ticm/v20181127/
+-rw-rw-rw-   0 root         (0) root         (0)     1575 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ticm/v20181127/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ticm/v20181127/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/billing/
+-rw-rw-rw-   0 root         (0) root         (0)    23297 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/billing/billing_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/billing/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/billing/v20180709/
+-rw-rw-rw-   0 root         (0) root         (0)     8218 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/billing/v20180709/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/billing/v20180709/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cloudaudit/
+-rw-rw-rw-   0 root         (0) root         (0)    23726 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cloudaudit/cloudaudit_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cloudaudit/v20190319/
+-rw-rw-rw-   0 root         (0) root         (0)     7236 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cloudaudit/v20190319/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cloudaudit/v20190319/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      245 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cloudaudit/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cws/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cws/v20180312/
+-rw-rw-rw-   0 root         (0) root         (0)     7088 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cws/v20180312/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cws/v20180312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cws/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    33702 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cws/cws_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/ic/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/ic/v20190307/
+-rw-rw-rw-   0 root         (0) root         (0)     1358 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ic/v20190307/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ic/v20190307/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      197 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ic/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    13117 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ic/ic_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tbp/
+-rw-rw-rw-   0 root         (0) root         (0)    10915 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tbp/tbp_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tbp/v20190311/
+-rw-rw-rw-   0 root         (0) root         (0)     2063 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tbp/v20190311/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tbp/v20190311/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tbp/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tbp/v20190627/
+-rw-rw-rw-   0 root         (0) root         (0)     1655 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tbp/v20190627/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tbp/v20190627/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tiia/
+-rw-rw-rw-   0 root         (0) root         (0)    16006 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tiia/tiia_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tiia/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tiia/v20190529/
+-rw-rw-rw-   0 root         (0) root         (0)     7583 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tiia/v20190529/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tiia/v20190529/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/msp/
+-rw-rw-rw-   0 root         (0) root         (0)    16783 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/msp/msp_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/msp/v20180319/
+-rw-rw-rw-   0 root         (0) root         (0)     3718 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/msp/v20180319/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/msp/v20180319/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/msp/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/ms/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/ms/v20180408/
+-rw-rw-rw-   0 root         (0) root         (0)     7067 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ms/v20180408/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ms/v20180408/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    28522 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ms/ms_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      197 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ms/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cis/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cis/v20180408/
+-rw-rw-rw-   0 root         (0) root         (0)     2992 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cis/v20180408/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cis/v20180408/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cis/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    16612 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cis/cis_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/bm/
+-rw-rw-rw-   0 root         (0) root         (0)    83043 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bm/bm_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      197 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bm/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/bm/v20180423/
+-rw-rw-rw-   0 root         (0) root         (0)    29814 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bm/v20180423/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bm/v20180423/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tbm/
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tbm/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    19967 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tbm/tbm_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tbm/v20180129/
+-rw-rw-rw-   0 root         (0) root         (0)     5108 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tbm/v20180129/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tbm/v20180129/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cds/
+-rw-rw-rw-   0 root         (0) root         (0)    13571 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cds/cds_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cds/v20180420/
+-rw-rw-rw-   0 root         (0) root         (0)     2050 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cds/v20180420/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cds/v20180420/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cds/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cr/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cr/v20180321/
+-rw-rw-rw-   0 root         (0) root         (0)     7856 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cr/v20180321/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cr/v20180321/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    21624 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cr/cr_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      197 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cr/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cdn/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cdn/v20180606/
+-rw-rw-rw-   0 root         (0) root         (0)    18294 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cdn/v20180606/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cdn/v20180606/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cdn/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    28542 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cdn/cdn_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/gaap/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/gaap/v20180529/
+-rw-rw-rw-   0 root         (0) root         (0)    50040 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/gaap/v20180529/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/gaap/v20180529/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/gaap/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   122129 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/gaap/gaap_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/trtc/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/trtc/v20190722/
+-rw-rw-rw-   0 root         (0) root         (0)      901 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/trtc/v20190722/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/trtc/v20190722/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/trtc/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     9017 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/trtc/trtc_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tts/
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tts/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tts/v20190823/
+-rw-rw-rw-   0 root         (0) root         (0)     2391 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tts/v20190823/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tts/v20190823/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     7976 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tts/tts_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/scf/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/scf/v20180416/
+-rw-rw-rw-   0 root         (0) root         (0)    16994 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/scf/v20180416/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/scf/v20180416/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/scf/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    34982 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/scf/scf_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/postgres/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/postgres/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)    14147 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/postgres/v20170312/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/postgres/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    45652 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/postgres/postgres_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      233 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/postgres/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cdb/
+-rw-rw-rw-   0 root         (0) root         (0)   126912 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cdb/cdb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cdb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cdb/v20170320/
+-rw-rw-rw-   0 root         (0) root         (0)    64828 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cdb/v20170320/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cdb/v20170320/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/ocr/
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/ocr/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    69114 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/ocr/ocr_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/ocr/v20181119/
+-rw-rw-rw-   0 root         (0) root         (0)    51619 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/ocr/v20181119/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/ocr/v20181119/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/asr/
+-rw-rw-rw-   0 root         (0) root         (0)    11054 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/asr/asr_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/asr/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/asr/v20190614/
+-rw-rw-rw-   0 root         (0) root         (0)     5584 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/asr/v20190614/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/asr/v20190614/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/mariadb/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/mariadb/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)    27768 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/mariadb/v20170312/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/mariadb/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/mariadb/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    64096 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/mariadb/mariadb_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/sts/
+-rw-rw-rw-   0 root         (0) root         (0)    10708 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/sts/sts_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/sts/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/sts/v20180813/
+-rw-rw-rw-   0 root         (0) root         (0)     2329 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/sts/v20180813/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/sts/v20180813/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/dts/
+-rw-rw-rw-   0 root         (0) root         (0)    31104 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/dts/dts_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/dts/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/dts/v20180330/
+-rw-rw-rw-   0 root         (0) root         (0)    13045 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/dts/v20180330/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/dts/v20180330/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/aai/
+-rw-rw-rw-   0 root         (0) root         (0)    13190 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/aai/aai_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/aai/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/aai/v20180522/
+-rw-rw-rw-   0 root         (0) root         (0)     6956 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/aai/v20180522/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/aai/v20180522/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/ecc/
+-rw-rw-rw-   0 root         (0) root         (0)    10945 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ecc/ecc_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ecc/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/ecc/v20181213/
+-rw-rw-rw-   0 root         (0) root         (0)     4257 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ecc/v20181213/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/ecc/v20181213/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/bmeip/
+-rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bmeip/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/bmeip/v20180625/
+-rw-rw-rw-   0 root         (0) root         (0)     7505 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bmeip/v20180625/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bmeip/v20180625/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    33405 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/bmeip/bmeip_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/mps/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/mps/v20190612/
+-rw-rw-rw-   0 root         (0) root         (0)    31786 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/mps/v20190612/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/mps/v20190612/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    62649 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/mps/mps_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/mps/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1066 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/services/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/soe/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/soe/v20180724/
+-rw-rw-rw-   0 root         (0) root         (0)    12618 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/soe/v20180724/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/soe/v20180724/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    14207 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/soe/soe_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/soe/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cvm/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cvm/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)    95255 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cvm/v20170312/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cvm/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   106509 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cvm/cvm_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cvm/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/yunsou/
+-rw-rw-rw-   0 root         (0) root         (0)    10269 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/yunsou/yunsou_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/yunsou/v20180504/
+-rw-rw-rw-   0 root         (0) root         (0)     2916 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/yunsou/v20180504/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/yunsou/v20180504/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      221 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/yunsou/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/batch/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/batch/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)    13566 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/batch/v20170312/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/batch/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    47164 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/batch/batch_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/batch/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/dcdb/
+-rw-rw-rw-   0 root         (0) root         (0)      209 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/dcdb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/dcdb/v20180411/
+-rw-rw-rw-   0 root         (0) root         (0)    24592 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/dcdb/v20180411/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/dcdb/v20180411/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    56729 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/dcdb/dcdb_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/redis/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/redis/v20180412/
+-rw-rw-rw-   0 root         (0) root         (0)    16445 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/redis/v20180412/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/redis/v20180412/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/redis/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    53358 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/redis/redis_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/vpc/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/vpc/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)   119831 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/vpc/v20170312/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/vpc/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   263935 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/vpc/vpc_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/vpc/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cbs/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cbs/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)    36719 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cbs/v20170312/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cbs/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    53700 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cbs/cbs_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cbs/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tia/
+-rw-rw-rw-   0 root         (0) root         (0)    21272 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tia/tia_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tia/v20180226/
+-rw-rw-rw-   0 root         (0) root         (0)     8787 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tia/v20180226/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tia/v20180226/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tia/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/autoscaling/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/autoscaling/v20180419/
+-rw-rw-rw-   0 root         (0) root         (0)    55492 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/autoscaling/v20180419/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/autoscaling/v20180419/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      251 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/autoscaling/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    76309 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/autoscaling/autoscaling_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/facefusion/
+-rw-rw-rw-   0 root         (0) root         (0)     9465 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/facefusion/facefusion_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/facefusion/v20181201/
+-rw-rw-rw-   0 root         (0) root         (0)     3257 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/facefusion/v20181201/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/facefusion/v20181201/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      245 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/facefusion/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/yunjing/
+-rw-rw-rw-   0 root         (0) root         (0)    91952 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/yunjing/yunjing_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/yunjing/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/yunjing/v20180228/
+-rw-rw-rw-   0 root         (0) root         (0)    23868 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/yunjing/v20180228/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/yunjing/v20180228/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/vod/
+-rw-rw-rw-   0 root         (0) root         (0)   139753 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/vod/vod_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/vod/v20180717/
+-rw-rw-rw-   0 root         (0) root         (0)    96483 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/vod/v20180717/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/vod/v20180717/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/vod/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/mongodb/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/mongodb/v20180408/
+-rw-rw-rw-   0 root         (0) root         (0)    10945 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/mongodb/v20180408/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/mongodb/v20180408/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    34599 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/mongodb/mongodb_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/mongodb/v20190725/
+-rw-rw-rw-   0 root         (0) root         (0)    11463 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/mongodb/v20190725/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/mongodb/v20190725/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/mongodb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/sms/
+-rw-rw-rw-   0 root         (0) root         (0)    14006 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/sms/sms_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/sms/v20190711/
+-rw-rw-rw-   0 root         (0) root         (0)     4456 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/sms/v20190711/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/sms/v20190711/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/sms/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cim/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cim/v20190318/
+-rw-rw-rw-   0 root         (0) root         (0)      171 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cim/v20190318/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cim/v20190318/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     7459 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cim/cim_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/cim/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/wss/
+-rw-rw-rw-   0 root         (0) root         (0)    10701 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/wss/wss_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/wss/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/wss/v20180426/
+-rw-rw-rw-   0 root         (0) root         (0)     1909 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/wss/v20180426/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/wss/v20180426/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/dc/
+-rw-rw-rw-   0 root         (0) root         (0)    24923 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/dc/dc_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/dc/v20180410/
+-rw-rw-rw-   0 root         (0) root         (0)     9220 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/dc/v20180410/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/dc/v20180410/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      197 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/dc/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/gme/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/gme/v20180711/
+-rw-rw-rw-   0 root         (0) root         (0)    10546 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/gme/v20180711/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/gme/v20180711/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    18430 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/gme/gme_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/gme/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/nlp/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/nlp/v20190408/
+-rw-rw-rw-   0 root         (0) root         (0)    11695 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/nlp/v20190408/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/nlp/v20190408/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    26830 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/nlp/nlp_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/nlp/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/iotcloud/
+-rw-rw-rw-   0 root         (0) root         (0)    56451 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iotcloud/iotcloud_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/iotcloud/v20180614/
+-rw-rw-rw-   0 root         (0) root         (0)    15424 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iotcloud/v20180614/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iotcloud/v20180614/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      233 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iotcloud/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/iot/
+-rw-rw-rw-   0 root         (0) root         (0)    70839 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iot/iot_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/iot/v20180123/
+-rw-rw-rw-   0 root         (0) root         (0)    16115 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iot/v20180123/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iot/v20180123/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/iot/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tkgdq/
+-rw-rw-rw-   0 root         (0) root         (0)    10311 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tkgdq/tkgdq_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tkgdq/v20190411/
+-rw-rw-rw-   0 root         (0) root         (0)     1271 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tkgdq/v20190411/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tkgdq/v20190411/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      215 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tkgdq/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tmt/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tmt/v20180321/
+-rw-rw-rw-   0 root         (0) root         (0)     5618 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tmt/v20180321/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tmt/v20180321/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tmt/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    12382 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tmt/tmt_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cms/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cms/v20190321/
+-rw-rw-rw-   0 root         (0) root         (0)     8410 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cms/v20190321/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cms/v20190321/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    22341 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cms/cms_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cms/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tcb/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tcb/v20180608/
+-rw-rw-rw-   0 root         (0) root         (0)     1469 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tcb/v20180608/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tcb/v20180608/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tcb/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    11689 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tcb/tcb_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tke/
+-rw-rw-rw-   0 root         (0) root         (0)    34035 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tke/tke_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tke/v20180525/
+-rw-rw-rw-   0 root         (0) root         (0)    10698 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tke/v20180525/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tke/v20180525/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tke/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/emr/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/emr/v20190103/
+-rw-rw-rw-   0 root         (0) root         (0)     7245 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/emr/v20190103/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/emr/v20190103/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/emr/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    22156 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/emr/emr_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tag/
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tag/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tag/v20180813/
+-rw-rw-rw-   0 root         (0) root         (0)     5629 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tag/v20180813/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tag/v20180813/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    22742 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/tag/tag_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/es/
+-rw-rw-rw-   0 root         (0) root         (0)    21664 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/es/es_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/es/v20180416/
+-rw-rw-rw-   0 root         (0) root         (0)    11423 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/es/v20180416/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/es/v20180416/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      197 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/es/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cfs/
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cfs/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/cfs/v20190719/
+-rw-rw-rw-   0 root         (0) root         (0)     8146 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cfs/v20190719/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cfs/v20190719/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    33324 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/cfs/cfs_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tsf/
+-rw-rw-rw-   0 root         (0) root         (0)   108316 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tsf/tsf_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tsf/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/tsf/v20180326/
+-rw-rw-rw-   0 root         (0) root         (0)    30499 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tsf/v20180326/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:25.000000 tccli-3.0.99.1/tccli/services/tsf/v20180326/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/monitor/
+-rw-rw-rw-   0 root         (0) root         (0)     9235 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/monitor/monitor_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/monitor/v20180724/
+-rw-rw-rw-   0 root         (0) root         (0)     1491 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/monitor/v20180724/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/monitor/v20180724/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      227 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/monitor/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/iottid/
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/services/iottid/v20190411/
+-rw-rw-rw-   0 root         (0) root         (0)     2188 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/iottid/v20190411/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/iottid/v20190411/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      221 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/iottid/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    18590 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/services/iottid/iottid_client.py
+-rw-rw-rw-   0 root         (0) root         (0)     2466 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/completer.py
+-rw-rw-rw-   0 root         (0) root         (0)    14793 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/table.py
+-rw-rw-rw-   0 root         (0) root         (0)     2563 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/nice_command.py
+-rw-rw-rw-   0 root         (0) root         (0)       26 2019-10-28 08:58:26.000000 tccli-3.0.99.1/tccli/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    26837 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/six.py
+-rw-rw-rw-   0 root         (0) root         (0)      353 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/options_define.py
+-rw-rw-rw-   0 root         (0) root         (0)     2113 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/main.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli/advance/
+-rw-rw-rw-   0 root         (0) root         (0)     2873 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/advance/userConfigHandler.py
+-rw-rw-rw-   0 root         (0) root         (0)    11514 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/advance/userProfileHandler.py
+-rw-rw-rw-   0 root         (0) root         (0)       23 2019-10-28 08:58:15.000000 tccli-3.0.99.1/tccli/advance/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)       67 2019-10-28 08:58:38.000000 tccli-3.0.99.1/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)     2611 2019-10-28 08:58:15.000000 tccli-3.0.99.1/setup.py
+-rw-rw-rw-   0 root         (0) root         (0)      935 2019-10-28 08:58:38.000000 tccli-3.0.99.1/PKG-INFO
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/jmespath/
+-rw-rw-rw-   0 root         (0) root         (0)    13111 2019-10-28 08:58:15.000000 tccli-3.0.99.1/jmespath/functions.py
+-rw-rw-rw-   0 root         (0) root         (0)     2026 2019-10-28 08:58:15.000000 tccli-3.0.99.1/jmespath/ast.py
+-rw-rw-rw-   0 root         (0) root         (0)     4250 2019-10-28 08:58:15.000000 tccli-3.0.99.1/jmespath/exceptions.py
+-rw-rw-rw-   0 root         (0) root         (0)     1932 2019-10-28 08:58:15.000000 tccli-3.0.99.1/jmespath/compat.py
+-rw-rw-rw-   0 root         (0) root         (0)    19890 2019-10-28 08:58:15.000000 tccli-3.0.99.1/jmespath/parser.py
+-rw-rw-rw-   0 root         (0) root         (0)      224 2019-10-28 08:58:15.000000 tccli-3.0.99.1/jmespath/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     7927 2019-10-28 08:58:15.000000 tccli-3.0.99.1/jmespath/visitor.py
+-rw-rw-rw-   0 root         (0) root         (0)     5696 2019-10-28 08:58:15.000000 tccli-3.0.99.1/jmespath/lexer.py
+-rw-rw-rw-   0 root         (0) root         (0)      298 2019-10-28 08:58:15.000000 tccli-3.0.99.1/MANIFEST.in
+drwxrwxrwx   0 root         (0) root         (0)        0 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli.egg-info/
+-rw-rw-rw-   0 root         (0) root         (0)       86 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli.egg-info/entry_points.txt
+-rw-rw-rw-   0 root         (0) root         (0)       32 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli.egg-info/requires.txt
+-rw-rw-rw-   0 root         (0) root         (0)      935 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli.egg-info/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)    14453 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli.egg-info/SOURCES.txt
+-rw-rw-rw-   0 root         (0) root         (0)       15 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli.egg-info/top_level.txt
+-rw-rw-rw-   0 root         (0) root         (0)        1 2019-10-28 08:58:38.000000 tccli-3.0.99.1/tccli.egg-info/dependency_links.txt
+-rw-rw-rw-   0 root         (0) root         (0)        0 2019-10-28 08:58:15.000000 tccli-3.0.99.1/README.rst
```

### Comparing `tccli-3.0.98.1/tccli/showHelp.py` & `tccli-3.0.99.1/tccli/showHelp.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/configure.py` & `tccli-3.0.99.1/tccli/configure.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/utils.py` & `tccli-3.0.99.1/tccli/utils.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/colorama/ansi.py` & `tccli-3.0.99.1/tccli/colorama/ansi.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/colorama/win32.py` & `tccli-3.0.99.1/tccli/colorama/win32.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/colorama/ansitowin32.py` & `tccli-3.0.99.1/tccli/colorama/ansitowin32.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/colorama/winterm.py` & `tccli-3.0.99.1/tccli/colorama/winterm.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/colorama/initialise.py` & `tccli-3.0.99.1/tccli/colorama/initialise.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/text.py` & `tccli-3.0.99.1/tccli/text.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/help_template.py` & `tccli-3.0.99.1/tccli/help_template.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/format_output.py` & `tccli-3.0.99.1/tccli/format_output.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/captcha/v20190722/help.py` & `tccli-3.0.99.1/tccli/services/captcha/v20190722/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/captcha/captcha_client.py` & `tccli-3.0.99.1/tccli/services/captcha/captcha_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/kms/v20190118/help.py` & `tccli-3.0.99.1/tccli/services/kms/v20190118/help.py`

 * *Files 0% similar despite different names*

```diff
@@ -52,15 +52,15 @@
       },
       {
         "name": "KeyId",
         "desc": "指定导入密钥材料的CMK，需要和GetParametersForImport 指定的CMK相同。"
       },
       {
         "name": "ValidTo",
-        "desc": "密钥材料过期时间 unix 时间戳，不指定或者 0 表示密钥材料不会过期，若指定过期时间，需要大于当前时间点。"
+        "desc": "密钥材料过期时间 unix 时间戳，不指定或者 0 表示密钥材料不会过期，若指定过期时间，需要大于当前时间点，最大支持 2147443200。"
       }
     ],
     "desc": "用于导入密钥材料。只有类型为EXTERNAL 的CMK 才可以导入，导入的密钥材料使用 GetParametersForImport 获取的密钥进行加密。可以为指定的 CMK 重新导入密钥材料，并重新指定过期时间，但必须导入相同的密钥材料。CMK 密钥材料导入后不可以更换密钥材料。导入的密钥材料过期或者被删除后，指定的CMK将无法使用，需要再次导入相同的密钥材料才能正常使用。CMK是独立的，同样的密钥材料可导入不同的 CMK 中，但使用其中一个 CMK 加密的数据无法使用另一个 CMK解密。\n只有Enabled 和 PendingImport状态的CMK可以导入密钥材料。"
   },
   "DisableKey": {
     "params": [
       {
@@ -140,14 +140,23 @@
       {
         "name": "Role",
         "desc": "根据创建者角色筛选，默认 0 表示用户自己创建的cmk， 1 表示授权其它云产品自动创建的cmk"
       }
     ],
     "desc": "列出账号下面状态为Enabled， Disabled 和 PendingImport 的CMK KeyId 列表"
   },
+  "GenerateRandom": {
+    "params": [
+      {
+        "name": "NumberOfBytes",
+        "desc": "生成的随机数的长度。最小值为1， 最大值为1024。"
+      }
+    ],
+    "desc": "随机数生成接口。"
+  },
   "CreateKey": {
     "params": [
       {
         "name": "Alias",
         "desc": "作为密钥更容易辨识，更容易被人看懂的别名， 不可为空，1-60个字母数字 - _ 的组合。以 kms- 作为前缀的用于云产品使用，Alias 不可重复。"
       },
       {
```

### Comparing `tccli-3.0.98.1/tccli/services/kms/kms_client.py` & `tccli-3.0.99.1/tccli/services/kms/kms_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -391,14 +391,47 @@
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
+def doGenerateRandom(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("GenerateRandom", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "NumberOfBytes": Utils.try_to_json(argv, "--NumberOfBytes"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.KmsClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.GenerateRandomRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.GenerateRandom(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
 def doCreateKey(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
         show_help("CreateKey", g_param[OptionsDefine.Version])
         return
 
     param = {
@@ -855,14 +888,15 @@
     "DisableKey": doDisableKey,
     "GenerateDataKey": doGenerateDataKey,
     "CancelKeyDeletion": doCancelKeyDeletion,
     "GetKeyRotationStatus": doGetKeyRotationStatus,
     "GetServiceStatus": doGetServiceStatus,
     "ReEncrypt": doReEncrypt,
     "ListKeys": doListKeys,
+    "GenerateRandom": doGenerateRandom,
     "CreateKey": doCreateKey,
     "GetParametersForImport": doGetParametersForImport,
     "ListKeyDetail": doListKeyDetail,
     "DisableKeyRotation": doDisableKeyRotation,
     "EnableKeys": doEnableKeys,
     "ScheduleKeyDeletion": doScheduleKeyDeletion,
     "DescribeKey": doDescribeKey,
```

### Comparing `tccli-3.0.98.1/tccli/services/faceid/v20180301/help.py` & `tccli-3.0.99.1/tccli/services/faceid/v20180301/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/faceid/faceid_client.py` & `tccli-3.0.99.1/tccli/services/faceid/faceid_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/chdfs/chdfs_client.py` & `tccli-3.0.99.1/tccli/services/chdfs/chdfs_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/chdfs/v20190718/help.py` & `tccli-3.0.99.1/tccli/services/chdfs/v20190718/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/clb/v20180317/help.py` & `tccli-3.0.99.1/tccli/services/clb/v20180317/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/clb/clb_client.py` & `tccli-3.0.99.1/tccli/services/clb/clb_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/bizlive/bizlive_client.py` & `tccli-3.0.99.1/tccli/services/bizlive/bizlive_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/bizlive/v20190313/help.py` & `tccli-3.0.99.1/tccli/services/bizlive/v20190313/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/bmvpc/bmvpc_client.py` & `tccli-3.0.99.1/tccli/services/bmvpc/bmvpc_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/bmvpc/v20180625/help.py` & `tccli-3.0.99.1/tccli/services/bmvpc/v20180625/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/ds/ds_client.py` & `tccli-3.0.99.1/tccli/services/ds/ds_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/ds/v20180523/help.py` & `tccli-3.0.99.1/tccli/services/ds/v20180523/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cam/cam_client.py` & `tccli-3.0.99.1/tccli/services/cam/cam_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cam/v20190116/help.py` & `tccli-3.0.99.1/tccli/services/cam/v20190116/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/drm/drm_client.py` & `tccli-3.0.99.1/tccli/services/drm/drm_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/drm/v20181115/help.py` & `tccli-3.0.99.1/tccli/services/drm/v20181115/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/live/live_client.py` & `tccli-3.0.99.1/tccli/services/live/live_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -2179,19 +2179,21 @@
 def doDescribeLiveTranscodeDetailInfo(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
         show_help("DescribeLiveTranscodeDetailInfo", g_param[OptionsDefine.Version])
         return
 
     param = {
-        "DayTime": argv.get("--DayTime"),
         "PushDomain": argv.get("--PushDomain"),
         "StreamName": argv.get("--StreamName"),
+        "DayTime": argv.get("--DayTime"),
         "PageNum": Utils.try_to_json(argv, "--PageNum"),
         "PageSize": Utils.try_to_json(argv, "--PageSize"),
+        "StartDayTime": argv.get("--StartDayTime"),
+        "EndDayTime": argv.get("--EndDayTime"),
 
     }
     cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
     http_profile = HttpProfile(
         reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
         reqMethod="POST",
         endpoint=g_param[OptionsDefine.Endpoint]
```

### Comparing `tccli-3.0.98.1/tccli/services/live/v20180801/help.py` & `tccli-3.0.99.1/tccli/services/live/v20180801/help.py`

 * *Files 1% similar despite different names*

```diff
@@ -1247,35 +1247,43 @@
       }
     ],
     "desc": "解绑域名证书"
   },
   "DescribeLiveTranscodeDetailInfo": {
     "params": [
       {
-        "name": "DayTime",
-        "desc": "起始时间，北京时间，\n格式：yyyymmdd。\n注意：当前只支持查询近30天内某天的详细数据。"
-      },
-      {
         "name": "PushDomain",
         "desc": "推流域名。"
       },
       {
         "name": "StreamName",
         "desc": "流名称。"
       },
       {
+        "name": "DayTime",
+        "desc": "查询时间，北京时间，\n格式：yyyymmdd。\n注意：支持查询近3个月内某天的详细数据。"
+      },
+      {
         "name": "PageNum",
         "desc": "页数，默认1，\n不超过100页。"
       },
       {
         "name": "PageSize",
         "desc": "每页个数，默认20，\n范围：[10,1000]。"
+      },
+      {
+        "name": "StartDayTime",
+        "desc": "起始天时间，北京时间，\n格式：yyyymmdd。\n注意：支持查询近3个月内的详细数据。"
+      },
+      {
+        "name": "EndDayTime",
+        "desc": "结束天时间，北京时间，\n格式：yyyymmdd。\n注意：支持查询近3个月内的详细数据，注意DayTime 与（StartDayTime，EndDayTime）必须要传一个，如果都传，会以DayTime为准 。"
       }
     ],
-    "desc": "支持查询某天的转码详细信息。\n注意：当前只支持查询近30天内某天的详细数据。"
+    "desc": "支持查询某天或某段时间的转码详细信息。"
   },
   "DescribeLogDownloadList": {
     "params": [
       {
         "name": "StartTime",
         "desc": "开始时间，北京时间。\n格式：yyyy-mm-dd HH:MM:SS。"
       },
@@ -1445,23 +1453,23 @@
     "params": [
       {
         "name": "AppName",
         "desc": "推流路径，与推流和播放地址中的AppName保持一致，默认为 live。"
       },
       {
         "name": "DomainName",
-        "desc": "您的加速域名。"
+        "desc": "您的推流域名。"
       },
       {
         "name": "StreamName",
         "desc": "流名称。"
       },
       {
         "name": "ResumeTime",
-        "desc": "恢复流的时间。UTC 格式，例如：2018-11-29T19:00:00Z。\n注意：\n1. 默认禁播90天，且最长支持禁播90天。\n2. 北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。"
+        "desc": "恢复流的时间。UTC 格式，例如：2018-11-29T19:00:00Z。\n注意：\n1. 默认禁播7天，且最长支持禁播90天。\n2. 北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。"
       },
       {
         "name": "Reason",
         "desc": "禁推原因。\n注明：请务必填写禁推原因，防止误操作。\n长度限制：2048字节。"
       }
     ],
     "desc": "禁止某条流的推送，可以预设某个时刻将流恢复。"
@@ -1637,15 +1645,15 @@
         "desc": "流名称。"
       },
       {
         "name": "TaskId",
         "desc": "任务ID，全局唯一标识录制任务。"
       }
     ],
-    "desc": "用于删除录制任务。"
+    "desc": "注：DeleteLiveRecord 接口仅用于删除录制任务记录，不具备停止录制的功能，也不能删除正在进行中的录制。如果需要停止录制任务，请使用终止录制[StopLiveRecord](/document/product/267/30146) 接口。"
   },
   "CreateLiveSnapshotRule": {
     "params": [
       {
         "name": "DomainName",
         "desc": "推流域名。"
       },
```

### Comparing `tccli-3.0.98.1/tccli/services/iai/v20180301/help.py` & `tccli-3.0.99.1/tccli/services/iai/v20180301/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/iai/iai_client.py` & `tccli-3.0.99.1/tccli/services/iai/iai_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/iotexplorer/v20190423/help.py` & `tccli-3.0.99.1/tccli/services/iotexplorer/v20190423/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/iotexplorer/iotexplorer_client.py` & `tccli-3.0.99.1/tccli/services/iotexplorer/iotexplorer_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tiems/v20190416/help.py` & `tccli-3.0.99.1/tccli/services/tiems/v20190416/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tiems/tiems_client.py` & `tccli-3.0.99.1/tccli/services/tiems/tiems_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/partners/v20180321/help.py` & `tccli-3.0.99.1/tccli/services/partners/v20180321/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/partners/partners_client.py` & `tccli-3.0.99.1/tccli/services/partners/partners_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/habo/habo_client.py` & `tccli-3.0.99.1/tccli/services/habo/habo_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/habo/v20181203/help.py` & `tccli-3.0.99.1/tccli/services/habo/v20181203/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/sqlserver/sqlserver_client.py` & `tccli-3.0.99.1/tccli/services/sqlserver/sqlserver_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/sqlserver/v20180328/help.py` & `tccli-3.0.99.1/tccli/services/sqlserver/v20180328/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/youmall/v20180228/help.py` & `tccli-3.0.99.1/tccli/services/youmall/v20180228/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/youmall/youmall_client.py` & `tccli-3.0.99.1/tccli/services/youmall/youmall_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tav/v20190118/help.py` & `tccli-3.0.99.1/tccli/services/tav/v20190118/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tav/tav_client.py` & `tccli-3.0.99.1/tccli/services/tav/tav_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/bmlb/bmlb_client.py` & `tccli-3.0.99.1/tccli/services/bmlb/bmlb_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/bmlb/v20180625/help.py` & `tccli-3.0.99.1/tccli/services/bmlb/v20180625/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/hcm/hcm_client.py` & `tccli-3.0.99.1/tccli/services/hcm/hcm_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/hcm/v20181106/help.py` & `tccli-3.0.99.1/tccli/services/hcm/v20181106/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tci/v20190318/help.py` & `tccli-3.0.99.1/tccli/services/tci/v20190318/help.py`

 * *Files 1% similar despite different names*

```diff
@@ -99,14 +99,18 @@
         "desc": "功能开关列表，表示是否需要打开相应的功能，返回相应的信息"
       },
       {
         "name": "FileType",
         "desc": "视频文件类型，默认点播，直播填 live_url"
       },
       {
+        "name": "MuteThreshold",
+        "desc": "静音阈值设置，如果静音检测开关开启，则静音时间超过这个阈值认为是静音片段，在结果中会返回, 没给的话默认值为3s"
+      },
+      {
         "name": "VocabLibNameList",
         "desc": "识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析"
       }
     ],
     "desc": "音频任务提交接口"
   },
   "CreateFace": {
```

### Comparing `tccli-3.0.98.1/tccli/services/tci/tci_client.py` & `tccli-3.0.99.1/tccli/services/tci/tci_client.py`

 * *Files 1% similar despite different names*

```diff
@@ -138,14 +138,15 @@
     param = {
         "Lang": Utils.try_to_json(argv, "--Lang"),
         "Url": argv.get("--Url"),
         "VoiceEncodeType": Utils.try_to_json(argv, "--VoiceEncodeType"),
         "VoiceFileType": Utils.try_to_json(argv, "--VoiceFileType"),
         "Functions": Utils.try_to_json(argv, "--Functions"),
         "FileType": argv.get("--FileType"),
+        "MuteThreshold": Utils.try_to_json(argv, "--MuteThreshold"),
         "VocabLibNameList": Utils.try_to_json(argv, "--VocabLibNameList"),
 
     }
     cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
     http_profile = HttpProfile(
         reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
         reqMethod="POST",
```

### Comparing `tccli-3.0.98.1/tccli/services/tbaas/v20180416/help.py` & `tccli-3.0.99.1/tccli/services/tbaas/v20180416/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tbaas/tbaas_client.py` & `tccli-3.0.99.1/tccli/services/tbaas/tbaas_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tics/tics_client.py` & `tccli-3.0.99.1/tccli/services/tics/tics_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tics/v20181115/help.py` & `tccli-3.0.99.1/tccli/services/tics/v20181115/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/bri/v20190328/help.py` & `tccli-3.0.99.1/tccli/services/bri/v20190328/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/bri/bri_client.py` & `tccli-3.0.99.1/tccli/services/bri/bri_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/ticm/ticm_client.py` & `tccli-3.0.99.1/tccli/services/ticm/ticm_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/ticm/v20181127/help.py` & `tccli-3.0.99.1/tccli/services/ticm/v20181127/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/billing/billing_client.py` & `tccli-3.0.99.1/tccli/services/billing/billing_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/billing/v20180709/help.py` & `tccli-3.0.99.1/tccli/services/billing/v20180709/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cloudaudit/cloudaudit_client.py` & `tccli-3.0.99.1/tccli/services/cloudaudit/cloudaudit_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cloudaudit/v20190319/help.py` & `tccli-3.0.99.1/tccli/services/cloudaudit/v20190319/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cws/v20180312/help.py` & `tccli-3.0.99.1/tccli/services/cws/v20180312/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cws/cws_client.py` & `tccli-3.0.99.1/tccli/services/cws/cws_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/ic/v20190307/help.py` & `tccli-3.0.99.1/tccli/services/ic/v20190307/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/ic/ic_client.py` & `tccli-3.0.99.1/tccli/services/ic/ic_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tbp/tbp_client.py` & `tccli-3.0.99.1/tccli/services/tbp/tbp_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tbp/v20190311/help.py` & `tccli-3.0.99.1/tccli/services/tbp/v20190311/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tbp/v20190627/help.py` & `tccli-3.0.99.1/tccli/services/tbp/v20190627/help.py`

 * *Files 5% similar despite different names*

```diff
@@ -13,15 +13,15 @@
       },
       {
         "name": "TerminalId",
         "desc": "终端标识，每个终端(或线程)对应一个，区分并发多用户。"
       },
       {
         "name": "PlatformType",
-        "desc": "平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount}。"
+        "desc": "平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount；企业微信: WXWork}。"
       }
     ],
     "desc": "会话重置接口。"
   },
   "TextProcess": {
     "params": [
       {
@@ -42,13 +42,13 @@
       },
       {
         "name": "SessionAttributes",
         "desc": "透传字段，透传给用户自定义的WebService服务。"
       },
       {
         "name": "PlatformType",
-        "desc": "平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount}。"
+        "desc": "平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount；企业微信: WXWork}。"
       }
     ],
     "desc": "接收调用侧的文本输入，返回应答文本。"
   }
 }
```

### Comparing `tccli-3.0.98.1/tccli/services/tiia/tiia_client.py` & `tccli-3.0.99.1/tccli/services/tiia/tiia_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tiia/v20190529/help.py` & `tccli-3.0.99.1/tccli/services/tiia/v20190529/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/msp/msp_client.py` & `tccli-3.0.99.1/tccli/services/msp/msp_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/msp/v20180319/help.py` & `tccli-3.0.99.1/tccli/services/msp/v20180319/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/ms/v20180408/help.py` & `tccli-3.0.99.1/tccli/services/ms/v20180408/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/ms/ms_client.py` & `tccli-3.0.99.1/tccli/services/ms/ms_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cis/v20180408/help.py` & `tccli-3.0.99.1/tccli/services/cis/v20180408/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cis/cis_client.py` & `tccli-3.0.99.1/tccli/services/cis/cis_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/bm/bm_client.py` & `tccli-3.0.99.1/tccli/services/bm/bm_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/bm/v20180423/help.py` & `tccli-3.0.99.1/tccli/services/bm/v20180423/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tbm/tbm_client.py` & `tccli-3.0.99.1/tccli/services/tbm/tbm_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tbm/v20180129/help.py` & `tccli-3.0.99.1/tccli/services/tbm/v20180129/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cds/cds_client.py` & `tccli-3.0.99.1/tccli/services/cds/cds_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cds/v20180420/help.py` & `tccli-3.0.99.1/tccli/services/cds/v20180420/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cr/v20180321/help.py` & `tccli-3.0.99.1/tccli/services/cr/v20180321/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cr/cr_client.py` & `tccli-3.0.99.1/tccli/services/cr/cr_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cdn/v20180606/help.py` & `tccli-3.0.99.1/tccli/services/cdn/v20180606/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cdn/cdn_client.py` & `tccli-3.0.99.1/tccli/services/cdn/cdn_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/gaap/v20180529/help.py` & `tccli-3.0.99.1/tccli/services/gaap/v20180529/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/gaap/gaap_client.py` & `tccli-3.0.99.1/tccli/services/gaap/gaap_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/trtc/v20190722/help.py` & `tccli-3.0.99.1/tccli/services/trtc/v20190722/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/trtc/trtc_client.py` & `tccli-3.0.99.1/tccli/services/trtc/trtc_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tts/v20190823/help.py` & `tccli-3.0.99.1/tccli/services/tts/v20190823/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tts/tts_client.py` & `tccli-3.0.99.1/tccli/services/tts/tts_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/scf/v20180416/help.py` & `tccli-3.0.99.1/tccli/services/scf/v20180416/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/scf/scf_client.py` & `tccli-3.0.99.1/tccli/services/scf/scf_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/postgres/v20170312/help.py` & `tccli-3.0.99.1/tccli/services/postgres/v20170312/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/postgres/postgres_client.py` & `tccli-3.0.99.1/tccli/services/postgres/postgres_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cdb/cdb_client.py` & `tccli-3.0.99.1/tccli/services/cdb/cdb_client.py`

 * *Files 1% similar despite different names*

```diff
@@ -508,14 +508,15 @@
 
     param = {
         "InstanceId": argv.get("--InstanceId"),
         "ExpireDays": Utils.try_to_json(argv, "--ExpireDays"),
         "StartTime": argv.get("--StartTime"),
         "BackupMethod": argv.get("--BackupMethod"),
         "BinlogExpireDays": Utils.try_to_json(argv, "--BinlogExpireDays"),
+        "BackupTimeWindow": Utils.try_to_json(argv, "--BackupTimeWindow"),
 
     }
     cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
     http_profile = HttpProfile(
         reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
         reqMethod="POST",
         endpoint=g_param[OptionsDefine.Endpoint]
@@ -567,38 +568,38 @@
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
-def doStopDBImportJob(argv, arglist):
+def doDeleteDeployGroups(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
-        show_help("StopDBImportJob", g_param[OptionsDefine.Version])
+        show_help("DeleteDeployGroups", g_param[OptionsDefine.Version])
         return
 
     param = {
-        "AsyncRequestId": argv.get("--AsyncRequestId"),
+        "DeployGroupIds": Utils.try_to_json(argv, "--DeployGroupIds"),
 
     }
     cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
     http_profile = HttpProfile(
         reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
         reqMethod="POST",
         endpoint=g_param[OptionsDefine.Endpoint]
     )
     profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
     mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
     client = mod.CdbClient(cred, g_param[OptionsDefine.Region], profile)
     client._sdkVersion += ("_CLI_" + __version__)
     models = MODELS_MAP[g_param[OptionsDefine.Version]]
-    model = models.StopDBImportJobRequest()
+    model = models.DeleteDeployGroupsRequest()
     model.from_json_string(json.dumps(param))
-    rsp = client.StopDBImportJob(model)
+    rsp = client.DeleteDeployGroups(model)
     result = rsp.to_json_string()
     jsonobj = None
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
@@ -770,38 +771,41 @@
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
-def doDescribeSupportedPrivileges(argv, arglist):
+def doDescribeDeployGroupList(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
-        show_help("DescribeSupportedPrivileges", g_param[OptionsDefine.Version])
+        show_help("DescribeDeployGroupList", g_param[OptionsDefine.Version])
         return
 
     param = {
-        "InstanceId": argv.get("--InstanceId"),
+        "DeployGroupId": argv.get("--DeployGroupId"),
+        "DeployGroupName": argv.get("--DeployGroupName"),
+        "Limit": Utils.try_to_json(argv, "--Limit"),
+        "Offset": Utils.try_to_json(argv, "--Offset"),
 
     }
     cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
     http_profile = HttpProfile(
         reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
         reqMethod="POST",
         endpoint=g_param[OptionsDefine.Endpoint]
     )
     profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
     mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
     client = mod.CdbClient(cred, g_param[OptionsDefine.Region], profile)
     client._sdkVersion += ("_CLI_" + __version__)
     models = MODELS_MAP[g_param[OptionsDefine.Version]]
-    model = models.DescribeSupportedPrivilegesRequest()
+    model = models.DescribeDeployGroupListRequest()
     model.from_json_string(json.dumps(param))
-    rsp = client.DescribeSupportedPrivileges(model)
+    rsp = client.DescribeDeployGroupList(model)
     result = rsp.to_json_string()
     jsonobj = None
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
@@ -1406,14 +1410,47 @@
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
+def doStopDBImportJob(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("StopDBImportJob", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "AsyncRequestId": argv.get("--AsyncRequestId"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.CdbClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.StopDBImportJobRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.StopDBImportJob(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
 def doDescribeDBInstanceCharset(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
         show_help("DescribeDBInstanceCharset", g_param[OptionsDefine.Version])
         return
 
     param = {
@@ -2273,38 +2310,40 @@
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
-def doOfflineIsolatedInstances(argv, arglist):
+def doModifyNameOrDescByDpId(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
-        show_help("OfflineIsolatedInstances", g_param[OptionsDefine.Version])
+        show_help("ModifyNameOrDescByDpId", g_param[OptionsDefine.Version])
         return
 
     param = {
-        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),
+        "DeployGroupId": argv.get("--DeployGroupId"),
+        "DeployGroupName": argv.get("--DeployGroupName"),
+        "Description": argv.get("--Description"),
 
     }
     cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
     http_profile = HttpProfile(
         reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
         reqMethod="POST",
         endpoint=g_param[OptionsDefine.Endpoint]
     )
     profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
     mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
     client = mod.CdbClient(cred, g_param[OptionsDefine.Region], profile)
     client._sdkVersion += ("_CLI_" + __version__)
     models = MODELS_MAP[g_param[OptionsDefine.Version]]
-    model = models.OfflineIsolatedInstancesRequest()
+    model = models.ModifyNameOrDescByDpIdRequest()
     model.from_json_string(json.dumps(param))
-    rsp = client.OfflineIsolatedInstances(model)
+    rsp = client.ModifyNameOrDescByDpId(model)
     result = rsp.to_json_string()
     jsonobj = None
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
@@ -2339,14 +2378,47 @@
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
+def doDescribeSupportedPrivileges(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("DescribeSupportedPrivileges", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "InstanceId": argv.get("--InstanceId"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.CdbClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.DescribeSupportedPrivilegesRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.DescribeSupportedPrivileges(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
 def doDescribeInstanceParams(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
         show_help("DescribeInstanceParams", g_param[OptionsDefine.Version])
         return
 
     param = {
@@ -2407,14 +2479,47 @@
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
+def doOfflineIsolatedInstances(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("OfflineIsolatedInstances", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.CdbClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.OfflineIsolatedInstancesRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.OfflineIsolatedInstances(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
 def doDescribeInstanceParamRecords(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
         show_help("DescribeInstanceParamRecords", g_param[OptionsDefine.Version])
         return
 
     param = {
@@ -2577,14 +2682,48 @@
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
+def doCreateDeployGroup(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("CreateDeployGroup", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "DeployGroupName": argv.get("--DeployGroupName"),
+        "Description": argv.get("--Description"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.CdbClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.CreateDeployGroupRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.CreateDeployGroup(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
 def doDeleteTimeWindow(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
         show_help("DeleteTimeWindow", g_param[OptionsDefine.Version])
         return
 
     param = {
@@ -2711,21 +2850,21 @@
     "DeleteBackup": doDeleteBackup,
     "ModifyTimeWindow": doModifyTimeWindow,
     "OpenDBInstanceGTID": doOpenDBInstanceGTID,
     "ModifyAccountDescription": doModifyAccountDescription,
     "IsolateDBInstance": doIsolateDBInstance,
     "ModifyBackupConfig": doModifyBackupConfig,
     "ModifyInstanceParam": doModifyInstanceParam,
-    "StopDBImportJob": doStopDBImportJob,
+    "DeleteDeployGroups": doDeleteDeployGroups,
     "ModifyDBInstanceProject": doModifyDBInstanceProject,
     "ModifyInstanceTag": doModifyInstanceTag,
     "DeleteParamTemplate": doDeleteParamTemplate,
     "DescribeBackups": doDescribeBackups,
     "DescribeAsyncRequestInfo": doDescribeAsyncRequestInfo,
-    "DescribeSupportedPrivileges": doDescribeSupportedPrivileges,
+    "DescribeDeployGroupList": doDescribeDeployGroupList,
     "CreateParamTemplate": doCreateParamTemplate,
     "InitDBInstances": doInitDBInstances,
     "CreateDBInstanceHour": doCreateDBInstanceHour,
     "AddTimeWindow": doAddTimeWindow,
     "ModifyDBInstanceName": doModifyDBInstanceName,
     "DescribeDBZoneConfig": doDescribeDBZoneConfig,
     "CreateBackup": doCreateBackup,
@@ -2734,14 +2873,15 @@
     "ModifyAutoRenewFlag": doModifyAutoRenewFlag,
     "DescribeDBInstanceRebootTime": doDescribeDBInstanceRebootTime,
     "DescribeBackupTables": doDescribeBackupTables,
     "RestartDBInstances": doRestartDBInstances,
     "DescribeDBInstances": doDescribeDBInstances,
     "VerifyRootAccount": doVerifyRootAccount,
     "RenewDBInstance": doRenewDBInstance,
+    "StopDBImportJob": doStopDBImportJob,
     "DescribeDBInstanceCharset": doDescribeDBInstanceCharset,
     "StartBatchRollback": doStartBatchRollback,
     "AssociateSecurityGroups": doAssociateSecurityGroups,
     "DescribeSlowLogs": doDescribeSlowLogs,
     "InquiryPriceUpgradeInstances": doInquiryPriceUpgradeInstances,
     "DescribeDBPrice": doDescribeDBPrice,
     "DescribeDeviceMonitorInfo": doDescribeDeviceMonitorInfo,
@@ -2758,23 +2898,26 @@
     "CloseWanService": doCloseWanService,
     "DescribeDefaultParams": doDescribeDefaultParams,
     "DescribeTagsOfInstanceIds": doDescribeTagsOfInstanceIds,
     "ModifyAccountPassword": doModifyAccountPassword,
     "DescribeBinlogs": doDescribeBinlogs,
     "DescribeDatabases": doDescribeDatabases,
     "CreateAccounts": doCreateAccounts,
-    "OfflineIsolatedInstances": doOfflineIsolatedInstances,
+    "ModifyNameOrDescByDpId": doModifyNameOrDescByDpId,
     "DescribeDBSecurityGroups": doDescribeDBSecurityGroups,
+    "DescribeSupportedPrivileges": doDescribeSupportedPrivileges,
     "DescribeInstanceParams": doDescribeInstanceParams,
     "DescribeUploadedFiles": doDescribeUploadedFiles,
+    "OfflineIsolatedInstances": doOfflineIsolatedInstances,
     "DescribeInstanceParamRecords": doDescribeInstanceParamRecords,
     "OpenWanService": doOpenWanService,
     "UpgradeDBInstanceEngineVersion": doUpgradeDBInstanceEngineVersion,
     "DescribeParamTemplateInfo": doDescribeParamTemplateInfo,
     "DisassociateSecurityGroups": doDisassociateSecurityGroups,
+    "CreateDeployGroup": doCreateDeployGroup,
     "DeleteTimeWindow": doDeleteTimeWindow,
     "DescribeTables": doDescribeTables,
     "DescribeBackupDatabases": doDescribeBackupDatabases,
 
 }
 
 AVAILABLE_VERSION_LIST = [
```

### Comparing `tccli-3.0.98.1/tccli/services/cdb/v20170320/help.py` & `tccli-3.0.99.1/tccli/services/cdb/v20170320/help.py`

 * *Files 2% similar despite different names*

```diff
@@ -54,14 +54,31 @@
       {
         "name": "InstanceId",
         "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
       }
     ],
     "desc": "本接口(DescribeDBInstanceCharset)用于查询云数据库实例的字符集，获取字符集的名称。"
   },
+  "DescribeInstanceParamRecords": {
+    "params": [
+      {
+        "name": "InstanceId",
+        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
+      },
+      {
+        "name": "Offset",
+        "desc": "分页偏移量。"
+      },
+      {
+        "name": "Limit",
+        "desc": "分页大小。"
+      }
+    ],
+    "desc": "该接口（DescribeInstanceParamRecords）用于查询实例参数修改历史。"
+  },
   "DescribeBackupConfig": {
     "params": [
       {
         "name": "InstanceId",
         "desc": "实例短实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。"
       }
     ],
@@ -181,23 +198,27 @@
       },
       {
         "name": "ExpireDays",
         "desc": "备份文件的保留时间，单位为天。最小值为7天，最大值为732天。"
       },
       {
         "name": "StartTime",
-        "desc": "备份时间范围，格式为：02:00-06:00，起点和终点时间目前限制为整点，目前可以选择的范围为： 00:00-12:00，02:00-06:00，06：00-10：00，10:00-14:00，14:00-18:00，18:00-22:00，22:00-02:00。"
+        "desc": "(将废弃，建议使用 BackupTimeWindow 参数) 备份时间范围，格式为：02:00-06:00，起点和终点时间目前限制为整点，目前可以选择的范围为： 00:00-12:00，02:00-06:00，06：00-10：00，10:00-14:00，14:00-18:00，18:00-22:00，22:00-02:00。"
       },
       {
         "name": "BackupMethod",
         "desc": "自动备份方式，仅支持：physical - 物理冷备"
       },
       {
         "name": "BinlogExpireDays",
         "desc": "binlog的保留时间，单位为天。最小值为7天，最大值为732天。该值的设置不能大于备份文件的保留时间。"
+      },
+      {
+        "name": "BackupTimeWindow",
+        "desc": "备份时间窗，比如要设置每周二和周日 10:00-14:00之间备份，该参数如下：{\"Monday\": \"\", \"Tuesday\": \"10:00-14:00\", \"Wednesday\": \"\", \"Thursday\": \"\", \"Friday\": \"\", \"Saturday\": \"\", \"Sunday\": \"10:00-14:00\"}    （注：可以设置一周的某几天备份，但是每天的备份时间需要设置为相同的时间段。 如果设置了该字段，将忽略StartTime字段的设置）"
       }
     ],
     "desc": "本接口(ModifyBackupConfig)用于修改数据库备份配置信息。"
   },
   "ModifyInstanceParam": {
     "params": [
       {
@@ -207,14 +228,23 @@
       {
         "name": "ParamList",
         "desc": "要修改的参数列表。每一个元素是 Name 和 CurrentValue 的组合。Name 是参数名，CurrentValue 是要修改成的值。"
       }
     ],
     "desc": "本接口(ModifyInstanceParam)用于修改云数据库实例的参数。"
   },
+  "DeleteDeployGroups": {
+    "params": [
+      {
+        "name": "DeployGroupIds",
+        "desc": "要删除的置放群组 ID 列表。"
+      }
+    ],
+    "desc": "根据置放群组ID删除置放群组（置放群组中有资源存在时不能删除该置放群组）"
+  },
   "ModifyDBInstanceProject": {
     "params": [
       {
         "name": "InstanceIds",
         "desc": "实例 ID 数组，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
       },
       {
@@ -681,23 +711,23 @@
       },
       {
         "name": "InitFlag",
         "desc": "初始化标记，可取值：0 - 未初始化，1 - 初始化。"
       },
       {
         "name": "WithDr",
-        "desc": "是否包含灾备实例，可取值：0 - 不包含，1 - 包含。"
+        "desc": "是否包含灾备关系对应的实例，可取值：0 - 不包含，1 - 包含。默认取值为1。如果拉取主实例，则灾备关系的数据在DrInfo字段中， 如果拉取灾备实例， 则灾备关系的数据在MasterInfo字段中。灾备关系中只包含部分基本的数据，详细的数据需要自行调接口拉取。"
       },
       {
         "name": "WithRo",
-        "desc": "是否包含只读实例，可取值：0 - 不包含，1 - 包含。"
+        "desc": "是否包含只读实例，可取值：0 - 不包含，1 - 包含。默认取值为1。"
       },
       {
         "name": "WithMaster",
-        "desc": "是否包含主实例，可取值：0 - 不包含，1 - 包含。"
+        "desc": "是否包含主实例，可取值：0 - 不包含，1 - 包含。默认取值为1。"
       }
     ],
     "desc": "本接口(DescribeDBInstances)用于查询云数据库实例列表，支持通过项目 ID、实例 ID、访问地址、实例状态等过滤条件来筛选实例。支持查询主实例、灾备实例和只读实例信息列表。"
   },
   "VerifyRootAccount": {
     "params": [
       {
@@ -1147,22 +1177,34 @@
       {
         "name": "Description",
         "desc": "数据库账号的备注信息。"
       }
     ],
     "desc": "本接口(ModifyAccountDescription)用于修改云数据库账户的备注信息。"
   },
-  "DescribeSupportedPrivileges": {
+  "DescribeDeployGroupList": {
     "params": [
       {
-        "name": "InstanceId",
-        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
+        "name": "DeployGroupId",
+        "desc": "置放群组 ID。"
+      },
+      {
+        "name": "DeployGroupName",
+        "desc": "置放群组名称。"
+      },
+      {
+        "name": "Limit",
+        "desc": "返回数量，默认为20，最大值为100。"
+      },
+      {
+        "name": "Offset",
+        "desc": "偏移量，默认为0。"
       }
     ],
-    "desc": "本接口(DescribeSupportedPrivileges)用于查询云数据库的支持的权限信息，包括全局权限，数据库权限，表权限以及列权限。"
+    "desc": "根据置放群组 ID 或置放群组名称查询置放群组列表"
   },
   "StopDBImportJob": {
     "params": [
       {
         "name": "AsyncRequestId",
         "desc": "异步任务的请求 ID。"
       }
@@ -1255,14 +1297,23 @@
       {
         "name": "InstanceId",
         "desc": "实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。"
       }
     ],
     "desc": "本接口(DescribeDBSecurityGroups)用于查询实例的安全组详情。"
   },
+  "DescribeSupportedPrivileges": {
+    "params": [
+      {
+        "name": "InstanceId",
+        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
+      }
+    ],
+    "desc": "本接口(DescribeSupportedPrivileges)用于查询云数据库的支持的权限信息，包括全局权限，数据库权限，表权限以及列权限。"
+  },
   "DescribeInstanceParams": {
     "params": [
       {
         "name": "InstanceId",
         "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
       }
     ],
@@ -1290,30 +1341,30 @@
       {
         "name": "InstanceId",
         "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
       }
     ],
     "desc": "本接口(OpenWanService)用于开通实例外网访问。\n\n注意，实例开通外网访问之前，需要先将实例进行 [实例初始化](https://cloud.tencent.com/document/api/236/15873) 操作。"
   },
-  "DescribeInstanceParamRecords": {
+  "ModifyNameOrDescByDpId": {
     "params": [
       {
-        "name": "InstanceId",
-        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
+        "name": "DeployGroupId",
+        "desc": "置放群组 ID。"
       },
       {
-        "name": "Offset",
-        "desc": "分页偏移量。"
+        "name": "DeployGroupName",
+        "desc": "置放群组名称，最长不能超过60个字符。置放群组名和置放群组描述不能都为空。"
       },
       {
-        "name": "Limit",
-        "desc": "分页大小。"
+        "name": "Description",
+        "desc": "置放群组描述，最长不能超过200个字符。置放群组名和置放群组描述不能都为空。"
       }
     ],
-    "desc": "该接口（DescribeInstanceParamRecords）用于查询实例参数修改历史。"
+    "desc": "修改置放群组的名称或者描述"
   },
   "UpgradeDBInstance": {
     "params": [
       {
         "name": "InstanceId",
         "desc": "实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
       },
@@ -1391,14 +1442,27 @@
       {
         "name": "InstanceIds",
         "desc": "实例 ID 列表，一个或者多个实例 ID 组成的数组。"
       }
     ],
     "desc": "本接口(DisassociateSecurityGroups)用于安全组批量解绑实例。"
   },
+  "CreateDeployGroup": {
+    "params": [
+      {
+        "name": "DeployGroupName",
+        "desc": "置放群组名称，最长不能超过60个字符。"
+      },
+      {
+        "name": "Description",
+        "desc": "置放群组描述，最长不能超过200个字符。"
+      }
+    ],
+    "desc": "创建放置实例的置放群组"
+  },
   "DeleteTimeWindow": {
     "params": [
       {
         "name": "InstanceId",
         "desc": "实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
       }
     ],
```

### Comparing `tccli-3.0.98.1/tccli/services/ocr/ocr_client.py` & `tccli-3.0.99.1/tccli/services/ocr/ocr_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/ocr/v20181119/help.py` & `tccli-3.0.99.1/tccli/services/ocr/v20181119/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/asr/asr_client.py` & `tccli-3.0.99.1/tccli/services/asr/asr_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/asr/v20190614/help.py` & `tccli-3.0.99.1/tccli/services/asr/v20190614/help.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # -*- coding: utf-8 -*-
 DESC = "asr-2019-06-14"
 INFO = {
   "CreateRecTask": {
     "params": [
       {
         "name": "EngineModelType",
-        "desc": "引擎类型。8k_0：电话 8k 通用模型；16k_0：16k 通用模型；8k_6: 电话场景下单声道话者分离模型。"
+        "desc": "引擎类型。\n8k_0：电话 8k 通用模型；\n16k_0：16k 通用模型；\n8k_6: 电话场景下单声道话者分离模型。"
       },
       {
         "name": "ChannelNum",
         "desc": "语音声道数。1：单声道；2：双声道（仅在电话 8k 通用模型下支持）。"
       },
       {
         "name": "ResTextFormat",
@@ -17,44 +17,44 @@
       },
       {
         "name": "SourceType",
         "desc": "语音数据来源。0：语音 URL；1：语音数据（post body）。"
       },
       {
         "name": "CallbackUrl",
-        "desc": "回调 URL，用户自行搭建的用于接收识别结果的服务器地址， 长度小于2048字节。"
+        "desc": "回调 URL，用户自行搭建的用于接收识别结果的服务器地址， 长度小于2048字节。如果用户使用回调方式获取识别结果，需提交该参数；如果用户使用轮询方式获取识别结果，则无需提交该参数。"
       },
       {
         "name": "Url",
         "desc": "语音的URL地址，需要公网可下载。长度小于2048字节，当 source_type 值为 0 时须填写该字段，为 1 时不需要填写。注意：请确保录音文件时长在一个小时之内，否则可能识别失败。请保证文件的下载速度，否则可能下载失败。"
       },
       {
         "name": "Data",
         "desc": "语音数据，当SourceType 值为1时必须填写，为0可不写。要base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频数据要小于5MB。"
       },
       {
         "name": "DataLen",
         "desc": "数据长度，当 SourceType 值为1时必须填写，为0可不写（此数据长度为数据未进行base64编码时的数据长度）。"
       }
     ],
-    "desc": "本接口服务对录音时长1小时以内的录音文件进行识别，异步返回识别全部结果。\n<br>• 支持回调或轮询的方式获取结果，轮询方式请参考“录音文件识别结果查询”。\n<br>• 支持语音 URL 和本地语音文件两种请求方式。\n<br>• 接口是 HTTP RESTful 形式\n\n在使用该接口前，需要在 [语音识别控制台](https://console.cloud.tencent.com/asr) 开通服务，并进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi) 新建密钥，<br>生成 AppID、SecretID 和 SecretKey ，用于 API 调用时生成签名，签名将用来进行接口鉴权。"
+    "desc": "本接口服务对录音时长1小时以内的录音文件进行识别，异步返回识别全部结果。\n<br>• 支持回调或轮询的方式获取结果，结果获取请参考[ 录音文件识别结果查询](https://cloud.tencent.com/document/product/1093/37822)。\n<br>• 支持语音 URL 和本地语音文件两种请求方式。\n<br>• 接口是 HTTP RESTful 形式"
   },
   "SentenceRecognition": {
     "params": [
       {
         "name": "ProjectId",
         "desc": "腾讯云项目 ID，可填 0，总长度不超过 1024 字节。"
       },
       {
         "name": "SubServiceType",
         "desc": "子服务类型。2： 一句话识别。"
       },
       {
         "name": "EngSerViceType",
-        "desc": "引擎类型。8k：电话 8k 中文普通话通用；16k：16k 中文普通话通用；16k_en：16k 英语；16k_ca：16k 粤语。"
+        "desc": "引擎类型。\n8k：电话 8k 中文普通话通用；\n16k：16k 中文普通话通用；\n16k_en：16k 英语；\n16k_ca：16k 粤语。"
       },
       {
         "name": "SourceType",
         "desc": "语音数据来源。0：语音 URL；1：语音数据（post body）。"
       },
       {
         "name": "VoiceFormat",
@@ -73,19 +73,19 @@
         "desc": "语音数据，当SourceType 值为1（本地语音数据上传）时必须填写，当SourceType 值为0（语音 URL上传）可不写。要使用base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频数据要小于600KB。"
       },
       {
         "name": "DataLen",
         "desc": "数据长度，单位为字节。当 SourceType 值为1（本地语音数据上传）时必须填写，当 SourceType 值为0（语音 URL上传）可不写（此数据长度为数据未进行base64编码时的数据长度）。"
       }
     ],
-    "desc": "本接口用于对60秒之内的短音频文件进行识别。\n<br>•   支持中文普通话、英语、粤语和带有一定方言口音的中文普通话识别。\n<br>•   支持本地语音文件上传和语音URL上传两种请求方式。\n<br>•   音频格式支持wav、mp3；采样率支持8000Hz或者16000Hz；采样精度支持16bits；声道支持单声道。\n<br>•   当音频文件通过请求中body内容上传时，请求大小不能超过600KB；当音频以URL方式传输时，音频时长不可超过60s。\n<br>•   所有请求参数放在POST请求的body中，编码类型采用x-www-form-urlencoded，参数进行urlencode编码后传输。"
+    "desc": "本接口用于对60秒之内的短音频文件进行识别。\n<br>•   支持中文普通话、英语、粤语。\n<br>•   支持本地语音文件上传和语音URL上传两种请求方式。\n<br>•   音频格式支持wav、mp3；采样率支持8000Hz或者16000Hz；采样精度支持16bits；声道支持单声道。\n<br>•   当音频文件通过请求中body内容上传时，请求大小不能超过600KB；当音频以URL方式传输时，音频时长不可超过60s。\n<br>•   所有请求参数放在POST请求的body中，编码类型采用x-www-form-urlencoded，参数进行urlencode编码后传输。"
   },
   "DescribeTaskStatus": {
     "params": [
       {
         "name": "TaskId",
         "desc": "从CreateRecTask接口获取的TaskId，用于获取任务状态与结果。"
       }
     ],
-    "desc": "本接口需要配合录音文件识别请求接口使用，单独使用无效。在调用录音文件识别接口后，可以在本接口传入TaskID来轮询识别结果。"
+    "desc": "在调用录音文件识别请求接口后，有回调和轮询两种方式获取识别结果。\n<br>• 当采用回调方式时，识别完成后会将结果通过 POST 请求的形式通知到用户在请求时填写的回调 URL，具体请参见[ 录音识别结果回调 ](https://cloud.tencent.com/document/product/1093/37139#callback)。\n<br>• 当采用轮询方式时，需要主动提交任务ID来轮询识别结果，共有任务成功、等待、执行中和失败四种结果，具体信息请参见下文说明。\n"
   }
 }
```

### Comparing `tccli-3.0.98.1/tccli/services/mariadb/v20170312/help.py` & `tccli-3.0.99.1/tccli/services/mariadb/v20170312/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/mariadb/mariadb_client.py` & `tccli-3.0.99.1/tccli/services/mariadb/mariadb_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/sts/sts_client.py` & `tccli-3.0.99.1/tccli/services/sts/sts_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/sts/v20180813/help.py` & `tccli-3.0.99.1/tccli/services/sts/v20180813/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/dts/dts_client.py` & `tccli-3.0.99.1/tccli/services/dts/dts_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/dts/v20180330/help.py` & `tccli-3.0.99.1/tccli/services/dts/v20180330/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/aai/aai_client.py` & `tccli-3.0.99.1/tccli/services/aai/aai_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/aai/v20180522/help.py` & `tccli-3.0.99.1/tccli/services/aai/v20180522/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/ecc/ecc_client.py` & `tccli-3.0.99.1/tccli/services/ecc/ecc_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/ecc/v20181213/help.py` & `tccli-3.0.99.1/tccli/services/ecc/v20181213/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/bmeip/v20180625/help.py` & `tccli-3.0.99.1/tccli/services/bmeip/v20180625/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/bmeip/bmeip_client.py` & `tccli-3.0.99.1/tccli/services/bmeip/bmeip_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/mps/v20190612/help.py` & `tccli-3.0.99.1/tccli/services/mps/v20190612/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/mps/mps_client.py` & `tccli-3.0.99.1/tccli/services/mps/mps_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/__init__.py` & `tccli-3.0.99.1/tccli/services/__init__.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/soe/v20180724/help.py` & `tccli-3.0.99.1/tccli/services/soe/v20180724/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/soe/soe_client.py` & `tccli-3.0.99.1/tccli/services/soe/soe_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cvm/v20170312/help.py` & `tccli-3.0.99.1/tccli/services/cvm/v20170312/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cvm/cvm_client.py` & `tccli-3.0.99.1/tccli/services/cvm/cvm_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/yunsou/yunsou_client.py` & `tccli-3.0.99.1/tccli/services/yunsou/yunsou_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/yunsou/v20180504/help.py` & `tccli-3.0.99.1/tccli/services/yunsou/v20180504/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/batch/v20170312/help.py` & `tccli-3.0.99.1/tccli/services/batch/v20170312/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/batch/batch_client.py` & `tccli-3.0.99.1/tccli/services/batch/batch_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/dcdb/v20180411/help.py` & `tccli-3.0.99.1/tccli/services/dcdb/v20180411/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/dcdb/dcdb_client.py` & `tccli-3.0.99.1/tccli/services/dcdb/dcdb_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/redis/v20180412/help.py` & `tccli-3.0.99.1/tccli/services/redis/v20180412/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/redis/redis_client.py` & `tccli-3.0.99.1/tccli/services/redis/redis_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/vpc/v20170312/help.py` & `tccli-3.0.99.1/tccli/services/vpc/v20170312/help.py`

 * *Files 2% similar despite different names*

```diff
@@ -315,14 +315,35 @@
       {
         "name": "InstanceId",
         "desc": "要查询的CVM实例ID"
       }
     ],
     "desc": "本接口（DescribeNetworkInterfaceLimit）根据CVM实例ID查询弹性网卡配额，返回该CVM实例能绑定的弹性网卡配额，以及每个弹性网卡可以分配的ip配额"
   },
+  "DescribeNetDetects": {
+    "params": [
+      {
+        "name": "NetDetectIds",
+        "desc": "网络探测实例`ID`数组。形如：[`netd-12345678`]"
+      },
+      {
+        "name": "Filters",
+        "desc": "过滤条件，参数不支持同时指定NetDetectIds和Filters。\n<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-12345678</li>\n<li>net-detect-id - String - （过滤条件）网络探测实例ID，形如：netd-12345678</li>\n<li>subnet-id - String - （过滤条件）子网实例ID，形如：subnet-12345678</li>\n<li>net-detect-name - String - （过滤条件）网络探测名称</li>"
+      },
+      {
+        "name": "Offset",
+        "desc": "偏移量，默认为0。"
+      },
+      {
+        "name": "Limit",
+        "desc": "返回数量，默认为20，最大值为100。"
+      }
+    ],
+    "desc": "本接口（DescribeNetDetects）用于查询网络探测列表。"
+  },
   "DescribeSecurityGroupPolicies": {
     "params": [
       {
         "name": "SecurityGroupId",
         "desc": "安全组实例ID，例如：sg-33ocnj9n，可通过DescribeSecurityGroups获取。"
       }
     ],
@@ -391,30 +412,22 @@
       {
         "name": "VpnConnectionId",
         "desc": "VPN通道实例ID。形如：vpnx-f49l6u0z。"
       }
     ],
     "desc": "本接口(DeleteVpnConnection)用于删除VPN通道。"
   },
-  "ModifyAddressTemplateGroupAttribute": {
+  "DeleteAddressTemplateGroup": {
     "params": [
       {
         "name": "AddressTemplateGroupId",
-        "desc": "IP地址模板集合实例ID，例如：ipmg-2uw6ujo6。"
-      },
-      {
-        "name": "AddressTemplateGroupName",
-        "desc": "IP地址模板集合名称。"
-      },
-      {
-        "name": "AddressTemplateIds",
-        "desc": "IP地址模板实例ID， 例如：ipm-mdunqeb6。"
+        "desc": "IP地址模板集合实例ID，例如：ipmg-90cex8mq。"
       }
     ],
-    "desc": "本接口（ModifyAddressTemplateGroupAttribute）用于修改IP地址模板集合"
+    "desc": "本接口（DeleteAddressTemplateGroup）用于删除IP地址模板集合"
   },
   "DescribeCustomerGatewayVendors": {
     "params": [],
     "desc": "本接口（DescribeCustomerGatewayVendors）用于查询可支持的对端网关厂商信息。"
   },
   "DescribeAddresses": {
     "params": [
@@ -628,14 +641,47 @@
       {
         "name": "RouteTableId",
         "desc": "路由表实例ID，例如：rtb-azd4dt1c。"
       }
     ],
     "desc": "本接口（ReplaceRouteTableAssociation)用于修改子网（Subnet）关联的路由表（RouteTable）。\n* 一个子网只能关联一个路由表。"
   },
+  "CheckNetDetectState": {
+    "params": [
+      {
+        "name": "DetectDestinationIp",
+        "desc": "探测目的IPv4地址数组，最多两个。"
+      },
+      {
+        "name": "NextHopType",
+        "desc": "下一跳类型，目前我们支持的类型有：\nVPN：VPN网关；\nDIRECTCONNECT：专线网关；\nPEERCONNECTION：对等连接；\nNAT：NAT网关；\nNORMAL_CVM：普通云主机；"
+      },
+      {
+        "name": "NextHopDestination",
+        "desc": "下一跳目的网关，取值与“下一跳类型”相关：\n下一跳类型为VPN，取值VPN网关ID，形如：vpngw-12345678；\n下一跳类型为DIRECTCONNECT，取值专线网关ID，形如：dcg-12345678；\n下一跳类型为PEERCONNECTION，取值对等连接ID，形如：pcx-12345678；\n下一跳类型为NAT，取值Nat网关，形如：nat-12345678；\n下一跳类型为NORMAL_CVM，取值云主机IPv4地址，形如：10.0.0.12；"
+      },
+      {
+        "name": "NetDetectId",
+        "desc": "网络探测实例ID。形如：netd-12345678。"
+      },
+      {
+        "name": "VpcId",
+        "desc": "`VPC`实例`ID`。形如：`vpc-12345678`"
+      },
+      {
+        "name": "SubnetId",
+        "desc": "子网实例ID。形如：subnet-12345678。"
+      },
+      {
+        "name": "NetDetectName",
+        "desc": "网络探测名称，最大长度不能超过60个字节。"
+      }
+    ],
+    "desc": "本接口(CheckNetDetectState)用于验证网络探测。"
+  },
   "DescribeVpcs": {
     "params": [
       {
         "name": "VpcIds",
         "desc": "VPC实例ID。形如：vpc-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpcIds和Filters。"
       },
       {
@@ -1182,14 +1228,35 @@
       {
         "name": "BandwidthPackageId",
         "desc": "待删除带宽包bwpId"
       }
     ],
     "desc": "接口支持删除共享带宽包，包括[设备带宽包](https://cloud.tencent.com/document/product/684/15246#.E8.AE.BE.E5.A4.87.E5.B8.A6.E5.AE.BD.E5.8C.85)和[ip带宽包](https://cloud.tencent.com/document/product/684/15246#ip-.E5.B8.A6.E5.AE.BD.E5.8C.85)"
   },
+  "DescribeNetDetectStates": {
+    "params": [
+      {
+        "name": "NetDetectIds",
+        "desc": "网络探测实例`ID`数组。形如：[`netd-12345678`]"
+      },
+      {
+        "name": "Filters",
+        "desc": "过滤条件，参数不支持同时指定NetDetectIds和Filters。\n<li>net-detect-id - String - （过滤条件）网络探测实例ID，形如：netd-12345678</li>"
+      },
+      {
+        "name": "Offset",
+        "desc": "偏移量，默认为0。"
+      },
+      {
+        "name": "Limit",
+        "desc": "返回数量，默认为20，最大值为100。"
+      }
+    ],
+    "desc": "本接口(DescribeNetDetectStates)用于查询网络探测验证结果列表。"
+  },
   "DescribeCcns": {
     "params": [
       {
         "name": "CcnIds",
         "desc": "CCN实例ID。形如：ccn-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定CcnIds和Filters。"
       },
       {
@@ -1394,22 +1461,30 @@
       {
         "name": "PrivateIpAddresses",
         "desc": "指定的内网IP信息，单次最多指定10个。"
       }
     ],
     "desc": "本接口（UnassignPrivateIpAddresses）用于弹性网卡退还内网 IP。\n* 退还弹性网卡上的辅助内网IP，接口自动解关联弹性公网 IP。不能退还弹性网卡的主内网IP。"
   },
-  "DeleteAddressTemplateGroup": {
+  "ModifyAddressTemplateGroupAttribute": {
     "params": [
       {
         "name": "AddressTemplateGroupId",
-        "desc": "IP地址模板集合实例ID，例如：ipmg-90cex8mq。"
+        "desc": "IP地址模板集合实例ID，例如：ipmg-2uw6ujo6。"
+      },
+      {
+        "name": "AddressTemplateGroupName",
+        "desc": "IP地址模板集合名称。"
+      },
+      {
+        "name": "AddressTemplateIds",
+        "desc": "IP地址模板实例ID， 例如：ipm-mdunqeb6。"
       }
     ],
-    "desc": "本接口（DeleteAddressTemplateGroup）用于删除IP地址模板集合"
+    "desc": "本接口（ModifyAddressTemplateGroupAttribute）用于修改IP地址模板集合"
   },
   "DescribeCcnRoutes": {
     "params": [
       {
         "name": "CcnId",
         "desc": "CCN实例ID，形如：ccn-gree226l。"
       },
@@ -1428,14 +1503,18 @@
       {
         "name": "Limit",
         "desc": "返回数量"
       }
     ],
     "desc": "本接口（DescribeCcnRoutes）用于查询已加入云联网（CCN）的路由"
   },
+  "DescribeBandwidthPackageQuota": {
+    "params": [],
+    "desc": "接口用于查询账户在当前地域的带宽包上限数量以及使用数量"
+  },
   "CreateIp6Translators": {
     "params": [
       {
         "name": "Ip6TranslatorName",
         "desc": "转换实例名称"
       },
       {
@@ -1517,14 +1596,23 @@
       {
         "name": "Zone",
         "desc": "可用区，形如：`ap-guangzhou-1`。"
       }
     ],
     "desc": "本接口(CreateNatGateway)用于创建NAT网关。"
   },
+  "DeleteNetDetect": {
+    "params": [
+      {
+        "name": "NetDetectId",
+        "desc": "网络探测实例`ID`。形如：`netd-12345678`"
+      }
+    ],
+    "desc": "本接口(DeleteNetDetect)用于删除网络探测实例。"
+  },
   "ModifySecurityGroupAttribute": {
     "params": [
       {
         "name": "SecurityGroupId",
         "desc": "安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。"
       },
       {
@@ -2346,14 +2434,43 @@
       {
         "name": "RouteTableName",
         "desc": "路由表名称。"
       }
     ],
     "desc": "本接口（ModifyRouteTableAttribute）用于修改路由表（RouteTable）属性。"
   },
+  "ModifyNetDetect": {
+    "params": [
+      {
+        "name": "NetDetectId",
+        "desc": "网络探测实例`ID`。形如：`netd-12345678`"
+      },
+      {
+        "name": "NetDetectName",
+        "desc": "网络探测名称，最大长度不能超过60个字节。"
+      },
+      {
+        "name": "DetectDestinationIp",
+        "desc": "探测目的IPv4地址数组，最多两个。"
+      },
+      {
+        "name": "NextHopType",
+        "desc": "下一跳类型，目前我们支持的类型有：\nVPN：VPN网关；\nDIRECTCONNECT：专线网关；\nPEERCONNECTION：对等连接；\nNAT：NAT网关；\nNORMAL_CVM：普通云主机；"
+      },
+      {
+        "name": "NextHopDestination",
+        "desc": "下一跳目的网关，取值与“下一跳类型”相关：\n下一跳类型为VPN，取值VPN网关ID，形如：vpngw-12345678；\n下一跳类型为DIRECTCONNECT，取值专线网关ID，形如：dcg-12345678；\n下一跳类型为PEERCONNECTION，取值对等连接ID，形如：pcx-12345678；\n下一跳类型为NAT，取值Nat网关，形如：nat-12345678；\n下一跳类型为NORMAL_CVM，取值云主机IPv4地址，形如：10.0.0.12；"
+      },
+      {
+        "name": "NetDetectDescription",
+        "desc": "网络探测描述。"
+      }
+    ],
+    "desc": "本接口(ModifyNetDetect)用于修改网络探测参数。"
+  },
   "DeleteNatGatewayDestinationIpPortTranslationNatRule": {
     "params": [
       {
         "name": "NatGatewayId",
         "desc": "NAT网关的ID，形如：`nat-df45454`。"
       },
       {
@@ -2372,17 +2489,46 @@
       {
         "name": "Routes",
         "desc": "路由策略对象。"
       }
     ],
     "desc": "本接口(CreateRoutes)用于创建路由策略。\n* 向指定路由表批量新增路由策略。"
   },
-  "DescribeBandwidthPackageQuota": {
-    "params": [],
-    "desc": "接口用于查询账户在当前地域的带宽包上限数量以及使用数量"
+  "CreateNetDetect": {
+    "params": [
+      {
+        "name": "VpcId",
+        "desc": "`VPC`实例`ID`。形如：`vpc-12345678`"
+      },
+      {
+        "name": "SubnetId",
+        "desc": "子网实例ID。形如：subnet-12345678。"
+      },
+      {
+        "name": "NetDetectName",
+        "desc": "网络探测名称，最大长度不能超过60个字节。"
+      },
+      {
+        "name": "DetectDestinationIp",
+        "desc": "探测目的IPv4地址数组。最多两个。"
+      },
+      {
+        "name": "NextHopType",
+        "desc": "下一跳类型，目前我们支持的类型有：\nVPN：VPN网关；\nDIRECTCONNECT：专线网关；\nPEERCONNECTION：对等连接；\nNAT：NAT网关；\nNORMAL_CVM：普通云主机；"
+      },
+      {
+        "name": "NextHopDestination",
+        "desc": "下一跳目的网关，取值与“下一跳类型”相关：\n下一跳类型为VPN，取值VPN网关ID，形如：vpngw-12345678；\n下一跳类型为DIRECTCONNECT，取值专线网关ID，形如：dcg-12345678；\n下一跳类型为PEERCONNECTION，取值对等连接ID，形如：pcx-12345678；\n下一跳类型为NAT，取值Nat网关，形如：nat-12345678；\n下一跳类型为NORMAL_CVM，取值云主机IPv4地址，形如：10.0.0.12；"
+      },
+      {
+        "name": "NetDetectDescription",
+        "desc": "网络探测描述。"
+      }
+    ],
+    "desc": "本接口(CreateNetDetect)用于创建网络探测。"
   },
   "ModifyHaVipAttribute": {
     "params": [
       {
         "name": "HaVipId",
         "desc": "`HAVIP`唯一`ID`，形如：`havip-9o233uri`。"
       },
```

### Comparing `tccli-3.0.98.1/tccli/services/vpc/vpc_client.py` & `tccli-3.0.99.1/tccli/services/vpc/vpc_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -650,14 +650,50 @@
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
+def doDescribeNetDetects(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("DescribeNetDetects", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "NetDetectIds": Utils.try_to_json(argv, "--NetDetectIds"),
+        "Filters": Utils.try_to_json(argv, "--Filters"),
+        "Offset": Utils.try_to_json(argv, "--Offset"),
+        "Limit": Utils.try_to_json(argv, "--Limit"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.DescribeNetDetectsRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.DescribeNetDetects(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
 def doModifyPrivateIpAddressesAttribute(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
         show_help("ModifyPrivateIpAddressesAttribute", g_param[OptionsDefine.Version])
         return
 
     param = {
@@ -1208,14 +1244,53 @@
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
+def doCheckNetDetectState(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("CheckNetDetectState", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "DetectDestinationIp": Utils.try_to_json(argv, "--DetectDestinationIp"),
+        "NextHopType": argv.get("--NextHopType"),
+        "NextHopDestination": argv.get("--NextHopDestination"),
+        "NetDetectId": argv.get("--NetDetectId"),
+        "VpcId": argv.get("--VpcId"),
+        "SubnetId": argv.get("--SubnetId"),
+        "NetDetectName": argv.get("--NetDetectName"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.CheckNetDetectStateRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.CheckNetDetectState(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
 def doDescribeVpcs(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
         show_help("DescribeVpcs", g_param[OptionsDefine.Version])
         return
 
     param = {
@@ -2376,14 +2451,50 @@
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
+def doDescribeNetDetectStates(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("DescribeNetDetectStates", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "NetDetectIds": Utils.try_to_json(argv, "--NetDetectIds"),
+        "Filters": Utils.try_to_json(argv, "--Filters"),
+        "Offset": Utils.try_to_json(argv, "--Offset"),
+        "Limit": Utils.try_to_json(argv, "--Limit"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.DescribeNetDetectStatesRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.DescribeNetDetectStates(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
 def doDescribeCcns(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
         show_help("DescribeCcns", g_param[OptionsDefine.Version])
         return
 
     param = {
@@ -2990,14 +3101,53 @@
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
+def doCreateNetDetect(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("CreateNetDetect", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "VpcId": argv.get("--VpcId"),
+        "SubnetId": argv.get("--SubnetId"),
+        "NetDetectName": argv.get("--NetDetectName"),
+        "DetectDestinationIp": Utils.try_to_json(argv, "--DetectDestinationIp"),
+        "NextHopType": argv.get("--NextHopType"),
+        "NextHopDestination": argv.get("--NextHopDestination"),
+        "NetDetectDescription": argv.get("--NetDetectDescription"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.CreateNetDetectRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.CreateNetDetect(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
 def doCreateIp6Translators(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
         show_help("CreateIp6Translators", g_param[OptionsDefine.Version])
         return
 
     param = {
@@ -3161,14 +3311,47 @@
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
+def doDeleteNetDetect(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("DeleteNetDetect", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "NetDetectId": argv.get("--NetDetectId"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.DeleteNetDetectRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.DeleteNetDetect(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
 def doModifySecurityGroupAttribute(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
         show_help("ModifySecurityGroupAttribute", g_param[OptionsDefine.Version])
         return
 
     param = {
@@ -5026,14 +5209,52 @@
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
+def doModifyNetDetect(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("ModifyNetDetect", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "NetDetectId": argv.get("--NetDetectId"),
+        "NetDetectName": argv.get("--NetDetectName"),
+        "DetectDestinationIp": Utils.try_to_json(argv, "--DetectDestinationIp"),
+        "NextHopType": argv.get("--NextHopType"),
+        "NextHopDestination": argv.get("--NextHopDestination"),
+        "NetDetectDescription": argv.get("--NetDetectDescription"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.VpcClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.ModifyNetDetectRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.ModifyNetDetect(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
 def doDeleteNatGatewayDestinationIpPortTranslationNatRule(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
         show_help("DeleteNatGatewayDestinationIpPortTranslationNatRule", g_param[OptionsDefine.Version])
         return
 
     param = {
@@ -5745,14 +5966,15 @@
     "AssignIpv6CidrBlock": doAssignIpv6CidrBlock,
     "DescribeNatGatewayDestinationIpPortTranslationNatRules": doDescribeNatGatewayDestinationIpPortTranslationNatRules,
     "ModifyFlowLogAttribute": doModifyFlowLogAttribute,
     "ModifyServiceTemplateGroupAttribute": doModifyServiceTemplateGroupAttribute,
     "DescribeCcnAttachedInstances": doDescribeCcnAttachedInstances,
     "ResetRoutes": doResetRoutes,
     "DescribeNetworkInterfaceLimit": doDescribeNetworkInterfaceLimit,
+    "DescribeNetDetects": doDescribeNetDetects,
     "ModifyPrivateIpAddressesAttribute": doModifyPrivateIpAddressesAttribute,
     "DescribeGatewayFlowMonitorDetail": doDescribeGatewayFlowMonitorDetail,
     "UnassignIpv6Addresses": doUnassignIpv6Addresses,
     "DeleteVpnConnection": doDeleteVpnConnection,
     "ModifyAddressTemplateGroupAttribute": doModifyAddressTemplateGroupAttribute,
     "DescribeCustomerGatewayVendors": doDescribeCustomerGatewayVendors,
     "DescribeAddresses": doDescribeAddresses,
@@ -5761,14 +5983,15 @@
     "CreateDirectConnectGatewayCcnRoutes": doCreateDirectConnectGatewayCcnRoutes,
     "RemoveBandwidthPackageResources": doRemoveBandwidthPackageResources,
     "InquiryPriceRenewVpnGateway": doInquiryPriceRenewVpnGateway,
     "AssignPrivateIpAddresses": doAssignPrivateIpAddresses,
     "DescribeNatGateways": doDescribeNatGateways,
     "CreateSubnets": doCreateSubnets,
     "ReplaceRouteTableAssociation": doReplaceRouteTableAssociation,
+    "CheckNetDetectState": doCheckNetDetectState,
     "DescribeVpcs": doDescribeVpcs,
     "InquiryPriceResetVpnGatewayInternetMaxBandwidth": doInquiryPriceResetVpnGatewayInternetMaxBandwidth,
     "DeleteDirectConnectGatewayCcnRoutes": doDeleteDirectConnectGatewayCcnRoutes,
     "RejectAttachCcnInstances": doRejectAttachCcnInstances,
     "MigrateNetworkInterface": doMigrateNetworkInterface,
     "ModifyAddressesBandwidth": doModifyAddressesBandwidth,
     "CreateNatGatewayDestinationIpPortTranslationNatRule": doCreateNatGatewayDestinationIpPortTranslationNatRule,
@@ -5794,14 +6017,15 @@
     "DisassociateNatGatewayAddress": doDisassociateNatGatewayAddress,
     "DescribeFlowLogs": doDescribeFlowLogs,
     "DeleteDirectConnectGateway": doDeleteDirectConnectGateway,
     "DescribeDirectConnectGatewayCcnRoutes": doDescribeDirectConnectGatewayCcnRoutes,
     "CreateNetworkInterface": doCreateNetworkInterface,
     "DeleteBandwidthPackage": doDeleteBandwidthPackage,
     "ModifySecurityGroupPolicies": doModifySecurityGroupPolicies,
+    "DescribeNetDetectStates": doDescribeNetDetectStates,
     "DescribeCcns": doDescribeCcns,
     "DeleteIp6Translators": doDeleteIp6Translators,
     "DeleteCcn": doDeleteCcn,
     "HaVipDisassociateAddressIp": doHaVipDisassociateAddressIp,
     "DetachNetworkInterface": doDetachNetworkInterface,
     "DeleteNetworkInterface": doDeleteNetworkInterface,
     "DescribeVpnConnections": doDescribeVpnConnections,
@@ -5812,19 +6036,21 @@
     "DisableRoutes": doDisableRoutes,
     "DescribeCcnRegionBandwidthLimits": doDescribeCcnRegionBandwidthLimits,
     "AddIp6Rules": doAddIp6Rules,
     "DeleteServiceTemplate": doDeleteServiceTemplate,
     "UnassignPrivateIpAddresses": doUnassignPrivateIpAddresses,
     "DeleteAddressTemplateGroup": doDeleteAddressTemplateGroup,
     "DescribeCcnRoutes": doDescribeCcnRoutes,
+    "CreateNetDetect": doCreateNetDetect,
     "CreateIp6Translators": doCreateIp6Translators,
     "CreateDefaultVpc": doCreateDefaultVpc,
     "AttachNetworkInterface": doAttachNetworkInterface,
     "ReplaceDirectConnectGatewayCcnRoutes": doReplaceDirectConnectGatewayCcnRoutes,
     "DeleteSecurityGroupPolicies": doDeleteSecurityGroupPolicies,
+    "DeleteNetDetect": doDeleteNetDetect,
     "ModifySecurityGroupAttribute": doModifySecurityGroupAttribute,
     "DeleteAddressTemplate": doDeleteAddressTemplate,
     "DeleteVpnGateway": doDeleteVpnGateway,
     "CreateServiceTemplate": doCreateServiceTemplate,
     "DeleteRoutes": doDeleteRoutes,
     "ModifyDirectConnectGatewayAttribute": doModifyDirectConnectGatewayAttribute,
     "ModifySubnetAttribute": doModifySubnetAttribute,
@@ -5871,14 +6097,15 @@
     "EnableRoutes": doEnableRoutes,
     "SetCcnRegionBandwidthLimits": doSetCcnRegionBandwidthLimits,
     "CreateHaVip": doCreateHaVip,
     "ModifyServiceTemplateAttribute": doModifyServiceTemplateAttribute,
     "DeleteSecurityGroup": doDeleteSecurityGroup,
     "EnableCcnRoutes": doEnableCcnRoutes,
     "ModifyRouteTableAttribute": doModifyRouteTableAttribute,
+    "ModifyNetDetect": doModifyNetDetect,
     "DeleteNatGatewayDestinationIpPortTranslationNatRule": doDeleteNatGatewayDestinationIpPortTranslationNatRule,
     "CreateRoutes": doCreateRoutes,
     "DescribeBandwidthPackageQuota": doDescribeBandwidthPackageQuota,
     "ModifyHaVipAttribute": doModifyHaVipAttribute,
     "ReleaseAddresses": doReleaseAddresses,
     "DescribeBandwidthPackages": doDescribeBandwidthPackages,
     "CreateServiceTemplateGroup": doCreateServiceTemplateGroup,
```

### Comparing `tccli-3.0.98.1/tccli/services/cbs/v20170312/help.py` & `tccli-3.0.99.1/tccli/services/cbs/v20170312/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cbs/cbs_client.py` & `tccli-3.0.99.1/tccli/services/cbs/cbs_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tia/tia_client.py` & `tccli-3.0.99.1/tccli/services/tia/tia_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tia/v20180226/help.py` & `tccli-3.0.99.1/tccli/services/tia/v20180226/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/autoscaling/v20180419/help.py` & `tccli-3.0.99.1/tccli/services/autoscaling/v20180419/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/autoscaling/autoscaling_client.py` & `tccli-3.0.99.1/tccli/services/autoscaling/autoscaling_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/facefusion/facefusion_client.py` & `tccli-3.0.99.1/tccli/services/facefusion/facefusion_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/facefusion/v20181201/help.py` & `tccli-3.0.99.1/tccli/services/facefusion/v20181201/help.py`

 * *Files 16% similar despite different names*

```diff
@@ -128,46 +128,77 @@
 000007f0: 8896 2062 6173 6536 3429 20ef bc8c e4ba  .. base64) .....
 00000800: 8ce9 8089 e4b8 80e3 8082 7572 6ce6 9c89  ..........url...
 00000810: e695 88e6 9c9f e4b8 ba33 30e5 a4a9 e380  .........30.....
 00000820: 8222 0a20 2020 2020 207d 2c0a 2020 2020  .".      },.    
 00000830: 2020 7b0a 2020 2020 2020 2020 226e 616d    {.        "nam
 00000840: 6522 3a20 224d 6572 6765 496e 666f 7322  e": "MergeInfos"
 00000850: 2c0a 2020 2020 2020 2020 2264 6573 6322  ,.        "desc"
-00000860: 3a20 22e4 baba e884 b8e5 9bbe e789 87e5  : ".............
-00000870: 928c e5be 85e8 a2ab e89e 8de5 9088 e79a  ................
-00000880: 84e7 b4a0 e69d 90e6 a8a1 e69d bfe5 9bbe  ................
-00000890: e79a 84e4 baba e884 b8e4 bd8d e7bd aee4  ................
-000008a0: bfa1 e681 afe3 8082 220a 2020 2020 2020  ........".      
-000008b0: 7d2c 0a20 2020 2020 207b 0a20 2020 2020  },.      {.     
-000008c0: 2020 2022 6e61 6d65 223a 2022 4675 7365     "name": "Fuse
-000008d0: 5072 6f66 696c 6544 6567 7265 6522 2c0a  ProfileDegree",.
-000008e0: 2020 2020 2020 2020 2264 6573 6322 3a20          "desc": 
-000008f0: 22e8 84b8 e59e 8be8 9e8d e590 88e6 af94  "...............
-00000900: e4be 8bef bc8c e695 b0e5 80bc e8b6 8ae9  ................
-00000910: ab98 efbc 8ce8 9e8d e590 88e5 908e e79a  ................
-00000920: 84e8 84b8 e59e 8be8 b68a e583 8fe7 b4a0  ................
-00000930: e69d 90e4 baba e789 a9e3 8082 e58f 96e5  ................
-00000940: 80bc e88c 83e5 9bb4 5b30 2c31 3030 5d20  ........[0,100] 
-00000950: 5c6e e88b a5e6 ada4 e58f 82e6 95b0 e4b8  \n..............
-00000960: 8de5 a1ab e586 99ef bc8c e588 99e4 bdbf  ................
-00000970: e794 a8e4 baba e884 b8e8 9e8d e590 88e6  ................
-00000980: 8ea7 e588 b6e5 8fb0 e4b8 ade8 84b8 e59e  ................
-00000990: 8be5 8f82 e695 b0e6 95b0 e580 bce3 8082  ................
-000009a0: 220a 2020 2020 2020 7d2c 0a20 2020 2020  ".      },.     
-000009b0: 207b 0a20 2020 2020 2020 2022 6e61 6d65   {.        "name
-000009c0: 223a 2022 4675 7365 4661 6365 4465 6772  ": "FuseFaceDegr
-000009d0: 6565 222c 0a20 2020 2020 2020 2022 6465  ee",.        "de
-000009e0: 7363 223a 2022 e4ba 94e5 ae98 e89e 8de5  sc": "..........
-000009f0: 9088 e6af 94e4 be8b efbc 8ce6 95b0 e580  ................
-00000a00: bce8 b68a e9ab 98ef bc8c e89e 8de5 9088  ................
-00000a10: e590 8ee7 9a84 e4ba 94e5 ae98 e8b6 8ae5  ................
-00000a20: 838f e7b4 a0e6 9d90 e4ba bae7 89a9 e380  ................
-00000a30: 82e5 8f96 e580 bce8 8c83 e59b b45b 302c  .............[0,
-00000a40: 3130 305d 205c 6ee8 8ba5 e6ad a4e5 8f82  100] \n.........
-00000a50: e695 b0e4 b88d e5a1 abe5 8699 efbc 8ce5  ................
-00000a60: 8899 e4bd bfe7 94a8 e4ba bae8 84b8 e89e  ................
-00000a70: 8de5 9088 e68e a7e5 88b6 e58f b0e4 b8ad  ................
-00000a80: e4ba 94e5 ae98 e58f 82e6 95b0 e695 b0e5  ................
-00000a90: 80bc e380 8222 0a20 2020 2020 207d 0a20  .....".      }. 
-00000aa0: 2020 205d 2c0a 2020 2020 2264 6573 6322     ],.    "desc"
-00000ab0: 3a20 22e9 8089 e884 b8e8 9e8d e590 8822  : "............"
-00000ac0: 0a20 207d 0a7d                           .  }.}
+00000860: 3a20 22e7 94a8 e688 b7e4 baba e884 b8e5  : ".............
+00000870: 9bbe e789 87e3 8081 e7b4 a0e6 9d90 e6a8  ................
+00000880: a1e6 9dbf e59b bee7 9a84 e4ba bae8 84b8  ................
+00000890: e4bd 8de7 bdae e4bf a1e6 81af e380 8222  ..............."
+000008a0: 0a20 2020 2020 207d 2c0a 2020 2020 2020  .      },.      
+000008b0: 7b0a 2020 2020 2020 2020 226e 616d 6522  {.        "name"
+000008c0: 3a20 2246 7573 6550 726f 6669 6c65 4465  : "FuseProfileDe
+000008d0: 6772 6565 222c 0a20 2020 2020 2020 2022  gree",.        "
+000008e0: 6465 7363 223a 2022 e884 b8e5 9e8b e89e  desc": "........
+000008f0: 8de5 9088 e6af 94e4 be8b efbc 8ce6 95b0  ................
+00000900: e580 bce8 b68a e9ab 98ef bc8c e89e 8de5  ................
+00000910: 9088 e590 8ee7 9a84 e884 b8e5 9e8b e8b6  ................
+00000920: 8ae5 838f e7b4 a0e6 9d90 e4ba bae7 89a9  ................
+00000930: e380 82e5 8f96 e580 bce8 8c83 e59b b45b  ...............[
+00000940: 302c 3130 305d 205c 6ee8 8ba5 e6ad a4e5  0,100] \n.......
+00000950: 8f82 e695 b0e4 b88d e5a1 abe5 8699 efbc  ................
+00000960: 8ce5 8899 e4bd bfe7 94a8 e4ba bae8 84b8  ................
+00000970: e89e 8de5 9088 e68e a7e5 88b6 e58f b0e4  ................
+00000980: b8ad e884 b8e5 9e8b e58f 82e6 95b0 e695  ................
+00000990: b0e5 80bc e380 8222 0a20 2020 2020 207d  .......".      }
+000009a0: 2c0a 2020 2020 2020 7b0a 2020 2020 2020  ,.      {.      
+000009b0: 2020 226e 616d 6522 3a20 2246 7573 6546    "name": "FuseF
+000009c0: 6163 6544 6567 7265 6522 2c0a 2020 2020  aceDegree",.    
+000009d0: 2020 2020 2264 6573 6322 3a20 22e4 ba94      "desc": "...
+000009e0: e5ae 98e8 9e8d e590 88e6 af94 e4be 8bef  ................
+000009f0: bc8c e695 b0e5 80bc e8b6 8ae9 ab98 efbc  ................
+00000a00: 8ce8 9e8d e590 88e5 908e e79a 84e4 ba94  ................
+00000a10: e5ae 98e8 b68a e583 8fe7 b4a0 e69d 90e4  ................
+00000a20: baba e789 a9e3 8082 e58f 96e5 80bc e88c  ................
+00000a30: 83e5 9bb4 5b30 2c31 3030 5d20 5c6e e88b  ....[0,100] \n..
+00000a40: a5e6 ada4 e58f 82e6 95b0 e4b8 8de5 a1ab  ................
+00000a50: e586 99ef bc8c e588 99e4 bdbf e794 a8e4  ................
+00000a60: baba e884 b8e8 9e8d e590 88e6 8ea7 e588  ................
+00000a70: b6e5 8fb0 e4b8 ade4 ba94 e5ae 98e5 8f82  ................
+00000a80: e695 b0e6 95b0 e580 bce3 8082 220a 2020  ............".  
+00000a90: 2020 2020 7d0a 2020 2020 5d2c 0a20 2020      }.    ],.   
+00000aa0: 2022 6465 7363 223a 2022 e69c ace6 8ea5   "desc": "......
+00000ab0: e58f a3e7 94a8 e4ba 8ee5 8d95 e884 b8e3  ................
+00000ac0: 8081 e5a4 9ae8 84b8 e89e 8de5 9088 efbc  ................
+00000ad0: 8ce7 94a8 e688 b7e4 b88a e4bc a0e4 baba  ................
+00000ae0: e884 b8e5 9bbe e789 87ef bc8c e88e b7e5  ................
+00000af0: 8f96 e4b8 8ee6 a8a1 e69d bfe8 9e8d e590  ................
+00000b00: 88e5 908e e79a 84e4 baba e884 b8e5 9bbe  ................
+00000b10: e789 87e3 8082 e69f a5e7 9c8b 203c 6120  ............ <a 
+00000b20: 6872 6566 3d5c 2268 7474 7073 3a2f 2f63  href=\"https://c
+00000b30: 6c6f 7564 2e74 656e 6365 6e74 2e63 6f6d  loud.tencent.com
+00000b40: 2f64 6f63 756d 656e 742f 7072 6f64 7563  /document/produc
+00000b50: 742f 3637 302f 3338 3234 375c 2220 7461  t/670/38247\" ta
+00000b60: 7267 6574 3d5c 225f 626c 616e 6b5c 223e  rget=\"_blank\">
+00000b70: e980 89e8 84b8 e89e 8de5 9088 e68e a5e5  ................
+00000b80: 85a5 e68c 87e5 bc95 3c2f 613e e380 825c  ........</a>...\
+00000b90: 6e5c 6ee6 9caa e58f 91e5 b883 e79a 84e6  n\n.............
+00000ba0: b4bb e58a a8e8 afb7 e6b1 82e9 a291 e78e  ................
+00000bb0: 87e9 9990 e588 b6e4 b8ba 31e6 aca1 2fe7  ..........1.../.
+00000bc0: a792 efbc 8ce5 b7b2 e58f 91e5 b883 e79a  ................
+00000bd0: 84e6 b4bb e58a a8e8 afb7 e6b1 82e9 a291  ................
+00000be0: e78e 87e9 9990 e588 b635 30e6 aca1 2fe7  .........50.../.
+00000bf0: a792 e380 82e5 a682 e69c 89e9 9c80 e8a6  ................
+00000c00: 81e6 8f90 e9ab 98e6 b4bb e58a a8e7 9a84  ................
+00000c10: e8af b7e6 b182 e9a2 91e7 8e87 e999 90e5  ................
+00000c20: 88b6 efbc 8ce8 afb7 e59c a8e6 8ea7 e588  ................
+00000c30: b6e5 8fb0 e4b8 ade7 94b3 e8af b7e3 8082  ................
+00000c40: 5c6e 3e5c 6e2d 20e5 85ac e585 b1e5 8f82  \n>\n- .........
+00000c50: e695 b0e4 b8ad e79a 84e7 adbe e590 8de6  ................
+00000c60: 96b9 e5bc 8fe5 bf85 e9a1 bbe6 8c87 e5ae  ................
+00000c70: 9ae4 b8ba 5633 e789 88e6 9cac efbc 8ce5  ....V3..........
+00000c80: 8db3 e985 8de7 bdae 5369 676e 6174 7572  ........Signatur
+00000c90: 654d 6574 686f 64e5 8f82 e695 b0e4 b8ba  eMethod.........
+00000ca0: 5443 332d 484d 4143 2d53 4841 3235 36e3  TC3-HMAC-SHA256.
+00000cb0: 8082 220a 2020 7d0a 7d                   ..".  }.}
```

### Comparing `tccli-3.0.98.1/tccli/services/yunjing/yunjing_client.py` & `tccli-3.0.99.1/tccli/services/yunjing/yunjing_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/yunjing/v20180228/help.py` & `tccli-3.0.99.1/tccli/services/yunjing/v20180228/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/vod/vod_client.py` & `tccli-3.0.99.1/tccli/services/vod/vod_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/vod/v20180717/help.py` & `tccli-3.0.99.1/tccli/services/vod/v20180717/help.py`

 * *Files 0% similar despite different names*

```diff
@@ -495,15 +495,15 @@
         "desc": "指定所有媒体文件需要返回的信息，可同时指定多个信息，N 从 0 开始递增。如果未填写该字段，默认返回所有信息。选项有：\n<li>basicInfo（视频基础信息）。</li>\n<li>metaData（视频元信息）。</li>\n<li>transcodeInfo（视频转码结果信息）。</li>\n<li>animatedGraphicsInfo（视频转动图结果信息）。</li>\n<li>imageSpriteInfo（视频雪碧图信息）。</li>\n<li>snapshotByTimeOffsetInfo（视频指定时间点截图信息）。</li>\n<li>sampleSnapshotInfo（采样截图信息）。</li>\n<li>keyFrameDescInfo（打点信息）。</li>\n<li>adaptiveDynamicStreamingInfo（转自适应码流信息）。</li>\n<li>miniProgramReviewInfo（小程序审核信息）。</li>"
       },
       {
         "name": "SubAppId",
         "desc": "点播[子应用](/document/product/266/14574) ID 。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
       }
     ],
-    "desc": "1. 该接口可以获取多个视频的多种信息，包括：\n    1. 基础信息（basicInfo）：包括视频名称、分类、播放地址、封面图片等。\n    2. 元信息（metaData）：包括大小、时长、视频流信息、音频流信息等。\n    3. 转码结果信息（transcodeInfo）：包括该视频转码生成的各种码率的视频的地址、规格、码率、分辨率等。\n    4. 转动图结果信息（animatedGraphicsInfo）：对视频转动图（如 gif）后，动图相关信息。\n    5. 采样截图信息（sampleSnapshotInfo）：对视频采样截图后，相关截图信息。\n    6. 雪碧图信息（imageSpriteInfo）：对视频截取雪碧图之后，雪碧图的相关信息。\n    7. 指定时间点截图信息（snapshotByTimeOffsetInfo）：对视频依照指定时间点截图后，各个截图的信息。\n    8. 视频打点信息（keyFrameDescInfo）：对视频设置的各个打点信息。\n    9. 转自适应码流信息（adaptiveDynamicStreamingInfo）：包括规格、加密类型、打包格式等相关信息。\n2. 可以指定回包只返回部分信息。"
+    "desc": "1. 该接口可以获取多个媒体文件的多种信息，包括：\n    1. 基础信息（basicInfo）：包括媒体名称、分类、播放地址、封面图片等。\n    2. 元信息（metaData）：包括大小、时长、视频流信息、音频流信息等。\n    3. 转码结果信息（transcodeInfo）：包括该媒体转码生成的各种规格的媒体地址、视频流参数、音频流参数等。\n    4. 转动图结果信息（animatedGraphicsInfo）：对视频转动图（如 gif）后的动图信息。\n    5. 采样截图信息（sampleSnapshotInfo）：对视频采样截图后的截图信息。\n    6. 雪碧图信息（imageSpriteInfo）：对视频截取雪碧图后的雪碧图信息。\n    7. 指定时间点截图信息（snapshotByTimeOffsetInfo）：对视频依照指定时间点截图后，的截图信息。\n    8. 视频打点信息（keyFrameDescInfo）：对视频设置的打点信息。\n    9. 转自适应码流信息（adaptiveDynamicStreamingInfo）：包括规格、加密类型、打包格式等相关信息。\n2. 可以指定回包只返回部分信息。"
   },
   "DescribeAIAnalysisTemplates": {
     "params": [
       {
         "name": "Definitions",
         "desc": "视频内容分析模板唯一标识过滤条件，数组长度最大值：100。"
       },
@@ -1755,15 +1755,15 @@
     ],
     "desc": "查询转自适应码流模板，支持根据条件，分页查询。"
   },
   "ProcessMedia": {
     "params": [
       {
         "name": "FileId",
-        "desc": "媒体文件 ID。"
+        "desc": "媒体文件 ID，即该文件在云点播上的全局唯一标识符，在上传成功后由云点播后台分配。可以在 [视频上传完成事件通知](/document/product/266/7830) 或 [云点播控制台](https://console.cloud.tencent.com/vod/media) 获取该字段。"
       },
       {
         "name": "MediaProcessTask",
         "desc": "视频处理类型任务参数。"
       },
       {
         "name": "AiContentReviewTask",
```

### Comparing `tccli-3.0.98.1/tccli/services/mongodb/v20180408/help.py` & `tccli-3.0.99.1/tccli/services/mongodb/v20180408/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/mongodb/mongodb_client.py` & `tccli-3.0.99.1/tccli/services/mongodb/mongodb_client.py`

 * *Files 13% similar despite different names*

```diff
@@ -10,16 +10,20 @@
 from tccli.utils import Utils
 from tccli.configure import Configure
 from tencentcloud.common import credential
 from tencentcloud.common.profile.http_profile import HttpProfile
 from tencentcloud.common.profile.client_profile import ClientProfile
 from tencentcloud.mongodb.v20180408 import mongodb_client as mongodb_client_v20180408
 from tencentcloud.mongodb.v20180408 import models as models_v20180408
+from tencentcloud.mongodb.v20190725 import mongodb_client as mongodb_client_v20190725
+from tencentcloud.mongodb.v20190725 import models as models_v20190725
 from tccli.services.mongodb import v20180408
 from tccli.services.mongodb.v20180408 import help as v20180408_help
+from tccli.services.mongodb import v20190725
+from tccli.services.mongodb.v20190725 import help as v20190725_help
 
 
 def doAssignProject(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
         show_help("AssignProject", g_param[OptionsDefine.Version])
         return
@@ -88,27 +92,30 @@
 def doCreateDBInstance(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
         show_help("CreateDBInstance", g_param[OptionsDefine.Version])
         return
 
     param = {
-        "SecondaryNum": Utils.try_to_json(argv, "--SecondaryNum"),
+        "NodeNum": Utils.try_to_json(argv, "--NodeNum"),
         "Memory": Utils.try_to_json(argv, "--Memory"),
         "Volume": Utils.try_to_json(argv, "--Volume"),
         "MongoVersion": argv.get("--MongoVersion"),
-        "MachineCode": argv.get("--MachineCode"),
         "GoodsNum": Utils.try_to_json(argv, "--GoodsNum"),
         "Zone": argv.get("--Zone"),
-        "TimeSpan": Utils.try_to_json(argv, "--TimeSpan"),
-        "Password": argv.get("--Password"),
+        "Period": Utils.try_to_json(argv, "--Period"),
+        "MachineCode": argv.get("--MachineCode"),
+        "ClusterType": argv.get("--ClusterType"),
+        "ReplicateSetNum": Utils.try_to_json(argv, "--ReplicateSetNum"),
         "ProjectId": Utils.try_to_json(argv, "--ProjectId"),
-        "SecurityGroup": Utils.try_to_json(argv, "--SecurityGroup"),
-        "UniqVpcId": argv.get("--UniqVpcId"),
-        "UniqSubnetId": argv.get("--UniqSubnetId"),
+        "VpcId": argv.get("--VpcId"),
+        "SubnetId": argv.get("--SubnetId"),
+        "Password": argv.get("--Password"),
+        "Tags": Utils.try_to_json(argv, "--Tags"),
+        "AutoRenewFlag": Utils.try_to_json(argv, "--AutoRenewFlag"),
 
     }
     cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
     http_profile = HttpProfile(
         reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
         reqMethod="POST",
         endpoint=g_param[OptionsDefine.Endpoint]
@@ -169,26 +176,25 @@
         show_help("CreateDBInstanceHour", g_param[OptionsDefine.Version])
         return
 
     param = {
         "Memory": Utils.try_to_json(argv, "--Memory"),
         "Volume": Utils.try_to_json(argv, "--Volume"),
         "ReplicateSetNum": Utils.try_to_json(argv, "--ReplicateSetNum"),
-        "SecondaryNum": Utils.try_to_json(argv, "--SecondaryNum"),
-        "EngineVersion": argv.get("--EngineVersion"),
-        "Machine": argv.get("--Machine"),
+        "NodeNum": Utils.try_to_json(argv, "--NodeNum"),
+        "MongoVersion": argv.get("--MongoVersion"),
+        "MachineCode": argv.get("--MachineCode"),
         "GoodsNum": Utils.try_to_json(argv, "--GoodsNum"),
         "Zone": argv.get("--Zone"),
-        "InstanceRole": argv.get("--InstanceRole"),
-        "InstanceType": argv.get("--InstanceType"),
-        "Encrypt": Utils.try_to_json(argv, "--Encrypt"),
+        "ClusterType": argv.get("--ClusterType"),
         "VpcId": argv.get("--VpcId"),
         "SubnetId": argv.get("--SubnetId"),
+        "Password": argv.get("--Password"),
         "ProjectId": Utils.try_to_json(argv, "--ProjectId"),
-        "SecurityGroup": Utils.try_to_json(argv, "--SecurityGroup"),
+        "Tags": Utils.try_to_json(argv, "--Tags"),
 
     }
     cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
     http_profile = HttpProfile(
         reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
         reqMethod="POST",
         endpoint=g_param[OptionsDefine.Endpoint]
@@ -470,14 +476,16 @@
         "VpcId": argv.get("--VpcId"),
         "SubnetId": argv.get("--SubnetId"),
         "PayMode": Utils.try_to_json(argv, "--PayMode"),
         "Limit": Utils.try_to_json(argv, "--Limit"),
         "Offset": Utils.try_to_json(argv, "--Offset"),
         "OrderBy": argv.get("--OrderBy"),
         "OrderByType": argv.get("--OrderByType"),
+        "ProjectIds": Utils.try_to_json(argv, "--ProjectIds"),
+        "SearchKey": argv.get("--SearchKey"),
 
     }
     cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
     http_profile = HttpProfile(
         reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
         reqMethod="POST",
         endpoint=g_param[OptionsDefine.Endpoint]
@@ -495,21 +503,192 @@
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
+def doModifyDBInstanceSpec(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("ModifyDBInstanceSpec", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "InstanceId": argv.get("--InstanceId"),
+        "Memory": Utils.try_to_json(argv, "--Memory"),
+        "Volume": Utils.try_to_json(argv, "--Volume"),
+        "OplogSize": Utils.try_to_json(argv, "--OplogSize"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.MongodbClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.ModifyDBInstanceSpecRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.ModifyDBInstanceSpec(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
+def doOfflineIsolatedDBInstance(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("OfflineIsolatedDBInstance", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "InstanceId": argv.get("--InstanceId"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.MongodbClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.OfflineIsolatedDBInstanceRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.OfflineIsolatedDBInstance(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
+def doDescribeDBBackups(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("DescribeDBBackups", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "InstanceId": argv.get("--InstanceId"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.MongodbClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.DescribeDBBackupsRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.DescribeDBBackups(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
+def doIsolateDBInstance(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("IsolateDBInstance", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "InstanceId": argv.get("--InstanceId"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.MongodbClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.IsolateDBInstanceRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.IsolateDBInstance(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
+def doDescribeBackupAccess(argv, arglist):
+    g_param = parse_global_arg(argv)
+    if "help" in argv:
+        show_help("DescribeBackupAccess", g_param[OptionsDefine.Version])
+        return
+
+    param = {
+        "InstanceId": argv.get("--InstanceId"),
+        "BackupName": argv.get("--BackupName"),
+
+    }
+    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
+    http_profile = HttpProfile(
+        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
+        reqMethod="POST",
+        endpoint=g_param[OptionsDefine.Endpoint]
+    )
+    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
+    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
+    client = mod.MongodbClient(cred, g_param[OptionsDefine.Region], profile)
+    client._sdkVersion += ("_CLI_" + __version__)
+    models = MODELS_MAP[g_param[OptionsDefine.Version]]
+    model = models.DescribeBackupAccessRequest()
+    model.from_json_string(json.dumps(param))
+    rsp = client.DescribeBackupAccess(model)
+    result = rsp.to_json_string()
+    jsonobj = None
+    try:
+        jsonobj = json.loads(result)
+    except TypeError as e:
+        jsonobj = json.loads(result.decode('utf-8')) # python3.3
+    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
+
+
 CLIENT_MAP = {
     "v20180408": mongodb_client_v20180408,
+    "v20190725": mongodb_client_v20190725,
 
 }
 
 MODELS_MAP = {
     "v20180408": models_v20180408,
+    "v20190725": models_v20190725,
 
 }
 
 ACTION_MAP = {
     "AssignProject": doAssignProject,
     "TerminateDBInstance": doTerminateDBInstance,
     "CreateDBInstance": doCreateDBInstance,
@@ -519,23 +698,30 @@
     "RenameInstance": doRenameInstance,
     "UpgradeDBInstance": doUpgradeDBInstance,
     "SetAutoRenew": doSetAutoRenew,
     "DescribeSpecInfo": doDescribeSpecInfo,
     "SetPassword": doSetPassword,
     "UpgradeDBInstanceHour": doUpgradeDBInstanceHour,
     "DescribeDBInstances": doDescribeDBInstances,
+    "ModifyDBInstanceSpec": doModifyDBInstanceSpec,
+    "OfflineIsolatedDBInstance": doOfflineIsolatedDBInstance,
+    "DescribeDBBackups": doDescribeDBBackups,
+    "IsolateDBInstance": doIsolateDBInstance,
+    "DescribeBackupAccess": doDescribeBackupAccess,
 
 }
 
 AVAILABLE_VERSION_LIST = [
     v20180408.version,
+    v20190725.version,
 
 ]
 AVAILABLE_VERSIONS = {
      'v' + v20180408.version.replace('-', ''): {"help": v20180408_help.INFO,"desc": v20180408_help.DESC},
+     'v' + v20190725.version.replace('-', ''): {"help": v20190725_help.INFO,"desc": v20190725_help.DESC},
 
 }
 
 
 def mongodb_action(argv, arglist):
     if "help" in argv:
         versions = sorted(AVAILABLE_VERSIONS.keys())
```

### Comparing `tccli-3.0.98.1/tccli/services/cim/cim_client.py` & `tccli-3.0.99.1/tccli/services/cim/cim_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/wss/wss_client.py` & `tccli-3.0.99.1/tccli/services/wss/wss_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/wss/v20180426/help.py` & `tccli-3.0.99.1/tccli/services/wss/v20180426/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/dc/dc_client.py` & `tccli-3.0.99.1/tccli/services/dc/dc_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/dc/v20180410/help.py` & `tccli-3.0.99.1/tccli/services/dc/v20180410/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/gme/v20180711/help.py` & `tccli-3.0.99.1/tccli/services/gme/v20180711/help.py`

 * *Files 24% similar despite different names*

```diff
@@ -10,27 +10,77 @@
       {
         "name": "FileId",
         "desc": "文件ID"
       }
     ],
     "desc": "根据应用ID和文件ID查询识别结果"
   },
+  "DescribeAppStatistics": {
+    "params": [
+      {
+        "name": "BizId",
+        "desc": "GME应用id"
+      },
+      {
+        "name": "StartDate",
+        "desc": "数据开始时间，东八区时间，格式: 年-月-日，如: 2018-07-13"
+      },
+      {
+        "name": "EndDate",
+        "desc": "数据结束时间，东八区时间，格式: 年-月-日，如: 2018-07-13"
+      },
+      {
+        "name": "Services",
+        "desc": "要查询的服务列表，取值：RealTimeSpeech/VoiceMessage/VoiceFilter"
+      }
+    ],
+    "desc": "本接口(DescribeAppStatistics)用户获取某个GME应用的用量数据。包括实时语音，离线语音，语音过滤等。最长查询周期为最近30天。"
+  },
   "DescribeScanResultList": {
     "params": [
       {
         "name": "BizId",
-        "desc": "应用 ID，在控制台统一创建。"
+        "desc": "应用 ID，登录[控制台](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID"
       },
       {
         "name": "TaskIdList",
         "desc": "查询的任务 ID 列表，任务 ID 列表最多支持 100 个。"
       }
     ],
     "desc": "本接口(DescribeScanResultList)用于查询语音检测结果，查询任务列表最多支持100个。\n<p style=\"color:red\">如果在提交语音检测任务时未设置 Callback 字段，则需要通过本接口获取检测结果</p>"
   },
+  "VoiceFilter": {
+    "params": [
+      {
+        "name": "BizId",
+        "desc": "应用ID，登录[控制台](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID"
+      },
+      {
+        "name": "FileId",
+        "desc": "文件ID，表示文件唯一ID"
+      },
+      {
+        "name": "FileName",
+        "desc": "文件名"
+      },
+      {
+        "name": "FileUrl",
+        "desc": "文件url，urlencode编码，FileUrl和FileContent二选一"
+      },
+      {
+        "name": "FileContent",
+        "desc": "文件内容，base64编码，FileUrl和FileContent二选一"
+      },
+      {
+        "name": "OpenId",
+        "desc": "用户ID"
+      }
+    ],
+    "desc": "本接口用于识别涉黄、涉政等违规音频，成功会回调配置在应用的回调地址。回调示例如下：\n{\"BizId\":0,\"FileId\":\"test_file_id\",\"FileName\":\"test_file_name\",\"FileUrl\":\"test_file_url\",\"OpenId\":\"test_open_id\",\"TimeStamp\":\"0000-00-00 00:00:00\",\"Data\":[{\"Type\":1,\"Word\":\"xx\"}]}\nType表示过滤类型，1：政治，2：色情，3：谩骂"
+  },
   "DescribeFilterResultList": {
     "params": [
       {
         "name": "BizId",
         "desc": "应用ID"
       },
       {
@@ -52,15 +102,15 @@
     ],
     "desc": "根据日期查询识别结果列表"
   },
   "ScanVoice": {
     "params": [
       {
         "name": "BizId",
-        "desc": "应用ID，登录控制台创建应用得到的AppID。"
+        "desc": "应用ID，登录[控制台 - 服务管理](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID"
       },
       {
         "name": "Scenes",
         "desc": "语音检测场景，参数值目前要求为 default。 预留场景设置： 谩骂、色情、涉政、广告、暴恐、违禁等场景，<a href=\"#Label_Value\">具体取值见上述 Label 说明。</a>"
       },
       {
         "name": "Live",
@@ -71,39 +121,60 @@
         "desc": "语音检测任务列表，列表最多支持100个检测任务。结构体中包含：\n<li>DataId：数据的唯一ID</li>\n<li>Url：数据文件的url，为 urlencode 编码，流式则为拉流地址</li>"
       },
       {
         "name": "Callback",
         "desc": "异步检测结果回调地址，具体见上述<a href=\"#Callback_Declare\">回调相关说明</a>。（说明：该字段为空时，必须通过接口(查询语音检测结果)获取检测结果）。"
       }
     ],
-    "desc": "本接口(ScanVoice)用于提交语音检测任务，检测任务列表最多支持100个。\n</br></br>\n<h4><b>接口功能说明：</b></h4>\n<li>支持对语音流或语音文件进行检测，判断其中是否包含违规内容。</li>\n<li>支持设置回调地址 Callback 获取检测结果，同时支持通过接口(查询语音检测结果)主动轮询获取检测结果。</li>\n<li>支持场景输入，包括：谩骂、色情、涉政等场景</li>\n<li>支持批量提交检测任务。检测任务列表最多支持100个。</li>\n</br>\n<h4><b>音频文件限制说明：</b></h4>\n<li>音频文件大小限制：100 M</li>\n<li>音频文件时长限制：30分钟</li>\n<li>音频文件格式支持的类型：.wav、.m4a、.amr、.mp3、.aac、.wma、.ogg</li>\n</br>\n<h4><b>语音流限制说明：</b></h4>\n<li>语音流格式支持的类型：.m3u8、.flv</li>\n<li>语音流支持的传输协议：RTMP、HTTP、HTTPS</li>\n<li>语音流时长限制：4小时</li>\n<li>支持音视频流分离并对音频流进行分析</li>\n</br>\n<h4 id=\"Label_Value\"><b>Scenes 与 Label 参数说明：</b></h4>\n<p>提交语音检测任务时，需要指定 Scenes 场景参数，<font color=\"red\">目前要求您设置 Scenes 参数值为：[\"default\"]</font>；而在检测结果中，则包含请求时指定的场景，以及对应类型的检测结果。</p>\n<table>\n<thread>\n<tr>\n<th>场景</th>\n<th>描述</th>\n<th>Label</th>\n</tr>\n</thread>\n<tbody>\n<tr>\n<td>语音检测</td>\n<td>语音检测的检测类型</td>\n<td>\n<p>normal:正常文本</p>\n<p>porn:色情</p>\n<p>politics:涉政</p>\n<p>abuse:谩骂</p>\n<p>ad :广告</p>\n<p>terrorism:暴恐</p>\n<p>contraband :违禁</p>\n<p>customized:自定义词库</p>\n</td>\n</tr>\n</tbody>\n</table>\n</br>\n<h4 id=\"Callback_Declare\"><b>回调相关说明：</b></h4>\n<li>如果在请求参数中指定了回调地址参数 Callback，即一个 HTTP(S) 协议接口的 URL，则需要支持 POST 方法，传输数据编码采用 UTF-8。</li>\n<li>在推送回调数据后，接收到的 HTTP 状态码为 200 时，表示推送成功。</li>\n<li>HTTP 头参数说明：</li>\n<table>\n<thread>\n<tr>\n<th>名称</th>\n<th>类型</th>\n<th>是否必需</th>\n<th>描述</th>\n</tr>\n</thread>\n<tbody>\n<tr>\n<td>Signatue</td>\n<td>string</td>\n<td>是</td>\n<td>签名，具体见<a href=\"#Callback_Signatue\">签名生成说明</a></td>\n</tr>\n</tbody>\n</table>\n<ul  id=\"Callback_Signatue\">\n\t<li>签名生成说明：</li>\n\t<ul>\n\t\t<li>使用 HMAC-SH1 算法, 最终结果做 BASE64 编码;</li>\n\t\t<li>签名原文串为 POST+body 的整个json内容(长度以 Content-Length 为准);</li>\n\t\t<li>签名key为应用的 secrectkey，可以通过控制台查看。</li>\n\t</ul>\n</ul>\n\n<ul>\n<li>\n回调请求 Body 的字段说明见结构：\n<a href=\"https://cloud.tencent.com/document/api/607/35375#DescribeScanResult\" target=\"_blank\">DescribeScanResult</a>\n</li>\n</ul>\n\n<li>回调示例如下<font color=\"red\">（详细字段说明见上述表格中 Data 字段说明）</font>：</li>\n<pre><code>{\n\t\"Code\": 0,\n\t\"DataId\": \"1400000000_test_data_id\",\n\t\"ScanFinishTime\": 1566720906,\n\t\"HitFlag\": true,\n\t\"Live\": false,\n\t\"Msg\": \"\",\n\t\"ScanPiece\": [{\n\t\t\"DumpUrl\": \"\",\n\t\t\"HitFlag\": true,\n\t\t\"MainType\": \"abuse\",\n\t\t\"RoomId\": \"123\",\n\t\t\"OpenId\": \"xxx\",\n\t\t\"ScanDetail\": [{\n\t\t\t\"EndTime\": 1110,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 1110\n\t\t}, {\n\t\t\t\"EndTime\": 1380,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 930\n\t\t}, {\n\t\t\t\"EndTime\": 1560,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 930\n\t\t}, {\n\t\t\t\"EndTime\": 2820,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 2490\n\t\t}]\n\t}],\n\t\"ScanStartTime\": 1566720905,\n\t\"Scenes\": [\n\t\t\"default\"\n\t],\n\t\"Status\": \"Success\",\n\t\"TaskId\": \"xxx\",\n\t\"Url\": \"https://xxx/xxx.m4a\"\n}\n</code></pre>"
+    "desc": "本接口(ScanVoice)用于提交语音检测任务，检测任务列表最多支持100个。使用前请您登录[控制台 - 服务配置](https://console.cloud.tencent.com/gamegme/conf)开启语音分析服务。\n</br></br>\n\n<h4><b>功能试用说明：</b></h4>\n<li>打开前往<a href=\"https://console.cloud.tencent.com/gamegme/tryout\">控制台 - 产品试用</a>免费试用语音分析服务。</li>\n</br>\n\n<h4><b>接口功能说明：</b></h4>\n<li>支持对语音流或语音文件进行检测，判断其中是否包含违规内容。</li>\n<li>支持设置回调地址 Callback 获取检测结果，同时支持通过接口(查询语音检测结果)主动轮询获取检测结果。</li>\n<li>支持场景输入，包括：谩骂、色情、涉政等场景</li>\n<li>支持批量提交检测任务。检测任务列表最多支持100个。</li>\n</br>\n<h4><b>音频文件限制说明：</b></h4>\n<li>音频文件大小限制：100 M</li>\n<li>音频文件时长限制：30分钟</li>\n<li>音频文件格式支持的类型：.wav、.m4a、.amr、.mp3、.aac、.wma、.ogg</li>\n</br>\n<h4><b>语音流限制说明：</b></h4>\n<li>语音流格式支持的类型：.m3u8、.flv</li>\n<li>语音流支持的传输协议：RTMP、HTTP、HTTPS</li>\n<li>语音流时长限制：4小时</li>\n<li>支持音视频流分离并对音频流进行分析</li>\n</br>\n<h4 id=\"Label_Value\"><b>Scenes 与 Label 参数说明：</b></h4>\n<p>提交语音检测任务时，需要指定 Scenes 场景参数，<font color=\"red\">目前要求您设置 Scenes 参数值为：[\"default\"]</font>；而在检测结果中，则包含请求时指定的场景，以及对应类型的检测结果。</p>\n<table>\n<thread>\n<tr>\n<th>场景</th>\n<th>描述</th>\n<th>Label</th>\n</tr>\n</thread>\n<tbody>\n<tr>\n<td>语音检测</td>\n<td>语音检测的检测类型</td>\n<td>\n<p>normal:正常文本</p>\n<p>porn:色情</p>\n<p>politics:涉政</p>\n<p>abuse:谩骂</p>\n<p>ad :广告</p>\n<p>terrorism:暴恐</p>\n<p>contraband :违禁</p>\n<p>customized:自定义词库。目前白名单开放，如有需要请<a href=\"https://cloud.tencent.com/apply/p/8809fjcik56\">联系我们</a>。</p>\n</td>\n</tr>\n</tbody>\n</table>\n</br>\n<h4 id=\"Callback_Declare\"><b>回调相关说明：</b></h4>\n<li>如果在请求参数中指定了回调地址参数 Callback，即一个 HTTP(S) 协议接口的 URL，则需要支持 POST 方法，传输数据编码采用 UTF-8。</li>\n<li>在推送回调数据后，接收到的 HTTP 状态码为 200 时，表示推送成功。</li>\n<li>HTTP 头参数说明：</li>\n<table>\n<thread>\n<tr>\n<th>名称</th>\n<th>类型</th>\n<th>是否必需</th>\n<th>描述</th>\n</tr>\n</thread>\n<tbody>\n<tr>\n<td>Signatue</td>\n<td>string</td>\n<td>是</td>\n<td>签名，具体见<a href=\"#Callback_Signatue\">签名生成说明</a></td>\n</tr>\n</tbody>\n</table>\n<ul  id=\"Callback_Signatue\">\n\t<li>签名生成说明：</li>\n\t<ul>\n\t\t<li>使用 HMAC-SH1 算法, 最终结果做 BASE64 编码;</li>\n\t\t<li>签名原文串为 POST+body 的整个json内容(长度以 Content-Length 为准);</li>\n\t\t<li>签名key为应用的 secrectkey，可以通过控制台查看。</li>\n\t</ul>\n</ul>\n\n<li>回调示例如下<font color=\"red\">（详细字段说明见结构：\n<a href=\"https://cloud.tencent.com/document/api/607/35375#DescribeScanResult\" target=\"_blank\">DescribeScanResult</a>）</font>：</li>\n<pre><code>{\n\t\"Code\": 0,\n\t\"DataId\": \"1400000000_test_data_id\",\n\t\"ScanFinishTime\": 1566720906,\n\t\"HitFlag\": true,\n\t\"Live\": false,\n\t\"Msg\": \"\",\n\t\"ScanPiece\": [{\n\t\t\"DumpUrl\": \"\",\n\t\t\"HitFlag\": true,\n\t\t\"MainType\": \"abuse\",\n\t\t\"RoomId\": \"123\",\n\t\t\"OpenId\": \"xxx\",\n\t\t\"Info\":\"\",\n\t\t\"ScanDetail\": [{\n\t\t\t\"EndTime\": 1110,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 1110\n\t\t}, {\n\t\t\t\"EndTime\": 1380,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 930\n\t\t}, {\n\t\t\t\"EndTime\": 1560,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 930\n\t\t}, {\n\t\t\t\"EndTime\": 2820,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 2490\n\t\t}]\n\t}],\n\t\"ScanStartTime\": 1566720905,\n\t\"Scenes\": [\n\t\t\"default\"\n\t],\n\t\"Status\": \"Success\",\n\t\"TaskId\": \"xxx\",\n\t\"Url\": \"https://xxx/xxx.m4a\"\n}\n</code></pre>"
   },
-  "VoiceFilter": {
+  "CreateApp": {
     "params": [
       {
-        "name": "BizId",
-        "desc": "应用ID，登录[控制台](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID"
+        "name": "AppName",
+        "desc": "应用名称"
       },
       {
-        "name": "FileId",
-        "desc": "文件ID，表示文件唯一ID"
+        "name": "ProjectId",
+        "desc": "腾讯云项目id，默认为0，表示默认项目"
       },
       {
-        "name": "FileName",
-        "desc": "文件名"
+        "name": "EngineList",
+        "desc": "需要支持的引擎列表，取值android, ios, uinty, cocos, unreal, windows。默认全选。"
       },
       {
-        "name": "FileUrl",
-        "desc": "文件url，urlencode编码，FileUrl和FileContent二选一"
+        "name": "RegionList",
+        "desc": "服务区域列表, 默认为空数组. 取值: mainland(美), sa(南美), eu(欧洲), oc(澳洲), me(中东)。默认全选"
       },
       {
-        "name": "FileContent",
-        "desc": "文件内容，base64编码，FileUrl和FileContent二选一"
+        "name": "RealtimeSpeechConf",
+        "desc": "实时语音服务配置数据"
       },
       {
-        "name": "OpenId",
-        "desc": "用户ID"
+        "name": "VoiceMessageConf",
+        "desc": "离线语音服务配置数据"
+      },
+      {
+        "name": "VoiceFilterConf",
+        "desc": "语音过滤服务配置数据"
+      },
+      {
+        "name": "Tags",
+        "desc": "需要添加的标签列表"
       }
     ],
-    "desc": "本接口用于识别涉黄、涉政等违规音频，成功会回调配置在应用的回调地址。回调示例如下：\n{\"BizId\":0,\"FileId\":\"test_file_id\",\"FileName\":\"test_file_name\",\"FileUrl\":\"test_file_url\",\"OpenId\":\"test_open_id\",\"TimeStamp\":\"0000-00-00 00:00:00\",\"Data\":[{\"Type\":1,\"Word\":\"xx\"}]}\nType表示过滤类型，1：政治，2：色情，3：谩骂"
+    "desc": "本接口(CreateApp)用于创建一个GME应用"
+  },
+  "ModifyAppStatus": {
+    "params": [
+      {
+        "name": "BizId",
+        "desc": "应用id，创建应用后由后台生成并返回。"
+      },
+      {
+        "name": "Status",
+        "desc": "应用状态，取值：open/close"
+      }
+    ],
+    "desc": "本接口(ModifyAppStatus)用于修改应用总开关状态。"
   }
 }
```

#### html2text {}

```diff
@@ -1,40 +1,71 @@
 # -*- coding: utf-8 -*- DESC = "gme-2018-07-11" INFO =
 { "DescribeFilterResult": { "params": [ { "name": "BizId", "desc": "åºç¨ID"
 }, { "name": "FileId", "desc": "æä»¶ID" } ], "desc":
-"æ ¹æ®åºç¨IDåæä»¶IDæ¥è¯¢è¯å«ç»æ" }, "DescribeScanResultList":
-{ "params": [ { "name": "BizId", "desc": "åºç¨
-IDï¼å¨æ§å¶å°ç»ä¸åå»ºã" }, { "name": "TaskIdList", "desc":
+"æ ¹æ®åºç¨IDåæä»¶IDæ¥è¯¢è¯å«ç»æ" }, "DescribeAppStatistics":
+{ "params": [ { "name": "BizId", "desc": "GMEåºç¨id" }, { "name":
+"StartDate", "desc": "æ°æ®å¼å§æ¶é´ï¼ä¸å«åºæ¶é´ï¼æ ¼å¼: å¹´-æ-
+æ¥ï¼å¦: 2018-07-13" }, { "name": "EndDate", "desc":
+"æ°æ®ç»ææ¶é´ï¼ä¸å«åºæ¶é´ï¼æ ¼å¼: å¹´-æ-æ¥ï¼å¦: 2018-07-13"
+}, { "name": "Services", "desc":
+"è¦æ¥è¯¢çæå¡åè¡¨ï¼åå¼ï¼RealTimeSpeech/VoiceMessage/VoiceFilter" }
+], "desc": "æ¬æ¥å£
+(DescribeAppStatistics)ç¨æ·è·åæä¸ªGMEåºç¨çç¨éæ°æ®ãåæ¬å®æ¶è¯­é³ï¼ç¦»çº¿è¯­é³ï¼è¯­é³è¿æ»¤ç­ãæé¿æ¥è¯¢å¨æä¸ºæè¿30å¤©ã"
+}, "DescribeScanResultList": { "params": [ { "name": "BizId", "desc": "åºç¨
+IDï¼ç»å½[æ§å¶å°](https://console.cloud.tencent.com/
+gamegme)åå»ºåºç¨å¾å°çAppID" }, { "name": "TaskIdList", "desc":
 "æ¥è¯¢çä»»å¡ ID åè¡¨ï¼ä»»å¡ ID åè¡¨æå¤æ¯æ 100 ä¸ªã" } ],
 "desc": "æ¬æ¥å£
 (DescribeScanResultList)ç¨äºæ¥è¯¢è¯­é³æ£æµç»æï¼æ¥è¯¢ä»»å¡åè¡¨æå¤æ¯æ100ä¸ªã\n
 å¦æå¨æäº¤è¯­é³æ£æµä»»å¡æ¶æªè®¾ç½® Callback
 å­æ®µï¼åéè¦éè¿æ¬æ¥å£è·åæ£æµç»æ
-" }, "DescribeFilterResultList": { "params": [ { "name": "BizId", "desc":
-"åºç¨ID" }, { "name": "StartDate", "desc": "å¼å§æ¶é´ï¼æ ¼å¼ä¸º å¹´-æ-
-æ¥ï¼å¦: 2018-07-11" }, { "name": "EndDate", "desc":
-"ç»ææ¶é´ï¼æ ¼å¼ä¸º å¹´-æ-æ¥ï¼å¦: 2018-07-11" }, { "name": "Offset",
-"desc": "åç§»éï¼é»è®¤å¼ä¸º0ã" }, { "name": "Limit", "desc":
+" }, "VoiceFilter": { "params": [ { "name": "BizId", "desc": "åºç¨IDï¼ç»å½
+[æ§å¶å°](https://console.cloud.tencent.com/
+gamegme)åå»ºåºç¨å¾å°çAppID" }, { "name": "FileId", "desc":
+"æä»¶IDï¼è¡¨ç¤ºæä»¶å¯ä¸ID" }, { "name": "FileName", "desc": "æä»¶å"
+}, { "name": "FileUrl", "desc":
+"æä»¶urlï¼urlencodeç¼ç ï¼FileUrlåFileContentäºéä¸" }, { "name":
+"FileContent", "desc":
+"æä»¶åå®¹ï¼base64ç¼ç ï¼FileUrlåFileContentäºéä¸" }, { "name":
+"OpenId", "desc": "ç¨æ·ID" } ], "desc":
+"æ¬æ¥å£ç¨äºè¯å«æ¶é»ãæ¶æ¿ç­è¿è§é³é¢ï¼æåä¼åè°éç½®å¨åºç¨çåè°å°åãåè°ç¤ºä¾å¦ä¸ï¼\n
+{\"BizId\":0,\"FileId\":\"test_file_id\",\"FileName\":
+\"test_file_name\",\"FileUrl\":\"test_file_url\",\"OpenId\":
+\"test_open_id\",\"TimeStamp\":\"0000-00-00 00:00:00\",\"Data\":[{\"Type\":
+1,\"Word\":
+\"xx\"}]}\nTypeè¡¨ç¤ºè¿æ»¤ç±»åï¼1ï¼æ¿æ²»ï¼2ï¼è²æï¼3ï¼è°©éª" },
+"DescribeFilterResultList": { "params": [ { "name": "BizId", "desc": "åºç¨ID"
+}, { "name": "StartDate", "desc": "å¼å§æ¶é´ï¼æ ¼å¼ä¸º å¹´-æ-æ¥ï¼å¦:
+2018-07-11" }, { "name": "EndDate", "desc": "ç»ææ¶é´ï¼æ ¼å¼ä¸º å¹´-æ-
+æ¥ï¼å¦: 2018-07-11" }, { "name": "Offset", "desc":
+"åç§»éï¼é»è®¤å¼ä¸º0ã" }, { "name": "Limit", "desc":
 "è¿åæ°éï¼é»è®¤å¼ä¸º10ï¼æå¤§å¼ä¸º100ã" } ], "desc":
 "æ ¹æ®æ¥ææ¥è¯¢è¯å«ç»æåè¡¨" }, "ScanVoice": { "params": [ { "name":
-"BizId", "desc": "åºç¨IDï¼ç»å½æ§å¶å°åå»ºåºç¨å¾å°çAppIDã" },
-{ "name": "Scenes", "desc": "è¯­é³æ£æµåºæ¯ï¼åæ°å¼ç®åè¦æ±ä¸º
-defaultã é¢çåºæ¯è®¾ç½®ï¼
+"BizId", "desc": "åºç¨IDï¼ç»å½[æ§å¶å° - æå¡ç®¡ç](https://
+console.cloud.tencent.com/gamegme)åå»ºåºç¨å¾å°çAppID" }, { "name":
+"Scenes", "desc": "è¯­é³æ£æµåºæ¯ï¼åæ°å¼ç®åè¦æ±ä¸º defaultã
+é¢çåºæ¯è®¾ç½®ï¼
 è°©éªãè²æãæ¶æ¿ãå¹¿åãæ´æãè¿ç¦ç­åºæ¯ï¼å·ä½åå¼è§ä¸è¿°
 Label_è¯´æã" }, { "name": "Live", "desc": "æ¯å¦ä¸ºç´æ­æµãå¼ä¸º
 false æ¶è¡¨ç¤ºæ®éè¯­é³æä»¶æ£æµï¼ä¸º true æ¶è¡¨ç¤ºè¯­é³æµæ£æµã"
 }, { "name": "Tasks", "desc":
 "è¯­é³æ£æµä»»å¡åè¡¨ï¼åè¡¨æå¤æ¯æ100ä¸ªæ£æµä»»å¡ãç»æä½ä¸­åå«ï¼\n
 DataIdï¼æ°æ®çå¯ä¸ID
 \n
 Urlï¼æ°æ®æä»¶çurlï¼ä¸º urlencode ç¼ç ï¼æµå¼åä¸ºææµå°å
 " }, { "name": "Callback", "desc":
 "å¼æ­¥æ£æµç»æåè°å°åï¼å·ä½è§ä¸è¿°åè°ç¸å³è¯´æãï¼è¯´æï¼è¯¥å­æ®µä¸ºç©ºæ¶ï¼å¿é¡»éè¿æ¥å£
 (æ¥è¯¢è¯­é³æ£æµç»æ)è·åæ£æµç»æï¼ã" } ], "desc": "æ¬æ¥å£
-(ScanVoice)ç¨äºæäº¤è¯­é³æ£æµä»»å¡ï¼æ£æµä»»å¡åè¡¨æå¤æ¯æ100ä¸ªã\n\n
+(ScanVoice)ç¨äºæäº¤è¯­é³æ£æµä»»å¡ï¼æ£æµä»»å¡åè¡¨æå¤æ¯æ100ä¸ªãä½¿ç¨åè¯·æ¨ç»å½
+[æ§å¶å° - æå¡éç½®](https://console.cloud.tencent.com/gamegme/
+conf)å¼å¯è¯­é³åææå¡ã\n\n\n
+*** åè½è¯ç¨è¯´æï¼ ***
+\n
+æå¼åå¾æ§å¶å°_-_äº§åè¯ç¨åè´¹è¯ç¨è¯­é³åææå¡ã
+\n\n\n
 *** æ¥å£åè½è¯´æï¼ ***
 \n
 æ¯æå¯¹è¯­é³æµæè¯­é³æä»¶è¿è¡æ£æµï¼å¤æ­å¶ä¸­æ¯å¦åå«è¿è§åå®¹ã
 \n
 æ¯æè®¾ç½®åè°å°å Callback è·åæ£æµç»æï¼åæ¶æ¯æéè¿æ¥å£
 (æ¥è¯¢è¯­é³æ£æµç»æ)ä¸»å¨è½®è¯¢è·åæ£æµç»æã
 \n
@@ -78,15 +109,15 @@
 è¯­é³�è¯­é³æ£æµç\n
                                          ad :å¹¿å
                                          \n
                                          terrorism:æ´æ
                                          \n
                                          contraband :è¿ç¦
                                          \n
-                                         customized:èªå®ä¹è¯åº
+                                         customized:èªå®ä¹è¯åºãç®åç½ååå¼æ¾ï¼å¦æéè¦è¯·èç³»æä»¬ã
                                          \n
 \n\n
 *** åè°ç¸å³è¯´æï¼ ***
 \n
 å¦æå¨è¯·æ±åæ°ä¸­æå®äºåè°å°ååæ° Callbackï¼å³ä¸ä¸ª HTTP
 (S) åè®®æ¥å£ç URLï¼åéè¦æ¯æ POST
 æ¹æ³ï¼ä¼ è¾æ°æ®ç¼ç éç¨ UTF-8ã
@@ -108,46 +139,42 @@
           o ç­¾ååæä¸²ä¸º POST+body çæ´ä¸ªjsonåå®¹(é¿åº¦ä»¥ Content-
             Length ä¸ºå);
           o \n\t\t
           o ç­¾åkeyä¸ºåºç¨ç secrectkeyï¼å¯ä»¥éè¿æ§å¶å°æ¥çã
           o \n\t
     * \n
 \n\n
-    * \n
-    * \nåè°è¯·æ± Body çå­æ®µè¯´æè§ç»æï¼\nDescribeScanResult\n
-    * \n
-\n\n
-åè°ç¤ºä¾å¦ä¸ï¼è¯¦ç»å­æ®µè¯´æè§ä¸è¿°è¡¨æ ¼ä¸­ Data
-å­æ®µè¯´æï¼ï¼
+åè°ç¤ºä¾å¦ä¸ï¼è¯¦ç»å­æ®µè¯´æè§ç»æï¼\nDescribeScanResultï¼ï¼
 \n
 {\n\t\"Code\": 0,\n\t\"DataId\":
 \"1400000000_test_data_id\",\n\t\"ScanFinishTime\": 1566720906,\n\t\"HitFlag\":
 true,\n\t\"Live\": false,\n\t\"Msg\": \"\",\n\t\"ScanPiece\": [
 {\n\t\t\"DumpUrl\": \"\",\n\t\t\"HitFlag\": true,\n\t\t\"MainType\":
-\"abuse\",\n\t\t\"RoomId\": \"123\",\n\t\t\"OpenId\":
-\"xxx\",\n\t\t\"ScanDetail\": [{\n\t\t\t\"EndTime\": 1110,\n\t\t\t\"KeyWord\":
+\"abuse\",\n\t\t\"RoomId\": \"123\",\n\t\t\"OpenId\": \"xxx\",\n\t\t\"Info\":
+\"\",\n\t\t\"ScanDetail\": [{\n\t\t\t\"EndTime\": 1110,\n\t\t\t\"KeyWord\":
 \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\":
 \"90.00\",\n\t\t\t\"StartTime\": 1110\n\t\t}, {\n\t\t\t\"EndTime\":
 1380,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\":
 \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 930\n\t\t},
 {\n\t\t\t\"EndTime\": 1560,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\":
 \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 930\n\t\t},
 {\n\t\t\t\"EndTime\": 2820,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\":
 \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\":
 2490\n\t\t}]\n\t}],\n\t\"ScanStartTime\": 1566720905,\n\t\"Scenes\":
 [\n\t\t\"default\"\n\t],\n\t\"Status\": \"Success\",\n\t\"TaskId\":
 \"xxx\",\n\t\"Url\": \"https://xxx/xxx.m4a\"\n}\n
-" }, "VoiceFilter": { "params": [ { "name": "BizId", "desc": "åºç¨IDï¼ç»å½
-[æ§å¶å°](https://console.cloud.tencent.com/
-gamegme)åå»ºåºç¨å¾å°çAppID" }, { "name": "FileId", "desc":
-"æä»¶IDï¼è¡¨ç¤ºæä»¶å¯ä¸ID" }, { "name": "FileName", "desc": "æä»¶å"
-}, { "name": "FileUrl", "desc":
-"æä»¶urlï¼urlencodeç¼ç ï¼FileUrlåFileContentäºéä¸" }, { "name":
-"FileContent", "desc":
-"æä»¶åå®¹ï¼base64ç¼ç ï¼FileUrlåFileContentäºéä¸" }, { "name":
-"OpenId", "desc": "ç¨æ·ID" } ], "desc":
-"æ¬æ¥å£ç¨äºè¯å«æ¶é»ãæ¶æ¿ç­è¿è§é³é¢ï¼æåä¼åè°éç½®å¨åºç¨çåè°å°åãåè°ç¤ºä¾å¦ä¸ï¼\n
-{\"BizId\":0,\"FileId\":\"test_file_id\",\"FileName\":
-\"test_file_name\",\"FileUrl\":\"test_file_url\",\"OpenId\":
-\"test_open_id\",\"TimeStamp\":\"0000-00-00 00:00:00\",\"Data\":[{\"Type\":
-1,\"Word\":
-\"xx\"}]}\nTypeè¡¨ç¤ºè¿æ»¤ç±»åï¼1ï¼æ¿æ²»ï¼2ï¼è²æï¼3ï¼è°©éª" } }
+" }, "CreateApp": { "params": [ { "name": "AppName", "desc": "åºç¨åç§°" },
+{ "name": "ProjectId", "desc":
+"è¾è®¯äºé¡¹ç®idï¼é»è®¤ä¸º0ï¼è¡¨ç¤ºé»è®¤é¡¹ç®" }, { "name":
+"EngineList", "desc": "éè¦æ¯æçå¼æåè¡¨ï¼åå¼android, ios, uinty,
+cocos, unreal, windowsãé»è®¤å¨éã" }, { "name": "RegionList", "desc":
+"æå¡åºååè¡¨, é»è®¤ä¸ºç©ºæ°ç». åå¼: mainland(ç¾), sa(åç¾), eu
+(æ¬§æ´²), oc(æ¾³æ´²), me(ä¸­ä¸)ãé»è®¤å¨é" }, { "name":
+"RealtimeSpeechConf", "desc": "å®æ¶è¯­é³æå¡éç½®æ°æ®" }, { "name":
+"VoiceMessageConf", "desc": "ç¦»çº¿è¯­é³æå¡éç½®æ°æ®" }, { "name":
+"VoiceFilterConf", "desc": "è¯­é³è¿æ»¤æå¡éç½®æ°æ®" }, { "name":
+"Tags", "desc": "éè¦æ·»å çæ ç­¾åè¡¨" } ], "desc": "æ¬æ¥å£
+(CreateApp)ç¨äºåå»ºä¸ä¸ªGMEåºç¨" }, "ModifyAppStatus": { "params": [
+{ "name": "BizId", "desc":
+"åºç¨idï¼åå»ºåºç¨åç±åå°çæå¹¶è¿åã" }, { "name": "Status",
+"desc": "åºç¨ç¶æï¼åå¼ï¼open/close" } ], "desc": "æ¬æ¥å£
+(ModifyAppStatus)ç¨äºä¿®æ¹åºç¨æ»å¼å³ç¶æã" } }
```

### Comparing `tccli-3.0.98.1/tccli/services/gme/gme_client.py` & `tccli-3.0.99.1/tccli/services/sms/sms_client.py`

 * *Files 12% similar despite different names*

```diff
@@ -8,230 +8,232 @@
 import tccli.help_template as HelpTemplate
 from tccli import __version__
 from tccli.utils import Utils
 from tccli.configure import Configure
 from tencentcloud.common import credential
 from tencentcloud.common.profile.http_profile import HttpProfile
 from tencentcloud.common.profile.client_profile import ClientProfile
-from tencentcloud.gme.v20180711 import gme_client as gme_client_v20180711
-from tencentcloud.gme.v20180711 import models as models_v20180711
-from tccli.services.gme import v20180711
-from tccli.services.gme.v20180711 import help as v20180711_help
+from tencentcloud.sms.v20190711 import sms_client as sms_client_v20190711
+from tencentcloud.sms.v20190711 import models as models_v20190711
+from tccli.services.sms import v20190711
+from tccli.services.sms.v20190711 import help as v20190711_help
 
 
-def doDescribeFilterResult(argv, arglist):
+def doPullSmsReplyStatus(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
-        show_help("DescribeFilterResult", g_param[OptionsDefine.Version])
+        show_help("PullSmsReplyStatus", g_param[OptionsDefine.Version])
         return
 
     param = {
-        "BizId": Utils.try_to_json(argv, "--BizId"),
-        "FileId": argv.get("--FileId"),
+        "Limit": Utils.try_to_json(argv, "--Limit"),
+        "SmsSdkAppid": argv.get("--SmsSdkAppid"),
 
     }
     cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
     http_profile = HttpProfile(
         reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
         reqMethod="POST",
         endpoint=g_param[OptionsDefine.Endpoint]
     )
     profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
     mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
-    client = mod.GmeClient(cred, g_param[OptionsDefine.Region], profile)
+    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
     client._sdkVersion += ("_CLI_" + __version__)
     models = MODELS_MAP[g_param[OptionsDefine.Version]]
-    model = models.DescribeFilterResultRequest()
+    model = models.PullSmsReplyStatusRequest()
     model.from_json_string(json.dumps(param))
-    rsp = client.DescribeFilterResult(model)
+    rsp = client.PullSmsReplyStatus(model)
     result = rsp.to_json_string()
     jsonobj = None
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
-def doVoiceFilter(argv, arglist):
+def doPullSmsSendStatus(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
-        show_help("VoiceFilter", g_param[OptionsDefine.Version])
+        show_help("PullSmsSendStatus", g_param[OptionsDefine.Version])
         return
 
     param = {
-        "BizId": Utils.try_to_json(argv, "--BizId"),
-        "FileId": argv.get("--FileId"),
-        "FileName": argv.get("--FileName"),
-        "FileUrl": argv.get("--FileUrl"),
-        "FileContent": argv.get("--FileContent"),
-        "OpenId": argv.get("--OpenId"),
+        "Limit": Utils.try_to_json(argv, "--Limit"),
+        "SmsSdkAppid": argv.get("--SmsSdkAppid"),
 
     }
     cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
     http_profile = HttpProfile(
         reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
         reqMethod="POST",
         endpoint=g_param[OptionsDefine.Endpoint]
     )
     profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
     mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
-    client = mod.GmeClient(cred, g_param[OptionsDefine.Region], profile)
+    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
     client._sdkVersion += ("_CLI_" + __version__)
     models = MODELS_MAP[g_param[OptionsDefine.Version]]
-    model = models.VoiceFilterRequest()
+    model = models.PullSmsSendStatusRequest()
     model.from_json_string(json.dumps(param))
-    rsp = client.VoiceFilter(model)
+    rsp = client.PullSmsSendStatus(model)
     result = rsp.to_json_string()
     jsonobj = None
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
-def doDescribeFilterResultList(argv, arglist):
+def doSendSms(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
-        show_help("DescribeFilterResultList", g_param[OptionsDefine.Version])
+        show_help("SendSms", g_param[OptionsDefine.Version])
         return
 
     param = {
-        "BizId": Utils.try_to_json(argv, "--BizId"),
-        "StartDate": argv.get("--StartDate"),
-        "EndDate": argv.get("--EndDate"),
-        "Offset": Utils.try_to_json(argv, "--Offset"),
-        "Limit": Utils.try_to_json(argv, "--Limit"),
+        "PhoneNumberSet": Utils.try_to_json(argv, "--PhoneNumberSet"),
+        "TemplateID": argv.get("--TemplateID"),
+        "SmsSdkAppid": argv.get("--SmsSdkAppid"),
+        "Sign": argv.get("--Sign"),
+        "TemplateParamSet": Utils.try_to_json(argv, "--TemplateParamSet"),
+        "ExtendCode": Utils.try_to_json(argv, "--ExtendCode"),
+        "SessionContext": argv.get("--SessionContext"),
+        "SenderId": argv.get("--SenderId"),
 
     }
     cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
     http_profile = HttpProfile(
         reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
         reqMethod="POST",
         endpoint=g_param[OptionsDefine.Endpoint]
     )
     profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
     mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
-    client = mod.GmeClient(cred, g_param[OptionsDefine.Region], profile)
+    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
     client._sdkVersion += ("_CLI_" + __version__)
     models = MODELS_MAP[g_param[OptionsDefine.Version]]
-    model = models.DescribeFilterResultListRequest()
+    model = models.SendSmsRequest()
     model.from_json_string(json.dumps(param))
-    rsp = client.DescribeFilterResultList(model)
+    rsp = client.SendSms(model)
     result = rsp.to_json_string()
     jsonobj = None
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
-def doScanVoice(argv, arglist):
+def doPullSmsSendStatusByPhoneNumber(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
-        show_help("ScanVoice", g_param[OptionsDefine.Version])
+        show_help("PullSmsSendStatusByPhoneNumber", g_param[OptionsDefine.Version])
         return
 
     param = {
-        "BizId": Utils.try_to_json(argv, "--BizId"),
-        "Scenes": Utils.try_to_json(argv, "--Scenes"),
-        "Live": Utils.try_to_json(argv, "--Live"),
-        "Tasks": Utils.try_to_json(argv, "--Tasks"),
-        "Callback": argv.get("--Callback"),
+        "SendDateTime": argv.get("--SendDateTime"),
+        "Offset": Utils.try_to_json(argv, "--Offset"),
+        "Limit": Utils.try_to_json(argv, "--Limit"),
+        "PhoneNumber": argv.get("--PhoneNumber"),
+        "SmsSdkAppid": argv.get("--SmsSdkAppid"),
 
     }
     cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
     http_profile = HttpProfile(
         reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
         reqMethod="POST",
         endpoint=g_param[OptionsDefine.Endpoint]
     )
     profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
     mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
-    client = mod.GmeClient(cred, g_param[OptionsDefine.Region], profile)
+    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
     client._sdkVersion += ("_CLI_" + __version__)
     models = MODELS_MAP[g_param[OptionsDefine.Version]]
-    model = models.ScanVoiceRequest()
+    model = models.PullSmsSendStatusByPhoneNumberRequest()
     model.from_json_string(json.dumps(param))
-    rsp = client.ScanVoice(model)
+    rsp = client.PullSmsSendStatusByPhoneNumber(model)
     result = rsp.to_json_string()
     jsonobj = None
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
-def doDescribeScanResultList(argv, arglist):
+def doPullSmsReplyStatusByPhoneNumber(argv, arglist):
     g_param = parse_global_arg(argv)
     if "help" in argv:
-        show_help("DescribeScanResultList", g_param[OptionsDefine.Version])
+        show_help("PullSmsReplyStatusByPhoneNumber", g_param[OptionsDefine.Version])
         return
 
     param = {
-        "BizId": Utils.try_to_json(argv, "--BizId"),
-        "TaskIdList": Utils.try_to_json(argv, "--TaskIdList"),
+        "SendDateTime": argv.get("--SendDateTime"),
+        "Offset": Utils.try_to_json(argv, "--Offset"),
+        "Limit": Utils.try_to_json(argv, "--Limit"),
+        "PhoneNumber": argv.get("--PhoneNumber"),
+        "SmsSdkAppid": argv.get("--SmsSdkAppid"),
 
     }
     cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
     http_profile = HttpProfile(
         reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
         reqMethod="POST",
         endpoint=g_param[OptionsDefine.Endpoint]
     )
     profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
     mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
-    client = mod.GmeClient(cred, g_param[OptionsDefine.Region], profile)
+    client = mod.SmsClient(cred, g_param[OptionsDefine.Region], profile)
     client._sdkVersion += ("_CLI_" + __version__)
     models = MODELS_MAP[g_param[OptionsDefine.Version]]
-    model = models.DescribeScanResultListRequest()
+    model = models.PullSmsReplyStatusByPhoneNumberRequest()
     model.from_json_string(json.dumps(param))
-    rsp = client.DescribeScanResultList(model)
+    rsp = client.PullSmsReplyStatusByPhoneNumber(model)
     result = rsp.to_json_string()
     jsonobj = None
     try:
         jsonobj = json.loads(result)
     except TypeError as e:
         jsonobj = json.loads(result.decode('utf-8')) # python3.3
     FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])
 
 
 CLIENT_MAP = {
-    "v20180711": gme_client_v20180711,
+    "v20190711": sms_client_v20190711,
 
 }
 
 MODELS_MAP = {
-    "v20180711": models_v20180711,
+    "v20190711": models_v20190711,
 
 }
 
 ACTION_MAP = {
-    "DescribeFilterResult": doDescribeFilterResult,
-    "VoiceFilter": doVoiceFilter,
-    "DescribeFilterResultList": doDescribeFilterResultList,
-    "ScanVoice": doScanVoice,
-    "DescribeScanResultList": doDescribeScanResultList,
+    "PullSmsReplyStatus": doPullSmsReplyStatus,
+    "PullSmsSendStatus": doPullSmsSendStatus,
+    "SendSms": doSendSms,
+    "PullSmsSendStatusByPhoneNumber": doPullSmsSendStatusByPhoneNumber,
+    "PullSmsReplyStatusByPhoneNumber": doPullSmsReplyStatusByPhoneNumber,
 
 }
 
 AVAILABLE_VERSION_LIST = [
-    v20180711.version,
+    v20190711.version,
 
 ]
 AVAILABLE_VERSIONS = {
-     'v' + v20180711.version.replace('-', ''): {"help": v20180711_help.INFO,"desc": v20180711_help.DESC},
+     'v' + v20190711.version.replace('-', ''): {"help": v20190711_help.INFO,"desc": v20190711_help.DESC},
 
 }
 
 
-def gme_action(argv, arglist):
+def sms_action(argv, arglist):
     if "help" in argv:
         versions = sorted(AVAILABLE_VERSIONS.keys())
         opt_v = "--" + OptionsDefine.Version
         version = versions[-1]
         if opt_v in argv:
             version = 'v' + argv[opt_v].replace('-', '')
         if version not in versions:
@@ -239,15 +241,15 @@
             return
         action_str = ""
         docs = AVAILABLE_VERSIONS[version]["help"]
         desc = AVAILABLE_VERSIONS[version]["desc"]
         for action, info in docs.items():
             action_str += "        %s\n" % action
             action_str += Utils.split_str("        ", info["desc"], 120)
-        helpstr = HelpTemplate.SERVICE % {"name": "gme", "desc": desc, "actions": action_str}
+        helpstr = HelpTemplate.SERVICE % {"name": "sms", "desc": desc, "actions": action_str}
         print(helpstr)
     else:
         print(ErrorMsg.FEW_ARG)
 
 
 def version_merge():
     help_merge = {}
@@ -260,15 +262,15 @@
             for param in AVAILABLE_VERSIONS[v]["help"][action]["params"]:
                 if param["name"] not in help_merge[action]["params"]:
                     help_merge[action]["params"].append(param["name"])
     return help_merge
 
 
 def register_arg(command):
-    cmd = NiceCommand("gme", gme_action)
+    cmd = NiceCommand("sms", sms_action)
     command.reg_cmd(cmd)
     cmd.reg_opt("help", "bool")
     cmd.reg_opt(OptionsDefine.Version, "string")
     help_merge = version_merge()
 
     for actionName, action in help_merge.items():
         c = NiceCommand(actionName, action["cb"])
@@ -319,19 +321,19 @@
             else:
                 if param in config:
                     params[param] = config[param]
                 elif param == OptionsDefine.Region:
                     raise Exception("%s is invalid" % OptionsDefine.Region)
     try:
         if params[OptionsDefine.Version] is None:
-            version = config["gme"][OptionsDefine.Version]
+            version = config["sms"][OptionsDefine.Version]
             params[OptionsDefine.Version] = "v" + version.replace('-', '')
 
         if params[OptionsDefine.Endpoint] is None:
-            params[OptionsDefine.Endpoint] = config["gme"][OptionsDefine.Endpoint]
+            params[OptionsDefine.Endpoint] = config["sms"][OptionsDefine.Endpoint]
     except Exception as err:
         raise Exception("config file:%s error, %s" % (conf_path, str(err)))
     versions = sorted(AVAILABLE_VERSIONS.keys())
     if params[OptionsDefine.Version] not in versions:
         raise Exception("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))
     return params
 
@@ -340,24 +342,24 @@
     docs = AVAILABLE_VERSIONS[version]["help"][action]
     desc = AVAILABLE_VERSIONS[version]["desc"]
     docstr = ""
     for param in docs["params"]:
         docstr += "        %s\n" % ("--" + param["name"])
         docstr += Utils.split_str("        ", param["desc"], 120)
 
-    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "gme", "desc": desc, "params": docstr}
+    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "sms", "desc": desc, "params": docstr}
     print(helpmsg)
 
 
 def get_actions_info():
     config = Configure()
     new_version = max(AVAILABLE_VERSIONS.keys())
     version = new_version
     try:
         profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
-        version = profile["gme"]["version"]
+        version = profile["sms"]["version"]
         version = "v" + version.replace('-', '')
     except Exception:
         pass
     if version not in AVAILABLE_VERSIONS.keys():
         version = new_version
     return AVAILABLE_VERSIONS[version]["help"]
```

### Comparing `tccli-3.0.98.1/tccli/services/nlp/v20190408/help.py` & `tccli-3.0.99.1/tccli/services/nlp/v20190408/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/nlp/nlp_client.py` & `tccli-3.0.99.1/tccli/services/nlp/nlp_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/iotcloud/iotcloud_client.py` & `tccli-3.0.99.1/tccli/services/iotcloud/iotcloud_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/iotcloud/v20180614/help.py` & `tccli-3.0.99.1/tccli/services/iotcloud/v20180614/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/iot/iot_client.py` & `tccli-3.0.99.1/tccli/services/iot/iot_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/iot/v20180123/help.py` & `tccli-3.0.99.1/tccli/services/iot/v20180123/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tkgdq/tkgdq_client.py` & `tccli-3.0.99.1/tccli/services/tkgdq/tkgdq_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tkgdq/v20190411/help.py` & `tccli-3.0.99.1/tccli/services/tkgdq/v20190411/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tmt/v20180321/help.py` & `tccli-3.0.99.1/tccli/services/tmt/v20180321/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tmt/tmt_client.py` & `tccli-3.0.99.1/tccli/services/tmt/tmt_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cms/v20190321/help.py` & `tccli-3.0.99.1/tccli/services/cms/v20190321/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cms/cms_client.py` & `tccli-3.0.99.1/tccli/services/cms/cms_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tcb/v20180608/help.py` & `tccli-3.0.99.1/tccli/services/tcb/v20180608/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tcb/tcb_client.py` & `tccli-3.0.99.1/tccli/services/tcb/tcb_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tke/tke_client.py` & `tccli-3.0.99.1/tccli/services/tke/tke_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tke/v20180525/help.py` & `tccli-3.0.99.1/tccli/services/tke/v20180525/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/emr/v20190103/help.py` & `tccli-3.0.99.1/tccli/services/emr/v20190103/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/emr/emr_client.py` & `tccli-3.0.99.1/tccli/services/emr/emr_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tag/v20180813/help.py` & `tccli-3.0.99.1/tccli/services/tag/v20180813/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tag/tag_client.py` & `tccli-3.0.99.1/tccli/services/tag/tag_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/es/es_client.py` & `tccli-3.0.99.1/tccli/services/es/es_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/es/v20180416/help.py` & `tccli-3.0.99.1/tccli/services/es/v20180416/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cfs/v20190719/help.py` & `tccli-3.0.99.1/tccli/services/cfs/v20190719/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/cfs/cfs_client.py` & `tccli-3.0.99.1/tccli/services/cfs/cfs_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tsf/tsf_client.py` & `tccli-3.0.99.1/tccli/services/tsf/tsf_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/tsf/v20180326/help.py` & `tccli-3.0.99.1/tccli/services/tsf/v20180326/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/monitor/monitor_client.py` & `tccli-3.0.99.1/tccli/services/monitor/monitor_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/monitor/v20180724/help.py` & `tccli-3.0.99.1/tccli/services/monitor/v20180724/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/iottid/v20190411/help.py` & `tccli-3.0.99.1/tccli/services/iottid/v20190411/help.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/services/iottid/iottid_client.py` & `tccli-3.0.99.1/tccli/services/iottid/iottid_client.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/completer.py` & `tccli-3.0.99.1/tccli/completer.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/table.py` & `tccli-3.0.99.1/tccli/table.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/nice_command.py` & `tccli-3.0.99.1/tccli/nice_command.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/six.py` & `tccli-3.0.99.1/tccli/six.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/main.py` & `tccli-3.0.99.1/tccli/main.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/advance/userConfigHandler.py` & `tccli-3.0.99.1/tccli/advance/userConfigHandler.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli/advance/userProfileHandler.py` & `tccli-3.0.99.1/tccli/advance/userProfileHandler.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/setup.py` & `tccli-3.0.99.1/setup.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/PKG-INFO` & `tccli-3.0.99.1/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: tccli
-Version: 3.0.98.1
+Version: 3.0.99.1
 Summary: Universal Command Line Environment for Tencent Cloud
 Home-page: https://github.com/TencentCloud/tencentcloud-cli.git
 Author: Tencent Cloud
 Maintainer-email: TencentCloudApi@tencent.com
 License: UNKNOWN
 Description: UNKNOWN
 Platform: unix
```

### Comparing `tccli-3.0.98.1/jmespath/functions.py` & `tccli-3.0.99.1/jmespath/functions.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/jmespath/ast.py` & `tccli-3.0.99.1/jmespath/ast.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/jmespath/exceptions.py` & `tccli-3.0.99.1/jmespath/exceptions.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/jmespath/compat.py` & `tccli-3.0.99.1/jmespath/compat.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/jmespath/parser.py` & `tccli-3.0.99.1/jmespath/parser.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/jmespath/visitor.py` & `tccli-3.0.99.1/jmespath/visitor.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/jmespath/lexer.py` & `tccli-3.0.99.1/jmespath/lexer.py`

 * *Files identical despite different names*

### Comparing `tccli-3.0.98.1/tccli.egg-info/PKG-INFO` & `tccli-3.0.99.1/tccli.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: tccli
-Version: 3.0.98.1
+Version: 3.0.99.1
 Summary: Universal Command Line Environment for Tencent Cloud
 Home-page: https://github.com/TencentCloud/tencentcloud-cli.git
 Author: Tencent Cloud
 Maintainer-email: TencentCloudApi@tencent.com
 License: UNKNOWN
 Description: UNKNOWN
 Platform: unix
```

### Comparing `tccli-3.0.98.1/tccli.egg-info/SOURCES.txt` & `tccli-3.0.99.1/tccli.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -240,14 +240,16 @@
 tccli/services/mariadb/mariadb_client.py
 tccli/services/mariadb/v20170312/__init__.py
 tccli/services/mariadb/v20170312/help.py
 tccli/services/mongodb/__init__.py
 tccli/services/mongodb/mongodb_client.py
 tccli/services/mongodb/v20180408/__init__.py
 tccli/services/mongodb/v20180408/help.py
+tccli/services/mongodb/v20190725/__init__.py
+tccli/services/mongodb/v20190725/help.py
 tccli/services/monitor/__init__.py
 tccli/services/monitor/monitor_client.py
 tccli/services/monitor/v20180724/__init__.py
 tccli/services/monitor/v20180724/help.py
 tccli/services/mps/__init__.py
 tccli/services/mps/mps_client.py
 tccli/services/mps/v20190612/__init__.py
@@ -264,14 +266,18 @@
 tccli/services/nlp/nlp_client.py
 tccli/services/nlp/v20190408/__init__.py
 tccli/services/nlp/v20190408/help.py
 tccli/services/ocr/__init__.py
 tccli/services/ocr/ocr_client.py
 tccli/services/ocr/v20181119/__init__.py
 tccli/services/ocr/v20181119/help.py
+tccli/services/organization/__init__.py
+tccli/services/organization/organization_client.py
+tccli/services/organization/v20181225/__init__.py
+tccli/services/organization/v20181225/help.py
 tccli/services/partners/__init__.py
 tccli/services/partners/partners_client.py
 tccli/services/partners/v20180321/__init__.py
 tccli/services/partners/v20180321/help.py
 tccli/services/postgres/__init__.py
 tccli/services/postgres/postgres_client.py
 tccli/services/postgres/v20170312/__init__.py
@@ -280,14 +286,18 @@
 tccli/services/redis/redis_client.py
 tccli/services/redis/v20180412/__init__.py
 tccli/services/redis/v20180412/help.py
 tccli/services/scf/__init__.py
 tccli/services/scf/scf_client.py
 tccli/services/scf/v20180416/__init__.py
 tccli/services/scf/v20180416/help.py
+tccli/services/sms/__init__.py
+tccli/services/sms/sms_client.py
+tccli/services/sms/v20190711/__init__.py
+tccli/services/sms/v20190711/help.py
 tccli/services/soe/__init__.py
 tccli/services/soe/soe_client.py
 tccli/services/soe/v20180724/__init__.py
 tccli/services/soe/v20180724/help.py
 tccli/services/sqlserver/__init__.py
 tccli/services/sqlserver/sqlserver_client.py
 tccli/services/sqlserver/v20180328/__init__.py
```

