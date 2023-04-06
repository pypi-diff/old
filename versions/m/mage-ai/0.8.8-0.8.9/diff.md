# Comparing `tmp/mage-ai-0.8.8.tar.gz` & `tmp/mage-ai-0.8.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mage-ai-0.8.8.tar", last modified: Sun Feb 26 17:54:39 2023, max compression
+gzip compressed data, was "mage-ai-0.8.9.tar", last modified: Sun Feb 26 23:53:03 2023, max compression
```

## Comparing `mage-ai-0.8.8.tar` & `mage-ai-0.8.9.tar`

### file list

```diff
@@ -1,1039 +1,1039 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.828873 mage-ai-0.8.8/
--rw-r--r--   0 runner    (1001) docker     (123)    11351 2023-02-26 17:54:33.000000 mage-ai-0.8.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      288 2023-02-26 17:54:33.000000 mage-ai-0.8.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)    14948 2023-02-26 17:54:39.828873 mage-ai-0.8.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    14191 2023-02-26 17:54:33.000000 mage-ai-0.8.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.688873 mage-ai-0.8.8/mage_ai/
--rw-r--r--   0 runner    (1001) docker     (123)     4235 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.688873 mage-ai-0.8.8/mage_ai/api/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      455 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/api_context.py
--rw-r--r--   0 runner    (1001) docker     (123)       54 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     1144 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)      400 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/logging.py
--rw-r--r--   0 runner    (1001) docker     (123)     3699 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/middleware.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.688873 mage-ai-0.8.8/mage_ai/api/monitors/
--rw-r--r--   0 runner    (1001) docker     (123)      624 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/monitors/BaseMonitor.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/monitors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      287 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/oauth_scope.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.688873 mage-ai-0.8.8/mage_ai/api/operations/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/operations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11251 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/operations/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      224 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/operations/constants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.692873 mage-ai-0.8.8/mage_ai/api/policies/
--rw-r--r--   0 runner    (1001) docker     (123)      678 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/AutocompleteItemPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)     2010 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/BackfillPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)    10953 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/BasePolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)     2100 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/BlockPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)      810 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/BlockRunPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)      991 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/ClusterPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)      654 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/DataProviderPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)      640 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/EventRulePolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)      992 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/FileContentPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)      965 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/FilePolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)     1200 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/IntegrationDestinationPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)     1788 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/IntegrationSourcePolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)      725 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/IntegrationSourceStreamPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)     1171 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/KernelPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/LogPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)      874 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/MonitorStatPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)      618 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/OutputPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)     2483 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/PipelinePolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)     2189 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/PipelineRunPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)     2524 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/PipelineSchedulePolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)      625 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/ProjectPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)     1224 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/SecretPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)      966 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/SessionPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)     1886 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/UserPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)     1310 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/VariablePolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)     1404 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/WidgetPolicy.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/policies/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.696873 mage-ai-0.8.8/mage_ai/api/presenters/
--rw-r--r--   0 runner    (1001) docker     (123)      303 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/AutocompleteItemPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1556 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/BackfillPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5872 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/BasePresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1924 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/BlockPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      464 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/BlockRunPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      206 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/ClusterPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      193 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/DataProviderPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      156 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/EventRulePresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      282 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/FileContentPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      206 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/FilePresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      382 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/IntegrationDestinationPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1040 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/IntegrationSourcePresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      438 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/IntegrationSourceStreamPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      394 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/KernelPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      265 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/LogPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      180 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/MonitorStatPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      238 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/OutputPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1742 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/PipelinePresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1884 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/PipelineRunPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1348 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/PipelineSchedulePresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      198 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/ProjectPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      166 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/SecretPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      286 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/SessionPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      453 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/UserPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      229 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/VariablePresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)      608 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/WidgetPresenter.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.696873 mage-ai-0.8.8/mage_ai/api/presenters/mixins/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/mixins/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      519 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/presenters/mixins/users.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.700873 mage-ai-0.8.8/mage_ai/api/resources/
--rw-r--r--   0 runner    (1001) docker     (123)     1631 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/AutocompleteItemResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     2053 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/BackfillResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     9482 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/BaseResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     2779 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/BlockResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     3000 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/BlockRunResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     1665 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/ClusterResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     1082 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/DataProviderResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     4973 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/DatabaseResource.py
--rw-r--r--   0 runner    (1001) docker     (123)      460 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/EventRuleResource.py
--rw-r--r--   0 runner    (1001) docker     (123)      898 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/FileContentResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     1511 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/FileResource.py
--rw-r--r--   0 runner    (1001) docker     (123)      237 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/GenericResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     1424 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/IntegrationDestinationResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     2010 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/IntegrationSourceResource.py
--rw-r--r--   0 runner    (1001) docker     (123)      413 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/IntegrationSourceStreamResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     1728 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/KernelResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     8969 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/LogResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     1397 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/MonitorStatResource.py
--rw-r--r--   0 runner    (1001) docker     (123)      572 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/OutputResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     5237 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/PipelineResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     8278 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/PipelineRunResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     3524 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/PipelineScheduleResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     1157 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/ProjectResource.py
--rw-r--r--   0 runner    (1001) docker     (123)      213 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/Resource.py
--rw-r--r--   0 runner    (1001) docker     (123)     1158 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/SecretResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     1792 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/SessionResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     4544 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/UserResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     5009 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/VariableResource.py
--rw-r--r--   0 runner    (1001) docker     (123)     2616 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/WidgetResource.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.700873 mage-ai-0.8.8/mage_ai/api/resources/mixins/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/mixins/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.700873 mage-ai-0.8.8/mage_ai/api/resources/shared/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/shared/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      487 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/shared/collections.py
--rw-r--r--   0 runner    (1001) docker     (123)     2716 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/resources/shared/collective_loaders.py
--rw-r--r--   0 runner    (1001) docker     (123)      950 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/result_set.py
--rw-r--r--   0 runner    (1001) docker     (123)     1452 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     6487 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/api/views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.700873 mage-ai-0.8.8/mage_ai/authentication/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/authentication/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1371 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/authentication/oauth2.py
--rw-r--r--   0 runner    (1001) docker     (123)      732 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/authentication/passwords.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.700873 mage-ai-0.8.8/mage_ai/autocomplete/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/autocomplete/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3651 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/autocomplete/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.700873 mage-ai-0.8.8/mage_ai/cli/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5826 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/cli/main.py
--rw-r--r--   0 runner    (1001) docker     (123)      880 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/cli/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.700873 mage-ai-0.8.8/mage_ai/cluster_manager/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/cluster_manager/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.700873 mage-ai-0.8.8/mage_ai/cluster_manager/aws/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/cluster_manager/aws/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5194 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/cluster_manager/aws/ecs_task_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     2546 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/cluster_manager/aws/emr_cluster_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)      269 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/cluster_manager/cluster_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)      923 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/cluster_manager/constants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.700873 mage-ai-0.8.8/mage_ai/cluster_manager/gcp/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/cluster_manager/gcp/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7933 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/cluster_manager/gcp/cloud_run_service_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.704873 mage-ai-0.8.8/mage_ai/cluster_manager/kubernetes/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/cluster_manager/kubernetes/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9372 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/cluster_manager/kubernetes/workload_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.704873 mage-ai-0.8.8/mage_ai/data_cleaner/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.704873 mage-ai-0.8.8/mage_ai/data_cleaner/analysis/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/analysis/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5932 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/analysis/calculator.py
--rw-r--r--   0 runner    (1001) docker     (123)    10359 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/analysis/charts.py
--rw-r--r--   0 runner    (1001) docker     (123)      510 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/analysis/constants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.704873 mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1977 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1828 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/clean_column_names.py
--rw-r--r--   0 runner    (1001) docker     (123)     1193 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/fix_syntax_errors.py
--rw-r--r--   0 runner    (1001) docker     (123)    16614 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/impute_values.py
--rw-r--r--   0 runner    (1001) docker     (123)    11299 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/reformat_values.py
--rw-r--r--   0 runner    (1001) docker     (123)     2034 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/remove_collinear_columns.py
--rw-r--r--   0 runner    (1001) docker     (123)     1737 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/remove_columns_with_high_empty_rate.py
--rw-r--r--   0 runner    (1001) docker     (123)     1159 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/remove_columns_with_single_value.py
--rw-r--r--   0 runner    (1001) docker     (123)      845 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/remove_duplicate_rows.py
--rw-r--r--   0 runner    (1001) docker     (123)     2069 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/remove_outliers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.704873 mage-ai-0.8.8/mage_ai/data_cleaner/column_types/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/column_types/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10744 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/column_types/column_type_detector.py
--rw-r--r--   0 runner    (1001) docker     (123)      707 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/column_types/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     3750 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/data_cleaner.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.704873 mage-ai-0.8.8/mage_ai/data_cleaner/estimators/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/estimators/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      271 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/estimators/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     3369 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/estimators/encoders.py
--rw-r--r--   0 runner    (1001) docker     (123)     4981 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/estimators/outlier_removal.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.704873 mage-ai-0.8.8/mage_ai/data_cleaner/pipelines/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/pipelines/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5624 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/pipelines/base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.704873 mage-ai-0.8.8/mage_ai/data_cleaner/shared/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/shared/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4497 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/shared/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.704873 mage-ai-0.8.8/mage_ai/data_cleaner/statistics/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/statistics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16266 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/statistics/calculator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.708873 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4652 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/action_code.py
--rw-r--r--   0 runner    (1001) docker     (123)     8471 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    13102 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/column.py
--rw-r--r--   0 runner    (1001) docker     (123)     3172 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     1803 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/custom_action.py
--rw-r--r--   0 runner    (1001) docker     (123)      806 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/dependency_resolution.py
--rw-r--r--   0 runner    (1001) docker     (123)     2535 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)     2740 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/row.py
--rw-r--r--   0 runner    (1001) docker     (123)     1508 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/shared.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.708873 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/spark/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/spark/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      538 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/spark/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)    10533 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/spark/transformers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.708873 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1316 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/addition.py
--rw-r--r--   0 runner    (1001) docker     (123)      593 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      153 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/constant.py
--rw-r--r--   0 runner    (1001) docker     (123)      615 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/date_trunc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1618 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/difference.py
--rw-r--r--   0 runner    (1001) docker     (123)      676 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/distance_between.py
--rw-r--r--   0 runner    (1001) docker     (123)      488 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/divide.py
--rw-r--r--   0 runner    (1001) docker     (123)      262 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/formatted_date.py
--rw-r--r--   0 runner    (1001) docker     (123)      781 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/if_else.py
--rw-r--r--   0 runner    (1001) docker     (123)      492 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/multiply.py
--rw-r--r--   0 runner    (1001) docker     (123)      429 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/string_replace.py
--rw-r--r--   0 runner    (1001) docker     (123)      453 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/string_split.py
--rw-r--r--   0 runner    (1001) docker     (123)      408 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/substring.py
--rw-r--r--   0 runner    (1001) docker     (123)     5748 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1176 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/variable_replacer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.708873 mage-ai-0.8.8/mage_ai/data_integrations/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_integrations/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.708873 mage-ai-0.8.8/mage_ai/data_integrations/destinations/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_integrations/destinations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      315 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_integrations/destinations/constants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.708873 mage-ai-0.8.8/mage_ai/data_integrations/logger/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_integrations/logger/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2493 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_integrations/logger/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.708873 mage-ai-0.8.8/mage_ai/data_integrations/sources/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_integrations/sources/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      978 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_integrations/sources/constants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.712873 mage-ai-0.8.8/mage_ai/data_integrations/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_integrations/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4536 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_integrations/utils/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1502 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_integrations/utils/parsers.py
--rw-r--r--   0 runner    (1001) docker     (123)     7313 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_integrations/utils/scheduler.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.712873 mage-ai-0.8.8/mage_ai/data_preparation/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      648 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/decorators.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.712873 mage-ai-0.8.8/mage_ai/data_preparation/executors/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/executors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10392 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/executors/block_executor.py
--rw-r--r--   0 runner    (1001) docker     (123)     1483 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/executors/ecs_block_executor.py
--rw-r--r--   0 runner    (1001) docker     (123)     3037 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/executors/executor_factory.py
--rw-r--r--   0 runner    (1001) docker     (123)     1872 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/executors/gcp_cloud_run_block_executor.py
--rw-r--r--   0 runner    (1001) docker     (123)      643 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/executors/k8s_block_executor.py
--rw-r--r--   0 runner    (1001) docker     (123)     1276 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/executors/pipeline_executor.py
--rw-r--r--   0 runner    (1001) docker     (123)     3520 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/executors/pyspark_block_executor.py
--rw-r--r--   0 runner    (1001) docker     (123)     2806 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/executors/pyspark_pipeline_executor.py
--rw-r--r--   0 runner    (1001) docker     (123)     4901 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/executors/streaming_pipeline_executor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.712873 mage-ai-0.8.8/mage_ai/data_preparation/logging/
--rw-r--r--   0 runner    (1001) docker     (123)      452 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/logging/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2010 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/logging/gcs_logger_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     2206 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/logging/logger.py
--rw-r--r--   0 runner    (1001) docker     (123)     3706 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/logging/logger_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)      988 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/logging/logger_manager_factory.py
--rw-r--r--   0 runner    (1001) docker     (123)     1653 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/logging/s3_logger_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.712873 mage-ai-0.8.8/mage_ai/data_preparation/models/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.712873 mage-ai-0.8.8/mage_ai/data_preparation/models/block/
--rw-r--r--   0 runner    (1001) docker     (123)    73037 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      525 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/constants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.712873 mage-ai-0.8.8/mage_ai/data_preparation/models/block/dbt/
--rw-r--r--   0 runner    (1001) docker     (123)     6979 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/dbt/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.716873 mage-ai-0.8.8/mage_ai/data_preparation/models/block/dbt/utils/
--rw-r--r--   0 runner    (1001) docker     (123)    30295 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/dbt/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      119 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/errors.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.716873 mage-ai-0.8.8/mage_ai/data_preparation/models/block/integration/
--rw-r--r--   0 runner    (1001) docker     (123)    12306 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/integration/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.716873 mage-ai-0.8.8/mage_ai/data_preparation/models/block/r/
--rw-r--r--   0 runner    (1001) docker     (123)     4572 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/r/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.716873 mage-ai-0.8.8/mage_ai/data_preparation/models/block/r/templates/
--rw-r--r--   0 runner    (1001) docker     (123)      228 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/r/templates/data_exporter.jinja
--rw-r--r--   0 runner    (1001) docker     (123)      312 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/r/templates/data_loader.jinja
--rw-r--r--   0 runner    (1001) docker     (123)      307 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/r/templates/transformer.jinja
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.716873 mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/
--rw-r--r--   0 runner    (1001) docker     (123)    12301 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2486 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/bigquery.py
--rw-r--r--   0 runner    (1001) docker     (123)      935 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/mysql.py
--rw-r--r--   0 runner    (1001) docker     (123)      883 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/postgres.py
--rw-r--r--   0 runner    (1001) docker     (123)      926 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/redshift.py
--rw-r--r--   0 runner    (1001) docker     (123)     2591 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/snowflake.py
--rw-r--r--   0 runner    (1001) docker     (123)     3047 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/trino.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.716873 mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5675 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/utils/shared.py
--rw-r--r--   0 runner    (1001) docker     (123)    14543 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/block/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2115 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)      103 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)     4381 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/file.py
--rw-r--r--   0 runner    (1001) docker     (123)    34818 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/pipeline.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.716873 mage-ai-0.8.8/mage_ai/data_preparation/models/pipelines/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/pipelines/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13563 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/pipelines/integration_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)      237 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/pipelines/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1443 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    19496 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/variable.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.716873 mage-ai-0.8.8/mage_ai/data_preparation/models/widget/
--rw-r--r--   0 runner    (1001) docker     (123)     6839 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/widget/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5277 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/widget/charts.py
--rw-r--r--   0 runner    (1001) docker     (123)     1806 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/widget/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     3117 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/models/widget/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     5703 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/repo_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.716873 mage-ai-0.8.8/mage_ai/data_preparation/shared/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/shared/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       80 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/shared/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     1986 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/shared/secrets.py
--rw-r--r--   0 runner    (1001) docker     (123)      703 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/shared/stream.py
--rw-r--r--   0 runner    (1001) docker     (123)      485 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/shared/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.716873 mage-ai-0.8.8/mage_ai/data_preparation/storage/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/storage/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1737 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/storage/base_storage.py
--rw-r--r--   0 runner    (1001) docker     (123)     2571 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/storage/local_storage.py
--rw-r--r--   0 runner    (1001) docker     (123)     2958 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/storage/s3_storage.py
--rw-r--r--   0 runner    (1001) docker     (123)     2729 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/storage/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.720873 mage-ai-0.8.8/mage_ai/data_preparation/templates/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.720873 mage-ai-0.8.8/mage_ai/data_preparation/templates/callbacks/
--rw-r--r--   0 runner    (1001) docker     (123)      114 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/callbacks/default.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.676873 mage-ai-0.8.8/mage_ai/data_preparation/templates/custom/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.720873 mage-ai-0.8.8/mage_ai/data_preparation/templates/custom/python/
--rw-r--r--   0 runner    (1001) docker     (123)      399 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/custom/python/default.jinja
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.720873 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/
--rw-r--r--   0 runner    (1001) docker     (123)      919 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/azure_blob_storage.py
--rw-r--r--   0 runner    (1001) docker     (123)      937 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/bigquery.py
--rw-r--r--   0 runner    (1001) docker     (123)      458 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/default.jinja
--rw-r--r--   0 runner    (1001) docker     (123)      447 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/file.py
--rw-r--r--   0 runner    (1001) docker     (123)      949 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/google_cloud_storage.py
--rw-r--r--   0 runner    (1001) docker     (123)     1092 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/mysql.py
--rw-r--r--   0 runner    (1001) docker     (123)     1210 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/postgres.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.720873 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/pyspark/
--rw-r--r--   0 runner    (1001) docker     (123)      458 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/pyspark/default.jinja
--rw-r--r--   0 runner    (1001) docker     (123)      479 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/pyspark/s3.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.720873 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/r/
--rw-r--r--   0 runner    (1001) docker     (123)      132 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/r/default.jinja
--rw-r--r--   0 runner    (1001) docker     (123)      954 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/redshift.py
--rw-r--r--   0 runner    (1001) docker     (123)      847 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/s3.py
--rw-r--r--   0 runner    (1001) docker     (123)     1072 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/snowflake.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.720873 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/streaming/
--rw-r--r--   0 runner    (1001) docker     (123)       68 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/streaming/kinesis.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      469 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/streaming/opensearch.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.720873 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/
--rw-r--r--   0 runner    (1001) docker     (123)      391 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/api.py
--rw-r--r--   0 runner    (1001) docker     (123)      901 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/azure_blob_storage.py
--rw-r--r--   0 runner    (1001) docker     (123)      772 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/bigquery.py
--rw-r--r--   0 runner    (1001) docker     (123)      466 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/default.jinja
--rw-r--r--   0 runner    (1001) docker     (123)      582 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/file.py
--rw-r--r--   0 runner    (1001) docker     (123)      914 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/google_cloud_storage.py
--rw-r--r--   0 runner    (1001) docker     (123)      816 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/mysql.py
--rw-r--r--   0 runner    (1001) docker     (123)      843 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/postgres.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.720873 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/pyspark/
--rw-r--r--   0 runner    (1001) docker     (123)      461 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/pyspark/default.jinja
--rw-r--r--   0 runner    (1001) docker     (123)      567 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/pyspark/s3.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.720873 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/r/
--rw-r--r--   0 runner    (1001) docker     (123)      156 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/r/default.jinja
--rw-r--r--   0 runner    (1001) docker     (123)      815 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/redshift.py
--rw-r--r--   0 runner    (1001) docker     (123)      819 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/s3.py
--rw-r--r--   0 runner    (1001) docker     (123)      850 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/snowflake.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/streaming/
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/streaming/azure_event_hub.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      499 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/streaming/kafka.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       65 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/streaming/kinesis.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      303 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/streaming/rabbitmq.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/pipeline/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/pipeline/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       43 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/pipeline/metadata.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/pipeline_execution/
--rw-r--r--   0 runner    (1001) docker     (123)      703 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/pipeline_execution/emr_bootstrap.sh
--rw-r--r--   0 runner    (1001) docker     (123)     2665 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/pipeline_execution/spark_script.jinja
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/charts/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/charts/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/data_exporters/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/data_exporters/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      460 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/data_exporters/export_titanic_clean.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/data_loaders/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/data_loaders/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      722 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/data_loaders/load_titanic.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/dbt/
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/dbt/profiles.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2040 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/io_config.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      975 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/metadata.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/pipelines/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/pipelines/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/pipelines/example_pipeline/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/pipelines/example_pipeline/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      705 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/pipelines/example_pipeline/metadata.yaml
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/requirements.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/scratchpads/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/scratchpads/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/transformers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/transformers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1320 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/transformers/fill_in_missing_values.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/utils/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/sensors/
--rw-r--r--   0 runner    (1001) docker     (123)      474 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/sensors/default.py
--rw-r--r--   0 runner    (1001) docker     (123)      677 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/sensors/s3.py
--rw-r--r--   0 runner    (1001) docker     (123)     9132 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/template.py
--rw-r--r--   0 runner    (1001) docker     (123)      333 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/testable.jinja
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/
--rw-r--r--   0 runner    (1001) docker     (123)     1171 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/data_warehouse_transformer.jinja
--rw-r--r--   0 runner    (1001) docker     (123)      692 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/default.jinja
--rw-r--r--   0 runner    (1001) docker     (123)      692 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/default_pyspark.jinja
--rw-r--r--   0 runner    (1001) docker     (123)      438 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/default_streaming.jinja
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/r/
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/r/default.r
--rw-r--r--   0 runner    (1001) docker     (123)      561 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/suggestion_fmt.jinja
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.724873 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/
--rw-r--r--   0 runner    (1001) docker     (123)      731 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/action.jinja
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.728873 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/
--rw-r--r--   0 runner    (1001) docker     (123)      774 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/average.py
--rw-r--r--   0 runner    (1001) docker     (123)      413 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/clean_column_name.py
--rw-r--r--   0 runner    (1001) docker     (123)      756 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/count.py
--rw-r--r--   0 runner    (1001) docker     (123)      774 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/count_distinct.py
--rw-r--r--   0 runner    (1001) docker     (123)      573 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/diff.py
--rw-r--r--   0 runner    (1001) docker     (123)      758 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/first.py
--rw-r--r--   0 runner    (1001) docker     (123)      546 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/fix_syntax_errors.py
--rw-r--r--   0 runner    (1001) docker     (123)      646 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/impute.py
--rw-r--r--   0 runner    (1001) docker     (123)      756 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/last.py
--rw-r--r--   0 runner    (1001) docker     (123)     1167 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/max.py
--rw-r--r--   0 runner    (1001) docker     (123)      772 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/median.py
--rw-r--r--   0 runner    (1001) docker     (123)      766 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/min.py
--rw-r--r--   0 runner    (1001) docker     (123)      467 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/normalize.py
--rw-r--r--   0 runner    (1001) docker     (123)      479 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/reformat.py
--rw-r--r--   0 runner    (1001) docker     (123)      408 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/remove.py
--rw-r--r--   0 runner    (1001) docker     (123)      677 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/remove_outliers.py
--rw-r--r--   0 runner    (1001) docker     (123)      416 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/select.py
--rw-r--r--   0 runner    (1001) docker     (123)      605 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/shift_down.py
--rw-r--r--   0 runner    (1001) docker     (123)      565 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/shift_up.py
--rw-r--r--   0 runner    (1001) docker     (123)      506 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/standardize.py
--rw-r--r--   0 runner    (1001) docker     (123)      766 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/sum.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.728873 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/row/
--rw-r--r--   0 runner    (1001) docker     (123)      543 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/row/drop_duplicate.py
--rw-r--r--   0 runner    (1001) docker     (123)      406 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/row/filter.py
--rw-r--r--   0 runner    (1001) docker     (123)      418 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/row/remove.py
--rw-r--r--   0 runner    (1001) docker     (123)      434 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/row/sort.py
--rw-r--r--   0 runner    (1001) docker     (123)     1951 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/templates/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.728873 mage-ai-0.8.8/mage_ai/data_preparation/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/utils/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.728873 mage-ai-0.8.8/mage_ai/data_preparation/utils/block/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/utils/block/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2831 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/utils/block/convert_content.py
--rw-r--r--   0 runner    (1001) docker     (123)    11944 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/data_preparation/variable_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.728873 mage-ai-0.8.8/mage_ai/errors/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/errors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       45 2023-02-26 17:54:33.000000 mage-ai-0.8.8/mage_ai/errors/base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.732873 mage-ai-0.8.8/mage_ai/io/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4569 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/azure_blob_storage.py
--rw-r--r--   0 runner    (1001) docker     (123)    10680 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    14957 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/bigquery.py
--rw-r--r--   0 runner    (1001) docker     (123)    14862 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     3272 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/export_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2564 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/file.py
--rw-r--r--   0 runner    (1001) docker     (123)     6636 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/google_cloud_storage.py
--rw-r--r--   0 runner    (1001) docker     (123)     1302 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/io_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     4585 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/mysql.py
--rw-r--r--   0 runner    (1001) docker     (123)     7513 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/postgres.py
--rw-r--r--   0 runner    (1001) docker     (123)    13408 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/redshift.py
--rw-r--r--   0 runner    (1001) docker     (123)     5800 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/s3.py
--rw-r--r--   0 runner    (1001) docker     (123)    10665 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/snowflake.py
--rw-r--r--   0 runner    (1001) docker     (123)    10075 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/sql.py
--rw-r--r--   0 runner    (1001) docker     (123)     9322 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/trino.py
--rw-r--r--   0 runner    (1001) docker     (123)      653 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/io/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.732873 mage-ai-0.8.8/mage_ai/orchestration/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2797 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/airflow.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.732873 mage-ai-0.8.8/mage_ai/orchestration/backfills/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/backfills/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3872 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/backfills/service.py
--rw-r--r--   0 runner    (1001) docker     (123)      126 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/constants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.732873 mage-ai-0.8.8/mage_ai/orchestration/db/
--rw-r--r--   0 runner    (1001) docker     (123)     2783 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3262 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/alembic.ini
--rw-r--r--   0 runner    (1001) docker     (123)      960 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/database_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)      406 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/errors.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.732873 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/
--rw-r--r--   0 runner    (1001) docker     (123)      264 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     2836 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/env.py
--rw-r--r--   0 runner    (1001) docker     (123)      510 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/script.py.mako
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.736873 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/
--rw-r--r--   0 runner    (1001) docker     (123)      859 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/053ee2c10d85_add_completed_at.py
--rw-r--r--   0 runner    (1001) docker     (123)      699 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/067326f43bc3_add_variables_to_pipelinerun.py
--rw-r--r--   0 runner    (1001) docker     (123)      711 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/1d8e65aeefdd_add_settings_to_pipeline_schedule.py
--rw-r--r--   0 runner    (1001) docker     (123)     1172 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/1f9353eddbc6_add_secrets_table.py
--rw-r--r--   0 runner    (1001) docker     (123)     1124 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/2266370f589b_add_indexes_to_pipeline_run.py
--rw-r--r--   0 runner    (1001) docker     (123)     2579 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/26305e46df52_create_backfills_table.py
--rw-r--r--   0 runner    (1001) docker     (123)     1607 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/3fafd217efa7_add_event_matcher_model.py
--rw-r--r--   0 runner    (1001) docker     (123)      715 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/52ab80005742_add_variables_to_pipeline_schedule.py
--rw-r--r--   0 runner    (1001) docker     (123)      705 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/5cd59ec4cf1d_add_passed_sla_to_pipeline_run.py
--rw-r--r--   0 runner    (1001) docker     (123)     1668 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/643b6e65e814_add_unique_indexes_on_authentication_.py
--rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/6aecc9bc451c_update_schedule_type_enum.py
--rw-r--r--   0 runner    (1001) docker     (123)      915 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/7ac6fed06918_add_token_column_to_pipeline_schedule_.py
--rw-r--r--   0 runner    (1001) docker     (123)      699 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/84de4cdd6126_add_sla_to_pipeline_schedule.py
--rw-r--r--   0 runner    (1001) docker     (123)      859 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/8971d4cd5b39_add_event_variables_and_metadata_to_.py
--rw-r--r--   0 runner    (1001) docker     (123)     3375 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/97ff9f55a3c0_create_users_oauth2_applications_and_.py
--rw-r--r--   0 runner    (1001) docker     (123)      710 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/b01be687e537_add_started_at_to_block_run.py
--rw-r--r--   0 runner    (1001) docker     (123)     3024 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/c07a23ff782b_add_initial_tables.py
--rw-r--r--   0 runner    (1001) docker     (123)      685 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/ec5df57a1c60_add_metrics_to_block_runs.py
--rw-r--r--   0 runner    (1001) docker     (123)    23745 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/models.py
--rw-r--r--   0 runner    (1001) docker     (123)      604 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/db/process.py
--rw-r--r--   0 runner    (1001) docker     (123)     3817 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/execution_process_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     1514 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/job_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.736873 mage-ai-0.8.8/mage_ai/orchestration/metrics/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/metrics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5553 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/metrics/pipeline_run.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.736873 mage-ai-0.8.8/mage_ai/orchestration/monitor/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/monitor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8352 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/monitor/monitor_stats.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.736873 mage-ai-0.8.8/mage_ai/orchestration/notification/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/notification/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2269 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/notification/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     4086 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/notification/sender.py
--rw-r--r--   0 runner    (1001) docker     (123)    33167 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/pipeline_scheduler.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.736873 mage-ai-0.8.8/mage_ai/orchestration/queue/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/queue/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      691 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/queue/celery_queue.py
--rw-r--r--   0 runner    (1001) docker     (123)      293 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/queue/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     3393 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/queue/process_queue.py
--rw-r--r--   0 runner    (1001) docker     (123)      472 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/queue/queue.py
--rw-r--r--   0 runner    (1001) docker     (123)      717 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/queue/queue_factory.py
--rw-r--r--   0 runner    (1001) docker     (123)     2405 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/run_status_checker.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.736873 mage-ai-0.8.8/mage_ai/orchestration/triggers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/triggers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      208 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/triggers/event_trigger.py
--rw-r--r--   0 runner    (1001) docker     (123)      439 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/triggers/loop_time_trigger.py
--rw-r--r--   0 runner    (1001) docker     (123)      382 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/triggers/time_trigger.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.736873 mage-ai-0.8.8/mage_ai/orchestration/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      636 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/orchestration/utils/resources.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.744873 mage-ai-0.8.8/mage_ai/sample_datasets/
--rw-r--r--   0 runner    (1001) docker     (123)      789 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/sample_datasets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   872940 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/sample_datasets/product_purchases.csv
--rw-r--r--   0 runner    (1001) docker     (123)  5385107 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/sample_datasets/salary_survey.csv
--rw-r--r--   0 runner    (1001) docker     (123)    60302 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/sample_datasets/titanic_survival.csv
--rw-r--r--   0 runner    (1001) docker     (123)   258700 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/sample_datasets/user_emails.csv
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.744873 mage-ai-0.8.8/mage_ai/server/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2129 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/active_kernel.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.748873 mage-ai-0.8.8/mage_ai/server/api/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3660 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/api/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1697 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/api/blocks.py
--rw-r--r--   0 runner    (1001) docker     (123)     7042 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/api/clusters.py
--rw-r--r--   0 runner    (1001) docker     (123)      172 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/api/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)      119 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/api/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)     2096 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/api/events.py
--rw-r--r--   0 runner    (1001) docker     (123)     1683 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/api/integration_sources.py
--rw-r--r--   0 runner    (1001) docker     (123)      946 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/api/projects.py
--rw-r--r--   0 runner    (1001) docker     (123)     2471 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/api/triggers.py
--rw-r--r--   0 runner    (1001) docker     (123)     1822 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/api/v1.py
--rw-r--r--   0 runner    (1001) docker     (123)    13229 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/app.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.748873 mage-ai-0.8.8/mage_ai/server/client/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/client/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2719 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/client/mage.py
--rw-r--r--   0 runner    (1001) docker     (123)      420 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/constants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.748873 mage-ai-0.8.8/mage_ai/server/data/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/data/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3827 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/data/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     9281 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/data/models.py
--rw-r--r--   0 runner    (1001) docker     (123)      618 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/docs_server.py
--rw-r--r--   0 runner    (1001) docker     (123)     2746 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/execution_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.748873 mage-ai-0.8.8/mage_ai/server/frontend_dist/
--rw-r--r--   0 runner    (1001) docker     (123)     8646 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/404.html
--rw-r--r--   0 runner    (1001) docker     (123)     8646 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/404.html.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.680873 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.680873 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.748873 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/7JlKIxz5l4mwJx6uj5--5/
--rw-r--r--   0 runner    (1001) docker     (123)     5190 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js
--rw-r--r--   0 runner    (1001) docker     (123)       92 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js
--rw-r--r--   0 runner    (1001) docker     (123)       77 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.768873 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/
--rw-r--r--   0 runner    (1001) docker     (123)     3531 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/1150.1378afaa474df64a.js
--rw-r--r--   0 runner    (1001) docker     (123)     6458 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/1240.0819f45820d22263.js
--rw-r--r--   0 runner    (1001) docker     (123)    32475 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/1286-a62050b3f897c6be.js
--rw-r--r--   0 runner    (1001) docker     (123)     5290 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/1450.d383f64c169d4278.js
--rw-r--r--   0 runner    (1001) docker     (123)     8652 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/1774-aa51ef1da7217ff9.js
--rw-r--r--   0 runner    (1001) docker     (123)    13323 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/1830-cb1bbbf9a9c54649.js
--rw-r--r--   0 runner    (1001) docker     (123)    60381 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2083-78a438dbdc57d1e4.js
--rw-r--r--   0 runner    (1001) docker     (123)    69805 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2125-0b537dc53fe71b18.js
--rw-r--r--   0 runner    (1001) docker     (123)    14082 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2249-70929b8c547bbc18.js
--rw-r--r--   0 runner    (1001) docker     (123)    14489 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2426-be3e2bc6625de582.js
--rw-r--r--   0 runner    (1001) docker     (123)     2942 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2481.0454a0e25dc7e027.js
--rw-r--r--   0 runner    (1001) docker     (123)     1649 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2508.724531e7f9cf5f36.js
--rw-r--r--   0 runner    (1001) docker     (123)   791202 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2524-6aeb9419acf5d1b4.js
--rw-r--r--   0 runner    (1001) docker     (123)     3432 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2545.8371b39c898ae92b.js
--rw-r--r--   0 runner    (1001) docker     (123)    10519 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/261.0a24b4ece1d29aa1.js
--rw-r--r--   0 runner    (1001) docker     (123)     2226 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/266.e301071d22592682.js
--rw-r--r--   0 runner    (1001) docker     (123)     9689 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2714-1e79e9f2e998b544.js
--rw-r--r--   0 runner    (1001) docker     (123)    71691 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/29107295-989a0767a635d9d5.js
--rw-r--r--   0 runner    (1001) docker     (123)     3524 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/3453.992f4b1667e9882c.js
--rw-r--r--   0 runner    (1001) docker     (123)     1618 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/3467.38cd0654ba6f788f.js
--rw-r--r--   0 runner    (1001) docker     (123)    30652 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/3835.df296b4e4078e985.js
--rw-r--r--   0 runner    (1001) docker     (123)    46702 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/3850-6395783d820def1c.js
--rw-r--r--   0 runner    (1001) docker     (123)   243728 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/3873.4b3eace753998412.js
--rw-r--r--   0 runner    (1001) docker     (123)     4171 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/3898.880191695bb05845.js
--rw-r--r--   0 runner    (1001) docker     (123)     1428 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4042.5e16d36209052351.js
--rw-r--r--   0 runner    (1001) docker     (123)     3421 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4092.536ee541241f4538.js
--rw-r--r--   0 runner    (1001) docker     (123)    12971 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/434-69ddfacd3e93f2db.js
--rw-r--r--   0 runner    (1001) docker     (123)     6457 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4388.04098706f32e69e7.js
--rw-r--r--   0 runner    (1001) docker     (123)     1122 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/440.3ab77942f659ea0c.js
--rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4450.79f14f763d55c63e.js
--rw-r--r--   0 runner    (1001) docker     (123)     2243 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4454.13a2404adecaa39e.js
--rw-r--r--   0 runner    (1001) docker     (123)    13231 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4463-1b9ce74c6e1bb14e.js
--rw-r--r--   0 runner    (1001) docker     (123)    57586 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4495-4f0340aa82e0c623.js
--rw-r--r--   0 runner    (1001) docker     (123)     2720 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4776.753ad29fa0a29a4a.js
--rw-r--r--   0 runner    (1001) docker     (123)    95131 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4804-01a10103ebe26ca8.js
--rw-r--r--   0 runner    (1001) docker     (123)    15512 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4846-b4ced91dc0e9fba9.js
--rw-r--r--   0 runner    (1001) docker     (123)     2310 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4883.a5bb0edbf8f3cc8f.js
--rw-r--r--   0 runner    (1001) docker     (123)    17422 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5008.29c2662ecc2b04c7.js
--rw-r--r--   0 runner    (1001) docker     (123)     2135 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5104.1edcf4437c471dd4.js
--rw-r--r--   0 runner    (1001) docker     (123)     1816 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5164.857023e800905b6f.js
--rw-r--r--   0 runner    (1001) docker     (123)     3490 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5729.0f2748e9e6dab951.js
--rw-r--r--   0 runner    (1001) docker     (123)     3479 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5824.628653557e904674.js
--rw-r--r--   0 runner    (1001) docker     (123)   105056 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5872-103815a4a043489b.js
--rw-r--r--   0 runner    (1001) docker     (123)    91825 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5896-f84e336fb8877027.js
--rw-r--r--   0 runner    (1001) docker     (123)    13407 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5944-757b7898608a65e1.js
--rw-r--r--   0 runner    (1001) docker     (123)     1867 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6042.c59010de9e699437.js
--rw-r--r--   0 runner    (1001) docker     (123)    18793 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6085-692d2f784c0504f2.js
--rw-r--r--   0 runner    (1001) docker     (123)     2203 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6115.0c85e507543394ea.js
--rw-r--r--   0 runner    (1001) docker     (123)    17641 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6116.871a682ddf535aca.js
--rw-r--r--   0 runner    (1001) docker     (123)     1467 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6434.10380ee0968636ba.js
--rw-r--r--   0 runner    (1001) docker     (123)     2315 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6443.7b6d2b4e51018184.js
--rw-r--r--   0 runner    (1001) docker     (123)    24930 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6507.d3a17777d2c294e6.js
--rw-r--r--   0 runner    (1001) docker     (123)    16709 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6532-a614f9e1f9434872.js
--rw-r--r--   0 runner    (1001) docker     (123)    18067 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6579-2b5d8d39472d85c0.js
--rw-r--r--   0 runner    (1001) docker     (123)    11627 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6641-a0ed2bd8f5dc777b.js
--rw-r--r--   0 runner    (1001) docker     (123)     2766 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6958.8f39c585d36737a7.js
--rw-r--r--   0 runner    (1001) docker     (123)    23228 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/7011-81dd8269c4806d26.js
--rw-r--r--   0 runner    (1001) docker     (123)    16617 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/704-4de8946d753a578a.js
--rw-r--r--   0 runner    (1001) docker     (123)  1409747 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/72fdc299.2d5ec188af5d0049.js
--rw-r--r--   0 runner    (1001) docker     (123)     3506 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/739.3d24945544b37e52.js
--rw-r--r--   0 runner    (1001) docker     (123)    16874 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/7400-1430ec3874c1fdee.js
--rw-r--r--   0 runner    (1001) docker     (123)     5292 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/792.010ca00d79b2112f.js
--rw-r--r--   0 runner    (1001) docker     (123)     1129 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/7947.77be4bec4d47774e.js
--rw-r--r--   0 runner    (1001) docker     (123)     1867 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/7951.fee8b6c27c9ef777.js
--rw-r--r--   0 runner    (1001) docker     (123)     4838 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8018.968bf87c390e3312.js
--rw-r--r--   0 runner    (1001) docker     (123)     2166 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8097.b0345f30a7390c1d.js
--rw-r--r--   0 runner    (1001) docker     (123)    12094 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8256.290ceb269b1ffe26.js
--rw-r--r--   0 runner    (1001) docker     (123)     3939 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/826.75268ee34f93393a.js
--rw-r--r--   0 runner    (1001) docker     (123)     1783 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8277.5003e1d94bb85156.js
--rw-r--r--   0 runner    (1001) docker     (123)     3479 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8762.dff300f86bef8573.js
--rw-r--r--   0 runner    (1001) docker     (123)    15534 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8789-4f858e520d46973b.js
--rw-r--r--   0 runner    (1001) docker     (123)     5003 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8807.a68c69c8fe0a8c01.js
--rw-r--r--   0 runner    (1001) docker     (123)     3020 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8849.db0d50b4d84b09a6.js
--rw-r--r--   0 runner    (1001) docker     (123)     4240 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8901.21d26d5a1ee473fe.js
--rw-r--r--   0 runner    (1001) docker     (123)     9937 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8920.5700e380a2999098.js
--rw-r--r--   0 runner    (1001) docker     (123)    16976 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8961-697fe5d4db44d909.js
--rw-r--r--   0 runner    (1001) docker     (123)    17386 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9140-6f67e0879394373d.js
--rw-r--r--   0 runner    (1001) docker     (123)     8406 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9258.6c6ef544c701a011.js
--rw-r--r--   0 runner    (1001) docker     (123)     2131 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9307.d4baf7aebbcef1f0.js
--rw-r--r--   0 runner    (1001) docker     (123)     1867 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9361.a0820e3069f5ef74.js
--rw-r--r--   0 runner    (1001) docker     (123)     5350 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9363.6b811b4c86277e07.js
--rw-r--r--   0 runner    (1001) docker     (123)     1655 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9437.a3c32f45cf9ef69b.js
--rw-r--r--   0 runner    (1001) docker     (123)     8443 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9565-28e1c30511c95c2d.js
--rw-r--r--   0 runner    (1001) docker     (123)     1963 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9566.f8bd24768ed14ecb.js
--rw-r--r--   0 runner    (1001) docker     (123)     3826 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9633.40e5056ca1e2b22a.js
--rw-r--r--   0 runner    (1001) docker     (123)    66714 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9767-3f852fd90cf7857f.js
--rw-r--r--   0 runner    (1001) docker     (123)     1428 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9785.5ff26cb26d84d6a1.js
--rw-r--r--   0 runner    (1001) docker     (123)    12357 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9832-c8b8970bb522f302.js
--rw-r--r--   0 runner    (1001) docker     (123)     3480 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9855.c4394a68322be9f8.js
--rw-r--r--   0 runner    (1001) docker     (123)    14948 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9898-51ca6a904b7a2382.js
--rw-r--r--   0 runner    (1001) docker     (123)     3030 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9927.e82a3e1e21990d77.js
--rw-r--r--   0 runner    (1001) docker     (123)   110731 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/bd1a647f.6050372acaa5cc3c.js
--rw-r--r--   0 runner    (1001) docker     (123)   140771 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/framework-7c365855dab1bf41.js
--rw-r--r--   0 runner    (1001) docker     (123)   102188 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/main-bb0dd5375146d7fd.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.772873 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/
--rw-r--r--   0 runner    (1001) docker     (123)   332649 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/_app-0aed65f2e085822e.js
--rw-r--r--   0 runner    (1001) docker     (123)     3190 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/_error-235304e5badb19eb.js
--rw-r--r--   0 runner    (1001) docker     (123)      636 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/index-e34a68d2f6fe16f2.js
--rw-r--r--   0 runner    (1001) docker     (123)    43508 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/manage-54fd0434f4f5305c.js
--rw-r--r--   0 runner    (1001) docker     (123)     9352 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipeline-runs-21fe37061bdaaaea.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.776873 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.776873 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.776873 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/backfills/
--rw-r--r--   0 runner    (1001) docker     (123)    27512 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/backfills/[...slug]-81e3c9ea75d7abb4.js
--rw-r--r--   0 runner    (1001) docker     (123)    25680 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/backfills-0ed0d70bc659c236.js
--rw-r--r--   0 runner    (1001) docker     (123)   335648 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/edit-1b8b406222fae908.js
--rw-r--r--   0 runner    (1001) docker     (123)    34280 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/logs-5ccc75887776efb0.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.780873 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/monitors/
--rw-r--r--   0 runner    (1001) docker     (123)    13594 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/monitors/block-runs-8f23f7ca9efcb069.js
--rw-r--r--   0 runner    (1001) docker     (123)    11953 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/monitors/block-runtime-f83ab9de4094e1b0.js
--rw-r--r--   0 runner    (1001) docker     (123)      345 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/monitors-8b08ec1aef4af4f2.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.780873 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/runs/
--rw-r--r--   0 runner    (1001) docker     (123)    17156 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/runs/[run]-73ced07cc98a4968.js
--rw-r--r--   0 runner    (1001) docker     (123)    13088 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/runs-67d23509a0c9a1b8.js
--rw-r--r--   0 runner    (1001) docker     (123)    44763 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/syncs-4084a44baf91f30e.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.780873 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/triggers/
--rw-r--r--   0 runner    (1001) docker     (123)    39151 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/triggers/[...slug]-ae970171cfe98c51.js
--rw-r--r--   0 runner    (1001) docker     (123)    36826 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/triggers-b0b91245d3299bdf.js
--rw-r--r--   0 runner    (1001) docker     (123)     4526 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]-ca9457e1a6bced4b.js
--rw-r--r--   0 runner    (1001) docker     (123)    21520 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines-12dc02ae431a6305.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.680873 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.780873 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/account/
--rw-r--r--   0 runner    (1001) docker     (123)     4003 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/account/profile-acd7ee47219fee3d.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.780873 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/workspace/
--rw-r--r--   0 runner    (1001) docker     (123)     9191 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/workspace/preferences-07bda506f68974fb.js
--rw-r--r--   0 runner    (1001) docker     (123)    10903 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/workspace/users-c128672e053a4c30.js
--rw-r--r--   0 runner    (1001) docker     (123)     4347 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings-d594a66a568306da.js
--rw-r--r--   0 runner    (1001) docker     (123)    16326 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/sign-in-b4e1eb529a184c60.js
--rw-r--r--   0 runner    (1001) docker     (123)    11068 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/terminal-5d7c45bb058a3f20.js
--rw-r--r--   0 runner    (1001) docker     (123)     4306 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/test-f567bdfcc1276249.js
--rw-r--r--   0 runner    (1001) docker     (123)    19885 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/triggers-e0172c422c95eda9.js
--rw-r--r--   0 runner    (1001) docker     (123)    91434 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/polyfills-5cd94c89d3acac5f.js
--rw-r--r--   0 runner    (1001) docker     (123)     5196 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.780873 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/css/
--rw-r--r--   0 runner    (1001) docker     (123)    15565 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/css/d1e8e64d0b07af2f.css
--rw-r--r--   0 runner    (1001) docker     (123)    15406 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/favicon.ico
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.680873 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.680873 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Fira_Code/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.784873 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/
--rw-r--r--   0 runner    (1001) docker     (123)   319368 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Bold.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   288380 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Light.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   283684 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Medium.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   289624 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Regular.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   285428 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Retina.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   304248 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-SemiBold.ttf
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.788873 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/
--rw-r--r--   0 runner    (1001) docker     (123)    11560 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)   168060 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Black.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   174108 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-BlackItalic.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   167336 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Bold.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   171508 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-BoldItalic.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   170504 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Italic.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   167000 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Light.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   173172 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-LightItalic.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   168644 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Medium.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   173416 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-MediumItalic.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   168260 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Regular.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   168488 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Thin.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   172860 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-ThinItalic.ttf
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.788873 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/
--rw-r--r--   0 runner    (1001) docker     (123)    11560 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)     2552 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/README.txt
--rw-r--r--   0 runner    (1001) docker     (123)   195012 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/RobotoMono-Italic-VariableFont_wght.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   182172 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/RobotoMono-VariableFont_wght.ttf
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.792873 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/
--rw-r--r--   0 runner    (1001) docker     (123)    87008 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Bold.ttf
--rw-r--r--   0 runner    (1001) docker     (123)    94148 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-BoldItalic.ttf
--rw-r--r--   0 runner    (1001) docker     (123)    87788 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-ExtraLight.ttf
--rw-r--r--   0 runner    (1001) docker     (123)    93408 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-ExtraLightItalic.ttf
--rw-r--r--   0 runner    (1001) docker     (123)    93904 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Italic.ttf
--rw-r--r--   0 runner    (1001) docker     (123)    87592 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Light.ttf
--rw-r--r--   0 runner    (1001) docker     (123)    93760 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-LightItalic.ttf
--rw-r--r--   0 runner    (1001) docker     (123)    86820 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Medium.ttf
--rw-r--r--   0 runner    (1001) docker     (123)    93948 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-MediumItalic.ttf
--rw-r--r--   0 runner    (1001) docker     (123)    86908 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Regular.ttf
--rw-r--r--   0 runner    (1001) docker     (123)    87076 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-SemiBold.ttf
--rw-r--r--   0 runner    (1001) docker     (123)    93940 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-SemiBoldItalic.ttf
--rw-r--r--   0 runner    (1001) docker     (123)    87872 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Thin.ttf
--rw-r--r--   0 runner    (1001) docker     (123)    93056 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-ThinItalic.ttf
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.792873 mage-ai-0.8.8/mage_ai/server/frontend_dist/images/
--rw-r--r--   0 runner    (1001) docker     (123)     4404 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/images/backfill.jpg
--rw-r--r--   0 runner    (1001) docker     (123)     4854 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/images/banner-shape-purple-peach.jpg
--rw-r--r--   0 runner    (1001) docker     (123)    57024 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/images/dashboard-api-key.webp
--rw-r--r--   0 runner    (1001) docker     (123)     5150 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/images/extra.jpg
--rw-r--r--   0 runner    (1001) docker     (123)     6969 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/images/monitor.jpg
--rw-r--r--   0 runner    (1001) docker     (123)     6850 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/images/run B.jpg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.792873 mage-ai-0.8.8/mage_ai/server/frontend_dist/images/sessions/
--rw-r--r--   0 runner    (1001) docker     (123)   256616 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/images/sessions/abstract.png
--rw-r--r--   0 runner    (1001) docker     (123)     7408 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/index.html
--rw-r--r--   0 runner    (1001) docker     (123)     9081 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/manage.html
--rw-r--r--   0 runner    (1001) docker     (123)     9369 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipeline-runs.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.792873 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.792873 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.792873 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/backfills/
--rw-r--r--   0 runner    (1001) docker     (123)    10273 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/backfills/[...slug].html
--rw-r--r--   0 runner    (1001) docker     (123)     9327 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/backfills.html
--rw-r--r--   0 runner    (1001) docker     (123)     9432 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/edit.html
--rw-r--r--   0 runner    (1001) docker     (123)     9785 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/logs.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.792873 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/monitors/
--rw-r--r--   0 runner    (1001) docker     (123)     9737 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/monitors/block-runs.html
--rw-r--r--   0 runner    (1001) docker     (123)     9903 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/monitors/block-runtime.html
--rw-r--r--   0 runner    (1001) docker     (123)     9637 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/monitors.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.792873 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/runs/
--rw-r--r--   0 runner    (1001) docker     (123)    10052 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/runs/[run].html
--rw-r--r--   0 runner    (1001) docker     (123)     9941 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/runs.html
--rw-r--r--   0 runner    (1001) docker     (123)     9397 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/syncs.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.792873 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/triggers/
--rw-r--r--   0 runner    (1001) docker     (123)    10349 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/triggers/[...slug].html
--rw-r--r--   0 runner    (1001) docker     (123)     9949 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/triggers.html
--rw-r--r--   0 runner    (1001) docker     (123)     7522 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline].html
--rw-r--r--   0 runner    (1001) docker     (123)     9201 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.684873 mage-ai-0.8.8/mage_ai/server/frontend_dist/settings/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.792873 mage-ai-0.8.8/mage_ai/server/frontend_dist/settings/account/
--rw-r--r--   0 runner    (1001) docker     (123)     9308 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/settings/account/profile.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.792873 mage-ai-0.8.8/mage_ai/server/frontend_dist/settings/workspace/
--rw-r--r--   0 runner    (1001) docker     (123)     9164 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/settings/workspace/preferences.html
--rw-r--r--   0 runner    (1001) docker     (123)     9308 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/settings/workspace/users.html
--rw-r--r--   0 runner    (1001) docker     (123)     7480 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/settings.html
--rw-r--r--   0 runner    (1001) docker     (123)    18393 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/sign-in.html
--rw-r--r--   0 runner    (1001) docker     (123)     9276 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/terminal.html
--rw-r--r--   0 runner    (1001) docker     (123)     7831 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/test.html
--rw-r--r--   0 runner    (1001) docker     (123)     9198 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/triggers.html
--rw-r--r--   0 runner    (1001) docker     (123)     1101 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/frontend_dist/vercel.svg
--rw-r--r--   0 runner    (1001) docker     (123)     2113 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/kernel_output_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)      787 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/kernels.py
--rw-r--r--   0 runner    (1001) docker     (123)     2030 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/scheduler_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)    12393 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/server.py
--rw-r--r--   0 runner    (1001) docker     (123)      659 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/subscriber.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.796873 mage-ai-0.8.8/mage_ai/server/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3295 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/utils/frontend_renderer.py
--rw-r--r--   0 runner    (1001) docker     (123)    11417 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/utils/output_display.py
--rw-r--r--   0 runner    (1001) docker     (123)    16870 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/server/websocket_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.796873 mage-ai-0.8.8/mage_ai/services/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.796873 mage-ai-0.8.8/mage_ai/services/airbyte/
--rw-r--r--   0 runner    (1001) docker     (123)     2876 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/airbyte/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3416 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/airbyte/client.py
--rw-r--r--   0 runner    (1001) docker     (123)      289 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/airbyte/config.py
--rw-r--r--   0 runner    (1001) docker     (123)      216 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/airbyte/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)      273 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/airbyte/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)      827 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/airbyte/server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.796873 mage-ai-0.8.8/mage_ai/services/aws/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.796873 mage-ai-0.8.8/mage_ai/services/aws/ecs/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/ecs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3168 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/ecs/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1285 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/ecs/ecs.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.796873 mage-ai-0.8.8/mage_ai/services/aws/emr/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/emr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3392 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/emr/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     9519 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/emr/emr.py
--rw-r--r--   0 runner    (1001) docker     (123)     7203 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/emr/emr_basics.py
--rw-r--r--   0 runner    (1001) docker     (123)     1117 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/emr/launcher.py
--rw-r--r--   0 runner    (1001) docker     (123)     1267 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/emr/resource_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.796873 mage-ai-0.8.8/mage_ai/services/aws/events/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/events/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1986 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/events/events.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.796873 mage-ai-0.8.8/mage_ai/services/aws/s3/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/s3/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2633 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/s3/s3.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.796873 mage-ai-0.8.8/mage_ai/services/aws/secrets_manager/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/secrets_manager/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1073 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/aws/secrets_manager/secrets_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.796873 mage-ai-0.8.8/mage_ai/services/datadog/
--rw-r--r--   0 runner    (1001) docker     (123)     2789 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/datadog/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.800873 mage-ai-0.8.8/mage_ai/services/dbt/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/dbt/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      160 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/dbt/config.py
--rw-r--r--   0 runner    (1001) docker     (123)      301 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/dbt/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     7529 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/dbt/dbt.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.800873 mage-ai-0.8.8/mage_ai/services/email/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/email/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      439 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/email/config.py
--rw-r--r--   0 runner    (1001) docker     (123)      658 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/email/email.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.800873 mage-ai-0.8.8/mage_ai/services/gcp/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/gcp/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.800873 mage-ai-0.8.8/mage_ai/services/gcp/cloud_run/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/gcp/cloud_run/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2694 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/gcp/cloud_run/cloud_run.py
--rw-r--r--   0 runner    (1001) docker     (123)      214 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/gcp/cloud_run/config.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.800873 mage-ai-0.8.8/mage_ai/services/hightouch/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/hightouch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      144 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/hightouch/config.py
--rw-r--r--   0 runner    (1001) docker     (123)      529 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/hightouch/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     3706 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/hightouch/hightouch.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.800873 mage-ai-0.8.8/mage_ai/services/k8s/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/k8s/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      106 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/k8s/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     4127 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/k8s/job_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.804873 mage-ai-0.8.8/mage_ai/services/metaplane/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/metaplane/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      211 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/metaplane/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     4594 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/metaplane/metaplane.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.804873 mage-ai-0.8.8/mage_ai/services/slack/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/slack/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      273 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/slack/config.py
--rw-r--r--   0 runner    (1001) docker     (123)      244 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/slack/slack.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.804873 mage-ai-0.8.8/mage_ai/services/stitch/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/stitch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      287 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/stitch/config.py
--rw-r--r--   0 runner    (1001) docker     (123)      123 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/stitch/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     8782 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/stitch/stitch.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.804873 mage-ai-0.8.8/mage_ai/services/teams/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/teams/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      273 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/teams/config.py
--rw-r--r--   0 runner    (1001) docker     (123)      441 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/teams/teams.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.804873 mage-ai-0.8.8/mage_ai/services/tracking/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/tracking/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      197 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/services/tracking/metrics.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.804873 mage-ai-0.8.8/mage_ai/settings/
--rw-r--r--   0 runner    (1001) docker     (123)      343 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/settings/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.808873 mage-ai-0.8.8/mage_ai/shared/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      946 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/array.py
--rw-r--r--   0 runner    (1001) docker     (123)       84 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/code.py
--rw-r--r--   0 runner    (1001) docker     (123)     1382 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/config.py
--rw-r--r--   0 runner    (1001) docker     (123)       75 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)    10912 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/conversions.py
--rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/custom_types.py
--rw-r--r--   0 runner    (1001) docker     (123)      949 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/dates.py
--rw-r--r--   0 runner    (1001) docker     (123)      426 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/environments.py
--rw-r--r--   0 runner    (1001) docker     (123)     2368 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/hash.py
--rw-r--r--   0 runner    (1001) docker     (123)     1064 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/http_client.py
--rw-r--r--   0 runner    (1001) docker     (123)     1545 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/io.py
--rw-r--r--   0 runner    (1001) docker     (123)     2993 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/logger.py
--rw-r--r--   0 runner    (1001) docker     (123)     1315 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/multi.py
--rw-r--r--   0 runner    (1001) docker     (123)     2153 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/parsers.py
--rw-r--r--   0 runner    (1001) docker     (123)     1471 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/retry.py
--rw-r--r--   0 runner    (1001) docker     (123)      834 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/strings.py
--rw-r--r--   0 runner    (1001) docker     (123)      251 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     2628 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/shared/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.808873 mage-ai-0.8.8/mage_ai/streaming/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/streaming/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      246 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/streaming/constants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.812873 mage-ai-0.8.8/mage_ai/streaming/sinks/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/streaming/sinks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      664 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/streaming/sinks/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1337 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/streaming/sinks/kinesis.py
--rw-r--r--   0 runner    (1001) docker     (123)     1936 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/streaming/sinks/opensearch.py
--rw-r--r--   0 runner    (1001) docker     (123)      652 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/streaming/sinks/sink_factory.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.812873 mage-ai-0.8.8/mage_ai/streaming/sources/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/streaming/sources/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3524 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/streaming/sources/azure_event_hub.py
--rw-r--r--   0 runner    (1001) docker     (123)     1363 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/streaming/sources/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     4059 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/streaming/sources/kafka.py
--rw-r--r--   0 runner    (1001) docker     (123)     3917 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/streaming/sources/kinesis.py
--rw-r--r--   0 runner    (1001) docker     (123)     3510 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/streaming/sources/rabbitmq.py
--rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/streaming/sources/source_factory.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.812873 mage-ai-0.8.8/mage_ai/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.812873 mage-ai-0.8.8/mage_ai/tests/api/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/api/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.812873 mage-ai-0.8.8/mage_ai/tests/api/operations/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/api/operations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6096 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/api/operations/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1552 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/api/operations/test_sessions.py
--rw-r--r--   0 runner    (1001) docker     (123)     3373 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/api/operations/test_users.py
--rw-r--r--   0 runner    (1001) docker     (123)     1988 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/base_test.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.816872 mage-ai-0.8.8/mage_ai/tests/data_cleaner/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.816872 mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2025 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_clean_column_names.py
--rw-r--r--   0 runner    (1001) docker     (123)     5135 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_fix_syntax_error.py
--rw-r--r--   0 runner    (1001) docker     (123)    25749 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_impute_values.py
--rw-r--r--   0 runner    (1001) docker     (123)    13421 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_reformat_values.py
--rw-r--r--   0 runner    (1001) docker     (123)    15612 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_collinear_columns.py
--rw-r--r--   0 runner    (1001) docker     (123)     2907 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_columns_with_high_empty_rate.py
--rw-r--r--   0 runner    (1001) docker     (123)     1713 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_columns_with_single_value.py
--rw-r--r--   0 runner    (1001) docker     (123)     1479 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_duplicate_rows.py
--rw-r--r--   0 runner    (1001) docker     (123)     5946 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_outliers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.816872 mage-ai-0.8.8/mage_ai/tests/data_cleaner/statistics/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/statistics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    21425 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/statistics/test_calculator.py
--rw-r--r--   0 runner    (1001) docker     (123)    19487 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/test_column_type_detector.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.820873 mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1513 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/shared.py
--rw-r--r--   0 runner    (1001) docker     (123)    13355 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/test_base.py
--rw-r--r--   0 runner    (1001) docker     (123)   116019 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/test_column.py
--rw-r--r--   0 runner    (1001) docker     (123)     7850 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/test_custom_actions.py
--rw-r--r--   0 runner    (1001) docker     (123)     1223 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/test_helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)    29338 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/test_row.py
--rw-r--r--   0 runner    (1001) docker     (123)      858 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/test_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1497 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/test_variable_replacer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.820873 mage-ai-0.8.8/mage_ai/tests/data_preparation/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_preparation/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.820873 mage-ai-0.8.8/mage_ai/tests/data_preparation/models/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_preparation/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12895 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_preparation/models/test_block.py
--rw-r--r--   0 runner    (1001) docker     (123)    26721 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_preparation/models/test_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)     4800 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_preparation/models/test_variable.py
--rw-r--r--   0 runner    (1001) docker     (123)    23686 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_preparation/test_templates.py
--rw-r--r--   0 runner    (1001) docker     (123)     4152 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/data_preparation/test_variable_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     2576 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/factory.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.820873 mage-ai-0.8.8/mage_ai/tests/io/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/io/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7425 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/io/test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     2453 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/io/test_export_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.820873 mage-ai-0.8.8/mage_ai/tests/orchestration/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/orchestration/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.824873 mage-ai-0.8.8/mage_ai/tests/orchestration/db/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/orchestration/db/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7974 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/orchestration/db/test_models.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.824873 mage-ai-0.8.8/mage_ai/tests/orchestration/notification/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/orchestration/notification/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      826 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/orchestration/notification/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     1859 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/orchestration/notification/test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     5749 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/orchestration/notification/test_sender.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.824873 mage-ai-0.8.8/mage_ai/tests/orchestration/queue/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/orchestration/queue/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1594 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/orchestration/queue/test_process_queue.py
--rw-r--r--   0 runner    (1001) docker     (123)     3540 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/orchestration/test_execution_process_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     1535 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/orchestration/test_job_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     6350 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/orchestration/test_pipeline_scheduler.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.824873 mage-ai-0.8.8/mage_ai/tests/orchestration/triggers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/orchestration/triggers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      461 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/orchestration/triggers/test_event_trigger.py
--rw-r--r--   0 runner    (1001) docker     (123)      541 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/orchestration/triggers/test_loop_time_trigger.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.824873 mage-ai-0.8.8/mage_ai/tests/services/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/services/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.824873 mage-ai-0.8.8/mage_ai/tests/services/aws/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/services/aws/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.824873 mage-ai-0.8.8/mage_ai/tests/services/aws/s3/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/services/aws/s3/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2310 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/services/aws/s3/test_s3.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.824873 mage-ai-0.8.8/mage_ai/tests/services/datadog/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/services/datadog/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2254 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/services/datadog/test_datadog.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.824873 mage-ai-0.8.8/mage_ai/tests/services/k8s/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/services/k8s/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6210 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/services/k8s/test_job_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.828873 mage-ai-0.8.8/mage_ai/tests/shared/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/shared/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1574 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/shared/test_io.py
--rw-r--r--   0 runner    (1001) docker     (123)      475 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/shared/test_retry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.828873 mage-ai-0.8.8/mage_ai/tests/streaming/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/streaming/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.828873 mage-ai-0.8.8/mage_ai/tests/streaming/sinks/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/streaming/sinks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1041 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/streaming/sinks/test_kinesis.py
--rw-r--r--   0 runner    (1001) docker     (123)      957 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/streaming/sinks/test_opensearch.py
--rw-r--r--   0 runner    (1001) docker     (123)      949 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/streaming/sinks/test_sink_factory.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.828873 mage-ai-0.8.8/mage_ai/tests/streaming/sources/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/streaming/sources/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1033 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/streaming/sources/test_azure_event_hub.py
--rw-r--r--   0 runner    (1001) docker     (123)     2115 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/streaming/sources/test_kafka.py
--rw-r--r--   0 runner    (1001) docker     (123)     1030 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/streaming/sources/test_kinesis.py
--rw-r--r--   0 runner    (1001) docker     (123)     1379 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/streaming/sources/test_rabbitmq.py
--rw-r--r--   0 runner    (1001) docker     (123)     2057 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/streaming/sources/test_source_factory.py
--rw-r--r--   0 runner    (1001) docker     (123)      838 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/tests/test_shared.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.828873 mage-ai-0.8.8/mage_ai/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      665 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/utils/code.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.828873 mage-ai-0.8.8/mage_ai/utils/logger/
--rw-r--r--   0 runner    (1001) docker     (123)     2518 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/utils/logger/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      271 2023-02-26 17:54:34.000000 mage-ai-0.8.8/mage_ai/utils/logger/constants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 17:54:39.688873 mage-ai-0.8.8/mage_ai.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    14948 2023-02-26 17:54:39.000000 mage-ai-0.8.8/mage_ai.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    45413 2023-02-26 17:54:39.000000 mage-ai-0.8.8/mage_ai.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-26 17:54:39.000000 mage-ai-0.8.8/mage_ai.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       46 2023-02-26 17:54:39.000000 mage-ai-0.8.8/mage_ai.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1990 2023-02-26 17:54:39.000000 mage-ai-0.8.8/mage_ai.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        8 2023-02-26 17:54:39.000000 mage-ai-0.8.8/mage_ai.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       85 2023-02-26 17:54:34.000000 mage-ai-0.8.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     1318 2023-02-26 17:54:34.000000 mage-ai-0.8.8/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-26 17:54:39.832872 mage-ai-0.8.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     3749 2023-02-26 17:54:34.000000 mage-ai-0.8.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.404090 mage-ai-0.8.9/
+-rw-r--r--   0 runner    (1001) docker     (123)    11351 2023-02-26 23:52:57.000000 mage-ai-0.8.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      288 2023-02-26 23:52:57.000000 mage-ai-0.8.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)    14948 2023-02-26 23:53:03.404090 mage-ai-0.8.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    14191 2023-02-26 23:52:57.000000 mage-ai-0.8.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.064087 mage-ai-0.8.9/mage_ai/
+-rw-r--r--   0 runner    (1001) docker     (123)     4235 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.068087 mage-ai-0.8.9/mage_ai/api/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      455 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/api_context.py
+-rw-r--r--   0 runner    (1001) docker     (123)       54 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1144 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)      400 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/logging.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3699 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/middleware.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.068087 mage-ai-0.8.9/mage_ai/api/monitors/
+-rw-r--r--   0 runner    (1001) docker     (123)      624 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/monitors/BaseMonitor.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/monitors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      287 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/oauth_scope.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.068087 mage-ai-0.8.9/mage_ai/api/operations/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/operations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11251 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/operations/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      224 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/operations/constants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.080087 mage-ai-0.8.9/mage_ai/api/policies/
+-rw-r--r--   0 runner    (1001) docker     (123)      678 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/AutocompleteItemPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2010 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/BackfillPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10953 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/BasePolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2140 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/BlockPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      810 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/BlockRunPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      991 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/ClusterPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      654 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/DataProviderPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      640 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/EventRulePolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      992 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/FileContentPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      965 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/FilePolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1200 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/IntegrationDestinationPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1788 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/IntegrationSourcePolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      725 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/IntegrationSourceStreamPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1171 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/KernelPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/LogPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      874 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/MonitorStatPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      618 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/OutputPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2483 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/PipelinePolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2189 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/PipelineRunPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2524 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/PipelineSchedulePolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      625 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/ProjectPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1224 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/SecretPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      966 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/SessionPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1886 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/UserPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1310 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/VariablePolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1404 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/WidgetPolicy.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/policies/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.088087 mage-ai-0.8.9/mage_ai/api/presenters/
+-rw-r--r--   0 runner    (1001) docker     (123)      303 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/AutocompleteItemPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1556 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/BackfillPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5872 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/BasePresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1948 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/BlockPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      464 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/BlockRunPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      206 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/ClusterPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      193 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/DataProviderPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      156 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/EventRulePresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      282 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/FileContentPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      206 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/FilePresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      382 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/IntegrationDestinationPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1040 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/IntegrationSourcePresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      438 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/IntegrationSourceStreamPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      394 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/KernelPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      265 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/LogPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      180 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/MonitorStatPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      238 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/OutputPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1742 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/PipelinePresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1884 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/PipelineRunPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1348 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/PipelineSchedulePresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      198 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/ProjectPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      166 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/SecretPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      286 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/SessionPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      453 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/UserPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      229 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/VariablePresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      608 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/WidgetPresenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.088087 mage-ai-0.8.9/mage_ai/api/presenters/mixins/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/mixins/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      519 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/presenters/mixins/users.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.100088 mage-ai-0.8.9/mage_ai/api/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)     1631 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/AutocompleteItemResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2053 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/BackfillResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9482 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/BaseResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2779 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/BlockResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3000 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/BlockRunResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1665 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/ClusterResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1082 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/DataProviderResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4973 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/DatabaseResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)      460 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/EventRuleResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)      898 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/FileContentResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1511 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/FileResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)      237 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/GenericResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1424 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/IntegrationDestinationResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2010 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/IntegrationSourceResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)      413 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/IntegrationSourceStreamResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1728 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/KernelResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8969 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/LogResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1397 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/MonitorStatResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)      572 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/OutputResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5237 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/PipelineResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8278 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/PipelineRunResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3524 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/PipelineScheduleResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1157 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/ProjectResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)      213 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/Resource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1158 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/SecretResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1792 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/SessionResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4544 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/UserResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5009 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/VariableResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2616 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/WidgetResource.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.100088 mage-ai-0.8.9/mage_ai/api/resources/mixins/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/mixins/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.100088 mage-ai-0.8.9/mage_ai/api/resources/shared/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/shared/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      487 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/shared/collections.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2716 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/resources/shared/collective_loaders.py
+-rw-r--r--   0 runner    (1001) docker     (123)      950 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/result_set.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1452 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6487 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/api/views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.104087 mage-ai-0.8.9/mage_ai/authentication/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/authentication/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1371 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/authentication/oauth2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      732 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/authentication/passwords.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.104087 mage-ai-0.8.9/mage_ai/autocomplete/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/autocomplete/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3651 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/autocomplete/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.104087 mage-ai-0.8.9/mage_ai/cli/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5826 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/cli/main.py
+-rw-r--r--   0 runner    (1001) docker     (123)      880 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/cli/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.104087 mage-ai-0.8.9/mage_ai/cluster_manager/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/cluster_manager/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.108087 mage-ai-0.8.9/mage_ai/cluster_manager/aws/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/cluster_manager/aws/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5194 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/cluster_manager/aws/ecs_task_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2546 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/cluster_manager/aws/emr_cluster_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)      269 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/cluster_manager/cluster_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)      923 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/cluster_manager/constants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.108087 mage-ai-0.8.9/mage_ai/cluster_manager/gcp/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/cluster_manager/gcp/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7933 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/cluster_manager/gcp/cloud_run_service_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.108087 mage-ai-0.8.9/mage_ai/cluster_manager/kubernetes/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/cluster_manager/kubernetes/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9372 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/cluster_manager/kubernetes/workload_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.108087 mage-ai-0.8.9/mage_ai/data_cleaner/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.112088 mage-ai-0.8.9/mage_ai/data_cleaner/analysis/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/analysis/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5932 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/analysis/calculator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10359 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/analysis/charts.py
+-rw-r--r--   0 runner    (1001) docker     (123)      510 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/analysis/constants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.116088 mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1977 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1828 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/clean_column_names.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1193 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/fix_syntax_errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16614 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/impute_values.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11299 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/reformat_values.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2034 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/remove_collinear_columns.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1737 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/remove_columns_with_high_empty_rate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1159 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/remove_columns_with_single_value.py
+-rw-r--r--   0 runner    (1001) docker     (123)      845 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/remove_duplicate_rows.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2069 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/remove_outliers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.116088 mage-ai-0.8.9/mage_ai/data_cleaner/column_types/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/column_types/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10744 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/column_types/column_type_detector.py
+-rw-r--r--   0 runner    (1001) docker     (123)      707 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/column_types/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3750 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/data_cleaner.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.116088 mage-ai-0.8.9/mage_ai/data_cleaner/estimators/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/estimators/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      271 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/estimators/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3369 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/estimators/encoders.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4981 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/estimators/outlier_removal.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.116088 mage-ai-0.8.9/mage_ai/data_cleaner/pipelines/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/pipelines/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5624 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/pipelines/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.120088 mage-ai-0.8.9/mage_ai/data_cleaner/shared/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/shared/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4497 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/shared/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.120088 mage-ai-0.8.9/mage_ai/data_cleaner/statistics/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/statistics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16266 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/statistics/calculator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.124088 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4652 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/action_code.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8471 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13102 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/column.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3172 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1803 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/custom_action.py
+-rw-r--r--   0 runner    (1001) docker     (123)      806 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/dependency_resolution.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2535 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2740 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/row.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1508 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/shared.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.124088 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/spark/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/spark/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      538 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/spark/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10533 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/spark/transformers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.132088 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1316 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/addition.py
+-rw-r--r--   0 runner    (1001) docker     (123)      593 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      153 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/constant.py
+-rw-r--r--   0 runner    (1001) docker     (123)      615 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/date_trunc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1618 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/difference.py
+-rw-r--r--   0 runner    (1001) docker     (123)      676 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/distance_between.py
+-rw-r--r--   0 runner    (1001) docker     (123)      488 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/divide.py
+-rw-r--r--   0 runner    (1001) docker     (123)      262 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/formatted_date.py
+-rw-r--r--   0 runner    (1001) docker     (123)      781 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/if_else.py
+-rw-r--r--   0 runner    (1001) docker     (123)      492 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/multiply.py
+-rw-r--r--   0 runner    (1001) docker     (123)      429 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/string_replace.py
+-rw-r--r--   0 runner    (1001) docker     (123)      453 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/string_split.py
+-rw-r--r--   0 runner    (1001) docker     (123)      408 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/substring.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5748 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1176 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/variable_replacer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.132088 mage-ai-0.8.9/mage_ai/data_integrations/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_integrations/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.132088 mage-ai-0.8.9/mage_ai/data_integrations/destinations/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_integrations/destinations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      315 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_integrations/destinations/constants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.132088 mage-ai-0.8.9/mage_ai/data_integrations/logger/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_integrations/logger/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2493 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_integrations/logger/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.132088 mage-ai-0.8.9/mage_ai/data_integrations/sources/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_integrations/sources/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      978 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_integrations/sources/constants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.136088 mage-ai-0.8.9/mage_ai/data_integrations/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_integrations/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4536 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_integrations/utils/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1502 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_integrations/utils/parsers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7313 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_integrations/utils/scheduler.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.136088 mage-ai-0.8.9/mage_ai/data_preparation/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      648 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/decorators.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.140088 mage-ai-0.8.9/mage_ai/data_preparation/executors/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/executors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10392 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/executors/block_executor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1483 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/executors/ecs_block_executor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3037 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/executors/executor_factory.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1872 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/executors/gcp_cloud_run_block_executor.py
+-rw-r--r--   0 runner    (1001) docker     (123)      643 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/executors/k8s_block_executor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1276 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/executors/pipeline_executor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3520 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/executors/pyspark_block_executor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2806 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/executors/pyspark_pipeline_executor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4901 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/executors/streaming_pipeline_executor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.144088 mage-ai-0.8.9/mage_ai/data_preparation/logging/
+-rw-r--r--   0 runner    (1001) docker     (123)      452 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/logging/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2010 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/logging/gcs_logger_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2206 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/logging/logger.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3706 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/logging/logger_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)      988 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/logging/logger_manager_factory.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1653 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/logging/s3_logger_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.144088 mage-ai-0.8.9/mage_ai/data_preparation/models/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.148088 mage-ai-0.8.9/mage_ai/data_preparation/models/block/
+-rw-r--r--   0 runner    (1001) docker     (123)    73171 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      525 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/constants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.148088 mage-ai-0.8.9/mage_ai/data_preparation/models/block/dbt/
+-rw-r--r--   0 runner    (1001) docker     (123)     6979 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/dbt/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.148088 mage-ai-0.8.9/mage_ai/data_preparation/models/block/dbt/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)    30295 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/dbt/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      119 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/errors.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.148088 mage-ai-0.8.9/mage_ai/data_preparation/models/block/integration/
+-rw-r--r--   0 runner    (1001) docker     (123)    12306 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/integration/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.148088 mage-ai-0.8.9/mage_ai/data_preparation/models/block/r/
+-rw-r--r--   0 runner    (1001) docker     (123)     4572 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/r/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.148088 mage-ai-0.8.9/mage_ai/data_preparation/models/block/r/templates/
+-rw-r--r--   0 runner    (1001) docker     (123)      228 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/r/templates/data_exporter.jinja
+-rw-r--r--   0 runner    (1001) docker     (123)      312 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/r/templates/data_loader.jinja
+-rw-r--r--   0 runner    (1001) docker     (123)      307 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/r/templates/transformer.jinja
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.152088 mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/
+-rw-r--r--   0 runner    (1001) docker     (123)    12301 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2486 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/bigquery.py
+-rw-r--r--   0 runner    (1001) docker     (123)      935 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/mysql.py
+-rw-r--r--   0 runner    (1001) docker     (123)      883 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/postgres.py
+-rw-r--r--   0 runner    (1001) docker     (123)      926 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/redshift.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2591 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/snowflake.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3047 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/trino.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.152088 mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5675 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/utils/shared.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14543 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/block/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2115 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)      103 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4381 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/file.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34818 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/pipeline.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.152088 mage-ai-0.8.9/mage_ai/data_preparation/models/pipelines/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/pipelines/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13563 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/pipelines/integration_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)      237 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/pipelines/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1443 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19496 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/variable.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.156088 mage-ai-0.8.9/mage_ai/data_preparation/models/widget/
+-rw-r--r--   0 runner    (1001) docker     (123)     6839 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/widget/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5277 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/widget/charts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1806 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/widget/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3117 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/models/widget/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5703 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/repo_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.156088 mage-ai-0.8.9/mage_ai/data_preparation/shared/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/shared/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       80 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/shared/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1986 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/shared/secrets.py
+-rw-r--r--   0 runner    (1001) docker     (123)      703 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/shared/stream.py
+-rw-r--r--   0 runner    (1001) docker     (123)      485 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/shared/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.160088 mage-ai-0.8.9/mage_ai/data_preparation/storage/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/storage/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1737 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/storage/base_storage.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2571 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/storage/local_storage.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2958 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/storage/s3_storage.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2729 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/storage/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.160088 mage-ai-0.8.9/mage_ai/data_preparation/templates/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.160088 mage-ai-0.8.9/mage_ai/data_preparation/templates/callbacks/
+-rw-r--r--   0 runner    (1001) docker     (123)      114 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/callbacks/default.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.016087 mage-ai-0.8.9/mage_ai/data_preparation/templates/custom/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.160088 mage-ai-0.8.9/mage_ai/data_preparation/templates/custom/python/
+-rw-r--r--   0 runner    (1001) docker     (123)      399 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/custom/python/default.jinja
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.164088 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/
+-rw-r--r--   0 runner    (1001) docker     (123)      919 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/azure_blob_storage.py
+-rw-r--r--   0 runner    (1001) docker     (123)      937 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/bigquery.py
+-rw-r--r--   0 runner    (1001) docker     (123)      458 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/default.jinja
+-rw-r--r--   0 runner    (1001) docker     (123)      447 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/file.py
+-rw-r--r--   0 runner    (1001) docker     (123)      949 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/google_cloud_storage.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1092 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/mysql.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1210 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/postgres.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.164088 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/pyspark/
+-rw-r--r--   0 runner    (1001) docker     (123)      458 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/pyspark/default.jinja
+-rw-r--r--   0 runner    (1001) docker     (123)      479 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/pyspark/s3.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.168088 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/r/
+-rw-r--r--   0 runner    (1001) docker     (123)      132 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/r/default.jinja
+-rw-r--r--   0 runner    (1001) docker     (123)      954 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/redshift.py
+-rw-r--r--   0 runner    (1001) docker     (123)      847 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/s3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1072 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/snowflake.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.168088 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/streaming/
+-rw-r--r--   0 runner    (1001) docker     (123)       68 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/streaming/kinesis.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      469 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/streaming/opensearch.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.172088 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/
+-rw-r--r--   0 runner    (1001) docker     (123)      391 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/api.py
+-rw-r--r--   0 runner    (1001) docker     (123)      901 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/azure_blob_storage.py
+-rw-r--r--   0 runner    (1001) docker     (123)      772 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/bigquery.py
+-rw-r--r--   0 runner    (1001) docker     (123)      466 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/default.jinja
+-rw-r--r--   0 runner    (1001) docker     (123)      582 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/file.py
+-rw-r--r--   0 runner    (1001) docker     (123)      914 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/google_cloud_storage.py
+-rw-r--r--   0 runner    (1001) docker     (123)      816 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/mysql.py
+-rw-r--r--   0 runner    (1001) docker     (123)      843 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/postgres.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.172088 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/pyspark/
+-rw-r--r--   0 runner    (1001) docker     (123)      461 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/pyspark/default.jinja
+-rw-r--r--   0 runner    (1001) docker     (123)      567 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/pyspark/s3.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.172088 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/r/
+-rw-r--r--   0 runner    (1001) docker     (123)      156 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/r/default.jinja
+-rw-r--r--   0 runner    (1001) docker     (123)      815 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/redshift.py
+-rw-r--r--   0 runner    (1001) docker     (123)      819 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/s3.py
+-rw-r--r--   0 runner    (1001) docker     (123)      850 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/snowflake.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.176088 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/streaming/
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/streaming/azure_event_hub.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      499 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/streaming/kafka.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       65 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/streaming/kinesis.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      303 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/streaming/rabbitmq.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.176088 mage-ai-0.8.9/mage_ai/data_preparation/templates/pipeline/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/pipeline/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       43 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/pipeline/metadata.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.176088 mage-ai-0.8.9/mage_ai/data_preparation/templates/pipeline_execution/
+-rw-r--r--   0 runner    (1001) docker     (123)      703 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/pipeline_execution/emr_bootstrap.sh
+-rw-r--r--   0 runner    (1001) docker     (123)     2665 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/pipeline_execution/spark_script.jinja
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.176088 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.176088 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/charts/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/charts/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.180088 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/data_exporters/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/data_exporters/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      460 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/data_exporters/export_titanic_clean.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.180088 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/data_loaders/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/data_loaders/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      722 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/data_loaders/load_titanic.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.180088 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/dbt/
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/dbt/profiles.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2040 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/io_config.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      975 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/metadata.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.180088 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/pipelines/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/pipelines/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.180088 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/pipelines/example_pipeline/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/pipelines/example_pipeline/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      705 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/pipelines/example_pipeline/metadata.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.180088 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/scratchpads/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/scratchpads/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.184088 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/transformers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/transformers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1320 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/transformers/fill_in_missing_values.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.184088 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/utils/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.184088 mage-ai-0.8.9/mage_ai/data_preparation/templates/sensors/
+-rw-r--r--   0 runner    (1001) docker     (123)      474 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/sensors/default.py
+-rw-r--r--   0 runner    (1001) docker     (123)      677 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/sensors/s3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9132 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/template.py
+-rw-r--r--   0 runner    (1001) docker     (123)      333 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/testable.jinja
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.184088 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/
+-rw-r--r--   0 runner    (1001) docker     (123)     1171 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/data_warehouse_transformer.jinja
+-rw-r--r--   0 runner    (1001) docker     (123)      692 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/default.jinja
+-rw-r--r--   0 runner    (1001) docker     (123)      692 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/default_pyspark.jinja
+-rw-r--r--   0 runner    (1001) docker     (123)      438 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/default_streaming.jinja
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.188088 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/r/
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/r/default.r
+-rw-r--r--   0 runner    (1001) docker     (123)      561 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/suggestion_fmt.jinja
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.188088 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/
+-rw-r--r--   0 runner    (1001) docker     (123)      731 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/action.jinja
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.196088 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/
+-rw-r--r--   0 runner    (1001) docker     (123)      774 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/average.py
+-rw-r--r--   0 runner    (1001) docker     (123)      413 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/clean_column_name.py
+-rw-r--r--   0 runner    (1001) docker     (123)      756 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/count.py
+-rw-r--r--   0 runner    (1001) docker     (123)      774 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/count_distinct.py
+-rw-r--r--   0 runner    (1001) docker     (123)      573 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/diff.py
+-rw-r--r--   0 runner    (1001) docker     (123)      758 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/first.py
+-rw-r--r--   0 runner    (1001) docker     (123)      546 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/fix_syntax_errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)      646 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/impute.py
+-rw-r--r--   0 runner    (1001) docker     (123)      756 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/last.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1167 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/max.py
+-rw-r--r--   0 runner    (1001) docker     (123)      772 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/median.py
+-rw-r--r--   0 runner    (1001) docker     (123)      766 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/min.py
+-rw-r--r--   0 runner    (1001) docker     (123)      467 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/normalize.py
+-rw-r--r--   0 runner    (1001) docker     (123)      479 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/reformat.py
+-rw-r--r--   0 runner    (1001) docker     (123)      408 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/remove.py
+-rw-r--r--   0 runner    (1001) docker     (123)      677 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/remove_outliers.py
+-rw-r--r--   0 runner    (1001) docker     (123)      416 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/select.py
+-rw-r--r--   0 runner    (1001) docker     (123)      605 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/shift_down.py
+-rw-r--r--   0 runner    (1001) docker     (123)      565 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/shift_up.py
+-rw-r--r--   0 runner    (1001) docker     (123)      506 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/standardize.py
+-rw-r--r--   0 runner    (1001) docker     (123)      766 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/sum.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.196088 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/row/
+-rw-r--r--   0 runner    (1001) docker     (123)      543 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/row/drop_duplicate.py
+-rw-r--r--   0 runner    (1001) docker     (123)      406 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/row/filter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      418 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/row/remove.py
+-rw-r--r--   0 runner    (1001) docker     (123)      434 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/row/sort.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1951 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/templates/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.200088 mage-ai-0.8.9/mage_ai/data_preparation/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/utils/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.200088 mage-ai-0.8.9/mage_ai/data_preparation/utils/block/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/utils/block/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2831 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/utils/block/convert_content.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11944 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/data_preparation/variable_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.200088 mage-ai-0.8.9/mage_ai/errors/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/errors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       45 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/errors/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.208088 mage-ai-0.8.9/mage_ai/io/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4569 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/azure_blob_storage.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10680 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14957 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/bigquery.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14862 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3272 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/export_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2564 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/file.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6636 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/google_cloud_storage.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1302 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/io_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4585 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/mysql.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7513 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/postgres.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13408 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/redshift.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5800 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/s3.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10665 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/snowflake.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10075 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/sql.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9322 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/trino.py
+-rw-r--r--   0 runner    (1001) docker     (123)      653 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/io/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.208088 mage-ai-0.8.9/mage_ai/orchestration/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2797 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/airflow.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.208088 mage-ai-0.8.9/mage_ai/orchestration/backfills/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/backfills/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3872 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/backfills/service.py
+-rw-r--r--   0 runner    (1001) docker     (123)      126 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/constants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.212088 mage-ai-0.8.9/mage_ai/orchestration/db/
+-rw-r--r--   0 runner    (1001) docker     (123)     2783 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3262 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/alembic.ini
+-rw-r--r--   0 runner    (1001) docker     (123)      960 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/database_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)      406 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/errors.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.212088 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/
+-rw-r--r--   0 runner    (1001) docker     (123)      264 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     2836 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/env.py
+-rw-r--r--   0 runner    (1001) docker     (123)      510 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/script.py.mako
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.220089 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/
+-rw-r--r--   0 runner    (1001) docker     (123)      859 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/053ee2c10d85_add_completed_at.py
+-rw-r--r--   0 runner    (1001) docker     (123)      699 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/067326f43bc3_add_variables_to_pipelinerun.py
+-rw-r--r--   0 runner    (1001) docker     (123)      711 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/1d8e65aeefdd_add_settings_to_pipeline_schedule.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1172 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/1f9353eddbc6_add_secrets_table.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1124 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/2266370f589b_add_indexes_to_pipeline_run.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2579 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/26305e46df52_create_backfills_table.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1607 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/3fafd217efa7_add_event_matcher_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)      715 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/52ab80005742_add_variables_to_pipeline_schedule.py
+-rw-r--r--   0 runner    (1001) docker     (123)      705 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/5cd59ec4cf1d_add_passed_sla_to_pipeline_run.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1668 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/643b6e65e814_add_unique_indexes_on_authentication_.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/6aecc9bc451c_update_schedule_type_enum.py
+-rw-r--r--   0 runner    (1001) docker     (123)      915 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/7ac6fed06918_add_token_column_to_pipeline_schedule_.py
+-rw-r--r--   0 runner    (1001) docker     (123)      699 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/84de4cdd6126_add_sla_to_pipeline_schedule.py
+-rw-r--r--   0 runner    (1001) docker     (123)      859 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/8971d4cd5b39_add_event_variables_and_metadata_to_.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3375 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/97ff9f55a3c0_create_users_oauth2_applications_and_.py
+-rw-r--r--   0 runner    (1001) docker     (123)      710 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/b01be687e537_add_started_at_to_block_run.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3024 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/c07a23ff782b_add_initial_tables.py
+-rw-r--r--   0 runner    (1001) docker     (123)      685 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/ec5df57a1c60_add_metrics_to_block_runs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23745 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)      604 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/db/process.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3817 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/execution_process_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1514 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/job_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.220089 mage-ai-0.8.9/mage_ai/orchestration/metrics/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/metrics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5553 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/metrics/pipeline_run.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.220089 mage-ai-0.8.9/mage_ai/orchestration/monitor/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/monitor/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8352 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/monitor/monitor_stats.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.220089 mage-ai-0.8.9/mage_ai/orchestration/notification/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/notification/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2269 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/notification/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4086 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/notification/sender.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33167 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/pipeline_scheduler.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.224089 mage-ai-0.8.9/mage_ai/orchestration/queue/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/queue/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      691 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/queue/celery_queue.py
+-rw-r--r--   0 runner    (1001) docker     (123)      293 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/queue/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3393 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/queue/process_queue.py
+-rw-r--r--   0 runner    (1001) docker     (123)      472 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/queue/queue.py
+-rw-r--r--   0 runner    (1001) docker     (123)      717 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/queue/queue_factory.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2405 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/run_status_checker.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.224089 mage-ai-0.8.9/mage_ai/orchestration/triggers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/triggers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      208 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/triggers/event_trigger.py
+-rw-r--r--   0 runner    (1001) docker     (123)      439 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/triggers/loop_time_trigger.py
+-rw-r--r--   0 runner    (1001) docker     (123)      382 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/triggers/time_trigger.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.224089 mage-ai-0.8.9/mage_ai/orchestration/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      636 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/orchestration/utils/resources.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.236089 mage-ai-0.8.9/mage_ai/sample_datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)      789 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/sample_datasets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   872940 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/sample_datasets/product_purchases.csv
+-rw-r--r--   0 runner    (1001) docker     (123)  5385107 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/sample_datasets/salary_survey.csv
+-rw-r--r--   0 runner    (1001) docker     (123)    60302 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/sample_datasets/titanic_survival.csv
+-rw-r--r--   0 runner    (1001) docker     (123)   258700 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/sample_datasets/user_emails.csv
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.240089 mage-ai-0.8.9/mage_ai/server/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2129 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/active_kernel.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.244089 mage-ai-0.8.9/mage_ai/server/api/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3660 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/api/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1697 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/api/blocks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7042 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/api/clusters.py
+-rw-r--r--   0 runner    (1001) docker     (123)      172 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/api/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)      119 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/api/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2096 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/api/events.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1683 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/api/integration_sources.py
+-rw-r--r--   0 runner    (1001) docker     (123)      946 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/api/projects.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2471 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/api/triggers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1822 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/api/v1.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13229 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/app.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.244089 mage-ai-0.8.9/mage_ai/server/client/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/client/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2719 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/client/mage.py
+-rw-r--r--   0 runner    (1001) docker     (123)      420 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/constants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.244089 mage-ai-0.8.9/mage_ai/server/data/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/data/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3827 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/data/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9281 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/data/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)      618 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/docs_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2746 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/execution_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.248089 mage-ai-0.8.9/mage_ai/server/frontend_dist/
+-rw-r--r--   0 runner    (1001) docker     (123)     8646 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/404.html
+-rw-r--r--   0 runner    (1001) docker     (123)     8646 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/404.html.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.032087 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.036087 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.292089 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/
+-rw-r--r--   0 runner    (1001) docker     (123)     3531 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/1150.1378afaa474df64a.js
+-rw-r--r--   0 runner    (1001) docker     (123)     6458 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/1240.0819f45820d22263.js
+-rw-r--r--   0 runner    (1001) docker     (123)    32475 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/1286-a62050b3f897c6be.js
+-rw-r--r--   0 runner    (1001) docker     (123)     5290 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/1450.d383f64c169d4278.js
+-rw-r--r--   0 runner    (1001) docker     (123)     8652 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/1774-aa51ef1da7217ff9.js
+-rw-r--r--   0 runner    (1001) docker     (123)    13323 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/1830-cb1bbbf9a9c54649.js
+-rw-r--r--   0 runner    (1001) docker     (123)    60381 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2083-78a438dbdc57d1e4.js
+-rw-r--r--   0 runner    (1001) docker     (123)    69805 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2125-0b537dc53fe71b18.js
+-rw-r--r--   0 runner    (1001) docker     (123)    14082 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2249-70929b8c547bbc18.js
+-rw-r--r--   0 runner    (1001) docker     (123)    14489 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2426-be3e2bc6625de582.js
+-rw-r--r--   0 runner    (1001) docker     (123)     2942 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2481.0454a0e25dc7e027.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1649 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2508.724531e7f9cf5f36.js
+-rw-r--r--   0 runner    (1001) docker     (123)   791202 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2524-6aeb9419acf5d1b4.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3432 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2545.8371b39c898ae92b.js
+-rw-r--r--   0 runner    (1001) docker     (123)    10519 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/261.0a24b4ece1d29aa1.js
+-rw-r--r--   0 runner    (1001) docker     (123)     2226 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/266.e301071d22592682.js
+-rw-r--r--   0 runner    (1001) docker     (123)     9689 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2714-1e79e9f2e998b544.js
+-rw-r--r--   0 runner    (1001) docker     (123)    71691 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/29107295-989a0767a635d9d5.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3524 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/3453.992f4b1667e9882c.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1618 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/3467.38cd0654ba6f788f.js
+-rw-r--r--   0 runner    (1001) docker     (123)    30652 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/3835.df296b4e4078e985.js
+-rw-r--r--   0 runner    (1001) docker     (123)    46702 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/3850-6395783d820def1c.js
+-rw-r--r--   0 runner    (1001) docker     (123)   243728 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/3873.4b3eace753998412.js
+-rw-r--r--   0 runner    (1001) docker     (123)     4171 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/3898.880191695bb05845.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1428 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4042.5e16d36209052351.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3421 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4092.536ee541241f4538.js
+-rw-r--r--   0 runner    (1001) docker     (123)    12971 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/434-69ddfacd3e93f2db.js
+-rw-r--r--   0 runner    (1001) docker     (123)     6457 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4388.04098706f32e69e7.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1122 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/440.3ab77942f659ea0c.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4450.79f14f763d55c63e.js
+-rw-r--r--   0 runner    (1001) docker     (123)     2243 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4454.13a2404adecaa39e.js
+-rw-r--r--   0 runner    (1001) docker     (123)    13231 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4463-1b9ce74c6e1bb14e.js
+-rw-r--r--   0 runner    (1001) docker     (123)    57586 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4495-4f0340aa82e0c623.js
+-rw-r--r--   0 runner    (1001) docker     (123)     2720 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4776.753ad29fa0a29a4a.js
+-rw-r--r--   0 runner    (1001) docker     (123)    95131 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4804-01a10103ebe26ca8.js
+-rw-r--r--   0 runner    (1001) docker     (123)    15512 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4846-b4ced91dc0e9fba9.js
+-rw-r--r--   0 runner    (1001) docker     (123)     2310 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4883.a5bb0edbf8f3cc8f.js
+-rw-r--r--   0 runner    (1001) docker     (123)    17422 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5008.29c2662ecc2b04c7.js
+-rw-r--r--   0 runner    (1001) docker     (123)     2135 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5104.1edcf4437c471dd4.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1816 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5164.857023e800905b6f.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3490 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5729.0f2748e9e6dab951.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3479 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5824.628653557e904674.js
+-rw-r--r--   0 runner    (1001) docker     (123)   105056 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5872-103815a4a043489b.js
+-rw-r--r--   0 runner    (1001) docker     (123)    91825 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5896-f84e336fb8877027.js
+-rw-r--r--   0 runner    (1001) docker     (123)    13407 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5944-757b7898608a65e1.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1867 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6042.c59010de9e699437.js
+-rw-r--r--   0 runner    (1001) docker     (123)    18793 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6085-692d2f784c0504f2.js
+-rw-r--r--   0 runner    (1001) docker     (123)     2203 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6115.0c85e507543394ea.js
+-rw-r--r--   0 runner    (1001) docker     (123)    17641 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6116.871a682ddf535aca.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1467 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6434.10380ee0968636ba.js
+-rw-r--r--   0 runner    (1001) docker     (123)     2315 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6443.7b6d2b4e51018184.js
+-rw-r--r--   0 runner    (1001) docker     (123)    24930 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6507.d3a17777d2c294e6.js
+-rw-r--r--   0 runner    (1001) docker     (123)    16709 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6532-a614f9e1f9434872.js
+-rw-r--r--   0 runner    (1001) docker     (123)    18067 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6579-2b5d8d39472d85c0.js
+-rw-r--r--   0 runner    (1001) docker     (123)    11627 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6641-a0ed2bd8f5dc777b.js
+-rw-r--r--   0 runner    (1001) docker     (123)     2766 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6958.8f39c585d36737a7.js
+-rw-r--r--   0 runner    (1001) docker     (123)    23228 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/7011-81dd8269c4806d26.js
+-rw-r--r--   0 runner    (1001) docker     (123)    16617 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/704-4de8946d753a578a.js
+-rw-r--r--   0 runner    (1001) docker     (123)  1409747 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/72fdc299.2d5ec188af5d0049.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3506 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/739.3d24945544b37e52.js
+-rw-r--r--   0 runner    (1001) docker     (123)    16874 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/7400-1430ec3874c1fdee.js
+-rw-r--r--   0 runner    (1001) docker     (123)     5292 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/792.010ca00d79b2112f.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1129 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/7947.77be4bec4d47774e.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1867 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/7951.fee8b6c27c9ef777.js
+-rw-r--r--   0 runner    (1001) docker     (123)     4838 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8018.968bf87c390e3312.js
+-rw-r--r--   0 runner    (1001) docker     (123)     2166 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8097.b0345f30a7390c1d.js
+-rw-r--r--   0 runner    (1001) docker     (123)    12094 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8256.290ceb269b1ffe26.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3939 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/826.75268ee34f93393a.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1783 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8277.5003e1d94bb85156.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3479 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8762.dff300f86bef8573.js
+-rw-r--r--   0 runner    (1001) docker     (123)    15534 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8789-4f858e520d46973b.js
+-rw-r--r--   0 runner    (1001) docker     (123)     5003 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8807.a68c69c8fe0a8c01.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3020 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8849.db0d50b4d84b09a6.js
+-rw-r--r--   0 runner    (1001) docker     (123)     4240 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8901.21d26d5a1ee473fe.js
+-rw-r--r--   0 runner    (1001) docker     (123)     9937 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8920.5700e380a2999098.js
+-rw-r--r--   0 runner    (1001) docker     (123)    16976 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8961-697fe5d4db44d909.js
+-rw-r--r--   0 runner    (1001) docker     (123)    17386 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9140-6f67e0879394373d.js
+-rw-r--r--   0 runner    (1001) docker     (123)     8406 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9258.6c6ef544c701a011.js
+-rw-r--r--   0 runner    (1001) docker     (123)     2131 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9307.d4baf7aebbcef1f0.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1867 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9361.a0820e3069f5ef74.js
+-rw-r--r--   0 runner    (1001) docker     (123)     5350 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9363.6b811b4c86277e07.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1655 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9437.a3c32f45cf9ef69b.js
+-rw-r--r--   0 runner    (1001) docker     (123)     8443 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9565-28e1c30511c95c2d.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1963 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9566.f8bd24768ed14ecb.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3826 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9633.40e5056ca1e2b22a.js
+-rw-r--r--   0 runner    (1001) docker     (123)    66714 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9767-3f852fd90cf7857f.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1428 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9785.5ff26cb26d84d6a1.js
+-rw-r--r--   0 runner    (1001) docker     (123)    12357 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9832-c8b8970bb522f302.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3480 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9855.c4394a68322be9f8.js
+-rw-r--r--   0 runner    (1001) docker     (123)    14948 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9898-51ca6a904b7a2382.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3030 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9927.e82a3e1e21990d77.js
+-rw-r--r--   0 runner    (1001) docker     (123)   110731 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/bd1a647f.6050372acaa5cc3c.js
+-rw-r--r--   0 runner    (1001) docker     (123)   140771 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/framework-7c365855dab1bf41.js
+-rw-r--r--   0 runner    (1001) docker     (123)   102188 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/main-bb0dd5375146d7fd.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.296089 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/
+-rw-r--r--   0 runner    (1001) docker     (123)   332649 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/_app-0aed65f2e085822e.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3190 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/_error-235304e5badb19eb.js
+-rw-r--r--   0 runner    (1001) docker     (123)      636 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/index-e34a68d2f6fe16f2.js
+-rw-r--r--   0 runner    (1001) docker     (123)    43508 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/manage-54fd0434f4f5305c.js
+-rw-r--r--   0 runner    (1001) docker     (123)     9352 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipeline-runs-21fe37061bdaaaea.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.296089 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.300089 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.304089 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/backfills/
+-rw-r--r--   0 runner    (1001) docker     (123)    27512 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/backfills/[...slug]-81e3c9ea75d7abb4.js
+-rw-r--r--   0 runner    (1001) docker     (123)    25680 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/backfills-0ed0d70bc659c236.js
+-rw-r--r--   0 runner    (1001) docker     (123)   335648 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/edit-1b8b406222fae908.js
+-rw-r--r--   0 runner    (1001) docker     (123)    34280 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/logs-5ccc75887776efb0.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.304089 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/monitors/
+-rw-r--r--   0 runner    (1001) docker     (123)    13594 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/monitors/block-runs-8f23f7ca9efcb069.js
+-rw-r--r--   0 runner    (1001) docker     (123)    11953 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/monitors/block-runtime-f83ab9de4094e1b0.js
+-rw-r--r--   0 runner    (1001) docker     (123)      345 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/monitors-8b08ec1aef4af4f2.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.304089 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/runs/
+-rw-r--r--   0 runner    (1001) docker     (123)    17156 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/runs/[run]-73ced07cc98a4968.js
+-rw-r--r--   0 runner    (1001) docker     (123)    13088 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/runs-67d23509a0c9a1b8.js
+-rw-r--r--   0 runner    (1001) docker     (123)    44763 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/syncs-4084a44baf91f30e.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.304089 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/triggers/
+-rw-r--r--   0 runner    (1001) docker     (123)    39151 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/triggers/[...slug]-ae970171cfe98c51.js
+-rw-r--r--   0 runner    (1001) docker     (123)    36826 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/triggers-b0b91245d3299bdf.js
+-rw-r--r--   0 runner    (1001) docker     (123)     4526 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]-ca9457e1a6bced4b.js
+-rw-r--r--   0 runner    (1001) docker     (123)    21520 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines-12dc02ae431a6305.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.036087 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.304089 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/account/
+-rw-r--r--   0 runner    (1001) docker     (123)     4003 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/account/profile-acd7ee47219fee3d.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.304089 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/workspace/
+-rw-r--r--   0 runner    (1001) docker     (123)     9191 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/workspace/preferences-07bda506f68974fb.js
+-rw-r--r--   0 runner    (1001) docker     (123)    10903 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/workspace/users-c128672e053a4c30.js
+-rw-r--r--   0 runner    (1001) docker     (123)     4347 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings-d594a66a568306da.js
+-rw-r--r--   0 runner    (1001) docker     (123)    16326 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/sign-in-b4e1eb529a184c60.js
+-rw-r--r--   0 runner    (1001) docker     (123)    11068 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/terminal-5d7c45bb058a3f20.js
+-rw-r--r--   0 runner    (1001) docker     (123)     4306 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/test-f567bdfcc1276249.js
+-rw-r--r--   0 runner    (1001) docker     (123)    19885 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/triggers-e0172c422c95eda9.js
+-rw-r--r--   0 runner    (1001) docker     (123)    91434 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/polyfills-5cd94c89d3acac5f.js
+-rw-r--r--   0 runner    (1001) docker     (123)     5196 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.308089 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/css/
+-rw-r--r--   0 runner    (1001) docker     (123)    15565 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/css/d1e8e64d0b07af2f.css
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.308089 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/hPU1Mni8edYXkEy_4mLHN/
+-rw-r--r--   0 runner    (1001) docker     (123)     5190 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js
+-rw-r--r--   0 runner    (1001) docker     (123)       77 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js
+-rw-r--r--   0 runner    (1001) docker     (123)    15406 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/favicon.ico
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.036087 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.036087 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Fira_Code/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.312090 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/
+-rw-r--r--   0 runner    (1001) docker     (123)   319368 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Bold.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   288380 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Light.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   283684 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Medium.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   289624 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Regular.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   285428 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Retina.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   304248 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-SemiBold.ttf
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.320089 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/
+-rw-r--r--   0 runner    (1001) docker     (123)    11560 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)   168060 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Black.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   174108 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-BlackItalic.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   167336 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Bold.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   171508 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-BoldItalic.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   170504 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Italic.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   167000 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Light.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   173172 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-LightItalic.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   168644 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Medium.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   173416 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-MediumItalic.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   168260 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Regular.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   168488 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Thin.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   172860 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-ThinItalic.ttf
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.320089 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/
+-rw-r--r--   0 runner    (1001) docker     (123)    11560 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     2552 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/README.txt
+-rw-r--r--   0 runner    (1001) docker     (123)   195012 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/RobotoMono-Italic-VariableFont_wght.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   182172 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/RobotoMono-VariableFont_wght.ttf
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.328090 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/
+-rw-r--r--   0 runner    (1001) docker     (123)    87008 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Bold.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)    94148 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-BoldItalic.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)    87788 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-ExtraLight.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)    93408 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-ExtraLightItalic.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)    93904 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Italic.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)    87592 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Light.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)    93760 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-LightItalic.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)    86820 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Medium.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)    93948 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-MediumItalic.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)    86908 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Regular.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)    87076 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-SemiBold.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)    93940 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-SemiBoldItalic.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)    87872 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Thin.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)    93056 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-ThinItalic.ttf
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.332090 mage-ai-0.8.9/mage_ai/server/frontend_dist/images/
+-rw-r--r--   0 runner    (1001) docker     (123)     4404 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/images/backfill.jpg
+-rw-r--r--   0 runner    (1001) docker     (123)     4854 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/images/banner-shape-purple-peach.jpg
+-rw-r--r--   0 runner    (1001) docker     (123)    57024 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/images/dashboard-api-key.webp
+-rw-r--r--   0 runner    (1001) docker     (123)     5150 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/images/extra.jpg
+-rw-r--r--   0 runner    (1001) docker     (123)     6969 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/images/monitor.jpg
+-rw-r--r--   0 runner    (1001) docker     (123)     6850 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/images/run B.jpg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.332090 mage-ai-0.8.9/mage_ai/server/frontend_dist/images/sessions/
+-rw-r--r--   0 runner    (1001) docker     (123)   256616 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/images/sessions/abstract.png
+-rw-r--r--   0 runner    (1001) docker     (123)     7408 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/index.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9081 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/manage.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9369 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipeline-runs.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.332090 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.336090 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.336090 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/backfills/
+-rw-r--r--   0 runner    (1001) docker     (123)    10273 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/backfills/[...slug].html
+-rw-r--r--   0 runner    (1001) docker     (123)     9327 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/backfills.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9432 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/edit.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9785 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/logs.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.336090 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/monitors/
+-rw-r--r--   0 runner    (1001) docker     (123)     9737 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/monitors/block-runs.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9903 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/monitors/block-runtime.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9637 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/monitors.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.336090 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/runs/
+-rw-r--r--   0 runner    (1001) docker     (123)    10052 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/runs/[run].html
+-rw-r--r--   0 runner    (1001) docker     (123)     9941 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/runs.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9397 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/syncs.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.336090 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/triggers/
+-rw-r--r--   0 runner    (1001) docker     (123)    10349 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/triggers/[...slug].html
+-rw-r--r--   0 runner    (1001) docker     (123)     9949 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/triggers.html
+-rw-r--r--   0 runner    (1001) docker     (123)     7522 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline].html
+-rw-r--r--   0 runner    (1001) docker     (123)     9201 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.040087 mage-ai-0.8.9/mage_ai/server/frontend_dist/settings/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.336090 mage-ai-0.8.9/mage_ai/server/frontend_dist/settings/account/
+-rw-r--r--   0 runner    (1001) docker     (123)     9308 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/settings/account/profile.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.340090 mage-ai-0.8.9/mage_ai/server/frontend_dist/settings/workspace/
+-rw-r--r--   0 runner    (1001) docker     (123)     9164 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/settings/workspace/preferences.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9308 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/settings/workspace/users.html
+-rw-r--r--   0 runner    (1001) docker     (123)     7480 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/settings.html
+-rw-r--r--   0 runner    (1001) docker     (123)    18393 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/sign-in.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9276 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/terminal.html
+-rw-r--r--   0 runner    (1001) docker     (123)     7831 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/test.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9198 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/triggers.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1101 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/frontend_dist/vercel.svg
+-rw-r--r--   0 runner    (1001) docker     (123)     2113 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/kernel_output_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)      787 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/kernels.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2030 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/scheduler_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12393 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/server.py
+-rw-r--r--   0 runner    (1001) docker     (123)      659 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/subscriber.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.340090 mage-ai-0.8.9/mage_ai/server/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3295 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/utils/frontend_renderer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11417 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/utils/output_display.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16870 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/server/websocket_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.340090 mage-ai-0.8.9/mage_ai/services/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.344090 mage-ai-0.8.9/mage_ai/services/airbyte/
+-rw-r--r--   0 runner    (1001) docker     (123)     2876 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/airbyte/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3416 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/airbyte/client.py
+-rw-r--r--   0 runner    (1001) docker     (123)      289 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/airbyte/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      216 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/airbyte/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)      273 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/airbyte/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      827 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/airbyte/server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.344090 mage-ai-0.8.9/mage_ai/services/aws/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.344090 mage-ai-0.8.9/mage_ai/services/aws/ecs/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/ecs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3168 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/ecs/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1285 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/ecs/ecs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.348090 mage-ai-0.8.9/mage_ai/services/aws/emr/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/emr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3392 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/emr/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9519 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/emr/emr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7203 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/emr/emr_basics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1117 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/emr/launcher.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1267 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/emr/resource_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.348090 mage-ai-0.8.9/mage_ai/services/aws/events/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/events/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1986 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/events/events.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.348090 mage-ai-0.8.9/mage_ai/services/aws/s3/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/s3/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2633 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/s3/s3.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.348090 mage-ai-0.8.9/mage_ai/services/aws/secrets_manager/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/secrets_manager/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1073 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/aws/secrets_manager/secrets_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.348090 mage-ai-0.8.9/mage_ai/services/datadog/
+-rw-r--r--   0 runner    (1001) docker     (123)     2789 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/datadog/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.352090 mage-ai-0.8.9/mage_ai/services/dbt/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/dbt/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      160 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/dbt/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      301 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/dbt/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7529 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/dbt/dbt.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.352090 mage-ai-0.8.9/mage_ai/services/email/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/email/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      439 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/email/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      658 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/email/email.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.352090 mage-ai-0.8.9/mage_ai/services/gcp/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/gcp/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.352090 mage-ai-0.8.9/mage_ai/services/gcp/cloud_run/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/gcp/cloud_run/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2694 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/gcp/cloud_run/cloud_run.py
+-rw-r--r--   0 runner    (1001) docker     (123)      214 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/gcp/cloud_run/config.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.356090 mage-ai-0.8.9/mage_ai/services/hightouch/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/hightouch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      144 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/hightouch/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      529 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/hightouch/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3706 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/hightouch/hightouch.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.356090 mage-ai-0.8.9/mage_ai/services/k8s/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/k8s/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      106 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/k8s/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4127 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/k8s/job_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.356090 mage-ai-0.8.9/mage_ai/services/metaplane/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/metaplane/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      211 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/metaplane/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4594 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/metaplane/metaplane.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.356090 mage-ai-0.8.9/mage_ai/services/slack/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/slack/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      273 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/slack/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      244 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/slack/slack.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.360090 mage-ai-0.8.9/mage_ai/services/stitch/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/stitch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      287 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/stitch/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      123 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/stitch/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8782 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/stitch/stitch.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.360090 mage-ai-0.8.9/mage_ai/services/teams/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/teams/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      273 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/teams/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      441 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/teams/teams.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.360090 mage-ai-0.8.9/mage_ai/services/tracking/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/tracking/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      197 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/services/tracking/metrics.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.360090 mage-ai-0.8.9/mage_ai/settings/
+-rw-r--r--   0 runner    (1001) docker     (123)      343 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/settings/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.368090 mage-ai-0.8.9/mage_ai/shared/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      946 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/array.py
+-rw-r--r--   0 runner    (1001) docker     (123)       84 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/code.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1382 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)       75 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10912 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/conversions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/custom_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)      949 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/dates.py
+-rw-r--r--   0 runner    (1001) docker     (123)      426 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/environments.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2368 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/hash.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1064 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/http_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1545 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2993 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/logger.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1315 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/multi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2153 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/parsers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1471 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/retry.py
+-rw-r--r--   0 runner    (1001) docker     (123)      834 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/strings.py
+-rw-r--r--   0 runner    (1001) docker     (123)      251 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2628 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/shared/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.368090 mage-ai-0.8.9/mage_ai/streaming/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/streaming/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      246 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/streaming/constants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.372090 mage-ai-0.8.9/mage_ai/streaming/sinks/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/streaming/sinks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      664 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/streaming/sinks/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1337 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/streaming/sinks/kinesis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1936 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/streaming/sinks/opensearch.py
+-rw-r--r--   0 runner    (1001) docker     (123)      652 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/streaming/sinks/sink_factory.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.372090 mage-ai-0.8.9/mage_ai/streaming/sources/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/streaming/sources/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3524 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/streaming/sources/azure_event_hub.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1363 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/streaming/sources/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4059 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/streaming/sources/kafka.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3917 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/streaming/sources/kinesis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3510 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/streaming/sources/rabbitmq.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/streaming/sources/source_factory.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.376090 mage-ai-0.8.9/mage_ai/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.376090 mage-ai-0.8.9/mage_ai/tests/api/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/api/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.376090 mage-ai-0.8.9/mage_ai/tests/api/operations/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/api/operations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6096 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/api/operations/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1552 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/api/operations/test_sessions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3373 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/api/operations/test_users.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1988 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/base_test.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.376090 mage-ai-0.8.9/mage_ai/tests/data_cleaner/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.380090 mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2025 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_clean_column_names.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5135 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_fix_syntax_error.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25749 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_impute_values.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13421 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_reformat_values.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15612 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_collinear_columns.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2907 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_columns_with_high_empty_rate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1713 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_columns_with_single_value.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1479 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_duplicate_rows.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5946 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_outliers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.380090 mage-ai-0.8.9/mage_ai/tests/data_cleaner/statistics/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/statistics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21425 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/statistics/test_calculator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19487 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/test_column_type_detector.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.384090 mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1513 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/shared.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13355 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/test_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)   116019 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/test_column.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7850 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/test_custom_actions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1223 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/test_helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29338 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/test_row.py
+-rw-r--r--   0 runner    (1001) docker     (123)      858 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/test_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1497 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/test_variable_replacer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.388090 mage-ai-0.8.9/mage_ai/tests/data_preparation/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_preparation/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.388090 mage-ai-0.8.9/mage_ai/tests/data_preparation/models/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_preparation/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12895 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_preparation/models/test_block.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26721 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_preparation/models/test_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4800 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_preparation/models/test_variable.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23686 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_preparation/test_templates.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4152 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/data_preparation/test_variable_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2576 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/factory.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.388090 mage-ai-0.8.9/mage_ai/tests/io/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/io/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7425 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/io/test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2453 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/io/test_export_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.392090 mage-ai-0.8.9/mage_ai/tests/orchestration/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/orchestration/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.392090 mage-ai-0.8.9/mage_ai/tests/orchestration/db/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/orchestration/db/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7974 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/orchestration/db/test_models.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.392090 mage-ai-0.8.9/mage_ai/tests/orchestration/notification/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/orchestration/notification/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      826 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/orchestration/notification/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1859 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/orchestration/notification/test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5749 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/orchestration/notification/test_sender.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.396090 mage-ai-0.8.9/mage_ai/tests/orchestration/queue/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/orchestration/queue/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1594 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/orchestration/queue/test_process_queue.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3540 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/orchestration/test_execution_process_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1535 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/orchestration/test_job_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6350 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/orchestration/test_pipeline_scheduler.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.396090 mage-ai-0.8.9/mage_ai/tests/orchestration/triggers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/orchestration/triggers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      461 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/orchestration/triggers/test_event_trigger.py
+-rw-r--r--   0 runner    (1001) docker     (123)      541 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/orchestration/triggers/test_loop_time_trigger.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.396090 mage-ai-0.8.9/mage_ai/tests/services/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/services/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.396090 mage-ai-0.8.9/mage_ai/tests/services/aws/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/services/aws/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.396090 mage-ai-0.8.9/mage_ai/tests/services/aws/s3/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/services/aws/s3/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2310 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/services/aws/s3/test_s3.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.396090 mage-ai-0.8.9/mage_ai/tests/services/datadog/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/services/datadog/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2254 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/services/datadog/test_datadog.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.400090 mage-ai-0.8.9/mage_ai/tests/services/k8s/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/services/k8s/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6210 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/services/k8s/test_job_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.400090 mage-ai-0.8.9/mage_ai/tests/shared/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/shared/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1574 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/shared/test_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)      475 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/shared/test_retry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.400090 mage-ai-0.8.9/mage_ai/tests/streaming/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/streaming/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.400090 mage-ai-0.8.9/mage_ai/tests/streaming/sinks/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/streaming/sinks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1041 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/streaming/sinks/test_kinesis.py
+-rw-r--r--   0 runner    (1001) docker     (123)      957 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/streaming/sinks/test_opensearch.py
+-rw-r--r--   0 runner    (1001) docker     (123)      949 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/streaming/sinks/test_sink_factory.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.404090 mage-ai-0.8.9/mage_ai/tests/streaming/sources/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/streaming/sources/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1033 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/streaming/sources/test_azure_event_hub.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2115 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/streaming/sources/test_kafka.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1030 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/streaming/sources/test_kinesis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1379 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/streaming/sources/test_rabbitmq.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2057 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/streaming/sources/test_source_factory.py
+-rw-r--r--   0 runner    (1001) docker     (123)      838 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/tests/test_shared.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.404090 mage-ai-0.8.9/mage_ai/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      665 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/utils/code.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.404090 mage-ai-0.8.9/mage_ai/utils/logger/
+-rw-r--r--   0 runner    (1001) docker     (123)     2518 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/utils/logger/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      271 2023-02-26 23:52:57.000000 mage-ai-0.8.9/mage_ai/utils/logger/constants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 23:53:03.064087 mage-ai-0.8.9/mage_ai.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    14948 2023-02-26 23:53:02.000000 mage-ai-0.8.9/mage_ai.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    45413 2023-02-26 23:53:03.000000 mage-ai-0.8.9/mage_ai.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-26 23:53:02.000000 mage-ai-0.8.9/mage_ai.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       46 2023-02-26 23:53:02.000000 mage-ai-0.8.9/mage_ai.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1990 2023-02-26 23:53:02.000000 mage-ai-0.8.9/mage_ai.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-02-26 23:53:02.000000 mage-ai-0.8.9/mage_ai.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       85 2023-02-26 23:52:57.000000 mage-ai-0.8.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     1318 2023-02-26 23:52:57.000000 mage-ai-0.8.9/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-26 23:53:03.404090 mage-ai-0.8.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     3749 2023-02-26 23:52:57.000000 mage-ai-0.8.9/setup.py
```

### Comparing `mage-ai-0.8.8/LICENSE` & `mage-ai-0.8.9/LICENSE`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/PKG-INFO` & `mage-ai-0.8.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mage-ai
-Version: 0.8.8
+Version: 0.8.9
 Summary: Mage is a tool for building and deploying data pipelines.
 Home-page: https://github.com/mage-ai/mage-ai
 Author: Mage
 Author-email: eng@mage.ai
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: OS Independent
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: mage-ai Version: 0.8.8 Summary: Mage is a tool for
+Metadata-Version: 2.1 Name: mage-ai Version: 0.8.9 Summary: Mage is a tool for
 building and deploying data pipelines. Home-page: https://github.com/mage-ai/
 mage-ai Author: Mage Author-email: eng@mage.ai Classifier: Programming Language
 :: Python :: 3 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: OS Independent Requires-Python: >=3.6
 Description-Content-Type: text/markdown Provides-Extra: azure Provides-Extra:
 bigquery Provides-Extra: dbt Provides-Extra: google-cloud-storage Provides-
 Extra: hdf5 Provides-Extra: mysql Provides-Extra: postgres Provides-Extra:
```

