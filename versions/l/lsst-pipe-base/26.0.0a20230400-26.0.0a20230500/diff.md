# Comparing `tmp/lsst-pipe-base-26.0.0a20230400.tar.gz` & `tmp/lsst-pipe-base-26.0.0a20230500.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lsst-pipe-base-26.0.0a20230400.tar", last modified: Thu Jan 26 09:56:38 2023, max compression
+gzip compressed data, was "lsst-pipe-base-26.0.0a20230500.tar", last modified: Thu Feb  2 14:05:08 2023, max compression
```

## Comparing `lsst-pipe-base-26.0.0a20230400.tar` & `lsst-pipe-base-26.0.0a20230500.tar`

### file list

```diff
@@ -1,84 +1,84 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:38.318299 lsst-pipe-base-26.0.0a20230400/
--rw-r--r--   0 runner    (1001) docker     (123)      362 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/COPYRIGHT
--rw-r--r--   0 runner    (1001) docker     (123)    35122 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       33 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1297 2023-01-26 09:56:38.318299 lsst-pipe-base-26.0.0a20230400/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      545 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:38.306299 lsst-pipe-base-26.0.0a20230400/doc/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:38.310299 lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/
--rw-r--r--   0 runner    (1001) docker     (123)     5702 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/CHANGES.rst
--rw-r--r--   0 runner    (1001) docker     (123)    23196 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/creating-a-pipeline.rst
--rw-r--r--   0 runner    (1001) docker     (123)    50757 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/creating-a-pipelinetask.rst
--rw-r--r--   0 runner    (1001) docker     (123)    14975 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/creating-a-task.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1767 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2808 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/task-framework-overview.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4472 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/task-retargeting-howto.rst
--rw-r--r--   0 runner    (1001) docker     (123)    11187 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/testing-a-pipeline-task.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2734 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:38.306299 lsst-pipe-base-26.0.0a20230400/python/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:38.310299 lsst-pipe-base-26.0.0a20230400/python/lsst/
--rw-r--r--   0 runner    (1001) docker     (123)      152 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:38.310299 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/
--rw-r--r--   0 runner    (1001) docker     (123)      152 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:38.314298 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/
--rw-r--r--   0 runner    (1001) docker     (123)      490 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5064 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/_datasetQueryConstraints.py
--rw-r--r--   0 runner    (1001) docker     (123)     7409 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/_dataset_handle.py
--rw-r--r--   0 runner    (1001) docker     (123)    17707 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/_instrument.py
--rw-r--r--   0 runner    (1001) docker     (123)     3466 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/_status.py
--rw-r--r--   0 runner    (1001) docker     (123)    21549 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/_task_metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)    14926 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/butlerQuantumContext.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:38.314298 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cli/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cli/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:38.314298 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cli/cmd/
--rw-r--r--   0 runner    (1001) docker     (123)     1016 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cli/cmd/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2364 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cli/cmd/commands.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:38.314298 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cli/opt/
--rw-r--r--   0 runner    (1001) docker     (123)      965 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cli/opt/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1102 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cli/opt/arguments.py
--rw-r--r--   0 runner    (1001) docker     (123)     1518 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cli/opt/options.py
--rw-r--r--   0 runner    (1001) docker     (123)     2382 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cmdLineTask.py
--rw-r--r--   0 runner    (1001) docker     (123)     9759 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/config.py
--rw-r--r--   0 runner    (1001) docker     (123)    11957 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/configOverrides.py
--rw-r--r--   0 runner    (1001) docker     (123)    14229 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/connectionTypes.py
--rw-r--r--   0 runner    (1001) docker     (123)    37220 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/connections.py
--rw-r--r--   0 runner    (1001) docker     (123)    20863 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/executionButlerBuilder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:38.314298 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/formatters/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/formatters/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2474 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/formatters/pexConfig.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:38.314298 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/graph/
--rw-r--r--   0 runner    (1001) docker     (123)       90 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/graph/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15442 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/graph/_implDetails.py
--rw-r--r--   0 runner    (1001) docker     (123)    17024 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/graph/_loadHelpers.py
--rw-r--r--   0 runner    (1001) docker     (123)    27181 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/graph/_versionDeserializers.py
--rw-r--r--   0 runner    (1001) docker     (123)    51296 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/graph/graph.py
--rw-r--r--   0 runner    (1001) docker     (123)     5566 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/graph/quantumNode.py
--rw-r--r--   0 runner    (1001) docker     (123)    64236 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/graphBuilder.py
--rw-r--r--   0 runner    (1001) docker     (123)     7426 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/pipeTools.py
--rw-r--r--   0 runner    (1001) docker     (123)    52053 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)    38503 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/pipelineIR.py
--rw-r--r--   0 runner    (1001) docker     (123)     8026 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/pipelineTask.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:38.314298 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/script/
--rw-r--r--   0 runner    (1001) docker     (123)     1024 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/script/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2057 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/script/register_instrument.py
--rw-r--r--   0 runner    (1001) docker     (123)     5173 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/script/transfer_from_graph.py
--rw-r--r--   0 runner    (1001) docker     (123)     5092 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/struct.py
--rw-r--r--   0 runner    (1001) docker     (123)    14934 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/task.py
--rw-r--r--   0 runner    (1001) docker     (123)     2436 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/taskFactory.py
--rw-r--r--   0 runner    (1001) docker     (123)    19441 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/testUtils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:38.314298 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3767 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/tests/no_dimensions.py
--rw-r--r--   0 runner    (1001) docker     (123)     4927 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/tests/pipelineStepTester.py
--rw-r--r--   0 runner    (1001) docker     (123)    17031 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/tests/simpleQGraph.py
--rw-r--r--   0 runner    (1001) docker     (123)     3426 2023-01-26 09:56:23.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/timer.py
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-01-26 09:56:38.000000 lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:38.318299 lsst-pipe-base-26.0.0a20230400/python/lsst_pipe_base.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1297 2023-01-26 09:56:38.000000 lsst-pipe-base-26.0.0a20230400/python/lsst_pipe_base.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2561 2023-01-26 09:56:38.000000 lsst-pipe-base-26.0.0a20230400/python/lsst_pipe_base.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:56:38.000000 lsst-pipe-base-26.0.0a20230400/python/lsst_pipe_base.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      183 2023-01-26 09:56:38.000000 lsst-pipe-base-26.0.0a20230400/python/lsst_pipe_base.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-26 09:56:38.000000 lsst-pipe-base-26.0.0a20230400/python/lsst_pipe_base.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:56:37.000000 lsst-pipe-base-26.0.0a20230400/python/lsst_pipe_base.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      168 2023-01-26 09:56:38.318299 lsst-pipe-base-26.0.0a20230400/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.752470 lsst-pipe-base-26.0.0a20230500/
+-rw-r--r--   0 runner    (1001) docker     (123)      362 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/COPYRIGHT
+-rw-r--r--   0 runner    (1001) docker     (123)    35121 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       33 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1297 2023-02-02 14:05:08.752470 lsst-pipe-base-26.0.0a20230500/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      545 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.740470 lsst-pipe-base-26.0.0a20230500/doc/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.744470 lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/
+-rw-r--r--   0 runner    (1001) docker     (123)     5702 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/CHANGES.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    23196 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/creating-a-pipeline.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    50757 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/creating-a-pipelinetask.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    14975 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/creating-a-task.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1767 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2808 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/task-framework-overview.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4472 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/task-retargeting-howto.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    11187 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/testing-a-pipeline-task.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2734 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.740470 lsst-pipe-base-26.0.0a20230500/python/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.744470 lsst-pipe-base-26.0.0a20230500/python/lsst/
+-rw-r--r--   0 runner    (1001) docker     (123)      152 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.744470 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/
+-rw-r--r--   0 runner    (1001) docker     (123)      152 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.748470 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/
+-rw-r--r--   0 runner    (1001) docker     (123)      490 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5064 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/_datasetQueryConstraints.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7409 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/_dataset_handle.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17707 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/_instrument.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3466 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/_status.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21548 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/_task_metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14926 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/butlerQuantumContext.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.748470 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cli/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cli/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.748470 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cli/cmd/
+-rw-r--r--   0 runner    (1001) docker     (123)     1016 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cli/cmd/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2364 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cli/cmd/commands.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.748470 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cli/opt/
+-rw-r--r--   0 runner    (1001) docker     (123)      965 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cli/opt/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1102 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cli/opt/arguments.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1518 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cli/opt/options.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2382 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cmdLineTask.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9758 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11957 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/configOverrides.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14229 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/connectionTypes.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37192 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/connections.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20831 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/executionButlerBuilder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.748470 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/formatters/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/formatters/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2474 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/formatters/pexConfig.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.748470 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/graph/
+-rw-r--r--   0 runner    (1001) docker     (123)       90 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/graph/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15442 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/graph/_implDetails.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11129 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/graph/_loadHelpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27231 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/graph/_versionDeserializers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    51296 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/graph/graph.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5550 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/graph/quantumNode.py
+-rw-r--r--   0 runner    (1001) docker     (123)    64232 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/graphBuilder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7423 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/pipeTools.py
+-rw-r--r--   0 runner    (1001) docker     (123)    55428 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39341 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/pipelineIR.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8026 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/pipelineTask.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.752470 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/script/
+-rw-r--r--   0 runner    (1001) docker     (123)     1024 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/script/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2057 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/script/register_instrument.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5173 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/script/transfer_from_graph.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5092 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/struct.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14934 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/task.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2436 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/taskFactory.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19441 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/testUtils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.752470 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3767 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/tests/no_dimensions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4927 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/tests/pipelineStepTester.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17030 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/tests/simpleQGraph.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3426 2023-02-02 14:04:52.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/timer.py
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-02-02 14:05:08.000000 lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.752470 lsst-pipe-base-26.0.0a20230500/python/lsst_pipe_base.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1297 2023-02-02 14:05:08.000000 lsst-pipe-base-26.0.0a20230500/python/lsst_pipe_base.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2561 2023-02-02 14:05:08.000000 lsst-pipe-base-26.0.0a20230500/python/lsst_pipe_base.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:05:08.000000 lsst-pipe-base-26.0.0a20230500/python/lsst_pipe_base.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      183 2023-02-02 14:05:08.000000 lsst-pipe-base-26.0.0a20230500/python/lsst_pipe_base.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-02-02 14:05:08.000000 lsst-pipe-base-26.0.0a20230500/python/lsst_pipe_base.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:05:08.000000 lsst-pipe-base-26.0.0a20230500/python/lsst_pipe_base.egg-info/zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      168 2023-02-02 14:05:08.752470 lsst-pipe-base-26.0.0a20230500/setup.cfg
```

### Comparing `lsst-pipe-base-26.0.0a20230400/LICENSE` & `lsst-pipe-base-26.0.0a20230500/LICENSE`

 * *Files 0% similar despite different names*

```diff
@@ -668,8 +668,7 @@
 
   The GNU General Public License does not permit incorporating your program
 into proprietary programs.  If your program is a subroutine library, you
 may consider it more useful to permit linking proprietary applications with
 the library.  If this is what you want to do, use the GNU Lesser General
 Public License instead of this License.  But first, please read
 <http://www.gnu.org/philosophy/why-not-lgpl.html>.
