# Comparing `tmp/modelon_impact_client-3.0.0.dev8.tar.gz` & `tmp/modelon_impact_client-3.0.0.dev9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "modelon_impact_client-3.0.0.dev8.tar", max compression
+gzip compressed data, was "modelon_impact_client-3.0.0.dev9.tar", max compression
```

## Comparing `modelon_impact_client-3.0.0.dev8.tar` & `modelon_impact_client-3.0.0.dev9.tar`

### file list

```diff
@@ -1,64 +1,64 @@
--rw-r--r--   0        0        0     1477 2022-12-21 14:06:14.546617 modelon_impact_client-3.0.0.dev8/LICENSE.md
--rw-r--r--   0        0        0     2748 2022-12-21 14:06:14.554617 modelon_impact_client-3.0.0.dev8/README.md
--rw-r--r--   0        0        0        0 2022-12-21 14:06:14.521616 modelon_impact_client-3.0.0.dev8/modelon/__init__.py
--rw-r--r--   0        0        0        0 2022-12-21 14:06:14.544617 modelon_impact_client-3.0.0.dev8/modelon/impact/__init__.py
--rw-r--r--   0        0        0      753 2022-12-21 14:06:14.541617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/__init__.py
--rw-r--r--   0        0        0    14534 2022-12-21 14:06:14.525616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/client.py
--rw-r--r--   0        0        0      787 2022-12-21 14:06:14.555617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/configuration.py
--rw-r--r--   0        0        0     1663 2022-12-21 14:06:14.525616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/credential_manager.py
--rw-r--r--   0        0        0      119 2022-12-21 14:06:14.535616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/__init__.py
--rw-r--r--   0        0        0      552 2022-12-21 14:06:14.517616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/asserts.py
--rw-r--r--   0        0        0    16640 2022-12-21 14:06:14.554617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/case.py
--rw-r--r--   0        0        0     5932 2022-12-21 14:06:14.563618 modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/content.py
--rw-r--r--   0        0        0     6385 2022-12-21 14:06:14.527616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/custom_function.py
--rw-r--r--   0        0        0    11124 2022-12-21 14:06:14.529616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/experiment.py
--rw-r--r--   0        0        0     1838 2022-12-21 14:06:14.517616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/external_result.py
--rw-r--r--   0        0        0      158 2022-12-21 14:06:14.536617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/log.py
--rw-r--r--   0        0        0    11249 2022-12-21 14:06:14.530616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/model.py
--rw-r--r--   0        0        0     8370 2022-12-21 14:06:14.523616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/model_executable.py
--rw-r--r--   0        0        0    10459 2022-12-21 14:06:14.561618 modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/project.py
--rw-r--r--   0        0        0     1555 2022-12-21 14:06:14.538617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/result.py
--rw-r--r--   0        0        0      775 2022-12-21 14:06:14.512616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/status.py
--rw-r--r--   0        0        0    20394 2022-12-21 14:06:14.558617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/workspace.py
--rw-r--r--   0        0        0     1093 2022-12-21 14:06:14.527616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/exceptions.py
--rw-r--r--   0        0        0        0 2022-12-21 14:06:14.518616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/experiment_definition/__init__.py
--rw-r--r--   0        0        0     3602 2022-12-21 14:06:14.567618 modelon_impact_client-3.0.0.dev8/modelon/impact/client/experiment_definition/asserts.py
--rw-r--r--   0        0        0    30259 2022-12-21 14:06:14.530616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/experiment_definition/base.py
--rw-r--r--   0        0        0     3250 2022-12-21 14:06:14.525616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/experiment_definition/expansion.py
--rw-r--r--   0        0        0     9643 2022-12-21 14:06:14.513615 modelon_impact_client-3.0.0.dev8/modelon/impact/client/experiment_definition/extension.py
--rw-r--r--   0        0        0     4642 2022-12-21 14:06:14.515616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/experiment_definition/operators.py
--rw-r--r--   0        0        0      414 2022-12-21 14:06:14.517616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/experiment_definition/util.py
--rw-r--r--   0        0        0       65 2022-12-21 14:06:14.565618 modelon_impact_client-3.0.0.dev8/modelon/impact/client/jupyterhub/__init__.py
--rw-r--r--   0        0        0     1860 2022-12-21 14:06:14.549617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/jupyterhub/authorize.py
--rw-r--r--   0        0        0      281 2022-12-21 14:06:14.569618 modelon_impact_client-3.0.0.dev8/modelon/impact/client/jupyterhub/exceptions.py
--rw-r--r--   0        0        0     2554 2022-12-21 14:06:14.528616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/jupyterhub/sal.py
--rw-r--r--   0        0        0       79 2022-12-21 14:06:14.519616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/__init__.py
--rw-r--r--   0        0        0     5002 2022-12-21 14:06:14.532616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/base.py
--rw-r--r--   0        0        0     2107 2022-12-21 14:06:14.539617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/case.py
--rw-r--r--   0        0        0     2363 2022-12-21 14:06:14.540617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/content_import.py
--rw-r--r--   0        0        0     2039 2022-12-21 14:06:14.518616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/experiment.py
--rw-r--r--   0        0        0     2244 2022-12-21 14:06:14.541617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/external_result.py
--rw-r--r--   0        0        0     5516 2022-12-21 14:06:14.566618 modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/model_executable.py
--rw-r--r--   0        0        0        0 2022-12-21 14:06:14.522616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/workspace/__init__.py
--rw-r--r--   0        0        0     2397 2022-12-21 14:06:14.566618 modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/workspace/conversion.py
--rw-r--r--   0        0        0     3081 2022-12-21 14:06:14.567618 modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/workspace/exports.py
--rw-r--r--   0        0        0     2464 2022-12-21 14:06:14.550617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/workspace/imports.py
--rw-r--r--   0        0        0     3397 2022-12-21 14:06:14.556617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/options.py
--rw-r--r--   0        0        0        0 2022-12-21 14:06:14.547617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/__init__.py
--rw-r--r--   0        0        0      123 2022-12-21 14:06:14.544617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/context.py
--rw-r--r--   0        0        0     1413 2022-12-21 14:06:14.533616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/custom_function.py
--rw-r--r--   0        0        0      723 2022-12-21 14:06:14.511615 modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/exceptions.py
--rw-r--r--   0        0        0     5739 2022-12-21 14:06:14.549617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/experiment.py
--rw-r--r--   0        0        0      419 2022-12-21 14:06:14.526616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/export.py
--rw-r--r--   0        0        0     2715 2022-12-21 14:06:14.542617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/http.py
--rw-r--r--   0        0        0     2706 2022-12-21 14:06:14.556617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/model_executable.py
--rw-r--r--   0        0        0     4023 2022-12-21 14:06:14.550617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/project.py
--rw-r--r--   0        0        0     3560 2022-12-21 14:06:14.526616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/request.py
--rw-r--r--   0        0        0     4509 2022-12-21 14:06:14.538617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/response.py
--rw-r--r--   0        0        0     3644 2022-12-21 14:06:14.519616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/service.py
--rw-r--r--   0        0        0      770 2022-12-21 14:06:14.514616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/uri.py
--rw-r--r--   0        0        0      405 2022-12-21 14:06:14.535616 modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/users.py
--rw-r--r--   0        0        0     7467 2022-12-21 14:06:14.534617 modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/workspace.py
--rw-r--r--   0        0        0      970 2022-12-21 14:06:52.498305 modelon_impact_client-3.0.0.dev8/pyproject.toml
--rw-r--r--   0        0        0     3873 1970-01-01 00:00:00.000000 modelon_impact_client-3.0.0.dev8/setup.py
--rw-r--r--   0        0        0     3785 1970-01-01 00:00:00.000000 modelon_impact_client-3.0.0.dev8/PKG-INFO
+-rw-r--r--   0        0        0     1477 2023-01-24 18:43:55.104900 modelon_impact_client-3.0.0.dev9/LICENSE.md
+-rw-r--r--   0        0        0     2748 2023-01-24 18:43:55.113901 modelon_impact_client-3.0.0.dev9/README.md
+-rw-r--r--   0        0        0        0 2023-01-24 18:43:55.079899 modelon_impact_client-3.0.0.dev9/modelon/__init__.py
+-rw-r--r--   0        0        0        0 2023-01-24 18:43:55.102900 modelon_impact_client-3.0.0.dev9/modelon/impact/__init__.py
+-rw-r--r--   0        0        0      753 2023-01-24 18:43:55.098900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/__init__.py
+-rw-r--r--   0        0        0    14534 2023-01-24 18:43:55.083899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/client.py
+-rw-r--r--   0        0        0      787 2023-01-24 18:43:55.114901 modelon_impact_client-3.0.0.dev9/modelon/impact/client/configuration.py
+-rw-r--r--   0        0        0     1663 2023-01-24 18:43:55.084899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/credential_manager.py
+-rw-r--r--   0        0        0      119 2023-01-24 18:43:55.094900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/__init__.py
+-rw-r--r--   0        0        0      552 2023-01-24 18:43:55.076899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/asserts.py
+-rw-r--r--   0        0        0    16640 2023-01-24 18:43:55.112901 modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/case.py
+-rw-r--r--   0        0        0     5932 2023-01-24 18:43:55.124901 modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/content.py
+-rw-r--r--   0        0        0     6385 2023-01-24 18:43:55.085899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/custom_function.py
+-rw-r--r--   0        0        0    11124 2023-01-24 18:43:55.088899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/experiment.py
+-rw-r--r--   0        0        0     1838 2023-01-24 18:43:55.076899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/external_result.py
+-rw-r--r--   0        0        0      158 2023-01-24 18:43:55.095900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/log.py
+-rw-r--r--   0        0        0    11249 2023-01-24 18:43:55.088899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/model.py
+-rw-r--r--   0        0        0     8671 2023-01-24 18:43:55.081899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/model_executable.py
+-rw-r--r--   0        0        0    10459 2023-01-24 18:43:55.121901 modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/project.py
+-rw-r--r--   0        0        0     1555 2023-01-24 18:43:55.096900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/result.py
+-rw-r--r--   0        0        0      775 2023-01-24 18:43:55.067899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/status.py
+-rw-r--r--   0        0        0    20394 2023-01-24 18:43:55.117901 modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/workspace.py
+-rw-r--r--   0        0        0     1093 2023-01-24 18:43:55.086899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/exceptions.py
+-rw-r--r--   0        0        0        0 2023-01-24 18:43:55.077899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/experiment_definition/__init__.py
+-rw-r--r--   0        0        0     3602 2023-01-24 18:43:55.130901 modelon_impact_client-3.0.0.dev9/modelon/impact/client/experiment_definition/asserts.py
+-rw-r--r--   0        0        0    30259 2023-01-24 18:43:55.089899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/experiment_definition/base.py
+-rw-r--r--   0        0        0     3250 2023-01-24 18:43:55.083899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/experiment_definition/expansion.py
+-rw-r--r--   0        0        0     9643 2023-01-24 18:43:55.068899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/experiment_definition/extension.py
+-rw-r--r--   0        0        0     4642 2023-01-24 18:43:55.074899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/experiment_definition/operators.py
+-rw-r--r--   0        0        0      414 2023-01-24 18:43:55.076899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/experiment_definition/util.py
+-rw-r--r--   0        0        0       65 2023-01-24 18:43:55.128901 modelon_impact_client-3.0.0.dev9/modelon/impact/client/jupyterhub/__init__.py
+-rw-r--r--   0        0        0     1860 2023-01-24 18:43:55.107900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/jupyterhub/authorize.py
+-rw-r--r--   0        0        0      281 2023-01-24 18:43:55.133901 modelon_impact_client-3.0.0.dev9/modelon/impact/client/jupyterhub/exceptions.py
+-rw-r--r--   0        0        0     2554 2023-01-24 18:43:55.086899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/jupyterhub/sal.py
+-rw-r--r--   0        0        0       79 2023-01-24 18:43:55.078899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/__init__.py
+-rw-r--r--   0        0        0     5002 2023-01-24 18:43:55.090900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/base.py
+-rw-r--r--   0        0        0     2107 2023-01-24 18:43:55.097900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/case.py
+-rw-r--r--   0        0        0     2363 2023-01-24 18:43:55.098900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/content_import.py
+-rw-r--r--   0        0        0     2039 2023-01-24 18:43:55.077899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/experiment.py
+-rw-r--r--   0        0        0     2244 2023-01-24 18:43:55.099900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/external_result.py
+-rw-r--r--   0        0        0     5516 2023-01-24 18:43:55.128901 modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/model_executable.py
+-rw-r--r--   0        0        0        0 2023-01-24 18:43:55.081899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/workspace/__init__.py
+-rw-r--r--   0        0        0     2397 2023-01-24 18:43:55.129901 modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/workspace/conversion.py
+-rw-r--r--   0        0        0     3081 2023-01-24 18:43:55.130901 modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/workspace/exports.py
+-rw-r--r--   0        0        0     2464 2023-01-24 18:43:55.108900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/workspace/imports.py
+-rw-r--r--   0        0        0     3397 2023-01-24 18:43:55.115901 modelon_impact_client-3.0.0.dev9/modelon/impact/client/options.py
+-rw-r--r--   0        0        0        0 2023-01-24 18:43:55.105900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/__init__.py
+-rw-r--r--   0        0        0      123 2023-01-24 18:43:55.102900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/context.py
+-rw-r--r--   0        0        0     1413 2023-01-24 18:43:55.091899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/custom_function.py
+-rw-r--r--   0        0        0      723 2023-01-24 18:43:55.066898 modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/exceptions.py
+-rw-r--r--   0        0        0     5739 2023-01-24 18:43:55.108900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/experiment.py
+-rw-r--r--   0        0        0      419 2023-01-24 18:43:55.084899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/export.py
+-rw-r--r--   0        0        0     2715 2023-01-24 18:43:55.100900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/http.py
+-rw-r--r--   0        0        0     2706 2023-01-24 18:43:55.115901 modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/model_executable.py
+-rw-r--r--   0        0        0     4023 2023-01-24 18:43:55.109900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/project.py
+-rw-r--r--   0        0        0     3560 2023-01-24 18:43:55.085899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/request.py
+-rw-r--r--   0        0        0     4509 2023-01-24 18:43:55.097900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/response.py
+-rw-r--r--   0        0        0     3644 2023-01-24 18:43:55.077899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/service.py
+-rw-r--r--   0        0        0      770 2023-01-24 18:43:55.069899 modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/uri.py
+-rw-r--r--   0        0        0      405 2023-01-24 18:43:55.094900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/users.py
+-rw-r--r--   0        0        0     7467 2023-01-24 18:43:55.092900 modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/workspace.py
+-rw-r--r--   0        0        0      970 2023-01-24 18:47:18.216913 modelon_impact_client-3.0.0.dev9/pyproject.toml
+-rw-r--r--   0        0        0     3873 1970-01-01 00:00:00.000000 modelon_impact_client-3.0.0.dev9/setup.py
+-rw-r--r--   0        0        0     3785 1970-01-01 00:00:00.000000 modelon_impact_client-3.0.0.dev9/PKG-INFO
```

### Comparing `modelon_impact_client-3.0.0.dev8/LICENSE.md` & `modelon_impact_client-3.0.0.dev9/LICENSE.md`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/README.md` & `modelon_impact_client-3.0.0.dev9/README.md`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/__init__.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/__init__.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/client.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/client.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/configuration.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/configuration.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/credential_manager.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/credential_manager.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/asserts.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/asserts.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/case.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/case.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/content.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/content.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/custom_function.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/custom_function.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/experiment.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/experiment.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/external_result.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/external_result.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/model.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/model.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/model_executable.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/model_executable.py`

 * *Files 1% similar despite different names*

```diff
@@ -234,19 +234,26 @@
                 If no path is given, FMU will be downloaded in a temporary directory.
 
         Returns:
 
             path --
                 Local path to the downloaded FMU.
 
