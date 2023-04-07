# Comparing `tmp/doped-1.0.8.tar.gz` & `tmp/doped-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "doped-1.0.8.tar", last modified: Wed Apr  5 23:53:33 2023, max compression
+gzip compressed data, was "doped-1.0.9.tar", last modified: Fri Apr  7 11:48:49 2023, max compression
```

## Comparing `doped-1.0.8.tar` & `doped-1.0.9.tar`

### file list

```diff
@@ -1,65 +1,65 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:53:33.349484 doped-1.0.8/
--rw-r--r--   0 runner    (1001) docker     (123)     1071 2023-04-05 23:38:09.000000 doped-1.0.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     8118 2023-04-05 23:53:33.349484 doped-1.0.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     6001 2023-04-05 23:38:09.000000 doped-1.0.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:53:33.341484 doped-1.0.8/doped/
--rw-r--r--   0 runner    (1001) docker     (123)      578 2023-04-05 23:38:09.000000 doped-1.0.8/doped/DefectSet.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      382 2023-04-05 23:38:09.000000 doped-1.0.8/doped/HSE06_RelaxSet.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      283 2023-04-05 23:38:09.000000 doped-1.0.8/doped/PBEsol_ConvergenceSet.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      920 2023-04-05 23:38:09.000000 doped-1.0.8/doped/PotcarSet.yaml
--rwxr-xr-x   0 runner    (1001) docker     (123)     2173 2023-04-05 23:38:09.000000 doped-1.0.8/doped/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7301 2023-04-05 23:38:09.000000 doped-1.0.8/doped/aide_murphy_correction.py
--rw-r--r--   0 runner    (1001) docker     (123)    15761 2023-04-05 23:38:09.000000 doped-1.0.8/doped/analysis.py
--rw-r--r--   0 runner    (1001) docker     (123)    69502 2023-04-05 23:38:09.000000 doped-1.0.8/doped/chemical_potentials.py
--rw-r--r--   0 runner    (1001) docker     (123)    35333 2023-04-05 23:38:09.000000 doped-1.0.8/doped/plotting.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:53:33.341484 doped-1.0.8/doped/pycdt/
--rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:53:33.345484 doped-1.0.8/doped/pycdt/core/
--rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/core/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    46022 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/core/_chemical_potentials.py
--rw-r--r--   0 runner    (1001) docker     (123)    24607 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/core/defects_analyzer.py
--rw-r--r--   0 runner    (1001) docker     (123)    43509 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/core/defectsmaker.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:53:33.345484 doped-1.0.8/doped/pycdt/core/tests/
--rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/core/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16095 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/core/tests/test_chemical_potentials.py
--rw-r--r--   0 runner    (1001) docker     (123)     9986 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/core/tests/test_defects_analyzer.py
--rw-r--r--   0 runner    (1001) docker     (123)    10237 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/core/tests/test_defectsmaker.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:53:33.345484 doped-1.0.8/doped/pycdt/corrections/
--rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/corrections/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13023 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/corrections/finite_size_charge_correction.py
--rw-r--r--   0 runner    (1001) docker     (123)    11084 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/corrections/freysoldt_plotter.py
--rw-r--r--   0 runner    (1001) docker     (123)     4843 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/corrections/ldau_correction.py
--rw-r--r--   0 runner    (1001) docker     (123)    19546 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/corrections/sxdefect_correction.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:53:33.345484 doped-1.0.8/doped/pycdt/corrections/tests/
--rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/corrections/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4610 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/corrections/tests/test_finite_size_charge_correction.py
--rw-r--r--   0 runner    (1001) docker     (123)     1230 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/corrections/tests/test_ldau_correction.py
--rw-r--r--   0 runner    (1001) docker     (123)     2376 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/corrections/tests/test_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     6598 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/corrections/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:53:33.345484 doped-1.0.8/doped/pycdt/utils/
--rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      542 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/utils/log_util.py
--rw-r--r--   0 runner    (1001) docker     (123)    64754 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/utils/parse_calculations.py
--rw-r--r--   0 runner    (1001) docker     (123)    10496 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/utils/plotter.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:53:33.345484 doped-1.0.8/doped/pycdt/utils/tests/
--rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/utils/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      737 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/utils/tests/test_log_util.py
--rw-r--r--   0 runner    (1001) docker     (123)    14406 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/utils/tests/test_parse_calculations.py
--rw-r--r--   0 runner    (1001) docker     (123)     1836 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/utils/tests/test_plotter.py
--rw-r--r--   0 runner    (1001) docker     (123)      466 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/utils/tests/test_units.py
--rw-r--r--   0 runner    (1001) docker     (123)     7653 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/utils/tests/test_vasp.py
--rw-r--r--   0 runner    (1001) docker     (123)     1274 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/utils/units.py
--rw-r--r--   0 runner    (1001) docker     (123)    22709 2023-04-05 23:38:09.000000 doped-1.0.8/doped/pycdt/utils/vasp.py
--rw-r--r--   0 runner    (1001) docker     (123)    40678 2023-04-05 23:38:09.000000 doped-1.0.8/doped/vasp_input.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:53:33.341484 doped-1.0.8/doped.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     8118 2023-04-05 23:53:33.000000 doped-1.0.8/doped.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1740 2023-04-05 23:53:33.000000 doped-1.0.8/doped.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-05 23:53:33.000000 doped-1.0.8/doped.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       94 2023-04-05 23:53:33.000000 doped-1.0.8/doped.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-05 23:53:33.000000 doped-1.0.8/doped.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1139 2023-04-05 23:38:11.000000 doped-1.0.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-05 23:53:33.349484 doped-1.0.8/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 23:53:33.349484 doped-1.0.8/tests/
--rwxr-xr-x   0 runner    (1001) docker     (123)    25523 2023-04-05 23:38:11.000000 doped-1.0.8/tests/test_chemical_potentials.py
--rw-r--r--   0 runner    (1001) docker     (123)    22093 2023-04-05 23:38:11.000000 doped-1.0.8/tests/test_parse_calculations.py
--rw-r--r--   0 runner    (1001) docker     (123)    13530 2023-04-05 23:38:11.000000 doped-1.0.8/tests/test_vasp_input.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:48:49.756421 doped-1.0.9/
+-rw-r--r--   0 runner    (1001) docker     (123)     1071 2023-04-07 11:34:11.000000 doped-1.0.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     8118 2023-04-07 11:48:49.756421 doped-1.0.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     6001 2023-04-07 11:34:11.000000 doped-1.0.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:48:49.752421 doped-1.0.9/doped/
+-rw-r--r--   0 runner    (1001) docker     (123)      578 2023-04-07 11:34:11.000000 doped-1.0.9/doped/DefectSet.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      382 2023-04-07 11:34:11.000000 doped-1.0.9/doped/HSE06_RelaxSet.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      283 2023-04-07 11:34:11.000000 doped-1.0.9/doped/PBEsol_ConvergenceSet.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      920 2023-04-07 11:34:11.000000 doped-1.0.9/doped/PotcarSet.yaml
+-rwxr-xr-x   0 runner    (1001) docker     (123)     2173 2023-04-07 11:34:11.000000 doped-1.0.9/doped/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7301 2023-04-07 11:34:11.000000 doped-1.0.9/doped/aide_murphy_correction.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15733 2023-04-07 11:34:11.000000 doped-1.0.9/doped/analysis.py
+-rw-r--r--   0 runner    (1001) docker     (123)    69785 2023-04-07 11:34:11.000000 doped-1.0.9/doped/chemical_potentials.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35319 2023-04-07 11:34:11.000000 doped-1.0.9/doped/plotting.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:48:49.752421 doped-1.0.9/doped/pycdt/
+-rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:48:49.752421 doped-1.0.9/doped/pycdt/core/
+-rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/core/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    46022 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/core/_chemical_potentials.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24607 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/core/defects_analyzer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    43509 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/core/defectsmaker.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:48:49.756421 doped-1.0.9/doped/pycdt/core/tests/
+-rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/core/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16095 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/core/tests/test_chemical_potentials.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9986 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/core/tests/test_defects_analyzer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10237 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/core/tests/test_defectsmaker.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:48:49.756421 doped-1.0.9/doped/pycdt/corrections/
+-rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/corrections/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13023 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/corrections/finite_size_charge_correction.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11084 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/corrections/freysoldt_plotter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4843 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/corrections/ldau_correction.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19546 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/corrections/sxdefect_correction.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:48:49.756421 doped-1.0.9/doped/pycdt/corrections/tests/
+-rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/corrections/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4610 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/corrections/tests/test_finite_size_charge_correction.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1230 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/corrections/tests/test_ldau_correction.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2376 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/corrections/tests/test_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6598 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/corrections/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:48:49.756421 doped-1.0.9/doped/pycdt/utils/
+-rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      542 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/utils/log_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)    65571 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/utils/parse_calculations.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10496 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/utils/plotter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:48:49.756421 doped-1.0.9/doped/pycdt/utils/tests/
+-rwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/utils/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      737 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/utils/tests/test_log_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14406 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/utils/tests/test_parse_calculations.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1836 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/utils/tests/test_plotter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      466 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/utils/tests/test_units.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7653 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/utils/tests/test_vasp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1274 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/utils/units.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22709 2023-04-07 11:34:11.000000 doped-1.0.9/doped/pycdt/utils/vasp.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40678 2023-04-07 11:34:11.000000 doped-1.0.9/doped/vasp_input.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:48:49.752421 doped-1.0.9/doped.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     8118 2023-04-07 11:48:49.000000 doped-1.0.9/doped.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1740 2023-04-07 11:48:49.000000 doped-1.0.9/doped.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 11:48:49.000000 doped-1.0.9/doped.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       94 2023-04-07 11:48:49.000000 doped-1.0.9/doped.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-07 11:48:49.000000 doped-1.0.9/doped.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1139 2023-04-07 11:34:13.000000 doped-1.0.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 11:48:49.756421 doped-1.0.9/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:48:49.756421 doped-1.0.9/tests/
+-rwxr-xr-x   0 runner    (1001) docker     (123)    25523 2023-04-07 11:34:13.000000 doped-1.0.9/tests/test_chemical_potentials.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22093 2023-04-07 11:34:13.000000 doped-1.0.9/tests/test_parse_calculations.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13530 2023-04-07 11:34:13.000000 doped-1.0.9/tests/test_vasp_input.py
```

### Comparing `doped-1.0.8/LICENSE` & `doped-1.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/PKG-INFO` & `doped-1.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: doped
-Version: 1.0.8
+Version: 1.0.9
 Summary: Python package to setup, process and analyse solid-state defect calculations with VASP
 Author-email: Seán Kavanagh <sean.kavanagh.19@ucl.ac.uk>
 License: MIT License
         
         Copyright (c) 2021 Seán Kavanagh
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
```

### Comparing `doped-1.0.8/README.md` & `doped-1.0.9/README.md`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/DefectSet.yaml` & `doped-1.0.9/doped/DefectSet.yaml`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/PotcarSet.yaml` & `doped-1.0.9/doped/PotcarSet.yaml`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/__init__.py` & `doped-1.0.9/doped/__init__.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/aide_murphy_correction.py` & `doped-1.0.9/doped/aide_murphy_correction.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/analysis.py` & `doped-1.0.9/doped/analysis.py`

 * *Files 2% similar despite different names*