-
```

### Comparing `lsst-pipe-base-26.0.0a20230400/PKG-INFO` & `lsst-pipe-base-26.0.0a20230500/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-pipe-base
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: Pipeline infrastructure for the Rubin Science Pipelines.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/pipe_base
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-pipe-base-26.0.0a20230400/README.md` & `lsst-pipe-base-26.0.0a20230500/README.md`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/CHANGES.rst` & `lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/CHANGES.rst`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/creating-a-pipeline.rst` & `lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/creating-a-pipeline.rst`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/creating-a-pipelinetask.rst` & `lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/creating-a-pipelinetask.rst`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/creating-a-task.rst` & `lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/creating-a-task.rst`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/index.rst` & `lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/index.rst`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/task-framework-overview.rst` & `lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/task-framework-overview.rst`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/task-retargeting-howto.rst` & `lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/task-retargeting-howto.rst`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/doc/lsst.pipe.base/testing-a-pipeline-task.rst` & `lsst-pipe-base-26.0.0a20230500/doc/lsst.pipe.base/testing-a-pipeline-task.rst`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/pyproject.toml` & `lsst-pipe-base-26.0.0a20230500/pyproject.toml`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/_datasetQueryConstraints.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/_datasetQueryConstraints.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/_dataset_handle.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/_dataset_handle.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/_instrument.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/_instrument.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/_status.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/_status.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/_task_metadata.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/_task_metadata.py`

 * *Files 0% similar despite different names*

```diff
@@ -165,15 +165,14 @@
             Name of the metadata property.
         value
             Metadata property value.
         """
         keys = self._getKeys(name)
         key0 = keys.pop(0)
         if len(keys) == 0:
-
             # If add() is being used, always store the value in the arrays
             # property as a list. It's likely there will be another call.
             slot_type, value = self._validate_value(value)
             if slot_type == "array":
                 pass
             elif slot_type == "scalar":
                 value = [value]
```

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/butlerQuantumContext.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/butlerQuantumContext.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cli/cmd/__init__.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cli/cmd/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cli/cmd/commands.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cli/cmd/commands.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cli/opt/__init__.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cli/opt/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cli/opt/arguments.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cli/opt/arguments.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cli/opt/options.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cli/opt/options.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/cmdLineTask.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/cmdLineTask.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/config.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/config.py`

 * *Files 1% similar despite different names*

```diff
@@ -67,15 +67,15 @@
     def _validateValue(self, value: Any) -> None:
         if value is None:
             return
 
         if not (isinstance(value, str) or isinstance(value, Number)):
             raise TypeError(
                 f"Value {value} is of incorrect type {pexConfig.config._typeStr(value)}."
-                f" Expected type str or a number"
+                " Expected type str or a number"
             )
         if self.check is not None and not self.check(value):
             ValueError("Value {value} is not a valid value")
 
     def __set__(
         self,
         instance: pexConfig.Config,
```

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/configOverrides.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/configOverrides.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/connectionTypes.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/connectionTypes.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/connections.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/connections.py`

 * *Files 0% similar despite different names*

```diff
@@ -141,16 +141,15 @@
                         kwargs["dimensions"] = base.dimensions
                         break
                 if "dimensions" not in kwargs:
                     raise dimensionsValueError
             try:
                 if isinstance(kwargs["dimensions"], str):
                     raise TypeError(
-                        "Dimensions must be iterable of dimensions, got str,"
-                        "possibly omitted trailing comma"
+                        "Dimensions must be iterable of dimensions, got str,possibly omitted trailing comma"
                     )
                 if not isinstance(kwargs["dimensions"], typing.Iterable):
                     raise TypeError("Dimensions must be iterable of dimensions")
                 dct["dimensions"] = set(kwargs["dimensions"])
             except TypeError as exc:
                 raise dimensionsValueError from exc
             # Lookup any python string templates that may have been used in the
@@ -194,15 +193,15 @@
                     raise TypeError(f"Default template keys were not provided for {templateDifference}")
                 # Verify that templates do not share names with variable names
                 # used for a connection, this is needed because of how
                 # templates are specified in an associated config class.
                 nameTemplateIntersection = allTemplates.intersection(set(dct["allConnections"].keys()))
                 if len(nameTemplateIntersection) > 0:
                     raise TypeError(
-                        f"Template parameters cannot share names with Class attributes"
+                        "Template parameters cannot share names with Class attributes"
                         f" (conflicts are {nameTemplateIntersection})."
                     )
             dct["defaultTemplates"] = kwargs.get("defaultTemplates", {})
 
         # Convert all the connection containers into frozensets so they cannot
         # be modified at the class scope
         for connectionName in ("inputs", "prerequisiteInputs", "outputs", "initInputs", "initOutputs"):
```

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/executionButlerBuilder.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/executionButlerBuilder.py`

 * *Files 0% similar despite different names*

```diff
@@ -30,15 +30,15 @@
 from lsst.daf.butler import Butler, Config, DataCoordinate, DatasetRef, DatasetType
 from lsst.daf.butler.core.repoRelocation import BUTLER_ROOT_TAG
 from lsst.daf.butler.registry import ConflictingDefinitionError
 from lsst.daf.butler.transfers import RepoExportContext
 from lsst.resources import ResourcePath, ResourcePathExpression
 from lsst.utils.introspection import get_class_of
 
-from .graph import QuantumGraph, QuantumNode
+from .graph import QuantumGraph
 from .pipeline import PipelineDatasetTypes
 
 DataSetTypeMap = Mapping[DatasetType, Set[DataCoordinate]]
 
 
 def _validate_dataset_type(
     candidate: DatasetType, previous: dict[Union[str, DatasetType], DatasetType]
@@ -138,15 +138,14 @@
     for dataset_type in itertools.chain(dataset_types.initIntermediates, dataset_types.initOutputs):
         dataset_type = _validate_dataset_type(dataset_type, datasetTypes)
         inserts[dataset_type].add(DataCoordinate.makeEmpty(dataset_type.dimensions.universe))
 
     # Output references may be resolved even if they do not exist. Find all
     # actually existing refs.
     check_refs: Set[DatasetRef] = set()
-    n: QuantumNode
     for quantum in (n.quantum for n in graph):
         for attrName in ("initInputs", "inputs", "outputs"):
             attr: Mapping[DatasetType, Union[DatasetRef, List[DatasetRef]]] = getattr(quantum, attrName)
             for type, refs in attr.items():
                 # This if block is because init inputs has a different
                 # signature for its items
                 if not isinstance(refs, list):
```

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/formatters/pexConfig.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/formatters/pexConfig.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/graph/_implDetails.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/graph/_implDetails.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/graph/_loadHelpers.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/graph/_loadHelpers.py`

 * *Files 26% similar despite different names*

```diff
@@ -18,193 +18,139 @@
 #
 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.
 from __future__ import annotations
 
 __all__ = ("LoadHelper",)
 
-import functools
-import io
 import struct
+from contextlib import ExitStack
 from dataclasses import dataclass
+from io import BufferedRandom, BytesIO
 from types import TracebackType
-from typing import (
-    TYPE_CHECKING,
-    Any,
-    BinaryIO,
-    Callable,
-    ContextManager,
-    Iterable,
-    Optional,
-    Set,
-    Type,
-    TypeVar,
-    Union,
-)
+from typing import TYPE_CHECKING, BinaryIO, ContextManager, Iterable, Optional, Set, Type, Union
 from uuid import UUID
 
 from lsst.daf.butler import DimensionUniverse
-from lsst.resources import ResourcePath
-from lsst.resources.file import FileResourcePath
-from lsst.resources.s3 import S3ResourcePath
+from lsst.resources import ResourceHandleProtocol, ResourcePath
 
 if TYPE_CHECKING:
     from ._versionDeserializers import DeserializerBase
     from .graph import QuantumGraph
 
 
-_T = TypeVar("_T")
-
-
-# Create a custom dict that will return the desired default if a key is missing
-class RegistryDict(dict):
-    def __missing__(self, key: Any) -> Type[DefaultLoadHelper]:
-        return DefaultLoadHelper
-
-
-# Create a registry to hold all the load Helper classes
-HELPER_REGISTRY = RegistryDict()
-
-
-def register_helper(URIClass: Union[Type[ResourcePath], Type[BinaryIO]]) -> Callable[[_T], _T]:
-    """Used to register classes as Load helpers
-
-    When decorating a class the parameter is the class of "handle type", i.e.
-    a ResourcePath type or open file handle that will be used to do the
-    loading. This is then associated with the decorated class such that when
-    the parameter type is used to load data, the appropriate helper to work
-    with that data type can be returned.
-
-    A decorator is used so that in theory someone could define another handler
-    in a different module and register it for use.
+@dataclass
+class LoadHelper(ContextManager["LoadHelper"]):
+    """This is a helper class to assist with selecting the appropriate loader
+    and managing any contexts that may be needed.
 
-    Parameters
-    ----------
-    URIClass : Type of `~lsst.resources.ResourcePath` or `~IO` of bytes
-        type for which the decorated class should be mapped to
+    This helper will raise a `ValueError` if the specified file does not appear
+    to be a valid `QuantumGraph` save file.
     """
 
