# Comparing `tmp/pyspedas-1.4.8.tar.gz` & `tmp/pyspedas-1.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyspedas-1.4.8.tar", last modified: Tue Nov 22 20:26:53 2022, max compression
+gzip compressed data, was "pyspedas-1.4.9.tar", last modified: Wed Nov 30 21:21:17 2022, max compression
```

## Comparing `pyspedas-1.4.8.tar` & `pyspedas-1.4.9.tar`

### file list

```diff
@@ -1,710 +1,713 @@
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.207988 pyspedas-1.4.8/
--rw-rw-r--   0 eric       (501) staff       (20)     3332 2022-11-22 20:26:16.000000 pyspedas-1.4.8/CODE_OF_CONDUCT.md
--rw-rw-r--   0 eric       (501) staff       (20)     1915 2022-11-22 20:26:16.000000 pyspedas-1.4.8/CONTRIBUTING.md
--rw-rw-r--   0 eric       (501) staff       (20)     1109 2022-11-22 20:26:16.000000 pyspedas-1.4.8/LICENSE.txt
--rw-rw-r--   0 eric       (501) staff       (20)      253 2022-11-22 20:26:16.000000 pyspedas-1.4.8/MANIFEST.in
--rw-r--r--   0 eric       (501) staff       (20)    13736 2022-11-22 20:26:53.207701 pyspedas-1.4.8/PKG-INFO
--rw-rw-r--   0 eric       (501) staff       (20)    13017 2022-11-22 20:26:16.000000 pyspedas-1.4.8/README.md
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.132853 pyspedas-1.4.8/pyspedas/
--rw-rw-r--   0 eric       (501) staff       (20)     3747 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/__init__.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.133837 pyspedas-1.4.8/pyspedas/ace/
--rw-rw-r--   0 eric       (501) staff       (20)    19061 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/ace/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      399 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/ace/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     3123 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/ace/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.134029 pyspedas-1.4.8/pyspedas/ace/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/ace/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1985 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/ace/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.134362 pyspedas-1.4.8/pyspedas/akebono/
--rw-rw-r--   0 eric       (501) staff       (20)    13223 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/akebono/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      421 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/akebono/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     2128 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/akebono/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.134562 pyspedas-1.4.8/pyspedas/akebono/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/akebono/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1164 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/akebono/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.136917 pyspedas-1.4.8/pyspedas/analysis/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     5042 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/avg_data.py
--rw-rw-r--   0 eric       (501) staff       (20)     3243 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/clean_spikes.py
--rw-rw-r--   0 eric       (501) staff       (20)     1490 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/deriv_data.py
--rw-rw-r--   0 eric       (501) staff       (20)     5763 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/dpwrspc.py
--rw-rw-r--   0 eric       (501) staff       (20)     7334 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/lingradest.py
--rw-rw-r--   0 eric       (501) staff       (20)    17634 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/neutral_sheet.py
--rw-rw-r--   0 eric       (501) staff       (20)     2371 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/subtract_average.py
--rw-rw-r--   0 eric       (501) staff       (20)      795 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/subtract_median.py
--rw-rw-r--   0 eric       (501) staff       (20)     1521 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/tcrossp.py
--rw-rw-r--   0 eric       (501) staff       (20)     1972 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/tdeflag.py
--rw-rw-r--   0 eric       (501) staff       (20)     1168 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/tdotp.py
--rw-rw-r--   0 eric       (501) staff       (20)     3244 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/tdpwrspc.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.137118 pyspedas-1.4.8/pyspedas/analysis/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)    11024 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/tests/tests.py
--rw-rw-r--   0 eric       (501) staff       (20)     6388 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/time_clip.py
--rw-rw-r--   0 eric       (501) staff       (20)     2061 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/time_domain_filter.py
--rw-rw-r--   0 eric       (501) staff       (20)     3404 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/tinterpol.py
--rw-rw-r--   0 eric       (501) staff       (20)     1509 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/tnormalize.py
--rw-rw-r--   0 eric       (501) staff       (20)     3251 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/tsmooth.py
--rw-rw-r--   0 eric       (501) staff       (20)    30016 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/twavpol.py
--rw-rw-r--   0 eric       (501) staff       (20)     2504 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/wavelet.py
--rw-rw-r--   0 eric       (501) staff       (20)     1800 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/analysis/yclip.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.137572 pyspedas-1.4.8/pyspedas/cdagui/
--rw-rw-r--   0 eric       (501) staff       (20)      121 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cdagui/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)    15999 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cdagui/cdagui.py
--rw-rw-r--   0 eric       (501) staff       (20)     5756 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cdagui/cdaweb.py
--rw-rw-r--   0 eric       (501) staff       (20)      234 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cdagui/config.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.138004 pyspedas-1.4.8/pyspedas/cluster/
--rw-rw-r--   0 eric       (501) staff       (20)    23559 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cluster/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      419 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cluster/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     4020 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cluster/load.py
--rw-rw-r--   0 eric       (501) staff       (20)     7012 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cluster/load_csa.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.138205 pyspedas-1.4.8/pyspedas/cluster/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cluster/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     2857 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cluster/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.138518 pyspedas-1.4.8/pyspedas/cnofs/
--rw-rw-r--   0 eric       (501) staff       (20)     6405 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cnofs/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      409 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cnofs/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     1936 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cnofs/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.138715 pyspedas-1.4.8/pyspedas/cnofs/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cnofs/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1040 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cnofs/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.140363 pyspedas-1.4.8/pyspedas/cotrans/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     3966 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/cotrans.py
--rw-rw-r--   0 eric       (501) staff       (20)      851 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/cotrans_get_coord.py
--rw-rw-r--   0 eric       (501) staff       (20)    30417 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/cotrans_lib.py
--rw-rw-r--   0 eric       (501) staff       (20)      952 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/cotrans_set_coord.py
--rw-rw-r--   0 eric       (501) staff       (20)     2265 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/fac_matrix_make.py
--rw-rw-r--   0 eric       (501) staff       (20)     2327 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/gsm2lmn.py
--rw-rw-r--   0 eric       (501) staff       (20)    17808 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/igrf.py
--rw-rw-r--   0 eric       (501) staff       (20)    13130 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/j2000.py
--rw-rw-r--   0 eric       (501) staff       (20)     5141 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/matrix_array_lib.py
--rw-rw-r--   0 eric       (501) staff       (20)     1703 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/minvar.py
--rw-rw-r--   0 eric       (501) staff       (20)     2372 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/minvar_matrix_make.py
--rw-rw-r--   0 eric       (501) staff       (20)    25354 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/quaternions.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.140731 pyspedas-1.4.8/pyspedas/cotrans/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     8316 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/tests/cotrans.py
--rw-rw-r--   0 eric       (501) staff       (20)     1235 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/tests/quaternions.py
--rw-rw-r--   0 eric       (501) staff       (20)     3024 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/tvector_rotate.py
--rw-rw-r--   0 eric       (501) staff       (20)      847 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/cotrans/xyz_to_polar.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.141165 pyspedas-1.4.8/pyspedas/csswe/
--rw-rw-r--   0 eric       (501) staff       (20)     2575 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/csswe/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      409 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/csswe/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     1671 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/csswe/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.141383 pyspedas-1.4.8/pyspedas/csswe/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/csswe/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      640 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/csswe/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.141919 pyspedas-1.4.8/pyspedas/de2/
--rw-rw-r--   0 eric       (501) staff       (20)    19109 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/de2/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      407 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/de2/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     2832 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/de2/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.142155 pyspedas-1.4.8/pyspedas/de2/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/de2/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1968 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/de2/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.142497 pyspedas-1.4.8/pyspedas/dscovr/
--rw-rw-r--   0 eric       (501) staff       (20)     9992 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/dscovr/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      408 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/dscovr/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     2299 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/dscovr/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.142716 pyspedas-1.4.8/pyspedas/dscovr/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/dscovr/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1433 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/dscovr/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.143090 pyspedas-1.4.8/pyspedas/equator_s/
--rw-rw-r--   0 eric       (501) staff       (20)    14979 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/equator_s/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      427 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/equator_s/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     2571 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/equator_s/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.143377 pyspedas-1.4.8/pyspedas/equator_s/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/equator_s/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1377 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/equator_s/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.143632 pyspedas-1.4.8/pyspedas/erg/
--rw-rw-r--   0 eric       (501) staff       (20)     1465 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      515 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/config.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.143807 pyspedas-1.4.8/pyspedas/erg/ground/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/__init__.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.144102 pyspedas-1.4.8/pyspedas/erg/ground/camera/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/camera/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     7748 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/camera/camera_omti_asi.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.145368 pyspedas-1.4.8/pyspedas/erg/ground/geomag/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/geomag/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     6106 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/geomag/gmag_isee_fluxgate.py
--rw-rw-r--   0 eric       (501) staff       (20)     5390 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/geomag/gmag_isee_induction.py
--rw-rw-r--   0 eric       (501) staff       (20)     6018 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/geomag/gmag_magdas_1sec.py
--rw-rw-r--   0 eric       (501) staff       (20)     6136 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/geomag/gmag_mm210.py
--rw-rw-r--   0 eric       (501) staff       (20)     1049 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/geomag/gmag_stel_fluxgate.py
--rw-rw-r--   0 eric       (501) staff       (20)     1193 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/geomag/gmag_stel_induction.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.145526 pyspedas-1.4.8/pyspedas/erg/ground/radar/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/radar/__init__.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.145999 pyspedas-1.4.8/pyspedas/erg/ground/radar/superdarn/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/radar/superdarn/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      720 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/radar/superdarn/get_sphcntr.py
--rw-rw-r--   0 eric       (501) staff       (20)    25115 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/radar/superdarn/sd_fit.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.146267 pyspedas-1.4.8/pyspedas/erg/ground/riometer/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/riometer/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     7768 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/riometer/isee_brio.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.146486 pyspedas-1.4.8/pyspedas/erg/ground/vlf/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/vlf/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     5373 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/ground/vlf/isee_vlf.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.146606 pyspedas-1.4.8/pyspedas/erg/satellite/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/__init__.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.146993 pyspedas-1.4.8/pyspedas/erg/satellite/erg/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/__init__.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.147294 pyspedas-1.4.8/pyspedas/erg/satellite/erg/att/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/att/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     4110 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/att/att.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.147451 pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/__init__.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.148715 pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      551 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/cart_trans_matrix_make.py
--rw-rw-r--   0 eric       (501) staff       (20)     3963 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/dsi2j2000.py
--rw-rw-r--   0 eric       (501) staff       (20)     7210 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/erg_cotrans.py
--rw-rw-r--   0 eric       (501) staff       (20)     6195 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/erg_interpolate_att.py
--rw-rw-r--   0 eric       (501) staff       (20)     2945 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/sga2sgi.py
--rw-rw-r--   0 eric       (501) staff       (20)     2651 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/sgi2dsi.py
--rw-rw-r--   0 eric       (501) staff       (20)     2344 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/vector_rotate.py
--rw-rw-r--   0 eric       (501) staff       (20)      525 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/config.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.148983 pyspedas-1.4.8/pyspedas/erg/satellite/erg/hep/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/hep/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)    21725 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/hep/hep.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.149226 pyspedas-1.4.8/pyspedas/erg/satellite/erg/lepe/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/lepe/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)    15170 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/lepe/lepe.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.149514 pyspedas-1.4.8/pyspedas/erg/satellite/erg/lepi/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/lepi/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)    13951 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/lepi/lepi.py
--rw-rw-r--   0 eric       (501) staff       (20)     2749 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.149804 pyspedas-1.4.8/pyspedas/erg/satellite/erg/mepe/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/mepe/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     6832 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/mepe/mepe.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.150257 pyspedas-1.4.8/pyspedas/erg/satellite/erg/mepi/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/mepi/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     6702 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/mepi/mepi_nml.py
--rw-rw-r--   0 eric       (501) staff       (20)     5576 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/mepi/mepi_tof.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.150521 pyspedas-1.4.8/pyspedas/erg/satellite/erg/mgf/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/mgf/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)    11494 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/mgf/mgf.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.150984 pyspedas-1.4.8/pyspedas/erg/satellite/erg/orb/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/orb/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)    14087 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/orb/orb.py
--rw-rw-r--   0 eric       (501) staff       (20)     2226 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/orb/remove_duplicated_tframe.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.156309 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     4270 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_convert_flux_units.py
--rw-rw-r--   0 eric       (501) staff       (20)    15517 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_hep_get_dist.py
--rw-rw-r--   0 eric       (501) staff       (20)    15772 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_hep_part_products.py
--rw-rw-r--   0 eric       (501) staff       (20)    21905 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_lep_part_products.py
--rw-rw-r--   0 eric       (501) staff       (20)    12762 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_lepe_get_dist.py
--rw-rw-r--   0 eric       (501) staff       (20)    10839 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_lepi_get_dist.py
--rw-rw-r--   0 eric       (501) staff       (20)    18033 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_mep_part_products.py
--rw-rw-r--   0 eric       (501) staff       (20)     9766 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_mepe_get_dist.py
--rw-rw-r--   0 eric       (501) staff       (20)    10528 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_mepi_get_dist.py
--rw-rw-r--   0 eric       (501) staff       (20)     2647 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_clean_data.py
--rw-rw-r--   0 eric       (501) staff       (20)     1110 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_do_fac.py
--rw-rw-r--   0 eric       (501) staff       (20)     2728 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_limit_range.py
--rw-rw-r--   0 eric       (501) staff       (20)      826 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_make_e_spec.py
--rw-rw-r--   0 eric       (501) staff       (20)    13111 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_make_fac.py
--rw-rw-r--   0 eric       (501) staff       (20)     5366 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_make_phi_spec.py
--rw-rw-r--   0 eric       (501) staff       (20)     4955 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_make_theta_spec.py
--rw-rw-r--   0 eric       (501) staff       (20)     1655 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_make_tplot.py
--rw-rw-r--   0 eric       (501) staff       (20)     2019 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_moments_tplot.py
--rw-rw-r--   0 eric       (501) staff       (20)     1260 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_progress_update.py
--rw-rw-r--   0 eric       (501) staff       (20)     2727 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_units_string.py
--rw-rw-r--   0 eric       (501) staff       (20)     9610 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_xep_get_dist.py
--rw-rw-r--   0 eric       (501) staff       (20)     9927 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_xep_part_products.py
--rw-rw-r--   0 eric       (501) staff       (20)     1443 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/get_lepi_flux_angle_in_sga.py
--rw-rw-r--   0 eric       (501) staff       (20)     1660 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/get_mepe_az_dir_in_sga.py
--rw-rw-r--   0 eric       (501) staff       (20)      666 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/get_mepe_flux_angle_in_sga.py
--rw-rw-r--   0 eric       (501) staff       (20)     1343 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/get_mepi_flux_angle_in_sga.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.157133 pyspedas-1.4.8/pyspedas/erg/satellite/erg/pwe/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/pwe/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     8933 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/pwe/pwe_efd.py
--rw-rw-r--   0 eric       (501) staff       (20)    10279 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/pwe/pwe_hfa.py
--rw-rw-r--   0 eric       (501) staff       (20)     5916 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/pwe/pwe_ofa.py
--rw-rw-r--   0 eric       (501) staff       (20)    11534 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/pwe/pwe_wfc.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.157368 pyspedas-1.4.8/pyspedas/erg/satellite/erg/xep/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/xep/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     7865 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/satellite/erg/xep/xep.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.157585 pyspedas-1.4.8/pyspedas/erg/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     3428 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/erg/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.157929 pyspedas-1.4.8/pyspedas/fast/
--rw-rw-r--   0 eric       (501) staff       (20)     8770 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/fast/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      404 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/fast/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     2274 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/fast/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.158134 pyspedas-1.4.8/pyspedas/fast/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/fast/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1365 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/fast/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.158888 pyspedas-1.4.8/pyspedas/geopack/
--rw-rw-r--   0 eric       (501) staff       (20)      133 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/geopack/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     6092 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/geopack/get_tsy_params.py
--rw-rw-r--   0 eric       (501) staff       (20)     3386 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/geopack/get_w_params.py
--rw-rw-r--   0 eric       (501) staff       (20)     2093 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/geopack/t01.py
--rw-rw-r--   0 eric       (501) staff       (20)     1830 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/geopack/t89.py
--rw-rw-r--   0 eric       (501) staff       (20)     1962 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/geopack/t96.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.159083 pyspedas-1.4.8/pyspedas/geopack/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/geopack/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     4101 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/geopack/tests/tests.py
--rw-rw-r--   0 eric       (501) staff       (20)     2268 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/geopack/ts04.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.159402 pyspedas-1.4.8/pyspedas/geotail/
--rw-rw-r--   0 eric       (501) staff       (20)    13020 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/geotail/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      419 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/geotail/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     2604 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/geotail/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.159594 pyspedas-1.4.8/pyspedas/geotail/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/geotail/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1352 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/geotail/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.160031 pyspedas-1.4.8/pyspedas/goes/
--rw-rw-r--   0 eric       (501) staff       (20)    11443 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/goes/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      406 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/goes/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     7081 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/goes/load.py
--rw-rw-r--   0 eric       (501) staff       (20)     1617 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/goes/load_orbit.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.160221 pyspedas-1.4.8/pyspedas/goes/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/goes/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     4466 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/goes/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.160410 pyspedas-1.4.8/pyspedas/hapi/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/hapi/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     5443 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/hapi/hapi.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.160595 pyspedas-1.4.8/pyspedas/hapi/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/hapi/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1336 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/hapi/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.160906 pyspedas-1.4.8/pyspedas/image/
--rw-rw-r--   0 eric       (501) staff       (20)    14745 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/image/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      409 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/image/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     2688 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/image/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.161098 pyspedas-1.4.8/pyspedas/image/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/image/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1664 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/image/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.161303 pyspedas-1.4.8/pyspedas/kyoto/
--rw-rw-r--   0 eric       (501) staff       (20)       26 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/kyoto/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     4411 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/kyoto/load_dst.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.161494 pyspedas-1.4.8/pyspedas/kyoto/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/kyoto/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      775 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/kyoto/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.161816 pyspedas-1.4.8/pyspedas/lanl/
--rw-rw-r--   0 eric       (501) staff       (20)     5640 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/lanl/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      409 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/lanl/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     1827 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/lanl/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.162040 pyspedas-1.4.8/pyspedas/lanl/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/lanl/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1076 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/lanl/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.162952 pyspedas-1.4.8/pyspedas/maven/
--rw-rw-r--   0 eric       (501) staff       (20)     9965 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/maven/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      334 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/maven/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     7009 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/maven/download_files_utilities.py
--rw-rw-r--   0 eric       (501) staff       (20)     1940 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/maven/file_regex.py
--rw-rw-r--   0 eric       (501) staff       (20)    21768 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/maven/maven_kp_to_tplot.py
--rw-rw-r--   0 eric       (501) staff       (20)    13748 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/maven/maven_load.py
--rw-rw-r--   0 eric       (501) staff       (20)     1609 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/maven/orbit_time.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.163190 pyspedas-1.4.8/pyspedas/maven/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/maven/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1929 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/maven/tests/tests.py
--rw-rw-r--   0 eric       (501) staff       (20)    79453 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/maven/utilities.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.163508 pyspedas-1.4.8/pyspedas/mica/
--rw-rw-r--   0 eric       (501) staff       (20)     2931 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mica/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      391 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mica/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     1843 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mica/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.163698 pyspedas-1.4.8/pyspedas/mica/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mica/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      854 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mica/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.165429 pyspedas-1.4.8/pyspedas/mms/
--rw-rw-r--   0 eric       (501) staff       (20)     2433 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/__init__.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.165651 pyspedas-1.4.8/pyspedas/mms/aspoc/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/aspoc/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     4054 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/aspoc/aspoc.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.166589 pyspedas-1.4.8/pyspedas/mms/cotrans/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/cotrans/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     3641 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/cotrans/mms_cotrans_lmn.py
--rw-rw-r--   0 eric       (501) staff       (20)     1597 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/cotrans/mms_cotrans_qrotate.py
--rw-rw-r--   0 eric       (501) staff       (20)     1392 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/cotrans/mms_cotrans_qtransformer.py
--rw-rw-r--   0 eric       (501) staff       (20)     4668 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/cotrans/mms_qcotrans.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.166965 pyspedas-1.4.8/pyspedas/mms/dsp/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/dsp/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     4223 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/dsp/dsp.py
--rw-rw-r--   0 eric       (501) staff       (20)     7433 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/dsp/mms_dsp_set_metadata.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.167297 pyspedas-1.4.8/pyspedas/mms/edi/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/edi/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     4237 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/edi/edi.py
--rw-rw-r--   0 eric       (501) staff       (20)     3513 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/edi/mms_edi_set_metadata.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.167649 pyspedas-1.4.8/pyspedas/mms/edp/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/edp/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     4258 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/edp/edp.py
--rw-rw-r--   0 eric       (501) staff       (20)     2555 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/edp/mms_edp_set_metadata.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.168567 pyspedas-1.4.8/pyspedas/mms/eis/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/eis/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)    12211 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/eis/eis.py
--rw-rw-r--   0 eric       (501) staff       (20)     3678 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/eis/mms_eis_omni.py
--rw-rw-r--   0 eric       (501) staff       (20)     9763 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/eis/mms_eis_pad.py
--rw-rw-r--   0 eric       (501) staff       (20)     3951 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/eis/mms_eis_pad_spinavg.py
--rw-rw-r--   0 eric       (501) staff       (20)     1420 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/eis/mms_eis_set_metadata.py
--rw-rw-r--   0 eric       (501) staff       (20)     7462 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/eis/mms_eis_spec_combine_sc.py
--rw-rw-r--   0 eric       (501) staff       (20)     3830 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/eis/mms_eis_spin_avg.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.170559 pyspedas-1.4.8/pyspedas/mms/feeps/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     6626 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/feeps.py
--rw-rw-r--   0 eric       (501) staff       (20)     3317 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_active_eyes.py
--rw-rw-r--   0 eric       (501) staff       (20)     1942 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_correct_energies.py
--rw-rw-r--   0 eric       (501) staff       (20)     2091 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_energy_table.py
--rw-rw-r--   0 eric       (501) staff       (20)     5775 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_flat_field_corrections.py
--rw-rw-r--   0 eric       (501) staff       (20)    15000 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_getgyrophase.py
--rw-rw-r--   0 eric       (501) staff       (20)     6564 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_gpd.py
--rw-rw-r--   0 eric       (501) staff       (20)     7114 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_omni.py
--rw-rw-r--   0 eric       (501) staff       (20)     7736 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_pad.py
--rw-rw-r--   0 eric       (501) staff       (20)     4041 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_pad_spinavg.py
--rw-rw-r--   0 eric       (501) staff       (20)    14414 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_pitch_angles.py
--rw-rw-r--   0 eric       (501) staff       (20)    15888 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_remove_bad_data.py
--rw-rw-r--   0 eric       (501) staff       (20)     3462 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_remove_sun.py
--rw-rw-r--   0 eric       (501) staff       (20)     2759 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_spin_avg.py
--rw-rw-r--   0 eric       (501) staff       (20)     2741 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_split_integral_ch.py
--rw-rw-r--   0 eric       (501) staff       (20)     2170 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/mms_read_feeps_sector_masks_csv.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.175257 pyspedas-1.4.8/pyspedas/mms/feeps/sun/
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20151111.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20160709.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20161028.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20170531.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20171003.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20181005.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20220113.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20220506.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3135 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20220815.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20151111.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20160709.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20161028.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20170531.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20171003.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20181005.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20220113.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20220506.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20220815.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20151111.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20160709.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20161028.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20170531.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20171003.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20181005.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20220113.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20220506.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20220815.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20151111.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20160709.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20161028.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20170531.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20171003.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20181005.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20220113.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20220506.csv
--rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20220815.csv
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.176416 pyspedas-1.4.8/pyspedas/mms/fgm/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fgm/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     7195 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fgm/fgm.py
--rw-rw-r--   0 eric       (501) staff       (20)     9700 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fgm/mms_curl.py
--rw-rw-r--   0 eric       (501) staff       (20)     2414 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fgm/mms_fgm_remove_flags.py
--rw-rw-r--   0 eric       (501) staff       (20)     4491 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fgm/mms_fgm_set_metadata.py
--rw-rw-r--   0 eric       (501) staff       (20)     3905 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fgm/mms_lingradest.py
--rw-rw-r--   0 eric       (501) staff       (20)     1774 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fgm/mms_split_fgm_data.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.178052 pyspedas-1.4.8/pyspedas/mms/fpi/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fpi/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)    15367 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fpi/fpi.py
--rw-rw-r--   0 eric       (501) staff       (20)     9259 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fpi/mms_fpi_ang_ang.py
--rw-rw-r--   0 eric       (501) staff       (20)     3113 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fpi/mms_fpi_make_compressionlossbars.py
--rw-rw-r--   0 eric       (501) staff       (20)    14088 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fpi/mms_fpi_make_errorflagbars.py
--rw-rw-r--   0 eric       (501) staff       (20)     7916 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fpi/mms_fpi_set_metadata.py
--rw-rw-r--   0 eric       (501) staff       (20)     2189 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fpi/mms_fpi_split_tensor.py
--rw-rw-r--   0 eric       (501) staff       (20)     6807 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fpi/mms_get_fpi_dist.py
--rw-rw-r--   0 eric       (501) staff       (20)     4368 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fpi/mms_load_fpi_calc_pad.py
--rw-rw-r--   0 eric       (501) staff       (20)    13596 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fpi/mms_pad_fpi.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.178358 pyspedas-1.4.8/pyspedas/mms/fsm/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fsm/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     3844 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/fsm/fsm.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.179593 pyspedas-1.4.8/pyspedas/mms/hpca/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/hpca/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     8024 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/hpca/hpca.py
--rw-rw-r--   0 eric       (501) staff       (20)     8055 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/hpca/mms_get_hpca_dist.py
--rw-rw-r--   0 eric       (501) staff       (20)     3255 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/hpca/mms_get_hpca_info.py
--rw-rw-r--   0 eric       (501) staff       (20)     3609 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/hpca/mms_hpca_calc_anodes.py
--rw-rw-r--   0 eric       (501) staff       (20)      690 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/hpca/mms_hpca_energies.py
--rw-rw-r--   0 eric       (501) staff       (20)     2817 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/hpca/mms_hpca_set_metadata.py
--rw-rw-r--   0 eric       (501) staff       (20)     2698 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/hpca/mms_hpca_spin_sum.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.180621 pyspedas-1.4.8/pyspedas/mms/mec/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mec/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)   769966 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mec/earth_polar1.png
--rw-rw-r--   0 eric       (501) staff       (20)     4616 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mec/mec.py
--rw-rw-r--   0 eric       (501) staff       (20)     4652 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mec/mms_mec_set_metadata.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.181434 pyspedas-1.4.8/pyspedas/mms/mec_ascii/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mec_ascii/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     2862 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mec_ascii/mms_get_local_state_files.py
--rw-rw-r--   0 eric       (501) staff       (20)     6175 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mec_ascii/mms_get_state_data.py
--rw-rw-r--   0 eric       (501) staff       (20)     2539 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mec_ascii/mms_load_att_tplot.py
--rw-rw-r--   0 eric       (501) staff       (20)     2504 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mec_ascii/mms_load_eph_tplot.py
--rw-rw-r--   0 eric       (501) staff       (20)     1571 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mec_ascii/state.py
--rw-rw-r--   0 eric       (501) staff       (20)      782 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mms_config.py
--rw-rw-r--   0 eric       (501) staff       (20)     3602 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mms_file_filter.py
--rw-rw-r--   0 eric       (501) staff       (20)     1643 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mms_files_in_interval.py
--rw-rw-r--   0 eric       (501) staff       (20)     4425 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mms_get_local_files.py
--rw-rw-r--   0 eric       (501) staff       (20)     2797 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mms_load_brst_segments.py
--rw-rw-r--   0 eric       (501) staff       (20)    10581 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mms_load_data.py
--rw-rw-r--   0 eric       (501) staff       (20)     5562 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mms_load_data_spdf.py
--rw-rw-r--   0 eric       (501) staff       (20)     2596 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mms_load_fast_segments.py
--rw-rw-r--   0 eric       (501) staff       (20)     3944 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mms_load_sroi_segments.py
--rw-rw-r--   0 eric       (501) staff       (20)     2437 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mms_login_lasp.py
--rw-rw-r--   0 eric       (501) staff       (20)     3399 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mms_orbit_plot.py
--rw-rw-r--   0 eric       (501) staff       (20)      507 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/mms_python_startup.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.183557 pyspedas-1.4.8/pyspedas/mms/particles/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/particles/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     2830 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/particles/mms_convert_flux_units.py
--rw-rw-r--   0 eric       (501) staff       (20)     2711 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/particles/mms_part_des_photoelectrons.py
--rw-rw-r--   0 eric       (501) staff       (20)     7786 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/particles/mms_part_getspec.py
--rw-rw-r--   0 eric       (501) staff       (20)    16515 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/particles/mms_part_products.py
--rw-rw-r--   0 eric       (501) staff       (20)    11103 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/particles/mms_part_slice2d.py
--rw-rw-r--   0 eric       (501) staff       (20)     1836 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/particles/mms_pgs_clean_data.py
--rw-rw-r--   0 eric       (501) staff       (20)     1459 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/particles/mms_pgs_clean_support.py
--rw-rw-r--   0 eric       (501) staff       (20)     1424 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/particles/mms_pgs_make_e_spec.py
--rw-rw-r--   0 eric       (501) staff       (20)     5066 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/particles/mms_pgs_make_fac.py
--rw-rw-r--   0 eric       (501) staff       (20)     1160 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/particles/mms_pgs_make_phi_spec.py
--rw-rw-r--   0 eric       (501) staff       (20)     1388 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/particles/mms_pgs_make_theta_spec.py
--rw-rw-r--   0 eric       (501) staff       (20)     1075 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/particles/mms_pgs_split_hpca.py
--rw-rw-r--   0 eric       (501) staff       (20)     3236 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/particles/moka_mms_clean_data.py
--rw-rw-r--   0 eric       (501) staff       (20)      645 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/print_vars.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.184020 pyspedas-1.4.8/pyspedas/mms/scm/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/scm/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1603 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/scm/mms_scm_set_metadata.py
--rw-rw-r--   0 eric       (501) staff       (20)     5414 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/scm/scm.py
--rw-rw-r--   0 eric       (501) staff       (20)     1896 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/spd_mms_load_bss.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.186327 pyspedas-1.4.8/pyspedas/mms/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      575 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/tests/cotrans.py
--rw-rw-r--   0 eric       (501) staff       (20)     3691 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/tests/curlometer.py
--rw-rw-r--   0 eric       (501) staff       (20)     1919 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/tests/data_rate_segments.py
--rw-rw-r--   0 eric       (501) staff       (20)     4620 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/tests/eis.py
--rw-rw-r--   0 eric       (501) staff       (20)     5625 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/tests/feeps.py
--rw-rw-r--   0 eric       (501) staff       (20)     3564 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/tests/file_filter.py
--rw-rw-r--   0 eric       (501) staff       (20)     2723 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/tests/fpi_tests.py
--rw-rw-r--   0 eric       (501) staff       (20)    22209 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/tests/load_routine_tests.py
--rw-rw-r--   0 eric       (501) staff       (20)     5789 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/tests/mms_part_getspec.py
--rw-rw-r--   0 eric       (501) staff       (20)     2595 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/tests/neutral_sheet.py
--rw-rw-r--   0 eric       (501) staff       (20)     4343 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/tests/ql_l1b_sitl_tests.py
--rw-rw-r--   0 eric       (501) staff       (20)      228 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/tests/setup_tests.py
--rw-rw-r--   0 eric       (501) staff       (20)     5867 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/tests/slice2d.py
--rw-rw-r--   0 eric       (501) staff       (20)     2341 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/mms/tests/wavpol.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.186796 pyspedas-1.4.8/pyspedas/omni/
--rw-rw-r--   0 eric       (501) staff       (20)     2552 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/omni/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      416 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/omni/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     2252 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/omni/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.187081 pyspedas-1.4.8/pyspedas/omni/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/omni/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     2041 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/omni/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.187359 pyspedas-1.4.8/pyspedas/particles/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/__init__.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.188420 pyspedas-1.4.8/pyspedas/particles/moments/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/moments/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     3465 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/moments/moments_3d.py
--rw-rw-r--   0 eric       (501) staff       (20)     1948 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/moments/moments_3d_omega_weights.py
--rw-rw-r--   0 eric       (501) staff       (20)      475 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/moments/spd_pgs_moments.py
--rw-rw-r--   0 eric       (501) staff       (20)     1326 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/moments/spd_pgs_moments_tplot.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.190118 pyspedas-1.4.8/pyspedas/particles/spd_part_products/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_part_products/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1061 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_do_fac.py
--rw-rw-r--   0 eric       (501) staff       (20)     2160 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_limit_range.py
--rw-rw-r--   0 eric       (501) staff       (20)      834 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_make_e_spec.py
--rw-rw-r--   0 eric       (501) staff       (20)     4821 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_make_phi_spec.py
--rw-rw-r--   0 eric       (501) staff       (20)     4244 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_make_theta_spec.py
--rw-rw-r--   0 eric       (501) staff       (20)     1571 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_make_tplot.py
--rw-rw-r--   0 eric       (501) staff       (20)     1243 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_progress_update.py
--rw-rw-r--   0 eric       (501) staff       (20)     2745 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_regrid.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.193091 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     2113 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/quaternions.py
--rw-rw-r--   0 eric       (501) staff       (20)     3394 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice1d_plot.py
--rw-rw-r--   0 eric       (501) staff       (20)    13802 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d.py
--rw-rw-r--   0 eric       (501) staff       (20)     3388 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_2di.py
--rw-rw-r--   0 eric       (501) staff       (20)      749 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_checkbins.py
--rw-rw-r--   0 eric       (501) staff       (20)     2419 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_collate.py
--rw-rw-r--   0 eric       (501) staff       (20)     1502 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_custom_rotation.py
--rw-rw-r--   0 eric       (501) staff       (20)     5883 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_geo.py
--rw-rw-r--   0 eric       (501) staff       (20)     3417 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_get_data.py
--rw-rw-r--   0 eric       (501) staff       (20)      853 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_get_ebounds.py
--rw-rw-r--   0 eric       (501) staff       (20)     1473 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_get_sphere.py
--rw-rw-r--   0 eric       (501) staff       (20)      753 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_get_support.py
--rw-rw-r--   0 eric       (501) staff       (20)     2702 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_getinfo.py
--rw-rw-r--   0 eric       (501) staff       (20)      682 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_intrange.py
--rw-rw-r--   0 eric       (501) staff       (20)     1025 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_nearest.py
--rw-rw-r--   0 eric       (501) staff       (20)     1986 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_orientslice.py
--rw-rw-r--   0 eric       (501) staff       (20)     3681 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_plot.py
--rw-rw-r--   0 eric       (501) staff       (20)      819 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_rlog.py
--rw-rw-r--   0 eric       (501) staff       (20)     3005 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_rotate.py
--rw-rw-r--   0 eric       (501) staff       (20)      556 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_s2c.py
--rw-rw-r--   0 eric       (501) staff       (20)     1686 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_smooth.py
--rw-rw-r--   0 eric       (501) staff       (20)      731 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_subtract.py
--rw-rw-r--   0 eric       (501) staff       (20)      776 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/spd_cal_rot.py
--rw-rw-r--   0 eric       (501) staff       (20)     1236 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_slice2d/tplot_average.py
--rw-rw-r--   0 eric       (501) staff       (20)     1114 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/particles/spd_units_string.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.193412 pyspedas-1.4.8/pyspedas/poes/
--rw-rw-r--   0 eric       (501) staff       (20)     2493 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/poes/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      404 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/poes/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     1757 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/poes/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.193607 pyspedas-1.4.8/pyspedas/poes/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/poes/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1173 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/poes/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.193994 pyspedas-1.4.8/pyspedas/polar/
--rw-rw-r--   0 eric       (501) staff       (20)    25546 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/polar/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      409 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/polar/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     3442 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/polar/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.194222 pyspedas-1.4.8/pyspedas/polar/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/polar/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     2143 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/polar/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.194865 pyspedas-1.4.8/pyspedas/psp/
--rw-rw-r--   0 eric       (501) staff       (20)    21250 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/psp/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      552 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/psp/config.py
--rw-rw-r--   0 eric       (501) staff       (20)    12844 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/psp/filter.py
--rw-rw-r--   0 eric       (501) staff       (20)     9064 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/psp/load.py
--rw-rw-r--   0 eric       (501) staff       (20)      800 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/psp/rfs.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.195094 pyspedas-1.4.8/pyspedas/psp/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/psp/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     7362 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/psp/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.195466 pyspedas-1.4.8/pyspedas/rbsp/
--rw-rw-r--   0 eric       (501) staff       (20)    19071 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/rbsp/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      404 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/rbsp/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     5264 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/rbsp/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.196138 pyspedas-1.4.8/pyspedas/rbsp/rbspice_lib/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/rbsp/rbspice_lib/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     4264 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/rbsp/rbspice_lib/rbsp_load_rbspice_read.py
--rw-rw-r--   0 eric       (501) staff       (20)     2865 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_omni.py
--rw-rw-r--   0 eric       (501) staff       (20)     7484 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_pad.py
--rw-rw-r--   0 eric       (501) staff       (20)     4755 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_pad_spinavg.py
--rw-rw-r--   0 eric       (501) staff       (20)     4145 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_spin_avg.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.196339 pyspedas-1.4.8/pyspedas/rbsp/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/rbsp/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     5153 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/rbsp/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.196771 pyspedas-1.4.8/pyspedas/secs/
--rw-rw-r--   0 eric       (501) staff       (20)     6701 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/secs/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1011 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/secs/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     4993 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/secs/load.py
--rw-rw-r--   0 eric       (501) staff       (20)    27415 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/secs/makeplots.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.197120 pyspedas-1.4.8/pyspedas/solo/
--rw-rw-r--   0 eric       (501) staff       (20)    12856 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/solo/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      431 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/solo/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     3964 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/solo/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.197315 pyspedas-1.4.8/pyspedas/solo/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/solo/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     2234 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/solo/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.197511 pyspedas-1.4.8/pyspedas/sosmag/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/sosmag/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)    18450 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/sosmag/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.197727 pyspedas-1.4.8/pyspedas/sosmag/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/sosmag/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1543 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/sosmag/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.198051 pyspedas-1.4.8/pyspedas/st5/
--rw-rw-r--   0 eric       (501) staff       (20)     2648 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/st5/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      404 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/st5/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     1612 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/st5/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.198245 pyspedas-1.4.8/pyspedas/st5/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/st5/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      625 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/st5/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.198576 pyspedas-1.4.8/pyspedas/stereo/
--rw-rw-r--   0 eric       (501) staff       (20)    17602 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/stereo/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      417 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/stereo/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     3011 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/stereo/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.198771 pyspedas-1.4.8/pyspedas/stereo/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/stereo/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     2170 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/stereo/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.199086 pyspedas-1.4.8/pyspedas/swarm/
--rw-rw-r--   0 eric       (501) staff       (20)     1408 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/swarm/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)       58 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/swarm/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     1505 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/swarm/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.199285 pyspedas-1.4.8/pyspedas/swarm/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/swarm/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      508 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/swarm/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.199601 pyspedas-1.4.8/pyspedas/themis/
--rw-rw-r--   0 eric       (501) staff       (20)      733 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/__init__.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.199806 pyspedas-1.4.8/pyspedas/themis/common/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/common/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1956 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/common/check_args.py
--rw-rw-r--   0 eric       (501) staff       (20)      452 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/config.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.200005 pyspedas-1.4.8/pyspedas/themis/cotrans/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/cotrans/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     3515 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/cotrans/dsl2gse.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.200306 pyspedas-1.4.8/pyspedas/themis/ground/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/ground/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     2317 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/ground/ask.py
--rw-rw-r--   0 eric       (501) staff       (20)     8292 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/ground/gmag.py
--rw-rw-r--   0 eric       (501) staff       (20)     9971 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.200410 pyspedas-1.4.8/pyspedas/themis/spacecraft/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/spacecraft/__init__.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.201256 pyspedas-1.4.8/pyspedas/themis/spacecraft/fields/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/spacecraft/fields/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     2311 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/spacecraft/fields/efi.py
--rw-rw-r--   0 eric       (501) staff       (20)     2290 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/spacecraft/fields/fbk.py
--rw-rw-r--   0 eric       (501) staff       (20)     2290 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/spacecraft/fields/fft.py
--rw-rw-r--   0 eric       (501) staff       (20)     5964 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/spacecraft/fields/fgm.py
--rw-rw-r--   0 eric       (501) staff       (20)    16561 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/spacecraft/fields/fit.py
--rw-rw-r--   0 eric       (501) staff       (20)     2309 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/spacecraft/fields/scm.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.201826 pyspedas-1.4.8/pyspedas/themis/spacecraft/particles/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/spacecraft/particles/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     2307 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/spacecraft/particles/esa.py
--rw-rw-r--   0 eric       (501) staff       (20)     2343 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/spacecraft/particles/gmom.py
--rw-rw-r--   0 eric       (501) staff       (20)     2294 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/spacecraft/particles/mom.py
--rw-rw-r--   0 eric       (501) staff       (20)     2306 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/spacecraft/particles/sst.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.202135 pyspedas-1.4.8/pyspedas/themis/state/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/state/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     2194 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/state/slp.py
--rw-rw-r--   0 eric       (501) staff       (20)     2309 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/state/state.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.202658 pyspedas-1.4.8/pyspedas/themis/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      520 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/tests/test_cal_fit_tplot_metadata.py
--rw-rw-r--   0 eric       (501) staff       (20)     4322 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/tests/tests.py
--rw-rw-r--   0 eric       (501) staff       (20)     9008 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/tests/tests_cal_fit.py
--rw-rw-r--   0 eric       (501) staff       (20)      885 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/tests/tests_themis_check_args.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.202962 pyspedas-1.4.8/pyspedas/themis/tests/validation/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/tests/validation/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     3217 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/tests/validation/cal_fit_validation.py
--rw-rw-r--   0 eric       (501) staff       (20)      746 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/themis/tests/validation/dsl2gse.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.203288 pyspedas-1.4.8/pyspedas/twins/
--rw-rw-r--   0 eric       (501) staff       (20)     6560 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/twins/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      409 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/twins/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     2111 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/twins/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.203482 pyspedas-1.4.8/pyspedas/twins/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/twins/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      899 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/twins/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.203810 pyspedas-1.4.8/pyspedas/ulysses/
--rw-rw-r--   0 eric       (501) staff       (20)    17679 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/ulysses/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      411 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/ulysses/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     2821 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/ulysses/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.204005 pyspedas-1.4.8/pyspedas/ulysses/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/ulysses/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1804 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/ulysses/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.205230 pyspedas-1.4.8/pyspedas/utilities/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     2176 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/dailynames.py
--rw-rw-r--   0 eric       (501) staff       (20)      445 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/data_exists.py
--rw-rw-r--   0 eric       (501) staff       (20)      457 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/datasets.py
--rw-rw-r--   0 eric       (501) staff       (20)    12080 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/download.py
--rw-rw-r--   0 eric       (501) staff       (20)      828 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/interpol.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.205510 pyspedas-1.4.8/pyspedas/utilities/spice/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/spice/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     2114 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/spice/time_ephemeris.py
--rw-rw-r--   0 eric       (501) staff       (20)     1867 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/tcopy.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.206133 pyspedas-1.4.8/pyspedas/utilities/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     2599 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/tests/download_tests.py
--rw-rw-r--   0 eric       (501) staff       (20)     3419 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/tests/misc_tests.py
--rw-rw-r--   0 eric       (501) staff       (20)     2731 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/tests/time_tests.py
--rw-rw-r--   0 eric       (501) staff       (20)     2089 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/time_double.py
--rw-rw-r--   0 eric       (501) staff       (20)     2527 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/time_string.py
--rw-rw-r--   0 eric       (501) staff       (20)     2697 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/tkm2re.py
--rw-rw-r--   0 eric       (501) staff       (20)      876 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/utilities/tnames.py
--rw-rw-r--   0 eric       (501) staff       (20)      315 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/version.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.206589 pyspedas-1.4.8/pyspedas/vires/
--rw-rw-r--   0 eric       (501) staff       (20)      487 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/vires/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/vires/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     1951 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/vires/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.207075 pyspedas-1.4.8/pyspedas/wind/
--rw-rw-r--   0 eric       (501) staff       (20)    12809 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/wind/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)      404 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/wind/config.py
--rw-rw-r--   0 eric       (501) staff       (20)     2902 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/wind/load.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.207378 pyspedas-1.4.8/pyspedas/wind/tests/
--rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/wind/tests/__init__.py
--rw-rw-r--   0 eric       (501) staff       (20)     1971 2022-11-22 20:26:16.000000 pyspedas-1.4.8/pyspedas/wind/tests/tests.py
-drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-22 20:26:53.133487 pyspedas-1.4.8/pyspedas.egg-info/
--rw-r--r--   0 eric       (501) staff       (20)    13736 2022-11-22 20:26:53.000000 pyspedas-1.4.8/pyspedas.egg-info/PKG-INFO
--rw-r--r--   0 eric       (501) staff       (20)    21969 2022-11-22 20:26:53.000000 pyspedas-1.4.8/pyspedas.egg-info/SOURCES.txt
--rw-r--r--   0 eric       (501) staff       (20)        1 2022-11-22 20:26:53.000000 pyspedas-1.4.8/pyspedas.egg-info/dependency_links.txt
--rw-r--r--   0 eric       (501) staff       (20)      148 2022-11-22 20:26:53.000000 pyspedas-1.4.8/pyspedas.egg-info/requires.txt
--rw-r--r--   0 eric       (501) staff       (20)        9 2022-11-22 20:26:53.000000 pyspedas-1.4.8/pyspedas.egg-info/top_level.txt
--rw-r--r--   0 eric       (501) staff       (20)       38 2022-11-22 20:26:53.208046 pyspedas-1.4.8/setup.cfg
--rwxr-xr-x   0 eric       (501) staff       (20)     1410 2022-11-22 20:26:16.000000 pyspedas-1.4.8/setup.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.878326 pyspedas-1.4.9/
+-rw-rw-r--   0 eric       (501) staff       (20)     3332 2022-11-30 21:20:37.000000 pyspedas-1.4.9/CODE_OF_CONDUCT.md
+-rw-rw-r--   0 eric       (501) staff       (20)     1915 2022-11-30 21:20:37.000000 pyspedas-1.4.9/CONTRIBUTING.md
+-rw-rw-r--   0 eric       (501) staff       (20)     1109 2022-11-30 21:20:37.000000 pyspedas-1.4.9/LICENSE.txt
+-rw-rw-r--   0 eric       (501) staff       (20)      253 2022-11-30 21:20:37.000000 pyspedas-1.4.9/MANIFEST.in
+-rw-r--r--   0 eric       (501) staff       (20)    13736 2022-11-30 21:21:17.878083 pyspedas-1.4.9/PKG-INFO
+-rw-rw-r--   0 eric       (501) staff       (20)    13017 2022-11-30 21:20:37.000000 pyspedas-1.4.9/README.md
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.788959 pyspedas-1.4.9/pyspedas/
+-rw-rw-r--   0 eric       (501) staff       (20)     3747 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/__init__.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.790560 pyspedas-1.4.9/pyspedas/ace/
+-rw-rw-r--   0 eric       (501) staff       (20)    19061 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/ace/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      399 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/ace/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3123 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/ace/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.790838 pyspedas-1.4.9/pyspedas/ace/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/ace/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1985 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/ace/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.791252 pyspedas-1.4.9/pyspedas/akebono/
+-rw-rw-r--   0 eric       (501) staff       (20)    13223 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/akebono/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      421 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/akebono/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2128 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/akebono/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.791521 pyspedas-1.4.9/pyspedas/akebono/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/akebono/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1164 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/akebono/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.794331 pyspedas-1.4.9/pyspedas/analysis/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5042 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/avg_data.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3243 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/clean_spikes.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1490 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/deriv_data.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5763 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/dpwrspc.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7334 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/lingradest.py
+-rw-rw-r--   0 eric       (501) staff       (20)    17634 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/neutral_sheet.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2371 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/subtract_average.py
+-rw-rw-r--   0 eric       (501) staff       (20)      795 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/subtract_median.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1521 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/tcrossp.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1972 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/tdeflag.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1168 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/tdotp.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3244 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/tdpwrspc.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.794545 pyspedas-1.4.9/pyspedas/analysis/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)    11024 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/tests/tests.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6388 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/time_clip.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2061 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/time_domain_filter.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3404 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/tinterpol.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1509 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/tnormalize.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3251 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/tsmooth.py
+-rw-rw-r--   0 eric       (501) staff       (20)    30016 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/twavpol.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2504 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/wavelet.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1800 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/analysis/yclip.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.795035 pyspedas-1.4.9/pyspedas/cdagui/
+-rw-rw-r--   0 eric       (501) staff       (20)      121 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cdagui/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)    15999 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cdagui/cdagui.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5756 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cdagui/cdaweb.py
+-rw-rw-r--   0 eric       (501) staff       (20)      234 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cdagui/config.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.795565 pyspedas-1.4.9/pyspedas/cluster/
+-rw-rw-r--   0 eric       (501) staff       (20)    23559 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cluster/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      419 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cluster/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4020 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cluster/load.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7012 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cluster/load_csa.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.795800 pyspedas-1.4.9/pyspedas/cluster/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cluster/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2857 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cluster/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.796222 pyspedas-1.4.9/pyspedas/cnofs/
+-rw-rw-r--   0 eric       (501) staff       (20)     6405 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cnofs/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      409 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cnofs/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1936 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cnofs/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.796464 pyspedas-1.4.9/pyspedas/cnofs/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cnofs/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1040 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cnofs/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.798650 pyspedas-1.4.9/pyspedas/cotrans/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3966 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/cotrans.py
+-rw-rw-r--   0 eric       (501) staff       (20)      851 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/cotrans_get_coord.py
+-rw-rw-r--   0 eric       (501) staff       (20)    30417 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/cotrans_lib.py
+-rw-rw-r--   0 eric       (501) staff       (20)      952 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/cotrans_set_coord.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2265 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/fac_matrix_make.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2327 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/gsm2lmn.py
+-rw-rw-r--   0 eric       (501) staff       (20)    17808 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/igrf.py
+-rw-rw-r--   0 eric       (501) staff       (20)    13130 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/j2000.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5141 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/matrix_array_lib.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1703 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/minvar.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2372 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/minvar_matrix_make.py
+-rw-rw-r--   0 eric       (501) staff       (20)    25354 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/quaternions.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.799096 pyspedas-1.4.9/pyspedas/cotrans/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     8316 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/tests/cotrans.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1235 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/tests/quaternions.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3024 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/tvector_rotate.py
+-rw-rw-r--   0 eric       (501) staff       (20)      847 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/cotrans/xyz_to_polar.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.799641 pyspedas-1.4.9/pyspedas/csswe/
+-rw-rw-r--   0 eric       (501) staff       (20)     2575 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/csswe/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      409 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/csswe/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1671 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/csswe/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.799880 pyspedas-1.4.9/pyspedas/csswe/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/csswe/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      640 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/csswe/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.800299 pyspedas-1.4.9/pyspedas/de2/
+-rw-rw-r--   0 eric       (501) staff       (20)    19109 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/de2/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      407 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/de2/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2832 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/de2/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.800659 pyspedas-1.4.9/pyspedas/de2/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/de2/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1968 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/de2/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.801191 pyspedas-1.4.9/pyspedas/dscovr/
+-rw-rw-r--   0 eric       (501) staff       (20)     9992 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/dscovr/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      408 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/dscovr/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2299 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/dscovr/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.801488 pyspedas-1.4.9/pyspedas/dscovr/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/dscovr/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1433 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/dscovr/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.802199 pyspedas-1.4.9/pyspedas/equator_s/
+-rw-rw-r--   0 eric       (501) staff       (20)    14979 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/equator_s/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      427 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/equator_s/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2571 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/equator_s/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.802547 pyspedas-1.4.9/pyspedas/equator_s/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/equator_s/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1377 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/equator_s/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.802891 pyspedas-1.4.9/pyspedas/erg/
+-rw-rw-r--   0 eric       (501) staff       (20)     1465 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      515 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/config.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.803067 pyspedas-1.4.9/pyspedas/erg/ground/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/__init__.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.803362 pyspedas-1.4.9/pyspedas/erg/ground/camera/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/camera/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7748 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/camera/camera_omti_asi.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.804484 pyspedas-1.4.9/pyspedas/erg/ground/geomag/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/geomag/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6106 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/geomag/gmag_isee_fluxgate.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5390 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/geomag/gmag_isee_induction.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6018 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/geomag/gmag_magdas_1sec.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6136 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/geomag/gmag_mm210.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1049 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/geomag/gmag_stel_fluxgate.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1193 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/geomag/gmag_stel_induction.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.804638 pyspedas-1.4.9/pyspedas/erg/ground/radar/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/radar/__init__.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.805078 pyspedas-1.4.9/pyspedas/erg/ground/radar/superdarn/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/radar/superdarn/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      720 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/radar/superdarn/get_sphcntr.py
+-rw-rw-r--   0 eric       (501) staff       (20)    25115 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/radar/superdarn/sd_fit.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.805479 pyspedas-1.4.9/pyspedas/erg/ground/riometer/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/riometer/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7768 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/riometer/isee_brio.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.805800 pyspedas-1.4.9/pyspedas/erg/ground/vlf/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/vlf/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5373 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/ground/vlf/isee_vlf.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.805963 pyspedas-1.4.9/pyspedas/erg/satellite/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/__init__.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.806405 pyspedas-1.4.9/pyspedas/erg/satellite/erg/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/__init__.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.806758 pyspedas-1.4.9/pyspedas/erg/satellite/erg/att/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/att/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4110 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/att/att.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.806911 pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/__init__.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.808124 pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      551 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/cart_trans_matrix_make.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3963 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/dsi2j2000.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7210 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/erg_cotrans.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6195 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/erg_interpolate_att.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2945 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/sga2sgi.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2651 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/sgi2dsi.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2344 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/vector_rotate.py
+-rw-rw-r--   0 eric       (501) staff       (20)      525 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/config.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.808446 pyspedas-1.4.9/pyspedas/erg/satellite/erg/hep/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/hep/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)    21725 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/hep/hep.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.808783 pyspedas-1.4.9/pyspedas/erg/satellite/erg/lepe/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/lepe/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)    15170 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/lepe/lepe.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.809069 pyspedas-1.4.9/pyspedas/erg/satellite/erg/lepi/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/lepi/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)    13951 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/lepi/lepi.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2749 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.809514 pyspedas-1.4.9/pyspedas/erg/satellite/erg/mepe/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/mepe/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6832 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/mepe/mepe.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.810003 pyspedas-1.4.9/pyspedas/erg/satellite/erg/mepi/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/mepi/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6702 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/mepi/mepi_nml.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5576 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/mepi/mepi_tof.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.810371 pyspedas-1.4.9/pyspedas/erg/satellite/erg/mgf/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/mgf/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)    11494 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/mgf/mgf.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.810787 pyspedas-1.4.9/pyspedas/erg/satellite/erg/orb/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/orb/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)    14087 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/orb/orb.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2226 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/orb/remove_duplicated_tframe.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.815665 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4270 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_convert_flux_units.py
+-rw-rw-r--   0 eric       (501) staff       (20)    15517 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_hep_get_dist.py
+-rw-rw-r--   0 eric       (501) staff       (20)    15772 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_hep_part_products.py
+-rw-rw-r--   0 eric       (501) staff       (20)    21905 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_lep_part_products.py
+-rw-rw-r--   0 eric       (501) staff       (20)    12762 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_lepe_get_dist.py
+-rw-rw-r--   0 eric       (501) staff       (20)    10839 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_lepi_get_dist.py
+-rw-rw-r--   0 eric       (501) staff       (20)    18033 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_mep_part_products.py
+-rw-rw-r--   0 eric       (501) staff       (20)     9766 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_mepe_get_dist.py
+-rw-rw-r--   0 eric       (501) staff       (20)    10528 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_mepi_get_dist.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2647 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_clean_data.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1110 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_do_fac.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2728 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_limit_range.py
+-rw-rw-r--   0 eric       (501) staff       (20)      826 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_make_e_spec.py
+-rw-rw-r--   0 eric       (501) staff       (20)    13111 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_make_fac.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5366 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_make_phi_spec.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4955 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_make_theta_spec.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1655 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_make_tplot.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2019 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_moments_tplot.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1260 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_progress_update.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2727 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_units_string.py
+-rw-rw-r--   0 eric       (501) staff       (20)     9610 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_xep_get_dist.py
+-rw-rw-r--   0 eric       (501) staff       (20)     9927 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_xep_part_products.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1443 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/get_lepi_flux_angle_in_sga.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1660 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/get_mepe_az_dir_in_sga.py
+-rw-rw-r--   0 eric       (501) staff       (20)      666 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/get_mepe_flux_angle_in_sga.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1343 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/get_mepi_flux_angle_in_sga.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.816590 pyspedas-1.4.9/pyspedas/erg/satellite/erg/pwe/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/pwe/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     8933 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/pwe/pwe_efd.py
+-rw-rw-r--   0 eric       (501) staff       (20)    10279 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/pwe/pwe_hfa.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5916 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/pwe/pwe_ofa.py
+-rw-rw-r--   0 eric       (501) staff       (20)    11534 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/pwe/pwe_wfc.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.816827 pyspedas-1.4.9/pyspedas/erg/satellite/erg/xep/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/xep/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7865 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/satellite/erg/xep/xep.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.817085 pyspedas-1.4.9/pyspedas/erg/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3428 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/erg/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.817545 pyspedas-1.4.9/pyspedas/fast/
+-rw-rw-r--   0 eric       (501) staff       (20)     8770 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/fast/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      404 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/fast/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2274 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/fast/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.817808 pyspedas-1.4.9/pyspedas/fast/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/fast/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1365 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/fast/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.819001 pyspedas-1.4.9/pyspedas/geopack/
+-rw-rw-r--   0 eric       (501) staff       (20)      133 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/geopack/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6092 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/geopack/get_tsy_params.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3386 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/geopack/get_w_params.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2093 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/geopack/t01.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1830 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/geopack/t89.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1962 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/geopack/t96.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.819304 pyspedas-1.4.9/pyspedas/geopack/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/geopack/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4101 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/geopack/tests/tests.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2268 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/geopack/ts04.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.819821 pyspedas-1.4.9/pyspedas/geotail/
+-rw-rw-r--   0 eric       (501) staff       (20)    13020 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/geotail/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      419 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/geotail/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2604 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/geotail/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.820152 pyspedas-1.4.9/pyspedas/geotail/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/geotail/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1352 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/geotail/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.820856 pyspedas-1.4.9/pyspedas/goes/
+-rw-rw-r--   0 eric       (501) staff       (20)    11443 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/goes/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      406 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/goes/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7081 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/goes/load.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1617 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/goes/load_orbit.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.821201 pyspedas-1.4.9/pyspedas/goes/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/goes/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4466 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/goes/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.821532 pyspedas-1.4.9/pyspedas/hapi/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/hapi/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5443 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/hapi/hapi.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.821847 pyspedas-1.4.9/pyspedas/hapi/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/hapi/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1336 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/hapi/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.822327 pyspedas-1.4.9/pyspedas/image/
+-rw-rw-r--   0 eric       (501) staff       (20)    14745 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/image/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      409 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/image/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2688 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/image/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.822621 pyspedas-1.4.9/pyspedas/image/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/image/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1664 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/image/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.823125 pyspedas-1.4.9/pyspedas/kyoto/
+-rw-rw-r--   0 eric       (501) staff       (20)       26 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/kyoto/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4411 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/kyoto/load_dst.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.823498 pyspedas-1.4.9/pyspedas/kyoto/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/kyoto/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      775 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/kyoto/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.824121 pyspedas-1.4.9/pyspedas/lanl/
+-rw-rw-r--   0 eric       (501) staff       (20)     5640 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/lanl/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      409 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/lanl/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1827 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/lanl/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.824527 pyspedas-1.4.9/pyspedas/lanl/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/lanl/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1076 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/lanl/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.826459 pyspedas-1.4.9/pyspedas/maven/
+-rw-rw-r--   0 eric       (501) staff       (20)     9965 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/maven/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      334 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/maven/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7009 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/maven/download_files_utilities.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1940 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/maven/file_regex.py
+-rw-rw-r--   0 eric       (501) staff       (20)    21768 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/maven/maven_kp_to_tplot.py
+-rw-rw-r--   0 eric       (501) staff       (20)    13748 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/maven/maven_load.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1609 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/maven/orbit_time.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.826806 pyspedas-1.4.9/pyspedas/maven/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/maven/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1929 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/maven/tests/tests.py
+-rw-rw-r--   0 eric       (501) staff       (20)    79453 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/maven/utilities.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.827283 pyspedas-1.4.9/pyspedas/mica/
+-rw-rw-r--   0 eric       (501) staff       (20)     2931 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mica/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      391 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mica/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1843 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mica/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.827524 pyspedas-1.4.9/pyspedas/mica/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mica/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      854 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mica/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.829860 pyspedas-1.4.9/pyspedas/mms/
+-rw-rw-r--   0 eric       (501) staff       (20)     2433 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/__init__.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.830155 pyspedas-1.4.9/pyspedas/mms/aspoc/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/aspoc/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4054 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/aspoc/aspoc.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.830867 pyspedas-1.4.9/pyspedas/mms/cotrans/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/cotrans/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3641 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/cotrans/mms_cotrans_lmn.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1597 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/cotrans/mms_cotrans_qrotate.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1392 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/cotrans/mms_cotrans_qtransformer.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4668 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/cotrans/mms_qcotrans.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.831251 pyspedas-1.4.9/pyspedas/mms/dsp/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/dsp/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4223 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/dsp/dsp.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7433 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/dsp/mms_dsp_set_metadata.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.831618 pyspedas-1.4.9/pyspedas/mms/edi/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/edi/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4237 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/edi/edi.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3513 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/edi/mms_edi_set_metadata.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.831984 pyspedas-1.4.9/pyspedas/mms/edp/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/edp/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4258 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/edp/edp.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2555 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/edp/mms_edp_set_metadata.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.832975 pyspedas-1.4.9/pyspedas/mms/eis/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/eis/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)    12211 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/eis/eis.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3678 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/eis/mms_eis_omni.py
+-rw-rw-r--   0 eric       (501) staff       (20)     9763 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/eis/mms_eis_pad.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3951 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/eis/mms_eis_pad_spinavg.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1420 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/eis/mms_eis_set_metadata.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7462 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/eis/mms_eis_spec_combine_sc.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3830 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/eis/mms_eis_spin_avg.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.835443 pyspedas-1.4.9/pyspedas/mms/feeps/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6626 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/feeps.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3317 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_active_eyes.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1942 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_correct_energies.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2091 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_energy_table.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5775 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_flat_field_corrections.py
+-rw-rw-r--   0 eric       (501) staff       (20)    15000 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_getgyrophase.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6564 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_gpd.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7114 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_omni.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7736 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_pad.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4041 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_pad_spinavg.py
+-rw-rw-r--   0 eric       (501) staff       (20)    14414 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_pitch_angles.py
+-rw-rw-r--   0 eric       (501) staff       (20)    15888 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_remove_bad_data.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3462 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_remove_sun.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2759 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_spin_avg.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2741 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_split_integral_ch.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2170 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/mms_read_feeps_sector_masks_csv.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.841509 pyspedas-1.4.9/pyspedas/mms/feeps/sun/
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20151111.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20160709.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20161028.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20170531.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20171003.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20181005.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20220113.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20220506.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3135 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS1_FEEPS_ContaminatedSectors_20220815.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20151111.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20160709.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20161028.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20170531.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20171003.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20181005.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20220113.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20220506.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS2_FEEPS_ContaminatedSectors_20220815.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20151111.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20160709.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20161028.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20170531.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20171003.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20181005.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20220113.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20220506.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS3_FEEPS_ContaminatedSectors_20220815.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20151111.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20160709.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20161028.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20170531.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20171003.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3072 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20181005.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20220113.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20220506.csv
+-rw-rw-r--   0 eric       (501) staff       (20)     3071 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/feeps/sun/MMS4_FEEPS_ContaminatedSectors_20220815.csv
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.842745 pyspedas-1.4.9/pyspedas/mms/fgm/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fgm/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7195 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fgm/fgm.py
+-rw-rw-r--   0 eric       (501) staff       (20)     9700 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fgm/mms_curl.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2414 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fgm/mms_fgm_remove_flags.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4491 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fgm/mms_fgm_set_metadata.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3905 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fgm/mms_lingradest.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1774 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fgm/mms_split_fgm_data.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.845142 pyspedas-1.4.9/pyspedas/mms/fpi/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fpi/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)    15367 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fpi/fpi.py
+-rw-rw-r--   0 eric       (501) staff       (20)     9259 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fpi/mms_fpi_ang_ang.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3113 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fpi/mms_fpi_make_compressionlossbars.py
+-rw-rw-r--   0 eric       (501) staff       (20)    14088 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fpi/mms_fpi_make_errorflagbars.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7916 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fpi/mms_fpi_set_metadata.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2189 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fpi/mms_fpi_split_tensor.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6807 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fpi/mms_get_fpi_dist.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4368 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fpi/mms_load_fpi_calc_pad.py
+-rw-rw-r--   0 eric       (501) staff       (20)    13596 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fpi/mms_pad_fpi.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.845550 pyspedas-1.4.9/pyspedas/mms/fsm/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fsm/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3844 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/fsm/fsm.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.847156 pyspedas-1.4.9/pyspedas/mms/hpca/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/hpca/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     8024 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/hpca/hpca.py
+-rw-rw-r--   0 eric       (501) staff       (20)     8055 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/hpca/mms_get_hpca_dist.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3255 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/hpca/mms_get_hpca_info.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3609 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/hpca/mms_hpca_calc_anodes.py
+-rw-rw-r--   0 eric       (501) staff       (20)      690 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/hpca/mms_hpca_energies.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2817 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/hpca/mms_hpca_set_metadata.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2698 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/hpca/mms_hpca_spin_sum.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.848969 pyspedas-1.4.9/pyspedas/mms/mec/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mec/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)   769966 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mec/earth_polar1.png
+-rw-rw-r--   0 eric       (501) staff       (20)     4616 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mec/mec.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4652 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mec/mms_mec_set_metadata.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.849925 pyspedas-1.4.9/pyspedas/mms/mec_ascii/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mec_ascii/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2862 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mec_ascii/mms_get_local_state_files.py
+-rw-rw-r--   0 eric       (501) staff       (20)     6175 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mec_ascii/mms_get_state_data.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2539 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mec_ascii/mms_load_att_tplot.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2504 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mec_ascii/mms_load_eph_tplot.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1571 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mec_ascii/state.py
+-rw-rw-r--   0 eric       (501) staff       (20)      782 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mms_config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3006 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mms_events.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3602 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mms_file_filter.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1643 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mms_files_in_interval.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4425 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mms_get_local_files.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2807 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mms_load_brst_segments.py
+-rw-rw-r--   0 eric       (501) staff       (20)    10581 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mms_load_data.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5562 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mms_load_data_spdf.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2596 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mms_load_fast_segments.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3944 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mms_load_sroi_segments.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2437 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mms_login_lasp.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3399 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mms_orbit_plot.py
+-rw-rw-r--   0 eric       (501) staff       (20)      507 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mms_python_startup.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1132 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/mms_tai2unix.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.852442 pyspedas-1.4.9/pyspedas/mms/particles/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/particles/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2830 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/particles/mms_convert_flux_units.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2711 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/particles/mms_part_des_photoelectrons.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7786 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/particles/mms_part_getspec.py
+-rw-rw-r--   0 eric       (501) staff       (20)    16515 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/particles/mms_part_products.py
+-rw-rw-r--   0 eric       (501) staff       (20)    11103 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/particles/mms_part_slice2d.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1836 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/particles/mms_pgs_clean_data.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1459 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/particles/mms_pgs_clean_support.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1424 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/particles/mms_pgs_make_e_spec.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5066 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/particles/mms_pgs_make_fac.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1160 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/particles/mms_pgs_make_phi_spec.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1388 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/particles/mms_pgs_make_theta_spec.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1075 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/particles/mms_pgs_split_hpca.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3236 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/particles/moka_mms_clean_data.py
+-rw-rw-r--   0 eric       (501) staff       (20)      645 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/print_vars.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.852880 pyspedas-1.4.9/pyspedas/mms/scm/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/scm/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1603 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/scm/mms_scm_set_metadata.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5414 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/scm/scm.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1896 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/spd_mms_load_bss.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.854720 pyspedas-1.4.9/pyspedas/mms/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      575 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/tests/cotrans.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3691 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/tests/curlometer.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1919 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/tests/data_rate_segments.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4620 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/tests/eis.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5625 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/tests/feeps.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3564 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/tests/file_filter.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2723 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/tests/fpi_tests.py
+-rw-rw-r--   0 eric       (501) staff       (20)    22209 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/tests/load_routine_tests.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5789 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/tests/mms_part_getspec.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2595 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/tests/neutral_sheet.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4343 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/tests/ql_l1b_sitl_tests.py
+-rw-rw-r--   0 eric       (501) staff       (20)      228 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/tests/setup_tests.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5867 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/tests/slice2d.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2341 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/mms/tests/wavpol.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.855067 pyspedas-1.4.9/pyspedas/omni/
+-rw-rw-r--   0 eric       (501) staff       (20)     2552 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/omni/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      416 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/omni/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2252 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/omni/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.855275 pyspedas-1.4.9/pyspedas/omni/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/omni/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2041 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/omni/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.855489 pyspedas-1.4.9/pyspedas/particles/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/__init__.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.856065 pyspedas-1.4.9/pyspedas/particles/moments/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/moments/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3465 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/moments/moments_3d.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1948 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/moments/moments_3d_omega_weights.py
+-rw-rw-r--   0 eric       (501) staff       (20)      475 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/moments/spd_pgs_moments.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1326 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/moments/spd_pgs_moments_tplot.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.857134 pyspedas-1.4.9/pyspedas/particles/spd_part_products/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_part_products/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1061 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_do_fac.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2160 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_limit_range.py
+-rw-rw-r--   0 eric       (501) staff       (20)      834 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_make_e_spec.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4821 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_make_phi_spec.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4244 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_make_theta_spec.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1571 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_make_tplot.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1243 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_progress_update.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2745 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_regrid.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.860568 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2113 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/quaternions.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3394 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice1d_plot.py
+-rw-rw-r--   0 eric       (501) staff       (20)    13802 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3388 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_2di.py
+-rw-rw-r--   0 eric       (501) staff       (20)      749 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_checkbins.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2419 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_collate.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1502 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_custom_rotation.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5883 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_geo.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3417 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_get_data.py
+-rw-rw-r--   0 eric       (501) staff       (20)      853 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_get_ebounds.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1473 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_get_sphere.py
+-rw-rw-r--   0 eric       (501) staff       (20)      753 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_get_support.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2702 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_getinfo.py
+-rw-rw-r--   0 eric       (501) staff       (20)      682 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_intrange.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1025 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_nearest.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1986 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_orientslice.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3681 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_plot.py
+-rw-rw-r--   0 eric       (501) staff       (20)      819 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_rlog.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3005 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_rotate.py
+-rw-rw-r--   0 eric       (501) staff       (20)      556 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_s2c.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1686 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_smooth.py
+-rw-rw-r--   0 eric       (501) staff       (20)      731 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_subtract.py
+-rw-rw-r--   0 eric       (501) staff       (20)      776 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/spd_cal_rot.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1236 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_slice2d/tplot_average.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1114 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/particles/spd_units_string.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.860940 pyspedas-1.4.9/pyspedas/poes/
+-rw-rw-r--   0 eric       (501) staff       (20)     2493 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/poes/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      404 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/poes/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1757 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/poes/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.861162 pyspedas-1.4.9/pyspedas/poes/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/poes/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1173 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/poes/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.861554 pyspedas-1.4.9/pyspedas/polar/
+-rw-rw-r--   0 eric       (501) staff       (20)    25546 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/polar/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      409 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/polar/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3442 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/polar/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.861770 pyspedas-1.4.9/pyspedas/polar/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/polar/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2143 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/polar/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.862377 pyspedas-1.4.9/pyspedas/psp/
+-rw-rw-r--   0 eric       (501) staff       (20)    21250 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/psp/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      552 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/psp/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)    12844 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/psp/filter.py
+-rw-rw-r--   0 eric       (501) staff       (20)     9064 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/psp/load.py
+-rw-rw-r--   0 eric       (501) staff       (20)      800 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/psp/rfs.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.862598 pyspedas-1.4.9/pyspedas/psp/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/psp/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7362 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/psp/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.862967 pyspedas-1.4.9/pyspedas/rbsp/
+-rw-rw-r--   0 eric       (501) staff       (20)    19071 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/rbsp/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      404 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/rbsp/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5264 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/rbsp/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.863670 pyspedas-1.4.9/pyspedas/rbsp/rbspice_lib/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/rbsp/rbspice_lib/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4264 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/rbsp/rbspice_lib/rbsp_load_rbspice_read.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2865 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_omni.py
+-rw-rw-r--   0 eric       (501) staff       (20)     7484 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_pad.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4755 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_pad_spinavg.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4145 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_spin_avg.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.863889 pyspedas-1.4.9/pyspedas/rbsp/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/rbsp/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5153 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/rbsp/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.864343 pyspedas-1.4.9/pyspedas/secs/
+-rw-rw-r--   0 eric       (501) staff       (20)     6701 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/secs/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1011 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/secs/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4993 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/secs/load.py
+-rw-rw-r--   0 eric       (501) staff       (20)    27415 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/secs/makeplots.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.864695 pyspedas-1.4.9/pyspedas/solo/
+-rw-rw-r--   0 eric       (501) staff       (20)    12856 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/solo/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      431 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/solo/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3964 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/solo/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.864918 pyspedas-1.4.9/pyspedas/solo/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/solo/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2243 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/solo/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.865156 pyspedas-1.4.9/pyspedas/sosmag/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/sosmag/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)    18450 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/sosmag/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.865386 pyspedas-1.4.9/pyspedas/sosmag/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/sosmag/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1543 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/sosmag/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.865763 pyspedas-1.4.9/pyspedas/st5/
+-rw-rw-r--   0 eric       (501) staff       (20)     2648 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/st5/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      404 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/st5/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1612 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/st5/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.865993 pyspedas-1.4.9/pyspedas/st5/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/st5/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      625 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/st5/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.866377 pyspedas-1.4.9/pyspedas/stereo/
+-rw-rw-r--   0 eric       (501) staff       (20)    17602 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/stereo/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      417 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/stereo/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3011 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/stereo/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.866594 pyspedas-1.4.9/pyspedas/stereo/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/stereo/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2170 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/stereo/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.866933 pyspedas-1.4.9/pyspedas/swarm/
+-rw-rw-r--   0 eric       (501) staff       (20)     1408 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/swarm/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)       58 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/swarm/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1505 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/swarm/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.867142 pyspedas-1.4.9/pyspedas/swarm/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/swarm/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      508 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/swarm/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.867493 pyspedas-1.4.9/pyspedas/themis/
+-rw-rw-r--   0 eric       (501) staff       (20)      733 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/__init__.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.867709 pyspedas-1.4.9/pyspedas/themis/common/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/common/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1956 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/common/check_args.py
+-rw-rw-r--   0 eric       (501) staff       (20)      452 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/config.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.867924 pyspedas-1.4.9/pyspedas/themis/cotrans/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/cotrans/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3515 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/cotrans/dsl2gse.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.868253 pyspedas-1.4.9/pyspedas/themis/ground/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/ground/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2317 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/ground/ask.py
+-rw-rw-r--   0 eric       (501) staff       (20)     8292 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/ground/gmag.py
+-rw-rw-r--   0 eric       (501) staff       (20)     9971 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.868375 pyspedas-1.4.9/pyspedas/themis/spacecraft/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/spacecraft/__init__.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.869429 pyspedas-1.4.9/pyspedas/themis/spacecraft/fields/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/spacecraft/fields/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2311 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/spacecraft/fields/efi.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2290 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/spacecraft/fields/fbk.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2290 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/spacecraft/fields/fft.py
+-rw-rw-r--   0 eric       (501) staff       (20)     5964 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/spacecraft/fields/fgm.py
+-rw-rw-r--   0 eric       (501) staff       (20)    16561 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/spacecraft/fields/fit.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2309 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/spacecraft/fields/scm.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.870067 pyspedas-1.4.9/pyspedas/themis/spacecraft/particles/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/spacecraft/particles/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2307 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/spacecraft/particles/esa.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2343 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/spacecraft/particles/gmom.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2294 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/spacecraft/particles/mom.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2306 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/spacecraft/particles/sst.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.870434 pyspedas-1.4.9/pyspedas/themis/state/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/state/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2194 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/state/slp.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2309 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/state/state.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.871003 pyspedas-1.4.9/pyspedas/themis/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      520 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/tests/test_cal_fit_tplot_metadata.py
+-rw-rw-r--   0 eric       (501) staff       (20)     4322 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/tests/tests.py
+-rw-rw-r--   0 eric       (501) staff       (20)     9008 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/tests/tests_cal_fit.py
+-rw-rw-r--   0 eric       (501) staff       (20)      885 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/tests/tests_themis_check_args.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.871385 pyspedas-1.4.9/pyspedas/themis/tests/validation/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/tests/validation/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3217 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/tests/validation/cal_fit_validation.py
+-rw-rw-r--   0 eric       (501) staff       (20)      746 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/themis/tests/validation/dsl2gse.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.871784 pyspedas-1.4.9/pyspedas/twins/
+-rw-rw-r--   0 eric       (501) staff       (20)     6560 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/twins/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      409 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/twins/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2111 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/twins/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.872050 pyspedas-1.4.9/pyspedas/twins/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/twins/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      899 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/twins/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.872591 pyspedas-1.4.9/pyspedas/ulysses/
+-rw-rw-r--   0 eric       (501) staff       (20)    17679 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/ulysses/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      411 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/ulysses/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2821 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/ulysses/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.872922 pyspedas-1.4.9/pyspedas/ulysses/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/ulysses/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1804 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/ulysses/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.874981 pyspedas-1.4.9/pyspedas/utilities/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2176 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/dailynames.py
+-rw-rw-r--   0 eric       (501) staff       (20)      445 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/data_exists.py
+-rw-rw-r--   0 eric       (501) staff       (20)      457 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/datasets.py
+-rw-rw-r--   0 eric       (501) staff       (20)    12080 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/download.py
+-rw-rw-r--   0 eric       (501) staff       (20)      828 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/interpol.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2009 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/leap_seconds.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.875366 pyspedas-1.4.9/pyspedas/utilities/spice/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/spice/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2114 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/spice/time_ephemeris.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1867 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/tcopy.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.876241 pyspedas-1.4.9/pyspedas/utilities/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2599 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/tests/download_tests.py
+-rw-rw-r--   0 eric       (501) staff       (20)     3419 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/tests/misc_tests.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2731 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/tests/time_tests.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2089 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/time_double.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2527 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/time_string.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2697 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/tkm2re.py
+-rw-rw-r--   0 eric       (501) staff       (20)      876 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/utilities/tnames.py
+-rw-rw-r--   0 eric       (501) staff       (20)      315 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/version.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.876800 pyspedas-1.4.9/pyspedas/vires/
+-rw-rw-r--   0 eric       (501) staff       (20)      487 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/vires/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/vires/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1951 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/vires/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.877381 pyspedas-1.4.9/pyspedas/wind/
+-rw-rw-r--   0 eric       (501) staff       (20)    12809 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/wind/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)      404 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/wind/config.py
+-rw-rw-r--   0 eric       (501) staff       (20)     2902 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/wind/load.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.877720 pyspedas-1.4.9/pyspedas/wind/tests/
+-rw-rw-r--   0 eric       (501) staff       (20)        0 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/wind/tests/__init__.py
+-rw-rw-r--   0 eric       (501) staff       (20)     1971 2022-11-30 21:20:37.000000 pyspedas-1.4.9/pyspedas/wind/tests/tests.py
+drwxr-xr-x   0 eric       (501) staff       (20)        0 2022-11-30 21:21:17.790030 pyspedas-1.4.9/pyspedas.egg-info/
+-rw-r--r--   0 eric       (501) staff       (20)    13736 2022-11-30 21:21:17.000000 pyspedas-1.4.9/pyspedas.egg-info/PKG-INFO
+-rw-r--r--   0 eric       (501) staff       (20)    22060 2022-11-30 21:21:17.000000 pyspedas-1.4.9/pyspedas.egg-info/SOURCES.txt
+-rw-r--r--   0 eric       (501) staff       (20)        1 2022-11-30 21:21:17.000000 pyspedas-1.4.9/pyspedas.egg-info/dependency_links.txt
+-rw-r--r--   0 eric       (501) staff       (20)      148 2022-11-30 21:21:17.000000 pyspedas-1.4.9/pyspedas.egg-info/requires.txt
+-rw-r--r--   0 eric       (501) staff       (20)        9 2022-11-30 21:21:17.000000 pyspedas-1.4.9/pyspedas.egg-info/top_level.txt
+-rw-r--r--   0 eric       (501) staff       (20)       38 2022-11-30 21:21:17.878378 pyspedas-1.4.9/setup.cfg
+-rwxr-xr-x   0 eric       (501) staff       (20)     1410 2022-11-30 21:20:37.000000 pyspedas-1.4.9/setup.py
```

### Comparing `pyspedas-1.4.8/CODE_OF_CONDUCT.md` & `pyspedas-1.4.9/CODE_OF_CONDUCT.md`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/CONTRIBUTING.md` & `pyspedas-1.4.9/CONTRIBUTING.md`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/LICENSE.txt` & `pyspedas-1.4.9/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/PKG-INFO` & `pyspedas-1.4.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyspedas
-Version: 1.4.8
+Version: 1.4.9
 Summary: Python Space Physics Environment Data Analysis Software (pySPEDAS)
 Home-page: https://github.com/spedas/pyspedas
 Author: Nick Hatzigeorgiu, Eric Grimes
 Author-email: nikos@berkeley.edu, egrimes@igpp.ucla.edu
 License: MIT
 Project-URL: Information, http://spedas.org/wiki/
 Keywords: spedas data tools
