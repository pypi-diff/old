# Comparing `tmp/Triumvirate-0.1.0.tar.gz` & `tmp/Triumvirate-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "Triumvirate-0.1.0.tar", last modified: Thu Mar 30 17:57:44 2023, max compression
+gzip compressed data, was "Triumvirate-0.1.1.tar", last modified: Fri Apr  7 00:04:52 2023, max compression
```

## Comparing `Triumvirate-0.1.0.tar` & `Triumvirate-0.1.1.tar`

### file list

```diff
@@ -1,117 +1,113 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.750302 Triumvirate-0.1.0/
--rw-r--r--   0 runner    (1001) docker     (123)       14 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/CHANGELOG.md
--rwxr-xr-x   0 runner    (1001) docker     (123)    35149 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/LICENCE
--rw-r--r--   0 runner    (1001) docker     (123)      514 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     8183 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/Makefile
--rw-r--r--   0 runner    (1001) docker     (123)    48949 2023-03-30 17:57:44.750302 Triumvirate-0.1.0/PKG-INFO
--rwxr-xr-x   0 runner    (1001) docker     (123)     5929 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     7213 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.718301 Triumvirate-0.1.0/deploy/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.726301 Triumvirate-0.1.0/deploy/doc/
--rw-r--r--   0 runner    (1001) docker     (123)     5621 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/deploy/doc/autogen_docs.sh
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.726301 Triumvirate-0.1.0/deploy/pkg/
--rw-r--r--   0 runner    (1001) docker     (123)      844 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/deploy/pkg/autoinc_vers.sh
--rw-r--r--   0 runner    (1001) docker     (123)      614 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/deploy/pkg/autorel_testpypi.sh
--rw-r--r--   0 runner    (1001) docker     (123)     2946 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     1669 2023-03-30 17:57:44.750302 Triumvirate-0.1.0/setup.cfg
--rwxr-xr-x   0 runner    (1001) docker     (123)    10219 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.718301 Triumvirate-0.1.0/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.726301 Triumvirate-0.1.0/src/Triumvirate.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    48949 2023-03-30 17:57:44.000000 Triumvirate-0.1.0/src/Triumvirate.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3301 2023-03-30 17:57:44.000000 Triumvirate-0.1.0/src/Triumvirate.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-30 17:57:44.000000 Triumvirate-0.1.0/src/Triumvirate.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       50 2023-03-30 17:57:44.000000 Triumvirate-0.1.0/src/Triumvirate.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       12 2023-03-30 17:57:44.000000 Triumvirate-0.1.0/src/Triumvirate.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.730301 Triumvirate-0.1.0/src/triumvirate/
--rw-r--r--   0 runner    (1001) docker     (123)     1449 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    17195 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/_bihankel.py
--rw-r--r--   0 runner    (1001) docker     (123)     2609 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/_fftlog.pyx
--rw-r--r--   0 runner    (1001) docker     (123)      617 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/_particles.pxd
--rw-r--r--   0 runner    (1001) docker     (123)      874 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/_particles.pyx
--rw-r--r--   0 runner    (1001) docker     (123)    11721 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/_threept.pyx
--rw-r--r--   0 runner    (1001) docker     (123)     8756 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/_twopt.pyx
--rw-r--r--   0 runner    (1001) docker     (123)    13364 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/_winconv.py
--rw-r--r--   0 runner    (1001) docker     (123)    27588 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/catalogue.py
--rw-r--r--   0 runner    (1001) docker     (123)     3139 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/dataobjs.pxd
--rw-r--r--   0 runner    (1001) docker     (123)     6316 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/dataobjs.pyx
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.734301 Triumvirate-0.1.0/src/triumvirate/include/
--rw-r--r--   0 runner    (1001) docker     (123)     4075 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/include/arrayops.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     9002 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/include/dataobjs.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     6338 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/include/fftlog.hpp
--rw-r--r--   0 runner    (1001) docker     (123)    25731 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/include/field.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     6447 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/include/io.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     8226 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/include/maths.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     9701 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/include/monitor.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     6216 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/include/parameters.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     9457 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/include/particles.hpp
--rw-r--r--   0 runner    (1001) docker     (123)    10110 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/include/threept.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     8949 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/include/twopt.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     4046 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/logger.py
--rw-r--r--   0 runner    (1001) docker     (123)     2014 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/parameters.pxd
--rw-r--r--   0 runner    (1001) docker     (123)    24801 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/parameters.pyx
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.734301 Triumvirate-0.1.0/src/triumvirate/resources/
--rw-r--r--   0 runner    (1001) docker     (123)     2664 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/resources/params_template.ini
--rw-r--r--   0 runner    (1001) docker     (123)     2556 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/resources/params_template.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.734301 Triumvirate-0.1.0/src/triumvirate/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.738302 Triumvirate-0.1.0/src/triumvirate/src/modules/
--rw-r--r--   0 runner    (1001) docker     (123)     7402 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/src/modules/arrayops.cpp
--rw-r--r--   0 runner    (1001) docker     (123)     8151 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/src/modules/dataobjs.cpp
--rw-r--r--   0 runner    (1001) docker     (123)     5962 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/src/modules/fftlog.cpp
--rw-r--r--   0 runner    (1001) docker     (123)    74090 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/src/modules/field.cpp
--rw-r--r--   0 runner    (1001) docker     (123)    12786 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/src/modules/io.cpp
--rw-r--r--   0 runner    (1001) docker     (123)    11600 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/src/modules/maths.cpp
--rw-r--r--   0 runner    (1001) docker     (123)     8910 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/src/modules/monitor.cpp
--rw-r--r--   0 runner    (1001) docker     (123)    25628 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/src/modules/parameters.cpp
--rw-r--r--   0 runner    (1001) docker     (123)    15506 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/src/modules/particles.cpp
--rw-r--r--   0 runner    (1001) docker     (123)    74238 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/src/modules/threept.cpp
--rw-r--r--   0 runner    (1001) docker     (123)    25335 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/src/modules/twopt.cpp
--rw-r--r--   0 runner    (1001) docker     (123)    22861 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/src/triumvirate.cpp
--rw-r--r--   0 runner    (1001) docker     (123)    60607 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/threept.py
--rw-r--r--   0 runner    (1001) docker     (123)    45237 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/src/triumvirate/twopt.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.742302 Triumvirate-0.1.0/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     6173 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.742302 Triumvirate-0.1.0/tests/test_build/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_build/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)    10584 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_catalogue.py
--rw-r--r--   0 runner    (1001) docker     (123)     2444 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_dataobjs.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.722301 Triumvirate-0.1.0/tests/test_input/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.742302 Triumvirate-0.1.0/tests/test_input/ctlgs/
--rw-r--r--   0 runner    (1001) docker     (123)       48 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/ctlgs/sample_catalogue.dat
--rw-r--r--   0 runner    (1001) docker     (123)     8640 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/ctlgs/sample_catalogue.fits
--rw-r--r--   0 runner    (1001) docker     (123)     4912 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/ctlgs/sample_catalogue.h5
--rw-r--r--   0 runner    (1001) docker     (123)      151 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/ctlgs/sample_catalogue.txt
--rw-r--r--   0 runner    (1001) docker     (123)      303 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/ctlgs/test_data_catalogue.txt
--rw-r--r--   0 runner    (1001) docker     (123)  3044753 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/ctlgs/test_rand_catalogue.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.746302 Triumvirate-0.1.0/tests/test_input/params/
--rw-r--r--   0 runner    (1001) docker     (123)     2760 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/params/test_params.ini
--rw-r--r--   0 runner    (1001) docker     (123)     2695 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/params/test_params.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 17:57:44.750302 Triumvirate-0.1.0/tests/test_input/stats/
--rw-r--r--   0 runner    (1001) docker     (123)     1183 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/bk000_bin0_gpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1440 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/bk000_bin0_lpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1183 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/bk000_diag_gpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1440 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/bk000_diag_lpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1183 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/bk202_diag_gpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1440 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/bk202_diag_lpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1021 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/pk0_gpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1278 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/pk0_lpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1021 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/pk2_gpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1278 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/pk2_lpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)      841 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/xi0_gpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1098 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/xi0_lpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)      841 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/xi2_gpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1098 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/xi2_lpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)      843 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/xiw0.txt
--rw-r--r--   0 runner    (1001) docker     (123)      843 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/xiw2.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1191 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/zeta000_bin0_gpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/zeta000_bin0_lpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1191 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/zeta000_diag_gpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/zeta000_diag_lpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1191 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/zeta202_diag_gpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/zeta202_diag_lpp.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1193 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/zetaw000_bin0.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1193 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/zetaw000_diag.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1193 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_input/stats/zetaw202_diag.txt
--rw-r--r--   0 runner    (1001) docker     (123)      952 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_logger.py
--rw-r--r--   0 runner    (1001) docker     (123)    13487 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_parameters.py
--rw-r--r--   0 runner    (1001) docker     (123)    10259 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_threept.py
--rw-r--r--   0 runner    (1001) docker     (123)     6553 2023-03-30 17:57:28.000000 Triumvirate-0.1.0/tests/test_twopt.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:04:52.653652 Triumvirate-0.1.1/
+-rw-r--r--   0 runner    (1001) docker     (123)      566 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/CHANGELOG.md
+-rwxr-xr-x   0 runner    (1001) docker     (123)    35149 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/LICENCE
+-rw-r--r--   0 runner    (1001) docker     (123)      515 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     8028 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/Makefile
+-rw-r--r--   0 runner    (1001) docker     (123)    49031 2023-04-07 00:04:52.653652 Triumvirate-0.1.1/PKG-INFO
+-rwxr-xr-x   0 runner    (1001) docker     (123)     6100 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     7354 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/README.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2837 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     1679 2023-04-07 00:04:52.653652 Triumvirate-0.1.1/setup.cfg
+-rwxr-xr-x   0 runner    (1001) docker     (123)    21704 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:04:52.633650 Triumvirate-0.1.1/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:04:52.637650 Triumvirate-0.1.1/src/Triumvirate.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    49031 2023-04-07 00:04:52.000000 Triumvirate-0.1.1/src/Triumvirate.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3290 2023-04-07 00:04:52.000000 Triumvirate-0.1.1/src/Triumvirate.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 00:04:52.000000 Triumvirate-0.1.1/src/Triumvirate.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       50 2023-04-07 00:04:52.000000 Triumvirate-0.1.1/src/Triumvirate.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       12 2023-04-07 00:04:52.000000 Triumvirate-0.1.1/src/Triumvirate.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:04:52.637650 Triumvirate-0.1.1/src/triumvirate/
+-rw-r--r--   0 runner    (1001) docker     (123)     1449 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17195 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/_bihankel.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2609 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/_fftlog.pyx
+-rw-r--r--   0 runner    (1001) docker     (123)      617 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/_particles.pxd
+-rw-r--r--   0 runner    (1001) docker     (123)      874 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/_particles.pyx
+-rw-r--r--   0 runner    (1001) docker     (123)    11721 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/_threept.pyx
+-rw-r--r--   0 runner    (1001) docker     (123)     8756 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/_twopt.pyx
+-rw-r--r--   0 runner    (1001) docker     (123)     2382 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/_valid_install.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13364 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/_winconv.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27588 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/catalogue.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3139 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/dataobjs.pxd
+-rw-r--r--   0 runner    (1001) docker     (123)     6316 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/dataobjs.pyx
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:04:52.641651 Triumvirate-0.1.1/src/triumvirate/include/
+-rw-r--r--   0 runner    (1001) docker     (123)     4075 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/include/arrayops.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     9002 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/include/dataobjs.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     6338 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/include/fftlog.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)    25731 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/include/field.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     6447 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/include/io.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     8226 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/include/maths.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     9701 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/include/monitor.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     6216 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/include/parameters.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     9457 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/include/particles.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)    10110 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/include/threept.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     8949 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/include/twopt.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     4046 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/logger.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2014 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/parameters.pxd
+-rw-r--r--   0 runner    (1001) docker     (123)    24801 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/parameters.pyx
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:04:52.641651 Triumvirate-0.1.1/src/triumvirate/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)     2664 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/resources/params_template.ini
+-rw-r--r--   0 runner    (1001) docker     (123)     2556 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/resources/params_template.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:04:52.641651 Triumvirate-0.1.1/src/triumvirate/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:04:52.641651 Triumvirate-0.1.1/src/triumvirate/src/modules/
+-rw-r--r--   0 runner    (1001) docker     (123)     7402 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/src/modules/arrayops.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)     8151 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/src/modules/dataobjs.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)     5962 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/src/modules/fftlog.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)    74090 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/src/modules/field.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)    12786 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/src/modules/io.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)    11600 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/src/modules/maths.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)     8910 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/src/modules/monitor.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)    25628 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/src/modules/parameters.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)    15506 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/src/modules/particles.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)    74238 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/src/modules/threept.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)    25335 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/src/modules/twopt.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)    22861 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/src/triumvirate.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)    60607 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/threept.py
+-rw-r--r--   0 runner    (1001) docker     (123)    45237 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/src/triumvirate/twopt.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:04:52.645651 Triumvirate-0.1.1/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     6173 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/conftest.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:04:52.645651 Triumvirate-0.1.1/tests/test_build/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_build/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)    10584 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_catalogue.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2444 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_dataobjs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:04:52.633650 Triumvirate-0.1.1/tests/test_input/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:04:52.645651 Triumvirate-0.1.1/tests/test_input/ctlgs/
+-rw-r--r--   0 runner    (1001) docker     (123)       48 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/ctlgs/sample_catalogue.dat
+-rw-r--r--   0 runner    (1001) docker     (123)     8640 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/ctlgs/sample_catalogue.fits
+-rw-r--r--   0 runner    (1001) docker     (123)     4912 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/ctlgs/sample_catalogue.h5
+-rw-r--r--   0 runner    (1001) docker     (123)      151 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/ctlgs/sample_catalogue.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      303 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/ctlgs/test_data_catalogue.txt
+-rw-r--r--   0 runner    (1001) docker     (123)  3044753 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/ctlgs/test_rand_catalogue.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:04:52.649651 Triumvirate-0.1.1/tests/test_input/params/
+-rw-r--r--   0 runner    (1001) docker     (123)     2760 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/params/test_params.ini
+-rw-r--r--   0 runner    (1001) docker     (123)     2695 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/params/test_params.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2626 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/params/tmpl_params.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:04:52.653652 Triumvirate-0.1.1/tests/test_input/stats/
+-rw-r--r--   0 runner    (1001) docker     (123)     1183 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/bk000_bin0_gpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1440 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/bk000_bin0_lpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1183 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/bk000_diag_gpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1440 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/bk000_diag_lpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1183 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/bk202_diag_gpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1440 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/bk202_diag_lpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1021 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/pk0_gpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1278 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/pk0_lpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1021 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/pk2_gpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1278 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/pk2_lpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      841 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/xi0_gpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1098 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/xi0_lpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      841 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/xi2_gpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1098 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/xi2_lpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      843 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/xiw0.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      843 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/xiw2.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1191 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/zeta000_bin0_gpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/zeta000_bin0_lpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1191 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/zeta000_diag_gpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/zeta000_diag_lpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1191 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/zeta202_diag_gpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/zeta202_diag_lpp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1193 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/zetaw000_bin0.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1193 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/zetaw000_diag.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1193 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_input/stats/zetaw202_diag.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      952 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_logger.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13433 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_parameters.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10259 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_threept.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6553 2023-04-07 00:04:25.000000 Triumvirate-0.1.1/tests/test_twopt.py
```

### Comparing `Triumvirate-0.1.0/LICENCE` & `Triumvirate-0.1.1/LICENCE`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/MANIFEST.in` & `Triumvirate-0.1.1/MANIFEST.in`

 * *Files 20% similar despite different names*

