# Comparing `tmp/ComponentDB-API-3.15.5.dev0.tar.gz` & `tmp/ComponentDB-API-3.15.5.dev1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ComponentDB-API-3.15.5.dev0.tar", last modified: Tue Mar 21 18:00:34 2023, max compression
+gzip compressed data, was "ComponentDB-API-3.15.5.dev1.tar", last modified: Thu Apr  6 20:52:45 2023, max compression
```

## Comparing `ComponentDB-API-3.15.5.dev0.tar` & `ComponentDB-API-3.15.5.dev1.tar`

### file list

```diff
@@ -1,135 +1,135 @@
-drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-03-21 18:00:34.558750 ComponentDB-API-3.15.5.dev0/
--rwxrwxr-x   0 darek     (1000) darek     (1000)     6301 2023-03-21 16:56:29.000000 ComponentDB-API-3.15.5.dev0/CdbApiFactory.py
-drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-03-21 18:00:34.542750 ComponentDB-API-3.15.5.dev0/ComponentDB_API.egg-info/
--rw-rw-r--   0 darek     (1000) darek     (1000)      335 2023-03-21 18:00:33.000000 ComponentDB-API-3.15.5.dev0/ComponentDB_API.egg-info/PKG-INFO
--rw-rw-r--   0 darek     (1000) darek     (1000)     4807 2023-03-21 18:00:34.000000 ComponentDB-API-3.15.5.dev0/ComponentDB_API.egg-info/SOURCES.txt
--rw-rw-r--   0 darek     (1000) darek     (1000)        1 2023-03-21 18:00:33.000000 ComponentDB-API-3.15.5.dev0/ComponentDB_API.egg-info/dependency_links.txt
--rw-rw-r--   0 darek     (1000) darek     (1000)       69 2023-03-21 18:00:34.000000 ComponentDB-API-3.15.5.dev0/ComponentDB_API.egg-info/entry_points.txt
--rw-rw-r--   0 darek     (1000) darek     (1000)       36 2023-03-21 18:00:34.000000 ComponentDB-API-3.15.5.dev0/ComponentDB_API.egg-info/requires.txt
--rw-rw-r--   0 darek     (1000) darek     (1000)       21 2023-03-21 18:00:34.000000 ComponentDB-API-3.15.5.dev0/ComponentDB_API.egg-info/top_level.txt
--rw-rw-r--   0 darek     (1000) darek     (1000)      335 2023-03-21 18:00:34.558750 ComponentDB-API-3.15.5.dev0/PKG-INFO
-drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-03-21 18:00:34.542750 ComponentDB-API-3.15.5.dev0/cdbApi/
--rw-rw-r--   0 darek     (1000) darek     (1000)     8420 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/__init__.py
-drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-03-21 18:00:34.542750 ComponentDB-API-3.15.5.dev0/cdbApi/api/
--rw-rw-r--   0 darek     (1000) darek     (1000)     1191 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/__init__.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5810 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/app_items_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    13649 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/authentication_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    15045 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/cable_catalog_items_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    67525 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/cable_design_items_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    17790 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/cable_import_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    12018 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/component_catalog_items_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     6008 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/component_inventory_items_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    20304 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/connector_types_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    43686 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/domain_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    11336 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/downloads_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)   243237 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/item_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    34909 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/location_items_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    28490 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/log_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    91953 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/machine_design_items_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    33222 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/property_type_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    37874 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/property_value_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     6105 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/search_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    19800 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/sources_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    13462 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/test_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    18909 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api/users_api.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    26194 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/api_client.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    13248 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/configuration.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     3779 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/exceptions.py
-drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-03-21 18:00:34.554750 ComponentDB-API-3.15.5.dev0/cdbApi/models/
--rw-rw-r--   0 darek     (1000) darek     (1000)     6936 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/__init__.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     7488 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/allowed_property_value.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     4882 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/api_exception_message.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     6898 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/api_exception_message_exception.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     6247 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/api_exception_message_exception_cause.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     9671 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/api_exception_message_exception_cause_stack_trace.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5488 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/api_exception_message_exception_cause_suppressed.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     4721 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/cable_catalog_item_info.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     9768 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/cable_design_connection_list_object.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    11417 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/concise_item.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     8129 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/concise_item_options.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     9613 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/connector.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     6476 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/connector_type.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     3471 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/connector_type_id_list_request.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5363 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/control_relationship_hierarchy.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    16233 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/domain.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    11678 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/entity_info.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     9064 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/entity_type.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     4145 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/file_upload_object.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     3979 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/inline_object.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    18387 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     6270 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_category.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    17813 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_connector.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    19071 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_app.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    20571 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_catalog.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     3561 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_catalog_all_of.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     3543 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_catalog_id_list_request.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    24701 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_design.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     7863 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_design_all_of.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     3535 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_design_id_list_request.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    22484 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_inventory.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5370 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_inventory_all_of.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    20171 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_catalog.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    20491 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_catalog_base.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     8505 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_catalog_search_result.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    23398 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_inventory.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     6684 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_inventory_all_of.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    23431 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_inventory_base.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    20236 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_location.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     3514 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_location_all_of.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     2677 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_maarc.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    29097 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_machine_design.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    12195 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_machine_design_all_of.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5153 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_machine_design_id_list_request.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     9145 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_md_search_result.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    18306 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_element.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    19458 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_element_history.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    30966 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_element_relationship.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    19118 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_element_relationship_history.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     7809 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_hierarchy.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    10023 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_location_information.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     4994 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_membership.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5605 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_permissions.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5628 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_project.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    11118 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_resource.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    14019 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_source.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     4280 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_status_basic_object.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     7074 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/item_type.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     8737 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/list_tbl.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    20719 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/locatable_item.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     9214 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/location_history_object.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     8054 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/log.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     4944 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/log_entry_edit_information.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     8461 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/machine_design_connector_list_object.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     4046 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/machine_design_item_info.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5728 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/new_app_information.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5208 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/new_catalog_element_information.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     8405 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/new_catalog_information.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     6943 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/new_control_relationship_information.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     6251 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/new_inventory_information.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     7685 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/new_location_information.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5751 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/new_machine_placeholder_options.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5350 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/promote_machine_element_information.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     6164 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/property_metadata.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    14686 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/property_type.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    21423 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/property_value.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    14381 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/property_value_history.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     7967 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/relationship_type.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     6856 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/relationship_type_handler.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     6086 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/representing_assembly_element_for_machine_information.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    14695 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/resource_type.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     6704 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/resource_type_category.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5580 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/role_type.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    18081 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/search_entities_options.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    19826 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/search_entities_results.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     6341 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/search_result.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5339 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/simple_location_information.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     9151 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/source.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     3415 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/source_id_list_request.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     7925 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/update_cable_design_assigned_item_information.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5298 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/update_machine_assigned_item_information.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     5596 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/user_group.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    12249 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/user_info.py
--rw-rw-r--   0 darek     (1000) darek     (1000)     4022 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/models/user_role.py
--rw-rw-r--   0 darek     (1000) darek     (1000)    12303 2023-03-21 18:00:32.000000 ComponentDB-API-3.15.5.dev0/cdbApi/rest.py
--rw-rw-r--   0 darek     (1000) darek     (1000)       38 2023-03-21 18:00:34.558750 ComponentDB-API-3.15.5.dev0/setup.cfg
--rw-rw-r--   0 darek     (1000) darek     (1000)     1037 2023-03-21 17:53:06.000000 ComponentDB-API-3.15.5.dev0/setup.py
+drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-04-06 20:52:45.935497 ComponentDB-API-3.15.5.dev1/
+-rwxrwxr-x   0 darek     (1000) darek     (1000)     6301 2023-03-21 16:56:29.000000 ComponentDB-API-3.15.5.dev1/CdbApiFactory.py
+drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-04-06 20:52:45.923497 ComponentDB-API-3.15.5.dev1/ComponentDB_API.egg-info/
+-rw-rw-r--   0 darek     (1000) darek     (1000)      335 2023-04-06 20:52:45.000000 ComponentDB-API-3.15.5.dev1/ComponentDB_API.egg-info/PKG-INFO
+-rw-rw-r--   0 darek     (1000) darek     (1000)     4807 2023-04-06 20:52:45.000000 ComponentDB-API-3.15.5.dev1/ComponentDB_API.egg-info/SOURCES.txt
+-rw-rw-r--   0 darek     (1000) darek     (1000)        1 2023-04-06 20:52:45.000000 ComponentDB-API-3.15.5.dev1/ComponentDB_API.egg-info/dependency_links.txt
+-rw-rw-r--   0 darek     (1000) darek     (1000)       69 2023-04-06 20:52:45.000000 ComponentDB-API-3.15.5.dev1/ComponentDB_API.egg-info/entry_points.txt
+-rw-rw-r--   0 darek     (1000) darek     (1000)       36 2023-04-06 20:52:45.000000 ComponentDB-API-3.15.5.dev1/ComponentDB_API.egg-info/requires.txt
+-rw-rw-r--   0 darek     (1000) darek     (1000)       21 2023-04-06 20:52:45.000000 ComponentDB-API-3.15.5.dev1/ComponentDB_API.egg-info/top_level.txt
+-rw-rw-r--   0 darek     (1000) darek     (1000)      335 2023-04-06 20:52:45.935497 ComponentDB-API-3.15.5.dev1/PKG-INFO
+drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-04-06 20:52:45.923497 ComponentDB-API-3.15.5.dev1/cdbApi/
+-rw-rw-r--   0 darek     (1000) darek     (1000)     8420 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/__init__.py
+drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-04-06 20:52:45.923497 ComponentDB-API-3.15.5.dev1/cdbApi/api/
+-rw-rw-r--   0 darek     (1000) darek     (1000)     1191 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/__init__.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5810 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/app_items_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    13649 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/authentication_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    15045 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/cable_catalog_items_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    67525 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/cable_design_items_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    17790 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/cable_import_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    12018 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/component_catalog_items_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     6008 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/component_inventory_items_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    20304 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/connector_types_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    43686 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/domain_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    11336 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/downloads_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)   243237 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/item_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    34909 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/location_items_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    28490 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/log_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    91953 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/machine_design_items_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    33222 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/property_type_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    37874 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/property_value_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     6105 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/search_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    19800 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/sources_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    13462 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/test_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    18909 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api/users_api.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    26194 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/api_client.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    13248 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/configuration.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     3779 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/exceptions.py
+drwxrwxr-x   0 darek     (1000) darek     (1000)        0 2023-04-06 20:52:45.935497 ComponentDB-API-3.15.5.dev1/cdbApi/models/
+-rw-rw-r--   0 darek     (1000) darek     (1000)     6936 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/__init__.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     7488 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/allowed_property_value.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     4882 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/api_exception_message.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     6898 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/api_exception_message_exception.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     6247 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/api_exception_message_exception_cause.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     9671 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/api_exception_message_exception_cause_stack_trace.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5488 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/api_exception_message_exception_cause_suppressed.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     4721 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/cable_catalog_item_info.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     9768 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/cable_design_connection_list_object.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    11417 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/concise_item.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     8129 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/concise_item_options.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     9613 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/connector.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     6476 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/connector_type.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     3471 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/connector_type_id_list_request.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5363 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/control_relationship_hierarchy.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    16233 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/domain.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    11678 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/entity_info.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     9064 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/entity_type.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     4145 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/file_upload_object.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     3979 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/inline_object.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    18387 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     6270 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_category.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    17813 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_connector.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    19071 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_app.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    20571 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_catalog.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     3561 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_catalog_all_of.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     3543 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_catalog_id_list_request.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    24701 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_design.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     7863 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_design_all_of.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     3535 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_design_id_list_request.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    22484 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_inventory.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5370 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_inventory_all_of.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    20171 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_catalog.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    20491 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_catalog_base.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     8505 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_catalog_search_result.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    23398 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_inventory.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     6684 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_inventory_all_of.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    23431 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_inventory_base.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    20236 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_location.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     3514 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_location_all_of.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     2677 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_maarc.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    29097 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_machine_design.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    12195 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_machine_design_all_of.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5153 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_machine_design_id_list_request.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     9145 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_md_search_result.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    18306 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_element.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    19458 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_element_history.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    30966 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_element_relationship.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    19118 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_element_relationship_history.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     7809 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_hierarchy.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    10023 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_location_information.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     4994 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_membership.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5605 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_permissions.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5628 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_project.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    11118 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_resource.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    14019 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_source.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     4280 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_status_basic_object.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     7074 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/item_type.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     8737 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/list_tbl.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    20719 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/locatable_item.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     9214 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/location_history_object.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     8054 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/log.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     4944 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/log_entry_edit_information.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     8461 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/machine_design_connector_list_object.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     4046 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/machine_design_item_info.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5728 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/new_app_information.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5208 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/new_catalog_element_information.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     8405 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/new_catalog_information.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     7202 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/new_control_relationship_information.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     6251 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/new_inventory_information.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     7685 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/new_location_information.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5751 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/new_machine_placeholder_options.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5350 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/promote_machine_element_information.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     6164 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/property_metadata.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    14686 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/property_type.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    21423 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/property_value.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    14381 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/property_value_history.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     7967 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/relationship_type.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     6856 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/relationship_type_handler.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     6086 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/representing_assembly_element_for_machine_information.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    14695 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/resource_type.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     6704 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/resource_type_category.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5580 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/role_type.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    18081 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/search_entities_options.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    19826 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/search_entities_results.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     6341 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/search_result.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5339 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/simple_location_information.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     9151 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/source.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     3415 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/source_id_list_request.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     7925 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/update_cable_design_assigned_item_information.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5298 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/update_machine_assigned_item_information.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     5596 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/user_group.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    12249 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/user_info.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)     4022 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/models/user_role.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)    12303 2023-04-06 20:52:44.000000 ComponentDB-API-3.15.5.dev1/cdbApi/rest.py
+-rw-rw-r--   0 darek     (1000) darek     (1000)       38 2023-04-06 20:52:45.935497 ComponentDB-API-3.15.5.dev1/setup.cfg
+-rw-rw-r--   0 darek     (1000) darek     (1000)     1037 2023-04-06 20:50:12.000000 ComponentDB-API-3.15.5.dev1/setup.py
```

### Comparing `ComponentDB-API-3.15.5.dev0/CdbApiFactory.py` & `ComponentDB-API-3.15.5.dev1/CdbApiFactory.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/ComponentDB_API.egg-info/SOURCES.txt` & `ComponentDB-API-3.15.5.dev1/ComponentDB_API.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/__init__.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/__init__.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/__init__.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/__init__.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/app_items_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/app_items_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/authentication_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/authentication_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/cable_catalog_items_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/cable_catalog_items_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/cable_design_items_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/cable_design_items_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/cable_import_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/cable_import_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/component_catalog_items_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/component_catalog_items_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/component_inventory_items_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/component_inventory_items_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/connector_types_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/connector_types_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/domain_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/domain_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/downloads_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/downloads_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/item_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/item_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/location_items_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/location_items_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/log_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/log_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/machine_design_items_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/machine_design_items_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/property_type_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/property_type_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/property_value_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/property_value_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/search_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/search_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/sources_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/sources_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/test_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/test_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api/users_api.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api/users_api.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/api_client.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/api_client.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/configuration.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/configuration.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/exceptions.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/exceptions.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/__init__.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/__init__.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/allowed_property_value.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/allowed_property_value.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/api_exception_message.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/api_exception_message.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/api_exception_message_exception.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/api_exception_message_exception.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/api_exception_message_exception_cause.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/api_exception_message_exception_cause.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/api_exception_message_exception_cause_stack_trace.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/api_exception_message_exception_cause_stack_trace.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/api_exception_message_exception_cause_suppressed.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/api_exception_message_exception_cause_suppressed.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/cable_catalog_item_info.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/cable_catalog_item_info.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/cable_design_connection_list_object.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/cable_design_connection_list_object.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/concise_item.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/concise_item.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/concise_item_options.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/concise_item_options.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/connector.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/connector.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/connector_type.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/connector_type.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/connector_type_id_list_request.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/connector_type_id_list_request.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/control_relationship_hierarchy.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/control_relationship_hierarchy.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/domain.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/domain.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/entity_info.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/entity_info.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/entity_type.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/entity_type.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/file_upload_object.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/file_upload_object.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/inline_object.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/inline_object.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item.py`

 * *Files 0% similar despite different names*

```diff
@@ -37,20 +37,20 @@
         'id': 'int',
         'name': 'str',
         'item_identifier1': 'str',
         'item_identifier2': 'str',
         'qr_id': 'int',
         'domain': 'Domain',
         'derived_from_item': 'Item',