```diff
@@ -19,15 +19,15 @@
 
 
 def bold_print(string: str) -> None:
     """Does what it says on the tin. Prints the input string in bold."""
     print("\033[1m" + string + "\033[0m")
 
 
-def dpd_from_parsed_defect_dict(parsed_defect_dict: dict) -> DefectPhaseDiagram:
+def dpd_from_defect_dict(parsed_defect_dict: dict) -> DefectPhaseDiagram:
     """Generates a DefectPhaseDiagram object from a dictionary of parsed defect calculations (
     format: {"defect_name": defect_entry}), likely created using SingleDefectParser from
     doped.pycdt.utils.parse_calculations), which can then be used to analyse and plot the defect
     thermodynamics (formation energies, transition levels, concentrations etc)
 
     Args:
         parsed_defect_dict (dict):
@@ -70,15 +70,15 @@
 def dpd_transition_levels(defect_phase_diagram: DefectPhaseDiagram):
     """Iteratively prints the charge transition levels for the input DefectPhaseDiagram object
     (via the from a defect_phase_diagram.transition_level_map attribute)
 
     Args:
         defect_phase_diagram (DefectPhaseDiagram):
             DefectPhaseDiagram object (likely created from
-            analysis.dpd_from_parsed_defect_dict)
+            analysis.dpd_from_defect_dict)
 
     Returns:
         None
     """
     for def_type, tl_info in defect_phase_diagram.transition_level_map.items():
         bold_print(f"\nDefect: {def_type.split('@')[0]}")
         for tl_efermi, chargeset in tl_info.items():
@@ -108,15 +108,15 @@
     pd_facets argument, or if not specified, will print formation energy tables for each facet in
     the phase diagram.
     Returns the results a pandas DataFrame or list of DataFrames.
 
     Args:
         defect_phase_diagram (DefectPhaseDiagram):
              DefectPhaseDiagram object (likely created from
-             analysis.dpd_from_parsed_defect_dict)
+             analysis.dpd_from_defect_dict)
         chempot_limits (dict):
             This can either be a dictionary of chosen absolute/DFT chemical potentials: {Elt:
             Energy} (giving a single formation energy table) or a dictionary including the
             key-value pair: {"facets": [{'facet': [chempot_dict]}]}, following the format generated
             by chempot_limits = cpa.read_phase_diagram_and_chempots() (see example notebooks). If
             not specified, chemical potentials are not included in the formation energy calculation
             (all set to zero energy).
@@ -180,15 +180,15 @@
     """
     Prints a defect formation energy table for a single chemical potential limit (i.e. phase diagram
     facet), and returns the results as a pandas DataFrame.
 
     Args:
         defect_phase_diagram (DefectPhaseDiagram):
              DefectPhaseDiagram object (likely created from
-             analysis.dpd_from_parsed_defect_dict)
+             analysis.dpd_from_defect_dict)
         chempots (dict):
             Dictionary of chosen absolute/DFT chemical potentials: {Elt: Energy}. If not
             specified, chemical potentials are not included in the formation energy calculation
             (all set to zero energy).
         fermi_level (float):
             Fermi level to use for computing the defect formation energies. (default: 0 (i.e.
             at the VBM))
```

