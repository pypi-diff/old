# Comparing `tmp/dragonfly-uwg-0.5.98.tar.gz` & `tmp/dragonfly-uwg-0.5.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/dragonfly-uwg-0.5.98.tar", last modified: Wed Oct  6 15:48:11 2021, max compression
+gzip compressed data, was "dist/dragonfly-uwg-0.5.99.tar", last modified: Fri Oct  8 18:36:50 2021, max compression
```

## Comparing `dragonfly-uwg-0.5.98.tar` & `dragonfly-uwg-0.5.99.tar`

### file list

```diff
@@ -1,96 +1,96 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/.github/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (121)     3569 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/.github/workflows/ci.yaml
--rw-r--r--   0 runner    (1001) docker     (121)     1904 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/.github/workflows/dependency-release.yaml
--rw-r--r--   0 runner    (1001) docker     (121)      142 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/.gitignore
--rw-r--r--   0 runner    (1001) docker     (121)      294 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/.releaserc.json
--rw-r--r--   0 runner    (1001) docker     (121)      279 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/CODE_OF_CONDUCT.md
--rw-r--r--   0 runner    (1001) docker     (121)      445 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/CONTRIBUTING.md
--rw-r--r--   0 runner    (1001) docker     (121)    34523 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     2392 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1707 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      165 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/deploy.sh
--rw-r--r--   0 runner    (1001) docker     (121)      698 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dev-requirements.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/docs/
--rw-r--r--   0 runner    (1001) docker     (121)      373 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/docs/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/docs/_build/
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/docs/_build/.nojekyll
--rw-r--r--   0 runner    (1001) docker     (121)       16 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/docs/_build/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/docs/_build/docs/
--rw-r--r--   0 runner    (1001) docker     (121)       16 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/docs/_build/docs/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/docs/_static/
--rw-r--r--   0 runner    (1001) docker     (121)      899 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/docs/_static/custom.css
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/docs/_templates/
--rw-r--r--   0 runner    (1001) docker     (121)     3668 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/docs/_templates/layout.html
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/docs/cli/
--rw-r--r--   0 runner    (1001) docker     (121)      127 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/docs/cli/index.rst
--rw-r--r--   0 runner    (1001) docker     (121)    15975 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/docs/conf.py
--rw-r--r--   0 runner    (1001) docker     (121)      822 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/docs/index.rst
--rw-r--r--   0 runner    (1001) docker     (121)       80 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/docs/modules.rst
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/
--rw-r--r--   0 runner    (1001) docker     (121)      229 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)       72 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/__main__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1863 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/_extend_dragonfly.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/cli/
--rw-r--r--   0 runner    (1001) docker     (121)      393 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3086 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/cli/simulate.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/properties/
--rw-r--r--   0 runner    (1001) docker     (121)       32 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/properties/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2841 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/properties/_refdefaults.py
--rw-r--r--   0 runner    (1001) docker     (121)    12434 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/properties/building.py
--rw-r--r--   0 runner    (1001) docker     (121)     3224 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/properties/context.py
--rw-r--r--   0 runner    (1001) docker     (121)    17716 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/properties/model.py
--rw-r--r--   0 runner    (1001) docker     (121)     2358 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/properties/room2d.py
--rw-r--r--   0 runner    (1001) docker     (121)     2338 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/properties/story.py
--rw-r--r--   0 runner    (1001) docker     (121)     5679 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/run.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/simulation/
--rw-r--r--   0 runner    (1001) docker     (121)       49 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/simulation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6662 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/simulation/boundary.py
--rw-r--r--   0 runner    (1001) docker     (121)    12680 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/simulation/parameter.py
--rw-r--r--   0 runner    (1001) docker     (121)     5150 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/simulation/refsite.py
--rw-r--r--   0 runner    (1001) docker     (121)     5061 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/simulation/runperiod.py
--rw-r--r--   0 runner    (1001) docker     (121)     6988 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/simulation/vegetation.py
--rw-r--r--   0 runner    (1001) docker     (121)    12766 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/terrain.py
--rw-r--r--   0 runner    (1001) docker     (121)     7595 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/traffic.py
--rw-r--r--   0 runner    (1001) docker     (121)     2077 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/dragonfly_uwg/writer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/dragonfly_uwg.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     2392 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/dragonfly_uwg.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2014 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/dragonfly_uwg.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/dragonfly_uwg.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       57 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/dragonfly_uwg.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)       35 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/dragonfly_uwg.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       20 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/dragonfly_uwg.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       35 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (121)      102 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1176 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/tests/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1804 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/boundary_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     2920 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/building_extend_test.py
--rw-r--r--   0 runner    (1001) docker     (121)      957 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/cli_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     1304 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/context_extend_test.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/tests/epw/
--rw-r--r--   0 runner    (1001) docker     (121)  1642801 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/epw/boston.epw
--rw-r--r--   0 runner    (1001) docker     (121)  1558359 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/epw/singapore.epw
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/tests/fixtures/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/fixtures/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      230 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/fixtures/boundary.py
--rw-r--r--   0 runner    (1001) docker     (121)     1881 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/fixtures/building.py
--rw-r--r--   0 runner    (1001) docker     (121)      882 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/fixtures/context.py
--rw-r--r--   0 runner    (1001) docker     (121)     3558 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/fixtures/model.py
--rw-r--r--   0 runner    (1001) docker     (121)      201 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/fixtures/refsite.py
--rw-r--r--   0 runner    (1001) docker     (121)      669 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/fixtures/sim_par.py
--rw-r--r--   0 runner    (1001) docker     (121)      584 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/fixtures/terrain.py
--rw-r--r--   0 runner    (1001) docker     (121)      375 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/fixtures/traffic.py
--rw-r--r--   0 runner    (1001) docker     (121)      224 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/fixtures/vegetation.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-06 15:48:11.000000 dragonfly-uwg-0.5.98/tests/json/
--rw-r--r--   0 runner    (1001) docker     (121)    90398 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/json/model_complete_simple.dfjson
--rw-r--r--   0 runner    (1001) docker     (121)      939 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/json/uwg_sim_par.json
--rw-r--r--   0 runner    (1001) docker     (121)     3806 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/model_extend_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     1491 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/refsite_test.py
--rw-r--r--   0 runner    (1001) docker     (121)      660 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/run_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     1064 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/sim_par_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     1733 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/terrain_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     1591 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/traffic_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     1845 2021-10-06 15:47:04.000000 dragonfly-uwg-0.5.98/tests/vegetation_test.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:50.000000 dragonfly-uwg-0.5.99/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/.github/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (121)     3569 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/.github/workflows/ci.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)     1904 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/.github/workflows/dependency-release.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)      142 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (121)      294 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/.releaserc.json
+-rw-r--r--   0 runner    (1001) docker     (121)      279 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/CODE_OF_CONDUCT.md
+-rw-r--r--   0 runner    (1001) docker     (121)      445 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/CONTRIBUTING.md
+-rw-r--r--   0 runner    (1001) docker     (121)    34523 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)     2392 2021-10-08 18:36:50.000000 dragonfly-uwg-0.5.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1707 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      165 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/deploy.sh
+-rw-r--r--   0 runner    (1001) docker     (121)      698 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dev-requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/docs/
+-rw-r--r--   0 runner    (1001) docker     (121)      373 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/docs/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/docs/_build/
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/docs/_build/.nojekyll
+-rw-r--r--   0 runner    (1001) docker     (121)       16 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/docs/_build/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/docs/_build/docs/
+-rw-r--r--   0 runner    (1001) docker     (121)       16 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/docs/_build/docs/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/docs/_static/
+-rw-r--r--   0 runner    (1001) docker     (121)      899 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/docs/_static/custom.css
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/docs/_templates/
+-rw-r--r--   0 runner    (1001) docker     (121)     3668 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/docs/_templates/layout.html
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/docs/cli/
+-rw-r--r--   0 runner    (1001) docker     (121)      127 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/docs/cli/index.rst
+-rw-r--r--   0 runner    (1001) docker     (121)    15975 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/docs/conf.py
+-rw-r--r--   0 runner    (1001) docker     (121)      822 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/docs/index.rst
+-rw-r--r--   0 runner    (1001) docker     (121)       80 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/docs/modules.rst
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/
+-rw-r--r--   0 runner    (1001) docker     (121)      229 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)       72 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1863 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/_extend_dragonfly.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/cli/
+-rw-r--r--   0 runner    (1001) docker     (121)      393 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3086 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/cli/simulate.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/properties/
+-rw-r--r--   0 runner    (1001) docker     (121)       32 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/properties/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2841 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/properties/_refdefaults.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12434 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/properties/building.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3224 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/properties/context.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17716 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/properties/model.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2358 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/properties/room2d.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2338 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/properties/story.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5679 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/run.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/simulation/
+-rw-r--r--   0 runner    (1001) docker     (121)       49 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/simulation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6662 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/simulation/boundary.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12680 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/simulation/parameter.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5150 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/simulation/refsite.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5061 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/simulation/runperiod.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6988 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/simulation/vegetation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12766 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/terrain.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7595 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/traffic.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2077 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/dragonfly_uwg/writer.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/dragonfly_uwg.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     2392 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/dragonfly_uwg.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2014 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/dragonfly_uwg.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/dragonfly_uwg.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       57 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/dragonfly_uwg.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       35 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/dragonfly_uwg.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       20 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/dragonfly_uwg.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       35 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      102 2021-10-08 18:36:50.000000 dragonfly-uwg-0.5.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1176 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:49.000000 dragonfly-uwg-0.5.99/tests/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1804 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/boundary_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2920 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/building_extend_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)      957 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/cli_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1304 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/context_extend_test.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:50.000000 dragonfly-uwg-0.5.99/tests/epw/
+-rw-r--r--   0 runner    (1001) docker     (121)  1642801 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/epw/boston.epw
+-rw-r--r--   0 runner    (1001) docker     (121)  1558359 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/epw/singapore.epw
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:50.000000 dragonfly-uwg-0.5.99/tests/fixtures/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/fixtures/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      230 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/fixtures/boundary.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1881 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/fixtures/building.py
+-rw-r--r--   0 runner    (1001) docker     (121)      882 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/fixtures/context.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3558 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/fixtures/model.py
+-rw-r--r--   0 runner    (1001) docker     (121)      201 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/fixtures/refsite.py
+-rw-r--r--   0 runner    (1001) docker     (121)      669 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/fixtures/sim_par.py
+-rw-r--r--   0 runner    (1001) docker     (121)      584 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/fixtures/terrain.py
+-rw-r--r--   0 runner    (1001) docker     (121)      375 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/fixtures/traffic.py
+-rw-r--r--   0 runner    (1001) docker     (121)      224 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/fixtures/vegetation.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-08 18:36:50.000000 dragonfly-uwg-0.5.99/tests/json/
+-rw-r--r--   0 runner    (1001) docker     (121)    90398 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/json/model_complete_simple.dfjson
+-rw-r--r--   0 runner    (1001) docker     (121)      939 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/json/uwg_sim_par.json
+-rw-r--r--   0 runner    (1001) docker     (121)     3806 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/model_extend_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1491 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/refsite_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)      660 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/run_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1064 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/sim_par_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1733 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/terrain_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1591 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/traffic_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1845 2021-10-08 18:35:39.000000 dragonfly-uwg-0.5.99/tests/vegetation_test.py
```

### Comparing `dragonfly-uwg-0.5.98/.github/workflows/ci.yaml` & `dragonfly-uwg-0.5.99/.github/workflows/ci.yaml`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/.github/workflows/dependency-release.yaml` & `dragonfly-uwg-0.5.99/.github/workflows/dependency-release.yaml`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/LICENSE` & `dragonfly-uwg-0.5.99/LICENSE`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/PKG-INFO` & `dragonfly-uwg-0.5.99/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dragonfly-uwg
-Version: 0.5.98
+Version: 0.5.99
 Summary: Dragonfly extension for the Urban Weather Generator (UWG).
 Home-page: https://github.com/ladybug-tools/dragonfly-uwg
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: AGPL-3.0
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 2.7
```

