# Comparing `tmp/emannotationschemas-5.7.1.tar.gz` & `tmp/emannotationschemas-5.8.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/emannotationschemas-5.7.1.tar", last modified: Tue Mar 28 21:19:12 2023, max compression
+gzip compressed data, was "dist/emannotationschemas-5.8.0.tar", last modified: Thu Apr  6 22:59:34 2023, max compression
```

## Comparing `emannotationschemas-5.7.1.tar` & `emannotationschemas-5.8.0.tar`

### file list

```diff
@@ -1,75 +1,76 @@
-drwxr-xr-x   0 forrestc   (503) staff       (20)        0 2023-03-28 21:19:12.694813 emannotationschemas-5.7.1/
--rw-r--r--   0 forrestc   (503) staff       (20)     1072 2020-03-03 22:34:04.000000 emannotationschemas-5.7.1/LICENSE
--rw-r--r--   0 forrestc   (503) staff       (20)      105 2022-06-27 19:54:59.000000 emannotationschemas-5.7.1/MANIFEST.in
--rw-r--r--   0 forrestc   (503) staff       (20)      307 2023-03-28 21:19:12.695058 emannotationschemas-5.7.1/PKG-INFO
--rw-r--r--   0 forrestc   (503) staff       (20)     3420 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/README.md
-drwxr-xr-x   0 forrestc   (503) staff       (20)        0 2023-03-28 21:19:12.640391 emannotationschemas-5.7.1/emannotationschemas/
--rw-r--r--   0 forrestc   (503) staff       (20)     5196 2023-03-28 21:19:02.000000 emannotationschemas-5.7.1/emannotationschemas/__init__.py
--rw-r--r--   0 forrestc   (503) staff       (20)     1321 2023-03-28 21:19:02.000000 emannotationschemas-5.7.1/emannotationschemas/app.py
--rw-r--r--   0 forrestc   (503) staff       (20)     1096 2023-03-28 21:19:02.000000 emannotationschemas-5.7.1/emannotationschemas/blueprint_app.py
--rw-r--r--   0 forrestc   (503) staff       (20)     1125 2022-06-22 22:14:12.000000 emannotationschemas-5.7.1/emannotationschemas/config.py
--rw-r--r--   0 forrestc   (503) staff       (20)      354 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/emannotationschemas/errors.py
--rw-r--r--   0 forrestc   (503) staff       (20)      969 2022-06-22 22:14:12.000000 emannotationschemas-5.7.1/emannotationschemas/flatten.py
-drwxr-xr-x   0 forrestc   (503) staff       (20)        0 2023-03-28 21:19:12.643074 emannotationschemas-5.7.1/emannotationschemas/migrations/
--rw-r--r--   0 forrestc   (503) staff       (20)        0 2022-06-27 19:19:02.000000 emannotationschemas-5.7.1/emannotationschemas/migrations/__init__.py
--rw-r--r--   0 forrestc   (503) staff       (20)     2876 2022-06-27 19:19:02.000000 emannotationschemas-5.7.1/emannotationschemas/migrations/alembic.ini
--rw-r--r--   0 forrestc   (503) staff       (20)     2916 2022-06-27 19:19:02.000000 emannotationschemas-5.7.1/emannotationschemas/migrations/env.py
--rw-r--r--   0 forrestc   (503) staff       (20)      929 2022-06-27 19:19:02.000000 emannotationschemas-5.7.1/emannotationschemas/migrations/run.py
-drwxr-xr-x   0 forrestc   (503) staff       (20)        0 2023-03-28 21:19:12.644988 emannotationschemas-5.7.1/emannotationschemas/migrations/versions/
--rw-r--r--   0 forrestc   (503) staff       (20)     9034 2022-06-27 19:19:02.000000 emannotationschemas-5.7.1/emannotationschemas/migrations/versions/34476f534ca9_add_new_schemas.py
--rw-r--r--   0 forrestc   (503) staff       (20)        0 2022-06-27 19:20:06.000000 emannotationschemas-5.7.1/emannotationschemas/migrations/versions/__init__.py
--rw-r--r--   0 forrestc   (503) staff       (20)     8439 2023-03-22 23:19:00.000000 emannotationschemas-5.7.1/emannotationschemas/migrations/versions/ad07b1b72351_add_additional_schemas.py
--rw-r--r--   0 forrestc   (503) staff       (20)    56918 2022-06-27 19:19:02.000000 emannotationschemas-5.7.1/emannotationschemas/migrations/versions/bc42c1e4cc1a_base_schemas.py
--rw-r--r--   0 forrestc   (503) staff       (20)    22722 2023-03-22 23:19:00.000000 emannotationschemas-5.7.1/emannotationschemas/models.py
-drwxr-xr-x   0 forrestc   (503) staff       (20)        0 2023-03-28 21:19:12.668015 emannotationschemas-5.7.1/emannotationschemas/schemas/
--rw-r--r--   0 forrestc   (503) staff       (20)        0 2021-02-19 01:53:05.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/__init__.py
--rw-r--r--   0 forrestc   (503) staff       (20)     5095 2022-12-20 20:09:43.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/base.py
--rw-r--r--   0 forrestc   (503) staff       (20)     1176 2022-06-22 22:14:12.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/bound_text_tag.py
--rw-r--r--   0 forrestc   (503) staff       (20)      356 2022-02-01 14:49:00.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/bouton_shape.py
--rw-r--r--   0 forrestc   (503) staff       (20)      478 2022-11-02 14:57:25.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/braincircuits.py
--rw-r--r--   0 forrestc   (503) staff       (20)     2042 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/categorical_factories.py
--rw-r--r--   0 forrestc   (503) staff       (20)     2582 2022-02-01 14:49:00.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/cell_type_local.py
--rw-r--r--   0 forrestc   (503) staff       (20)     1201 2022-04-29 03:45:10.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/contact.py
--rw-r--r--   0 forrestc   (503) staff       (20)      937 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/derived_spatial_point.py
--rw-r--r--   0 forrestc   (503) staff       (20)      647 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/extended_classical_cell_type.py
--rw-r--r--   0 forrestc   (503) staff       (20)      849 2022-06-22 22:14:12.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/fly_cell_types.py
--rw-r--r--   0 forrestc   (503) staff       (20)     1762 2022-09-29 23:08:12.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/functional_coregistration.py
--rw-r--r--   0 forrestc   (503) staff       (20)      565 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/glia_contact.py
--rw-r--r--   0 forrestc   (503) staff       (20)      223 2022-06-22 22:14:12.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/groups.py
--rw-r--r--   0 forrestc   (503) staff       (20)      228 2022-02-01 14:49:00.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/neuropil.py
--rw-r--r--   0 forrestc   (503) staff       (20)      713 2022-03-03 21:02:57.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/nucleus_detection.py
--rw-r--r--   0 forrestc   (503) staff       (20)      849 2022-02-01 14:49:00.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/postsynaptic_compartment.py
--rw-r--r--   0 forrestc   (503) staff       (20)      509 2022-02-01 14:49:00.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/presynaptic_bouton_type.py
--rw-r--r--   0 forrestc   (503) staff       (20)     1787 2022-04-29 03:45:10.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/proofreading.py
--rw-r--r--   0 forrestc   (503) staff       (20)     3045 2022-06-22 22:14:12.000000 emannotationschemas-5.7.1/emannotationschemas/schemas/synapse.py
--rw-r--r--   0 forrestc   (503) staff       (20)     1123 2022-06-22 22:14:12.000000 emannotationschemas-5.7.1/emannotationschemas/utils.py
--rw-r--r--   0 forrestc   (503) staff       (20)     2232 2023-03-28 21:19:02.000000 emannotationschemas-5.7.1/emannotationschemas/views.py
-drwxr-xr-x   0 forrestc   (503) staff       (20)        0 2023-03-28 21:19:12.641776 emannotationschemas-5.7.1/emannotationschemas.egg-info/
--rw-r--r--   0 forrestc   (503) staff       (20)      307 2023-03-28 21:19:12.000000 emannotationschemas-5.7.1/emannotationschemas.egg-info/PKG-INFO
--rw-r--r--   0 forrestc   (503) staff       (20)     2445 2023-03-28 21:19:12.000000 emannotationschemas-5.7.1/emannotationschemas.egg-info/SOURCES.txt
--rw-r--r--   0 forrestc   (503) staff       (20)        1 2023-03-28 21:19:12.000000 emannotationschemas-5.7.1/emannotationschemas.egg-info/dependency_links.txt
--rw-r--r--   0 forrestc   (503) staff       (20)      266 2023-03-28 21:19:12.000000 emannotationschemas-5.7.1/emannotationschemas.egg-info/requires.txt
--rw-r--r--   0 forrestc   (503) staff       (20)       26 2023-03-28 21:19:12.000000 emannotationschemas-5.7.1/emannotationschemas.egg-info/top_level.txt
--rw-r--r--   0 forrestc   (503) staff       (20)      268 2023-03-28 21:18:50.000000 emannotationschemas-5.7.1/requirements.txt
--rw-r--r--   0 forrestc   (503) staff       (20)      140 2023-03-28 21:19:12.696219 emannotationschemas-5.7.1/setup.cfg
--rw-r--r--   0 forrestc   (503) staff       (20)     1242 2020-03-03 22:34:04.000000 emannotationschemas-5.7.1/setup.py
--rw-r--r--   0 forrestc   (503) staff       (20)       43 2021-06-03 23:41:27.000000 emannotationschemas-5.7.1/test_requirements.txt
-drwxr-xr-x   0 forrestc   (503) staff       (20)        0 2023-03-28 21:19:12.694453 emannotationschemas-5.7.1/tests/
--rw-r--r--   0 forrestc   (503) staff       (20)        0 2021-06-03 23:41:27.000000 emannotationschemas-5.7.1/tests/__init__.py
--rw-r--r--   0 forrestc   (503) staff       (20)      374 2022-06-27 19:19:02.000000 emannotationschemas-5.7.1/tests/conftest.py
--rw-r--r--   0 forrestc   (503) staff       (20)      949 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/tests/test_bouton_shape.py
--rw-r--r--   0 forrestc   (503) staff       (20)      800 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/tests/test_cell_types.py
--rw-r--r--   0 forrestc   (503) staff       (20)      576 2022-04-29 03:45:10.000000 emannotationschemas-5.7.1/tests/test_contact.py
--rw-r--r--   0 forrestc   (503) staff       (20)     1852 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/tests/test_derived_spatial_point.py
--rw-r--r--   0 forrestc   (503) staff       (20)      757 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/tests/test_extended_classical_cell_type.py
--rw-r--r--   0 forrestc   (503) staff       (20)      382 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/tests/test_flatten.py
--rw-r--r--   0 forrestc   (503) staff       (20)     1341 2022-06-22 22:14:12.000000 emannotationschemas-5.7.1/tests/test_fly_cell_types.py
--rw-r--r--   0 forrestc   (503) staff       (20)      794 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/tests/test_glia_contact.py
--rw-r--r--   0 forrestc   (503) staff       (20)     5730 2022-10-20 19:49:47.000000 emannotationschemas-5.7.1/tests/test_models.py
--rw-r--r--   0 forrestc   (503) staff       (20)      447 2022-02-01 14:49:00.000000 emannotationschemas-5.7.1/tests/test_neuropil.py
--rw-r--r--   0 forrestc   (503) staff       (20)      607 2022-04-29 03:45:10.000000 emannotationschemas-5.7.1/tests/test_nucleus_detection.py
--rw-r--r--   0 forrestc   (503) staff       (20)     2415 2022-02-01 14:49:00.000000 emannotationschemas-5.7.1/tests/test_proofreading_schema.py
--rw-r--r--   0 forrestc   (503) staff       (20)      877 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/tests/test_schema_blueprint.py
--rw-r--r--   0 forrestc   (503) staff       (20)      524 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/tests/test_schema_module.py
--rw-r--r--   0 forrestc   (503) staff       (20)     2492 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/tests/test_synapse_reference_schema.py
--rw-r--r--   0 forrestc   (503) staff       (20)     6461 2021-10-19 21:11:56.000000 emannotationschemas-5.7.1/tests/test_synapse_schema.py
+drwxr-xr-x   0 forrestc   (503) staff       (20)        0 2023-04-06 22:59:34.295180 emannotationschemas-5.8.0/
+-rw-r--r--   0 forrestc   (503) staff       (20)     1072 2020-03-03 22:34:04.000000 emannotationschemas-5.8.0/LICENSE
+-rw-r--r--   0 forrestc   (503) staff       (20)      105 2022-06-27 19:54:59.000000 emannotationschemas-5.8.0/MANIFEST.in
+-rw-r--r--   0 forrestc   (503) staff       (20)      307 2023-04-06 22:59:34.295480 emannotationschemas-5.8.0/PKG-INFO
+-rw-r--r--   0 forrestc   (503) staff       (20)     3420 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/README.md
+drwxr-xr-x   0 forrestc   (503) staff       (20)        0 2023-04-06 22:59:34.212533 emannotationschemas-5.8.0/emannotationschemas/
+-rw-r--r--   0 forrestc   (503) staff       (20)     5196 2023-04-06 22:59:28.000000 emannotationschemas-5.8.0/emannotationschemas/__init__.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     1321 2023-04-06 22:59:28.000000 emannotationschemas-5.8.0/emannotationschemas/app.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     1096 2023-04-06 22:59:28.000000 emannotationschemas-5.8.0/emannotationschemas/blueprint_app.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     1125 2022-06-22 22:14:12.000000 emannotationschemas-5.8.0/emannotationschemas/config.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      354 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/emannotationschemas/errors.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      969 2022-06-22 22:14:12.000000 emannotationschemas-5.8.0/emannotationschemas/flatten.py
+drwxr-xr-x   0 forrestc   (503) staff       (20)        0 2023-04-06 22:59:34.216895 emannotationschemas-5.8.0/emannotationschemas/migrations/
+-rw-r--r--   0 forrestc   (503) staff       (20)        0 2022-06-27 19:19:02.000000 emannotationschemas-5.8.0/emannotationschemas/migrations/__init__.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     2876 2022-06-27 19:19:02.000000 emannotationschemas-5.8.0/emannotationschemas/migrations/alembic.ini
+-rw-r--r--   0 forrestc   (503) staff       (20)     2916 2022-06-27 19:19:02.000000 emannotationschemas-5.8.0/emannotationschemas/migrations/env.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      929 2022-06-27 19:19:02.000000 emannotationschemas-5.8.0/emannotationschemas/migrations/run.py
+drwxr-xr-x   0 forrestc   (503) staff       (20)        0 2023-04-06 22:59:34.219704 emannotationschemas-5.8.0/emannotationschemas/migrations/versions/
+-rw-r--r--   0 forrestc   (503) staff       (20)    23415 2023-04-06 22:59:09.000000 emannotationschemas-5.8.0/emannotationschemas/migrations/versions/13dffb003203_add_delete_cascade_to_fkeys.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     9034 2022-06-27 19:19:02.000000 emannotationschemas-5.8.0/emannotationschemas/migrations/versions/34476f534ca9_add_new_schemas.py
+-rw-r--r--   0 forrestc   (503) staff       (20)        0 2022-06-27 19:20:06.000000 emannotationschemas-5.8.0/emannotationschemas/migrations/versions/__init__.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     8439 2023-03-22 23:19:00.000000 emannotationschemas-5.8.0/emannotationschemas/migrations/versions/ad07b1b72351_add_additional_schemas.py
+-rw-r--r--   0 forrestc   (503) staff       (20)    56918 2022-06-27 19:19:02.000000 emannotationschemas-5.8.0/emannotationschemas/migrations/versions/bc42c1e4cc1a_base_schemas.py
+-rw-r--r--   0 forrestc   (503) staff       (20)    22966 2023-04-06 22:59:09.000000 emannotationschemas-5.8.0/emannotationschemas/models.py
+drwxr-xr-x   0 forrestc   (503) staff       (20)        0 2023-04-06 22:59:34.243169 emannotationschemas-5.8.0/emannotationschemas/schemas/
+-rw-r--r--   0 forrestc   (503) staff       (20)        0 2021-02-19 01:53:05.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/__init__.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     5095 2022-12-20 20:09:43.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/base.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     1176 2022-06-22 22:14:12.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/bound_text_tag.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      356 2022-02-01 14:49:00.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/bouton_shape.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      478 2022-11-02 14:57:25.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/braincircuits.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     2042 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/categorical_factories.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     2582 2022-02-01 14:49:00.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/cell_type_local.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     1201 2022-04-29 03:45:10.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/contact.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      937 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/derived_spatial_point.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      647 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/extended_classical_cell_type.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      849 2022-06-22 22:14:12.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/fly_cell_types.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     1762 2022-09-29 23:08:12.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/functional_coregistration.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      565 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/glia_contact.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      223 2022-06-22 22:14:12.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/groups.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      228 2022-02-01 14:49:00.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/neuropil.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      713 2022-03-03 21:02:57.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/nucleus_detection.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      849 2022-02-01 14:49:00.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/postsynaptic_compartment.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      509 2022-02-01 14:49:00.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/presynaptic_bouton_type.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     1787 2022-04-29 03:45:10.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/proofreading.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     3045 2022-06-22 22:14:12.000000 emannotationschemas-5.8.0/emannotationschemas/schemas/synapse.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     1123 2022-06-22 22:14:12.000000 emannotationschemas-5.8.0/emannotationschemas/utils.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     2232 2023-04-06 22:59:28.000000 emannotationschemas-5.8.0/emannotationschemas/views.py
+drwxr-xr-x   0 forrestc   (503) staff       (20)        0 2023-04-06 22:59:34.213437 emannotationschemas-5.8.0/emannotationschemas.egg-info/
+-rw-r--r--   0 forrestc   (503) staff       (20)      307 2023-04-06 22:59:34.000000 emannotationschemas-5.8.0/emannotationschemas.egg-info/PKG-INFO
+-rw-r--r--   0 forrestc   (503) staff       (20)     2529 2023-04-06 22:59:34.000000 emannotationschemas-5.8.0/emannotationschemas.egg-info/SOURCES.txt
+-rw-r--r--   0 forrestc   (503) staff       (20)        1 2023-04-06 22:59:34.000000 emannotationschemas-5.8.0/emannotationschemas.egg-info/dependency_links.txt
+-rw-r--r--   0 forrestc   (503) staff       (20)      266 2023-04-06 22:59:34.000000 emannotationschemas-5.8.0/emannotationschemas.egg-info/requires.txt
+-rw-r--r--   0 forrestc   (503) staff       (20)       26 2023-04-06 22:59:34.000000 emannotationschemas-5.8.0/emannotationschemas.egg-info/top_level.txt
+-rw-r--r--   0 forrestc   (503) staff       (20)      268 2023-03-28 21:18:50.000000 emannotationschemas-5.8.0/requirements.txt
+-rw-r--r--   0 forrestc   (503) staff       (20)      140 2023-04-06 22:59:34.296130 emannotationschemas-5.8.0/setup.cfg
+-rw-r--r--   0 forrestc   (503) staff       (20)     1242 2020-03-03 22:34:04.000000 emannotationschemas-5.8.0/setup.py
+-rw-r--r--   0 forrestc   (503) staff       (20)       43 2021-06-03 23:41:27.000000 emannotationschemas-5.8.0/test_requirements.txt
+drwxr-xr-x   0 forrestc   (503) staff       (20)        0 2023-04-06 22:59:34.289538 emannotationschemas-5.8.0/tests/
+-rw-r--r--   0 forrestc   (503) staff       (20)        0 2021-06-03 23:41:27.000000 emannotationschemas-5.8.0/tests/__init__.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      374 2022-06-27 19:19:02.000000 emannotationschemas-5.8.0/tests/conftest.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      949 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/tests/test_bouton_shape.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      800 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/tests/test_cell_types.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      576 2022-04-29 03:45:10.000000 emannotationschemas-5.8.0/tests/test_contact.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     1852 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/tests/test_derived_spatial_point.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      757 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/tests/test_extended_classical_cell_type.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      382 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/tests/test_flatten.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     1341 2022-06-22 22:14:12.000000 emannotationschemas-5.8.0/tests/test_fly_cell_types.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      794 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/tests/test_glia_contact.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     5730 2022-10-20 19:49:47.000000 emannotationschemas-5.8.0/tests/test_models.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      447 2022-02-01 14:49:00.000000 emannotationschemas-5.8.0/tests/test_neuropil.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      607 2022-04-29 03:45:10.000000 emannotationschemas-5.8.0/tests/test_nucleus_detection.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     2415 2022-02-01 14:49:00.000000 emannotationschemas-5.8.0/tests/test_proofreading_schema.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      877 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/tests/test_schema_blueprint.py
+-rw-r--r--   0 forrestc   (503) staff       (20)      524 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/tests/test_schema_module.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     2492 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/tests/test_synapse_reference_schema.py
+-rw-r--r--   0 forrestc   (503) staff       (20)     6461 2021-10-19 21:11:56.000000 emannotationschemas-5.8.0/tests/test_synapse_schema.py
```

### Comparing `emannotationschemas-5.7.1/LICENSE` & `emannotationschemas-5.8.0/LICENSE`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/README.md` & `emannotationschemas-5.8.0/README.md`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/__init__.py` & `emannotationschemas-5.8.0/emannotationschemas/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -48,15 +48,15 @@
 from emannotationschemas.schemas.braincircuits import (
     BrainCircuitsBoundTagAnnotationUser,
 )
 
 from emannotationschemas.errors import UnknownAnnotationTypeException
 from emannotationschemas.flatten import create_flattened_schema
 
