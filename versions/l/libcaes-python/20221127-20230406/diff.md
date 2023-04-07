# Comparing `tmp/libcaes-python-20221127.tar.gz` & `tmp/libcaes-python-20230406.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "libcaes-python-20221127.tar", last modified: Sun Nov 27 19:10:22 2022, max compression
+gzip compressed data, was "libcaes-python-20230406.tar", last modified: Fri Apr  7 05:43:30 2023, max compression
```

## Comparing `libcaes-python-20221127.tar` & `libcaes-python-20230406.tar`

### file list

```diff
@@ -1,226 +1,226 @@
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/common/
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1157 2022-11-27 18:53:35.000000 libcaes-20221127/common/config_msc.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    10437 2022-11-27 18:53:35.000000 libcaes-20221127/common/byte_stream.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1250 2022-11-27 18:53:35.000000 libcaes-20221127/common/common.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     4611 2022-11-27 18:53:35.000000 libcaes-20221127/common/system_string.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      378 2022-11-27 18:53:34.000000 libcaes-20221127/common/Makefile.am
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     7234 2022-11-27 19:00:26.000000 libcaes-20221127/common/types.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     7236 2022-11-27 18:53:35.000000 libcaes-20221127/common/types.h.in
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     2243 2022-11-27 18:53:35.000000 libcaes-20221127/common/config_winapi.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     3259 2022-11-27 18:53:35.000000 libcaes-20221127/common/memory.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    11096 2022-11-27 18:58:24.000000 libcaes-20221127/common/config.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     5419 2022-11-27 18:53:35.000000 libcaes-20221127/common/narrow_string.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    19030 2022-11-27 19:00:16.000000 libcaes-20221127/common/Makefile.in
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     3878 2022-11-27 18:53:35.000000 libcaes-20221127/common/file_stream.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      957 2022-11-27 18:53:35.000000 libcaes-20221127/common/config_borlandc.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    10484 2022-11-27 19:00:16.000000 libcaes-20221127/common/config.h.in
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     5064 2022-11-27 18:53:35.000000 libcaes-20221127/common/wide_string.h
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/tests/
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     4653 2022-11-27 18:53:36.000000 libcaes-20221127/tests/caes_test_memory.c
--rwxrwxr-x   0 lordyesta  (1000) lordyesta  (1000)     3801 2022-11-27 18:53:35.000000 libcaes-20221127/tests/test_library.sh
--rwxrwxr-x   0 lordyesta  (1000) lordyesta  (1000)     3410 2022-11-27 18:53:35.000000 libcaes-20221127/tests/test_python_module.sh
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1152 2022-11-27 18:53:36.000000 libcaes-20221127/tests/pycaes_test_support.py
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)   268872 2022-11-27 18:53:36.000000 libcaes-20221127/tests/caes_test_crypt_xts.c
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     2240 2022-11-27 18:54:10.000000 libcaes-20221127/tests/Makefile.am
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)  1216152 2022-11-27 18:54:10.000000 libcaes-20221127/tests/caes_test_context.c
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)   175372 2022-11-27 18:53:35.000000 libcaes-20221127/tests/pycaes_test_crypt_cbc.py
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)   177604 2022-11-27 18:53:36.000000 libcaes-20221127/tests/caes_test_crypt_cbc.c
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)   174565 2022-11-27 18:53:35.000000 libcaes-20221127/tests/pycaes_test_crypt_ecb.py
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     8539 2022-11-27 18:53:36.000000 libcaes-20221127/tests/caes_test_macros.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     3099 2022-11-27 18:53:36.000000 libcaes-20221127/tests/caes_test_error.c
--rwxrw-r--   0 lordyesta  (1000) lordyesta  (1000)     1645 2022-11-27 18:53:35.000000 libcaes-20221127/tests/test_manpage.sh
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     2056 2022-11-27 18:53:36.000000 libcaes-20221127/tests/caes_test_support.c
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1536 2022-11-27 18:53:36.000000 libcaes-20221127/tests/caes_test_unused.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    37784 2022-11-27 18:53:35.000000 libcaes-20221127/tests/test_runner.sh
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    28105 2022-11-27 18:54:10.000000 libcaes-20221127/tests/caes_test_tweaked_context.c
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)   271703 2022-11-27 18:53:36.000000 libcaes-20221127/tests/pycaes_test_crypt_xts.py
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    42707 2022-11-27 19:00:17.000000 libcaes-20221127/tests/Makefile.in
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      973 2022-11-27 18:53:36.000000 libcaes-20221127/tests/caes_test_libcaes.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1691 2022-11-27 18:53:36.000000 libcaes-20221127/tests/caes_test_memory.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     6243 2022-11-27 18:53:36.000000 libcaes-20221127/tests/caes_test_crypt_ccm.c
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1441 2022-11-27 18:53:36.000000 libcaes-20221127/tests/caes_test_libcerror.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     3434 2022-11-27 18:53:35.000000 libcaes-20221127/tests/pycaes_test_crypt_ccm.py
--rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)     6878 2022-11-27 19:00:16.000000 libcaes-20221127/missing
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1747 2022-04-24 06:42:24.000000 libcaes-20221127/Makefile.am
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    55609 2022-11-27 19:00:14.000000 libcaes-20221127/aclocal.m4
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    35149 2022-11-27 18:53:34.000000 libcaes-20221127/COPYING
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      295 2022-11-27 18:53:34.000000 libcaes-20221127/README
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/libcaes/
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     2885 2022-11-27 18:53:35.000000 libcaes-20221127/libcaes/libcaes_tweaked_context.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1745 2022-11-27 18:53:35.000000 libcaes-20221127/libcaes/libcaes_definitions.h.in
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     4464 2022-11-27 18:53:35.000000 libcaes-20221127/libcaes/libcaes_context.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    33103 2022-11-27 18:53:35.000000 libcaes-20221127/libcaes/libcaes_tweaked_context.c
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      953 2018-09-02 17:00:22.000000 libcaes-20221127/libcaes/Makefile.am
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1075 2022-11-27 19:00:26.000000 libcaes-20221127/libcaes/libcaes.rc
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1077 2022-11-27 18:53:35.000000 libcaes-20221127/libcaes/libcaes.rc.in
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1185 2022-11-27 18:53:35.000000 libcaes-20221127/libcaes/libcaes_support.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1608 2022-11-27 18:53:35.000000 libcaes-20221127/libcaes/libcaes_types.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1109 2022-11-27 18:53:35.000000 libcaes-20221127/libcaes/libcaes_support.c
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    83342 2022-11-27 18:53:35.000000 libcaes-20221127/libcaes/libcaes_context.c
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1772 2022-11-27 18:53:35.000000 libcaes-20221127/libcaes/libcaes_error.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1400 2022-11-27 18:53:35.000000 libcaes-20221127/libcaes/libcaes_unused.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1743 2022-11-27 19:00:26.000000 libcaes-20221127/libcaes/libcaes_definitions.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1435 2022-11-27 18:53:35.000000 libcaes-20221127/libcaes/libcaes_libcerror.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    26308 2022-11-27 19:00:16.000000 libcaes-20221127/libcaes/Makefile.in
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1376 2022-11-27 18:53:35.000000 libcaes-20221127/libcaes/libcaes_extern.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1817 2022-11-27 18:53:35.000000 libcaes-20221127/libcaes/libcaes.c
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     2896 2022-11-27 18:53:35.000000 libcaes-20221127/libcaes/libcaes_error.c
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/include/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     6659 2022-11-27 19:00:26.000000 libcaes-20221127/include/libcaes.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      457 2022-11-27 18:53:34.000000 libcaes-20221127/include/Makefile.am
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/include/libcaes/
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1188 2022-11-27 18:53:35.000000 libcaes-20221127/include/libcaes/definitions.h.in
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1412 2022-11-27 18:53:35.000000 libcaes-20221127/include/libcaes/extern.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4849 2022-11-27 19:00:26.000000 libcaes-20221127/include/libcaes/types.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1221 2022-11-27 18:53:35.000000 libcaes-20221127/include/libcaes/features.h.in
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4980 2022-11-27 18:53:35.000000 libcaes-20221127/include/libcaes/types.h.in
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1221 2022-11-27 19:00:26.000000 libcaes-20221127/include/libcaes/features.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1186 2022-11-27 19:00:26.000000 libcaes-20221127/include/libcaes/definitions.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     6689 2022-11-27 18:53:35.000000 libcaes-20221127/include/libcaes/error.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    21990 2022-11-27 19:00:16.000000 libcaes-20221127/include/Makefile.in
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     6659 2022-11-27 18:53:35.000000 libcaes-20221127/include/libcaes.h.in
--rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)    15358 2022-11-27 19:00:16.000000 libcaes-20221127/install-sh
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/pycaes-python3/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1210 2022-11-27 18:53:34.000000 libcaes-20221127/pycaes-python3/Makefile.am
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    34318 2022-11-27 19:00:17.000000 libcaes-20221127/pycaes-python3/Makefile.in
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    15766 2022-11-27 19:00:16.000000 libcaes-20221127/INSTALL
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:20.000000 libcaes-20221127/dpkg/
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      120 2022-11-27 18:53:34.000000 libcaes-20221127/dpkg/changelog.in
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      139 2022-11-27 19:00:26.000000 libcaes-20221127/dpkg/changelog
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)       96 2022-11-27 18:53:34.000000 libcaes-20221127/dpkg/libcaes-dev.install
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1024 2022-11-27 18:53:36.000000 libcaes-20221127/dpkg/copyright
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:20.000000 libcaes-20221127/dpkg/source/
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)       12 2022-11-27 18:53:34.000000 libcaes-20221127/dpkg/source/format
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)       22 2022-11-27 18:53:34.000000 libcaes-20221127/dpkg/libcaes.install
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      704 2022-11-27 18:53:34.000000 libcaes-20221127/dpkg/rules
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)        3 2022-11-27 18:53:34.000000 libcaes-20221127/dpkg/compat
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)       18 2022-11-27 18:53:34.000000 libcaes-20221127/dpkg/libcaes-python3.install
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1555 2022-11-27 18:53:34.000000 libcaes-20221127/dpkg/control
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      200 2022-11-27 18:53:35.000000 libcaes-20221127/AUTHORS
--rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)    35409 2022-11-27 19:00:16.000000 libcaes-20221127/config.sub
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/pycaes-python2/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1210 2022-11-27 18:53:34.000000 libcaes-20221127/pycaes-python2/Makefile.am
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    34318 2022-11-27 19:00:16.000000 libcaes-20221127/pycaes-python2/Makefile.in
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/manuals/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     3172 2022-11-27 18:53:36.000000 libcaes-20221127/manuals/libcaes.3
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      130 2016-02-02 07:37:20.000000 libcaes-20221127/manuals/Makefile.am
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    19229 2022-11-27 19:00:16.000000 libcaes-20221127/manuals/Makefile.in
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/pycaes/
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1392 2022-11-27 18:53:35.000000 libcaes-20221127/pycaes/pycaes_unused.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1617 2022-11-27 18:53:35.000000 libcaes-20221127/pycaes/pycaes_crypt_modes.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1432 2022-11-27 18:53:35.000000 libcaes-20221127/pycaes/pycaes_libcerror.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    21284 2022-11-27 18:53:35.000000 libcaes-20221127/pycaes/pycaes_crypt.c
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      965 2022-11-27 18:53:35.000000 libcaes-20221127/pycaes/pycaes_libcaes.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     8942 2022-11-27 18:54:10.000000 libcaes-20221127/pycaes/pycaes_tweaked_context.c
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      739 2018-07-28 12:24:08.000000 libcaes-20221127/pycaes/Makefile.am
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1742 2022-11-27 18:53:35.000000 libcaes-20221127/pycaes/pycaes_crypt.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1739 2022-11-27 18:54:10.000000 libcaes-20221127/pycaes/pycaes_context.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1304 2022-11-27 18:53:35.000000 libcaes-20221127/pycaes/pycaes.h
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     5499 2022-11-27 18:53:35.000000 libcaes-20221127/pycaes/pycaes_crypt_modes.c
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1531 2022-11-27 18:53:35.000000 libcaes-20221127/pycaes/pycaes_error.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1916 2022-11-27 18:54:10.000000 libcaes-20221127/pycaes/pycaes_tweaked_context.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    33847 2022-11-27 19:00:17.000000 libcaes-20221127/pycaes/Makefile.in
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     6332 2022-11-27 18:54:10.000000 libcaes-20221127/pycaes/pycaes.c
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     9526 2022-11-27 18:53:35.000000 libcaes-20221127/pycaes/pycaes_error.c
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     2030 2022-11-27 18:53:35.000000 libcaes-20221127/pycaes/pycaes_python.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     7398 2022-11-27 18:54:10.000000 libcaes-20221127/pycaes/pycaes_context.c
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)       67 2022-07-10 14:47:45.000000 libcaes-20221127/ABOUT-NLS
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/msvscpp/
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/msvscpp/caes_test_support/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4626 2022-11-27 18:53:37.000000 libcaes-20221127/msvscpp/caes_test_support/caes_test_support.vcproj
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      570 2022-11-27 18:54:10.000000 libcaes-20221127/msvscpp/Makefile.am
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/msvscpp/libcaes/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     5391 2022-11-27 18:53:37.000000 libcaes-20221127/msvscpp/libcaes/libcaes.vcproj
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/msvscpp/caes_test_tweaked_context/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4893 2022-11-27 18:53:37.000000 libcaes-20221127/msvscpp/caes_test_tweaked_context/caes_test_tweaked_context.vcproj
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/msvscpp/caes_test_crypt_ccm/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4635 2022-11-27 18:54:10.000000 libcaes-20221127/msvscpp/caes_test_crypt_ccm/caes_test_crypt_ccm.vcproj
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/msvscpp/caes_test_crypt_cbc/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4635 2022-11-27 18:54:10.000000 libcaes-20221127/msvscpp/caes_test_crypt_cbc/caes_test_crypt_cbc.vcproj
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/msvscpp/pycaes/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     5513 2022-11-27 18:53:37.000000 libcaes-20221127/msvscpp/pycaes/pycaes.vcproj
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    16556 2022-11-27 19:00:16.000000 libcaes-20221127/msvscpp/Makefile.in
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/msvscpp/libcerror/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4488 2022-11-27 18:53:37.000000 libcaes-20221127/msvscpp/libcerror/libcerror.vcproj
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/msvscpp/caes_test_context/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4869 2022-11-27 18:53:37.000000 libcaes-20221127/msvscpp/caes_test_context/caes_test_context.vcproj
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/msvscpp/caes_test_crypt_xts/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4635 2022-11-27 18:54:10.000000 libcaes-20221127/msvscpp/caes_test_crypt_xts/caes_test_crypt_xts.vcproj
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/msvscpp/caes_test_error/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4620 2022-11-27 18:53:37.000000 libcaes-20221127/msvscpp/caes_test_error/caes_test_error.vcproj
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     7249 2022-11-27 18:54:10.000000 libcaes-20221127/msvscpp/libcaes.sln
--rwxrwxr-x   0 lordyesta  (1000) lordyesta  (1000)    10199 2022-11-27 18:53:37.000000 libcaes-20221127/setup.py
--rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)    49797 2022-11-27 19:00:16.000000 libcaes-20221127/config.guess
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 18:53:34.000000 libcaes-20221127/NEWS
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/ossfuzz/
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1496 2020-11-14 08:26:01.000000 libcaes-20221127/ossfuzz/Makefile.am
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1891 2022-11-27 18:53:35.000000 libcaes-20221127/ossfuzz/crypt_cbc_fuzzer.cc
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     2093 2022-11-27 18:53:35.000000 libcaes-20221127/ossfuzz/crypt_xts_fuzzer.cc
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1792 2022-11-27 18:53:35.000000 libcaes-20221127/ossfuzz/crypt_ccm_fuzzer.cc
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      967 2022-11-27 18:53:35.000000 libcaes-20221127/ossfuzz/ossfuzz_libcaes.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    29659 2022-11-27 19:00:16.000000 libcaes-20221127/ossfuzz/Makefile.in
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1701 2022-11-27 18:53:35.000000 libcaes-20221127/ossfuzz/crypt_ecb_fuzzer.cc
--rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)     4879 2022-11-27 19:00:17.000000 libcaes-20221127/test-driver
--rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)   939850 2022-11-27 19:00:15.000000 libcaes-20221127/configure
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      304 2022-11-27 18:53:34.000000 libcaes-20221127/libcaes.pc.in
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     2288 2022-11-27 18:53:34.000000 libcaes-20221127/libcaes.spec.in
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    34352 2022-11-27 19:00:16.000000 libcaes-20221127/Makefile.in
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      650 2019-12-24 12:39:01.000000 libcaes-20221127/ChangeLog
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:20.000000 libcaes-20221127/m4/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    14488 2022-07-10 14:47:46.000000 libcaes-20221127/m4/gettext.m4
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      756 2020-07-22 06:56:10.000000 libcaes-20221127/m4/tests.m4
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    11944 2022-07-10 14:47:46.000000 libcaes-20221127/m4/lib-prefix.m4
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    14525 2022-11-27 19:00:12.000000 libcaes-20221127/m4/ltoptions.m4
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     5370 2022-07-10 14:47:46.000000 libcaes-20221127/m4/lib-ld.m4
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    34802 2022-07-10 14:47:46.000000 libcaes-20221127/m4/lib-link.m4
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    17674 2021-11-16 20:59:07.000000 libcaes-20221127/m4/python.m4
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)   307188 2022-11-27 19:00:12.000000 libcaes-20221127/m4/libtool.m4
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1234 2022-07-10 14:47:46.000000 libcaes-20221127/m4/nls.m4
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    22432 2022-07-10 14:47:46.000000 libcaes-20221127/m4/host-cpu-c-abi.m4
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      714 2022-11-27 19:00:12.000000 libcaes-20221127/m4/ltversion.m4
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     3090 2022-07-10 14:47:46.000000 libcaes-20221127/m4/progtest.m4
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     6151 2022-11-27 19:00:12.000000 libcaes-20221127/m4/lt~obsolete.m4
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    27306 2022-11-27 18:51:02.000000 libcaes-20221127/m4/libcrypto.m4
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    18831 2022-07-10 14:47:46.000000 libcaes-20221127/m4/po.m4
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    14115 2018-12-18 07:27:30.000000 libcaes-20221127/m4/common.m4
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     6260 2019-03-18 05:41:01.000000 libcaes-20221127/m4/libcerror.m4
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     9731 2022-07-10 14:47:46.000000 libcaes-20221127/m4/iconv.m4
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4395 2022-11-27 19:00:12.000000 libcaes-20221127/m4/ltsugar.m4
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     3229 2022-07-10 14:47:46.000000 libcaes-20221127/m4/intlmacosx.m4
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     2058 2018-07-28 03:37:28.000000 libcaes-20221127/m4/types.m4
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     7652 2022-11-27 18:53:34.000000 libcaes-20221127/COPYING.LESSER
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/libcerror/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    15420 2022-11-27 19:00:08.000000 libcaes-20221127/libcerror/libcerror_system.c
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    19408 2022-11-27 19:00:08.000000 libcaes-20221127/libcerror/libcerror_error.c
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1402 2022-11-27 19:00:08.000000 libcaes-20221127/libcerror/libcerror_extern.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      605 2022-11-27 19:00:08.000000 libcaes-20221127/libcerror/Makefile.am
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     2880 2022-11-27 19:00:08.000000 libcaes-20221127/libcerror/libcerror_error.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1238 2022-11-27 19:00:08.000000 libcaes-20221127/libcerror/libcerror_support.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1522 2022-11-27 19:00:08.000000 libcaes-20221127/libcerror/libcerror_types.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     7629 2022-11-27 19:00:08.000000 libcaes-20221127/libcerror/libcerror_definitions.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1416 2022-11-27 19:00:08.000000 libcaes-20221127/libcerror/libcerror_unused.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    23375 2022-11-27 19:00:16.000000 libcaes-20221127/libcerror/Makefile.in
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1158 2022-11-27 19:00:08.000000 libcaes-20221127/libcerror/libcerror_support.c
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     2026 2022-11-27 19:00:08.000000 libcaes-20221127/libcerror/libcerror_system.h
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)   332808 2022-11-27 19:00:12.000000 libcaes-20221127/ltmain.sh
--rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)     7400 2022-11-27 19:00:16.000000 libcaes-20221127/compile
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     2172 2022-11-27 19:00:26.000000 libcaes-20221127/libcaes.spec
--rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)    18574 2022-07-10 14:47:52.000000 libcaes-20221127/config.rpath
--rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)    23568 2022-11-27 19:00:17.000000 libcaes-20221127/depcomp
-drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2022-11-27 19:10:21.000000 libcaes-20221127/po/
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1204 2022-07-10 14:47:45.000000 libcaes-20221127/po/en@quot.header
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     2395 2022-07-10 14:47:45.000000 libcaes-20221127/po/Rules-quot
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)       59 2013-03-31 11:48:44.000000 libcaes-20221127/po/POTFILES.in
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      720 2022-07-10 14:47:45.000000 libcaes-20221127/po/remove-potcdate.sin
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1808 2013-03-31 11:48:44.000000 libcaes-20221127/po/Makevars.in
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)       50 2016-11-06 11:55:10.000000 libcaes-20221127/po/ChangeLog
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1338 2022-07-10 14:47:45.000000 libcaes-20221127/po/en@boldquot.header
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      153 2022-07-10 14:47:45.000000 libcaes-20221127/po/quot.sed
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1809 2022-11-27 19:00:26.000000 libcaes-20221127/po/Makevars
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      906 2022-07-10 14:47:45.000000 libcaes-20221127/po/insert-header.sin
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    19571 2022-07-10 14:47:45.000000 libcaes-20221127/po/Makefile.in.in
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      217 2022-07-10 14:47:45.000000 libcaes-20221127/po/boldquot.sed
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1489 2022-11-27 18:53:34.000000 libcaes-20221127/acinclude.m4
--rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     3760 2022-11-27 18:53:34.000000 libcaes-20221127/configure.ac
--rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      439 2022-11-27 19:10:22.744616 libcaes-20221127/PKG-INFO
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/common/
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1157 2023-04-06 02:42:05.000000 libcaes-20230406/common/config_msc.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    10437 2023-04-06 02:42:05.000000 libcaes-20230406/common/byte_stream.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1250 2023-04-06 02:42:05.000000 libcaes-20230406/common/common.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     4611 2023-04-06 02:42:05.000000 libcaes-20230406/common/system_string.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      378 2023-04-06 02:42:03.000000 libcaes-20230406/common/Makefile.am
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     7234 2023-04-07 05:34:56.000000 libcaes-20230406/common/types.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     7236 2023-04-06 02:42:05.000000 libcaes-20230406/common/types.h.in
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     2243 2023-04-06 02:42:05.000000 libcaes-20230406/common/config_winapi.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     3259 2023-04-06 02:42:05.000000 libcaes-20230406/common/memory.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    11096 2023-04-06 03:22:55.000000 libcaes-20230406/common/config.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     5419 2023-04-06 02:42:05.000000 libcaes-20230406/common/narrow_string.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    19030 2023-04-07 05:34:45.000000 libcaes-20230406/common/Makefile.in
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     3878 2023-04-06 02:42:05.000000 libcaes-20230406/common/file_stream.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      957 2023-04-06 02:42:05.000000 libcaes-20230406/common/config_borlandc.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    10484 2023-04-07 05:34:44.000000 libcaes-20230406/common/config.h.in
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     5064 2023-04-06 02:42:05.000000 libcaes-20230406/common/wide_string.h
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/tests/
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     4653 2023-04-06 02:42:06.000000 libcaes-20230406/tests/caes_test_memory.c
+-rwxrwxr-x   0 lordyesta  (1000) lordyesta  (1000)     3801 2023-04-06 02:42:06.000000 libcaes-20230406/tests/test_library.sh
+-rwxrwxr-x   0 lordyesta  (1000) lordyesta  (1000)     3410 2023-04-06 02:42:06.000000 libcaes-20230406/tests/test_python_module.sh
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1152 2023-04-06 02:42:06.000000 libcaes-20230406/tests/pycaes_test_support.py
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)   268872 2023-04-06 02:42:06.000000 libcaes-20230406/tests/caes_test_crypt_xts.c
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     2240 2023-04-06 02:42:27.000000 libcaes-20230406/tests/Makefile.am
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)  1216152 2023-04-06 02:42:27.000000 libcaes-20230406/tests/caes_test_context.c
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)   175372 2023-04-06 02:42:06.000000 libcaes-20230406/tests/pycaes_test_crypt_cbc.py
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)   177604 2023-04-06 02:42:06.000000 libcaes-20230406/tests/caes_test_crypt_cbc.c
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)   174565 2023-04-06 02:42:06.000000 libcaes-20230406/tests/pycaes_test_crypt_ecb.py
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     8539 2023-04-06 02:42:06.000000 libcaes-20230406/tests/caes_test_macros.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     3099 2023-04-06 02:42:06.000000 libcaes-20230406/tests/caes_test_error.c
+-rwxrw-r--   0 lordyesta  (1000) lordyesta  (1000)     1645 2023-04-06 02:42:06.000000 libcaes-20230406/tests/test_manpage.sh
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     2056 2023-04-06 02:42:06.000000 libcaes-20230406/tests/caes_test_support.c
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1536 2023-04-06 02:42:06.000000 libcaes-20230406/tests/caes_test_unused.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    37784 2023-04-06 02:42:06.000000 libcaes-20230406/tests/test_runner.sh
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    28105 2023-04-06 02:42:27.000000 libcaes-20230406/tests/caes_test_tweaked_context.c
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)   271703 2023-04-06 02:42:06.000000 libcaes-20230406/tests/pycaes_test_crypt_xts.py
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    42707 2023-04-07 05:34:45.000000 libcaes-20230406/tests/Makefile.in
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      973 2023-04-06 02:42:06.000000 libcaes-20230406/tests/caes_test_libcaes.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1691 2023-04-06 02:42:06.000000 libcaes-20230406/tests/caes_test_memory.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     6243 2023-04-06 02:42:06.000000 libcaes-20230406/tests/caes_test_crypt_ccm.c
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1441 2023-04-06 02:42:06.000000 libcaes-20230406/tests/caes_test_libcerror.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     3434 2023-04-06 02:42:06.000000 libcaes-20230406/tests/pycaes_test_crypt_ccm.py
+-rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)     6878 2023-04-07 05:34:45.000000 libcaes-20230406/missing
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1747 2022-04-24 06:42:24.000000 libcaes-20230406/Makefile.am
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    55609 2023-04-07 05:34:43.000000 libcaes-20230406/aclocal.m4
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    35149 2023-04-06 02:42:03.000000 libcaes-20230406/COPYING
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      295 2023-04-06 02:42:03.000000 libcaes-20230406/README
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/libcaes/
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     2885 2023-04-06 02:42:05.000000 libcaes-20230406/libcaes/libcaes_tweaked_context.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1745 2023-04-06 02:42:05.000000 libcaes-20230406/libcaes/libcaes_definitions.h.in
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     4464 2023-04-06 02:42:05.000000 libcaes-20230406/libcaes/libcaes_context.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    33103 2023-04-06 02:42:05.000000 libcaes-20230406/libcaes/libcaes_tweaked_context.c
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      953 2018-09-02 17:00:22.000000 libcaes-20230406/libcaes/Makefile.am
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1075 2023-04-07 05:34:56.000000 libcaes-20230406/libcaes/libcaes.rc
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1077 2023-04-06 02:42:05.000000 libcaes-20230406/libcaes/libcaes.rc.in
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1185 2023-04-06 02:42:05.000000 libcaes-20230406/libcaes/libcaes_support.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1608 2023-04-06 02:42:05.000000 libcaes-20230406/libcaes/libcaes_types.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1109 2023-04-06 02:42:05.000000 libcaes-20230406/libcaes/libcaes_support.c
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    82616 2023-04-06 03:18:40.000000 libcaes-20230406/libcaes/libcaes_context.c
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1772 2023-04-06 02:42:05.000000 libcaes-20230406/libcaes/libcaes_error.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1400 2023-04-06 02:42:05.000000 libcaes-20230406/libcaes/libcaes_unused.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1743 2023-04-07 05:34:56.000000 libcaes-20230406/libcaes/libcaes_definitions.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1435 2023-04-06 02:42:05.000000 libcaes-20230406/libcaes/libcaes_libcerror.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    26308 2023-04-07 05:34:45.000000 libcaes-20230406/libcaes/Makefile.in
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1376 2023-04-06 02:42:05.000000 libcaes-20230406/libcaes/libcaes_extern.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1817 2023-04-06 02:42:05.000000 libcaes-20230406/libcaes/libcaes.c
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     2896 2023-04-06 02:42:05.000000 libcaes-20230406/libcaes/libcaes_error.c
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/include/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     6659 2023-04-07 05:34:56.000000 libcaes-20230406/include/libcaes.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      457 2023-04-06 02:42:03.000000 libcaes-20230406/include/Makefile.am
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/include/libcaes/
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1188 2023-04-06 02:42:05.000000 libcaes-20230406/include/libcaes/definitions.h.in
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1412 2023-04-06 02:42:05.000000 libcaes-20230406/include/libcaes/extern.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4849 2023-04-07 05:34:56.000000 libcaes-20230406/include/libcaes/types.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1221 2023-04-06 02:42:05.000000 libcaes-20230406/include/libcaes/features.h.in
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4980 2023-04-06 02:42:05.000000 libcaes-20230406/include/libcaes/types.h.in
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1221 2023-04-07 05:34:56.000000 libcaes-20230406/include/libcaes/features.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1186 2023-04-07 05:34:56.000000 libcaes-20230406/include/libcaes/definitions.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     6689 2023-04-06 02:42:05.000000 libcaes-20230406/include/libcaes/error.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    21990 2023-04-07 05:34:45.000000 libcaes-20230406/include/Makefile.in
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     6659 2023-04-06 02:42:05.000000 libcaes-20230406/include/libcaes.h.in
+-rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)    15358 2023-04-07 05:34:45.000000 libcaes-20230406/install-sh
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/pycaes-python3/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1210 2023-04-06 02:42:04.000000 libcaes-20230406/pycaes-python3/Makefile.am
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    34318 2023-04-07 05:34:45.000000 libcaes-20230406/pycaes-python3/Makefile.in
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    15766 2023-04-07 05:34:45.000000 libcaes-20230406/INSTALL
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/dpkg/
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      120 2023-04-06 02:42:03.000000 libcaes-20230406/dpkg/changelog.in
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      139 2023-04-07 05:34:56.000000 libcaes-20230406/dpkg/changelog
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)       96 2023-04-06 02:42:03.000000 libcaes-20230406/dpkg/libcaes-dev.install
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1024 2023-04-06 02:42:06.000000 libcaes-20230406/dpkg/copyright
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/dpkg/source/
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)       12 2023-04-06 02:42:03.000000 libcaes-20230406/dpkg/source/format
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)       22 2023-04-06 02:42:03.000000 libcaes-20230406/dpkg/libcaes.install
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      704 2023-04-06 02:42:03.000000 libcaes-20230406/dpkg/rules
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)        3 2023-04-06 02:42:03.000000 libcaes-20230406/dpkg/compat
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)       18 2023-04-06 02:42:03.000000 libcaes-20230406/dpkg/libcaes-python3.install
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1555 2023-04-06 02:42:03.000000 libcaes-20230406/dpkg/control
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      200 2023-04-06 02:42:05.000000 libcaes-20230406/AUTHORS
+-rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)    35409 2023-04-07 05:34:45.000000 libcaes-20230406/config.sub
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/pycaes-python2/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1210 2023-04-06 02:42:04.000000 libcaes-20230406/pycaes-python2/Makefile.am
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    34318 2023-04-07 05:34:45.000000 libcaes-20230406/pycaes-python2/Makefile.in
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/manuals/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     3172 2023-04-06 02:42:06.000000 libcaes-20230406/manuals/libcaes.3
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      130 2016-02-02 07:37:20.000000 libcaes-20230406/manuals/Makefile.am
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    19229 2023-04-07 05:34:45.000000 libcaes-20230406/manuals/Makefile.in
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/pycaes/
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1392 2023-04-06 02:42:06.000000 libcaes-20230406/pycaes/pycaes_unused.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1617 2023-04-06 02:42:06.000000 libcaes-20230406/pycaes/pycaes_crypt_modes.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1432 2023-04-06 02:42:06.000000 libcaes-20230406/pycaes/pycaes_libcerror.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    21284 2023-04-06 02:42:06.000000 libcaes-20230406/pycaes/pycaes_crypt.c
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      965 2023-04-06 02:42:06.000000 libcaes-20230406/pycaes/pycaes_libcaes.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     8942 2023-04-06 02:42:40.000000 libcaes-20230406/pycaes/pycaes_tweaked_context.c
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      739 2018-07-28 12:24:08.000000 libcaes-20230406/pycaes/Makefile.am
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1742 2023-04-06 02:42:06.000000 libcaes-20230406/pycaes/pycaes_crypt.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1739 2023-04-06 02:42:40.000000 libcaes-20230406/pycaes/pycaes_context.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1304 2023-04-06 02:42:06.000000 libcaes-20230406/pycaes/pycaes.h
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     5499 2023-04-06 02:42:06.000000 libcaes-20230406/pycaes/pycaes_crypt_modes.c
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1531 2023-04-06 02:42:06.000000 libcaes-20230406/pycaes/pycaes_error.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1916 2023-04-06 02:42:40.000000 libcaes-20230406/pycaes/pycaes_tweaked_context.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    33847 2023-04-07 05:34:45.000000 libcaes-20230406/pycaes/Makefile.in
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     6327 2023-04-06 02:42:40.000000 libcaes-20230406/pycaes/pycaes.c
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     9526 2023-04-06 02:42:06.000000 libcaes-20230406/pycaes/pycaes_error.c
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     2030 2023-04-06 02:42:06.000000 libcaes-20230406/pycaes/pycaes_python.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     7398 2023-04-06 02:42:40.000000 libcaes-20230406/pycaes/pycaes_context.c
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)       67 2022-07-10 14:47:45.000000 libcaes-20230406/ABOUT-NLS
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/msvscpp/
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/msvscpp/caes_test_support/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4626 2023-04-06 02:42:08.000000 libcaes-20230406/msvscpp/caes_test_support/caes_test_support.vcproj
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      570 2023-04-06 02:42:27.000000 libcaes-20230406/msvscpp/Makefile.am
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/msvscpp/libcaes/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     5391 2023-04-06 02:42:08.000000 libcaes-20230406/msvscpp/libcaes/libcaes.vcproj
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/msvscpp/caes_test_tweaked_context/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4893 2023-04-06 02:42:08.000000 libcaes-20230406/msvscpp/caes_test_tweaked_context/caes_test_tweaked_context.vcproj
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/msvscpp/caes_test_crypt_ccm/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4635 2023-04-06 02:42:27.000000 libcaes-20230406/msvscpp/caes_test_crypt_ccm/caes_test_crypt_ccm.vcproj
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/msvscpp/caes_test_crypt_cbc/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4635 2023-04-06 02:42:27.000000 libcaes-20230406/msvscpp/caes_test_crypt_cbc/caes_test_crypt_cbc.vcproj
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/msvscpp/pycaes/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     5513 2023-04-06 02:42:08.000000 libcaes-20230406/msvscpp/pycaes/pycaes.vcproj
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    16556 2023-04-07 05:34:45.000000 libcaes-20230406/msvscpp/Makefile.in
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/msvscpp/libcerror/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4488 2023-04-06 02:42:08.000000 libcaes-20230406/msvscpp/libcerror/libcerror.vcproj
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/msvscpp/caes_test_context/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4869 2023-04-06 02:42:08.000000 libcaes-20230406/msvscpp/caes_test_context/caes_test_context.vcproj
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/msvscpp/caes_test_crypt_xts/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4635 2023-04-06 02:42:27.000000 libcaes-20230406/msvscpp/caes_test_crypt_xts/caes_test_crypt_xts.vcproj
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/msvscpp/caes_test_error/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4620 2023-04-06 02:42:08.000000 libcaes-20230406/msvscpp/caes_test_error/caes_test_error.vcproj
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     7249 2023-04-06 02:42:27.000000 libcaes-20230406/msvscpp/libcaes.sln
+-rwxrwxr-x   0 lordyesta  (1000) lordyesta  (1000)    11454 2023-04-06 02:42:08.000000 libcaes-20230406/setup.py
+-rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)    49797 2023-04-07 05:34:45.000000 libcaes-20230406/config.guess
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-06 02:42:03.000000 libcaes-20230406/NEWS
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/ossfuzz/
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1496 2020-11-14 08:26:01.000000 libcaes-20230406/ossfuzz/Makefile.am
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1891 2023-04-06 02:42:05.000000 libcaes-20230406/ossfuzz/crypt_cbc_fuzzer.cc
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     2093 2023-04-06 02:42:05.000000 libcaes-20230406/ossfuzz/crypt_xts_fuzzer.cc
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1792 2023-04-06 02:42:05.000000 libcaes-20230406/ossfuzz/crypt_ccm_fuzzer.cc
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      967 2023-04-06 02:42:05.000000 libcaes-20230406/ossfuzz/ossfuzz_libcaes.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    29659 2023-04-07 05:34:45.000000 libcaes-20230406/ossfuzz/Makefile.in
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1701 2023-04-06 02:42:05.000000 libcaes-20230406/ossfuzz/crypt_ecb_fuzzer.cc
+-rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)     4879 2023-04-07 05:34:45.000000 libcaes-20230406/test-driver
+-rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)   939850 2023-04-07 05:34:44.000000 libcaes-20230406/configure
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      304 2023-04-06 02:42:03.000000 libcaes-20230406/libcaes.pc.in
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     2288 2023-04-06 02:42:03.000000 libcaes-20230406/libcaes.spec.in
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    34352 2023-04-07 05:34:45.000000 libcaes-20230406/Makefile.in
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      719 2023-04-06 02:46:42.000000 libcaes-20230406/ChangeLog
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/m4/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    14488 2022-07-10 14:47:46.000000 libcaes-20230406/m4/gettext.m4
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)      756 2020-07-22 06:56:10.000000 libcaes-20230406/m4/tests.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    11944 2022-07-10 14:47:46.000000 libcaes-20230406/m4/lib-prefix.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    14525 2023-04-07 05:34:40.000000 libcaes-20230406/m4/ltoptions.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     5370 2022-07-10 14:47:46.000000 libcaes-20230406/m4/lib-ld.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    34802 2022-07-10 14:47:46.000000 libcaes-20230406/m4/lib-link.m4
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    17674 2021-11-16 20:59:07.000000 libcaes-20230406/m4/python.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)   307188 2023-04-07 05:34:40.000000 libcaes-20230406/m4/libtool.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1234 2022-07-10 14:47:46.000000 libcaes-20230406/m4/nls.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    22432 2022-07-10 14:47:46.000000 libcaes-20230406/m4/host-cpu-c-abi.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      714 2023-04-07 05:34:40.000000 libcaes-20230406/m4/ltversion.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     3090 2022-07-10 14:47:46.000000 libcaes-20230406/m4/progtest.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     6151 2023-04-07 05:34:40.000000 libcaes-20230406/m4/lt~obsolete.m4
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    27306 2022-11-27 18:51:02.000000 libcaes-20230406/m4/libcrypto.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    18831 2022-07-10 14:47:46.000000 libcaes-20230406/m4/po.m4
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)    14115 2018-12-18 07:27:30.000000 libcaes-20230406/m4/common.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     6260 2019-03-18 05:41:01.000000 libcaes-20230406/m4/libcerror.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     9731 2022-07-10 14:47:46.000000 libcaes-20230406/m4/iconv.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     4395 2023-04-07 05:34:40.000000 libcaes-20230406/m4/ltsugar.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     3229 2022-07-10 14:47:46.000000 libcaes-20230406/m4/intlmacosx.m4
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     2058 2018-07-28 03:37:28.000000 libcaes-20230406/m4/types.m4
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     7652 2023-04-06 02:42:03.000000 libcaes-20230406/COPYING.LESSER
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/libcerror/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    15420 2023-04-07 05:34:34.000000 libcaes-20230406/libcerror/libcerror_system.c
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    19408 2023-04-07 05:34:34.000000 libcaes-20230406/libcerror/libcerror_error.c
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1402 2023-04-07 05:34:34.000000 libcaes-20230406/libcerror/libcerror_extern.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      605 2023-04-07 05:34:34.000000 libcaes-20230406/libcerror/Makefile.am
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     2880 2023-04-07 05:34:34.000000 libcaes-20230406/libcerror/libcerror_error.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1238 2023-04-07 05:34:34.000000 libcaes-20230406/libcerror/libcerror_support.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1522 2023-04-07 05:34:34.000000 libcaes-20230406/libcerror/libcerror_types.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     7629 2023-04-07 05:34:34.000000 libcaes-20230406/libcerror/libcerror_definitions.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1416 2023-04-07 05:34:34.000000 libcaes-20230406/libcerror/libcerror_unused.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    23375 2023-04-07 05:34:45.000000 libcaes-20230406/libcerror/Makefile.in
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1158 2023-04-07 05:34:34.000000 libcaes-20230406/libcerror/libcerror_support.c
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     2026 2023-04-07 05:34:34.000000 libcaes-20230406/libcerror/libcerror_system.h
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)   332808 2023-04-07 05:34:40.000000 libcaes-20230406/ltmain.sh
+-rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)     7400 2023-04-07 05:34:45.000000 libcaes-20230406/compile
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     2172 2023-04-07 05:34:56.000000 libcaes-20230406/libcaes.spec
+-rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)    18574 2022-07-10 14:47:52.000000 libcaes-20230406/config.rpath
+-rwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)    23568 2023-04-07 05:34:45.000000 libcaes-20230406/depcomp
+drwxr-xr-x   0 lordyesta  (1000) lordyesta  (1000)        0 2023-04-07 05:43:29.000000 libcaes-20230406/po/
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1204 2022-07-10 14:47:45.000000 libcaes-20230406/po/en@quot.header
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     2395 2022-07-10 14:47:45.000000 libcaes-20230406/po/Rules-quot
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)       59 2013-03-31 11:48:44.000000 libcaes-20230406/po/POTFILES.in
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      720 2022-07-10 14:47:45.000000 libcaes-20230406/po/remove-potcdate.sin
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1808 2013-03-31 11:48:44.000000 libcaes-20230406/po/Makevars.in
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)       50 2016-11-06 11:55:10.000000 libcaes-20230406/po/ChangeLog
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1338 2022-07-10 14:47:45.000000 libcaes-20230406/po/en@boldquot.header
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      153 2022-07-10 14:47:45.000000 libcaes-20230406/po/quot.sed
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     1809 2023-04-07 05:34:56.000000 libcaes-20230406/po/Makevars
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      906 2022-07-10 14:47:45.000000 libcaes-20230406/po/insert-header.sin
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)    19571 2022-07-10 14:47:45.000000 libcaes-20230406/po/Makefile.in.in
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      217 2022-07-10 14:47:45.000000 libcaes-20230406/po/boldquot.sed
+-rw-rw-r--   0 lordyesta  (1000) lordyesta  (1000)     1489 2023-04-06 02:42:03.000000 libcaes-20230406/acinclude.m4
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)     3760 2023-04-06 02:46:42.000000 libcaes-20230406/configure.ac
+-rw-r--r--   0 lordyesta  (1000) lordyesta  (1000)      347 2023-04-07 05:43:30.976472 libcaes-20230406/PKG-INFO
```

### Comparing `libcaes-20221127/common/config_msc.h` & `libcaes-20230406/common/config_msc.h`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Configuration for the Microsoft Visual Studio C++ compiler
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/common/byte_stream.h` & `libcaes-20230406/common/byte_stream.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Byte stream functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/common/common.h` & `libcaes-20230406/common/common.h`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Common include file
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/common/system_string.h` & `libcaes-20230406/common/system_string.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * System character string functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/common/types.h` & `libcaes-20230406/common/types.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Type and type-support definitions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/common/types.h.in` & `libcaes-20230406/common/types.h.in`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Type and type-support definitions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/common/config_winapi.h` & `libcaes-20230406/common/config_winapi.h`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Configuration file for WINAPI
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/common/memory.h` & `libcaes-20230406/common/memory.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Memory functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/common/config.h` & `libcaes-20230406/common/config.h`

 * *Files 1% similar despite different names*

```diff
@@ -322,24 +322,24 @@
 /* Define to the address where bug reports for this package should be sent. */
 #define PACKAGE_BUGREPORT "joachim.metz@gmail.com"
 
 /* Define to the full name of this package. */
 #define PACKAGE_NAME "libcaes"
 
 /* Define to the full name and version of this package. */