-    def wrapper(class_: _T) -> _T:
-        HELPER_REGISTRY[URIClass] = class_
-        return class_
-
-    return wrapper
-
-
-class DefaultLoadHelper:
-    """Default load helper for `QuantumGraph` save files
-
-    This class, and its subclasses, are used to unpack a quantum graph save
-    file. This file is a binary representation of the graph in a format that
-    allows individual nodes to be loaded without needing to load the entire
-    file.
-
-    This default implementation has the interface to load select nodes
-    from disk, but actually always loads the entire save file and simply
-    returns what nodes (or all) are requested. This is intended to serve for
-    all cases where there is a read method on the input parameter, but it is
-    unknown how to read select bytes of the stream. It is the responsibility of
-    sub classes to implement the method responsible for loading individual
-    bytes from the stream.
-
-    Parameters
-    ----------
-    uriObject : `~lsst.resources.ResourcePath` or `IO` of bytes
-        This is the object that will be used to retrieve the raw bytes of the
-        save.
-    minimumVersion : `int`
-        Minimum version of a save file to load. Set to -1 to load all
-        versions. Older versions may need to be loaded, and re-saved
-        to upgrade them to the latest format. This upgrade may not happen
-        deterministically each time an older graph format is loaded. Because
-        of this behavior, the minimumVersion parameter, forces a user to
-        interact manually and take this into account before they can be used in
-        production.
-
-    Raises
-    ------
-    ValueError
-        Raised if the specified file contains the wrong file signature and is
-        not a `QuantumGraph` save, or if the graph save version is below the
-        minimum specified version.
+    uri: Union[ResourcePath, BinaryIO]
+    """ResourcePath object from which the `QuantumGraph` is to be loaded
+    """
+    minimumVersion: int
+    """
+    Minimum version of a save file to load. Set to -1 to load all
+    versions. Older versions may need to be loaded, and re-saved
+    to upgrade them to the latest format before they can be used in
+    production.
     """
 
-    def __init__(self, uriObject: Union[ResourcePath, BinaryIO], minimumVersion: int):
-        headerBytes = self.__setup_impl(uriObject, minimumVersion)
-        self.headerInfo = self.deserializer.readHeaderInfo(headerBytes)
+    def __post_init__(self) -> None:
+        self._resourceHandle: Optional[ResourceHandleProtocol] = None
+        self._exitStack = ExitStack()
 
-    def __setup_impl(self, uriObject: Union[ResourcePath, BinaryIO], minimumVersion: int) -> bytes:
-        self.uriObject = uriObject
+    def _initialize(self) -> None:
         # need to import here to avoid cyclic imports
         from ._versionDeserializers import DESERIALIZER_MAP
-        from .graph import MAGIC_BYTES, SAVE_VERSION, STRUCT_FMT_BASE
+        from .graph import MAGIC_BYTES, STRUCT_FMT_BASE
 
         # Read the first few bytes which correspond to the  magic identifier
         # bytes, and save version
         magicSize = len(MAGIC_BYTES)
         # read in just the fmt base to determine the save version
         fmtSize = struct.calcsize(STRUCT_FMT_BASE)
         preambleSize = magicSize + fmtSize
         headerBytes = self._readBytes(0, preambleSize)
         magic = headerBytes[:magicSize]
         versionBytes = headerBytes[magicSize:]
 
+        save_version = self._validateSave(magic, versionBytes)
+
+        # select the appropriate deserializer for this save version
+        deserializerClass = DESERIALIZER_MAP[save_version]
+
+        # read in the bytes corresponding to the mappings and initialize the
+        # deserializer. This will be the bytes that describe the following
+        # byte boundaries of the header info
+        sizeBytes = self._readBytes(preambleSize, preambleSize + deserializerClass.structSize)
+        # DeserializerBase subclasses are required to have the same constructor
+        # signature as the base class itself, but there is no way to express
+        # this in the type system, so we just tell MyPy to ignore it.
+        self.deserializer: DeserializerBase = deserializerClass(preambleSize, sizeBytes)
+        # get the header byte range for later reading
+        self.headerBytesRange = (preambleSize + deserializerClass.structSize, self.deserializer.headerSize)
+
+    def _validateSave(self, magic: bytes, versionBytes: bytes) -> int:
+        """Implement validation on input file, prior to attempting to load it
+
+        Paramters
+        ---------
+        magic : `bytes`
+            The first few bytes of the file, used to verify it is a
+            QuantumGraph save file
+        versionBytes : `bytes`
+            The next few bytes from the beginning of the file, used to parse
+            which version of the QuantumGraph file the save corresponds to
+
+        Returns
+        -------
+        save_version : `int`
+            The save version parsed from the supplied bytes
+
+        Raises
+        ------
+        ValueError
+            Raised if the specified file contains the wrong file signature and
+            is not a `QuantumGraph` save, or if the graph save version is
+            below the minimum specified version.
+        """
+        from .graph import MAGIC_BYTES, SAVE_VERSION, STRUCT_FMT_BASE
+
         if magic != MAGIC_BYTES:
             raise ValueError(
                 "This file does not appear to be a quantum graph save got magic bytes "
                 f"{magic!r}, expected {MAGIC_BYTES!r}"
             )
 
         # unpack the save version bytes and verify it is a version that this
         # code can understand
         (save_version,) = struct.unpack(STRUCT_FMT_BASE, versionBytes)
         # loads can sometimes trigger upgrades in format to a latest version,
         # in which case accessory code might not match the upgraded graph.
         # I.E. switching from old node number to UUID. This clause necessitates
         # that users specifically interact with older graph versions and verify
         # everything happens appropriately.
-        if save_version < minimumVersion:
+        if save_version < self.minimumVersion:
             raise ValueError(
                 f"The loaded QuantumGraph is version {save_version}, and the minimum "
-                f"version specified is {minimumVersion}. Please re-run this method "
+                f"version specified is {self.minimumVersion}. Please re-run this method "
                 "with a lower minimum version, then re-save the graph to automatically upgrade"
                 "to the newest version. Older versions may not work correctly with newer code"
             )
 
         if save_version > SAVE_VERSION:
-            raise RuntimeError(
+            raise ValueError(
                 f"The version of this save file is {save_version}, but this version of"
                 f"Quantum Graph software only knows how to read up to version {SAVE_VERSION}"
             )
-
-        # select the appropriate deserializer for this save version
-        deserializerClass = DESERIALIZER_MAP[save_version]
-
-        # read in the bytes corresponding to the mappings and initialize the
-        # deserializer. This will be the bytes that describe the following
-        # byte boundaries of the header info
-        sizeBytes = self._readBytes(preambleSize, preambleSize + deserializerClass.structSize)
-        # DeserializerBase subclasses are required to have the same constructor
-        # signature as the base class itself, but there is no way to express
-        # this in the type system, so we just tell MyPy to ignore it.
-        self.deserializer: DeserializerBase = deserializerClass(preambleSize, sizeBytes)  # type: ignore
-
-        # get the header info
-        headerBytes = self._readBytes(
-            preambleSize + deserializerClass.structSize, self.deserializer.headerSize
-        )
-        return headerBytes
-
-    @classmethod
-    def dumpHeader(cls, uriObject: Union[ResourcePath, BinaryIO], minimumVersion: int = 3) -> Optional[str]:
-        instance = cls.__new__(cls)
-        headerBytes = instance.__setup_impl(uriObject, minimumVersion)
-        header = instance.deserializer.unpackHeader(headerBytes)
-        instance.close()
-        return header
+        return save_version
 
     def load(
         self,
         universe: Optional[DimensionUniverse] = None,
         nodes: Optional[Iterable[Union[UUID, str]]] = None,
         graphID: Optional[str] = None,
     ) -> QuantumGraph:
@@ -238,178 +184,85 @@
         Raises
         ------
         ValueError
             Raised if one or more of the nodes requested is not in the
             `QuantumGraph` or if graphID parameter does not match the graph
             being loaded.
         RuntimeError
-            Raise if Supplied DimensionUniverse is not compatible with the
+            Raised if Supplied DimensionUniverse is not compatible with the
             DimensionUniverse saved in the graph
+            Raised if the method was not called from within a context block
         """