```

### Comparing `pyspedas-1.4.8/README.md` & `pyspedas-1.4.9/README.md`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/__init__.py` & `pyspedas-1.4.9/pyspedas/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/ace/__init__.py` & `pyspedas-1.4.9/pyspedas/ace/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/ace/load.py` & `pyspedas-1.4.9/pyspedas/ace/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/ace/tests/tests.py` & `pyspedas-1.4.9/pyspedas/ace/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/akebono/__init__.py` & `pyspedas-1.4.9/pyspedas/akebono/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/akebono/load.py` & `pyspedas-1.4.9/pyspedas/akebono/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/akebono/tests/tests.py` & `pyspedas-1.4.9/pyspedas/akebono/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/avg_data.py` & `pyspedas-1.4.9/pyspedas/analysis/avg_data.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/clean_spikes.py` & `pyspedas-1.4.9/pyspedas/analysis/clean_spikes.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/deriv_data.py` & `pyspedas-1.4.9/pyspedas/analysis/deriv_data.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/dpwrspc.py` & `pyspedas-1.4.9/pyspedas/analysis/dpwrspc.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/lingradest.py` & `pyspedas-1.4.9/pyspedas/analysis/lingradest.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/neutral_sheet.py` & `pyspedas-1.4.9/pyspedas/analysis/neutral_sheet.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/subtract_average.py` & `pyspedas-1.4.9/pyspedas/analysis/subtract_average.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/subtract_median.py` & `pyspedas-1.4.9/pyspedas/analysis/subtract_median.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/tcrossp.py` & `pyspedas-1.4.9/pyspedas/analysis/tcrossp.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/tdeflag.py` & `pyspedas-1.4.9/pyspedas/analysis/tdeflag.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/tdotp.py` & `pyspedas-1.4.9/pyspedas/analysis/tdotp.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/tdpwrspc.py` & `pyspedas-1.4.9/pyspedas/analysis/tdpwrspc.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/tests/tests.py` & `pyspedas-1.4.9/pyspedas/analysis/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/time_clip.py` & `pyspedas-1.4.9/pyspedas/analysis/time_clip.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/time_domain_filter.py` & `pyspedas-1.4.9/pyspedas/analysis/time_domain_filter.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/tinterpol.py` & `pyspedas-1.4.9/pyspedas/analysis/tinterpol.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/tnormalize.py` & `pyspedas-1.4.9/pyspedas/analysis/tnormalize.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/tsmooth.py` & `pyspedas-1.4.9/pyspedas/analysis/tsmooth.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/twavpol.py` & `pyspedas-1.4.9/pyspedas/analysis/twavpol.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/wavelet.py` & `pyspedas-1.4.9/pyspedas/analysis/wavelet.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/analysis/yclip.py` & `pyspedas-1.4.9/pyspedas/analysis/yclip.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cdagui/cdagui.py` & `pyspedas-1.4.9/pyspedas/cdagui/cdagui.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cdagui/cdaweb.py` & `pyspedas-1.4.9/pyspedas/cdagui/cdaweb.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cluster/__init__.py` & `pyspedas-1.4.9/pyspedas/cluster/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cluster/load.py` & `pyspedas-1.4.9/pyspedas/cluster/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cluster/load_csa.py` & `pyspedas-1.4.9/pyspedas/cluster/load_csa.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cluster/tests/tests.py` & `pyspedas-1.4.9/pyspedas/cluster/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cnofs/__init__.py` & `pyspedas-1.4.9/pyspedas/cnofs/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cnofs/load.py` & `pyspedas-1.4.9/pyspedas/cnofs/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cnofs/tests/tests.py` & `pyspedas-1.4.9/pyspedas/cnofs/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/cotrans.py` & `pyspedas-1.4.9/pyspedas/cotrans/cotrans.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/cotrans_get_coord.py` & `pyspedas-1.4.9/pyspedas/cotrans/cotrans_get_coord.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/cotrans_lib.py` & `pyspedas-1.4.9/pyspedas/cotrans/cotrans_lib.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/cotrans_set_coord.py` & `pyspedas-1.4.9/pyspedas/cotrans/cotrans_set_coord.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/fac_matrix_make.py` & `pyspedas-1.4.9/pyspedas/cotrans/fac_matrix_make.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/gsm2lmn.py` & `pyspedas-1.4.9/pyspedas/cotrans/gsm2lmn.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/igrf.py` & `pyspedas-1.4.9/pyspedas/cotrans/igrf.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/j2000.py` & `pyspedas-1.4.9/pyspedas/cotrans/j2000.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/matrix_array_lib.py` & `pyspedas-1.4.9/pyspedas/cotrans/matrix_array_lib.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/minvar.py` & `pyspedas-1.4.9/pyspedas/cotrans/minvar.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/minvar_matrix_make.py` & `pyspedas-1.4.9/pyspedas/cotrans/minvar_matrix_make.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/quaternions.py` & `pyspedas-1.4.9/pyspedas/cotrans/quaternions.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/tests/cotrans.py` & `pyspedas-1.4.9/pyspedas/cotrans/tests/cotrans.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/tests/quaternions.py` & `pyspedas-1.4.9/pyspedas/cotrans/tests/quaternions.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/tvector_rotate.py` & `pyspedas-1.4.9/pyspedas/cotrans/tvector_rotate.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/cotrans/xyz_to_polar.py` & `pyspedas-1.4.9/pyspedas/cotrans/xyz_to_polar.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/csswe/__init__.py` & `pyspedas-1.4.9/pyspedas/csswe/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/csswe/load.py` & `pyspedas-1.4.9/pyspedas/csswe/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/csswe/tests/tests.py` & `pyspedas-1.4.9/pyspedas/csswe/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/de2/__init__.py` & `pyspedas-1.4.9/pyspedas/de2/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/de2/load.py` & `pyspedas-1.4.9/pyspedas/de2/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/de2/tests/tests.py` & `pyspedas-1.4.9/pyspedas/de2/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/dscovr/__init__.py` & `pyspedas-1.4.9/pyspedas/dscovr/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/dscovr/load.py` & `pyspedas-1.4.9/pyspedas/dscovr/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/dscovr/tests/tests.py` & `pyspedas-1.4.9/pyspedas/dscovr/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/equator_s/__init__.py` & `pyspedas-1.4.9/pyspedas/equator_s/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/equator_s/load.py` & `pyspedas-1.4.9/pyspedas/equator_s/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/equator_s/tests/tests.py` & `pyspedas-1.4.9/pyspedas/equator_s/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/__init__.py` & `pyspedas-1.4.9/pyspedas/erg/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/config.py` & `pyspedas-1.4.9/pyspedas/erg/config.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/ground/camera/camera_omti_asi.py` & `pyspedas-1.4.9/pyspedas/erg/ground/camera/camera_omti_asi.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/ground/geomag/gmag_isee_fluxgate.py` & `pyspedas-1.4.9/pyspedas/erg/ground/geomag/gmag_isee_fluxgate.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/ground/geomag/gmag_isee_induction.py` & `pyspedas-1.4.9/pyspedas/erg/ground/geomag/gmag_isee_induction.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/ground/geomag/gmag_magdas_1sec.py` & `pyspedas-1.4.9/pyspedas/erg/ground/geomag/gmag_magdas_1sec.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/ground/geomag/gmag_mm210.py` & `pyspedas-1.4.9/pyspedas/erg/ground/geomag/gmag_mm210.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/ground/geomag/gmag_stel_fluxgate.py` & `pyspedas-1.4.9/pyspedas/erg/ground/geomag/gmag_stel_fluxgate.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/ground/geomag/gmag_stel_induction.py` & `pyspedas-1.4.9/pyspedas/erg/ground/geomag/gmag_stel_induction.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/ground/radar/superdarn/get_sphcntr.py` & `pyspedas-1.4.9/pyspedas/erg/ground/radar/superdarn/get_sphcntr.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/ground/radar/superdarn/sd_fit.py` & `pyspedas-1.4.9/pyspedas/erg/ground/radar/superdarn/sd_fit.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/ground/riometer/isee_brio.py` & `pyspedas-1.4.9/pyspedas/erg/ground/riometer/isee_brio.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/ground/vlf/isee_vlf.py` & `pyspedas-1.4.9/pyspedas/erg/ground/vlf/isee_vlf.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/att/att.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/att/att.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/cart_trans_matrix_make.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/cart_trans_matrix_make.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/dsi2j2000.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/dsi2j2000.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/erg_cotrans.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/erg_cotrans.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/erg_interpolate_att.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/erg_interpolate_att.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/sga2sgi.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/sga2sgi.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/sgi2dsi.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/sgi2dsi.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/common/cotrans/vector_rotate.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/common/cotrans/vector_rotate.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/config.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/config.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/hep/hep.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/hep/hep.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/lepe/lepe.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/lepe/lepe.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/lepi/lepi.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/lepi/lepi.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/load.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/mepe/mepe.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/mepe/mepe.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/mepi/mepi_nml.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/mepi/mepi_nml.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/mepi/mepi_tof.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/mepi/mepi_tof.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/mgf/mgf.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/mgf/mgf.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/orb/orb.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/orb/orb.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/orb/remove_duplicated_tframe.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/orb/remove_duplicated_tframe.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_convert_flux_units.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_convert_flux_units.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_hep_get_dist.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_hep_get_dist.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_hep_part_products.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_hep_part_products.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_lep_part_products.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_lep_part_products.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_lepe_get_dist.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_lepe_get_dist.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_lepi_get_dist.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_lepi_get_dist.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_mep_part_products.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_mep_part_products.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_mepe_get_dist.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_mepe_get_dist.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_mepi_get_dist.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_mepi_get_dist.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_clean_data.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_clean_data.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_do_fac.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_do_fac.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_limit_range.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_limit_range.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_make_e_spec.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_make_e_spec.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_make_fac.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_make_fac.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_make_phi_spec.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_make_phi_spec.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_make_theta_spec.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_make_theta_spec.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_make_tplot.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_make_tplot.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_moments_tplot.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_moments_tplot.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_pgs_progress_update.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_pgs_progress_update.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_units_string.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_units_string.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_xep_get_dist.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_xep_get_dist.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/erg_xep_part_products.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/erg_xep_part_products.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/get_lepi_flux_angle_in_sga.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/get_lepi_flux_angle_in_sga.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/get_mepe_az_dir_in_sga.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/get_mepe_az_dir_in_sga.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/get_mepe_flux_angle_in_sga.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/get_mepe_flux_angle_in_sga.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/particle/get_mepi_flux_angle_in_sga.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/particle/get_mepi_flux_angle_in_sga.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/pwe/pwe_efd.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/pwe/pwe_efd.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/pwe/pwe_hfa.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/pwe/pwe_hfa.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/pwe/pwe_ofa.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/pwe/pwe_ofa.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/pwe/pwe_wfc.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/pwe/pwe_wfc.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/satellite/erg/xep/xep.py` & `pyspedas-1.4.9/pyspedas/erg/satellite/erg/xep/xep.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/erg/tests/tests.py` & `pyspedas-1.4.9/pyspedas/erg/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/fast/__init__.py` & `pyspedas-1.4.9/pyspedas/fast/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/fast/load.py` & `pyspedas-1.4.9/pyspedas/fast/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/fast/tests/tests.py` & `pyspedas-1.4.9/pyspedas/fast/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/geopack/get_tsy_params.py` & `pyspedas-1.4.9/pyspedas/geopack/get_tsy_params.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/geopack/get_w_params.py` & `pyspedas-1.4.9/pyspedas/geopack/get_w_params.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/geopack/t01.py` & `pyspedas-1.4.9/pyspedas/geopack/t01.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/geopack/t89.py` & `pyspedas-1.4.9/pyspedas/geopack/t89.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/geopack/t96.py` & `pyspedas-1.4.9/pyspedas/geopack/t96.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/geopack/tests/tests.py` & `pyspedas-1.4.9/pyspedas/geopack/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/geopack/ts04.py` & `pyspedas-1.4.9/pyspedas/geopack/ts04.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/geotail/__init__.py` & `pyspedas-1.4.9/pyspedas/geotail/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/geotail/load.py` & `pyspedas-1.4.9/pyspedas/geotail/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/geotail/tests/tests.py` & `pyspedas-1.4.9/pyspedas/geotail/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/goes/__init__.py` & `pyspedas-1.4.9/pyspedas/goes/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/goes/load.py` & `pyspedas-1.4.9/pyspedas/goes/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/goes/load_orbit.py` & `pyspedas-1.4.9/pyspedas/goes/load_orbit.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/goes/tests/tests.py` & `pyspedas-1.4.9/pyspedas/goes/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/hapi/hapi.py` & `pyspedas-1.4.9/pyspedas/hapi/hapi.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/hapi/tests/tests.py` & `pyspedas-1.4.9/pyspedas/hapi/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/image/__init__.py` & `pyspedas-1.4.9/pyspedas/image/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/image/load.py` & `pyspedas-1.4.9/pyspedas/image/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/image/tests/tests.py` & `pyspedas-1.4.9/pyspedas/image/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/kyoto/load_dst.py` & `pyspedas-1.4.9/pyspedas/kyoto/load_dst.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/kyoto/tests/tests.py` & `pyspedas-1.4.9/pyspedas/kyoto/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/lanl/__init__.py` & `pyspedas-1.4.9/pyspedas/lanl/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/lanl/load.py` & `pyspedas-1.4.9/pyspedas/lanl/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/lanl/tests/tests.py` & `pyspedas-1.4.9/pyspedas/lanl/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/maven/__init__.py` & `pyspedas-1.4.9/pyspedas/maven/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/maven/download_files_utilities.py` & `pyspedas-1.4.9/pyspedas/maven/download_files_utilities.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/maven/file_regex.py` & `pyspedas-1.4.9/pyspedas/maven/file_regex.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/maven/maven_kp_to_tplot.py` & `pyspedas-1.4.9/pyspedas/maven/maven_kp_to_tplot.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/maven/maven_load.py` & `pyspedas-1.4.9/pyspedas/maven/maven_load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/maven/orbit_time.py` & `pyspedas-1.4.9/pyspedas/maven/orbit_time.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/maven/tests/tests.py` & `pyspedas-1.4.9/pyspedas/maven/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/maven/utilities.py` & `pyspedas-1.4.9/pyspedas/maven/utilities.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mica/__init__.py` & `pyspedas-1.4.9/pyspedas/mica/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mica/load.py` & `pyspedas-1.4.9/pyspedas/mica/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mica/tests/tests.py` & `pyspedas-1.4.9/pyspedas/mica/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/__init__.py` & `pyspedas-1.4.9/pyspedas/mms/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/aspoc/aspoc.py` & `pyspedas-1.4.9/pyspedas/mms/aspoc/aspoc.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/cotrans/mms_cotrans_lmn.py` & `pyspedas-1.4.9/pyspedas/mms/cotrans/mms_cotrans_lmn.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/cotrans/mms_cotrans_qrotate.py` & `pyspedas-1.4.9/pyspedas/mms/cotrans/mms_cotrans_qrotate.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/cotrans/mms_cotrans_qtransformer.py` & `pyspedas-1.4.9/pyspedas/mms/cotrans/mms_cotrans_qtransformer.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/cotrans/mms_qcotrans.py` & `pyspedas-1.4.9/pyspedas/mms/cotrans/mms_qcotrans.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/dsp/dsp.py` & `pyspedas-1.4.9/pyspedas/mms/dsp/dsp.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/dsp/mms_dsp_set_metadata.py` & `pyspedas-1.4.9/pyspedas/mms/dsp/mms_dsp_set_metadata.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/edi/edi.py` & `pyspedas-1.4.9/pyspedas/mms/edi/edi.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/edi/mms_edi_set_metadata.py` & `pyspedas-1.4.9/pyspedas/mms/edi/mms_edi_set_metadata.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/edp/edp.py` & `pyspedas-1.4.9/pyspedas/mms/edp/edp.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/edp/mms_edp_set_metadata.py` & `pyspedas-1.4.9/pyspedas/mms/edp/mms_edp_set_metadata.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/eis/eis.py` & `pyspedas-1.4.9/pyspedas/mms/eis/eis.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/eis/mms_eis_omni.py` & `pyspedas-1.4.9/pyspedas/mms/eis/mms_eis_omni.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/eis/mms_eis_pad.py` & `pyspedas-1.4.9/pyspedas/mms/eis/mms_eis_pad.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/eis/mms_eis_pad_spinavg.py` & `pyspedas-1.4.9/pyspedas/mms/eis/mms_eis_pad_spinavg.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/eis/mms_eis_set_metadata.py` & `pyspedas-1.4.9/pyspedas/mms/eis/mms_eis_set_metadata.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/eis/mms_eis_spec_combine_sc.py` & `pyspedas-1.4.9/pyspedas/mms/eis/mms_eis_spec_combine_sc.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/eis/mms_eis_spin_avg.py` & `pyspedas-1.4.9/pyspedas/mms/eis/mms_eis_spin_avg.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/feeps.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/feeps.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_active_eyes.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_active_eyes.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_correct_energies.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_correct_energies.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_energy_table.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_energy_table.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_flat_field_corrections.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_flat_field_corrections.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_getgyrophase.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_getgyrophase.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_gpd.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_gpd.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_omni.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_omni.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_pad.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_pad.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_pad_spinavg.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_pad_spinavg.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_pitch_angles.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_pitch_angles.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_remove_bad_data.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_remove_bad_data.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_remove_sun.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_remove_sun.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_spin_avg.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_spin_avg.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/mms_feeps_split_integral_ch.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/mms_feeps_split_integral_ch.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/feeps/mms_read_feeps_sector_masks_csv.py` & `pyspedas-1.4.9/pyspedas/mms/feeps/mms_read_feeps_sector_masks_csv.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fgm/fgm.py` & `pyspedas-1.4.9/pyspedas/mms/fgm/fgm.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fgm/mms_curl.py` & `pyspedas-1.4.9/pyspedas/mms/fgm/mms_curl.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fgm/mms_fgm_remove_flags.py` & `pyspedas-1.4.9/pyspedas/mms/fgm/mms_fgm_remove_flags.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fgm/mms_fgm_set_metadata.py` & `pyspedas-1.4.9/pyspedas/mms/fgm/mms_fgm_set_metadata.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fgm/mms_lingradest.py` & `pyspedas-1.4.9/pyspedas/mms/fgm/mms_lingradest.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fgm/mms_split_fgm_data.py` & `pyspedas-1.4.9/pyspedas/mms/fgm/mms_split_fgm_data.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fpi/fpi.py` & `pyspedas-1.4.9/pyspedas/mms/fpi/fpi.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fpi/mms_fpi_ang_ang.py` & `pyspedas-1.4.9/pyspedas/mms/fpi/mms_fpi_ang_ang.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fpi/mms_fpi_make_compressionlossbars.py` & `pyspedas-1.4.9/pyspedas/mms/fpi/mms_fpi_make_compressionlossbars.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fpi/mms_fpi_make_errorflagbars.py` & `pyspedas-1.4.9/pyspedas/mms/fpi/mms_fpi_make_errorflagbars.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fpi/mms_fpi_set_metadata.py` & `pyspedas-1.4.9/pyspedas/mms/fpi/mms_fpi_set_metadata.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fpi/mms_fpi_split_tensor.py` & `pyspedas-1.4.9/pyspedas/mms/fpi/mms_fpi_split_tensor.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fpi/mms_get_fpi_dist.py` & `pyspedas-1.4.9/pyspedas/mms/fpi/mms_get_fpi_dist.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fpi/mms_load_fpi_calc_pad.py` & `pyspedas-1.4.9/pyspedas/mms/fpi/mms_load_fpi_calc_pad.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fpi/mms_pad_fpi.py` & `pyspedas-1.4.9/pyspedas/mms/fpi/mms_pad_fpi.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/fsm/fsm.py` & `pyspedas-1.4.9/pyspedas/mms/fsm/fsm.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/hpca/hpca.py` & `pyspedas-1.4.9/pyspedas/mms/hpca/hpca.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/hpca/mms_get_hpca_dist.py` & `pyspedas-1.4.9/pyspedas/mms/hpca/mms_get_hpca_dist.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/hpca/mms_get_hpca_info.py` & `pyspedas-1.4.9/pyspedas/mms/hpca/mms_get_hpca_info.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/hpca/mms_hpca_calc_anodes.py` & `pyspedas-1.4.9/pyspedas/mms/hpca/mms_hpca_calc_anodes.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/hpca/mms_hpca_energies.py` & `pyspedas-1.4.9/pyspedas/mms/hpca/mms_hpca_energies.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/hpca/mms_hpca_set_metadata.py` & `pyspedas-1.4.9/pyspedas/mms/hpca/mms_hpca_set_metadata.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/hpca/mms_hpca_spin_sum.py` & `pyspedas-1.4.9/pyspedas/mms/hpca/mms_hpca_spin_sum.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mec/earth_polar1.png` & `pyspedas-1.4.9/pyspedas/mms/mec/earth_polar1.png`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mec/mec.py` & `pyspedas-1.4.9/pyspedas/mms/mec/mec.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mec/mms_mec_set_metadata.py` & `pyspedas-1.4.9/pyspedas/mms/mec/mms_mec_set_metadata.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mec_ascii/mms_get_local_state_files.py` & `pyspedas-1.4.9/pyspedas/mms/mec_ascii/mms_get_local_state_files.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mec_ascii/mms_get_state_data.py` & `pyspedas-1.4.9/pyspedas/mms/mec_ascii/mms_get_state_data.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mec_ascii/mms_load_att_tplot.py` & `pyspedas-1.4.9/pyspedas/mms/mec_ascii/mms_load_att_tplot.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mec_ascii/mms_load_eph_tplot.py` & `pyspedas-1.4.9/pyspedas/mms/mec_ascii/mms_load_eph_tplot.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mec_ascii/state.py` & `pyspedas-1.4.9/pyspedas/mms/mec_ascii/state.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mms_config.py` & `pyspedas-1.4.9/pyspedas/mms/mms_config.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mms_file_filter.py` & `pyspedas-1.4.9/pyspedas/mms/mms_file_filter.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mms_files_in_interval.py` & `pyspedas-1.4.9/pyspedas/mms/mms_files_in_interval.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mms_get_local_files.py` & `pyspedas-1.4.9/pyspedas/mms/mms_get_local_files.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mms_load_brst_segments.py` & `pyspedas-1.4.9/pyspedas/mms/mms_load_brst_segments.py`

 * *Files 2% similar despite different names*

```diff
@@ -54,15 +54,15 @@
     times_in_range = (unix_start >= tr[0]-300.0) & (unix_start <= tr[1]+300.0)
 
     unix_start = unix_start[times_in_range]
     unix_end = unix_end[times_in_range]
 
     # +10 second offset added; there appears to be an extra 10
     # seconds of data, consistently, not included in the range here
