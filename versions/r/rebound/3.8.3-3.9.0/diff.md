# Comparing `tmp/rebound-3.8.3.tar.gz` & `tmp/rebound-3.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/rebound-3.8.3.tar", last modified: Tue May 28 13:17:25 2019, max compression
+gzip compressed data, was "dist/rebound-3.9.0.tar", last modified: Fri Jul 26 15:31:16 2019, max compression
```

## Comparing `rebound-3.8.3.tar` & `rebound-3.9.0.tar`

### file list

```diff
@@ -1,100 +1,103 @@
-drwxr-xr-x   0 rein       (502) staff       (20)        0 2019-05-28 13:17:25.000000 rebound-3.8.3/
--rw-r--r--   0 rein       (502) staff       (20)     5532 2019-05-28 13:17:25.000000 rebound-3.8.3/PKG-INFO
--rw-r--r--   0 rein       (502) staff       (20)    35147 2016-11-17 01:44:28.000000 rebound-3.8.3/LICENSE
--rw-r--r--   0 rein       (502) staff       (20)     1210 2019-02-25 18:09:42.000000 rebound-3.8.3/MANIFEST.in
-drwxr-xr-x   0 rein       (502) staff       (20)        0 2019-05-28 13:17:25.000000 rebound-3.8.3/rebound.egg-info/
--rw-r--r--   0 rein       (502) staff       (20)     5532 2019-05-28 13:17:25.000000 rebound-3.8.3/rebound.egg-info/PKG-INFO
--rw-r--r--   0 rein       (502) staff       (20)        1 2016-12-28 23:18:02.000000 rebound-3.8.3/rebound.egg-info/not-zip-safe
--rw-r--r--   0 rein       (502) staff       (20)     2164 2019-05-28 13:17:25.000000 rebound-3.8.3/rebound.egg-info/SOURCES.txt
--rw-r--r--   0 rein       (502) staff       (20)       19 2019-05-28 13:17:25.000000 rebound-3.8.3/rebound.egg-info/top_level.txt
--rw-r--r--   0 rein       (502) staff       (20)        1 2019-05-28 13:17:25.000000 rebound-3.8.3/rebound.egg-info/dependency_links.txt
--rw-r--r--   0 rein       (502) staff       (20)     3996 2019-05-28 13:15:52.000000 rebound-3.8.3/setup.py
--rw-r--r--   0 rein       (502) staff       (20)       38 2019-05-28 13:17:25.000000 rebound-3.8.3/setup.cfg
--rw-r--r--   0 rein       (502) staff       (20)     4084 2019-05-28 13:15:52.000000 rebound-3.8.3/README.rst
--rw-r--r--   0 rein       (502) staff       (20)        6 2019-05-28 13:15:50.000000 rebound-3.8.3/version.txt
-drwxr-xr-x   0 rein       (502) staff       (20)        0 2019-05-28 13:17:25.000000 rebound-3.8.3/rebound/
--rw-r--r--   0 rein       (502) staff       (20)    80693 2019-05-28 12:56:44.000000 rebound-3.8.3/rebound/simulation.py
--rw-r--r--   0 rein       (502) staff       (20)     9504 2018-08-12 23:42:58.000000 rebound-3.8.3/rebound/horizons.py
--rw-r--r--   0 rein       (502) staff       (20)    25951 2018-08-12 23:42:58.000000 rebound-3.8.3/rebound/widget.py
--rw-r--r--   0 rein       (502) staff       (20)     4362 2019-05-26 13:03:46.000000 rebound-3.8.3/rebound/units.py
--rw-r--r--   0 rein       (502) staff       (20)    96195 2019-05-28 12:56:44.000000 rebound-3.8.3/rebound/rebound.h
--rw-r--r--   0 rein       (502) staff       (20)    14416 2019-02-25 18:09:42.000000 rebound-3.8.3/rebound/plotting.py
--rw-r--r--   0 rein       (502) staff       (20)      700 2016-11-17 01:44:28.000000 rebound-3.8.3/rebound/tools.py
-drwxr-xr-x   0 rein       (502) staff       (20)        0 2019-05-28 13:17:25.000000 rebound-3.8.3/rebound/tests/
--rw-r--r--   0 rein       (502) staff       (20)     1618 2019-02-25 18:09:42.000000 rebound-3.8.3/rebound/tests/test_restart_mercurius.py
--rw-r--r--   0 rein       (502) staff       (20)      892 2016-11-17 01:44:28.000000 rebound-3.8.3/rebound/tests/test_interruble_pool.py
--rw-r--r--   0 rein       (502) staff       (20)     1551 2016-11-17 01:44:28.000000 rebound-3.8.3/rebound/tests/test_plotting.py
--rw-r--r--   0 rein       (502) staff       (20)     3028 2019-05-28 12:56:44.000000 rebound-3.8.3/rebound/tests/test_megno.py
--rw-r--r--   0 rein       (502) staff       (20)    16284 2018-08-12 23:42:58.000000 rebound-3.8.3/rebound/tests/test_orbital_elements.py
--rw-r--r--   0 rein       (502) staff       (20)     7209 2019-02-25 18:09:42.000000 rebound-3.8.3/rebound/tests/test_mercurius.py
--rw-r--r--   0 rein       (502) staff       (20)     4576 2019-02-25 18:09:42.000000 rebound-3.8.3/rebound/tests/test_simulationarchive_matrix.py
--rw-r--r--   0 rein       (502) staff       (20)     2220 2018-08-12 23:42:58.000000 rebound-3.8.3/rebound/tests/test_shearingsheet.py
--rw-r--r--   0 rein       (502) staff       (20)     1236 2016-11-17 01:44:28.000000 rebound-3.8.3/rebound/tests/test_horizons.py
--rw-r--r--   0 rein       (502) staff       (20)     9400 2019-02-25 18:09:42.000000 rebound-3.8.3/rebound/tests/test_copy.py
--rw-r--r--   0 rein       (502) staff       (20)      997 2018-08-12 23:42:58.000000 rebound-3.8.3/rebound/tests/test_boundary.py
--rw-r--r--   0 rein       (502) staff       (20)        1 2016-11-17 01:44:28.000000 rebound-3.8.3/rebound/tests/__init__.py
--rw-r--r--   0 rein       (502) staff       (20)     8074 2018-08-12 23:42:58.000000 rebound-3.8.3/rebound/tests/test_whfast.py
--rw-r--r--   0 rein       (502) staff       (20)     2324 2019-02-25 18:09:42.000000 rebound-3.8.3/rebound/tests/test_post_timestep_modifications.py
--rw-r--r--   0 rein       (502) staff       (20)     4349 2018-08-12 23:42:58.000000 rebound-3.8.3/rebound/tests/test_transformations.py
--rw-r--r--   0 rein       (502) staff       (20)     1883 2019-02-25 18:09:42.000000 rebound-3.8.3/rebound/tests/test_units.py
--rw-r--r--   0 rein       (502) staff       (20)     2573 2016-11-17 01:44:28.000000 rebound-3.8.3/rebound/tests/test_gravity.py
--rw-r--r--   0 rein       (502) staff       (20)     4983 2019-05-28 12:56:44.000000 rebound-3.8.3/rebound/tests/test_collisions.py
--rw-r--r--   0 rein       (502) staff       (20)     5200 2016-11-17 01:44:28.000000 rebound-3.8.3/rebound/tests/test_hash.py
--rw-r--r--   0 rein       (502) staff       (20)     1047 2016-11-17 01:44:28.000000 rebound-3.8.3/rebound/tests/test_serialize.py
--rw-r--r--   0 rein       (502) staff       (20)     3228 2019-02-25 18:09:42.000000 rebound-3.8.3/rebound/tests/test_janus.py
--rw-r--r--   0 rein       (502) staff       (20)      526 2016-11-17 01:44:28.000000 rebound-3.8.3/rebound/tests/test_data.py
--rw-r--r--   0 rein       (502) staff       (20)     3681 2019-02-25 18:09:42.000000 rebound-3.8.3/rebound/tests/test_additional_forces.py
--rw-r--r--   0 rein       (502) staff       (20)    10464 2019-02-25 18:09:42.000000 rebound-3.8.3/rebound/tests/test_simulation.py
--rw-r--r--   0 rein       (502) staff       (20)    11802 2019-02-25 18:09:42.000000 rebound-3.8.3/rebound/tests/test_particle.py
--rw-r--r--   0 rein       (502) staff       (20)    11749 2016-11-17 01:44:28.000000 rebound-3.8.3/rebound/tests/test_variational.py
--rw-r--r--   0 rein       (502) staff       (20)    19257 2019-02-25 18:09:42.000000 rebound-3.8.3/rebound/tests/test_simulationarchive.py
--rw-r--r--   0 rein       (502) staff       (20)     5996 2016-11-17 01:44:28.000000 rebound-3.8.3/rebound/tests/test_integrator.py
--rw-r--r--   0 rein       (502) staff       (20)     3019 2018-08-12 23:42:58.000000 rebound-3.8.3/rebound/__init__.py
--rw-r--r--   0 rein       (502) staff       (20)     3313 2016-11-17 01:44:28.000000 rebound-3.8.3/rebound/interruptible_pool.py
--rw-r--r--   0 rein       (502) staff       (20)    13819 2019-02-25 18:09:42.000000 rebound-3.8.3/rebound/simulationarchive.py
--rw-r--r--   0 rein       (502) staff       (20)     9499 2016-11-17 01:44:28.000000 rebound-3.8.3/rebound/debug.py
--rw-r--r--   0 rein       (502) staff       (20)    29960 2019-02-25 18:09:42.000000 rebound-3.8.3/rebound/particle.py
--rw-r--r--   0 rein       (502) staff       (20)     1567 2016-11-17 01:44:28.000000 rebound-3.8.3/rebound/data.py
-drwxr-xr-x   0 rein       (502) staff       (20)        0 2019-05-28 13:17:25.000000 rebound-3.8.3/src/
--rw-r--r--   0 rein       (502) staff       (20)     1684 2019-02-25 18:09:43.000000 rebound-3.8.3/src/integrator_mercurius.h
--rw-r--r--   0 rein       (502) staff       (20)    27613 2019-03-24 23:38:53.000000 rebound-3.8.3/src/simulationarchive.c
--rw-r--r--   0 rein       (502) staff       (20)    45314 2019-02-25 18:09:43.000000 rebound-3.8.3/src/display.c
--rw-r--r--   0 rein       (502) staff       (20)     1416 2018-12-14 19:57:19.000000 rebound-3.8.3/src/input.h
--rw-r--r--   0 rein       (502) staff       (20)    86090 2016-11-17 01:44:28.000000 rebound-3.8.3/src/derivatives.c
--rw-r--r--   0 rein       (502) staff       (20)     2492 2016-11-17 01:44:28.000000 rebound-3.8.3/src/integrator_leapfrog.c
--rw-r--r--   0 rein       (502) staff       (20)     1508 2017-02-07 01:49:27.000000 rebound-3.8.3/src/integrator_sei.h
--rw-r--r--   0 rein       (502) staff       (20)    37715 2019-02-25 18:09:43.000000 rebound-3.8.3/src/integrator_ias15.c
--rw-r--r--   0 rein       (502) staff       (20)     5691 2019-02-25 18:09:43.000000 rebound-3.8.3/src/integrator.c
--rw-r--r--   0 rein       (502) staff       (20)    42341 2019-05-28 12:56:44.000000 rebound-3.8.3/src/tools.c
--rw-r--r--   0 rein       (502) staff       (20)     1404 2016-11-17 01:44:28.000000 rebound-3.8.3/src/gravity.h
--rw-r--r--   0 rein       (502) staff       (20)    96195 2019-05-28 12:56:44.000000 rebound-3.8.3/src/rebound.h
--rw-r--r--   0 rein       (502) staff       (20)    10961 2019-02-25 18:09:43.000000 rebound-3.8.3/src/particle.c
--rw-r--r--   0 rein       (502) staff       (20)     1769 2019-03-09 18:18:15.000000 rebound-3.8.3/src/integrator_whfast.h
--rw-r--r--   0 rein       (502) staff       (20)     1757 2016-11-17 01:44:28.000000 rebound-3.8.3/src/boundary.h
--rw-r--r--   0 rein       (502) staff       (20)      963 2017-03-21 14:37:46.000000 rebound-3.8.3/src/transformations.h
--rw-r--r--   0 rein       (502) staff       (20)      935 2018-08-12 23:42:58.000000 rebound-3.8.3/src/binarydiff.h
--rw-r--r--   0 rein       (502) staff       (20)     1034 2016-11-17 01:44:28.000000 rebound-3.8.3/src/collision.h
--rw-r--r--   0 rein       (502) staff       (20)     1424 2018-08-12 23:42:58.000000 rebound-3.8.3/src/integrator_janus.h
--rw-r--r--   0 rein       (502) staff       (20)     3935 2016-11-17 01:44:28.000000 rebound-3.8.3/src/tree.h
--rw-r--r--   0 rein       (502) staff       (20)     1822 2018-12-14 19:57:19.000000 rebound-3.8.3/src/output.h
--rw-r--r--   0 rein       (502) staff       (20)     1456 2016-11-17 01:44:28.000000 rebound-3.8.3/src/integrator_leapfrog.h
--rw-r--r--   0 rein       (502) staff       (20)     1015 2016-11-17 01:44:28.000000 rebound-3.8.3/src/derivatives.h
--rw-r--r--   0 rein       (502) staff       (20)    17592 2019-05-28 13:13:56.000000 rebound-3.8.3/src/input.c
--rw-r--r--   0 rein       (502) staff       (20)     1481 2017-01-18 14:44:42.000000 rebound-3.8.3/src/display.h
--rw-r--r--   0 rein       (502) staff       (20)     1402 2019-02-25 18:09:43.000000 rebound-3.8.3/src/simulationarchive.h
--rw-r--r--   0 rein       (502) staff       (20)    19875 2019-02-25 18:09:43.000000 rebound-3.8.3/src/integrator_mercurius.c
--rw-r--r--   0 rein       (502) staff       (20)    27426 2019-05-28 13:15:52.000000 rebound-3.8.3/src/rebound.c
--rw-r--r--   0 rein       (502) staff       (20)     1329 2016-11-17 01:44:28.000000 rebound-3.8.3/src/particle.h
--rw-r--r--   0 rein       (502) staff       (20)    40354 2019-02-25 18:09:43.000000 rebound-3.8.3/src/gravity.c
--rw-r--r--   0 rein       (502) staff       (20)     2896 2019-02-25 18:09:43.000000 rebound-3.8.3/src/tools.h
--rw-r--r--   0 rein       (502) staff       (20)     6707 2019-02-25 18:09:43.000000 rebound-3.8.3/src/boundary.c
--rw-r--r--   0 rein       (502) staff       (20)    38149 2019-05-28 12:56:44.000000 rebound-3.8.3/src/integrator_whfast.c
--rw-r--r--   0 rein       (502) staff       (20)     1446 2019-03-09 18:18:15.000000 rebound-3.8.3/src/integrator_ias15.h
--rw-r--r--   0 rein       (502) staff       (20)     2026 2019-03-09 18:18:15.000000 rebound-3.8.3/src/integrator.h
--rw-r--r--   0 rein       (502) staff       (20)     5290 2018-08-12 23:42:58.000000 rebound-3.8.3/src/integrator_sei.c
--rw-r--r--   0 rein       (502) staff       (20)    22925 2019-05-28 12:56:44.000000 rebound-3.8.3/src/collision.c
--rw-r--r--   0 rein       (502) staff       (20)     8740 2019-02-25 18:09:43.000000 rebound-3.8.3/src/integrator_janus.c
--rw-r--r--   0 rein       (502) staff       (20)    15885 2019-02-25 18:09:43.000000 rebound-3.8.3/src/transformations.c
--rw-r--r--   0 rein       (502) staff       (20)     6075 2018-08-12 23:42:58.000000 rebound-3.8.3/src/binarydiff.c
--rw-r--r--   0 rein       (502) staff       (20)    23990 2019-02-25 18:09:43.000000 rebound-3.8.3/src/output.c
--rw-r--r--   0 rein       (502) staff       (20)    13202 2016-11-17 01:44:28.000000 rebound-3.8.3/src/tree.c
+drwxr-xr-x   0 rein       (502) staff       (20)        0 2019-07-26 15:31:16.000000 rebound-3.9.0/
+-rw-r--r--   0 rein       (502) staff       (20)     5532 2019-07-26 15:31:16.000000 rebound-3.9.0/PKG-INFO
+-rw-r--r--   0 rein       (502) staff       (20)    35147 2016-11-17 01:44:28.000000 rebound-3.9.0/LICENSE
+-rw-r--r--   0 rein       (502) staff       (20)     1270 2019-07-26 15:29:46.000000 rebound-3.9.0/MANIFEST.in
+drwxr-xr-x   0 rein       (502) staff       (20)        0 2019-07-26 15:31:16.000000 rebound-3.9.0/rebound.egg-info/
+-rw-r--r--   0 rein       (502) staff       (20)     5532 2019-07-26 15:31:16.000000 rebound-3.9.0/rebound.egg-info/PKG-INFO
+-rw-r--r--   0 rein       (502) staff       (20)        1 2016-12-28 23:18:02.000000 rebound-3.9.0/rebound.egg-info/not-zip-safe
+-rw-r--r--   0 rein       (502) staff       (20)     2256 2019-07-26 15:31:16.000000 rebound-3.9.0/rebound.egg-info/SOURCES.txt
+-rw-r--r--   0 rein       (502) staff       (20)       19 2019-07-26 15:31:16.000000 rebound-3.9.0/rebound.egg-info/top_level.txt
+-rw-r--r--   0 rein       (502) staff       (20)        1 2019-07-26 15:31:16.000000 rebound-3.9.0/rebound.egg-info/dependency_links.txt
+-rw-r--r--   0 rein       (502) staff       (20)     4053 2019-07-26 15:29:46.000000 rebound-3.9.0/setup.py
+-rw-r--r--   0 rein       (502) staff       (20)       38 2019-07-26 15:31:16.000000 rebound-3.9.0/setup.cfg
+-rw-r--r--   0 rein       (502) staff       (20)     4084 2019-07-26 15:29:46.000000 rebound-3.9.0/README.rst
+-rw-r--r--   0 rein       (502) staff       (20)        6 2019-07-26 15:29:46.000000 rebound-3.9.0/version.txt
+drwxr-xr-x   0 rein       (502) staff       (20)        0 2019-07-26 15:31:16.000000 rebound-3.9.0/rebound/
+-rw-r--r--   0 rein       (502) staff       (20)    84053 2019-07-26 15:29:46.000000 rebound-3.9.0/rebound/simulation.py
+-rw-r--r--   0 rein       (502) staff       (20)     9504 2018-08-12 23:42:58.000000 rebound-3.9.0/rebound/horizons.py
+-rw-r--r--   0 rein       (502) staff       (20)    25951 2018-08-12 23:42:58.000000 rebound-3.9.0/rebound/widget.py
+-rw-r--r--   0 rein       (502) staff       (20)     4416 2019-05-28 13:21:27.000000 rebound-3.9.0/rebound/units.py
+-rw-r--r--   0 rein       (502) staff       (20)   100197 2019-07-26 15:30:09.000000 rebound-3.9.0/rebound/rebound.h
+-rw-r--r--   0 rein       (502) staff       (20)    14416 2019-02-25 18:09:42.000000 rebound-3.9.0/rebound/plotting.py
+-rw-r--r--   0 rein       (502) staff       (20)      700 2016-11-17 01:44:28.000000 rebound-3.9.0/rebound/tools.py
+drwxr-xr-x   0 rein       (502) staff       (20)        0 2019-07-26 15:31:16.000000 rebound-3.9.0/rebound/tests/
+-rw-r--r--   0 rein       (502) staff       (20)     1618 2019-02-25 18:09:42.000000 rebound-3.9.0/rebound/tests/test_restart_mercurius.py
+-rw-r--r--   0 rein       (502) staff       (20)      892 2016-11-17 01:44:28.000000 rebound-3.9.0/rebound/tests/test_interruble_pool.py
+-rw-r--r--   0 rein       (502) staff       (20)     1551 2016-11-17 01:44:28.000000 rebound-3.9.0/rebound/tests/test_plotting.py
+-rw-r--r--   0 rein       (502) staff       (20)     3086 2019-07-07 23:35:42.000000 rebound-3.9.0/rebound/tests/test_megno.py
+-rw-r--r--   0 rein       (502) staff       (20)    16284 2018-08-12 23:42:58.000000 rebound-3.9.0/rebound/tests/test_orbital_elements.py
+-rw-r--r--   0 rein       (502) staff       (20)     7209 2019-02-25 18:09:42.000000 rebound-3.9.0/rebound/tests/test_mercurius.py
+-rw-r--r--   0 rein       (502) staff       (20)     4576 2019-02-25 18:09:42.000000 rebound-3.9.0/rebound/tests/test_simulationarchive_matrix.py
+-rw-r--r--   0 rein       (502) staff       (20)     4715 2019-07-26 15:29:46.000000 rebound-3.9.0/rebound/tests/test_saba.py
+-rw-r--r--   0 rein       (502) staff       (20)     2220 2018-08-12 23:42:58.000000 rebound-3.9.0/rebound/tests/test_shearingsheet.py
+-rw-r--r--   0 rein       (502) staff       (20)     5720 2019-07-26 15:29:46.000000 rebound-3.9.0/rebound/tests/test_whfast_advanced.py
+-rw-r--r--   0 rein       (502) staff       (20)     1236 2016-11-17 01:44:28.000000 rebound-3.9.0/rebound/tests/test_horizons.py
+-rw-r--r--   0 rein       (502) staff       (20)     9400 2019-07-09 20:05:15.000000 rebound-3.9.0/rebound/tests/test_copy.py
+-rw-r--r--   0 rein       (502) staff       (20)      997 2018-08-12 23:42:58.000000 rebound-3.9.0/rebound/tests/test_boundary.py
+-rw-r--r--   0 rein       (502) staff       (20)        1 2016-11-17 01:44:28.000000 rebound-3.9.0/rebound/tests/__init__.py
+-rw-r--r--   0 rein       (502) staff       (20)     8074 2018-08-12 23:42:58.000000 rebound-3.9.0/rebound/tests/test_whfast.py
+-rw-r--r--   0 rein       (502) staff       (20)     2324 2019-02-25 18:09:42.000000 rebound-3.9.0/rebound/tests/test_post_timestep_modifications.py
+-rw-r--r--   0 rein       (502) staff       (20)     4349 2018-08-12 23:42:58.000000 rebound-3.9.0/rebound/tests/test_transformations.py
+-rw-r--r--   0 rein       (502) staff       (20)     1883 2019-02-25 18:09:42.000000 rebound-3.9.0/rebound/tests/test_units.py
+-rw-r--r--   0 rein       (502) staff       (20)     2573 2016-11-17 01:44:28.000000 rebound-3.9.0/rebound/tests/test_gravity.py
+-rw-r--r--   0 rein       (502) staff       (20)     4983 2019-05-28 12:56:44.000000 rebound-3.9.0/rebound/tests/test_collisions.py
+-rw-r--r--   0 rein       (502) staff       (20)     5200 2016-11-17 01:44:28.000000 rebound-3.9.0/rebound/tests/test_hash.py
+-rw-r--r--   0 rein       (502) staff       (20)     1047 2016-11-17 01:44:28.000000 rebound-3.9.0/rebound/tests/test_serialize.py
+-rw-r--r--   0 rein       (502) staff       (20)     3228 2019-02-25 18:09:42.000000 rebound-3.9.0/rebound/tests/test_janus.py
+-rw-r--r--   0 rein       (502) staff       (20)      526 2016-11-17 01:44:28.000000 rebound-3.9.0/rebound/tests/test_data.py
+-rw-r--r--   0 rein       (502) staff       (20)     3681 2019-02-25 18:09:42.000000 rebound-3.9.0/rebound/tests/test_additional_forces.py
+-rw-r--r--   0 rein       (502) staff       (20)    10464 2019-02-25 18:09:42.000000 rebound-3.9.0/rebound/tests/test_simulation.py
+-rw-r--r--   0 rein       (502) staff       (20)    11802 2019-02-25 18:09:42.000000 rebound-3.9.0/rebound/tests/test_particle.py
+-rw-r--r--   0 rein       (502) staff       (20)    11749 2016-11-17 01:44:28.000000 rebound-3.9.0/rebound/tests/test_variational.py
+-rw-r--r--   0 rein       (502) staff       (20)    19257 2019-02-25 18:09:42.000000 rebound-3.9.0/rebound/tests/test_simulationarchive.py
+-rw-r--r--   0 rein       (502) staff       (20)     5996 2016-11-17 01:44:28.000000 rebound-3.9.0/rebound/tests/test_integrator.py
+-rw-r--r--   0 rein       (502) staff       (20)     3019 2018-08-12 23:42:58.000000 rebound-3.9.0/rebound/__init__.py
+-rw-r--r--   0 rein       (502) staff       (20)     3313 2016-11-17 01:44:28.000000 rebound-3.9.0/rebound/interruptible_pool.py
+-rw-r--r--   0 rein       (502) staff       (20)    13819 2019-07-24 15:20:19.000000 rebound-3.9.0/rebound/simulationarchive.py
+-rw-r--r--   0 rein       (502) staff       (20)    29960 2019-02-25 18:09:42.000000 rebound-3.9.0/rebound/particle.py
+-rw-r--r--   0 rein       (502) staff       (20)     1567 2016-11-17 01:44:28.000000 rebound-3.9.0/rebound/data.py
+drwxr-xr-x   0 rein       (502) staff       (20)        0 2019-07-26 15:31:16.000000 rebound-3.9.0/src/
+-rw-r--r--   0 rein       (502) staff       (20)     1684 2019-02-25 18:09:43.000000 rebound-3.9.0/src/integrator_mercurius.h
+-rw-r--r--   0 rein       (502) staff       (20)    27685 2019-07-26 15:29:46.000000 rebound-3.9.0/src/simulationarchive.c
+-rw-r--r--   0 rein       (502) staff       (20)    45314 2019-02-25 18:09:43.000000 rebound-3.9.0/src/display.c
+-rw-r--r--   0 rein       (502) staff       (20)     1416 2018-12-14 19:57:19.000000 rebound-3.9.0/src/input.h
+-rw-r--r--   0 rein       (502) staff       (20)    86090 2016-11-17 01:44:28.000000 rebound-3.9.0/src/derivatives.c
+-rw-r--r--   0 rein       (502) staff       (20)     2492 2016-11-17 01:44:28.000000 rebound-3.9.0/src/integrator_leapfrog.c
+-rw-r--r--   0 rein       (502) staff       (20)     1508 2017-02-07 01:49:27.000000 rebound-3.9.0/src/integrator_sei.h
+-rw-r--r--   0 rein       (502) staff       (20)    37715 2019-07-26 02:29:35.000000 rebound-3.9.0/src/integrator_ias15.c
+-rw-r--r--   0 rein       (502) staff       (20)     5970 2019-07-26 15:29:46.000000 rebound-3.9.0/src/integrator.c
+-rw-r--r--   0 rein       (502) staff       (20)    42341 2019-05-28 12:56:44.000000 rebound-3.9.0/src/tools.c
+-rw-r--r--   0 rein       (502) staff       (20)     1404 2016-11-17 01:44:28.000000 rebound-3.9.0/src/gravity.h
+-rw-r--r--   0 rein       (502) staff       (20)   100197 2019-07-26 15:30:09.000000 rebound-3.9.0/src/rebound.h
+-rw-r--r--   0 rein       (502) staff       (20)    10961 2019-02-25 18:09:43.000000 rebound-3.9.0/src/particle.c
+-rw-r--r--   0 rein       (502) staff       (20)     1634 2019-07-26 15:29:46.000000 rebound-3.9.0/src/integrator_whfast.h
+-rw-r--r--   0 rein       (502) staff       (20)     1757 2016-11-17 01:44:28.000000 rebound-3.9.0/src/boundary.h
+-rw-r--r--   0 rein       (502) staff       (20)      963 2017-03-21 14:37:46.000000 rebound-3.9.0/src/transformations.h
+-rw-r--r--   0 rein       (502) staff       (20)      936 2019-07-26 15:29:46.000000 rebound-3.9.0/src/binarydiff.h
+-rw-r--r--   0 rein       (502) staff       (20)     1534 2019-07-26 15:29:46.000000 rebound-3.9.0/src/integrator_saba.h
+-rw-r--r--   0 rein       (502) staff       (20)     1034 2016-11-17 01:44:28.000000 rebound-3.9.0/src/collision.h
+-rw-r--r--   0 rein       (502) staff       (20)     1424 2018-08-12 23:42:58.000000 rebound-3.9.0/src/integrator_janus.h
+-rw-r--r--   0 rein       (502) staff       (20)     3935 2016-11-17 01:44:28.000000 rebound-3.9.0/src/tree.h
+-rw-r--r--   0 rein       (502) staff       (20)     1822 2018-12-14 19:57:19.000000 rebound-3.9.0/src/output.h
+-rw-r--r--   0 rein       (502) staff       (20)     1456 2016-11-17 01:44:28.000000 rebound-3.9.0/src/integrator_leapfrog.h
+-rw-r--r--   0 rein       (502) staff       (20)     1015 2016-11-17 01:44:28.000000 rebound-3.9.0/src/derivatives.h
+-rw-r--r--   0 rein       (502) staff       (20)    17986 2019-07-26 15:29:46.000000 rebound-3.9.0/src/input.c
+-rw-r--r--   0 rein       (502) staff       (20)     1481 2017-01-18 14:44:42.000000 rebound-3.9.0/src/display.h
+-rw-r--r--   0 rein       (502) staff       (20)     1402 2019-02-25 18:09:43.000000 rebound-3.9.0/src/simulationarchive.h
+-rw-r--r--   0 rein       (502) staff       (20)    19875 2019-02-25 18:09:43.000000 rebound-3.9.0/src/integrator_mercurius.c
+-rw-r--r--   0 rein       (502) staff       (20)    28481 2019-07-26 15:29:46.000000 rebound-3.9.0/src/rebound.c
+-rw-r--r--   0 rein       (502) staff       (20)     1329 2016-11-17 01:44:28.000000 rebound-3.9.0/src/particle.h
+-rw-r--r--   0 rein       (502) staff       (20)    42971 2019-07-26 15:29:46.000000 rebound-3.9.0/src/gravity.c
+-rw-r--r--   0 rein       (502) staff       (20)     2896 2019-02-25 18:09:43.000000 rebound-3.9.0/src/tools.h
+-rw-r--r--   0 rein       (502) staff       (20)     6707 2019-02-25 18:09:43.000000 rebound-3.9.0/src/boundary.c
+-rw-r--r--   0 rein       (502) staff       (20)    53480 2019-07-26 15:29:46.000000 rebound-3.9.0/src/integrator_whfast.c
+-rw-r--r--   0 rein       (502) staff       (20)     1446 2019-03-09 18:18:15.000000 rebound-3.9.0/src/integrator_ias15.h
+-rw-r--r--   0 rein       (502) staff       (20)     2026 2019-03-09 18:18:15.000000 rebound-3.9.0/src/integrator.h
+-rw-r--r--   0 rein       (502) staff       (20)     5290 2018-08-12 23:42:58.000000 rebound-3.9.0/src/integrator_sei.c
+-rw-r--r--   0 rein       (502) staff       (20)    22925 2019-05-28 12:56:44.000000 rebound-3.9.0/src/collision.c
+-rw-r--r--   0 rein       (502) staff       (20)     8740 2019-02-25 18:09:43.000000 rebound-3.9.0/src/integrator_janus.c
+-rw-r--r--   0 rein       (502) staff       (20)    10361 2019-07-26 15:29:46.000000 rebound-3.9.0/src/integrator_saba.c
+-rw-r--r--   0 rein       (502) staff       (20)    15885 2019-02-25 18:09:43.000000 rebound-3.9.0/src/transformations.c
+-rw-r--r--   0 rein       (502) staff       (20)     7631 2019-07-26 15:29:46.000000 rebound-3.9.0/src/binarydiff.c
+-rw-r--r--   0 rein       (502) staff       (20)    24749 2019-07-26 15:29:46.000000 rebound-3.9.0/src/output.c
+-rw-r--r--   0 rein       (502) staff       (20)    13202 2016-11-17 01:44:28.000000 rebound-3.9.0/src/tree.c
```

### Comparing `rebound-3.8.3/PKG-INFO` & `rebound-3.9.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 Metadata-Version: 1.1
 Name: rebound
