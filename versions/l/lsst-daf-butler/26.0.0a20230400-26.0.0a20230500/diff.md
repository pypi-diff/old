# Comparing `tmp/lsst-daf-butler-26.0.0a20230400.tar.gz` & `tmp/lsst-daf-butler-26.0.0a20230500.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lsst-daf-butler-26.0.0a20230400.tar", last modified: Thu Jan 26 10:05:15 2023, max compression
+gzip compressed data, was "lsst-daf-butler-26.0.0a20230500.tar", last modified: Thu Feb  2 14:13:57 2023, max compression
```

## Comparing `lsst-daf-butler-26.0.0a20230400.tar` & `lsst-daf-butler-26.0.0a20230500.tar`

### file list

```diff
@@ -1,295 +1,295 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.632211 lsst-daf-butler-26.0.0a20230400/
--rw-r--r--   0 runner    (1001) docker     (123)      306 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/COPYRIGHT
--rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       34 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1701 2023-01-26 10:05:15.632211 lsst-daf-butler-26.0.0a20230400/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      841 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.568211 lsst-daf-butler-26.0.0a20230400/doc/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.576211 lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/
--rw-r--r--   0 runner    (1001) docker     (123)    24362 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/CHANGES.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/concreteStorageClasses.rst
--rw-r--r--   0 runner    (1001) docker     (123)     5620 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/configuring.rst
--rw-r--r--   0 runner    (1001) docker     (123)     6436 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/datastores.rst
--rw-r--r--   0 runner    (1001) docker     (123)     9272 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/dimensions.rst
--rw-r--r--   0 runner    (1001) docker     (123)    22653 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/formatters.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4602 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)    10215 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/organizing.rst
--rw-r--r--   0 runner    (1001) docker     (123)    23048 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/queries.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3754 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/use-in-tests.rst
--rw-r--r--   0 runner    (1001) docker     (123)    16368 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/writing-subcommands.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4112 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.572211 lsst-daf-butler-26.0.0a20230400/python/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.576211 lsst-daf-butler-26.0.0a20230400/python/lsst/
--rw-r--r--   0 runner    (1001) docker     (123)       67 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.576211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/
--rw-r--r--   0 runner    (1001) docker     (123)       67 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.580211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/
--rw-r--r--   0 runner    (1001) docker     (123)      627 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   115081 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/_butler.py
--rw-r--r--   0 runner    (1001) docker     (123)     6010 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/_butlerConfig.py
--rw-r--r--   0 runner    (1001) docker     (123)     5474 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/_butlerRepoIndex.py
--rw-r--r--   0 runner    (1001) docker     (123)     4407 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/_deferredDatasetHandle.py
--rw-r--r--   0 runner    (1001) docker     (123)     9972 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/_limited_butler.py
--rw-r--r--   0 runner    (1001) docker     (123)    29167 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/_quantum_backed.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.580211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    13597 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/butler.py
--rw-r--r--   0 runner    (1001) docker     (123)    16072 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/cliLog.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.584211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/cmd/
--rw-r--r--   0 runner    (1001) docker     (123)     1988 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/cmd/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3519 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/cmd/_remove_collections.py
--rw-r--r--   0 runner    (1001) docker     (123)     4921 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/cmd/_remove_runs.py
--rw-r--r--   0 runner    (1001) docker     (123)    31566 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/cmd/commands.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.584211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/opt/
--rw-r--r--   0 runner    (1001) docker     (123)      994 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/opt/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2015 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/opt/arguments.py
--rw-r--r--   0 runner    (1001) docker     (123)     3197 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/opt/optionGroups.py
--rw-r--r--   0 runner    (1001) docker     (123)     9808 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/opt/options.py
--rw-r--r--   0 runner    (1001) docker     (123)     2805 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/progress.py
--rw-r--r--   0 runner    (1001) docker     (123)    41193 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.584211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/
--rw-r--r--   0 runner    (1001) docker     (123)      130 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/datastore.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.584211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/datastores/
--rw-r--r--   0 runner    (1001) docker     (123)      660 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/datastores/composites.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     1994 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/datastores/fileDatastore.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     5125 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/datastores/formatters.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     1417 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/datastores/writeRecipes.yaml
--rw-r--r--   0 runner    (1001) docker     (123)    15416 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/dimensions.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      814 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/registry.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/repo_transfer_formats.yaml
--rw-r--r--   0 runner    (1001) docker     (123)    13420 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/storageClasses.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.592211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/
--rw-r--r--   0 runner    (1001) docker     (123)     1126 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2226 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/_butlerUri.py
--rw-r--r--   0 runner    (1001) docker     (123)     3272 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/_column_categorization.py
--rw-r--r--   0 runner    (1001) docker     (123)     5626 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/_column_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)     5956 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/_column_type_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     5438 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/_topology.py
--rw-r--r--   0 runner    (1001) docker     (123)     5580 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/composites.py
--rw-r--r--   0 runner    (1001) docker     (123)    49204 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/config.py
--rw-r--r--   0 runner    (1001) docker     (123)    14012 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/configSupport.py
--rw-r--r--   0 runner    (1001) docker     (123)     5530 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/constraints.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.596211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)     1027 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/datasets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1947 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/datasets/association.py
--rw-r--r--   0 runner    (1001) docker     (123)    22968 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/datasets/ref.py
--rw-r--r--   0 runner    (1001) docker     (123)    28105 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/datasets/type.py
--rw-r--r--   0 runner    (1001) docker     (123)    45635 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/datastore.py
--rw-r--r--   0 runner    (1001) docker     (123)    39561 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/datastoreCacheManager.py
--rw-r--r--   0 runner    (1001) docker     (123)     8545 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/datastoreRecordData.py
--rw-r--r--   0 runner    (1001) docker     (123)    21911 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/ddl.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.596211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/
--rw-r--r--   0 runner    (1001) docker     (123)     1616 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11519 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_config.py
--rw-r--r--   0 runner    (1001) docker     (123)    40909 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_coordinate.py
--rw-r--r--   0 runner    (1001) docker     (123)    29704 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_dataCoordinateIterable.py
--rw-r--r--   0 runner    (1001) docker     (123)    20098 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_database.py
--rw-r--r--   0 runner    (1001) docker     (123)    13606 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_elements.py
--rw-r--r--   0 runner    (1001) docker     (123)     8724 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_governor.py
--rw-r--r--   0 runner    (1001) docker     (123)    19054 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_graph.py
--rw-r--r--   0 runner    (1001) docker     (123)    10112 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_packer.py
--rw-r--r--   0 runner    (1001) docker     (123)    16954 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_records.py
--rw-r--r--   0 runner    (1001) docker     (123)    12453 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     9069 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_skypix.py
--rw-r--r--   0 runner    (1001) docker     (123)    20010 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_universe.py
--rw-r--r--   0 runner    (1001) docker     (123)     7596 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/construction.py
--rw-r--r--   0 runner    (1001) docker     (123)     1356 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2748 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/fileDataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     3115 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/fileDescriptor.py
--rw-r--r--   0 runner    (1001) docker     (123)    28129 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/fileTemplates.py
--rw-r--r--   0 runner    (1001) docker     (123)    29888 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/formatter.py
--rw-r--r--   0 runner    (1001) docker     (123)     4069 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/json.py
--rw-r--r--   0 runner    (1001) docker     (123)     8582 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/location.py
--rw-r--r--   0 runner    (1001) docker     (123)    17742 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/logging.py
--rw-r--r--   0 runner    (1001) docker     (123)    10062 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/mappingFactory.py
--rw-r--r--   0 runner    (1001) docker     (123)    18559 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/named.py
--rw-r--r--   0 runner    (1001) docker     (123)    15439 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/progress.py
--rw-r--r--   0 runner    (1001) docker     (123)    26100 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/quantum.py
--rw-r--r--   0 runner    (1001) docker     (123)     3332 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/repoRelocation.py
--rw-r--r--   0 runner    (1001) docker     (123)     8901 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/serverModels.py
--rw-r--r--   0 runner    (1001) docker     (123)    35288 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/storageClass.py
--rw-r--r--   0 runner    (1001) docker     (123)    14116 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/storageClassDelegate.py
--rw-r--r--   0 runner    (1001) docker     (123)     8255 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/storedFileInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     9734 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/time_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    44136 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/timespan.py
--rw-r--r--   0 runner    (1001) docker     (123)     3731 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.600211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/datastores/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/datastores/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    40821 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/datastores/chainedDatastore.py
--rw-r--r--   0 runner    (1001) docker     (123)   120809 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/datastores/fileDatastore.py
--rw-r--r--   0 runner    (1001) docker     (123)     8638 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/datastores/genericDatastore.py
--rw-r--r--   0 runner    (1001) docker     (123)    25045 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/datastores/inMemoryDatastore.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.600211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/delegates/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/delegates/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2576 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/delegates/arrowastropy.py
--rw-r--r--   0 runner    (1001) docker     (123)     2552 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/delegates/arrownumpy.py
--rw-r--r--   0 runner    (1001) docker     (123)     4354 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/delegates/arrowtable.py
--rw-r--r--   0 runner    (1001) docker     (123)     5105 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/delegates/dataframe.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.604211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2995 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/astropyTable.py
--rw-r--r--   0 runner    (1001) docker     (123)    13007 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/file.py
--rw-r--r--   0 runner    (1001) docker     (123)     3997 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/json.py
--rw-r--r--   0 runner    (1001) docker     (123)     3887 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/logs.py
--rw-r--r--   0 runner    (1001) docker     (123)     1716 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/matplotlib.py
--rw-r--r--   0 runner    (1001) docker     (123)     4649 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/packages.py
--rw-r--r--   0 runner    (1001) docker     (123)    34243 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/parquet.py
--rw-r--r--   0 runner    (1001) docker     (123)     3703 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/pickle.py
--rw-r--r--   0 runner    (1001) docker     (123)     5514 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/yaml.py
--rw-r--r--   0 runner    (1001) docker     (123)     2787 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/instrument.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.604211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registries/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registries/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    24714 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registries/remote.py
--rw-r--r--   0 runner    (1001) docker     (123)    57927 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registries/sql.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.608211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/
--rw-r--r--   0 runner    (1001) docker     (123)     1500 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4147 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/_collectionType.py
--rw-r--r--   0 runner    (1001) docker     (123)     9148 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/_collection_summary.py
--rw-r--r--   0 runner    (1001) docker     (123)     4043 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/_config.py
--rw-r--r--   0 runner    (1001) docker     (123)    11413 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/_dbAuth.py
--rw-r--r--   0 runner    (1001) docker     (123)     6379 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/_defaults.py
--rw-r--r--   0 runner    (1001) docker     (123)     4947 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/_exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    66793 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/_registry.py
--rw-r--r--   0 runner    (1001) docker     (123)     5127 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/attributes.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.608211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/bridge/
--rw-r--r--   0 runner    (1001) docker     (123)      916 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/bridge/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5055 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/bridge/ephemeral.py
--rw-r--r--   0 runner    (1001) docker     (123)    15612 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/bridge/monolithic.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.608211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/collections/
--rw-r--r--   0 runner    (1001) docker     (123)      916 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/collections/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    20296 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/collections/_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     5409 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/collections/nameKey.py
--rw-r--r--   0 runner    (1001) docker     (123)     7139 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/collections/synthIntKey.py
--rw-r--r--   0 runner    (1001) docker     (123)     5431 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/connectionString.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.608211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/databases/
--rw-r--r--   0 runner    (1001) docker     (123)      916 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/databases/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    19725 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/databases/postgresql.py
--rw-r--r--   0 runner    (1001) docker     (123)    15798 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/databases/sqlite.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.608211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)      916 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/datasets/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.608211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/datasets/byDimensions/
--rw-r--r--   0 runner    (1001) docker     (123)      965 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/datasets/byDimensions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    22078 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/datasets/byDimensions/_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)    41139 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/datasets/byDimensions/_storage.py
--rw-r--r--   0 runner    (1001) docker     (123)    14021 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/datasets/byDimensions/summaries.py
--rw-r--r--   0 runner    (1001) docker     (123)    17971 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/datasets/byDimensions/tables.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.612211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/
--rw-r--r--   0 runner    (1001) docker     (123)      916 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7078 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/caching.py
--rw-r--r--   0 runner    (1001) docker     (123)     7370 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/governor.py
--rw-r--r--   0 runner    (1001) docker     (123)     7486 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/overlaps.py
--rw-r--r--   0 runner    (1001) docker     (123)     6005 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/query.py
--rw-r--r--   0 runner    (1001) docker     (123)     4167 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/skypix.py
--rw-r--r--   0 runner    (1001) docker     (123)    19278 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/static.py
--rw-r--r--   0 runner    (1001) docker     (123)    26120 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/table.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.616211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/
--rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5773 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_attributes.py
--rw-r--r--   0 runner    (1001) docker     (123)    13676 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_bridge.py
--rw-r--r--   0 runner    (1001) docker     (123)    24259 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_collections.py
--rw-r--r--   0 runner    (1001) docker     (123)    75617 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_database.py
--rw-r--r--   0 runner    (1001) docker     (123)    26936 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_datasets.py
--rw-r--r--   0 runner    (1001) docker     (123)    31139 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_dimensions.py
--rw-r--r--   0 runner    (1001) docker     (123)     6900 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_obscore.py
--rw-r--r--   0 runner    (1001) docker     (123)     7354 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_opaque.py
--rw-r--r--   0 runner    (1001) docker     (123)     6989 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_versioning.py
--rw-r--r--   0 runner    (1001) docker     (123)    15783 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/managers.py
--rw-r--r--   0 runner    (1001) docker     (123)     2794 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/nameShrinker.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.616211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/
--rw-r--r--   0 runner    (1001) docker     (123)     1035 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7351 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/_config.py
--rw-r--r--   0 runner    (1001) docker     (123)    11818 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)    10219 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/_records.py
--rw-r--r--   0 runner    (1001) docker     (123)     8593 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     6046 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/_spatial.py
--rw-r--r--   0 runner    (1001) docker     (123)     3676 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/default_spatial.py
--rw-r--r--   0 runner    (1001) docker     (123)     6930 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/pgsphere.py
--rw-r--r--   0 runner    (1001) docker     (123)     7636 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/opaque.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.620211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/
--rw-r--r--   0 runner    (1001) docker     (123)     1263 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12700 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_builder.py
--rw-r--r--   0 runner    (1001) docker     (123)    42156 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_query.py
--rw-r--r--   0 runner    (1001) docker     (123)    32065 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_query_backend.py
--rw-r--r--   0 runner    (1001) docker     (123)    17775 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_query_context.py
--rw-r--r--   0 runner    (1001) docker     (123)    11510 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_readers.py
--rw-r--r--   0 runner    (1001) docker     (123)    33926 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_results.py
--rw-r--r--   0 runner    (1001) docker     (123)    14714 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_sql_query_backend.py
--rw-r--r--   0 runner    (1001) docker     (123)    23820 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_sql_query_context.py
--rw-r--r--   0 runner    (1001) docker     (123)    20973 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_structs.py
--rw-r--r--   0 runner    (1001) docker     (123)     8698 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/butler_sql_engine.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.620211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/
--rw-r--r--   0 runner    (1001) docker     (123)      999 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    20784 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/_predicate.py
--rw-r--r--   0 runner    (1001) docker     (123)    11613 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/categorize.py
--rw-r--r--   0 runner    (1001) docker     (123)    22717 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/check.py
--rw-r--r--   0 runner    (1001) docker     (123)    40510 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/normalForm.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.620211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/
--rw-r--r--   0 runner    (1001) docker     (123)     1019 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12615 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/exprTree.py
--rw-r--r--   0 runner    (1001) docker     (123)     6033 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/parserLex.py
--rw-r--r--   0 runner    (1001) docker     (123)    13319 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/parserYacc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.624210 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/ply/
--rw-r--r--   0 runner    (1001) docker     (123)      104 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/ply/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    43383 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/ply/lex.py
--rw-r--r--   0 runner    (1001) docker     (123)   137091 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/ply/yacc.py
--rw-r--r--   0 runner    (1001) docker     (123)     8136 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/treeVisitor.py
--rw-r--r--   0 runner    (1001) docker     (123)     2424 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/find_first_dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.624210 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      967 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    57516 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/tests/_database.py
--rw-r--r--   0 runner    (1001) docker     (123)   154817 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/tests/_registry.py
--rw-r--r--   0 runner    (1001) docker     (123)    12410 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/versions.py
--rw-r--r--   0 runner    (1001) docker     (123)    22941 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/wildcards.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.628210 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/
--rw-r--r--   0 runner    (1001) docker     (123)     1982 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1720 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/_associate.py
--rw-r--r--   0 runner    (1001) docker     (123)     9615 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/_pruneDatasets.py
--rw-r--r--   0 runner    (1001) docker     (123)     2508 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/butlerImport.py
--rw-r--r--   0 runner    (1001) docker     (123)     3345 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/certifyCalibrations.py
--rw-r--r--   0 runner    (1001) docker     (123)     4946 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/collectionChain.py
--rw-r--r--   0 runner    (1001) docker     (123)     2223 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/configDump.py
--rw-r--r--   0 runner    (1001) docker     (123)     1984 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/configValidate.py
--rw-r--r--   0 runner    (1001) docker     (123)     2347 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/createRepo.py
--rw-r--r--   0 runner    (1001) docker     (123)     6468 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/exportCalibs.py
--rw-r--r--   0 runner    (1001) docker     (123)     7616 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/ingest_files.py
--rw-r--r--   0 runner    (1001) docker     (123)     6080 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/pruneCollection.py
--rw-r--r--   0 runner    (1001) docker     (123)     7371 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/queryCollections.py
--rw-r--r--   0 runner    (1001) docker     (123)     5308 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/queryDataIds.py
--rw-r--r--   0 runner    (1001) docker     (123)     2837 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/queryDatasetTypes.py
--rw-r--r--   0 runner    (1001) docker     (123)     8391 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/queryDatasets.py
--rw-r--r--   0 runner    (1001) docker     (123)     2465 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/queryDimensionRecords.py
--rw-r--r--   0 runner    (1001) docker     (123)     2872 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/register_dataset_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     4574 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/removeCollections.py
--rw-r--r--   0 runner    (1001) docker     (123)     1478 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/removeDatasetType.py
--rw-r--r--   0 runner    (1001) docker     (123)     4886 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/removeRuns.py
--rw-r--r--   0 runner    (1001) docker     (123)     3225 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/retrieveArtifacts.py
--rw-r--r--   0 runner    (1001) docker     (123)     3354 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/transferDatasets.py
--rw-r--r--   0 runner    (1001) docker     (123)    14489 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.632211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     1124 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6614 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/_datasetsHelper.py
--rw-r--r--   0 runner    (1001) docker     (123)     7086 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/_dummyRegistry.py
--rw-r--r--   0 runner    (1001) docker     (123)    11799 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/_examplePythonTypes.py
--rw-r--r--   0 runner    (1001) docker     (123)    23169 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/_testRepo.py
--rw-r--r--   0 runner    (1001) docker     (123)     6585 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/cliCmdTestBase.py
--rw-r--r--   0 runner    (1001) docker     (123)    16191 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/cliLogTestBase.py
--rw-r--r--   0 runner    (1001) docker     (123)     1530 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/deferredFormatter.py
--rw-r--r--   0 runner    (1001) docker     (123)     2331 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/dict_convertible_model.py
--rw-r--r--   0 runner    (1001) docker     (123)     8624 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/testFormatters.py
--rw-r--r--   0 runner    (1001) docker     (123)    10372 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.632211 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/transfers/
--rw-r--r--   0 runner    (1001) docker     (123)      989 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/transfers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16321 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/transfers/_context.py
--rw-r--r--   0 runner    (1001) docker     (123)     6994 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/transfers/_interfaces.py
--rw-r--r--   0 runner    (1001) docker     (123)    20819 2023-01-26 10:04:59.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/transfers/_yaml.py
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-01-26 10:05:15.000000 lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 10:05:15.632211 lsst-daf-butler-26.0.0a20230400/python/lsst_daf_butler.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1701 2023-01-26 10:05:15.000000 lsst-daf-butler-26.0.0a20230400/python/lsst_daf_butler.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    12307 2023-01-26 10:05:15.000000 lsst-daf-butler-26.0.0a20230400/python/lsst_daf_butler.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 10:05:15.000000 lsst-daf-butler-26.0.0a20230400/python/lsst_daf_butler.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       59 2023-01-26 10:05:15.000000 lsst-daf-butler-26.0.0a20230400/python/lsst_daf_butler.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-01-26 10:05:15.000000 lsst-daf-butler-26.0.0a20230400/python/lsst_daf_butler.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-26 10:05:15.000000 lsst-daf-butler-26.0.0a20230400/python/lsst_daf_butler.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 10:05:14.000000 lsst-daf-butler-26.0.0a20230400/python/lsst_daf_butler.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      185 2023-01-26 10:05:15.632211 lsst-daf-butler-26.0.0a20230400/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.237630 lsst-daf-butler-26.0.0a20230500/
+-rw-r--r--   0 runner    (1001) docker     (123)      306 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/COPYRIGHT
+-rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       34 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1701 2023-02-02 14:13:57.237630 lsst-daf-butler-26.0.0a20230500/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      841 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.201629 lsst-daf-butler-26.0.0a20230500/doc/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.209630 lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/
+-rw-r--r--   0 runner    (1001) docker     (123)    24362 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/CHANGES.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/concreteStorageClasses.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     5620 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/configuring.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     6436 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/datastores.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     9272 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/dimensions.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    22653 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/formatters.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4602 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    10216 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/organizing.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    23048 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/queries.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3754 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/use-in-tests.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    16368 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/writing-subcommands.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4112 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.205629 lsst-daf-butler-26.0.0a20230500/python/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.209630 lsst-daf-butler-26.0.0a20230500/python/lsst/
+-rw-r--r--   0 runner    (1001) docker     (123)       67 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.209630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/
+-rw-r--r--   0 runner    (1001) docker     (123)       67 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.209630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/
+-rw-r--r--   0 runner    (1001) docker     (123)      627 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   115080 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/_butler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6009 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/_butlerConfig.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5474 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/_butlerRepoIndex.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4407 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/_deferredDatasetHandle.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9972 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/_limited_butler.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29167 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/_quantum_backed.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.209630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    13596 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/butler.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16071 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/cliLog.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.209630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/cmd/
+-rw-r--r--   0 runner    (1001) docker     (123)     1988 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/cmd/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3519 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/cmd/_remove_collections.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4921 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/cmd/_remove_runs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31553 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/cmd/commands.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.209630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/opt/
+-rw-r--r--   0 runner    (1001) docker     (123)      994 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/opt/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2015 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/opt/arguments.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3197 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/opt/optionGroups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9807 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/opt/options.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2805 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/progress.py
+-rw-r--r--   0 runner    (1001) docker     (123)    41192 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.213630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/
+-rw-r--r--   0 runner    (1001) docker     (123)      130 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/datastore.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.213630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/datastores/
+-rw-r--r--   0 runner    (1001) docker     (123)      660 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/datastores/composites.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1994 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/datastores/fileDatastore.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     5125 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/datastores/formatters.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1417 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/datastores/writeRecipes.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)    15416 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/dimensions.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      814 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/registry.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/repo_transfer_formats.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)    13420 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/storageClasses.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.217630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/
+-rw-r--r--   0 runner    (1001) docker     (123)     1126 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2226 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/_butlerUri.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3272 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/_column_categorization.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5625 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/_column_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5956 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/_column_type_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5438 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/_topology.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5580 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/composites.py
+-rw-r--r--   0 runner    (1001) docker     (123)    49201 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14011 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/configSupport.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5530 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/constraints.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.217630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)     1027 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/datasets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1947 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/datasets/association.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22968 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/datasets/ref.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28105 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/datasets/type.py
+-rw-r--r--   0 runner    (1001) docker     (123)    45634 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/datastore.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39561 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/datastoreCacheManager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8544 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/datastoreRecordData.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21911 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/ddl.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.217630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/
+-rw-r--r--   0 runner    (1001) docker     (123)     1616 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11519 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40909 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_coordinate.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29704 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_dataCoordinateIterable.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20098 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_database.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13606 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_elements.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8724 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_governor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19054 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_graph.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10112 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_packer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16953 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_records.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12453 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9069 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_skypix.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20006 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_universe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7596 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/construction.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1356 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2748 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/fileDataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3115 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/fileDescriptor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28108 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/fileTemplates.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29865 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/formatter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4069 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/json.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8582 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/location.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17742 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/logging.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10081 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/mappingFactory.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18559 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/named.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15439 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/progress.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26100 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/quantum.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3317 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/repoRelocation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8901 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/serverModels.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35288 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/storageClass.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14025 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/storageClassDelegate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8254 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/storedFileInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9734 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/time_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    44136 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/timespan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3731 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.217630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/datastores/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/datastores/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40821 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/datastores/chainedDatastore.py
+-rw-r--r--   0 runner    (1001) docker     (123)   120802 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/datastores/fileDatastore.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8629 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/datastores/genericDatastore.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25045 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/datastores/inMemoryDatastore.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.221629 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/delegates/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/delegates/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2576 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/delegates/arrowastropy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2552 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/delegates/arrownumpy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4354 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/delegates/arrowtable.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5105 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/delegates/dataframe.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.221629 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2995 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/astropyTable.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13007 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/file.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3997 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/json.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3887 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/logs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1716 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/matplotlib.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4649 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/packages.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34905 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/parquet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3703 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/pickle.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5514 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/yaml.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2787 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/instrument.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.221629 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registries/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registries/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24714 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registries/remote.py
+-rw-r--r--   0 runner    (1001) docker     (123)    57917 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registries/sql.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.221629 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/
+-rw-r--r--   0 runner    (1001) docker     (123)     1500 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4147 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/_collectionType.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9148 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/_collection_summary.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4043 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11397 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/_dbAuth.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6379 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/_defaults.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4947 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/_exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    66793 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/_registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5127 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/attributes.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.225629 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/bridge/
+-rw-r--r--   0 runner    (1001) docker     (123)      916 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/bridge/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5055 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/bridge/ephemeral.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15612 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/bridge/monolithic.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.225629 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/collections/
+-rw-r--r--   0 runner    (1001) docker     (123)      916 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/collections/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20296 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/collections/_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5409 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/collections/nameKey.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7139 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/collections/synthIntKey.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5431 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/connectionString.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.225629 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/databases/
+-rw-r--r--   0 runner    (1001) docker     (123)      916 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/databases/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19725 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/databases/postgresql.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15798 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/databases/sqlite.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.225629 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)      916 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/datasets/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.225629 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/datasets/byDimensions/
+-rw-r--r--   0 runner    (1001) docker     (123)      965 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/datasets/byDimensions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22078 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/datasets/byDimensions/_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)    41137 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/datasets/byDimensions/_storage.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14021 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/datasets/byDimensions/summaries.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17969 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/datasets/byDimensions/tables.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.225629 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/
+-rw-r--r--   0 runner    (1001) docker     (123)      916 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7078 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/caching.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7370 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/governor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7486 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/overlaps.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6005 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4167 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/skypix.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19278 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/static.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26120 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/table.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.229630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/
+-rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5773 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_attributes.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13676 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_bridge.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24259 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_collections.py
+-rw-r--r--   0 runner    (1001) docker     (123)    75596 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_database.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26936 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_datasets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31139 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_dimensions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6900 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_obscore.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7354 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_opaque.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6989 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_versioning.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15783 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/managers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2794 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/nameShrinker.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.229630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/
+-rw-r--r--   0 runner    (1001) docker     (123)     1035 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7351 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11815 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10219 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/_records.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8592 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6046 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/_spatial.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3676 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/default_spatial.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6930 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/pgsphere.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7636 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/opaque.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.229630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/
+-rw-r--r--   0 runner    (1001) docker     (123)     1263 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12700 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)    42156 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32065 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_query_backend.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17775 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_query_context.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11510 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_readers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33926 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_results.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14714 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_sql_query_backend.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23820 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_sql_query_context.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20972 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_structs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8698 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/butler_sql_engine.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.229630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/
+-rw-r--r--   0 runner    (1001) docker     (123)      999 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20780 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/_predicate.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11613 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/categorize.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22717 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/check.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40510 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/normalForm.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.233630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/
+-rw-r--r--   0 runner    (1001) docker     (123)     1019 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12615 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/exprTree.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6033 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/parserLex.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13318 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/parserYacc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.233630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/ply/
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/ply/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    43384 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/ply/lex.py
+-rw-r--r--   0 runner    (1001) docker     (123)   137077 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/ply/yacc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8136 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/treeVisitor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2424 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/find_first_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.233630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      967 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    57493 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/tests/_database.py
+-rw-r--r--   0 runner    (1001) docker     (123)   154809 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/tests/_registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12409 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/versions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22941 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/wildcards.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.233630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/
+-rw-r--r--   0 runner    (1001) docker     (123)     1982 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1720 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/_associate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9615 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/_pruneDatasets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2508 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/butlerImport.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3345 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/certifyCalibrations.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4946 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/collectionChain.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2223 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/configDump.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1984 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/configValidate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2347 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/createRepo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6468 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/exportCalibs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7615 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/ingest_files.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6080 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/pruneCollection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7371 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/queryCollections.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5308 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/queryDataIds.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2837 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/queryDatasetTypes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8391 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/queryDatasets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2465 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/queryDimensionRecords.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2872 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/register_dataset_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4574 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/removeCollections.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1478 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/removeDatasetType.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4886 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/removeRuns.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3225 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/retrieveArtifacts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3354 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/transferDatasets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14487 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.237630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1124 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6614 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/_datasetsHelper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7086 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/_dummyRegistry.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11799 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/_examplePythonTypes.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23169 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/_testRepo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6585 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/cliCmdTestBase.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16190 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/cliLogTestBase.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1530 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/deferredFormatter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2331 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/dict_convertible_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8624 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/testFormatters.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10372 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.237630 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/transfers/
+-rw-r--r--   0 runner    (1001) docker     (123)      989 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/transfers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16321 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/transfers/_context.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6994 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/transfers/_interfaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20819 2023-02-02 14:13:42.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/transfers/_yaml.py
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-02-02 14:13:57.000000 lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:13:57.237630 lsst-daf-butler-26.0.0a20230500/python/lsst_daf_butler.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1701 2023-02-02 14:13:57.000000 lsst-daf-butler-26.0.0a20230500/python/lsst_daf_butler.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    12307 2023-02-02 14:13:57.000000 lsst-daf-butler-26.0.0a20230500/python/lsst_daf_butler.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:13:57.000000 lsst-daf-butler-26.0.0a20230500/python/lsst_daf_butler.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-02-02 14:13:57.000000 lsst-daf-butler-26.0.0a20230500/python/lsst_daf_butler.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-02-02 14:13:57.000000 lsst-daf-butler-26.0.0a20230500/python/lsst_daf_butler.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-02-02 14:13:57.000000 lsst-daf-butler-26.0.0a20230500/python/lsst_daf_butler.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:13:56.000000 lsst-daf-butler-26.0.0a20230500/python/lsst_daf_butler.egg-info/zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      185 2023-02-02 14:13:57.237630 lsst-daf-butler-26.0.0a20230500/setup.cfg
```

### Comparing `lsst-daf-butler-26.0.0a20230400/LICENSE` & `lsst-daf-butler-26.0.0a20230500/LICENSE`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/PKG-INFO` & `lsst-daf-butler-26.0.0a20230500/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-daf-butler
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: An abstraction layer for reading and writing astronomical data to datastores.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/daf_butler
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-daf-butler-26.0.0a20230400/README.md` & `lsst-daf-butler-26.0.0a20230500/README.md`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/CHANGES.rst` & `lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/CHANGES.rst`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/concreteStorageClasses.rst` & `lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/concreteStorageClasses.rst`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/configuring.rst` & `lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/configuring.rst`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/datastores.rst` & `lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/datastores.rst`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/dimensions.rst` & `lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/dimensions.rst`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/formatters.rst` & `lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/formatters.rst`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/index.rst` & `lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/index.rst`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/organizing.rst` & `lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/organizing.rst`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -98,8 +98,8 @@
 
 A `CollectionType.CHAINED` collection is essentially a multi-collection search path that has been saved in the `Registry` database and associated with a name of its own.
 Querying a ``CHAINED`` collection simply queries its child collections in order, and a ``CHAINED`` collection is always (and only) updated when its child collections are.
 
 ``CHAINED`` collections may contain other chained collections, as long as they do not contain cycles, and they can also include restrictions on the dataset types to search for within each child collection (see :ref:`daf_butler_collection_expressions`).
 
 The usual constraint on dataset type and data ID uniqueness within a collection is only lazily enforced for chained collections: operations that query them either deduplicate results themselves or terminate single-dataset searches after the first match in a child collection is found.