### Comparing `doped-1.0.8/doped/chemical_potentials.py` & `doped-1.0.9/doped/chemical_potentials.py`

 * *Files 1% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 )  # currently rely on this so shouldn't show warning
 warnings.filterwarnings("ignore", message="Ignoring unknown variable type")
 
 
 # TODO: Check default error when user attempts `CompetingPhases()` with no API key setup; if not
 #  sufficiently informative, add try except catch to give more informative error message for this.
 # TODO: Need to recheck all functionality from old `_chemical_potentials.py` is now present here.
+# TODO: Add chemical potential diagram plotting functionality that we had before with `plot_cplap_ternary`.
 
 
 def make_molecule_in_a_box(element):
     # (but do try to fix it so that the nupdown is the same as magnetisation
     # so that it makes that assignment easier later on when making files)
     # the bond distances are taken from various sources and *not* thoroughly vetted
     lattice = [[30, 0, 0], [0, 30, 0], [0, 0, 30]]
@@ -389,14 +390,16 @@
                 x.data["e_above_hull"],
                 len(Composition(x.name).as_dict()),
                 x.name,
             )
         )
 
     # TODO: Similar refactor to work mainly off config dict object here as well (as vasp_input)?
+    # TODO: Return dict of DictSet objects for this and vasp_std_setup() functions, as well as
+    #  write_files option, for ready integration with high-throughput workflows
     # TODO: Currently doesn't exactly match vaspup2.0 naming convention which means it doesn't
     #  account for the ordering switch from 1..9 to 10 etc
     def convergence_setup(
         self,
         kpoints_metals=(40, 120, 5),
         kpoints_nonmetals=(5, 80, 5),
         user_potcar_functional="PBE_54",
```

### Comparing `doped-1.0.8/doped/plotting.py` & `doped-1.0.9/doped/plotting.py`

 * *Files 0% similar despite different names*

```diff
@@ -52,15 +52,15 @@
     emphasis=False,
 ):
     """
     Produce a defect formation energy vs Fermi energy plot (i.e. a defect transition level diagram).
 
     Args:
         defect_phase_diagram (DefectPhaseDiagram):
-             DefectPhaseDiagram object (likely created from analysis.dpd_from_parsed_defect_dict)
+             DefectPhaseDiagram object (likely created from analysis.dpd_from_defect_dict)
         chempot_limits (dict):
             This can either be a dictionary of chosen absolute/DFT chemical potentials: {Elt:
             Energy} (giving a single formation energy table – recommended to use the elt_refs
             option with this to show the formal (relative) chemical potentials in the plot) or a
             dictionary including the key-value pair: {"facets": [{'facet': [chempot_dict]}]},
             following the format generated by doped: cpa.read_phase_diagram_and_chempots() (see
             example notebooks). If not specified, chemical potentials are not included in the
@@ -639,15 +639,15 @@
 ):
     """
     Produce a defect formation energy vs Fermi energy plot (i.e. a defect transition level
     diagram), showing the full formation energy lines for all defect species present.
 
     Args:
         defect_phase_diagram (DefectPhaseDiagram):