-Version: 3.8.3
+Version: 3.9.0
 Summary: An open-source multi-purpose N-body code
 Home-page: http://github.com/hannorein/rebound
 Author: Hanno Rein
 Author-email: hanno@hanno-rein.de
 License: GPL
 Description: REBOUND - An open-source multi-purpose N-body code
         ==================================================
         
-        .. image:: http://img.shields.io/badge/rebound-v3.8.3-green.svg?style=flat
+        .. image:: http://img.shields.io/badge/rebound-v3.9.0-green.svg?style=flat
             :target: http://rebound.readthedocs.org
         .. image:: https://badge.fury.io/py/rebound.svg
             :target: https://badge.fury.io/py/rebound
         .. image:: http://img.shields.io/badge/license-GPL-green.svg?style=flat 
             :target: https://github.com/hannorein/rebound/blob/master/LICENSE
         .. image:: http://img.shields.io/travis/hannorein/rebound/master.svg?style=flat 
             :target: https://travis-ci.org/hannorein/rebound/
```

### Comparing `rebound-3.8.3/LICENSE` & `rebound-3.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/MANIFEST.in` & `rebound-3.9.0/MANIFEST.in`

 * *Files 5% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 include src/integrator_ias15.c
 include src/integrator_whfast.c
+include src/integrator_saba.c
 include src/integrator_leapfrog.c
 include src/integrator_sei.c
 include src/integrator_mercurius.c
 include src/integrator_janus.c
 include src/integrator.c
 include src/gravity.c
 include src/collision.c
@@ -15,14 +16,15 @@
 include src/rebound.c
 include src/tools.c
 include src/derivatives.c
 include src/particle.c
 include src/simulationarchive.c
 include src/integrator_ias15.h
 include src/integrator_whfast.h
+include src/integrator_saba.h
 include src/integrator_leapfrog.h
 include src/integrator_sei.h
 include src/integrator_mercurius.h
 include src/integrator_janus.h
 include src/integrator.h
 include src/collision.h
 include src/boundary.h
```