### Comparing `dragonfly-uwg-0.5.98/README.md` & `dragonfly-uwg-0.5.99/README.md`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dev-requirements.txt` & `dragonfly-uwg-0.5.99/dev-requirements.txt`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/docs/_static/custom.css` & `dragonfly-uwg-0.5.99/docs/_static/custom.css`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/docs/_templates/layout.html` & `dragonfly-uwg-0.5.99/docs/_templates/layout.html`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/docs/conf.py` & `dragonfly-uwg-0.5.99/docs/conf.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/docs/index.rst` & `dragonfly-uwg-0.5.99/docs/index.rst`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/_extend_dragonfly.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/_extend_dragonfly.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/cli/simulate.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/cli/simulate.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/properties/_refdefaults.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/properties/_refdefaults.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/properties/building.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/properties/building.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/properties/context.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/properties/context.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/properties/model.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/properties/model.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/properties/room2d.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/properties/room2d.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/properties/story.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/properties/story.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/run.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/run.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/simulation/boundary.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/simulation/boundary.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/simulation/parameter.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/simulation/parameter.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/simulation/refsite.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/simulation/refsite.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/simulation/runperiod.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/simulation/runperiod.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/simulation/vegetation.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/simulation/vegetation.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/terrain.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/terrain.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/traffic.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/traffic.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg/writer.py` & `dragonfly-uwg-0.5.99/dragonfly_uwg/writer.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg.egg-info/PKG-INFO` & `dragonfly-uwg-0.5.99/dragonfly_uwg.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dragonfly-uwg
-Version: 0.5.98
+Version: 0.5.99
 Summary: Dragonfly extension for the Urban Weather Generator (UWG).
 Home-page: https://github.com/ladybug-tools/dragonfly-uwg
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: AGPL-3.0
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 2.7
```

### Comparing `dragonfly-uwg-0.5.98/dragonfly_uwg.egg-info/SOURCES.txt` & `dragonfly-uwg-0.5.99/dragonfly_uwg.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/setup.py` & `dragonfly-uwg-0.5.99/setup.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/boundary_test.py` & `dragonfly-uwg-0.5.99/tests/boundary_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/building_extend_test.py` & `dragonfly-uwg-0.5.99/tests/building_extend_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/cli_test.py` & `dragonfly-uwg-0.5.99/tests/cli_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/context_extend_test.py` & `dragonfly-uwg-0.5.99/tests/context_extend_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/epw/boston.epw` & `dragonfly-uwg-0.5.99/tests/epw/boston.epw`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/epw/singapore.epw` & `dragonfly-uwg-0.5.99/tests/epw/singapore.epw`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/fixtures/building.py` & `dragonfly-uwg-0.5.99/tests/fixtures/building.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/fixtures/context.py` & `dragonfly-uwg-0.5.99/tests/fixtures/context.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/fixtures/model.py` & `dragonfly-uwg-0.5.99/tests/fixtures/model.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/fixtures/sim_par.py` & `dragonfly-uwg-0.5.99/tests/fixtures/sim_par.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/fixtures/terrain.py` & `dragonfly-uwg-0.5.99/tests/fixtures/terrain.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/json/model_complete_simple.dfjson` & `dragonfly-uwg-0.5.99/tests/json/model_complete_simple.dfjson`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/json/uwg_sim_par.json` & `dragonfly-uwg-0.5.99/tests/json/uwg_sim_par.json`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/model_extend_test.py` & `dragonfly-uwg-0.5.99/tests/model_extend_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/refsite_test.py` & `dragonfly-uwg-0.5.99/tests/refsite_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/run_test.py` & `dragonfly-uwg-0.5.99/tests/run_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/sim_par_test.py` & `dragonfly-uwg-0.5.99/tests/sim_par_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/terrain_test.py` & `dragonfly-uwg-0.5.99/tests/terrain_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/traffic_test.py` & `dragonfly-uwg-0.5.99/tests/traffic_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-uwg-0.5.98/tests/vegetation_test.py` & `dragonfly-uwg-0.5.99/tests/vegetation_test.py`

 * *Files identical despite different names*