```diff
@@ -6,17 +6,17 @@
 
 recursive-include tests *.py
 graft tests/test_input/
 
 prune .github
 prune application
 prune build
+prune deploy
 prune docs
 prune examples
 prune publication
-prune tools
 exclude .gitattributes
 exclude .gitignore
 exclude .readthedocs.yml
 exclude CONTRIBUTING.md
 exclude NOTES.md
 include Makefile
```

### Comparing `Triumvirate-0.1.0/Makefile` & `Triumvirate-0.1.1/Makefile`

 * *Files 24% similar despite different names*

```diff
@@ -50,43 +50,40 @@
 
 # ------------------------------------------------------------------------
 # OS-dependent Compilation
 # ------------------------------------------------------------------------
 
 # -- Compiler ------------------------------------------------------------
 
-# Linux: GNU compiler by default. [modify]
+# Assume GCC compiler by default. [modify]
 ifeq ($(shell uname -s), Linux)
 
 CXX ?= g++
 
-# macOS: GNU compiler by default. [modify]
 else ifeq ($(shell uname -s), Darwin)
 
-# Use GNU compiler from Homebrew (installed with formula 'gcc').
-# The compiler binary provided with a full path must have the suffix
-# '-<version>'; check which version is available with `brew info gcc`
-# (here 'g++-11' is assumed). Alternatively, use an appropriate alias.
-CXX ?= $(shell brew --prefix gcc)/bin/g++-11
+# Use GCC compiler from Homebrew (brew formula 'gcc').
+# The compiler binary provided may have the suffix '-<version>';
+# check the version number with `brew info gcc` (here 'g++-11' is assumed).
+CXX_DIR = $(shell brew --prefix gcc)/bin
+CXX_BIN = $(shell ls ${CXX_DIR} | grep '^g++')
+CXX ?= ${CXX_DIR}/${CXX_BIN}
 
-# Use LLVM compiler from Homebrew (installed with formula 'llvm').
-# CXX ?= $(shell brew --prefix llvm)/bin/clang++
-
-# Others: GNU compiler by default. [modify]
+# Others: GCC compiler by default. [modify]
 else  # uname -s
 
 CXX ?= g++
 
 endif  # uname -s
 
 
 # -- Options -------------------------------------------------------------
 
 INCLUDES += -I${DIR_PKG_INCLUDE}
-CFLAGS += -O3 -Wall $(shell pkg-config --cflags gsl fftw3)
+CXXFLAGS += -O3 -Wall $(shell pkg-config --cflags gsl fftw3)
 LDFLAGS += $(if $(shell pkg-config --libs gsl fftw3),\
                 $(shell pkg-config --libs gsl fftw3),\
                 $(-lgsl -lgslcblas -lm -lfftw3))
 
 
 # ------------------------------------------------------------------------
 # Environment-specific Settings
@@ -96,56 +93,57 @@
 ifdef NERSC_HOST
 
 FFTW_DIR = ${FFTW_ROOT}
 
 # GSL library
 ifdef GSL_DIR
 INCLUDES += -I${GSL_DIR}/include
-LDFLAGS += -L${GSL_DIR}/lib
+LDFLAGS = -L${GSL_DIR}/lib ${LDFLAGS}
 endif  # GSL_DIR
 
 # FFTW library
 ifdef FFTW_DIR
 INCLUDES += -I${FFTW_DIR}/include
-LDFLAGS += -L${FFTW_DIR}/lib
+LDFLAGS = -L${FFTW_DIR}/lib ${LDFLAGS}
 endif  # FFTW_DIR
 
 endif  # NERSC_HOST
 
 
 # ------------------------------------------------------------------------
 # Customisation
 # ------------------------------------------------------------------------
 
 # OpenMP: enabled with `useomp=(true|1)`; disabled otherwise.
 ifdef useomp
 
 ifeq ($(strip ${useomp}), $(filter $(strip ${useomp}), true 1))
 
-# Linux: GNU OpenMP by default. [modify]
+# Assume GCC OpenMP implementation by default. [modify]
 ifeq ($(shell uname -s), Linux)
 
-LDFLAG_OMP = -lgomp
+# Pass...
 
-# macOS: GNU OpenMP by default. [modify]
 else ifeq ($(shell uname -s), Darwin)
 
-# Use LLVM OpenMP from Homebrew (installed with formula 'libomp').
-# CFLAGS += -Xpreprocessor
-# LDFLAG_OMP = -L$(shell brew --prefix libomp)/lib -lomp
+# For LLVM OpenMP implementation, use 'libomp' from Homebrew
+# (brew formula 'libomp'). Set also the following flags.
+# CXXFLAGS += -Xpreprocessor
+# LDFLAGS_OMP = -L$(shell brew --prefix libomp)/lib -lomp
+
+# Pass...
 
-# Others: GNU OpenMP by default. [modify]
 else  # uname -s
 
-LDFLAG_OMP = -lgomp
+# Pass...
 
 endif  # uname -s
 
-CFLAGS += -fopenmp -DTRV_USE_OMP -DTRV_USE_FFTWOMP
-LDFLAGS += -lfftw3_omp ${LDFLAG_OMP}
+CXXFLAGS += -fopenmp -DTRV_USE_OMP -DTRV_USE_FFTWOMP
+LDFLAGS += -lfftw3_omp ${LDFLAGS_OMP}
 
 endif  # useomp=(true|1)
 
 else  # useomp
 
 # NOTE: Use `undefine` for make>=3.82.
 unexport useomp
@@ -157,39 +155,39 @@
 else  # useomp
 WOMP=without
 endif  # useomp
 
 # Visual enhancements: enabled with `uselogo=(true|1)`; disabled otherwise.
 ifdef uselogo
 ifeq ($(strip ${uselogo}), $(filter $(strip ${uselogo}), true 1))
-CFLAGS += -DTRV_USE_LOGO
+CXXFLAGS += -DTRV_USE_LOGO
 endif  # uselogo=(true|1)
 endif  # uselogo
 
 # Parameter debugging: enabled with `dbgpars=(true|1)`; disabled otherwise.
 ifdef dbgpars
 ifeq ($(strip ${dbgpars}), $(filter $(strip ${dbgpars}), true 1))
-CFLAGS += -DDBG_MODE -DDBG_PARS
+CXXFLAGS += -DDBG_MODE -DDBG_PARS
 endif  # dbgpars=(true|1)
 endif  # dbgpars
 
 # Other options:
 # e.g. {-g, -DTRV_USE_LEGACY_CODE, -DDBG_MODE, -DDBG_FLAG_NOAC, ...}.
 
 
 # ------------------------------------------------------------------------
 # Language-specific Settings
 # ------------------------------------------------------------------------
 
 # Python: export CXX compilation options as environmental variables.
 export PY_CXX=${CXX}
-export PY_INCLUDES=${INCLUDES}
-export PY_CFLAGS=${CFLAGS}
+export PY_CXXFLAGS=${CXXFLAGS}
 export PY_LDFLAGS=${LDFLAGS}
-export PY_LDOMP=${LDFLAG_OMP}
+export PY_INCLUDES=${INCLUDES}
+# export PY_OPTS_OMP=${LDFLAGS_OMP}
 ifndef useomp
 export PY_NO_OMP
 endif  # !useomp
 export PY_BUILD_PARALLEL=${MAKEFLAGS_JOBS}
 
 
 # ========================================================================
@@ -212,15 +210,15 @@
 
 install: cppinstall pyinstall
 
 cppinstall: cpplibinstall cppappbuild
 
 pyinstall:
 	@echo "Installing Triumvirate Python package ${WOMP} OpenMP (in development mode)..."
-	python -m pip install --upgrade --user --editable . --verbose
+	python -m pip install --user --editable . --verbose
 
 cppappbuild: ${PROGEXE}
 
 cpplibinstall: ${PROGLIB}
 
 
 # ------------------------------------------------------------------------
@@ -238,28 +236,28 @@
 # ------------------------------------------------------------------------
 # Components
 # ------------------------------------------------------------------------
 
 ${PROGEXE}: ${PROGOBJ} ${MODULEOBJ}
 	@echo "Compiling Triumvirate C++ program ${WOMP} OpenMP..."
 	if [ ! -d build/bin ]; then mkdir -p build/bin; fi
-	$(CXX) $(CFLAGS) -o $(addprefix $(DIR_BUILDBIN)/, $(notdir $@)) $^ $(LDFLAGS)
+	$(CXX) $(CXXFLAGS) -o $(addprefix $(DIR_BUILDBIN)/, $(notdir $@)) $^ $(LDFLAGS)
 
 ${PROGLIB}: ${MODULEOBJ}
 	@echo "Building Triumvirate C++ library ${WOMP} OpenMP..."
 	if [ ! -d build/lib ]; then mkdir -p build/lib; fi
 	ar -rcsv build/lib/libtrv.a $^
 
 ${PROGOBJ}: ${PROGSRC}
 	if [ ! -d build/obj ]; then mkdir -p build/obj; fi
-	$(CXX) $(CFLAGS) -o $@ -c $< $(INCLUDES)
+	$(CXX) $(CXXFLAGS) $(INCLUDES) -o $@ -c $<
 
 ${MODULEOBJ}: ${DIR_BUILDOBJ}/%.o: ${DIR_PKG_SRCMODULES}/%.cpp
 	if [ ! -d build/obj ]; then mkdir -p build/obj; fi
-	$(CXX) $(CFLAGS) -o $@ -c $< $(INCLUDES)
+	$(CXX) $(CXXFLAGS) $(INCLUDES) -o $@ -c $<
 
 
 # ========================================================================
 # Clean
 # ========================================================================
 
 clean: cppclean pyclean
```