-             DefectPhaseDiagram object (likely created from analysis.dpd_from_parsed_defect_dict)
+             DefectPhaseDiagram object (likely created from analysis.dpd_from_defect_dict)
         chempot_limits (dict):
             This can either be a dictionary of chosen absolute/DFT chemical potentials: {Elt:
             Energy} (giving a single formation energy table – recommended to use the elt_refs
             option with this to show the formal (relative) chemical potentials in the plot) or a
             dictionary including the key-value pair: {"facets": [{'facet': [chempot_dict]}]},
             following the format generated by doped: cpa.read_phase_diagram_and_chempots() (see
             example notebooks). If not specified, chemical potentials are not included in the
```

### Comparing `doped-1.0.8/doped/pycdt/core/_chemical_potentials.py` & `doped-1.0.9/doped/pycdt/core/_chemical_potentials.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/core/defects_analyzer.py` & `doped-1.0.9/doped/pycdt/core/defects_analyzer.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/core/defectsmaker.py` & `doped-1.0.9/doped/pycdt/core/defectsmaker.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/core/tests/test_chemical_potentials.py` & `doped-1.0.9/doped/pycdt/core/tests/test_chemical_potentials.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/core/tests/test_defects_analyzer.py` & `doped-1.0.9/doped/pycdt/core/tests/test_defects_analyzer.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/core/tests/test_defectsmaker.py` & `doped-1.0.9/doped/pycdt/core/tests/test_defectsmaker.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/corrections/finite_size_charge_correction.py` & `doped-1.0.9/doped/pycdt/corrections/finite_size_charge_correction.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/corrections/freysoldt_plotter.py` & `doped-1.0.9/doped/pycdt/corrections/freysoldt_plotter.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/corrections/ldau_correction.py` & `doped-1.0.9/doped/pycdt/corrections/ldau_correction.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/corrections/sxdefect_correction.py` & `doped-1.0.9/doped/pycdt/corrections/sxdefect_correction.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/corrections/tests/test_finite_size_charge_correction.py` & `doped-1.0.9/doped/pycdt/corrections/tests/test_finite_size_charge_correction.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/corrections/tests/test_ldau_correction.py` & `doped-1.0.9/doped/pycdt/corrections/tests/test_ldau_correction.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/corrections/tests/test_utils.py` & `doped-1.0.9/doped/pycdt/corrections/tests/test_utils.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/corrections/utils.py` & `doped-1.0.9/doped/pycdt/corrections/utils.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/utils/log_util.py` & `doped-1.0.9/doped/pycdt/utils/log_util.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/utils/parse_calculations.py` & `doped-1.0.9/doped/pycdt/utils/parse_calculations.py`

 * *Files 1% similar despite different names*

```diff
@@ -27,15 +27,15 @@
 from pymatgen.ext.matproj import MPRester
 from pymatgen.io.vasp.inputs import Potcar, UnknownPotcarWarning
 from pymatgen.io.vasp.outputs import Locpot, Outcar, Poscar, Vasprun
 from pymatgen.util.coord import pbc_diff
 
 from doped.pycdt.core import _chemical_potentials
 