-        'description': 'str',
         'domain_id': 'int',
         'item_category_list_import': 'list[ItemCategory]',
         'primary_image_for_item': 'str',
         'item_control': 'bool',
         'max_sort_order': 'float',
+        'description': 'str',
         'entity_type_list': 'list[EntityType]',
         'item_category_list': 'list[ItemCategory]',
         'item_type_list': 'list[ItemType]',
         'item_project_list': 'list[ItemProject]',
         'item_source_list': 'list[ItemSource]'
     }
 
@@ -58,46 +58,46 @@
         'id': 'id',
         'name': 'name',
         'item_identifier1': 'itemIdentifier1',
         'item_identifier2': 'itemIdentifier2',
         'qr_id': 'qrId',
         'domain': 'domain',
         'derived_from_item': 'derivedFromItem',
-        'description': 'description',
         'domain_id': 'domainId',
         'item_category_list_import': 'itemCategoryListImport',
         'primary_image_for_item': 'primaryImageForItem',
         'item_control': 'itemControl',
         'max_sort_order': 'maxSortOrder',
+        'description': 'description',
         'entity_type_list': 'entityTypeList',
         'item_category_list': 'itemCategoryList',
         'item_type_list': 'itemTypeList',
         'item_project_list': 'itemProjectList',
         'item_source_list': 'itemSourceList'
     }
 
-    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, description=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, description=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, local_vars_configuration=None):  # noqa: E501
         """Item - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._id = None
         self._name = None
         self._item_identifier1 = None
         self._item_identifier2 = None
         self._qr_id = None
         self._domain = None
         self._derived_from_item = None
-        self._description = None
         self._domain_id = None
         self._item_category_list_import = None
         self._primary_image_for_item = None
         self._item_control = None
         self._max_sort_order = None
+        self._description = None
         self._entity_type_list = None
         self._item_category_list = None
         self._item_type_list = None
         self._item_project_list = None
         self._item_source_list = None
         self.discriminator = None
 
@@ -111,26 +111,26 @@
             self.item_identifier2 = item_identifier2
         if qr_id is not None:
             self.qr_id = qr_id
         if domain is not None:
             self.domain = domain
         if derived_from_item is not None:
             self.derived_from_item = derived_from_item
-        if description is not None:
-            self.description = description
         if domain_id is not None:
             self.domain_id = domain_id
         if item_category_list_import is not None:
             self.item_category_list_import = item_category_list_import
         if primary_image_for_item is not None:
             self.primary_image_for_item = primary_image_for_item
         if item_control is not None:
             self.item_control = item_control
         if max_sort_order is not None:
             self.max_sort_order = max_sort_order
+        if description is not None:
+            self.description = description
         if entity_type_list is not None:
             self.entity_type_list = entity_type_list
         if item_category_list is not None:
             self.item_category_list = item_category_list
         if item_type_list is not None:
             self.item_type_list = item_type_list
         if item_project_list is not None:
@@ -303,41 +303,14 @@
         :param derived_from_item: The derived_from_item of this Item.  # noqa: E501
         :type: Item
         """
 
         self._derived_from_item = derived_from_item
 
     @property
-    def description(self):
-        """Gets the description of this Item.  # noqa: E501
-
-
-        :return: The description of this Item.  # noqa: E501
-        :rtype: str
-        """
-        return self._description
-
-    @description.setter
-    def description(self, description):
-        """Sets the description of this Item.
-
-
-        :param description: The description of this Item.  # noqa: E501
-        :type: str
-        """
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) > 256):
-            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) < 0):
-            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
-
-        self._description = description
-
-    @property
     def domain_id(self):
         """Gets the domain_id of this Item.  # noqa: E501
 
 
         :return: The domain_id of this Item.  # noqa: E501
         :rtype: int
         """
@@ -435,14 +408,41 @@
         :param max_sort_order: The max_sort_order of this Item.  # noqa: E501
         :type: float
         """
 
         self._max_sort_order = max_sort_order
 
     @property
+    def description(self):
+        """Gets the description of this Item.  # noqa: E501
+
+
+        :return: The description of this Item.  # noqa: E501
+        :rtype: str
+        """
+        return self._description
+
+    @description.setter
+    def description(self, description):
+        """Sets the description of this Item.
+
+
+        :param description: The description of this Item.  # noqa: E501
+        :type: str
+        """
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) > 256):
+            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) < 0):
+            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
+
+        self._description = description
+
+    @property
     def entity_type_list(self):
         """Gets the entity_type_list of this Item.  # noqa: E501
 
 
         :return: The entity_type_list of this Item.  # noqa: E501
         :rtype: list[EntityType]
         """
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_category.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_category.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_connector.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_connector.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_app.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_app.py`

 * *Files 0% similar despite different names*

```diff
@@ -37,20 +37,20 @@
         'id': 'int',
         'name': 'str',
         'item_identifier1': 'str',
         'item_identifier2': 'str',
         'qr_id': 'int',
         'domain': 'Domain',
         'derived_from_item': 'Item',
-        'description': 'str',
         'domain_id': 'int',
         'item_category_list_import': 'list[ItemCategory]',
         'primary_image_for_item': 'str',
         'item_control': 'bool',
         'max_sort_order': 'float',
+        'description': 'str',
         'entity_type_list': 'list[EntityType]',
         'item_category_list': 'list[ItemCategory]',
         'item_type_list': 'list[ItemType]',
         'item_project_list': 'list[ItemProject]',
         'item_source_list': 'list[ItemSource]'
     }
 
@@ -58,46 +58,46 @@
         'id': 'id',
         'name': 'name',
         'item_identifier1': 'itemIdentifier1',
         'item_identifier2': 'itemIdentifier2',
         'qr_id': 'qrId',
         'domain': 'domain',
         'derived_from_item': 'derivedFromItem',
-        'description': 'description',
         'domain_id': 'domainId',
         'item_category_list_import': 'itemCategoryListImport',
         'primary_image_for_item': 'primaryImageForItem',
         'item_control': 'itemControl',
         'max_sort_order': 'maxSortOrder',
+        'description': 'description',
         'entity_type_list': 'entityTypeList',
         'item_category_list': 'itemCategoryList',
         'item_type_list': 'itemTypeList',
         'item_project_list': 'itemProjectList',
         'item_source_list': 'itemSourceList'
     }
 
-    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, description=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, description=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, local_vars_configuration=None):  # noqa: E501
         """ItemDomainApp - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._id = None
         self._name = None
         self._item_identifier1 = None
         self._item_identifier2 = None
         self._qr_id = None
         self._domain = None
         self._derived_from_item = None
-        self._description = None
         self._domain_id = None
         self._item_category_list_import = None
         self._primary_image_for_item = None
         self._item_control = None
         self._max_sort_order = None
+        self._description = None
         self._entity_type_list = None
         self._item_category_list = None
         self._item_type_list = None
         self._item_project_list = None
         self._item_source_list = None
         self.discriminator = None
 
@@ -111,26 +111,26 @@
             self.item_identifier2 = item_identifier2
         if qr_id is not None:
             self.qr_id = qr_id
         if domain is not None:
             self.domain = domain
         if derived_from_item is not None:
             self.derived_from_item = derived_from_item
-        if description is not None:
-            self.description = description
         if domain_id is not None:
             self.domain_id = domain_id
         if item_category_list_import is not None:
             self.item_category_list_import = item_category_list_import
         if primary_image_for_item is not None:
             self.primary_image_for_item = primary_image_for_item
         if item_control is not None:
             self.item_control = item_control
         if max_sort_order is not None:
             self.max_sort_order = max_sort_order
+        if description is not None:
+            self.description = description
         if entity_type_list is not None:
             self.entity_type_list = entity_type_list
         if item_category_list is not None:
             self.item_category_list = item_category_list
         if item_type_list is not None:
             self.item_type_list = item_type_list
         if item_project_list is not None:
@@ -303,41 +303,14 @@
         :param derived_from_item: The derived_from_item of this ItemDomainApp.  # noqa: E501
         :type: Item
         """
 
         self._derived_from_item = derived_from_item
 
     @property
-    def description(self):
-        """Gets the description of this ItemDomainApp.  # noqa: E501
-
-
-        :return: The description of this ItemDomainApp.  # noqa: E501
-        :rtype: str
-        """
-        return self._description
-
-    @description.setter
-    def description(self, description):
-        """Sets the description of this ItemDomainApp.
-
-
-        :param description: The description of this ItemDomainApp.  # noqa: E501
-        :type: str
-        """
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) > 256):
-            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) < 0):
-            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
-
-        self._description = description
-
-    @property
     def domain_id(self):
         """Gets the domain_id of this ItemDomainApp.  # noqa: E501
 
 
         :return: The domain_id of this ItemDomainApp.  # noqa: E501
         :rtype: int
         """
@@ -435,14 +408,41 @@
         :param max_sort_order: The max_sort_order of this ItemDomainApp.  # noqa: E501
         :type: float
         """
 
         self._max_sort_order = max_sort_order
 
     @property
+    def description(self):
+        """Gets the description of this ItemDomainApp.  # noqa: E501
+
+
+        :return: The description of this ItemDomainApp.  # noqa: E501
+        :rtype: str
+        """
+        return self._description
+
+    @description.setter
+    def description(self, description):
+        """Sets the description of this ItemDomainApp.
+
+
+        :param description: The description of this ItemDomainApp.  # noqa: E501
+        :type: str
+        """
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) > 256):
+            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) < 0):
+            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
+
+        self._description = description
+
+    @property
     def entity_type_list(self):
         """Gets the entity_type_list of this ItemDomainApp.  # noqa: E501
 
 
         :return: The entity_type_list of this ItemDomainApp.  # noqa: E501
         :rtype: list[EntityType]
         """
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_catalog.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_catalog.py`

 * *Files 0% similar despite different names*

```diff
@@ -37,20 +37,20 @@
         'id': 'int',
         'name': 'str',
         'item_identifier1': 'str',
         'item_identifier2': 'str',
         'qr_id': 'int',
         'domain': 'Domain',
         'derived_from_item': 'Item',
-        'description': 'str',
         'domain_id': 'int',
         'item_category_list_import': 'list[ItemCategory]',
         'primary_image_for_item': 'str',
         'item_control': 'bool',
         'max_sort_order': 'float',
+        'description': 'str',
         'entity_type_list': 'list[EntityType]',
         'item_category_list': 'list[ItemCategory]',
         'item_type_list': 'list[ItemType]',
         'item_project_list': 'list[ItemProject]',
         'item_source_list': 'list[ItemSource]',
         'alternate_name': 'str'
     }
@@ -59,47 +59,47 @@
         'id': 'id',
         'name': 'name',
         'item_identifier1': 'itemIdentifier1',
         'item_identifier2': 'itemIdentifier2',
         'qr_id': 'qrId',
         'domain': 'domain',
         'derived_from_item': 'derivedFromItem',
-        'description': 'description',
         'domain_id': 'domainId',
         'item_category_list_import': 'itemCategoryListImport',
         'primary_image_for_item': 'primaryImageForItem',
         'item_control': 'itemControl',
         'max_sort_order': 'maxSortOrder',
+        'description': 'description',
         'entity_type_list': 'entityTypeList',
         'item_category_list': 'itemCategoryList',
         'item_type_list': 'itemTypeList',
         'item_project_list': 'itemProjectList',
         'item_source_list': 'itemSourceList',
         'alternate_name': 'alternateName'
     }
 
-    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, description=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, alternate_name=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, description=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, alternate_name=None, local_vars_configuration=None):  # noqa: E501
         """ItemDomainCableCatalog - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._id = None
         self._name = None
         self._item_identifier1 = None
         self._item_identifier2 = None
         self._qr_id = None
         self._domain = None
         self._derived_from_item = None
-        self._description = None
         self._domain_id = None
         self._item_category_list_import = None
         self._primary_image_for_item = None
         self._item_control = None
         self._max_sort_order = None
+        self._description = None
         self._entity_type_list = None
         self._item_category_list = None
         self._item_type_list = None
         self._item_project_list = None
         self._item_source_list = None
         self._alternate_name = None
         self.discriminator = None
@@ -114,26 +114,26 @@
             self.item_identifier2 = item_identifier2
         if qr_id is not None:
             self.qr_id = qr_id
         if domain is not None:
             self.domain = domain
         if derived_from_item is not None:
             self.derived_from_item = derived_from_item
-        if description is not None:
-            self.description = description
         if domain_id is not None:
             self.domain_id = domain_id
         if item_category_list_import is not None:
             self.item_category_list_import = item_category_list_import
         if primary_image_for_item is not None:
             self.primary_image_for_item = primary_image_for_item
         if item_control is not None:
             self.item_control = item_control
         if max_sort_order is not None:
             self.max_sort_order = max_sort_order
+        if description is not None:
+            self.description = description
         if entity_type_list is not None:
             self.entity_type_list = entity_type_list
         if item_category_list is not None:
             self.item_category_list = item_category_list
         if item_type_list is not None:
             self.item_type_list = item_type_list
         if item_project_list is not None:
@@ -308,41 +308,14 @@
         :param derived_from_item: The derived_from_item of this ItemDomainCableCatalog.  # noqa: E501
         :type: Item
         """
 
         self._derived_from_item = derived_from_item
 
     @property
-    def description(self):
-        """Gets the description of this ItemDomainCableCatalog.  # noqa: E501
-
-
-        :return: The description of this ItemDomainCableCatalog.  # noqa: E501
-        :rtype: str
-        """
-        return self._description
-
-    @description.setter
-    def description(self, description):
-        """Sets the description of this ItemDomainCableCatalog.
-
-
-        :param description: The description of this ItemDomainCableCatalog.  # noqa: E501
-        :type: str
-        """
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) > 256):
-            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) < 0):
-            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
-
-        self._description = description
-
-    @property
     def domain_id(self):
         """Gets the domain_id of this ItemDomainCableCatalog.  # noqa: E501
 
 
         :return: The domain_id of this ItemDomainCableCatalog.  # noqa: E501
         :rtype: int
         """