+        if self._resourceHandle is None:
+            raise RuntimeError("Load can only be used within a context manager")
+
+        headerInfo = self.deserializer.readHeaderInfo(self._readBytes(*self.headerBytesRange))
         # verify this is the expected graph
-        if graphID is not None and self.headerInfo._buildId != graphID:
+        if graphID is not None and headerInfo._buildId != graphID:
             raise ValueError("graphID does not match that of the graph being loaded")
         # Read in specified nodes, or all the nodes
         nodeSet: Set[UUID]
         if nodes is None:
-            nodeSet = set(self.headerInfo.map.keys())
-            # if all nodes are to be read, force the reader from the base class
-            # that will read all they bytes in one go
-            _readBytes: Callable[[int, int], bytes] = functools.partial(DefaultLoadHelper._readBytes, self)
+            nodeSet = set(headerInfo.map.keys())
         else:
             # only some bytes are being read using the reader specialized for
             # this class
             # create a set to ensure nodes are only loaded once
             nodeSet = {UUID(n) if isinstance(n, str) else n for n in nodes}
             # verify that all nodes requested are in the graph
-            remainder = nodeSet - self.headerInfo.map.keys()
+            remainder = nodeSet - headerInfo.map.keys()
             if remainder:
                 raise ValueError(
                     f"Nodes {remainder} were requested, but could not be found in the input graph"
                 )
