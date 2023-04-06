# Comparing `tmp/honeybee-core-1.8.1.tar.gz` & `tmp/honeybee-core-1.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/honeybee-core-1.8.1.tar", last modified: Wed Oct 16 20:44:52 2019, max compression
+gzip compressed data, was "dist/honeybee-core-1.9.0.tar", last modified: Fri Oct 18 04:24:27 2019, max compression
```

## Comparing `honeybee-core-1.8.1.tar` & `honeybee-core-1.9.0.tar`

### file list

```diff
@@ -1,66 +1,73 @@
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/.github/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1738 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/.github/project-manager.yml
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/docs/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/docs/_build/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/docs/_build/docs/
--rw-rw-r--   0 travis    (2000) travis    (2000)       16 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/docs/_build/docs/README.md
--rw-rw-r--   0 travis    (2000) travis    (2000)       16 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/docs/_build/README.md
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/docs/_build/.nojekyll
--rw-rw-r--   0 travis    (2000) travis    (2000)     6450 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/docs/conf.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1419 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/docs/index.rst
--rw-rw-r--   0 travis    (2000) travis    (2000)      130 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/docs/cli.rst
--rw-rw-r--   0 travis    (2000) travis    (2000)       61 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/docs/modules.rst
--rw-rw-r--   0 travis    (2000) travis    (2000)      279 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/CODE_OF_CONDUCT.md
--rw-rw-r--   0 travis    (2000) travis    (2000)       19 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/requirements.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)     2927 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/PKG-INFO
--rw-rw-r--   0 travis    (2000) travis    (2000)      294 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/.releaserc.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     1882 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/README.md
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/honeybee_core.egg-info/
--rw-rw-r--   0 travis    (2000) travis    (2000)     2927 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/honeybee_core.egg-info/PKG-INFO
--rw-rw-r--   0 travis    (2000) travis    (2000)        1 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/honeybee_core.egg-info/dependency_links.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)        9 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/honeybee_core.egg-info/top_level.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)     1186 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/honeybee_core.egg-info/SOURCES.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)       19 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/honeybee_core.egg-info/requires.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)       48 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/honeybee_core.egg-info/entry_points.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)      144 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/.gitignore
--rw-rw-r--   0 travis    (2000) travis    (2000)      445 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/CONTRIBUTING.md
--rw-rw-r--   0 travis    (2000) travis    (2000)      174 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/setup.cfg
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/honeybee/
--rw-rw-r--   0 travis    (2000) travis    (2000)    26351 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/room.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    10156 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/_basewithshade.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4978 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/typing.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3129 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/facetype.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1726 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/_base.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2371 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/cli.py
--rw-rw-r--   0 travis    (2000) travis    (2000)       69 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/__main__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     9823 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/shade.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    14024 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/door.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      117 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/writer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7732 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/extensionutil.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    13719 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/properties.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    24965 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/aperture.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3677 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/_lockable.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2249 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/logutil.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      624 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    40827 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/model.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    41604 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/face.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    11105 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/honeybee/boundarycondition.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1041 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/.travis.yml
--rw-rw-r--   0 travis    (2000) travis    (2000)    35149 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/LICENSE
--rw-rw-r--   0 travis    (2000) travis    (2000)      215 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/dev-requirements.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)     1242 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/setup.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      166 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/deploy.sh
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-16 20:44:52.000000 honeybee-core-1.8.1/tests/
--rw-rw-r--   0 travis    (2000) travis    (2000)    11056 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/tests/shade_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    14898 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/tests/aperture_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1248 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/tests/facetype_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5988 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/tests/typing_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    36641 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/tests/model_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2857 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/tests/boundary_condition_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3115 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/tests/lockable_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      489 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/tests/cli_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/tests/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    24427 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/tests/face_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    11198 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/tests/door_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    23082 2019-10-16 20:43:56.000000 honeybee-core-1.8.1/tests/room_test.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-18 04:24:27.000000 honeybee-core-1.9.0/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-18 04:24:27.000000 honeybee-core-1.9.0/.github/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1738 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/.github/project-manager.yml
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-18 04:24:27.000000 honeybee-core-1.9.0/docs/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-18 04:24:27.000000 honeybee-core-1.9.0/docs/_build/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-18 04:24:27.000000 honeybee-core-1.9.0/docs/_build/docs/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       16 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/docs/_build/docs/README.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)       16 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/docs/_build/README.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/docs/_build/.nojekyll
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6450 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/docs/conf.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1419 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/docs/index.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)      130 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/docs/cli.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)       61 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/docs/modules.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)      279 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/CODE_OF_CONDUCT.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)       19 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/requirements.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2927 2019-10-18 04:24:27.000000 honeybee-core-1.9.0/PKG-INFO
+-rw-rw-r--   0 travis    (2000) travis    (2000)      294 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/.releaserc.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1882 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/README.md
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-18 04:24:27.000000 honeybee-core-1.9.0/honeybee_core.egg-info/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2927 2019-10-18 04:24:26.000000 honeybee-core-1.9.0/honeybee_core.egg-info/PKG-INFO
+-rw-rw-r--   0 travis    (2000) travis    (2000)        1 2019-10-18 04:24:26.000000 honeybee-core-1.9.0/honeybee_core.egg-info/dependency_links.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)        9 2019-10-18 04:24:26.000000 honeybee-core-1.9.0/honeybee_core.egg-info/top_level.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1345 2019-10-18 04:24:27.000000 honeybee-core-1.9.0/honeybee_core.egg-info/SOURCES.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)       19 2019-10-18 04:24:26.000000 honeybee-core-1.9.0/honeybee_core.egg-info/requires.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)       48 2019-10-18 04:24:26.000000 honeybee-core-1.9.0/honeybee_core.egg-info/entry_points.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)      144 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/.gitignore
+-rw-rw-r--   0 travis    (2000) travis    (2000)      445 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/CONTRIBUTING.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)      174 2019-10-18 04:24:27.000000 honeybee-core-1.9.0/setup.cfg
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-18 04:24:27.000000 honeybee-core-1.9.0/honeybee/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    26356 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/room.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10156 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/_basewithshade.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4978 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/typing.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3129 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/facetype.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1726 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/_base.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2371 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/cli.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-18 04:24:27.000000 honeybee-core-1.9.0/honeybee/writer/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      174 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/writer/room.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      177 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/writer/shade.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      174 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/writer/door.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      186 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/writer/aperture.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      246 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/writer/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      177 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/writer/model.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      174 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/writer/face.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)       69 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/__main__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9829 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/shade.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    14029 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/door.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7732 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/extensionutil.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    13719 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/properties.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    24974 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/aperture.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3677 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/_lockable.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2249 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/logutil.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      624 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    40833 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/model.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    41609 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/face.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    11105 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/honeybee/boundarycondition.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1041 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/.travis.yml
+-rw-rw-r--   0 travis    (2000) travis    (2000)    35149 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/LICENSE
+-rw-rw-r--   0 travis    (2000) travis    (2000)      215 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/dev-requirements.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1242 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/setup.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      166 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/deploy.sh
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2019-10-18 04:24:27.000000 honeybee-core-1.9.0/tests/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    11338 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/tests/shade_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    15185 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/tests/aperture_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1248 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/tests/facetype_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5988 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/tests/typing_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    36898 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/tests/model_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2857 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/tests/boundary_condition_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3115 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/tests/lockable_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      489 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/tests/cli_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/tests/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    24778 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/tests/face_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    11479 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/tests/door_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    23295 2019-10-18 04:23:32.000000 honeybee-core-1.9.0/tests/room_test.py
```

### Comparing `honeybee-core-1.8.1/.github/project-manager.yml` & `honeybee-core-1.9.0/.github/project-manager.yml`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/docs/conf.py` & `honeybee-core-1.9.0/docs/conf.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/docs/index.rst` & `honeybee-core-1.9.0/docs/index.rst`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/PKG-INFO` & `honeybee-core-1.9.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: honeybee-core
-Version: 1.8.1
+Version: 1.9.0
 Summary: Honeybee is a Python library to create, run and visualize the results of environmental simulation. See extensions (e.g. honeybee_radiance) for specific simulation type.
 Home-page: https://github.com/ladybug-tools/honeybee-core
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: UNKNOWN
 Description: ![Honeybee](https://www.ladybug.tools/assets/img/honeybee.png)
```

### Comparing `honeybee-core-1.8.1/README.md` & `honeybee-core-1.9.0/README.md`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/honeybee_core.egg-info/PKG-INFO` & `honeybee-core-1.9.0/honeybee_core.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: honeybee-core
-Version: 1.8.1
+Version: 1.9.0
 Summary: Honeybee is a Python library to create, run and visualize the results of environmental simulation. See extensions (e.g. honeybee_radiance) for specific simulation type.
 Home-page: https://github.com/ladybug-tools/honeybee-core
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: UNKNOWN
 Description: ![Honeybee](https://www.ladybug.tools/assets/img/honeybee.png)
```

### Comparing `honeybee-core-1.8.1/honeybee_core.egg-info/SOURCES.txt` & `honeybee-core-1.9.0/honeybee_core.egg-info/SOURCES.txt`

 * *Files 22% similar despite different names*

```diff
@@ -32,15 +32,21 @@
 honeybee/facetype.py
 honeybee/logutil.py
 honeybee/model.py
 honeybee/properties.py
 honeybee/room.py
 honeybee/shade.py
 honeybee/typing.py
-honeybee/writer.py
+honeybee/writer/__init__.py
+honeybee/writer/aperture.py
+honeybee/writer/door.py
+honeybee/writer/face.py
+honeybee/writer/model.py
+honeybee/writer/room.py
+honeybee/writer/shade.py
 honeybee_core.egg-info/PKG-INFO
 honeybee_core.egg-info/SOURCES.txt
 honeybee_core.egg-info/dependency_links.txt
 honeybee_core.egg-info/entry_points.txt
 honeybee_core.egg-info/requires.txt
 honeybee_core.egg-info/top_level.txt
 tests/__init__.py
```

### Comparing `honeybee-core-1.8.1/honeybee/room.py` & `honeybee-core-1.9.0/honeybee/room.py`

 * *Files 0% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 """Honeybee Room."""
 from ._basewithshade import _BaseWithShade
 from .properties import RoomProperties
 from .face import Face
 from .facetype import get_type_from_normal, Wall, Floor
 from .boundarycondition import get_bc_from_position, Outdoors, Surface
 from .typing import float_in_range, int_in_range
-import honeybee.writer as writer
+import honeybee.writer.room as writer
 
 from ladybug_geometry.geometry2d.pointvector import Vector2D
 from ladybug_geometry.geometry3d.pointvector import Vector3D, Point3D
 from ladybug_geometry.geometry3d.plane import Plane
 from ladybug_geometry.geometry3d.polyface import Polyface3D
 
 import math
```

### Comparing `honeybee-core-1.8.1/honeybee/_basewithshade.py` & `honeybee-core-1.9.0/honeybee/_basewithshade.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/honeybee/typing.py` & `honeybee-core-1.9.0/honeybee/typing.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/honeybee/facetype.py` & `honeybee-core-1.9.0/honeybee/facetype.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/honeybee/_base.py` & `honeybee-core-1.9.0/honeybee/_base.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/honeybee/cli.py` & `honeybee-core-1.9.0/honeybee/cli.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/honeybee/shade.py` & `honeybee-core-1.9.0/honeybee/shade.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 # coding: utf-8
 """Honeybee Shade."""
 from ._base import _Base
 from .properties import ShadeProperties
-import honeybee.writer as writer
+import honeybee.writer.shade as writer
 
 from ladybug_geometry.geometry3d.pointvector import Point3D
 from ladybug_geometry.geometry3d.face import Face3D
 
 import math
```

### Comparing `honeybee-core-1.8.1/honeybee/door.py` & `honeybee-core-1.9.0/honeybee/door.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 # coding: utf-8
 """Honeybee Door."""
 from ._base import _Base
 from .properties import DoorProperties
 from .boundarycondition import boundary_conditions, Outdoors, Surface
-import honeybee.writer as writer
+import honeybee.writer.door as writer
 
 from ladybug_geometry.geometry3d.pointvector import Point3D
 from ladybug_geometry.geometry3d.face import Face3D
 
 import math
```

### Comparing `honeybee-core-1.8.1/honeybee/extensionutil.py` & `honeybee-core-1.9.0/honeybee/extensionutil.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/honeybee/properties.py` & `honeybee-core-1.9.0/honeybee/properties.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/honeybee/aperture.py` & `honeybee-core-1.9.0/honeybee/aperture.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # coding: utf-8
 """Honeybee Aperture."""
 from ._basewithshade import _BaseWithShade
 from .properties import ApertureProperties
 from .boundarycondition import boundary_conditions, Outdoors, Surface
 from .shade import Shade
-import honeybee.writer as writer
+import honeybee.writer.aperture as writer
 
 from ladybug_geometry.geometry3d.pointvector import Point3D, Vector3D
 from ladybug_geometry.geometry3d.face import Face3D
 
 import math
```

### Comparing `honeybee-core-1.8.1/honeybee/_lockable.py` & `honeybee-core-1.9.0/honeybee/_lockable.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/honeybee/logutil.py` & `honeybee-core-1.9.0/honeybee/logutil.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/honeybee/__init__.py` & `honeybee-core-1.9.0/honeybee/__init__.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/honeybee/model.py` & `honeybee-core-1.9.0/honeybee/model.py`

 * *Files 0% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 from .face import Face
 from .shade import Shade
 from .aperture import Aperture
 from .door import Door
 from .typing import float_in_range
 from .boundarycondition import Surface
 from .facetype import AirWall
-import honeybee.writer as writer
+import honeybee.writer.model as writer
 
 from ladybug_geometry.geometry2d.pointvector import Vector2D
 from ladybug_geometry.geometry3d.face import Face3D
 
 import math
```

### Comparing `honeybee-core-1.8.1/honeybee/face.py` & `honeybee-core-1.9.0/honeybee/face.py`

 * *Files 0% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 from .facetype import face_types, get_type_from_normal, AirWall
 from .boundarycondition import boundary_conditions, get_bc_from_position, \
     _BoundaryCondition, Outdoors, Surface
 from .shade import Shade
 from .aperture import Aperture
 from .door import Door
 import honeybee.boundarycondition as hbc
-import honeybee.writer as writer
+import honeybee.writer.face as writer
 
 from ladybug_geometry.geometry2d.pointvector import Point2D, Vector2D
 from ladybug_geometry.geometry3d.pointvector import Point3D, Vector3D
 from ladybug_geometry.geometry3d.plane import Plane
 from ladybug_geometry.geometry3d.face import Face3D
 
 import math
```

### Comparing `honeybee-core-1.8.1/honeybee/boundarycondition.py` & `honeybee-core-1.9.0/honeybee/boundarycondition.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/.travis.yml` & `honeybee-core-1.9.0/.travis.yml`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/LICENSE` & `honeybee-core-1.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/setup.py` & `honeybee-core-1.9.0/setup.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/tests/shade_test.py` & `honeybee-core-1.9.0/tests/shade_test.py`

 * *Files 1% similar despite different names*

```diff
@@ -268,7 +268,16 @@
     vertices = [[0, 0, 0], [0, 10, 0], [0, 10, 3], [0, 0, 3]]
     shd = Shade.from_vertices('Rectangle Shade', vertices)
 
     shd_dict = shd.to_dict()
     new_shd = Shade.from_dict(shd_dict)
     assert isinstance(new_shd, Shade)
     assert new_shd.to_dict() == shd_dict
+
+
+def test_writer():
+    """Test the Shade writer object."""
+    vertices = [[0, 0, 0], [0, 10, 0], [0, 10, 3], [0, 0, 3]]
+    shd = Shade.from_vertices('Rectangle Shade', vertices)
+
+    writers = [mod for mod in dir(shd.to) if not mod.startswith('_')]
+    assert len(writers) == 0
```

### Comparing `honeybee-core-1.8.1/tests/aperture_test.py` & `honeybee-core-1.9.0/tests/aperture_test.py`

 * *Files 1% similar despite different names*

```diff
@@ -346,7 +346,16 @@
     vertices = [[0, 0, 0], [0, 10, 0], [0, 10, 3], [0, 0, 3]]
     ap = Aperture.from_vertices('Rectangle Window', vertices)
 
     ap_dict = ap.to_dict()
     new_ap = Aperture.from_dict(ap_dict)
     assert isinstance(new_ap, Aperture)
     assert new_ap.to_dict() == ap_dict
+
+
+def test_writer():
+    """Test the Aperture writer object."""
+    vertices = [[0, 0, 0], [0, 10, 0], [0, 10, 3], [0, 0, 3]]
+    ap = Aperture.from_vertices('Rectangle Window', vertices)
+
+    writers = [mod for mod in dir(ap.to) if not mod.startswith('_')]
+    assert len(writers) == 0
```

### Comparing `honeybee-core-1.8.1/tests/facetype_test.py` & `honeybee-core-1.9.0/tests/facetype_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/tests/typing_test.py` & `honeybee-core-1.9.0/tests/typing_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/tests/model_test.py` & `honeybee-core-1.9.0/tests/model_test.py`

 * *Files 0% similar despite different names*

```diff
@@ -793,7 +793,16 @@
     assert isinstance(new_model.apertures[0], Aperture)
     assert len(new_model.doors) == 1
     assert isinstance(new_model.doors[0], Door)
     assert len(new_model.orphaned_faces) == 0
     assert len(new_model.orphaned_shades) == 0
     assert len(new_model.orphaned_apertures) == 0
     assert len(new_model.orphaned_doors) == 0
+
+
+def test_writer():
+    """Test the Model writer object."""
+    room = Room.from_box('Tiny House Zone', 5, 10, 3)
+    model = Model('Tiny House', [room])
+
+    writers = [mod for mod in dir(model.to) if not mod.startswith('_')]
+    assert len(writers) == 0
```

### Comparing `honeybee-core-1.8.1/tests/boundary_condition_test.py` & `honeybee-core-1.9.0/tests/boundary_condition_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/tests/lockable_test.py` & `honeybee-core-1.9.0/tests/lockable_test.py`

 * *Files identical despite different names*

### Comparing `honeybee-core-1.8.1/tests/face_test.py` & `honeybee-core-1.9.0/tests/face_test.py`

 * *Files 0% similar despite different names*

```diff
@@ -593,7 +593,17 @@
     face = Face.from_vertices('test wall', vertices, face_types.wall,
                               boundary_conditions.ground)
 
     face_dict = face.to_dict()
     new_face = Face.from_dict(face_dict)
     assert isinstance(new_face, Face)
     assert new_face.to_dict() == face_dict
+
+
+def test_writer():
+    """Test the Face writer object."""
+    vertices = [[0, 0, 0], [0, 10, 0], [0, 10, 3], [0, 0, 3]]
+    face = Face.from_vertices('test wall', vertices, face_types.wall,
+                              boundary_conditions.ground)
+
+    writers = [mod for mod in dir(face.to) if not mod.startswith('_')]
+    assert len(writers) == 0
```

### Comparing `honeybee-core-1.8.1/tests/door_test.py` & `honeybee-core-1.9.0/tests/door_test.py`

 * *Files 1% similar despite different names*

```diff
@@ -274,7 +274,16 @@
     vertices = [[0, 0, 0], [0, 10, 0], [0, 10, 3], [0, 0, 3]]
     dr = Door.from_vertices('Rectangle Door', vertices)
 
     dr_dict = dr.to_dict()
     new_dr = Door.from_dict(dr_dict)
     assert isinstance(new_dr, Door)
     assert new_dr.to_dict() == dr_dict
+
+
+def test_writer():
+    """Test the Door writer object."""
+    vertices = [[0, 0, 0], [0, 10, 0], [0, 10, 3], [0, 0, 3]]
+    door = Door.from_vertices('Rectangle Door', vertices)
+
+    writers = [mod for mod in dir(door.to) if not mod.startswith('_')]
+    assert len(writers) == 0
```

### Comparing `honeybee-core-1.8.1/tests/room_test.py` & `honeybee-core-1.9.0/tests/room_test.py`

 * *Files 1% similar despite different names*

```diff
@@ -501,7 +501,15 @@
     """Test the to/from dict of Room objects."""
     room = Room.from_box('Shoe Box Zone', 5, 10, 3)
 
     room_dict = room.to_dict()
     new_room = Room.from_dict(room_dict)
     assert isinstance(new_room, Room)
     assert new_room.to_dict() == room_dict
+
+
+def test_writer():
+    """Test the Room writer object."""
+    room = Room.from_box('Shoe Box Zone', 5, 10, 3)
+
+    writers = [mod for mod in dir(room.to) if not mod.startswith('_')]
+    assert len(writers) == 0
```