@@ -440,14 +413,41 @@
         :param max_sort_order: The max_sort_order of this ItemDomainCableCatalog.  # noqa: E501
         :type: float
         """
 
         self._max_sort_order = max_sort_order
 
     @property
+    def description(self):
+        """Gets the description of this ItemDomainCableCatalog.  # noqa: E501
+
+
+        :return: The description of this ItemDomainCableCatalog.  # noqa: E501
+        :rtype: str
+        """
+        return self._description
+
+    @description.setter
+    def description(self, description):
+        """Sets the description of this ItemDomainCableCatalog.
+
+
+        :param description: The description of this ItemDomainCableCatalog.  # noqa: E501
+        :type: str
+        """
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) > 256):
+            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) < 0):
+            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
+
+        self._description = description
+
+    @property
     def entity_type_list(self):
         """Gets the entity_type_list of this ItemDomainCableCatalog.  # noqa: E501
 
 
         :return: The entity_type_list of this ItemDomainCableCatalog.  # noqa: E501
         :rtype: list[EntityType]
         """
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_catalog_all_of.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_catalog_all_of.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_catalog_id_list_request.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_catalog_id_list_request.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_design.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_design.py`

 * *Files 0% similar despite different names*

```diff
@@ -37,90 +37,90 @@
         'id': 'int',
         'name': 'str',
         'item_identifier1': 'str',
         'item_identifier2': 'str',
         'qr_id': 'int',
         'domain': 'Domain',
         'derived_from_item': 'Item',
-        'description': 'str',
         'domain_id': 'int',
         'item_category_list_import': 'list[ItemCategory]',
         'primary_image_for_item': 'str',
         'item_control': 'bool',
         'max_sort_order': 'float',
+        'description': 'str',
         'entity_type_list': 'list[EntityType]',
         'item_category_list': 'list[ItemCategory]',
         'item_type_list': 'list[ItemType]',
         'item_project_list': 'list[ItemProject]',
         'item_source_list': 'list[ItemSource]',
-        'technical_system_list': 'list[ItemCategory]',
         'alternate_name': 'str',
         'assigned_item': 'Item',
         'is_housed': 'bool',
         'catalog_item': 'ItemDomainCableCatalog',
-        'inventory_item': 'ItemDomainCableInventory'
+        'inventory_item': 'ItemDomainCableInventory',
+        'technical_system_list': 'list[ItemCategory]'
     }
 
     attribute_map = {
         'id': 'id',
         'name': 'name',
         'item_identifier1': 'itemIdentifier1',
         'item_identifier2': 'itemIdentifier2',
         'qr_id': 'qrId',
         'domain': 'domain',
         'derived_from_item': 'derivedFromItem',
-        'description': 'description',
         'domain_id': 'domainId',
         'item_category_list_import': 'itemCategoryListImport',
         'primary_image_for_item': 'primaryImageForItem',
         'item_control': 'itemControl',
         'max_sort_order': 'maxSortOrder',
+        'description': 'description',
         'entity_type_list': 'entityTypeList',
         'item_category_list': 'itemCategoryList',
         'item_type_list': 'itemTypeList',
         'item_project_list': 'itemProjectList',
         'item_source_list': 'itemSourceList',
-        'technical_system_list': 'technicalSystemList',
         'alternate_name': 'alternateName',
         'assigned_item': 'assignedItem',
         'is_housed': 'isHoused',
         'catalog_item': 'catalogItem',
-        'inventory_item': 'inventoryItem'
+        'inventory_item': 'inventoryItem',
+        'technical_system_list': 'technicalSystemList'
     }
 
-    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, description=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, technical_system_list=None, alternate_name=None, assigned_item=None, is_housed=None, catalog_item=None, inventory_item=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, description=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, alternate_name=None, assigned_item=None, is_housed=None, catalog_item=None, inventory_item=None, technical_system_list=None, local_vars_configuration=None):  # noqa: E501
         """ItemDomainCableDesign - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._id = None
         self._name = None
         self._item_identifier1 = None
         self._item_identifier2 = None
         self._qr_id = None
         self._domain = None
         self._derived_from_item = None
-        self._description = None
         self._domain_id = None
         self._item_category_list_import = None
         self._primary_image_for_item = None
         self._item_control = None
         self._max_sort_order = None
+        self._description = None
         self._entity_type_list = None
         self._item_category_list = None
         self._item_type_list = None
         self._item_project_list = None
         self._item_source_list = None
-        self._technical_system_list = None
         self._alternate_name = None
         self._assigned_item = None
         self._is_housed = None
         self._catalog_item = None
         self._inventory_item = None
+        self._technical_system_list = None
         self.discriminator = None
 
         if id is not None:
             self.id = id
         if name is not None:
             self.name = name
         if item_identifier1 is not None:
@@ -129,48 +129,48 @@
             self.item_identifier2 = item_identifier2
         if qr_id is not None:
             self.qr_id = qr_id
         if domain is not None:
             self.domain = domain
         if derived_from_item is not None:
             self.derived_from_item = derived_from_item
-        if description is not None:
-            self.description = description
         if domain_id is not None:
             self.domain_id = domain_id
         if item_category_list_import is not None:
             self.item_category_list_import = item_category_list_import
         if primary_image_for_item is not None:
             self.primary_image_for_item = primary_image_for_item
         if item_control is not None:
             self.item_control = item_control
         if max_sort_order is not None:
             self.max_sort_order = max_sort_order
+        if description is not None:
+            self.description = description
         if entity_type_list is not None:
             self.entity_type_list = entity_type_list
         if item_category_list is not None:
             self.item_category_list = item_category_list
         if item_type_list is not None:
             self.item_type_list = item_type_list
         if item_project_list is not None:
             self.item_project_list = item_project_list
         if item_source_list is not None:
             self.item_source_list = item_source_list
-        if technical_system_list is not None:
-            self.technical_system_list = technical_system_list
         if alternate_name is not None:
             self.alternate_name = alternate_name
         if assigned_item is not None:
             self.assigned_item = assigned_item
         if is_housed is not None:
             self.is_housed = is_housed
         if catalog_item is not None:
             self.catalog_item = catalog_item
         if inventory_item is not None:
             self.inventory_item = inventory_item
+        if technical_system_list is not None:
+            self.technical_system_list = technical_system_list
 
     @property
     def id(self):
         """Gets the id of this ItemDomainCableDesign.  # noqa: E501
 
 
         :return: The id of this ItemDomainCableDesign.  # noqa: E501
@@ -333,41 +333,14 @@
         :param derived_from_item: The derived_from_item of this ItemDomainCableDesign.  # noqa: E501
         :type: Item
         """
 
         self._derived_from_item = derived_from_item
 
     @property
-    def description(self):
-        """Gets the description of this ItemDomainCableDesign.  # noqa: E501
-
-
-        :return: The description of this ItemDomainCableDesign.  # noqa: E501
-        :rtype: str
-        """
-        return self._description
-
-    @description.setter
-    def description(self, description):
-        """Sets the description of this ItemDomainCableDesign.
-
-
-        :param description: The description of this ItemDomainCableDesign.  # noqa: E501
-        :type: str
-        """
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) > 256):
-            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) < 0):
-            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
-
-        self._description = description
-
-    @property
     def domain_id(self):
         """Gets the domain_id of this ItemDomainCableDesign.  # noqa: E501
 
 
         :return: The domain_id of this ItemDomainCableDesign.  # noqa: E501
         :rtype: int
         """
@@ -465,14 +438,41 @@
         :param max_sort_order: The max_sort_order of this ItemDomainCableDesign.  # noqa: E501
         :type: float
         """
 
         self._max_sort_order = max_sort_order
 
     @property
+    def description(self):
+        """Gets the description of this ItemDomainCableDesign.  # noqa: E501
+
+
+        :return: The description of this ItemDomainCableDesign.  # noqa: E501
+        :rtype: str
+        """
+        return self._description
+
+    @description.setter
+    def description(self, description):
+        """Sets the description of this ItemDomainCableDesign.
+
+
+        :param description: The description of this ItemDomainCableDesign.  # noqa: E501
+        :type: str
+        """
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) > 256):
+            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) < 0):
+            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
+
+        self._description = description
+
+    @property
     def entity_type_list(self):
         """Gets the entity_type_list of this ItemDomainCableDesign.  # noqa: E501
 
 
         :return: The entity_type_list of this ItemDomainCableDesign.  # noqa: E501
         :rtype: list[EntityType]
         """
@@ -570,35 +570,14 @@
         :param item_source_list: The item_source_list of this ItemDomainCableDesign.  # noqa: E501
         :type: list[ItemSource]
         """
 
         self._item_source_list = item_source_list
 
     @property
-    def technical_system_list(self):
-        """Gets the technical_system_list of this ItemDomainCableDesign.  # noqa: E501
-
-
-        :return: The technical_system_list of this ItemDomainCableDesign.  # noqa: E501
-        :rtype: list[ItemCategory]
-        """
-        return self._technical_system_list
-
-    @technical_system_list.setter
-    def technical_system_list(self, technical_system_list):
-        """Sets the technical_system_list of this ItemDomainCableDesign.
-
-
-        :param technical_system_list: The technical_system_list of this ItemDomainCableDesign.  # noqa: E501
-        :type: list[ItemCategory]
-        """
-
-        self._technical_system_list = technical_system_list
-
-    @property
     def alternate_name(self):
         """Gets the alternate_name of this ItemDomainCableDesign.  # noqa: E501
 
 
         :return: The alternate_name of this ItemDomainCableDesign.  # noqa: E501
         :rtype: str
         """
@@ -695,14 +674,35 @@
 
         :param inventory_item: The inventory_item of this ItemDomainCableDesign.  # noqa: E501
         :type: ItemDomainCableInventory
         """
 
         self._inventory_item = inventory_item
 
+    @property
+    def technical_system_list(self):
+        """Gets the technical_system_list of this ItemDomainCableDesign.  # noqa: E501
+
+
+        :return: The technical_system_list of this ItemDomainCableDesign.  # noqa: E501
+        :rtype: list[ItemCategory]
+        """
+        return self._technical_system_list
+
+    @technical_system_list.setter
+    def technical_system_list(self, technical_system_list):
+        """Sets the technical_system_list of this ItemDomainCableDesign.
+
+
+        :param technical_system_list: The technical_system_list of this ItemDomainCableDesign.  # noqa: E501
+        :type: list[ItemCategory]
+        """
+
+        self._technical_system_list = technical_system_list
+
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.openapi_types):
             value = getattr(self, attr)
             if isinstance(value, list):
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_design_all_of.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_design_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -30,78 +30,57 @@
     Attributes:
       openapi_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     openapi_types = {
-        'technical_system_list': 'list[ItemCategory]',
         'alternate_name': 'str',
         'assigned_item': 'Item',
         'is_housed': 'bool',
         'catalog_item': 'ItemDomainCableCatalog',
-        'inventory_item': 'ItemDomainCableInventory'
+        'inventory_item': 'ItemDomainCableInventory',
+        'technical_system_list': 'list[ItemCategory]'
     }
 
     attribute_map = {
-        'technical_system_list': 'technicalSystemList',
         'alternate_name': 'alternateName',
         'assigned_item': 'assignedItem',
         'is_housed': 'isHoused',
         'catalog_item': 'catalogItem',
-        'inventory_item': 'inventoryItem'
+        'inventory_item': 'inventoryItem',
+        'technical_system_list': 'technicalSystemList'
     }
 
-    def __init__(self, technical_system_list=None, alternate_name=None, assigned_item=None, is_housed=None, catalog_item=None, inventory_item=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, alternate_name=None, assigned_item=None, is_housed=None, catalog_item=None, inventory_item=None, technical_system_list=None, local_vars_configuration=None):  # noqa: E501
         """ItemDomainCableDesignAllOf - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
-        self._technical_system_list = None
         self._alternate_name = None
         self._assigned_item = None
         self._is_housed = None
         self._catalog_item = None
         self._inventory_item = None
+        self._technical_system_list = None
         self.discriminator = None
 
-        if technical_system_list is not None:
-            self.technical_system_list = technical_system_list
         if alternate_name is not None:
             self.alternate_name = alternate_name
         if assigned_item is not None:
             self.assigned_item = assigned_item
         if is_housed is not None:
             self.is_housed = is_housed
         if catalog_item is not None:
             self.catalog_item = catalog_item
         if inventory_item is not None:
             self.inventory_item = inventory_item
-
-    @property
-    def technical_system_list(self):
-        """Gets the technical_system_list of this ItemDomainCableDesignAllOf.  # noqa: E501
-
-
-        :return: The technical_system_list of this ItemDomainCableDesignAllOf.  # noqa: E501
-        :rtype: list[ItemCategory]
-        """
-        return self._technical_system_list
-
-    @technical_system_list.setter
-    def technical_system_list(self, technical_system_list):
-        """Sets the technical_system_list of this ItemDomainCableDesignAllOf.
-
-
-        :param technical_system_list: The technical_system_list of this ItemDomainCableDesignAllOf.  # noqa: E501
-        :type: list[ItemCategory]
-        """
-
-        self._technical_system_list = technical_system_list
+        if technical_system_list is not None:
+            self.technical_system_list = technical_system_list
 
     @property
     def alternate_name(self):
         """Gets the alternate_name of this ItemDomainCableDesignAllOf.  # noqa: E501
 
 
         :return: The alternate_name of this ItemDomainCableDesignAllOf.  # noqa: E501
@@ -200,14 +179,35 @@
 
         :param inventory_item: The inventory_item of this ItemDomainCableDesignAllOf.  # noqa: E501
         :type: ItemDomainCableInventory
         """
 
         self._inventory_item = inventory_item
 
+    @property
+    def technical_system_list(self):
+        """Gets the technical_system_list of this ItemDomainCableDesignAllOf.  # noqa: E501
+
+
+        :return: The technical_system_list of this ItemDomainCableDesignAllOf.  # noqa: E501
+        :rtype: list[ItemCategory]
+        """
+        return self._technical_system_list
+
+    @technical_system_list.setter
+    def technical_system_list(self, technical_system_list):
+        """Sets the technical_system_list of this ItemDomainCableDesignAllOf.
+
+
+        :param technical_system_list: The technical_system_list of this ItemDomainCableDesignAllOf.  # noqa: E501
+        :type: list[ItemCategory]
+        """
+
+        self._technical_system_list = technical_system_list
+
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.openapi_types):
             value = getattr(self, attr)
             if isinstance(value, list):
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_design_id_list_request.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_design_id_list_request.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_inventory.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_inventory.py`

 * *Files 0% similar despite different names*

```diff
@@ -37,20 +37,20 @@
         'id': 'int',
         'name': 'str',
         'item_identifier1': 'str',
         'item_identifier2': 'str',
         'qr_id': 'int',
         'domain': 'Domain',
         'derived_from_item': 'Item',
-        'description': 'str',
         'domain_id': 'int',
         'item_category_list_import': 'list[ItemCategory]',
         'primary_image_for_item': 'str',
         'item_control': 'bool',
         'max_sort_order': 'float',
+        'description': 'str',
         'entity_type_list': 'list[EntityType]',
         'item_category_list': 'list[ItemCategory]',
         'item_type_list': 'list[ItemType]',
         'item_project_list': 'list[ItemProject]',
         'item_source_list': 'list[ItemSource]',
         'membership_loaded': 'bool',
         'catalog_item': 'ItemDomainCableCatalog',
@@ -61,49 +61,49 @@
         'id': 'id',
         'name': 'name',
         'item_identifier1': 'itemIdentifier1',
         'item_identifier2': 'itemIdentifier2',
         'qr_id': 'qrId',
         'domain': 'domain',
         'derived_from_item': 'derivedFromItem',