-In some methods, like `Registry.queryDatasets`, this behavior is optional: passing ``findFirst=True`` will enforce the constraint, while ``findFirst=False`` will not.
+In some methods, like `Registry.queryDatasets`, this behavior is optional: passing ``findFirst=True`` will enforce the constraint, while ``findFirst=False`` will not.
```

### Comparing `lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/queries.rst` & `lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/queries.rst`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/use-in-tests.rst` & `lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/use-in-tests.rst`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/doc/lsst.daf.butler/writing-subcommands.rst` & `lsst-daf-butler-26.0.0a20230500/doc/lsst.daf.butler/writing-subcommands.rst`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/pyproject.toml` & `lsst-daf-butler-26.0.0a20230500/pyproject.toml`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/_butler.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/_butler.py`

 * *Files 0% similar despite different names*

```diff
@@ -1950,15 +1950,14 @@
                         # Nothing else to do until we have finished
                         # iterating.
                         continue
 
                 groupedData[ref.datasetType][ref.dataId] = (dataset, resolvedRefs)
 
             if existingRefs:
-
                 if len(dataset.refs) != len(existingRefs):
                     # Keeping track of partially pre-existing datasets is hard
                     # and should generally never happen. For now don't allow
                     # it.
                     raise ConflictingDefinitionError(
                         f"For dataset {dataset.path} some dataIds already exist"
                         " in registry but others do not. This is not supported."
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/_butlerConfig.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/_butlerConfig.py`

 * *Files 1% similar despite different names*

```diff
@@ -64,15 +64,14 @@
     """
 
     def __init__(
         self,
         other: Optional[Union[ResourcePathExpression, Config]] = None,
         searchPaths: Sequence[ResourcePathExpression] | None = None,
     ):
-
         self.configDir: Optional[ResourcePath] = None
 
         # If this is already a ButlerConfig we assume that defaults
         # have already been loaded.
         if other is not None and isinstance(other, ButlerConfig):
             super().__init__(other)
             # Ensure that the configuration directory propagates
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/_butlerRepoIndex.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/_butlerRepoIndex.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/_deferredDatasetHandle.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/_deferredDatasetHandle.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/_limited_butler.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/_limited_butler.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/_quantum_backed.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/_quantum_backed.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/butler.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/butler.py`

 * *Files 0% similar despite different names*

```diff
@@ -314,15 +314,14 @@
             if len(packages) > 1:
                 msg += f"Command '{command}' exists in packages {', '.join(packages)}. "
         if msg:
             raise click.ClickException(message=msg + "Duplicate commands are not supported, aborting.")
 
 
 class ButlerCLI(LoaderCLI):
-
     localCmdPkg = "lsst.daf.butler.cli.cmd"
 
     pluginEnvVar = "DAF_BUTLER_PLUGINS"
 
     @classmethod
     def _funcNameToCmdName(cls, functionName: str) -> str:
         # Docstring inherited from base class.
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/cliLog.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/cliLog.py`

 * *Files 0% similar despite different names*

```diff
@@ -168,15 +168,14 @@
             # MDC is set via ButlerMDC, rather than in lsst.log.
             lsstLog.usePythonLogging()
 
         formatter: logging.Formatter
         if not log_tty:
             logging.basicConfig(force=True, handlers=[logging.NullHandler()])
         elif longlog:
-
             # Want to create our own Formatter so that we can get high
             # precision timestamps. This requires we attach our own
             # default stream handler.
             defaultHandler = logging.StreamHandler()
             formatter = PrecisionLogFormatter(fmt=cls.pylog_longLogFmt, style="{")
             defaultHandler.setFormatter(formatter)
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/cmd/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/cmd/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/cmd/_remove_collections.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/cmd/_remove_collections.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/cmd/_remove_runs.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/cmd/_remove_runs.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/cmd/commands.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/cmd/commands.py`

 * *Files 1% similar despite different names*

```diff
@@ -168,16 +168,15 @@
     help="Additional search paths to use for configuration overrides",
 )
 @click.option(
     "--file",
     "outfile",
     type=click.File(mode="w"),
     default="-",
-    help="Print the (possibly-expanded) configuration for a repository to a file, or to stdout "
-    "by default.",
+    help="Print the (possibly-expanded) configuration for a repository to a file, or to stdout by default.",
 )
 @options_file_option()
 def config_dump(*args: Any, **kwargs: Any) -> None:
     """Dump either a subset or full Butler configuration to standard output."""
     script.configDump(*args, **kwargs)
 
 
@@ -219,15 +218,15 @@
                           Requires --unstore as an added precaution against accidental deletion. Must not be
                           passed if the collection is not a RUN."""
     ),
     is_flag=True,
 )
 @click.option(
     "--unstore",
-    help=("""Remove all datasets in the collection from all datastores in which they appear."""),
+    help="Remove all datasets in the collection from all datastores in which they appear.",
     is_flag=True,
 )
 @click.option(
     "--unlink",
     help="Before removing the given `collection` unlink it from from this parent collection.",
     multiple=True,
     callback=split_commas,
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/opt/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/opt/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/opt/arguments.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/opt/arguments.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/opt/optionGroups.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/opt/optionGroups.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/opt/options.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/opt/options.py`

 * *Files 0% similar despite different names*

```diff
@@ -56,15 +56,14 @@
 from lsst.daf.butler.registry import CollectionType
 
 from ..cliLog import CliLog
 from ..utils import MWOptionDecorator, MWPath, split_commas, split_kv, unwrap, yaml_presets
 
 
 class CollectionTypeCallback:
-
     collectionTypes = tuple(collectionType.name for collectionType in CollectionType.all())
 
     @staticmethod
     def makeCollectionTypes(
         context: click.Context, param: click.Option, value: tuple[str, ...] | str
     ) -> tuple[CollectionType, ...]:
         if not value:
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/progress.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/progress.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/cli/utils.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/cli/utils.py`

 * *Files 0% similar despite different names*

```diff
@@ -933,15 +933,14 @@
     args : `list` [`str`]
         A list of options, option values, and arguments simialr to those that
         were passed in on the command line. See comments about captured options
         & arguments above.
     """
 
     def __init__(self) -> None:
-
         self.args = None
 
     @staticmethod
     def getFrom(ctx: click.Context) -> Any:
         """If needed, initialize `ctx.obj` with a new `MWCtxObj`, and return
         the new or already existing `MWCtxObj`."""
         if ctx.obj is not None:
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/datastores/composites.yaml` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/datastores/composites.yaml`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/datastores/fileDatastore.yaml` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/datastores/fileDatastore.yaml`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/datastores/formatters.yaml` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/datastores/formatters.yaml`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/datastores/writeRecipes.yaml` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/datastores/writeRecipes.yaml`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/dimensions.yaml` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/dimensions.yaml`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/registry.yaml` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/registry.yaml`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/configs/storageClasses.yaml` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/configs/storageClasses.yaml`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/_butlerUri.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/_butlerUri.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/_column_categorization.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/_column_categorization.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/_column_tags.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/_column_tags.py`

 * *Files 0% similar despite different names*

```diff
@@ -35,15 +35,14 @@
 _S = TypeVar("_S")
 
 if TYPE_CHECKING:
     from lsst.daf.relation import ColumnTag
 
 
 class _BaseColumnTag:
-
     __slots__ = ()
 
     @classmethod
     def filter_from(cls: type[_S], tags: Iterable[Any]) -> set[_S]:
         return {tag for tag in tags if type(tag) is cls}
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/_column_type_info.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/_column_type_info.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/_topology.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/_topology.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/composites.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/composites.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/config.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/config.py`

 * *Files 0% similar despite different names*

```diff
@@ -425,15 +425,14 @@
                 raise RuntimeError(f"Unexpected type for config file: {self.configFile}")
             searchPaths.append(configDir)
 
         # Ensure we know what delimiter to use
         names = self.nameTuples()
         for path in names:
             if path[-1] == self.includeKey:
-
                 log.debug("Processing file include directive at %s", self._D + self._D.join(path))
                 basePath = path[:-1]
 
                 # Extract the includes and then delete them from the config
                 includes = self[path]
                 del self[path]
 
@@ -1119,15 +1118,14 @@
     """
 
     defaultConfigFile: ClassVar[Optional[str]] = None
     """Name of the file containing defaults for this config class.
     """
 
     def __init__(self, other=None, validate=True, mergeDefaults=True, searchPaths=None):
-
         # Create a blank object to receive the defaults
         # Once we have the defaults we then update with the external values
         super().__init__()
 
         # Create a standard Config rather than subset
         externalConfig = Config(other)
 
@@ -1147,15 +1145,14 @@
         self.filesRead = []
 
         # Assume we are not looking up child configurations
         containerKey = None
 
         # Sometimes we do not want to merge with defaults.
         if mergeDefaults:
-
             # Supplied search paths have highest priority
             fullSearchPath = []
             if searchPaths:
                 fullSearchPath.extend(searchPaths)
 
             # Read default paths from environment
             fullSearchPath.extend(self.defaultSearchPaths())
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/configSupport.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/configSupport.py`

 * *Files 0% similar despite different names*

```diff
@@ -79,15 +79,14 @@
         if name is not None and dimensions is not None:
             raise ValueError("Can only accept one of name or dimensions")
 
         self._dimensions = None
         self._name = None
 
         if name is not None:
-
             if not isinstance(name, str):
                 raise ValueError(f"Supplied name must be str not: '{name}'")
 
             if "+" in name:
                 if universe is None:
                     raise ValueError(f"Cannot construct LookupKey for {name} without dimension universe.")
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/constraints.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/constraints.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/datasets/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/datasets/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/datasets/association.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/datasets/association.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/datasets/ref.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/datasets/ref.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/datasets/type.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/datasets/type.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/datastore.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/datastore.py`

 * *Files 0% similar despite different names*

```diff
@@ -206,15 +206,14 @@
     """
 
     def __init__(
         self,
         primaryURI: Optional[ResourcePath] = None,
         componentURIs: Optional[Dict[str, ResourcePath]] = None,
     ):
-
         self.primaryURI = primaryURI
         """The URI to the primary artifact associated with this dataset. If the
         dataset was disassembled within the datastore this may be `None`.
         """
 
         self.componentURIs = componentURIs or {}
         """The URIs to any components associated with the dataset artifact
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/datastoreCacheManager.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/datastoreCacheManager.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/datastoreRecordData.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/datastoreRecordData.py`

 * *Files 0% similar despite different names*

```diff
@@ -35,15 +35,14 @@
 from pydantic import BaseModel
 
 from .datasets import DatasetId
 from .dimensions import DimensionUniverse
 from .storedFileInfo import StoredDatastoreItemInfo
 
 if TYPE_CHECKING:
-
     from ..registry import Registry
 
 _Record = Dict[str, Any]
 
 
 class SerializedDatastoreRecordData(BaseModel):
     """Representation of a `DatastoreRecordData` suitable for serialization."""
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/ddl.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/ddl.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_config.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_config.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_coordinate.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_coordinate.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_dataCoordinateIterable.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_dataCoordinateIterable.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_database.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_database.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_elements.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_elements.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_governor.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_governor.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_graph.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_graph.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_packer.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_packer.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_records.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_records.py`

 * *Files 0% similar despite different names*

```diff
@@ -233,15 +233,15 @@
                         f"No value provided for {self.definition.name}.{self.definition.primaryKey.name}."
                     )
                 kwargs[self.definition.primaryKey.name] = v
             else:
                 v2 = kwargs.setdefault(self.definition.name, v)
                 if v != v2:
                     raise ValueError(
-                        f"Multiple inconsistent values for "
+                        "Multiple inconsistent values for "
                         f"{self.definition.name}.{self.definition.primaryKey.name}: {v!r} != {v2!r}."
                     )
         for name in self.__slots__:
             object.__setattr__(self, name, kwargs.get(name))
         if self.definition.temporal is not None:
             if self.timespan is None:
                 object.__setattr__(
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_schema.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_schema.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_skypix.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_skypix.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/_universe.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/_universe.py`

 * *Files 1% similar despite different names*

```diff
@@ -501,18 +501,18 @@
             # Old pickled universe.
             namespace = _DEFAULT_NAMESPACE
         try:
             return cls._instances[version, namespace]
         except KeyError as err:
             raise pickle.UnpicklingError(
                 f"DimensionUniverse with version '{version}' and namespace {namespace!r} "
-                f"not found.  Note that DimensionUniverse objects are not "
-                f"truly serialized; when using pickle to transfer them "
-                f"between processes, an equivalent instance with the same "
-                f"version must already exist in the receiving process."
+                "not found.  Note that DimensionUniverse objects are not "
+                "truly serialized; when using pickle to transfer them "
+                "between processes, an equivalent instance with the same "
+                "version must already exist in the receiving process."
             ) from err
 
     def __reduce__(self) -> tuple:
         return (self._unpickle, (self._version, self._namespace))
 
     def __deepcopy__(self, memo: dict) -> DimensionUniverse:
         # DimensionUniverse is recursively immutable; see note in @immutable
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/dimensions/construction.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/dimensions/construction.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/exceptions.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/exceptions.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/fileDataset.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/fileDataset.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/fileDescriptor.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/fileDescriptor.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/fileTemplates.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/fileTemplates.py`

 * *Files 0% similar despite different names*

```diff
@@ -466,15 +466,14 @@
         fields["id"] = ref.id
 
         fmt = string.Formatter()
         parts = fmt.parse(self.template)
         output = ""
 
         for literal, field_name, format_spec, conversion in parts:
-
             if field_name == "component":
                 usedComponent = True
 
             if format_spec is None:
                 output = output + literal
                 continue
 
@@ -687,16 +686,15 @@
             maximal.remove(skypix_alias)
 
         required = self.fields(optionals=False)
 
         # Calculate any field usage that does not match a dimension
         if not required.issubset(maximal):
             raise FileTemplateValidationError(
-                f"Template '{self}' is inconsistent with {entity}:"
-                f" {required} is not a subset of {maximal}."
+                f"Template '{self}' is inconsistent with {entity}: {required} is not a subset of {maximal}."
             )
 
         if not allfields.issuperset(minimal):
             raise FileTemplateValidationError(
                 f"Template '{self}' is inconsistent with {entity}:"
                 f" {allfields} is not a superset of {minimal}."
             )
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/formatter.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/formatter.py`

 * *Files 0% similar despite different names*

```diff
@@ -119,16 +119,15 @@
         self._fileDescriptor = fileDescriptor
         self._dataId = dataId
 
         # Check that the write parameters are allowed
         if writeParameters:
             if self.supportedWriteParameters is None:
                 raise ValueError(
-                    "This formatter does not accept any write parameters. "
-                    f"Got: {', '.join(writeParameters)}"
+                    f"This formatter does not accept any write parameters. Got: {', '.join(writeParameters)}"
                 )
             else:
                 given = set(writeParameters)
                 unknown = given - self.supportedWriteParameters
                 if unknown:
                     s = "s" if len(unknown) != 1 else ""
                     unknownStr = ", ".join(f"'{u}'" for u in unknown)
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/json.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/json.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/location.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/location.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/logging.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/logging.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/mappingFactory.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/mappingFactory.py`

 * *Files 1% similar despite different names*

```diff
@@ -248,16 +248,17 @@
         if key in self._registry and not overwrite:
             # Compare the class strings since dynamic classes can be the
             # same thing but be different.
             if str(self._registry[key]) == str(typeName):
                 return
 
             raise KeyError(
-                "Item with key {} already registered with different value"
-                " ({} != {})".format(key, self._registry[key], typeName)
+                "Item with key {} already registered with different value ({} != {})".format(
+                    key, self._registry[key], typeName
+                )
             )
 
         self._registry[key] = {
             "type": typeName,
             "kwargs": dict(**kwargs),
         }
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/named.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/named.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/progress.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/progress.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/quantum.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/quantum.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/repoRelocation.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/repoRelocation.py`

 * *Files 2% similar despite different names*

```diff
@@ -71,16 +71,15 @@
             return configRoot
     except TypeError:
         return configRoot
 
     # None or empty string indicate a problem
     if not butlerRoot:
         raise ValueError(
-            f"Required to replace {BUTLER_ROOT_TAG} in '{configRoot}' "
-            "but a replacement has not been defined"
+            f"Required to replace {BUTLER_ROOT_TAG} in '{configRoot}' but a replacement has not been defined"
         )
 
     # Use absolute file path if this refers to a local file, else use
     # unchanged since all other URI schemes are absolute
     uri = ResourcePath(butlerRoot)
     if uri.isLocal:
         # This will be a local file with URI quoting removed
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/serverModels.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/serverModels.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/storageClass.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/storageClass.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/storageClassDelegate.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/storageClassDelegate.py`

 * *Files 2% similar despite different names*

```diff
@@ -98,16 +98,16 @@
         # Capitalized name for getXxx must only capitalize first letter and not
         # downcase the rest. getVisitInfo and not getVisitinfo
         first = componentName[0].upper()
         if len(componentName) > 1:
             tail = componentName[1:]
         else:
             tail = ""
-        capitalized = "{}{}{}".format(root, first, tail)
-        return (componentName, "{}_{}".format(root, componentName), capitalized)
+        capitalized = f"{root}{first}{tail}"
+        return (componentName, f"{root}_{componentName}", capitalized)
 
     def assemble(self, components: Dict[str, Any], pytype: Optional[Type] = None) -> Any:
         """Construct an object from components based on storageClass.
 
         This generic implementation assumes that instances of objects
         can be created either by passing all the components to a constructor
         or by calling setter methods with the name.
@@ -140,15 +140,15 @@
             cls = self.storageClass.pytype
 
         # Check that the storage class components are consistent
         understood = set(self.storageClass.components)
         requested = set(components.keys())
         unknown = requested - understood
         if unknown:
-            raise ValueError("Requested component(s) not known to StorageClass: {}".format(unknown))
+            raise ValueError(f"Requested component(s) not known to StorageClass: {unknown}")
 
         # First try to create an instance directly using keyword args
         try:
             obj = cls(**components)
         except TypeError:
             obj = None
 
@@ -168,15 +168,15 @@
                             setter = getattr(obj, attr)
                             setter(component)
                         break
                     else:
                         failed.append(name)
 
             if failed:
-                raise ValueError("Unhandled components during assembly ({})".format(failed))
+                raise ValueError(f"Unhandled components during assembly ({failed})")
 
         return obj
 
     def getValidComponents(self, composite: Any) -> Dict[str, Any]:
         """Extract all non-None components from a composite.
 
         Parameters
@@ -238,15 +238,15 @@
         for attr in self._attrNames(componentName, getter=True):
             if hasattr(composite, attr):
                 component = getattr(composite, attr)
                 if attr != componentName:  # We have a method
                     component = component()
                 break
         else:
-            raise AttributeError("Unable to get component {}".format(componentName))
+            raise AttributeError(f"Unable to get component {componentName}")
         return component
 
     def disassemble(
         self, composite: Any, subset: Optional[Iterable] = None, override: Optional[Any] = None
     ) -> Dict[str, DatasetComponent]:
         """Disassembler a composite.
 
@@ -282,31 +282,30 @@
             lookups.
         TypeError
             The parent object does not match the supplied
             `StorageClassDelegate.storageClass`.
         """
         if not self.storageClass.isComposite():
             raise TypeError(
-                "Can not disassemble something that is not a composite"
-                f" (storage class={self.storageClass})"
+                f"Can not disassemble something that is not a composite (storage class={self.storageClass})"
             )
 
         if not self.storageClass.validateInstance(composite):
             raise TypeError(
-                "Unexpected type mismatch between parent and StorageClass"
-                " ({} != {})".format(type(composite), self.storageClass.pytype)
+                "Unexpected type mismatch between parent and StorageClass "
+                f"({type(composite)} != {self.storageClass.pytype})"
             )
 
         requested = set(self.storageClass.components)
 
         if subset is not None:
             subset = set(subset)
             diff = subset - requested
             if diff:
-                raise ValueError("Requested subset is not a subset of supported components: {}".format(diff))
+                raise ValueError(f"Requested subset is not a subset of supported components: {diff}")
             requested = subset
 
         if override is not None:
             composite = override
 
         components = {}
         for c in list(requested):
@@ -322,15 +321,15 @@
                 # If we found a match store it in the results dict and remove
                 # it from the list of components we are still looking for.
                 if component is not None:
                     components[c] = DatasetComponent(c, self.storageClass.components[c], component)
                 requested.remove(c)
 
         if requested:
-            raise ValueError("Unhandled components during disassembly ({})".format(requested))
+            raise ValueError(f"Unhandled components during disassembly ({requested})")
 
         return components
 
     def handleParameters(self, inMemoryDataset: Any, parameters: Optional[Mapping[str, Any]] = None) -> Any:
         """Modify the in-memory dataset using the supplied parameters.
 
         Can return a possibly new object.
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/storedFileInfo.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/storedFileInfo.py`

 * *Files 1% similar despite different names*

```diff
@@ -104,15 +104,14 @@
         path: str,
         storageClass: StorageClass,
         component: Optional[str],
         checksum: Optional[str],
         file_size: int,
         dataset_id: DatasetId,
     ):
-
         # Use these shenanigans to allow us to use a frozen dataclass
         object.__setattr__(self, "path", path)
         object.__setattr__(self, "storageClass", storageClass)
         object.__setattr__(self, "component", component)
         object.__setattr__(self, "checksum", checksum)
         object.__setattr__(self, "file_size", file_size)
         object.__setattr__(self, "dataset_id", dataset_id)
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/time_utils.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/time_utils.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/timespan.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/timespan.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/core/utils.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/core/utils.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/datastores/chainedDatastore.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/datastores/chainedDatastore.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/datastores/fileDatastore.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/datastores/fileDatastore.py`

 * *Files 0% similar despite different names*

```diff
@@ -623,15 +623,14 @@
             disassembled = False
 
         # Is this a component request?
         refComponent = ref.datasetType.component()
 
         fileGetInfo = []
         for location, storedFileInfo in fileLocations:
-
             # The storage class used to write the file
             writeStorageClass = storedFileInfo.storageClass
 
             # If this has been disassembled we need read to match the write
             if disassembled:
                 readStorageClass = writeStorageClass
             else:
@@ -1290,15 +1289,14 @@
             with self.cacheManager.find_in_cache(cache_ref, uri.getExtension()) as cached_file:
                 if cached_file is not None:
                     msg = f"(via cache read of remote file {uri})"
                     uri = cached_file
                     location_updated = True
 
                 with uri.as_local() as local_uri:
-
                     can_be_cached = False
                     if uri != local_uri:
                         # URI was remote and file was downloaded
                         cache_msg = ""
                         location_updated = True
 
                         if self.cacheManager.should_be_cached(cache_ref):
@@ -1765,25 +1763,23 @@
         URI : DatasetRefUris
             Primary and component URIs. URIs will contain a URI fragment
             "#predicted".
         """
         uris = DatasetRefURIs()
 
         if self.composites.shouldBeDisassembled(ref):
-
             for component, _ in ref.datasetType.storageClass.components.items():
                 comp_ref = ref.makeComponentRef(component)
                 comp_location, _ = self._determine_put_formatter_location(comp_ref)
 
                 # Add the "#predicted" URI fragment to indicate this is a
                 # guess
                 uris.componentURIs[component] = ResourcePath(comp_location.uri.geturl() + "#predicted")
 
         else:
-
             location, _ = self._determine_put_formatter_location(ref)
 
             # Add the "#predicted" URI fragment to indicate this is a guess
             uris.primaryURI = ResourcePath(location.uri.geturl() + "#predicted")
 
         return uris
 
@@ -2088,15 +2084,14 @@
 
             # Process parameters
             return ref.datasetType.storageClass.delegate().handleParameters(
                 inMemoryDataset, parameters=unusedParams
             )
 
         elif isDisassembledReadOnlyComponent:
-
             compositeStorageClass = ref.datasetType.parentStorageClass
             if compositeStorageClass is None:
                 raise RuntimeError(
                     f"Unable to retrieve derived component '{refComponent}' since"
                     "no composite storage class is available."
                 )
 
@@ -2397,29 +2392,27 @@
                 # The instance check is for mypy since up to this point it
                 # does not know the type of info.
                 path_map = self._refs_associated_with_artifacts(
                     [info.path for _, info in trashed if isinstance(info, StoredFileInfo)]
                 )
 
                 for ref, info in trashed:
-
                     # Mypy needs to know this is not the base class
                     assert isinstance(info, StoredFileInfo), f"Unexpectedly got info of class {type(info)}"
 
                     # Check for mypy
                     assert ref.id is not None, f"Internal logic error in emptyTrash with ref {ref}/{info}"
 
                     path_map[info.path].remove(ref.id)
                     if not path_map[info.path]:
                         del path_map[info.path]
 
                 artifacts_to_keep = set(path_map)
 
             for ref, info in trashed:
-
                 # Should not happen for this implementation but need
                 # to keep mypy happy.
                 assert info is not None, f"Internal logic error in emptyTrash with ref {ref}."
 
                 # Mypy needs to know this is not the base class
                 assert isinstance(info, StoredFileInfo), f"Unexpectedly got info of class {type(info)}"
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/datastores/genericDatastore.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/datastores/genericDatastore.py`

 * *Files 1% similar despite different names*

```diff
@@ -176,16 +176,16 @@
             Reference to the associated Dataset.
         """
         storageClass = ref.datasetType.storageClass
 
         # Sanity check
         if not isinstance(inMemoryDataset, storageClass.pytype):
             raise TypeError(
-                "Inconsistency between supplied object ({}) "
-                "and storage class type ({})".format(type(inMemoryDataset), storageClass.pytype)
+                f"Inconsistency between supplied object ({type(inMemoryDataset)}) "
+                f"and storage class type ({storageClass.pytype})"
             )
 
         # Confirm that we can accept this dataset
         if not self.constraints.isAcceptable(ref):
             # Raise rather than use boolean return value.
             raise DatasetTypeNotSupportedError(
                 f"Dataset {ref} has been rejected by this datastore via configuration."
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/datastores/inMemoryDatastore.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/datastores/inMemoryDatastore.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/delegates/arrowastropy.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/delegates/arrowastropy.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/delegates/arrownumpy.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/delegates/arrownumpy.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/delegates/arrowtable.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/delegates/arrowtable.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/delegates/dataframe.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/delegates/dataframe.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/astropyTable.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/astropyTable.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/file.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/file.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/json.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/json.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/logs.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/logs.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/matplotlib.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/matplotlib.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/packages.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/packages.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/parquet.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/parquet.py`

 * *Files 0% similar despite different names*

```diff
@@ -169,15 +169,15 @@
         ``DataFrame``.
 
     Returns
     -------
     dataframe : `pandas.DataFrame`
         Converted pandas dataframe.
     """
-    return arrow_table.to_pandas(use_threads=False)
+    return arrow_table.to_pandas(use_threads=False, integer_object_nulls=True)
 
 
 def arrow_to_astropy(arrow_table: pa.Table) -> atable.Table:
     """Convert a pyarrow table to an `astropy.Table`.
 
     Parameters
     ----------
@@ -249,17 +249,34 @@
 
     schema = arrow_table.schema
     metadata = schema.metadata if schema.metadata is not None else {}
 
     numpy_dict = {}
 
     for name in schema.names:
-        col = arrow_table[name].to_numpy()
-
         t = schema.field(name).type
+
+        if arrow_table[name].null_count == 0:
+            # Regular non-masked column
+            col = arrow_table[name].to_numpy()
+        else:
+            # For a masked column, we need to ask arrow to fill the null
+            # values with an appropriately typed value before conversion.
+            # Then we apply the mask to get a masked array of the correct type.
+
+            if t in (pa.string(), pa.binary()):
+                dummy = ""
+            else:
+                dummy = t.to_pandas_dtype()(0)
+
+            col = np.ma.masked_array(
+                data=arrow_table[name].fill_null(dummy).to_numpy(),
+                mask=arrow_table[name].is_null().to_numpy(),
+            )
+
         if t in (pa.string(), pa.binary()):
             col = col.astype(_arrow_string_to_numpy_dtype(schema, name, col))
         elif isinstance(t, pa.FixedSizeListType):
             if len(col) > 0:
                 col = np.stack(col)
             else:
                 # this is an empty column, and needs to be coerced to type.
@@ -841,16 +858,15 @@
         if not isinstance(columns, collections.abc.Mapping):
             raise ValueError(
                 "Columns parameter for multi-index data frame must be a dictionary or list of tuples. "
                 f"Instead got a {get_full_type_name(columns)}."
             )
         if not set(index_level_names).issuperset(columns.keys()):
             raise ValueError(
-                f"Cannot use dict with keys {set(columns.keys())} "
-                f"to select columns from {index_level_names}."
+                f"Cannot use dict with keys {set(columns.keys())} to select columns from {index_level_names}."
             )
         factors = [
             ensure_iterable(columns.get(level, pd_index.levels[i]))
             for i, level in enumerate(index_level_names)
         ]
         for requested in itertools.product(*factors):
             for i, value in enumerate(requested):
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/pickle.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/pickle.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/formatters/yaml.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/formatters/yaml.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/instrument.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/instrument.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registries/remote.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registries/remote.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registries/sql.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registries/sql.py`

 * *Files 1% similar despite different names*

```diff
@@ -586,20 +586,20 @@
         try:
             refs = list(storage.insert(runRecord, expandedDataIds, idGenerationMode))
             if self._managers.obscore:
                 context = queries.SqlQueryContext(self._db, self._managers.column_types)
                 self._managers.obscore.add_datasets(refs, context)
         except sqlalchemy.exc.IntegrityError as err:
             raise ConflictingDefinitionError(
-                f"A database constraint failure was triggered by inserting "
+                "A database constraint failure was triggered by inserting "
                 f"one or more datasets of type {storage.datasetType} into "
                 f"collection '{run}'. "
-                f"This probably means a dataset with the same data ID "
-                f"and dataset type already exists, but it may also mean a "
-                f"dimension row is missing."
+                "This probably means a dataset with the same data ID "
+                "and dataset type already exists, but it may also mean a "
+                "dimension row is missing."
             ) from err
         return refs
 
     @transactional
     def _importDatasets(
         self,
         datasets: Iterable[DatasetRef],
@@ -659,20 +659,20 @@
         try:
             refs = list(storage.import_(runRecord, expandedDatasets, idGenerationMode, reuseIds))
             if self._managers.obscore:
                 context = queries.SqlQueryContext(self._db, self._managers.column_types)
                 self._managers.obscore.add_datasets(refs, context)
         except sqlalchemy.exc.IntegrityError as err:
             raise ConflictingDefinitionError(
-                f"A database constraint failure was triggered by inserting "
+                "A database constraint failure was triggered by inserting "
                 f"one or more datasets of type {storage.datasetType} into "
                 f"collection '{run}'. "
-                f"This probably means a dataset with the same data ID "
-                f"and dataset type already exists, but it may also mean a "
-                f"dimension row is missing."
+                "This probably means a dataset with the same data ID "
+                "and dataset type already exists, but it may also mean a "
+                "dimension row is missing."
             ) from err
         return refs
 
     def getDataset(self, id: DatasetId) -> Optional[DatasetRef]:
         # Docstring inherited from lsst.daf.butler.registry.Registry
         return self._managers.datasets.getDatasetRef(id)
 
@@ -711,16 +711,16 @@
                     # manager then we may need to save the dataset.
                     context = queries.SqlQueryContext(self._db, self._managers.column_types)
                     self._managers.obscore.associate(refsForType, collectionRecord, context)
             except sqlalchemy.exc.IntegrityError as err:
                 raise ConflictingDefinitionError(
                     f"Constraint violation while associating dataset of type {datasetType.name} with "
                     f"collection {collection}.  This probably means that one or more datasets with the same "
-                    f"dataset type and data ID already exist in the collection, but it may also indicate "
-                    f"that the datasets do not exist."
+                    "dataset type and data ID already exist in the collection, but it may also indicate "
+                    "that the datasets do not exist."
                 ) from err
 
     @transactional
     def disassociate(self, collection: str, refs: Iterable[DatasetRef]) -> None:
         # Docstring inherited from lsst.daf.butler.registry.Registry
         progress = Progress("lsst.daf.butler.Registry.disassociate", level=logging.DEBUG)
         collectionRecord = self._managers.collections.find(collection)
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/_collectionType.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/_collectionType.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/_collection_summary.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/_collection_summary.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/_config.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/_config.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/_dbAuth.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/_dbAuth.py`

 * *Files 0% similar despite different names*

```diff
@@ -187,15 +187,14 @@
             raise DbAuthError("Missing dialectname parameter")
         if host is None or host == "":
             raise DbAuthError("Missing host parameter")
         if database is None or database == "":
             raise DbAuthError("Missing database parameter")
 
         for authDict in self.authList:
-
             # Check for mandatory entries
             if "url" not in authDict:
                 raise DbAuthError("Missing URL in DbAuth configuration")
 
             # Parse pseudo-URL from db-auth.yaml
             components = urllib.parse.urlparse(authDict["url"])
 
@@ -244,16 +243,15 @@
                 return (username, authDict["password"])
             else:
                 if "username" not in authDict:
                     return (None, authDict["password"])
                 return (authDict["username"], authDict["password"])
 
         raise DbAuthNotFoundError(
-            "No matching DbAuth configuration for: "
-            f"({dialectname}, {username}, {host}, {port}, {database})"
+            f"No matching DbAuth configuration for: ({dialectname}, {username}, {host}, {port}, {database})"
         )
 
     def getUrl(self, url: str) -> str:
         """Fill in a username and password in a database connection URL.
 
         This function parses the URL and calls `getAuth`.
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/_defaults.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/_defaults.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/_exceptions.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/_exceptions.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/_registry.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/_registry.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/attributes.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/attributes.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/bridge/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/bridge/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/bridge/ephemeral.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/bridge/ephemeral.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/bridge/monolithic.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/bridge/monolithic.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/collections/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/collections/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/collections/_base.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/collections/_base.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/collections/nameKey.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/collections/nameKey.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/collections/synthIntKey.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/collections/synthIntKey.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/connectionString.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/connectionString.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/databases/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/databases/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/databases/postgresql.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/databases/postgresql.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/databases/sqlite.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/databases/sqlite.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/datasets/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/datasets/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/datasets/byDimensions/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/datasets/byDimensions/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/datasets/byDimensions/_manager.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/datasets/byDimensions/_manager.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/datasets/byDimensions/_storage.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/datasets/byDimensions/_storage.py`

 * *Files 0% similar despite different names*

```diff
@@ -167,15 +167,15 @@
         timespan: Timespan,
         context: SqlQueryContext,
     ) -> None:
         # Docstring inherited from DatasetRecordStorage.
         if self._calibs is None:
             raise CollectionTypeError(
                 f"Cannot certify datasets of type {self.datasetType.name}, for which "
-                f"DatasetType.isCalibration() is False."
+                "DatasetType.isCalibration() is False."
             )
         if collection.type is not CollectionType.CALIBRATION:
             raise CollectionTypeError(
                 f"Cannot certify into collection '{collection.name}' "
                 f"of type {collection.type.name}; must be CALIBRATION."
             )
         TimespanReprClass = self._db.getTimespanRepresentation()