-        Example::
+        Raises:
+
+            OperationNotCompleteError if compilation process is in progress.
+            OperationFailureError if compilation process has failed or was cancelled.
 
-            fmu_path = model.compile().wait().download()
-            fmu_path = model.compile().wait().download('C:/Downloads')
+        Example::
+            fmu =  model.compile().wait()
+            if fmu.is_successful():
+                fmu_path = fmu.download()
+                fmu_path = fmu.download('C:/Downloads')
         """
+        assert_successful_operation(self.is_successful(), "Compilation")
         data = self._sal.workspace.fmu_download(self._workspace_id, self._fmu_id)
         if path is None:
             path = os.path.join(tempfile.gettempdir(), "impact-downloads")
         os.makedirs(path, exist_ok=True)
         fmu_path = os.path.join(path, self._fmu_id + ".fmu")
         with open(fmu_path, "wb") as f:
             f.write(data)
```

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/project.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/project.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/result.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/result.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/status.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/status.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/entities/workspace.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/entities/workspace.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/exceptions.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/exceptions.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/experiment_definition/asserts.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/experiment_definition/asserts.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/experiment_definition/base.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/experiment_definition/base.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/experiment_definition/expansion.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/experiment_definition/expansion.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/experiment_definition/extension.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/experiment_definition/extension.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/experiment_definition/operators.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/experiment_definition/operators.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/jupyterhub/authorize.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/jupyterhub/authorize.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/jupyterhub/sal.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/jupyterhub/sal.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/base.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/base.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/case.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/case.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/content_import.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/content_import.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/experiment.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/experiment.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/external_result.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/external_result.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/model_executable.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/model_executable.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/workspace/conversion.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/workspace/conversion.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/workspace/exports.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/workspace/exports.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/operations/workspace/imports.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/operations/workspace/imports.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/options.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/options.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/custom_function.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/custom_function.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/exceptions.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/exceptions.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/experiment.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/experiment.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/http.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/http.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/model_executable.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/model_executable.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/project.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/project.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/request.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/request.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/response.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/response.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/service.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/service.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/uri.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/uri.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/modelon/impact/client/sal/workspace.py` & `modelon_impact_client-3.0.0.dev9/modelon/impact/client/sal/workspace.py`

 * *Files identical despite different names*

### Comparing `modelon_impact_client-3.0.0.dev8/pyproject.toml` & `modelon_impact_client-3.0.0.dev9/pyproject.toml`

 * *Files 12% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 [tool.poetry]
 name = "modelon-impact-client"
 packages = [
     { include = "modelon" },
 ]
-version = "3.0.0-dev.8"
+version = "3.0.0-dev.9"
 description = "Client library for easy scripting against Modelon Impact"
 readme = "README.md"
 homepage = "https://www.modelon.com/modelon-impact"
 repository = "https://github.com/modelon-community/impact-client-python"
 documentation = "https://modelon-impact-client.readthedocs.io"
 license = "BSD"
 authors = [
```

### Comparing `modelon_impact_client-3.0.0.dev8/setup.py` & `modelon_impact_client-3.0.0.dev9/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -18,15 +18,15 @@
 install_requires = \
 ['requests>=2.23,<3.0',
  'semantic_version>=2.8.5,<3.0.0',
  'types-requests>=2.27.30,<3.0.0']
 
 setup_kwargs = {
     'name': 'modelon-impact-client',
-    'version': '3.0.0.dev8',
+    'version': '3.0.0.dev9',
     'description': 'Client library for easy scripting against Modelon Impact',
     'long_description': '# Modelon-impact-client\nClient library for easy scripting against Modelon Impact\n\n## Installation\n\nFor installation instructions and requirements, please refer to the [documentation](https://modelon-impact-client.readthedocs.io).\n\n## Develop\n\n### Devcontainer\nIf you are developing with VS Code you can use the devcontainer which gives gives you a ready to use environment for development. Just click the "Reopen in Container" button after opening the project in VS Code.\n\n#### Tips and tricks\nIt is possible to run the \'make\' commands listed bellow using the devcontainer. It will detect being in a container and bypass Docker parts of the commands.\n\nYou can open a project with the dev-container directly without having to open and then re-load. Standing in the project directory you can run:\n```\ndevcontainer open .\n```\nNote that this requires the [devcontainer-cli](https://code.visualstudio.com/docs/remote/devcontainer-cli).\n\nYou can add your own extensions to devcontainers. These extensions will be added for all devcontainers. First open your \'settings\' as JSON. Then, to add for example the "GitLens" extension, put the following at the bottom of the settings:\n```\n    ...\n    "remote.containers.defaultExtensions": ["eamodio.gitlens"]\n}\n```\nVS Code also have a `\'Install Local Extensions in \'Remote\'` command, but it must be repeated for each devcontainer and everytime a devcontainer is re-built.\n\n### Creating a shell\nModelon-impact-client is developed using a Docker container for all build tools.\nYou can get a shell into said container by running:\n\n```\nmake shell\n```\n\n### Manage dependencies\nDependencies are managed by poetry. Add dependencies by running \n`poetry add <package>`  or `poetry add <package> --dev` inside the shell\n\n### Running tests\n\nTests are executed by running `make test`. You can also run `make test-watch` to get a watcher\nthat continuously re-runs the tests.\n\n### Running lint\n```\nmake lint\n```\n\n## Build\n\nBuilding modelon-impact-client is done by running\n\n```\nmake wheel\n```\n\n## Release\n\nThe modelon-impact-client build process is a fully automated using `Semantic-release`.\n\nAutomation is enabled for:\n- Bumping version\n- Generate changelog\n\nThis is done based on git commit semantics as described here: https://semantic-release.gitbook.io/semantic-release/\n\nTo make a new release simply run:\n```\nmake publish\n```\n\nThis command will detect what branch you are on and your git history and make a appropriate release.\n\nCurrent configuration can be found in `.releaserc` and specifies that commits to branch `master` should be released and\ncommits to branch `beta` should be released as a `pre-release`.\n\nThis workflow make sure that no administrative time needs to be put into managing the release workflow.\n',
     'author': 'WEP',
     'author_email': 'impact@modelon.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://www.modelon.com/modelon-impact',
```

### Comparing `modelon_impact_client-3.0.0.dev8/PKG-INFO` & `modelon_impact_client-3.0.0.dev9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: modelon-impact-client
-Version: 3.0.0.dev8
+Version: 3.0.0.dev9
 Summary: Client library for easy scripting against Modelon Impact
 Home-page: https://www.modelon.com/modelon-impact
 License: BSD
 Keywords: impact,client,API
 Author: WEP
 Author-email: impact@modelon.com
 Requires-Python: >=3.7.0,<4.0.0
```