-        'description': 'description',
         'domain_id': 'domainId',
         'item_category_list_import': 'itemCategoryListImport',
         'primary_image_for_item': 'primaryImageForItem',
         'item_control': 'itemControl',
         'max_sort_order': 'maxSortOrder',
+        'description': 'description',
         'entity_type_list': 'entityTypeList',
         'item_category_list': 'itemCategoryList',
         'item_type_list': 'itemTypeList',
         'item_project_list': 'itemProjectList',
         'item_source_list': 'itemSourceList',
         'membership_loaded': 'membershipLoaded',
         'catalog_item': 'catalogItem',
         'location_item': 'locationItem'
     }
 
-    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, description=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, membership_loaded=None, catalog_item=None, location_item=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, description=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, membership_loaded=None, catalog_item=None, location_item=None, local_vars_configuration=None):  # noqa: E501
         """ItemDomainCableInventory - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._id = None
         self._name = None
         self._item_identifier1 = None
         self._item_identifier2 = None
         self._qr_id = None
         self._domain = None
         self._derived_from_item = None
-        self._description = None
         self._domain_id = None
         self._item_category_list_import = None
         self._primary_image_for_item = None
         self._item_control = None
         self._max_sort_order = None
+        self._description = None
         self._entity_type_list = None
         self._item_category_list = None
         self._item_type_list = None
         self._item_project_list = None
         self._item_source_list = None
         self._membership_loaded = None
         self._catalog_item = None
@@ -120,26 +120,26 @@
             self.item_identifier2 = item_identifier2
         if qr_id is not None:
             self.qr_id = qr_id
         if domain is not None:
             self.domain = domain
         if derived_from_item is not None:
             self.derived_from_item = derived_from_item
-        if description is not None:
-            self.description = description
         if domain_id is not None:
             self.domain_id = domain_id
         if item_category_list_import is not None:
             self.item_category_list_import = item_category_list_import
         if primary_image_for_item is not None:
             self.primary_image_for_item = primary_image_for_item
         if item_control is not None:
             self.item_control = item_control
         if max_sort_order is not None:
             self.max_sort_order = max_sort_order
+        if description is not None:
+            self.description = description
         if entity_type_list is not None:
             self.entity_type_list = entity_type_list
         if item_category_list is not None:
             self.item_category_list = item_category_list
         if item_type_list is not None:
             self.item_type_list = item_type_list
         if item_project_list is not None:
@@ -318,41 +318,14 @@
         :param derived_from_item: The derived_from_item of this ItemDomainCableInventory.  # noqa: E501
         :type: Item
         """
 
         self._derived_from_item = derived_from_item
 
     @property
-    def description(self):
-        """Gets the description of this ItemDomainCableInventory.  # noqa: E501
-
-
-        :return: The description of this ItemDomainCableInventory.  # noqa: E501
-        :rtype: str
-        """
-        return self._description
-
-    @description.setter
-    def description(self, description):
-        """Sets the description of this ItemDomainCableInventory.
-
-
-        :param description: The description of this ItemDomainCableInventory.  # noqa: E501
-        :type: str
-        """
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) > 256):
-            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) < 0):
-            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
-
-        self._description = description
-
-    @property
     def domain_id(self):
         """Gets the domain_id of this ItemDomainCableInventory.  # noqa: E501
 
 
         :return: The domain_id of this ItemDomainCableInventory.  # noqa: E501
         :rtype: int
         """
@@ -450,14 +423,41 @@
         :param max_sort_order: The max_sort_order of this ItemDomainCableInventory.  # noqa: E501
         :type: float
         """
 
         self._max_sort_order = max_sort_order
 
     @property
+    def description(self):
+        """Gets the description of this ItemDomainCableInventory.  # noqa: E501
+
+
+        :return: The description of this ItemDomainCableInventory.  # noqa: E501
+        :rtype: str
+        """
+        return self._description
+
+    @description.setter
+    def description(self, description):
+        """Sets the description of this ItemDomainCableInventory.
+
+
+        :param description: The description of this ItemDomainCableInventory.  # noqa: E501
+        :type: str
+        """
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) > 256):
+            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) < 0):
+            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
+
+        self._description = description
+
+    @property
     def entity_type_list(self):
         """Gets the entity_type_list of this ItemDomainCableInventory.  # noqa: E501
 
 
         :return: The entity_type_list of this ItemDomainCableInventory.  # noqa: E501
         :rtype: list[EntityType]
         """
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_cable_inventory_all_of.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_cable_inventory_all_of.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_catalog.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_catalog.py`

 * *Files 0% similar despite different names*

```diff
@@ -37,20 +37,20 @@
         'id': 'int',
         'name': 'str',
         'item_identifier1': 'str',
         'item_identifier2': 'str',
         'qr_id': 'int',
         'domain': 'Domain',
         'derived_from_item': 'Item',
-        'description': 'str',
         'domain_id': 'int',
         'item_category_list_import': 'list[ItemCategory]',
         'primary_image_for_item': 'str',
         'item_control': 'bool',
         'max_sort_order': 'float',
+        'description': 'str',
         'entity_type_list': 'list[EntityType]',
         'item_category_list': 'list[ItemCategory]',
         'item_type_list': 'list[ItemType]',
         'item_project_list': 'list[ItemProject]',
         'item_source_list': 'list[ItemSource]',
         'alternate_name': 'str'
     }
@@ -59,47 +59,47 @@
         'id': 'id',
         'name': 'name',
         'item_identifier1': 'itemIdentifier1',
         'item_identifier2': 'itemIdentifier2',
         'qr_id': 'qrId',
         'domain': 'domain',
         'derived_from_item': 'derivedFromItem',
-        'description': 'description',
         'domain_id': 'domainId',
         'item_category_list_import': 'itemCategoryListImport',
         'primary_image_for_item': 'primaryImageForItem',
         'item_control': 'itemControl',
         'max_sort_order': 'maxSortOrder',
+        'description': 'description',
         'entity_type_list': 'entityTypeList',
         'item_category_list': 'itemCategoryList',
         'item_type_list': 'itemTypeList',
         'item_project_list': 'itemProjectList',
         'item_source_list': 'itemSourceList',
         'alternate_name': 'alternateName'
     }
 
-    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, description=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, alternate_name=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, description=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, alternate_name=None, local_vars_configuration=None):  # noqa: E501
         """ItemDomainCatalog - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._id = None
         self._name = None
         self._item_identifier1 = None
         self._item_identifier2 = None
         self._qr_id = None
         self._domain = None
         self._derived_from_item = None
-        self._description = None
         self._domain_id = None
         self._item_category_list_import = None
         self._primary_image_for_item = None
         self._item_control = None
         self._max_sort_order = None
+        self._description = None
         self._entity_type_list = None
         self._item_category_list = None
         self._item_type_list = None
         self._item_project_list = None
         self._item_source_list = None
         self._alternate_name = None
         self.discriminator = None
@@ -114,26 +114,26 @@
             self.item_identifier2 = item_identifier2
         if qr_id is not None:
             self.qr_id = qr_id
         if domain is not None:
             self.domain = domain
         if derived_from_item is not None:
             self.derived_from_item = derived_from_item
-        if description is not None:
-            self.description = description
         if domain_id is not None:
             self.domain_id = domain_id
         if item_category_list_import is not None:
             self.item_category_list_import = item_category_list_import
         if primary_image_for_item is not None:
             self.primary_image_for_item = primary_image_for_item
         if item_control is not None:
             self.item_control = item_control
         if max_sort_order is not None:
             self.max_sort_order = max_sort_order
+        if description is not None:
+            self.description = description
         if entity_type_list is not None:
             self.entity_type_list = entity_type_list
         if item_category_list is not None:
             self.item_category_list = item_category_list
         if item_type_list is not None:
             self.item_type_list = item_type_list
         if item_project_list is not None:
@@ -308,41 +308,14 @@
         :param derived_from_item: The derived_from_item of this ItemDomainCatalog.  # noqa: E501
         :type: Item
         """
 
         self._derived_from_item = derived_from_item
 
     @property
-    def description(self):
-        """Gets the description of this ItemDomainCatalog.  # noqa: E501
-
-
-        :return: The description of this ItemDomainCatalog.  # noqa: E501
-        :rtype: str
-        """
-        return self._description
-
-    @description.setter
-    def description(self, description):
-        """Sets the description of this ItemDomainCatalog.
-
-
-        :param description: The description of this ItemDomainCatalog.  # noqa: E501
-        :type: str
-        """
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) > 256):
-            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) < 0):
-            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
-
-        self._description = description
-
-    @property
     def domain_id(self):
         """Gets the domain_id of this ItemDomainCatalog.  # noqa: E501
 
 
         :return: The domain_id of this ItemDomainCatalog.  # noqa: E501
         :rtype: int
         """
@@ -440,14 +413,41 @@
         :param max_sort_order: The max_sort_order of this ItemDomainCatalog.  # noqa: E501
         :type: float
         """
 
         self._max_sort_order = max_sort_order
 
     @property
+    def description(self):
+        """Gets the description of this ItemDomainCatalog.  # noqa: E501
+
+
+        :return: The description of this ItemDomainCatalog.  # noqa: E501
+        :rtype: str
+        """
+        return self._description
+
+    @description.setter
+    def description(self, description):
+        """Sets the description of this ItemDomainCatalog.
+
+
+        :param description: The description of this ItemDomainCatalog.  # noqa: E501
+        :type: str
+        """
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) > 256):
+            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) < 0):
+            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
+
+        self._description = description
+
+    @property
     def entity_type_list(self):
         """Gets the entity_type_list of this ItemDomainCatalog.  # noqa: E501
 
 
         :return: The entity_type_list of this ItemDomainCatalog.  # noqa: E501
         :rtype: list[EntityType]
         """
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_catalog_base.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_catalog_base.py`

 * *Files 0% similar despite different names*

```diff
@@ -38,20 +38,20 @@
         'name': 'str',
         'item_identifier1': 'str',
         'item_identifier2': 'str',
         'qr_id': 'int',
         'domain': 'Domain',
         'derived_from_item': 'Item',
         'alternate_name': 'str',
-        'description': 'str',
         'domain_id': 'int',
         'item_category_list_import': 'list[ItemCategory]',
         'primary_image_for_item': 'str',
         'item_control': 'bool',
         'max_sort_order': 'float',
+        'description': 'str',
         'entity_type_list': 'list[EntityType]',
         'item_category_list': 'list[ItemCategory]',
         'item_type_list': 'list[ItemType]',
         'item_project_list': 'list[ItemProject]',
         'item_source_list': 'list[ItemSource]'
     }
 
@@ -60,47 +60,47 @@
         'name': 'name',
         'item_identifier1': 'itemIdentifier1',
         'item_identifier2': 'itemIdentifier2',
         'qr_id': 'qrId',
         'domain': 'domain',
         'derived_from_item': 'derivedFromItem',
         'alternate_name': 'alternateName',
-        'description': 'description',
         'domain_id': 'domainId',
         'item_category_list_import': 'itemCategoryListImport',
         'primary_image_for_item': 'primaryImageForItem',
         'item_control': 'itemControl',
         'max_sort_order': 'maxSortOrder',
+        'description': 'description',
         'entity_type_list': 'entityTypeList',
         'item_category_list': 'itemCategoryList',
         'item_type_list': 'itemTypeList',
         'item_project_list': 'itemProjectList',
         'item_source_list': 'itemSourceList'
     }
 
-    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, alternate_name=None, description=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, alternate_name=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, description=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, local_vars_configuration=None):  # noqa: E501
         """ItemDomainCatalogBase - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._id = None
         self._name = None
         self._item_identifier1 = None
         self._item_identifier2 = None
         self._qr_id = None
         self._domain = None
         self._derived_from_item = None
         self._alternate_name = None
-        self._description = None
         self._domain_id = None
         self._item_category_list_import = None
         self._primary_image_for_item = None
         self._item_control = None
         self._max_sort_order = None
+        self._description = None
         self._entity_type_list = None
         self._item_category_list = None
         self._item_type_list = None
         self._item_project_list = None
         self._item_source_list = None
         self.discriminator = None
 
@@ -116,26 +116,26 @@
             self.qr_id = qr_id
         if domain is not None:
             self.domain = domain
         if derived_from_item is not None:
             self.derived_from_item = derived_from_item
         if alternate_name is not None:
             self.alternate_name = alternate_name
-        if description is not None:
-            self.description = description
         if domain_id is not None:
             self.domain_id = domain_id
         if item_category_list_import is not None:
             self.item_category_list_import = item_category_list_import
         if primary_image_for_item is not None:
             self.primary_image_for_item = primary_image_for_item
         if item_control is not None:
             self.item_control = item_control
         if max_sort_order is not None:
             self.max_sort_order = max_sort_order
+        if description is not None:
+            self.description = description
         if entity_type_list is not None:
             self.entity_type_list = entity_type_list
         if item_category_list is not None:
             self.item_category_list = item_category_list
         if item_type_list is not None:
             self.item_type_list = item_type_list
         if item_project_list is not None:
@@ -329,41 +329,14 @@
         :param alternate_name: The alternate_name of this ItemDomainCatalogBase.  # noqa: E501
         :type: str
         """
 
         self._alternate_name = alternate_name
 
     @property
-    def description(self):
-        """Gets the description of this ItemDomainCatalogBase.  # noqa: E501
-
-
-        :return: The description of this ItemDomainCatalogBase.  # noqa: E501
-        :rtype: str
-        """
-        return self._description
-
-    @description.setter
-    def description(self, description):
-        """Sets the description of this ItemDomainCatalogBase.
-
-
-        :param description: The description of this ItemDomainCatalogBase.  # noqa: E501
-        :type: str
-        """
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) > 256):
-            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) < 0):
-            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
-
-        self._description = description
-
-    @property
     def domain_id(self):
         """Gets the domain_id of this ItemDomainCatalogBase.  # noqa: E501
 
 
         :return: The domain_id of this ItemDomainCatalogBase.  # noqa: E501
         :rtype: int
         """