@@ -247,15 +247,15 @@
         dataIds: Iterable[DataCoordinate] | None = None,
         context: SqlQueryContext,
     ) -> None:
         # Docstring inherited from DatasetRecordStorage.
         if self._calibs is None:
             raise CollectionTypeError(
                 f"Cannot decertify datasets of type {self.datasetType.name}, for which "
-                f"DatasetType.isCalibration() is False."
+                "DatasetType.isCalibration() is False."
             )
         if collection.type is not CollectionType.CALIBRATION:
             raise CollectionTypeError(
                 f"Cannot decertify from collection '{collection.name}' "
                 f"of type {collection.type.name}; must be CALIBRATION."
             )
         TimespanReprClass = self._db.getTimespanRepresentation()
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/datasets/byDimensions/summaries.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/datasets/byDimensions/summaries.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/datasets/byDimensions/tables.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/datasets/byDimensions/tables.py`

 * *Files 0% similar despite different names*

```diff
@@ -211,15 +211,15 @@
                     primaryKey=True,
                     doc="A unique field used as the primary key for dataset.",
                 ),
                 ddl.FieldSpec(
                     name="dataset_type_id",
                     dtype=sqlalchemy.BigInteger,
                     nullable=False,
-                    doc=("Reference to the associated entry in the dataset_type table."),
+                    doc="Reference to the associated entry in the dataset_type table.",
                 ),
                 ddl.FieldSpec(
                     name="ingest_date",
                     dtype=sqlalchemy.TIMESTAMP,
                     default=sqlalchemy.sql.func.now(),
                     nullable=False,
                     doc="Time of dataset ingestion.",
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/caching.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/caching.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/governor.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/governor.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/overlaps.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/overlaps.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/query.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/query.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/skypix.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/skypix.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/static.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/static.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/dimensions/table.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/dimensions/table.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_attributes.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_attributes.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_bridge.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_bridge.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_collections.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_collections.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_database.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_database.py`

 * *Files 0% similar despite different names*

```diff
@@ -1035,16 +1035,15 @@
         ), "Table creation interrupts transactions."
         assert self._metadata is not None, "Static tables must be declared before dynamic tables."
         table = self.getExistingTable(name, spec)
         if table is not None:
             return table
         if not self.isWriteable():
             raise ReadOnlyDatabaseError(
-                f"Table {name} does not exist, and cannot be created "
-                f"because database {self} is read-only."
+                f"Table {name} does not exist, and cannot be created because database {self} is read-only."
             )
         table = self._convertTableSpec(name, spec, self._metadata)
         for foreignKeySpec in spec.foreignKeys:
             table.append_constraint(self._convertForeignKeySpec(name, foreignKeySpec, self._metadata))
         try:
             with self._transaction() as (_, connection):
                 table.create(connection)