-angstrom = "\u212B"  # unicode symbol for angstrom to print in strings
+_ANGSTROM = "\u212B"  # unicode symbol for angstrom to print in strings
 
 # globally ignore these POTCAR warnings
 warnings.filterwarnings("ignore", category=UnknownPotcarWarning)
 warnings.filterwarnings("ignore", message="No POTCAR file with matching TITEL fields")
 warnings.filterwarnings("ignore", message="Ignoring unknown variable type")
 
 # until updated from pymatgen==2022.7.25 :
@@ -397,14 +397,23 @@
     #  than with the single looping function described below):
     # TODO: Add a function that loops over all the defects in a directory (with `defect_dir = .`,
     #  and `subfolder = vasp_ncl` options) and parses them all, returning a dictionary of defect
     #  entries, with the defect name as the key. (i.e. doing the loop in the example notebook).
     #  Show both this function and the individual function calls in the example notebook. Benefit
     #  of this one is that we can then auto-run `check_defects_compatibility()` at the end of
     #  parsing the full defects dict.
+
+    _delocalization_warning_printed = False  # class variable
+    # ensures the verbose delocalization analysis warning is only printed once. Needs to be done
+    # this way because the current workflow is to create a `SingleDefectParser` object for each
+    # defect, and then warning originates from the `run_compatibility()` method of different
+    # `SingleDefectParser` instances, so warnings detects each instance as a different source and
+    # prints the warning multiple times. When we move to a single function call for all defects
+    # (as described above), this can be removed.
+
     def __init__(
         self,
         defect_entry,
         compatibility=DefectCompatibility(
             plnr_avg_var_tol=0.01,
             plnr_avg_minmax_tol=0.3,
             atomic_site_var_tol=0.025,
@@ -585,15 +594,15 @@
                         f"it in {searched}. Abandoning parsing."
                     ) from exc
                 if poss_deflist[0][1] > 1:
                     site_matched_defect = poss_deflist[0]  # pymatgen Neighbor object
                     offsite_warning = (
                         f"Site-matching has determined {site_matched_defect.species} at "
                         f"{site_matched_defect.coords} as the defect site, located "
-                        f"{site_matched_defect.nn_distance:.2f} {angstrom} from its initial "
+                        f"{site_matched_defect.nn_distance:.2f} {_ANGSTROM} from its initial "
                         f"position. This may incur small errors in the charge correction."
                     )
                     warnings.warn(message=offsite_warning)
 
             else:
                 raise RuntimeError(
                     f"Could not identify {def_type} defect site in defect structure. "
@@ -1090,17 +1099,21 @@
 accurate total energies. Recommended to look at the correction plots (i.e. run 
 `get_correction_freysoldt(DefectEntry,...,plot=True)` from
 `doped.pycdt.corrections.finite_size_charge_correction`) to visually determine if the charge 
 correction scheme is still appropriate (replace 'freysoldt' with 'kumagai' if using anisotropic 
 correction). You can also change the DefectCompatibility() tolerance settings via the 
 `compatibility` parameter in `SingleDefectParser.from_paths()`."""
                 warnings.warn(message=specific_delocalized_warning)
-                warnings.warn(
-                    message=general_delocalization_warning
-                )  # should only print once
+                if not self._delocalization_warning_printed:
+                    warnings.warn(
+                        message=general_delocalization_warning
+                    )  # should only print once
+                    SingleDefectParser._delocalization_warning_printed = (
+                        True  # don't print again
+                    )
 
         if "num_hole_vbm" in self.defect_entry.parameters:
             if (
                 self.compatibility.free_chg_cutoff
                 < self.defect_entry.parameters["num_hole_vbm"]
             ) or (
                 self.compatibility.free_chg_cutoff
@@ -1401,29 +1414,29 @@
         Note to user: If personal phase diagram desired,
             option exists in the pycdt.core.chemical_potentials to setup,
             run and parse personal phase diagrams for purposes of chemical potentials
         """
         logger = logging.getLogger(__name__)
 
         if self._mpid:
-            cpa = chemical_potentials.MPChemPotAnalyzer(
+            cpa = _chemical_potentials.MPChemPotAnalyzer(
                 mpid=self._mpid,
                 sub_species=self._substitution_species,
                 mapi_key=self._mapi_key,
             )
         else:
             bulkvr, bulkvr_path = get_vasprun(
                 os.path.join(self._root_fldr, "bulk", "vasprun.xml"),
                 parse_potcar_file=False,
             )
             if not bulkvr:
                 msg = "Could not fetch computed entry for atomic chempots!"
                 logger.warning(msg)
                 raise ValueError(msg)
-            cpa = chemical_potentials.MPChemPotAnalyzer(
+            cpa = _chemical_potentials.MPChemPotAnalyzer(
                 bulk_ce=bulkvr.get_computed_entry(),
                 sub_species=self._substitution_species,
                 mapi_key=self._mapi_key,
             )
 
         chem_lims = cpa.analyze_GGA_chempots()
```

### Comparing `doped-1.0.8/doped/pycdt/utils/plotter.py` & `doped-1.0.9/doped/pycdt/utils/plotter.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/utils/tests/test_log_util.py` & `doped-1.0.9/doped/pycdt/utils/tests/test_log_util.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/utils/tests/test_parse_calculations.py` & `doped-1.0.9/doped/pycdt/utils/tests/test_parse_calculations.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/utils/tests/test_plotter.py` & `doped-1.0.9/doped/pycdt/utils/tests/test_plotter.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/utils/tests/test_vasp.py` & `doped-1.0.9/doped/pycdt/utils/tests/test_vasp.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/utils/units.py` & `doped-1.0.9/doped/pycdt/utils/units.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/pycdt/utils/vasp.py` & `doped-1.0.9/doped/pycdt/utils/vasp.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/doped/vasp_input.py` & `doped-1.0.9/doped/vasp_input.py`

 * *Files 0% similar despite different names*

```diff
@@ -536,16 +536,16 @@
 
 
 # TODO: Remove these functions once confirming all functionality is in `chemical_potentials.py`;
 # need `vasp_ncl_chempot` generation, `vaspup2.0` `input` folder with `CONFIG` generation as an
 # option, improve chemical_potentials docstrings (i.e. mention defaults, note in notebooks if changing
 # `INCAR`/`POTCAR` settings for competing phase production calcs, should also do with defect
 # supercell calcs (and note this in vasp_input as well)), ensure consistent INCAR tags in defect
-# supercell defaults and competing phase defaults, point too DefectSet in docstrings for defaults
-# (noting the other INCAR tags that are changed)
+# supercell defaults and competing phase defaults, point to DefectSet in docstrings for defaults
+# (noting the other INCAR tags that are changed).
 def _vasp_converge_files(
     structure: "pymatgen.core.Structure",
     input_dir: str = None,
     incar_settings: dict = None,
     potcar_settings: dict = None,
     config: str = None,
 ) -> None:
```

### Comparing `doped-1.0.8/doped.egg-info/PKG-INFO` & `doped-1.0.9/doped.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: doped
-Version: 1.0.8
+Version: 1.0.9
 Summary: Python package to setup, process and analyse solid-state defect calculations with VASP
 Author-email: Seán Kavanagh <sean.kavanagh.19@ucl.ac.uk>
 License: MIT License
         
         Copyright (c) 2021 Seán Kavanagh
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
```

### Comparing `doped-1.0.8/doped.egg-info/SOURCES.txt` & `doped-1.0.9/doped.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/pyproject.toml` & `doped-1.0.9/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "doped"
-version = "1.0.8"
+version = "1.0.9"
 description = "Python package to setup, process and analyse solid-state defect calculations with VASP"
 authors = [{name = "Seán Kavanagh", email = "sean.kavanagh.19@ucl.ac.uk"}]
 readme = "README.md"
 license = {file = "LICENSE"}
 classifiers = [
     "License :: OSI Approved :: MIT License",
     "Programming Language :: Python :: 3",
```

### Comparing `doped-1.0.8/tests/test_chemical_potentials.py` & `doped-1.0.9/tests/test_chemical_potentials.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/tests/test_parse_calculations.py` & `doped-1.0.9/tests/test_parse_calculations.py`

 * *Files identical despite different names*

### Comparing `doped-1.0.8/tests/test_vasp_input.py` & `doped-1.0.9/tests/test_vasp_input.py`

 * *Files identical despite different names*