-#define PACKAGE_STRING "libcaes 20221127"
+#define PACKAGE_STRING "libcaes 20230406"
 
 /* Define to the one symbol short name of this package. */
 #define PACKAGE_TARNAME "libcaes"
 
 /* Define to the home page for this package. */
 #define PACKAGE_URL ""
 
 /* Define to the version of this package. */
-#define PACKAGE_VERSION "20221127"
+#define PACKAGE_VERSION "20230406"
 
 /* The size of `int', as computed by sizeof. */
 #define SIZEOF_INT 4
 
 /* The size of `long', as computed by sizeof. */
 #define SIZEOF_LONG 8
 
@@ -357,15 +357,15 @@
    backward compatibility; new code need not use it. */
 #define STDC_HEADERS 1
 
 /* Define to 1 if strerror_r returns char *. */
 /* #undef STRERROR_R_CHAR_P */
 
 /* Version number of package */
-#define VERSION "20221127"
+#define VERSION "20230406"
 
 /* Number of bits in a file offset, on hosts where this is settable. */
 /* #undef _FILE_OFFSET_BITS */
 
 /* Define for large files, on AIX-style hosts. */
 /* #undef _LARGE_FILES */
```

### Comparing `libcaes-20221127/common/narrow_string.h` & `libcaes-20230406/common/narrow_string.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Narrow character string functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/common/Makefile.in` & `libcaes-20230406/common/Makefile.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/common/file_stream.h` & `libcaes-20230406/common/file_stream.h`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * FILE stream functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/common/config_borlandc.h` & `libcaes-20230406/common/config_borlandc.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Configuration for the Borland/CodeGear C++ Builder compiler
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/common/config.h.in` & `libcaes-20230406/common/config.h.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/common/wide_string.h` & `libcaes-20230406/common/wide_string.h`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Wide character string functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/caes_test_memory.c` & `libcaes-20230406/tests/caes_test_memory.c`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Memory allocation functions for testing
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/test_library.sh` & `libcaes-20230406/tests/test_library.sh`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/tests/test_python_module.sh` & `libcaes-20230406/tests/test_python_module.sh`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/tests/pycaes_test_support.py` & `libcaes-20230406/tests/pycaes_test_support.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 #!/usr/bin/env python
 #
 # Python-bindings support functions test script
 #
-# Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+# Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
 #
 # Refer to AUTHORS for acknowledgements.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU Lesser General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/caes_test_crypt_xts.c` & `libcaes-20230406/tests/caes_test_crypt_xts.c`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Library AES-XTS de/encryption testing program
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/Makefile.am` & `libcaes-20230406/tests/Makefile.am`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/tests/caes_test_context.c` & `libcaes-20230406/tests/caes_test_context.c`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Library context type test program
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/pycaes_test_crypt_cbc.py` & `libcaes-20230406/tests/pycaes_test_crypt_cbc.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 #!/usr/bin/env python
 #
 # Python-bindings AES-CBC de/encryption testing program
 #
-# Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+# Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
 #
 # Refer to AUTHORS for acknowledgements.
 #
 # This software is free software: you can redistribute it and/or modify
 # it under the terms of the GNU Lesser General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/caes_test_crypt_cbc.c` & `libcaes-20230406/tests/caes_test_crypt_cbc.c`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Library AES-CBC de/encryption testing program
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/pycaes_test_crypt_ecb.py` & `libcaes-20230406/tests/pycaes_test_crypt_ecb.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 #!/usr/bin/env python
 #
 # Python-bindings AES-ECB de/encryption testing program
 #
-# Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+# Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
 #
 # Refer to AUTHORS for acknowledgements.
 #
 # This software is free software: you can redistribute it and/or modify
 # it under the terms of the GNU Lesser General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/caes_test_macros.h` & `libcaes-20230406/tests/caes_test_macros.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Macros for testing
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/caes_test_error.c` & `libcaes-20230406/tests/caes_test_error.c`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Library error functions test program
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/test_manpage.sh` & `libcaes-20230406/tests/test_manpage.sh`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/tests/caes_test_support.c` & `libcaes-20230406/tests/caes_test_support.c`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Library support functions test program
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/caes_test_unused.h` & `libcaes-20230406/tests/caes_test_unused.h`

 * *Files 7% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Definitions to silence compiler warnings about unused function attributes/parameters.
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/test_runner.sh` & `libcaes-20230406/tests/test_runner.sh`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/tests/caes_test_tweaked_context.c` & `libcaes-20230406/tests/caes_test_tweaked_context.c`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Library tweaked_context type test program
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/pycaes_test_crypt_xts.py` & `libcaes-20230406/tests/pycaes_test_crypt_xts.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 #!/usr/bin/env python
 #
 # Python-bindings AES-XTS de/encryption testing program
 #
-# Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+# Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
 #
 # Refer to AUTHORS for acknowledgements.
 #
 # This software is free software: you can redistribute it and/or modify
 # it under the terms of the GNU Lesser General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/Makefile.in` & `libcaes-20230406/tests/Makefile.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/tests/caes_test_libcaes.h` & `libcaes-20230406/tests/caes_test_libcaes.h`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * The libcaes header wrapper
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/caes_test_memory.h` & `libcaes-20230406/tests/caes_test_memory.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Memory allocation functions for testing
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/caes_test_crypt_ccm.c` & `libcaes-20230406/tests/caes_test_crypt_ccm.c`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Library AES-CCM de/encryption testing program
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/caes_test_libcerror.h` & `libcaes-20230406/tests/caes_test_libcerror.h`

 * *Files 8% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * The libcerror header wrapper
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/tests/pycaes_test_crypt_ccm.py` & `libcaes-20230406/tests/pycaes_test_crypt_ccm.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 #!/usr/bin/env python
 #
 # Python-bindings AES-CCM de/encryption testing program
 #
-# Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+# Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
 #
 # Refer to AUTHORS for acknowledgements.
 #
 # This software is free software: you can redistribute it and/or modify
 # it under the terms of the GNU Lesser General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.
```

### Comparing `libcaes-20221127/missing` & `libcaes-20230406/missing`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/Makefile.am` & `libcaes-20230406/Makefile.am`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/aclocal.m4` & `libcaes-20230406/aclocal.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/COPYING` & `libcaes-20230406/COPYING`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcaes/libcaes_tweaked_context.h` & `libcaes-20230406/libcaes/libcaes_tweaked_context.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * AES tweaked de/encryption context functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/libcaes/libcaes_definitions.h.in` & `libcaes-20230406/libcaes/libcaes_definitions.h.in`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * The internal definitions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/libcaes/libcaes_context.h` & `libcaes-20230406/libcaes/libcaes_context.h`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * AES de/encryption context functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/libcaes/libcaes_tweaked_context.c` & `libcaes-20230406/libcaes/libcaes_tweaked_context.c`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * AES encryption functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/libcaes/Makefile.am` & `libcaes-20230406/libcaes/Makefile.am`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcaes/libcaes.rc` & `libcaes-20230406/libcaes/libcaes.rc.in`

 * *Files 4% similar despite different names*