@@ -1151,15 +1150,15 @@
         table = self._convertTableSpec(
             name, spec, metadata, prefixes=["TEMPORARY"], schema=sqlalchemy.schema.BLANK_SCHEMA, **kwargs
         )
         if table.key in self._temp_tables:
             if table.key != name:
                 raise ValueError(
                     f"A temporary table with name {name} (transformed to {table.key} by "
-                    f"Database) already exists."
+                    "Database) already exists."
                 )
         for foreignKeySpec in spec.foreignKeys:
             table.append_constraint(self._convertForeignKeySpec(name, foreignKeySpec, metadata))
         table.create(connection)
         return table
 
     @classmethod
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_datasets.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_datasets.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_dimensions.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_dimensions.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_obscore.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_obscore.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_opaque.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_opaque.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/interfaces/_versioning.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/interfaces/_versioning.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/managers.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/managers.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/nameShrinker.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/nameShrinker.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/_config.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/_config.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/_manager.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/_manager.py`

 * *Files 0% similar despite different names*

```diff
@@ -212,15 +212,14 @@
             # Check each dataset run against configured run list. We want to
             # reduce number of calls to _check_dataset_run, which may be
             # expensive. Normally references are grouped by run, if there are
             # multiple input references, they should have the same run.
             # Instead of just checking that, we group them by run again.
             refs_by_run: Dict[str, List[DatasetRef]] = defaultdict(list)
             for ref in refs:
-
                 # Record factory will filter dataset types, but to reduce
                 # collection checks we also pre-filter it here.
                 if ref.datasetType.name not in self.config.dataset_types:
                     continue
 
                 assert ref.run is not None, "Run cannot be None"
                 refs_by_run[ref.run].append(ref)
@@ -229,15 +228,14 @@
             for run, run_refs in refs_by_run.items():
                 if not self._check_dataset_run(run):
                     continue
                 good_refs.extend(run_refs)
             obscore_refs = good_refs
 
         else:
-
             # Take all refs, no collection check.
             obscore_refs = refs
 
         return self._populate(obscore_refs, context)
 
     def associate(
         self, refs: Iterable[DatasetRef], collection: CollectionRecord, context: SqlQueryContext
@@ -258,15 +256,14 @@
 
         # Only works when collection type is TAGGED
         if self.tagged_collection is None:
             return 0
 
         count = 0
         if collection.name == self.tagged_collection:
-
             # Sorting may improve performance
             dataset_ids = sorted(cast(uuid.UUID, ref.id) for ref in refs)
             if dataset_ids:
                 fk_field = self.schema.dataset_fk
                 assert fk_field is not None, "Cannot be None by construction"
                 # There may be too many of them, do it in chunks.
                 for ids in chunk_iterable(dataset_ids):
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/_records.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/_records.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/_schema.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/_schema.py`

 * *Files 1% similar despite different names*

```diff
@@ -134,15 +134,14 @@
 
     def __init__(
         self,
         config: ObsCoreConfig,
         spatial_plugins: Sequence[SpatialObsCorePlugin],
         datasets: Optional[Type[DatasetRecordStorageManager]] = None,
     ):
-
         fields = list(_STATIC_COLUMNS)
 
         column_names = set(col.name for col in fields)
 
         all_configs: List[ObsCoreConfig | DatasetTypeConfig] = [config]
         if config.dataset_types:
             all_configs += list(config.dataset_types.values())
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/_spatial.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/_spatial.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/default_spatial.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/default_spatial.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/obscore/pgsphere.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/obscore/pgsphere.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/opaque.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/opaque.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_builder.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_builder.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_query.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_query.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_query_backend.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_query_backend.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_query_context.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_query_context.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_readers.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_readers.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_results.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_results.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_sql_query_backend.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_sql_query_backend.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_sql_query_context.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_sql_query_context.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/_structs.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/_structs.py`

 * *Files 0% similar despite different names*

```diff
@@ -307,15 +307,14 @@
     order_by : `Iterable` [ `str` ]
         Sequence of names to use for ordering with optional "-" prefix.
     element : `DimensionElement`
         Dimensions used by a query.
     """
 
     def __init__(self, order_by: Iterable[str], element: DimensionElement):
-
         self.order_by_columns = []
         for name in order_by:
             if not name or name == "-":
                 raise ValueError("Empty dimension name in ORDER BY")
             ascending = True
             if name[0] == "-":
                 ascending = False
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/butler_sql_engine.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/butler_sql_engine.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/_predicate.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/_predicate.py`

 * *Files 1% similar despite different names*

```diff
@@ -157,15 +157,15 @@
         summary = expr.visit(visitor)
     except UserExpressionError as err:
         exprOriginal = str(tree)
         exprNormal = str(expr.toTree())
         if exprNormal == exprOriginal:
             msg = f'Error in query expression "{exprOriginal}": {err}'
         else:
-            msg = f'Error in query expression "{exprOriginal}" ' f'(normalized to "{exprNormal}"): {err}'
+            msg = f'Error in query expression "{exprOriginal}" (normalized to "{exprNormal}"): {err}'
         raise UserExpressionError(msg) from None
     for dimension_name, values in summary.dimension_constraints.items():
         if dimension_name in dimensions.universe.getGovernorDimensions().names:
             governor_constraints[dimension_name] = cast(Set[str], values)
     converter = PredicateConversionVisitor(bind, dataset_type_name, dimensions.universe)
     predicate = tree.visit(converter)
     return predicate, governor_constraints
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/categorize.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/categorize.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/check.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/check.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/normalForm.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/normalForm.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/exprTree.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/exprTree.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/parserLex.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/parserLex.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/parserYacc.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/parserYacc.py`

 * *Files 0% similar despite different names*

```diff
@@ -230,15 +230,14 @@
         expression. If identifier does not exist in the mapping then
         `Identifier` is inserted into parse tree.
     **kwargs
         optional keyword arguments that are passed to `yacc.yacc` constructor.
     """
 
     def __init__(self, idMap=None, **kwargs):
-
         kw = dict(write_tables=0, debug=False)
         kw.update(kwargs)
 
         self.parser = yacc.yacc(module=self, **kw)
         self._idMap = idMap or {}
 
     def parse(self, input, lexer=None, debug=False, tracking=False):
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/ply/lex.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/ply/lex.py`

 * *Files 0% similar despite different names*

```diff
@@ -48,14 +48,15 @@
 except AttributeError:
     # Python 3.0
     StringTypes = (str, bytes)
 
 # This regular expression is used to match valid token names
 _is_identifier = re.compile(r"^[a-zA-Z0-9_]+$")
 
+
 # Exception thrown when invalid token encountered and no default error
 # handler is defined.
 class LexError(Exception):
     def __init__(self, message, s):
         self.args = (message,)
         self.text = s
 
@@ -445,14 +446,15 @@
 # -----------------------------------------------------------------------------
 #                           ==== Lex Builder ===
 #
 # The functions and classes below are used to collect lexing information
 # and build a Lexer object from it.
 # -----------------------------------------------------------------------------
 
+
 # -----------------------------------------------------------------------------
 # _get_regex(func)
 #
 # Returns the regular expression assigned to a function either as a doc string
 # or as a .regex attribute attached by the @TOKEN decorator.
 # -----------------------------------------------------------------------------
 def _get_regex(func):
@@ -908,15 +910,14 @@
     lextab="lextab",
     reflags=int(re.VERBOSE),
     nowarn=False,
     outputdir=None,
     debuglog=None,
     errorlog=None,
 ):
