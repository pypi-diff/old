# Comparing `tmp/pyhf-0.7.0rc4.tar.gz` & `tmp/pyhf-0.7.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyhf-0.7.0rc4.tar", last modified: Sat Sep 10 02:49:14 2022, max compression
+gzip compressed data, last modified: Sun Feb  2 00:00:00 2020, max compression
```

## Comparing `pyhf-0.7.0rc4.tar` & `pyhf-0.7.1.tar`

### file list

```diff
@@ -1,112 +1,88 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.991539 pyhf-0.7.0rc4/
--rw-r--r--   0 runner    (1001) docker     (121)      108 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/AUTHORS
--rw-r--r--   0 runner    (1001) docker     (121)    10760 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      187 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)    15512 2022-09-10 02:49:14.991539 pyhf-0.7.0rc4/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    13857 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/README.rst
--rw-r--r--   0 runner    (1001) docker     (121)     3965 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)     1956 2022-09-10 02:49:14.991539 pyhf-0.7.0rc4/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2457 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.967539 pyhf-0.7.0rc4/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.979539 pyhf-0.7.0rc4/src/pyhf/
--rw-r--r--   0 runner    (1001) docker     (121)     1164 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      179 2022-09-10 02:49:14.000000 pyhf-0.7.0rc4/src/pyhf/_version.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.979539 pyhf-0.7.0rc4/src/pyhf/cli/
--rw-r--r--   0 runner    (1001) docker     (121)      387 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1299 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/cli/cli.py
--rw-r--r--   0 runner    (1001) docker     (121)      981 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/cli/complete.py
--rw-r--r--   0 runner    (1001) docker     (121)     6901 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/cli/infer.py
--rw-r--r--   0 runner    (1001) docker     (121)     4318 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/cli/patchset.py
--rw-r--r--   0 runner    (1001) docker     (121)     3743 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/cli/rootio.py
--rw-r--r--   0 runner    (1001) docker     (121)    12511 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/cli/spec.py
--rw-r--r--   0 runner    (1001) docker     (121)     4036 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/compat.py
--rw-r--r--   0 runner    (1001) docker     (121)     9892 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/constraints.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.983539 pyhf-0.7.0rc4/src/pyhf/contrib/
--rw-r--r--   0 runner    (1001) docker     (121)       89 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/contrib/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2051 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/contrib/cli.py
--rw-r--r--   0 runner    (1001) docker     (121)     6313 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/contrib/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.983539 pyhf-0.7.0rc4/src/pyhf/contrib/viz/
--rw-r--r--   0 runner    (1001) docker     (121)       49 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/contrib/viz/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    13476 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/contrib/viz/brazil.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.983539 pyhf-0.7.0rc4/src/pyhf/data/
--rw-r--r--   0 runner    (1001) docker     (121)      708 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/data/citation.bib
--rw-r--r--   0 runner    (1001) docker     (121)     4751 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/events.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.983539 pyhf-0.7.0rc4/src/pyhf/exceptions/
--rw-r--r--   0 runner    (1001) docker     (121)     5071 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/exceptions/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.983539 pyhf-0.7.0rc4/src/pyhf/infer/
--rw-r--r--   0 runner    (1001) docker     (121)     8939 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/infer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    38704 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/infer/calculators.py
--rw-r--r--   0 runner    (1001) docker     (121)     2792 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/infer/intervals.py
--rw-r--r--   0 runner    (1001) docker     (121)     8281 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/infer/mle.py
--rw-r--r--   0 runner    (1001) docker     (121)    20903 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/infer/test_statistics.py
--rw-r--r--   0 runner    (1001) docker     (121)     3336 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/infer/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.983539 pyhf-0.7.0rc4/src/pyhf/interpolators/
--rw-r--r--   0 runner    (1001) docker     (121)     1644 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/interpolators/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3822 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/interpolators/code0.py
--rw-r--r--   0 runner    (1001) docker     (121)     4473 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/interpolators/code1.py
--rw-r--r--   0 runner    (1001) docker     (121)     5324 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/interpolators/code2.py
--rw-r--r--   0 runner    (1001) docker     (121)    15982 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/interpolators/code4.py
--rw-r--r--   0 runner    (1001) docker     (121)     4929 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/interpolators/code4p.py
--rw-r--r--   0 runner    (1001) docker     (121)     2992 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/mixins.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.987539 pyhf-0.7.0rc4/src/pyhf/modifiers/
--rw-r--r--   0 runner    (1001) docker     (121)     1451 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/modifiers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6369 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/modifiers/histosys.py
--rw-r--r--   0 runner    (1001) docker     (121)     3352 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/modifiers/lumi.py
--rw-r--r--   0 runner    (1001) docker     (121)     3616 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/modifiers/normfactor.py
--rw-r--r--   0 runner    (1001) docker     (121)     4737 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/modifiers/normsys.py
--rw-r--r--   0 runner    (1001) docker     (121)     7719 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/modifiers/shapefactor.py
--rw-r--r--   0 runner    (1001) docker     (121)     7746 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/modifiers/shapesys.py
--rw-r--r--   0 runner    (1001) docker     (121)     8781 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/modifiers/staterror.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.987539 pyhf-0.7.0rc4/src/pyhf/optimize/
--rw-r--r--   0 runner    (1001) docker     (121)     1493 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/optimize/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5557 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/optimize/common.py
--rw-r--r--   0 runner    (1001) docker     (121)     7632 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/optimize/mixins.py
--rw-r--r--   0 runner    (1001) docker     (121)     2493 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/optimize/opt_jax.py
--rw-r--r--   0 runner    (1001) docker     (121)     5340 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/optimize/opt_minuit.py
--rw-r--r--   0 runner    (1001) docker     (121)     1051 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/optimize/opt_numpy.py
--rw-r--r--   0 runner    (1001) docker     (121)     1353 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/optimize/opt_pytorch.py
--rw-r--r--   0 runner    (1001) docker     (121)     3434 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/optimize/opt_scipy.py
--rw-r--r--   0 runner    (1001) docker     (121)     1583 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/optimize/opt_tflow.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.987539 pyhf-0.7.0rc4/src/pyhf/parameters/
--rw-r--r--   0 runner    (1001) docker     (121)      447 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/parameters/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2855 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/parameters/paramsets.py
--rw-r--r--   0 runner    (1001) docker     (121)     3164 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/parameters/paramview.py
--rw-r--r--   0 runner    (1001) docker     (121)     2820 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/parameters/utils.py
--rw-r--r--   0 runner    (1001) docker     (121)    11335 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/patchset.py
--rw-r--r--   0 runner    (1001) docker     (121)    32065 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/pdf.py
--rw-r--r--   0 runner    (1001) docker     (121)     9529 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/probability.py
--rw-r--r--   0 runner    (1001) docker     (121)    17260 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/readxml.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.987539 pyhf-0.7.0rc4/src/pyhf/schema/
--rw-r--r--   0 runner    (1001) docker     (121)     2858 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/schema/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2014 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/schema/loader.py
--rw-r--r--   0 runner    (1001) docker     (121)     3198 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/schema/validator.py
--rw-r--r--   0 runner    (1001) docker     (121)      418 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/schema/variables.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.987539 pyhf-0.7.0rc4/src/pyhf/schemas/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.987539 pyhf-0.7.0rc4/src/pyhf/schemas/1.0.0/
--rw-r--r--   0 runner    (1001) docker     (121)    13069 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/schemas/1.0.0/defs.json
--rw-r--r--   0 runner    (1001) docker     (121)      180 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/schemas/1.0.0/jsonpatch.json
--rw-r--r--   0 runner    (1001) docker     (121)      184 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/schemas/1.0.0/measurement.json
--rw-r--r--   0 runner    (1001) docker     (121)      172 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/schemas/1.0.0/model.json
--rw-r--r--   0 runner    (1001) docker     (121)      178 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/schemas/1.0.0/patchset.json
--rw-r--r--   0 runner    (1001) docker     (121)      180 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/schemas/1.0.0/workspace.json
--rw-r--r--   0 runner    (1001) docker     (121)     6521 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/schemas/HistFactorySchema.dtd
--rw-r--r--   0 runner    (1001) docker     (121)     5684 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/simplemodels.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.991539 pyhf-0.7.0rc4/src/pyhf/tensor/
--rw-r--r--   0 runner    (1001) docker     (121)     3026 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/tensor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3367 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/tensor/common.py
--rw-r--r--   0 runner    (1001) docker     (121)    20954 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/tensor/jax_backend.py
--rw-r--r--   0 runner    (1001) docker     (121)     7196 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/tensor/manager.py
--rw-r--r--   0 runner    (1001) docker     (121)    22863 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/tensor/numpy_backend.py
--rw-r--r--   0 runner    (1001) docker     (121)    21209 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/tensor/pytorch_backend.py
--rw-r--r--   0 runner    (1001) docker     (121)    25518 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/tensor/tensorflow_backend.py
--rw-r--r--   0 runner    (1001) docker     (121)     2893 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/typing.py
--rw-r--r--   0 runner    (1001) docker     (121)     4434 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/utils.py
--rw-r--r--   0 runner    (1001) docker     (121)    34829 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/workspace.py
--rw-r--r--   0 runner    (1001) docker     (121)    10905 2022-09-10 02:48:25.000000 pyhf-0.7.0rc4/src/pyhf/writexml.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-10 02:49:14.979539 pyhf-0.7.0rc4/src/pyhf.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)    15512 2022-09-10 02:49:14.000000 pyhf-0.7.0rc4/src/pyhf.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2537 2022-09-10 02:49:14.000000 pyhf-0.7.0rc4/src/pyhf.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-10 02:49:14.000000 pyhf-0.7.0rc4/src/pyhf.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-09-10 02:49:14.000000 pyhf-0.7.0rc4/src/pyhf.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)     2484 2022-09-10 02:49:14.000000 pyhf-0.7.0rc4/src/pyhf.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        5 2022-09-10 02:49:14.000000 pyhf-0.7.0rc4/src/pyhf.egg-info/top_level.txt
+-rw-r--r--   0        0        0     2526 2020-02-02 00:00:00.000000 pyhf-0.7.1/CITATION.cff
+-rw-r--r--   0        0        0     1164 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/__init__.py
+-rw-r--r--   0        0        0      160 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/_version.py
+-rw-r--r--   0        0        0     4036 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/compat.py
+-rw-r--r--   0        0        0     9892 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/constraints.py
+-rw-r--r--   0        0        0     4751 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/events.py
+-rw-r--r--   0        0        0     2992 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/mixins.py
+-rw-r--r--   0        0        0    11335 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/patchset.py
+-rw-r--r--   0        0        0    32155 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/pdf.py
+-rw-r--r--   0        0        0     9529 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/probability.py
+-rw-r--r--   0        0        0    17487 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/readxml.py
+-rw-r--r--   0        0        0     5684 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/simplemodels.py
+-rw-r--r--   0        0        0     2893 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/typing.py
+-rw-r--r--   0        0        0     4425 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/utils.py
+-rw-r--r--   0        0        0    34829 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/workspace.py
+-rw-r--r--   0        0        0    10923 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/writexml.py
+-rw-r--r--   0        0        0      387 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/cli/__init__.py
+-rw-r--r--   0        0        0     1299 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/cli/cli.py
+-rw-r--r--   0        0        0      981 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/cli/complete.py
+-rw-r--r--   0        0        0     7049 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/cli/infer.py
+-rw-r--r--   0        0        0     4461 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/cli/patchset.py
+-rw-r--r--   0        0        0     3815 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/cli/rootio.py
+-rw-r--r--   0        0        0    12719 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/cli/spec.py
+-rw-r--r--   0        0        0       89 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/contrib/__init__.py
+-rw-r--r--   0        0        0     2051 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/contrib/cli.py
+-rw-r--r--   0        0        0     6313 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/contrib/utils.py
+-rw-r--r--   0        0        0       49 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/contrib/viz/__init__.py
+-rw-r--r--   0        0        0    13476 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/contrib/viz/brazil.py
+-rw-r--r--   0        0        0      699 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/data/citation.bib
+-rw-r--r--   0        0        0     5483 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/exceptions/__init__.py
+-rw-r--r--   0        0        0     8939 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/infer/__init__.py
+-rw-r--r--   0        0        0    38704 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/infer/calculators.py
+-rw-r--r--   0        0        0     8281 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/infer/mle.py
+-rw-r--r--   0        0        0    20903 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/infer/test_statistics.py
+-rw-r--r--   0        0        0     3336 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/infer/utils.py
+-rw-r--r--   0        0        0      822 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/infer/intervals/__init__.py
+-rw-r--r--   0        0        0     9724 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/infer/intervals/upper_limits.py
+-rw-r--r--   0        0        0     1644 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/interpolators/__init__.py
+-rw-r--r--   0        0        0     3822 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/interpolators/code0.py
+-rw-r--r--   0        0        0     4473 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/interpolators/code1.py
+-rw-r--r--   0        0        0     5324 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/interpolators/code2.py
+-rw-r--r--   0        0        0    15982 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/interpolators/code4.py
+-rw-r--r--   0        0        0     4929 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/interpolators/code4p.py
+-rw-r--r--   0        0        0     1451 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/modifiers/__init__.py
+-rw-r--r--   0        0        0     6369 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/modifiers/histosys.py
+-rw-r--r--   0        0        0     3351 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/modifiers/lumi.py
+-rw-r--r--   0        0        0     3616 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/modifiers/normfactor.py
+-rw-r--r--   0        0        0     4736 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/modifiers/normsys.py
+-rw-r--r--   0        0        0     7719 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/modifiers/shapefactor.py
+-rw-r--r--   0        0        0     7746 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/modifiers/shapesys.py
+-rw-r--r--   0        0        0     8780 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/modifiers/staterror.py
+-rw-r--r--   0        0        0     1493 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/optimize/__init__.py
+-rw-r--r--   0        0        0     5557 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/optimize/common.py
+-rw-r--r--   0        0        0     7629 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/optimize/mixins.py
+-rw-r--r--   0        0        0     2493 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/optimize/opt_jax.py
+-rw-r--r--   0        0        0     5338 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/optimize/opt_minuit.py
+-rw-r--r--   0        0        0     1051 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/optimize/opt_numpy.py
+-rw-r--r--   0        0        0     1353 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/optimize/opt_pytorch.py
+-rw-r--r--   0        0        0     3434 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/optimize/opt_scipy.py
+-rw-r--r--   0        0        0     1583 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/optimize/opt_tflow.py
+-rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/parameters/__init__.py
+-rw-r--r--   0        0        0     2855 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/parameters/paramsets.py
+-rw-r--r--   0        0        0     3163 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/parameters/paramview.py
+-rw-r--r--   0        0        0     2820 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/parameters/utils.py
+-rw-r--r--   0        0        0     2858 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/schema/__init__.py
+-rw-r--r--   0        0        0     2030 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/schema/loader.py
+-rw-r--r--   0        0        0     3198 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/schema/validator.py
+-rw-r--r--   0        0        0      418 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/schema/variables.py
+-rw-r--r--   0        0        0     6521 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/schemas/HistFactorySchema.dtd
+-rw-r--r--   0        0        0    13069 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/schemas/1.0.0/defs.json
+-rw-r--r--   0        0        0      180 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/schemas/1.0.0/jsonpatch.json
+-rw-r--r--   0        0        0      184 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/schemas/1.0.0/measurement.json
+-rw-r--r--   0        0        0      172 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/schemas/1.0.0/model.json
+-rw-r--r--   0        0        0      178 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/schemas/1.0.0/patchset.json
+-rw-r--r--   0        0        0      180 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/schemas/1.0.0/workspace.json
+-rw-r--r--   0        0        0     3026 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/tensor/__init__.py
+-rw-r--r--   0        0        0     3367 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/tensor/common.py
+-rw-r--r--   0        0        0    20814 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/tensor/jax_backend.py
+-rw-r--r--   0        0        0     7196 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/tensor/manager.py
+-rw-r--r--   0        0        0    22865 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/tensor/numpy_backend.py
+-rw-r--r--   0        0        0    21273 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/tensor/pytorch_backend.py
+-rw-r--r--   0        0        0    25582 2020-02-02 00:00:00.000000 pyhf-0.7.1/src/pyhf/tensor/tensorflow_backend.py
+-rw-r--r--   0        0        0      409 2020-02-02 00:00:00.000000 pyhf-0.7.1/.gitignore
+-rw-r--r--   0        0        0      108 2020-02-02 00:00:00.000000 pyhf-0.7.1/AUTHORS
+-rw-r--r--   0        0        0    10760 2020-02-02 00:00:00.000000 pyhf-0.7.1/LICENSE
+-rw-r--r--   0        0        0    13916 2020-02-02 00:00:00.000000 pyhf-0.7.1/README.rst
+-rw-r--r--   0        0        0     8489 2020-02-02 00:00:00.000000 pyhf-0.7.1/pyproject.toml
+-rw-r--r--   0        0        0    18519 2020-02-02 00:00:00.000000 pyhf-0.7.1/PKG-INFO
```

### Comparing `pyhf-0.7.0rc4/LICENSE` & `pyhf-0.7.1/LICENSE`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/PKG-INFO` & `pyhf-0.7.1/README.rst`

 * *Files 10% similar despite different names*