```diff
@@ -18,20 +18,20 @@
   FILESUBTYPE				0x0L
 BEGIN
   BLOCK "StringFileInfo"
   BEGIN
     BLOCK "040904E4"
     BEGIN
       VALUE "FileDescription",		"Library to support cross-platform AES encryption\0"
-      VALUE "FileVersion",		"20221127" "\0"
+      VALUE "FileVersion",		"@VERSION@" "\0"
       VALUE "InternalName",		"libcaes.dll\0"
-      VALUE "LegalCopyright",		"(C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>\0"
+      VALUE "LegalCopyright",		"(C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>\0"
       VALUE "OriginalFilename",		"libcaes.dll\0"
       VALUE "ProductName",		"libcaes\0"
-      VALUE "ProductVersion",		"20221127" "\0"
+      VALUE "ProductVersion",		"@VERSION@" "\0"
       VALUE "Comments",			"For more information visit https://github.com/libyal/libcaes/\0"
     END
   END
   BLOCK "VarFileInfo"
   BEGIN
     VALUE "Translation", 0x0409, 1200
   END
```

### Comparing `libcaes-20221127/libcaes/libcaes.rc.in` & `libcaes-20230406/libcaes/libcaes.rc`

 * *Files 11% similar despite different names*

```diff
@@ -18,20 +18,20 @@
   FILESUBTYPE				0x0L
 BEGIN
   BLOCK "StringFileInfo"
   BEGIN
     BLOCK "040904E4"
     BEGIN
       VALUE "FileDescription",		"Library to support cross-platform AES encryption\0"
-      VALUE "FileVersion",		"@VERSION@" "\0"
+      VALUE "FileVersion",		"20230406" "\0"
       VALUE "InternalName",		"libcaes.dll\0"
-      VALUE "LegalCopyright",		"(C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>\0"
+      VALUE "LegalCopyright",		"(C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>\0"
       VALUE "OriginalFilename",		"libcaes.dll\0"
       VALUE "ProductName",		"libcaes\0"
-      VALUE "ProductVersion",		"@VERSION@" "\0"
+      VALUE "ProductVersion",		"20230406" "\0"
       VALUE "Comments",			"For more information visit https://github.com/libyal/libcaes/\0"
     END
   END
   BLOCK "VarFileInfo"
   BEGIN
     VALUE "Translation", 0x0409, 1200
   END
```

### Comparing `libcaes-20221127/libcaes/libcaes_support.h` & `libcaes-20230406/libcaes/libcaes_support.h`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Support functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/libcaes/libcaes_types.h` & `libcaes-20230406/libcaes/libcaes_types.h`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * The internal type definitions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/libcaes/libcaes_support.c` & `libcaes-20230406/libcaes/libcaes_support.c`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Support functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/libcaes/libcaes_context.c` & `libcaes-20230406/libcaes/libcaes_context.c`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * AES de/encryption context functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
@@ -1250,28 +1250,18 @@
 		 LIBCERROR_ERROR_DOMAIN_ARGUMENTS,
 		 LIBCERROR_ARGUMENT_ERROR_INVALID_VALUE,
 		 "%s: invalid input data.",
 		 function );
 
 		return( -1 );
 	}
-	if( input_data_size > (size_t) SSIZE_MAX )
-	{
-		libcerror_error_set(
-		 error,
-		 LIBCERROR_ERROR_DOMAIN_ARGUMENTS,
-		 LIBCERROR_ARGUMENT_ERROR_VALUE_EXCEEDS_MAXIMUM,
-		 "%s: invalid input data size value exceeds maximum.",
-		 function );
-
-		return( -1 );
-	}
 	/* Check if the input data size is a multitude of 16-byte
 	 */
-	if( ( input_data_size & (size_t) 0x0f ) != 0 )
+	if( ( ( input_data_size & (size_t) 0x0f ) != 0 )
+	 || ( input_data_size > (size_t) SSIZE_MAX ) )
 	{
 		libcerror_error_set(
 		 error,
 		 LIBCERROR_ERROR_DOMAIN_ARGUMENTS,
 		 LIBCERROR_ARGUMENT_ERROR_VALUE_OUT_OF_BOUNDS,
 		 "%s: invalid input data size value out of bounds.",
 		 function );
@@ -1452,28 +1442,18 @@
 		 LIBCERROR_ERROR_DOMAIN_ARGUMENTS,
 		 LIBCERROR_ARGUMENT_ERROR_INVALID_VALUE,
 		 "%s: invalid input data.",
 		 function );
 
 		return( -1 );
 	}
-	if( input_data_size > (size_t) INT_MAX )
-	{
-		libcerror_error_set(
-		 error,
-		 LIBCERROR_ERROR_DOMAIN_ARGUMENTS,
-		 LIBCERROR_ARGUMENT_ERROR_VALUE_EXCEEDS_MAXIMUM,
-		 "%s: invalid input data size value exceeds maximum.",
-		 function );
-
-		return( -1 );
-	}
 	/* Check if the input data size is a multitude of 16-byte
 	 */
-	if( ( input_data_size & (size_t) 0x0f ) != 0 )
+	if( ( ( input_data_size & (size_t) 0x0f ) != 0 )
+	 || ( input_data_size > (size_t) INT_MAX ) )
 	{
 		libcerror_error_set(
 		 error,
 		 LIBCERROR_ERROR_DOMAIN_ARGUMENTS,
 		 LIBCERROR_ARGUMENT_ERROR_VALUE_OUT_OF_BOUNDS,
 		 "%s: invalid input data size value out of bounds.",
 		 function );
@@ -1784,29 +1764,19 @@
 		 LIBCERROR_ERROR_DOMAIN_ARGUMENTS,
 		 LIBCERROR_ARGUMENT_ERROR_INVALID_VALUE,
 		 "%s: invalid input data.",
 		 function );
 
 		return( -1 );
 	}
-	if( ( input_data_size < 16 )
-	 || ( input_data_size > (size_t) SSIZE_MAX ) )
-	{
-		libcerror_error_set(
-		 error,
-		 LIBCERROR_ERROR_DOMAIN_ARGUMENTS,
-		 LIBCERROR_ARGUMENT_ERROR_VALUE_OUT_OF_BOUNDS,
-		 "%s: invalid input data size value out of bounds.",
-		 function );
-
-		return( -1 );
-	}
 	/* Check if the input data size is a multitude of 16-byte
 	 */