-
     if lextab is None:
         lextab = "lextab"
 
     global lexer
 
     ldict = None
     stateinfo = {"INITIAL": "inclusive"}
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/ply/yacc.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/ply/yacc.py`

 * *Files 0% similar despite different names*

```diff
@@ -545,15 +545,14 @@
                             errorcount = error_count
                             self.errorok = False
 
                         continue
                         # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 
                     else:
-
                         # --! TRACKING
                         if tracking:
                             sym.lineno = lexer.lineno
                             sym.lexpos = lexer.lexpos
                         # --! TRACKING
 
                         targ = [sym]
@@ -595,15 +594,14 @@
                     # --! DEBUG
                     debug.info("Done   : Returning %s", format_result(result))
                     debug.info("PLY: PARSE DEBUG END")
                     # --! DEBUG
                     return result
 
             if t is None:
-
                 # --! DEBUG
                 debug.error(
                     "Error  : %s",
                     ("%s . %s" % (" ".join([xx.type for xx in symstack][1:]), str(lookahead))).lstrip(),
                 )
                 # --! DEBUG
 
@@ -862,15 +860,14 @@
                             errorcount = error_count
                             self.errorok = False
 
                         continue
                         # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 
                     else:
-
                         # --! TRACKING
                         if tracking:
                             sym.lineno = lexer.lineno
                             sym.lexpos = lexer.lexpos
                         # --! TRACKING
 
                         targ = [sym]
