# Comparing `tmp/spsdk-1.9.0.tar.gz` & `tmp/spsdk-1.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\spsdk-1.9.0.tar", last modified: Tue Jan 31 14:39:22 2023, max compression
+gzip compressed data, was "dist\spsdk-1.9.1.tar", last modified: Mon Mar 27 14:07:38 2023, max compression
```

## Comparing `spsdk-1.9.0.tar` & `spsdk-1.9.1.tar`

### file list

```diff
@@ -1,356 +1,358 @@
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:22.310384 spsdk-1.9.0/
--rw-rw-rw-   0        0        0     1975 2023-01-19 13:42:08.000000 spsdk-1.9.0/LICENSE
--rw-rw-rw-   0        0        0      166 2023-01-31 10:42:38.000000 spsdk-1.9.0/MANIFEST.in
--rw-rw-rw-   0        0        0     6529 2023-01-31 14:39:22.304383 spsdk-1.9.0/PKG-INFO
--rw-rw-rw-   0        0        0     4821 2023-01-31 14:36:13.000000 spsdk-1.9.0/README.md
--rw-rw-rw-   0        0        0     1777 2023-01-19 13:43:25.000000 spsdk-1.9.0/SW_Content_Register_SPSDK.txt
--rw-rw-rw-   0        0        0      782 2023-01-19 13:42:08.000000 spsdk-1.9.0/pyproject.toml
--rw-rw-rw-   0        0        0      578 2023-01-26 13:14:17.000000 spsdk-1.9.0/requirements-develop.txt
--rw-rw-rw-   0        0        0      687 2023-01-19 13:42:08.000000 spsdk-1.9.0/requirements.txt
--rw-rw-rw-   0        0        0       42 2023-01-31 14:39:22.311385 spsdk-1.9.0/setup.cfg
--rw-rw-rw-   0        0        0     3234 2023-01-31 10:06:08.000000 spsdk-1.9.0/setup.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.098811 spsdk-1.9.0/spsdk/
--rw-rw-rw-   0        0        0     4059 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/__init__.py
--rw-rw-rw-   0        0        0      256 2023-01-19 14:12:28.000000 spsdk-1.9.0/spsdk/__version__.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.213821 spsdk-1.9.0/spsdk/apps/
--rw-rw-rw-   0        0        0      195 2022-07-29 10:48:10.000000 spsdk-1.9.0/spsdk/apps/__init__.py
--rw-rw-rw-   0        0        0    62967 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/apps/blhost.py
--rw-rw-rw-   0        0        0     6420 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/apps/blhost_helper.py
--rw-rw-rw-   0        0        0    10674 2023-01-31 14:08:52.000000 spsdk-1.9.0/spsdk/apps/elftosb.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.225811 spsdk-1.9.0/spsdk/apps/elftosb_utils/
--rw-rw-rw-   0        0        0      193 2021-09-07 11:53:05.000000 spsdk-1.9.0/spsdk/apps/elftosb_utils/__init__.py
--rw-rw-rw-   0        0        0     2567 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/apps/elftosb_utils/sb_31_helper.py
--rw-rw-rw-   0        0        0     5062 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/apps/ifr.py
--rw-rw-rw-   0        0        0     8328 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/apps/nxpcertgen.py
--rw-rw-rw-   0        0        0     8098 2023-01-31 14:10:41.000000 spsdk-1.9.0/spsdk/apps/nxpcrypto.py
--rw-rw-rw-   0        0        0    36960 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/apps/nxpdebugmbox.py
--rw-rw-rw-   0        0        0    29086 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/apps/nxpdevhsm.py
--rw-rw-rw-   0        0        0     2976 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/apps/nxpdevscan.py
--rw-rw-rw-   0        0        0    68856 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/apps/nxpimage.py
--rw-rw-rw-   0        0        0     4028 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/apps/nxpkeygen.py
--rw-rw-rw-   0        0        0    14562 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/apps/pfr.py
--rw-rw-rw-   0        0        0     7097 2023-01-31 14:05:47.000000 spsdk-1.9.0/spsdk/apps/sdphost.py
--rw-rw-rw-   0        0        0     2184 2023-01-31 13:38:47.000000 spsdk-1.9.0/spsdk/apps/sdpshost.py
--rw-rw-rw-   0        0        0    12905 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/apps/shadowregs.py
--rw-rw-rw-   0        0        0     2661 2023-01-31 14:05:38.000000 spsdk-1.9.0/spsdk/apps/spsdk_apps.py
--rw-rw-rw-   0        0        0    19573 2023-01-31 14:12:08.000000 spsdk-1.9.0/spsdk/apps/tp_utils.py
--rw-rw-rw-   0        0        0     5417 2023-01-31 13:40:50.000000 spsdk-1.9.0/spsdk/apps/tpconfig.py
--rw-rw-rw-   0        0        0    17456 2023-01-31 14:09:24.000000 spsdk-1.9.0/spsdk/apps/tphost.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.242813 spsdk-1.9.0/spsdk/apps/utils/
--rw-rw-rw-   0        0        0      390 2023-01-31 14:07:37.000000 spsdk-1.9.0/spsdk/apps/utils/__init__.py
--rw-rw-rw-   0        0        0     9673 2023-01-31 14:09:16.000000 spsdk-1.9.0/spsdk/apps/utils/common_cli_options.py
--rw-rw-rw-   0        0        0    13526 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/apps/utils/utils.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.271826 spsdk-1.9.0/spsdk/crypto/
--rw-rw-rw-   0        0        0     3817 2023-01-31 14:05:04.000000 spsdk-1.9.0/spsdk/crypto/__init__.py
--rw-rw-rw-   0        0        0     7108 2023-01-31 14:10:23.000000 spsdk-1.9.0/spsdk/crypto/certificate_management.py
--rw-rw-rw-   0        0        0     7721 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/crypto/keys_management.py
--rw-rw-rw-   0        0        0     7702 2023-01-31 14:06:24.000000 spsdk-1.9.0/spsdk/crypto/loaders.py
--rw-rw-rw-   0        0        0     5459 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/crypto/signature_provider.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.305812 spsdk-1.9.0/spsdk/dat/
--rw-rw-rw-   0        0        0      337 2022-03-04 15:14:41.000000 spsdk-1.9.0/spsdk/dat/__init__.py
--rw-rw-rw-   0        0        0     5782 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/dat/dac_packet.py
--rw-rw-rw-   0        0        0     6692 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/dat/dar_packet.py
--rw-rw-rw-   0        0        0    29300 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/dat/debug_credential.py
--rw-rw-rw-   0        0        0    10729 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/dat/debug_mailbox.py
--rw-rw-rw-   0        0        0     7368 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/dat/dm_commands.py
--rw-rw-rw-   0        0        0     2797 2023-01-31 14:11:11.000000 spsdk-1.9.0/spsdk/dat/utils.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:19.998813 spsdk-1.9.0/spsdk/data/
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.321812 spsdk-1.9.0/spsdk/data/ahab/
--rw-rw-rw-   0        0        0      447 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/ahab/database.yml
--rw-rw-rw-   0        0        0    14834 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/ahab/sch_ahab.yml
--rw-rw-rw-   0        0        0     6722 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/ahab/sch_signed_msg.yml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.355812 spsdk-1.9.0/spsdk/data/cpu_data/
--rw-rw-rw-   0        0        0     5767 2021-03-29 09:53:43.000000 spsdk-1.9.0/spsdk/data/cpu_data/exec_hab_audit_rt1020.c
--rw-rw-rw-   0        0        0     5780 2021-03-29 09:53:43.000000 spsdk-1.9.0/spsdk/data/cpu_data/exec_hab_audit_rt1050.c
--rw-rw-rw-   0        0        0       34 2021-03-29 09:53:43.000000 spsdk-1.9.0/spsdk/data/cpu_data/exec_hab_audit_rt1060.c
--rw-rw-rw-   0        0        0     8772 2021-03-29 09:53:43.000000 spsdk-1.9.0/spsdk/data/cpu_data/rt1020_exec_hab_audit.bin
--rw-rw-rw-   0        0        0     5704 2021-03-29 09:53:43.000000 spsdk-1.9.0/spsdk/data/cpu_data/rt1050_exec_hab_audit.bin
--rw-rw-rw-   0        0        0     8908 2021-03-29 09:53:43.000000 spsdk-1.9.0/spsdk/data/cpu_data/rt1060_exec_hab_audit.bin
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.380815 spsdk-1.9.0/spsdk/data/ifr/
--rw-rw-rw-   0        0        0      279 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/ifr/database.yaml
--rw-rw-rw-   0        0        0    18488 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/ifr/k32w1xx_a0.xml
--rw-rw-rw-   0        0        0    19138 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/ifr/k32w1xx_a1.xml
--rw-rw-rw-   0        0        0    19612 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/ifr/kw45xx_a0.xml
--rw-rw-rw-   0        0        0    20262 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/ifr/kw45xx_a1.xml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.402813 spsdk-1.9.0/spsdk/data/image/
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.414813 spsdk-1.9.0/spsdk/data/image/bootable_image/
--rw-rw-rw-   0        0        0     1313 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/image/bootable_image/database.yml
--rw-rw-rw-   0        0        0     3007 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/image/bootable_image/sch_bimg.yml
--rw-rw-rw-   0        0        0     3800 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/data/image/database.yml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.456815 spsdk-1.9.0/spsdk/data/image/fcb/
--rw-rw-rw-   0        0        0      715 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/image/fcb/database.yml
--rw-rw-rw-   0        0        0    28577 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/image/fcb/lpc55s3x_flexspi_nor.xml
--rw-rw-rw-   0        0        0    27983 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/data/image/fcb/rt105x_flexspi_nor.xml
--rw-rw-rw-   0        0        0    27983 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/data/image/fcb/rt106x_flexspi_nor.xml
--rw-rw-rw-   0        0        0    27983 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/data/image/fcb/rt117x_flexspi_nor.xml
--rw-rw-rw-   0        0        0    29801 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/image/fcb/rt118x_flexspi_nor.xml
--rw-rw-rw-   0        0        0    28764 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/data/image/fcb/rt5xx_flexspi_nor.xml
--rw-rw-rw-   0        0        0    28942 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/data/image/fcb/rt6xx_flexspi_nor.xml
--rw-rw-rw-   0        0        0      949 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/image/fcb/sch_fcb.yml
--rw-rw-rw-   0        0        0     4138 2023-01-31 10:42:38.000000 spsdk-1.9.0/spsdk/data/image/sch_binary.yml
--rw-rw-rw-   0        0        0     9963 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/data/image/sch_mbimg.yml
--rw-rw-rw-   0        0        0    17536 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/data/image/sch_sb3.yml
--rw-rw-rw-   0        0        0     1394 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/data/image/sch_tz.yml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.550813 spsdk-1.9.0/spsdk/data/image/xmcd/
--rw-rw-rw-   0        0        0      943 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/image/xmcd/database.yml
--rw-rw-rw-   0        0        0    27981 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/image/xmcd/flexspi_ram_full.xml
--rw-rw-rw-   0        0        0     1479 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/image/xmcd/flexspi_ram_simplified.xml
--rw-rw-rw-   0        0        0     1397 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/image/xmcd/header.xml
--rw-rw-rw-   0        0        0     1008 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/image/xmcd/sch_xmcd.yml
--rw-rw-rw-   0        0        0     6304 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/image/xmcd/semc_sdram_full.xml
--rw-rw-rw-   0        0        0      843 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/image/xmcd/semc_sdram_simplified.xml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.557827 spsdk-1.9.0/spsdk/data/nxpcertgen/
--rw-rw-rw-   0        0        0     1874 2021-09-07 11:53:05.000000 spsdk-1.9.0/spsdk/data/nxpcertgen/certgen_config.yml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.567813 spsdk-1.9.0/spsdk/data/nxpdebugmbox/
--rw-rw-rw-   0        0        0     5696 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/data/nxpdebugmbox/template_config.yml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.575815 spsdk-1.9.0/spsdk/data/nxpdevhsm/
--rw-rw-rw-   0        0        0      104 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/data/nxpdevhsm/database.yaml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:19.991813 spsdk-1.9.0/spsdk/data/pfr/
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.646817 spsdk-1.9.0/spsdk/data/pfr/cfpa/
--rw-rw-rw-   0        0        0     3745 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/data/pfr/cfpa/database.yaml
--rw-rw-rw-   0        0        0    26604 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc550x_a.xml
--rw-rw-rw-   0        0        0    26604 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc551x_a.xml
--rw-rw-rw-   0        0        0    26604 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc552x_1b.xml
--rw-rw-rw-   0        0        0    16172 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc553x_0a.xml
--rw-rw-rw-   0        0        0    16289 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc553x_1a.xml
--rw-rw-rw-   0        0        0    75247 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc55s0x_a.xml
--rw-rw-rw-   0        0        0    75247 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc55s1x_a.xml
--rw-rw-rw-   0        0        0    77153 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc55s2x_1b.xml
--rw-rw-rw-   0        0        0    28916 2022-10-19 09:00:54.000000 spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc55s3x_0a.xml
--rw-rw-rw-   0        0        0    29024 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc55s3x_1a.xml
--rw-rw-rw-   0        0        0    77153 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc55s6x_1b.xml
--rw-rw-rw-   0        0        0    51284 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/pfr/cfpa/nhs52s04.xml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.718818 spsdk-1.9.0/spsdk/data/pfr/cmpa/
--rw-rw-rw-   0        0        0     3055 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/data/pfr/cmpa/database.yaml
--rw-rw-rw-   0        0        0    37700 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc550x_a.xml
--rw-rw-rw-   0        0        0    39156 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc551x_a.xml
--rw-rw-rw-   0        0        0    37600 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc552x_1b.xml
--rw-rw-rw-   0        0        0    57700 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc553x_0a.xml
--rw-rw-rw-   0        0        0    58198 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc553x_1a.xml
--rw-rw-rw-   0        0        0    58733 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc55s0x_a.xml
--rw-rw-rw-   0        0        0    60102 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc55s1x_a.xml
--rw-rw-rw-   0        0        0    57781 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc55s2x_1b.xml
--rw-rw-rw-   0        0        0    91574 2022-10-19 09:00:54.000000 spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc55s3x_0a.xml
--rw-rw-rw-   0        0        0    92280 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc55s3x_1a.xml
--rw-rw-rw-   0        0        0    57781 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc55s6x_1b.xml
--rw-rw-rw-   0        0        0   119265 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/pfr/cmpa/nhs52s04.xml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.747817 spsdk-1.9.0/spsdk/data/pfr/pfrc/
--rw-rw-rw-   0        0        0      824 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/pfr/pfrc/database.yaml
--rw-rw-rw-   0        0        0     3583 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/pfr/pfrc/rules_common.yaml
--rw-rw-rw-   0        0        0      913 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/pfr/pfrc/rules_lpc55s3x.yaml
--rw-rw-rw-   0        0        0      930 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/pfr/pfrc/rules_lpc55xx.yaml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.756819 spsdk-1.9.0/spsdk/data/regs/
--rw-rw-rw-   0        0        0     2122 2021-03-29 13:05:36.000000 spsdk-1.9.0/spsdk/data/regs/regs_desc_template.html
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.781818 spsdk-1.9.0/spsdk/data/shadowregs/
--rw-rw-rw-   0        0        0     2741 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/shadowregs/database.yaml
--rw-rw-rw-   0        0        0    60423 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/shadowregs/imxrt595_b0.xml
--rw-rw-rw-   0        0        0    59539 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/shadowregs/imxrt685_b0.xml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.806815 spsdk-1.9.0/spsdk/data/tp/
--rw-rw-rw-   0        0        0      543 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tp/database.yaml
--rw-rw-rw-   0        0        0    11195 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tp/sch_tp.yaml
--rw-rw-rw-   0        0        0     1517 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tp/tpconfig_cfg_template.yml
--rw-rw-rw-   0        0        0     1177 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/data/tp/tphost_cfg_template.yml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.877817 spsdk-1.9.0/spsdk/data/tz_presets/
--rw-rw-rw-   0        0        0     1096 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/data/tz_presets/database.yaml
--rw-rw-rw-   0        0        0    20268 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tz_presets/kw45xx_a0.yaml
--rw-rw-rw-   0        0        0     6497 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tz_presets/lpc55s0x.yaml
--rw-rw-rw-   0        0        0     6505 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tz_presets/lpc55s1x.yaml
--rw-rw-rw-   0        0        0     7613 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tz_presets/lpc55s3x_a0.yaml
--rw-rw-rw-   0        0        0     8837 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tz_presets/lpc55s3x_a1.yaml
--rw-rw-rw-   0        0        0     7274 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tz_presets/lpc55xx.yaml
--rw-rw-rw-   0        0        0     7219 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tz_presets/lpc55xx_a0.yaml
--rw-rw-rw-   0        0        0     7274 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tz_presets/lpc55xx_a1.yaml
--rw-rw-rw-   0        0        0     6720 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tz_presets/nhs52s04.yaml
--rw-rw-rw-   0        0        0    18585 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tz_presets/rt5xx.yaml
--rw-rw-rw-   0        0        0    16683 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tz_presets/rt5xx_a0.yaml
--rw-rw-rw-   0        0        0    17167 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tz_presets/rt6xx.yaml
--rw-rw-rw-   0        0        0    14520 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tz_presets/rt6xx_a0.yaml
--rw-rw-rw-   0        0        0    15419 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/tz_presets/rt6xx_b0.yaml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.882815 spsdk-1.9.0/spsdk/data/utils/
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.896819 spsdk-1.9.0/spsdk/data/utils/bee/
--rw-rw-rw-   0        0        0      176 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/utils/bee/database.yaml
--rw-rw-rw-   0        0        0     4313 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/utils/bee/sch_bee.yml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.916816 spsdk-1.9.0/spsdk/data/utils/iee/
--rw-rw-rw-   0        0        0      808 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/utils/iee/database.yml
--rw-rw-rw-   0        0        0     4628 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/utils/iee/fuses_rt117x.xml
--rw-rw-rw-   0        0        0     5626 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/utils/iee/sch_iee.yml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.945817 spsdk-1.9.0/spsdk/data/utils/otfad/
--rw-rw-rw-   0        0        0     2373 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/utils/otfad/database.yml
--rw-rw-rw-   0        0        0     3876 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/utils/otfad/fuses_rt118x.xml
--rw-rw-rw-   0        0        0     1860 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/utils/otfad/fuses_rt5xx.xml
--rw-rw-rw-   0        0        0     1860 2023-01-19 13:34:21.000000 spsdk-1.9.0/spsdk/data/utils/otfad/fuses_rt6xx.xml
--rw-rw-rw-   0        0        0     5451 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/utils/otfad/sch_otfad.yml
--rw-rw-rw-   0        0        0     7596 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/data/utils/sch_crypto.yml
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.977819 spsdk-1.9.0/spsdk/debuggers/
--rw-rw-rw-   0        0        0      360 2022-03-04 15:19:27.000000 spsdk-1.9.0/spsdk/debuggers/__init__.py
--rw-rw-rw-   0        0        0    17164 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/debuggers/debug_probe.py
--rw-rw-rw-   0        0        0     8879 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/debuggers/debug_probe_jlink.py
--rw-rw-rw-   0        0        0     8053 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/debuggers/debug_probe_pemicro.py
--rw-rw-rw-   0        0        0     9223 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/debuggers/debug_probe_pyocd.py
--rw-rw-rw-   0        0        0     8630 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/debuggers/utils.py
--rw-rw-rw-   0        0        0     1704 2023-01-31 14:04:56.000000 spsdk-1.9.0/spsdk/exceptions.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.050817 spsdk-1.9.0/spsdk/image/
--rw-rw-rw-   0        0        0     2887 2022-03-04 15:09:48.000000 spsdk-1.9.0/spsdk/image/__init__.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.072818 spsdk-1.9.0/spsdk/image/ahab/
--rw-rw-rw-   0        0        0      512 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/image/ahab/__init__.py
--rw-rw-rw-   0        0        0     7333 2023-01-31 14:03:06.000000 spsdk-1.9.0/spsdk/image/ahab/ahab_abstract_interfaces.py
--rw-rw-rw-   0        0        0   132907 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/image/ahab/ahab_container.py
--rw-rw-rw-   0        0        0    30909 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/image/ahab/signed_msg.py
--rw-rw-rw-   0        0        0    27735 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/image/bee.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.085817 spsdk-1.9.0/spsdk/image/bootable_image/
--rw-rw-rw-   0        0        0      455 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/image/bootable_image/__init__.py
--rw-rw-rw-   0        0        0    54569 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/image/bootable_image/bimg.py
--rw-rw-rw-   0        0        0    59069 2023-01-31 14:12:19.000000 spsdk-1.9.0/spsdk/image/commands.py
--rw-rw-rw-   0        0        0      308 2022-03-04 15:10:55.000000 spsdk-1.9.0/spsdk/image/exceptions.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.097818 spsdk-1.9.0/spsdk/image/fcb/
--rw-rw-rw-   0        0        0      455 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/image/fcb/__init__.py
--rw-rw-rw-   0        0        0     6037 2023-01-31 13:43:42.000000 spsdk-1.9.0/spsdk/image/fcb/fcb.py
--rw-rw-rw-   0        0        0    14371 2023-01-31 14:11:52.000000 spsdk-1.9.0/spsdk/image/hab_audit_log.py
--rw-rw-rw-   0        0        0     7433 2023-01-31 13:43:32.000000 spsdk-1.9.0/spsdk/image/header.py
--rw-rw-rw-   0        0        0   101439 2023-01-31 14:00:22.000000 spsdk-1.9.0/spsdk/image/images.py
--rw-rw-rw-   0        0        0     4824 2023-01-31 14:11:22.000000 spsdk-1.9.0/spsdk/image/keystore.py
--rw-rw-rw-   0        0        0    44840 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/image/mbi_mixin.py
--rw-rw-rw-   0        0        0    40160 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/image/mbimg.py
--rw-rw-rw-   0        0        0     3168 2023-01-31 14:09:33.000000 spsdk-1.9.0/spsdk/image/misc.py
--rw-rw-rw-   0        0        0    29498 2023-01-31 14:06:07.000000 spsdk-1.9.0/spsdk/image/secret.py
--rw-rw-rw-   0        0        0    83184 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/image/segments.py
--rw-rw-rw-   0        0        0     3363 2023-01-31 14:24:00.000000 spsdk-1.9.0/spsdk/image/segments_base.py
--rw-rw-rw-   0        0        0    12112 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/image/trustzone.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.110818 spsdk-1.9.0/spsdk/image/xmcd/
--rw-rw-rw-   0        0        0      477 2023-01-31 14:20:15.000000 spsdk-1.9.0/spsdk/image/xmcd/__init__.py
--rw-rw-rw-   0        0        0    13013 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/image/xmcd/xmcd.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.166818 spsdk-1.9.0/spsdk/mboot/
--rw-rw-rw-   0        0        0     1043 2021-09-07 11:53:05.000000 spsdk-1.9.0/spsdk/mboot/__init__.py
--rw-rw-rw-   0        0        0    19924 2023-01-31 13:40:08.000000 spsdk-1.9.0/spsdk/mboot/commands.py
--rw-rw-rw-   0        0        0    27139 2023-01-31 13:59:54.000000 spsdk-1.9.0/spsdk/mboot/error_codes.py
--rw-rw-rw-   0        0        0     1650 2021-09-07 11:53:05.000000 spsdk-1.9.0/spsdk/mboot/exceptions.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.245822 spsdk-1.9.0/spsdk/mboot/interfaces/
--rw-rw-rw-   0        0        0      477 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/mboot/interfaces/__init__.py
--rw-rw-rw-   0        0        0     1556 2023-01-31 14:04:18.000000 spsdk-1.9.0/spsdk/mboot/interfaces/base.py
--rw-rw-rw-   0        0        0     6894 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/mboot/interfaces/buspal.py
--rw-rw-rw-   0        0        0     5383 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/mboot/interfaces/buspal_i2c.py
--rw-rw-rw-   0        0        0     6740 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/mboot/interfaces/buspal_spi.py
--rw-rw-rw-   0        0        0    17912 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/mboot/interfaces/uart.py
--rw-rw-rw-   0        0        0    11049 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/mboot/interfaces/usb.py
--rw-rw-rw-   0        0        0    17059 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/mboot/interfaces/usbsio.py
--rw-rw-rw-   0        0        0    60779 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/mboot/mcuboot.py
--rw-rw-rw-   0        0        0     6999 2023-01-31 14:04:36.000000 spsdk-1.9.0/spsdk/mboot/memories.py
--rw-rw-rw-   0        0        0    30075 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/mboot/properties.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.322378 spsdk-1.9.0/spsdk/pfr/
--rw-rw-rw-   0        0        0      595 2023-01-31 13:41:46.000000 spsdk-1.9.0/spsdk/pfr/__init__.py
--rw-rw-rw-   0        0        0      684 2023-01-31 14:05:22.000000 spsdk-1.9.0/spsdk/pfr/exceptions.py
--rw-rw-rw-   0        0        0    23603 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/pfr/pfr.py
--rw-rw-rw-   0        0        0     6075 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/pfr/pfrc.py
--rw-rw-rw-   0        0        0     3075 2023-01-31 14:02:56.000000 spsdk-1.9.0/spsdk/pfr/processor.py
--rw-rw-rw-   0        0        0     2991 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/pfr/translator.py
--rw-rw-rw-   0        0        0        0 2022-02-02 14:02:26.000000 spsdk-1.9.0/spsdk/py.typed
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.335377 spsdk-1.9.0/spsdk/sbfile/
--rw-rw-rw-   0        0        0      159 2021-03-29 09:53:43.000000 spsdk-1.9.0/spsdk/sbfile/__init__.py
--rw-rw-rw-   0        0        0     7129 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/sbfile/misc.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.375378 spsdk-1.9.0/spsdk/sbfile/sb1/
--rw-rw-rw-   0        0        0      913 2022-03-04 15:20:47.000000 spsdk-1.9.0/spsdk/sbfile/sb1/__init__.py
--rw-rw-rw-   0        0        0     1477 2022-03-04 15:14:10.000000 spsdk-1.9.0/spsdk/sbfile/sb1/commands.py
--rw-rw-rw-   0        0        0    16704 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/sbfile/sb1/headers.py
--rw-rw-rw-   0        0        0     9856 2022-03-04 12:48:46.000000 spsdk-1.9.0/spsdk/sbfile/sb1/images.py
--rw-rw-rw-   0        0        0     4800 2023-01-31 13:41:26.000000 spsdk-1.9.0/spsdk/sbfile/sb1/sections.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.427378 spsdk-1.9.0/spsdk/sbfile/sb2/
--rw-rw-rw-   0        0        0      171 2022-03-04 15:12:28.000000 spsdk-1.9.0/spsdk/sbfile/sb2/__init__.py
--rw-rw-rw-   0        0        0    36713 2023-01-31 14:02:36.000000 spsdk-1.9.0/spsdk/sbfile/sb2/commands.py
--rw-rw-rw-   0        0        0     9104 2023-01-31 14:01:57.000000 spsdk-1.9.0/spsdk/sbfile/sb2/headers.py
--rw-rw-rw-   0        0        0    42448 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/sbfile/sb2/images.py
--rw-rw-rw-   0        0        0    14085 2023-01-31 13:59:45.000000 spsdk-1.9.0/spsdk/sbfile/sb2/sb_21_helper.py
--rw-rw-rw-   0        0        0    15895 2023-01-31 14:00:04.000000 spsdk-1.9.0/spsdk/sbfile/sb2/sections.py
--rw-rw-rw-   0        0        0    11197 2023-01-31 10:42:38.000000 spsdk-1.9.0/spsdk/sbfile/sb2/sly_bd_lexer.py
--rw-rw-rw-   0        0        0    60550 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/sbfile/sb2/sly_bd_parser.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.463379 spsdk-1.9.0/spsdk/sbfile/sb31/
--rw-rw-rw-   0        0        0      852 2022-03-04 15:15:25.000000 spsdk-1.9.0/spsdk/sbfile/sb31/__init__.py
--rw-rw-rw-   0        0        0    39242 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/sbfile/sb31/commands.py
--rw-rw-rw-   0        0        0     1062 2021-09-07 10:04:34.000000 spsdk-1.9.0/spsdk/sbfile/sb31/constants.py
--rw-rw-rw-   0        0        0     6213 2021-09-07 11:53:05.000000 spsdk-1.9.0/spsdk/sbfile/sb31/functions.py
--rw-rw-rw-   0        0        0    26829 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/sbfile/sb31/images.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.511380 spsdk-1.9.0/spsdk/sdp/
--rw-rw-rw-   0        0        0      673 2022-03-04 15:17:16.000000 spsdk-1.9.0/spsdk/sdp/__init__.py
--rw-rw-rw-   0        0        0     4471 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/sdp/commands.py
--rw-rw-rw-   0        0        0     3997 2021-09-07 10:04:34.000000 spsdk-1.9.0/spsdk/sdp/error_codes.py
--rw-rw-rw-   0        0        0     1476 2021-09-07 11:53:05.000000 spsdk-1.9.0/spsdk/sdp/exceptions.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.589379 spsdk-1.9.0/spsdk/sdp/interfaces/
--rw-rw-rw-   0        0        0      359 2022-03-04 12:48:46.000000 spsdk-1.9.0/spsdk/sdp/interfaces/__init__.py
--rw-rw-rw-   0        0        0     1185 2023-01-31 14:00:11.000000 spsdk-1.9.0/spsdk/sdp/interfaces/base.py
--rw-rw-rw-   0        0        0     6880 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/sdp/interfaces/uart.py
--rw-rw-rw-   0        0        0    10208 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/sdp/interfaces/usb.py
--rw-rw-rw-   0        0        0    15667 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/sdp/sdp.py
--rw-rw-rw-   0        0        0     3526 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/sdp/sdps.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.611380 spsdk-1.9.0/spsdk/shadowregs/
--rw-rw-rw-   0        0        0      237 2021-03-29 13:05:36.000000 spsdk-1.9.0/spsdk/shadowregs/__init__.py
--rw-rw-rw-   0        0        0    18112 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/shadowregs/shadowregs.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.707380 spsdk-1.9.0/spsdk/tp/
--rw-rw-rw-   0        0        0      773 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/tp/__init__.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.797381 spsdk-1.9.0/spsdk/tp/adapters/
--rw-rw-rw-   0        0        0     1024 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/tp/adapters/__init__.py
--rw-rw-rw-   0        0        0    12296 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/tp/adapters/scard_commands.py
--rw-rw-rw-   0        0        0     6649 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/tp/adapters/scard_utils.py
--rw-rw-rw-   0        0        0    21907 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/tp/adapters/tpdev_scard.py
--rw-rw-rw-   0        0        0    14846 2023-01-31 13:39:35.000000 spsdk-1.9.0/spsdk/tp/adapters/tptarget_blhost.py
--rw-rw-rw-   0        0        0     3245 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/tp/adapters/utils.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.841381 spsdk-1.9.0/spsdk/tp/data_container/
--rw-rw-rw-   0        0        0      493 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/tp/data_container/__init__.py
--rw-rw-rw-   0        0        0    12445 2023-01-31 14:01:49.000000 spsdk-1.9.0/spsdk/tp/data_container/audit_log.py
--rw-rw-rw-   0        0        0    16529 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/tp/data_container/data_container.py
--rw-rw-rw-   0        0        0     7194 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/tp/data_container/data_container_auth.py
--rw-rw-rw-   0        0        0     2587 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/tp/data_container/payload_types.py
--rw-rw-rw-   0        0        0      523 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/tp/exceptions.py
--rw-rw-rw-   0        0        0     9760 2023-01-31 14:07:04.000000 spsdk-1.9.0/spsdk/tp/tp_intf.py
--rw-rw-rw-   0        0        0     4109 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/tp/tpconfig.py
--rw-rw-rw-   0        0        0    27249 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/tp/tphost.py
--rw-rw-rw-   0        0        0     5900 2023-01-31 13:38:26.000000 spsdk-1.9.0/spsdk/tp/utils.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:21.973382 spsdk-1.9.0/spsdk/utils/
--rw-rw-rw-   0        0        0      590 2022-03-04 15:16:43.000000 spsdk-1.9.0/spsdk/utils/__init__.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:22.155385 spsdk-1.9.0/spsdk/utils/crypto/
--rw-rw-rw-   0        0        0     1338 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/utils/crypto/__init__.py
--rw-rw-rw-   0        0        0     7703 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/utils/crypto/abstract.py
--rw-rw-rw-   0        0        0    15719 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/utils/crypto/backend_internal.py
--rw-rw-rw-   0        0        0    15108 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/utils/crypto/backend_openssl.py
--rw-rw-rw-   0        0        0    36312 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/utils/crypto/cert_blocks.py
--rw-rw-rw-   0        0        0     7944 2022-07-29 07:41:59.000000 spsdk-1.9.0/spsdk/utils/crypto/certificate.py
--rw-rw-rw-   0        0        0     4946 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/utils/crypto/common.py
--rw-rw-rw-   0        0        0    29310 2023-01-26 13:14:17.000000 spsdk-1.9.0/spsdk/utils/crypto/iee.py
--rw-rw-rw-   0        0        0    36560 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/utils/crypto/otfad.py
--rw-rw-rw-   0        0        0     7370 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/utils/crypto/rkht.py
--rw-rw-rw-   0        0        0     7995 2023-01-31 14:10:13.000000 spsdk-1.9.0/spsdk/utils/database.py
--rw-rw-rw-   0        0        0     7368 2023-01-31 14:11:02.000000 spsdk-1.9.0/spsdk/utils/devicedescription.py
--rw-rw-rw-   0        0        0     6147 2023-01-31 13:39:24.000000 spsdk-1.9.0/spsdk/utils/easy_enum.py
--rw-rw-rw-   0        0        0     2086 2021-09-07 11:53:05.000000 spsdk-1.9.0/spsdk/utils/easy_enum.pyi
--rw-rw-rw-   0        0        0      782 2021-09-07 11:53:05.000000 spsdk-1.9.0/spsdk/utils/exceptions.py
--rw-rw-rw-   0        0        0    20976 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/utils/images.py
--rw-rw-rw-   0        0        0    28210 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/utils/misc.py
--rw-rw-rw-   0        0        0     5662 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/utils/nxpdevscan.py
--rw-rw-rw-   0        0        0     5583 2023-01-31 13:36:38.000000 spsdk-1.9.0/spsdk/utils/reg_config.py
--rw-rw-rw-   0        0        0    52384 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/utils/registers.py
--rw-rw-rw-   0        0        0    20425 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/utils/schema_validator.py
--rw-rw-rw-   0        0        0     3890 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/utils/serial_buspal_proxy.py
--rw-rw-rw-   0        0        0     4656 2023-01-19 13:42:08.000000 spsdk-1.9.0/spsdk/utils/serial_proxy.py
--rw-rw-rw-   0        0        0    12381 2023-01-31 13:40:28.000000 spsdk-1.9.0/spsdk/utils/usbfilter.py
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:20.124811 spsdk-1.9.0/spsdk.egg-info/
--rw-rw-rw-   0        0        0     6529 2023-01-31 14:39:19.000000 spsdk-1.9.0/spsdk.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     9111 2023-01-31 14:39:19.000000 spsdk-1.9.0/spsdk.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-01-31 14:39:19.000000 spsdk-1.9.0/spsdk.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      709 2023-01-31 14:39:19.000000 spsdk-1.9.0/spsdk.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0      585 2023-01-31 14:39:19.000000 spsdk-1.9.0/spsdk.egg-info/requires.txt
--rw-rw-rw-   0        0        0       12 2023-01-31 14:39:19.000000 spsdk-1.9.0/spsdk.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-01-31 14:39:22.298388 spsdk-1.9.0/tools/
--rw-rw-rw-   0        0        0      122 2023-01-31 14:19:49.000000 spsdk-1.9.0/tools/__init__.py
--rw-rw-rw-   0        0        0     1852 2023-01-31 14:07:22.000000 spsdk-1.9.0/tools/checker_copyright_year.py
--rw-rw-rw-   0        0        0    12467 2023-01-31 14:01:31.000000 spsdk-1.9.0/tools/checker_dependencies.py
--rw-rw-rw-   0        0        0     3821 2023-01-31 14:10:03.000000 spsdk-1.9.0/tools/checker_mypy_annotations.py
--rw-rw-rw-   0        0        0     2942 2023-01-31 14:04:09.000000 spsdk-1.9.0/tools/checker_pydocstyle.py
--rw-rw-rw-   0        0        0     3841 2022-07-29 13:12:50.000000 spsdk-1.9.0/tools/clr.py
--rw-rw-rw-   0        0        0     7399 2023-01-31 13:43:17.000000 spsdk-1.9.0/tools/fcb_header_to_xml.py
--rw-rw-rw-   0        0        0     3965 2022-03-04 12:48:46.000000 spsdk-1.9.0/tools/flashloader_converter.py
--rw-rw-rw-   0        0        0     1794 2022-07-29 10:15:30.000000 spsdk-1.9.0/tools/git_operations.py
--rw-rw-rw-   0        0        0    17631 2023-01-31 13:40:59.000000 spsdk-1.9.0/tools/gitcov.py
--rw-rw-rw-   0        0        0     9174 2023-01-31 13:40:38.000000 spsdk-1.9.0/tools/release_notes.py
--rw-rw-rw-   0        0        0    13987 2023-01-31 14:19:58.000000 spsdk-1.9.0/tools/req_update.py
--rw-rw-rw-   0        0        0    21451 2023-01-31 14:08:11.000000 spsdk-1.9.0/tools/sr_xls2xml.py
--rw-rw-rw-   0        0        0    11051 2023-01-31 14:01:39.000000 spsdk-1.9.0/tools/task_scheduler.py
--rw-rw-rw-   0        0        0     1996 2023-01-31 14:11:42.000000 spsdk-1.9.0/tools/tp_migrate_audit_log.py
--rw-rw-rw-   0        0        0    13876 2023-01-31 14:05:31.000000 spsdk-1.9.0/tools/tp_setup_workspace.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:38.200108 spsdk-1.9.1/
+-rw-rw-rw-   0        0        0     1975 2023-03-27 13:10:53.000000 spsdk-1.9.1/LICENSE
+-rw-rw-rw-   0        0        0      166 2023-03-27 13:10:53.000000 spsdk-1.9.1/MANIFEST.in
+-rw-rw-rw-   0        0        0     6136 2023-03-27 14:07:38.200108 spsdk-1.9.1/PKG-INFO
+-rw-rw-rw-   0        0        0     4810 2023-03-27 14:05:15.000000 spsdk-1.9.1/README.md
+-rw-rw-rw-   0        0        0     1777 2023-03-27 13:15:20.000000 spsdk-1.9.1/SW_Content_Register_SPSDK.txt
+-rw-rw-rw-   0        0        0      782 2023-03-27 13:10:54.000000 spsdk-1.9.1/pyproject.toml
+-rw-rw-rw-   0        0        0      578 2023-03-27 13:10:54.000000 spsdk-1.9.1/requirements-develop.txt
+-rw-rw-rw-   0        0        0      691 2023-03-27 13:15:20.000000 spsdk-1.9.1/requirements.txt
+-rw-rw-rw-   0        0        0       42 2023-03-27 14:07:38.200108 spsdk-1.9.1/setup.cfg
+-rw-rw-rw-   0        0        0     3234 2023-03-27 13:10:54.000000 spsdk-1.9.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.359972 spsdk-1.9.1/spsdk/
+-rw-rw-rw-   0        0        0     4059 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/__init__.py
+-rw-rw-rw-   0        0        0      256 2023-03-27 13:15:20.000000 spsdk-1.9.1/spsdk/__version__.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.475898 spsdk-1.9.1/spsdk/apps/
+-rw-rw-rw-   0        0        0      195 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/__init__.py
+-rw-rw-rw-   0        0        0    63025 2023-03-27 13:15:20.000000 spsdk-1.9.1/spsdk/apps/blhost.py
+-rw-rw-rw-   0        0        0     6420 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/blhost_helper.py
+-rw-rw-rw-   0        0        0    10674 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/elftosb.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.475898 spsdk-1.9.1/spsdk/apps/elftosb_utils/
+-rw-rw-rw-   0        0        0      193 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/elftosb_utils/__init__.py
+-rw-rw-rw-   0        0        0     2567 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/elftosb_utils/sb_31_helper.py
+-rw-rw-rw-   0        0        0     5062 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/ifr.py
+-rw-rw-rw-   0        0        0     8328 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/nxpcertgen.py
+-rw-rw-rw-   0        0        0     8098 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/nxpcrypto.py
+-rw-rw-rw-   0        0        0    37012 2023-03-27 13:15:20.000000 spsdk-1.9.1/spsdk/apps/nxpdebugmbox.py
+-rw-rw-rw-   0        0        0    31243 2023-03-27 13:15:20.000000 spsdk-1.9.1/spsdk/apps/nxpdevhsm.py
+-rw-rw-rw-   0        0        0     2976 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/nxpdevscan.py
+-rw-rw-rw-   0        0        0    68856 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/nxpimage.py
+-rw-rw-rw-   0        0        0     4028 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/nxpkeygen.py
+-rw-rw-rw-   0        0        0    14562 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/pfr.py
+-rw-rw-rw-   0        0        0     7097 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/sdphost.py
+-rw-rw-rw-   0        0        0     2184 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/sdpshost.py
+-rw-rw-rw-   0        0        0    12905 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/shadowregs.py
+-rw-rw-rw-   0        0        0     2661 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/spsdk_apps.py
+-rw-rw-rw-   0        0        0    19573 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/tp_utils.py
+-rw-rw-rw-   0        0        0     5417 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/tpconfig.py
+-rw-rw-rw-   0        0        0    17497 2023-03-27 13:15:20.000000 spsdk-1.9.1/spsdk/apps/tphost.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.491523 spsdk-1.9.1/spsdk/apps/utils/
+-rw-rw-rw-   0        0        0      390 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/utils/__init__.py
+-rw-rw-rw-   0        0        0     9673 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/utils/common_cli_options.py
+-rw-rw-rw-   0        0        0    13526 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/apps/utils/utils.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.498040 spsdk-1.9.1/spsdk/crypto/
+-rw-rw-rw-   0        0        0     3817 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/crypto/__init__.py
+-rw-rw-rw-   0        0        0     7108 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/crypto/certificate_management.py
+-rw-rw-rw-   0        0        0     7721 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/crypto/keys_management.py
+-rw-rw-rw-   0        0        0     7702 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/crypto/loaders.py
+-rw-rw-rw-   0        0        0     5459 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/crypto/signature_provider.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.513704 spsdk-1.9.1/spsdk/dat/
+-rw-rw-rw-   0        0        0      337 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/dat/__init__.py
+-rw-rw-rw-   0        0        0     5782 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/dat/dac_packet.py
+-rw-rw-rw-   0        0        0     6692 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/dat/dar_packet.py
+-rw-rw-rw-   0        0        0    29300 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/dat/debug_credential.py
+-rw-rw-rw-   0        0        0    10729 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/dat/debug_mailbox.py
+-rw-rw-rw-   0        0        0     7368 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/dat/dm_commands.py
+-rw-rw-rw-   0        0        0     2797 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/dat/utils.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.297454 spsdk-1.9.1/spsdk/data/
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.529331 spsdk-1.9.1/spsdk/data/ahab/
+-rw-rw-rw-   0        0        0      447 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/ahab/database.yml
+-rw-rw-rw-   0        0        0    14834 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/ahab/sch_ahab.yml
+-rw-rw-rw-   0        0        0     6722 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/ahab/sch_signed_msg.yml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.544955 spsdk-1.9.1/spsdk/data/cpu_data/
+-rw-rw-rw-   0        0        0     5767 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/cpu_data/exec_hab_audit_rt1020.c
+-rw-rw-rw-   0        0        0     5780 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/cpu_data/exec_hab_audit_rt1050.c
+-rw-rw-rw-   0        0        0       34 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/cpu_data/exec_hab_audit_rt1060.c
+-rw-rw-rw-   0        0        0     8772 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/cpu_data/rt1020_exec_hab_audit.bin
+-rw-rw-rw-   0        0        0     5704 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/cpu_data/rt1050_exec_hab_audit.bin
+-rw-rw-rw-   0        0        0     8908 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/cpu_data/rt1060_exec_hab_audit.bin
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.560578 spsdk-1.9.1/spsdk/data/ifr/
+-rw-rw-rw-   0        0        0      279 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/ifr/database.yaml
+-rw-rw-rw-   0        0        0    18488 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/ifr/k32w1xx_a0.xml
+-rw-rw-rw-   0        0        0    19138 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/ifr/k32w1xx_a1.xml
+-rw-rw-rw-   0        0        0    19612 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/ifr/kw45xx_a0.xml
+-rw-rw-rw-   0        0        0    20262 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/ifr/kw45xx_a1.xml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.560578 spsdk-1.9.1/spsdk/data/image/
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.576203 spsdk-1.9.1/spsdk/data/image/bootable_image/
+-rw-rw-rw-   0        0        0     1313 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/bootable_image/database.yml
+-rw-rw-rw-   0        0        0     3007 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/bootable_image/sch_bimg.yml
+-rw-rw-rw-   0        0        0     3800 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/database.yml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.598347 spsdk-1.9.1/spsdk/data/image/fcb/
+-rw-rw-rw-   0        0        0      715 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/fcb/database.yml
+-rw-rw-rw-   0        0        0    28577 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/fcb/lpc55s3x_flexspi_nor.xml
+-rw-rw-rw-   0        0        0    27983 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/fcb/rt105x_flexspi_nor.xml
+-rw-rw-rw-   0        0        0    27983 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/fcb/rt106x_flexspi_nor.xml
+-rw-rw-rw-   0        0        0    27983 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/fcb/rt117x_flexspi_nor.xml
+-rw-rw-rw-   0        0        0    29801 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/fcb/rt118x_flexspi_nor.xml
+-rw-rw-rw-   0        0        0    28764 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/fcb/rt5xx_flexspi_nor.xml
+-rw-rw-rw-   0        0        0    28942 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/fcb/rt6xx_flexspi_nor.xml
+-rw-rw-rw-   0        0        0      949 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/fcb/sch_fcb.yml
+-rw-rw-rw-   0        0        0     4138 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/sch_binary.yml
+-rw-rw-rw-   0        0        0     9963 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/sch_mbimg.yml
+-rw-rw-rw-   0        0        0    17536 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/sch_sb3.yml
+-rw-rw-rw-   0        0        0     1394 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/sch_tz.yml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.613993 spsdk-1.9.1/spsdk/data/image/xmcd/
+-rw-rw-rw-   0        0        0      943 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/xmcd/database.yml
+-rw-rw-rw-   0        0        0    27981 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/xmcd/flexspi_ram_full.xml
+-rw-rw-rw-   0        0        0     1479 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/xmcd/flexspi_ram_simplified.xml
+-rw-rw-rw-   0        0        0     1397 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/xmcd/header.xml
+-rw-rw-rw-   0        0        0     1008 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/xmcd/sch_xmcd.yml
+-rw-rw-rw-   0        0        0     6304 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/xmcd/semc_sdram_full.xml
+-rw-rw-rw-   0        0        0      843 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/image/xmcd/semc_sdram_simplified.xml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.629655 spsdk-1.9.1/spsdk/data/nxpcertgen/
+-rw-rw-rw-   0        0        0     1874 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/nxpcertgen/certgen_config.yml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.629655 spsdk-1.9.1/spsdk/data/nxpdebugmbox/
+-rw-rw-rw-   0        0        0     5696 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/nxpdebugmbox/template_config.yml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.629655 spsdk-1.9.1/spsdk/data/nxpdevhsm/
+-rw-rw-rw-   0        0        0      104 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/nxpdevhsm/database.yaml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.297454 spsdk-1.9.1/spsdk/data/pfr/
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.676490 spsdk-1.9.1/spsdk/data/pfr/cfpa/
+-rw-rw-rw-   0        0        0     3745 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cfpa/database.yaml
+-rw-rw-rw-   0        0        0    26604 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc550x_a.xml
+-rw-rw-rw-   0        0        0    26604 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc551x_a.xml
+-rw-rw-rw-   0        0        0    26604 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc552x_1b.xml
+-rw-rw-rw-   0        0        0    16172 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc553x_0a.xml
+-rw-rw-rw-   0        0        0    16289 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc553x_1a.xml
+-rw-rw-rw-   0        0        0    75247 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc55s0x_a.xml
+-rw-rw-rw-   0        0        0    75247 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc55s1x_a.xml
+-rw-rw-rw-   0        0        0    77153 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc55s2x_1b.xml
+-rw-rw-rw-   0        0        0    28916 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc55s3x_0a.xml
+-rw-rw-rw-   0        0        0    29024 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc55s3x_1a.xml
+-rw-rw-rw-   0        0        0    77153 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc55s6x_1b.xml
+-rw-rw-rw-   0        0        0    51284 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cfpa/nhs52s04.xml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.698631 spsdk-1.9.1/spsdk/data/pfr/cmpa/
+-rw-rw-rw-   0        0        0     3055 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cmpa/database.yaml
+-rw-rw-rw-   0        0        0    37700 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc550x_a.xml
+-rw-rw-rw-   0        0        0    39156 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc551x_a.xml
+-rw-rw-rw-   0        0        0    37600 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc552x_1b.xml
+-rw-rw-rw-   0        0        0    57700 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc553x_0a.xml
+-rw-rw-rw-   0        0        0    58198 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc553x_1a.xml
+-rw-rw-rw-   0        0        0    58733 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc55s0x_a.xml
+-rw-rw-rw-   0        0        0    60102 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc55s1x_a.xml
+-rw-rw-rw-   0        0        0    57781 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc55s2x_1b.xml
+-rw-rw-rw-   0        0        0    91574 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc55s3x_0a.xml
+-rw-rw-rw-   0        0        0    92280 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc55s3x_1a.xml
+-rw-rw-rw-   0        0        0    57781 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc55s6x_1b.xml
+-rw-rw-rw-   0        0        0   119265 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/cmpa/nhs52s04.xml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.714272 spsdk-1.9.1/spsdk/data/pfr/pfrc/
+-rw-rw-rw-   0        0        0      824 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/pfrc/database.yaml
+-rw-rw-rw-   0        0        0     3583 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/pfrc/rules_common.yaml
+-rw-rw-rw-   0        0        0      913 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/pfrc/rules_lpc55s3x.yaml
+-rw-rw-rw-   0        0        0      930 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/pfr/pfrc/rules_lpc55xx.yaml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.714272 spsdk-1.9.1/spsdk/data/regs/
+-rw-rw-rw-   0        0        0     2122 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/regs/regs_desc_template.html
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.729910 spsdk-1.9.1/spsdk/data/shadowregs/
+-rw-rw-rw-   0        0        0     2741 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/shadowregs/database.yaml
+-rw-rw-rw-   0        0        0    60423 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/shadowregs/imxrt595_b0.xml
+-rw-rw-rw-   0        0        0    59539 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/shadowregs/imxrt685_b0.xml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.745520 spsdk-1.9.1/spsdk/data/tp/
+-rw-rw-rw-   0        0        0      505 2023-03-27 13:15:20.000000 spsdk-1.9.1/spsdk/data/tp/database.yaml
+-rw-rw-rw-   0        0        0    11195 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tp/sch_tp.yaml
+-rw-rw-rw-   0        0        0     1517 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tp/tpconfig_cfg_template.yml
+-rw-rw-rw-   0        0        0     1177 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tp/tphost_cfg_template.yml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.776770 spsdk-1.9.1/spsdk/data/tz_presets/
+-rw-rw-rw-   0        0        0     1096 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tz_presets/database.yaml
+-rw-rw-rw-   0        0        0    20268 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tz_presets/kw45xx_a0.yaml
+-rw-rw-rw-   0        0        0     6497 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tz_presets/lpc55s0x.yaml
+-rw-rw-rw-   0        0        0     6505 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tz_presets/lpc55s1x.yaml
+-rw-rw-rw-   0        0        0     7613 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tz_presets/lpc55s3x_a0.yaml
+-rw-rw-rw-   0        0        0     8837 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tz_presets/lpc55s3x_a1.yaml
+-rw-rw-rw-   0        0        0     7274 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tz_presets/lpc55xx.yaml
+-rw-rw-rw-   0        0        0     7219 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tz_presets/lpc55xx_a0.yaml
+-rw-rw-rw-   0        0        0     7274 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tz_presets/lpc55xx_a1.yaml
+-rw-rw-rw-   0        0        0     6720 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tz_presets/nhs52s04.yaml
+-rw-rw-rw-   0        0        0    18585 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tz_presets/rt5xx.yaml
+-rw-rw-rw-   0        0        0    16683 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tz_presets/rt5xx_a0.yaml
+-rw-rw-rw-   0        0        0    17167 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tz_presets/rt6xx.yaml
+-rw-rw-rw-   0        0        0    14520 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tz_presets/rt6xx_a0.yaml
+-rw-rw-rw-   0        0        0    15419 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/tz_presets/rt6xx_b0.yaml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.776770 spsdk-1.9.1/spsdk/data/utils/
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.792397 spsdk-1.9.1/spsdk/data/utils/bee/
+-rw-rw-rw-   0        0        0      176 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/utils/bee/database.yaml
+-rw-rw-rw-   0        0        0     4313 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/utils/bee/sch_bee.yml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.798912 spsdk-1.9.1/spsdk/data/utils/iee/
+-rw-rw-rw-   0        0        0      808 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/utils/iee/database.yml
+-rw-rw-rw-   0        0        0     4628 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/utils/iee/fuses_rt117x.xml
+-rw-rw-rw-   0        0        0     5626 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/utils/iee/sch_iee.yml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.814558 spsdk-1.9.1/spsdk/data/utils/otfad/
+-rw-rw-rw-   0        0        0     2373 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/utils/otfad/database.yml
+-rw-rw-rw-   0        0        0     3876 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/utils/otfad/fuses_rt118x.xml
+-rw-rw-rw-   0        0        0     1860 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/utils/otfad/fuses_rt5xx.xml
+-rw-rw-rw-   0        0        0     1860 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/utils/otfad/fuses_rt6xx.xml
+-rw-rw-rw-   0        0        0     5451 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/utils/otfad/sch_otfad.yml
+-rw-rw-rw-   0        0        0     7596 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/data/utils/sch_crypto.yml
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.830181 spsdk-1.9.1/spsdk/debuggers/
+-rw-rw-rw-   0        0        0      360 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/debuggers/__init__.py
+-rw-rw-rw-   0        0        0    17164 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/debuggers/debug_probe.py
+-rw-rw-rw-   0        0        0     8879 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/debuggers/debug_probe_jlink.py
+-rw-rw-rw-   0        0        0     8053 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/debuggers/debug_probe_pemicro.py
+-rw-rw-rw-   0        0        0     9384 2023-03-27 13:15:20.000000 spsdk-1.9.1/spsdk/debuggers/debug_probe_pyocd.py
+-rw-rw-rw-   0        0        0     8630 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/debuggers/utils.py
+-rw-rw-rw-   0        0        0     1704 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/exceptions.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.861432 spsdk-1.9.1/spsdk/image/
+-rw-rw-rw-   0        0        0     2887 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/__init__.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.877056 spsdk-1.9.1/spsdk/image/ahab/
+-rw-rw-rw-   0        0        0      512 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/ahab/__init__.py
+-rw-rw-rw-   0        0        0     7333 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/ahab/ahab_abstract_interfaces.py
+-rw-rw-rw-   0        0        0   132907 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/ahab/ahab_container.py
+-rw-rw-rw-   0        0        0    30909 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/ahab/signed_msg.py
+-rw-rw-rw-   0        0        0    27735 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/bee.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.877056 spsdk-1.9.1/spsdk/image/bootable_image/
+-rw-rw-rw-   0        0        0      455 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/bootable_image/__init__.py
+-rw-rw-rw-   0        0        0    54569 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/bootable_image/bimg.py
+-rw-rw-rw-   0        0        0    59069 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/commands.py
+-rw-rw-rw-   0        0        0      308 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/exceptions.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.892688 spsdk-1.9.1/spsdk/image/fcb/
+-rw-rw-rw-   0        0        0      455 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/fcb/__init__.py
+-rw-rw-rw-   0        0        0     6037 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/fcb/fcb.py
+-rw-rw-rw-   0        0        0    14371 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/hab_audit_log.py
+-rw-rw-rw-   0        0        0     7433 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/header.py
+-rw-rw-rw-   0        0        0   101439 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/images.py
+-rw-rw-rw-   0        0        0     4824 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/keystore.py
+-rw-rw-rw-   0        0        0    44840 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/mbi_mixin.py
+-rw-rw-rw-   0        0        0    40160 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/mbimg.py
+-rw-rw-rw-   0        0        0     3168 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/misc.py
+-rw-rw-rw-   0        0        0    29498 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/secret.py
+-rw-rw-rw-   0        0        0    83184 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/segments.py
+-rw-rw-rw-   0        0        0     3363 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/segments_base.py
+-rw-rw-rw-   0        0        0    12112 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/trustzone.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.899212 spsdk-1.9.1/spsdk/image/xmcd/
+-rw-rw-rw-   0        0        0      477 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/xmcd/__init__.py
+-rw-rw-rw-   0        0        0    13013 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/image/xmcd/xmcd.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.914859 spsdk-1.9.1/spsdk/mboot/
+-rw-rw-rw-   0        0        0     1043 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/mboot/__init__.py
+-rw-rw-rw-   0        0        0    19924 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/mboot/commands.py
+-rw-rw-rw-   0        0        0    27139 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/mboot/error_codes.py
+-rw-rw-rw-   0        0        0     1650 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/mboot/exceptions.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.930483 spsdk-1.9.1/spsdk/mboot/interfaces/
+-rw-rw-rw-   0        0        0      477 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/mboot/interfaces/__init__.py
+-rw-rw-rw-   0        0        0     1556 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/mboot/interfaces/base.py
+-rw-rw-rw-   0        0        0     6894 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/mboot/interfaces/buspal.py
+-rw-rw-rw-   0        0        0     5383 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/mboot/interfaces/buspal_i2c.py
+-rw-rw-rw-   0        0        0     6740 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/mboot/interfaces/buspal_spi.py
+-rw-rw-rw-   0        0        0    17912 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/mboot/interfaces/uart.py
+-rw-rw-rw-   0        0        0    11049 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/mboot/interfaces/usb.py
+-rw-rw-rw-   0        0        0    17059 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/mboot/interfaces/usbsio.py
+-rw-rw-rw-   0        0        0    60779 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/mboot/mcuboot.py
+-rw-rw-rw-   0        0        0     6999 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/mboot/memories.py
+-rw-rw-rw-   0        0        0    30075 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/mboot/properties.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.946109 spsdk-1.9.1/spsdk/pfr/
+-rw-rw-rw-   0        0        0      595 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/pfr/__init__.py
+-rw-rw-rw-   0        0        0      684 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/pfr/exceptions.py
+-rw-rw-rw-   0        0        0    23603 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/pfr/pfr.py
+-rw-rw-rw-   0        0        0     6075 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/pfr/pfrc.py
+-rw-rw-rw-   0        0        0     3075 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/pfr/processor.py
+-rw-rw-rw-   0        0        0     2991 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/pfr/translator.py
+-rw-rw-rw-   0        0        0        0 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/py.typed
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.946109 spsdk-1.9.1/spsdk/sbfile/
+-rw-rw-rw-   0        0        0      159 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/__init__.py
+-rw-rw-rw-   0        0        0     7129 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/misc.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.961732 spsdk-1.9.1/spsdk/sbfile/sb1/
+-rw-rw-rw-   0        0        0      913 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb1/__init__.py
+-rw-rw-rw-   0        0        0     1477 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb1/commands.py
+-rw-rw-rw-   0        0        0    16704 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb1/headers.py
+-rw-rw-rw-   0        0        0     9856 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb1/images.py
+-rw-rw-rw-   0        0        0     4800 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb1/sections.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.992983 spsdk-1.9.1/spsdk/sbfile/sb2/
+-rw-rw-rw-   0        0        0      171 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb2/__init__.py
+-rw-rw-rw-   0        0        0    36713 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb2/commands.py
+-rw-rw-rw-   0        0        0     9104 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb2/headers.py
+-rw-rw-rw-   0        0        0    42448 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb2/images.py
+-rw-rw-rw-   0        0        0    14085 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb2/sb_21_helper.py
+-rw-rw-rw-   0        0        0    15895 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb2/sections.py
+-rw-rw-rw-   0        0        0    11197 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb2/sly_bd_lexer.py
+-rw-rw-rw-   0        0        0    60550 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb2/sly_bd_parser.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.999504 spsdk-1.9.1/spsdk/sbfile/sb31/
+-rw-rw-rw-   0        0        0      852 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb31/__init__.py
+-rw-rw-rw-   0        0        0    39242 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb31/commands.py
+-rw-rw-rw-   0        0        0     1062 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb31/constants.py
+-rw-rw-rw-   0        0        0     6213 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb31/functions.py
+-rw-rw-rw-   0        0        0    26829 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sbfile/sb31/images.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:38.015161 spsdk-1.9.1/spsdk/sdp/
+-rw-rw-rw-   0        0        0      673 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sdp/__init__.py
+-rw-rw-rw-   0        0        0     4471 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sdp/commands.py
+-rw-rw-rw-   0        0        0     3997 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sdp/error_codes.py
+-rw-rw-rw-   0        0        0     1476 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sdp/exceptions.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:38.030788 spsdk-1.9.1/spsdk/sdp/interfaces/
+-rw-rw-rw-   0        0        0      359 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sdp/interfaces/__init__.py
+-rw-rw-rw-   0        0        0     1185 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sdp/interfaces/base.py
+-rw-rw-rw-   0        0        0     6880 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sdp/interfaces/uart.py
+-rw-rw-rw-   0        0        0    10208 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sdp/interfaces/usb.py
+-rw-rw-rw-   0        0        0    15667 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sdp/sdp.py
+-rw-rw-rw-   0        0        0     3526 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/sdp/sdps.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:38.030788 spsdk-1.9.1/spsdk/shadowregs/
+-rw-rw-rw-   0        0        0      237 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/shadowregs/__init__.py
+-rw-rw-rw-   0        0        0    18112 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/shadowregs/shadowregs.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:38.046425 spsdk-1.9.1/spsdk/tp/
+-rw-rw-rw-   0        0        0      773 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/tp/__init__.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:38.062035 spsdk-1.9.1/spsdk/tp/adapters/
+-rw-rw-rw-   0        0        0     1024 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/tp/adapters/__init__.py
+-rw-rw-rw-   0        0        0    12296 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/tp/adapters/scard_commands.py
+-rw-rw-rw-   0        0        0     6649 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/tp/adapters/scard_utils.py
+-rw-rw-rw-   0        0        0    21907 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/tp/adapters/tpdev_scard.py
+-rw-rw-rw-   0        0        0    14846 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/tp/adapters/tptarget_blhost.py
+-rw-rw-rw-   0        0        0     3567 2023-03-27 13:15:20.000000 spsdk-1.9.1/spsdk/tp/adapters/utils.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:38.077660 spsdk-1.9.1/spsdk/tp/data_container/
+-rw-rw-rw-   0        0        0      493 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/tp/data_container/__init__.py
+-rw-rw-rw-   0        0        0    12445 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/tp/data_container/audit_log.py
+-rw-rw-rw-   0        0        0    16529 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/tp/data_container/data_container.py
+-rw-rw-rw-   0        0        0     7194 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/tp/data_container/data_container_auth.py
+-rw-rw-rw-   0        0        0     2587 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/tp/data_container/payload_types.py
+-rw-rw-rw-   0        0        0      523 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/tp/exceptions.py
+-rw-rw-rw-   0        0        0     9760 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/tp/tp_intf.py
+-rw-rw-rw-   0        0        0     4109 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/tp/tpconfig.py
+-rw-rw-rw-   0        0        0    27484 2023-03-27 13:15:20.000000 spsdk-1.9.1/spsdk/tp/tphost.py
+-rw-rw-rw-   0        0        0     5900 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/tp/utils.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:38.115457 spsdk-1.9.1/spsdk/utils/
+-rw-rw-rw-   0        0        0      590 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/__init__.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:38.146722 spsdk-1.9.1/spsdk/utils/crypto/
+-rw-rw-rw-   0        0        0     1338 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/crypto/__init__.py
+-rw-rw-rw-   0        0        0     7703 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/crypto/abstract.py
+-rw-rw-rw-   0        0        0    15719 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/crypto/backend_internal.py
+-rw-rw-rw-   0        0        0    15108 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/crypto/backend_openssl.py
+-rw-rw-rw-   0        0        0    36549 2023-03-27 13:15:20.000000 spsdk-1.9.1/spsdk/utils/crypto/cert_blocks.py
+-rw-rw-rw-   0        0        0     7944 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/crypto/certificate.py
+-rw-rw-rw-   0        0        0     4946 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/crypto/common.py
+-rw-rw-rw-   0        0        0    29310 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/crypto/iee.py
+-rw-rw-rw-   0        0        0    36560 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/crypto/otfad.py
+-rw-rw-rw-   0        0        0     7370 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/crypto/rkht.py
+-rw-rw-rw-   0        0        0     7995 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/database.py
+-rw-rw-rw-   0        0        0     7368 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/devicedescription.py
+-rw-rw-rw-   0        0        0     6147 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/easy_enum.py
+-rw-rw-rw-   0        0        0     2086 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/easy_enum.pyi
+-rw-rw-rw-   0        0        0      782 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/exceptions.py
+-rw-rw-rw-   0        0        0    20976 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/images.py
+-rw-rw-rw-   0        0        0    28210 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/misc.py
+-rw-rw-rw-   0        0        0     5662 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/nxpdevscan.py
+-rw-rw-rw-   0        0        0     5583 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/reg_config.py
+-rw-rw-rw-   0        0        0    53575 2023-03-27 13:15:20.000000 spsdk-1.9.1/spsdk/utils/registers.py
+-rw-rw-rw-   0        0        0    20425 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/schema_validator.py
+-rw-rw-rw-   0        0        0     3890 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/serial_buspal_proxy.py
+-rw-rw-rw-   0        0        0     4656 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/serial_proxy.py
+-rw-rw-rw-   0        0        0    12381 2023-03-27 13:10:54.000000 spsdk-1.9.1/spsdk/utils/usbfilter.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:37.413400 spsdk-1.9.1/spsdk.egg-info/
+-rw-rw-rw-   0        0        0     6136 2023-03-27 14:07:36.000000 spsdk-1.9.1/spsdk.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     9130 2023-03-27 14:07:37.000000 spsdk-1.9.1/spsdk.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-27 14:07:36.000000 spsdk-1.9.1/spsdk.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      708 2023-03-27 14:07:36.000000 spsdk-1.9.1/spsdk.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0      589 2023-03-27 14:07:36.000000 spsdk-1.9.1/spsdk.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       12 2023-03-27 14:07:36.000000 spsdk-1.9.1/spsdk.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:38.146722 spsdk-1.9.1/tests/
+-rw-rw-rw-   0        0        0      174 2023-03-27 13:10:56.000000 spsdk-1.9.1/tests/test_self.py
+drwxrwxrwx   0        0        0        0 2023-03-27 14:07:38.200108 spsdk-1.9.1/tools/
+-rw-rw-rw-   0        0        0      122 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/__init__.py
+-rw-rw-rw-   0        0        0     1852 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/checker_copyright_year.py
+-rw-rw-rw-   0        0        0    12467 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/checker_dependencies.py
+-rw-rw-rw-   0        0        0     3821 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/checker_mypy_annotations.py
+-rw-rw-rw-   0        0        0     2942 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/checker_pydocstyle.py
+-rw-rw-rw-   0        0        0     3841 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/clr.py
+-rw-rw-rw-   0        0        0     7399 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/fcb_header_to_xml.py
+-rw-rw-rw-   0        0        0     3965 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/flashloader_converter.py
+-rw-rw-rw-   0        0        0     1794 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/git_operations.py
+-rw-rw-rw-   0        0        0    17631 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/gitcov.py
+-rw-rw-rw-   0        0        0     9174 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/release_notes.py
+-rw-rw-rw-   0        0        0    13987 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/req_update.py
+-rw-rw-rw-   0        0        0    21451 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/sr_xls2xml.py
+-rw-rw-rw-   0        0        0    11051 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/task_scheduler.py
+-rw-rw-rw-   0        0        0     1996 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/tp_migrate_audit_log.py
+-rw-rw-rw-   0        0        0    13876 2023-03-27 13:10:56.000000 spsdk-1.9.1/tools/tp_setup_workspace.py
```

### Comparing `spsdk-1.9.0/LICENSE` & `spsdk-1.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/PKG-INFO` & `spsdk-1.9.1/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,68 +1,18 @@
 Metadata-Version: 2.1
 Name: spsdk