### Comparing `Triumvirate-0.1.0/PKG-INFO` & `Triumvirate-0.1.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Triumvirate
-Version: 0.1.0
+Version: 0.1.1
 Summary: Three-point clustering measurements in large-scale structure analyses.
 Home-page: https://mikeswang.github.io/Triumvirate
 Author: Mike S Wang, Naonori S Sugiyama
 Maintainer: Mike S Wang
 Maintainer-email: Mike S Wang <mikeshengbo.wang@ed.ac.uk>
 License:                     GNU GENERAL PUBLIC LICENSE
                                Version 3, 29 June 2007
@@ -677,15 +677,14 @@
           The GNU General Public License does not permit incorporating your program
         into proprietary programs.  If your program is a subroutine library, you
         may consider it more useful to permit linking proprietary applications with
         the library.  If this is what you want to do, use the GNU Lesser General
         Public License instead of this License.  But first, please read
         <https://www.gnu.org/licenses/why-not-lgpl.html>.
         
-Project-URL: Home, https://mikeswang.github.io/Triumvirate
 Project-URL: Documentation, https://triumvirate.readthedocs.io/
 Project-URL: Source, https://github.com/MikeSWang/Triumvirate
 Project-URL: Changelog, https://github.com/MikeSWang/Triumvirate/blob/main/CHANGELOG.md
 Platform: Linux
 Platform: Darwin
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Operating System :: POSIX :: Linux
@@ -767,69 +766,75 @@
 <https://triumvirate.readthedocs.io/en/latest/installation.html#python-package>`__
 page in the documentation.
 
 
 C++ library & program
 ---------------------
 