@@ -905,15 +902,14 @@
 
                 if t == 0:
                     n = symstack[-1]
                     result = getattr(n, "value", None)
                     return result
 
             if t is None:
-
                 # We have some kind of parsing error here.  To handle
                 # this, we are going to push the current token onto
                 # the tokenstack and replace it with an 'error' token.
                 # If there are any synchronization rules, they may
                 # catch it.
                 #
                 # In addition to pushing the error token, we call call
@@ -1155,15 +1151,14 @@
                             errorcount = error_count
                             self.errorok = False
 
                         continue
                         # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 
                     else:
-
                         targ = [sym]
 
                         # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                         # The code enclosed in this section is duplicated
                         # above as a performance optimization.  Make sure
                         # changes get made in both locations.
 
@@ -1192,15 +1187,14 @@
 
                 if t == 0:
                     n = symstack[-1]
                     result = getattr(n, "value", None)
                     return result
 
             if t is None:
-
                 # We have some kind of parsing error here.  To handle
                 # this, we are going to push the current token onto
                 # the tokenstack and replace it with an 'error' token.
                 # If there are any synchronization rules, they may
                 # catch it.
                 #
                 # In addition to pushing the error token, we call call
@@ -1574,15 +1568,14 @@
     # or the precedence of a terminal specified by %prec.
     #
     # A variety of error checks are performed to make sure production symbols
     # are valid and that %prec is used correctly.
     # -----------------------------------------------------------------------------
 
     def add_production(self, prodname, syms, func=None, file="", line=0):