-            _readBytes = self._readBytes
+        _readBytes = self._readBytes
         if universe is None:
-            universe = self.headerInfo.universe
+            universe = headerInfo.universe
         return self.deserializer.constructGraph(nodeSet, _readBytes, universe)
 
     def _readBytes(self, start: int, stop: int) -> bytes:
-        """Loads the specified byte range from the ResourcePath object
-
-        In the base class, this actually will read all the bytes into a buffer
-        from the specified ResourcePath object. Then for each method call will
-        return the requested byte range. This is the most flexible
-        implementation, as no special read is required. This will not give a
-        speed up with any sub graph reads though.
-        """
-        if not hasattr(self, "buffer"):
-            self.buffer = self.uriObject.read()
-        return self.buffer[start:stop]
-
-    def close(self) -> None:
-        """Cleans up an instance if needed. Base class does nothing"""
-        pass
-
-
-@register_helper(S3ResourcePath)
-class S3LoadHelper(DefaultLoadHelper):
-    # This subclass implements partial loading of a graph using a s3 uri
-    def _readBytes(self, start: int, stop: int) -> bytes:
-        args = {}
-        # minus 1 in the stop range, because this header is inclusive rather
-        # than standard python where the end point is generally exclusive
-        args["Range"] = f"bytes={start}-{stop-1}"
-        try:
-            response = self.uriObject.client.get_object(
-                Bucket=self.uriObject.netloc, Key=self.uriObject.relativeToPathRoot, **args
-            )
-        except (
-            self.uriObject.client.exceptions.NoSuchKey,
-            self.uriObject.client.exceptions.NoSuchBucket,
-        ) as err:
-            raise FileNotFoundError(f"No such resource: {self.uriObject}") from err
-        body = response["Body"].read()
-        response["Body"].close()
-        return body
-
-    uriObject: S3ResourcePath
-
-
-@register_helper(FileResourcePath)
-class FileLoadHelper(DefaultLoadHelper):
-    # This subclass implements partial loading of a graph using a file uri
-    def _readBytes(self, start: int, stop: int) -> bytes:
-        if not hasattr(self, "fileHandle"):
-            self.fileHandle = open(self.uriObject.ospath, "rb")
-        self.fileHandle.seek(start)
-        return self.fileHandle.read(stop - start)
-
-    def close(self) -> None:
-        if hasattr(self, "fileHandle"):
-            self.fileHandle.close()
-
-    uriObject: FileResourcePath
-
-
-@register_helper(BinaryIO)
-class OpenFileHandleHelper(DefaultLoadHelper):
-    # This handler is special in that it does not get initialized with a
-    # ResourcePath, but an open file handle.
-
-    # Most everything stays the same, the variable is even stored as uriObject,
-    # because the interface needed for reading is the same. Unfortunately
-    # because we do not have Protocols yet, this can not be nicely expressed
-    # with typing.
-
-    # This helper does support partial loading
-
-    def __init__(self, uriObject: BinaryIO, minimumVersion: int):
-        # Explicitly annotate type and not infer from super
-        self.uriObject: BinaryIO
-        super().__init__(uriObject, minimumVersion=minimumVersion)
-        # This differs from the default __init__ to force the io object
-        # back to the beginning so that in the case the entire file is to
-        # read in the file is not already in a partially read state.
-        self.uriObject.seek(0)
-
-    def _readBytes(self, start: int, stop: int) -> bytes:
-        self.uriObject.seek(start)
-        result = self.uriObject.read(stop - start)
-        return result
-
-
-@dataclass
-class LoadHelper(ContextManager[DefaultLoadHelper]):
-    """This is a helper class to assist with selecting the appropriate loader
-    and managing any contexts that may be needed.
-
-    Note
-    ----
-    This class may go away or be modified in the future if some of the
-    features of this module can be propagated to
-    `~lsst.resources.ResourcePath`.
+        """Load the specified byte range from the ResourcePath object
 