@@ -461,14 +434,41 @@
         :param max_sort_order: The max_sort_order of this ItemDomainCatalogBase.  # noqa: E501
         :type: float
         """
 
         self._max_sort_order = max_sort_order
 
     @property
+    def description(self):
+        """Gets the description of this ItemDomainCatalogBase.  # noqa: E501
+
+
+        :return: The description of this ItemDomainCatalogBase.  # noqa: E501
+        :rtype: str
+        """
+        return self._description
+
+    @description.setter
+    def description(self, description):
+        """Sets the description of this ItemDomainCatalogBase.
+
+
+        :param description: The description of this ItemDomainCatalogBase.  # noqa: E501
+        :type: str
+        """
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) > 256):
+            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) < 0):
+            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
+
+        self._description = description
+
+    @property
     def entity_type_list(self):
         """Gets the entity_type_list of this ItemDomainCatalogBase.  # noqa: E501
 
 
         :return: The entity_type_list of this ItemDomainCatalogBase.  # noqa: E501
         :rtype: list[EntityType]
         """
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_catalog_search_result.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_catalog_search_result.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_inventory.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_inventory.py`

 * *Files 0% similar despite different names*

```diff
@@ -37,86 +37,86 @@
         'id': 'int',
         'name': 'str',
         'item_identifier1': 'str',
         'item_identifier2': 'str',
         'qr_id': 'int',
         'domain': 'Domain',
         'derived_from_item': 'Item',
-        'description': 'str',
         'domain_id': 'int',
         'item_category_list_import': 'list[ItemCategory]',
         'primary_image_for_item': 'str',
         'item_control': 'bool',
         'max_sort_order': 'float',
+        'description': 'str',
         'entity_type_list': 'list[EntityType]',
         'item_category_list': 'list[ItemCategory]',
         'item_type_list': 'list[ItemType]',
         'item_project_list': 'list[ItemProject]',
         'item_source_list': 'list[ItemSource]',
         'membership_loaded': 'bool',
         'serial_number': 'str',
-        'catalog_item': 'ItemDomainCatalog',
         'tag': 'str',
+        'catalog_item': 'ItemDomainCatalog',
         'location_item': 'ItemDomainLocation'
     }
 
     attribute_map = {
         'id': 'id',
         'name': 'name',
         'item_identifier1': 'itemIdentifier1',
         'item_identifier2': 'itemIdentifier2',
         'qr_id': 'qrId',
         'domain': 'domain',
         'derived_from_item': 'derivedFromItem',
-        'description': 'description',
         'domain_id': 'domainId',
         'item_category_list_import': 'itemCategoryListImport',
         'primary_image_for_item': 'primaryImageForItem',
         'item_control': 'itemControl',
         'max_sort_order': 'maxSortOrder',
+        'description': 'description',
         'entity_type_list': 'entityTypeList',
         'item_category_list': 'itemCategoryList',
         'item_type_list': 'itemTypeList',
         'item_project_list': 'itemProjectList',
         'item_source_list': 'itemSourceList',
         'membership_loaded': 'membershipLoaded',
         'serial_number': 'serialNumber',
-        'catalog_item': 'catalogItem',
         'tag': 'tag',
+        'catalog_item': 'catalogItem',
         'location_item': 'locationItem'
     }
 
-    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, description=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, membership_loaded=None, serial_number=None, catalog_item=None, tag=None, location_item=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, description=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, membership_loaded=None, serial_number=None, tag=None, catalog_item=None, location_item=None, local_vars_configuration=None):  # noqa: E501
         """ItemDomainInventory - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._id = None
         self._name = None
         self._item_identifier1 = None
         self._item_identifier2 = None
         self._qr_id = None
         self._domain = None
         self._derived_from_item = None
-        self._description = None
         self._domain_id = None
         self._item_category_list_import = None
         self._primary_image_for_item = None
         self._item_control = None
         self._max_sort_order = None
+        self._description = None
         self._entity_type_list = None
         self._item_category_list = None
         self._item_type_list = None
         self._item_project_list = None
         self._item_source_list = None
         self._membership_loaded = None
         self._serial_number = None
-        self._catalog_item = None
         self._tag = None
+        self._catalog_item = None
         self._location_item = None
         self.discriminator = None
 
         if id is not None:
             self.id = id
         if name is not None:
             self.name = name
@@ -126,44 +126,44 @@
             self.item_identifier2 = item_identifier2
         if qr_id is not None:
             self.qr_id = qr_id
         if domain is not None:
             self.domain = domain
         if derived_from_item is not None:
             self.derived_from_item = derived_from_item
-        if description is not None:
-            self.description = description
         if domain_id is not None:
             self.domain_id = domain_id
         if item_category_list_import is not None:
             self.item_category_list_import = item_category_list_import
         if primary_image_for_item is not None:
             self.primary_image_for_item = primary_image_for_item
         if item_control is not None:
             self.item_control = item_control
         if max_sort_order is not None:
             self.max_sort_order = max_sort_order
+        if description is not None:
+            self.description = description
         if entity_type_list is not None:
             self.entity_type_list = entity_type_list
         if item_category_list is not None:
             self.item_category_list = item_category_list
         if item_type_list is not None:
             self.item_type_list = item_type_list
         if item_project_list is not None:
             self.item_project_list = item_project_list
         if item_source_list is not None:
             self.item_source_list = item_source_list
         if membership_loaded is not None:
             self.membership_loaded = membership_loaded
         if serial_number is not None:
             self.serial_number = serial_number
-        if catalog_item is not None:
-            self.catalog_item = catalog_item
         if tag is not None:
             self.tag = tag
+        if catalog_item is not None:
+            self.catalog_item = catalog_item
         if location_item is not None:
             self.location_item = location_item
 
     @property
     def id(self):
         """Gets the id of this ItemDomainInventory.  # noqa: E501
 
@@ -328,41 +328,14 @@
         :param derived_from_item: The derived_from_item of this ItemDomainInventory.  # noqa: E501
         :type: Item
         """
 
         self._derived_from_item = derived_from_item
 
     @property
-    def description(self):
-        """Gets the description of this ItemDomainInventory.  # noqa: E501
-
-
-        :return: The description of this ItemDomainInventory.  # noqa: E501
-        :rtype: str
-        """
-        return self._description
-
-    @description.setter
-    def description(self, description):
-        """Sets the description of this ItemDomainInventory.
-
-
-        :param description: The description of this ItemDomainInventory.  # noqa: E501
-        :type: str
-        """
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) > 256):
-            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) < 0):
-            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
-
-        self._description = description
-
-    @property
     def domain_id(self):
         """Gets the domain_id of this ItemDomainInventory.  # noqa: E501
 
 
         :return: The domain_id of this ItemDomainInventory.  # noqa: E501
         :rtype: int
         """
@@ -460,14 +433,41 @@
         :param max_sort_order: The max_sort_order of this ItemDomainInventory.  # noqa: E501
         :type: float
         """
 
         self._max_sort_order = max_sort_order
 
     @property
+    def description(self):
+        """Gets the description of this ItemDomainInventory.  # noqa: E501
+
+
+        :return: The description of this ItemDomainInventory.  # noqa: E501
+        :rtype: str
+        """
+        return self._description
+
+    @description.setter
+    def description(self, description):
+        """Sets the description of this ItemDomainInventory.
+
+
+        :param description: The description of this ItemDomainInventory.  # noqa: E501
+        :type: str
+        """
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) > 256):
+            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) < 0):
+            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
+
+        self._description = description
+
+    @property
     def entity_type_list(self):
         """Gets the entity_type_list of this ItemDomainInventory.  # noqa: E501
 
 
         :return: The entity_type_list of this ItemDomainInventory.  # noqa: E501
         :rtype: list[EntityType]
         """
@@ -607,35 +607,14 @@
         :param serial_number: The serial_number of this ItemDomainInventory.  # noqa: E501
         :type: str
         """
 
         self._serial_number = serial_number
 
     @property
-    def catalog_item(self):
-        """Gets the catalog_item of this ItemDomainInventory.  # noqa: E501
-
-
-        :return: The catalog_item of this ItemDomainInventory.  # noqa: E501
-        :rtype: ItemDomainCatalog
-        """
-        return self._catalog_item
-
-    @catalog_item.setter
-    def catalog_item(self, catalog_item):
-        """Sets the catalog_item of this ItemDomainInventory.
-
-
-        :param catalog_item: The catalog_item of this ItemDomainInventory.  # noqa: E501
-        :type: ItemDomainCatalog
-        """
-
-        self._catalog_item = catalog_item
-
-    @property
     def tag(self):
         """Gets the tag of this ItemDomainInventory.  # noqa: E501
 
 
         :return: The tag of this ItemDomainInventory.  # noqa: E501
         :rtype: str
         """
@@ -649,14 +628,35 @@
         :param tag: The tag of this ItemDomainInventory.  # noqa: E501
         :type: str
         """
 
         self._tag = tag
 
     @property
+    def catalog_item(self):
+        """Gets the catalog_item of this ItemDomainInventory.  # noqa: E501
+
+
+        :return: The catalog_item of this ItemDomainInventory.  # noqa: E501
+        :rtype: ItemDomainCatalog
+        """
+        return self._catalog_item
+
+    @catalog_item.setter
+    def catalog_item(self, catalog_item):
+        """Sets the catalog_item of this ItemDomainInventory.
+
+
+        :param catalog_item: The catalog_item of this ItemDomainInventory.  # noqa: E501
+        :type: ItemDomainCatalog
+        """
+
+        self._catalog_item = catalog_item
+
+    @property
     def location_item(self):
         """Gets the location_item of this ItemDomainInventory.  # noqa: E501
 
 
         :return: The location_item of this ItemDomainInventory.  # noqa: E501
         :rtype: ItemDomainLocation
         """
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_inventory_all_of.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_inventory_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -32,48 +32,48 @@
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     openapi_types = {
         'membership_loaded': 'bool',
         'serial_number': 'str',
-        'catalog_item': 'ItemDomainCatalog',
         'tag': 'str',
+        'catalog_item': 'ItemDomainCatalog',
         'location_item': 'ItemDomainLocation'
     }
 
     attribute_map = {
         'membership_loaded': 'membershipLoaded',
         'serial_number': 'serialNumber',
-        'catalog_item': 'catalogItem',
         'tag': 'tag',
+        'catalog_item': 'catalogItem',
         'location_item': 'locationItem'
     }
 
-    def __init__(self, membership_loaded=None, serial_number=None, catalog_item=None, tag=None, location_item=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, membership_loaded=None, serial_number=None, tag=None, catalog_item=None, location_item=None, local_vars_configuration=None):  # noqa: E501
         """ItemDomainInventoryAllOf - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._membership_loaded = None
         self._serial_number = None
-        self._catalog_item = None
         self._tag = None
+        self._catalog_item = None
         self._location_item = None
         self.discriminator = None
 
         if membership_loaded is not None:
             self.membership_loaded = membership_loaded
         if serial_number is not None:
             self.serial_number = serial_number
-        if catalog_item is not None:
-            self.catalog_item = catalog_item
         if tag is not None:
             self.tag = tag
+        if catalog_item is not None:
+            self.catalog_item = catalog_item
         if location_item is not None:
             self.location_item = location_item
 
     @property
     def membership_loaded(self):
         """Gets the membership_loaded of this ItemDomainInventoryAllOf.  # noqa: E501
 
@@ -112,35 +112,14 @@
         :param serial_number: The serial_number of this ItemDomainInventoryAllOf.  # noqa: E501
         :type: str
         """
 
         self._serial_number = serial_number
 
     @property
-    def catalog_item(self):
-        """Gets the catalog_item of this ItemDomainInventoryAllOf.  # noqa: E501
-
-
-        :return: The catalog_item of this ItemDomainInventoryAllOf.  # noqa: E501
-        :rtype: ItemDomainCatalog
-        """
-        return self._catalog_item
-
-    @catalog_item.setter
-    def catalog_item(self, catalog_item):
-        """Sets the catalog_item of this ItemDomainInventoryAllOf.
-
-
-        :param catalog_item: The catalog_item of this ItemDomainInventoryAllOf.  # noqa: E501
-        :type: ItemDomainCatalog
-        """
-
-        self._catalog_item = catalog_item
-
-    @property
     def tag(self):
         """Gets the tag of this ItemDomainInventoryAllOf.  # noqa: E501
 
 
         :return: The tag of this ItemDomainInventoryAllOf.  # noqa: E501
         :rtype: str
         """
@@ -154,14 +133,35 @@
         :param tag: The tag of this ItemDomainInventoryAllOf.  # noqa: E501
         :type: str
         """
 
         self._tag = tag
 
     @property
+    def catalog_item(self):
+        """Gets the catalog_item of this ItemDomainInventoryAllOf.  # noqa: E501
+
+
+        :return: The catalog_item of this ItemDomainInventoryAllOf.  # noqa: E501
+        :rtype: ItemDomainCatalog
+        """
+        return self._catalog_item
+
+    @catalog_item.setter
+    def catalog_item(self, catalog_item):
+        """Sets the catalog_item of this ItemDomainInventoryAllOf.
+
+
+        :param catalog_item: The catalog_item of this ItemDomainInventoryAllOf.  # noqa: E501
+        :type: ItemDomainCatalog
+        """
+
+        self._catalog_item = catalog_item
+
+    @property
     def location_item(self):
         """Gets the location_item of this ItemDomainInventoryAllOf.  # noqa: E501
 
 
         :return: The location_item of this ItemDomainInventoryAllOf.  # noqa: E501
         :rtype: ItemDomainLocation
         """
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_inventory_base.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_inventory_base.py`

 * *Files 0% similar despite different names*

```diff
@@ -41,20 +41,20 @@
         'qr_id': 'int',
         'domain': 'Domain',
         'derived_from_item': 'Item',
         'membership_loaded': 'bool',
         'catalog_item': 'ItemDomainCatalogBase',
         'status_property_type_name': 'str',
         'location_item': 'ItemDomainLocation',
-        'description': 'str',
         'domain_id': 'int',
         'item_category_list_import': 'list[ItemCategory]',
         'primary_image_for_item': 'str',
         'item_control': 'bool',
         'max_sort_order': 'float',
+        'description': 'str',
         'entity_type_list': 'list[EntityType]',
         'item_category_list': 'list[ItemCategory]',
         'item_type_list': 'list[ItemType]',
         'item_project_list': 'list[ItemProject]',
         'item_source_list': 'list[ItemSource]'
     }
 
@@ -66,28 +66,28 @@
         'qr_id': 'qrId',
         'domain': 'domain',
         'derived_from_item': 'derivedFromItem',
         'membership_loaded': 'membershipLoaded',
         'catalog_item': 'catalogItem',
         'status_property_type_name': 'statusPropertyTypeName',
         'location_item': 'locationItem',
-        'description': 'description',
         'domain_id': 'domainId',
         'item_category_list_import': 'itemCategoryListImport',
         'primary_image_for_item': 'primaryImageForItem',
         'item_control': 'itemControl',
         'max_sort_order': 'maxSortOrder',
+        'description': 'description',
         'entity_type_list': 'entityTypeList',
         'item_category_list': 'itemCategoryList',
         'item_type_list': 'itemTypeList',
         'item_project_list': 'itemProjectList',
         'item_source_list': 'itemSourceList'
     }
 
-    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, membership_loaded=None, catalog_item=None, status_property_type_name=None, location_item=None, description=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, membership_loaded=None, catalog_item=None, status_property_type_name=None, location_item=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, description=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, local_vars_configuration=None):  # noqa: E501
         """ItemDomainInventoryBase - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._id = None
         self._name = None
@@ -96,20 +96,20 @@
         self._qr_id = None
         self._domain = None
         self._derived_from_item = None
         self._membership_loaded = None
         self._catalog_item = None
         self._status_property_type_name = None
         self._location_item = None
-        self._description = None
         self._domain_id = None
         self._item_category_list_import = None
         self._primary_image_for_item = None
         self._item_control = None
         self._max_sort_order = None
+        self._description = None
         self._entity_type_list = None
         self._item_category_list = None
         self._item_type_list = None
         self._item_project_list = None
         self._item_source_list = None
         self.discriminator = None
 
@@ -131,26 +131,26 @@
             self.membership_loaded = membership_loaded
         if catalog_item is not None:
             self.catalog_item = catalog_item
         if status_property_type_name is not None:
             self.status_property_type_name = status_property_type_name
         if location_item is not None:
             self.location_item = location_item
-        if description is not None:
-            self.description = description
         if domain_id is not None:
             self.domain_id = domain_id
         if item_category_list_import is not None:
             self.item_category_list_import = item_category_list_import
         if primary_image_for_item is not None:
             self.primary_image_for_item = primary_image_for_item
         if item_control is not None:
             self.item_control = item_control
         if max_sort_order is not None:
             self.max_sort_order = max_sort_order