-	if( ( input_data_size & (size_t) 0x0f ) != 0 )
+	if( ( ( input_data_size & (size_t) 0x0f ) != 0 )
+	 || ( input_data_size < 16 )
+	 || ( input_data_size > (size_t) SSIZE_MAX ) )
 	{
 		libcerror_error_set(
 		 error,
 		 LIBCERROR_ERROR_DOMAIN_ARGUMENTS,
 		 LIBCERROR_ARGUMENT_ERROR_VALUE_OUT_OF_BOUNDS,
 		 "%s: invalid input data size value out of bounds.",
 		 function );
@@ -2369,29 +2339,19 @@
 		 LIBCERROR_ERROR_DOMAIN_ARGUMENTS,
 		 LIBCERROR_ARGUMENT_ERROR_INVALID_VALUE,
 		 "%s: invalid input data.",
 		 function );
 
 		return( -1 );
 	}
-	if( ( input_data_size < 16 )
-	 || ( input_data_size > (size_t) SSIZE_MAX ) )
-	{
-		libcerror_error_set(
-		 error,
-		 LIBCERROR_ERROR_DOMAIN_ARGUMENTS,
-		 LIBCERROR_ARGUMENT_ERROR_VALUE_OUT_OF_BOUNDS,
-		 "%s: invalid input data size value out of bounds.",
-		 function );
-
-		return( -1 );
-	}
 	/* Check if the input data size is a multitude of 16-byte
 	 */
-	if( ( input_data_size & (size_t) 0x0f ) != 0 )
+	if( ( ( input_data_size & (size_t) 0x0f ) != 0 )
+	 || ( input_data_size < 16 )
+	 || ( input_data_size > (size_t) SSIZE_MAX ) )
 	{
 		libcerror_error_set(
 		 error,
 		 LIBCERROR_ERROR_DOMAIN_ARGUMENTS,
 		 LIBCERROR_ARGUMENT_ERROR_VALUE_OUT_OF_BOUNDS,
 		 "%s: invalid input data size value out of bounds.",
 		 function );
@@ -2987,15 +2947,18 @@
 		 LIBCERROR_ERROR_DOMAIN_ARGUMENTS,
 		 LIBCERROR_ARGUMENT_ERROR_INVALID_VALUE,
 		 "%s: invalid input data.",
 		 function );
 
 		return( -1 );
 	}