-    This helper will raise a `ValueError` if the specified file does not appear
-    to be a valid `QuantumGraph` save file.
-    """
+        Parameters
+        ----------
+        start : `int`
+            The beginning byte location to read
+        end : `int`
+            The end byte location to read
 
-    uri: Union[ResourcePath, BinaryIO]
-    """ResourcePath object from which the `QuantumGraph` is to be loaded
-    """
-    minimumVersion: int
-    """
-    Minimum version of a save file to load. Set to -1 to load all
-    versions. Older versions may need to be loaded, and re-saved
-    to upgrade them to the latest format before they can be used in
-    production.
-    """
+        Returns
+        -------
+        result : `bytes`
+            The byte range specified from the `ResourceHandle`
 
-    def __enter__(self) -> DefaultLoadHelper:
-        # Only one handler is registered for anything that is an instance of
-        # IOBase, so if any type is a subtype of that, set the key explicitly
-        # so the correct loader is found, otherwise index by the type
-        self._loaded = self._determineLoader()(self.uri, self.minimumVersion)
-        return self._loaded
+        Raises
+        ------
+        RuntimeError
+            Raise if the method was not called from within a context block
+        """
+        if self._resourceHandle is None:
+            raise RuntimeError("_readBytes must be called from within a context block")
+        self._resourceHandle.seek(start)
+        return self._resourceHandle.read(stop - start)
+
+    def __enter__(self) -> "LoadHelper":
+        if isinstance(self.uri, (BinaryIO, BytesIO, BufferedRandom)):
+            self._resourceHandle = self.uri
+        else:
+            self._resourceHandle = self._exitStack.enter_context(self.uri.open("rb"))
+        self._initialize()
+        return self
 
     def __exit__(
         self,
         type: Optional[Type[BaseException]],
         value: Optional[BaseException],
         traceback: Optional[TracebackType],
     ) -> None:
-        self._loaded.close()
-
-    def _determineLoader(self) -> Type[DefaultLoadHelper]:
-        key: Union[Type[ResourcePath], Type[BinaryIO]]
-        # Typing for file-like types is a mess; BinaryIO isn't actually
-        # a base class of what open(..., 'rb') returns, and MyPy claims
-        # that IOBase and BinaryIO actually have incompatible method
-        # signatures.  IOBase *is* a base class of what open(..., 'rb')
-        # returns, so it's what we have to use at runtime.
-        if isinstance(self.uri, io.IOBase):  # type: ignore
-            key = BinaryIO
-        else:
-            key = type(self.uri)
-        return HELPER_REGISTRY[key]
+        assert self._resourceHandle is not None
+        self._exitStack.close()
+        self._resourceHandle = None
 
     def readHeader(self) -> Optional[str]:
-        type_ = self._determineLoader()
-        return type_.dumpHeader(self.uri, self.minimumVersion)
+        with self as handle:
+            result = handle.deserializer.unpackHeader(self._readBytes(*self.headerBytesRange))
+        return result
```

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/graph/_versionDeserializers.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/graph/_versionDeserializers.py`

 * *Files 2% similar despite different names*

```diff
@@ -643,8 +643,12 @@
         newGraph._initInputRefs = initInputRefs
         newGraph._initOutputRefs = initOutputRefs
         newGraph._globalInitOutputRefs = self.infoMappings.globalInitOutputRefs
         newGraph._universe = universe
         return newGraph
 
 
-DESERIALIZER_MAP = {1: DeserializerV1, 2: DeserializerV2, 3: DeserializerV3}
+DESERIALIZER_MAP: dict[int, Type[DeserializerBase]] = {
+    1: DeserializerV1,
+    2: DeserializerV2,
+    3: DeserializerV3,
+}
```

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/graph/graph.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/graph/graph.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/graph/quantumNode.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/graph/quantumNode.py`

 * *Files 1% similar despite different names*

```diff
@@ -114,16 +114,15 @@
         by the default quantum id based hashing
         """
         return self._precomputedHash
 
     def __repr__(self) -> str:
         """Make more human readable string representation."""
         return (
-            f"{self.__class__.__name__}(quantum={self.quantum}, "
-            f"taskDef={self.taskDef}, nodeId={self.nodeId})"
+            f"{self.__class__.__name__}(quantum={self.quantum}, taskDef={self.taskDef}, nodeId={self.nodeId})"
         )
 
     def to_simple(self, accumulator: Optional[DimensionRecordsAccumulator] = None) -> SerializedQuantumNode:
         return SerializedQuantumNode(
             quantum=self.quantum.to_simple(accumulator=accumulator),
             taskLabel=self.taskDef.label,
             nodeId=self.nodeId,
```

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/graphBuilder.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/graphBuilder.py`

 * *Files 0% similar despite different names*

```diff
@@ -1025,18 +1025,18 @@
                     resolvedRef if component is None else resolvedRef.makeComponentRef(component)
                 )
             if dataIdsNotFoundYet:
                 if constrainedByAllDatasets:
                     raise RuntimeError(
                         f"{len(dataIdsNotFoundYet)} dataset(s) of type "
                         f"'{datasetType.name}' was/were present in a previous "
-                        f"query, but could not be found now. "
-                        f"This is either a logic bug in QuantumGraph generation "
-                        f"or the input collections have been modified since "
-                        f"QuantumGraph generation began."
+                        "query, but could not be found now. "
+                        "This is either a logic bug in QuantumGraph generation "
+                        "or the input collections have been modified since "
+                        "QuantumGraph generation began."
                     )
                 else:
                     # if the common dataIds were not constrained using all the
                     # input dataset types, it is possible that some data ids
                     # found dont correspond to existing dataset types and they
                     # will be un-resolved. Mark these for later pruning from
                     # the quantum graph.
```

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/pipeTools.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/pipeTools.py`

 * *Files 0% similar despite different names*

```diff
@@ -98,25 +98,23 @@
     dataset type.
     `MissingTaskFactoryError` is raised when TaskFactory is needed but not
     provided.
     """
     # Build a map of DatasetType name to producer's index in a pipeline
     producerIndex = {}
     for idx, taskDef in enumerate(pipeline):