-    unix_end = [end_time+10.0 for end_time in unix_end]
+    unix_end = np.array([end_time+10.0 for end_time in unix_end])
 
     bar_x = []
     bar_y = []
 
     for start_time, end_time in zip(unix_start, unix_end):
         if end_time >= tr[0] and start_time <= tr[1]:
             bar_x.extend([start_time, start_time, end_time, end_time])
```

### Comparing `pyspedas-1.4.8/pyspedas/mms/mms_load_data.py` & `pyspedas-1.4.9/pyspedas/mms/mms_load_data.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mms_load_data_spdf.py` & `pyspedas-1.4.9/pyspedas/mms/mms_load_data_spdf.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mms_load_fast_segments.py` & `pyspedas-1.4.9/pyspedas/mms/mms_load_fast_segments.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mms_load_sroi_segments.py` & `pyspedas-1.4.9/pyspedas/mms/mms_load_sroi_segments.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mms_login_lasp.py` & `pyspedas-1.4.9/pyspedas/mms/mms_login_lasp.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/mms_orbit_plot.py` & `pyspedas-1.4.9/pyspedas/mms/mms_orbit_plot.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/particles/mms_convert_flux_units.py` & `pyspedas-1.4.9/pyspedas/mms/particles/mms_convert_flux_units.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/particles/mms_part_des_photoelectrons.py` & `pyspedas-1.4.9/pyspedas/mms/particles/mms_part_des_photoelectrons.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/particles/mms_part_getspec.py` & `pyspedas-1.4.9/pyspedas/mms/particles/mms_part_getspec.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/particles/mms_part_products.py` & `pyspedas-1.4.9/pyspedas/mms/particles/mms_part_products.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/particles/mms_part_slice2d.py` & `pyspedas-1.4.9/pyspedas/mms/particles/mms_part_slice2d.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/particles/mms_pgs_clean_data.py` & `pyspedas-1.4.9/pyspedas/mms/particles/mms_pgs_clean_data.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/particles/mms_pgs_clean_support.py` & `pyspedas-1.4.9/pyspedas/mms/particles/mms_pgs_clean_support.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/particles/mms_pgs_make_e_spec.py` & `pyspedas-1.4.9/pyspedas/mms/particles/mms_pgs_make_e_spec.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/particles/mms_pgs_make_fac.py` & `pyspedas-1.4.9/pyspedas/mms/particles/mms_pgs_make_fac.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/particles/mms_pgs_make_phi_spec.py` & `pyspedas-1.4.9/pyspedas/mms/particles/mms_pgs_make_phi_spec.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/particles/mms_pgs_make_theta_spec.py` & `pyspedas-1.4.9/pyspedas/mms/particles/mms_pgs_make_theta_spec.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/particles/mms_pgs_split_hpca.py` & `pyspedas-1.4.9/pyspedas/mms/particles/mms_pgs_split_hpca.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/particles/moka_mms_clean_data.py` & `pyspedas-1.4.9/pyspedas/mms/particles/moka_mms_clean_data.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/print_vars.py` & `pyspedas-1.4.9/pyspedas/mms/print_vars.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/scm/mms_scm_set_metadata.py` & `pyspedas-1.4.9/pyspedas/mms/scm/mms_scm_set_metadata.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/scm/scm.py` & `pyspedas-1.4.9/pyspedas/mms/scm/scm.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/spd_mms_load_bss.py` & `pyspedas-1.4.9/pyspedas/mms/spd_mms_load_bss.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/tests/cotrans.py` & `pyspedas-1.4.9/pyspedas/mms/tests/cotrans.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/tests/curlometer.py` & `pyspedas-1.4.9/pyspedas/mms/tests/curlometer.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/tests/data_rate_segments.py` & `pyspedas-1.4.9/pyspedas/mms/tests/data_rate_segments.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/tests/eis.py` & `pyspedas-1.4.9/pyspedas/mms/tests/eis.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/tests/feeps.py` & `pyspedas-1.4.9/pyspedas/mms/tests/feeps.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/tests/file_filter.py` & `pyspedas-1.4.9/pyspedas/mms/tests/file_filter.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/tests/fpi_tests.py` & `pyspedas-1.4.9/pyspedas/mms/tests/fpi_tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/tests/load_routine_tests.py` & `pyspedas-1.4.9/pyspedas/mms/tests/load_routine_tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/tests/mms_part_getspec.py` & `pyspedas-1.4.9/pyspedas/mms/tests/mms_part_getspec.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/tests/neutral_sheet.py` & `pyspedas-1.4.9/pyspedas/mms/tests/neutral_sheet.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/tests/ql_l1b_sitl_tests.py` & `pyspedas-1.4.9/pyspedas/mms/tests/ql_l1b_sitl_tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/tests/slice2d.py` & `pyspedas-1.4.9/pyspedas/mms/tests/slice2d.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/mms/tests/wavpol.py` & `pyspedas-1.4.9/pyspedas/mms/tests/wavpol.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/omni/__init__.py` & `pyspedas-1.4.9/pyspedas/omni/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/omni/load.py` & `pyspedas-1.4.9/pyspedas/omni/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/omni/tests/tests.py` & `pyspedas-1.4.9/pyspedas/omni/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/moments/moments_3d.py` & `pyspedas-1.4.9/pyspedas/particles/moments/moments_3d.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/moments/moments_3d_omega_weights.py` & `pyspedas-1.4.9/pyspedas/particles/moments/moments_3d_omega_weights.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/moments/spd_pgs_moments_tplot.py` & `pyspedas-1.4.9/pyspedas/particles/moments/spd_pgs_moments_tplot.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_do_fac.py` & `pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_do_fac.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_limit_range.py` & `pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_limit_range.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_make_e_spec.py` & `pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_make_e_spec.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_make_phi_spec.py` & `pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_make_phi_spec.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_make_theta_spec.py` & `pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_make_theta_spec.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_make_tplot.py` & `pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_make_tplot.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_progress_update.py` & `pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_progress_update.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_part_products/spd_pgs_regrid.py` & `pyspedas-1.4.9/pyspedas/particles/spd_part_products/spd_pgs_regrid.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/quaternions.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/quaternions.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice1d_plot.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice1d_plot.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_2di.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_2di.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_checkbins.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_checkbins.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_collate.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_collate.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_custom_rotation.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_custom_rotation.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_geo.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_geo.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_get_data.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_get_data.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_get_ebounds.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_get_ebounds.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_get_sphere.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_get_sphere.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_get_support.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_get_support.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_getinfo.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_getinfo.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_intrange.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_intrange.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_nearest.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_nearest.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_orientslice.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_orientslice.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_plot.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_plot.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_rlog.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_rlog.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_rotate.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_rotate.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_s2c.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_s2c.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_smooth.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_smooth.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/slice2d_subtract.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/slice2d_subtract.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/spd_cal_rot.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/spd_cal_rot.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_slice2d/tplot_average.py` & `pyspedas-1.4.9/pyspedas/particles/spd_slice2d/tplot_average.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/particles/spd_units_string.py` & `pyspedas-1.4.9/pyspedas/particles/spd_units_string.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/poes/__init__.py` & `pyspedas-1.4.9/pyspedas/poes/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/poes/load.py` & `pyspedas-1.4.9/pyspedas/poes/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/poes/tests/tests.py` & `pyspedas-1.4.9/pyspedas/poes/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/polar/__init__.py` & `pyspedas-1.4.9/pyspedas/polar/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/polar/load.py` & `pyspedas-1.4.9/pyspedas/polar/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/polar/tests/tests.py` & `pyspedas-1.4.9/pyspedas/polar/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/psp/__init__.py` & `pyspedas-1.4.9/pyspedas/psp/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/psp/config.py` & `pyspedas-1.4.9/pyspedas/psp/config.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/psp/filter.py` & `pyspedas-1.4.9/pyspedas/psp/filter.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/psp/load.py` & `pyspedas-1.4.9/pyspedas/psp/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/psp/rfs.py` & `pyspedas-1.4.9/pyspedas/psp/rfs.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/psp/tests/tests.py` & `pyspedas-1.4.9/pyspedas/psp/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/rbsp/__init__.py` & `pyspedas-1.4.9/pyspedas/rbsp/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/rbsp/load.py` & `pyspedas-1.4.9/pyspedas/rbsp/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/rbsp/rbspice_lib/rbsp_load_rbspice_read.py` & `pyspedas-1.4.9/pyspedas/rbsp/rbspice_lib/rbsp_load_rbspice_read.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_omni.py` & `pyspedas-1.4.9/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_omni.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_pad.py` & `pyspedas-1.4.9/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_pad.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_pad_spinavg.py` & `pyspedas-1.4.9/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_pad_spinavg.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_spin_avg.py` & `pyspedas-1.4.9/pyspedas/rbsp/rbspice_lib/rbsp_rbspice_spin_avg.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/rbsp/tests/tests.py` & `pyspedas-1.4.9/pyspedas/rbsp/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/secs/__init__.py` & `pyspedas-1.4.9/pyspedas/secs/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/secs/config.py` & `pyspedas-1.4.9/pyspedas/secs/config.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/secs/load.py` & `pyspedas-1.4.9/pyspedas/secs/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/secs/makeplots.py` & `pyspedas-1.4.9/pyspedas/secs/makeplots.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/solo/__init__.py` & `pyspedas-1.4.9/pyspedas/solo/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/solo/load.py` & `pyspedas-1.4.9/pyspedas/solo/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/solo/tests/tests.py` & `pyspedas-1.4.9/pyspedas/solo/tests/tests.py`

 * *Files 2% similar despite different names*

```diff
@@ -32,15 +32,15 @@
         self.assertTrue(data_exists('FLUX_DENSITY1'))
         self.assertTrue(data_exists('FLUX_DENSITY2'))
 
     def test_load_swa_data(self):
         swa_vars = pyspedas.solo.swa()
         self.assertTrue(data_exists('eflux'))
         swa_vars = pyspedas.solo.swa(level='l2', datatype='eas1-nm3d-def')