+        if description is not None:
+            self.description = description
         if entity_type_list is not None:
             self.entity_type_list = entity_type_list
         if item_category_list is not None:
             self.item_category_list = item_category_list
         if item_type_list is not None:
             self.item_type_list = item_type_list
         if item_project_list is not None:
@@ -407,41 +407,14 @@
         :param location_item: The location_item of this ItemDomainInventoryBase.  # noqa: E501
         :type: ItemDomainLocation
         """
 
         self._location_item = location_item
 
     @property
-    def description(self):
-        """Gets the description of this ItemDomainInventoryBase.  # noqa: E501
-
-
-        :return: The description of this ItemDomainInventoryBase.  # noqa: E501
-        :rtype: str
-        """
-        return self._description
-
-    @description.setter
-    def description(self, description):
-        """Sets the description of this ItemDomainInventoryBase.
-
-
-        :param description: The description of this ItemDomainInventoryBase.  # noqa: E501
-        :type: str
-        """
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) > 256):
-            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) < 0):
-            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
-
-        self._description = description
-
-    @property
     def domain_id(self):
         """Gets the domain_id of this ItemDomainInventoryBase.  # noqa: E501
 
 
         :return: The domain_id of this ItemDomainInventoryBase.  # noqa: E501
         :rtype: int
         """
@@ -539,14 +512,41 @@
         :param max_sort_order: The max_sort_order of this ItemDomainInventoryBase.  # noqa: E501
         :type: float
         """
 
         self._max_sort_order = max_sort_order
 
     @property
+    def description(self):
+        """Gets the description of this ItemDomainInventoryBase.  # noqa: E501
+
+
+        :return: The description of this ItemDomainInventoryBase.  # noqa: E501
+        :rtype: str
+        """
+        return self._description
+
+    @description.setter
+    def description(self, description):
+        """Sets the description of this ItemDomainInventoryBase.
+
+
+        :param description: The description of this ItemDomainInventoryBase.  # noqa: E501
+        :type: str
+        """
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) > 256):
+            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) < 0):
+            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
+
+        self._description = description
+
+    @property
     def entity_type_list(self):
         """Gets the entity_type_list of this ItemDomainInventoryBase.  # noqa: E501
 
 
         :return: The entity_type_list of this ItemDomainInventoryBase.  # noqa: E501
         :rtype: list[EntityType]
         """
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_location.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_location.py`

 * *Files 0% similar despite different names*

```diff
@@ -37,20 +37,20 @@
         'id': 'int',
         'name': 'str',
         'item_identifier1': 'str',
         'item_identifier2': 'str',
         'qr_id': 'int',
         'domain': 'Domain',
         'derived_from_item': 'Item',
-        'description': 'str',
         'domain_id': 'int',
         'item_category_list_import': 'list[ItemCategory]',
         'primary_image_for_item': 'str',
         'item_control': 'bool',
         'max_sort_order': 'float',
+        'description': 'str',
         'entity_type_list': 'list[EntityType]',
         'item_category_list': 'list[ItemCategory]',
         'item_type_list': 'list[ItemType]',
         'item_project_list': 'list[ItemProject]',
         'item_source_list': 'list[ItemSource]',
         'parent_item': 'ItemDomainLocation'
     }
@@ -59,47 +59,47 @@
         'id': 'id',
         'name': 'name',
         'item_identifier1': 'itemIdentifier1',
         'item_identifier2': 'itemIdentifier2',
         'qr_id': 'qrId',
         'domain': 'domain',
         'derived_from_item': 'derivedFromItem',
-        'description': 'description',
         'domain_id': 'domainId',
         'item_category_list_import': 'itemCategoryListImport',
         'primary_image_for_item': 'primaryImageForItem',
         'item_control': 'itemControl',
         'max_sort_order': 'maxSortOrder',
+        'description': 'description',
         'entity_type_list': 'entityTypeList',
         'item_category_list': 'itemCategoryList',
         'item_type_list': 'itemTypeList',
         'item_project_list': 'itemProjectList',
         'item_source_list': 'itemSourceList',
         'parent_item': 'parentItem'
     }
 
-    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, description=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, parent_item=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, description=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, parent_item=None, local_vars_configuration=None):  # noqa: E501
         """ItemDomainLocation - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._id = None
         self._name = None
         self._item_identifier1 = None
         self._item_identifier2 = None
         self._qr_id = None
         self._domain = None
         self._derived_from_item = None
-        self._description = None
         self._domain_id = None
         self._item_category_list_import = None
         self._primary_image_for_item = None
         self._item_control = None
         self._max_sort_order = None
+        self._description = None
         self._entity_type_list = None
         self._item_category_list = None
         self._item_type_list = None
         self._item_project_list = None
         self._item_source_list = None
         self._parent_item = None
         self.discriminator = None
@@ -114,26 +114,26 @@
             self.item_identifier2 = item_identifier2
         if qr_id is not None:
             self.qr_id = qr_id
         if domain is not None:
             self.domain = domain
         if derived_from_item is not None:
             self.derived_from_item = derived_from_item
-        if description is not None:
-            self.description = description
         if domain_id is not None:
             self.domain_id = domain_id
         if item_category_list_import is not None:
             self.item_category_list_import = item_category_list_import
         if primary_image_for_item is not None:
             self.primary_image_for_item = primary_image_for_item
         if item_control is not None:
             self.item_control = item_control
         if max_sort_order is not None:
             self.max_sort_order = max_sort_order
+        if description is not None:
+            self.description = description
         if entity_type_list is not None:
             self.entity_type_list = entity_type_list
         if item_category_list is not None:
             self.item_category_list = item_category_list
         if item_type_list is not None:
             self.item_type_list = item_type_list
         if item_project_list is not None:
@@ -308,41 +308,14 @@
         :param derived_from_item: The derived_from_item of this ItemDomainLocation.  # noqa: E501
         :type: Item
         """
 
         self._derived_from_item = derived_from_item
 
     @property
-    def description(self):
-        """Gets the description of this ItemDomainLocation.  # noqa: E501
-
-
-        :return: The description of this ItemDomainLocation.  # noqa: E501
-        :rtype: str
-        """
-        return self._description
-
-    @description.setter
-    def description(self, description):
-        """Sets the description of this ItemDomainLocation.
-
-
-        :param description: The description of this ItemDomainLocation.  # noqa: E501
-        :type: str
-        """
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) > 256):
-            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) < 0):
-            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
-
-        self._description = description
-
-    @property
     def domain_id(self):
         """Gets the domain_id of this ItemDomainLocation.  # noqa: E501
 
 
         :return: The domain_id of this ItemDomainLocation.  # noqa: E501
         :rtype: int
         """
@@ -440,14 +413,41 @@
         :param max_sort_order: The max_sort_order of this ItemDomainLocation.  # noqa: E501
         :type: float
         """
 
         self._max_sort_order = max_sort_order
 
     @property
+    def description(self):
+        """Gets the description of this ItemDomainLocation.  # noqa: E501
+
+
+        :return: The description of this ItemDomainLocation.  # noqa: E501
+        :rtype: str
+        """
+        return self._description
+
+    @description.setter
+    def description(self, description):
+        """Sets the description of this ItemDomainLocation.
+
+
+        :param description: The description of this ItemDomainLocation.  # noqa: E501
+        :type: str
+        """
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) > 256):
+            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) < 0):
+            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
+
+        self._description = description
+
+    @property
     def entity_type_list(self):
         """Gets the entity_type_list of this ItemDomainLocation.  # noqa: E501
 
 
         :return: The entity_type_list of this ItemDomainLocation.  # noqa: E501
         :rtype: list[EntityType]
         """
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_location_all_of.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_location_all_of.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_maarc.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_maarc.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_machine_design.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_machine_design.py`

 * *Files 0% similar despite different names*

```diff
@@ -37,20 +37,20 @@
         'id': 'int',
         'name': 'str',
         'item_identifier1': 'str',
         'item_identifier2': 'str',
         'qr_id': 'int',
         'domain': 'Domain',
         'derived_from_item': 'Item',
-        'description': 'str',
         'domain_id': 'int',
         'item_category_list_import': 'list[ItemCategory]',
         'primary_image_for_item': 'str',
         'item_control': 'bool',
         'max_sort_order': 'float',
+        'description': 'str',
         'entity_type_list': 'list[EntityType]',
         'item_category_list': 'list[ItemCategory]',
         'item_type_list': 'list[ItemType]',
         'item_project_list': 'list[ItemProject]',
         'item_source_list': 'list[ItemSource]',
         'membership_loaded': 'bool',
         'move_to_trash_error_msg': 'str',
@@ -68,20 +68,20 @@
         'id': 'id',
         'name': 'name',
         'item_identifier1': 'itemIdentifier1',
         'item_identifier2': 'itemIdentifier2',
         'qr_id': 'qrId',
         'domain': 'domain',
         'derived_from_item': 'derivedFromItem',
-        'description': 'description',
         'domain_id': 'domainId',
         'item_category_list_import': 'itemCategoryListImport',
         'primary_image_for_item': 'primaryImageForItem',
         'item_control': 'itemControl',
         'max_sort_order': 'maxSortOrder',
+        'description': 'description',
         'entity_type_list': 'entityTypeList',
         'item_category_list': 'itemCategoryList',
         'item_type_list': 'itemTypeList',
         'item_project_list': 'itemProjectList',
         'item_source_list': 'itemSourceList',
         'membership_loaded': 'membershipLoaded',
         'move_to_trash_error_msg': 'moveToTrashErrorMsg',
@@ -91,33 +91,33 @@
         'is_housed': 'isHoused',
         'assigned_represented_element': 'assignedRepresentedElement',
         'status_property_type_name': 'statusPropertyTypeName',
         'move_to_trash_row_style': 'moveToTrashRowStyle',
         'location_item': 'locationItem'
     }
 
-    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, description=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, membership_loaded=None, move_to_trash_error_msg=None, move_to_trash_warning_msg=None, alternate_name=None, assigned_item=None, is_housed=None, assigned_represented_element=None, status_property_type_name=None, move_to_trash_row_style=None, location_item=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, description=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, membership_loaded=None, move_to_trash_error_msg=None, move_to_trash_warning_msg=None, alternate_name=None, assigned_item=None, is_housed=None, assigned_represented_element=None, status_property_type_name=None, move_to_trash_row_style=None, location_item=None, local_vars_configuration=None):  # noqa: E501
         """ItemDomainMachineDesign - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._id = None
         self._name = None
         self._item_identifier1 = None
         self._item_identifier2 = None
         self._qr_id = None
         self._domain = None
         self._derived_from_item = None
-        self._description = None
         self._domain_id = None
         self._item_category_list_import = None
         self._primary_image_for_item = None
         self._item_control = None
         self._max_sort_order = None
+        self._description = None
         self._entity_type_list = None
         self._item_category_list = None
         self._item_type_list = None
         self._item_project_list = None
         self._item_source_list = None
         self._membership_loaded = None
         self._move_to_trash_error_msg = None
@@ -141,26 +141,26 @@
             self.item_identifier2 = item_identifier2
         if qr_id is not None:
             self.qr_id = qr_id
         if domain is not None:
             self.domain = domain
         if derived_from_item is not None:
             self.derived_from_item = derived_from_item
-        if description is not None:
-            self.description = description
         if domain_id is not None:
             self.domain_id = domain_id
         if item_category_list_import is not None:
             self.item_category_list_import = item_category_list_import
         if primary_image_for_item is not None:
             self.primary_image_for_item = primary_image_for_item
         if item_control is not None:
             self.item_control = item_control
         if max_sort_order is not None:
             self.max_sort_order = max_sort_order
+        if description is not None:
+            self.description = description
         if entity_type_list is not None:
             self.entity_type_list = entity_type_list
         if item_category_list is not None:
             self.item_category_list = item_category_list
         if item_type_list is not None:
             self.item_type_list = item_type_list
         if item_project_list is not None:
@@ -353,41 +353,14 @@
         :param derived_from_item: The derived_from_item of this ItemDomainMachineDesign.  # noqa: E501
         :type: Item
         """
 
         self._derived_from_item = derived_from_item
 
     @property
-    def description(self):
-        """Gets the description of this ItemDomainMachineDesign.  # noqa: E501
-
-
-        :return: The description of this ItemDomainMachineDesign.  # noqa: E501
-        :rtype: str
-        """
-        return self._description
-
-    @description.setter
-    def description(self, description):
-        """Sets the description of this ItemDomainMachineDesign.
-
-
-        :param description: The description of this ItemDomainMachineDesign.  # noqa: E501
-        :type: str
-        """
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) > 256):
-            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) < 0):
-            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
-
-        self._description = description
-
-    @property
     def domain_id(self):
         """Gets the domain_id of this ItemDomainMachineDesign.  # noqa: E501
 
 
         :return: The domain_id of this ItemDomainMachineDesign.  # noqa: E501
         :rtype: int
         """
@@ -485,14 +458,41 @@
         :param max_sort_order: The max_sort_order of this ItemDomainMachineDesign.  # noqa: E501
         :type: float
         """
 
         self._max_sort_order = max_sort_order
 
     @property
+    def description(self):
+        """Gets the description of this ItemDomainMachineDesign.  # noqa: E501
+
+
+        :return: The description of this ItemDomainMachineDesign.  # noqa: E501
+        :rtype: str
+        """
+        return self._description
+
+    @description.setter
+    def description(self, description):
+        """Sets the description of this ItemDomainMachineDesign.
+
+
+        :param description: The description of this ItemDomainMachineDesign.  # noqa: E501
+        :type: str
+        """
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) > 256):
+            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) < 0):
+            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
+
+        self._description = description
+
+    @property
     def entity_type_list(self):
         """Gets the entity_type_list of this ItemDomainMachineDesign.  # noqa: E501
 
 
         :return: The entity_type_list of this ItemDomainMachineDesign.  # noqa: E501
         :rtype: list[EntityType]
         """
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_machine_design_all_of.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_machine_design_all_of.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_machine_design_id_list_request.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_machine_design_id_list_request.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_domain_md_search_result.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_domain_md_search_result.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_element.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_element.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_element_history.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_element_history.py`

 * *Files 1% similar despite different names*

```diff
@@ -45,16 +45,16 @@
         'represents_item_element': 'ItemElement',
         'parent_item': 'Item',
         'snapshot_parent_name': 'str',
         'contained_item2': 'Item',
         'snapshot_contained_item2_name': 'str',
         'entered_by_user': 'UserInfo',
         'entered_on_date_time': 'datetime',
-        'contained_item': 'Item',
-        'snapshot_contained_item_name': 'str'
+        'snapshot_contained_item_name': 'str',
+        'contained_item': 'Item'
     }
 
     attribute_map = {
         'id': 'id',
         'item_element': 'itemElement',
         'snapshot_element_name': 'snapshotElementName',
         'is_required': 'isRequired',
@@ -65,19 +65,19 @@
         'represents_item_element': 'representsItemElement',
         'parent_item': 'parentItem',
         'snapshot_parent_name': 'snapshotParentName',
         'contained_item2': 'containedItem2',
         'snapshot_contained_item2_name': 'snapshotContainedItem2Name',
         'entered_by_user': 'enteredByUser',
         'entered_on_date_time': 'enteredOnDateTime',
-        'contained_item': 'containedItem',
-        'snapshot_contained_item_name': 'snapshotContainedItemName'
+        'snapshot_contained_item_name': 'snapshotContainedItemName',
+        'contained_item': 'containedItem'
     }
 