-Version: 1.9.0
+Version: 1.9.1
 Summary: Open Source Secure Provisioning SDK for NXP MCU/MPU
 Home-page: https://github.com/NXPmicro/spsdk
 Author: NXP
 Author-email: michal.starecek@nxp.com
 License: BSD-3-Clause
 Project-URL: Code, https://github.com/NXPmicro/spsdk
 Project-URL: Issue tracker, https://github.com/NXPmicro/spsdk/issues
 Project-URL: Documentation, https://spsdk.readthedocs.io
-Description: # NXP Secure Provisioning SDK
-        
-        **Secure Provisioning SDK (SPSDK)** enables connection and communication with target devices for purposes of secure provisioning and programming. Delivered as python library with command-line applications for direct utilization.
-        
-        ![](https://github.com/NXPmicro/spsdk/raw/master/docs/_static/images/spsdk-architecture.png)
-        
-        * [PyPi](https://pypi.org/project/spsdk/)
-        * [Documentation](https://spsdk.readthedocs.io)
-        * [Project page](https://www.nxp.com/design/software/development-software/secure-provisioning-sdk-spsdk:SPSDK)
-        
-        ## Supported Devices
-        
-        Following NXP devices are supported:
-        
-        - LPC55 [S6x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/high-efficiency-arm-cortex-m33-based-microcontroller-family:LPC55S6x) / [S3x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33:LPC5500_SERIES) / [S2x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc552x-s2x-mainstream-arm-cortex-m33-based-microcontroller-family:LPC552x-S2x) / [S1x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc551x-s1x-baseline-arm-cortex-m33-based-microcontroller-family:LPC551X-S1X) / [S0x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc550x-s0x-baseline-arm-cortex-m33-based-microcontroller-family:LPC550x)
-        - i.MX RT [600](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt600-crossover-mcu-with-arm-cortex-m33-and-dsp-cores:i.MX-RT600) / [500](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt500-crossover-mcu-with-arm-cortex-m33-core:i.MX-RT500)
-        - i.MX RT [1064](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1064-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1064) / [1060](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1060-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1060) / [1050](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1050-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1050) / [1020](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1020-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1020) / [1010](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1010-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1010)
-        - i.MX RT [1170](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1170-crossover-mcu-family-first-ghz-mcu-with-arm-cortex-m7-and-cortex-m4-cores:i.MX-RT1170) / [1160](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx-rt1160-evaluation-kit:MIMXRT1160-EVK)
-        - KW45 [KW45](https://www.nxp.com/products/wireless/bluetooth-low-energy/32-bit-bluetooth-5-3-long-range-mcus-with-can-fd-and-lin-bus-options-arm-cortex-m33-core:KW45)
-        - K32W1 [K32W1](https://www.nxp.com/products/wireless/multiprotocol-mcus/tri-core-secure-and-ultra-low-power-mcu-for-matter-over-thread-and-bluetooth-le-5-3:K32W148)
-        
-        ## Supported environments
-        
-        - Windows 10, 64bit
-        - Ubuntu 18.04 or above, 64bit
-        - Mac OS 10.15 or above, x64, ARM64
-        
-        ## Usage
-        
-        - See [installation](https://spsdk.readthedocs.io/en/latest/usage/installation.html) guide
-        - See [examples](https://github.com/nxp-mcuxpresso/spsdk/tree/master/examples) directory
-        - See [application](https://github.com/nxp-mcuxpresso/spsdk/tree/master/spsdk/apps) directory
-        
-        ---
-        **i.Mx RT 1050**
-        
-        To run examples using i.MX RT 1050 you need to download a flashloader:
-        - Go to: https://www.nxp.com/webapp/sps/download/license.jsp?colCode=IMX-RT1050-FLASHLOADER
-        - Review the license agreement, download and unzip the package
-        - Convert the elf file into bin (For this operation you need to have MCUXpresso IDE, IAR or Keil)
-          - run ```python tools\flashloader_converter.py --elf-path <path/to/flashloader.elf> --ide-type <mcux | iar | keil> --ide-path <path/to/IDE/install/folder```
-        
-        ---
-        
-        ## Dependencies
-        
-        The core dependencies are included in [requirements.txt](https://github.com/nxp-mcuxpresso/spsdk/blob/master/requirements.txt).
-        
-        The dependencies for the development and testing are included in [requirements-develop.txt](https://github.com/nxp-mcuxpresso/spsdk/blob/master/requirements-develop.txt).
-        
 Platform: Windows
 Platform: Linux
 Platform: Mac OSX
 Classifier: Development Status :: 3 - Alpha
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
@@ -76,7 +26,58 @@
 Classifier: Topic :: Scientific/Engineering
 Classifier: Topic :: Software Development :: Embedded Systems
 Classifier: Topic :: System :: Hardware
 Classifier: Topic :: Utilities
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 Provides-Extra: tp
+License-File: LICENSE
+
+# NXP Secure Provisioning SDK
+
+**Secure Provisioning SDK (SPSDK)** enables connection and communication with target devices for purposes of secure provisioning and programming. Delivered as python library with command-line applications for direct utilization.
+
+![](https://github.com/NXPmicro/spsdk/raw/master/docs/_static/images/spsdk-architecture.png)
+
+* [PyPi](https://pypi.org/project/spsdk/)
+* [Documentation](https://spsdk.readthedocs.io)
+* [Project page](https://www.nxp.com/design/software/development-software/secure-provisioning-sdk-spsdk:SPSDK)
+
+## Supported Devices
+
+Following NXP devices are supported:
+
+- LPC55 [S6x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/high-efficiency-arm-cortex-m33-based-microcontroller-family:LPC55S6x) / [S3x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33:LPC5500_SERIES) / [S2x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc552x-s2x-mainstream-arm-cortex-m33-based-microcontroller-family:LPC552x-S2x) / [S1x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc551x-s1x-baseline-arm-cortex-m33-based-microcontroller-family:LPC551X-S1X) / [S0x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc550x-s0x-baseline-arm-cortex-m33-based-microcontroller-family:LPC550x)
+- i.MX RT [600](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt600-crossover-mcu-with-arm-cortex-m33-and-dsp-cores:i.MX-RT600) / [500](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt500-crossover-mcu-with-arm-cortex-m33-core:i.MX-RT500)
+- i.MX RT [1064](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1064-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1064) / [1060](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1060-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1060) / [1050](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1050-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1050) / [1020](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1020-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1020) / [1010](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1010-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1010)
+- i.MX RT [1170](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1170-crossover-mcu-family-first-ghz-mcu-with-arm-cortex-m7-and-cortex-m4-cores:i.MX-RT1170) / [1160](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx-rt1160-evaluation-kit:MIMXRT1160-EVK)
+- [KW45](https://www.nxp.com/products/wireless/bluetooth-low-energy/32-bit-bluetooth-5-3-long-range-mcus-with-can-fd-and-lin-bus-options-arm-cortex-m33-core:KW45)
+- [K32W1](https://www.nxp.com/products/wireless/multiprotocol-mcus/tri-core-secure-and-ultra-low-power-mcu-for-matter-over-thread-and-bluetooth-le-5-3:K32W148)
+
+## Supported environments
+
+- Windows 10, 64bit
+- Ubuntu 18.04 or above, 64bit
+- Mac OS 10.15 or above, x64, ARM64
+
+## Usage
+
+- See [installation](https://spsdk.readthedocs.io/en/latest/usage/installation.html) guide
+- See [examples](https://github.com/nxp-mcuxpresso/spsdk/tree/master/examples) directory
+- See [application](https://github.com/nxp-mcuxpresso/spsdk/tree/master/spsdk/apps) directory
+
+---
+**i.Mx RT 1050**
+
+To run examples using i.MX RT 1050 you need to download a flashloader:
+- Go to: https://www.nxp.com/webapp/sps/download/license.jsp?colCode=IMX-RT1050-FLASHLOADER
+- Review the license agreement, download and unzip the package
+- Convert the elf file into bin (For this operation you need to have MCUXpresso IDE, IAR or Keil)
+  - run ```python tools\flashloader_converter.py --elf-path <path/to/flashloader.elf> --ide-type <mcux | iar | keil> --ide-path <path/to/IDE/install/folder```
+
+---
+
+## Dependencies
+
+The core dependencies are included in [requirements.txt](https://github.com/nxp-mcuxpresso/spsdk/blob/master/requirements.txt).
+
+The dependencies for the development and testing are included in [requirements-develop.txt](https://github.com/nxp-mcuxpresso/spsdk/blob/master/requirements-develop.txt).
```

### Comparing `spsdk-1.9.0/README.md` & `spsdk-1.9.1/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -12,16 +12,16 @@
 
 Following NXP devices are supported:
 
 - LPC55 [S6x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/high-efficiency-arm-cortex-m33-based-microcontroller-family:LPC55S6x) / [S3x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33:LPC5500_SERIES) / [S2x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc552x-s2x-mainstream-arm-cortex-m33-based-microcontroller-family:LPC552x-S2x) / [S1x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc551x-s1x-baseline-arm-cortex-m33-based-microcontroller-family:LPC551X-S1X) / [S0x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc550x-s0x-baseline-arm-cortex-m33-based-microcontroller-family:LPC550x)
 - i.MX RT [600](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt600-crossover-mcu-with-arm-cortex-m33-and-dsp-cores:i.MX-RT600) / [500](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt500-crossover-mcu-with-arm-cortex-m33-core:i.MX-RT500)
 - i.MX RT [1064](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1064-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1064) / [1060](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1060-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1060) / [1050](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1050-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1050) / [1020](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1020-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1020) / [1010](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1010-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1010)
 - i.MX RT [1170](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1170-crossover-mcu-family-first-ghz-mcu-with-arm-cortex-m7-and-cortex-m4-cores:i.MX-RT1170) / [1160](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx-rt1160-evaluation-kit:MIMXRT1160-EVK)
-- KW45 [KW45](https://www.nxp.com/products/wireless/bluetooth-low-energy/32-bit-bluetooth-5-3-long-range-mcus-with-can-fd-and-lin-bus-options-arm-cortex-m33-core:KW45)
-- K32W1 [K32W1](https://www.nxp.com/products/wireless/multiprotocol-mcus/tri-core-secure-and-ultra-low-power-mcu-for-matter-over-thread-and-bluetooth-le-5-3:K32W148)
+- [KW45](https://www.nxp.com/products/wireless/bluetooth-low-energy/32-bit-bluetooth-5-3-long-range-mcus-with-can-fd-and-lin-bus-options-arm-cortex-m33-core:KW45)
+- [K32W1](https://www.nxp.com/products/wireless/multiprotocol-mcus/tri-core-secure-and-ultra-low-power-mcu-for-matter-over-thread-and-bluetooth-le-5-3:K32W148)
 
 ## Supported environments
 
 - Windows 10, 64bit
 - Ubuntu 18.04 or above, 64bit
 - Mac OS 10.15 or above, x64, ARM64
```

### Comparing `spsdk-1.9.0/SW_Content_Register_SPSDK.txt` & `spsdk-1.9.1/SW_Content_Register_SPSDK.txt`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 NXP Software Content Register
 
 Package:                   NXP SPSDK
-Version:                   1.9.0
+Version:                   1.9.1
 Outgoing License:          BSD-3-Clause
 License Files:             LICENSE
 Type of content:           Source code
 Description and comments:  NXP Secure Provisioning SDK
 Origin:                    NXP (BSD-3-Clause)
 
 PyIMX               Name: PyIMX
```

### Comparing `spsdk-1.9.0/pyproject.toml` & `spsdk-1.9.1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/requirements-develop.txt` & `spsdk-1.9.1/requirements-develop.txt`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/requirements.txt` & `spsdk-1.9.1/requirements.txt`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 asn1crypto>=1.2,<1.6
 astunparse>=1.6,<1.7
-bincopy>=17.10.2,<17.15
+bincopy>=17.10.2,<=17.14.0
 bitstring>=3.1,<4.1
 click-option-group>=0.3.0,<0.6
 click-command-tree<1.2
 click>=7.1,<8.2
 colorama>=0.4.6,<0.5
 commentjson>=0.9,<0.10
 crcmod<1.8
@@ -13,17 +13,17 @@
 fastjsonschema>=2.15.1,<2.17
 hexdump<3.4
 jinja2>=3.0,<3.2
 libusbsio>=2.1.11,<2.2
 oscrypto<1.4
 pycryptodome>=3.9.3,<3.17
 pylink-square>=0.8.2,<0.15
-pyocd-pemicro>=1.1.1,<1.2
+pyocd-pemicro>=1.1.5,<1.2
 pyocd>=0.28.3,<0.32
-pypemicro>=0.1.9,<0.2
+pypemicro>=0.1.11,<0.2
 pyserial>=3.1,<3.6
 ruamel.yaml>=0.17,<0.18
 sly<0.6
 # There's an issue with 0.3.0 on win
 # https://github.com/pyocd/cmsis-pack-manager/issues/176
 cmsis-pack-manager<0.3.0
 typing-extensions<4.5
```

### Comparing `spsdk-1.9.0/setup.py` & `spsdk-1.9.1/setup.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/__init__.py` & `spsdk-1.9.1/spsdk/__init__.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/blhost.py` & `spsdk-1.9.1/spsdk/apps/blhost.py`

 * *Files 0% similar despite different names*

```diff
@@ -1511,15 +1511,17 @@
     """
     with McuBoot(ctx.obj["interface"]) as mboot:
         tp_response_length = mboot.tp_prove_genuinity(address=address, buffer_size=buffer_size)
         display_output(
             [tp_response_length],
             mboot.status_code,
             use_json=ctx.obj["use_json"],
-            extra_output=f"TP response will be {tp_response_length} bytes long.",
+            extra_output=f"TP response will be {tp_response_length} bytes long."
+            if tp_response_length
+            else None,
         )
 
 
 @trust_provisioning.command(name="isp_set_wrap_data")
 @click.argument("address", type=INT())
 @click.argument("control", type=INT(), required=False, default=0x1)
 @click.argument("stage", type=INT(), required=False, default=0x4B)
```

### Comparing `spsdk-1.9.0/spsdk/apps/blhost_helper.py` & `spsdk-1.9.1/spsdk/apps/blhost_helper.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/elftosb.py` & `spsdk-1.9.1/spsdk/apps/elftosb.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/elftosb_utils/sb_31_helper.py` & `spsdk-1.9.1/spsdk/apps/elftosb_utils/sb_31_helper.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/ifr.py` & `spsdk-1.9.1/spsdk/apps/ifr.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/nxpcertgen.py` & `spsdk-1.9.1/spsdk/apps/nxpcertgen.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/nxpcrypto.py` & `spsdk-1.9.1/spsdk/apps/nxpcrypto.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/nxpdebugmbox.py` & `spsdk-1.9.1/spsdk/apps/nxpdebugmbox.py`

 * *Files 0% similar despite different names*

```diff
@@ -9,14 +9,15 @@
 
 import contextlib
 import logging
 import os
 import struct
 import sys
 from dataclasses import dataclass
+from time import sleep
 from typing import Callable, Iterator, List, Optional
 
 import click
 import colorama
 
 from spsdk import SPSDK_DATA_FOLDER, SPSDKError
 from spsdk.apps.blhost_helper import progress_bar
@@ -313,14 +314,15 @@
             if not no_exit:
                 exit_response = dm_commands.ExitDebugMailbox(dm=mail_box).run()
                 logger.debug(f"Exit response: {exit_response}")
                 # Re-open debug probe
                 mail_box.debug_probe.close()
                 mail_box.debug_probe.open()
                 # Do test of access to AHB bus
+                sleep(0.2)
                 ahb_access_granted = test_ahb_access(mail_box.debug_probe)
                 res_str = (
                     (colorama.Fore.GREEN + "successfully")
                     if ahb_access_granted
                     else (colorama.Fore.RED + "without AHB access")
                 )
                 logger.info(f"Debug Authentication ends {res_str}{colorama.Fore.RESET}.")
```

### Comparing `spsdk-1.9.0/spsdk/apps/nxpdevhsm.py` & `spsdk-1.9.1/spsdk/apps/nxpdevhsm.py`

 * *Files 8% similar despite different names*

```diff
@@ -39,15 +39,15 @@
 NXPDEVHSM_DATA_FOLDER: str = os.path.join(SPSDK_DATA_FOLDER, "nxpdevhsm")
 NXPDEVHSM_DATABASE_FILE: str = os.path.join(NXPDEVHSM_DATA_FOLDER, "database.yaml")
 
 
 class DeviceHsm:
     """Class to handle device HSM provisioning procedure."""
 
-    DEVBUFF_BASE = 0x20007000
+    DEVBUFF_BASE = 0x20008000
     DEVBUFF_SIZE = 0x100
 
     DEVBUFF_BASE0 = DEVBUFF_BASE
     DEVBUFF_BASE1 = DEVBUFF_BASE0 + DEVBUFF_SIZE
     DEVBUFF_BASE2 = DEVBUFF_BASE1 + DEVBUFF_SIZE
     DEVBUFF_BASE3 = DEVBUFF_BASE2 + DEVBUFF_SIZE
 
@@ -69,34 +69,37 @@
         mboot: McuBoot,
         user_pck: bytes,
         oem_share_input: bytes,
         info_print: Callable,
         family: str,
         container_conf: Optional[str] = None,
         workspace: Optional[str] = None,
-        reset: bool = True,
+        initial_reset: bool = False,
+        final_reset: bool = True,
     ) -> None:
         """Initialization of device HSM class. Its design to create provisioned SB3 file.
 
         :param mboot: mBoot communication interface.
         :param oem_share_input: OEM share input data.
         :param user_pck: USER PCK key.
         :param family: chip family
         :param container_conf: Optional elftosb configuration file (to specify user list of SB commands).
         :param workspace: Optional folder to store middle results.
-        :param reset: Reset device before and after DevHSM creation of SB3 file.
+        :param initial_reset: Reset device before DevHSM creation of SB3 file.
+        :param final_reset: Reset device after DevHSM creation of SB3 file.
         :raises SPSDKError: In case of any vulnerability.
         """
         self.database = Database(NXPDEVHSM_DATABASE_FILE)
         self.mboot = mboot
         self.user_pck = user_pck
         self.oem_share_input = oem_share_input
         self.info_print = info_print
         self.workspace = workspace
-        self.reset = reset
+        self.initial_reset = initial_reset
+        self.final_reset = final_reset
         self.container_conf_dir = os.path.dirname(container_conf) if container_conf else None
         if self.workspace and not os.path.isdir(self.workspace):
             os.mkdir(self.workspace)
 
         # store input of OEM_SHARE_INPUT to workspace in case that is generated randomly
         self.store_temp_res("OEM_SHARE_INPUT.BIN", self.oem_share_input)
 
@@ -146,15 +149,15 @@
         ret.extend([mbi_sch_cfg["firmware_version"]])
         ret.extend([sb3_sch_cfg[x] for x in ["sb3_description", "sb3_commands", "sb3_test"]])
         return ret
 
     def create_sb3(self) -> None:
         """Do device hsm process to create SB_KEK provisioning SB file."""
         # 1: Initial target reset to ensure OEM_MASTER_SHARE works properly (not tainted by previous run)
-        if self.reset:
+        if self.initial_reset:
             self.info_print(" 1: Resetting the target device")
             self.mboot.reset(timeout=self.RESET_TIMEOUT)
         else:
             self.info_print(" 1: Initial target reset is disabled ")
 
         # 2: Call GEN_OEM_MASTER_SHARE to generate encOemShare.bin (ENC_OEM_SHARE will be later put in place of ISK)
         self.info_print(" 2: Generating OEM master share.")
@@ -280,17 +283,17 @@
         self.final_sb += enc_final_data
         self.store_temp_res("Final_SB3.sb3", self.final_sb)
         logger.debug(
             f" 9: The final SB3 file data:\n{format_raw_data(self.final_sb, use_hexdump=True)}."
         )
 
         # 10: Final reset to ensure followup operations (e.g. receive-sb-file) work correctly
-        if self.reset:
+        if self.final_reset:
             self.info_print("10: Resetting the target device")
-            self.mboot.reset(timeout=self.RESET_TIMEOUT)
+            self.mboot.reset(timeout=self.RESET_TIMEOUT, reopen=False)
         else:
             self.info_print("10: Final target reset disabled")
 
     def export(self) -> bytes:
         """Get the Final SB file.
 
         :return: Final SB file in bytes.
@@ -301,62 +304,70 @@
         """Generate on device Encrypted OEM master share outputs.
 
         :param oem_share_input: OEM input (randomize seed)
         :raises SPSDKError: In case of any vulnerability.
         :return: Tuple with OEM generate master share outputs.
         """
         if not self.mboot.write_memory(self.DEVBUFF_BASE0, oem_share_input):
-            raise SPSDKError("Cannot write OEM SHARE INPUT into device.")
+            raise SPSDKError(
+                f"Cannot write OEM SHARE INPUT into device. Error: {self.mboot.status_string}"
+            )
 
         oem_gen_master_share_res = self.mboot.tp_oem_gen_master_share(
             self.DEVBUFF_BASE0,
             self.DEVBUFF_GEN_MASTER_SHARE_INPUT_SIZE,
             self.DEVBUFF_BASE1,
             self.DEVBUFF_SIZE,
             self.DEVBUFF_BASE2,
             self.DEVBUFF_SIZE,
             self.DEVBUFF_BASE3,
             self.DEVBUFF_SIZE,
         )
 
         if not oem_gen_master_share_res:
             raise SPSDKError(
-                "OEM generate master share command failed,"
-                " device probably needs reset due to doubled call of this command."
+                f"OEM generate master share command failed. Error: {self.mboot.status_string}\n"
+                "Device probably needs reset due to doubled call of this command."
             )
 
         if (
             oem_gen_master_share_res[0] != self.DEVBUFF_GEN_MASTER_ENC_SHARE_OUTPUT_SIZE
             and oem_gen_master_share_res[1] != self.DEVBUFF_GEN_MASTER_ENC_MASTER_SHARE_OUTPUT_SIZE
             and oem_gen_master_share_res[2] != self.DEVBUFF_GEN_MASTER_CUST_CERT_PUK_OUTPUT_SIZE
         ):
             raise SPSDKError("OEM generate master share command has invalid results.")
 
         oem_enc_share = self.mboot.read_memory(
             self.DEVBUFF_BASE1,
             self.DEVBUFF_GEN_MASTER_ENC_SHARE_OUTPUT_SIZE,
         )
         if not oem_enc_share:
-            raise SPSDKError("Cannot read OEM ENCRYPTED SHARE OUTPUT from device.")
+            raise SPSDKError(
+                f"Cannot read OEM ENCRYPTED SHARE OUTPUT from device. Error: {self.mboot.status_string}"
+            )
         self.store_temp_res("ENC_OEM_SHARE.bin", oem_enc_share)
 
         oem_enc_master_share = self.mboot.read_memory(
             self.DEVBUFF_BASE2,
             self.DEVBUFF_GEN_MASTER_ENC_MASTER_SHARE_OUTPUT_SIZE,
         )
         if not oem_enc_master_share:
-            raise SPSDKError("Cannot read OEM ENCRYPTED MASTER SHARE OUTPUT from device.")
+            raise SPSDKError(
+                f"Cannot read OEM ENCRYPTED MASTER SHARE OUTPUT from device. Error: {self.mboot.status_string}"
+            )
         self.store_temp_res("ENC_OEM_MASTER_SHARE.bin", oem_enc_master_share)
 
         oem_cert = self.mboot.read_memory(
             self.DEVBUFF_BASE3,
             self.DEVBUFF_GEN_MASTER_CUST_CERT_PUK_OUTPUT_SIZE,
         )
         if not oem_cert:
-            raise SPSDKError("Cannot read OEM CERTIFICATE from device.")
+            raise SPSDKError(
+                f"Cannot read OEM CERTIFICATE from device. Error: {self.mboot.status_string}"
+            )
         self.store_temp_res("OEM_CERT.bin", oem_cert)
 
         return oem_enc_share, oem_enc_master_share, oem_cert
 
     def generate_key(
         self, key_type: TrustProvOemKeyType, key_name: Optional[str] = None
     ) -> Tuple[bytes, bytes]:
@@ -373,107 +384,124 @@
             self.DEVBUFF_BASE0,
             self.DEVBUFF_SIZE,
             self.DEVBUFF_BASE1,
             self.DEVBUFF_SIZE,
         )
 
         if not hsm_gen_key_res:
-            raise SPSDKError("HSM generate key command failed.")
+            raise SPSDKError(f"HSM generate key command failed. Error: {self.mboot.status_string}")
 
         if (
             hsm_gen_key_res[0] != self.DEVBUFF_HSM_GENKEY_KEYBLOB_SIZE
             and hsm_gen_key_res[1] != self.DEVBUFF_HSM_GENKEY_KEYBLOB_PUK_SIZE
         ):
             raise SPSDKError("OEM generate master share command has invalid results.")
 
         prk = self.mboot.read_memory(
             self.DEVBUFF_BASE0,
             self.DEVBUFF_HSM_GENKEY_KEYBLOB_SIZE,
         )
         if not prk:
-            raise SPSDKError("Cannot read generated private key from device.")
+            raise SPSDKError(
+                f"Cannot read generated private key from device. Error: {self.mboot.status_string}"
+            )
 
         puk = self.mboot.read_memory(
             self.DEVBUFF_BASE1,
             self.DEVBUFF_HSM_GENKEY_KEYBLOB_PUK_SIZE,
         )
         if not puk:
-            raise SPSDKError("Cannot read generated public key from device.")
+            raise SPSDKError(
+                f"Cannot read generated public key from device. Error: {self.mboot.status_string}"
+            )
 
         self.store_temp_res((key_name or str(TrustProvOemKeyType[str(key_type)])) + "_PRK.bin", prk)
         self.store_temp_res((key_name or str(TrustProvOemKeyType[str(key_type)])) + "_PUK.bin", puk)
 
         return prk, puk
 
     def wrap_key(self, user_pck: bytes) -> bytes:
         """Wrap the user PCK key.
 
         :param user_pck: User PCK key
         :raises SPSDKError: In case of any vulnerability.
         :return: Wrapped user PCK by RFC3396.
         """
         if not self.mboot.write_memory(self.DEVBUFF_BASE0, user_pck):
-            raise SPSDKError("Cannot write USER_PCK into device.")
+            raise SPSDKError(
+                f"Cannot write USER_PCK into device. Error: {self.mboot.status_string}"
+            )
 
         hsm_store_key_res = self.mboot.tp_hsm_store_key(
             TrustProvKeyType.CKDFK,
             0x01,
             self.DEVBUFF_BASE0,
             self.DEVBUFF_USER_PCK_KEY_SIZE,
             self.DEVBUFF_BASE1,
             self.DEVBUFF_SIZE,
         )
 
         if not hsm_store_key_res:
-            raise SPSDKError("HSM Store Key command failed.")
+            raise SPSDKError(f"HSM Store Key command failed. Error: {self.mboot.status_string}")
 
         if hsm_store_key_res[1] != self.DEVBUFF_WRAPPED_USER_PCK_KEY_SIZE:
             raise SPSDKError("HSM Store Key command has invalid results.")
 
         wrapped_user_pck = self.mboot.read_memory(
             self.DEVBUFF_BASE1,
             self.DEVBUFF_WRAPPED_USER_PCK_KEY_SIZE,
         )
         if not wrapped_user_pck:
-            raise SPSDKError("Cannot read WRAPPED USER PCK from device.")
+            raise SPSDKError(
+                f"Cannot read WRAPPED USER PCK from device. Error: {self.mboot.status_string}"
+            )
 
         self.store_temp_res("CUST_MK_SK.bin", wrapped_user_pck)
 
         return wrapped_user_pck
 
     def sign_data_blob(self, data_to_sign: bytes, key: bytes) -> bytes:
         """Get HSM encryption sign for data blob.
 
         :param data_to_sign: Input data to sign.
         :param key: FW signing key (MFWISK).
         :raises SPSDKError: In case of any vulnerability.
         :return: Data blob signature (64 bytes).
         """
         if not self.mboot.write_memory(self.DEVBUFF_BASE0, key):
-            raise SPSDKError("Cannot write signing key into device.")
+            raise SPSDKError(
+                f"Cannot write signing key into device. Error: {self.mboot.status_string}"
+            )
         if not self.mboot.write_memory(self.DEVBUFF_BASE1, data_to_sign):
-            raise SPSDKError("Cannot write Data to sign into device.")
+            raise SPSDKError(
+                f"Cannot write Data to sign into device. Error: {self.mboot.status_string}"
+            )
         hsm_gen_key_res = self.mboot.tp_hsm_enc_sign(
             self.DEVBUFF_BASE0,
             len(key),
             self.DEVBUFF_BASE1,
             len(data_to_sign),
             self.DEVBUFF_BASE2,
             self.DEVBUFF_SB3_SIGNATURE_SIZE,
         )
 
         if hsm_gen_key_res != self.DEVBUFF_SB3_SIGNATURE_SIZE:
-            raise SPSDKError("HSM signing command failed.")
+            raise SPSDKError(
+                f"HSM signing command failed. Invalid signature size: {hsm_gen_key_res} "
+                f"MBoot Status: {self.mboot.status_string}"
+            )
 
         signature = self.mboot.read_memory(
             self.DEVBUFF_BASE2,
             self.DEVBUFF_SB3_SIGNATURE_SIZE,
         )
         if not signature:
-            raise SPSDKError("Cannot read generated signature from device.")
+            raise SPSDKError(
+                f"Cannot read generated signature from device. Error: {self.mboot.status_string}"
+            )
 
         self.store_temp_res("SB3_sign.bin", signature, "to_merge")
 
         return signature
 
     def store_temp_res(self, file_name: str, data: bytes, group: Optional[str] = None) -> None:
         """Storing temporary files into workspace.
@@ -521,47 +549,58 @@
         :param cust_fw_enc_key: Firmware encryption key.
         :param sb3_header: Un Encrypted SB3 file header.
         :param data_cmd_blocks: List of un-encrypted SB3 file command blocks.
         :raises SPSDKError: In case of any vulnerability.
         :return: List of encrypted command blocks on device.
         """
         if not self.mboot.write_memory(self.DEVBUFF_BASE0, cust_fw_enc_key):
-            raise SPSDKError("Cannot write customer fw encryption key into device.")
+            raise SPSDKError(
+                f"Cannot write customer fw encryption key into device. Error: {self.mboot.status_string}"
+            )
         self.store_temp_res("SB3_header.bin", sb3_header, "to_encrypt")
         if not self.mboot.write_memory(self.DEVBUFF_BASE1, sb3_header):
-            raise SPSDKError("Cannot write SB3 header into device.")
+            raise SPSDKError(
+                f"Cannot write SB3 header into device. Error: {self.mboot.status_string}"
+            )
 
         encrypted_blocks = []
         for data_cmd_block_ix, data_cmd_block in enumerate(data_cmd_blocks, start=1):
             self.store_temp_res(f"SB3_block_{data_cmd_block_ix}.bin", data_cmd_block, "to_encrypt")
             if not self.mboot.write_memory(self.DEVBUFF_BASE2, data_cmd_block):
-                raise SPSDKError(f"Cannot write SB3 data block{data_cmd_block_ix} into device.")
+                raise SPSDKError(
+                    f"Cannot write SB3 data block{data_cmd_block_ix} into device. "
+                    f"Error: {self.mboot.status_string}"
+                )
             key_id = CmdLoadKeyBlob.get_key_id(
                 self.family, CmdLoadKeyBlob.KeyTypes.NXP_CUST_KEK_INT_SK
             )
             if not self.mboot.tp_hsm_enc_blk(
                 self.DEVBUFF_BASE0,
                 len(cust_fw_enc_key),
                 key_id,
                 self.DEVBUFF_BASE1,
                 len(sb3_header),
                 data_cmd_block_ix,
                 self.DEVBUFF_BASE2,
                 self.DEVBUFF_DATA_BLOCK_SIZE,
             ):
                 raise SPSDKError(
-                    f"Cannot run SB3 data block_{data_cmd_block_ix} HSM Encryption in device."
+                    f"Cannot run SB3 data block_{data_cmd_block_ix} HSM Encryption in device. "
+                    f"Error: {self.mboot.status_string}"
                 )
 
             encrypted_block = self.mboot.read_memory(
                 self.DEVBUFF_BASE2,
                 self.DEVBUFF_DATA_BLOCK_SIZE,
             )
             if not encrypted_block:
-                raise SPSDKError(f"Cannot read SB3 data block_{data_cmd_block_ix} from device.")
+                raise SPSDKError(
+                    f"Cannot read SB3 data block_{data_cmd_block_ix} from device. "
+                    f"Error: {self.mboot.status_string}"
+                )
 
             self.store_temp_res(f"SB3_block_{data_cmd_block_ix}.bin", encrypted_block, "encrypted")
 
             encrypted_blocks.append(encrypted_block)
 
         return encrypted_blocks
 
@@ -646,33 +685,47 @@
     "-f",
     "--family",
     required=False,
     help="Select the chip family.",
     type=click.Choice(["lpc55s3x"], case_sensitive=False),
 )
 @click.option(
-    "-r/-R",
-    "--reset/--no-reset",
+    "-ir/-IR",
+    "--initial-reset/--no-init-reset",
+    default=False,
+    help=(
+        "Reset device BEFORE DevHSM operation. The DevHSM operation can run only once between resets. "
+        "Do not enable this option on Linux/Mac when using USB. By default this reset is DISABLED."
+    ),
+)
+@click.option(
+    "-fr/-FR",
+    "--final-reset/--no-final-reset",
     default=True,
-    help="Control resetting target before and after DevHSM operation. Reset is enabled by default.",
+    help=(
+        "Reset device AFTER DevHSM operation. This reset is required if you need to use the device "
+        "after DevHSM operation for other security related operations (e.g. receive-sb-file). "
+        "By default this reset is ENABLED."
+    ),
 )
 @click.argument("output-path", type=click.File(mode="wb"))
 def generate(
     port: str,
     usb: str,
     buspal: str,
     lpcusbsio: str,
     oem_share_input: BinaryIO,
     key: BinaryIO,
     output_path: BinaryIO,
     workspace: str,
     container_conf: str,
     timeout: int,
     family: str,
-    reset: bool,
+    initial_reset: bool,
+    final_reset: bool,
 ) -> None:
     """Generate provisioning SB3.1 file.
 
     \b
     PATH    - output file path, where the final provisioned SB file will be stored.
     """
     interface = get_interface(
@@ -702,15 +755,16 @@
             mboot=mboot,
             user_pck=user_pck,
             oem_share_input=oem_share_in,
             info_print=click.echo,
             container_conf=container_conf,
             workspace=workspace,
             family=family_final,
-            reset=reset,
+            initial_reset=initial_reset,
+            final_reset=final_reset,
         )
         devhsm.create_sb3()
         output_path.write(devhsm.export())
 
     click.echo(f"Final SB3 file has been written: {os.path.abspath(output_path.name)}")
```

### Comparing `spsdk-1.9.0/spsdk/apps/nxpdevscan.py` & `spsdk-1.9.1/spsdk/apps/nxpdevscan.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/nxpimage.py` & `spsdk-1.9.1/spsdk/apps/nxpimage.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/nxpkeygen.py` & `spsdk-1.9.1/spsdk/apps/nxpkeygen.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/pfr.py` & `spsdk-1.9.1/spsdk/apps/pfr.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/sdphost.py` & `spsdk-1.9.1/spsdk/apps/sdphost.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/sdpshost.py` & `spsdk-1.9.1/spsdk/apps/sdpshost.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/shadowregs.py` & `spsdk-1.9.1/spsdk/apps/shadowregs.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/spsdk_apps.py` & `spsdk-1.9.1/spsdk/apps/spsdk_apps.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/tp_utils.py` & `spsdk-1.9.1/spsdk/apps/tp_utils.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/tpconfig.py` & `spsdk-1.9.1/spsdk/apps/tpconfig.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/tphost.py` & `spsdk-1.9.1/spsdk/apps/tphost.py`

 * *Files 0% similar despite different names*

```diff
@@ -228,14 +228,15 @@
     )
     tp_worker.load_provisioning_fw(
         family=tp_config.family,
         prov_fw=tp_config.prov_firmware_data,
         timeout=tp_config.timeout,
         skip_test=skip_test,
         keep_target_open=False,
+        skip_usb_enumeration=skip_test,
     )
 
 
 @main.command(name="get-template", no_args_is_help=True)
 @click.option(
     "-f",
     "--family",
```

### Comparing `spsdk-1.9.0/spsdk/apps/utils/common_cli_options.py` & `spsdk-1.9.1/spsdk/apps/utils/common_cli_options.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/apps/utils/utils.py` & `spsdk-1.9.1/spsdk/apps/utils/utils.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/crypto/__init__.py` & `spsdk-1.9.1/spsdk/crypto/__init__.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/crypto/certificate_management.py` & `spsdk-1.9.1/spsdk/crypto/certificate_management.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/crypto/keys_management.py` & `spsdk-1.9.1/spsdk/crypto/keys_management.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/crypto/loaders.py` & `spsdk-1.9.1/spsdk/crypto/loaders.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/crypto/signature_provider.py` & `spsdk-1.9.1/spsdk/crypto/signature_provider.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/dat/dac_packet.py` & `spsdk-1.9.1/spsdk/dat/dac_packet.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/dat/dar_packet.py` & `spsdk-1.9.1/spsdk/dat/dar_packet.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/dat/debug_credential.py` & `spsdk-1.9.1/spsdk/dat/debug_credential.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/dat/debug_mailbox.py` & `spsdk-1.9.1/spsdk/dat/debug_mailbox.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/dat/dm_commands.py` & `spsdk-1.9.1/spsdk/dat/dm_commands.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/dat/utils.py` & `spsdk-1.9.1/spsdk/dat/utils.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/ahab/sch_ahab.yml` & `spsdk-1.9.1/spsdk/data/ahab/sch_ahab.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/ahab/sch_signed_msg.yml` & `spsdk-1.9.1/spsdk/data/ahab/sch_signed_msg.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/cpu_data/exec_hab_audit_rt1020.c` & `spsdk-1.9.1/spsdk/data/cpu_data/exec_hab_audit_rt1020.c`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/cpu_data/exec_hab_audit_rt1050.c` & `spsdk-1.9.1/spsdk/data/cpu_data/exec_hab_audit_rt1050.c`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/cpu_data/rt1020_exec_hab_audit.bin` & `spsdk-1.9.1/spsdk/data/cpu_data/rt1020_exec_hab_audit.bin`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/cpu_data/rt1050_exec_hab_audit.bin` & `spsdk-1.9.1/spsdk/data/cpu_data/rt1050_exec_hab_audit.bin`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/cpu_data/rt1060_exec_hab_audit.bin` & `spsdk-1.9.1/spsdk/data/cpu_data/rt1060_exec_hab_audit.bin`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/ifr/k32w1xx_a0.xml` & `spsdk-1.9.1/spsdk/data/ifr/k32w1xx_a0.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/ifr/k32w1xx_a1.xml` & `spsdk-1.9.1/spsdk/data/ifr/k32w1xx_a1.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/ifr/kw45xx_a0.xml` & `spsdk-1.9.1/spsdk/data/ifr/kw45xx_a0.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/ifr/kw45xx_a1.xml` & `spsdk-1.9.1/spsdk/data/ifr/kw45xx_a1.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/bootable_image/database.yml` & `spsdk-1.9.1/spsdk/data/image/bootable_image/database.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/bootable_image/sch_bimg.yml` & `spsdk-1.9.1/spsdk/data/image/bootable_image/sch_bimg.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/database.yml` & `spsdk-1.9.1/spsdk/data/image/database.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/fcb/database.yml` & `spsdk-1.9.1/spsdk/data/image/fcb/database.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/fcb/lpc55s3x_flexspi_nor.xml` & `spsdk-1.9.1/spsdk/data/image/fcb/lpc55s3x_flexspi_nor.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/fcb/rt105x_flexspi_nor.xml` & `spsdk-1.9.1/spsdk/data/image/fcb/rt105x_flexspi_nor.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/fcb/rt106x_flexspi_nor.xml` & `spsdk-1.9.1/spsdk/data/image/fcb/rt106x_flexspi_nor.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/fcb/rt117x_flexspi_nor.xml` & `spsdk-1.9.1/spsdk/data/image/fcb/rt117x_flexspi_nor.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/fcb/rt118x_flexspi_nor.xml` & `spsdk-1.9.1/spsdk/data/image/fcb/rt118x_flexspi_nor.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/fcb/rt5xx_flexspi_nor.xml` & `spsdk-1.9.1/spsdk/data/image/fcb/rt5xx_flexspi_nor.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/fcb/rt6xx_flexspi_nor.xml` & `spsdk-1.9.1/spsdk/data/image/fcb/rt6xx_flexspi_nor.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/fcb/sch_fcb.yml` & `spsdk-1.9.1/spsdk/data/image/fcb/sch_fcb.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/sch_binary.yml` & `spsdk-1.9.1/spsdk/data/image/sch_binary.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/sch_mbimg.yml` & `spsdk-1.9.1/spsdk/data/image/sch_mbimg.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/sch_sb3.yml` & `spsdk-1.9.1/spsdk/data/image/sch_sb3.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/sch_tz.yml` & `spsdk-1.9.1/spsdk/data/image/sch_tz.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/xmcd/database.yml` & `spsdk-1.9.1/spsdk/data/image/xmcd/database.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/xmcd/flexspi_ram_full.xml` & `spsdk-1.9.1/spsdk/data/image/xmcd/flexspi_ram_full.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/xmcd/flexspi_ram_simplified.xml` & `spsdk-1.9.1/spsdk/data/image/xmcd/flexspi_ram_simplified.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/xmcd/header.xml` & `spsdk-1.9.1/spsdk/data/image/xmcd/header.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/xmcd/sch_xmcd.yml` & `spsdk-1.9.1/spsdk/data/image/xmcd/sch_xmcd.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/xmcd/semc_sdram_full.xml` & `spsdk-1.9.1/spsdk/data/image/xmcd/semc_sdram_full.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/image/xmcd/semc_sdram_simplified.xml` & `spsdk-1.9.1/spsdk/data/image/xmcd/semc_sdram_simplified.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/nxpcertgen/certgen_config.yml` & `spsdk-1.9.1/spsdk/data/nxpcertgen/certgen_config.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/nxpdebugmbox/template_config.yml` & `spsdk-1.9.1/spsdk/data/nxpdebugmbox/template_config.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cfpa/database.yaml` & `spsdk-1.9.1/spsdk/data/pfr/cfpa/database.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc550x_a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc550x_a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc551x_a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc551x_a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc552x_1b.xml` & `spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc552x_1b.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc553x_0a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc553x_0a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc553x_1a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc553x_1a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc55s0x_a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc55s0x_a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc55s1x_a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc55s1x_a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc55s2x_1b.xml` & `spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc55s2x_1b.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc55s3x_0a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc55s3x_0a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc55s3x_1a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc55s3x_1a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cfpa/lpc55s6x_1b.xml` & `spsdk-1.9.1/spsdk/data/pfr/cfpa/lpc55s6x_1b.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cfpa/nhs52s04.xml` & `spsdk-1.9.1/spsdk/data/pfr/cfpa/nhs52s04.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cmpa/database.yaml` & `spsdk-1.9.1/spsdk/data/pfr/cmpa/database.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc550x_a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc550x_a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc551x_a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc551x_a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc552x_1b.xml` & `spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc552x_1b.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc553x_0a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc553x_0a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc553x_1a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc553x_1a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc55s0x_a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc55s0x_a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc55s1x_a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc55s1x_a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc55s2x_1b.xml` & `spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc55s2x_1b.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc55s3x_0a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc55s3x_0a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc55s3x_1a.xml` & `spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc55s3x_1a.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cmpa/lpc55s6x_1b.xml` & `spsdk-1.9.1/spsdk/data/pfr/cmpa/lpc55s6x_1b.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/cmpa/nhs52s04.xml` & `spsdk-1.9.1/spsdk/data/pfr/cmpa/nhs52s04.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/pfrc/database.yaml` & `spsdk-1.9.1/spsdk/data/pfr/pfrc/database.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/pfrc/rules_common.yaml` & `spsdk-1.9.1/spsdk/data/pfr/pfrc/rules_common.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/pfrc/rules_lpc55s3x.yaml` & `spsdk-1.9.1/spsdk/data/pfr/pfrc/rules_lpc55s3x.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/pfr/pfrc/rules_lpc55xx.yaml` & `spsdk-1.9.1/spsdk/data/pfr/pfrc/rules_lpc55xx.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/regs/regs_desc_template.html` & `spsdk-1.9.1/spsdk/data/regs/regs_desc_template.html`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/shadowregs/database.yaml` & `spsdk-1.9.1/spsdk/data/shadowregs/database.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/shadowregs/imxrt595_b0.xml` & `spsdk-1.9.1/spsdk/data/shadowregs/imxrt595_b0.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/shadowregs/imxrt685_b0.xml` & `spsdk-1.9.1/spsdk/data/shadowregs/imxrt685_b0.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tp/sch_tp.yaml` & `spsdk-1.9.1/spsdk/data/tp/sch_tp.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tp/tpconfig_cfg_template.yml` & `spsdk-1.9.1/spsdk/data/tp/tpconfig_cfg_template.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tp/tphost_cfg_template.yml` & `spsdk-1.9.1/spsdk/data/tp/tphost_cfg_template.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tz_presets/database.yaml` & `spsdk-1.9.1/spsdk/data/tz_presets/database.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tz_presets/kw45xx_a0.yaml` & `spsdk-1.9.1/spsdk/data/tz_presets/kw45xx_a0.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tz_presets/lpc55s0x.yaml` & `spsdk-1.9.1/spsdk/data/tz_presets/lpc55s0x.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tz_presets/lpc55s1x.yaml` & `spsdk-1.9.1/spsdk/data/tz_presets/lpc55s1x.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tz_presets/lpc55s3x_a0.yaml` & `spsdk-1.9.1/spsdk/data/tz_presets/lpc55s3x_a0.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tz_presets/lpc55s3x_a1.yaml` & `spsdk-1.9.1/spsdk/data/tz_presets/lpc55s3x_a1.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tz_presets/lpc55xx.yaml` & `spsdk-1.9.1/spsdk/data/tz_presets/lpc55xx.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tz_presets/lpc55xx_a0.yaml` & `spsdk-1.9.1/spsdk/data/tz_presets/lpc55xx_a0.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tz_presets/lpc55xx_a1.yaml` & `spsdk-1.9.1/spsdk/data/tz_presets/lpc55xx_a1.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tz_presets/nhs52s04.yaml` & `spsdk-1.9.1/spsdk/data/tz_presets/nhs52s04.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tz_presets/rt5xx.yaml` & `spsdk-1.9.1/spsdk/data/tz_presets/rt5xx.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tz_presets/rt5xx_a0.yaml` & `spsdk-1.9.1/spsdk/data/tz_presets/rt5xx_a0.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tz_presets/rt6xx.yaml` & `spsdk-1.9.1/spsdk/data/tz_presets/rt6xx.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tz_presets/rt6xx_a0.yaml` & `spsdk-1.9.1/spsdk/data/tz_presets/rt6xx_a0.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/tz_presets/rt6xx_b0.yaml` & `spsdk-1.9.1/spsdk/data/tz_presets/rt6xx_b0.yaml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/utils/bee/sch_bee.yml` & `spsdk-1.9.1/spsdk/data/utils/bee/sch_bee.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/utils/iee/database.yml` & `spsdk-1.9.1/spsdk/data/utils/iee/database.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/utils/iee/fuses_rt117x.xml` & `spsdk-1.9.1/spsdk/data/utils/iee/fuses_rt117x.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/utils/iee/sch_iee.yml` & `spsdk-1.9.1/spsdk/data/utils/iee/sch_iee.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/utils/otfad/database.yml` & `spsdk-1.9.1/spsdk/data/utils/otfad/database.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/utils/otfad/fuses_rt118x.xml` & `spsdk-1.9.1/spsdk/data/utils/otfad/fuses_rt118x.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/utils/otfad/fuses_rt5xx.xml` & `spsdk-1.9.1/spsdk/data/utils/otfad/fuses_rt5xx.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/utils/otfad/fuses_rt6xx.xml` & `spsdk-1.9.1/spsdk/data/utils/otfad/fuses_rt6xx.xml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/utils/otfad/sch_otfad.yml` & `spsdk-1.9.1/spsdk/data/utils/otfad/sch_otfad.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/data/utils/sch_crypto.yml` & `spsdk-1.9.1/spsdk/data/utils/sch_crypto.yml`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/debuggers/debug_probe.py` & `spsdk-1.9.1/spsdk/debuggers/debug_probe.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/debuggers/debug_probe_jlink.py` & `spsdk-1.9.1/spsdk/debuggers/debug_probe_jlink.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/debuggers/debug_probe_pemicro.py` & `spsdk-1.9.1/spsdk/debuggers/debug_probe_pemicro.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/debuggers/debug_probe_pyocd.py` & `spsdk-1.9.1/spsdk/debuggers/debug_probe_pyocd.py`

 * *Files 3% similar despite different names*

```diff
@@ -107,16 +107,14 @@
             self.probe: PyOCDDebugProbe = ConnectHelper.choose_probe(
                 blocking=False,
                 return_first=True,
                 unique_id=self.hardware_id,
             )
 
             self.probe.session = Session(self.probe)
-
-            # pylint: disable=protected-access  # we require a more specific setup
             self.probe.open()
             if isinstance(self.probe, JLinkProbe):
                 self.probe._link.set_tif(pylink.enums.JLinkInterfaces.SWD)
                 self.probe._link.coresight_configure()
                 self._protocol = pylink.enums.JLinkInterfaces.SWD
             else:
                 self.probe.connect(pyocd.probe.debug_probe.DebugProbe.Protocol.SWD)
@@ -134,14 +132,15 @@
     def close(self) -> None:
         """Close PyLink interface.
 
         The PyLink closing function for SPSDK library to support various DEBUG PROBES.
         """
         if self.probe:
             self.probe.close()
+            self.probe = None
 
     def assert_reset_line(self, assert_reset: bool = False) -> None:
         """Control reset line at a target.
 
         :param assert_reset: If True, the reset line is asserted(pulled down), if False the reset line is not affected.
         :raises SPSDKDebugProbeNotOpenError: The PyOCD debug probe is not opened yet
         :raises SPSDKDebugProbeError: The PyOCD probe RESET function failed
@@ -182,16 +181,17 @@
         :raises SPSDKDebugProbeTransferError: The IO operation failed
         :raises SPSDKDebugProbeNotOpenError: The PyOCD probe is NOT opened
         """
         if self.probe is None:
             raise SPSDKDebugProbeNotOpenError("The PyOCD debug probe is not opened yet")
         try:
             if access_port:
-                self.select_ap(addr)
-                addr = addr & 0x0F
+                if not PyOCDDebugProbe.Capability.MANAGED_AP_SELECTION in self.probe.capabilities:
+                    self.select_ap(addr)
+                    addr = addr & 0x0F
                 ret = self.probe.read_ap(addr=addr)
             else:
                 ret = self.probe.read_dp(addr)
             if TRACE_ENABLE:
                 logger.debug(
                     f"Coresight read {'AP' if access_port else 'DP'}, address: {addr:08X}, data: {ret:08X}"
                 )
@@ -211,16 +211,17 @@
         :raises SPSDKDebugProbeTransferError: The IO operation failed
         :raises SPSDKDebugProbeNotOpenError: The PyOCD probe is NOT opened
         """
         if self.probe is None:
             raise SPSDKDebugProbeNotOpenError("The PyOCD debug probe is not opened yet")
         try:
             if access_port:
-                self.select_ap(addr)
-                addr = addr & 0x0F
+                if not PyOCDDebugProbe.Capability.MANAGED_AP_SELECTION in self.probe.capabilities:
+                    self.select_ap(addr)
+                    addr = addr & 0x0F
                 self.probe.write_ap(addr=addr, data=data)
             else:
                 self.probe.write_dp(addr, data)
             if TRACE_ENABLE:
                 logger.debug(
                     f"Coresight write {'AP' if access_port else 'DP'}, address: {addr:08X}, data: {data:08X}"
                 )
```

### Comparing `spsdk-1.9.0/spsdk/debuggers/utils.py` & `spsdk-1.9.1/spsdk/debuggers/utils.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/exceptions.py` & `spsdk-1.9.1/spsdk/exceptions.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/__init__.py` & `spsdk-1.9.1/spsdk/image/__init__.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/ahab/__init__.py` & `spsdk-1.9.1/spsdk/image/ahab/__init__.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/ahab/ahab_abstract_interfaces.py` & `spsdk-1.9.1/spsdk/image/ahab/ahab_abstract_interfaces.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/ahab/ahab_container.py` & `spsdk-1.9.1/spsdk/image/ahab/ahab_container.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/ahab/signed_msg.py` & `spsdk-1.9.1/spsdk/image/ahab/signed_msg.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/bee.py` & `spsdk-1.9.1/spsdk/image/bee.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/bootable_image/bimg.py` & `spsdk-1.9.1/spsdk/image/bootable_image/bimg.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/commands.py` & `spsdk-1.9.1/spsdk/image/commands.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/fcb/fcb.py` & `spsdk-1.9.1/spsdk/image/fcb/fcb.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/hab_audit_log.py` & `spsdk-1.9.1/spsdk/image/hab_audit_log.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/header.py` & `spsdk-1.9.1/spsdk/image/header.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/images.py` & `spsdk-1.9.1/spsdk/image/images.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/keystore.py` & `spsdk-1.9.1/spsdk/image/keystore.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/mbi_mixin.py` & `spsdk-1.9.1/spsdk/image/mbi_mixin.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/mbimg.py` & `spsdk-1.9.1/spsdk/image/mbimg.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/misc.py` & `spsdk-1.9.1/spsdk/image/misc.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/secret.py` & `spsdk-1.9.1/spsdk/image/secret.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/segments.py` & `spsdk-1.9.1/spsdk/image/segments.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/segments_base.py` & `spsdk-1.9.1/spsdk/image/segments_base.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/trustzone.py` & `spsdk-1.9.1/spsdk/image/trustzone.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/image/xmcd/xmcd.py` & `spsdk-1.9.1/spsdk/image/xmcd/xmcd.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/mboot/__init__.py` & `spsdk-1.9.1/spsdk/mboot/__init__.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/mboot/commands.py` & `spsdk-1.9.1/spsdk/mboot/commands.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/mboot/error_codes.py` & `spsdk-1.9.1/spsdk/mboot/error_codes.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/mboot/exceptions.py` & `spsdk-1.9.1/spsdk/mboot/exceptions.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/mboot/interfaces/base.py` & `spsdk-1.9.1/spsdk/mboot/interfaces/base.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/mboot/interfaces/buspal.py` & `spsdk-1.9.1/spsdk/mboot/interfaces/buspal.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/mboot/interfaces/buspal_i2c.py` & `spsdk-1.9.1/spsdk/mboot/interfaces/buspal_i2c.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/mboot/interfaces/buspal_spi.py` & `spsdk-1.9.1/spsdk/mboot/interfaces/buspal_spi.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/mboot/interfaces/uart.py` & `spsdk-1.9.1/spsdk/mboot/interfaces/uart.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/mboot/interfaces/usb.py` & `spsdk-1.9.1/spsdk/mboot/interfaces/usb.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/mboot/interfaces/usbsio.py` & `spsdk-1.9.1/spsdk/mboot/interfaces/usbsio.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/mboot/mcuboot.py` & `spsdk-1.9.1/spsdk/mboot/mcuboot.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/mboot/memories.py` & `spsdk-1.9.1/spsdk/mboot/memories.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/mboot/properties.py` & `spsdk-1.9.1/spsdk/mboot/properties.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/pfr/__init__.py` & `spsdk-1.9.1/spsdk/pfr/__init__.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/pfr/exceptions.py` & `spsdk-1.9.1/spsdk/pfr/exceptions.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/pfr/pfr.py` & `spsdk-1.9.1/spsdk/pfr/pfr.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/pfr/pfrc.py` & `spsdk-1.9.1/spsdk/pfr/pfrc.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/pfr/processor.py` & `spsdk-1.9.1/spsdk/pfr/processor.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/pfr/translator.py` & `spsdk-1.9.1/spsdk/pfr/translator.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/misc.py` & `spsdk-1.9.1/spsdk/sbfile/misc.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb1/__init__.py` & `spsdk-1.9.1/spsdk/sbfile/sb1/__init__.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb1/commands.py` & `spsdk-1.9.1/spsdk/sbfile/sb1/commands.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb1/headers.py` & `spsdk-1.9.1/spsdk/sbfile/sb1/headers.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb1/images.py` & `spsdk-1.9.1/spsdk/sbfile/sb1/images.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb1/sections.py` & `spsdk-1.9.1/spsdk/sbfile/sb1/sections.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb2/commands.py` & `spsdk-1.9.1/spsdk/sbfile/sb2/commands.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb2/headers.py` & `spsdk-1.9.1/spsdk/sbfile/sb2/headers.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb2/images.py` & `spsdk-1.9.1/spsdk/sbfile/sb2/images.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb2/sb_21_helper.py` & `spsdk-1.9.1/spsdk/sbfile/sb2/sb_21_helper.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb2/sections.py` & `spsdk-1.9.1/spsdk/sbfile/sb2/sections.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb2/sly_bd_lexer.py` & `spsdk-1.9.1/spsdk/sbfile/sb2/sly_bd_lexer.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb2/sly_bd_parser.py` & `spsdk-1.9.1/spsdk/sbfile/sb2/sly_bd_parser.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb31/__init__.py` & `spsdk-1.9.1/spsdk/sbfile/sb31/__init__.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb31/commands.py` & `spsdk-1.9.1/spsdk/sbfile/sb31/commands.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb31/constants.py` & `spsdk-1.9.1/spsdk/sbfile/sb31/constants.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb31/functions.py` & `spsdk-1.9.1/spsdk/sbfile/sb31/functions.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sbfile/sb31/images.py` & `spsdk-1.9.1/spsdk/sbfile/sb31/images.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sdp/__init__.py` & `spsdk-1.9.1/spsdk/sdp/__init__.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sdp/commands.py` & `spsdk-1.9.1/spsdk/sdp/commands.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sdp/error_codes.py` & `spsdk-1.9.1/spsdk/sdp/error_codes.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sdp/exceptions.py` & `spsdk-1.9.1/spsdk/sdp/exceptions.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sdp/interfaces/base.py` & `spsdk-1.9.1/spsdk/sdp/interfaces/base.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sdp/interfaces/uart.py` & `spsdk-1.9.1/spsdk/sdp/interfaces/uart.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sdp/interfaces/usb.py` & `spsdk-1.9.1/spsdk/sdp/interfaces/usb.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sdp/sdp.py` & `spsdk-1.9.1/spsdk/sdp/sdp.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/sdp/sdps.py` & `spsdk-1.9.1/spsdk/sdp/sdps.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/shadowregs/shadowregs.py` & `spsdk-1.9.1/spsdk/shadowregs/shadowregs.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/tp/__init__.py` & `spsdk-1.9.1/spsdk/tp/__init__.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/tp/adapters/__init__.py` & `spsdk-1.9.1/spsdk/tp/adapters/__init__.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/tp/adapters/scard_commands.py` & `spsdk-1.9.1/spsdk/tp/adapters/scard_commands.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/tp/adapters/scard_utils.py` & `spsdk-1.9.1/spsdk/tp/adapters/scard_utils.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/tp/adapters/tpdev_scard.py` & `spsdk-1.9.1/spsdk/tp/adapters/tpdev_scard.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/tp/adapters/tptarget_blhost.py` & `spsdk-1.9.1/spsdk/tp/adapters/tptarget_blhost.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/tp/adapters/utils.py` & `spsdk-1.9.1/spsdk/tp/adapters/utils.py`

 * *Files 20% similar despite different names*

```diff
@@ -12,16 +12,14 @@
 from spsdk.crypto.certificate_management import X509NameConfig
 from spsdk.mboot.interfaces.usb import RawHid, scan_usb
 from spsdk.utils.misc import Timeout
 
 from .. import SPSDKTpError
 from .tptarget_blhost import TpTargetBlHost
 
-USB_DETECTION_TIMEOUT = 1
-
 logger = logging.getLogger(__name__)
 
 
 def sanitize_common_name(name_config: X509NameConfig) -> None:
     """Adjust the COMMON_NAME for TrustProvisioning purposes.
 
     Base common name will be AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-BB
@@ -53,36 +51,46 @@
 
 
 def get_current_usb_paths() -> Set[bytes]:
     """Get paths to all NXP USB devices."""
     return {device.path for device in scan_usb()}
 
 
-def detect_new_usb_path(initial_set: Optional[Set[bytes]] = None) -> bytes:
+def detect_new_usb_path(
+    initial_set: Optional[Set[bytes]] = None, timeout: int = 1000
+) -> Optional[bytes]:
     """Return USB path to newly found NXP USB device.
 
     :param initial_set: Initial set of USB device paths, defaults to None
-    :raises SPSDKTpError: Unable to detect new device in time USB_DETECTION_TIMEOUT (default: 1sec)
+    :param timeout: Timeout in milliseconds for the device detection
+    :raises SPSDKTpError: Unable to determine single USB device change in time
     :raises SPSDKTpError: Multiple USB devices detected at once
-    :return: USB path to newly detected device
+    :return: USB path to newly detected device, None in case no changes were detected
     """
-    timeout = Timeout(USB_DETECTION_TIMEOUT)
+    loc_timeout = Timeout(timeout=timeout, units="ms")
     previous_set = initial_set or set()
-    while not timeout.overflow():
+    while not loc_timeout.overflow():
         new_set = get_current_usb_paths()
         addition = new_set.difference(previous_set)
         logger.info(f"Additions: {addition}")
         previous_set = new_set
         if len(addition) > 1:
             raise SPSDKTpError("Multiple new usb devices detected at once!")
         if len(addition) == 1:
             return addition.pop()
-        # TODO: should we wait here for a bit?
 
-    raise SPSDKTpError(f"No new USB device detected in time ({USB_DETECTION_TIMEOUT} sec)")
+    # when timeout passes and the USB paths set stays the same
+    # this happens mostly on Windows under higher CPU load
+    if initial_set == previous_set:
+        logger.info("No changes were detected")
+        return None
+
+    raise SPSDKTpError(f"USB device detected malfunctioned")
 
 
-def update_usb_path(tptarget: TpTargetBlHost, new_usb_path: bytes) -> None:
+def update_usb_path(tptarget: TpTargetBlHost, new_usb_path: Optional[bytes]) -> None:
     """Update USB path in TP target's MBoot USB."""
     if not isinstance(tptarget.mboot._device, RawHid):
         return
+    if new_usb_path is None:
+        return
     tptarget.mboot._device.path = new_usb_path
```

### Comparing `spsdk-1.9.0/spsdk/tp/data_container/audit_log.py` & `spsdk-1.9.1/spsdk/tp/data_container/audit_log.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/tp/data_container/data_container.py` & `spsdk-1.9.1/spsdk/tp/data_container/data_container.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/tp/data_container/data_container_auth.py` & `spsdk-1.9.1/spsdk/tp/data_container/data_container_auth.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/tp/data_container/payload_types.py` & `spsdk-1.9.1/spsdk/tp/data_container/payload_types.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/tp/exceptions.py` & `spsdk-1.9.1/spsdk/tp/exceptions.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/tp/tp_intf.py` & `spsdk-1.9.1/spsdk/tp/tp_intf.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/tp/tpconfig.py` & `spsdk-1.9.1/spsdk/tp/tpconfig.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/tp/tphost.py` & `spsdk-1.9.1/spsdk/tp/tphost.py`

 * *Files 1% similar despite different names*

```diff
@@ -58,23 +58,25 @@
         self,
         prov_fw: bytes,
         family: str,
         timeout: int = 60,
         database: Optional[Database] = None,
         skip_test: bool = True,
         keep_target_open: bool = True,
+        skip_usb_enumeration: bool = False,
     ) -> None:
         """Method loads the provisioning firmware into device.
 
         :param prov_fw: Provisioning Firmware data
         :param family: Chip family
         :param timeout: Timeout for loading provisioning firmware operation in seconds.
         :param database: Database of all supported devices (automatic lookup if not specified)
         :param skip_test: Skip test for checking that OEM Provisioning Firmware booted-up
         :param keep_target_open: Keep target device open
+        :param skip_usb_enumeration: Skip USB enumeration after loading the Provisioning firmware
         :raises SPSDKTpError: The Provisioning firmware doesn't boot
         """
         if database is None:
             logger.debug("Looking up device in database")
             database = Database(os.path.join(TP_DATA_FOLDER, "database.yaml"))
         if family not in database.devices.device_names:
             raise SPSDKTpError(f"Database info missing for '{family}'")
@@ -94,15 +96,15 @@
             if self.tptarget.uses_usb:
                 initial_usb_set = get_current_usb_paths()
 
             self.tptarget.load_sb_file(prov_fw, timeout)
             # Need to reset the connection due to re-init on the MCU side
             self.tptarget.close()
 
-            if self.tptarget.uses_usb:
+            if self.tptarget.uses_usb and not skip_usb_enumeration:
                 assert isinstance(self.tptarget, TpTargetBlHost)
                 new_usb_path = detect_new_usb_path(initial_set=initial_usb_set)
                 update_usb_path(self.tptarget, new_usb_path=new_usb_path)
 
             logger.info(f"Waiting for {REOPEN_WAIT_TIME} seconds for the ProvFW to boot up.")
             time.sleep(REOPEN_WAIT_TIME)
 
@@ -114,15 +116,15 @@
 
             if keep_target_open and not self.tptarget.is_open:
                 self.tptarget.open()
 
         except SPSDKError as e:
             self.tptarget.close()
             raise SPSDKTpError(
-                "Can't load/connect to the TrustProvisioning Firmware. "
+                f"Can't load/connect to the TrustProvisioning Firmware. Error: {e}\n"
                 "Please make sure your device supports TrustProvisioning."
             ) from e
 
     def update_cfpa_page(self, family: str, database: Database) -> None:
         """Update CFPA page according to chip family."""
         if not database.get_device_value("need_cfpa_update", family):
             logger.info("CFPA update not required")
@@ -216,14 +218,15 @@
                 self.load_provisioning_fw(
                     prov_fw=prov_fw,
                     family=family,
                     timeout=loc_timeout.get_rest_time_ms(True),
                     database=database,
                     skip_test=True,
                     keep_target_open=True,
+                    skip_usb_enumeration=False,
                 )
 
             self.info_print("2.Step - Get the initial challenge from TP device.")
             challenge = self.tpdev.get_challenge(timeout=loc_timeout.get_rest_time_ms(True))
 
             logger.info(f"TP Challenge:\n{Container.parse(challenge)}")
             if save_debug_data:
```

### Comparing `spsdk-1.9.0/spsdk/tp/utils.py` & `spsdk-1.9.1/spsdk/tp/utils.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/__init__.py` & `spsdk-1.9.1/spsdk/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/crypto/__init__.py` & `spsdk-1.9.1/spsdk/utils/crypto/__init__.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/crypto/abstract.py` & `spsdk-1.9.1/spsdk/utils/crypto/abstract.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/crypto/backend_internal.py` & `spsdk-1.9.1/spsdk/utils/crypto/backend_internal.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/crypto/backend_openssl.py` & `spsdk-1.9.1/spsdk/utils/crypto/backend_openssl.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/crypto/cert_blocks.py` & `spsdk-1.9.1/spsdk/utils/crypto/cert_blocks.py`

 * *Files 2% similar despite different names*

```diff
@@ -832,14 +832,21 @@
         # filter out None and empty values
         root_certificates = list(filter(None, root_certificates_loaded))
         for org, filtered in zip(root_certificates_loaded, root_certificates):
             if org != filtered:
                 raise SPSDKError("There are gaps in rootCertificateXFile definition")
 
         main_root_cert_id = get_main_cert_index(config, default=0)
+        try:
+            root_certificates[main_root_cert_id]
+        except IndexError as e:
+            raise SPSDKError(
+                f"Main root certificate with id {main_root_cert_id} does not exist"
+            ) from e
+
         main_root_private_key_file = config.get("mainRootCertPrivateKeyFile")
         use_isk = config.get("useIsk", False)
         isk_certificate = config.get("signingCertificateFile")
         isk_constraint = misc.value_to_int(config.get("signingCertificateConstraint", "0"))
         isk_sign_data_path = config.get("signCertData")
 
         root_certs = [
```

### Comparing `spsdk-1.9.0/spsdk/utils/crypto/certificate.py` & `spsdk-1.9.1/spsdk/utils/crypto/certificate.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/crypto/common.py` & `spsdk-1.9.1/spsdk/utils/crypto/common.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/crypto/iee.py` & `spsdk-1.9.1/spsdk/utils/crypto/iee.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/crypto/otfad.py` & `spsdk-1.9.1/spsdk/utils/crypto/otfad.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/crypto/rkht.py` & `spsdk-1.9.1/spsdk/utils/crypto/rkht.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/database.py` & `spsdk-1.9.1/spsdk/utils/database.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/devicedescription.py` & `spsdk-1.9.1/spsdk/utils/devicedescription.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/easy_enum.py` & `spsdk-1.9.1/spsdk/utils/easy_enum.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/easy_enum.pyi` & `spsdk-1.9.1/spsdk/utils/easy_enum.pyi`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/exceptions.py` & `spsdk-1.9.1/spsdk/utils/exceptions.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/images.py` & `spsdk-1.9.1/spsdk/utils/images.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/misc.py` & `spsdk-1.9.1/spsdk/utils/misc.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/nxpdevscan.py` & `spsdk-1.9.1/spsdk/utils/nxpdevscan.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/reg_config.py` & `spsdk-1.9.1/spsdk/utils/reg_config.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/registers.py` & `spsdk-1.9.1/spsdk/utils/registers.py`

 * *Files 2% similar despite different names*

```diff
@@ -1169,23 +1169,43 @@
                     if register.config_as_hexstring and isinstance(raw_val, str)
                     else value_to_int(raw_val)
                 )
                 register.set_value(val, True)
             elif "bitfields" in reg_dict.keys():
                 for bitfield_name in reg_dict["bitfields"]:
                     bitfield_val = reg_dict["bitfields"][bitfield_name]
-                    bitfield = register.find_bitfield(bitfield_name)
+                    try:
+                        bitfield = register.find_bitfield(bitfield_name)
+                    except SPSDKRegsErrorBitfieldNotFound:
+                        logger.error(
+                            f"The {bitfield_name} is not found in register {register.name}."
+                            " Please update the PFR configuration data"
+                        )
+                        continue
                     if (
                         exclude_fields
                         and reg_name in exclude_fields.keys()
                         and bitfield_name in exclude_fields[reg_name]
                     ):
                         continue
 
-                    bitfield.set_enum_value(bitfield_val, True)
+                    try:
+                        bitfield.set_enum_value(bitfield_val, True)
+                    except SPSDKError:
+                        # New versions of register data do not contain register and bitfield value in enum
+                        old_bitfield = bitfield_val
+                        bitfield_val = bitfield_val.replace(bitfield.name + "_", "").replace(
+                            register.name + "_", ""
+                        )
+                        # Some bitfield were renamed from ENABLE to ALLOW
+                        bitfield_val = "ALLOW" if bitfield_val == "ENABLE" else bitfield_val
+                        logger.warning(
+                            f"Bitfield {old_bitfield} not found, trying backward compatibility mode with {bitfield_val}"
+                        )
+                        bitfield.set_enum_value(bitfield_val, True)
             else:
                 logger.error(f"There are no data for {reg_name} register.")
 
             logger.debug(f"The register {reg_name} has been loaded from configuration.")
 
     def _get_bitfield_yaml_description(self, bitfield: RegsBitField, indent: int) -> str:
         """Create the valuable comment for bitfield.
```

### Comparing `spsdk-1.9.0/spsdk/utils/schema_validator.py` & `spsdk-1.9.1/spsdk/utils/schema_validator.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/serial_buspal_proxy.py` & `spsdk-1.9.1/spsdk/utils/serial_buspal_proxy.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/serial_proxy.py` & `spsdk-1.9.1/spsdk/utils/serial_proxy.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk/utils/usbfilter.py` & `spsdk-1.9.1/spsdk/utils/usbfilter.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/spsdk.egg-info/PKG-INFO` & `spsdk-1.9.1/spsdk.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,68 +1,18 @@
 Metadata-Version: 2.1
 Name: spsdk
-Version: 1.9.0
+Version: 1.9.1
 Summary: Open Source Secure Provisioning SDK for NXP MCU/MPU
 Home-page: https://github.com/NXPmicro/spsdk
 Author: NXP
 Author-email: michal.starecek@nxp.com
 License: BSD-3-Clause
 Project-URL: Code, https://github.com/NXPmicro/spsdk
 Project-URL: Issue tracker, https://github.com/NXPmicro/spsdk/issues
 Project-URL: Documentation, https://spsdk.readthedocs.io
-Description: # NXP Secure Provisioning SDK
-        
-        **Secure Provisioning SDK (SPSDK)** enables connection and communication with target devices for purposes of secure provisioning and programming. Delivered as python library with command-line applications for direct utilization.
-        
-        ![](https://github.com/NXPmicro/spsdk/raw/master/docs/_static/images/spsdk-architecture.png)
-        
-        * [PyPi](https://pypi.org/project/spsdk/)
-        * [Documentation](https://spsdk.readthedocs.io)
-        * [Project page](https://www.nxp.com/design/software/development-software/secure-provisioning-sdk-spsdk:SPSDK)
-        
-        ## Supported Devices
-        
-        Following NXP devices are supported:
-        
-        - LPC55 [S6x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/high-efficiency-arm-cortex-m33-based-microcontroller-family:LPC55S6x) / [S3x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33:LPC5500_SERIES) / [S2x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc552x-s2x-mainstream-arm-cortex-m33-based-microcontroller-family:LPC552x-S2x) / [S1x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc551x-s1x-baseline-arm-cortex-m33-based-microcontroller-family:LPC551X-S1X) / [S0x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc550x-s0x-baseline-arm-cortex-m33-based-microcontroller-family:LPC550x)
-        - i.MX RT [600](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt600-crossover-mcu-with-arm-cortex-m33-and-dsp-cores:i.MX-RT600) / [500](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt500-crossover-mcu-with-arm-cortex-m33-core:i.MX-RT500)
-        - i.MX RT [1064](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1064-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1064) / [1060](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1060-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1060) / [1050](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1050-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1050) / [1020](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1020-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1020) / [1010](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1010-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1010)
-        - i.MX RT [1170](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1170-crossover-mcu-family-first-ghz-mcu-with-arm-cortex-m7-and-cortex-m4-cores:i.MX-RT1170) / [1160](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx-rt1160-evaluation-kit:MIMXRT1160-EVK)
-        - KW45 [KW45](https://www.nxp.com/products/wireless/bluetooth-low-energy/32-bit-bluetooth-5-3-long-range-mcus-with-can-fd-and-lin-bus-options-arm-cortex-m33-core:KW45)
-        - K32W1 [K32W1](https://www.nxp.com/products/wireless/multiprotocol-mcus/tri-core-secure-and-ultra-low-power-mcu-for-matter-over-thread-and-bluetooth-le-5-3:K32W148)
-        
-        ## Supported environments
-        
-        - Windows 10, 64bit
-        - Ubuntu 18.04 or above, 64bit
-        - Mac OS 10.15 or above, x64, ARM64
-        
-        ## Usage
-        
-        - See [installation](https://spsdk.readthedocs.io/en/latest/usage/installation.html) guide
-        - See [examples](https://github.com/nxp-mcuxpresso/spsdk/tree/master/examples) directory
-        - See [application](https://github.com/nxp-mcuxpresso/spsdk/tree/master/spsdk/apps) directory
-        
-        ---
-        **i.Mx RT 1050**
-        
-        To run examples using i.MX RT 1050 you need to download a flashloader:
-        - Go to: https://www.nxp.com/webapp/sps/download/license.jsp?colCode=IMX-RT1050-FLASHLOADER
-        - Review the license agreement, download and unzip the package
-        - Convert the elf file into bin (For this operation you need to have MCUXpresso IDE, IAR or Keil)
-          - run ```python tools\flashloader_converter.py --elf-path <path/to/flashloader.elf> --ide-type <mcux | iar | keil> --ide-path <path/to/IDE/install/folder```
-        
-        ---
-        
-        ## Dependencies
-        
-        The core dependencies are included in [requirements.txt](https://github.com/nxp-mcuxpresso/spsdk/blob/master/requirements.txt).
-        
-        The dependencies for the development and testing are included in [requirements-develop.txt](https://github.com/nxp-mcuxpresso/spsdk/blob/master/requirements-develop.txt).
-        
 Platform: Windows
 Platform: Linux
 Platform: Mac OSX
 Classifier: Development Status :: 3 - Alpha
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
@@ -76,7 +26,58 @@
 Classifier: Topic :: Scientific/Engineering
 Classifier: Topic :: Software Development :: Embedded Systems
 Classifier: Topic :: System :: Hardware
 Classifier: Topic :: Utilities
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 Provides-Extra: tp
+License-File: LICENSE
+
+# NXP Secure Provisioning SDK
+
+**Secure Provisioning SDK (SPSDK)** enables connection and communication with target devices for purposes of secure provisioning and programming. Delivered as python library with command-line applications for direct utilization.
+
+![](https://github.com/NXPmicro/spsdk/raw/master/docs/_static/images/spsdk-architecture.png)
+
+* [PyPi](https://pypi.org/project/spsdk/)
+* [Documentation](https://spsdk.readthedocs.io)
+* [Project page](https://www.nxp.com/design/software/development-software/secure-provisioning-sdk-spsdk:SPSDK)
+
+## Supported Devices
+
+Following NXP devices are supported:
+
+- LPC55 [S6x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/high-efficiency-arm-cortex-m33-based-microcontroller-family:LPC55S6x) / [S3x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33:LPC5500_SERIES) / [S2x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc552x-s2x-mainstream-arm-cortex-m33-based-microcontroller-family:LPC552x-S2x) / [S1x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc551x-s1x-baseline-arm-cortex-m33-based-microcontroller-family:LPC551X-S1X) / [S0x](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc550x-s0x-baseline-arm-cortex-m33-based-microcontroller-family:LPC550x)
+- i.MX RT [600](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt600-crossover-mcu-with-arm-cortex-m33-and-dsp-cores:i.MX-RT600) / [500](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt500-crossover-mcu-with-arm-cortex-m33-core:i.MX-RT500)
+- i.MX RT [1064](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1064-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1064) / [1060](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1060-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1060) / [1050](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1050-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1050) / [1020](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1020-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1020) / [1010](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1010-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1010)
+- i.MX RT [1170](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1170-crossover-mcu-family-first-ghz-mcu-with-arm-cortex-m7-and-cortex-m4-cores:i.MX-RT1170) / [1160](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx-rt1160-evaluation-kit:MIMXRT1160-EVK)
+- [KW45](https://www.nxp.com/products/wireless/bluetooth-low-energy/32-bit-bluetooth-5-3-long-range-mcus-with-can-fd-and-lin-bus-options-arm-cortex-m33-core:KW45)
+- [K32W1](https://www.nxp.com/products/wireless/multiprotocol-mcus/tri-core-secure-and-ultra-low-power-mcu-for-matter-over-thread-and-bluetooth-le-5-3:K32W148)
+
+## Supported environments
+
+- Windows 10, 64bit
+- Ubuntu 18.04 or above, 64bit
+- Mac OS 10.15 or above, x64, ARM64
+
+## Usage
+
+- See [installation](https://spsdk.readthedocs.io/en/latest/usage/installation.html) guide
+- See [examples](https://github.com/nxp-mcuxpresso/spsdk/tree/master/examples) directory
+- See [application](https://github.com/nxp-mcuxpresso/spsdk/tree/master/spsdk/apps) directory
+
+---
+**i.Mx RT 1050**
+
+To run examples using i.MX RT 1050 you need to download a flashloader:
+- Go to: https://www.nxp.com/webapp/sps/download/license.jsp?colCode=IMX-RT1050-FLASHLOADER
+- Review the license agreement, download and unzip the package
+- Convert the elf file into bin (For this operation you need to have MCUXpresso IDE, IAR or Keil)
+  - run ```python tools\flashloader_converter.py --elf-path <path/to/flashloader.elf> --ide-type <mcux | iar | keil> --ide-path <path/to/IDE/install/folder```
+
+---
+
+## Dependencies
+
+The core dependencies are included in [requirements.txt](https://github.com/nxp-mcuxpresso/spsdk/blob/master/requirements.txt).
+
+The dependencies for the development and testing are included in [requirements-develop.txt](https://github.com/nxp-mcuxpresso/spsdk/blob/master/requirements-develop.txt).
```

### Comparing `spsdk-1.9.0/spsdk.egg-info/SOURCES.txt` & `spsdk-1.9.1/spsdk.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -279,14 +279,15 @@
 spsdk/utils/crypto/backend_openssl.py
 spsdk/utils/crypto/cert_blocks.py
 spsdk/utils/crypto/certificate.py
 spsdk/utils/crypto/common.py
 spsdk/utils/crypto/iee.py
 spsdk/utils/crypto/otfad.py
 spsdk/utils/crypto/rkht.py
+tests/test_self.py
 tools/__init__.py
 tools/checker_copyright_year.py
 tools/checker_dependencies.py
 tools/checker_mypy_annotations.py
 tools/checker_pydocstyle.py
 tools/clr.py
 tools/fcb_header_to_xml.py
```

### Comparing `spsdk-1.9.0/spsdk.egg-info/entry_points.txt` & `spsdk-1.9.1/spsdk.egg-info/entry_points.txt`

 * *Files 0% similar despite different names*

```diff
@@ -12,8 +12,7 @@
 pfr = spsdk.apps.pfr:safe_main
 sdphost = spsdk.apps.sdphost:safe_main
 sdpshost = spsdk.apps.sdpshost:safe_main
 shadowregs = spsdk.apps.shadowregs:safe_main
 spsdk = spsdk.apps.spsdk_apps:safe_main
 tpconfig = spsdk.apps.tpconfig:safe_main
 tphost = spsdk.apps.tphost:safe_main
-
```

### Comparing `spsdk-1.9.0/spsdk.egg-info/requires.txt` & `spsdk-1.9.1/spsdk.egg-info/requires.txt`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 asn1crypto<1.6,>=1.2
 astunparse<1.7,>=1.6
-bincopy<17.15,>=17.10.2
+bincopy<=17.14.0,>=17.10.2
 bitstring<4.1,>=3.1
 click-option-group<0.6,>=0.3.0
 click-command-tree<1.2
 click<8.2,>=7.1
 colorama<0.5,>=0.4.6
 commentjson<0.10,>=0.9
 crcmod<1.8
@@ -13,17 +13,17 @@
 fastjsonschema<2.17,>=2.15.1
 hexdump<3.4
 jinja2<3.2,>=3.0
 libusbsio<2.2,>=2.1.11
 oscrypto<1.4
 pycryptodome<3.17,>=3.9.3
 pylink-square<0.15,>=0.8.2
-pyocd-pemicro<1.2,>=1.1.1
+pyocd-pemicro<1.2,>=1.1.5
 pyocd<0.32,>=0.28.3
-pypemicro<0.2,>=0.1.9
+pypemicro<0.2,>=0.1.11
 pyserial<3.6,>=3.1
 ruamel.yaml<0.18,>=0.17
 sly<0.6
 cmsis-pack-manager<0.3.0
 typing-extensions<4.5
 
 [tp]
```

### Comparing `spsdk-1.9.0/tools/checker_copyright_year.py` & `spsdk-1.9.1/tools/checker_copyright_year.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/tools/checker_dependencies.py` & `spsdk-1.9.1/tools/checker_dependencies.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/tools/checker_mypy_annotations.py` & `spsdk-1.9.1/tools/checker_mypy_annotations.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/tools/checker_pydocstyle.py` & `spsdk-1.9.1/tools/checker_pydocstyle.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/tools/clr.py` & `spsdk-1.9.1/tools/clr.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/tools/fcb_header_to_xml.py` & `spsdk-1.9.1/tools/fcb_header_to_xml.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/tools/flashloader_converter.py` & `spsdk-1.9.1/tools/flashloader_converter.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/tools/git_operations.py` & `spsdk-1.9.1/tools/git_operations.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/tools/gitcov.py` & `spsdk-1.9.1/tools/gitcov.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/tools/release_notes.py` & `spsdk-1.9.1/tools/release_notes.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/tools/req_update.py` & `spsdk-1.9.1/tools/req_update.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/tools/sr_xls2xml.py` & `spsdk-1.9.1/tools/sr_xls2xml.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/tools/task_scheduler.py` & `spsdk-1.9.1/tools/task_scheduler.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/tools/tp_migrate_audit_log.py` & `spsdk-1.9.1/tools/tp_migrate_audit_log.py`

 * *Files identical despite different names*

### Comparing `spsdk-1.9.0/tools/tp_setup_workspace.py` & `spsdk-1.9.1/tools/tp_setup_workspace.py`

 * *Files identical despite different names*