-        self.assertTrue(data_exists('SWA_EAS1_Data'))
+        self.assertTrue(data_exists('SWA_EAS1_NM3D_DEF_Data'))
         swa_vars = pyspedas.solo.swa(notplot=True)
         self.assertTrue('eflux' in swa_vars)
 
     def test_load_swa_l1_data(self):
         swa_vars = pyspedas.solo.swa(level='l1', datatype='eas-padc')
         self.assertTrue(data_exists('SWA_EAS_BM_Data'))
         self.assertTrue(data_exists('SWA_EAS_MagDataUsed'))
```

### Comparing `pyspedas-1.4.8/pyspedas/sosmag/load.py` & `pyspedas-1.4.9/pyspedas/sosmag/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/sosmag/tests/tests.py` & `pyspedas-1.4.9/pyspedas/sosmag/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/st5/__init__.py` & `pyspedas-1.4.9/pyspedas/st5/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/st5/load.py` & `pyspedas-1.4.9/pyspedas/st5/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/st5/tests/tests.py` & `pyspedas-1.4.9/pyspedas/st5/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/stereo/__init__.py` & `pyspedas-1.4.9/pyspedas/stereo/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/stereo/load.py` & `pyspedas-1.4.9/pyspedas/stereo/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/stereo/tests/tests.py` & `pyspedas-1.4.9/pyspedas/stereo/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/swarm/__init__.py` & `pyspedas-1.4.9/pyspedas/swarm/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/swarm/load.py` & `pyspedas-1.4.9/pyspedas/swarm/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/__init__.py` & `pyspedas-1.4.9/pyspedas/themis/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/common/check_args.py` & `pyspedas-1.4.9/pyspedas/themis/common/check_args.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/cotrans/dsl2gse.py` & `pyspedas-1.4.9/pyspedas/themis/cotrans/dsl2gse.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/ground/ask.py` & `pyspedas-1.4.9/pyspedas/themis/ground/ask.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/ground/gmag.py` & `pyspedas-1.4.9/pyspedas/themis/ground/gmag.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/load.py` & `pyspedas-1.4.9/pyspedas/themis/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/spacecraft/fields/efi.py` & `pyspedas-1.4.9/pyspedas/themis/spacecraft/fields/efi.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/spacecraft/fields/fbk.py` & `pyspedas-1.4.9/pyspedas/themis/spacecraft/fields/fbk.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/spacecraft/fields/fft.py` & `pyspedas-1.4.9/pyspedas/themis/spacecraft/fields/fft.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/spacecraft/fields/fgm.py` & `pyspedas-1.4.9/pyspedas/themis/spacecraft/fields/fgm.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/spacecraft/fields/fit.py` & `pyspedas-1.4.9/pyspedas/themis/spacecraft/fields/fit.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/spacecraft/fields/scm.py` & `pyspedas-1.4.9/pyspedas/themis/spacecraft/fields/scm.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/spacecraft/particles/esa.py` & `pyspedas-1.4.9/pyspedas/themis/spacecraft/particles/esa.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/spacecraft/particles/gmom.py` & `pyspedas-1.4.9/pyspedas/themis/spacecraft/particles/gmom.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/spacecraft/particles/mom.py` & `pyspedas-1.4.9/pyspedas/themis/spacecraft/particles/mom.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/spacecraft/particles/sst.py` & `pyspedas-1.4.9/pyspedas/themis/spacecraft/particles/sst.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/state/slp.py` & `pyspedas-1.4.9/pyspedas/themis/state/slp.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/state/state.py` & `pyspedas-1.4.9/pyspedas/themis/state/state.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/tests/test_cal_fit_tplot_metadata.py` & `pyspedas-1.4.9/pyspedas/themis/tests/test_cal_fit_tplot_metadata.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/tests/tests.py` & `pyspedas-1.4.9/pyspedas/themis/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/tests/tests_cal_fit.py` & `pyspedas-1.4.9/pyspedas/themis/tests/tests_cal_fit.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/tests/tests_themis_check_args.py` & `pyspedas-1.4.9/pyspedas/themis/tests/tests_themis_check_args.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/tests/validation/cal_fit_validation.py` & `pyspedas-1.4.9/pyspedas/themis/tests/validation/cal_fit_validation.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/themis/tests/validation/dsl2gse.py` & `pyspedas-1.4.9/pyspedas/themis/tests/validation/dsl2gse.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/twins/__init__.py` & `pyspedas-1.4.9/pyspedas/twins/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/twins/load.py` & `pyspedas-1.4.9/pyspedas/twins/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/twins/tests/tests.py` & `pyspedas-1.4.9/pyspedas/twins/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/ulysses/__init__.py` & `pyspedas-1.4.9/pyspedas/ulysses/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/ulysses/load.py` & `pyspedas-1.4.9/pyspedas/ulysses/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/ulysses/tests/tests.py` & `pyspedas-1.4.9/pyspedas/ulysses/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/utilities/dailynames.py` & `pyspedas-1.4.9/pyspedas/utilities/dailynames.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/utilities/download.py` & `pyspedas-1.4.9/pyspedas/utilities/download.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/utilities/interpol.py` & `pyspedas-1.4.9/pyspedas/utilities/interpol.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/utilities/spice/time_ephemeris.py` & `pyspedas-1.4.9/pyspedas/utilities/spice/time_ephemeris.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/utilities/tcopy.py` & `pyspedas-1.4.9/pyspedas/utilities/tcopy.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/utilities/tests/download_tests.py` & `pyspedas-1.4.9/pyspedas/utilities/tests/download_tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/utilities/tests/misc_tests.py` & `pyspedas-1.4.9/pyspedas/utilities/tests/misc_tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/utilities/tests/time_tests.py` & `pyspedas-1.4.9/pyspedas/utilities/tests/time_tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/utilities/time_double.py` & `pyspedas-1.4.9/pyspedas/utilities/time_double.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/utilities/time_string.py` & `pyspedas-1.4.9/pyspedas/utilities/time_string.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/utilities/tkm2re.py` & `pyspedas-1.4.9/pyspedas/utilities/tkm2re.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/utilities/tnames.py` & `pyspedas-1.4.9/pyspedas/utilities/tnames.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/vires/load.py` & `pyspedas-1.4.9/pyspedas/vires/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/wind/__init__.py` & `pyspedas-1.4.9/pyspedas/wind/__init__.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/wind/load.py` & `pyspedas-1.4.9/pyspedas/wind/load.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas/wind/tests/tests.py` & `pyspedas-1.4.9/pyspedas/wind/tests/tests.py`

 * *Files identical despite different names*

### Comparing `pyspedas-1.4.8/pyspedas.egg-info/PKG-INFO` & `pyspedas-1.4.9/pyspedas.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyspedas
-Version: 1.4.8
+Version: 1.4.9
 Summary: Python Space Physics Environment Data Analysis Software (pySPEDAS)
 Home-page: https://github.com/spedas/pyspedas
 Author: Nick Hatzigeorgiu, Eric Grimes
 Author-email: nikos@berkeley.edu, egrimes@igpp.ucla.edu
 License: MIT
 Project-URL: Information, http://spedas.org/wiki/
 Keywords: spedas data tools