-
         for attr in iterConnections(taskDef.connections, "outputs"):
             if attr.name in producerIndex:
                 raise DuplicateOutputError(
                     "DatasetType `{}' appears more than once as output".format(attr.name)
                 )
             producerIndex[attr.name] = idx
 
     # check all inputs that are also someone's outputs
     for idx, taskDef in enumerate(pipeline):
-
         # get task input DatasetTypes, this can only be done via class method
         inputs = {name: getattr(taskDef.connections, name) for name in taskDef.connections.inputs}
         for dsTypeDescr in inputs.values():
             # all pre-existing datasets have effective index -1
             prodIdx = producerIndex.get(dsTypeDescr.name, -1)
             if prodIdx >= idx:
                 # not good, producer is downstream
@@ -176,15 +174,14 @@
     preExisting = allInputs - allOutputs
     outputs[-1] = preExisting
 
     # Set of nodes with no incoming edges, initially set to pseudo-node
     queue = [-1]
     result = []
     while queue:
-
         # move to final list, drop -1
         idx = queue.pop(0)
         if idx >= 0:
             result.append(idx)
 
         # remove task outputs from other tasks inputs
         thisTaskOutputs = outputs.get(idx, set())
```

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/pipeline.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/pipeline.py`

 * *Files 3% similar despite different names*