```diff
@@ -1,59 +1,18 @@
-Metadata-Version: 2.1
-Name: pyhf
-Version: 0.7.0rc4
-Summary: pure-Python HistFactory implementation with tensors and autodiff
-Home-page: https://github.com/scikit-hep/pyhf
-Author: Lukas Heinrich, Matthew Feickert, Giordon Stark
-Author-email: lukas.heinrich@cern.ch, matthew.feickert@cern.ch, gstark@cern.ch
-License: Apache
-Project-URL: Documentation, https://pyhf.readthedocs.io/
-Project-URL: Source Code, https://github.com/scikit-hep/pyhf
-Project-URL: Issue Tracker, https://github.com/scikit-hep/pyhf/issues
-Project-URL: Release Notes, https://pyhf.readthedocs.io/en/stable/release-notes.html
-Keywords: physics fitting numpy scipy tensorflow pytorch jax
-Classifier: Development Status :: 4 - Beta
-Classifier: License :: OSI Approved :: Apache Software License
-Classifier: Intended Audience :: Science/Research
-Classifier: Topic :: Scientific/Engineering
-Classifier: Topic :: Scientific/Engineering :: Physics
-Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3 :: Only
-Classifier: Programming Language :: Python :: 3.7
-Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9
-Classifier: Programming Language :: Python :: 3.10
-Classifier: Programming Language :: Python :: Implementation :: CPython
-Requires-Python: >=3.7
-Description-Content-Type: text/x-rst
-Provides-Extra: shellcomplete
-Provides-Extra: tensorflow
-Provides-Extra: torch
-Provides-Extra: jax
-Provides-Extra: xmlio
-Provides-Extra: minuit
-Provides-Extra: backends
-Provides-Extra: contrib
-Provides-Extra: test
-Provides-Extra: docs
-Provides-Extra: develop
-Provides-Extra: complete
-License-File: LICENSE
-
-.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/_static/img/pyhf-logo-small.png
+.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/_static/img/pyhf-logo-small.png
    :alt: pyhf logo
    :width: 320
    :align: center
 
 pure-python fitting/limit-setting/interval estimation HistFactory-style
 =======================================================================
 
 |GitHub Project| |DOI| |JOSS DOI| |Scikit-HEP| |NSF Award Number|
 
-|Docs from latest| |Docs from master| |Jupyter Book tutorial| |Binder|
+|Docs from latest| |Docs from main| |Jupyter Book tutorial| |Binder|
 
 |PyPI version| |Conda-forge version| |Supported Python versions| |Docker Hub pyhf| |Docker Hub pyhf CUDA|
 
 |Code Coverage| |CodeFactor| |pre-commit.ci Status| |Code style: black|
 
 |GitHub Actions Status: CI| |GitHub Actions Status: Docs| |GitHub Actions Status: Publish|
 |GitHub Actions Status: Docker|
@@ -107,15 +66,15 @@
 Alternatively the statistical model and observational data can be read from its serialized JSON representation (see next section).
 
 .. code:: pycon
 
    >>> import pyhf
    >>> import requests
    >>> pyhf.set_backend("numpy")
-   >>> url = "https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/examples/json/2-bin_1-channel.json"
+   >>> url = "https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/examples/json/2-bin_1-channel.json"
    >>> wspace = pyhf.Workspace(requests.get(url).json())
    >>> model = wspace.model()
    >>> data = wspace.data(model)
    >>> test_mu = 1.0
    >>> CLs_obs, CLs_exp = pyhf.infer.hypotest(
    ...     test_mu, data, model, test_stat="qtilde", return_expected=True
    ... )
@@ -231,22 +190,22 @@
    fig, ax = plt.subplots()
    fig.set_size_inches(7, 5)
    brazil.plot_results(poi_vals, results, ax=ax)
    fig.show()
 
 **pyhf**
 
-.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/_static/img/README_1bin_example.png
+.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/_static/img/README_1bin_example.png
    :alt: manual
    :width: 500
    :align: center
 
 **ROOT**
 
-.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/_static/img/hfh_1bin_55_50_7.png
+.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/_static/img/hfh_1bin_55_50_7.png
    :alt: manual
    :width: 500
    :align: center
 
 A two bin example
 -----------------
 
@@ -275,22 +234,22 @@
    fig.set_size_inches(7, 5)
    brazil.plot_results(poi_vals, results, ax=ax)
    fig.show()
 
 
 **pyhf**
 
-.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/_static/img/README_2bin_example.png
+.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/_static/img/README_2bin_example.png
    :alt: manual
    :width: 500
    :align: center
 
 **ROOT**
 
-.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/_static/img/hfh_2_bin_100.0_145.0_100.0_150.0_15.0_20.0_30.0_45.0.png
+.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/_static/img/hfh_2_bin_100.0_145.0_100.0_150.0_15.0_20.0_30.0_45.0.png
    :alt: manual
    :width: 500
    :align: center
 
 Installation
 ------------
 
@@ -346,19 +305,19 @@
 `Zenodo <https://zenodo.org/>`__ archive and the
 `JOSS <https://joss.theoj.org/>`__ paper:
 
 .. code:: bibtex
 
    @software{pyhf,
      author = {Lukas Heinrich and Matthew Feickert and Giordon Stark},
-     title = "{pyhf: v0.7.0rc4}",
-     version = {0.7.0rc4},
+     title = "{pyhf: v0.7.1}",
+     version = {0.7.1},
      doi = {10.5281/zenodo.1169739},
      url = {https://doi.org/10.5281/zenodo.1169739},
-     note = {https://github.com/scikit-hep/pyhf/releases/tag/v0.7.0rc4}
+     note = {https://github.com/scikit-hep/pyhf/releases/tag/v0.7.1}
    }
 
    @article{pyhf_joss,
      doi = {10.21105/joss.02823},
      url = {https://doi.org/10.21105/joss.02823},
      year = {2021},
      publisher = {The Open Journal},
@@ -377,14 +336,15 @@
 
 Please check the `contribution statistics for a list of
 contributors <https://github.com/scikit-hep/pyhf/graphs/contributors>`__.
 
 Milestones
 ----------
 
+- 2022-09-12: 2000 GitHub issues and pull requests. (See PR `#2000 <https://github.com/scikit-hep/pyhf/pull/2000>`__)
 - 2021-12-09: 1000 commits to the project. (See PR `#1710 <https://github.com/scikit-hep/pyhf/pull/1710>`__)
 - 2020-07-28: 1000 GitHub issues and pull requests. (See PR `#1000 <https://github.com/scikit-hep/pyhf/pull/1000>`__)
 
 Acknowledgements
 ----------------
 
 Matthew Feickert has received support to work on ``pyhf`` provided by NSF
@@ -397,45 +357,45 @@
    :target: https://doi.org/10.5281/zenodo.1169739
 .. |JOSS DOI| image:: https://joss.theoj.org/papers/10.21105/joss.02823/status.svg
    :target: https://doi.org/10.21105/joss.02823
 .. |Scikit-HEP| image:: https://scikit-hep.org/assets/images/Scikit--HEP-Project-blue.svg
    :target: https://scikit-hep.org/
 .. |NSF Award Number| image:: https://img.shields.io/badge/NSF-1836650-blue.svg
    :target: https://nsf.gov/awardsearch/showAward?AWD_ID=1836650
-.. |Docs from latest| image:: https://img.shields.io/badge/docs-v0.7.0rc4-blue.svg
+.. |Docs from latest| image:: https://img.shields.io/badge/docs-v0.7.1-blue.svg
    :target: https://pyhf.readthedocs.io/
-.. |Docs from master| image:: https://img.shields.io/badge/docs-master-blue.svg
+.. |Docs from main| image:: https://img.shields.io/badge/docs-main-blue.svg
    :target: https://scikit-hep.github.io/pyhf
 .. |Jupyter Book tutorial| image:: https://jupyterbook.org/_images/badge.svg
    :target: https://pyhf.github.io/pyhf-tutorial/
 .. |Binder| image:: https://mybinder.org/badge_logo.svg
-   :target: https://mybinder.org/v2/gh/scikit-hep/pyhf/master?filepath=docs%2Fexamples%2Fnotebooks%2Fbinderexample%2FStatisticalAnalysis.ipynb
+   :target: https://mybinder.org/v2/gh/scikit-hep/pyhf/main?filepath=docs%2Fexamples%2Fnotebooks%2Fbinderexample%2FStatisticalAnalysis.ipynb
 
 .. |PyPI version| image:: https://badge.fury.io/py/pyhf.svg
    :target: https://badge.fury.io/py/pyhf
 .. |Conda-forge version| image:: https://img.shields.io/conda/vn/conda-forge/pyhf.svg
    :target: https://github.com/conda-forge/pyhf-feedstock
 .. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/pyhf.svg
    :target: https://pypi.org/project/pyhf/
-.. |Docker Hub pyhf| image:: https://img.shields.io/badge/pyhf-v0.7.0rc4-blue?logo=Docker
+.. |Docker Hub pyhf| image:: https://img.shields.io/badge/pyhf-v0.7.1-blue?logo=Docker
    :target: https://hub.docker.com/r/pyhf/pyhf/tags
 .. |Docker Hub pyhf CUDA| image:: https://img.shields.io/badge/pyhf-CUDA-blue?logo=Docker
    :target: https://hub.docker.com/r/pyhf/cuda/tags
 
-.. |Code Coverage| image:: https://codecov.io/gh/scikit-hep/pyhf/graph/badge.svg?branch=master
-   :target: https://codecov.io/gh/scikit-hep/pyhf?branch=master
+.. |Code Coverage| image:: https://codecov.io/gh/scikit-hep/pyhf/graph/badge.svg?branch=main
+   :target: https://codecov.io/gh/scikit-hep/pyhf?branch=main
 .. |CodeFactor| image:: https://www.codefactor.io/repository/github/scikit-hep/pyhf/badge
    :target: https://www.codefactor.io/repository/github/scikit-hep/pyhf
-.. |pre-commit.ci Status| image:: https://results.pre-commit.ci/badge/github/scikit-hep/pyhf/master.svg
-  :target: https://results.pre-commit.ci/latest/github/scikit-hep/pyhf/master
+.. |pre-commit.ci Status| image:: https://results.pre-commit.ci/badge/github/scikit-hep/pyhf/main.svg
+  :target: https://results.pre-commit.ci/latest/github/scikit-hep/pyhf/main
   :alt: pre-commit.ci status
 .. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
 
-.. |GitHub Actions Status: CI| image:: https://github.com/scikit-hep/pyhf/workflows/CI/CD/badge.svg?branch=master
-   :target: https://github.com/scikit-hep/pyhf/actions?query=workflow%3ACI%2FCD+branch%3Amaster
-.. |GitHub Actions Status: Docs| image:: https://github.com/scikit-hep/pyhf/workflows/Docs/badge.svg?branch=master
-   :target: https://github.com/scikit-hep/pyhf/actions?query=workflow%3ADocs+branch%3Amaster
-.. |GitHub Actions Status: Publish| image:: https://github.com/scikit-hep/pyhf/workflows/publish%20distributions/badge.svg?branch=master
-   :target: https://github.com/scikit-hep/pyhf/actions?query=workflow%3A%22publish+distributions%22+branch%3Amaster
-.. |GitHub Actions Status: Docker| image:: https://github.com/scikit-hep/pyhf/actions/workflows/docker.yml/badge.svg?branch=master
-   :target: https://github.com/scikit-hep/pyhf/actions/workflows/docker.yml?query=branch%3Amaster
+.. |GitHub Actions Status: CI| image:: https://github.com/scikit-hep/pyhf/workflows/CI/CD/badge.svg?branch=main
+   :target: https://github.com/scikit-hep/pyhf/actions?query=workflow%3ACI%2FCD+branch%3Amain
+.. |GitHub Actions Status: Docs| image:: https://github.com/scikit-hep/pyhf/workflows/Docs/badge.svg?branch=main
+   :target: https://github.com/scikit-hep/pyhf/actions?query=workflow%3ADocs+branch%3Amain
+.. |GitHub Actions Status: Publish| image:: https://github.com/scikit-hep/pyhf/workflows/publish%20distributions/badge.svg?branch=main
+   :target: https://github.com/scikit-hep/pyhf/actions?query=workflow%3A%22publish+distributions%22+branch%3Amain
+.. |GitHub Actions Status: Docker| image:: https://github.com/scikit-hep/pyhf/actions/workflows/docker.yml/badge.svg?branch=main
+   :target: https://github.com/scikit-hep/pyhf/actions/workflows/docker.yml?query=branch%3Amain
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/__init__.py` & `pyhf-0.7.1/src/pyhf/__init__.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/cli/cli.py` & `pyhf-0.7.1/src/pyhf/cli/cli.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/cli/complete.py` & `pyhf-0.7.1/src/pyhf/cli/complete.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/cli/infer.py` & `pyhf-0.7.1/src/pyhf/cli/infer.py`

 * *Files 8% similar despite different names*

```diff
@@ -59,15 +59,15 @@
     """
     Perform a maximum likelihood fit for a given pyhf workspace.
 
     Example:
 
     .. code-block:: shell
 
-        $ curl -sL https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/examples/json/2-bin_1-channel.json | pyhf fit --value
+        $ curl -sL https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/examples/json/2-bin_1-channel.json | pyhf fit --value
 
         \b
         {
             "mle_parameters": {
                 "mu": [
                     0.00017298628839781602
                 ],
@@ -95,18 +95,21 @@
     # set the new optimizer
     if optimizer:
         new_optimizer = getattr(optimize, optimizer) or getattr(
             optimize, f"{optimizer}_optimizer"
         )
         set_backend(tensorlib, new_optimizer(**optconf))
 
-    with click.open_file(workspace, "r") as specstream:
+    with click.open_file(workspace, "r", encoding="utf-8") as specstream:
         spec = json.load(specstream)
     ws = Workspace(spec)
-    patches = [json.loads(click.open_file(pfile, "r").read()) for pfile in patch]
+    patches = [
+        json.loads(click.open_file(pfile, "r", encoding="utf-8").read())
+        for pfile in patch
+    ]
 
     model = ws.model(
         measurement_name=measurement,
         patches=patches,
     )
     data = ws.data(model)
 
@@ -121,15 +124,15 @@
     result = {"mle_parameters": bestfit_pars}
     if value:
         result["twice_nll"] = tensorlib.tolist(fit_result[-1])
 
     if output_file is None:
         click.echo(json.dumps(result, indent=4, sort_keys=True))
     else:
-        with open(output_file, "w+") as out_file:
+        with open(output_file, "w+", encoding="utf-8") as out_file:
             json.dump(result, out_file, indent=4, sort_keys=True)
         log.debug(f"Written to {output_file:s}")
 
 
 @cli.command()
 @click.argument('workspace', default='-')
 @click.option(
@@ -172,34 +175,37 @@
     """
     Compute CLs value(s) for a given pyhf workspace.
 
     Example:
 
     .. code-block:: shell
 
-        $ curl -sL https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/examples/json/2-bin_1-channel.json | pyhf cls
+        $ curl -sL https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/examples/json/2-bin_1-channel.json | pyhf cls
 
         \b
         {
             "CLs_exp": [
                 0.07807427911686156,
                 0.17472571775474618,
                 0.35998495263681285,
                 0.6343568235898907,
                 0.8809947004472013
             ],
             "CLs_obs": 0.3599845631401915
         }
     """
-    with click.open_file(workspace, 'r') as specstream:
+    with click.open_file(workspace, "r", encoding="utf-8") as specstream:
         spec = json.load(specstream)
 
     ws = Workspace(spec)
 
-    patches = [json.loads(click.open_file(pfile, 'r').read()) for pfile in patch]
+    patches = [
+        json.loads(click.open_file(pfile, "r", encoding="utf-8").read())
+        for pfile in patch
+    ]
     model = ws.model(
         measurement_name=measurement,
         patches=patches,
         modifier_settings={
             'normsys': {'interpcode': 'code4'},
             'histosys': {'interpcode': 'code4p'},
         },
@@ -237,10 +243,10 @@
         'CLs_obs': tensorlib.tolist(result[0]),
         'CLs_exp': [tensorlib.tolist(tensor) for tensor in result[-1]],
     }
 
     if output_file is None:
         click.echo(json.dumps(result, indent=4, sort_keys=True))
     else:
-        with open(output_file, 'w+') as out_file:
+        with open(output_file, "w+", encoding="utf-8") as out_file:
             json.dump(result, out_file, indent=4, sort_keys=True)
         log.debug(f"Written to {output_file:s}")
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/cli/patchset.py` & `pyhf-0.7.1/src/pyhf/cli/patchset.py`

 * *Files 8% similar despite different names*

```diff
@@ -35,28 +35,28 @@
 
     Raises:
         :class:`~pyhf.exceptions.InvalidPatchLookup`: if the provided patch name is not in the patchset
 
     Returns:
         jsonpatch (:obj:`list`): A list of jsonpatch operations to apply to a workspace.
     """
-    with click.open_file(patchset, 'r') as fstream:
+    with click.open_file(patchset, "r", encoding="utf-8") as fstream:
         patchset_spec = json.load(fstream)
 
     patchset = PatchSet(patchset_spec)
     patch = patchset[name]
 
     if with_metadata:
         result = {'metadata': patch.metadata, 'patch': patch.patch}
         result['metadata'].update(patchset.metadata)
     else:
         result = patch.patch
 
     if output_file:
-        with open(output_file, 'w+') as out_file:
+        with open(output_file, "w", encoding="utf-8") as out_file:
             json.dump(result, out_file, indent=4, sort_keys=True)
         log.debug(f"Written to {output_file:s}")
     else:
         click.echo(json.dumps(result, indent=4, sort_keys=True))
 
 
 @cli.command()
@@ -75,27 +75,27 @@
     Raises:
         :class:`~pyhf.exceptions.InvalidPatchLookup`: if the provided patch name is not in the patchset
         :class:`~pyhf.exceptions.PatchSetVerificationError`: if the patchset cannot be verified against the workspace specification
 
     Returns:
         workspace (:class:`~pyhf.workspace.Workspace`): The patched background-only workspace.
     """
-    with click.open_file(background_only, 'r') as specstream:
+    with click.open_file(background_only, "r", encoding="utf-8") as specstream:
         spec = json.load(specstream)
 
     ws = Workspace(spec)
 
-    with click.open_file(patchset, 'r') as fstream:
+    with click.open_file(patchset, "r", encoding="utf-8") as fstream:
         patchset_spec = json.load(fstream)
 
     patchset = PatchSet(patchset_spec)
     patched_ws = patchset.apply(ws, name)
 
     if output_file:
-        with open(output_file, 'w+') as out_file:
+        with open(output_file, "w+", encoding="utf-8") as out_file:
             json.dump(patched_ws, out_file, indent=4, sort_keys=True)
         log.debug(f"Written to {output_file:s}")
     else:
         click.echo(json.dumps(patched_ws, indent=4, sort_keys=True))
 
 
 @cli.command()
@@ -107,20 +107,20 @@
 
     Raises:
         :class:`~pyhf.exceptions.PatchSetVerificationError`: if the patchset cannot be verified against the workspace specification
 
     Returns:
         None
     """
-    with click.open_file(background_only, 'r') as specstream:
+    with click.open_file(background_only, "r", encoding="utf-8") as specstream:
         spec = json.load(specstream)
 
     ws = Workspace(spec)
 
-    with click.open_file(patchset, 'r') as fstream:
+    with click.open_file(patchset, "r", encoding="utf-8") as fstream:
         patchset_spec = json.load(fstream)
 
     patchset = PatchSet(patchset_spec)
     patchset.verify(ws)
 
     click.echo("All good.")
 
@@ -130,15 +130,15 @@
 def inspect(patchset):
     """
     Inspect the PatchSet (e.g. list individual patches).
 
     Returns:
         None
     """
-    with click.open_file(patchset, 'r') as fstream:
+    with click.open_file(patchset, "r", encoding="utf-8") as fstream:
         patchset_spec = json.load(fstream)
 
     patchset = PatchSet(patchset_spec)
     click.secho(f'\n    {len(patchset.patches)} patches found in Patchset')
     click.secho('---------------------------------\n')
     for p in patchset.patches:
         click.echo(p.name)
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/cli/rootio.py` & `pyhf-0.7.1/src/pyhf/cli/rootio.py`

 * *Files 6% similar despite different names*

```diff
@@ -23,15 +23,15 @@
     help='The base directory for the XML files to point relative to.',
     type=click.Path(exists=True),
     default=Path.cwd(),
 )
 @click.option(
     '-v',
     '--mount',
-    help='Consists of two fields, separated by a colon character ( : ). The first field is the local path to where files are located, the second field is the path where the file or directory are saved in the XML configuration. This is similar in spirit to docker.',
+    help='Consists of two fields, separated by a colon character ( : ). The first field is the local path to where files are located, the second field is the path where the file or directory are saved in the XML configuration. This is similar in spirit to Docker.',
     type=VolumeMountPath(exists=True, resolve_path=True, path_type=Path),
     default=None,
     multiple=True,
 )
 @click.option(
     '--output-file',
     help='The location of the output json file. If not specified, prints to screen.',
@@ -61,15 +61,15 @@
         mounts=mount,
         track_progress=track_progress,
         validation_as_error=validation_as_error,
     )
     if output_file is None:
         click.echo(json.dumps(spec, indent=4, sort_keys=True))
     else:
-        with open(output_file, 'w+') as out_file:
+        with open(output_file, "w+", encoding="utf-8") as out_file:
             json.dump(spec, out_file, indent=4, sort_keys=True)
         log.debug(f"Written to {output_file:s}")
 
 
 @cli.command()
 @click.argument('workspace', default='-')
 @click.option('--output-dir', type=click.Path(exists=True), default='.')
@@ -88,23 +88,23 @@
             "json2xml requires uproot, please install pyhf using the "
             "xmlio extra: python -m pip install pyhf[xmlio]",
             exc_info=True,
         )
     from pyhf import writexml
 
     os.makedirs(output_dir, exist_ok=True)
-    with click.open_file(workspace, 'r') as specstream:
+    with click.open_file(workspace, "r", encoding="utf-8") as specstream:
         spec = json.load(specstream)
         for pfile in patch:
-            patch = json.loads(click.open_file(pfile, 'r').read())
+            patch = json.loads(click.open_file(pfile, "r", encoding="utf-8").read())
             spec = jsonpatch.JsonPatch(patch).apply(spec)
         os.makedirs(Path(output_dir).joinpath(specroot), exist_ok=True)
         os.makedirs(Path(output_dir).joinpath(dataroot), exist_ok=True)
         with click.open_file(
-            Path(output_dir).joinpath(f'{resultprefix}.xml'), 'w'
+            Path(output_dir).joinpath(f"{resultprefix}.xml"), "w", encoding="utf-8"
         ) as outstream:
             outstream.write(
                 writexml.writexml(
                     spec,
                     Path(output_dir).joinpath(specroot),
                     Path(output_dir).joinpath(dataroot),
                     resultprefix,
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/cli/spec.py` & `pyhf-0.7.1/src/pyhf/cli/spec.py`

 * *Files 4% similar despite different names*

```diff
@@ -29,15 +29,15 @@
     """
     Inspect a pyhf JSON document.
 
     Example:
 
     .. code-block:: shell
 
-        $ curl -sL https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/examples/json/2-bin_1-channel.json | pyhf inspect
+        $ curl -sL https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/examples/json/2-bin_1-channel.json | pyhf inspect
                   Summary
             ------------------
                channels  1
                 samples  2
              parameters  2
               modifiers  2
 
@@ -56,15 +56,15 @@
         uncorr_bkguncrt  constrained_by_poisson  shapesys
 
             measurement           poi            parameters
              ----------        ----------        ----------
         (*) Measurement            mu            (none)
 
     """
-    with click.open_file(workspace, 'r') as specstream:
+    with click.open_file(workspace, "r", encoding="utf-8") as specstream:
         spec = json.load(specstream)
 
     ws = Workspace(spec)
     default_measurement = ws.get_measurement()
 
     result = {}
     result['samples'] = ws.samples
@@ -154,15 +154,15 @@
                 else '(none)',
             )
         )
 
     click.echo()
 
     if output_file:
-        with open(output_file, 'w+') as out_file:
+        with open(output_file, "w+", encoding="utf-8") as out_file:
             json.dump(result, out_file, indent=4, sort_keys=True)
         log.debug(f"Written to {output_file:s}")
 
 
 @cli.command()
 @click.argument('workspace', default='-')
 @click.option(
@@ -185,30 +185,30 @@
     workspace, output_file, channel, sample, modifier, modifier_type, measurement
 ):
     """
     Prune components from the workspace.
 
     See :func:`pyhf.workspace.Workspace.prune` for more information.
     """
-    with click.open_file(workspace, 'r') as specstream:
+    with click.open_file(workspace, "r", encoding="utf-8") as specstream:
         spec = json.load(specstream)
 
     ws = Workspace(spec)
     pruned_ws = ws.prune(
         channels=channel,
         samples=sample,
         modifiers=modifier,
         modifier_types=modifier_type,
         measurements=measurement,
     )
 
     if output_file is None:
         click.echo(json.dumps(pruned_ws, indent=4, sort_keys=True))
     else:
-        with open(output_file, 'w+') as out_file:
+        with open(output_file, "w+", encoding="utf-8") as out_file:
             json.dump(pruned_ws, out_file, indent=4, sort_keys=True)
         log.debug(f"Written to {output_file:s}")
 
 
 @cli.command()
 @click.argument('workspace', default='-')
 @click.option(
@@ -249,29 +249,29 @@
 )
 def rename(workspace, output_file, channel, sample, modifier, measurement):
     """
     Rename components of the workspace.
 
     See :func:`pyhf.workspace.Workspace.rename` for more information.
     """
-    with click.open_file(workspace, 'r') as specstream:
+    with click.open_file(workspace, "r", encoding="utf-8") as specstream:
         spec = json.load(specstream)
 
     ws = Workspace(spec)
     renamed_ws = ws.rename(
         channels=dict(channel),
         samples=dict(sample),
         modifiers=dict(modifier),
         measurements=dict(measurement),
     )
 
     if output_file is None:
         click.echo(json.dumps(renamed_ws, indent=4, sort_keys=True))
     else:
-        with open(output_file, 'w+') as out_file:
+        with open(output_file, "w+", encoding="utf-8") as out_file:
             json.dump(renamed_ws, out_file, indent=4, sort_keys=True)
         log.debug(f"Written to {output_file:s}")
 
 
 @cli.command()
 @click.argument('workspace-one', default='-')
 @click.argument('workspace-two', default='-')
@@ -294,30 +294,30 @@
 )
 def combine(workspace_one, workspace_two, join, output_file, merge_channels):
     """
     Combine two workspaces into a single workspace.
 
     See :func:`pyhf.workspace.Workspace.combine` for more information.
     """
-    with click.open_file(workspace_one, 'r') as specstream:
+    with click.open_file(workspace_one, "r", encoding="utf-8") as specstream:
         spec_one = json.load(specstream)
 
-    with click.open_file(workspace_two, 'r') as specstream:
+    with click.open_file(workspace_two, "r", encoding="utf-8") as specstream:
         spec_two = json.load(specstream)
 
     ws_one = Workspace(spec_one)
     ws_two = Workspace(spec_two)
     combined_ws = Workspace.combine(
         ws_one, ws_two, join=join, merge_channels=merge_channels
     )
 
     if output_file is None:
         click.echo(json.dumps(combined_ws, indent=4, sort_keys=True))
     else:
-        with open(output_file, 'w+') as out_file:
+        with open(output_file, "w+", encoding="utf-8") as out_file:
             json.dump(combined_ws, out_file, indent=4, sort_keys=True)
         log.debug(f"Written to {output_file:s}")
 
 
 @cli.command()
 @click.argument('workspace', default='-')
 @click.option(
@@ -340,18 +340,18 @@
     Returns:
         digests (:obj:`dict`): A mapping of the hashing algorithms used to the computed digest for the workspace.
 
     Example:
 
     .. code-block:: shell
 
-        $ curl -sL https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/examples/json/2-bin_1-channel.json | pyhf digest
+        $ curl -sL https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/examples/json/2-bin_1-channel.json | pyhf digest
         sha256:dad8822af55205d60152cbe4303929042dbd9d4839012e055e7c6b6459d68d73
     """
-    with click.open_file(workspace, 'r') as specstream:
+    with click.open_file(workspace, "r", encoding="utf-8") as specstream:
         spec = json.load(specstream)
 
     workspace = Workspace(spec)
 
     digests = {
         hash_alg: utils.digest(workspace, algorithm=hash_alg) for hash_alg in algorithm
     }
@@ -379,29 +379,29 @@
 
     See :func:`pyhf.workspace.Workspace.sorted` for more information.
 
     Example:
 
     .. code-block:: shell
 
-        $ curl -sL https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/examples/json/2-bin_1-channel.json | pyhf sort | jq '.' | md5
+        $ curl -sL https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/examples/json/2-bin_1-channel.json | pyhf sort | jq '.' | md5
         8be5186ec249d2704e14dd29ef05ffb0
 
     .. code-block:: shell
 
-        $ curl -sL https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/examples/json/2-bin_1-channel.json | jq -S '.channels|=sort_by(.name)|.channels[].samples|=sort_by(.name)|.channels[].samples[].modifiers|=sort_by(.name,.type)|.observations|=sort_by(.name)' | md5
+        $ curl -sL https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/examples/json/2-bin_1-channel.json | jq -S '.channels|=sort_by(.name)|.channels[].samples|=sort_by(.name)|.channels[].samples[].modifiers|=sort_by(.name,.type)|.observations|=sort_by(.name)' | md5
         8be5186ec249d2704e14dd29ef05ffb0
 
 
     """
-    with click.open_file(workspace, 'r') as specstream:
+    with click.open_file(workspace, "r", encoding="utf-8") as specstream:
         spec = json.load(specstream)
 
     workspace = Workspace(spec)
     sorted_ws = Workspace.sorted(workspace)
 
     if output_file is None:
         click.echo(json.dumps(sorted_ws, indent=4, sort_keys=True))
     else:
-        with open(output_file, 'w+') as out_file:
+        with open(output_file, "w+", encoding="utf-8") as out_file:
             json.dump(sorted_ws, out_file, indent=4, sort_keys=True)
         log.debug(f"Written to {output_file}")
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/compat.py` & `pyhf-0.7.1/src/pyhf/compat.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/constraints.py` & `pyhf-0.7.1/src/pyhf/constraints.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/contrib/cli.py` & `pyhf-0.7.1/src/pyhf/contrib/cli.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/contrib/utils.py` & `pyhf-0.7.1/src/pyhf/contrib/utils.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/contrib/viz/brazil.py` & `pyhf-0.7.1/src/pyhf/contrib/viz/brazil.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/data/citation.bib` & `pyhf-0.7.1/src/pyhf/data/citation.bib`

 * *Files 5% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 @software{pyhf,
   author = {Lukas Heinrich and Matthew Feickert and Giordon Stark},
-  title = "{pyhf: v0.7.0rc4}",
-  version = {0.7.0rc4},
+  title = "{pyhf: v0.7.1}",
+  version = {0.7.1},
   doi = {10.5281/zenodo.1169739},
   url = {https://doi.org/10.5281/zenodo.1169739},
-  note = {https://github.com/scikit-hep/pyhf/releases/tag/v0.7.0rc4}
+  note = {https://github.com/scikit-hep/pyhf/releases/tag/v0.7.1}
 }
 
 @article{pyhf_joss,
   doi = {10.21105/joss.02823},
   url = {https://doi.org/10.21105/joss.02823},
   year = {2021},
   publisher = {The Open Journal},
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/events.py` & `pyhf-0.7.1/src/pyhf/events.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/exceptions/__init__.py` & `pyhf-0.7.1/src/pyhf/exceptions/__init__.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,8 +1,9 @@
 import sys
+from warnings import warn
 
 __all__ = [
     "FailedMinimization",
     "ImportBackendError",
     "InvalidArchiveHost",
     "InvalidBackend",
     "InvalidInterpCode",
@@ -171,7 +172,19 @@
 
     def __init__(self, result):
         self.result = result
         message = getattr(
             result, 'message', "Unknown failure. See fit result for more details."
         )
         super().__init__(message)
+
+
+# Deprecated APIs
+def _deprecated_api_warning(
+    deprecated_api, new_api, deprecated_release, remove_release
+):
+    warn(
+        f"{deprecated_api} is deprecated in favor of {new_api} as of pyhf v{deprecated_release} and will be removed in pyhf v{remove_release}."
+        + f" Please use {new_api}.",
+        DeprecationWarning,
+        stacklevel=3,  # Raise to user level
+    )
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/infer/__init__.py` & `pyhf-0.7.1/src/pyhf/infer/__init__.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/infer/calculators.py` & `pyhf-0.7.1/src/pyhf/infer/calculators.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/infer/mle.py` & `pyhf-0.7.1/src/pyhf/infer/mle.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/infer/test_statistics.py` & `pyhf-0.7.1/src/pyhf/infer/test_statistics.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/infer/utils.py` & `pyhf-0.7.1/src/pyhf/infer/utils.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/interpolators/__init__.py` & `pyhf-0.7.1/src/pyhf/interpolators/__init__.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/interpolators/code0.py` & `pyhf-0.7.1/src/pyhf/interpolators/code0.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/interpolators/code1.py` & `pyhf-0.7.1/src/pyhf/interpolators/code1.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/interpolators/code2.py` & `pyhf-0.7.1/src/pyhf/interpolators/code2.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/interpolators/code4.py` & `pyhf-0.7.1/src/pyhf/interpolators/code4.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/interpolators/code4p.py` & `pyhf-0.7.1/src/pyhf/interpolators/code4p.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/mixins.py` & `pyhf-0.7.1/src/pyhf/mixins.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/modifiers/__init__.py` & `pyhf-0.7.1/src/pyhf/modifiers/__init__.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/modifiers/histosys.py` & `pyhf-0.7.1/src/pyhf/modifiers/histosys.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/modifiers/lumi.py` & `pyhf-0.7.1/src/pyhf/modifiers/lumi.py`

 * *Files 1% similar despite different names*

```diff
@@ -16,15 +16,15 @@
         'fixed': False,
         'auxdata': None,  # lumi
         'sigmas': None,  # lumi * lumirelerror
     }
 
 
 class lumi_builder:
-    """Builder class for collecting lumi modiifier data"""
+    """Builder class for collecting lumi modifier data"""
 
     is_shared = True
 
     def __init__(self, config):
         self.builder_data = {}
         self.config = config
         self.required_parsets = {}
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/modifiers/normfactor.py` & `pyhf-0.7.1/src/pyhf/modifiers/normfactor.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/modifiers/normsys.py` & `pyhf-0.7.1/src/pyhf/modifiers/normsys.py`

 * *Files 0% similar despite different names*

```diff
@@ -68,15 +68,14 @@
 class normsys_combined:
     name = 'normsys'
     op_code = 'multiplication'
 
     def __init__(
         self, modifiers, pdfconfig, builder_data, interpcode='code1', batch_size=None
     ):
-
         self.interpcode = interpcode
         assert self.interpcode in ['code1', 'code4']
 
         keys = [f'{mtype}/{m}' for m, mtype in modifiers]
         normsys_mods = [m for m, _ in modifiers]
 
         self.batch_size = batch_size
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/modifiers/shapefactor.py` & `pyhf-0.7.1/src/pyhf/modifiers/shapefactor.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/modifiers/shapesys.py` & `pyhf-0.7.1/src/pyhf/modifiers/shapesys.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/modifiers/staterror.py` & `pyhf-0.7.1/src/pyhf/modifiers/staterror.py`

 * *Files 0% similar despite different names*

```diff
@@ -132,15 +132,14 @@
 
 
 class staterror_combined:
     name = 'staterror'
     op_code = 'multiplication'
 
     def __init__(self, modifiers, pdfconfig, builder_data, batch_size=None):
-
         default_backend = pyhf.default_backend
         self.batch_size = batch_size
 
         keys = [f'{mtype}/{m}' for m, mtype in modifiers]
         self._staterr_mods = [m for m, _ in modifiers]
 
         parfield_shape = (self.batch_size or 1, pdfconfig.npars)
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/optimize/__init__.py` & `pyhf-0.7.1/src/pyhf/optimize/__init__.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/optimize/common.py` & `pyhf-0.7.1/src/pyhf/optimize/common.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/optimize/mixins.py` & `pyhf-0.7.1/src/pyhf/optimize/mixins.py`

 * *Files 0% similar despite different names*

```diff
@@ -37,15 +37,14 @@
         x0,
         do_grad=False,
         bounds=None,
         fixed_vals=None,
         options={},
         par_names=None,
     ):
-
         minimizer = self._get_minimizer(
             func,
             x0,
             bounds,
             fixed_vals=fixed_vals,
             do_grad=do_grad,
             par_names=par_names,
@@ -177,15 +176,15 @@
             fixed_vals,
             do_grad=do_grad,
             do_stitch=do_stitch,
         )
 
         # handle non-pyhf ModelConfigs
         try:
-            par_names = pdf.config.par_names()
+            par_names = pdf.config.par_names
         except AttributeError:
             par_names = None
 
         # need to remove parameters that are fixed in the fit
         if par_names and do_stitch and fixed_vals:
             for index, _ in fixed_vals:
                 par_names[index] = None
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/optimize/opt_jax.py` & `pyhf-0.7.1/src/pyhf/optimize/opt_jax.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/optimize/opt_minuit.py` & `pyhf-0.7.1/src/pyhf/optimize/opt_minuit.py`

 * *Files 1% similar despite different names*

```diff
@@ -45,15 +45,14 @@
         objective_and_grad,
         init_pars,
         init_bounds,
         fixed_vals=None,
         do_grad=False,
         par_names=None,
     ):
-
         fixed_vals = fixed_vals or []
         # Minuit wants True/False for each parameter
         fixed_bools = [False] * len(init_pars)
         for index, val in fixed_vals:
             fixed_bools[index] = True
             init_pars[index] = val
 
@@ -78,15 +77,14 @@
         func,
         x0,
         do_grad=False,
         bounds=None,
         fixed_vals=None,
         options={},
     ):
-
         """
         Same signature as :func:`scipy.optimize.minimize`.
 
         Note: an additional `minuit` is injected into the fitresult to get the
         underlying minimizer.
 
         Minimizer Options:
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/optimize/opt_numpy.py` & `pyhf-0.7.1/src/pyhf/optimize/opt_numpy.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/optimize/opt_pytorch.py` & `pyhf-0.7.1/src/pyhf/optimize/opt_pytorch.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/optimize/opt_scipy.py` & `pyhf-0.7.1/src/pyhf/optimize/opt_scipy.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/optimize/opt_tflow.py` & `pyhf-0.7.1/src/pyhf/optimize/opt_tflow.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/parameters/paramsets.py` & `pyhf-0.7.1/src/pyhf/parameters/paramsets.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/parameters/paramview.py` & `pyhf-0.7.1/src/pyhf/parameters/paramview.py`

 * *Files 1% similar despite different names*

```diff
@@ -54,15 +54,14 @@
 
 class ParamViewer:
     """
     Helper class to extract parameter data from possibly batched input
     """
 
     def __init__(self, shape, par_map, par_selection):
-
         default_backend = pyhf.default_backend
 
         batch_size = shape[0] if len(shape) > 1 else None
 
         fullsize = default_backend.product(default_backend.astensor(shape))
         flat_indices = default_backend.astensor(range(int(fullsize)), dtype='int')
         self._all_indices = default_backend.reshape(flat_indices, shape)
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/parameters/utils.py` & `pyhf-0.7.1/src/pyhf/parameters/utils.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/patchset.py` & `pyhf-0.7.1/src/pyhf/patchset.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/pdf.py` & `pyhf-0.7.1/src/pyhf/pdf.py`

 * *Files 0% similar despite different names*

```diff
@@ -354,28 +354,31 @@
             ...     signal=[12.0, 11.0], bkg=[50.0, 52.0], bkg_uncertainty=[3.0, 7.0]
             ... )
             >>> model.config.par_slice("uncorr_bkguncrt")
             slice(1, 3, None)
         """
         return self.par_map[name]['slice']
 
+    @property
     def par_names(self):
         """
         The names of the parameters in the model including binned-parameter indexing.
 
         Returns:
             :obj:`list`: Names of the model parameters.
 
         Example:
             >>> import pyhf
             >>> model = pyhf.simplemodels.uncorrelated_background(
             ...     signal=[12.0, 11.0], bkg=[50.0, 52.0], bkg_uncertainty=[3.0, 7.0]
             ... )
-            >>> model.config.par_names()
+            >>> model.config.par_names
             ['mu', 'uncorr_bkguncrt[0]', 'uncorr_bkguncrt[1]']
+
+        .. versionchanged:: 0.7.0 Changed from method to property attribute.
         """
         _names = []
         for name in self.par_order:
             param_set = self.param_set(name)
             if param_set.is_scalar:
                 _names.append(name)
                 continue
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/probability.py` & `pyhf-0.7.1/src/pyhf/probability.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/readxml.py` & `pyhf-0.7.1/src/pyhf/readxml.py`

 * *Files 1% similar despite different names*

```diff
@@ -275,14 +275,19 @@
     inputfile: str,
     histopath: str,
 ) -> list[float]:
     inputfile = sample.attrib.get('InputFile', inputfile)
     histopath = sample.attrib.get('HistoPath', histopath)
     histoname = sample.attrib['HistoName']
 
+    if inputfile == "" or histoname == "":
+        raise NotImplementedError(
+            "Conversion of workspaces without data is currently not supported.\nSee https://github.com/scikit-hep/pyhf/issues/566"
+        )
+
     data, _ = import_root_histogram(resolver, inputfile, histopath, histoname)
     return data
 
 
 def process_channel(
     channelxml: ET.ElementTree, resolver: ResolverType, track_progress: bool = False
 ) -> tuple[str, list[float], list[Sample], list[Parameter]]:
@@ -462,15 +467,15 @@
     measurements = process_measurements(
         toplvl, other_parameter_configs=parameter_configs
     )
     result: Workspace = {
         'measurements': measurements,
         'channels': channels,
         'observations': observations,
-        'version': schema.version,  # type: ignore[typeddict-item]
+        'version': schema.version,  # type: ignore[typeddict-unknown-key]
     }
     try:
         schema.validate(result, 'workspace.json')
     except exceptions.InvalidSpecification as exc:
         if validation_as_error:
             raise exc
         else:
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/schema/__init__.py` & `pyhf-0.7.1/src/pyhf/schema/__init__.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/schema/loader.py` & `pyhf-0.7.1/src/pyhf/schema/loader.py`

 * *Files 2% similar despite different names*

```diff
@@ -46,15 +46,15 @@
 
     ref = variables.schemas.joinpath(schema_id)
     with resources.as_file(ref) as path:
         if not path.exists():
             raise pyhf.exceptions.SchemaNotFound(
                 f'The schema {schema_id} was not found. Do you have the right version or the right path? {path}'
             )
-        with path.open() as json_schema:
+        with path.open(encoding="utf-8") as json_schema:
             schema = json.load(json_schema)
             variables.SCHEMA_CACHE[schema['$id']] = schema
         return variables.SCHEMA_CACHE[schema['$id']]
 
 
 # pre-populate the cache to avoid network access
 # on first validation in standard usage
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/schema/validator.py` & `pyhf-0.7.1/src/pyhf/schema/validator.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/schemas/1.0.0/defs.json` & `pyhf-0.7.1/src/pyhf/schemas/1.0.0/defs.json`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/schemas/HistFactorySchema.dtd` & `pyhf-0.7.1/src/pyhf/schemas/HistFactorySchema.dtd`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/simplemodels.py` & `pyhf-0.7.1/src/pyhf/simplemodels.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/tensor/__init__.py` & `pyhf-0.7.1/src/pyhf/tensor/__init__.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/tensor/common.py` & `pyhf-0.7.1/src/pyhf/tensor/common.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/tensor/jax_backend.py` & `pyhf-0.7.1/src/pyhf/tensor/jax_backend.py`

 * *Files 2% similar despite different names*

```diff
@@ -80,15 +80,15 @@
 
         Example:
 
             >>> import pyhf
             >>> pyhf.set_backend("jax")
             >>> a = pyhf.tensorlib.astensor([-2, -1, 0, 1, 2])
             >>> pyhf.tensorlib.clip(a, -1, 1)
-            DeviceArray([-1., -1.,  0.,  1.,  1.], dtype=float64)
+            Array([-1., -1.,  0.,  1.,  1.], dtype=float64)
 
         Args:
             tensor_in (:obj:`tensor`): The input tensor object
             min_value (:obj:`scalar` or :obj:`tensor` or :obj:`None`): The minimum value to be cliped to
             max_value (:obj:`scalar` or :obj:`tensor` or :obj:`None`): The maximum value to be cliped to
 
         Returns:
@@ -102,16 +102,15 @@
 
         Example:
 
             >>> import pyhf
             >>> pyhf.set_backend("jax")
             >>> a = pyhf.tensorlib.astensor([-2., -1., 0., 1., 2.])
             >>> pyhf.tensorlib.erf(a)
-            DeviceArray([-0.99532227, -0.84270079,  0.        ,  0.84270079,
-                          0.99532227], dtype=float64)
+            Array([-0.99532227, -0.84270079,  0.        ,  0.84270079,  0.99532227],      dtype=float64)
 
         Args:
             tensor_in (:obj:`tensor`): The input tensor object
 
         Returns:
             JAX ndarray: The values of the error function at the given points.
         """
@@ -123,15 +122,15 @@
 
         Example:
 
             >>> import pyhf
             >>> pyhf.set_backend("jax")
             >>> a = pyhf.tensorlib.astensor([-2., -1., 0., 1., 2.])
             >>> pyhf.tensorlib.erfinv(pyhf.tensorlib.erf(a))
-            DeviceArray([-2., -1.,  0.,  1.,  2.], dtype=float64)
+            Array([-2., -1.,  0.,  1.,  2.], dtype=float64)
 
         Args:
             tensor_in (:obj:`tensor`): The input tensor object
 
         Returns:
             JAX ndarray: The values of the inverse of the error function at the given points.
         """
@@ -143,16 +142,16 @@
 
         Example:
 
             >>> import pyhf
             >>> pyhf.set_backend("jax")
             >>> a = pyhf.tensorlib.astensor([[1.0], [2.0]])
             >>> pyhf.tensorlib.tile(a, (1, 2))
-            DeviceArray([[1., 1.],
-                         [2., 2.]], dtype=float64)
+            Array([[1., 1.],
+                   [2., 2.]], dtype=float64)
 
         Args:
             tensor_in (:obj:`tensor`): The tensor to be repeated
             repeats (:obj:`tensor`): The tuple of multipliers for each dimension
 
         Returns:
             JAX ndarray: The tensor with repeated axes
@@ -167,15 +166,15 @@
 
             >>> import pyhf
             >>> pyhf.set_backend("jax")
             >>> tensorlib = pyhf.tensorlib
             >>> a = tensorlib.astensor([4])
             >>> b = tensorlib.astensor([5])
             >>> tensorlib.conditional((a < b)[0], lambda: a + b, lambda: a - b)
-            DeviceArray([9.], dtype=float64)
+            Array([9.], dtype=float64)
 
         Args:
             predicate (:obj:`scalar`): The logical condition that determines which callable to evaluate
             true_callable (:obj:`callable`): The callable that is evaluated when the :code:`predicate` evaluates to :code:`true`
             false_callable (:obj:`callable`): The callable that is evaluated when the :code:`predicate` evaluates to :code:`false`
 
         Returns:
@@ -209,24 +208,24 @@
 
         Example:
 
             >>> import pyhf
             >>> pyhf.set_backend("jax")
             >>> tensor = pyhf.tensorlib.astensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
             >>> tensor
-            DeviceArray([[1., 2., 3.],
-                         [4., 5., 6.]], dtype=float64)
+            Array([[1., 2., 3.],
+                   [4., 5., 6.]], dtype=float64)
             >>> type(tensor) # doctest:+ELLIPSIS
-            <class '...DeviceArray'>
+            <class '...ArrayImpl'>
 
         Args:
             tensor_in (Number or Tensor): Tensor object
 
         Returns:
-            `jaxlib.xla_extension.DeviceArray`: A multi-dimensional, fixed-size homogeneous array.
+            `jaxlib.xla_extension.ArrayImpl`: A multi-dimensional, fixed-size homogeneous array.
         """
         # TODO: Remove doctest:+ELLIPSIS when JAX API stabilized
         try:
             dtype = self.dtypemap[dtype]
         except KeyError:
             log.error(
                 'Invalid dtype: dtype must be float, int, or bool.', exc_info=True
@@ -290,17 +289,17 @@
         Example:
 
             >>> import pyhf
             >>> import jax.numpy as jnp
             >>> pyhf.set_backend("jax")
             >>> a = pyhf.tensorlib.astensor([[10, 7, 4], [3, 2, 1]])
             >>> pyhf.tensorlib.percentile(a, 50)
-            DeviceArray(3.5, dtype=float64)
+            Array(3.5, dtype=float64)
             >>> pyhf.tensorlib.percentile(a, 50, axis=1)
-            DeviceArray([7., 2.], dtype=float64)
+            Array([7., 2.], dtype=float64)
 
         Args:
             tensor_in (`tensor`): The tensor containing the data
             q (:obj:`float` or `tensor`): The :math:`q`-th percentile to compute
             axis (`number` or `tensor`): The dimensions along which to compute
             interpolation (:obj:`str`): The interpolation method to use when the
              desired percentile lies between two data points ``i < j``:
@@ -315,14 +314,15 @@
                 - ``'midpoint'``: ``(i + j) / 2``.
 
                 - ``'nearest'``: ``i`` or ``j``, whichever is nearest.
 
         Returns:
             JAX ndarray: The value of the :math:`q`-th percentile of the tensor along the specified axis.
 
+        .. versionadded:: 0.7.0
         """
         return jnp.percentile(tensor_in, q, axis=axis, interpolation=interpolation)
 
     def stack(self, sequence, axis=0):
         return jnp.stack(sequence, axis=axis)
 
     def where(self, mask, tensor_in_1, tensor_in_2):
@@ -350,15 +350,15 @@
 
             >>> import pyhf
             >>> pyhf.set_backend("jax")
             >>> pyhf.tensorlib.simple_broadcast(
             ...   pyhf.tensorlib.astensor([1]),
             ...   pyhf.tensorlib.astensor([2, 3, 4]),
             ...   pyhf.tensorlib.astensor([5, 6, 7]))
-            [DeviceArray([1., 1., 1.], dtype=float64), DeviceArray([2., 3., 4.], dtype=float64), DeviceArray([5., 6., 7.], dtype=float64)]
+            [Array([1., 1., 1.], dtype=float64), Array([2., 3., 4.], dtype=float64), Array([5., 6., 7.], dtype=float64)]
 
         Args:
             args (Array of Tensors): Sequence of arrays
 
         Returns:
             list of Tensors: The sequence broadcast together.
         """
@@ -376,21 +376,21 @@
 
         Example:
 
             >>> import pyhf
             >>> pyhf.set_backend("jax")
             >>> tensor = pyhf.tensorlib.astensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
             >>> pyhf.tensorlib.ravel(tensor)
-            DeviceArray([1., 2., 3., 4., 5., 6.], dtype=float64)
+            Array([1., 2., 3., 4., 5., 6.], dtype=float64)
 
         Args:
             tensor (Tensor): Tensor object
 
         Returns:
-            `jaxlib.xla_extension.DeviceArray`: A flattened array.
+            `jaxlib.xla_extension.Array`: A flattened array.
         """
         return jnp.ravel(tensor)
 
     def einsum(self, subscripts, *operands):
         """
         Evaluates the Einstein summation convention on the operands.
 
@@ -436,19 +436,19 @@
                 \end{array}\right.
 
         Example:
 
             >>> import pyhf
             >>> pyhf.set_backend("jax")
             >>> pyhf.tensorlib.poisson(5., 6.)
-            DeviceArray(0.16062314, dtype=float64, weak_type=True)
+            Array(0.16062314, dtype=float64, weak_type=True)
             >>> values = pyhf.tensorlib.astensor([5., 9.])
             >>> rates = pyhf.tensorlib.astensor([6., 8.])
             >>> pyhf.tensorlib.poisson(values, rates)
-            DeviceArray([0.16062314, 0.12407692], dtype=float64)
+            Array([0.16062314, 0.12407692], dtype=float64)
 
         Args:
             n (:obj:`tensor` or :obj:`float`): The value at which to evaluate the approximation to the Poisson distribution p.m.f.
                                   (the observed number of events)
             lam (:obj:`tensor` or :obj:`float`): The mean of the Poisson distribution p.m.f.
                                     (the expected number of events)
 
@@ -479,20 +479,20 @@
         of :code:`sigma`.
 
         Example:
 
             >>> import pyhf
             >>> pyhf.set_backend("jax")
             >>> pyhf.tensorlib.normal(0.5, 0., 1.)
-            DeviceArray(0.35206533, dtype=float64, weak_type=True)
+            Array(0.35206533, dtype=float64, weak_type=True)
             >>> values = pyhf.tensorlib.astensor([0.5, 2.0])
             >>> means = pyhf.tensorlib.astensor([0., 2.3])
             >>> sigmas = pyhf.tensorlib.astensor([1., 0.8])
             >>> pyhf.tensorlib.normal(values, means, sigmas)
-            DeviceArray([0.35206533, 0.46481887], dtype=float64)
+            Array([0.35206533, 0.46481887], dtype=float64)
 
         Args:
             x (:obj:`tensor` or :obj:`float`): The value at which to evaluate the Normal distribution p.d.f.
             mu (:obj:`tensor` or :obj:`float`): The mean of the Normal distribution
             sigma (:obj:`tensor` or :obj:`float`): The standard deviation of the Normal distribution
 
         Returns:
@@ -505,18 +505,18 @@
         The cumulative distribution function for the Normal distribution
 
         Example:
 
             >>> import pyhf
             >>> pyhf.set_backend("jax")
             >>> pyhf.tensorlib.normal_cdf(0.8)
-            DeviceArray(0.7881446, dtype=float64)
+            Array(0.7881446, dtype=float64)
             >>> values = pyhf.tensorlib.astensor([0.8, 2.0])
             >>> pyhf.tensorlib.normal_cdf(values)
-            DeviceArray([0.7881446 , 0.97724987], dtype=float64)
+            Array([0.7881446 , 0.97724987], dtype=float64)
 
         Args:
             x (:obj:`tensor` or :obj:`float`): The observed value of the random variable to evaluate the CDF for
             mu (:obj:`tensor` or :obj:`float`): The mean of the Normal distribution
             sigma (:obj:`tensor` or :obj:`float`): The standard deviation of the Normal distribution
 
         Returns:
@@ -531,15 +531,15 @@
         Example:
             >>> import pyhf
             >>> pyhf.set_backend("jax")
             >>> rates = pyhf.tensorlib.astensor([5, 8])
             >>> values = pyhf.tensorlib.astensor([4, 9])
             >>> poissons = pyhf.tensorlib.poisson_dist(rates)
             >>> poissons.log_prob(values)
-            DeviceArray([-1.74030218, -2.0868536 ], dtype=float64)
+            Array([-1.74030218, -2.0868536 ], dtype=float64)
 
         Args:
             rate (:obj:`tensor` or :obj:`float`): The mean of the Poisson distribution (the expected number of events)
 
         Returns:
             Poisson distribution: The Poisson distribution class
         """
@@ -553,15 +553,15 @@
             >>> import pyhf
             >>> pyhf.set_backend("jax")
             >>> means = pyhf.tensorlib.astensor([5, 8])
             >>> stds = pyhf.tensorlib.astensor([1, 0.5])
             >>> values = pyhf.tensorlib.astensor([4, 9])
             >>> normals = pyhf.tensorlib.normal_dist(means, stds)
             >>> normals.log_prob(values)
-            DeviceArray([-1.41893853, -2.22579135], dtype=float64)
+            Array([-1.41893853, -2.22579135], dtype=float64)
 
         Args:
             mu (:obj:`tensor` or :obj:`float`): The mean of the Normal distribution
             sigma (:obj:`tensor` or :obj:`float`): The standard deviation of the Normal distribution
 
         Returns:
             Normal distribution: The Normal distribution class
@@ -574,16 +574,16 @@
         Convert the JAX tensor to a :class:`numpy.ndarray`.
 
         Example:
             >>> import pyhf
             >>> pyhf.set_backend("jax")
             >>> tensor = pyhf.tensorlib.astensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
             >>> tensor
-            DeviceArray([[1., 2., 3.],
-                         [4., 5., 6.]], dtype=float64)
+            Array([[1., 2., 3.],
+                   [4., 5., 6.]], dtype=float64)
             >>> numpy_ndarray = pyhf.tensorlib.to_numpy(tensor)
             >>> numpy_ndarray
             array([[1., 2., 3.],
                    [4., 5., 6.]])
             >>> type(numpy_ndarray)
             <class 'numpy.ndarray'>
 
@@ -601,22 +601,23 @@
         Transpose the tensor.
 
         Example:
             >>> import pyhf
             >>> pyhf.set_backend("jax")
             >>> tensor = pyhf.tensorlib.astensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
             >>> tensor
-            DeviceArray([[1., 2., 3.],
-                         [4., 5., 6.]], dtype=float64)
+            Array([[1., 2., 3.],
+                   [4., 5., 6.]], dtype=float64)
             >>> pyhf.tensorlib.transpose(tensor)
-            DeviceArray([[1., 4.],
-                         [2., 5.],
-                         [3., 6.]], dtype=float64)
+            Array([[1., 4.],
+                   [2., 5.],
+                   [3., 6.]], dtype=float64)
 
         Args:
             tensor_in (:obj:`tensor`): The input tensor object.
 
         Returns:
             JAX ndarray: The transpose of the input tensor.
 
+        .. versionadded:: 0.7.0
         """
         return tensor_in.transpose()
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/tensor/manager.py` & `pyhf-0.7.1/src/pyhf/tensor/manager.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/tensor/numpy_backend.py` & `pyhf-0.7.1/src/pyhf/tensor/numpy_backend.py`

 * *Files 1% similar despite different names*

```diff
@@ -199,18 +199,18 @@
                 return tensor_in
             raise
 
     def outer(self, tensor_in_1: Tensor[T], tensor_in_2: Tensor[T]) -> ArrayLike:
         return np.outer(tensor_in_1, tensor_in_2)  # type: ignore[arg-type]
 
     def gather(self, tensor: Tensor[T], indices: NDArray[np.integer[T]]) -> ArrayLike:
-        return tensor[indices]  # type: ignore[no-any-return]
+        return tensor[indices]
 
     def boolean_mask(self, tensor: Tensor[T], mask: NDArray[np.bool_]) -> ArrayLike:
-        return tensor[mask]  # type: ignore[no-any-return]
+        return tensor[mask]
 
     def isfinite(self, tensor: Tensor[T]) -> NDArray[np.bool_]:
         return np.isfinite(tensor)
 
     def astensor(
         self, tensor_in: ArrayLike, dtype: FloatIntOrBool = 'float'
     ) -> ArrayLike:
@@ -331,14 +331,15 @@
                 - ``'midpoint'``: ``(i + j) / 2``.
 
                 - ``'nearest'``: ``i`` or ``j``, whichever is nearest.
 
         Returns:
             NumPy ndarray: The value of the :math:`q`-th percentile of the tensor along the specified axis.
 
+        .. versionadded:: 0.7.0
         """
         # see https://github.com/numpy/numpy/issues/22125
         return np.percentile(tensor_in, q, axis=axis, interpolation=interpolation)  # type: ignore[call-overload,no-any-return]
 
     def stack(self, sequence: Sequence[Tensor[T]], axis: int = 0) -> ArrayLike:
         return np.stack(sequence, axis=axis)
 
@@ -633,9 +634,10 @@
 
         Args:
             tensor_in (:obj:`tensor`): The input tensor object.
 
         Returns:
             :class:`numpy.ndarray`: The transpose of the input tensor.
 
+        .. versionadded:: 0.7.0
         """
         return tensor_in.transpose()
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/tensor/pytorch_backend.py` & `pyhf-0.7.1/src/pyhf/tensor/pytorch_backend.py`

 * *Files 2% similar despite different names*

```diff
@@ -321,14 +321,15 @@
                 - ``'midpoint'``: Not yet implemented in PyTorch.
 
                 - ``'nearest'``: Not yet implemented in PyTorch.
 
         Returns:
             PyTorch tensor: The value of the :math:`q`-th percentile of the tensor along the specified axis.
 
+        .. versionadded:: 0.7.0
         """
         # Interpolation options not yet supported
         # c.f. https://github.com/pytorch/pytorch/pull/49267
         # c.f. https://github.com/pytorch/pytorch/pull/59397
         return torch.quantile(tensor_in, q / 100, dim=axis)
 
     def stack(self, sequence, axis=0):
@@ -617,9 +618,10 @@
 
         Args:
             tensor_in (:obj:`tensor`): The input tensor object.
 
         Returns:
             PyTorch FloatTensor: The transpose of the input tensor.
 
+        .. versionadded:: 0.7.0
         """
         return tensor_in.transpose(0, 1)
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/tensor/tensorflow_backend.py` & `pyhf-0.7.1/src/pyhf/tensor/tensorflow_backend.py`

 * *Files 0% similar despite different names*

```diff
@@ -342,14 +342,15 @@
                 - ``'midpoint'``: ``(i + j) / 2``.
 
                 - ``'nearest'``: ``i`` or ``j``, whichever is nearest.
 
         Returns:
             TensorFlow Tensor: The value of the :math:`q`-th percentile of the tensor along the specified axis.
 
+        .. versionadded:: 0.7.0
         """
         return tfp.stats.percentile(
             tensor_in, q, axis=axis, interpolation=interpolation
         )
 
     def stack(self, sequence, axis=0):
         return tf.stack(sequence, axis=axis)
@@ -714,9 +715,10 @@
 
         Args:
             tensor_in (:obj:`tensor`): The input tensor object.
 
         Returns:
             TensorFlow Tensor: The transpose of the input tensor.
 
+        .. versionadded:: 0.7.0
         """
         return tf.transpose(tensor_in)
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/typing.py` & `pyhf-0.7.1/src/pyhf/typing.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/utils.py` & `pyhf-0.7.1/src/pyhf/utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -107,15 +107,15 @@
     """
     Get the bibtex citation for pyhf
 
     Example:
 
         >>> import pyhf
         >>> pyhf.utils.citation(oneline=True)
-        '@software{pyhf,  author = {Lukas Heinrich and Matthew Feickert and Giordon Stark},  title = "{pyhf: v0.7.0rc4}",  version = {0.7.0rc4},  doi = {10.5281/zenodo.1169739},  url = {https://doi.org/10.5281/zenodo.1169739},  note = {https://github.com/scikit-hep/pyhf/releases/tag/v0.7.0rc4}}@article{pyhf_joss,  doi = {10.21105/joss.02823},  url = {https://doi.org/10.21105/joss.02823},  year = {2021},  publisher = {The Open Journal},  volume = {6},  number = {58},  pages = {2823},  author = {Lukas Heinrich and Matthew Feickert and Giordon Stark and Kyle Cranmer},  title = {pyhf: pure-Python implementation of HistFactory statistical models},  journal = {Journal of Open Source Software}}'
+        '@software{pyhf,  author = {Lukas Heinrich and Matthew Feickert and Giordon Stark},  title = "{pyhf: v0.7.1}",  version = {0.7.1},  doi = {10.5281/zenodo.1169739},  url = {https://doi.org/10.5281/zenodo.1169739},  note = {https://github.com/scikit-hep/pyhf/releases/tag/v0.7.1}}@article{pyhf_joss,  doi = {10.21105/joss.02823},  url = {https://doi.org/10.21105/joss.02823},  year = {2021},  publisher = {The Open Journal},  volume = {6},  number = {58},  pages = {2823},  author = {Lukas Heinrich and Matthew Feickert and Giordon Stark and Kyle Cranmer},  title = {pyhf: pure-Python implementation of HistFactory statistical models},  journal = {Journal of Open Source Software}}'
 
     Keyword Args:
         oneline (:obj:`bool`): Whether to provide citation with new lines (default) or as a one-liner.
 
     Returns:
         citation (:obj:`str`): The citation for this software
     """
```

### Comparing `pyhf-0.7.0rc4/src/pyhf/workspace.py` & `pyhf-0.7.1/src/pyhf/workspace.py`

 * *Files identical despite different names*

### Comparing `pyhf-0.7.0rc4/src/pyhf/writexml.py` & `pyhf-0.7.1/src/pyhf/writexml.py`

 * *Files 1% similar despite different names*

```diff
@@ -285,15 +285,15 @@
     )
 
     with uproot.recreate(Path(data_rootdir).joinpath('data.root')) as _ROOT_DATA_FILE:
         for channelspec in spec['channels']:
             channelfilename = str(
                 Path(specdir).joinpath(f'{resultprefix}_{channelspec["name"]}.xml')
             )
-            with open(channelfilename, 'w') as channelfile:
+            with open(channelfilename, "w", encoding="utf-8") as channelfile:
                 channel = build_channel(spec, channelspec, spec.get('observations'))
                 indent(channel)
                 channelfile.write(
                     "<!DOCTYPE Channel SYSTEM '../HistFactorySchema.dtd'>\n\n"
                 )
                 channelfile.write(
                     ET.tostring(channel, encoding='utf-8').decode('utf-8')
```

### Comparing `pyhf-0.7.0rc4/src/pyhf.egg-info/PKG-INFO` & `pyhf-0.7.1/PKG-INFO`

 * *Files 25% similar despite different names*

```diff
@@ -1,59 +1,116 @@
 Metadata-Version: 2.1
 Name: pyhf
-Version: 0.7.0rc4
+Version: 0.7.1
 Summary: pure-Python HistFactory implementation with tensors and autodiff
-Home-page: https://github.com/scikit-hep/pyhf
-Author: Lukas Heinrich, Matthew Feickert, Giordon Stark
-Author-email: lukas.heinrich@cern.ch, matthew.feickert@cern.ch, gstark@cern.ch
-License: Apache
 Project-URL: Documentation, https://pyhf.readthedocs.io/
-Project-URL: Source Code, https://github.com/scikit-hep/pyhf
+Project-URL: Homepage, https://github.com/scikit-hep/pyhf
 Project-URL: Issue Tracker, https://github.com/scikit-hep/pyhf/issues
 Project-URL: Release Notes, https://pyhf.readthedocs.io/en/stable/release-notes.html
-Keywords: physics fitting numpy scipy tensorflow pytorch jax
+Project-URL: Releases, https://github.com/scikit-hep/pyhf/releases
+Project-URL: Source Code, https://github.com/scikit-hep/pyhf
+Author-email: Lukas Heinrich <lukas.heinrich@cern.ch>, Matthew Feickert <matthew.feickert@cern.ch>, Giordon Stark <gstark@cern.ch>
+Maintainer-email: The Scikit-HEP admins <scikit-hep-admins@googlegroups.com>
+License: Apache-2.0
+License-File: AUTHORS
+License-File: LICENSE
+Keywords: fitting,jax,numpy,physics,pytorch,scipy,tensorflow
 Classifier: Development Status :: 4 - Beta
-Classifier: License :: OSI Approved :: Apache Software License
+Classifier: Environment :: WebAssembly :: Emscripten
 Classifier: Intended Audience :: Science/Research
-Classifier: Topic :: Scientific/Engineering
-Classifier: Topic :: Scientific/Engineering :: Physics
+Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: Implementation :: CPython
+Classifier: Topic :: Scientific/Engineering
+Classifier: Topic :: Scientific/Engineering :: Physics
 Requires-Python: >=3.7
-Description-Content-Type: text/x-rst
+Requires-Dist: click>=8.0.0
+Requires-Dist: importlib-resources>=1.4.0; python_version < '3.9'
+Requires-Dist: jsonpatch>=1.15
+Requires-Dist: jsonschema>=4.15.0
+Requires-Dist: numpy
+Requires-Dist: pyyaml>=5.1
+Requires-Dist: scipy>=1.2.0
+Requires-Dist: tqdm>=4.56.0
+Requires-Dist: typing-extensions>=3.7.4.3; python_version == '3.7'
+Provides-Extra: all
+Requires-Dist: pyhf[backends,contrib,shellcomplete,xmlio]; extra == 'all'
+Provides-Extra: backends
+Requires-Dist: pyhf[jax,minuit,tensorflow,torch]; extra == 'backends'
+Provides-Extra: contrib
+Requires-Dist: matplotlib>=3.0.0; extra == 'contrib'
+Requires-Dist: requests>=2.22.0; extra == 'contrib'
+Provides-Extra: develop
+Requires-Dist: codemetapy>=2.3.0; extra == 'develop'
+Requires-Dist: nox; extra == 'develop'
+Requires-Dist: pre-commit; extra == 'develop'
+Requires-Dist: pyhf[docs,test]; extra == 'develop'
+Requires-Dist: tbump>=6.7.0; extra == 'develop'
+Provides-Extra: docs
+Requires-Dist: ipython!=8.7.0; extra == 'docs'
+Requires-Dist: ipywidgets; extra == 'docs'
+Requires-Dist: nbsphinx!=0.8.8; extra == 'docs'
+Requires-Dist: pyhf[contrib,xmlio]; extra == 'docs'
+Requires-Dist: sphinx-click; extra == 'docs'
+Requires-Dist: sphinx-copybutton>=0.3.2; extra == 'docs'
+Requires-Dist: sphinx-issues; extra == 'docs'
+Requires-Dist: sphinx-rtd-theme; extra == 'docs'
+Requires-Dist: sphinx-togglebutton>=0.3.0; extra == 'docs'
+Requires-Dist: sphinx>=5.1.1; extra == 'docs'
+Requires-Dist: sphinxcontrib-bibtex~=2.1; extra == 'docs'
+Provides-Extra: jax
+Requires-Dist: jax>=0.2.10; extra == 'jax'
+Requires-Dist: jaxlib!=0.1.68,>=0.1.61; extra == 'jax'
+Provides-Extra: minuit
+Requires-Dist: iminuit>=2.7.0; extra == 'minuit'
 Provides-Extra: shellcomplete
+Requires-Dist: click-completion; extra == 'shellcomplete'
 Provides-Extra: tensorflow
+Requires-Dist: tensorflow-macos>=2.7.0; platform_machine == 'arm64' and platform_system == 'Darwin' and extra == 'tensorflow'
+Requires-Dist: tensorflow-probability>=0.11.0; extra == 'tensorflow'
+Requires-Dist: tensorflow>=2.7.0; platform_machine != 'arm64' and extra == 'tensorflow'
+Provides-Extra: test
+Requires-Dist: graphviz; extra == 'test'
+Requires-Dist: jupyter; extra == 'test'
+Requires-Dist: papermill~=2.3.4; extra == 'test'
+Requires-Dist: pydocstyle; extra == 'test'
+Requires-Dist: pyhf[all]; extra == 'test'
+Requires-Dist: pytest-benchmark[histogram]; extra == 'test'
+Requires-Dist: pytest-console-scripts; extra == 'test'
+Requires-Dist: pytest-cov>=2.5.1; extra == 'test'
+Requires-Dist: pytest-mock; extra == 'test'
+Requires-Dist: pytest-mpl; extra == 'test'
+Requires-Dist: pytest-socket>=0.2.0; extra == 'test'
+Requires-Dist: pytest>=6.0; extra == 'test'
+Requires-Dist: requests-mock>=1.9.0; extra == 'test'
+Requires-Dist: scikit-hep-testdata>=0.4.11; extra == 'test'
+Requires-Dist: scrapbook~=0.5.0; extra == 'test'
 Provides-Extra: torch
-Provides-Extra: jax
+Requires-Dist: torch>=1.10.0; extra == 'torch'
 Provides-Extra: xmlio
-Provides-Extra: minuit
-Provides-Extra: backends
-Provides-Extra: contrib
-Provides-Extra: test
-Provides-Extra: docs
-Provides-Extra: develop
-Provides-Extra: complete
-License-File: LICENSE
+Requires-Dist: uproot>=4.1.1; extra == 'xmlio'
+Description-Content-Type: text/x-rst
 
-.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/_static/img/pyhf-logo-small.png
+.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/_static/img/pyhf-logo-small.png
    :alt: pyhf logo
    :width: 320
    :align: center
 
 pure-python fitting/limit-setting/interval estimation HistFactory-style
 =======================================================================
 
 |GitHub Project| |DOI| |JOSS DOI| |Scikit-HEP| |NSF Award Number|
 
-|Docs from latest| |Docs from master| |Jupyter Book tutorial| |Binder|
+|Docs from latest| |Docs from main| |Jupyter Book tutorial| |Binder|
 
 |PyPI version| |Conda-forge version| |Supported Python versions| |Docker Hub pyhf| |Docker Hub pyhf CUDA|
 
 |Code Coverage| |CodeFactor| |pre-commit.ci Status| |Code style: black|
 
 |GitHub Actions Status: CI| |GitHub Actions Status: Docs| |GitHub Actions Status: Publish|
 |GitHub Actions Status: Docker|
@@ -107,15 +164,15 @@
 Alternatively the statistical model and observational data can be read from its serialized JSON representation (see next section).
 
 .. code:: pycon
 
    >>> import pyhf
    >>> import requests
    >>> pyhf.set_backend("numpy")
-   >>> url = "https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/examples/json/2-bin_1-channel.json"
+   >>> url = "https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/examples/json/2-bin_1-channel.json"
    >>> wspace = pyhf.Workspace(requests.get(url).json())
    >>> model = wspace.model()
    >>> data = wspace.data(model)
    >>> test_mu = 1.0
    >>> CLs_obs, CLs_exp = pyhf.infer.hypotest(
    ...     test_mu, data, model, test_stat="qtilde", return_expected=True
    ... )
@@ -231,22 +288,22 @@
    fig, ax = plt.subplots()
    fig.set_size_inches(7, 5)
    brazil.plot_results(poi_vals, results, ax=ax)
    fig.show()
 
 **pyhf**
 
-.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/_static/img/README_1bin_example.png
+.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/_static/img/README_1bin_example.png
    :alt: manual
    :width: 500
    :align: center
 
 **ROOT**
 
-.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/_static/img/hfh_1bin_55_50_7.png
+.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/_static/img/hfh_1bin_55_50_7.png
    :alt: manual
    :width: 500
    :align: center
 
 A two bin example
 -----------------
 
@@ -275,22 +332,22 @@
    fig.set_size_inches(7, 5)
    brazil.plot_results(poi_vals, results, ax=ax)
    fig.show()
 
 
 **pyhf**
 
-.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/_static/img/README_2bin_example.png
+.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/_static/img/README_2bin_example.png
    :alt: manual
    :width: 500
    :align: center
 
 **ROOT**
 
-.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/_static/img/hfh_2_bin_100.0_145.0_100.0_150.0_15.0_20.0_30.0_45.0.png
+.. image:: https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/_static/img/hfh_2_bin_100.0_145.0_100.0_150.0_15.0_20.0_30.0_45.0.png
    :alt: manual
    :width: 500
    :align: center
 
 Installation
 ------------
 
@@ -346,19 +403,19 @@
 `Zenodo <https://zenodo.org/>`__ archive and the
 `JOSS <https://joss.theoj.org/>`__ paper:
 
 .. code:: bibtex
 
    @software{pyhf,
      author = {Lukas Heinrich and Matthew Feickert and Giordon Stark},
-     title = "{pyhf: v0.7.0rc4}",
-     version = {0.7.0rc4},
+     title = "{pyhf: v0.7.1}",
+     version = {0.7.1},
      doi = {10.5281/zenodo.1169739},
      url = {https://doi.org/10.5281/zenodo.1169739},
-     note = {https://github.com/scikit-hep/pyhf/releases/tag/v0.7.0rc4}
+     note = {https://github.com/scikit-hep/pyhf/releases/tag/v0.7.1}
    }
 
    @article{pyhf_joss,
      doi = {10.21105/joss.02823},
      url = {https://doi.org/10.21105/joss.02823},
      year = {2021},
      publisher = {The Open Journal},
@@ -377,14 +434,15 @@
 
 Please check the `contribution statistics for a list of
 contributors <https://github.com/scikit-hep/pyhf/graphs/contributors>`__.
 
 Milestones
 ----------
 
+- 2022-09-12: 2000 GitHub issues and pull requests. (See PR `#2000 <https://github.com/scikit-hep/pyhf/pull/2000>`__)
 - 2021-12-09: 1000 commits to the project. (See PR `#1710 <https://github.com/scikit-hep/pyhf/pull/1710>`__)
 - 2020-07-28: 1000 GitHub issues and pull requests. (See PR `#1000 <https://github.com/scikit-hep/pyhf/pull/1000>`__)
 
 Acknowledgements
 ----------------
 
 Matthew Feickert has received support to work on ``pyhf`` provided by NSF
@@ -397,45 +455,45 @@
    :target: https://doi.org/10.5281/zenodo.1169739
 .. |JOSS DOI| image:: https://joss.theoj.org/papers/10.21105/joss.02823/status.svg
    :target: https://doi.org/10.21105/joss.02823
 .. |Scikit-HEP| image:: https://scikit-hep.org/assets/images/Scikit--HEP-Project-blue.svg
    :target: https://scikit-hep.org/
 .. |NSF Award Number| image:: https://img.shields.io/badge/NSF-1836650-blue.svg
    :target: https://nsf.gov/awardsearch/showAward?AWD_ID=1836650
-.. |Docs from latest| image:: https://img.shields.io/badge/docs-v0.7.0rc4-blue.svg
+.. |Docs from latest| image:: https://img.shields.io/badge/docs-v0.7.1-blue.svg
    :target: https://pyhf.readthedocs.io/
-.. |Docs from master| image:: https://img.shields.io/badge/docs-master-blue.svg
+.. |Docs from main| image:: https://img.shields.io/badge/docs-main-blue.svg
    :target: https://scikit-hep.github.io/pyhf
 .. |Jupyter Book tutorial| image:: https://jupyterbook.org/_images/badge.svg
    :target: https://pyhf.github.io/pyhf-tutorial/
 .. |Binder| image:: https://mybinder.org/badge_logo.svg
-   :target: https://mybinder.org/v2/gh/scikit-hep/pyhf/master?filepath=docs%2Fexamples%2Fnotebooks%2Fbinderexample%2FStatisticalAnalysis.ipynb
+   :target: https://mybinder.org/v2/gh/scikit-hep/pyhf/main?filepath=docs%2Fexamples%2Fnotebooks%2Fbinderexample%2FStatisticalAnalysis.ipynb
 
 .. |PyPI version| image:: https://badge.fury.io/py/pyhf.svg
    :target: https://badge.fury.io/py/pyhf
 .. |Conda-forge version| image:: https://img.shields.io/conda/vn/conda-forge/pyhf.svg
    :target: https://github.com/conda-forge/pyhf-feedstock
 .. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/pyhf.svg
    :target: https://pypi.org/project/pyhf/
-.. |Docker Hub pyhf| image:: https://img.shields.io/badge/pyhf-v0.7.0rc4-blue?logo=Docker
+.. |Docker Hub pyhf| image:: https://img.shields.io/badge/pyhf-v0.7.1-blue?logo=Docker
    :target: https://hub.docker.com/r/pyhf/pyhf/tags
 .. |Docker Hub pyhf CUDA| image:: https://img.shields.io/badge/pyhf-CUDA-blue?logo=Docker
    :target: https://hub.docker.com/r/pyhf/cuda/tags
 
-.. |Code Coverage| image:: https://codecov.io/gh/scikit-hep/pyhf/graph/badge.svg?branch=master
-   :target: https://codecov.io/gh/scikit-hep/pyhf?branch=master
+.. |Code Coverage| image:: https://codecov.io/gh/scikit-hep/pyhf/graph/badge.svg?branch=main
+   :target: https://codecov.io/gh/scikit-hep/pyhf?branch=main
 .. |CodeFactor| image:: https://www.codefactor.io/repository/github/scikit-hep/pyhf/badge
    :target: https://www.codefactor.io/repository/github/scikit-hep/pyhf
-.. |pre-commit.ci Status| image:: https://results.pre-commit.ci/badge/github/scikit-hep/pyhf/master.svg
-  :target: https://results.pre-commit.ci/latest/github/scikit-hep/pyhf/master
+.. |pre-commit.ci Status| image:: https://results.pre-commit.ci/badge/github/scikit-hep/pyhf/main.svg
+  :target: https://results.pre-commit.ci/latest/github/scikit-hep/pyhf/main
   :alt: pre-commit.ci status
 .. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
 
-.. |GitHub Actions Status: CI| image:: https://github.com/scikit-hep/pyhf/workflows/CI/CD/badge.svg?branch=master
-   :target: https://github.com/scikit-hep/pyhf/actions?query=workflow%3ACI%2FCD+branch%3Amaster
-.. |GitHub Actions Status: Docs| image:: https://github.com/scikit-hep/pyhf/workflows/Docs/badge.svg?branch=master
-   :target: https://github.com/scikit-hep/pyhf/actions?query=workflow%3ADocs+branch%3Amaster
-.. |GitHub Actions Status: Publish| image:: https://github.com/scikit-hep/pyhf/workflows/publish%20distributions/badge.svg?branch=master
-   :target: https://github.com/scikit-hep/pyhf/actions?query=workflow%3A%22publish+distributions%22+branch%3Amaster
-.. |GitHub Actions Status: Docker| image:: https://github.com/scikit-hep/pyhf/actions/workflows/docker.yml/badge.svg?branch=master
-   :target: https://github.com/scikit-hep/pyhf/actions/workflows/docker.yml?query=branch%3Amaster
+.. |GitHub Actions Status: CI| image:: https://github.com/scikit-hep/pyhf/workflows/CI/CD/badge.svg?branch=main
+   :target: https://github.com/scikit-hep/pyhf/actions?query=workflow%3ACI%2FCD+branch%3Amain
+.. |GitHub Actions Status: Docs| image:: https://github.com/scikit-hep/pyhf/workflows/Docs/badge.svg?branch=main
+   :target: https://github.com/scikit-hep/pyhf/actions?query=workflow%3ADocs+branch%3Amain
+.. |GitHub Actions Status: Publish| image:: https://github.com/scikit-hep/pyhf/workflows/publish%20distributions/badge.svg?branch=main
+   :target: https://github.com/scikit-hep/pyhf/actions?query=workflow%3A%22publish+distributions%22+branch%3Amain
+.. |GitHub Actions Status: Docker| image:: https://github.com/scikit-hep/pyhf/actions/workflows/docker.yml/badge.svg?branch=main
+   :target: https://github.com/scikit-hep/pyhf/actions/workflows/docker.yml?query=branch%3Amain
```