```

### Comparing `pyspedas-1.4.8/pyspedas.egg-info/SOURCES.txt` & `pyspedas-1.4.9/pyspedas.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -240,25 +240,27 @@
 pyspedas/mica/__init__.py
 pyspedas/mica/config.py
 pyspedas/mica/load.py
 pyspedas/mica/tests/__init__.py
 pyspedas/mica/tests/tests.py
 pyspedas/mms/__init__.py
 pyspedas/mms/mms_config.py
+pyspedas/mms/mms_events.py
 pyspedas/mms/mms_file_filter.py
 pyspedas/mms/mms_files_in_interval.py
 pyspedas/mms/mms_get_local_files.py
 pyspedas/mms/mms_load_brst_segments.py
 pyspedas/mms/mms_load_data.py
 pyspedas/mms/mms_load_data_spdf.py
 pyspedas/mms/mms_load_fast_segments.py
 pyspedas/mms/mms_load_sroi_segments.py
 pyspedas/mms/mms_login_lasp.py
 pyspedas/mms/mms_orbit_plot.py
 pyspedas/mms/mms_python_startup.py
+pyspedas/mms/mms_tai2unix.py
 pyspedas/mms/print_vars.py
 pyspedas/mms/spd_mms_load_bss.py
 pyspedas/mms/aspoc/__init__.py
 pyspedas/mms/aspoc/aspoc.py
 pyspedas/mms/cotrans/__init__.py
 pyspedas/mms/cotrans/mms_cotrans_lmn.py
 pyspedas/mms/cotrans/mms_cotrans_qrotate.py