-	if( ( input_data_size < 16 )
+	/* Check if the input data size is a multitude of 16-byte
+	 */
+	if( ( ( input_data_size & (size_t) 0x0f ) != 0 )
+	 || ( input_data_size < 16 )
 	 || ( input_data_size > (size_t) SSIZE_MAX ) )
 	{
 		libcerror_error_set(
 		 error,
 		 LIBCERROR_ERROR_DOMAIN_ARGUMENTS,
 		 LIBCERROR_ARGUMENT_ERROR_VALUE_OUT_OF_BOUNDS,
 		 "%s: invalid input data size value out of bounds.",
```

### Comparing `libcaes-20221127/libcaes/libcaes_error.h` & `libcaes-20230406/libcaes/libcaes_error.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Error functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/libcaes/libcaes_unused.h` & `libcaes-20230406/libcaes/libcaes_unused.h`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Definitions to silence compiler warnings about unused function attributes/parameters.
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/libcaes/libcaes_definitions.h` & `libcaes-20230406/libcaes/libcaes_definitions.h`

 * *Files 6% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * The internal definitions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
@@ -30,19 +30,19 @@
 #if !defined( HAVE_LOCAL_LIBCAES )
 #include <libcaes/definitions.h>
 
 /* The definitions in <libcaes/definitions.h> are copied here
  * for local use of libcaes
  */
 #else
-#define LIBCAES_VERSION				20221127
+#define LIBCAES_VERSION				20230406
 
 /* The libcaes version string
  */
-#define LIBCAES_VERSION_STRING			"20221127"
+#define LIBCAES_VERSION_STRING			"20230406"
 
 /* The crypt modes
  */
 enum LIBCAES_CRYPT_MODES
 {
 	LIBCAES_CRYPT_MODE_DECRYPT		= 0,
 	LIBCAES_CRYPT_MODE_ENCRYPT		= 1
```

### Comparing `libcaes-20221127/libcaes/libcaes_libcerror.h` & `libcaes-20230406/libcaes/libcaes_libcerror.h`

 * *Files 8% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * The libcerror header wrapper
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/libcaes/Makefile.in` & `libcaes-20230406/libcaes/Makefile.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcaes/libcaes_extern.h` & `libcaes-20230406/libcaes/libcaes_extern.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * The internal extern definition
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/libcaes/libcaes.c` & `libcaes-20230406/libcaes/libcaes.c`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Library to support cross-platform AES encryption
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/libcaes/libcaes_error.c` & `libcaes-20230406/libcaes/libcaes_error.c`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Error functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/include/libcaes.h` & `libcaes-20230406/include/libcaes.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Library to support support file format date and time values
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/include/libcaes/definitions.h.in` & `libcaes-20230406/include/libcaes/definitions.h.in`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Definitions for libcaes
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/include/libcaes/extern.h` & `libcaes-20230406/include/libcaes/extern.h`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 /*
  * The extern definition
  *
  * This header should be included in header files that export or import
  * library functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/include/libcaes/types.h` & `libcaes-20230406/include/libcaes/types.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Type definitions for libcaes
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/include/libcaes/features.h.in` & `libcaes-20230406/include/libcaes/features.h.in`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Features of libcaes
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/include/libcaes/types.h.in` & `libcaes-20230406/include/libcaes/types.h.in`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Type definitions for libcaes
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/include/libcaes/features.h` & `libcaes-20230406/include/libcaes/features.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Features of libcaes
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/include/libcaes/definitions.h` & `libcaes-20230406/include/libcaes/definitions.h`

 * *Files 3% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Definitions for libcaes
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
@@ -20,19 +20,19 @@
  */
 
 #if !defined( _LIBCAES_DEFINITIONS_H )
 #define _LIBCAES_DEFINITIONS_H
 
 #include <libcaes/types.h>
 
-#define LIBCAES_VERSION			20221127
+#define LIBCAES_VERSION			20230406
 
 /* The version string
  */
-#define LIBCAES_VERSION_STRING		"20221127"
+#define LIBCAES_VERSION_STRING		"20230406"
 
 /* The crypt modes
  */
 enum LIBCAES_CRYPT_MODES
 {
 	LIBCAES_CRYPT_MODE_DECRYPT	= 0,
 	LIBCAES_CRYPT_MODE_ENCRYPT	= 1
```

### Comparing `libcaes-20221127/include/libcaes/error.h` & `libcaes-20230406/include/libcaes/error.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * The error code definitions for libcaes
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/include/Makefile.in` & `libcaes-20230406/include/Makefile.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/include/libcaes.h.in` & `libcaes-20230406/include/libcaes.h.in`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Library to support support file format date and time values
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/install-sh` & `libcaes-20230406/install-sh`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/pycaes-python3/Makefile.am` & `libcaes-20230406/pycaes-python3/Makefile.am`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/pycaes-python3/Makefile.in` & `libcaes-20230406/pycaes-python3/Makefile.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/INSTALL` & `libcaes-20230406/INSTALL`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/dpkg/copyright` & `libcaes-20230406/dpkg/copyright`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Format: http://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
 Upstream-Name: libcaes
 Source: https://github.com/libyal/libcaes
 
 Files: *
-Copyright: 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+Copyright: 2011-2023, Joachim Metz <joachim.metz@gmail.com>
 License: LGPL-3.0+
 
 License: LGPL-3.0+
  This package is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License as published by the Free Software Foundation; either
  version 3 of the License, or (at your option) any later version.
```

### Comparing `libcaes-20221127/dpkg/rules` & `libcaes-20230406/dpkg/rules`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/dpkg/control` & `libcaes-20230406/dpkg/control`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/config.sub` & `libcaes-20230406/config.sub`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/pycaes-python2/Makefile.am` & `libcaes-20230406/pycaes-python2/Makefile.am`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/pycaes-python2/Makefile.in` & `libcaes-20230406/pycaes-python2/Makefile.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/manuals/libcaes.3` & `libcaes-20230406/manuals/libcaes.3`

 * *Files 0% similar despite different names*

```diff
@@ -58,13 +58,13 @@
 .Sh FILES
 None
 .Sh BUGS
 Please report bugs of any kind on the project issue tracker: https://github.com/libyal/libcaes/issues
 .Sh AUTHOR
 These man pages are generated from "libcaes.h".
 .Sh COPYRIGHT
-Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>.
+Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>.
 .sp
 This is free software; see the source for copying conditions.
 There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 .Sh SEE ALSO
 the libcaes.h include file
```

### Comparing `libcaes-20221127/manuals/Makefile.in` & `libcaes-20230406/manuals/Makefile.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/pycaes/pycaes_unused.h` & `libcaes-20230406/pycaes/pycaes_unused.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Definitions to silence compiler warnings about unused function attributes/parameters.
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/pycaes/pycaes_crypt_modes.h` & `libcaes-20230406/pycaes/pycaes_crypt_modes.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Python object definition of the libcaes crypt modes
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/pycaes/pycaes_libcerror.h` & `libcaes-20230406/pycaes/pycaes_libcerror.h`

 * *Files 8% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * The libcerror header wrapper
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/pycaes/pycaes_crypt.c` & `libcaes-20230406/pycaes/pycaes_crypt.c`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Python definition of the libcaes crypt functions
  *
- * Copyright (C) 2010-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2010-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/pycaes/pycaes_libcaes.h` & `libcaes-20230406/pycaes/pycaes_libcaes.h`

 * *Files 10% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * The internal libcaes header
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/pycaes/pycaes_tweaked_context.c` & `libcaes-20230406/pycaes/pycaes_tweaked_context.c`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Python object wrapper of libcaes_tweaked_context_t
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/pycaes/Makefile.am` & `libcaes-20230406/pycaes/Makefile.am`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/pycaes/pycaes_crypt.h` & `libcaes-20230406/pycaes/pycaes_crypt.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Python definition of the libcaes crypt functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/pycaes/pycaes_context.h` & `libcaes-20230406/pycaes/pycaes_context.h`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Python object wrapper of libcaes_context_t
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/pycaes/pycaes.h` & `libcaes-20230406/pycaes/pycaes.h`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Python bindings module for libcaes (pycaes)
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/pycaes/pycaes_crypt_modes.c` & `libcaes-20230406/pycaes/pycaes_crypt_modes.c`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Python object definition of the libcaes crypt modes
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/pycaes/pycaes_error.h` & `libcaes-20230406/pycaes/pycaes_error.h`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Error functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/pycaes/pycaes_tweaked_context.h` & `libcaes-20230406/pycaes/pycaes_tweaked_context.h`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Python object wrapper of libcaes_tweaked_context_t
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/pycaes/Makefile.in` & `libcaes-20230406/pycaes/Makefile.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/pycaes/pycaes.c` & `libcaes-20230406/pycaes/pycaes.c`

 * *Files 6% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Python bindings module for libcaes (pycaes)
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
@@ -46,45 +46,45 @@
 	  "get_version() -> String\n"
 	  "\n"
 	  "Retrieves the version." },
 
 	{ "crypt_cbc",
 	  (PyCFunction) pycaes_crypt_cbc,
 	  METH_VARARGS | METH_KEYWORDS,
-	  "crypt_cbc(context, mode, initialization_vector, data) -> String\n"
+	  "crypt_cbc(context, mode, initialization_vector, data) -> Bytes\n"
 	  "\n"
 	  "De- or encrypts a block of data using AES-CBC (Cipher Block Chaining)." },
 
 	{ "crypt_ccm",
 	  (PyCFunction) pycaes_crypt_ccm,
 	  METH_VARARGS | METH_KEYWORDS,
-	  "crypt_ccm(context, mode, nonce, data) -> String\n"
+	  "crypt_ccm(context, mode, nonce, data) -> Bytes\n"
 	  "\n"
 	  "De- or encrypts a block of data using AES-CCM (Counter with CBC-MAC)." },
 
 #ifdef TODO
 	{ "crypt_cfb",
 	  (PyCFunction) pycaes_crypt_cfb,
 	  METH_VARARGS | METH_KEYWORDS,
-	  "crypt_cfb(context, mode, initialization_vector, data) -> String\n"
+	  "crypt_cfb(context, mode, initialization_vector, data) -> Bytes\n"
 	  "\n"
 	  "De- or encrypts a block of data using AES-CFB (Cipher Feedback Mode)." },
 #endif
 
 	{ "crypt_ecb",
 	  (PyCFunction) pycaes_crypt_ecb,
 	  METH_VARARGS | METH_KEYWORDS,
-	  "crypt_ecb(context, mode, data) -> String\n"
+	  "crypt_ecb(context, mode, data) -> Bytes\n"
 	  "\n"
 	  "De- or encrypts a block of data using AES-ECB (Electronic CodeBook)." },
 
 	{ "crypt_xts",
 	  (PyCFunction) pycaes_crypt_xts,
 	  METH_VARARGS | METH_KEYWORDS,
-	  "crypt_xts(tweaked_context, mode, tweak_value, data) -> String\n"
+	  "crypt_xts(tweaked_context, mode, tweak_value, data) -> Bytes\n"
 	  "\n"
 	  "De- or encrypts a block of data using AES-XTS (XEX-based tweaked-codebook mode with ciphertext stealing)." },
 
 	/* Sentinel */
 	{ NULL, NULL, 0, NULL }
 };
```

### Comparing `libcaes-20221127/pycaes/pycaes_error.c` & `libcaes-20230406/pycaes/pycaes_error.c`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Error functions
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/pycaes/pycaes_python.h` & `libcaes-20230406/pycaes/pycaes_python.h`

 * *Files 5% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * The python header wrapper
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/pycaes/pycaes_context.c` & `libcaes-20230406/pycaes/pycaes_context.c`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * Python object wrapper of libcaes_context_t
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/msvscpp/caes_test_support/caes_test_support.vcproj` & `libcaes-20230406/msvscpp/caes_test_support/caes_test_support.vcproj`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/msvscpp/Makefile.am` & `libcaes-20230406/msvscpp/Makefile.am`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/msvscpp/libcaes/libcaes.vcproj` & `libcaes-20230406/msvscpp/libcaes/libcaes.vcproj`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/msvscpp/caes_test_tweaked_context/caes_test_tweaked_context.vcproj` & `libcaes-20230406/msvscpp/caes_test_tweaked_context/caes_test_tweaked_context.vcproj`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/msvscpp/caes_test_crypt_ccm/caes_test_crypt_ccm.vcproj` & `libcaes-20230406/msvscpp/caes_test_crypt_ccm/caes_test_crypt_ccm.vcproj`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/msvscpp/caes_test_crypt_cbc/caes_test_crypt_cbc.vcproj` & `libcaes-20230406/msvscpp/caes_test_crypt_cbc/caes_test_crypt_cbc.vcproj`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/msvscpp/pycaes/pycaes.vcproj` & `libcaes-20230406/msvscpp/pycaes/pycaes.vcproj`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/msvscpp/Makefile.in` & `libcaes-20230406/msvscpp/Makefile.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/msvscpp/libcerror/libcerror.vcproj` & `libcaes-20230406/msvscpp/libcerror/libcerror.vcproj`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/msvscpp/caes_test_context/caes_test_context.vcproj` & `libcaes-20230406/msvscpp/caes_test_context/caes_test_context.vcproj`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/msvscpp/caes_test_crypt_xts/caes_test_crypt_xts.vcproj` & `libcaes-20230406/msvscpp/caes_test_crypt_xts/caes_test_crypt_xts.vcproj`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/msvscpp/caes_test_error/caes_test_error.vcproj` & `libcaes-20230406/msvscpp/caes_test_error/caes_test_error.vcproj`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/msvscpp/libcaes.sln` & `libcaes-20230406/msvscpp/libcaes.sln`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/setup.py` & `libcaes-20230406/setup.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,24 +1,26 @@
 #!/usr/bin/env python
 #
 # Script to build and install Python-bindings.
-# Version: 20220806
+# Version: 20221217
 
 from __future__ import print_function
 
 import copy
+import datetime
 import glob
 import gzip
 import platform
 import os
 import shlex
 import shutil
 import subprocess
 import sys
 import tarfile
+import zipfile
 
 from distutils.ccompiler import new_compiler
 
 from setuptools import Extension
 from setuptools import setup
 from setuptools.command.build_ext import build_ext
 from setuptools.command.sdist import sdist
@@ -93,82 +95,108 @@
     compiler = new_compiler(compiler=self.compiler)
     if compiler.compiler_type == "msvc":
       self.define = [
           ("UNICODE", ""),
       ]
 
     else:
-      command = "sh configure --disable-shared-libs"
+      command = "sh configure --disable-nls --disable-shared-libs"
       output = self._RunCommand(command)
 
       print_line = False
       for line in output.split("\n"):
         line = line.rstrip()
         if line == "configure:":
           print_line = True
 
         if print_line:
           print(line)
 
       self.define = [
           ("HAVE_CONFIG_H", ""),
-          ("LOCALEDIR", "\"/usr/share/locale\""),
       ]
 
     build_ext.run(self)
 
 
 class custom_sdist(sdist):
   """Custom handler for the sdist command."""
 
   def run(self):
     """Builds a source distribution (sdist) package."""
-    if self.formats != ["gztar"]:
+    if self.formats != ["gztar"] and self.formats != ["zip"]:
       print("'setup.py sdist' unsupported format.")
       sys.exit(1)
 
     if glob.glob("*.tar.gz"):
       print("'setup.py sdist' remove existing *.tar.gz files from "
             "source directory.")
       sys.exit(1)
 
     command = "make dist"
     exit_code = subprocess.call(command, shell=True)
     if exit_code != 0:
       raise RuntimeError("Running: {0:s} failed.".format(command))
 
-    if not os.path.exists("dist"):
-      os.mkdir("dist")
+    if not os.path.exists(self.dist_dir):
+      os.mkdir(self.dist_dir)
 
     source_package_file = glob.glob("*.tar.gz")[0]
     source_package_prefix, _, source_package_suffix = (
         source_package_file.partition("-"))
     sdist_package_file = "{0:s}-python-{1:s}".format(
         source_package_prefix, source_package_suffix)
-    sdist_package_file = os.path.join("dist", sdist_package_file)
+    sdist_package_file = os.path.join(self.dist_dir, sdist_package_file)
     os.rename(source_package_file, sdist_package_file)
 
     # Create and add the PKG-INFO file to the source package.
-    with gzip.open(sdist_package_file, 'rb') as input_file:
-      with open(sdist_package_file[:-3], 'wb') as output_file:
+    with gzip.open(sdist_package_file, "rb") as input_file:
+      with open(sdist_package_file[:-3], "wb") as output_file:
         shutil.copyfileobj(input_file, output_file)
     os.remove(sdist_package_file)
 
     self.distribution.metadata.write_pkg_info(".")
     pkg_info_path = "{0:s}-{1:s}/PKG-INFO".format(
         source_package_prefix, source_package_suffix[:-7])
     with tarfile.open(sdist_package_file[:-3], "a:") as tar_file:
       tar_file.add("PKG-INFO", arcname=pkg_info_path)
     os.remove("PKG-INFO")
 
-    with open(sdist_package_file[:-3], 'rb') as input_file:
-      with gzip.open(sdist_package_file, 'wb') as output_file:
+    with open(sdist_package_file[:-3], "rb") as input_file:
+      with gzip.open(sdist_package_file, "wb") as output_file:
         shutil.copyfileobj(input_file, output_file)
     os.remove(sdist_package_file[:-3])
 
+    # Convert the .tar.gz into a .zip
+    if self.formats == ["zip"]:
+      zip_sdist_package_file = "{0:s}.zip".format(sdist_package_file[:-7])
+
+      with tarfile.open(sdist_package_file, "r|gz") as tar_file:
+        with zipfile.ZipFile(
+            zip_sdist_package_file, "w", zipfile.ZIP_DEFLATED) as zip_file:
+          for tar_file_entry in tar_file:
+            file_entry = tar_file.extractfile(tar_file_entry)
+            if tar_file_entry.isfile():
+              modification_time = datetime.datetime.fromtimestamp(
+                  tar_file_entry.mtime)
+              zip_modification_time = (
+                  modification_time.year, modification_time.month,
+                  modification_time.day, modification_time.hour,
+                  modification_time.minute, modification_time.second)
+              zip_info = zipfile.ZipInfo(
+                  date_time=zip_modification_time,
+                  filename=tar_file_entry.name)
+              zip_info.external_attr = (tar_file_entry.mode & 0xff) << 16
+
+              file_data = file_entry.read()
+              zip_file.writestr(zip_info, file_data)
+
+      os.remove(sdist_package_file)
+      sdist_package_file = zip_sdist_package_file
+
     # Inform distutils what files were created.
     dist_files = getattr(self.distribution, "dist_files", [])
     dist_files.append(("sdist", "", sdist_package_file))
 
 
 class ProjectInformation(object):
   """Project information."""
```

### Comparing `libcaes-20221127/config.guess` & `libcaes-20230406/config.guess`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/ossfuzz/Makefile.am` & `libcaes-20230406/ossfuzz/Makefile.am`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/ossfuzz/crypt_cbc_fuzzer.cc` & `libcaes-20230406/ossfuzz/crypt_cbc_fuzzer.cc`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * OSS-Fuzz target for libcaes AES-CBC crypt function
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/ossfuzz/crypt_xts_fuzzer.cc` & `libcaes-20230406/ossfuzz/crypt_xts_fuzzer.cc`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * OSS-Fuzz target for libcaes AES-ECB crypt function
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/ossfuzz/crypt_ccm_fuzzer.cc` & `libcaes-20230406/ossfuzz/crypt_ccm_fuzzer.cc`

 * *Files 5% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * OSS-Fuzz target for libcaes AES-CCM crypt function
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/ossfuzz/ossfuzz_libcaes.h` & `libcaes-20230406/ossfuzz/ossfuzz_libcaes.h`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * The libcaes header wrapper
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/ossfuzz/Makefile.in` & `libcaes-20230406/ossfuzz/Makefile.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/ossfuzz/crypt_ecb_fuzzer.cc` & `libcaes-20230406/ossfuzz/crypt_ecb_fuzzer.cc`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 /*
  * OSS-Fuzz target for libcaes AES-ECB crypt function
  *
- * Copyright (C) 2011-2022, Joachim Metz <joachim.metz@gmail.com>
+ * Copyright (C) 2011-2023, Joachim Metz <joachim.metz@gmail.com>
  *
  * Refer to AUTHORS for acknowledgements.
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU Lesser General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
```

### Comparing `libcaes-20221127/test-driver` & `libcaes-20230406/test-driver`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/configure` & `libcaes-20230406/configure`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #! /bin/sh
 # Guess values for system-dependent variables and create Makefiles.
-# Generated by GNU Autoconf 2.71 for libcaes 20221127.
+# Generated by GNU Autoconf 2.71 for libcaes 20230406.
 #
 # Report bugs to <joachim.metz@gmail.com>.
 #
 #
 # Copyright (C) 1992-1996, 1998-2017, 2020-2021 Free Software Foundation,
 # Inc.
 #
@@ -617,16 +617,16 @@
 subdirs=
 MFLAGS=
 MAKEFLAGS=
 
 # Identity of this package.
 PACKAGE_NAME='libcaes'
 PACKAGE_TARNAME='libcaes'
-PACKAGE_VERSION='20221127'
-PACKAGE_STRING='libcaes 20221127'
+PACKAGE_VERSION='20230406'
+PACKAGE_STRING='libcaes 20230406'
 PACKAGE_BUGREPORT='joachim.metz@gmail.com'
 PACKAGE_URL=''
 
 ac_unique_file="include/libcaes.h.in"
 # Factoring default headers for most tests.
 ac_includes_default="\
 #include <stddef.h>
@@ -1491,15 +1491,15 @@
 #
 # Report the --help message.
 #
 if test "$ac_init_help" = "long"; then
   # Omit some internal or obsolete options to make the list less imposing.
   # This message is too long to be a string in the A/UX 3.1 sh.
   cat <<_ACEOF
-\`configure' configures libcaes 20221127 to adapt to many kinds of systems.
+\`configure' configures libcaes 20230406 to adapt to many kinds of systems.
 
 Usage: $0 [OPTION]... [VAR=VALUE]...
 
 To assign environment variables (e.g., CC, CFLAGS...), specify them as
 VAR=VALUE.  See below for descriptions of some of the useful variables.
 
 Defaults for the options are specified in brackets.
@@ -1562,15 +1562,15 @@
   --build=BUILD     configure for building on BUILD [guessed]
   --host=HOST       cross-compile to build programs to run on HOST [BUILD]
 _ACEOF
 fi
 
 if test -n "$ac_init_help"; then
   case $ac_init_help in
-     short | recursive ) echo "Configuration of libcaes 20221127:";;
+     short | recursive ) echo "Configuration of libcaes 20230406:";;
    esac
   cat <<\_ACEOF
 
 Optional Features:
   --disable-option-checking  ignore unrecognized --enable/--with options
   --disable-FEATURE       do not include FEATURE (same as --enable-FEATURE=no)
   --enable-FEATURE[=ARG]  include FEATURE [ARG=yes]
@@ -1722,15 +1722,15 @@
     cd "$ac_pwd" || { ac_status=$?; break; }
   done
 fi
 
 test -n "$ac_init_help" && exit $ac_status
 if $ac_init_version; then
   cat <<\_ACEOF
-libcaes configure 20221127
+libcaes configure 20230406
 generated by GNU Autoconf 2.71
 
 Copyright (C) 2021 Free Software Foundation, Inc.
 This configure script is free software; the Free Software Foundation
 gives unlimited permission to copy, distribute and modify it.
 _ACEOF
   exit
@@ -2443,15 +2443,15 @@
     ac_configure_args_raw=`      printf "%s\n" "$ac_configure_args_raw" | sed "$ac_safe_unquote"`;;
 esac
 
 cat >config.log <<_ACEOF
 This file contains any messages produced by compilers while
 running configure, to aid debugging if configure makes a mistake.
 
-It was created by libcaes $as_me 20221127, which was
+It was created by libcaes $as_me 20230406, which was
 generated by GNU Autoconf 2.71.  Invocation command line was
 
   $ $0$ac_configure_args_raw
 
 _ACEOF
 exec 5>>config.log
 {
@@ -3932,15 +3932,15 @@
     CYGPATH_W=echo
   fi
 fi
 
 
 # Define the identity of the package.
  PACKAGE='libcaes'
- VERSION='20221127'
+ VERSION='20230406'
 
 
 printf "%s\n" "#define PACKAGE \"$PACKAGE\"" >>confdefs.h
 
 
 printf "%s\n" "#define VERSION \"$VERSION\"" >>confdefs.h
 
@@ -28773,15 +28773,15 @@
 test $as_write_fail = 0 && chmod +x $CONFIG_STATUS || ac_write_fail=1
 
 cat >>$CONFIG_STATUS <<\_ACEOF || ac_write_fail=1
 # Save the log message, to keep $0 and so on meaningful, and to
 # report actual input values of CONFIG_FILES etc. instead of their
 # values after options handling.
 ac_log="
-This file was extended by libcaes $as_me 20221127, which was
+This file was extended by libcaes $as_me 20230406, which was
 generated by GNU Autoconf 2.71.  Invocation command line was
 
   CONFIG_FILES    = $CONFIG_FILES
   CONFIG_HEADERS  = $CONFIG_HEADERS
   CONFIG_LINKS    = $CONFIG_LINKS
   CONFIG_COMMANDS = $CONFIG_COMMANDS
   $ $0 $@
@@ -28841,15 +28841,15 @@
 
 _ACEOF
 ac_cs_config=`printf "%s\n" "$ac_configure_args" | sed "$ac_safe_unquote"`
 ac_cs_config_escaped=`printf "%s\n" "$ac_cs_config" | sed "s/^ //; s/'/'\\\\\\\\''/g"`
 cat >>$CONFIG_STATUS <<_ACEOF || ac_write_fail=1
 ac_cs_config='$ac_cs_config_escaped'
 ac_cs_version="\\
-libcaes config.status 20221127
+libcaes config.status 20230406
 configured by $0, generated by GNU Autoconf 2.71,
   with options \\"\$ac_cs_config\\"
 
 Copyright (C) 2021 Free Software Foundation, Inc.
 This config.status script is free software; the Free Software Foundation
 gives unlimited permission to copy, distribute and modify it."
```

### Comparing `libcaes-20221127/libcaes.spec.in` & `libcaes-20230406/libcaes.spec.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/Makefile.in` & `libcaes-20230406/Makefile.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/ChangeLog` & `libcaes-20230406/ChangeLog`

 * *Files 10% similar despite different names*

```diff
@@ -1,16 +1,21 @@
 TODO
 * look into supporting input buffer == output buffer for optimization
 * CCM add separate function for authentication data support
-* implement libcaes_crypt_cfb; complete CFB suport
 * add OFB suport ?
 * add restriction that context should be used in the mode the keys were set ?
   does not work for CCM
 
+complete CFB suport
+* implement libcaes_crypt_cfb
+* add API function
+* add fuzz target
+
 Tests:
+* move crypt tests into context
 * integrate test runner into tests
 * add pycaes ECB and XTS encryption tests
 * add tests
   - CFB
   - OFB ?
   - XTS (add more test vectors?) 256-bit
   - make sure to test non-16 byte aligned data for the different implementations
```

### Comparing `libcaes-20221127/m4/gettext.m4` & `libcaes-20230406/m4/gettext.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/tests.m4` & `libcaes-20230406/m4/tests.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/lib-prefix.m4` & `libcaes-20230406/m4/lib-prefix.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/ltoptions.m4` & `libcaes-20230406/m4/ltoptions.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/lib-ld.m4` & `libcaes-20230406/m4/lib-ld.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/lib-link.m4` & `libcaes-20230406/m4/lib-link.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/python.m4` & `libcaes-20230406/m4/python.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/libtool.m4` & `libcaes-20230406/m4/libtool.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/nls.m4` & `libcaes-20230406/m4/nls.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/host-cpu-c-abi.m4` & `libcaes-20230406/m4/host-cpu-c-abi.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/ltversion.m4` & `libcaes-20230406/m4/ltversion.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/progtest.m4` & `libcaes-20230406/m4/progtest.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/lt~obsolete.m4` & `libcaes-20230406/m4/lt~obsolete.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/libcrypto.m4` & `libcaes-20230406/m4/libcrypto.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/po.m4` & `libcaes-20230406/m4/po.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/common.m4` & `libcaes-20230406/m4/common.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/libcerror.m4` & `libcaes-20230406/m4/libcerror.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/iconv.m4` & `libcaes-20230406/m4/iconv.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/ltsugar.m4` & `libcaes-20230406/m4/ltsugar.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/intlmacosx.m4` & `libcaes-20230406/m4/intlmacosx.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/m4/types.m4` & `libcaes-20230406/m4/types.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/COPYING.LESSER` & `libcaes-20230406/COPYING.LESSER`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcerror/libcerror_system.c` & `libcaes-20230406/libcerror/libcerror_system.c`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcerror/libcerror_error.c` & `libcaes-20230406/libcerror/libcerror_error.c`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcerror/libcerror_extern.h` & `libcaes-20230406/libcerror/libcerror_extern.h`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcerror/Makefile.am` & `libcaes-20230406/libcerror/Makefile.am`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcerror/libcerror_error.h` & `libcaes-20230406/libcerror/libcerror_error.h`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcerror/libcerror_support.h` & `libcaes-20230406/libcerror/libcerror_support.h`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcerror/libcerror_types.h` & `libcaes-20230406/libcerror/libcerror_types.h`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcerror/libcerror_definitions.h` & `libcaes-20230406/libcerror/libcerror_definitions.h`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcerror/libcerror_unused.h` & `libcaes-20230406/libcerror/libcerror_unused.h`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcerror/Makefile.in` & `libcaes-20230406/libcerror/Makefile.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcerror/libcerror_support.c` & `libcaes-20230406/libcerror/libcerror_support.c`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcerror/libcerror_system.h` & `libcaes-20230406/libcerror/libcerror_system.h`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/ltmain.sh` & `libcaes-20230406/ltmain.sh`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/compile` & `libcaes-20230406/compile`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/libcaes.spec` & `libcaes-20230406/libcaes.spec`

 * *Files 15% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 Name: libcaes
-Version: 20221127
+Version: 20230406
 Release: 1
 Summary: Library to support cross-platform AES encryption
 Group: System Environment/Libraries
 License: LGPLv3+
 Source: %{name}-%{version}.tar.gz
 URL: https://github.com/libyal/libcaes
 BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
@@ -81,10 +81,10 @@
 %defattr(644,root,root,755)
 %license COPYING COPYING.LESSER
 %doc AUTHORS README
 %{_libdir}/python3*/site-packages/*.a
 %{_libdir}/python3*/site-packages/*.so
 
 %changelog
-* Sun Nov 27 2022 Joachim Metz <joachim.metz@gmail.com> 20221127-1
+* Fri Apr  7 2023 Joachim Metz <joachim.metz@gmail.com> 20230406-1
 - Auto-generated
```

### Comparing `libcaes-20221127/config.rpath` & `libcaes-20230406/config.rpath`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/depcomp` & `libcaes-20230406/depcomp`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/po/en@quot.header` & `libcaes-20230406/po/en@quot.header`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/po/Rules-quot` & `libcaes-20230406/po/Rules-quot`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/po/remove-potcdate.sin` & `libcaes-20230406/po/remove-potcdate.sin`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/po/Makevars.in` & `libcaes-20230406/po/Makevars.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/po/en@boldquot.header` & `libcaes-20230406/po/en@boldquot.header`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/po/Makevars` & `libcaes-20230406/po/Makevars`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/po/insert-header.sin` & `libcaes-20230406/po/insert-header.sin`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/po/Makefile.in.in` & `libcaes-20230406/po/Makefile.in.in`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/acinclude.m4` & `libcaes-20230406/acinclude.m4`

 * *Files identical despite different names*

### Comparing `libcaes-20221127/configure.ac` & `libcaes-20230406/configure.ac`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 AC_PREREQ([2.71])
 
 AC_INIT(
  [libcaes],
- [20221127],
+ [20230406],
  [joachim.metz@gmail.com])
 
 AC_CONFIG_SRCDIR(
  [include/libcaes.h.in])
 
 AM_INIT_AUTOMAKE([gnu 1.6 tar-ustar])
```