-|Triumvirate| as either a C++ library or a 'black-box' C++ program can be
+|Triumvirate| as either a static library or a binary executable can be
 built using `make`. Instructions for compilation can be found on the
 `Installation
 <https://triumvirate.readthedocs.io/en/latest/installation.html#c-program>`__
 page in the documentation.
 
 
 Development mode
 ----------------
 
 Both the Python package and the C++ library/program can be set up in
-development mode with `make`. First check the required dependencies,
-namely the GSL and FFTW3 libraries, are installed. Then `git clone` the
-GitHub repository and `git checkout` the branch/release to be edited:
+development mode with `make`, provided that dependency requirements are
+satisfied (GSL and FFTW3 libraries are mandatory while an OpenMP library
+is optional).
+
+First `git clone` the desired branch/release from the GitHub repository and
+change into the repository directory path:
 
 .. code-block:: console
 
     $ git clone git@github.com:MikeSWang/Triumvirate.git --branch <branch-or-release>
     $ cd Triumvirate
 
-Then at the repository directory root, run
+Then, execute in terminal:
 
 .. code-block:: console
 
     $ make clean
     $ make [py|cpp]install [useomp=(true|1)]
 
-where ``install`` builds both and ``pyinstall``/``cppinstall`` is for
-Python/C++ build only; you may also replace this with ``cpplibinstall`` or
-``cppappbuild`` above to compile the C++ static library or binary executable
-only. To enable OpenMP parallelisation, append ``useomp=true`` or ``useomp=1``
-to the end of the second line as shown above.
-
-The latest release is on the |main|_ branch. The default |Makefile|_
-(located at the repository directory root) suits most use cases, but you may
-modify it as appropriate for your need.
+where ``cpplibinstall`` or ``cppappbuild`` respectively builds the C++
+static library or binary executable only, ``cppinstall`` builds both,
+``pyinstall`` builds the Python package only, and ``install`` builds
+all of the above. To enable OpenMP parallelisation, append ``useomp=true`` or ``useomp=1`` to the end of the second line as shown above.
+
+.. note::
+
+    The latest release is on the |main|_ branch. The default |Makefile|_
+    (located at the repository directory root) should work in most
+    build environments, but may need to be modified as appropriate.
 
 .. note::
 
     See the `Installation
     <https://triumvirate.readthedocs.io/en/latest/installation.html#dependencies>`__
-    page in the documentation for more details about the required dependencies.
+    page in the documentation for more details about dependency requirements.
 
 .. warning::
 