@@ -551,14 +553,15 @@
 pyspedas/ulysses/tests/tests.py
 pyspedas/utilities/__init__.py
 pyspedas/utilities/dailynames.py
 pyspedas/utilities/data_exists.py
 pyspedas/utilities/datasets.py
 pyspedas/utilities/download.py
 pyspedas/utilities/interpol.py
+pyspedas/utilities/leap_seconds.py
 pyspedas/utilities/tcopy.py
 pyspedas/utilities/time_double.py
 pyspedas/utilities/time_string.py
 pyspedas/utilities/tkm2re.py
 pyspedas/utilities/tnames.py
 pyspedas/utilities/spice/__init__.py
 pyspedas/utilities/spice/time_ephemeris.py
```

### Comparing `pyspedas-1.4.8/setup.py` & `pyspedas-1.4.9/setup.py`

 * *Files 11% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 # Always prefer setuptools over distutils
 from setuptools import setup, find_packages
 # To use a consistent encoding
 from codecs import open
 
 setup(
     name='pyspedas',
-    version='1.4.8',
+    version='1.4.9',
     description='Python Space Physics Environment Data Analysis Software (pySPEDAS)',
     long_description=open('README.md').read(),
     long_description_content_type='text/markdown',
     url='https://github.com/spedas/pyspedas',
     author='Nick Hatzigeorgiu, Eric Grimes',
     author_email='nikos@berkeley.edu, egrimes@igpp.ucla.edu',
     license='MIT',
```