-    def __init__(self, id=None, item_element=None, snapshot_element_name=None, is_required=None, is_housed=None, description=None, sort_order=None, derived_from_item_element=None, represents_item_element=None, parent_item=None, snapshot_parent_name=None, contained_item2=None, snapshot_contained_item2_name=None, entered_by_user=None, entered_on_date_time=None, contained_item=None, snapshot_contained_item_name=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, id=None, item_element=None, snapshot_element_name=None, is_required=None, is_housed=None, description=None, sort_order=None, derived_from_item_element=None, represents_item_element=None, parent_item=None, snapshot_parent_name=None, contained_item2=None, snapshot_contained_item2_name=None, entered_by_user=None, entered_on_date_time=None, snapshot_contained_item_name=None, contained_item=None, local_vars_configuration=None):  # noqa: E501
         """ItemElementHistory - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._id = None
         self._item_element = None
@@ -90,16 +90,16 @@
         self._represents_item_element = None
         self._parent_item = None
         self._snapshot_parent_name = None
         self._contained_item2 = None
         self._snapshot_contained_item2_name = None
         self._entered_by_user = None
         self._entered_on_date_time = None
-        self._contained_item = None
         self._snapshot_contained_item_name = None
+        self._contained_item = None
         self.discriminator = None
 
         if id is not None:
             self.id = id
         if item_element is not None:
             self.item_element = item_element
         if snapshot_element_name is not None:
@@ -124,18 +124,18 @@
             self.contained_item2 = contained_item2
         if snapshot_contained_item2_name is not None:
             self.snapshot_contained_item2_name = snapshot_contained_item2_name
         if entered_by_user is not None:
             self.entered_by_user = entered_by_user
         if entered_on_date_time is not None:
             self.entered_on_date_time = entered_on_date_time
-        if contained_item is not None:
-            self.contained_item = contained_item
         if snapshot_contained_item_name is not None:
             self.snapshot_contained_item_name = snapshot_contained_item_name
+        if contained_item is not None:
+            self.contained_item = contained_item
 
     @property
     def id(self):
         """Gets the id of this ItemElementHistory.  # noqa: E501
 
 
         :return: The id of this ItemElementHistory.  # noqa: E501
@@ -469,35 +469,14 @@
         :param entered_on_date_time: The entered_on_date_time of this ItemElementHistory.  # noqa: E501
         :type: datetime
         """
 
         self._entered_on_date_time = entered_on_date_time
 
     @property
-    def contained_item(self):
-        """Gets the contained_item of this ItemElementHistory.  # noqa: E501
-
-
-        :return: The contained_item of this ItemElementHistory.  # noqa: E501
-        :rtype: Item
-        """
-        return self._contained_item
-
-    @contained_item.setter
-    def contained_item(self, contained_item):
-        """Sets the contained_item of this ItemElementHistory.
-
-
-        :param contained_item: The contained_item of this ItemElementHistory.  # noqa: E501
-        :type: Item
-        """
-
-        self._contained_item = contained_item
-
-    @property
     def snapshot_contained_item_name(self):
         """Gets the snapshot_contained_item_name of this ItemElementHistory.  # noqa: E501
 
 
         :return: The snapshot_contained_item_name of this ItemElementHistory.  # noqa: E501
         :rtype: str
         """
@@ -510,14 +489,35 @@
 
         :param snapshot_contained_item_name: The snapshot_contained_item_name of this ItemElementHistory.  # noqa: E501
         :type: str
         """
 
         self._snapshot_contained_item_name = snapshot_contained_item_name
 
+    @property
+    def contained_item(self):
+        """Gets the contained_item of this ItemElementHistory.  # noqa: E501
+
+
+        :return: The contained_item of this ItemElementHistory.  # noqa: E501
+        :rtype: Item
+        """
+        return self._contained_item
+
+    @contained_item.setter
+    def contained_item(self, contained_item):
+        """Sets the contained_item of this ItemElementHistory.
+
+
+        :param contained_item: The contained_item of this ItemElementHistory.  # noqa: E501
+        :type: Item
+        """
+
+        self._contained_item = contained_item
+
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.openapi_types):
             value = getattr(self, attr)
             if isinstance(value, list):
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_element_relationship.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_element_relationship.py`

 * *Files 0% similar despite different names*

```diff
@@ -51,20 +51,20 @@
         'link_item_element': 'ItemElement',
         'resource_type': 'ResourceType',
         'import_first_item': 'Item',
         'import_second_item': 'Item',
         'import_first_item_connector_name': 'str',
         'import_second_item_connector_name': 'str',
         'import_primary_cable_connection': 'bool',
-        'primary_cable_connection': 'bool',
         'first_item': 'Item',
+        'primary_cable_connection': 'bool',
         'first_item_connector_name': 'str',
-        'second_item': 'Item',
         'second_item_connector_name': 'str',
         'cable_end_primary_indicator': 'str',
+        'second_item': 'Item',
         'cable_end_primary_sort_value': 'str'
     }
 
     attribute_map = {
         'id': 'id',
         'relationship_details': 'relationshipDetails',
         'label': 'label',
@@ -82,24 +82,24 @@
         'link_item_element': 'linkItemElement',
         'resource_type': 'resourceType',
         'import_first_item': 'importFirstItem',
         'import_second_item': 'importSecondItem',
         'import_first_item_connector_name': 'importFirstItemConnectorName',
         'import_second_item_connector_name': 'importSecondItemConnectorName',
         'import_primary_cable_connection': 'importPrimaryCableConnection',
-        'primary_cable_connection': 'primaryCableConnection',
         'first_item': 'firstItem',
+        'primary_cable_connection': 'primaryCableConnection',
         'first_item_connector_name': 'firstItemConnectorName',
-        'second_item': 'secondItem',
         'second_item_connector_name': 'secondItemConnectorName',
         'cable_end_primary_indicator': 'cableEndPrimaryIndicator',
+        'second_item': 'secondItem',
         'cable_end_primary_sort_value': 'cableEndPrimarySortValue'
     }
 
-    def __init__(self, id=None, relationship_details=None, label=None, description=None, property_value_list=None, item_element_relationship_history_list=None, first_item_element=None, first_item_connector=None, first_sort_order=None, second_item_element=None, second_item_connector=None, second_sort_order=None, relationship_for_parent=None, relationship_type=None, link_item_element=None, resource_type=None, import_first_item=None, import_second_item=None, import_first_item_connector_name=None, import_second_item_connector_name=None, import_primary_cable_connection=None, primary_cable_connection=None, first_item=None, first_item_connector_name=None, second_item=None, second_item_connector_name=None, cable_end_primary_indicator=None, cable_end_primary_sort_value=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, id=None, relationship_details=None, label=None, description=None, property_value_list=None, item_element_relationship_history_list=None, first_item_element=None, first_item_connector=None, first_sort_order=None, second_item_element=None, second_item_connector=None, second_sort_order=None, relationship_for_parent=None, relationship_type=None, link_item_element=None, resource_type=None, import_first_item=None, import_second_item=None, import_first_item_connector_name=None, import_second_item_connector_name=None, import_primary_cable_connection=None, first_item=None, primary_cable_connection=None, first_item_connector_name=None, second_item_connector_name=None, cable_end_primary_indicator=None, second_item=None, cable_end_primary_sort_value=None, local_vars_configuration=None):  # noqa: E501
         """ItemElementRelationship - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._id = None
         self._relationship_details = None
@@ -118,20 +118,20 @@
         self._link_item_element = None
         self._resource_type = None
         self._import_first_item = None
         self._import_second_item = None
         self._import_first_item_connector_name = None
         self._import_second_item_connector_name = None
         self._import_primary_cable_connection = None
-        self._primary_cable_connection = None
         self._first_item = None
+        self._primary_cable_connection = None
         self._first_item_connector_name = None
-        self._second_item = None
         self._second_item_connector_name = None
         self._cable_end_primary_indicator = None
+        self._second_item = None
         self._cable_end_primary_sort_value = None
         self.discriminator = None
 
         if id is not None:
             self.id = id
         if relationship_details is not None:
             self.relationship_details = relationship_details
@@ -169,26 +169,26 @@
             self.import_second_item = import_second_item
         if import_first_item_connector_name is not None:
             self.import_first_item_connector_name = import_first_item_connector_name
         if import_second_item_connector_name is not None:
             self.import_second_item_connector_name = import_second_item_connector_name
         if import_primary_cable_connection is not None:
             self.import_primary_cable_connection = import_primary_cable_connection
-        if primary_cable_connection is not None:
-            self.primary_cable_connection = primary_cable_connection
         if first_item is not None:
             self.first_item = first_item
+        if primary_cable_connection is not None:
+            self.primary_cable_connection = primary_cable_connection
         if first_item_connector_name is not None:
             self.first_item_connector_name = first_item_connector_name
-        if second_item is not None:
-            self.second_item = second_item
         if second_item_connector_name is not None:
             self.second_item_connector_name = second_item_connector_name
         if cable_end_primary_indicator is not None:
             self.cable_end_primary_indicator = cable_end_primary_indicator
+        if second_item is not None:
+            self.second_item = second_item
         if cable_end_primary_sort_value is not None:
             self.cable_end_primary_sort_value = cable_end_primary_sort_value
 
     @property
     def id(self):
         """Gets the id of this ItemElementRelationship.  # noqa: E501
 
@@ -644,35 +644,14 @@
         :param import_primary_cable_connection: The import_primary_cable_connection of this ItemElementRelationship.  # noqa: E501
         :type: bool
         """
 
         self._import_primary_cable_connection = import_primary_cable_connection
 
     @property
-    def primary_cable_connection(self):
-        """Gets the primary_cable_connection of this ItemElementRelationship.  # noqa: E501
-
-
-        :return: The primary_cable_connection of this ItemElementRelationship.  # noqa: E501
-        :rtype: bool
-        """
-        return self._primary_cable_connection
-
-    @primary_cable_connection.setter
-    def primary_cable_connection(self, primary_cable_connection):
-        """Sets the primary_cable_connection of this ItemElementRelationship.
-
-
-        :param primary_cable_connection: The primary_cable_connection of this ItemElementRelationship.  # noqa: E501
-        :type: bool
-        """
-
-        self._primary_cable_connection = primary_cable_connection
-
-    @property
     def first_item(self):
         """Gets the first_item of this ItemElementRelationship.  # noqa: E501
 
 
         :return: The first_item of this ItemElementRelationship.  # noqa: E501
         :rtype: Item
         """
@@ -686,14 +665,35 @@
         :param first_item: The first_item of this ItemElementRelationship.  # noqa: E501
         :type: Item
         """
 
         self._first_item = first_item
 
     @property
+    def primary_cable_connection(self):
+        """Gets the primary_cable_connection of this ItemElementRelationship.  # noqa: E501
+
+
+        :return: The primary_cable_connection of this ItemElementRelationship.  # noqa: E501
+        :rtype: bool
+        """
+        return self._primary_cable_connection
+
+    @primary_cable_connection.setter
+    def primary_cable_connection(self, primary_cable_connection):
+        """Sets the primary_cable_connection of this ItemElementRelationship.
+
+
+        :param primary_cable_connection: The primary_cable_connection of this ItemElementRelationship.  # noqa: E501
+        :type: bool
+        """
+
+        self._primary_cable_connection = primary_cable_connection
+
+    @property
     def first_item_connector_name(self):
         """Gets the first_item_connector_name of this ItemElementRelationship.  # noqa: E501
 
 
         :return: The first_item_connector_name of this ItemElementRelationship.  # noqa: E501
         :rtype: str
         """
@@ -707,35 +707,14 @@
         :param first_item_connector_name: The first_item_connector_name of this ItemElementRelationship.  # noqa: E501
         :type: str
         """
 
         self._first_item_connector_name = first_item_connector_name
 
     @property
-    def second_item(self):
-        """Gets the second_item of this ItemElementRelationship.  # noqa: E501
-
-
-        :return: The second_item of this ItemElementRelationship.  # noqa: E501
-        :rtype: Item
-        """
-        return self._second_item
-
-    @second_item.setter
-    def second_item(self, second_item):
-        """Sets the second_item of this ItemElementRelationship.
-
-
-        :param second_item: The second_item of this ItemElementRelationship.  # noqa: E501
-        :type: Item
-        """
-
-        self._second_item = second_item
-
-    @property
     def second_item_connector_name(self):
         """Gets the second_item_connector_name of this ItemElementRelationship.  # noqa: E501
 
 
         :return: The second_item_connector_name of this ItemElementRelationship.  # noqa: E501
         :rtype: str
         """
@@ -770,14 +749,35 @@
         :param cable_end_primary_indicator: The cable_end_primary_indicator of this ItemElementRelationship.  # noqa: E501
         :type: str
         """
 
         self._cable_end_primary_indicator = cable_end_primary_indicator
 
     @property
+    def second_item(self):
+        """Gets the second_item of this ItemElementRelationship.  # noqa: E501
+
+
+        :return: The second_item of this ItemElementRelationship.  # noqa: E501
+        :rtype: Item
+        """
+        return self._second_item
+
+    @second_item.setter
+    def second_item(self, second_item):
+        """Sets the second_item of this ItemElementRelationship.
+
+
+        :param second_item: The second_item of this ItemElementRelationship.  # noqa: E501
+        :type: Item
+        """
+
+        self._second_item = second_item
+
+    @property
     def cable_end_primary_sort_value(self):
         """Gets the cable_end_primary_sort_value of this ItemElementRelationship.  # noqa: E501
 
 
         :return: The cable_end_primary_sort_value of this ItemElementRelationship.  # noqa: E501
         :rtype: str
         """
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_element_relationship_history.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_element_relationship_history.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_hierarchy.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_hierarchy.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_location_information.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_location_information.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_membership.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_membership.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_permissions.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_permissions.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_project.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_project.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_resource.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_resource.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_source.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_source.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_status_basic_object.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_status_basic_object.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/item_type.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/item_type.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/list_tbl.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/list_tbl.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/locatable_item.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/locatable_item.py`

 * *Files 0% similar despite different names*

```diff
@@ -39,20 +39,20 @@
         'item_identifier1': 'str',
         'item_identifier2': 'str',
         'qr_id': 'int',
         'domain': 'Domain',
         'derived_from_item': 'Item',
         'membership_loaded': 'bool',
         'location_item': 'ItemDomainLocation',
-        'description': 'str',
         'domain_id': 'int',
         'item_category_list_import': 'list[ItemCategory]',
         'primary_image_for_item': 'str',
         'item_control': 'bool',
         'max_sort_order': 'float',
+        'description': 'str',
         'entity_type_list': 'list[EntityType]',
         'item_category_list': 'list[ItemCategory]',
         'item_type_list': 'list[ItemType]',
         'item_project_list': 'list[ItemProject]',
         'item_source_list': 'list[ItemSource]'
     }
 
@@ -62,48 +62,48 @@
         'item_identifier1': 'itemIdentifier1',
         'item_identifier2': 'itemIdentifier2',
         'qr_id': 'qrId',
         'domain': 'domain',
         'derived_from_item': 'derivedFromItem',
         'membership_loaded': 'membershipLoaded',
         'location_item': 'locationItem',