### Comparing `mage-ai-0.8.8/README.md` & `mage-ai-0.8.9/README.md`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/__init__.py` & `mage-ai-0.8.9/mage_ai/__init__.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/errors.py` & `mage-ai-0.8.9/mage_ai/api/errors.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/middleware.py` & `mage-ai-0.8.9/mage_ai/api/middleware.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/monitors/BaseMonitor.py` & `mage-ai-0.8.9/mage_ai/api/monitors/BaseMonitor.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/operations/base.py` & `mage-ai-0.8.9/mage_ai/api/operations/base.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/AutocompleteItemPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/AutocompleteItemPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/BackfillPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/BackfillPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/BasePolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/BasePolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/BlockPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/BlockPolicy.py`

 * *Files 4% similar despite different names*

```diff
@@ -48,14 +48,15 @@
 
 BlockPolicy.allow_write([
     'color',
     'config',
     'configuration',
     'content',
     'converted_from',
+    'has_callback',
     'language',
     'metadata',
     'name',
     'priority',
     'type',
     'upstream_blocks',
     'uuid',
@@ -69,14 +70,15 @@
     'all_upstream_blocks_executed',
     'color',
     'configuration',
     'content',
     'downstream_blocks',
     'executor_config',
     'executor_type',
+    'has_callback',
     'language',
     'metadata',
     'name',
     'outputs',
     'status',
     'type',
     'upstream_blocks',
```

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/BlockRunPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/BlockRunPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/ClusterPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/ClusterPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/DataProviderPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/DataProviderPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/EventRulePolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/EventRulePolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/FileContentPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/FileContentPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/FilePolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/FilePolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/IntegrationDestinationPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/IntegrationDestinationPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/IntegrationSourcePolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/IntegrationSourcePolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/IntegrationSourceStreamPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/IntegrationSourceStreamPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/KernelPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/KernelPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/LogPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/LogPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/MonitorStatPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/MonitorStatPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/OutputPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/OutputPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/PipelinePolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/PipelinePolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/PipelineRunPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/PipelineRunPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/PipelineSchedulePolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/PipelineSchedulePolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/ProjectPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/ProjectPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/SecretPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/SecretPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/SessionPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/SessionPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/UserPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/UserPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/VariablePolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/VariablePolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/policies/WidgetPolicy.py` & `mage-ai-0.8.9/mage_ai/api/policies/WidgetPolicy.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/presenters/BackfillPresenter.py` & `mage-ai-0.8.9/mage_ai/api/presenters/BackfillPresenter.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/presenters/BasePresenter.py` & `mage-ai-0.8.9/mage_ai/api/presenters/BasePresenter.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/presenters/BlockPresenter.py` & `mage-ai-0.8.9/mage_ai/api/presenters/BlockPresenter.py`

 * *Files 1% similar despite different names*

```diff
@@ -10,14 +10,15 @@
     default_attributes = [
         'all_upstream_blocks_executed',
         'color',
         'configuration',
         'downstream_blocks',
         'executor_config',
         'executor_type',
+        'has_callback',
         'language',
         'metadata',
         'name',
         'status',
         'type',
         'upstream_blocks',
         'uuid',
```

### Comparing `mage-ai-0.8.8/mage_ai/api/presenters/IntegrationSourcePresenter.py` & `mage-ai-0.8.9/mage_ai/api/presenters/IntegrationSourcePresenter.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/presenters/PipelinePresenter.py` & `mage-ai-0.8.9/mage_ai/api/presenters/PipelinePresenter.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/presenters/PipelineRunPresenter.py` & `mage-ai-0.8.9/mage_ai/api/presenters/PipelineRunPresenter.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/presenters/PipelineSchedulePresenter.py` & `mage-ai-0.8.9/mage_ai/api/presenters/PipelineSchedulePresenter.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/presenters/WidgetPresenter.py` & `mage-ai-0.8.9/mage_ai/api/presenters/WidgetPresenter.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/presenters/mixins/users.py` & `mage-ai-0.8.9/mage_ai/api/presenters/mixins/users.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/AutocompleteItemResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/AutocompleteItemResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/BackfillResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/BackfillResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/BaseResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/BaseResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/BlockResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/BlockResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/BlockRunResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/BlockRunResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/ClusterResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/ClusterResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/DataProviderResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/DataProviderResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/DatabaseResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/DatabaseResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/FileContentResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/FileContentResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/FileResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/FileResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/IntegrationDestinationResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/IntegrationDestinationResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/IntegrationSourceResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/IntegrationSourceResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/KernelResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/KernelResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/LogResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/LogResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/MonitorStatResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/MonitorStatResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/OutputResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/OutputResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/PipelineResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/PipelineResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/PipelineRunResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/PipelineRunResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/PipelineScheduleResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/PipelineScheduleResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/ProjectResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/ProjectResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/SecretResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/SecretResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/SessionResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/SessionResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/UserResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/UserResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/VariableResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/VariableResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/WidgetResource.py` & `mage-ai-0.8.9/mage_ai/api/resources/WidgetResource.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/resources/shared/collective_loaders.py` & `mage-ai-0.8.9/mage_ai/api/resources/shared/collective_loaders.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/result_set.py` & `mage-ai-0.8.9/mage_ai/api/result_set.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/utils.py` & `mage-ai-0.8.9/mage_ai/api/utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/api/views.py` & `mage-ai-0.8.9/mage_ai/api/views.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/authentication/oauth2.py` & `mage-ai-0.8.9/mage_ai/authentication/oauth2.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/authentication/passwords.py` & `mage-ai-0.8.9/mage_ai/authentication/passwords.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/autocomplete/utils.py` & `mage-ai-0.8.9/mage_ai/autocomplete/utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/cli/main.py` & `mage-ai-0.8.9/mage_ai/cli/main.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/cli/utils.py` & `mage-ai-0.8.9/mage_ai/cli/utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/cluster_manager/aws/ecs_task_manager.py` & `mage-ai-0.8.9/mage_ai/cluster_manager/aws/ecs_task_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/cluster_manager/aws/emr_cluster_manager.py` & `mage-ai-0.8.9/mage_ai/cluster_manager/aws/emr_cluster_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/cluster_manager/constants.py` & `mage-ai-0.8.9/mage_ai/cluster_manager/constants.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/cluster_manager/gcp/cloud_run_service_manager.py` & `mage-ai-0.8.9/mage_ai/cluster_manager/gcp/cloud_run_service_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/cluster_manager/kubernetes/workload_manager.py` & `mage-ai-0.8.9/mage_ai/cluster_manager/kubernetes/workload_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/analysis/calculator.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/analysis/calculator.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/analysis/charts.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/analysis/charts.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/base.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/base.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/clean_column_names.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/clean_column_names.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/fix_syntax_errors.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/fix_syntax_errors.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/impute_values.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/impute_values.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/reformat_values.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/reformat_values.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/remove_collinear_columns.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/remove_collinear_columns.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/remove_columns_with_high_empty_rate.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/remove_columns_with_high_empty_rate.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/remove_columns_with_single_value.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/remove_columns_with_single_value.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/remove_duplicate_rows.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/remove_duplicate_rows.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/cleaning_rules/remove_outliers.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/cleaning_rules/remove_outliers.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/column_types/column_type_detector.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/column_types/column_type_detector.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/column_types/constants.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/column_types/constants.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/data_cleaner.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/data_cleaner.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/estimators/encoders.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/estimators/encoders.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/estimators/outlier_removal.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/estimators/outlier_removal.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/pipelines/base.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/pipelines/base.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/shared/utils.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/shared/utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/statistics/calculator.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/statistics/calculator.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/action_code.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/action_code.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/base.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/base.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/column.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/column.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/constants.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/constants.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/custom_action.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/custom_action.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/dependency_resolution.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/dependency_resolution.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/helpers.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/helpers.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/row.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/row.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/shared.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/shared.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/spark/constants.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/spark/constants.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/spark/transformers.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/spark/transformers.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/addition.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/addition.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/base.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/base.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/date_trunc.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/date_trunc.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/difference.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/difference.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/distance_between.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/distance_between.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/udf/if_else.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/udf/if_else.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/utils.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_cleaner/transformer_actions/variable_replacer.py` & `mage-ai-0.8.9/mage_ai/data_cleaner/transformer_actions/variable_replacer.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_integrations/logger/utils.py` & `mage-ai-0.8.9/mage_ai/data_integrations/logger/utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_integrations/sources/constants.py` & `mage-ai-0.8.9/mage_ai/data_integrations/sources/constants.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_integrations/utils/config.py` & `mage-ai-0.8.9/mage_ai/data_integrations/utils/config.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_integrations/utils/parsers.py` & `mage-ai-0.8.9/mage_ai/data_integrations/utils/parsers.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_integrations/utils/scheduler.py` & `mage-ai-0.8.9/mage_ai/data_integrations/utils/scheduler.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/decorators.py` & `mage-ai-0.8.9/mage_ai/data_preparation/decorators.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/executors/block_executor.py` & `mage-ai-0.8.9/mage_ai/data_preparation/executors/block_executor.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/executors/ecs_block_executor.py` & `mage-ai-0.8.9/mage_ai/data_preparation/executors/ecs_block_executor.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/executors/executor_factory.py` & `mage-ai-0.8.9/mage_ai/data_preparation/executors/executor_factory.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/executors/gcp_cloud_run_block_executor.py` & `mage-ai-0.8.9/mage_ai/data_preparation/executors/gcp_cloud_run_block_executor.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/executors/k8s_block_executor.py` & `mage-ai-0.8.9/mage_ai/data_preparation/executors/k8s_block_executor.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/executors/pipeline_executor.py` & `mage-ai-0.8.9/mage_ai/data_preparation/executors/pipeline_executor.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/executors/pyspark_block_executor.py` & `mage-ai-0.8.9/mage_ai/data_preparation/executors/pyspark_block_executor.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/executors/pyspark_pipeline_executor.py` & `mage-ai-0.8.9/mage_ai/data_preparation/executors/pyspark_pipeline_executor.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/executors/streaming_pipeline_executor.py` & `mage-ai-0.8.9/mage_ai/data_preparation/executors/streaming_pipeline_executor.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/logging/gcs_logger_manager.py` & `mage-ai-0.8.9/mage_ai/data_preparation/logging/gcs_logger_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/logging/logger.py` & `mage-ai-0.8.9/mage_ai/data_preparation/logging/logger.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/logging/logger_manager.py` & `mage-ai-0.8.9/mage_ai/data_preparation/logging/logger_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/logging/logger_manager_factory.py` & `mage-ai-0.8.9/mage_ai/data_preparation/logging/logger_manager_factory.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/logging/s3_logger_manager.py` & `mage-ai-0.8.9/mage_ai/data_preparation/logging/s3_logger_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/block/__init__.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/block/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -856,18 +856,20 @@
             global_vars,
             dynamic_block_index=dynamic_block_index,
             dynamic_upstream_block_uuids=dynamic_upstream_block_uuids,
         )
 
         outputs_from_input_vars = {}
         if input_args is None:
+            upstream_block_uuids_length = len(upstream_block_uuids)
             for idx, input_var in enumerate(input_vars):
-                upstream_block_uuid = upstream_block_uuids[idx]
-                outputs_from_input_vars[upstream_block_uuid] = input_var
-                outputs_from_input_vars[f'df_{idx + 1}'] = input_var
+                if idx < upstream_block_uuids_length:
+                    upstream_block_uuid = upstream_block_uuids[idx]
+                    outputs_from_input_vars[upstream_block_uuid] = input_var
+                    outputs_from_input_vars[f'df_{idx + 1}'] = input_var
         else:
             outputs_from_input_vars = dict()
 
         with redirect_stdout(stdout):
             outputs = self._execute_block(
                 outputs_from_input_vars,
                 custom_code=custom_code,
```

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/block/constants.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/block/constants.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/block/dbt/__init__.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/block/dbt/__init__.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/block/dbt/utils/__init__.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/block/dbt/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/block/integration/__init__.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/block/integration/__init__.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/block/r/__init__.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/block/r/__init__.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/__init__.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/__init__.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/bigquery.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/bigquery.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/mysql.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/mysql.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/postgres.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/postgres.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/redshift.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/redshift.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/snowflake.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/snowflake.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/trino.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/trino.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/block/sql/utils/shared.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/block/sql/utils/shared.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/block/utils.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/block/utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/constants.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/constants.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/file.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/file.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/pipeline.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/pipeline.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/pipelines/integration_pipeline.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/pipelines/integration_pipeline.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/utils.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/variable.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/variable.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/widget/__init__.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/widget/__init__.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/widget/charts.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/widget/charts.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/widget/constants.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/widget/constants.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/models/widget/utils.py` & `mage-ai-0.8.9/mage_ai/data_preparation/models/widget/utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/repo_manager.py` & `mage-ai-0.8.9/mage_ai/data_preparation/repo_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/shared/secrets.py` & `mage-ai-0.8.9/mage_ai/data_preparation/shared/secrets.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/shared/stream.py` & `mage-ai-0.8.9/mage_ai/data_preparation/shared/stream.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/storage/base_storage.py` & `mage-ai-0.8.9/mage_ai/data_preparation/storage/base_storage.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/storage/local_storage.py` & `mage-ai-0.8.9/mage_ai/data_preparation/storage/local_storage.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/storage/s3_storage.py` & `mage-ai-0.8.9/mage_ai/data_preparation/storage/s3_storage.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/storage/utils.py` & `mage-ai-0.8.9/mage_ai/data_preparation/storage/utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/azure_blob_storage.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/azure_blob_storage.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/bigquery.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/bigquery.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/google_cloud_storage.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/google_cloud_storage.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/mysql.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/mysql.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/postgres.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/postgres.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/redshift.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/redshift.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/s3.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/s3.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_exporters/snowflake.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_exporters/snowflake.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/azure_blob_storage.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/azure_blob_storage.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/bigquery.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/bigquery.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/file.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/file.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/google_cloud_storage.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/google_cloud_storage.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/mysql.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/mysql.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/postgres.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/postgres.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/pyspark/s3.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/pyspark/s3.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/redshift.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/redshift.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/s3.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/s3.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/data_loaders/snowflake.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/data_loaders/snowflake.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/pipeline_execution/emr_bootstrap.sh` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/pipeline_execution/emr_bootstrap.sh`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/pipeline_execution/spark_script.jinja` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/pipeline_execution/spark_script.jinja`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/data_loaders/load_titanic.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/data_loaders/load_titanic.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/io_config.yaml` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/io_config.yaml`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/metadata.yaml` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/metadata.yaml`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/pipelines/example_pipeline/metadata.yaml` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/pipelines/example_pipeline/metadata.yaml`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/repo/transformers/fill_in_missing_values.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/repo/transformers/fill_in_missing_values.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/sensors/s3.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/sensors/s3.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/template.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/template.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/data_warehouse_transformer.jinja` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/data_warehouse_transformer.jinja`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/default.jinja` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/default.jinja`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/default_pyspark.jinja` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/default_pyspark.jinja`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/suggestion_fmt.jinja` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/suggestion_fmt.jinja`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/action.jinja` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/action.jinja`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/average.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/average.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/count.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/count.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/count_distinct.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/count_distinct.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/diff.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/diff.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/first.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/first.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/fix_syntax_errors.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/fix_syntax_errors.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/impute.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/impute.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/last.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/last.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/max.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/max.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/median.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/median.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/min.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/min.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/remove_outliers.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/remove_outliers.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/shift_down.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/shift_down.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/shift_up.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/shift_up.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/column/sum.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/column/sum.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/transformers/transformer_actions/row/drop_duplicate.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/transformers/transformer_actions/row/drop_duplicate.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/templates/utils.py` & `mage-ai-0.8.9/mage_ai/data_preparation/templates/utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/utils/block/convert_content.py` & `mage-ai-0.8.9/mage_ai/data_preparation/utils/block/convert_content.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/data_preparation/variable_manager.py` & `mage-ai-0.8.9/mage_ai/data_preparation/variable_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/azure_blob_storage.py` & `mage-ai-0.8.9/mage_ai/io/azure_blob_storage.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/base.py` & `mage-ai-0.8.9/mage_ai/io/base.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/bigquery.py` & `mage-ai-0.8.9/mage_ai/io/bigquery.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/config.py` & `mage-ai-0.8.9/mage_ai/io/config.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/export_utils.py` & `mage-ai-0.8.9/mage_ai/io/export_utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/file.py` & `mage-ai-0.8.9/mage_ai/io/file.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/google_cloud_storage.py` & `mage-ai-0.8.9/mage_ai/io/google_cloud_storage.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/io_config.py` & `mage-ai-0.8.9/mage_ai/io/io_config.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/mysql.py` & `mage-ai-0.8.9/mage_ai/io/mysql.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/postgres.py` & `mage-ai-0.8.9/mage_ai/io/postgres.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/redshift.py` & `mage-ai-0.8.9/mage_ai/io/redshift.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/s3.py` & `mage-ai-0.8.9/mage_ai/io/s3.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/snowflake.py` & `mage-ai-0.8.9/mage_ai/io/snowflake.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/sql.py` & `mage-ai-0.8.9/mage_ai/io/sql.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/trino.py` & `mage-ai-0.8.9/mage_ai/io/trino.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/io/utils.py` & `mage-ai-0.8.9/mage_ai/io/utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/airflow.py` & `mage-ai-0.8.9/mage_ai/orchestration/airflow.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/backfills/service.py` & `mage-ai-0.8.9/mage_ai/orchestration/backfills/service.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/__init__.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/__init__.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/alembic.ini` & `mage-ai-0.8.9/mage_ai/orchestration/db/alembic.ini`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/database_manager.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/database_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/env.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/env.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/053ee2c10d85_add_completed_at.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/053ee2c10d85_add_completed_at.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/067326f43bc3_add_variables_to_pipelinerun.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/067326f43bc3_add_variables_to_pipelinerun.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/1d8e65aeefdd_add_settings_to_pipeline_schedule.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/1d8e65aeefdd_add_settings_to_pipeline_schedule.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/1f9353eddbc6_add_secrets_table.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/1f9353eddbc6_add_secrets_table.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/2266370f589b_add_indexes_to_pipeline_run.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/2266370f589b_add_indexes_to_pipeline_run.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/26305e46df52_create_backfills_table.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/26305e46df52_create_backfills_table.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/3fafd217efa7_add_event_matcher_model.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/3fafd217efa7_add_event_matcher_model.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/52ab80005742_add_variables_to_pipeline_schedule.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/52ab80005742_add_variables_to_pipeline_schedule.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/5cd59ec4cf1d_add_passed_sla_to_pipeline_run.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/5cd59ec4cf1d_add_passed_sla_to_pipeline_run.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/643b6e65e814_add_unique_indexes_on_authentication_.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/643b6e65e814_add_unique_indexes_on_authentication_.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/6aecc9bc451c_update_schedule_type_enum.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/6aecc9bc451c_update_schedule_type_enum.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/7ac6fed06918_add_token_column_to_pipeline_schedule_.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/7ac6fed06918_add_token_column_to_pipeline_schedule_.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/84de4cdd6126_add_sla_to_pipeline_schedule.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/84de4cdd6126_add_sla_to_pipeline_schedule.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/8971d4cd5b39_add_event_variables_and_metadata_to_.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/8971d4cd5b39_add_event_variables_and_metadata_to_.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/97ff9f55a3c0_create_users_oauth2_applications_and_.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/97ff9f55a3c0_create_users_oauth2_applications_and_.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/b01be687e537_add_started_at_to_block_run.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/b01be687e537_add_started_at_to_block_run.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/c07a23ff782b_add_initial_tables.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/c07a23ff782b_add_initial_tables.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/migrations/versions/ec5df57a1c60_add_metrics_to_block_runs.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/migrations/versions/ec5df57a1c60_add_metrics_to_block_runs.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/models.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/models.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/db/process.py` & `mage-ai-0.8.9/mage_ai/orchestration/db/process.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/execution_process_manager.py` & `mage-ai-0.8.9/mage_ai/orchestration/execution_process_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/job_manager.py` & `mage-ai-0.8.9/mage_ai/orchestration/job_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/metrics/pipeline_run.py` & `mage-ai-0.8.9/mage_ai/orchestration/metrics/pipeline_run.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/monitor/monitor_stats.py` & `mage-ai-0.8.9/mage_ai/orchestration/monitor/monitor_stats.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/notification/config.py` & `mage-ai-0.8.9/mage_ai/orchestration/notification/config.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/notification/sender.py` & `mage-ai-0.8.9/mage_ai/orchestration/notification/sender.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/pipeline_scheduler.py` & `mage-ai-0.8.9/mage_ai/orchestration/pipeline_scheduler.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/queue/celery_queue.py` & `mage-ai-0.8.9/mage_ai/orchestration/queue/celery_queue.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/queue/process_queue.py` & `mage-ai-0.8.9/mage_ai/orchestration/queue/process_queue.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/queue/queue_factory.py` & `mage-ai-0.8.9/mage_ai/orchestration/queue/queue_factory.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/run_status_checker.py` & `mage-ai-0.8.9/mage_ai/orchestration/run_status_checker.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/orchestration/utils/resources.py` & `mage-ai-0.8.9/mage_ai/orchestration/utils/resources.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/sample_datasets/__init__.py` & `mage-ai-0.8.9/mage_ai/sample_datasets/__init__.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/sample_datasets/product_purchases.csv` & `mage-ai-0.8.9/mage_ai/sample_datasets/product_purchases.csv`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/sample_datasets/salary_survey.csv` & `mage-ai-0.8.9/mage_ai/sample_datasets/salary_survey.csv`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/sample_datasets/titanic_survival.csv` & `mage-ai-0.8.9/mage_ai/sample_datasets/titanic_survival.csv`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/sample_datasets/user_emails.csv` & `mage-ai-0.8.9/mage_ai/sample_datasets/user_emails.csv`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/active_kernel.py` & `mage-ai-0.8.9/mage_ai/server/active_kernel.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/api/base.py` & `mage-ai-0.8.9/mage_ai/server/api/base.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/api/blocks.py` & `mage-ai-0.8.9/mage_ai/server/api/blocks.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/api/clusters.py` & `mage-ai-0.8.9/mage_ai/server/api/clusters.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/api/events.py` & `mage-ai-0.8.9/mage_ai/server/api/events.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/api/integration_sources.py` & `mage-ai-0.8.9/mage_ai/server/api/integration_sources.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/api/projects.py` & `mage-ai-0.8.9/mage_ai/server/api/projects.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/api/triggers.py` & `mage-ai-0.8.9/mage_ai/server/api/triggers.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/api/v1.py` & `mage-ai-0.8.9/mage_ai/server/api/v1.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/app.py` & `mage-ai-0.8.9/mage_ai/server/app.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/client/mage.py` & `mage-ai-0.8.9/mage_ai/server/client/mage.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/data/base.py` & `mage-ai-0.8.9/mage_ai/server/data/base.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/data/models.py` & `mage-ai-0.8.9/mage_ai/server/data/models.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/docs_server.py` & `mage-ai-0.8.9/mage_ai/server/docs_server.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/execution_manager.py` & `mage-ai-0.8.9/mage_ai/server/execution_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/404.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/404.html`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>404: This page could not be found</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/pages/_error-235304e5badb19eb.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>404: This page could not be found</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/pages/_error-235304e5badb19eb.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -15,8 +15,8 @@
                   border-right: 1px solid rgba(0, 0, 0, .3);
                 }
                 @media (prefers-color-scheme: dark) {
                   body { color: #fff; background: #000; }
                   .next-error-h1 {
                     border-right: 1px solid rgba(255, 255, 255, .3);
                   }
-                }</style><h1 class="next-error-h1" style="display:inline-block;margin:0;margin-right:20px;padding:10px 23px 10px 0;font-size:24px;font-weight:500;vertical-align:top">404<!-- --></h1><div style="display:inline-block;text-align:left;line-height:49px;height:49px;vertical-align:middle"><h2 style="font-size:14px;font-weight:normal;line-height:inherit;margin:0;padding:0">This page could not be found<!-- -->.<!-- --></h2></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"statusCode":404},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/_error","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+                }</style><h1 class="next-error-h1" style="display:inline-block;margin:0;margin-right:20px;padding:10px 23px 10px 0;font-size:24px;font-weight:500;vertical-align:top">404<!-- --></h1><div style="display:inline-block;text-align:left;line-height:49px;height:49px;vertical-align:middle"><h2 style="font-size:14px;font-weight:normal;line-height:inherit;margin:0;padding:0">This page could not be found<!-- -->.<!-- --></h2></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"statusCode":404},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/_error","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/404.html.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/404.html.html`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>404: This page could not be found</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/pages/_error-235304e5badb19eb.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>404: This page could not be found</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/pages/_error-235304e5badb19eb.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -15,8 +15,8 @@
                   border-right: 1px solid rgba(0, 0, 0, .3);
                 }
                 @media (prefers-color-scheme: dark) {
                   body { color: #fff; background: #000; }
                   .next-error-h1 {
                     border-right: 1px solid rgba(255, 255, 255, .3);
                   }
-                }</style><h1 class="next-error-h1" style="display:inline-block;margin:0;margin-right:20px;padding:10px 23px 10px 0;font-size:24px;font-weight:500;vertical-align:top">404<!-- --></h1><div style="display:inline-block;text-align:left;line-height:49px;height:49px;vertical-align:middle"><h2 style="font-size:14px;font-weight:normal;line-height:inherit;margin:0;padding:0">This page could not be found<!-- -->.<!-- --></h2></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"statusCode":404},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/_error","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+                }</style><h1 class="next-error-h1" style="display:inline-block;margin:0;margin-right:20px;padding:10px 23px 10px 0;font-size:24px;font-weight:500;vertical-align:top">404<!-- --></h1><div style="display:inline-block;text-align:left;line-height:49px;height:49px;vertical-align:middle"><h2 style="font-size:14px;font-weight:normal;line-height:inherit;margin:0;padding:0">This page could not be found<!-- -->.<!-- --></h2></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"statusCode":404},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/_error","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/1150.1378afaa474df64a.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/1150.1378afaa474df64a.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/1240.0819f45820d22263.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/1240.0819f45820d22263.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/1286-a62050b3f897c6be.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/1286-a62050b3f897c6be.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/1450.d383f64c169d4278.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/1450.d383f64c169d4278.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/1774-aa51ef1da7217ff9.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/1774-aa51ef1da7217ff9.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/1830-cb1bbbf9a9c54649.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/1830-cb1bbbf9a9c54649.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2083-78a438dbdc57d1e4.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2083-78a438dbdc57d1e4.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2125-0b537dc53fe71b18.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2125-0b537dc53fe71b18.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2249-70929b8c547bbc18.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2249-70929b8c547bbc18.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2426-be3e2bc6625de582.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2426-be3e2bc6625de582.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2481.0454a0e25dc7e027.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2481.0454a0e25dc7e027.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2508.724531e7f9cf5f36.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2508.724531e7f9cf5f36.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2524-6aeb9419acf5d1b4.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2524-6aeb9419acf5d1b4.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2545.8371b39c898ae92b.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2545.8371b39c898ae92b.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/261.0a24b4ece1d29aa1.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/261.0a24b4ece1d29aa1.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/266.e301071d22592682.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/266.e301071d22592682.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/2714-1e79e9f2e998b544.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/2714-1e79e9f2e998b544.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/29107295-989a0767a635d9d5.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/29107295-989a0767a635d9d5.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/3453.992f4b1667e9882c.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/3453.992f4b1667e9882c.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/3467.38cd0654ba6f788f.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/3467.38cd0654ba6f788f.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/3835.df296b4e4078e985.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/3835.df296b4e4078e985.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/3850-6395783d820def1c.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/3850-6395783d820def1c.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/3873.4b3eace753998412.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/3873.4b3eace753998412.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/3898.880191695bb05845.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/3898.880191695bb05845.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4042.5e16d36209052351.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4042.5e16d36209052351.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4092.536ee541241f4538.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4092.536ee541241f4538.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/434-69ddfacd3e93f2db.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/434-69ddfacd3e93f2db.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4388.04098706f32e69e7.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4388.04098706f32e69e7.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/440.3ab77942f659ea0c.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/440.3ab77942f659ea0c.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4450.79f14f763d55c63e.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4450.79f14f763d55c63e.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4454.13a2404adecaa39e.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4454.13a2404adecaa39e.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4463-1b9ce74c6e1bb14e.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4463-1b9ce74c6e1bb14e.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4495-4f0340aa82e0c623.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4495-4f0340aa82e0c623.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4776.753ad29fa0a29a4a.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4776.753ad29fa0a29a4a.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4804-01a10103ebe26ca8.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4804-01a10103ebe26ca8.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4846-b4ced91dc0e9fba9.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4846-b4ced91dc0e9fba9.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/4883.a5bb0edbf8f3cc8f.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/4883.a5bb0edbf8f3cc8f.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5008.29c2662ecc2b04c7.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5008.29c2662ecc2b04c7.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5104.1edcf4437c471dd4.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5104.1edcf4437c471dd4.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5164.857023e800905b6f.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5164.857023e800905b6f.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5729.0f2748e9e6dab951.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5729.0f2748e9e6dab951.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5824.628653557e904674.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5824.628653557e904674.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5872-103815a4a043489b.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5872-103815a4a043489b.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5896-f84e336fb8877027.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5896-f84e336fb8877027.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/5944-757b7898608a65e1.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/5944-757b7898608a65e1.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6042.c59010de9e699437.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6042.c59010de9e699437.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6085-692d2f784c0504f2.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6085-692d2f784c0504f2.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6115.0c85e507543394ea.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6115.0c85e507543394ea.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6116.871a682ddf535aca.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6116.871a682ddf535aca.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6434.10380ee0968636ba.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6434.10380ee0968636ba.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6443.7b6d2b4e51018184.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6443.7b6d2b4e51018184.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6507.d3a17777d2c294e6.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6507.d3a17777d2c294e6.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6532-a614f9e1f9434872.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6532-a614f9e1f9434872.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6579-2b5d8d39472d85c0.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6579-2b5d8d39472d85c0.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6641-a0ed2bd8f5dc777b.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6641-a0ed2bd8f5dc777b.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/6958.8f39c585d36737a7.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/6958.8f39c585d36737a7.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/7011-81dd8269c4806d26.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/7011-81dd8269c4806d26.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/704-4de8946d753a578a.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/704-4de8946d753a578a.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/72fdc299.2d5ec188af5d0049.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/72fdc299.2d5ec188af5d0049.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/739.3d24945544b37e52.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/739.3d24945544b37e52.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/7400-1430ec3874c1fdee.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/7400-1430ec3874c1fdee.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/792.010ca00d79b2112f.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/792.010ca00d79b2112f.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/7947.77be4bec4d47774e.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/7947.77be4bec4d47774e.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/7951.fee8b6c27c9ef777.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/7951.fee8b6c27c9ef777.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8018.968bf87c390e3312.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8018.968bf87c390e3312.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8097.b0345f30a7390c1d.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8097.b0345f30a7390c1d.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8256.290ceb269b1ffe26.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8256.290ceb269b1ffe26.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/826.75268ee34f93393a.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/826.75268ee34f93393a.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8277.5003e1d94bb85156.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8277.5003e1d94bb85156.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8762.dff300f86bef8573.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8762.dff300f86bef8573.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8789-4f858e520d46973b.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8789-4f858e520d46973b.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8807.a68c69c8fe0a8c01.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8807.a68c69c8fe0a8c01.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8849.db0d50b4d84b09a6.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8849.db0d50b4d84b09a6.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8901.21d26d5a1ee473fe.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8901.21d26d5a1ee473fe.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8920.5700e380a2999098.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8920.5700e380a2999098.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/8961-697fe5d4db44d909.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/8961-697fe5d4db44d909.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9140-6f67e0879394373d.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9140-6f67e0879394373d.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9258.6c6ef544c701a011.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9258.6c6ef544c701a011.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9307.d4baf7aebbcef1f0.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9307.d4baf7aebbcef1f0.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9361.a0820e3069f5ef74.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9361.a0820e3069f5ef74.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9363.6b811b4c86277e07.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9363.6b811b4c86277e07.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9437.a3c32f45cf9ef69b.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9437.a3c32f45cf9ef69b.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9565-28e1c30511c95c2d.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9565-28e1c30511c95c2d.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9566.f8bd24768ed14ecb.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9566.f8bd24768ed14ecb.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9633.40e5056ca1e2b22a.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9633.40e5056ca1e2b22a.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9767-3f852fd90cf7857f.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9767-3f852fd90cf7857f.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9785.5ff26cb26d84d6a1.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9785.5ff26cb26d84d6a1.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9832-c8b8970bb522f302.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9832-c8b8970bb522f302.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9855.c4394a68322be9f8.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9855.c4394a68322be9f8.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9898-51ca6a904b7a2382.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9898-51ca6a904b7a2382.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/9927.e82a3e1e21990d77.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/9927.e82a3e1e21990d77.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/bd1a647f.6050372acaa5cc3c.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/bd1a647f.6050372acaa5cc3c.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/framework-7c365855dab1bf41.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/framework-7c365855dab1bf41.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/main-bb0dd5375146d7fd.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/main-bb0dd5375146d7fd.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/_app-0aed65f2e085822e.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/_app-0aed65f2e085822e.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/_error-235304e5badb19eb.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/_error-235304e5badb19eb.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/index-e34a68d2f6fe16f2.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/index-e34a68d2f6fe16f2.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/manage-54fd0434f4f5305c.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/manage-54fd0434f4f5305c.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipeline-runs-21fe37061bdaaaea.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipeline-runs-21fe37061bdaaaea.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/backfills/[...slug]-81e3c9ea75d7abb4.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/backfills/[...slug]-81e3c9ea75d7abb4.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/backfills-0ed0d70bc659c236.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/backfills-0ed0d70bc659c236.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/edit-1b8b406222fae908.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/edit-1b8b406222fae908.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/logs-5ccc75887776efb0.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/logs-5ccc75887776efb0.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/monitors/block-runs-8f23f7ca9efcb069.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/monitors/block-runs-8f23f7ca9efcb069.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/monitors/block-runtime-f83ab9de4094e1b0.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/monitors/block-runtime-f83ab9de4094e1b0.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/runs/[run]-73ced07cc98a4968.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/runs/[run]-73ced07cc98a4968.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/runs-67d23509a0c9a1b8.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/runs-67d23509a0c9a1b8.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/syncs-4084a44baf91f30e.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/syncs-4084a44baf91f30e.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/triggers/[...slug]-ae970171cfe98c51.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/triggers/[...slug]-ae970171cfe98c51.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/triggers-b0b91245d3299bdf.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/triggers-b0b91245d3299bdf.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]-ca9457e1a6bced4b.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]-ca9457e1a6bced4b.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines-12dc02ae431a6305.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines-12dc02ae431a6305.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/account/profile-acd7ee47219fee3d.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/account/profile-acd7ee47219fee3d.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/workspace/preferences-07bda506f68974fb.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/workspace/preferences-07bda506f68974fb.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/workspace/users-c128672e053a4c30.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/workspace/users-c128672e053a4c30.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings-d594a66a568306da.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/settings-d594a66a568306da.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/sign-in-b4e1eb529a184c60.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/sign-in-b4e1eb529a184c60.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/terminal-5d7c45bb058a3f20.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/terminal-5d7c45bb058a3f20.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/test-f567bdfcc1276249.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/test-f567bdfcc1276249.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/pages/triggers-e0172c422c95eda9.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/pages/triggers-e0172c422c95eda9.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/polyfills-5cd94c89d3acac5f.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/polyfills-5cd94c89d3acac5f.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/_next/static/css/d1e8e64d0b07af2f.css` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/_next/static/css/d1e8e64d0b07af2f.css`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/favicon.ico` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/favicon.ico`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Bold.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Bold.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Light.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Light.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Medium.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Medium.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Regular.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Regular.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Retina.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Retina.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-SemiBold.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-SemiBold.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/LICENSE.txt` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Black.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Black.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-BlackItalic.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-BlackItalic.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Bold.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Bold.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-BoldItalic.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-BoldItalic.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Italic.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Italic.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Light.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Light.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-LightItalic.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-LightItalic.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Medium.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Medium.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-MediumItalic.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-MediumItalic.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Regular.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Regular.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Thin.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-Thin.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-ThinItalic.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto/Roboto-ThinItalic.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/LICENSE.txt` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/README.txt` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/README.txt`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/RobotoMono-Italic-VariableFont_wght.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/RobotoMono-Italic-VariableFont_wght.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/RobotoMono-VariableFont_wght.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/RobotoMono-VariableFont_wght.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Bold.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Bold.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-BoldItalic.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-BoldItalic.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-ExtraLight.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-ExtraLight.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-ExtraLightItalic.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-ExtraLightItalic.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Italic.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Italic.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Light.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Light.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-LightItalic.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-LightItalic.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Medium.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Medium.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-MediumItalic.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-MediumItalic.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Regular.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Regular.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-SemiBold.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-SemiBold.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-SemiBoldItalic.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-SemiBoldItalic.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Thin.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-Thin.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-ThinItalic.ttf` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/fonts/Roboto_Mono/static/RobotoMono-ThinItalic.ttf`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/images/backfill.jpg` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/images/backfill.jpg`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/images/banner-shape-purple-peach.jpg` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/images/banner-shape-purple-peach.jpg`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/images/dashboard-api-key.webp` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/images/dashboard-api-key.webp`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/images/extra.jpg` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/images/extra.jpg`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/images/monitor.jpg` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/images/monitor.jpg`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/images/run B.jpg` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/images/run B.jpg`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/images/sessions/abstract.png` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/images/sessions/abstract.png`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/index.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/index.html`

 * *Files 3% similar despite different names*

```diff
@@ -1,12 +1,12 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><title>Mage</title><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/pages/index-e34a68d2f6fe16f2.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><title>Mage</title><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/pages/index-e34a68d2f6fe16f2.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--success{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--warning{background:#DD9900 !important;color:#FFFFFF !important;}/*!sc*/
 data-styled.g5[id="ToastWrapper-sc-1a33ph1-0"]{content:"kOVcuR,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/manage.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/syncs.html`

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Manage | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/8789-4f858e520d46973b.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/pages/manage-54fd0434f4f5305c.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/9565-28e1c30511c95c2d.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/syncs-4084a44baf91f30e.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -11,8 +11,10 @@
 data-styled.g5[id="ToastWrapper-sc-1a33ph1-0"]{content:"kOVcuR,"}/*!sc*/
 .dKQluW{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex:1;-ms-flex:1;flex:1;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}/*!sc*/
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/manage","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+.jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
+data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/syncs","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/pipeline-runs.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/settings/account/profile.html`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Pipeline runs | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/4846-b4ced91dc0e9fba9.js" defer=""></script><script src="/_next/static/chunks/pages/pipeline-runs-21fe37061bdaaaea.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Settings | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/9140-6f67e0879394373d.js" defer=""></script><script src="/_next/static/chunks/pages/settings/account/profile-acd7ee47219fee3d.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipeline-runs","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/settings/account/profile","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/backfills/[...slug].html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/runs.html`

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/4804-01a10103ebe26ca8.js" defer=""></script><script src="/_next/static/chunks/1774-aa51ef1da7217ff9.js" defer=""></script><script src="/_next/static/chunks/5872-103815a4a043489b.js" defer=""></script><script src="/_next/static/chunks/2524-6aeb9419acf5d1b4.js" defer=""></script><script src="/_next/static/chunks/4495-4f0340aa82e0c623.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/4463-1b9ce74c6e1bb14e.js" defer=""></script><script src="/_next/static/chunks/6532-a614f9e1f9434872.js" defer=""></script><script src="/_next/static/chunks/1286-a62050b3f897c6be.js" defer=""></script><script src="/_next/static/chunks/4846-b4ced91dc0e9fba9.js" defer=""></script><script src="/_next/static/chunks/8961-697fe5d4db44d909.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/backfills/%5B...slug%5D-81e3c9ea75d7abb4.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/4804-01a10103ebe26ca8.js" defer=""></script><script src="/_next/static/chunks/1774-aa51ef1da7217ff9.js" defer=""></script><script src="/_next/static/chunks/2524-6aeb9419acf5d1b4.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/4463-1b9ce74c6e1bb14e.js" defer=""></script><script src="/_next/static/chunks/6532-a614f9e1f9434872.js" defer=""></script><script src="/_next/static/chunks/4846-b4ced91dc0e9fba9.js" defer=""></script><script src="/_next/static/chunks/5944-757b7898608a65e1.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/runs-67d23509a0c9a1b8.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/backfills/[...slug]","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/runs","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/backfills.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/monitors.html`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/backfills-0ed0d70bc659c236.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/2714-1e79e9f2e998b544.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/2249-70929b8c547bbc18.js" defer=""></script><script src="/_next/static/chunks/7400-1430ec3874c1fdee.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/monitors-8b08ec1aef4af4f2.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/backfills","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/monitors","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/edit.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/edit.html`

 * *Files 3% similar despite different names*

```diff
@@ -1,12 +1,12 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/29107295-989a0767a635d9d5.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/4804-01a10103ebe26ca8.js" defer=""></script><script src="/_next/static/chunks/1774-aa51ef1da7217ff9.js" defer=""></script><script src="/_next/static/chunks/5872-103815a4a043489b.js" defer=""></script><script src="/_next/static/chunks/2524-6aeb9419acf5d1b4.js" defer=""></script><script src="/_next/static/chunks/9565-28e1c30511c95c2d.js" defer=""></script><script src="/_next/static/chunks/2714-1e79e9f2e998b544.js" defer=""></script><script src="/_next/static/chunks/2125-0b537dc53fe71b18.js" defer=""></script><script src="/_next/static/chunks/7011-81dd8269c4806d26.js" defer=""></script><script src="/_next/static/chunks/6085-692d2f784c0504f2.js" defer=""></script><script src="/_next/static/chunks/8789-4f858e520d46973b.js" defer=""></script><script src="/_next/static/chunks/704-4de8946d753a578a.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/4463-1b9ce74c6e1bb14e.js" defer=""></script><script src="/_next/static/chunks/6532-a614f9e1f9434872.js" defer=""></script><script src="/_next/static/chunks/1286-a62050b3f897c6be.js" defer=""></script><script src="/_next/static/chunks/2426-be3e2bc6625de582.js" defer=""></script><script src="/_next/static/chunks/6641-a0ed2bd8f5dc777b.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/edit-1b8b406222fae908.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/29107295-989a0767a635d9d5.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/4804-01a10103ebe26ca8.js" defer=""></script><script src="/_next/static/chunks/1774-aa51ef1da7217ff9.js" defer=""></script><script src="/_next/static/chunks/5872-103815a4a043489b.js" defer=""></script><script src="/_next/static/chunks/2524-6aeb9419acf5d1b4.js" defer=""></script><script src="/_next/static/chunks/9565-28e1c30511c95c2d.js" defer=""></script><script src="/_next/static/chunks/2714-1e79e9f2e998b544.js" defer=""></script><script src="/_next/static/chunks/2125-0b537dc53fe71b18.js" defer=""></script><script src="/_next/static/chunks/7011-81dd8269c4806d26.js" defer=""></script><script src="/_next/static/chunks/6085-692d2f784c0504f2.js" defer=""></script><script src="/_next/static/chunks/8789-4f858e520d46973b.js" defer=""></script><script src="/_next/static/chunks/704-4de8946d753a578a.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/4463-1b9ce74c6e1bb14e.js" defer=""></script><script src="/_next/static/chunks/6532-a614f9e1f9434872.js" defer=""></script><script src="/_next/static/chunks/1286-a62050b3f897c6be.js" defer=""></script><script src="/_next/static/chunks/2426-be3e2bc6625de582.js" defer=""></script><script src="/_next/static/chunks/6641-a0ed2bd8f5dc777b.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/edit-1b8b406222fae908.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--success{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--warning{background:#DD9900 !important;color:#FFFFFF !important;}/*!sc*/
 data-styled.g5[id="ToastWrapper-sc-1a33ph1-0"]{content:"kOVcuR,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"page":"edit","pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/edit","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"page":"edit","pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/edit","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/logs.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/monitors/block-runtime.html`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/4804-01a10103ebe26ca8.js" defer=""></script><script src="/_next/static/chunks/9565-28e1c30511c95c2d.js" defer=""></script><script src="/_next/static/chunks/4495-4f0340aa82e0c623.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/4463-1b9ce74c6e1bb14e.js" defer=""></script><script src="/_next/static/chunks/8961-697fe5d4db44d909.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/logs-5ccc75887776efb0.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/29107295-989a0767a635d9d5.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/2714-1e79e9f2e998b544.js" defer=""></script><script src="/_next/static/chunks/9832-c8b8970bb522f302.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/2249-70929b8c547bbc18.js" defer=""></script><script src="/_next/static/chunks/6641-a0ed2bd8f5dc777b.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/monitors/block-runtime-f83ab9de4094e1b0.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/logs","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/monitors/block-runtime","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/monitors/block-runs.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/monitors/block-runs.html`

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/2714-1e79e9f2e998b544.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/2249-70929b8c547bbc18.js" defer=""></script><script src="/_next/static/chunks/7400-1430ec3874c1fdee.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/monitors/block-runs-8f23f7ca9efcb069.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/2714-1e79e9f2e998b544.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/2249-70929b8c547bbc18.js" defer=""></script><script src="/_next/static/chunks/7400-1430ec3874c1fdee.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/monitors/block-runs-8f23f7ca9efcb069.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/monitors/block-runs","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/monitors/block-runs","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/monitors/block-runtime.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/logs.html`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/29107295-989a0767a635d9d5.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/2714-1e79e9f2e998b544.js" defer=""></script><script src="/_next/static/chunks/9832-c8b8970bb522f302.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/2249-70929b8c547bbc18.js" defer=""></script><script src="/_next/static/chunks/6641-a0ed2bd8f5dc777b.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/monitors/block-runtime-f83ab9de4094e1b0.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/4804-01a10103ebe26ca8.js" defer=""></script><script src="/_next/static/chunks/9565-28e1c30511c95c2d.js" defer=""></script><script src="/_next/static/chunks/4495-4f0340aa82e0c623.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/4463-1b9ce74c6e1bb14e.js" defer=""></script><script src="/_next/static/chunks/8961-697fe5d4db44d909.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/logs-5ccc75887776efb0.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/monitors/block-runtime","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/logs","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/monitors.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/pipeline-runs.html`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/2714-1e79e9f2e998b544.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/2249-70929b8c547bbc18.js" defer=""></script><script src="/_next/static/chunks/7400-1430ec3874c1fdee.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/monitors-8b08ec1aef4af4f2.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Pipeline runs | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/4846-b4ced91dc0e9fba9.js" defer=""></script><script src="/_next/static/chunks/pages/pipeline-runs-21fe37061bdaaaea.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/monitors","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipeline-runs","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/runs/[run].html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/runs/[run].html`

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/4804-01a10103ebe26ca8.js" defer=""></script><script src="/_next/static/chunks/1774-aa51ef1da7217ff9.js" defer=""></script><script src="/_next/static/chunks/5872-103815a4a043489b.js" defer=""></script><script src="/_next/static/chunks/2125-0b537dc53fe71b18.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/4463-1b9ce74c6e1bb14e.js" defer=""></script><script src="/_next/static/chunks/6532-a614f9e1f9434872.js" defer=""></script><script src="/_next/static/chunks/1286-a62050b3f897c6be.js" defer=""></script><script src="/_next/static/chunks/5944-757b7898608a65e1.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/runs/%5Brun%5D-73ced07cc98a4968.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/4804-01a10103ebe26ca8.js" defer=""></script><script src="/_next/static/chunks/1774-aa51ef1da7217ff9.js" defer=""></script><script src="/_next/static/chunks/5872-103815a4a043489b.js" defer=""></script><script src="/_next/static/chunks/2125-0b537dc53fe71b18.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/4463-1b9ce74c6e1bb14e.js" defer=""></script><script src="/_next/static/chunks/6532-a614f9e1f9434872.js" defer=""></script><script src="/_next/static/chunks/1286-a62050b3f897c6be.js" defer=""></script><script src="/_next/static/chunks/5944-757b7898608a65e1.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/runs/%5Brun%5D-73ced07cc98a4968.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"pipelineRun":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/runs/[run]","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"pipelineRun":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/runs/[run]","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/runs.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/triggers.html`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/4804-01a10103ebe26ca8.js" defer=""></script><script src="/_next/static/chunks/1774-aa51ef1da7217ff9.js" defer=""></script><script src="/_next/static/chunks/2524-6aeb9419acf5d1b4.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/4463-1b9ce74c6e1bb14e.js" defer=""></script><script src="/_next/static/chunks/6532-a614f9e1f9434872.js" defer=""></script><script src="/_next/static/chunks/4846-b4ced91dc0e9fba9.js" defer=""></script><script src="/_next/static/chunks/5944-757b7898608a65e1.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/runs-67d23509a0c9a1b8.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/4804-01a10103ebe26ca8.js" defer=""></script><script src="/_next/static/chunks/1774-aa51ef1da7217ff9.js" defer=""></script><script src="/_next/static/chunks/5872-103815a4a043489b.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/4463-1b9ce74c6e1bb14e.js" defer=""></script><script src="/_next/static/chunks/6532-a614f9e1f9434872.js" defer=""></script><script src="/_next/static/chunks/1286-a62050b3f897c6be.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/triggers-b0b91245d3299bdf.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/runs","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/triggers","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/syncs.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/backfills.html`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/9565-28e1c30511c95c2d.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/syncs-4084a44baf91f30e.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/backfills-0ed0d70bc659c236.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/syncs","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/backfills","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/triggers/[...slug].html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/triggers/[...slug].html`

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/4804-01a10103ebe26ca8.js" defer=""></script><script src="/_next/static/chunks/1774-aa51ef1da7217ff9.js" defer=""></script><script src="/_next/static/chunks/5872-103815a4a043489b.js" defer=""></script><script src="/_next/static/chunks/2524-6aeb9419acf5d1b4.js" defer=""></script><script src="/_next/static/chunks/4495-4f0340aa82e0c623.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/4463-1b9ce74c6e1bb14e.js" defer=""></script><script src="/_next/static/chunks/6532-a614f9e1f9434872.js" defer=""></script><script src="/_next/static/chunks/1286-a62050b3f897c6be.js" defer=""></script><script src="/_next/static/chunks/4846-b4ced91dc0e9fba9.js" defer=""></script><script src="/_next/static/chunks/8961-697fe5d4db44d909.js" defer=""></script><script src="/_next/static/chunks/2426-be3e2bc6625de582.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/triggers/%5B...slug%5D-ae970171cfe98c51.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/4804-01a10103ebe26ca8.js" defer=""></script><script src="/_next/static/chunks/1774-aa51ef1da7217ff9.js" defer=""></script><script src="/_next/static/chunks/5872-103815a4a043489b.js" defer=""></script><script src="/_next/static/chunks/2524-6aeb9419acf5d1b4.js" defer=""></script><script src="/_next/static/chunks/4495-4f0340aa82e0c623.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/4463-1b9ce74c6e1bb14e.js" defer=""></script><script src="/_next/static/chunks/6532-a614f9e1f9434872.js" defer=""></script><script src="/_next/static/chunks/1286-a62050b3f897c6be.js" defer=""></script><script src="/_next/static/chunks/4846-b4ced91dc0e9fba9.js" defer=""></script><script src="/_next/static/chunks/8961-697fe5d4db44d909.js" defer=""></script><script src="/_next/static/chunks/2426-be3e2bc6625de582.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/triggers/%5B...slug%5D-ae970171cfe98c51.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/triggers/[...slug]","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/triggers/[...slug]","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline]/triggers.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline]/backfills/[...slug].html`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/4804-01a10103ebe26ca8.js" defer=""></script><script src="/_next/static/chunks/1774-aa51ef1da7217ff9.js" defer=""></script><script src="/_next/static/chunks/5872-103815a4a043489b.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/4463-1b9ce74c6e1bb14e.js" defer=""></script><script src="/_next/static/chunks/6532-a614f9e1f9434872.js" defer=""></script><script src="/_next/static/chunks/1286-a62050b3f897c6be.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/triggers-b0b91245d3299bdf.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/5896-f84e336fb8877027.js" defer=""></script><script src="/_next/static/chunks/4804-01a10103ebe26ca8.js" defer=""></script><script src="/_next/static/chunks/1774-aa51ef1da7217ff9.js" defer=""></script><script src="/_next/static/chunks/5872-103815a4a043489b.js" defer=""></script><script src="/_next/static/chunks/2524-6aeb9419acf5d1b4.js" defer=""></script><script src="/_next/static/chunks/4495-4f0340aa82e0c623.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/1830-cb1bbbf9a9c54649.js" defer=""></script><script src="/_next/static/chunks/4463-1b9ce74c6e1bb14e.js" defer=""></script><script src="/_next/static/chunks/6532-a614f9e1f9434872.js" defer=""></script><script src="/_next/static/chunks/1286-a62050b3f897c6be.js" defer=""></script><script src="/_next/static/chunks/4846-b4ced91dc0e9fba9.js" defer=""></script><script src="/_next/static/chunks/8961-697fe5d4db44d909.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D/backfills/%5B...slug%5D-81e3c9ea75d7abb4.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/triggers","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]/backfills/[...slug]","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines/[pipeline].html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/settings.html`

 * *Files 4% similar despite different names*

```diff
@@ -1,12 +1,12 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><title>Mage</title><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D-ca9457e1a6bced4b.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><title>Mage</title><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/pages/settings-d594a66a568306da.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--success{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--warning{background:#DD9900 !important;color:#FFFFFF !important;}/*!sc*/
 data-styled.g5[id="ToastWrapper-sc-1a33ph1-0"]{content:"kOVcuR,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/settings","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/pipelines.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines.html`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Pipelines | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines-12dc02ae431a6305.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Pipelines | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines-12dc02ae431a6305.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/settings/account/profile.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/terminal.html`

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Settings | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/9140-6f67e0879394373d.js" defer=""></script><script src="/_next/static/chunks/pages/settings/account/profile-acd7ee47219fee3d.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Terminal | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/9565-28e1c30511c95c2d.js" defer=""></script><script src="/_next/static/chunks/6085-692d2f784c0504f2.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/pages/terminal-5d7c45bb058a3f20.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/settings/account/profile","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/terminal","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/settings/workspace/preferences.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/triggers.html`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Settings | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/pages/settings/workspace/preferences-07bda506f68974fb.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Triggers | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/pages/triggers-e0172c422c95eda9.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/settings/workspace/preferences","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/triggers","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/settings/workspace/users.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/manage.html`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Settings | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/9140-6f67e0879394373d.js" defer=""></script><script src="/_next/static/chunks/pages/settings/workspace/users-c128672e053a4c30.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Manage | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/2083-78a438dbdc57d1e4.js" defer=""></script><script src="/_next/static/chunks/8789-4f858e520d46973b.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/pages/manage-54fd0434f4f5305c.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -11,10 +11,8 @@
 data-styled.g5[id="ToastWrapper-sc-1a33ph1-0"]{content:"kOVcuR,"}/*!sc*/
 .dKQluW{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex:1;-ms-flex:1;flex:1;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}/*!sc*/
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
-.jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
-data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/settings/workspace/users","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/manage","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/settings.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/test.html`

 * *Files 6% similar despite different names*

```diff
@@ -1,12 +1,14 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><title>Mage</title><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/pages/settings-d594a66a568306da.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><title>Mage</title><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/7011-81dd8269c4806d26.js" defer=""></script><script src="/_next/static/chunks/pages/test-f567bdfcc1276249.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--success{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--warning{background:#DD9900 !important;color:#FFFFFF !important;}/*!sc*/
 data-styled.g5[id="ToastWrapper-sc-1a33ph1-0"]{content:"kOVcuR,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/settings","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+.flrenm:hover{cursor:pointer;}/*!sc*/
+data-styled.g134[id="MultiFileInput__DropzoneStyle-sc-1l6yd2y-0"]{content:"flrenm,"}/*!sc*/
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div><div role="presentation" tabindex="0" class="MultiFileInput__DropzoneStyle-sc-1l6yd2y-0 flrenm"><input multiple="" style="display:none" tabindex="-1" type="file" directory="" webkitdirectory=""/></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/test","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"appGip":true,"scriptLoader":[]}</script></body></html>
```

#### html2text {}

```diff
@@ -0,0 +1 @@
+[File]
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/sign-in.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/sign-in.html`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Sign in | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/pages/sign-in-b4e1eb529a184c60.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">.lpkUpY{display:-ms-flexbox;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;margin-right:-0px;margin-left:-0px;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Sign in | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/pages/sign-in-b4e1eb529a184c60.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">.lpkUpY{display:-ms-flexbox;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;margin-right:-0px;margin-left:-0px;}/*!sc*/
 data-styled.g2[id="sc-gswNZR"]{content:"lpkUpY,"}/*!sc*/
 .gNEDLC{position:relative;width:100%;min-height:1px;padding-right:0px;padding-left:0px;}/*!sc*/
 @media (max-width:574px){.gNEDLC{-ms-flex:0 0 100%;-webkit-flex:0 0 100%;-ms-flex:0 0 100%;flex:0 0 100%;max-width:100%;}}/*!sc*/
 .gNEDLC 0       0        @media (min-width:992px){-ms-flex:0 0 100%;-webkit-flex:0 0 100%;-ms-flex:0 0 100%;flex:0 0 100%;max-width:100%;}/*!sc*/
 .dLgItz{position:relative;width:100%;min-height:1px;padding-right:0px;padding-left:0px;}/*!sc*/
 @media (min-width:768px){.dLgItz{-ms-flex:0 0 100%;-webkit-flex:0 0 100%;-ms-flex:0 0 100%;flex:0 0 100%;max-width:100%;}}/*!sc*/
 @media (min-width:992px){.dLgItz{-ms-flex:0 0 50%;-webkit-flex:0 0 50%;-ms-flex:0 0 50%;flex:0 0 50%;max-width:50%;}}/*!sc*/
@@ -75,8 +75,8 @@
 data-styled.g94[id="KeyboardShortcutButton__ButtonStyle-sc-10tm4pj-0"]{content:"vwWbU,"}/*!sc*/
 .hMeiSD{padding-top:48px;height:calc(100vh);}/*!sc*/
 data-styled.g204[id="indexstyle__ContainerStyle-sc-jcgu5l-0"]{content:"hMeiSD,"}/*!sc*/
 .CMvDV{border-radius:10px;padding-bottom:168px;padding-left:40px;padding-right:40px;padding-top:40px;width:100%;background-color:#232429;}/*!sc*/
 data-styled.g205[id="indexstyle__ContainerStyle-sc-641xul-0"]{content:"CMvDV,"}/*!sc*/
 .dDoioK{border-radius:20px;font-size:0;overflow:hidden;background-image:url(/images/sessions/abstract.png);background-size:cover;background-repeat:no-repeat;height:100%;width:100%;}/*!sc*/
 data-styled.g206[id="indexstyle__BackgroundImageStyle-sc-641xul-1"]{content:"dDoioK,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 cAYLbO"><div class="sc-gswNZR lpkUpY"><div class="sc-dkrFOg gNEDLC"><div class="indexstyle__ContainerStyle-sc-jcgu5l-0 hMeiSD"><div style="height:100%" class="sc-gswNZR lpkUpY"><div class="sc-dkrFOg dLgItz"><div class="FlexContainer__FlexContainerStyle-sc-fv2cul-0 kphHys"><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 dyGjsV"><div class="indexstyle__ContainerStyle-sc-641xul-0 CMvDV"><div class="Headline__HeadlineContainerStyle-sc-12jzt2e-0 dDWSWx"><h3 class="Headline__H3Style-sc-12jzt2e-5 fUIxMs">👋 Sign in<!-- --></h3></div><form><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 ljsxhe"><div class="InputWrapper__ContainerStyle-sc-aepxnk-0 eccjqq"><input autoComplete="username" label="Email" placeholder="Email" class="TextInput__TextInputStyle-sc-1ii4qtc-0 gRnCoi"/></div><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 cvEUur"><div class="InputWrapper__ContainerStyle-sc-aepxnk-0 eccjqq"><input autoComplete="current-password" label="Password" type="password" placeholder="Password" class="TextInput__TextInputStyle-sc-1ii4qtc-0 gRnCoi"/></div></div></div><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 ljsxhe"><button selected="" type="button" class="KeyboardShortcutButton__ButtonStyle-sc-10tm4pj-0 vwWbU"><div class="Flex-sc-sgfnl9-0 kYvkZx">Sign into Mage<!-- --></div><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 litLtc"><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 litLtc"><div class="FlexContainer__FlexContainerStyle-sc-fv2cul-0 ecTpOw"><span style="border-color:#FFFFFF;border-radius:4px;border-style:solid;border-width:1px;overflow:hidden" class="Text__SpanStyle-sc-sl5nur-1 kdkfAS"><div class="KeyboardText__DivStyle-sc-18540m4-1 fLQRXT">enter</div></span></div></div></div></button></div></form></div></div></div></div><div style="flex:1" class="sc-dkrFOg dOhToE"><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 ijHkgz"><div src="/images/sessions/abstract.png" class="indexstyle__BackgroundImageStyle-sc-641xul-1 dDoioK">Sign in abstract image</div></div></div></div></div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/sign-in","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 cAYLbO"><div class="sc-gswNZR lpkUpY"><div class="sc-dkrFOg gNEDLC"><div class="indexstyle__ContainerStyle-sc-jcgu5l-0 hMeiSD"><div style="height:100%" class="sc-gswNZR lpkUpY"><div class="sc-dkrFOg dLgItz"><div class="FlexContainer__FlexContainerStyle-sc-fv2cul-0 kphHys"><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 dyGjsV"><div class="indexstyle__ContainerStyle-sc-641xul-0 CMvDV"><div class="Headline__HeadlineContainerStyle-sc-12jzt2e-0 dDWSWx"><h3 class="Headline__H3Style-sc-12jzt2e-5 fUIxMs">👋 Sign in<!-- --></h3></div><form><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 ljsxhe"><div class="InputWrapper__ContainerStyle-sc-aepxnk-0 eccjqq"><input autoComplete="username" label="Email" placeholder="Email" class="TextInput__TextInputStyle-sc-1ii4qtc-0 gRnCoi"/></div><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 cvEUur"><div class="InputWrapper__ContainerStyle-sc-aepxnk-0 eccjqq"><input autoComplete="current-password" label="Password" type="password" placeholder="Password" class="TextInput__TextInputStyle-sc-1ii4qtc-0 gRnCoi"/></div></div></div><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 ljsxhe"><button selected="" type="button" class="KeyboardShortcutButton__ButtonStyle-sc-10tm4pj-0 vwWbU"><div class="Flex-sc-sgfnl9-0 kYvkZx">Sign into Mage<!-- --></div><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 litLtc"><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 litLtc"><div class="FlexContainer__FlexContainerStyle-sc-fv2cul-0 ecTpOw"><span style="border-color:#FFFFFF;border-radius:4px;border-style:solid;border-width:1px;overflow:hidden" class="Text__SpanStyle-sc-sl5nur-1 kdkfAS"><div class="KeyboardText__DivStyle-sc-18540m4-1 fLQRXT">enter</div></span></div></div></div></button></div></form></div></div></div></div><div style="flex:1" class="sc-dkrFOg dOhToE"><div class="Spacing__SpacingStyle-sc-1mpmtgj-0 ijHkgz"><div src="/images/sessions/abstract.png" class="indexstyle__BackgroundImageStyle-sc-641xul-1 dDoioK">Sign in abstract image</div></div></div></div></div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/sign-in","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/terminal.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/settings/workspace/users.html`

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Terminal | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/9565-28e1c30511c95c2d.js" defer=""></script><script src="/_next/static/chunks/6085-692d2f784c0504f2.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/pages/terminal-5d7c45bb058a3f20.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Settings | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/9140-6f67e0879394373d.js" defer=""></script><script src="/_next/static/chunks/pages/settings/workspace/users-c128672e053a4c30.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/terminal","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/settings/workspace/users","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/test.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/pipelines/[pipeline].html`

 * *Files 8% similar despite different names*

```diff
@@ -1,14 +1,12 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><title>Mage</title><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/7011-81dd8269c4806d26.js" defer=""></script><script src="/_next/static/chunks/pages/test-f567bdfcc1276249.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><title>Mage</title><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/pages/pipelines/%5Bpipeline%5D-ca9457e1a6bced4b.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--success{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--warning{background:#DD9900 !important;color:#FFFFFF !important;}/*!sc*/
 data-styled.g5[id="ToastWrapper-sc-1a33ph1-0"]{content:"kOVcuR,"}/*!sc*/
-.flrenm:hover{cursor:pointer;}/*!sc*/
-data-styled.g134[id="MultiFileInput__DropzoneStyle-sc-1l6yd2y-0"]{content:"flrenm,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div><div role="presentation" tabindex="0" class="MultiFileInput__DropzoneStyle-sc-1l6yd2y-0 flrenm"><input multiple="" style="display:none" tabindex="-1" type="file" directory="" webkitdirectory=""/></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/test","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"pipeline":{},"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/pipelines/[pipeline]","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

#### html2text {}

```diff
@@ -1 +0,0 @@
-[File]
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/triggers.html` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/settings/workspace/preferences.html`

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Triggers | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/9898-51ca6a904b7a2382.js" defer=""></script><script src="/_next/static/chunks/pages/triggers-e0172c422c95eda9.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js" defer=""></script><script src="/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
+<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><meta content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=0" name="viewport"/><title>Settings | Mage</title><meta name="next-head-count" content="3"/><link href="/favicon.ico" rel="icon"/><link rel="preload" href="/_next/static/css/d1e8e64d0b07af2f.css" as="style"/><link rel="stylesheet" href="/_next/static/css/d1e8e64d0b07af2f.css" data-n-g=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-5cd94c89d3acac5f.js"></script><script src="/_next/static/chunks/webpack-bc5e4eb2c1ff587c.js" defer=""></script><script src="/_next/static/chunks/framework-7c365855dab1bf41.js" defer=""></script><script src="/_next/static/chunks/main-bb0dd5375146d7fd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-0aed65f2e085822e.js" defer=""></script><script src="/_next/static/chunks/3850-6395783d820def1c.js" defer=""></script><script src="/_next/static/chunks/9767-3f852fd90cf7857f.js" defer=""></script><script src="/_next/static/chunks/6579-2b5d8d39472d85c0.js" defer=""></script><script src="/_next/static/chunks/434-69ddfacd3e93f2db.js" defer=""></script><script src="/_next/static/chunks/pages/settings/workspace/preferences-07bda506f68974fb.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js" defer=""></script><script src="/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js" defer=""></script><style data-styled="" data-styled-version="5.3.6">html{-webkit-box-sizing:border-box;box-sizing:border-box;-ms-overflow-style:scrollbar;}/*!sc*/
 *,*::before,*::after{-webkit-box-sizing:inherit;box-sizing:inherit;}/*!sc*/
 data-styled.g4[id="sc-global-czSCUT1"]{content:"sc-global-czSCUT1,"}/*!sc*/
 .kOVcuR .Toastify__toast-container{margin-top:24px;padding:0 !important;width:500px !important;}/*!sc*/
 .kOVcuR .Toastify__toast{border-radius:8px !important;font-family:Greycliff Medium,Helvetica Neue,Helvetica,sans-serif !important;font-size:14px !important;line-height:20px !important;margin-bottom:0 !important;margin-left:0 !important;margin-right:0 !important;margin-top:16px !important;min-height:0 !important;padding:16px !important;}/*!sc*/
 .kOVcuR .Toastify__toast-body{margin:0 !important;}/*!sc*/
 .kOVcuR .Toastify__toast--error{background:#FF1E59 !important;color:#FFFFFF !important;}/*!sc*/
 .kOVcuR .Toastify__toast--info{background:#00A81A !important;color:#FFFFFF !important;}/*!sc*/
@@ -13,8 +13,8 @@
 data-styled.g23[id="Flex-sc-sgfnl9-0"]{content:"dKQluW,"}/*!sc*/
 .gbXfes{height:48px;left:0;padding-left:16px;padding-right:16px;position:fixed;top:0;width:100%;z-index:10;background-color:#232429;border-bottom:1px solid #1C1C1C;}/*!sc*/
 data-styled.g72[id="indexstyle__HeaderStyle-sc-1bk8irg-0"]{content:"gbXfes,"}/*!sc*/
 .ijwRXz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;height:calc(100vh - 48px);position:fixed;top:48px;width:100%;background-color:#1E1F24;}/*!sc*/
 data-styled.g74[id="indexstyle__ContainerStyle-sc-ecogjt-0"]{content:"ijwRXz,"}/*!sc*/
 .jMqDRN{padding:16px;background-color:#232429;border-right:1px solid #1C1C1C;}/*!sc*/
 data-styled.g75[id="indexstyle__VerticalNavigationStyle-sc-ecogjt-1"]{content:"jMqDRN,"}/*!sc*/
-</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/triggers","query":{},"buildId":"7JlKIxz5l4mwJx6uj5--5","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
+</style></head><body><div id="__next"><div class="" style="position:fixed;top:0;left:0;height:2px;background:transparent;z-index:99999999999;width:100%"><div class="" style="height:100%;background:#FF144D;transition:all 500ms ease;width:0%"><div style="box-shadow:0 0 10px #FF144D, 0 0 10px #FF144D;width:5%;opacity:1;position:absolute;height:100%;transition:all 500ms ease;transform:rotate(3deg) translate(0px, -4px);left:-10rem"></div></div></div><div class="indexstyle__HeaderStyle-sc-1bk8irg-0 gbXfes"><div></div></div><div class="indexstyle__ContainerStyle-sc-ecogjt-0 ijwRXz"><div class="indexstyle__VerticalNavigationStyle-sc-ecogjt-1 jMqDRN"><div></div></div><div class="Flex-sc-sgfnl9-0 dKQluW"><div></div></div></div><div></div><div></div><div class="ToastWrapper-sc-1a33ph1-0 kOVcuR"><div class="Toastify"></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"auth":{"decodedToken":{"expires":0,"token":null}}},"currentTheme":{"accent":{"alert":"#F6540B","blue":"#4877FF","blueLight":"rgba(72, 119, 255, 0.5)","contentDefaultTransparent":"rgba(174, 174, 174, 0.5)","cyan":"#65E3FF","cyanTransparent":"rgba(101, 227, 255, 0.12)","dbt":"#fc6949","dbtLight":"rgba(252, 105, 73, 0.5)","info":"#00ABFF","infoTransparent":"rgba(0, 171, 255, 0.5)","negative":"#FF1E59","negativeTransparent":"rgba(255, 30, 89, 0.3)","pink":"#FF4FF8","pinkLight":"#FFB9FC","positive":"#00A81A","primaryTransparent":"rgba(155, 108, 167, 0.5)","purple":"#7D55EC","purpleLight":"rgba(125, 85, 236, 0.5)","teal":"#00B4CC","tealLight":"rgba(0, 180, 204, 0.5)","warning":"#DD9900","warningTransparent":"rgba(221, 153, 0, 0.5)","yellow":"#FFCC19","yellowLight":"rgba(255, 204, 25, 0.5)"},"background":{"chartBlock":"#2E3036","codeArea":"#1E1F24","codeTextarea":"#000000","content":"#1B1C20","danger":"#FFD0DB","dark":"#B1B8C3","header":"#1B1B1B","menu":"#0F4CFF","muted":"#F9FAFC","navigation":"#EDEDED","output":"#2E3036","page":"#1E1F24","panel":"#232429","popup":"#27292E","row":"#2C2C2C","row2":"#51535C","scrollbarThumb":"rgba(100, 100, 100, 0.5)","scrollbarThumbHover":"rgba(255, 255, 255, 0.3)","scrollbarTrack":"#2E3036","success":"#8ADE00","table":"#292A2F"},"borders":{"contrast":"#FFFFFF","danger":"#FF144D","dark":"#000000","info":"#FFCC19","light":"#2F3034","medium":"#1C1C1C","success":"#2FCB52"},"brand":{"earth100":"#C6EEDB","earth200":"#9DDFBF","earth300":"#6BBF96","earth400":"#37A46F","earth400Transparent":"rgba(55, 164, 111, 0.4)","earth500":"#00954C","energy100":"#FFF4BA","energy200":"#FFED92","energy300":"#FFE662","energy400":"#FFDA19","energy400Transparent":"rgba(255, 218, 25, 0.04)","energy500":"#F6C000","fire100":"#FFD7E0","fire200":"#FFA3B9","fire300":"#FF547D","fire400":"#FF144D","fire400Transparent":"rgba(255, 20, 77, 0.4)","fire500":"#EB0032","stone100":"#F3E6D7","stone200":"#E3D4C2","stone400":"#BFA78B","stone500":"#AF8859","water100":"#BDCEFF","water200":"#81A1FF","water300":"#517DFF","water400":"#2A60FE","water400Transparent":"rgba(42, 96, 254, 0.4)","water500":"#0F4CFF","wind100":"#EEEAFF","wind200":"#CCC1F4","wind300":"#A698DD","wind400":"#6B50D7","wind400SuperTransparent":"rgba(107, 80, 215, 0.12)","wind400Transparent":"rgba(107, 80, 215, 0.4)","wind500":"#4E32BC"},"chart":{"backgroundPrimary":"#7D55EC","backgroundSecondary":"#FF144D","backgroundTertiary":"#86E2FF","button1":"#4877FF","button2":"#FFCC19","button3":"#8ADE00","button4":"#FF4FF8","button5":"#B98D95","lines":"#9B6CA7","primary":"#6B50D7","secondary":"#FF144D","tertiary":"#2A60FE"},"content":{"active":"#FFFFFF","default":"#AEAEAE","disabled":"rgba(255, 255, 255, 0.3)","inverted":"#2C2C2C","muted":"#787A85"},"elevation":{"visualizationAccent":"#996CFF","visualizationAccentAlt":"#C1ACF7"},"feature":{"active":"rgba(250, 248, 254, 0.14)","disabled":"rgba(201, 206, 218, 0.12)"},"icons":{"neutral":"#787878"},"interactive":{"activeBorder":"#060606","checked":"#060606","dangerBorder":"#FF144D","defaultBackground":"#36383F","defaultBorder":"#1C1C1C","disabledBorder":"#B1B8C3","focusBackground":"#B1B8C3","focusBorder":"#86E2FF","hoverBackground":"#4E4E4E","hoverBorder":"#B9BFCA","hoverOverlay":"rgba(255, 255, 255, 0.1)","linkPrimary":"#1752FF","linkPrimaryHover":"#4877FF","linkSecondary":"#6B50D7","linkSecondaryDisabled":"#C4B9EF","rowHoverBackground":"rgba(0, 0, 0, 0.1)"},"loader":{"color":"#EB0032","colorInverted":"#8ADE00"},"logo":{"color":"#FFFFFF"},"monotone":{"black":"#060606","blackTransparent":"rgba(0, 0, 0, 0.6)","gray":"#B1B8C3","grey100":"#F2F2F2","grey200":"#D5D7DC","grey300":"#B4B8C0","grey400":"#70747C","grey500":"#51535C","purple":"#6B50D7","white":"#FFFFFF"},"neutral":{"n100":"#E7E8EA","n200":"#D8DADE","n300":"#CBCCD0","n400":"#BCBEC4","n500":"#AEB0B6"},"progress":{"negative":"#FF144D","positive":"#6B50D7"},"shadow":{"base":"12px 40px 120px rgba(106, 117, 139, 0.4)","menu":"4px 10px 20px rgba(6, 6, 6, 0.12)","popup":"10px 20px 40px rgba(0, 0, 0, 0.2)","small":"0px, 4px, rgba(0, 0, 0, 0.25)","window":"0px 10px 60px rgba(0, 0, 0, 0.7)"},"status":{"negative":"#FF144D","positive":"#24B400"},"text":{"fileBrowser":"#787A85"}}},"page":"/settings/workspace/preferences","query":{},"buildId":"hPU1Mni8edYXkEy_4mLHN","nextExport":true,"isFallback":false,"gip":true,"appGip":true,"scriptLoader":[]}</script></body></html>
```

### Comparing `mage-ai-0.8.8/mage_ai/server/frontend_dist/vercel.svg` & `mage-ai-0.8.9/mage_ai/server/frontend_dist/vercel.svg`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/kernel_output_parser.py` & `mage-ai-0.8.9/mage_ai/server/kernel_output_parser.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/kernels.py` & `mage-ai-0.8.9/mage_ai/server/kernels.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/scheduler_manager.py` & `mage-ai-0.8.9/mage_ai/server/scheduler_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/server.py` & `mage-ai-0.8.9/mage_ai/server/server.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/subscriber.py` & `mage-ai-0.8.9/mage_ai/server/subscriber.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/utils/frontend_renderer.py` & `mage-ai-0.8.9/mage_ai/server/utils/frontend_renderer.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/utils/output_display.py` & `mage-ai-0.8.9/mage_ai/server/utils/output_display.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/server/websocket_server.py` & `mage-ai-0.8.9/mage_ai/server/websocket_server.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/airbyte/__init__.py` & `mage-ai-0.8.9/mage_ai/services/airbyte/__init__.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/airbyte/client.py` & `mage-ai-0.8.9/mage_ai/services/airbyte/client.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/airbyte/server.py` & `mage-ai-0.8.9/mage_ai/services/airbyte/server.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/aws/ecs/config.py` & `mage-ai-0.8.9/mage_ai/services/aws/ecs/config.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/aws/ecs/ecs.py` & `mage-ai-0.8.9/mage_ai/services/aws/ecs/ecs.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/aws/emr/config.py` & `mage-ai-0.8.9/mage_ai/services/aws/emr/config.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/aws/emr/emr.py` & `mage-ai-0.8.9/mage_ai/services/aws/emr/emr.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/aws/emr/emr_basics.py` & `mage-ai-0.8.9/mage_ai/services/aws/emr/emr_basics.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/aws/emr/launcher.py` & `mage-ai-0.8.9/mage_ai/services/aws/emr/launcher.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/aws/emr/resource_manager.py` & `mage-ai-0.8.9/mage_ai/services/aws/emr/resource_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/aws/events/events.py` & `mage-ai-0.8.9/mage_ai/services/aws/events/events.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/aws/s3/s3.py` & `mage-ai-0.8.9/mage_ai/services/aws/s3/s3.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/aws/secrets_manager/secrets_manager.py` & `mage-ai-0.8.9/mage_ai/services/aws/secrets_manager/secrets_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/datadog/__init__.py` & `mage-ai-0.8.9/mage_ai/services/datadog/__init__.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/dbt/dbt.py` & `mage-ai-0.8.9/mage_ai/services/dbt/dbt.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/email/email.py` & `mage-ai-0.8.9/mage_ai/services/email/email.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/gcp/cloud_run/cloud_run.py` & `mage-ai-0.8.9/mage_ai/services/gcp/cloud_run/cloud_run.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/hightouch/constants.py` & `mage-ai-0.8.9/mage_ai/services/hightouch/constants.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/hightouch/hightouch.py` & `mage-ai-0.8.9/mage_ai/services/hightouch/hightouch.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/k8s/job_manager.py` & `mage-ai-0.8.9/mage_ai/services/k8s/job_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/metaplane/metaplane.py` & `mage-ai-0.8.9/mage_ai/services/metaplane/metaplane.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/services/stitch/stitch.py` & `mage-ai-0.8.9/mage_ai/services/stitch/stitch.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/shared/array.py` & `mage-ai-0.8.9/mage_ai/shared/array.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/shared/config.py` & `mage-ai-0.8.9/mage_ai/shared/config.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/shared/conversions.py` & `mage-ai-0.8.9/mage_ai/shared/conversions.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/shared/custom_types.py` & `mage-ai-0.8.9/mage_ai/shared/custom_types.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/shared/dates.py` & `mage-ai-0.8.9/mage_ai/shared/dates.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/shared/hash.py` & `mage-ai-0.8.9/mage_ai/shared/hash.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/shared/http_client.py` & `mage-ai-0.8.9/mage_ai/shared/http_client.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/shared/io.py` & `mage-ai-0.8.9/mage_ai/shared/io.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/shared/logger.py` & `mage-ai-0.8.9/mage_ai/shared/logger.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/shared/multi.py` & `mage-ai-0.8.9/mage_ai/shared/multi.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/shared/parsers.py` & `mage-ai-0.8.9/mage_ai/shared/parsers.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/shared/retry.py` & `mage-ai-0.8.9/mage_ai/shared/retry.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/shared/strings.py` & `mage-ai-0.8.9/mage_ai/shared/strings.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/shared/utils.py` & `mage-ai-0.8.9/mage_ai/shared/utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/streaming/sinks/base.py` & `mage-ai-0.8.9/mage_ai/streaming/sinks/base.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/streaming/sinks/kinesis.py` & `mage-ai-0.8.9/mage_ai/streaming/sinks/kinesis.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/streaming/sinks/opensearch.py` & `mage-ai-0.8.9/mage_ai/streaming/sinks/opensearch.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/streaming/sinks/sink_factory.py` & `mage-ai-0.8.9/mage_ai/streaming/sinks/sink_factory.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/streaming/sources/azure_event_hub.py` & `mage-ai-0.8.9/mage_ai/streaming/sources/azure_event_hub.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/streaming/sources/base.py` & `mage-ai-0.8.9/mage_ai/streaming/sources/base.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/streaming/sources/kafka.py` & `mage-ai-0.8.9/mage_ai/streaming/sources/kafka.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/streaming/sources/kinesis.py` & `mage-ai-0.8.9/mage_ai/streaming/sources/kinesis.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/streaming/sources/rabbitmq.py` & `mage-ai-0.8.9/mage_ai/streaming/sources/rabbitmq.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/streaming/sources/source_factory.py` & `mage-ai-0.8.9/mage_ai/streaming/sources/source_factory.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/api/operations/base.py` & `mage-ai-0.8.9/mage_ai/tests/api/operations/base.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/api/operations/test_sessions.py` & `mage-ai-0.8.9/mage_ai/tests/api/operations/test_sessions.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/api/operations/test_users.py` & `mage-ai-0.8.9/mage_ai/tests/api/operations/test_users.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/base_test.py` & `mage-ai-0.8.9/mage_ai/tests/base_test.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_clean_column_names.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_clean_column_names.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_fix_syntax_error.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_fix_syntax_error.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_impute_values.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_impute_values.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_reformat_values.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_reformat_values.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_collinear_columns.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_collinear_columns.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_columns_with_high_empty_rate.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_columns_with_high_empty_rate.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_columns_with_single_value.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_columns_with_single_value.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_duplicate_rows.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_duplicate_rows.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_outliers.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/cleaning_rules/test_remove_outliers.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/statistics/test_calculator.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/statistics/test_calculator.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/test_column_type_detector.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/test_column_type_detector.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/shared.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/shared.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/test_base.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/test_base.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/test_column.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/test_column.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/test_custom_actions.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/test_custom_actions.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/test_helpers.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/test_helpers.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/test_row.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/test_row.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/test_utils.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/test_utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_cleaner/transformer_actions/test_variable_replacer.py` & `mage-ai-0.8.9/mage_ai/tests/data_cleaner/transformer_actions/test_variable_replacer.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_preparation/models/test_block.py` & `mage-ai-0.8.9/mage_ai/tests/data_preparation/models/test_block.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_preparation/models/test_pipeline.py` & `mage-ai-0.8.9/mage_ai/tests/data_preparation/models/test_pipeline.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_preparation/models/test_variable.py` & `mage-ai-0.8.9/mage_ai/tests/data_preparation/models/test_variable.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_preparation/test_templates.py` & `mage-ai-0.8.9/mage_ai/tests/data_preparation/test_templates.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/data_preparation/test_variable_manager.py` & `mage-ai-0.8.9/mage_ai/tests/data_preparation/test_variable_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/factory.py` & `mage-ai-0.8.9/mage_ai/tests/factory.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/io/test_config.py` & `mage-ai-0.8.9/mage_ai/tests/io/test_config.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/io/test_export_utils.py` & `mage-ai-0.8.9/mage_ai/tests/io/test_export_utils.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/orchestration/db/test_models.py` & `mage-ai-0.8.9/mage_ai/tests/orchestration/db/test_models.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/orchestration/notification/constants.py` & `mage-ai-0.8.9/mage_ai/tests/orchestration/notification/constants.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/orchestration/notification/test_config.py` & `mage-ai-0.8.9/mage_ai/tests/orchestration/notification/test_config.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/orchestration/notification/test_sender.py` & `mage-ai-0.8.9/mage_ai/tests/orchestration/notification/test_sender.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/orchestration/queue/test_process_queue.py` & `mage-ai-0.8.9/mage_ai/tests/orchestration/queue/test_process_queue.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/orchestration/test_execution_process_manager.py` & `mage-ai-0.8.9/mage_ai/tests/orchestration/test_execution_process_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/orchestration/test_job_manager.py` & `mage-ai-0.8.9/mage_ai/tests/orchestration/test_job_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/orchestration/test_pipeline_scheduler.py` & `mage-ai-0.8.9/mage_ai/tests/orchestration/test_pipeline_scheduler.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/orchestration/triggers/test_loop_time_trigger.py` & `mage-ai-0.8.9/mage_ai/tests/orchestration/triggers/test_loop_time_trigger.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/services/aws/s3/test_s3.py` & `mage-ai-0.8.9/mage_ai/tests/services/aws/s3/test_s3.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/services/datadog/test_datadog.py` & `mage-ai-0.8.9/mage_ai/tests/services/datadog/test_datadog.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/services/k8s/test_job_manager.py` & `mage-ai-0.8.9/mage_ai/tests/services/k8s/test_job_manager.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/shared/test_io.py` & `mage-ai-0.8.9/mage_ai/tests/shared/test_io.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/streaming/sinks/test_kinesis.py` & `mage-ai-0.8.9/mage_ai/tests/streaming/sinks/test_kinesis.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/streaming/sinks/test_opensearch.py` & `mage-ai-0.8.9/mage_ai/tests/streaming/sinks/test_opensearch.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/streaming/sinks/test_sink_factory.py` & `mage-ai-0.8.9/mage_ai/tests/streaming/sinks/test_sink_factory.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/streaming/sources/test_azure_event_hub.py` & `mage-ai-0.8.9/mage_ai/tests/streaming/sources/test_azure_event_hub.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/streaming/sources/test_kafka.py` & `mage-ai-0.8.9/mage_ai/tests/streaming/sources/test_kafka.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/streaming/sources/test_kinesis.py` & `mage-ai-0.8.9/mage_ai/tests/streaming/sources/test_kinesis.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/streaming/sources/test_rabbitmq.py` & `mage-ai-0.8.9/mage_ai/tests/streaming/sources/test_rabbitmq.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/streaming/sources/test_source_factory.py` & `mage-ai-0.8.9/mage_ai/tests/streaming/sources/test_source_factory.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/tests/test_shared.py` & `mage-ai-0.8.9/mage_ai/tests/test_shared.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/utils/code.py` & `mage-ai-0.8.9/mage_ai/utils/code.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai/utils/logger/__init__.py` & `mage-ai-0.8.9/mage_ai/utils/logger/__init__.py`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/mage_ai.egg-info/PKG-INFO` & `mage-ai-0.8.9/mage_ai.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mage-ai
-Version: 0.8.8
+Version: 0.8.9
 Summary: Mage is a tool for building and deploying data pipelines.
 Home-page: https://github.com/mage-ai/mage-ai
 Author: Mage
 Author-email: eng@mage.ai
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: OS Independent
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: mage-ai Version: 0.8.8 Summary: Mage is a tool for
+Metadata-Version: 2.1 Name: mage-ai Version: 0.8.9 Summary: Mage is a tool for
 building and deploying data pipelines. Home-page: https://github.com/mage-ai/
 mage-ai Author: Mage Author-email: eng@mage.ai Classifier: Programming Language
 :: Python :: 3 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: OS Independent Requires-Python: >=3.6
 Description-Content-Type: text/markdown Provides-Extra: azure Provides-Extra:
 bigquery Provides-Extra: dbt Provides-Extra: google-cloud-storage Provides-
 Extra: hdf5 Provides-Extra: mysql Provides-Extra: postgres Provides-Extra:
```

### Comparing `mage-ai-0.8.8/mage_ai.egg-info/SOURCES.txt` & `mage-ai-0.8.9/mage_ai.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -481,17 +481,14 @@
 mage_ai/server/frontend_dist/pipelines.html
 mage_ai/server/frontend_dist/settings.html
 mage_ai/server/frontend_dist/sign-in.html
 mage_ai/server/frontend_dist/terminal.html
 mage_ai/server/frontend_dist/test.html
 mage_ai/server/frontend_dist/triggers.html
 mage_ai/server/frontend_dist/vercel.svg
-mage_ai/server/frontend_dist/_next/static/7JlKIxz5l4mwJx6uj5--5/_buildManifest.js
-mage_ai/server/frontend_dist/_next/static/7JlKIxz5l4mwJx6uj5--5/_middlewareManifest.js
-mage_ai/server/frontend_dist/_next/static/7JlKIxz5l4mwJx6uj5--5/_ssgManifest.js
 mage_ai/server/frontend_dist/_next/static/chunks/1150.1378afaa474df64a.js
 mage_ai/server/frontend_dist/_next/static/chunks/1240.0819f45820d22263.js
 mage_ai/server/frontend_dist/_next/static/chunks/1286-a62050b3f897c6be.js
 mage_ai/server/frontend_dist/_next/static/chunks/1450.d383f64c169d4278.js
 mage_ai/server/frontend_dist/_next/static/chunks/1774-aa51ef1da7217ff9.js
 mage_ai/server/frontend_dist/_next/static/chunks/1830-cb1bbbf9a9c54649.js
 mage_ai/server/frontend_dist/_next/static/chunks/2083-78a438dbdc57d1e4.js
@@ -608,14 +605,17 @@
 mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/monitors/block-runtime-f83ab9de4094e1b0.js
 mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/runs/[run]-73ced07cc98a4968.js
 mage_ai/server/frontend_dist/_next/static/chunks/pages/pipelines/[pipeline]/triggers/[...slug]-ae970171cfe98c51.js
 mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/account/profile-acd7ee47219fee3d.js
 mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/workspace/preferences-07bda506f68974fb.js
 mage_ai/server/frontend_dist/_next/static/chunks/pages/settings/workspace/users-c128672e053a4c30.js
 mage_ai/server/frontend_dist/_next/static/css/d1e8e64d0b07af2f.css
+mage_ai/server/frontend_dist/_next/static/hPU1Mni8edYXkEy_4mLHN/_buildManifest.js
+mage_ai/server/frontend_dist/_next/static/hPU1Mni8edYXkEy_4mLHN/_middlewareManifest.js
+mage_ai/server/frontend_dist/_next/static/hPU1Mni8edYXkEy_4mLHN/_ssgManifest.js
 mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Bold.ttf
 mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Light.ttf
 mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Medium.ttf
 mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Regular.ttf
 mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-Retina.ttf
 mage_ai/server/frontend_dist/fonts/Fira_Code/ttf/FiraCode-SemiBold.ttf
 mage_ai/server/frontend_dist/fonts/Roboto/LICENSE.txt
```

### Comparing `mage-ai-0.8.8/mage_ai.egg-info/requires.txt` & `mage-ai-0.8.9/mage_ai.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/requirements.txt` & `mage-ai-0.8.9/requirements.txt`

 * *Files identical despite different names*

### Comparing `mage-ai-0.8.8/setup.py` & `mage-ai-0.8.9/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -14,15 +14,15 @@
             break
         requirements.append(line)
 
 setuptools.setup(
     name='mage-ai',
     # NOTE: when you change this, change the value of VERSION in the following file:
     # mage_ai/server/constants.py
-    version='0.8.8',
+    version='0.8.9',
     author='Mage',
     author_email='eng@mage.ai',
     description='Mage is a tool for building and deploying data pipelines.',
     long_description=readme(),
     long_description_content_type='text/markdown',
     url='https://github.com/mage-ai/mage-ai',
     packages=setuptools.find_packages('.'),
```