### Comparing `rebound-3.8.3/rebound.egg-info/PKG-INFO` & `rebound-3.9.0/rebound.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 Metadata-Version: 1.1
 Name: rebound
-Version: 3.8.3
+Version: 3.9.0
 Summary: An open-source multi-purpose N-body code
 Home-page: http://github.com/hannorein/rebound
 Author: Hanno Rein
 Author-email: hanno@hanno-rein.de
 License: GPL
 Description: REBOUND - An open-source multi-purpose N-body code
         ==================================================
         
-        .. image:: http://img.shields.io/badge/rebound-v3.8.3-green.svg?style=flat
+        .. image:: http://img.shields.io/badge/rebound-v3.9.0-green.svg?style=flat
             :target: http://rebound.readthedocs.org
         .. image:: https://badge.fury.io/py/rebound.svg
             :target: https://badge.fury.io/py/rebound
         .. image:: http://img.shields.io/badge/license-GPL-green.svg?style=flat 
             :target: https://github.com/hannorein/rebound/blob/master/LICENSE
         .. image:: http://img.shields.io/travis/hannorein/rebound/master.svg?style=flat 
             :target: https://travis-ci.org/hannorein/rebound/
```

### Comparing `rebound-3.8.3/rebound.egg-info/SOURCES.txt` & `rebound-3.9.0/rebound.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,14 @@
 LICENSE
 MANIFEST.in
 README.rst
 setup.py
 version.txt
 rebound/__init__.py
 rebound/data.py
-rebound/debug.py
 rebound/horizons.py
 rebound/interruptible_pool.py
 rebound/particle.py
 rebound/plotting.py
 rebound/rebound.h
 rebound/simulation.py
 rebound/simulationarchive.py
@@ -36,23 +35,25 @@
 rebound/tests/test_megno.py
 rebound/tests/test_mercurius.py
 rebound/tests/test_orbital_elements.py
 rebound/tests/test_particle.py
 rebound/tests/test_plotting.py
 rebound/tests/test_post_timestep_modifications.py
 rebound/tests/test_restart_mercurius.py
+rebound/tests/test_saba.py
 rebound/tests/test_serialize.py
 rebound/tests/test_shearingsheet.py
 rebound/tests/test_simulation.py
 rebound/tests/test_simulationarchive.py
 rebound/tests/test_simulationarchive_matrix.py
 rebound/tests/test_transformations.py
 rebound/tests/test_units.py
 rebound/tests/test_variational.py
 rebound/tests/test_whfast.py
+rebound/tests/test_whfast_advanced.py
 src/binarydiff.c
 src/binarydiff.h
 src/boundary.c
 src/boundary.h
 src/collision.c
 src/collision.h
 src/derivatives.c
@@ -69,14 +70,16 @@
 src/integrator_ias15.h
 src/integrator_janus.c
 src/integrator_janus.h
 src/integrator_leapfrog.c
 src/integrator_leapfrog.h
 src/integrator_mercurius.c
 src/integrator_mercurius.h
+src/integrator_saba.c
+src/integrator_saba.h
 src/integrator_sei.c
 src/integrator_sei.h
 src/integrator_whfast.c
 src/integrator_whfast.h
 src/output.c
 src/output.h
 src/particle.c
```

### Comparing `rebound-3.8.3/setup.py` & `rebound-3.9.0/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -13,27 +13,28 @@
 
 # Try to get git hash
 try:
     import subprocess
     ghash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("ascii")
     ghash_arg = "-DGITHASH="+ghash.strip()
 except:
-    ghash_arg = "-DGITHASH=24612371c00bbdea906a6291567952e3062ebf9b" #GITHASHAUTOUPDATE
+    ghash_arg = "-DGITHASH=f99b700fd0fa329a6e79c6f9621986e45f0b415d" #GITHASHAUTOUPDATE
 
 extra_link_args=[]
 if sys.platform == 'darwin':
     from distutils import sysconfig
     vars = sysconfig.get_config_vars()
     vars['LDSHARED'] = vars['LDSHARED'].replace('-bundle', '-shared')
     extra_link_args=['-Wl,-install_name,@rpath/librebound'+suffix]
     
 libreboundmodule = Extension('librebound',
                     sources = [ 'src/rebound.c',
                                 'src/integrator_ias15.c',
                                 'src/integrator_whfast.c',
+                                'src/integrator_saba.c',
                                 'src/integrator_mercurius.c',
                                 'src/integrator_leapfrog.c',
                                 'src/integrator_janus.c',
                                 'src/integrator_sei.c',
                                 'src/integrator.c',
                                 'src/gravity.c',
                                 'src/boundary.c',
@@ -57,15 +58,15 @@
                     )
 
 here = os.path.abspath(os.path.dirname(__file__))
 with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
     long_description = f.read()
 
 setup(name='rebound',
-    version='3.8.3',
+    version='3.9.0',
     description='An open-source multi-purpose N-body code',
     long_description=long_description,
     url='http://github.com/hannorein/rebound',
     author='Hanno Rein',
     author_email='hanno@hanno-rein.de',
     license='GPL',
     classifiers=[
```

### Comparing `rebound-3.8.3/README.rst` & `rebound-3.9.0/README.rst`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 REBOUND - An open-source multi-purpose N-body code
 ==================================================
 
-.. image:: http://img.shields.io/badge/rebound-v3.8.3-green.svg?style=flat
+.. image:: http://img.shields.io/badge/rebound-v3.9.0-green.svg?style=flat
     :target: http://rebound.readthedocs.org
 .. image:: https://badge.fury.io/py/rebound.svg
     :target: https://badge.fury.io/py/rebound
 .. image:: http://img.shields.io/badge/license-GPL-green.svg?style=flat 
     :target: https://github.com/hannorein/rebound/blob/master/LICENSE
 .. image:: http://img.shields.io/travis/hannorein/rebound/master.svg?style=flat 
     :target: https://travis-ci.org/hannorein/rebound/
```

### Comparing `rebound-3.8.3/rebound/simulation.py` & `rebound-3.9.0/rebound/simulation.py`

 * *Files 2% similar despite different names*

```diff
@@ -16,20 +16,22 @@
     # Fails on python3, but not important
     pass
 import types
       
 ### The following enum and class definitions need to
 ### consitent with those in rebound.h
         
-INTEGRATORS = {"ias15": 0, "whfast": 1, "sei": 2, "leapfrog": 4, "none": 7, "janus": 8, "mercurius": 9}
+INTEGRATORS = {"ias15": 0, "whfast": 1, "sei": 2, "leapfrog": 4, "none": 7, "janus": 8, "mercurius": 9, "saba": 10}
 BOUNDARIES = {"none": 0, "open": 1, "periodic": 2, "shear": 3}
 GRAVITIES = {"none": 0, "basic": 1, "compensated": 2, "tree": 3, "mercurius": 4}
 COLLISIONS = {"none": 0, "direct": 1, "tree": 2, "mercurius": 3, "line": 4}
 VISUALIZATIONS = {"none": 0, "opengl": 1, "webgl": 2}
-COORDINATES = {"jacobi": 0, "democraticheliocentric": 1, "whds": 2}
+WHFAST_KERNELS = {"default": 0, "modifiedkick": 1, "composition": 2, "lazy": 3}
+WHFAST_COORDINATES = {"jacobi": 0, "democraticheliocentric": 1, "whds": 2}
+SABA_CORRECTORS = {"none": 0, "modifiedkick": 1, "lazy": 2}
 
 # Format: Majorerror, id, message
 BINARY_WARNINGS = [
     (True,  1, "Cannot read binary file. Check filename and file contents."),
     (False, 2, "Binary file was saved with a different version of REBOUND. Binary format might have changed."),
     (False, 4, "You have to reset function pointers after creating a reb_simulation struct with a binary file."),
     (False, 8, "Binary file might be corrupted. Number of particles found does not match particle number expected."),
@@ -120,14 +122,57 @@
                 ("e", reb_dp7),
                 ("br", reb_dp7),
                 ("er", reb_dp7),
                 ("map", POINTER(c_int)),
                 ("map_allocated_n", c_int),
                 ]
 
+class reb_simulation_integrator_saba(Structure):
+    """
+    This class is an abstraction of the C-struct reb_simulation_integrator_saba.
+    It controls the behaviour of the SABA / SABAC integrator family. 
+
+    :ivar int k:      
+        Sets the number of evalutations. k=1 is SABA1/SABAC1, k=2 is SABA2/SABAC2
+        and so forth.
+    :ivar int corrector:      
+        Turns correctors on (1) or off (0)
+    """
+    _fields_ = [("k", c_uint),
+                ("_corrector", c_uint),
+                ("safe_mode", c_uint),
+                ("is_synchronized", c_uint),
+            ]
+    @property
+    def corrector(self):
+        """
+        Get or set the SABA Corrector.
+
+        Available correctors are:
+
+        - ``'none'`` (no corrector used, SABA)
+        - ``'modifiedkick'`` (modified kick, SABAC)
+        - ``'lazy'`` (Lazy implementer's method, SABACL)
+        """
+        i = self._corrector
+        for name, _i in SABA_CORRECTORS.items():
+            if i==_i:
+                return name
+        return i
+    @corrector.setter
+    def corrector(self, value):
+        if isinstance(value, int):
+            self._corrector = c_uint(value)
+        elif isinstance(value, basestring):
+            value = value.lower().replace(" ", "")
+            if value in SABA_CORRECTORS: 
+                self._corrector = SABA_CORRECTORS[value]
+            else:
+                raise ValueError("Warning. Kernel not found.")
+
 class reb_simulation_integrator_whfast(Structure):
     """
     This class is an abstraction of the C-struct reb_simulation_integrator_whfast.
     It controls the behaviour of the symplectic WHFast integrator described 
     in Rein and Tamayo (2015).
     
     This struct should be accessed via the simulation class only. Here is an 
@@ -136,16 +181,23 @@
     >>> sim = rebound.Simulation()
     >>> sim.ri_whfast.corrector =  11
 
     
     :ivar int corrector:      
         The order of the symplectic corrector in the WHFast integrator.
         By default the symplectic correctors are turned off (=0). For high
-        accuracy simulation set this value to 11. For more details read 
+        accuracy simulation set this value to 11 or 17. For more details read 
         Rein and Tamayo (2015).
+    :ivar int corrector2:      
+        Second correctors (C2 of Wisdom et al 1996).
+        By default the second symplectic correctors are turned off (=0). 
+        Set to 1 to turn them on.
+    :ivar int kernel:      
+        Kernel option. Set to 0 for the default WH kernel (standard kick step).
+        Other options are "modifiedkick" (1), "composition" (2), "lazy" (3).
     :ivar int recalculate_coordinates_this_timestep:
         Sets a flag that tells WHFast that the particles have changed.
         Setting this flag to 1 (default 0) triggers the WHFast integrator
         to recalculate Jacobi/heliocenctric coordinates. This is needed 
         if the user changes the particle position, velocity or mass 
         inbetween timesteps.  After every timestep the flag is set back 
         to 0, so if you continuously update the particles manually, 
@@ -159,18 +211,21 @@
         If safe_mode is 1 (default) particles can be modified between
         timesteps and particle velocities and positions are always synchronised.
         If you set safe_mode to 0, the speed and accuracy of WHFast improve.
         However, make sure you are aware of the consequences. Read the iPython tutorial
         on advanced WHFast usage to learn more.
     """
     _fields_ = [("corrector", c_uint),
+                ("corrector2", c_uint),
+                ("_kernel", c_uint),
                 ("_coordinates", c_uint),
                 ("recalculate_coordinates_this_timestep", c_uint),
                 ("safe_mode", c_uint),
                 ("p_jh", POINTER(Particle)),
+                ("p_temp", POINTER(Particle)),
                 ("keep_unsynchronized", c_uint),
                 ("is_synchronized", c_uint),
                 ("allocatedN", c_uint),
                 ("timestep_warning", c_uint),
                 ("recalculate_coordinates_but_not_synchronized_warning", c_uint)]
     @property
     def coordinates(self):
@@ -180,28 +235,55 @@
         Available coordinate systems are:
 
         - ``'jacobi'`` (default)
         - ``'democraticheliocentric'``
         - ``'whds'``
         """
         i = self._coordinates
-        for name, _i in COORDINATES.items():
+        for name, _i in WHFAST_COORDINATES.items():
             if i==_i:
                 return name
         return i
     @coordinates.setter
     def coordinates(self, value):
         if isinstance(value, int):
             self._coordinates = c_uint(value)
         elif isinstance(value, basestring):
             value = value.lower()
-            if value in COORDINATES: 
-                self._coordinates = COORDINATES[value]
+            if value in WHFAST_COORDINATES: 
+                self._coordinates = WHFAST_COORDINATES[value]
             else:
                 raise ValueError("Warning. Coordinate system not found.")
+    @property
+    def kernel(self):
+        """
+        Get or set the WHFast Kernel.
+
+        Available kernels are:
+
+        - ``'default'`` (standard WH kernel, kick)
+        - ``'modifiedkick'`` (modified kick for newtonian gravity)
+        - ``'composition'`` (Wisdom's composition method)
+        - ``'lazy'`` (Lazy implementer's method)
+        """
+        i = self._kernel
+        for name, _i in WHFAST_KERNELS.items():
+            if i==_i:
+                return name
+        return i
+    @kernel.setter
+    def kernel(self, value):
+        if isinstance(value, int):
+            self._kernel = c_uint(value)
+        elif isinstance(value, basestring):
+            value = value.lower().replace(" ", "")
+            if value in WHFAST_KERNELS: 
+                self._kernel = WHFAST_KERNELS[value]
+            else:
+                raise ValueError("Warning. Kernel not found.")
 
 class Orbit(Structure):
     """
     A class containing orbital parameters for a particle.
     This is an abstraction of the reb_orbit data structure in C.
 
     When using the various REBOUND functions using Orbits, all angles are in radians. 
@@ -461,14 +543,17 @@
             Interval between outputs in code units.
         walltime : float
             Interval between outputs in wall time (seconds). 
             Useful when using IAS15 with adaptive timesteps. 
         step : int
             Interval between outputs in number of timesteps. 
             Useful when outputs need to be spaced exactly.
+        deletefile: bool
+            False (default) appends to archive if it exists.
+            True deletes filename and starts a new archive.
         
         Examples
         --------
         The following example creates a simulation, then 
         initializes the Simulation Archive and integrates
         it forward in time. 
 
@@ -494,27 +579,33 @@
             clibrebound.reb_simulationarchive_automate_interval(byref(self), c_char_p(filename.encode("ascii")), c_double(interval))
         if walltime:
             clibrebound.reb_simulationarchive_automate_walltime(byref(self), c_char_p(filename.encode("ascii")), c_double(walltime))
         if step:
             clibrebound.reb_simulationarchive_automate_step(byref(self), c_char_p(filename.encode("ascii")), c_ulonglong(step))
         self.process_messages()
 
-    def simulationarchive_snapshot(self, filename):
+    def simulationarchive_snapshot(self, filename, deletefile=False):
         """
         Take a snapshot and save it to a SimulationArchive file.
         If the file does not exist yet, a new one will be created. 
         If the file does exist, a snapshot will be appended.
         
         Arguments
         ---------
         filename : str
             Filename of the binary file.
+        deletefile: bool
+            False (default) appends to archive if it exists.
+            True deletes filename and starts a new archive.
 
         """
+        if deletefile and os.path.isfile(filename):
+            os.remove(filename)
         clibrebound.reb_simulationarchive_snapshot(byref(self), c_char_p(filename.encode("ascii")))
+        self.process_messages()
 
     @property
     def simulationarchive_filename(self):
         """
         Returns the current SimulationArchive filename in use. 
         Do not set manually. Use sim.automateSimulationArchive() instead
         """
@@ -531,14 +622,21 @@
             elif msg[0]=='e':
                 raise RuntimeError(msg[1:])
 
 
     def __del__(self):
         if self._b_needsfree_ == 1: # to avoid, e.g., sim.particles[1]._sim.contents.G creating a Simulation instance to get G, and then freeing the C simulation when it immediately goes out of scope
             clibrebound.reb_free_pointers(byref(self))
+    def __eq__(self, other):
+        # This ignores the walltime parameter
+        if not isinstance(other,Simulation):
+            return NotImplemented
+        clibrebound.reb_diff_simulations.restype = c_int
+        ret = clibrebound.reb_diff_simulations(byref(self), byref(other),c_int(2))
+        return not ret
 
     def __add__(self, other):
         if not isinstance(other,Simulation):
             return NotImplemented
         c = self.copy()
         return c.__iadd__(other)
     
@@ -623,14 +721,17 @@
         try:
             scalar_pos = float(scalar_pos)
             scalar_vel = float(scalar_vel)
         except:
             raise ValueError("Cannot multiply simulation with non-scalars.")
         clibrebound.reb_simulation_imul(byref(self), c_double(scalar_pos), c_double(scalar_vel))
 
+    def clear_pre_post_pointers(self):
+        # temporary fix for REBOUNDx
+        clibrebound.reb_clear_pre_post_pointers(byref(self))
 
 # Status functions
     def status(self):
         """ 
         Prints a summary of the current status 
         of the simulation.
         """
@@ -797,50 +898,43 @@
         """
         Get or set the intergrator module.
 
         Available integrators are:
 
         - ``'ias15'`` (default)
         - ``'whfast'``
+        - ``'saba'``
         - ``'sei'``
         - ``'leapfrog'``
         - ``'janus'``
         - ``'mercurius'``
-        - ``'bs'``
+        - ``'WHCKL'`` (a wrapper which uses and configures WHFAST)
         - ``'none'``
         
         Check the online documentation for a full description of each of the integrators. 
         """
         i = self._integrator
         for name, _i in INTEGRATORS.items():
             if i==_i:
                 return name
         return i
     @integrator.setter
     def integrator(self, value):
         if isinstance(value, int):
             self._integrator = c_int(value)
         elif isinstance(value, basestring):
-            debug.integrator_fullname = value
-            debug.integrator_package = "REBOUND"
             value = value.lower()
             if value in INTEGRATORS: 
                 self._integrator = INTEGRATORS[value]
-            elif value.lower() == "mercury":
-                debug.integrator_package = "MERCURY"
-            elif value.lower() == "swifter-whm":
-                debug.integrator_package = "SWIFTER"
-            elif value.lower() == "swifter-symba":
-                debug.integrator_package = "SWIFTER"
-            elif value.lower() == "swifter-helio":
-                debug.integrator_package = "SWIFTER"
-            elif value.lower() == "swifter-tu4":
-                debug.integrator_package = "SWIFTER"
+            elif value=="whckl":
+                self.integrator = "whfast"
+                self.ri_whfast.corrector = 17
+                self.ri_whfast.kernel = "lazy"
             else:
-                raise ValueError("Warning. Integrator not found.")
+                raise ValueError("Integrator not found.")
     
     @property
     def boundary(self):
         """
         Get or set the boundary module.
 
         Available boundary modules are:
@@ -1529,34 +1623,31 @@
 
         >>> import numpy as np
         >>> for time in np.linspace(0,100.,10): 
         >>>     sim.integrate(time)
         >>>     perform_output(sim)
         
         """
-        if debug.integrator_package =="REBOUND":
-            self.exact_finish_time = c_int(exact_finish_time)
-            ret_value = clibrebound.reb_integrate(byref(self), c_double(tmax))
-            if ret_value == 1:
-                self.process_messages()
-                raise SimulationError("An error occured during the integration.")
-            if ret_value == 2:
-                raise NoParticles("No more particles left in simulation.")
-            if ret_value == 3:
-                raise Encounter("Two particles had a close encounter (d<exit_min_distance).")
-            if ret_value == 4:
-                raise Escape("A particle escaped (r>exit_max_distance).")
-            if ret_value == 5:
-                raise Escape("User caused exit. Simulation did not finish.") # should not occur in python
-            if ret_value == 6:
-                raise KeyboardInterrupt
-            if ret_value == 7:
-                raise Collision("Two particles collided (d < r1+r2)")
-        else:
-            debug.integrate_other_package(tmax,exact_finish_time)
+        self.exact_finish_time = c_int(exact_finish_time)
+        ret_value = clibrebound.reb_integrate(byref(self), c_double(tmax))
+        if ret_value == 1:
+            self.process_messages()
+            raise SimulationError("An error occured during the integration.")
+        if ret_value == 2:
+            raise NoParticles("No more particles left in simulation.")
+        if ret_value == 3:
+            raise Encounter("Two particles had a close encounter (d<exit_min_distance).")
+        if ret_value == 4:
+            raise Escape("A particle escaped (r>exit_max_distance).")
+        if ret_value == 5:
+            raise Escape("User caused exit. Simulation did not finish.") # should not occur in python
+        if ret_value == 6:
+            raise KeyboardInterrupt
+        if ret_value == 7:
+            raise Collision("Two particles collided (d < r1+r2)")
         self.process_messages()
 
     def integrator_reset(self):
         """
         Call this function to reset temporary integrator variables
         """
         clibrebound.reb_integrator_reset(byref(self))
@@ -1832,14 +1923,15 @@
                 ("_visualization", c_int),
                 ("_collision", c_int),
                 ("_integrator", c_int),
                 ("_boundary", c_int),
                 ("_gravity", c_int),
                 ("ri_sei", reb_simulation_integrator_sei), 
                 ("ri_whfast", reb_simulation_integrator_whfast),
+                ("ri_saba", reb_simulation_integrator_saba),
                 ("ri_ias15", reb_simulation_integrator_ias15),
                 ("ri_mercurius", reb_simulation_integrator_mercurius),
                 ("ri_janus", reb_simulation_integrator_janus),
                 ("_additional_forces", CFUNCTYPE(None,POINTER(Simulation))),
                 ("_pre_timestep_modifications", CFUNCTYPE(None,POINTER(Simulation))),
                 ("_post_timestep_modifications", CFUNCTYPE(None,POINTER(Simulation))),
                 ("_heartbeat", CFUNCTYPE(None,POINTER(Simulation))),
@@ -1938,9 +2030,8 @@
             yield p
 
     def __len__(self):
         return self.sim.N
 
 # Import at the end to avoid circular dependence
 from . import horizons
-from . import debug
 from .simulationarchive import SimulationArchive
```

### Comparing `rebound-3.8.3/rebound/horizons.py` & `rebound-3.9.0/rebound/horizons.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/widget.py` & `rebound-3.9.0/rebound/widget.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/units.py` & `rebound-3.9.0/rebound/units.py`

 * *Files 2% similar despite different names*

```diff
@@ -34,15 +34,17 @@
     'kyr':31557600.*1.e3,
     'myr':31557600.*1.e6,
     'gyr':31557600.*1.e9}
 lengths_SI =  {'m':1.,
     'cm':0.01,
     'km':1000.,
     'au':149597870700.,
-    'aus':149597870700.
+    'aus':149597870700.,
+    'pc':3.085677581e16,
+    'parsec':3.085677581e16
     }
 
     #What we measure accurately is GM, so set mass units such that G*M gives the value of GM in horizons.py (in the list at the end of horizons.py, the NAIF codes ending in 99 refer to the planets, single digits to the total mass of the planet plus its moons).  Have to multiply by 10**9 since that list has G in kg^-1km^3/s^2 and we use SI.
 
 masses_SI = {'kg':1.,
     'g':1.0e-3,
     'gram':1.0e-3,
```

### Comparing `rebound-3.8.3/rebound/rebound.h` & `rebound-3.9.0/rebound/rebound.h`

 * *Files 2% similar despite different names*

```diff
@@ -292,29 +292,87 @@
     double tandt;       ///< Cached tan() 
     double sindtz;      ///< Cached sin(), z axis
     double tandtz;      ///< Cached tan(), z axis
     /** @endcond */
 };
 
 /**
+ * @brief This structure contains variables used by the SABA integrator.
+ */
+struct reb_simulation_integrator_saba {
+    /**
+     * @brief Number of evaluations of the interaction step.
+     * @details
+     * - 1: standard WH 
+     * - 2: SABA2/SABAC2 
+     * - 3: SABA3/SABAC3 
+     * - 4: SABA4/SABAC4 
+     */
+    unsigned int k;
+    /**
+     * @brief Turn corrector on/off.
+     * @details
+     * - 0: corrector off
+     * - 1: normal (modified kick) corrector on
+     * - 2: lazy implementer's corrector on
+     */
+    enum {
+        REB_SABA_CORRECTOR_NONE = 0,
+        REB_SABA_CORRECTOR_MODIFIEDKICK = 1,
+        REB_SABA_CORRECTOR_LAZY = 2,
+    } corrector;
+
+    /**
+     * @brief safe_mode has the same functionality as in WHFast.
+     */
+    unsigned int safe_mode;
+    unsigned int is_synchronized;
+};
+
+/**
  * @brief This structure contains variables used by the WHFast integrator.
  */
 struct reb_simulation_integrator_whfast {
     /**
-     * @brief This variable turns on/off different symplectic correctors for WHFast. See Rein & Tamayo 2015 and Wisdom 2006 for a discussion.
-     * @details 
-     * - 0 (default): turns off all correctors
-     * - 3: uses third order (two-stage) corrector 
-     * - 5: uses fifth order (four-stage) corrector 
-     * - 7: uses seventh order (six-stage) corrector 
-     * - 11: uses eleventh order (ten-stage) corrector 
+     * @brief This variable turns on/off different first symplectic correctors for WHFast.
+     * @details These correctors remove terms of order O(eps*dt^2) 
+     * - 0 (default): turns off all first correctors
+     * - 3: uses third order (two-stage) first corrector 
+     * - 5: uses fifth order (four-stage) first corrector 
+     * - 7: uses seventh order (six-stage) first corrector 
+     * - 11: uses eleventh order (ten-stage) first corrector 
+     * - 17: uses 17th order (16-stage) first corrector 
      */
     unsigned int corrector;
     
     /**
+     * @brief This variable turns on/off the second symplectic correctors for WHFast.
+     * @details 
+     * - 0 (default): turns off second correctors
+     * - 1: uses second corrector 
+     */
+    unsigned int corrector2;
+    
+    /**
+     * @brief This variable determines the kernel of the WHFast integrator.
+     * @details 
+     * - 0 (default): Uses a standard WH kick step 
+     * - 1: uses the exact modified kick (for Newtonian gravity) 
+     * - 2: uses the composition kernel  
+     * - 3: uses the lazy implementer's modified kick   
+     */
+    enum {
+        REB_WHFAST_KERNEL_DEFAULT = 0,
+        REB_WHFAST_KERNEL_MODIFIEDKICK = 1,
+        REB_WHFAST_KERNEL_COMPOSITION = 2,
+        REB_WHFAST_KERNEL_LAZY = 3,
+    }kernel;
+    
+    
+    /**
      * @brief Chooses the coordinate system for the WHFast algorithm. Default is Jacobi Coordinates.
      */
     enum {
         REB_WHFAST_COORDINATES_JACOBI = 0,                      ///< Jacobi coordinates (default)
         REB_WHFAST_COORDINATES_DEMOCRATICHELIOCENTRIC = 1,      ///< Democratic Heliocentric coordinates
         REB_WHFAST_COORDINATES_WHDS = 2,                        ///< WHDS coordinates (Hernandez and Dehnen, 2017)
         } coordinates;
@@ -347,28 +405,34 @@
      * coordinates of all particles.
      * It is automatically filled and updated by WHfast.
      * Access this array with caution.
      */
     struct reb_particle* REBOUND_RESTRICT p_jh;
     
     /**
+     * @brief Internal temporary array used for lazy implementer's kernel method
+     */
+    struct reb_particle* REBOUND_RESTRICT p_temp;
+    
+    /**
      * @brief Generate inertial coordinates at the end of the integration, but do not change the Jacobi/heliocentric coordinates
      * @details Danger zone! Only use this flag if you are absolutely sure
      * what you are doing. This is intended for
      * simulation which have to be reproducible on a bit by bit basis.
      */
     unsigned int keep_unsynchronized;
 
     /**
      * @cond PRIVATE
      * Internal data structures below. Nothing to be changed by the user.
      */
 
     unsigned int is_synchronized;   ///< Flag to determine if current particle structure is synchronized
-    unsigned int allocated_N;   ///< Space allocated in arrays
+    unsigned int allocated_N;       ///< Space allocated in p_jh array
+    unsigned int allocated_Ntemp;   ///< Space allocated in p_temp array
     unsigned int timestep_warning;  ///< Counter of timestep warnings
     unsigned int recalculate_coordinates_but_not_synchronized_warning;   ///< Counter of Jacobi synchronization errors
     /**
      * @endcond
      */
 };
 
@@ -597,14 +661,21 @@
     REB_BINARY_FIELD_TYPE_PYTHON_UNIT_M = 131,
     REB_BINARY_FIELD_TYPE_PYTHON_UNIT_T = 132,
     REB_BINARY_FIELD_TYPE_MERCURIUS_COMPOS = 133,
     REB_BINARY_FIELD_TYPE_MERCURIUS_COMVEL = 134,
     REB_BINARY_FIELD_TYPE_SAAUTOSTEP = 135,
     REB_BINARY_FIELD_TYPE_SANEXTSTEP = 136,
     REB_BINARY_FIELD_TYPE_STEPSDONE = 137,
+    REB_BINARY_FIELD_TYPE_SABA_K = 138,
+    REB_BINARY_FIELD_TYPE_SABA_CORRECTOR = 139,
+    REB_BINARY_FIELD_TYPE_SABA_SAFEMODE = 140,
+    REB_BINARY_FIELD_TYPE_SABA_ISSYNCHRON = 141,
+    REB_BINARY_FIELD_TYPE_WHFAST_CORRECTOR2 = 143,
+    REB_BINARY_FIELD_TYPE_WHFAST_KERNEL = 144,
+    REB_BINARY_FIELD_TYPE_DTLASTDONE = 145,
     REB_BINARY_FIELD_TYPE_HEADER = 1329743186,  // Corresponds to REBO (first characters of header text)
     REB_BINARY_FIELD_TYPE_SABLOB = 9998,        // SA Blob
     REB_BINARY_FIELD_TYPE_END = 9999,
 };
 
 /**
  * @brief This structure is used to save and load binary files.
@@ -856,14 +927,15 @@
         REB_INTEGRATOR_WHFAST = 1,   ///< WHFast integrator, symplectic, 2nd order, up to 11th order correctors
         REB_INTEGRATOR_SEI = 2,      ///< SEI integrator for shearing sheet simulations, symplectic, needs OMEGA variable
         REB_INTEGRATOR_LEAPFROG = 4, ///< LEAPFROG integrator, simple, 2nd order, symplectic
         // REB_INTEGRATOR_HERMES = 5,   ///< HERMES Integrator, not available anymore. Use MERCURIUS instead.
         REB_INTEGRATOR_NONE = 7,     ///< Do not integrate anything
         REB_INTEGRATOR_JANUS = 8,    ///< Bit-wise reversible JANUS integrator.
         REB_INTEGRATOR_MERCURIUS = 9,///< MERCURIUS integrator 
+        REB_INTEGRATOR_SABA = 10,    ///< SABA integrator family (Laskar and Robutel 2001)
         } integrator;
 
     /**
      * @brief Available boundary conditions
      */
     enum {
         REB_BOUNDARY_NONE = 0,      ///< Do not check for anything (default)
@@ -877,24 +949,26 @@
      */
     enum {
         REB_GRAVITY_NONE = 0,       ///< Do not calculate graviational forces
         REB_GRAVITY_BASIC = 1,      ///< Basic O(N^2) direct summation algorithm, choose this for shearing sheet and periodic boundary conditions
         REB_GRAVITY_COMPENSATED = 2,    ///< Direct summation algorithm O(N^2) but with compensated summation, slightly slower than BASIC but more accurate
         REB_GRAVITY_TREE = 3,       ///< Use the tree to calculate gravity, O(N log(N)), set opening_angle2 to adjust accuracy.
         REB_GRAVITY_MERCURIUS = 4,  ///< Special gravity routine only for MERCURIUS
+        REB_GRAVITY_JACOBI = 5,     ///< Special gravity routine which includes the Jacobi terms for WH integrators 
         } gravity;
     /** @} */
 
 
     /**
      * \name Integrator structs (the contain integrator specific variables and temporary data structures) 
      * @{
      */
     struct reb_simulation_integrator_sei ri_sei;        ///< The SEI struct 
     struct reb_simulation_integrator_whfast ri_whfast;  ///< The WHFast struct 
+    struct reb_simulation_integrator_saba ri_saba;      ///< The SABA struct 
     struct reb_simulation_integrator_ias15 ri_ias15;    ///< The IAS15 struct
     struct reb_simulation_integrator_mercurius ri_mercurius;      ///< The MERCURIUS struct
     struct reb_simulation_integrator_janus ri_janus;    ///< The JANUS struct 
     /** @} */
 
     /**
      * \name Callback functions
@@ -972,14 +1046,24 @@
  * @details All simulation data, including all particle data will be copied. Function pointers
  * need to be set manually afterwards. 
  * Working on the copy will not affect the original simulation.
  */
 struct reb_simulation* reb_copy_simulation(struct reb_simulation* r);
 
 /**
+ * @brief Compares to REBOUND simulations bit by bit.
+ * @return If r1 and r2 are exactly equal to each other then 0 is returned, otherwise 1. The walltime parameter in 
+ * the REBOUND struct is ignored in this comparison.
+ * @param r1 The first REBOUND simulation to be compared.
+ * @param r2 The second REBOUND simulation to be compared.
+ * @param output_option Is set to 1, then the output is printed on the screen. If set to 2, only the return value indicates if the simulations are different. 
+ */
+int reb_diff_simulations(struct reb_simulation* r1, struct reb_simulation* r2, int output_option);
+
+/**
  * @brief Initialize reb_simulation structure.
  *
  * @details Same as reb_create_simulation() but does not allocate memory for structure itself.
  * @param r Structure to be initialized (needs to be allocated externally).
  */
 void reb_init_simulation(struct reb_simulation* r);
 
@@ -1342,17 +1426,31 @@
  * @details This function can be used to save the current status of a REBOUND simualtion 
  * and later restart the simualtion.
  * @param r The rebound simulation to be considered
  * @param filename Output filename.
  */
 void reb_output_binary(struct reb_simulation* r, const char* filename);
 
+/**
+ * @brief This function compares two REBOUND simulations and records the difference in a buffer.
+ * @details This is used for taking a SimulationArchive Snapshot.
+ * @param buf1 The buffer corresponding to the first rebound simulation to be compared
+ * @param buf2 The buffer corresponding to the second rebound simulation to be compared
+ * @param bufp The buffer which will contain the differences. 
+ */
 void reb_binary_diff(char* buf1, size_t size1, char* buf2, size_t size2, char** bufp, size_t* sizep);
 
 /**
+ * @brief Same as reb_binary_diff but with more options.
+ * @param output_option If set to 0, the differences are written to bufp. If set to 1, printed on the screen. If set to 2, then only the return value indicates any differences.
+ * @return 0 is returned if the simulations do not differ (are equal). 1 is return if they differ.
+ */
+int reb_binary_diff_with_options(char* buf1, size_t size1, char* buf2, size_t size2, char** bufp, size_t* sizep, int output_option);
+
+/**
  * @brief Append the positions and velocities of all particles to an ASCII file.
  * @param r The rebound simulation to be considered
  * @param filename Output filename.
  */
 void reb_output_ascii(struct reb_simulation* r, char* filename);
 
 /**
```

### Comparing `rebound-3.8.3/rebound/plotting.py` & `rebound-3.9.0/rebound/plotting.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tools.py` & `rebound-3.9.0/rebound/tools.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_restart_mercurius.py` & `rebound-3.9.0/rebound/tests/test_restart_mercurius.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_interruble_pool.py` & `rebound-3.9.0/rebound/tests/test_interruble_pool.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_plotting.py` & `rebound-3.9.0/rebound/tests/test_plotting.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_megno.py` & `rebound-3.9.0/rebound/tests/test_megno.py`

 * *Files 2% similar despite different names*

```diff
@@ -11,51 +11,52 @@
     
     def test_ias15(self):
         self.sim.integrator = "ias15"
         self.sim.add(m=1)
         self.sim.add(m=1e-3,a=1.5,e=0.1,inc=0.1)
         self.sim.add(m=1.e-3, a=15., e=0.1, inc=0.1)
         self.sim.init_megno(seed=0)
-        self.sim.integrate(1000)
+        self.sim.integrate(10000.)
         self.assertAlmostEqual(self.sim.calculate_megno(),2.,delta=2e-1)
         self.assertAlmostEqual(self.sim.calculate_lyapunov(),0.,delta=1e-3)
 
     def test_whfast(self):
         self.sim.integrator = "whfast"
         self.sim.add(m=1)
         self.sim.add(m=1e-3,a=1.5,e=0.1,inc=0.1)
         self.sim.add(m=1.e-3, a=15., e=0.1, inc=0.1)
         self.sim.init_megno(seed=0)
-        self.sim.integrate(1000)
+        self.sim.dt = self.sim.particles[1].P*0.07
+        self.sim.integrate(10000.)
         self.assertAlmostEqual(self.sim.calculate_megno(),2.,delta=2e-1)
         self.assertAlmostEqual(self.sim.calculate_lyapunov(),0.,delta=1e-3)
 
     def test_whfast_close_regular(self):
         self.sim = rebound.Simulation()
         self.sim.integrator = "whfast"
         self.sim.G = 4*math.pi**2
         self.sim.add(m=1.0, x=-4.7298443749900997e-07, y=2.3452237398515157e-06, z=-2.8779986923394045e-08, vx=-9.994358883493113e-06, vy=-2.8416720717989476e-06, vz=1.5927607755978474e-07)
         self.sim.add(m=4.544728982917554e-07, x=0.9818659845399763, y=0.19089291910956852, z=-0.011300485084842085, vx=-1.1951384526938573, vy=6.164295939653557, vz=0.16345519841419276)
         self.sim.add(m=1.7367161546229798e-06, x=-0.07616371745657412, y=-1.2648949778387153, z=0.01873838700271951, vx=5.516651885197617, vy=-0.34889260830083374, vz=-0.13577609379397024)
         self.sim.add(m=2.1454312223049496e-07, x=0.741238938912468, y=-1.0963570106709737, z=0.006397276680495443, vx=4.459049824337919, vy=3.011488098634852, vz=0.010452444973871466)
         self.sim.init_megno(seed=0)
         self.sim.dt = 0.034641008279678746
-        self.sim.integrate(1000)
+        self.sim.integrate(10000.)
         self.assertAlmostEqual(self.sim.calculate_megno(),2.,delta=2e-1)
         self.assertAlmostEqual(self.sim.calculate_lyapunov(),0.,delta=1e-3)
 
     def test_chaotic(self):
         self.sim = rebound.Simulation()
         self.sim.integrator = "ias15"
         self.sim.add(m=1.)
         self.sim.add(m=1.e-4, P=1.)
         self.sim.add(m=1.e-4, P=1.17)
         self.sim.init_megno(seed=0)
         self.sim.move_to_com()
-        self.sim.integrate(1000)
+        self.sim.integrate(1000.)
         self.megnoIAS = self.sim.calculate_megno()
         self.sim = rebound.Simulation()
         self.sim.integrator = "whfast"
         self.sim.add(m=1.)
         self.sim.add(m=1.e-4, P=1.)
         self.sim.add(m=1.e-4, P=1.17)
         self.sim.init_megno(seed=0)
```

### Comparing `rebound-3.8.3/rebound/tests/test_orbital_elements.py` & `rebound-3.9.0/rebound/tests/test_orbital_elements.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_mercurius.py` & `rebound-3.9.0/rebound/tests/test_mercurius.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_simulationarchive_matrix.py` & `rebound-3.9.0/rebound/tests/test_simulationarchive_matrix.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_shearingsheet.py` & `rebound-3.9.0/rebound/tests/test_shearingsheet.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_horizons.py` & `rebound-3.9.0/rebound/tests/test_horizons.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_copy.py` & `rebound-3.9.0/rebound/tests/test_copy.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_boundary.py` & `rebound-3.9.0/rebound/tests/test_boundary.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_whfast.py` & `rebound-3.9.0/rebound/tests/test_whfast.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_post_timestep_modifications.py` & `rebound-3.9.0/rebound/tests/test_post_timestep_modifications.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_transformations.py` & `rebound-3.9.0/rebound/tests/test_transformations.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_units.py` & `rebound-3.9.0/rebound/tests/test_units.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_gravity.py` & `rebound-3.9.0/rebound/tests/test_gravity.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_collisions.py` & `rebound-3.9.0/rebound/tests/test_collisions.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_hash.py` & `rebound-3.9.0/rebound/tests/test_hash.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_serialize.py` & `rebound-3.9.0/rebound/tests/test_serialize.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_janus.py` & `rebound-3.9.0/rebound/tests/test_janus.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_data.py` & `rebound-3.9.0/rebound/tests/test_data.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_additional_forces.py` & `rebound-3.9.0/rebound/tests/test_additional_forces.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_simulation.py` & `rebound-3.9.0/rebound/tests/test_simulation.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_particle.py` & `rebound-3.9.0/rebound/tests/test_particle.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_variational.py` & `rebound-3.9.0/rebound/tests/test_variational.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_simulationarchive.py` & `rebound-3.9.0/rebound/tests/test_simulationarchive.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/tests/test_integrator.py` & `rebound-3.9.0/rebound/tests/test_integrator.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/__init__.py` & `rebound-3.9.0/rebound/__init__.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/interruptible_pool.py` & `rebound-3.9.0/rebound/interruptible_pool.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/simulationarchive.py` & `rebound-3.9.0/rebound/simulationarchive.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/particle.py` & `rebound-3.9.0/rebound/particle.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/rebound/data.py` & `rebound-3.9.0/rebound/data.py`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/integrator_mercurius.h` & `rebound-3.9.0/src/integrator_mercurius.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/simulationarchive.c` & `rebound-3.9.0/src/simulationarchive.c`

 * *Files 1% similar despite different names*

```diff
@@ -97,14 +97,15 @@
                         r->ri_janus.allocated_N = r->N;
                     }
                     fread(r->ri_janus.p_int,sizeof(struct reb_particle_int)*r->N,1,inf);
                     reb_integrator_synchronize(r);  // get floating point coordinates 
                 }
                 break;
             case REB_INTEGRATOR_WHFAST:
+            case REB_INTEGRATOR_SABA:
                 {
                     // Recreate Jacobi arrrays
                     struct reb_particle* ps = r->particles;
                     if (r->ri_whfast.safe_mode==0){
                         // If same mode is off, store unsynchronized Jacobi coordinates
                         if (r->ri_whfast.allocated_N<(unsigned int)r->N){
                             if (r->ri_whfast.p_jh){
@@ -387,14 +388,15 @@
 static int reb_simulationarchive_snapshotsize(struct reb_simulation* const r){
     int size_snapshot = 0;
     switch (r->integrator){
         case REB_INTEGRATOR_JANUS:
             size_snapshot = sizeof(double)*2+sizeof(struct reb_particle_int)*r->N;
             break;
         case REB_INTEGRATOR_WHFAST:
+        case REB_INTEGRATOR_SABA:
             size_snapshot = sizeof(double)*2+sizeof(double)*7*r->N;
             break;
         case REB_INTEGRATOR_MERCURIUS:
             size_snapshot = sizeof(double)*2+sizeof(double)*8*r->N;
             break;
         case REB_INTEGRATOR_IAS15:
             size_snapshot =  sizeof(double)*4  // time, walltime, dt, dt_last_done
```

### Comparing `rebound-3.8.3/src/display.c` & `rebound-3.9.0/src/display.c`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/input.h` & `rebound-3.9.0/src/input.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/derivatives.c` & `rebound-3.9.0/src/derivatives.c`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/integrator_leapfrog.c` & `rebound-3.9.0/src/integrator_leapfrog.c`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/integrator_sei.h` & `rebound-3.9.0/src/integrator_sei.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/integrator_ias15.c` & `rebound-3.9.0/src/integrator_ias15.c`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/integrator.c` & `rebound-3.9.0/src/integrator.c`

 * *Files 4% similar despite different names*

```diff
@@ -34,14 +34,15 @@
 #include <time.h>
 #include <string.h>
 #include "rebound.h"
 #include "gravity.h"
 #include "output.h"
 #include "integrator.h"
 #include "integrator_whfast.h"
+#include "integrator_saba.h"
 #include "integrator_ias15.h"
 #include "integrator_mercurius.h"
 #include "integrator_leapfrog.h"
 #include "integrator_sei.h"
 #include "integrator_janus.h"
 
 void reb_integrator_part1(struct reb_simulation* r){
@@ -54,14 +55,17 @@
 			break;
 		case REB_INTEGRATOR_SEI:
 			reb_integrator_sei_part1(r);
 			break;
 		case REB_INTEGRATOR_WHFAST:
 			reb_integrator_whfast_part1(r);
 			break;
+		case REB_INTEGRATOR_SABA:
+			reb_integrator_saba_part1(r);
+			break;
 		case REB_INTEGRATOR_MERCURIUS:
 			reb_integrator_mercurius_part1(r);
 			break;
 		case REB_INTEGRATOR_JANUS:
 			reb_integrator_janus_part1(r);
 			break;
 		default:
@@ -79,14 +83,17 @@
 			break;
 		case REB_INTEGRATOR_SEI:
 			reb_integrator_sei_part2(r);
 			break;
 		case REB_INTEGRATOR_WHFAST:
 			reb_integrator_whfast_part2(r);
 			break;
+		case REB_INTEGRATOR_SABA:
+			reb_integrator_saba_part2(r);
+			break;
 		case REB_INTEGRATOR_MERCURIUS:
 			reb_integrator_mercurius_part2(r);
 			break;
 		case REB_INTEGRATOR_JANUS:
 			reb_integrator_janus_part2(r);
 			break;
         case REB_INTEGRATOR_NONE:
@@ -108,14 +115,17 @@
 			break;
 		case REB_INTEGRATOR_SEI:
 			reb_integrator_sei_synchronize(r);
 			break;
 		case REB_INTEGRATOR_WHFAST:
 			reb_integrator_whfast_synchronize(r);
 			break;
+		case REB_INTEGRATOR_SABA:
+			reb_integrator_saba_synchronize(r);
+			break;
 		case REB_INTEGRATOR_MERCURIUS:
 			reb_integrator_mercurius_synchronize(r);
 			break;
 		case REB_INTEGRATOR_JANUS:
 			reb_integrator_janus_synchronize(r);
 			break;
 		default:
@@ -137,14 +147,15 @@
 	r->integrator = REB_INTEGRATOR_IAS15;
 	r->gravity_ignore_terms = 0;
 	reb_integrator_ias15_reset(r);
 	reb_integrator_mercurius_reset(r);
 	reb_integrator_leapfrog_reset(r);
 	reb_integrator_sei_reset(r);
 	reb_integrator_whfast_reset(r);
+	reb_integrator_saba_reset(r);
 	reb_integrator_janus_reset(r);
 }
 
 void reb_update_acceleration(struct reb_simulation* r){
 	// This should probably go elsewhere
 	PROFILING_STOP(PROFILING_CAT_INTEGRATOR)
 	PROFILING_START()
```

### Comparing `rebound-3.8.3/src/tools.c` & `rebound-3.9.0/src/tools.c`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/gravity.h` & `rebound-3.9.0/src/gravity.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/rebound.h` & `rebound-3.9.0/src/rebound.h`

 * *Files 2% similar despite different names*

```diff
@@ -292,29 +292,87 @@
     double tandt;       ///< Cached tan() 
     double sindtz;      ///< Cached sin(), z axis
     double tandtz;      ///< Cached tan(), z axis
     /** @endcond */
 };
 
 /**
+ * @brief This structure contains variables used by the SABA integrator.
+ */
+struct reb_simulation_integrator_saba {
+    /**
+     * @brief Number of evaluations of the interaction step.
+     * @details
+     * - 1: standard WH 
+     * - 2: SABA2/SABAC2 
+     * - 3: SABA3/SABAC3 
+     * - 4: SABA4/SABAC4 
+     */
+    unsigned int k;
+    /**
+     * @brief Turn corrector on/off.
+     * @details
+     * - 0: corrector off
+     * - 1: normal (modified kick) corrector on
+     * - 2: lazy implementer's corrector on
+     */
+    enum {
+        REB_SABA_CORRECTOR_NONE = 0,
+        REB_SABA_CORRECTOR_MODIFIEDKICK = 1,
+        REB_SABA_CORRECTOR_LAZY = 2,
+    } corrector;
+
+    /**
+     * @brief safe_mode has the same functionality as in WHFast.
+     */
+    unsigned int safe_mode;
+    unsigned int is_synchronized;
+};
+
+/**
  * @brief This structure contains variables used by the WHFast integrator.
  */
 struct reb_simulation_integrator_whfast {
     /**
-     * @brief This variable turns on/off different symplectic correctors for WHFast. See Rein & Tamayo 2015 and Wisdom 2006 for a discussion.
-     * @details 
-     * - 0 (default): turns off all correctors
-     * - 3: uses third order (two-stage) corrector 
-     * - 5: uses fifth order (four-stage) corrector 
-     * - 7: uses seventh order (six-stage) corrector 
-     * - 11: uses eleventh order (ten-stage) corrector 
+     * @brief This variable turns on/off different first symplectic correctors for WHFast.
+     * @details These correctors remove terms of order O(eps*dt^2) 
+     * - 0 (default): turns off all first correctors
+     * - 3: uses third order (two-stage) first corrector 
+     * - 5: uses fifth order (four-stage) first corrector 
+     * - 7: uses seventh order (six-stage) first corrector 
+     * - 11: uses eleventh order (ten-stage) first corrector 
+     * - 17: uses 17th order (16-stage) first corrector 
      */
     unsigned int corrector;
     
     /**
+     * @brief This variable turns on/off the second symplectic correctors for WHFast.
+     * @details 
+     * - 0 (default): turns off second correctors
+     * - 1: uses second corrector 
+     */
+    unsigned int corrector2;
+    
+    /**
+     * @brief This variable determines the kernel of the WHFast integrator.
+     * @details 
+     * - 0 (default): Uses a standard WH kick step 
+     * - 1: uses the exact modified kick (for Newtonian gravity) 
+     * - 2: uses the composition kernel  
+     * - 3: uses the lazy implementer's modified kick   
+     */
+    enum {
+        REB_WHFAST_KERNEL_DEFAULT = 0,
+        REB_WHFAST_KERNEL_MODIFIEDKICK = 1,
+        REB_WHFAST_KERNEL_COMPOSITION = 2,
+        REB_WHFAST_KERNEL_LAZY = 3,
+    }kernel;
+    
+    
+    /**
      * @brief Chooses the coordinate system for the WHFast algorithm. Default is Jacobi Coordinates.
      */
     enum {
         REB_WHFAST_COORDINATES_JACOBI = 0,                      ///< Jacobi coordinates (default)
         REB_WHFAST_COORDINATES_DEMOCRATICHELIOCENTRIC = 1,      ///< Democratic Heliocentric coordinates
         REB_WHFAST_COORDINATES_WHDS = 2,                        ///< WHDS coordinates (Hernandez and Dehnen, 2017)
         } coordinates;
@@ -347,28 +405,34 @@
      * coordinates of all particles.
      * It is automatically filled and updated by WHfast.
      * Access this array with caution.
      */
     struct reb_particle* REBOUND_RESTRICT p_jh;
     
     /**
+     * @brief Internal temporary array used for lazy implementer's kernel method
+     */
+    struct reb_particle* REBOUND_RESTRICT p_temp;
+    
+    /**
      * @brief Generate inertial coordinates at the end of the integration, but do not change the Jacobi/heliocentric coordinates
      * @details Danger zone! Only use this flag if you are absolutely sure
      * what you are doing. This is intended for
      * simulation which have to be reproducible on a bit by bit basis.
      */
     unsigned int keep_unsynchronized;
 
     /**
      * @cond PRIVATE
      * Internal data structures below. Nothing to be changed by the user.
      */
 
     unsigned int is_synchronized;   ///< Flag to determine if current particle structure is synchronized
-    unsigned int allocated_N;   ///< Space allocated in arrays
+    unsigned int allocated_N;       ///< Space allocated in p_jh array
+    unsigned int allocated_Ntemp;   ///< Space allocated in p_temp array
     unsigned int timestep_warning;  ///< Counter of timestep warnings
     unsigned int recalculate_coordinates_but_not_synchronized_warning;   ///< Counter of Jacobi synchronization errors
     /**
      * @endcond
      */
 };
 
@@ -597,14 +661,21 @@
     REB_BINARY_FIELD_TYPE_PYTHON_UNIT_M = 131,
     REB_BINARY_FIELD_TYPE_PYTHON_UNIT_T = 132,
     REB_BINARY_FIELD_TYPE_MERCURIUS_COMPOS = 133,
     REB_BINARY_FIELD_TYPE_MERCURIUS_COMVEL = 134,
     REB_BINARY_FIELD_TYPE_SAAUTOSTEP = 135,
     REB_BINARY_FIELD_TYPE_SANEXTSTEP = 136,
     REB_BINARY_FIELD_TYPE_STEPSDONE = 137,
+    REB_BINARY_FIELD_TYPE_SABA_K = 138,
+    REB_BINARY_FIELD_TYPE_SABA_CORRECTOR = 139,
+    REB_BINARY_FIELD_TYPE_SABA_SAFEMODE = 140,
+    REB_BINARY_FIELD_TYPE_SABA_ISSYNCHRON = 141,
+    REB_BINARY_FIELD_TYPE_WHFAST_CORRECTOR2 = 143,
+    REB_BINARY_FIELD_TYPE_WHFAST_KERNEL = 144,
+    REB_BINARY_FIELD_TYPE_DTLASTDONE = 145,
     REB_BINARY_FIELD_TYPE_HEADER = 1329743186,  // Corresponds to REBO (first characters of header text)
     REB_BINARY_FIELD_TYPE_SABLOB = 9998,        // SA Blob
     REB_BINARY_FIELD_TYPE_END = 9999,
 };
 
 /**
  * @brief This structure is used to save and load binary files.
@@ -856,14 +927,15 @@
         REB_INTEGRATOR_WHFAST = 1,   ///< WHFast integrator, symplectic, 2nd order, up to 11th order correctors
         REB_INTEGRATOR_SEI = 2,      ///< SEI integrator for shearing sheet simulations, symplectic, needs OMEGA variable
         REB_INTEGRATOR_LEAPFROG = 4, ///< LEAPFROG integrator, simple, 2nd order, symplectic
         // REB_INTEGRATOR_HERMES = 5,   ///< HERMES Integrator, not available anymore. Use MERCURIUS instead.
         REB_INTEGRATOR_NONE = 7,     ///< Do not integrate anything
         REB_INTEGRATOR_JANUS = 8,    ///< Bit-wise reversible JANUS integrator.
         REB_INTEGRATOR_MERCURIUS = 9,///< MERCURIUS integrator 
+        REB_INTEGRATOR_SABA = 10,    ///< SABA integrator family (Laskar and Robutel 2001)
         } integrator;
 
     /**
      * @brief Available boundary conditions
      */
     enum {
         REB_BOUNDARY_NONE = 0,      ///< Do not check for anything (default)
@@ -877,24 +949,26 @@
      */
     enum {
         REB_GRAVITY_NONE = 0,       ///< Do not calculate graviational forces
         REB_GRAVITY_BASIC = 1,      ///< Basic O(N^2) direct summation algorithm, choose this for shearing sheet and periodic boundary conditions
         REB_GRAVITY_COMPENSATED = 2,    ///< Direct summation algorithm O(N^2) but with compensated summation, slightly slower than BASIC but more accurate
         REB_GRAVITY_TREE = 3,       ///< Use the tree to calculate gravity, O(N log(N)), set opening_angle2 to adjust accuracy.
         REB_GRAVITY_MERCURIUS = 4,  ///< Special gravity routine only for MERCURIUS
+        REB_GRAVITY_JACOBI = 5,     ///< Special gravity routine which includes the Jacobi terms for WH integrators 
         } gravity;
     /** @} */
 
 
     /**
      * \name Integrator structs (the contain integrator specific variables and temporary data structures) 
      * @{
      */
     struct reb_simulation_integrator_sei ri_sei;        ///< The SEI struct 
     struct reb_simulation_integrator_whfast ri_whfast;  ///< The WHFast struct 
+    struct reb_simulation_integrator_saba ri_saba;      ///< The SABA struct 
     struct reb_simulation_integrator_ias15 ri_ias15;    ///< The IAS15 struct
     struct reb_simulation_integrator_mercurius ri_mercurius;      ///< The MERCURIUS struct
     struct reb_simulation_integrator_janus ri_janus;    ///< The JANUS struct 
     /** @} */
 
     /**
      * \name Callback functions
@@ -972,14 +1046,24 @@
  * @details All simulation data, including all particle data will be copied. Function pointers
  * need to be set manually afterwards. 
  * Working on the copy will not affect the original simulation.
  */
 struct reb_simulation* reb_copy_simulation(struct reb_simulation* r);
 
 /**
+ * @brief Compares to REBOUND simulations bit by bit.
+ * @return If r1 and r2 are exactly equal to each other then 0 is returned, otherwise 1. The walltime parameter in 
+ * the REBOUND struct is ignored in this comparison.
+ * @param r1 The first REBOUND simulation to be compared.
+ * @param r2 The second REBOUND simulation to be compared.
+ * @param output_option Is set to 1, then the output is printed on the screen. If set to 2, only the return value indicates if the simulations are different. 
+ */
+int reb_diff_simulations(struct reb_simulation* r1, struct reb_simulation* r2, int output_option);
+
+/**
  * @brief Initialize reb_simulation structure.
  *
  * @details Same as reb_create_simulation() but does not allocate memory for structure itself.
  * @param r Structure to be initialized (needs to be allocated externally).
  */
 void reb_init_simulation(struct reb_simulation* r);
 
@@ -1342,17 +1426,31 @@
  * @details This function can be used to save the current status of a REBOUND simualtion 
  * and later restart the simualtion.
  * @param r The rebound simulation to be considered
  * @param filename Output filename.
  */
 void reb_output_binary(struct reb_simulation* r, const char* filename);
 
+/**
+ * @brief This function compares two REBOUND simulations and records the difference in a buffer.
+ * @details This is used for taking a SimulationArchive Snapshot.
+ * @param buf1 The buffer corresponding to the first rebound simulation to be compared
+ * @param buf2 The buffer corresponding to the second rebound simulation to be compared
+ * @param bufp The buffer which will contain the differences. 
+ */
 void reb_binary_diff(char* buf1, size_t size1, char* buf2, size_t size2, char** bufp, size_t* sizep);
 
 /**
+ * @brief Same as reb_binary_diff but with more options.
+ * @param output_option If set to 0, the differences are written to bufp. If set to 1, printed on the screen. If set to 2, then only the return value indicates any differences.
+ * @return 0 is returned if the simulations do not differ (are equal). 1 is return if they differ.
+ */
+int reb_binary_diff_with_options(char* buf1, size_t size1, char* buf2, size_t size2, char** bufp, size_t* sizep, int output_option);
+
+/**
  * @brief Append the positions and velocities of all particles to an ASCII file.
  * @param r The rebound simulation to be considered
  * @param filename Output filename.
  */
 void reb_output_ascii(struct reb_simulation* r, char* filename);
 
 /**
```

### Comparing `rebound-3.8.3/src/particle.c` & `rebound-3.9.0/src/particle.c`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/integrator_whfast.h` & `rebound-3.9.0/src/integrator_janus.h`

 * *Files 13% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 /**
- * @file 	integrator_whfast.h
+ * @file 	integrator_janus.h
  * @brief 	Interface for numerical particle integrator
  * @author 	Hanno Rein <hanno@hanno-rein.de>
  * 
  * @section 	LICENSE
- * Copyright (c) 2015 Hanno Rein, Daniel Tamayo
+ * Copyright (c) 2017 Hanno Rein, Daniel Tamayo
  *
  * This file is part of rebound.
  *
  * rebound is free software: you can redistribute it and/or modify
  * it under the terms of the GNU General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
@@ -18,19 +18,15 @@
  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  * GNU General Public License for more details.
  *
  * You should have received a copy of the GNU General Public License
  * along with rebound.  If not, see <http://www.gnu.org/licenses/>.
  *
  */
-#ifndef _INTEGRATOR_WHFAST_H
-#define _INTEGRATOR_WHFAST_H
+#ifndef _INTEGRATOR_JANUS_H
+#define _INTEGRATOR_JANUS_H
+void reb_integrator_janus_part1(struct reb_simulation* r);		///< Internal function used to call a specific integrator
+void reb_integrator_janus_part2(struct reb_simulation* r);		///< Internal function used to call a specific integrator
+void reb_integrator_janus_synchronize(struct reb_simulation* r);	///< Internal function used to call a specific integrator
+void reb_integrator_janus_reset(struct reb_simulation* r);		///< Internal function used to call a specific integrator
 
-#include "rebound.h"
-
-void reb_integrator_whfast_part1(struct reb_simulation* r);		///< Internal function used to call a specific integrator
-void reb_integrator_whfast_part2(struct reb_simulation* r);		///< Internal function used to call a specific integrator
-void reb_integrator_whfast_synchronize(struct reb_simulation* r);	///< Internal function used to call a specific integrator
-void reb_whfast_kepler_solver(const struct reb_simulation* const r, struct reb_particle* const restrict p_j, const double M, unsigned int i, double _dt);   ///< Internal function (Main WHFast Kepler Solver)
-
-void reb_whfast_apply_corrector(struct reb_simulation* r, double inv, int order, void (*corrector_Z)(struct reb_simulation*, const double, const double)); ///< Internal function to apply correctors according to Wisdom (2006). 
 #endif
```

### Comparing `rebound-3.8.3/src/boundary.h` & `rebound-3.9.0/src/boundary.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/transformations.h` & `rebound-3.9.0/src/transformations.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/binarydiff.h` & `rebound-3.9.0/src/binarydiff.h`

 * *Files 0% similar despite different names*

```diff
@@ -21,8 +21,9 @@
  * You should have received a copy of the GNU General Public License
  * along with rebound.  If not, see <http://www.gnu.org/licenses/>.
  *
  */
 #ifndef _BINARYDIFF_H
 #define _BINARYDIFF_H
 
+
 #endif // _BINARYDIFF_H
```

### Comparing `rebound-3.8.3/src/collision.h` & `rebound-3.9.0/src/collision.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/integrator_janus.h` & `rebound-3.9.0/src/integrator_whfast.h`

 * *Files 18% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 /**
- * @file 	integrator_janus.h
+ * @file 	integrator_whfast.h
  * @brief 	Interface for numerical particle integrator
  * @author 	Hanno Rein <hanno@hanno-rein.de>
  * 
  * @section 	LICENSE
- * Copyright (c) 2017 Hanno Rein, Daniel Tamayo
+ * Copyright (c) 2015 Hanno Rein, Daniel Tamayo
  *
  * This file is part of rebound.
  *
  * rebound is free software: you can redistribute it and/or modify
  * it under the terms of the GNU General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
@@ -18,15 +18,19 @@
  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  * GNU General Public License for more details.
  *
  * You should have received a copy of the GNU General Public License
  * along with rebound.  If not, see <http://www.gnu.org/licenses/>.
  *
  */
-#ifndef _INTEGRATOR_JANUS_H
-#define _INTEGRATOR_JANUS_H
-void reb_integrator_janus_part1(struct reb_simulation* r);		///< Internal function used to call a specific integrator
-void reb_integrator_janus_part2(struct reb_simulation* r);		///< Internal function used to call a specific integrator
-void reb_integrator_janus_synchronize(struct reb_simulation* r);	///< Internal function used to call a specific integrator
-void reb_integrator_janus_reset(struct reb_simulation* r);		///< Internal function used to call a specific integrator
+#ifndef _INTEGRATOR_WHFAST_H
+#define _INTEGRATOR_WHFAST_H
+
+#include "rebound.h"
+
+void reb_integrator_whfast_part1(struct reb_simulation* r);		///< Internal function used to call a specific integrator
+void reb_integrator_whfast_part2(struct reb_simulation* r);		///< Internal function used to call a specific integrator
+void reb_integrator_whfast_synchronize(struct reb_simulation* r);	///< Internal function used to call a specific integrator
+void reb_whfast_kepler_solver(const struct reb_simulation* const r, struct reb_particle* const restrict p_j, const double M, unsigned int i, double _dt);   ///< Internal function (Main WHFast Kepler Solver)
+void reb_whfast_calculate_jerk(struct reb_simulation* r);       ///< Calculates "jerk" term
 
 #endif
```

### Comparing `rebound-3.8.3/src/tree.h` & `rebound-3.9.0/src/tree.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/output.h` & `rebound-3.9.0/src/output.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/integrator_leapfrog.h` & `rebound-3.9.0/src/integrator_leapfrog.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/derivatives.h` & `rebound-3.9.0/src/derivatives.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/input.c` & `rebound-3.9.0/src/input.c`

 * *Files 2% similar despite different names*

```diff
@@ -165,14 +165,15 @@
         return 0; // End of file
     }
     switch (field.type){
         CASE(T,                  &r->t);
         CASE(G,                  &r->G);
         CASE(SOFTENING,          &r->softening);
         CASE(DT,                 &r->dt);
+        CASE(DTLASTDONE,         &r->dt_last_done);
         CASE(N,                  &r->N);
         CASE(NVAR,               &r->N_var);
         CASE(VARCONFIGN,         &r->var_config_N);
         CASE(NACTIVE,            &r->N_active);
         CASE(TESTPARTICLETYPE,   &r->testparticle_type);
         CASE(HASHCTR,            &r->hash_ctr);
         CASE(OPENINGANGLE2,      &r->opening_angle2);
@@ -253,14 +254,20 @@
         CASE(MERCURIUS_COMVEL,   &r->ri_mercurius.com_vel);
         CASE(PYTHON_UNIT_L,      &r->python_unit_l);
         CASE(PYTHON_UNIT_M,      &r->python_unit_m);
         CASE(PYTHON_UNIT_T,      &r->python_unit_t);
         CASE(STEPSDONE,          &r->steps_done);
         CASE(SAAUTOSTEP,         &r->simulationarchive_auto_step);
         CASE(SANEXTSTEP,         &r->simulationarchive_next_step);
+        CASE(SABA_K,             &r->ri_saba.k);
+        CASE(SABA_CORRECTOR,     &r->ri_saba.corrector);
+        CASE(SABA_SAFEMODE,      &r->ri_saba.safe_mode);
+        CASE(SABA_ISSYNCHRON,    &r->ri_saba.is_synchronized);
+        CASE(WHFAST_CORRECTOR2,  &r->ri_whfast.corrector2);
+        CASE(WHFAST_KERNEL,      &r->ri_whfast.kernel);
         case REB_BINARY_FIELD_TYPE_PARTICLES:
             if(r->particles){
                 free(r->particles);
             }
             r->allocatedN = (int)(field.size/sizeof(struct reb_particle));
             if (field.size){
                 r->particles = malloc(field.size);
```

### Comparing `rebound-3.8.3/src/display.h` & `rebound-3.9.0/src/display.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/simulationarchive.h` & `rebound-3.9.0/src/simulationarchive.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/integrator_mercurius.c` & `rebound-3.9.0/src/integrator_mercurius.c`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/rebound.c` & `rebound-3.9.0/src/rebound.c`

 * *Files 2% similar despite different names*

```diff
@@ -32,25 +32,27 @@
 #include <sys/time.h>
 #include <sys/mman.h>
 #include <sys/wait.h>
 #include <pthread.h>
 #include <fcntl.h>
 #include "rebound.h"
 #include "integrator.h"
+#include "integrator_saba.h"
 #include "integrator_whfast.h"
 #include "integrator_ias15.h"
 #include "integrator_mercurius.h"
 #include "boundary.h"
 #include "gravity.h"
 #include "collision.h"
 #include "tree.h"
 #include "output.h"
 #include "tools.h"
 #include "particle.h"
 #include "input.h"
+#include "binarydiff.h"
 #include "simulationarchive.h"
 #ifdef MPI
 #include "communication_mpi.h"
 #endif
 #include "display.h"
 #ifdef OPENMP
 #include <omp.h>
@@ -58,15 +60,15 @@
 #define MAX(a, b) ((a) < (b) ? (b) : (a))       ///< Returns the maximum of a and b
 #define STRINGIFY(s) str(s)
 #define str(s) #s
 
 const int reb_max_messages_length = 1024;   // needs to be constant expression for array size
 const int reb_max_messages_N = 10;
 const char* reb_build_str = __DATE__ " " __TIME__;  // Date and time build string. 
-const char* reb_version_str = "3.8.3";         // **VERSIONLINE** This line gets updated automatically. Do not edit manually.
+const char* reb_version_str = "3.9.0";         // **VERSIONLINE** This line gets updated automatically. Do not edit manually.
 const char* reb_githash_str = STRINGIFY(GITHASH);             // This line gets updated automatically. Do not edit manually.
 
 static int reb_error_message_waiting(struct reb_simulation* const r);
 
 void reb_step(struct reb_simulation* const r){
     // Update walltime
     struct timeval time_beginning;
@@ -332,15 +334,17 @@
     r->messages             = NULL;
     // ********** Lookup Table
     r->particle_lookup_table = NULL;
     r->N_lookup = 0;
     r->allocatedN_lookup = 0;
     // ********** WHFAST
     r->ri_whfast.allocated_N    = 0;
+    r->ri_whfast.allocated_Ntemp= 0;
     r->ri_whfast.p_jh           = NULL;
+    r->ri_whfast.p_temp         = NULL;
     r->ri_whfast.keep_unsynchronized = 0;
     // ********** IAS15
     r->ri_ias15.allocatedN      = 0;
     set_dp7_null(&(r->ri_ias15.g));
     set_dp7_null(&(r->ri_ias15.b));
     set_dp7_null(&(r->ri_ias15.csb));
     set_dp7_null(&(r->ri_ias15.e));
@@ -418,22 +422,46 @@
 
     char* bufp_beginning = bufp; // bufp will be changed
     while(reb_input_field(r_copy, NULL, warnings, &bufp)){ }
     free(bufp_beginning);
     
 }
 
+int reb_diff_simulations(struct reb_simulation* r1, struct reb_simulation* r2, int output_option){
+    if (output_option!=1 && output_option!=2){
+        // Not implemented
+        return -1;
+    }
+    char* bufp1;
+    char* bufp2;
+    size_t sizep1, sizep2;
+    reb_output_binary_to_stream(r1, &bufp1,&sizep1);
+    reb_output_binary_to_stream(r2, &bufp2,&sizep2);
+
+    int ret = reb_binary_diff_with_options(bufp1, sizep1, bufp2, sizep2, NULL, NULL, output_option);
+    
+    free(bufp1);
+    free(bufp2);
+    return ret;
+}
+
 struct reb_simulation* reb_copy_simulation(struct reb_simulation* r){
     struct reb_simulation* r_copy = reb_create_simulation();
     enum reb_input_binary_messages warnings = REB_INPUT_BINARY_WARNING_NONE;
     _reb_copy_simulation_with_messages(r_copy,r,&warnings);
     r = reb_input_process_warnings(r, warnings);
     return r_copy;
 }
 
+void reb_clear_pre_post_pointers(struct reb_simulation* const r){
+    // Temporary fix for REBOUNDx. 
+    r->pre_timestep_modifications  = NULL;
+    r->post_timestep_modifications  = NULL;
+}
+
 void reb_init_simulation(struct reb_simulation* r){
     reb_tools_init_srand();
     reb_reset_temporary_pointers(r);
     reb_reset_function_pointers(r);
     r->t        = 0; 
     r->G        = 1;
     r->softening    = 0;
@@ -502,21 +530,29 @@
 
 
     // Integrators  
     // ********** WHFAST
     // the defaults below are chosen to safeguard the user against spurious results, but
     // will be slower and less accurate
     r->ri_whfast.corrector = 0;
+    r->ri_whfast.corrector2 = 0;
+    r->ri_whfast.kernel = 0;
     r->ri_whfast.coordinates = REB_WHFAST_COORDINATES_JACOBI;
     r->ri_whfast.safe_mode = 1;
     r->ri_whfast.recalculate_coordinates_this_timestep = 0;
     r->ri_whfast.is_synchronized = 1;
     r->ri_whfast.timestep_warning = 0;
     r->ri_whfast.recalculate_coordinates_but_not_synchronized_warning = 0;
     
+    // ********** SABA
+    r->ri_saba.k = 1;
+    r->ri_saba.corrector = 0;
+    r->ri_saba.safe_mode = 1;
+    r->ri_saba.is_synchronized = 1;
+    
     // ********** IAS15
     r->ri_ias15.epsilon         = 1e-9;
     r->ri_ias15.min_dt      = 0;
     r->ri_ias15.epsilon_global  = 1;
     r->ri_ias15.iterations_max_exceeded = 0;    
     
     // ********** SEI
```

### Comparing `rebound-3.8.3/src/particle.h` & `rebound-3.9.0/src/particle.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/gravity.c` & `rebound-3.9.0/src/gravity.c`

 * *Files 11% similar despite different names*

```diff
@@ -66,14 +66,69 @@
 	const unsigned int _gravity_ignore_terms = r->gravity_ignore_terms;
 	const int _N_real   = N  - r->N_var;
 	const int _N_active = ((N_active==-1)?_N_real:N_active);
 	const int _testparticle_type   = r->testparticle_type;
 	switch (r->gravity){
 		case REB_GRAVITY_NONE: // Do nothing.
 		break;
+		case REB_GRAVITY_JACOBI:
+		{
+            double Rjx = 0.;
+            double Rjy = 0.;
+            double Rjz = 0.;
+            double Mj = 0.;
+            for (int j=0; j<N; j++){
+				particles[j].ax = 0; 
+				particles[j].ay = 0; 
+				particles[j].az = 0; 
+                for (int i=0; i<j+1; i++){
+                    if (j>1){
+                        ////////////////
+                        // Jacobi Term
+                        // Note: ignoring j==1 term here and below as they cancel
+                        const double Qjx = particles[j].x - Rjx/Mj; 
+                        const double Qjy = particles[j].y - Rjy/Mj;
+                        const double Qjz = particles[j].z - Rjz/Mj;
+                        const double dr = sqrt(Qjx*Qjx + Qjy*Qjy + Qjz*Qjz);
+                        double dQjdri = Mj; 
+                        if (i<j){
+                            dQjdri = -particles[j].m; //rearranged such that m==0 does not diverge
+                        }
+                        const double prefact = G*dQjdri/(dr*dr*dr);
+                        particles[i].ax    += prefact*Qjx;
+                        particles[i].ay    += prefact*Qjy;
+                        particles[i].az    += prefact*Qjz;
+                    }
+                    if (i!=j && (i!=0 || j!=1)){
+                        ////////////////
+                        // Direct Term
+                        // Note: ignoring i==0 && j==1 term here and above as they cancel 
+                        const double dx = particles[i].x - particles[j].x;
+                        const double dy = particles[i].y - particles[j].y;
+                        const double dz = particles[i].z - particles[j].z;
+                        const double dr = sqrt(dx*dx + dy*dy + dz*dz);
+                        const double prefact = G /(dr*dr*dr);
+                        const double prefacti = prefact*particles[i].m;
+                        const double prefactj = prefact*particles[j].m;
+                        
+                        particles[i].ax    -= prefactj*dx;
+                        particles[i].ay    -= prefactj*dy;
+                        particles[i].az    -= prefactj*dz;
+                        particles[j].ax    += prefacti*dx;
+                        particles[j].ay    += prefacti*dy;
+                        particles[j].az    += prefacti*dz;
+                    }
+                }
+                Rjx += particles[j].m*particles[j].x;
+                Rjy += particles[j].m*particles[j].y;
+                Rjz += particles[j].m*particles[j].z;
+                Mj += particles[j].m;
+            }
+		}
+		break;
 		case REB_GRAVITY_BASIC:
 		{
 			const int nghostx = r->nghostx;
 			const int nghosty = r->nghosty;
 			const int nghostz = r->nghostz;
 #pragma omp parallel for 
 			for (int i=0; i<N; i++){
```

### Comparing `rebound-3.8.3/src/tools.h` & `rebound-3.9.0/src/tools.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/boundary.c` & `rebound-3.9.0/src/boundary.c`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/integrator_ias15.h` & `rebound-3.9.0/src/integrator_ias15.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/integrator.h` & `rebound-3.9.0/src/integrator.h`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/integrator_sei.c` & `rebound-3.9.0/src/integrator_sei.c`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/collision.c` & `rebound-3.9.0/src/collision.c`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/integrator_janus.c` & `rebound-3.9.0/src/integrator_janus.c`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/transformations.c` & `rebound-3.9.0/src/transformations.c`

 * *Files identical despite different names*

### Comparing `rebound-3.8.3/src/binarydiff.c` & `rebound-3.9.0/src/binarydiff.c`

 * *Files 22% similar despite different names*

```diff
@@ -31,24 +31,32 @@
 #include <sys/time.h>
 #include "particle.h"
 #include "rebound.h"
 #include "tools.h"
 #include "output.h"
 #include "binarydiff.h"
 
-
-
+// Wrapper for backwards compatibility
 void reb_binary_diff(char* buf1, size_t size1, char* buf2, size_t size2, char** bufp, size_t* sizep){
+    // Ignores return value
+    reb_binary_diff_with_options(buf1, size1, buf2, size2, bufp, sizep, 0);
+}
+
+int reb_binary_diff_with_options(char* buf1, size_t size1, char* buf2, size_t size2, char** bufp, size_t* sizep, int output_option){
     if (!buf1 || !buf2 || size1<64 || size2<64){
         printf("Cannot read input buffers.\n");
-        return;
+        return 0;
     }
+
+    int are_different = 0;
     
-    *bufp = NULL;
-    *sizep = 0;
+    if (output_option==0){
+        *bufp = NULL;
+        *sizep = 0;
+    }
     size_t allocatedsize = 0;
 
     // Header.
     if(memcmp(buf1,buf2,64)!=0){
         printf("Header in binary files are different.\n");
     }
 
@@ -90,15 +98,25 @@
                 }
             };
             if (notfound == 1){
                 // Output field with size 0
                 pos1 += field1.size; // For next search
                 pos2 = 64; // For next search
                 field1.size = 0;
-                reb_output_stream_write(bufp, &allocatedsize, sizep, &field1,sizeof(struct reb_binary_field));
+                are_different = 1.;
+                switch(output_option){
+                    case 0:
+                        reb_output_stream_write(bufp, &allocatedsize, sizep, &field1,sizeof(struct reb_binary_field));
+                        break;
+                    case 1:
+                        printf("Field %d not in simulation 2.\n",field1.type);
+                        break;
+                    default:
+                        break;
+                }
                 continue;
             }
         }
         // Can assume field1.type == field2.type from here on
         if (pos1+field1.size>size1) printf("Corrupt binary file buf1.\n");
         if (pos2+field2.size>size2) printf("Corrupt binary file buf2.\n");
         int fields_differ = 0;
@@ -106,16 +124,30 @@
             if (memcmp(buf1+pos1,buf2+pos2,field1.size)!=0){
                 fields_differ = 1;
             }
         }else{
             fields_differ = 1;
         }
         if(fields_differ){
-            reb_output_stream_write(bufp, &allocatedsize, sizep, &field2,sizeof(struct reb_binary_field));
-            reb_output_stream_write(bufp, &allocatedsize, sizep, buf2+pos2,field2.size);
+            if (field1.type!=REB_BINARY_FIELD_TYPE_WALLTIME){
+                // Ignore the walltime field for the return value.
+                // Typically we do not care about this field when comparing simulations.
+                are_different = 1.;
+            }
+            switch(output_option){
+                case 0:
+                    reb_output_stream_write(bufp, &allocatedsize, sizep, &field2,sizeof(struct reb_binary_field));
+                    reb_output_stream_write(bufp, &allocatedsize, sizep, buf2+pos2,field2.size);
+                    break;
+                case 1:
+                    printf("Field %d differs.\n",field1.type);
+                    break;
+                default:
+                    break;
+            }
         }
         pos1 += field1.size;
         pos2 += field2.size;
     }
     // Search for fields which are present in buf2 but not in buf1
     pos1 = 64;
     pos2 = 64;
@@ -161,14 +193,24 @@
         if (notfound == 0){
             // Not a new field. Skip.
             pos1 = 64;
             pos2 += field2.size;
             continue;
         }
 
-        reb_output_stream_write(bufp, &allocatedsize, sizep, &field2,sizeof(struct reb_binary_field));
-        reb_output_stream_write(bufp, &allocatedsize, sizep, buf2+pos2,field2.size);
+        are_different = 1.;
+        switch(output_option){
+            case 0:
+                reb_output_stream_write(bufp, &allocatedsize, sizep, &field2,sizeof(struct reb_binary_field));
+                reb_output_stream_write(bufp, &allocatedsize, sizep, buf2+pos2,field2.size);
+                break;
+            case 1:
+                printf("Field %d not in simulation 1.\n",field2.type);
+                break;
+            default:
+                break;
+        }
         pos1 = 64;
         pos2 += field2.size;
     }
-    return;
+    return are_different;
 }
```

### Comparing `rebound-3.8.3/src/output.c` & `rebound-3.9.0/src/output.c`

 * *Files 3% similar despite different names*

```diff
@@ -182,15 +182,16 @@
     char filename_mpi[1024];
     sprintf(filename_mpi,"%s_%d",filename,r->mpi_id);
     FILE* of = fopen(filename_mpi,"a"); 
 #else // MPI
     FILE* of = fopen(filename,"a"); 
 #endif // MPI
     if (of==NULL){
-        reb_exit("Can not open file.");
+        reb_error(r, "Can not open file.");
+        return;
     }
     for (int i=0;i<N;i++){
         struct reb_particle p = r->particles[i];
         fprintf(of,"%e\t%e\t%e\t%e\t%e\t%e\n",p.x,p.y,p.z,p.vx,p.vy,p.vz);
     }
     fclose(of);
 }
@@ -201,15 +202,16 @@
     char filename_mpi[1024];
     sprintf(filename_mpi,"%s_%d",filename,r->mpi_id);
     FILE* of = fopen(filename_mpi,"a"); 
 #else // MPI
     FILE* of = fopen(filename,"a"); 
 #endif // MPI
     if (of==NULL){
-        reb_exit("Can not open file.");
+        reb_error(r, "Can not open file.");
+        return;
     }
     struct reb_particle com = r->particles[0];
     for (int i=1;i<N;i++){
         struct reb_orbit o = reb_tools_particle_to_orbit(r->G, r->particles[i],com);
         fprintf(of,"%e\t%e\t%e\t%e\t%e\t%e\t%e\t%e\t%e\n",r->t,o.a,o.e,o.inc,o.Omega,o.omega,o.l,o.P,o.f);
         com = reb_get_com_of_pair(com,r->particles[i]);
     }
@@ -218,15 +220,15 @@
 
 void static inline reb_save_dp7(struct reb_dp7* dp7, const int N3, char** bufp, size_t* sizep, size_t* allocatedsize){
     reb_output_stream_write(bufp, allocatedsize, sizep, dp7->p0,sizeof(double)*N3);
     reb_output_stream_write(bufp, allocatedsize, sizep, dp7->p1,sizeof(double)*N3);
     reb_output_stream_write(bufp, allocatedsize, sizep, dp7->p2,sizeof(double)*N3);
     reb_output_stream_write(bufp, allocatedsize, sizep, dp7->p3,sizeof(double)*N3);
     reb_output_stream_write(bufp, allocatedsize, sizep, dp7->p4,sizeof(double)*N3);
-    reb_output_stream_write(bufp, allocatedsize, sizep, dp7->p4,sizeof(double)*N3);
+    reb_output_stream_write(bufp, allocatedsize, sizep, dp7->p5,sizeof(double)*N3);
     reb_output_stream_write(bufp, allocatedsize, sizep, dp7->p6,sizeof(double)*N3);
 }
 
 // Macro to write a single field to a binary file.
 // Memset forces padding to be set to 0 (not necessary but
 // helps when comparing binary files)
 #define WRITE_FIELD(typename, value, length) {\
@@ -252,14 +254,15 @@
     snprintf(header+cwritten+1,64-cwritten-1,"%s",reb_githash_str);
     reb_output_stream_write(bufp, &allocatedsize, sizep, header,sizeof(char)*64);
    
     WRITE_FIELD(T,                  &r->t,                              sizeof(double));
     WRITE_FIELD(G,                  &r->G,                              sizeof(double));
     WRITE_FIELD(SOFTENING,          &r->softening,                      sizeof(double));
     WRITE_FIELD(DT,                 &r->dt,                             sizeof(double));
+    WRITE_FIELD(DTLASTDONE,         &r->dt_last_done,                   sizeof(double));
     WRITE_FIELD(N,                  &r->N,                              sizeof(int));
     WRITE_FIELD(NVAR,               &r->N_var,                          sizeof(int));
     WRITE_FIELD(VARCONFIGN,         &r->var_config_N,                   sizeof(int));
     WRITE_FIELD(NACTIVE,            &r->N_active,                       sizeof(int));
     WRITE_FIELD(TESTPARTICLETYPE,   &r->testparticle_type,              sizeof(int));
     WRITE_FIELD(HASHCTR,            &r->hash_ctr,                       sizeof(int));
     WRITE_FIELD(OPENINGANGLE2,      &r->opening_angle2,                 sizeof(double));
@@ -342,14 +345,20 @@
     WRITE_FIELD(MERCURIUS_COMVEL,   &(r->ri_mercurius.com_vel),         sizeof(struct reb_vec3d));
     WRITE_FIELD(PYTHON_UNIT_L,      &r->python_unit_l,                  sizeof(uint32_t));
     WRITE_FIELD(PYTHON_UNIT_M,      &r->python_unit_m,                  sizeof(uint32_t));
     WRITE_FIELD(PYTHON_UNIT_T,      &r->python_unit_t,                  sizeof(uint32_t));
     WRITE_FIELD(STEPSDONE,          &r->steps_done,                     sizeof(unsigned long long));
     WRITE_FIELD(SAAUTOSTEP,         &r->simulationarchive_auto_step,    sizeof(unsigned long long));
     WRITE_FIELD(SANEXTSTEP,         &r->simulationarchive_next_step,    sizeof(unsigned long long));
+    WRITE_FIELD(SABA_K,             &r->ri_saba.k,                      sizeof(unsigned int));
+    WRITE_FIELD(SABA_CORRECTOR,     &r->ri_saba.corrector,              sizeof(unsigned int));
+    WRITE_FIELD(SABA_SAFEMODE,      &r->ri_saba.safe_mode,              sizeof(unsigned int));
+    WRITE_FIELD(SABA_ISSYNCHRON,    &r->ri_saba.is_synchronized,        sizeof(unsigned int));
+    WRITE_FIELD(WHFAST_CORRECTOR2,  &r->ri_whfast.corrector2,           sizeof(unsigned int));
+    WRITE_FIELD(WHFAST_KERNEL,      &r->ri_whfast.kernel,               sizeof(unsigned int));
     int functionpointersused = 0;
     if (r->coefficient_of_restitution ||
         r->collision_resolve ||
         r->additional_forces ||
         r->heartbeat ||
         r->post_timestep_modifications ||
         r->free_particle_ap){
@@ -428,15 +437,16 @@
     char filename_mpi[1024];
     sprintf(filename_mpi,"%s_%d",filename,r->mpi_id);
     FILE* of = fopen(filename_mpi,"wb"); 
 #else // MPI
     FILE* of = fopen(filename,"wb"); 
 #endif // MPI
     if (of==NULL){
-        reb_exit("Can not open file.");
+        reb_error(r, "Can not open file.");
+        return;
     }
     char* bufp;
     size_t sizep;
     reb_output_binary_to_stream(r, &bufp,&sizep);
     fwrite(bufp,sizep,1,of);
     free(bufp);
     fclose(of);
@@ -448,15 +458,16 @@
     char filename_mpi[1024];
     sprintf(filename_mpi,"%s_%d",filename,r->mpi_id);
     FILE* of = fopen(filename_mpi,"wb"); 
 #else // MPI
     FILE* of = fopen(filename,"wb"); 
 #endif // MPI
     if (of==NULL){
-        reb_exit("Can not open file.");
+        reb_error(r, "Can not open file.");
+        return;
     }
     for (int i=0;i<N;i++){
         struct reb_vec3d v;
         v.x = r->particles[i].x;
         v.y = r->particles[i].y;
         v.z = r->particles[i].z;
         fwrite(&(v),sizeof(struct reb_vec3d),1,of);
@@ -501,14 +512,15 @@
     struct reb_vec3d Q_tot = Q;
 #endif
     Q_tot.x = sqrt(Q_tot.x/(double)N_tot);
     Q_tot.y = sqrt(Q_tot.y/(double)N_tot);
     Q_tot.z = sqrt(Q_tot.z/(double)N_tot);
     FILE* of = fopen(filename,"a"); 
     if (of==NULL){
-        reb_exit("Can not open file.");
+        reb_error(r, "Can not open file.");
+        return;
     }
     fprintf(of,"%e\t%e\t%e\t%e\t%e\t%e\t%e\n",r->t,A_tot.x,A_tot.y,A_tot.z,Q_tot.x,Q_tot.y,Q_tot.z);
     fclose(of);
 }
```

### Comparing `rebound-3.8.3/src/tree.c` & `rebound-3.9.0/src/tree.c`

 * *Files identical despite different names*