-__version__ = "5.7.1"
+__version__ = "5.8.0"
 
 type_mapping = {
     "synapse": SynapseSchema,
     "nocleft_synapse": NoCleftSynapse,
     "fly_synapse": BuhmannSynapseSchema,
     "fly_nt_synapse": BuhmannEcksteinSynapseSchema,
     "bouton_shape": BoutonShape,
```

### Comparing `emannotationschemas-5.7.1/emannotationschemas/app.py` & `emannotationschemas-5.8.0/emannotationschemas/app.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 from flask_restx import Api
 
 from emannotationschemas.blueprint_app import api_bp
 from emannotationschemas.config import configure_app
 from emannotationschemas.utils import get_instance_folder_path
 from emannotationschemas.views import views_bp
 
-__version__ = "5.7.1"
+__version__ = "5.8.0"
 
 
 def create_app(test_config=None):
 
     # Define the Flask Object
     app = Flask(
         __name__,
```

### Comparing `emannotationschemas-5.7.1/emannotationschemas/blueprint_app.py` & `emannotationschemas-5.8.0/emannotationschemas/blueprint_app.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from flask import abort
 from flask_restx import Namespace, Resource
 from marshmallow_jsonschema import JSONSchema
 
 from emannotationschemas import get_schema, get_types
 from emannotationschemas.errors import UnknownAnnotationTypeException
 
-__version__ = "5.7.1"
+__version__ = "5.8.0"
 
 authorizations = {
     "apikey": {"type": "apiKey", "in": "query", "name": "middle_auth_token"}
 }
 
 api_bp = Namespace(
     "EMAnnotation Schemas",
```

### Comparing `emannotationschemas-5.7.1/emannotationschemas/config.py` & `emannotationschemas-5.8.0/emannotationschemas/config.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/flatten.py` & `emannotationschemas-5.8.0/emannotationschemas/flatten.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/migrations/alembic.ini` & `emannotationschemas-5.8.0/emannotationschemas/migrations/alembic.ini`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/migrations/env.py` & `emannotationschemas-5.8.0/emannotationschemas/migrations/env.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/migrations/run.py` & `emannotationschemas-5.8.0/emannotationschemas/migrations/run.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/migrations/versions/34476f534ca9_add_new_schemas.py` & `emannotationschemas-5.8.0/emannotationschemas/migrations/versions/34476f534ca9_add_new_schemas.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/migrations/versions/ad07b1b72351_add_additional_schemas.py` & `emannotationschemas-5.8.0/emannotationschemas/migrations/versions/ad07b1b72351_add_additional_schemas.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/migrations/versions/bc42c1e4cc1a_base_schemas.py` & `emannotationschemas-5.8.0/emannotationschemas/migrations/versions/bc42c1e4cc1a_base_schemas.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/models.py` & `emannotationschemas-5.8.0/emannotationschemas/models.py`

 * *Files 2% similar despite different names*

```diff
@@ -280,15 +280,20 @@
     if segmentation_source:
         model_dict.update(
             {
                 "__tablename__": create_segmentation_table_name(
                     table_name, segmentation_source
                 ),
                 "id": Column(
-                    BigInteger, ForeignKey(f"{table_name}.id"), primary_key=True
+                    BigInteger,
+                    ForeignKey(
+                        f"{table_name}.id",
+                        ondelete="CASCADE",
+                    ),
+                    primary_key=True,
                 ),
                 "__mapper_args__": {
                     "polymorphic_identity": create_segmentation_table_name(
                         table_name, segmentation_source
                     ),
                     "concrete": True,
                 },
@@ -364,15 +369,20 @@
                     geometry_type=postgis_geom, dimension=3, use_N_D_index=has_index
                 )
             )
         elif field_type == ReferenceTableField:
             reference_table_name = model_dict.pop("reference_table_name")
             foreign_key_name = f"{reference_table_name}.id"
             model_dict[key] = Column(
-                BigInteger, ForeignKey(foreign_key_name), index=has_index
+                BigInteger,
+                ForeignKey(
+                    foreign_key_name,
+                    ondelete="CASCADE",
+                ),
+                index=has_index,
             )
         else:
             model_dict[key] = Column(field_column_map[field_type], index=has_index)
 
     else:
         raise InvalidSchemaField(f"field type {field_type} not supported")
```

### Comparing `emannotationschemas-5.7.1/emannotationschemas/schemas/base.py` & `emannotationschemas-5.8.0/emannotationschemas/schemas/base.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/schemas/bound_text_tag.py` & `emannotationschemas-5.8.0/emannotationschemas/schemas/bound_text_tag.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/schemas/categorical_factories.py` & `emannotationschemas-5.8.0/emannotationschemas/schemas/categorical_factories.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/schemas/cell_type_local.py` & `emannotationschemas-5.8.0/emannotationschemas/schemas/cell_type_local.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/schemas/contact.py` & `emannotationschemas-5.8.0/emannotationschemas/schemas/contact.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/schemas/derived_spatial_point.py` & `emannotationschemas-5.8.0/emannotationschemas/schemas/derived_spatial_point.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/schemas/extended_classical_cell_type.py` & `emannotationschemas-5.8.0/emannotationschemas/schemas/extended_classical_cell_type.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/schemas/fly_cell_types.py` & `emannotationschemas-5.8.0/emannotationschemas/schemas/fly_cell_types.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/schemas/functional_coregistration.py` & `emannotationschemas-5.8.0/emannotationschemas/schemas/functional_coregistration.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/schemas/glia_contact.py` & `emannotationschemas-5.8.0/emannotationschemas/schemas/glia_contact.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/schemas/nucleus_detection.py` & `emannotationschemas-5.8.0/emannotationschemas/schemas/nucleus_detection.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/schemas/postsynaptic_compartment.py` & `emannotationschemas-5.8.0/emannotationschemas/schemas/postsynaptic_compartment.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/schemas/proofreading.py` & `emannotationschemas-5.8.0/emannotationschemas/schemas/proofreading.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/schemas/synapse.py` & `emannotationschemas-5.8.0/emannotationschemas/schemas/synapse.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/utils.py` & `emannotationschemas-5.8.0/emannotationschemas/utils.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/emannotationschemas/views.py` & `emannotationschemas-5.8.0/emannotationschemas/views.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import marshmallow as mm
 import pandas as pd
 from flask import Blueprint, jsonify, render_template
 
 from emannotationschemas import get_flat_schema, get_schema, get_types
 
-__version__ = "5.7.1"
+__version__ = "5.8.0"
 
 
 views_bp = Blueprint("views", __name__, url_prefix="/schema/views")
 
 
 @views_bp.route("/")
 def index():
```

### Comparing `emannotationschemas-5.7.1/emannotationschemas.egg-info/SOURCES.txt` & `emannotationschemas-5.8.0/emannotationschemas.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -19,14 +19,15 @@
 emannotationschemas.egg-info/dependency_links.txt
 emannotationschemas.egg-info/requires.txt
 emannotationschemas.egg-info/top_level.txt
 emannotationschemas/migrations/__init__.py
 emannotationschemas/migrations/alembic.ini
 emannotationschemas/migrations/env.py
 emannotationschemas/migrations/run.py
+emannotationschemas/migrations/versions/13dffb003203_add_delete_cascade_to_fkeys.py
 emannotationschemas/migrations/versions/34476f534ca9_add_new_schemas.py
 emannotationschemas/migrations/versions/__init__.py
 emannotationschemas/migrations/versions/ad07b1b72351_add_additional_schemas.py
 emannotationschemas/migrations/versions/bc42c1e4cc1a_base_schemas.py
 emannotationschemas/schemas/__init__.py
 emannotationschemas/schemas/base.py
 emannotationschemas/schemas/bound_text_tag.py
```

### Comparing `emannotationschemas-5.7.1/setup.py` & `emannotationschemas-5.8.0/setup.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/tests/test_bouton_shape.py` & `emannotationschemas-5.8.0/tests/test_bouton_shape.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/tests/test_cell_types.py` & `emannotationschemas-5.8.0/tests/test_cell_types.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/tests/test_contact.py` & `emannotationschemas-5.8.0/tests/test_contact.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/tests/test_derived_spatial_point.py` & `emannotationschemas-5.8.0/tests/test_derived_spatial_point.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/tests/test_extended_classical_cell_type.py` & `emannotationschemas-5.8.0/tests/test_extended_classical_cell_type.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/tests/test_fly_cell_types.py` & `emannotationschemas-5.8.0/tests/test_fly_cell_types.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/tests/test_glia_contact.py` & `emannotationschemas-5.8.0/tests/test_glia_contact.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/tests/test_models.py` & `emannotationschemas-5.8.0/tests/test_models.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/tests/test_nucleus_detection.py` & `emannotationschemas-5.8.0/tests/test_nucleus_detection.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/tests/test_proofreading_schema.py` & `emannotationschemas-5.8.0/tests/test_proofreading_schema.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/tests/test_schema_blueprint.py` & `emannotationschemas-5.8.0/tests/test_schema_blueprint.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/tests/test_schema_module.py` & `emannotationschemas-5.8.0/tests/test_schema_module.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/tests/test_synapse_reference_schema.py` & `emannotationschemas-5.8.0/tests/test_synapse_reference_schema.py`

 * *Files identical despite different names*

### Comparing `emannotationschemas-5.7.1/tests/test_synapse_schema.py` & `emannotationschemas-5.8.0/tests/test_synapse_schema.py`

 * *Files identical despite different names*

