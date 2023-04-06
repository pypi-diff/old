# Comparing `tmp/dragonfly-energy-1.9.8.tar.gz` & `tmp/dragonfly-energy-1.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/dragonfly-energy-1.9.8.tar", last modified: Thu Aug 20 17:06:52 2020, max compression
+gzip compressed data, was "dist/dragonfly-energy-1.9.9.tar", last modified: Mon Aug 24 16:31:33 2020, max compression
```

## Comparing `dragonfly-energy-1.9.8.tar` & `dragonfly-energy-1.9.9.tar`

### file list

```diff
@@ -1,77 +1,77 @@
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/
--rw-rw-r--   0 travis    (2000) travis    (2000)       56 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/.coveragerc
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/.dependabot/
--rw-rw-r--   0 travis    (2000) travis    (2000)      305 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/.dependabot/config.yml
--rw-rw-r--   0 travis    (2000) travis    (2000)      142 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/.gitignore
--rw-rw-r--   0 travis    (2000) travis    (2000)      294 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/.releaserc.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     1095 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/.travis.yml
--rw-rw-r--   0 travis    (2000) travis    (2000)      279 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/CODE_OF_CONDUCT.md
--rw-rw-r--   0 travis    (2000) travis    (2000)      445 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/CONTRIBUTING.md
--rw-rw-r--   0 travis    (2000) travis    (2000)    35149 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/LICENSE
--rw-rw-r--   0 travis    (2000) travis    (2000)       37 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/MANIFEST.in
--rw-rw-r--   0 travis    (2000) travis    (2000)     5348 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/PKG-INFO
--rw-rw-r--   0 travis    (2000) travis    (2000)     3793 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/README.md
--rw-rw-r--   0 travis    (2000) travis    (2000)      165 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/deploy.sh
--rw-rw-r--   0 travis    (2000) travis    (2000)      604 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dev-requirements.txt
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/docs/
--rw-rw-r--   0 travis    (2000) travis    (2000)      376 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/docs/README.md
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/docs/_build/
--rw-rw-r--   0 travis    (2000) travis    (2000)        1 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/docs/_build/.nojekyll
--rw-rw-r--   0 travis    (2000) travis    (2000)       16 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/docs/_build/README.md
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/docs/_build/docs/
--rw-rw-r--   0 travis    (2000) travis    (2000)       16 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/docs/_build/docs/README.md
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/docs/_static/
--rw-rw-r--   0 travis    (2000) travis    (2000)      939 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/docs/_static/custom.css
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/docs/_templates/
--rw-rw-r--   0 travis    (2000) travis    (2000)     3775 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/docs/_templates/layout.html
--rw-rw-r--   0 travis    (2000) travis    (2000)      155 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/docs/cli.rst
--rw-rw-r--   0 travis    (2000) travis    (2000)     7242 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/docs/conf.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      927 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/docs/index.rst
--rw-rw-r--   0 travis    (2000) travis    (2000)       86 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/docs/modules.rst
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/dragonfly_energy/
--rw-rw-r--   0 travis    (2000) travis    (2000)      238 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)       81 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/__main__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2028 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/_extend_dragonfly.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/dragonfly_energy/cli/
--rw-rw-r--   0 travis    (2000) travis    (2000)      608 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/cli/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7722 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/cli/simulate.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    10434 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/cli/translate.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      139 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/config.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     5568 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/config.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/dragonfly_energy/properties/
--rw-rw-r--   0 travis    (2000) travis    (2000)       35 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/properties/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     9257 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/properties/building.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7673 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/properties/context.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    16855 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/properties/model.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    14838 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/properties/room2d.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     9229 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/properties/story.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    16465 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/run.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5329 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/dragonfly_energy/writer.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/dragonfly_energy.egg-info/
--rw-rw-r--   0 travis    (2000) travis    (2000)     5348 2020-08-20 17:06:51.000000 dragonfly-energy-1.9.8/dragonfly_energy.egg-info/PKG-INFO
--rw-rw-r--   0 travis    (2000) travis    (2000)     1611 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/dragonfly_energy.egg-info/SOURCES.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)        1 2020-08-20 17:06:51.000000 dragonfly-energy-1.9.8/dragonfly_energy.egg-info/dependency_links.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)       66 2020-08-20 17:06:51.000000 dragonfly-energy-1.9.8/dragonfly_energy.egg-info/entry_points.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)       95 2020-08-20 17:06:51.000000 dragonfly-energy-1.9.8/dragonfly_energy.egg-info/requires.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)       17 2020-08-20 17:06:51.000000 dragonfly-energy-1.9.8/dragonfly_energy.egg-info/top_level.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)       47 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/requirements.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)      102 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/setup.cfg
--rw-rw-r--   0 travis    (2000) travis    (2000)     1243 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/setup.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/tests/
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/tests/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    17391 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/tests/building_extend_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      475 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/tests/cli_translate_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5641 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/tests/context_extend_test.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/tests/epw/
--rw-rw-r--   0 travis    (2000) travis    (2000)    28793 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/tests/epw/chicago.ddy
--rw-rw-r--   0 travis    (2000) travis    (2000)  1639985 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/tests/epw/chicago.epw
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/tests/json/
--rw-rw-r--   0 travis    (2000) travis    (2000)    88964 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/tests/json/model_complete_simple.json
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/tests/measure/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-20 17:06:52.000000 dragonfly-energy-1.9.8/tests/measure/edit_fraction_radiant_of_lighting_and_equipment/
--rw-rw-r--   0 travis    (2000) travis    (2000)     3506 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/tests/measure/edit_fraction_radiant_of_lighting_and_equipment/measure.rb
--rw-rw-r--   0 travis    (2000) travis    (2000)     2691 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/tests/measure/edit_fraction_radiant_of_lighting_and_equipment/measure.xml
--rw-rw-r--   0 travis    (2000) travis    (2000)    19802 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/tests/model_extend_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    14002 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/tests/room2d_extend_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4673 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/tests/run_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    11096 2020-08-20 17:05:54.000000 dragonfly-energy-1.9.8/tests/story_extend_test.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       56 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/.coveragerc
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/.dependabot/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      305 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/.dependabot/config.yml
+-rw-rw-r--   0 travis    (2000) travis    (2000)      142 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/.gitignore
+-rw-rw-r--   0 travis    (2000) travis    (2000)      294 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/.releaserc.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1095 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/.travis.yml
+-rw-rw-r--   0 travis    (2000) travis    (2000)      279 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/CODE_OF_CONDUCT.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)      445 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/CONTRIBUTING.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)    35149 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/LICENSE
+-rw-rw-r--   0 travis    (2000) travis    (2000)       37 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/MANIFEST.in
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5348 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/PKG-INFO
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3793 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/README.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)      165 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/deploy.sh
+-rw-rw-r--   0 travis    (2000) travis    (2000)      604 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dev-requirements.txt
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/docs/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      376 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/docs/README.md
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/docs/_build/
+-rw-rw-r--   0 travis    (2000) travis    (2000)        1 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/docs/_build/.nojekyll
+-rw-rw-r--   0 travis    (2000) travis    (2000)       16 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/docs/_build/README.md
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/docs/_build/docs/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       16 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/docs/_build/docs/README.md
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/docs/_static/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      939 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/docs/_static/custom.css
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/docs/_templates/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3775 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/docs/_templates/layout.html
+-rw-rw-r--   0 travis    (2000) travis    (2000)      155 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/docs/cli.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7242 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/docs/conf.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      927 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/docs/index.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)       86 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/docs/modules.rst
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/dragonfly_energy/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      238 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)       81 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/__main__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2028 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/_extend_dragonfly.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/dragonfly_energy/cli/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      608 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/cli/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7722 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/cli/simulate.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10434 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/cli/translate.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      139 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/config.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5568 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/config.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/dragonfly_energy/properties/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       35 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/properties/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9257 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/properties/building.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7673 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/properties/context.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    16855 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/properties/model.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    14838 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/properties/room2d.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9229 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/properties/story.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    16465 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/run.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5329 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/dragonfly_energy/writer.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/dragonfly_energy.egg-info/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5348 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/dragonfly_energy.egg-info/PKG-INFO
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1611 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/dragonfly_energy.egg-info/SOURCES.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)        1 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/dragonfly_energy.egg-info/dependency_links.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)       66 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/dragonfly_energy.egg-info/entry_points.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)       95 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/dragonfly_energy.egg-info/requires.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)       17 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/dragonfly_energy.egg-info/top_level.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)       47 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/requirements.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)      102 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/setup.cfg
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1243 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/setup.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/tests/
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/tests/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    17391 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/tests/building_extend_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      475 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/tests/cli_translate_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5641 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/tests/context_extend_test.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/tests/epw/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    28793 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/tests/epw/chicago.ddy
+-rw-rw-r--   0 travis    (2000) travis    (2000)  1639985 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/tests/epw/chicago.epw
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/tests/json/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    88964 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/tests/json/model_complete_simple.json
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/tests/measure/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-24 16:31:33.000000 dragonfly-energy-1.9.9/tests/measure/edit_fraction_radiant_of_lighting_and_equipment/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3506 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/tests/measure/edit_fraction_radiant_of_lighting_and_equipment/measure.rb
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2691 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/tests/measure/edit_fraction_radiant_of_lighting_and_equipment/measure.xml
+-rw-rw-r--   0 travis    (2000) travis    (2000)    19802 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/tests/model_extend_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    14002 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/tests/room2d_extend_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4673 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/tests/run_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    11096 2020-08-24 16:30:37.000000 dragonfly-energy-1.9.9/tests/story_extend_test.py
```

### Comparing `dragonfly-energy-1.9.8/.travis.yml` & `dragonfly-energy-1.9.9/.travis.yml`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/LICENSE` & `dragonfly-energy-1.9.9/LICENSE`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/PKG-INFO` & `dragonfly-energy-1.9.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dragonfly-energy
-Version: 1.9.8
+Version: 1.9.9
 Summary: Dragonfly extension for energy simulation.
 Home-page: https://github.com/ladybug-tools/dragonfly-energy
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: UNKNOWN
 Description: [![Build Status](https://travis-ci.org/ladybug-tools/dragonfly-energy.svg?branch=master)](https://travis-ci.org/ladybug-tools/dragonfly-energy)
         [![Coverage Status](https://coveralls.io/repos/github/ladybug-tools/dragonfly-energy/badge.svg?branch=master)](https://coveralls.io/github/ladybug-tools/dragonfly-energy)
```

### Comparing `dragonfly-energy-1.9.8/README.md` & `dragonfly-energy-1.9.9/README.md`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/dev-requirements.txt` & `dragonfly-energy-1.9.9/dev-requirements.txt`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/docs/_static/custom.css` & `dragonfly-energy-1.9.9/docs/_static/custom.css`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/docs/_templates/layout.html` & `dragonfly-energy-1.9.9/docs/_templates/layout.html`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/docs/conf.py` & `dragonfly-energy-1.9.9/docs/conf.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/docs/index.rst` & `dragonfly-energy-1.9.9/docs/index.rst`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/dragonfly_energy/_extend_dragonfly.py` & `dragonfly-energy-1.9.9/dragonfly_energy/_extend_dragonfly.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/dragonfly_energy/cli/__init__.py` & `dragonfly-energy-1.9.9/dragonfly_energy/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/dragonfly_energy/cli/simulate.py` & `dragonfly-energy-1.9.9/dragonfly_energy/cli/simulate.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/dragonfly_energy/cli/translate.py` & `dragonfly-energy-1.9.9/dragonfly_energy/cli/translate.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/dragonfly_energy/config.py` & `dragonfly-energy-1.9.9/dragonfly_energy/config.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/dragonfly_energy/properties/building.py` & `dragonfly-energy-1.9.9/dragonfly_energy/properties/building.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/dragonfly_energy/properties/context.py` & `dragonfly-energy-1.9.9/dragonfly_energy/properties/context.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/dragonfly_energy/properties/model.py` & `dragonfly-energy-1.9.9/dragonfly_energy/properties/model.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/dragonfly_energy/properties/room2d.py` & `dragonfly-energy-1.9.9/dragonfly_energy/properties/room2d.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/dragonfly_energy/properties/story.py` & `dragonfly-energy-1.9.9/dragonfly_energy/properties/story.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/dragonfly_energy/run.py` & `dragonfly-energy-1.9.9/dragonfly_energy/run.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/dragonfly_energy/writer.py` & `dragonfly-energy-1.9.9/dragonfly_energy/writer.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/dragonfly_energy.egg-info/PKG-INFO` & `dragonfly-energy-1.9.9/dragonfly_energy.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dragonfly-energy
-Version: 1.9.8
+Version: 1.9.9
 Summary: Dragonfly extension for energy simulation.
 Home-page: https://github.com/ladybug-tools/dragonfly-energy
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: UNKNOWN
 Description: [![Build Status](https://travis-ci.org/ladybug-tools/dragonfly-energy.svg?branch=master)](https://travis-ci.org/ladybug-tools/dragonfly-energy)
         [![Coverage Status](https://coveralls.io/repos/github/ladybug-tools/dragonfly-energy/badge.svg?branch=master)](https://coveralls.io/github/ladybug-tools/dragonfly-energy)
```

### Comparing `dragonfly-energy-1.9.8/dragonfly_energy.egg-info/SOURCES.txt` & `dragonfly-energy-1.9.9/dragonfly_energy.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/setup.py` & `dragonfly-energy-1.9.9/setup.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/tests/building_extend_test.py` & `dragonfly-energy-1.9.9/tests/building_extend_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/tests/context_extend_test.py` & `dragonfly-energy-1.9.9/tests/context_extend_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/tests/epw/chicago.ddy` & `dragonfly-energy-1.9.9/tests/epw/chicago.ddy`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/tests/epw/chicago.epw` & `dragonfly-energy-1.9.9/tests/epw/chicago.epw`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/tests/json/model_complete_simple.json` & `dragonfly-energy-1.9.9/tests/json/model_complete_simple.json`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/tests/measure/edit_fraction_radiant_of_lighting_and_equipment/measure.rb` & `dragonfly-energy-1.9.9/tests/measure/edit_fraction_radiant_of_lighting_and_equipment/measure.rb`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/tests/measure/edit_fraction_radiant_of_lighting_and_equipment/measure.xml` & `dragonfly-energy-1.9.9/tests/measure/edit_fraction_radiant_of_lighting_and_equipment/measure.xml`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/tests/model_extend_test.py` & `dragonfly-energy-1.9.9/tests/model_extend_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/tests/room2d_extend_test.py` & `dragonfly-energy-1.9.9/tests/room2d_extend_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/tests/run_test.py` & `dragonfly-energy-1.9.9/tests/run_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-energy-1.9.8/tests/story_extend_test.py` & `dragonfly-energy-1.9.9/tests/story_extend_test.py`

 * *Files identical despite different names*