-        'description': 'description',
         'domain_id': 'domainId',
         'item_category_list_import': 'itemCategoryListImport',
         'primary_image_for_item': 'primaryImageForItem',
         'item_control': 'itemControl',
         'max_sort_order': 'maxSortOrder',
+        'description': 'description',
         'entity_type_list': 'entityTypeList',
         'item_category_list': 'itemCategoryList',
         'item_type_list': 'itemTypeList',
         'item_project_list': 'itemProjectList',
         'item_source_list': 'itemSourceList'
     }
 
-    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, membership_loaded=None, location_item=None, description=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, id=None, name=None, item_identifier1=None, item_identifier2=None, qr_id=None, domain=None, derived_from_item=None, membership_loaded=None, location_item=None, domain_id=None, item_category_list_import=None, primary_image_for_item=None, item_control=None, max_sort_order=None, description=None, entity_type_list=None, item_category_list=None, item_type_list=None, item_project_list=None, item_source_list=None, local_vars_configuration=None):  # noqa: E501
         """LocatableItem - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._id = None
         self._name = None
         self._item_identifier1 = None
         self._item_identifier2 = None
         self._qr_id = None
         self._domain = None
         self._derived_from_item = None
         self._membership_loaded = None
         self._location_item = None
-        self._description = None
         self._domain_id = None
         self._item_category_list_import = None
         self._primary_image_for_item = None
         self._item_control = None
         self._max_sort_order = None
+        self._description = None
         self._entity_type_list = None
         self._item_category_list = None
         self._item_type_list = None
         self._item_project_list = None
         self._item_source_list = None
         self.discriminator = None
 
@@ -121,26 +121,26 @@
             self.domain = domain
         if derived_from_item is not None:
             self.derived_from_item = derived_from_item
         if membership_loaded is not None:
             self.membership_loaded = membership_loaded
         if location_item is not None:
             self.location_item = location_item
-        if description is not None:
-            self.description = description
         if domain_id is not None:
             self.domain_id = domain_id
         if item_category_list_import is not None:
             self.item_category_list_import = item_category_list_import
         if primary_image_for_item is not None:
             self.primary_image_for_item = primary_image_for_item
         if item_control is not None:
             self.item_control = item_control
         if max_sort_order is not None:
             self.max_sort_order = max_sort_order
+        if description is not None:
+            self.description = description
         if entity_type_list is not None:
             self.entity_type_list = entity_type_list
         if item_category_list is not None:
             self.item_category_list = item_category_list
         if item_type_list is not None:
             self.item_type_list = item_type_list
         if item_project_list is not None:
@@ -355,41 +355,14 @@
         :param location_item: The location_item of this LocatableItem.  # noqa: E501
         :type: ItemDomainLocation
         """
 
         self._location_item = location_item
 
     @property
-    def description(self):
-        """Gets the description of this LocatableItem.  # noqa: E501
-
-
-        :return: The description of this LocatableItem.  # noqa: E501
-        :rtype: str
-        """
-        return self._description
-
-    @description.setter
-    def description(self, description):
-        """Sets the description of this LocatableItem.
-
-
-        :param description: The description of this LocatableItem.  # noqa: E501
-        :type: str
-        """
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) > 256):
-            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
-        if (self.local_vars_configuration.client_side_validation and
-                description is not None and len(description) < 0):
-            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
-
-        self._description = description
-
-    @property
     def domain_id(self):
         """Gets the domain_id of this LocatableItem.  # noqa: E501
 
 
         :return: The domain_id of this LocatableItem.  # noqa: E501
         :rtype: int
         """
@@ -487,14 +460,41 @@
         :param max_sort_order: The max_sort_order of this LocatableItem.  # noqa: E501
         :type: float
         """
 
         self._max_sort_order = max_sort_order
 
     @property
+    def description(self):
+        """Gets the description of this LocatableItem.  # noqa: E501
+
+
+        :return: The description of this LocatableItem.  # noqa: E501
+        :rtype: str
+        """
+        return self._description
+
+    @description.setter
+    def description(self, description):
+        """Sets the description of this LocatableItem.
+
+
+        :param description: The description of this LocatableItem.  # noqa: E501
+        :type: str
+        """
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) > 256):
+            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
+        if (self.local_vars_configuration.client_side_validation and
+                description is not None and len(description) < 0):
+            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
+
+        self._description = description
+
+    @property
     def entity_type_list(self):
         """Gets the entity_type_list of this LocatableItem.  # noqa: E501
 
 
         :return: The entity_type_list of this LocatableItem.  # noqa: E501
         :rtype: list[EntityType]
         """
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/location_history_object.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/location_history_object.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/log.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/log.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/log_entry_edit_information.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/log_entry_edit_information.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/machine_design_connector_list_object.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/machine_design_connector_list_object.py`

 * *Files 2% similar despite different names*

```diff
@@ -34,53 +34,53 @@
                             and the value is json key in definition.
     """
     openapi_types = {
         'item_connector': 'ItemConnector',
         'connected_cables': 'list[ItemDomainCableDesign]',
         'connected_items': 'list[Item]',
         'connected_to_items_string': 'str',
-        'connector_name': 'str',
-        'connected_cables_string': 'str'
+        'connected_cables_string': 'str',
+        'connector_name': 'str'
     }
 
     attribute_map = {
         'item_connector': 'itemConnector',
         'connected_cables': 'connectedCables',
         'connected_items': 'connectedItems',
         'connected_to_items_string': 'connectedToItemsString',
-        'connector_name': 'connectorName',
-        'connected_cables_string': 'connectedCablesString'
+        'connected_cables_string': 'connectedCablesString',
+        'connector_name': 'connectorName'
     }
 
-    def __init__(self, item_connector=None, connected_cables=None, connected_items=None, connected_to_items_string=None, connector_name=None, connected_cables_string=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, item_connector=None, connected_cables=None, connected_items=None, connected_to_items_string=None, connected_cables_string=None, connector_name=None, local_vars_configuration=None):  # noqa: E501
         """MachineDesignConnectorListObject - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._item_connector = None
         self._connected_cables = None
         self._connected_items = None
         self._connected_to_items_string = None
-        self._connector_name = None
         self._connected_cables_string = None
+        self._connector_name = None
         self.discriminator = None
 
         if item_connector is not None:
             self.item_connector = item_connector
         if connected_cables is not None:
             self.connected_cables = connected_cables
         if connected_items is not None:
             self.connected_items = connected_items
         if connected_to_items_string is not None:
             self.connected_to_items_string = connected_to_items_string
-        if connector_name is not None:
-            self.connector_name = connector_name
         if connected_cables_string is not None:
             self.connected_cables_string = connected_cables_string
+        if connector_name is not None:
+            self.connector_name = connector_name
 
     @property
     def item_connector(self):
         """Gets the item_connector of this MachineDesignConnectorListObject.  # noqa: E501
 
 
         :return: The item_connector of this MachineDesignConnectorListObject.  # noqa: E501
@@ -159,54 +159,54 @@
         :param connected_to_items_string: The connected_to_items_string of this MachineDesignConnectorListObject.  # noqa: E501
         :type: str
         """
 
         self._connected_to_items_string = connected_to_items_string
 
     @property
-    def connector_name(self):
-        """Gets the connector_name of this MachineDesignConnectorListObject.  # noqa: E501
+    def connected_cables_string(self):
+        """Gets the connected_cables_string of this MachineDesignConnectorListObject.  # noqa: E501
 
 
-        :return: The connector_name of this MachineDesignConnectorListObject.  # noqa: E501
+        :return: The connected_cables_string of this MachineDesignConnectorListObject.  # noqa: E501
         :rtype: str
         """
-        return self._connector_name
+        return self._connected_cables_string
 
-    @connector_name.setter
-    def connector_name(self, connector_name):
-        """Sets the connector_name of this MachineDesignConnectorListObject.
+    @connected_cables_string.setter
+    def connected_cables_string(self, connected_cables_string):
+        """Sets the connected_cables_string of this MachineDesignConnectorListObject.
 
 
-        :param connector_name: The connector_name of this MachineDesignConnectorListObject.  # noqa: E501
+        :param connected_cables_string: The connected_cables_string of this MachineDesignConnectorListObject.  # noqa: E501
         :type: str
         """
 
-        self._connector_name = connector_name
+        self._connected_cables_string = connected_cables_string
 
     @property
-    def connected_cables_string(self):
-        """Gets the connected_cables_string of this MachineDesignConnectorListObject.  # noqa: E501
+    def connector_name(self):
+        """Gets the connector_name of this MachineDesignConnectorListObject.  # noqa: E501
 
 
-        :return: The connected_cables_string of this MachineDesignConnectorListObject.  # noqa: E501
+        :return: The connector_name of this MachineDesignConnectorListObject.  # noqa: E501
         :rtype: str
         """
-        return self._connected_cables_string
+        return self._connector_name
 
-    @connected_cables_string.setter
-    def connected_cables_string(self, connected_cables_string):
-        """Sets the connected_cables_string of this MachineDesignConnectorListObject.
+    @connector_name.setter
+    def connector_name(self, connector_name):
+        """Sets the connector_name of this MachineDesignConnectorListObject.
 
 
-        :param connected_cables_string: The connected_cables_string of this MachineDesignConnectorListObject.  # noqa: E501
+        :param connector_name: The connector_name of this MachineDesignConnectorListObject.  # noqa: E501
         :type: str
         """
 
-        self._connected_cables_string = connected_cables_string
+        self._connector_name = connector_name
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.openapi_types):
             value = getattr(self, attr)
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/machine_design_item_info.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/machine_design_item_info.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/new_app_information.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/new_app_information.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/new_catalog_element_information.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/new_catalog_element_information.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/new_catalog_information.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/new_catalog_information.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/new_control_relationship_information.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/new_control_relationship_information.py`

 * *Files 14% similar despite different names*

```diff
@@ -32,43 +32,43 @@
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     openapi_types = {
         'controlled_machine_id': 'int',
         'controlling_machine_id': 'int',
-        'linked_parent_machine_id': 'int',
+        'linked_parent_machine_relationship_id': 'int',
         'control_interface_to_parent': 'str'
     }
 
     attribute_map = {
         'controlled_machine_id': 'controlledMachineId',
         'controlling_machine_id': 'controllingMachineId',
-        'linked_parent_machine_id': 'linkedParentMachineId',
+        'linked_parent_machine_relationship_id': 'linkedParentMachineRelationshipId',
         'control_interface_to_parent': 'controlInterfaceToParent'
     }
 
-    def __init__(self, controlled_machine_id=None, controlling_machine_id=None, linked_parent_machine_id=None, control_interface_to_parent=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, controlled_machine_id=None, controlling_machine_id=None, linked_parent_machine_relationship_id=None, control_interface_to_parent=None, local_vars_configuration=None):  # noqa: E501
         """NewControlRelationshipInformation - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._controlled_machine_id = None
         self._controlling_machine_id = None
-        self._linked_parent_machine_id = None
+        self._linked_parent_machine_relationship_id = None
         self._control_interface_to_parent = None
         self.discriminator = None
 
         if controlled_machine_id is not None:
             self.controlled_machine_id = controlled_machine_id
         if controlling_machine_id is not None:
             self.controlling_machine_id = controlling_machine_id
-        if linked_parent_machine_id is not None:
-            self.linked_parent_machine_id = linked_parent_machine_id
+        if linked_parent_machine_relationship_id is not None:
+            self.linked_parent_machine_relationship_id = linked_parent_machine_relationship_id
         if control_interface_to_parent is not None:
             self.control_interface_to_parent = control_interface_to_parent
 
     @property
     def controlled_machine_id(self):
         """Gets the controlled_machine_id of this NewControlRelationshipInformation.  # noqa: E501
 
@@ -107,33 +107,33 @@
         :param controlling_machine_id: The controlling_machine_id of this NewControlRelationshipInformation.  # noqa: E501
         :type: int
         """
 
         self._controlling_machine_id = controlling_machine_id
 
     @property
-    def linked_parent_machine_id(self):
-        """Gets the linked_parent_machine_id of this NewControlRelationshipInformation.  # noqa: E501
+    def linked_parent_machine_relationship_id(self):
+        """Gets the linked_parent_machine_relationship_id of this NewControlRelationshipInformation.  # noqa: E501
 
 
-        :return: The linked_parent_machine_id of this NewControlRelationshipInformation.  # noqa: E501
+        :return: The linked_parent_machine_relationship_id of this NewControlRelationshipInformation.  # noqa: E501
         :rtype: int
         """
-        return self._linked_parent_machine_id
+        return self._linked_parent_machine_relationship_id
 
-    @linked_parent_machine_id.setter
-    def linked_parent_machine_id(self, linked_parent_machine_id):
-        """Sets the linked_parent_machine_id of this NewControlRelationshipInformation.
+    @linked_parent_machine_relationship_id.setter
+    def linked_parent_machine_relationship_id(self, linked_parent_machine_relationship_id):
+        """Sets the linked_parent_machine_relationship_id of this NewControlRelationshipInformation.
 
 
-        :param linked_parent_machine_id: The linked_parent_machine_id of this NewControlRelationshipInformation.  # noqa: E501
+        :param linked_parent_machine_relationship_id: The linked_parent_machine_relationship_id of this NewControlRelationshipInformation.  # noqa: E501
         :type: int
         """
 
-        self._linked_parent_machine_id = linked_parent_machine_id
+        self._linked_parent_machine_relationship_id = linked_parent_machine_relationship_id
 
     @property
     def control_interface_to_parent(self):
         """Gets the control_interface_to_parent of this NewControlRelationshipInformation.  # noqa: E501
 
 
         :return: The control_interface_to_parent of this NewControlRelationshipInformation.  # noqa: E501
```

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/new_inventory_information.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/new_inventory_information.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/new_location_information.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/new_location_information.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/new_machine_placeholder_options.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/new_machine_placeholder_options.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/promote_machine_element_information.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/promote_machine_element_information.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/property_metadata.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/property_metadata.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/property_type.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/property_type.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/property_value.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/property_value.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/property_value_history.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/property_value_history.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/relationship_type.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/relationship_type.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/relationship_type_handler.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/relationship_type_handler.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/representing_assembly_element_for_machine_information.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/representing_assembly_element_for_machine_information.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/resource_type.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/resource_type.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/resource_type_category.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/resource_type_category.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/role_type.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/role_type.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/search_entities_options.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/search_entities_options.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/search_entities_results.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/search_entities_results.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/search_result.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/search_result.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/simple_location_information.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/simple_location_information.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/source.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/source.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/source_id_list_request.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/source_id_list_request.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/update_cable_design_assigned_item_information.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/update_cable_design_assigned_item_information.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/update_machine_assigned_item_information.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/update_machine_assigned_item_information.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/user_group.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/user_group.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/user_info.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/user_info.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/models/user_role.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/models/user_role.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/cdbApi/rest.py` & `ComponentDB-API-3.15.5.dev1/cdbApi/rest.py`

 * *Files identical despite different names*

### Comparing `ComponentDB-API-3.15.5.dev0/setup.py` & `ComponentDB-API-3.15.5.dev1/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 twine upload dist/(specific version file)
 """
 
 from setuptools import setup
 from setuptools import find_packages
 
 setup(name='ComponentDB-API',
-      version='3.15.5.dev0',
+      version='3.15.5.dev1',
       packages=["cdbApi",
                 "cdbApi.api",
                 "cdbApi.models"],
       py_modules=["CdbApiFactory"],
       install_requires=['python-dateutil', 
           'urllib3',
           'certifi',
```