```diff
@@ -376,16 +376,15 @@
             pipeline._pipelineIR.contracts = []
             labels = {taskdef.label: True for taskdef in pipeline.toExpandedPipeline()}
 
             # Verify the bounds are in the labels
             if labelSpecifier.begin is not None:
                 if labelSpecifier.begin not in labels:
                     raise ValueError(
-                        f"Beginning of range subset, {labelSpecifier.begin}, not found in "
-                        "pipeline definition"
+                        f"Beginning of range subset, {labelSpecifier.begin}, not found in pipeline definition"
                     )
             if labelSpecifier.end is not None:
                 if labelSpecifier.end not in labels:
                     raise ValueError(
                         f"End of range subset, {labelSpecifier.end}, not found in pipeline definition"
                     )
 
@@ -497,14 +496,104 @@
         pipeline: `Pipeline`
         """
         return cls.fromIR(copy.deepcopy(pipeline._pipelineIR))
 
     def __str__(self) -> str:
         return str(self._pipelineIR)
 
+    def mergePipeline(self, pipeline: Pipeline) -> None:
+        """Merge another in-memory `Pipeline` object into this one.
+
+        This merges another pipeline into this object, as if it were declared
+        in the import block of the yaml definition of this pipeline. This
+        modifies this pipeline in place.
+
+        Parameters
+        ----------
+        pipeline : `Pipeline`
+            The `Pipeline` object that is to be merged into this object.
+        """
+        self._pipelineIR.merge_pipelines((pipeline._pipelineIR,))
+
+    def addLabelToSubset(self, subset: str, label: str) -> None:
+        """Add a task label from the specified subset.
+
+        Parameters
+        ----------
+        subset : `str`
+            The labeled subset to modify
+        label : `str`
+            The task label to add to the specified subset.
+
+        Raises
+        ------
+        ValueError
+            Raised if the specified subset does not exist within the pipeline.
+            Raised if the specified label does not exist within the pipeline.
+        """
+        if label not in self._pipelineIR.tasks:
+            raise ValueError(f"Label {label} does not appear within the pipeline")
+        if subset not in self._pipelineIR.labeled_subsets:
+            raise ValueError(f"Subset {subset} does not appear within the pipeline")
+        self._pipelineIR.labeled_subsets[subset].subset.add(label)
+
+    def removeLabelFromSubset(self, subset: str, label: str) -> None:
+        """Remove a task label from the specified subset.
+
+        Parameters
+        ----------
+        subset : `str`
+            The labeled subset to modify
+        label : `str`
+            The task label to remove from the specified subset.
+
+        Raises
+        ------
+        ValueError
+            Raised if the specified subset does not exist in the pipeline.
+            Raised if the specified label does not exist within the specified
+            subset.
+        """
+        if subset not in self._pipelineIR.labeled_subsets:
+            raise ValueError(f"Subset {subset} does not appear within the pipeline")
+        if label not in self._pipelineIR.labeled_subsets[subset].subset:
+            raise ValueError(f"Label {label} does not appear within the pipeline")
+        self._pipelineIR.labeled_subsets[subset].subset.remove(label)
+
+    def findSubsetsWithLabel(self, label: str) -> set[str]:
+        """Find any subsets which may contain the specified label.
+
+        This function returns the name of subsets which return the specified
+        label. May return an empty set if there are no subsets, or no subsets
+        containing the specified label.
+
+        Parameters
+        ----------
+        label : `str`
+            The task label to use in membership check
+
+        Returns
+        -------
+        subsets : `set` of `str`
+            Returns a set (possibly empty) of subsets names which contain the
+            specified label.
+
+        Raises
+        ------
+        ValueError
+            Raised if the specified label does not exist within this pipeline.
+        """
+        results = set()
+        if label not in self._pipelineIR.tasks:
+            raise ValueError(f"Label {label} does not appear within the pipeline")
+        for subset in self._pipelineIR.labeled_subsets.values():
+            if label in subset.subset:
+                results.add(subset.label)
+        return results
+
     def addInstrument(self, instrument: Union[Instrument, str]) -> None:
         """Add an instrument to the pipeline, or replace an instrument that is
         already defined.
 
         Parameters
         ----------
         instrument : `~lsst.daf.butler.instrument.Instrument` or `str`
@@ -879,17 +968,17 @@
                 if "skypix" in dimensions:
                     try:
                         datasetType = registry.getDatasetType(c.name)
                     except LookupError as err:
                         raise LookupError(
                             f"DatasetType '{c.name}' referenced by "
                             f"{type(taskDef.connections).__name__} uses 'skypix' as a dimension "
-                            f"placeholder, but does not already exist in the registry.  "
-                            f"Note that reference catalog names are now used as the dataset "
-                            f"type name instead of 'ref_cat'."
+                            "placeholder, but does not already exist in the registry.  "
+                            "Note that reference catalog names are now used as the dataset "
+                            "type name instead of 'ref_cat'."
                         ) from err
                     rest1 = set(registry.dimensions.extract(dimensions - set(["skypix"])).names)
                     rest2 = set(
                         dim.name for dim in datasetType.dimensions if not isinstance(dim, SkyPixDimension)
                     )
                     if rest1 != rest2:
                         raise ValueError(
@@ -1254,15 +1343,14 @@
             # Package versions dataset type
             yield cls.packagesDatasetName
 
         if isinstance(pipeline, Pipeline):
             pipeline = pipeline.toExpandedPipeline()
 
         for taskDef in pipeline:
-
             # all task InitOutputs
             for name in taskDef.connections.initOutputs:
                 attribute = getattr(taskDef.connections, name)
                 yield attribute.name
 
             # config dataset name
             if include_configs:
```

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/pipelineIR.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/pipelineIR.py`

 * *Files 2% similar despite different names*

```diff
@@ -31,14 +31,15 @@
 from collections.abc import Iterable as abcIterable
 from dataclasses import dataclass, field
 from typing import (
     Any,
     Dict,
     Generator,
     Hashable,
+    Iterable,
     List,
     Literal,
     Mapping,
     MutableMapping,
     Optional,
     Set,
     Union,
@@ -660,26 +661,47 @@
         if tmp_import is None:
             self.imports: List[ImportIR] = []
         elif isinstance(tmp_import, list):
             self.imports = [ImportIR(**process_args(args)) for args in tmp_import]
         else:
             self.imports = [ImportIR(**process_args(tmp_import))]
 
+        self.merge_pipelines([fragment.toPipelineIR() for fragment in self.imports])
+
+    def merge_pipelines(self, pipelines: Iterable[PipelineIR]) -> None:
+        """Merge one or more other `PipelineIR` objects into this object.
+
+        Parameters
+        ----------
+        pipelines : `Iterable` of `PipelineIR` objects
+            An `Iterable` that contains one or more `PipelineIR` objects to
+            merge into this object.
+
+        Raises
+        ------
+        ValueError
+            Raised if there is a conflict in instrument specifications.
+            Raised if a task label appears in more than one of the input
+            `PipelineIR` objects which are to be merged.
+            Raised if a labeled subset appears in more than one of the input
+            `PipelineIR` objects which are to be merged, and with any subset
+            existing in this object.
+        """
         # integrate any imported pipelines
         accumulate_tasks: Dict[str, TaskIR] = {}
         accumulate_labeled_subsets: Dict[str, LabeledSubset] = {}
         accumulated_parameters = ParametersIR({})
-        for other_pipeline in self.imports:
-            tmp_IR = other_pipeline.toPipelineIR()
+
+        for tmp_IR in pipelines:
             if self.instrument is None:
                 self.instrument = tmp_IR.instrument
             elif self.instrument != tmp_IR.instrument and tmp_IR.instrument is not None:
                 msg = (
                     "Only one instrument can be declared in a pipeline or its imports. "
-                    f"Top level pipeline defines {self.instrument} but {other_pipeline.location} "
+                    f"Top level pipeline defines {self.instrument} but pipeline to merge "
                     f"defines {tmp_IR.instrument}."
                 )
                 raise ValueError(msg)
             if duplicate_labels := accumulate_tasks.keys() & tmp_IR.tasks.keys():
                 msg = (
                     "Task labels in the imported pipelines must be unique. "
                     f"These labels appear multiple times: {duplicate_labels}"
```

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/pipelineTask.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/pipelineTask.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/script/__init__.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/script/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/script/register_instrument.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/script/register_instrument.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/script/transfer_from_graph.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/script/transfer_from_graph.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/struct.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/struct.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/task.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/task.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/taskFactory.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/taskFactory.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/testUtils.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/testUtils.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/tests/no_dimensions.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/tests/no_dimensions.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/tests/pipelineStepTester.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/tests/pipelineStepTester.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/tests/simpleQGraph.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/tests/simpleQGraph.py`

 * *Files 1% similar despite different names*

```diff
@@ -123,15 +123,14 @@
     initout = numpy.array([999])
     """InitOutputs for this task"""
 
     taskFactory: Optional[AddTaskFactoryMock] = None
     """Factory that makes instances"""
 
     def run(self, input: int) -> Struct:  # type: ignore
-
         if self.taskFactory:
             # do some bookkeeping
             if self.taskFactory.stopAt == self.taskFactory.countExec:
                 raise RuntimeError("pretend something bad happened")
             self.taskFactory.countExec += 1
 
         self.config = cast(AddTaskConfig, self.config)
```

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst/pipe/base/timer.py` & `lsst-pipe-base-26.0.0a20230500/python/lsst/pipe/base/timer.py`

 * *Files identical despite different names*

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst_pipe_base.egg-info/PKG-INFO` & `lsst-pipe-base-26.0.0a20230500/python/lsst_pipe_base.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-pipe-base
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: Pipeline infrastructure for the Rubin Science Pipelines.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/pipe_base
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-pipe-base-26.0.0a20230400/python/lsst_pipe_base.egg-info/SOURCES.txt` & `lsst-pipe-base-26.0.0a20230500/python/lsst_pipe_base.egg-info/SOURCES.txt`

 * *Files identical despite different names*