-    Ensure your C++ compiler has OpenMP support and is configured
+    Ensure your C++ compiler used supports OpenMP and is configured
     accordingly. The default |Makefile|_ (located at the repository
-    directory root) assumes the GNU compiler. See the `Installation
+    directory root) assumes the GCC compiler and OpenMP library. See the
+    `Installation
     <https://triumvirate.readthedocs.io/en/latest/installation.html#openmp-support>`__
     page in the documentation for more details.
 
 .. note::
 
-    Pass option ``-j[N] -O`` to `make` to run multiple concurrent
-    jobs (optional ``N`` is the number of parallel jobs; see `GNU Make Manual
+    Pass option ``-j[N] -O`` to `make` to run multiple concurrent jobs
+    for parallel building (optional parameter ``N`` is the number of
+    parallel jobs; see `GNU Make Manual
     <https://www.gnu.org/software/make/manual/html_node/Options-Summary.html>`_).
 
 
 Attribution
 ===========
 
 .. image:: https://img.shields.io/badge/JOSS-doi-brightgreen
```

### Comparing `Triumvirate-0.1.0/README.md` & `Triumvirate-0.1.1/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -37,59 +37,67 @@
 https://anaconda.org/msw/triumvirate). Instructions for installation
 can be found on the [Installation](
 https://triumvirate.readthedocs.io/en/latest/installation.html#python-package)
 page in the documentation.
 
 ### C++ library & program
 
-``Triumvirate`` as either a C++ library or a 'black-box' C++ program can be
+``Triumvirate`` as either a static library or a binary executable can be
 built using `make`. Instructions for compilation can be found on the
 [Installation](
-https://triumvirate.readthedocs.io/en/latest/installation.html#c-program)
+https://triumvirate.readthedocs.io/en/latest/installation.html#c-library-program)
 page in the documentation.
 
 ### Development mode
 
 Both the Python package and the C++ library/program can be set up in
-development mode with `make`. First check the required dependencies,
-namely the GSL and FFTW3 libraries, are installed. Then `git clone` the
-GitHub repository and `git checkout` the branch/release to be edited:
+development mode with `make`, provided that dependency requirements are
+satisfied (GSL and FFTW3 libraries are mandatory while an OpenMP library
+is optional).
+
+First `git clone` the desired branch/release from the GitHub repository and
+change into the repository directory path:
+
 ```console
 $ git clone git@github.com:MikeSWang/Triumvirate.git --branch <branch-or-release>
 $ cd Triumvirate
 ```
-Then at the repository directory root, run
+
+Then, execute in terminal:
+
 ```console
 $ make clean
-$ make [py|cpp]install [useomp=(true|1)]
+$ make ([py|cpp]install)|(cpp[libinstall|appbuild]) [useomp=(true|1)]
 ```
-where ``install`` builds both and ``pyinstall``/``cppinstall`` is for
-Python/C++ build only; you may also replace this with ``cpplibinstall`` or
-``cppappbuild`` above to compile the C++ static library or binary executable
-only. To enable OpenMP parallelisation, append ``useomp=true`` or ``useomp=1``
-to the end of the second line as shown above.
-
-The latest release is on the
-[``main``](https://github.com/MikeSWang/Triumvirate/tree/main) branch.
-The default [``Makefile``](Makefile) (located at the repository directory root)
-suits most use cases, but you may modify it as appropriate for your need.
+
+where ``cpplibinstall`` or ``cppappbuild`` respectively builds the C++
+static library or binary executable only, ``cppinstall`` builds both,
+``pyinstall`` builds the Python package only, and ``install`` builds
+all of the above. To enable OpenMP parallelisation, append ``useomp=true`` or ``useomp=1`` to the end of the second line as shown above.
+
+> :bulb: The latest release is on the [``main``](
+> https://github.com/MikeSWang/Triumvirate/tree/main) branch. The default
+> [``Makefile``](Makefile) (located at the repository directory root) should
+> work in most build environments, but may need to be modified as appropriate.
 
 > :bulb: See the [Installation](
 > https://triumvirate.readthedocs.io/en/latest/installation.html#dependencies)
-> page in the documentation for more details about the required dependencies.
+> page in the documentation for more details about dependency requirements.
 
-> :warning: Ensure your C++ compiler has OpenMP support and is configured
+> :warning: Ensure the C++ compiler used supports OpenMP and is configured
 > accordingly. The default [``Makefile``](Makefile) (located at the repository
-> directory root) assumes the GNU compiler. See the [Installation](
+> directory root) assumes the GCC compiler and OpenMP library. See the
+> [Installation](
 > https://triumvirate.readthedocs.io/en/latest/installation.html#openmp-support)
 > page in the documentation for more details.
 
-> :bulb: Pass option ``-j[N] -O`` to `make` to run multiple concurrent
-> jobs (optional ``N`` is the number of parallel jobs; see
-> [GNU Make Manual](https://www.gnu.org/software/make/manual/html_node/Options-Summary.html)).
+> :bulb: Pass option ``-j[N] -O`` to `make` to run multiple concurrent jobs
+> for parallel building (optional parameter ``N`` is the number of
+> parallel jobs; see [GNU Make Manual](
+> https://www.gnu.org/software/make/manual/html_node/Options-Summary.html)).
 
 
 ## Attribution
 
 [![JOSS](https://img.shields.io/badge/JOSS-doi-brightgreen)](https://joss.theoj.org/papers/?/status.svg)
 [![arXiv](https://img.shields.io/badge/arXiv-yymm.%3F-b31b1b)](https://arxiv.org/abs/?.?)
 [![MNRAS](https://img.shields.io/badge/doi-10.1093%2Fmnras%2Fsty3249-informational)](https://doi.org/10.1093/mnras/sty3249)
```

### Comparing `Triumvirate-0.1.0/README.rst` & `Triumvirate-0.1.1/README.rst`

 * *Files 2% similar despite different names*

```diff
@@ -64,69 +64,75 @@
 <https://triumvirate.readthedocs.io/en/latest/installation.html#python-package>`__
 page in the documentation.
 
 
 C++ library & program
 ---------------------
 
-|Triumvirate| as either a C++ library or a 'black-box' C++ program can be
+|Triumvirate| as either a static library or a binary executable can be
 built using `make`. Instructions for compilation can be found on the
 `Installation
 <https://triumvirate.readthedocs.io/en/latest/installation.html#c-program>`__
 page in the documentation.
 
 
 Development mode
 ----------------
 
 Both the Python package and the C++ library/program can be set up in
-development mode with `make`. First check the required dependencies,
-namely the GSL and FFTW3 libraries, are installed. Then `git clone` the
-GitHub repository and `git checkout` the branch/release to be edited:
+development mode with `make`, provided that dependency requirements are
+satisfied (GSL and FFTW3 libraries are mandatory while an OpenMP library
+is optional).
+
+First `git clone` the desired branch/release from the GitHub repository and
+change into the repository directory path:
 
 .. code-block:: console
 
     $ git clone git@github.com:MikeSWang/Triumvirate.git --branch <branch-or-release>
     $ cd Triumvirate
 
-Then at the repository directory root, run
+Then, execute in terminal:
 
 .. code-block:: console
 
     $ make clean
     $ make [py|cpp]install [useomp=(true|1)]
 
-where ``install`` builds both and ``pyinstall``/``cppinstall`` is for
-Python/C++ build only; you may also replace this with ``cpplibinstall`` or
-``cppappbuild`` above to compile the C++ static library or binary executable
-only. To enable OpenMP parallelisation, append ``useomp=true`` or ``useomp=1``
-to the end of the second line as shown above.
-
-The latest release is on the |main|_ branch. The default |Makefile|_
-(located at the repository directory root) suits most use cases, but you may
-modify it as appropriate for your need.
+where ``cpplibinstall`` or ``cppappbuild`` respectively builds the C++
+static library or binary executable only, ``cppinstall`` builds both,
+``pyinstall`` builds the Python package only, and ``install`` builds
+all of the above. To enable OpenMP parallelisation, append ``useomp=true`` or ``useomp=1`` to the end of the second line as shown above.
+
+.. note::
+
+    The latest release is on the |main|_ branch. The default |Makefile|_
+    (located at the repository directory root) should work in most
+    build environments, but may need to be modified as appropriate.
 
 .. note::
 
     See the `Installation
     <https://triumvirate.readthedocs.io/en/latest/installation.html#dependencies>`__
-    page in the documentation for more details about the required dependencies.
+    page in the documentation for more details about dependency requirements.
 
 .. warning::
 
-    Ensure your C++ compiler has OpenMP support and is configured
+    Ensure your C++ compiler used supports OpenMP and is configured
     accordingly. The default |Makefile|_ (located at the repository
-    directory root) assumes the GNU compiler. See the `Installation
+    directory root) assumes the GCC compiler and OpenMP library. See the
+    `Installation
     <https://triumvirate.readthedocs.io/en/latest/installation.html#openmp-support>`__
     page in the documentation for more details.
 
 .. note::
 
-    Pass option ``-j[N] -O`` to `make` to run multiple concurrent
-    jobs (optional ``N`` is the number of parallel jobs; see `GNU Make Manual
+    Pass option ``-j[N] -O`` to `make` to run multiple concurrent jobs
+    for parallel building (optional parameter ``N`` is the number of
+    parallel jobs; see `GNU Make Manual
     <https://www.gnu.org/software/make/manual/html_node/Options-Summary.html>`_).
 
 
 Attribution
 ===========
 
 .. image:: https://img.shields.io/badge/JOSS-doi-brightgreen
```

### Comparing `Triumvirate-0.1.0/pyproject.toml` & `Triumvirate-0.1.1/pyproject.toml`

 * *Files 5% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = [
     'setuptools>=61.0.0',
     'setuptools_scm>=6.4.0',
     'Cython>=0.25',
-    'oldest-supported-numpy',
     'extension-helpers',
+    'oldest-supported-numpy',
 ]
 build-backend = 'setuptools.build_meta'
 
 [project]
 name = 'Triumvirate'
 authors = [{name = 'Mike S Wang'}, {name = 'Naonori S Sugiyama'}]
 maintainers = [{name = 'Mike S Wang', email = "mikeshengbo.wang@ed.ac.uk"}]
@@ -37,15 +37,15 @@
   'readme',
 ]
 
 [project.optional-dependencies]
 nbk = ['nbodykit']
 
 [project.urls]
-Home = "https://mikeswang.github.io/Triumvirate"
+# Home = "https://mikeswang.github.io/Triumvirate"
 Documentation = "https://triumvirate.readthedocs.io/"
 Source = "https://github.com/MikeSWang/Triumvirate"
 Changelog = "https://github.com/MikeSWang/Triumvirate/blob/main/CHANGELOG.md"
 
 [tool.setuptools]
 include-package-data = true
 
@@ -77,19 +77,22 @@
     "tests",
 ]
 
 [tool.cibuildwheel]
 build-frontend = 'build'
 skip = [
     'pp*',
+    '*-win32',
     '*-manylinux_i686',
     '*-musllinux*',
-    # '*-macosx_universal2',
-    # '*_ppc64le',
-    # '*_s390x',
+    '*_ppc64le',
+    '*_s390x',
+]
+before-build = [
+    "export PY_BUILD_PARALLEL=-j",
 ]
 test-requires = "pytest"
 test-command = "pytest {project}/tests"
 
 # Use images that support `apt` as `yum` hangs in CentOS.
 manylinux-x86_64-image = 'manylinux_2_24'
 manylinux-aarch64-image = 'manylinux_2_24'
@@ -98,18 +101,15 @@
 before-all = [
     "apt-get update",
     "apt-get install -y libgsl-dev libfftw3-dev",
 ]
 
 [tool.cibuildwheel.macos]
 before-all = [
-    "brew update",
+    # "brew update",
     "brew install gsl fftw",
-    # Add OpenMP-supported compiler dependencies.
-    "brew install gcc libomp",
 ]
 before-build = [
     "export PY_CXX_DIR=$(brew --prefix gcc)/bin",
     "export PY_CXX_BIN=$(ls ${PY_CXX_DIR} | grep '^g++')",
     "export PY_CXX=${PY_CXX_DIR}/${PY_CXX_BIN}",
-    "echo \"ATTENTION: C++ compiler should be set to ${PY_CXX}!\"",
 ]
```

### Comparing `Triumvirate-0.1.0/setup.cfg` & `Triumvirate-0.1.1/setup.cfg`

 * *Files 6% similar despite different names*

```diff
@@ -23,15 +23,15 @@
 	Source = https://github.com/MikeSWang/Triumvirate
 	Changelog = https://github.com/MikeSWang/Triumvirate/blob/main/CHANGELOG.md
 
 [options]
 package_dir = 
 	=src
 packages = find:
-include-package-data = True
+include_package_data = True
 python_requires = >=3.8
 setup_requires = 
 	setuptools>=61.0.0
 	setuptools_scm>=6.4.0
 	Cython>=0.25
 	oldest-supported-numpy
 install_requires = 
@@ -63,15 +63,15 @@
 	*.cpp
 triumvirate.resources = 
 	*.ini
 	*.yml
 
 [tool:pytest]
 minversion = 6.0
-addopts = --full-trace --capture=no --runslow
+addopts = --full-trace --verbose --capture=no --runslow
 testpaths = 
 	tests
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

### Comparing `Triumvirate-0.1.0/src/Triumvirate.egg-info/PKG-INFO` & `Triumvirate-0.1.1/src/Triumvirate.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Triumvirate
-Version: 0.1.0
+Version: 0.1.1
 Summary: Three-point clustering measurements in large-scale structure analyses.
 Home-page: https://mikeswang.github.io/Triumvirate
 Author: Mike S Wang, Naonori S Sugiyama
 Maintainer: Mike S Wang
 Maintainer-email: Mike S Wang <mikeshengbo.wang@ed.ac.uk>
 License:                     GNU GENERAL PUBLIC LICENSE
                                Version 3, 29 June 2007
@@ -677,15 +677,14 @@
           The GNU General Public License does not permit incorporating your program
         into proprietary programs.  If your program is a subroutine library, you
         may consider it more useful to permit linking proprietary applications with
         the library.  If this is what you want to do, use the GNU Lesser General
         Public License instead of this License.  But first, please read
         <https://www.gnu.org/licenses/why-not-lgpl.html>.
         
-Project-URL: Home, https://mikeswang.github.io/Triumvirate
 Project-URL: Documentation, https://triumvirate.readthedocs.io/
 Project-URL: Source, https://github.com/MikeSWang/Triumvirate
 Project-URL: Changelog, https://github.com/MikeSWang/Triumvirate/blob/main/CHANGELOG.md
 Platform: Linux
 Platform: Darwin
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Operating System :: POSIX :: Linux
@@ -767,69 +766,75 @@
 <https://triumvirate.readthedocs.io/en/latest/installation.html#python-package>`__
 page in the documentation.
 
 
 C++ library & program
 ---------------------
 
-|Triumvirate| as either a C++ library or a 'black-box' C++ program can be
+|Triumvirate| as either a static library or a binary executable can be
 built using `make`. Instructions for compilation can be found on the
 `Installation
 <https://triumvirate.readthedocs.io/en/latest/installation.html#c-program>`__
 page in the documentation.
 
 
 Development mode
 ----------------
 
 Both the Python package and the C++ library/program can be set up in
-development mode with `make`. First check the required dependencies,
-namely the GSL and FFTW3 libraries, are installed. Then `git clone` the
-GitHub repository and `git checkout` the branch/release to be edited:
+development mode with `make`, provided that dependency requirements are
+satisfied (GSL and FFTW3 libraries are mandatory while an OpenMP library
+is optional).
+
+First `git clone` the desired branch/release from the GitHub repository and
+change into the repository directory path:
 
 .. code-block:: console
 
     $ git clone git@github.com:MikeSWang/Triumvirate.git --branch <branch-or-release>
     $ cd Triumvirate
 
-Then at the repository directory root, run
+Then, execute in terminal:
 
 .. code-block:: console
 
     $ make clean
     $ make [py|cpp]install [useomp=(true|1)]
 
-where ``install`` builds both and ``pyinstall``/``cppinstall`` is for
-Python/C++ build only; you may also replace this with ``cpplibinstall`` or
-``cppappbuild`` above to compile the C++ static library or binary executable
-only. To enable OpenMP parallelisation, append ``useomp=true`` or ``useomp=1``
-to the end of the second line as shown above.
-
-The latest release is on the |main|_ branch. The default |Makefile|_
-(located at the repository directory root) suits most use cases, but you may
-modify it as appropriate for your need.
+where ``cpplibinstall`` or ``cppappbuild`` respectively builds the C++
+static library or binary executable only, ``cppinstall`` builds both,
+``pyinstall`` builds the Python package only, and ``install`` builds
+all of the above. To enable OpenMP parallelisation, append ``useomp=true`` or ``useomp=1`` to the end of the second line as shown above.
+
+.. note::
+
+    The latest release is on the |main|_ branch. The default |Makefile|_
+    (located at the repository directory root) should work in most
+    build environments, but may need to be modified as appropriate.
 
 .. note::
 
     See the `Installation
     <https://triumvirate.readthedocs.io/en/latest/installation.html#dependencies>`__
-    page in the documentation for more details about the required dependencies.
+    page in the documentation for more details about dependency requirements.
 
 .. warning::
 
-    Ensure your C++ compiler has OpenMP support and is configured
+    Ensure your C++ compiler used supports OpenMP and is configured
     accordingly. The default |Makefile|_ (located at the repository
-    directory root) assumes the GNU compiler. See the `Installation
+    directory root) assumes the GCC compiler and OpenMP library. See the
+    `Installation
     <https://triumvirate.readthedocs.io/en/latest/installation.html#openmp-support>`__
     page in the documentation for more details.
 
 .. note::
 
-    Pass option ``-j[N] -O`` to `make` to run multiple concurrent
-    jobs (optional ``N`` is the number of parallel jobs; see `GNU Make Manual
+    Pass option ``-j[N] -O`` to `make` to run multiple concurrent jobs
+    for parallel building (optional parameter ``N`` is the number of
+    parallel jobs; see `GNU Make Manual
     <https://www.gnu.org/software/make/manual/html_node/Options-Summary.html>`_).
 
 
 Attribution
 ===========
 
 .. image:: https://img.shields.io/badge/JOSS-doi-brightgreen
```

### Comparing `Triumvirate-0.1.0/src/Triumvirate.egg-info/SOURCES.txt` & `Triumvirate-0.1.1/src/Triumvirate.egg-info/SOURCES.txt`

 * *Files 11% similar despite different names*

```diff
@@ -3,29 +3,27 @@
 MANIFEST.in
 Makefile
 README.md
 README.rst
 pyproject.toml
 setup.cfg
 setup.py
-deploy/doc/autogen_docs.sh
-deploy/pkg/autoinc_vers.sh
-deploy/pkg/autorel_testpypi.sh
 src/Triumvirate.egg-info/PKG-INFO
 src/Triumvirate.egg-info/SOURCES.txt
 src/Triumvirate.egg-info/dependency_links.txt
 src/Triumvirate.egg-info/requires.txt
 src/Triumvirate.egg-info/top_level.txt
 src/triumvirate/__init__.py
 src/triumvirate/_bihankel.py
 src/triumvirate/_fftlog.pyx
 src/triumvirate/_particles.pxd
 src/triumvirate/_particles.pyx
 src/triumvirate/_threept.pyx
 src/triumvirate/_twopt.pyx
+src/triumvirate/_valid_install.py
 src/triumvirate/_winconv.py
 src/triumvirate/catalogue.py
 src/triumvirate/dataobjs.pxd
 src/triumvirate/dataobjs.pyx
 src/triumvirate/logger.py
 src/triumvirate/parameters.pxd
 src/triumvirate/parameters.pyx
@@ -68,14 +66,15 @@
 tests/test_input/ctlgs/sample_catalogue.fits
 tests/test_input/ctlgs/sample_catalogue.h5
 tests/test_input/ctlgs/sample_catalogue.txt
 tests/test_input/ctlgs/test_data_catalogue.txt
 tests/test_input/ctlgs/test_rand_catalogue.txt
 tests/test_input/params/test_params.ini
 tests/test_input/params/test_params.yml
+tests/test_input/params/tmpl_params.yml
 tests/test_input/stats/bk000_bin0_gpp.txt
 tests/test_input/stats/bk000_bin0_lpp.txt
 tests/test_input/stats/bk000_diag_gpp.txt
 tests/test_input/stats/bk000_diag_lpp.txt
 tests/test_input/stats/bk202_diag_gpp.txt
 tests/test_input/stats/bk202_diag_lpp.txt
 tests/test_input/stats/pk0_gpp.txt
```

### Comparing `Triumvirate-0.1.0/src/triumvirate/__init__.py` & `Triumvirate-0.1.1/src/triumvirate/__init__.py`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/_bihankel.py` & `Triumvirate-0.1.1/src/triumvirate/_bihankel.py`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/_fftlog.pyx` & `Triumvirate-0.1.1/src/triumvirate/_fftlog.pyx`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/_particles.pxd` & `Triumvirate-0.1.1/src/triumvirate/_particles.pxd`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/_particles.pyx` & `Triumvirate-0.1.1/src/triumvirate/_particles.pyx`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/_threept.pyx` & `Triumvirate-0.1.1/src/triumvirate/_threept.pyx`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/_twopt.pyx` & `Triumvirate-0.1.1/src/triumvirate/_twopt.pyx`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/_winconv.py` & `Triumvirate-0.1.1/src/triumvirate/_winconv.py`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/catalogue.py` & `Triumvirate-0.1.1/src/triumvirate/catalogue.py`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/dataobjs.pxd` & `Triumvirate-0.1.1/src/triumvirate/dataobjs.pxd`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/dataobjs.pyx` & `Triumvirate-0.1.1/src/triumvirate/dataobjs.pyx`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/include/arrayops.hpp` & `Triumvirate-0.1.1/src/triumvirate/include/arrayops.hpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/include/dataobjs.hpp` & `Triumvirate-0.1.1/src/triumvirate/include/dataobjs.hpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/include/fftlog.hpp` & `Triumvirate-0.1.1/src/triumvirate/include/fftlog.hpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/include/field.hpp` & `Triumvirate-0.1.1/src/triumvirate/include/field.hpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/include/io.hpp` & `Triumvirate-0.1.1/src/triumvirate/include/io.hpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/include/maths.hpp` & `Triumvirate-0.1.1/src/triumvirate/include/maths.hpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/include/monitor.hpp` & `Triumvirate-0.1.1/src/triumvirate/include/monitor.hpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/include/parameters.hpp` & `Triumvirate-0.1.1/src/triumvirate/include/parameters.hpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/include/particles.hpp` & `Triumvirate-0.1.1/src/triumvirate/include/particles.hpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/include/threept.hpp` & `Triumvirate-0.1.1/src/triumvirate/include/threept.hpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/include/twopt.hpp` & `Triumvirate-0.1.1/src/triumvirate/include/twopt.hpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/logger.py` & `Triumvirate-0.1.1/src/triumvirate/logger.py`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/parameters.pxd` & `Triumvirate-0.1.1/src/triumvirate/parameters.pxd`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/parameters.pyx` & `Triumvirate-0.1.1/src/triumvirate/parameters.pyx`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/resources/params_template.ini` & `Triumvirate-0.1.1/src/triumvirate/resources/params_template.ini`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/resources/params_template.yml` & `Triumvirate-0.1.1/src/triumvirate/resources/params_template.yml`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/src/modules/arrayops.cpp` & `Triumvirate-0.1.1/src/triumvirate/src/modules/arrayops.cpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/src/modules/dataobjs.cpp` & `Triumvirate-0.1.1/src/triumvirate/src/modules/dataobjs.cpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/src/modules/fftlog.cpp` & `Triumvirate-0.1.1/src/triumvirate/src/modules/fftlog.cpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/src/modules/field.cpp` & `Triumvirate-0.1.1/src/triumvirate/src/modules/field.cpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/src/modules/io.cpp` & `Triumvirate-0.1.1/src/triumvirate/src/modules/io.cpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/src/modules/maths.cpp` & `Triumvirate-0.1.1/src/triumvirate/src/modules/maths.cpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/src/modules/monitor.cpp` & `Triumvirate-0.1.1/src/triumvirate/src/modules/monitor.cpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/src/modules/parameters.cpp` & `Triumvirate-0.1.1/src/triumvirate/src/modules/parameters.cpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/src/modules/particles.cpp` & `Triumvirate-0.1.1/src/triumvirate/src/modules/particles.cpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/src/modules/threept.cpp` & `Triumvirate-0.1.1/src/triumvirate/src/modules/threept.cpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/src/modules/twopt.cpp` & `Triumvirate-0.1.1/src/triumvirate/src/modules/twopt.cpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/src/triumvirate.cpp` & `Triumvirate-0.1.1/src/triumvirate/src/triumvirate.cpp`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/threept.py` & `Triumvirate-0.1.1/src/triumvirate/threept.py`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/src/triumvirate/twopt.py` & `Triumvirate-0.1.1/src/triumvirate/twopt.py`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/conftest.py` & `Triumvirate-0.1.1/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_catalogue.py` & `Triumvirate-0.1.1/tests/test_catalogue.py`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_dataobjs.py` & `Triumvirate-0.1.1/tests/test_dataobjs.py`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/ctlgs/sample_catalogue.fits` & `Triumvirate-0.1.1/tests/test_input/ctlgs/sample_catalogue.fits`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/ctlgs/sample_catalogue.h5` & `Triumvirate-0.1.1/tests/test_input/ctlgs/sample_catalogue.h5`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/ctlgs/test_rand_catalogue.txt` & `Triumvirate-0.1.1/tests/test_input/ctlgs/test_rand_catalogue.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/params/test_params.ini` & `Triumvirate-0.1.1/tests/test_input/params/test_params.ini`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/params/test_params.yml` & `Triumvirate-0.1.1/tests/test_input/params/test_params.yml`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/bk000_bin0_gpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/bk000_bin0_gpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/bk000_bin0_lpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/bk000_bin0_lpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/bk000_diag_gpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/bk000_diag_gpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/bk000_diag_lpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/bk000_diag_lpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/bk202_diag_gpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/bk202_diag_gpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/bk202_diag_lpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/bk202_diag_lpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/pk0_gpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/pk0_gpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/pk0_lpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/pk0_lpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/pk2_gpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/pk2_gpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/pk2_lpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/pk2_lpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/xi0_gpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/xi0_gpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/xi0_lpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/xi0_lpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/xi2_gpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/xi2_gpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/xi2_lpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/xi2_lpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/xiw0.txt` & `Triumvirate-0.1.1/tests/test_input/stats/xiw0.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/xiw2.txt` & `Triumvirate-0.1.1/tests/test_input/stats/xiw2.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/zeta000_bin0_gpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/zeta000_bin0_gpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/zeta000_bin0_lpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/zeta000_bin0_lpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/zeta000_diag_gpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/zeta000_diag_gpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/zeta000_diag_lpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/zeta000_diag_lpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/zeta202_diag_gpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/zeta202_diag_gpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/zeta202_diag_lpp.txt` & `Triumvirate-0.1.1/tests/test_input/stats/zeta202_diag_lpp.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/zetaw000_bin0.txt` & `Triumvirate-0.1.1/tests/test_input/stats/zetaw000_bin0.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/zetaw000_diag.txt` & `Triumvirate-0.1.1/tests/test_input/stats/zetaw000_diag.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_input/stats/zetaw202_diag.txt` & `Triumvirate-0.1.1/tests/test_input/stats/zetaw202_diag.txt`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_logger.py` & `Triumvirate-0.1.1/tests/test_logger.py`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_parameters.py` & `Triumvirate-0.1.1/tests/test_parameters.py`

 * *Files 1% similar despite different names*

```diff
@@ -196,28 +196,28 @@
                 "found in parameter template."
             )
 
 
 @pytest.mark.parametrize(
     "param_filepath, param_dict",
     [
-        ("src/triumvirate/resources/params_template.yml", None),
+        ("tmpl_params.yml", None),
         (None, 'template_parameters_dict'),
         (
-            "src/triumvirate/resources/params_template.yml",
+            "tmpl_params.yml",
             'template_parameters_dict',
         ),
     ]
 )
-def test_ParameterSet___cinit__(param_filepath, param_dict, test_dir,
+def test_ParameterSet___cinit__(param_filepath, param_dict, test_param_dir,
                                 request, tmp_path):
 
     # Patch paths for wheel testing.
     if param_filepath is not None:
-        param_filepath = os.path.join(test_dir, '..', param_filepath)
+        param_filepath = os.path.join(test_param_dir, param_filepath)
 
     # Convert parametrized parameters to fixtures.
     if param_dict is not None:
         param_dict = request.getfixturevalue(param_dict)
 
     # Check initialisation fails (and exit early if needed).
     if param_filepath is not None and param_dict is not None:
```

### Comparing `Triumvirate-0.1.0/tests/test_threept.py` & `Triumvirate-0.1.1/tests/test_threept.py`

 * *Files identical despite different names*

### Comparing `Triumvirate-0.1.0/tests/test_twopt.py` & `Triumvirate-0.1.1/tests/test_twopt.py`

 * *Files identical despite different names*