-
         if prodname in self.Terminals:
             raise GrammarError(
                 "%s:%d: Illegal rule name %r. Already defined as a token" % (file, line, prodname)
             )
         if prodname == "error":
             raise GrammarError(
                 "%s:%d: Illegal rule name %r. error is a reserved word" % (file, line, prodname)
@@ -1683,15 +1676,14 @@
     # find_unreachable()
     #
     # Find all of the nonterminal symbols that can't be reached from the starting
     # symbol.  Returns a list of nonterminals that can't be reached.
     # -----------------------------------------------------------------------------
 
     def find_unreachable(self):
-
         # Mark all symbols that are reachable from a symbol s
         def mark_reachable_from(s):
             if s in reachable:
                 return
             reachable.add(s)
             for p in self.Prodnames.get(s, []):
                 for r in p.prod:
@@ -1723,15 +1715,15 @@
         # Initialize to false:
         for n in self.Nonterminals:
             terminates[n] = False
 
         # Then propagate termination until no change:
         while True:
             some_change = False
-            for (n, pl) in self.Prodnames.items():
+            for n, pl in self.Prodnames.items():
                 # Nonterminal n terminates iff any of its productions terminates.
                 for p in pl:
                     # Production p terminates iff all of its rhs symbols terminate.
                     for s in p.prod:
                         if not terminates[s]:
                             # The symbol s does not terminate,
                             # so production p does not terminate.
@@ -1751,15 +1743,15 @@
                         # Don't need to consider any more productions for this n.
                         break
 
             if not some_change:
                 break
 
         infinite = []
-        for (s, term) in terminates.items():
+        for s, term in terminates.items():
             if not term:
                 if s not in self.Prodnames and s not in self.Terminals and s != "error":
                     # s is used-but-not-defined, and we've already warned of that,
                     # so it would be overkill to say that it's also non-terminating.
                     pass
                 else:
                     infinite.append(s)
@@ -1835,15 +1827,14 @@
     #
     # Compute the value of FIRST1(beta) where beta is a tuple of symbols.
     #
     # During execution of compute_first1, the result may be incomplete.
     # Afterward (e.g., when called from compute_follow()), it will be complete.
     # -------------------------------------------------------------------------
     def _first(self, beta):
-
         # We are computing First(x1,x2,x3,...,xn)
         result = []
         for x in beta:
             x_produces_empty = False
 
             # Add all the non-<empty> symbols of First[x] to the result.
             for f in self.First[x]:
@@ -3299,15 +3290,14 @@
     write_tables=True,
     debugfile=debug_file,
     outputdir=None,
     debuglog=None,
     errorlog=None,
     picklefile=None,
 ):
-
     if tabmodule is None:
         tabmodule = tab_module
 
     # Reference to the parsing method of the last built parser
     global parse
 
     # If pickling is enabled, table files are not created
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/expressions/parser/treeVisitor.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/expressions/parser/treeVisitor.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/queries/find_first_dataset.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/queries/find_first_dataset.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/tests/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/tests/_database.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/tests/_database.py`

 * *Files 0% similar despite different names*

```diff
@@ -788,16 +788,15 @@
             task1 = asyncio.create_task(side1())
             task2 = asyncio.create_task(side2())
 
             names1, names2 = await task1
             await task2
             if "a2" in names1:
                 warnings.warn(
-                    "Unlucky scheduling in no-locking test: concurrent INSERT "
-                    "happened before first SELECT."
+                    "Unlucky scheduling in no-locking test: concurrent INSERT happened before first SELECT."
                 )
                 self.assertEqual(names1, {"a2"})
                 self.assertEqual(names2, {"a1", "a2"})
             elif "a2" not in names2:
                 warnings.warn(
                     "Unlucky scheduling in no-locking test: concurrent INSERT "
                     "happened after second SELECT even without locking."
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/tests/_registry.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/tests/_registry.py`

 * *Files 0% similar despite different names*

```diff
@@ -549,15 +549,14 @@
         for ref in refs:
             with self.assertRaises(ConflictingDefinitionError):
                 registry._importDatasets([ref])
 
         # Test for non-unique IDs, they can be re-imported multiple times.
         for run, idGenMode in ((2, DatasetIdGenEnum.DATAID_TYPE), (4, DatasetIdGenEnum.DATAID_TYPE_RUN)):
             with self.subTest(idGenMode=idGenMode):
-
                 # Use integer dataset ID to force UUID calculation in _import
                 ref = DatasetRef(datasetTypeBias, dataIdBias1, id=0, run=f"run{run}")
                 (ref1,) = registry._importDatasets([ref], idGenerationMode=idGenMode)
                 self.assertIsInstance(ref1.id, uuid.UUID)
                 self.assertEqual(ref1.id.version, 5)
 
                 # Importing it again is OK
@@ -2358,15 +2357,14 @@
         self.assertGreater(len(datasets), 0)
 
         # few tests with findFirst
         datasets = list(registry.queryDatasets("bias", collections=chain, findFirst=True))
         self.assertGreater(len(datasets), 0)
 
     def testIngestTimeQuery(self):
-
         registry = self.makeRegistry()
         self.loadData(registry, "base.yaml")
         dt0 = datetime.utcnow()
         self.loadData(registry, "datasets.yaml")
         dt1 = datetime.utcnow()
 
         datasets = list(registry.queryDatasets(..., collections=...))
@@ -2879,21 +2877,21 @@
 
         with self.assertRaisesRegex(ValueError, "Timespan exists in more than one dimesion"):
             list(do_query(("exposure", "visit")).order_by("timespan.begin"))
 
         with self.assertRaisesRegex(
             ValueError, "Cannot find any temporal dimension element for 'timespan.begin'"
         ):
-            list(do_query(("tract")).order_by("timespan.begin"))
+            list(do_query("tract").order_by("timespan.begin"))
 
         with self.assertRaisesRegex(ValueError, "Cannot use 'timespan.begin' with non-temporal element"):
-            list(do_query(("tract")).order_by("tract.timespan.begin"))
+            list(do_query("tract").order_by("tract.timespan.begin"))
 
         with self.assertRaisesRegex(ValueError, "Field 'name' does not exist in 'tract'."):
-            list(do_query(("tract")).order_by("tract.name"))
+            list(do_query("tract").order_by("tract.name"))
 
     def testQueryDataIdsGovernorExceptions(self):
         """Test exceptions raised by queryDataIds() for incorrect governors."""
         registry = self.makeRegistry()
         self.loadData(registry, "base.yaml")
         self.loadData(registry, "datasets.yaml")
         self.loadData(registry, "spatial.yaml")
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/versions.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/versions.py`

 * *Files 0% similar despite different names*

```diff
@@ -221,15 +221,14 @@
 
             - record with the key "version:{fullExtensionName}" and version
               number in its string format as a value,
             - record with the key "schema_digest:{fullExtensionName}" and
               schema digest as a value.
         """
         for extension in self._managers.values():
-
             version = extension.currentVersion()
             if version:
                 key = self._managerVersionKey(extension)
                 value = str(version)
                 self._attributes.set(key, value)
                 _LOG.debug("saved manager version %s=%s", key, value)
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/registry/wildcards.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/registry/wildcards.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/_associate.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/_associate.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/_pruneDatasets.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/_pruneDatasets.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/butlerImport.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/butlerImport.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/certifyCalibrations.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/certifyCalibrations.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/collectionChain.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/collectionChain.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/configDump.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/configDump.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/configValidate.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/configValidate.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/createRepo.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/createRepo.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/exportCalibs.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/exportCalibs.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/ingest_files.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/ingest_files.py`

 * *Files 0% similar despite different names*

```diff
@@ -155,15 +155,14 @@
     # be dimensions so we need to know the name of that column.
     file_column = table.colnames[0]
 
     # Handle multiple dataIds per file by grouping by file.
     refs_by_file = defaultdict(list)
     n_dataset_refs = 0
     for row in table:
-
         # Convert the row to a dataId, remembering to extract the
         # path column.
         dataId = dict(row)
         path = dataId.pop(file_column)
 
         # The command line can override a column.
         dataId.update(common_data_id)
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/pruneCollection.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/pruneCollection.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/queryCollections.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/queryCollections.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/queryDataIds.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/queryDataIds.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/queryDatasetTypes.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/queryDatasetTypes.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/queryDatasets.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/queryDatasets.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/queryDimensionRecords.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/queryDimensionRecords.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/register_dataset_type.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/register_dataset_type.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/removeCollections.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/removeCollections.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/removeDatasetType.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/removeDatasetType.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/removeRuns.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/removeRuns.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/retrieveArtifacts.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/retrieveArtifacts.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/script/transferDatasets.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/script/transferDatasets.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/server.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/server.py`

 * *Files 0% similar despite different names*

```diff
@@ -223,15 +223,14 @@
     glob: list[str] | None = Query(None),
     datasetType: str | None = Query(None),
     flattenChains: bool = Query(False),
     collectionType: list[CollectionTypeNames] | None = Query(None),
     includeChains: bool | None = Query(None),
     butler: Butler = Depends(butler_readonly_dependency),
 ) -> list[str]:
-
     expression_params = ExpressionQueryParameter(regex=regex, glob=glob)
     collectionTypes = CollectionType.from_names(collectionType)
     dataset_type = butler.registry.getDatasetType(datasetType) if datasetType else None
 
     collections = butler.registry.queryCollections(
         expression=expression_params.expression(),
         datasetType=dataset_type,
@@ -403,15 +402,14 @@
     response_model_exclude_unset=True,
     response_model_exclude_defaults=True,
     response_model_exclude_none=True,
 )
 def query_dimension_records(
     element: str, query: QueryDimensionRecordsModel, butler: Butler = Depends(butler_readonly_dependency)
 ) -> list[SerializedDimensionRecord]:
-
     if query.datasets:
         datasets = query.datasets.expression()
     else:
         datasets = None
     if query.collections:
         collections = query.collections.expression()
     else:
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/_datasetsHelper.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/_datasetsHelper.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/_dummyRegistry.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/_dummyRegistry.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/_examplePythonTypes.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/_examplePythonTypes.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/_testRepo.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/_testRepo.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/cliCmdTestBase.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/cliCmdTestBase.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/cliLogTestBase.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/cliLogTestBase.py`

 * *Files 0% similar despite different names*

```diff
@@ -71,15 +71,14 @@
     expected_pyroot_level: str,
     expected_pylsst_level: str,
     expected_pybutler_level: str,
     expected_lsstroot_level: str,
     expected_lsstbutler_level: str,
     expected_lsstx_level: str,
 ) -> None:
-
     LogLevel = namedtuple("LogLevel", ("expected", "actual", "name"))
 
     logLevels = [
         LogLevel(expected_pyroot_level, logging.getLogger().level, "pyRoot"),
         LogLevel(expected_pylsst_level, logging.getLogger("lsst").getEffectiveLevel(), "pyLsst"),
         LogLevel(
             expected_pybutler_level, logging.getLogger("lsst.daf.butler").getEffectiveLevel(), "pyButler"
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/deferredFormatter.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/deferredFormatter.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/dict_convertible_model.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/dict_convertible_model.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/testFormatters.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/testFormatters.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/tests/utils.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/tests/utils.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/transfers/__init__.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/transfers/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/transfers/_context.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/transfers/_context.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/transfers/_interfaces.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/transfers/_interfaces.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst/daf/butler/transfers/_yaml.py` & `lsst-daf-butler-26.0.0a20230500/python/lsst/daf/butler/transfers/_yaml.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst_daf_butler.egg-info/PKG-INFO` & `lsst-daf-butler-26.0.0a20230500/python/lsst_daf_butler.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-daf-butler
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: An abstraction layer for reading and writing astronomical data to datastores.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/daf_butler
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-daf-butler-26.0.0a20230400/python/lsst_daf_butler.egg-info/SOURCES.txt` & `lsst-daf-butler-26.0.0a20230500/python/lsst_daf_butler.egg-info/SOURCES.txt`

 * *Files identical despite different names*

