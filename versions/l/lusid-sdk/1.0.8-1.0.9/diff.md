# Comparing `tmp/lusid-sdk-1.0.8.tar.gz` & `tmp/lusid-sdk-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/lusid-sdk-1.0.8.tar", last modified: Thu Mar 16 22:15:18 2023, max compression
+gzip compressed data, was "dist/lusid-sdk-1.0.9.tar", last modified: Thu Mar 16 22:59:30 2023, max compression
```

## Comparing `lusid-sdk-1.0.8.tar` & `lusid-sdk-1.0.9.tar`

### file list

```diff
@@ -1,616 +1,616 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:15:18.848405 lusid-sdk-1.0.8/
--rw-r--r--   0 root         (0) root         (0)       40 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      309 2023-03-16 22:15:18.848405 lusid-sdk-1.0.8/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    93442 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:15:18.790405 lusid-sdk-1.0.8/lusid/
--rw-r--r--   0 root         (0) root         (0)    42157 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/__init__.py
--rw-r--r--   0 root         (0) root         (0)       22 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/__version__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:15:18.795405 lusid-sdk-1.0.8/lusid/api/
--rw-r--r--   0 root         (0) root         (0)     2147 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/__init__.py
--rw-r--r--   0 root         (0) root         (0)    31243 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/aggregation_api.py
--rw-r--r--   0 root         (0) root         (0)    39961 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/allocations_api.py
--rw-r--r--   0 root         (0) root         (0)    21666 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/application_metadata_api.py
--rw-r--r--   0 root         (0) root         (0)    38741 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/blocks_api.py
--rw-r--r--   0 root         (0) root         (0)   128574 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/calendars_api.py
--rw-r--r--   0 root         (0) root         (0)    37075 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/complex_market_data_api.py
--rw-r--r--   0 root         (0) root         (0)    37217 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/configuration_recipe_api.py
--rw-r--r--   0 root         (0) root         (0)    92907 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/corporate_action_sources_api.py
--rw-r--r--   0 root         (0) root         (0)    71069 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/counterparties_api.py
--rw-r--r--   0 root         (0) root         (0)   177505 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/custom_entities_api.py
--rw-r--r--   0 root         (0) root         (0)    36859 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/custom_entity_definitions_api.py
--rw-r--r--   0 root         (0) root         (0)    42656 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/cut_label_definitions_api.py
--rw-r--r--   0 root         (0) root         (0)    74817 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/data_types_api.py
--rw-r--r--   0 root         (0) root         (0)    21097 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/derived_transaction_portfolios_api.py
--rw-r--r--   0 root         (0) root         (0)    11461 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/entities_api.py
--rw-r--r--   0 root         (0) root         (0)    39311 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/executions_api.py
--rw-r--r--   0 root         (0) root         (0)   173179 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/instruments_api.py
--rw-r--r--   0 root         (0) root         (0)   237747 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/legal_entities_api.py
--rw-r--r--   0 root         (0) root         (0)    39234 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/orders_api.py
--rw-r--r--   0 root         (0) root         (0)    39885 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/participations_api.py
--rw-r--r--   0 root         (0) root         (0)   223041 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/persons_api.py
--rw-r--r--   0 root         (0) root         (0)   339172 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/portfolio_groups_api.py
--rw-r--r--   0 root         (0) root         (0)   297030 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/portfolios_api.py
--rw-r--r--   0 root         (0) root         (0)    58891 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/property_definitions_api.py
--rw-r--r--   0 root         (0) root         (0)    58370 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/quotes_api.py
--rw-r--r--   0 root         (0) root         (0)    70602 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/reconciliations_api.py
--rw-r--r--   0 root         (0) root         (0)    46619 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/reference_portfolio_api.py
--rw-r--r--   0 root         (0) root         (0)    51157 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/relationship_definitions_api.py
--rw-r--r--   0 root         (0) root         (0)    22583 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/relationships_api.py
--rw-r--r--   0 root         (0) root         (0)    27642 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/schemas_api.py
--rw-r--r--   0 root         (0) root         (0)     8323 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/scopes_api.py
--rw-r--r--   0 root         (0) root         (0)    48095 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/search_api.py
--rw-r--r--   0 root         (0) root         (0)    39247 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/sequences_api.py
--rw-r--r--   0 root         (0) root         (0)    14424 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/system_configuration_api.py
--rw-r--r--   0 root         (0) root         (0)   323744 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api/transaction_portfolios_api.py
--rw-r--r--   0 root         (0) root         (0)    27344 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/api_client.py
--rw-r--r--   0 root         (0) root         (0)    16571 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/configuration.py
--rw-r--r--   0 root         (0) root         (0)     5079 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/exceptions.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:15:18.846405 lusid-sdk-1.0.8/lusid/models/
--rw-r--r--   0 root         (0) root         (0)    39307 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/__init__.py
--rw-r--r--   0 root         (0) root         (0)     6340 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/a2_b_breakdown.py
--rw-r--r--   0 root         (0) root         (0)     5185 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/a2_b_category.py
--rw-r--r--   0 root         (0) root         (0)    17994 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/a2_b_data_record.py
--rw-r--r--   0 root         (0) root         (0)    21249 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/a2_b_movement_record.py
--rw-r--r--   0 root         (0) root         (0)     7104 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/access_controlled_action.py
--rw-r--r--   0 root         (0) root         (0)     8867 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/access_controlled_resource.py
--rw-r--r--   0 root         (0) root         (0)     8023 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/access_metadata_operation.py
--rw-r--r--   0 root         (0) root         (0)     5784 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/access_metadata_value.py
--rw-r--r--   0 root         (0) root         (0)     7198 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/action_id.py
--rw-r--r--   0 root         (0) root         (0)     4725 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/action_result_of_portfolio.py
--rw-r--r--   0 root         (0) root         (0)     7222 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/add_business_days_to_date_request.py
--rw-r--r--   0 root         (0) root         (0)     4157 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/add_business_days_to_date_response.py
--rw-r--r--   0 root         (0) root         (0)    10980 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/address_definition.py
--rw-r--r--   0 root         (0) root         (0)     6118 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/address_key_filter.py
--rw-r--r--   0 root         (0) root         (0)     9172 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/address_key_option_definition.py
--rw-r--r--   0 root         (0) root         (0)     6832 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/adjust_holding.py
--rw-r--r--   0 root         (0) root         (0)    12008 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/adjust_holding_for_date_request.py
--rw-r--r--   0 root         (0) root         (0)    10262 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/adjust_holding_request.py
--rw-r--r--   0 root         (0) root         (0)     7500 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/aggregate_spec.py
--rw-r--r--   0 root         (0) root         (0)    13024 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/aggregated_return.py
--rw-r--r--   0 root         (0) root         (0)    13772 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/aggregated_returns_request.py
--rw-r--r--   0 root         (0) root         (0)     6028 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/aggregated_returns_response.py
--rw-r--r--   0 root         (0) root         (0)    10298 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/aggregation.py
--rw-r--r--   0 root         (0) root         (0)     4009 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/aggregation_context.py
--rw-r--r--   0 root         (0) root         (0)     7085 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/aggregation_measure_failure_detail.py
--rw-r--r--   0 root         (0) root         (0)     8775 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/aggregation_options.py
--rw-r--r--   0 root         (0) root         (0)    25169 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/aggregation_query.py
--rw-r--r--   0 root         (0) root         (0)    24848 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/allocation.py
--rw-r--r--   0 root         (0) root         (0)    21188 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/allocation_request.py
--rw-r--r--   0 root         (0) root         (0)     4436 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/allocation_set_request.py
--rw-r--r--   0 root         (0) root         (0)    12994 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/amortisation_event.py
--rw-r--r--   0 root         (0) root         (0)    13134 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/amortisation_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7168 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/annul_quotes_response.py
--rw-r--r--   0 root         (0) root         (0)     6065 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/annul_single_structured_data_response.py
--rw-r--r--   0 root         (0) root         (0)     7181 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/annul_structured_data_response.py
--rw-r--r--   0 root         (0) root         (0)     7902 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/barrier.py
--rw-r--r--   0 root         (0) root         (0)    10814 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/basket.py
--rw-r--r--   0 root         (0) root         (0)    10914 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/basket_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7620 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/basket_identifier.py
--rw-r--r--   0 root         (0) root         (0)     7230 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/batch_adjust_holdings_response.py
--rw-r--r--   0 root         (0) root         (0)     7647 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/batch_upsert_portfolio_transactions_response.py
--rw-r--r--   0 root         (0) root         (0)    18549 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/block.py
--rw-r--r--   0 root         (0) root         (0)    15838 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/block_request.py
--rw-r--r--   0 root         (0) root         (0)     4109 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/block_set_request.py
--rw-r--r--   0 root         (0) root         (0)    22931 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/bond.py
--rw-r--r--   0 root         (0) root         (0)    23191 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/bond_all_of.py
--rw-r--r--   0 root         (0) root         (0)    14817 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/bond_default_event.py
--rw-r--r--   0 root         (0) root         (0)    14977 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/bond_default_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)     9031 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/calendar.py
--rw-r--r--   0 root         (0) root         (0)    13374 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/calendar_date.py
--rw-r--r--   0 root         (0) root         (0)    13183 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cap_floor.py
--rw-r--r--   0 root         (0) root         (0)    13323 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cap_floor_all_of.py
--rw-r--r--   0 root         (0) root         (0)     9845 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cash_dividend_event.py
--rw-r--r--   0 root         (0) root         (0)     9945 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cash_dividend_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10169 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cash_flow_event.py
--rw-r--r--   0 root         (0) root         (0)    10269 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cash_flow_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10510 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cash_flow_lineage.py
--rw-r--r--   0 root         (0) root         (0)    11249 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cash_flow_value.py
--rw-r--r--   0 root         (0) root         (0)    11389 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cash_flow_value_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6768 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cash_flow_value_set.py
--rw-r--r--   0 root         (0) root         (0)     6828 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cash_flow_value_set_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6856 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cash_ladder_record.py
--rw-r--r--   0 root         (0) root         (0)    10170 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cash_perpetual.py
--rw-r--r--   0 root         (0) root         (0)    10270 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cash_perpetual_all_of.py
--rw-r--r--   0 root         (0) root         (0)    24112 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cds_flow_conventions.py
--rw-r--r--   0 root         (0) root         (0)    17378 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cds_index.py
--rw-r--r--   0 root         (0) root         (0)    17578 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cds_index_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10137 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cds_protection_detail_specification.py
--rw-r--r--   0 root         (0) root         (0)    11015 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/change.py
--rw-r--r--   0 root         (0) root         (0)    10714 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/change_history.py
--rw-r--r--   0 root         (0) root         (0)     8704 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/change_item.py
--rw-r--r--   0 root         (0) root         (0)     7846 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/close_event.py
--rw-r--r--   0 root         (0) root         (0)     7926 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/close_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    15717 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/complete_portfolio.py
--rw-r--r--   0 root         (0) root         (0)    14719 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/complete_relationship.py
--rw-r--r--   0 root         (0) root         (0)    11257 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/complex_bond.py
--rw-r--r--   0 root         (0) root         (0)    11357 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/complex_bond_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7096 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/complex_market_data.py
--rw-r--r--   0 root         (0) root         (0)    11521 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/complex_market_data_id.py
--rw-r--r--   0 root         (0) root         (0)    11637 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/compounding.py
--rw-r--r--   0 root         (0) root         (0)    14328 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/configuration_recipe.py
--rw-r--r--   0 root         (0) root         (0)    15247 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/configuration_recipe_snippet.py
--rw-r--r--   0 root         (0) root         (0)     6181 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/constituents_adjustment_header.py
--rw-r--r--   0 root         (0) root         (0)    19498 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/contract_for_difference.py
--rw-r--r--   0 root         (0) root         (0)    19718 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/contract_for_difference_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10863 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/corporate_action.py
--rw-r--r--   0 root         (0) root         (0)     9857 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/corporate_action_source.py
--rw-r--r--   0 root         (0) root         (0)     5718 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/corporate_action_transition.py
--rw-r--r--   0 root         (0) root         (0)    10625 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/corporate_action_transition_component.py
--rw-r--r--   0 root         (0) root         (0)     7357 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/corporate_action_transition_component_request.py
--rw-r--r--   0 root         (0) root         (0)     5646 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/corporate_action_transition_request.py
--rw-r--r--   0 root         (0) root         (0)    11822 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/counterparty_agreement.py
--rw-r--r--   0 root         (0) root         (0)     8524 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/counterparty_risk_information.py
--rw-r--r--   0 root         (0) root         (0)     6161 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/counterparty_signatory.py
--rw-r--r--   0 root         (0) root         (0)    10189 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_calendar_request.py
--rw-r--r--   0 root         (0) root         (0)    12686 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_corporate_action_source_request.py
--rw-r--r--   0 root         (0) root         (0)     9424 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_cut_label_definition_request.py
--rw-r--r--   0 root         (0) root         (0)    20417 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_data_type_request.py
--rw-r--r--   0 root         (0) root         (0)    13518 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_date_request.py
--rw-r--r--   0 root         (0) root         (0)    15511 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_derived_property_definition_request.py
--rw-r--r--   0 root         (0) root         (0)    20890 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_derived_transaction_portfolio_request.py
--rw-r--r--   0 root         (0) root         (0)     4462 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_portfolio_details.py
--rw-r--r--   0 root         (0) root         (0)    12383 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_portfolio_group_request.py
--rw-r--r--   0 root         (0) root         (0)    17579 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_property_definition_request.py
--rw-r--r--   0 root         (0) root         (0)    11661 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_reference_portfolio_request.py
--rw-r--r--   0 root         (0) root         (0)    22106 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_relationship_definition_request.py
--rw-r--r--   0 root         (0) root         (0)    10113 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_relationship_request.py
--rw-r--r--   0 root         (0) root         (0)    11654 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_sequence_request.py
--rw-r--r--   0 root         (0) root         (0)    20612 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_transaction_portfolio_request.py
--rw-r--r--   0 root         (0) root         (0)     9310 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/create_unit_definition.py
--rw-r--r--   0 root         (0) root         (0)    18199 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/credit_default_swap.py
--rw-r--r--   0 root         (0) root         (0)    18399 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/credit_default_swap_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7521 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/credit_rating.py
--rw-r--r--   0 root         (0) root         (0)    16567 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/credit_spread_curve_data.py
--rw-r--r--   0 root         (0) root         (0)    16767 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/credit_spread_curve_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)    20912 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/credit_support_annex.py
--rw-r--r--   0 root         (0) root         (0)     4642 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/currency_and_amount.py
--rw-r--r--   0 root         (0) root         (0)    15766 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/custodian_account.py
--rw-r--r--   0 root         (0) root         (0)    11807 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/custom_entity_definition.py
--rw-r--r--   0 root         (0) root         (0)    10534 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/custom_entity_definition_request.py
--rw-r--r--   0 root         (0) root         (0)     8081 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/custom_entity_field.py
--rw-r--r--   0 root         (0) root         (0)    11325 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/custom_entity_field_definition.py
--rw-r--r--   0 root         (0) root         (0)    12486 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/custom_entity_id.py
--rw-r--r--   0 root         (0) root         (0)     8385 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/custom_entity_request.py
--rw-r--r--   0 root         (0) root         (0)    13657 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/custom_entity_response.py
--rw-r--r--   0 root         (0) root         (0)     8560 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cut_label_definition.py
--rw-r--r--   0 root         (0) root         (0)     4563 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/cut_local_time.py
--rw-r--r--   0 root         (0) root         (0)    15955 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/data_type.py
--rw-r--r--   0 root         (0) root         (0)    15138 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/data_type_summary.py
--rw-r--r--   0 root         (0) root         (0)    14147 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/date_attributes.py
--rw-r--r--   0 root         (0) root         (0)     4864 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/date_range.py
--rw-r--r--   0 root         (0) root         (0)     3458 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/day_of_week.py
--rw-r--r--   0 root         (0) root         (0)     5179 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/delete_instrument_properties_response.py
--rw-r--r--   0 root         (0) root         (0)     6116 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/delete_instrument_response.py
--rw-r--r--   0 root         (0) root         (0)     6132 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/delete_instruments_response.py
--rw-r--r--   0 root         (0) root         (0)    10335 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/delete_relationship_request.py
--rw-r--r--   0 root         (0) root         (0)     7419 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/deleted_entity_response.py
--rw-r--r--   0 root         (0) root         (0)     8387 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/dependency_source_filter.py
--rw-r--r--   0 root         (0) root         (0)    11233 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/discount_factor_curve_data.py
--rw-r--r--   0 root         (0) root         (0)    11353 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/discount_factor_curve_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)     5619 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/economic_dependency.py
--rw-r--r--   0 root         (0) root         (0)     6020 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/economic_dependency_with_complex_market_data.py
--rw-r--r--   0 root         (0) root         (0)     6830 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/economic_dependency_with_quote.py
--rw-r--r--   0 root         (0) root         (0)     5398 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/empty_model_options.py
--rw-r--r--   0 root         (0) root         (0)     5438 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/empty_model_options_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6713 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/entity_identifier.py
--rw-r--r--   0 root         (0) root         (0)     8495 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/equity.py
--rw-r--r--   0 root         (0) root         (0)     8575 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/equity_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11924 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/equity_all_of_identifiers.py
--rw-r--r--   0 root         (0) root         (0)    11440 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/equity_curve_by_prices_data.py
--rw-r--r--   0 root         (0) root         (0)    11560 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/equity_curve_by_prices_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7849 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/equity_model_options.py
--rw-r--r--   0 root         (0) root         (0)     7909 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/equity_model_options_all_of.py
--rw-r--r--   0 root         (0) root         (0)    24187 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/equity_option.py
--rw-r--r--   0 root         (0) root         (0)    24487 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/equity_option_all_of.py
--rw-r--r--   0 root         (0) root         (0)    23696 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/equity_swap.py
--rw-r--r--   0 root         (0) root         (0)    23956 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/equity_swap_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11231 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/equity_vol_surface_data.py
--rw-r--r--   0 root         (0) root         (0)    11351 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/equity_vol_surface_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6806 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/error_detail.py
--rw-r--r--   0 root         (0) root         (0)     4531 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/event_date_range.py
--rw-r--r--   0 root         (0) root         (0)    11841 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/exchange_traded_option.py
--rw-r--r--   0 root         (0) root         (0)    11961 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/exchange_traded_option_all_of.py
--rw-r--r--   0 root         (0) root         (0)    23036 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/exchange_traded_option_contract_details.py
--rw-r--r--   0 root         (0) root         (0)    24122 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/execution.py
--rw-r--r--   0 root         (0) root         (0)    21469 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/execution_request.py
--rw-r--r--   0 root         (0) root         (0)     4169 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/execution_set_request.py
--rw-r--r--   0 root         (0) root         (0)    11000 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/exercise_event.py
--rw-r--r--   0 root         (0) root         (0)    11120 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/exercise_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10285 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/exotic_instrument.py
--rw-r--r--   0 root         (0) root         (0)    10365 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/exotic_instrument_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11174 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/expanded_group.py
--rw-r--r--   0 root         (0) root         (0)     6695 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/field_definition.py
--rw-r--r--   0 root         (0) root         (0)     8258 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/field_schema.py
--rw-r--r--   0 root         (0) root         (0)     5658 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/field_value.py
--rw-r--r--   0 root         (0) root         (0)     5781 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/file_response.py
--rw-r--r--   0 root         (0) root         (0)    13116 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fixed_leg.py
--rw-r--r--   0 root         (0) root         (0)    13256 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fixed_leg_all_of.py
--rw-r--r--   0 root         (0) root         (0)     4915 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fixed_leg_all_of_overrides.py
--rw-r--r--   0 root         (0) root         (0)    13373 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/floating_leg.py
--rw-r--r--   0 root         (0) root         (0)    13513 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/floating_leg_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6592 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/flow_convention_name.py
--rw-r--r--   0 root         (0) root         (0)    23990 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/flow_conventions.py
--rw-r--r--   0 root         (0) root         (0)    15807 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/forward_rate_agreement.py
--rw-r--r--   0 root         (0) root         (0)    15987 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/forward_rate_agreement_all_of.py
--rw-r--r--   0 root         (0) root         (0)    14013 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/funding_leg.py
--rw-r--r--   0 root         (0) root         (0)    14133 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/funding_leg_all_of.py
--rw-r--r--   0 root         (0) root         (0)    20197 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/future.py
--rw-r--r--   0 root         (0) root         (0)    20397 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/future_all_of.py
--rw-r--r--   0 root         (0) root         (0)    21009 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/futures_contract_details.py
--rw-r--r--   0 root         (0) root         (0)    20192 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_forward.py
--rw-r--r--   0 root         (0) root         (0)    20432 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_forward_all_of.py
--rw-r--r--   0 root         (0) root         (0)    12659 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_forward_curve_by_quote_reference.py
--rw-r--r--   0 root         (0) root         (0)    12799 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_forward_curve_by_quote_reference_all_of.py
--rw-r--r--   0 root         (0) root         (0)    13026 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_forward_curve_data.py
--rw-r--r--   0 root         (0) root         (0)    13186 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_forward_curve_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11327 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_forward_model_options.py
--rw-r--r--   0 root         (0) root         (0)    11427 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_forward_model_options_all_of.py
--rw-r--r--   0 root         (0) root         (0)    13322 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_forward_pips_curve_data.py
--rw-r--r--   0 root         (0) root         (0)    13482 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_forward_pips_curve_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)    13194 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_forward_tenor_curve_data.py
--rw-r--r--   0 root         (0) root         (0)    13354 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_forward_tenor_curve_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)    13490 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_forward_tenor_pips_curve_data.py
--rw-r--r--   0 root         (0) root         (0)    13650 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_forward_tenor_pips_curve_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)    28087 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_option.py
--rw-r--r--   0 root         (0) root         (0)    28447 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_option_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11021 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_swap.py
--rw-r--r--   0 root         (0) root         (0)    11121 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_swap_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11135 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/fx_vol_surface_data.py
--rw-r--r--   0 root         (0) root         (0)     7279 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/get_complex_market_data_response.py
--rw-r--r--   0 root         (0) root         (0)     7088 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/get_counterparty_agreement_response.py
--rw-r--r--   0 root         (0) root         (0)     7040 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/get_credit_support_annex_response.py
--rw-r--r--   0 root         (0) root         (0)     7371 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/get_instruments_response.py
--rw-r--r--   0 root         (0) root         (0)     8047 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/get_quotes_response.py
--rw-r--r--   0 root         (0) root         (0)     5689 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/get_recipe_response.py
--rw-r--r--   0 root         (0) root         (0)    12030 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/get_reference_portfolio_constituents_response.py
--rw-r--r--   0 root         (0) root         (0)    12535 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/holding_adjustment.py
--rw-r--r--   0 root         (0) root         (0)    13889 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/holding_adjustment_with_date.py
--rw-r--r--   0 root         (0) root         (0)     4577 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/holding_context.py
--rw-r--r--   0 root         (0) root         (0)    10491 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/holdings_adjustment.py
--rw-r--r--   0 root         (0) root         (0)     9374 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/holdings_adjustment_header.py
--rw-r--r--   0 root         (0) root         (0)     3970 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/i_data_record.py
--rw-r--r--   0 root         (0) root         (0)     6778 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/i_unit_definition_dto.py
--rw-r--r--   0 root         (0) root         (0)     7949 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/id_selector_definition.py
--rw-r--r--   0 root         (0) root         (0)     9438 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/identifier_part_schema.py
--rw-r--r--   0 root         (0) root         (0)    18219 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/index_convention.py
--rw-r--r--   0 root         (0) root         (0)     7150 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/index_model_options.py
--rw-r--r--   0 root         (0) root         (0)     7210 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/index_model_options_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7581 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/industry_classifier.py
--rw-r--r--   0 root         (0) root         (0)    36320 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/inflation_linked_bond.py
--rw-r--r--   0 root         (0) root         (0)    36720 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/inflation_linked_bond_all_of.py
--rw-r--r--   0 root         (0) root         (0)    25334 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/inflation_swap.py
--rw-r--r--   0 root         (0) root         (0)    25634 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/inflation_swap_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10090 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/informational_error_event.py
--rw-r--r--   0 root         (0) root         (0)    10190 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/informational_error_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    13185 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/informational_event.py
--rw-r--r--   0 root         (0) root         (0)    13325 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/informational_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    22490 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/inline_valuation_request.py
--rw-r--r--   0 root         (0) root         (0)     8210 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/inline_valuations_reconciliation_request.py
--rw-r--r--   0 root         (0) root         (0)     5481 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/input_transition.py
--rw-r--r--   0 root         (0) root         (0)    19961 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/instrument.py
--rw-r--r--   0 root         (0) root         (0)     9470 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/instrument_definition.py
--rw-r--r--   0 root         (0) root         (0)     8348 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/instrument_definition_format.py
--rw-r--r--   0 root         (0) root         (0)     6924 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/instrument_event.py
--rw-r--r--   0 root         (0) root         (0)    17157 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/instrument_event_holder.py
--rw-r--r--   0 root         (0) root         (0)     7700 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/instrument_id_type_descriptor.py
--rw-r--r--   0 root         (0) root         (0)     5728 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/instrument_id_value.py
--rw-r--r--   0 root         (0) root         (0)     7134 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/instrument_leg.py
--rw-r--r--   0 root         (0) root         (0)     6699 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/instrument_leg_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6118 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/instrument_match.py
--rw-r--r--   0 root         (0) root         (0)     6889 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/instrument_properties.py
--rw-r--r--   0 root         (0) root         (0)     6083 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/instrument_search_property.py
--rw-r--r--   0 root         (0) root         (0)    14277 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/interest_rate_swap.py
--rw-r--r--   0 root         (0) root         (0)    14417 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/interest_rate_swap_all_of.py
--rw-r--r--   0 root         (0) root         (0)    13510 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/interest_rate_swaption.py
--rw-r--r--   0 root         (0) root         (0)    13650 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/interest_rate_swaption_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11120 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/ir_vol_cube_data.py
--rw-r--r--   0 root         (0) root         (0)    11240 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/ir_vol_cube_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)     5575 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/is_business_day_response.py
--rw-r--r--   0 root         (0) root         (0)     4311 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/label_value_set.py
--rw-r--r--   0 root         (0) root         (0)    17095 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/leg_definition.py
--rw-r--r--   0 root         (0) root         (0)    13346 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/legal_entity.py
--rw-r--r--   0 root         (0) root         (0)     5400 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/level_step.py
--rw-r--r--   0 root         (0) root         (0)     8320 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/life_cycle_event_lineage.py
--rw-r--r--   0 root         (0) root         (0)     8841 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/life_cycle_event_value.py
--rw-r--r--   0 root         (0) root         (0)     8941 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/life_cycle_event_value_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6392 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/link.py
--rw-r--r--   0 root         (0) root         (0)     6623 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/list_aggregation_reconciliation.py
--rw-r--r--   0 root         (0) root         (0)    10736 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/list_aggregation_response.py
--rw-r--r--   0 root         (0) root         (0)     8140 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/lusid_instrument.py
--rw-r--r--   0 root         (0) root         (0)     9506 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/lusid_problem_details.py
--rw-r--r--   0 root         (0) root         (0)     5947 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/lusid_unique_id.py
--rw-r--r--   0 root         (0) root         (0)    10706 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/lusid_validation_problem_details.py
--rw-r--r--   0 root         (0) root         (0)     6589 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/mapped_string.py
--rw-r--r--   0 root         (0) root         (0)    10565 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/mapping.py
--rw-r--r--   0 root         (0) root         (0)    10470 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/mapping_rule.py
--rw-r--r--   0 root         (0) root         (0)     9380 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/market_context.py
--rw-r--r--   0 root         (0) root         (0)     6867 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/market_context_suppliers.py
--rw-r--r--   0 root         (0) root         (0)    26172 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/market_data_key_rule.py
--rw-r--r--   0 root         (0) root         (0)     5841 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/market_data_overrides.py
--rw-r--r--   0 root         (0) root         (0)    23809 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/market_data_specific_rule.py
--rw-r--r--   0 root         (0) root         (0)    14880 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/market_options.py
--rw-r--r--   0 root         (0) root         (0)     5970 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/market_quote.py
--rw-r--r--   0 root         (0) root         (0)     4609 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/metric_value.py
--rw-r--r--   0 root         (0) root         (0)     5992 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/model_options.py
--rw-r--r--   0 root         (0) root         (0)     7700 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/model_property.py
--rw-r--r--   0 root         (0) root         (0)     7505 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/model_selection.py
--rw-r--r--   0 root         (0) root         (0)     5119 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/next_value_in_sequence_response.py
--rw-r--r--   0 root         (0) root         (0)    11964 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/opaque_market_data.py
--rw-r--r--   0 root         (0) root         (0)    12084 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/opaque_market_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6307 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/opaque_model_options.py
--rw-r--r--   0 root         (0) root         (0)     6367 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/opaque_model_options_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6895 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/open_event.py
--rw-r--r--   0 root         (0) root         (0)     6955 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/open_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)     5598 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/operation.py
--rw-r--r--   0 root         (0) root         (0)    22500 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/order.py
--rw-r--r--   0 root         (0) root         (0)     5698 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/order_by_spec.py
--rw-r--r--   0 root         (0) root         (0)    18756 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/order_request.py
--rw-r--r--   0 root         (0) root         (0)     4246 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/order_set_request.py
--rw-r--r--   0 root         (0) root         (0)     4383 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/otc_confirmation.py
--rw-r--r--   0 root         (0) root         (0)    33018 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/output_transaction.py
--rw-r--r--   0 root         (0) root         (0)    10332 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/output_transition.py
--rw-r--r--   0 root         (0) root         (0)     7385 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_allocation.py
--rw-r--r--   0 root         (0) root         (0)     7245 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_block.py
--rw-r--r--   0 root         (0) root         (0)     7329 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_calendar.py
--rw-r--r--   0 root         (0) root         (0)     7693 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_corporate_action_source.py
--rw-r--r--   0 root         (0) root         (0)     7721 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_custom_entity_definition.py
--rw-r--r--   0 root         (0) root         (0)     7665 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_custom_entity_response.py
--rw-r--r--   0 root         (0) root         (0)     7609 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_cut_label_definition.py
--rw-r--r--   0 root         (0) root         (0)     7525 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_data_type_summary.py
--rw-r--r--   0 root         (0) root         (0)     7357 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_execution.py
--rw-r--r--   0 root         (0) root         (0)     7385 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_instrument.py
--rw-r--r--   0 root         (0) root         (0)     7693 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_instrument_event_holder.py
--rw-r--r--   0 root         (0) root         (0)     7413 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_legal_entity.py
--rw-r--r--   0 root         (0) root         (0)     7245 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_order.py
--rw-r--r--   0 root         (0) root         (0)     7469 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_participation.py
--rw-r--r--   0 root         (0) root         (0)     7273 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_person.py
--rw-r--r--   0 root         (0) root         (0)     7833 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_portfolio_group_search_result.py
--rw-r--r--   0 root         (0) root         (0)     7693 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_portfolio_search_result.py
--rw-r--r--   0 root         (0) root         (0)     7945 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_property_definition_search_result.py
--rw-r--r--   0 root         (0) root         (0)     7721 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_relationship_definition.py
--rw-r--r--   0 root         (0) root         (0)     7609 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_sequence_definition.py
--rw-r--r--   0 root         (0) root         (0)     7482 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/participation.py
--rw-r--r--   0 root         (0) root         (0)     6926 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/participation_request.py
--rw-r--r--   0 root         (0) root         (0)     4229 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/participation_set_request.py
--rw-r--r--   0 root         (0) root         (0)     8788 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/performance_return.py
--rw-r--r--   0 root         (0) root         (0)    10181 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/performance_returns_metric.py
--rw-r--r--   0 root         (0) root         (0)     5213 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/perpetual_property.py
--rw-r--r--   0 root         (0) root         (0)    11043 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/person.py
--rw-r--r--   0 root         (0) root         (0)    21169 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/portfolio.py
--rw-r--r--   0 root         (0) root         (0)    23700 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/portfolio_cash_flow.py
--rw-r--r--   0 root         (0) root         (0)     8810 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/portfolio_cash_ladder.py
--rw-r--r--   0 root         (0) root         (0)    15147 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/portfolio_details.py
--rw-r--r--   0 root         (0) root         (0)     8460 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/portfolio_entity_id.py
--rw-r--r--   0 root         (0) root         (0)    13607 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/portfolio_group.py
--rw-r--r--   0 root         (0) root         (0)     6996 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/portfolio_group_properties.py
--rw-r--r--   0 root         (0) root         (0)    12953 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/portfolio_group_search_result.py
--rw-r--r--   0 root         (0) root         (0)    17791 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/portfolio_holding.py
--rw-r--r--   0 root         (0) root         (0)     6863 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/portfolio_properties.py
--rw-r--r--   0 root         (0) root         (0)     6775 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/portfolio_reconciliation_request.py
--rw-r--r--   0 root         (0) root         (0)    17336 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/portfolio_result_data_key_rule.py
--rw-r--r--   0 root         (0) root         (0)    17516 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/portfolio_result_data_key_rule_all_of.py
--rw-r--r--   0 root         (0) root         (0)    15510 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/portfolio_search_result.py
--rw-r--r--   0 root         (0) root         (0)     7197 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/portfolios_reconciliation_request.py
--rw-r--r--   0 root         (0) root         (0)     6022 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/premium.py
--rw-r--r--   0 root         (0) root         (0)     9445 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/pricing_context.py
--rw-r--r--   0 root         (0) root         (0)    27514 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/pricing_options.py
--rw-r--r--   0 root         (0) root         (0)     7870 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/processed_command.py
--rw-r--r--   0 root         (0) root         (0)    27010 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/property_definition.py
--rw-r--r--   0 root         (0) root         (0)    27874 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/property_definition_search_result.py
--rw-r--r--   0 root         (0) root         (0)     7835 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/property_filter.py
--rw-r--r--   0 root         (0) root         (0)     7969 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/property_interval.py
--rw-r--r--   0 root         (0) root         (0)     5265 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/property_schema.py
--rw-r--r--   0 root         (0) root         (0)     6066 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/property_value.py
--rw-r--r--   0 root         (0) root         (0)    10795 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/quote.py
--rw-r--r--   0 root         (0) root         (0)     5783 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/quote_id.py
--rw-r--r--   0 root         (0) root         (0)    14721 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/quote_series_id.py
--rw-r--r--   0 root         (0) root         (0)    11311 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/raw_vendor_event.py
--rw-r--r--   0 root         (0) root         (0)    11431 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/raw_vendor_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    17980 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/realised_gain_loss.py
--rw-r--r--   0 root         (0) root         (0)     9883 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reconcile_date_time_rule.py
--rw-r--r--   0 root         (0) root         (0)     9983 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reconcile_date_time_rule_all_of.py
--rw-r--r--   0 root         (0) root         (0)     9945 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reconcile_numeric_rule.py
--rw-r--r--   0 root         (0) root         (0)    10045 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reconcile_numeric_rule_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10716 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reconcile_string_rule.py
--rw-r--r--   0 root         (0) root         (0)    10816 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reconcile_string_rule_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7788 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reconciled_transaction.py
--rw-r--r--   0 root         (0) root         (0)    15668 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reconciliation_break.py
--rw-r--r--   0 root         (0) root         (0)     5468 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reconciliation_left_right_address_key_pair.py
--rw-r--r--   0 root         (0) root         (0)     7307 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reconciliation_line.py
--rw-r--r--   0 root         (0) root         (0)    10383 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reconciliation_request.py
--rw-r--r--   0 root         (0) root         (0)     5245 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reconciliation_response.py
--rw-r--r--   0 root         (0) root         (0)     5472 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reconciliation_rule.py
--rw-r--r--   0 root         (0) root         (0)     5343 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reference_data.py
--rw-r--r--   0 root         (0) root         (0)    11099 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reference_instrument.py
--rw-r--r--   0 root         (0) root         (0)    11199 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reference_instrument_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11192 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reference_portfolio_constituent.py
--rw-r--r--   0 root         (0) root         (0)     7556 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reference_portfolio_constituent_request.py
--rw-r--r--   0 root         (0) root         (0)    12677 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/related_entity.py
--rw-r--r--   0 root         (0) root         (0)    10235 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/relation.py
--rw-r--r--   0 root         (0) root         (0)    13986 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/relationship.py
--rw-r--r--   0 root         (0) root         (0)    19714 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/relationship_definition.py
--rw-r--r--   0 root         (0) root         (0)    25564 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/repo.py
--rw-r--r--   0 root         (0) root         (0)    25824 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/repo_all_of.py
--rw-r--r--   0 root         (0) root         (0)    12033 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reset_event.py
--rw-r--r--   0 root         (0) root         (0)    12173 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/reset_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6065 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_id.py
--rw-r--r--   0 root         (0) root         (0)     7657 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_access_controlled_resource.py
--rw-r--r--   0 root         (0) root         (0)     7571 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_access_metadata_value_of.py
--rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_aggregation_query.py
--rw-r--r--   0 root         (0) root         (0)     7265 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_allocation.py
--rw-r--r--   0 root         (0) root         (0)     7125 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_block.py
--rw-r--r--   0 root         (0) root         (0)     7321 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_calendar_date.py
--rw-r--r--   0 root         (0) root         (0)     7153 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_change.py
--rw-r--r--   0 root         (0) root         (0)     7349 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_change_history.py
--rw-r--r--   0 root         (0) root         (0)     7769 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_constituents_adjustment_header.py
--rw-r--r--   0 root         (0) root         (0)     7405 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_corporate_action.py
--rw-r--r--   0 root         (0) root         (0)     7209 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_data_type.py
--rw-r--r--   0 root         (0) root         (0)     7237 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_execution.py
--rw-r--r--   0 root         (0) root         (0)     7881 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_get_counterparty_agreement_response.py
--rw-r--r--   0 root         (0) root         (0)     7797 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_get_credit_support_annex_response.py
--rw-r--r--   0 root         (0) root         (0)     7461 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_get_recipe_response.py
--rw-r--r--   0 root         (0) root         (0)     7657 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_holdings_adjustment_header.py
--rw-r--r--   0 root         (0) root         (0)     7489 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_i_unit_definition_dto.py
--rw-r--r--   0 root         (0) root         (0)     7713 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_instrument_id_type_descriptor.py
--rw-r--r--   0 root         (0) root         (0)     7293 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_legal_entity.py
--rw-r--r--   0 root         (0) root         (0)     7181 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_mapping.py
--rw-r--r--   0 root         (0) root         (0)     7125 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_order.py
--rw-r--r--   0 root         (0) root         (0)     7349 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_participation.py
--rw-r--r--   0 root         (0) root         (0)     7461 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_performance_return.py
--rw-r--r--   0 root         (0) root         (0)     7153 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_person.py
--rw-r--r--   0 root         (0) root         (0)     7237 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_portfolio.py
--rw-r--r--   0 root         (0) root         (0)     7461 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_portfolio_cash_flow.py
--rw-r--r--   0 root         (0) root         (0)     7517 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_portfolio_cash_ladder.py
--rw-r--r--   0 root         (0) root         (0)     7377 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_portfolio_group.py
--rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_processed_command.py
--rw-r--r--   0 root         (0) root         (0)     7229 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_property.py
--rw-r--r--   0 root         (0) root         (0)     7489 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_property_definition.py
--rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_property_interval.py
--rw-r--r--   0 root         (0) root         (0)     7125 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_quote.py
--rw-r--r--   0 root         (0) root         (0)     7517 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_reconciliation_break.py
--rw-r--r--   0 root         (0) root         (0)     7209 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_relation.py
--rw-r--r--   0 root         (0) root         (0)     7321 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_relationship.py
--rw-r--r--   0 root         (0) root         (0)     7405 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_scope_definition.py
--rw-r--r--   0 root         (0) root         (0)     7123 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_string.py
--rw-r--r--   0 root         (0) root         (0)     7237 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/resource_list_of_value_type.py
--rw-r--r--   0 root         (0) root         (0)     7131 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/response_meta_data.py
--rw-r--r--   0 root         (0) root         (0)    16884 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_data_key_rule.py
--rw-r--r--   0 root         (0) root         (0)    17064 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_data_key_rule_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6620 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_data_schema.py
--rw-r--r--   0 root         (0) root         (0)     5593 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_key_rule.py
--rw-r--r--   0 root         (0) root         (0)     6667 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value.py
--rw-r--r--   0 root         (0) root         (0)     8572 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value0_d.py
--rw-r--r--   0 root         (0) root         (0)     8672 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value0_d_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6563 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value_bool.py
--rw-r--r--   0 root         (0) root         (0)     6623 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value_bool_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6573 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value_currency.py
--rw-r--r--   0 root         (0) root         (0)     6633 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value_currency_all_of.py
--rw-r--r--   0 root         (0) root         (0)     8004 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value_date_time_offset.py
--rw-r--r--   0 root         (0) root         (0)     8084 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value_date_time_offset_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7880 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value_decimal.py
--rw-r--r--   0 root         (0) root         (0)     7960 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value_decimal_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6781 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value_dictionary.py
--rw-r--r--   0 root         (0) root         (0)     6841 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value_dictionary_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7808 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value_int.py
--rw-r--r--   0 root         (0) root         (0)     7888 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value_int_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6549 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value_string.py
--rw-r--r--   0 root         (0) root         (0)     6609 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/result_value_string_all_of.py
--rw-r--r--   0 root         (0) root         (0)     5298 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/schedule.py
--rw-r--r--   0 root         (0) root         (0)     5782 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/schema.py
--rw-r--r--   0 root         (0) root         (0)     4421 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/scope_definition.py
--rw-r--r--   0 root         (0) root         (0)    12312 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/sequence_definition.py
--rw-r--r--   0 root         (0) root         (0)     4545 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/set_legal_entity_identifiers_request.py
--rw-r--r--   0 root         (0) root         (0)     4697 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/set_legal_entity_properties_request.py
--rw-r--r--   0 root         (0) root         (0)     4487 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/set_person_identifiers_request.py
--rw-r--r--   0 root         (0) root         (0)     4849 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/set_person_properties_request.py
--rw-r--r--   0 root         (0) root         (0)    11343 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/side_configuration_data.py
--rw-r--r--   0 root         (0) root         (0)    14459 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/simple_instrument.py
--rw-r--r--   0 root         (0) root         (0)    14599 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/simple_instrument_all_of.py
--rw-r--r--   0 root         (0) root         (0)     9596 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/step_schedule.py
--rw-r--r--   0 root         (0) root         (0)     9696 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/step_schedule_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10119 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/stock_split_event.py
--rw-r--r--   0 root         (0) root         (0)    10219 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/stock_split_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)     9229 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/stream.py
--rw-r--r--   0 root         (0) root         (0)     9013 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/supported_analytics_internal_request.py
--rw-r--r--   0 root         (0) root         (0)     9501 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/target_tax_lot.py
--rw-r--r--   0 root         (0) root         (0)     9697 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/target_tax_lot_request.py
--rw-r--r--   0 root         (0) root         (0)    18130 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/term_deposit.py
--rw-r--r--   0 root         (0) root         (0)    18290 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/term_deposit_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7853 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/touch.py
--rw-r--r--   0 root         (0) root         (0)    30338 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transaction.py
--rw-r--r--   0 root         (0) root         (0)     7083 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transaction_configuration_data.py
--rw-r--r--   0 root         (0) root         (0)     7208 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transaction_configuration_data_request.py
--rw-r--r--   0 root         (0) root         (0)    15020 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transaction_configuration_movement_data.py
--rw-r--r--   0 root         (0) root         (0)    13934 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transaction_configuration_movement_data_request.py
--rw-r--r--   0 root         (0) root         (0)    14164 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transaction_configuration_type_alias.py
--rw-r--r--   0 root         (0) root         (0)     5083 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transaction_price.py
--rw-r--r--   0 root         (0) root         (0)     6459 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transaction_property_mapping.py
--rw-r--r--   0 root         (0) root         (0)     6568 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transaction_property_mapping_request.py
--rw-r--r--   0 root         (0) root         (0)     9881 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transaction_query_parameters.py
--rw-r--r--   0 root         (0) root         (0)    11041 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transaction_reconciliation_request.py
--rw-r--r--   0 root         (0) root         (0)    25203 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transaction_request.py
--rw-r--r--   0 root         (0) root         (0)     6795 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transaction_set_configuration_data.py
--rw-r--r--   0 root         (0) root         (0)     5076 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transactions_reconciliations_response.py
--rw-r--r--   0 root         (0) root         (0)    12319 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transition_event.py
--rw-r--r--   0 root         (0) root         (0)    12479 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/transition_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    12563 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/trigger_event.py
--rw-r--r--   0 root         (0) root         (0)    12703 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/trigger_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)     9765 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/typed_resource_id.py
--rw-r--r--   0 root         (0) root         (0)     7389 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/update_calendar_request.py
--rw-r--r--   0 root         (0) root         (0)     8384 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/update_custom_entity_definition_request.py
--rw-r--r--   0 root         (0) root         (0)     8527 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/update_cut_label_definition_request.py
--rw-r--r--   0 root         (0) root         (0)     9293 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/update_data_type_request.py
--rw-r--r--   0 root         (0) root         (0)     7187 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/update_instrument_identifier_request.py
--rw-r--r--   0 root         (0) root         (0)     5732 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/update_portfolio_group_request.py
--rw-r--r--   0 root         (0) root         (0)     5684 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/update_portfolio_request.py
--rw-r--r--   0 root         (0) root         (0)     6201 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/update_property_definition_request.py
--rw-r--r--   0 root         (0) root         (0)    10184 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/update_relationship_definition_request.py
--rw-r--r--   0 root         (0) root         (0)     7868 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/update_unit_request.py
--rw-r--r--   0 root         (0) root         (0)     5591 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_complex_market_data_request.py
--rw-r--r--   0 root         (0) root         (0)    13956 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_corporate_action_request.py
--rw-r--r--   0 root         (0) root         (0)     7350 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_corporate_actions_response.py
--rw-r--r--   0 root         (0) root         (0)     4691 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_counterparty_agreement_request.py
--rw-r--r--   0 root         (0) root         (0)     4423 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_credit_support_annex_request.py
--rw-r--r--   0 root         (0) root         (0)     7423 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_custom_entities_response.py
--rw-r--r--   0 root         (0) root         (0)     4488 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_custom_entity_access_metadata_request.py
--rw-r--r--   0 root         (0) root         (0)    11530 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_instrument_event_request.py
--rw-r--r--   0 root         (0) root         (0)     7374 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_instrument_events_response.py
--rw-r--r--   0 root         (0) root         (0)     5336 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_instrument_properties_response.py
--rw-r--r--   0 root         (0) root         (0)     7966 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_instrument_property_request.py
--rw-r--r--   0 root         (0) root         (0)     8362 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_instruments_response.py
--rw-r--r--   0 root         (0) root         (0)     4480 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_legal_entity_access_metadata_request.py
--rw-r--r--   0 root         (0) root         (0)    11115 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_legal_entity_request.py
--rw-r--r--   0 root         (0) root         (0)     4422 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_person_access_metadata_request.py
--rw-r--r--   0 root         (0) root         (0)     9117 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_person_request.py
--rw-r--r--   0 root         (0) root         (0)     4652 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_portfolio_access_metadata_request.py
--rw-r--r--   0 root         (0) root         (0)     4710 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_portfolio_group_access_metadata_request.py
--rw-r--r--   0 root         (0) root         (0)     7446 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_portfolio_transactions_response.py
--rw-r--r--   0 root         (0) root         (0)     7602 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_quote_request.py
--rw-r--r--   0 root         (0) root         (0)     7044 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_quotes_response.py
--rw-r--r--   0 root         (0) root         (0)     5700 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_recipe_request.py
--rw-r--r--   0 root         (0) root         (0)    10645 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_reference_portfolio_constituents_request.py
--rw-r--r--   0 root         (0) root         (0)     5744 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_reference_portfolio_constituents_response.py
--rw-r--r--   0 root         (0) root         (0)     8081 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_returns_response.py
--rw-r--r--   0 root         (0) root         (0)     6072 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_single_structured_data_response.py
--rw-r--r--   0 root         (0) root         (0)     7225 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_structured_data_response.py
--rw-r--r--   0 root         (0) root         (0)     6948 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/upsert_transaction_properties_response.py
--rw-r--r--   0 root         (0) root         (0)     3793 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/user.py
--rw-r--r--   0 root         (0) root         (0)    21405 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/valuation_request.py
--rw-r--r--   0 root         (0) root         (0)    13908 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/valuation_schedule.py
--rw-r--r--   0 root         (0) root         (0)     8627 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/valuations_reconciliation_request.py
--rw-r--r--   0 root         (0) root         (0)     4004 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/value_type.py
--rw-r--r--   0 root         (0) root         (0)    15639 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/vendor_model_rule.py
--rw-r--r--   0 root         (0) root         (0)    11534 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/version.py
--rw-r--r--   0 root         (0) root         (0)     6388 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/version_summary_dto.py
--rw-r--r--   0 root         (0) root         (0)     8591 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/versioned_resource_list_of_a2_b_data_record.py
--rw-r--r--   0 root         (0) root         (0)     8719 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/versioned_resource_list_of_a2_b_movement_record.py
--rw-r--r--   0 root         (0) root         (0)     8719 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/versioned_resource_list_of_output_transaction.py
--rw-r--r--   0 root         (0) root         (0)     8687 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/versioned_resource_list_of_portfolio_holding.py
--rw-r--r--   0 root         (0) root         (0)     8527 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/versioned_resource_list_of_transaction.py
--rw-r--r--   0 root         (0) root         (0)     5793 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/weekend_mask.py
--rw-r--r--   0 root         (0) root         (0)     8441 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/weighted_instrument.py
--rw-r--r--   0 root         (0) root         (0)     4479 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/weighted_instruments.py
--rw-r--r--   0 root         (0) root         (0)    11018 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/yield_curve_data.py
--rw-r--r--   0 root         (0) root         (0)    11138 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/models/yield_curve_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)    13517 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/rest.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:15:18.846405 lusid-sdk-1.0.8/lusid/tcp/
--rw-r--r--   0 root         (0) root         (0)       93 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/tcp/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5321 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/tcp/tcp_keep_alive_probes.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:15:18.847405 lusid-sdk-1.0.8/lusid/utilities/
--rw-r--r--   0 root         (0) root         (0)      432 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/utilities/__init__.py
--rw-r--r--   0 root         (0) root         (0)     6434 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/utilities/api_client_builder.py
--rw-r--r--   0 root         (0) root         (0)     5397 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/utilities/api_client_factory.py
--rw-r--r--   0 root         (0) root         (0)     3970 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/utilities/api_configuration.py
--rw-r--r--   0 root         (0) root         (0)     4065 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/utilities/api_configuration_loader.py
--rw-r--r--   0 root         (0) root         (0)     1030 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/utilities/config_keys.json
--rw-r--r--   0 root         (0) root         (0)     1236 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/utilities/lusid_retry.py
--rw-r--r--   0 root         (0) root         (0)     1725 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/utilities/proxy_config.py
--rw-r--r--   0 root         (0) root         (0)     9701 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/lusid/utilities/refreshing_token.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:15:18.847405 lusid-sdk-1.0.8/lusid_sdk.egg-info/
--rw-r--r--   0 root         (0) root         (0)      309 2023-03-16 22:15:18.000000 lusid-sdk-1.0.8/lusid_sdk.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    23954 2023-03-16 22:15:18.000000 lusid-sdk-1.0.8/lusid_sdk.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-03-16 22:15:18.000000 lusid-sdk-1.0.8/lusid_sdk.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      122 2023-03-16 22:15:18.000000 lusid-sdk-1.0.8/lusid_sdk.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        6 2023-03-16 22:15:18.000000 lusid-sdk-1.0.8/lusid_sdk.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       38 2023-03-16 22:15:18.848405 lusid-sdk-1.0.8/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     2211 2023-03-16 22:05:46.000000 lusid-sdk-1.0.8/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:59:30.982177 lusid-sdk-1.0.9/
+-rw-r--r--   0 root         (0) root         (0)       40 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      309 2023-03-16 22:59:30.981177 lusid-sdk-1.0.9/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    93442 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:59:30.923177 lusid-sdk-1.0.9/lusid/
+-rw-r--r--   0 root         (0) root         (0)    42157 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/__init__.py
+-rw-r--r--   0 root         (0) root         (0)       22 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/__version__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:59:30.928177 lusid-sdk-1.0.9/lusid/api/
+-rw-r--r--   0 root         (0) root         (0)     2147 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    31243 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/aggregation_api.py
+-rw-r--r--   0 root         (0) root         (0)    39961 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/allocations_api.py
+-rw-r--r--   0 root         (0) root         (0)    21666 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/application_metadata_api.py
+-rw-r--r--   0 root         (0) root         (0)    38741 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/blocks_api.py
+-rw-r--r--   0 root         (0) root         (0)   128574 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/calendars_api.py
+-rw-r--r--   0 root         (0) root         (0)    37075 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/complex_market_data_api.py
+-rw-r--r--   0 root         (0) root         (0)    37217 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/configuration_recipe_api.py
+-rw-r--r--   0 root         (0) root         (0)    92907 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/corporate_action_sources_api.py
+-rw-r--r--   0 root         (0) root         (0)    71069 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/counterparties_api.py
+-rw-r--r--   0 root         (0) root         (0)   177505 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/custom_entities_api.py
+-rw-r--r--   0 root         (0) root         (0)    36859 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/custom_entity_definitions_api.py
+-rw-r--r--   0 root         (0) root         (0)    42656 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/cut_label_definitions_api.py
+-rw-r--r--   0 root         (0) root         (0)    74817 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/data_types_api.py
+-rw-r--r--   0 root         (0) root         (0)    21097 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/derived_transaction_portfolios_api.py
+-rw-r--r--   0 root         (0) root         (0)    11461 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/entities_api.py
+-rw-r--r--   0 root         (0) root         (0)    39311 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/executions_api.py
+-rw-r--r--   0 root         (0) root         (0)   173179 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/instruments_api.py
+-rw-r--r--   0 root         (0) root         (0)   237747 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/legal_entities_api.py
+-rw-r--r--   0 root         (0) root         (0)    39234 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/orders_api.py
+-rw-r--r--   0 root         (0) root         (0)    39885 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/participations_api.py
+-rw-r--r--   0 root         (0) root         (0)   223041 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/persons_api.py
+-rw-r--r--   0 root         (0) root         (0)   339172 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/portfolio_groups_api.py
+-rw-r--r--   0 root         (0) root         (0)   297030 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/portfolios_api.py
+-rw-r--r--   0 root         (0) root         (0)    58891 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/property_definitions_api.py
+-rw-r--r--   0 root         (0) root         (0)    58370 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/quotes_api.py
+-rw-r--r--   0 root         (0) root         (0)    70602 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/reconciliations_api.py
+-rw-r--r--   0 root         (0) root         (0)    46619 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/reference_portfolio_api.py
+-rw-r--r--   0 root         (0) root         (0)    51157 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/relationship_definitions_api.py
+-rw-r--r--   0 root         (0) root         (0)    22583 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/relationships_api.py
+-rw-r--r--   0 root         (0) root         (0)    27642 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/schemas_api.py
+-rw-r--r--   0 root         (0) root         (0)     8323 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/scopes_api.py
+-rw-r--r--   0 root         (0) root         (0)    48095 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/search_api.py
+-rw-r--r--   0 root         (0) root         (0)    39247 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/sequences_api.py
+-rw-r--r--   0 root         (0) root         (0)    14424 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/system_configuration_api.py
+-rw-r--r--   0 root         (0) root         (0)   323744 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api/transaction_portfolios_api.py
+-rw-r--r--   0 root         (0) root         (0)    27344 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/api_client.py
+-rw-r--r--   0 root         (0) root         (0)    16571 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/configuration.py
+-rw-r--r--   0 root         (0) root         (0)     5079 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/exceptions.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:59:30.980177 lusid-sdk-1.0.9/lusid/models/
+-rw-r--r--   0 root         (0) root         (0)    39307 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     6340 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/a2_b_breakdown.py
+-rw-r--r--   0 root         (0) root         (0)     5185 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/a2_b_category.py
+-rw-r--r--   0 root         (0) root         (0)    17994 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/a2_b_data_record.py
+-rw-r--r--   0 root         (0) root         (0)    21249 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/a2_b_movement_record.py
+-rw-r--r--   0 root         (0) root         (0)     7104 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/access_controlled_action.py
+-rw-r--r--   0 root         (0) root         (0)     8867 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/access_controlled_resource.py
+-rw-r--r--   0 root         (0) root         (0)     8023 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/access_metadata_operation.py
+-rw-r--r--   0 root         (0) root         (0)     5784 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/access_metadata_value.py
+-rw-r--r--   0 root         (0) root         (0)     7198 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/action_id.py
+-rw-r--r--   0 root         (0) root         (0)     4725 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/action_result_of_portfolio.py
+-rw-r--r--   0 root         (0) root         (0)     7222 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/add_business_days_to_date_request.py
+-rw-r--r--   0 root         (0) root         (0)     4157 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/add_business_days_to_date_response.py
+-rw-r--r--   0 root         (0) root         (0)    10980 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/address_definition.py
+-rw-r--r--   0 root         (0) root         (0)     6118 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/address_key_filter.py
+-rw-r--r--   0 root         (0) root         (0)     9172 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/address_key_option_definition.py
+-rw-r--r--   0 root         (0) root         (0)     6832 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/adjust_holding.py
+-rw-r--r--   0 root         (0) root         (0)    12008 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/adjust_holding_for_date_request.py
+-rw-r--r--   0 root         (0) root         (0)    10262 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/adjust_holding_request.py
+-rw-r--r--   0 root         (0) root         (0)     7500 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/aggregate_spec.py
+-rw-r--r--   0 root         (0) root         (0)    13024 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/aggregated_return.py
+-rw-r--r--   0 root         (0) root         (0)    13772 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/aggregated_returns_request.py
+-rw-r--r--   0 root         (0) root         (0)     6028 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/aggregated_returns_response.py
+-rw-r--r--   0 root         (0) root         (0)    10298 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/aggregation.py
+-rw-r--r--   0 root         (0) root         (0)     4009 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/aggregation_context.py
+-rw-r--r--   0 root         (0) root         (0)     7085 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/aggregation_measure_failure_detail.py
+-rw-r--r--   0 root         (0) root         (0)     8775 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/aggregation_options.py
+-rw-r--r--   0 root         (0) root         (0)    25169 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/aggregation_query.py
+-rw-r--r--   0 root         (0) root         (0)    24848 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/allocation.py
+-rw-r--r--   0 root         (0) root         (0)    21188 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/allocation_request.py
+-rw-r--r--   0 root         (0) root         (0)     4436 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/allocation_set_request.py
+-rw-r--r--   0 root         (0) root         (0)    12994 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/amortisation_event.py
+-rw-r--r--   0 root         (0) root         (0)    13134 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/amortisation_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7168 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/annul_quotes_response.py
+-rw-r--r--   0 root         (0) root         (0)     6065 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/annul_single_structured_data_response.py
+-rw-r--r--   0 root         (0) root         (0)     7181 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/annul_structured_data_response.py
+-rw-r--r--   0 root         (0) root         (0)     7902 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/barrier.py
+-rw-r--r--   0 root         (0) root         (0)    10814 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/basket.py
+-rw-r--r--   0 root         (0) root         (0)    10914 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/basket_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7620 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/basket_identifier.py
+-rw-r--r--   0 root         (0) root         (0)     7230 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/batch_adjust_holdings_response.py
+-rw-r--r--   0 root         (0) root         (0)     7647 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/batch_upsert_portfolio_transactions_response.py
+-rw-r--r--   0 root         (0) root         (0)    18549 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/block.py
+-rw-r--r--   0 root         (0) root         (0)    15838 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/block_request.py
+-rw-r--r--   0 root         (0) root         (0)     4109 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/block_set_request.py
+-rw-r--r--   0 root         (0) root         (0)    22931 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/bond.py
+-rw-r--r--   0 root         (0) root         (0)    23191 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/bond_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    14817 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/bond_default_event.py
+-rw-r--r--   0 root         (0) root         (0)    14977 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/bond_default_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     9031 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/calendar.py
+-rw-r--r--   0 root         (0) root         (0)    13374 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/calendar_date.py
+-rw-r--r--   0 root         (0) root         (0)    13183 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cap_floor.py
+-rw-r--r--   0 root         (0) root         (0)    13323 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cap_floor_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     9845 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cash_dividend_event.py
+-rw-r--r--   0 root         (0) root         (0)     9945 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cash_dividend_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10169 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cash_flow_event.py
+-rw-r--r--   0 root         (0) root         (0)    10269 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cash_flow_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10510 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cash_flow_lineage.py
+-rw-r--r--   0 root         (0) root         (0)    11249 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cash_flow_value.py
+-rw-r--r--   0 root         (0) root         (0)    11389 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cash_flow_value_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6768 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cash_flow_value_set.py
+-rw-r--r--   0 root         (0) root         (0)     6828 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cash_flow_value_set_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6856 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cash_ladder_record.py
+-rw-r--r--   0 root         (0) root         (0)    10170 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cash_perpetual.py
+-rw-r--r--   0 root         (0) root         (0)    10270 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cash_perpetual_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    24112 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cds_flow_conventions.py
+-rw-r--r--   0 root         (0) root         (0)    17378 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cds_index.py
+-rw-r--r--   0 root         (0) root         (0)    17578 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cds_index_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10137 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cds_protection_detail_specification.py
+-rw-r--r--   0 root         (0) root         (0)    11015 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/change.py
+-rw-r--r--   0 root         (0) root         (0)    10714 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/change_history.py
+-rw-r--r--   0 root         (0) root         (0)     8704 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/change_item.py
+-rw-r--r--   0 root         (0) root         (0)     7846 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/close_event.py
+-rw-r--r--   0 root         (0) root         (0)     7926 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/close_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    15717 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/complete_portfolio.py
+-rw-r--r--   0 root         (0) root         (0)    14719 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/complete_relationship.py
+-rw-r--r--   0 root         (0) root         (0)    11257 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/complex_bond.py
+-rw-r--r--   0 root         (0) root         (0)    11357 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/complex_bond_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7096 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/complex_market_data.py
+-rw-r--r--   0 root         (0) root         (0)    11521 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/complex_market_data_id.py
+-rw-r--r--   0 root         (0) root         (0)    11637 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/compounding.py
+-rw-r--r--   0 root         (0) root         (0)    14328 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/configuration_recipe.py
+-rw-r--r--   0 root         (0) root         (0)    15247 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/configuration_recipe_snippet.py
+-rw-r--r--   0 root         (0) root         (0)     6181 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/constituents_adjustment_header.py
+-rw-r--r--   0 root         (0) root         (0)    19498 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/contract_for_difference.py
+-rw-r--r--   0 root         (0) root         (0)    19718 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/contract_for_difference_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10863 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/corporate_action.py
+-rw-r--r--   0 root         (0) root         (0)     9857 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/corporate_action_source.py
+-rw-r--r--   0 root         (0) root         (0)     5718 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/corporate_action_transition.py
+-rw-r--r--   0 root         (0) root         (0)    10625 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/corporate_action_transition_component.py
+-rw-r--r--   0 root         (0) root         (0)     7357 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/corporate_action_transition_component_request.py
+-rw-r--r--   0 root         (0) root         (0)     5646 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/corporate_action_transition_request.py
+-rw-r--r--   0 root         (0) root         (0)    11822 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/counterparty_agreement.py
+-rw-r--r--   0 root         (0) root         (0)     8524 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/counterparty_risk_information.py
+-rw-r--r--   0 root         (0) root         (0)     6161 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/counterparty_signatory.py
+-rw-r--r--   0 root         (0) root         (0)    10189 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_calendar_request.py
+-rw-r--r--   0 root         (0) root         (0)    12686 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_corporate_action_source_request.py
+-rw-r--r--   0 root         (0) root         (0)     9424 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_cut_label_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)    20417 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_data_type_request.py
+-rw-r--r--   0 root         (0) root         (0)    13518 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_date_request.py
+-rw-r--r--   0 root         (0) root         (0)    15511 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_derived_property_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)    20890 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_derived_transaction_portfolio_request.py
+-rw-r--r--   0 root         (0) root         (0)     4462 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_portfolio_details.py
+-rw-r--r--   0 root         (0) root         (0)    12383 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_portfolio_group_request.py
+-rw-r--r--   0 root         (0) root         (0)    17579 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_property_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)    11661 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_reference_portfolio_request.py
+-rw-r--r--   0 root         (0) root         (0)    22106 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_relationship_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)    10113 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_relationship_request.py
+-rw-r--r--   0 root         (0) root         (0)    11654 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_sequence_request.py
+-rw-r--r--   0 root         (0) root         (0)    20612 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_transaction_portfolio_request.py
+-rw-r--r--   0 root         (0) root         (0)     9310 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/create_unit_definition.py
+-rw-r--r--   0 root         (0) root         (0)    18199 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/credit_default_swap.py
+-rw-r--r--   0 root         (0) root         (0)    18399 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/credit_default_swap_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7521 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/credit_rating.py
+-rw-r--r--   0 root         (0) root         (0)    16567 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/credit_spread_curve_data.py
+-rw-r--r--   0 root         (0) root         (0)    16767 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/credit_spread_curve_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    20912 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/credit_support_annex.py
+-rw-r--r--   0 root         (0) root         (0)     4642 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/currency_and_amount.py
+-rw-r--r--   0 root         (0) root         (0)    15766 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/custodian_account.py
+-rw-r--r--   0 root         (0) root         (0)    11807 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/custom_entity_definition.py
+-rw-r--r--   0 root         (0) root         (0)    10534 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/custom_entity_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)     8081 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/custom_entity_field.py
+-rw-r--r--   0 root         (0) root         (0)    11325 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/custom_entity_field_definition.py
+-rw-r--r--   0 root         (0) root         (0)    12486 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/custom_entity_id.py
+-rw-r--r--   0 root         (0) root         (0)     8385 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/custom_entity_request.py
+-rw-r--r--   0 root         (0) root         (0)    13657 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/custom_entity_response.py
+-rw-r--r--   0 root         (0) root         (0)     8560 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cut_label_definition.py
+-rw-r--r--   0 root         (0) root         (0)     4563 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/cut_local_time.py
+-rw-r--r--   0 root         (0) root         (0)    15955 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/data_type.py
+-rw-r--r--   0 root         (0) root         (0)    15138 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/data_type_summary.py
+-rw-r--r--   0 root         (0) root         (0)    14147 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/date_attributes.py
+-rw-r--r--   0 root         (0) root         (0)     4864 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/date_range.py
+-rw-r--r--   0 root         (0) root         (0)     3458 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/day_of_week.py
+-rw-r--r--   0 root         (0) root         (0)     5179 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/delete_instrument_properties_response.py
+-rw-r--r--   0 root         (0) root         (0)     6116 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/delete_instrument_response.py
+-rw-r--r--   0 root         (0) root         (0)     6132 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/delete_instruments_response.py
+-rw-r--r--   0 root         (0) root         (0)    10335 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/delete_relationship_request.py
+-rw-r--r--   0 root         (0) root         (0)     7419 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/deleted_entity_response.py
+-rw-r--r--   0 root         (0) root         (0)     8387 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/dependency_source_filter.py
+-rw-r--r--   0 root         (0) root         (0)    11233 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/discount_factor_curve_data.py
+-rw-r--r--   0 root         (0) root         (0)    11353 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/discount_factor_curve_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     5619 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/economic_dependency.py
+-rw-r--r--   0 root         (0) root         (0)     6020 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/economic_dependency_with_complex_market_data.py
+-rw-r--r--   0 root         (0) root         (0)     6830 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/economic_dependency_with_quote.py
+-rw-r--r--   0 root         (0) root         (0)     5398 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/empty_model_options.py
+-rw-r--r--   0 root         (0) root         (0)     5438 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/empty_model_options_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6713 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/entity_identifier.py
+-rw-r--r--   0 root         (0) root         (0)     8495 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/equity.py
+-rw-r--r--   0 root         (0) root         (0)     8575 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/equity_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11924 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/equity_all_of_identifiers.py
+-rw-r--r--   0 root         (0) root         (0)    11440 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/equity_curve_by_prices_data.py
+-rw-r--r--   0 root         (0) root         (0)    11560 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/equity_curve_by_prices_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7849 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/equity_model_options.py
+-rw-r--r--   0 root         (0) root         (0)     7909 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/equity_model_options_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    24187 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/equity_option.py
+-rw-r--r--   0 root         (0) root         (0)    24487 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/equity_option_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    23696 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/equity_swap.py
+-rw-r--r--   0 root         (0) root         (0)    23956 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/equity_swap_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11231 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/equity_vol_surface_data.py
+-rw-r--r--   0 root         (0) root         (0)    11351 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/equity_vol_surface_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6806 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/error_detail.py
+-rw-r--r--   0 root         (0) root         (0)     4531 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/event_date_range.py
+-rw-r--r--   0 root         (0) root         (0)    11841 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/exchange_traded_option.py
+-rw-r--r--   0 root         (0) root         (0)    11961 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/exchange_traded_option_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    23036 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/exchange_traded_option_contract_details.py
+-rw-r--r--   0 root         (0) root         (0)    24122 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/execution.py
+-rw-r--r--   0 root         (0) root         (0)    21469 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/execution_request.py
+-rw-r--r--   0 root         (0) root         (0)     4169 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/execution_set_request.py
+-rw-r--r--   0 root         (0) root         (0)    11000 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/exercise_event.py
+-rw-r--r--   0 root         (0) root         (0)    11120 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/exercise_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10285 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/exotic_instrument.py
+-rw-r--r--   0 root         (0) root         (0)    10365 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/exotic_instrument_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11174 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/expanded_group.py
+-rw-r--r--   0 root         (0) root         (0)     6695 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/field_definition.py
+-rw-r--r--   0 root         (0) root         (0)     8258 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/field_schema.py
+-rw-r--r--   0 root         (0) root         (0)     5658 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/field_value.py
+-rw-r--r--   0 root         (0) root         (0)     5781 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/file_response.py
+-rw-r--r--   0 root         (0) root         (0)    13116 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fixed_leg.py
+-rw-r--r--   0 root         (0) root         (0)    13256 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fixed_leg_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     4915 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fixed_leg_all_of_overrides.py
+-rw-r--r--   0 root         (0) root         (0)    13373 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/floating_leg.py
+-rw-r--r--   0 root         (0) root         (0)    13513 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/floating_leg_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6592 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/flow_convention_name.py
+-rw-r--r--   0 root         (0) root         (0)    23990 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/flow_conventions.py
+-rw-r--r--   0 root         (0) root         (0)    15807 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/forward_rate_agreement.py
+-rw-r--r--   0 root         (0) root         (0)    15987 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/forward_rate_agreement_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    14013 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/funding_leg.py
+-rw-r--r--   0 root         (0) root         (0)    14133 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/funding_leg_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    20197 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/future.py
+-rw-r--r--   0 root         (0) root         (0)    20397 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/future_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    21009 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/futures_contract_details.py
+-rw-r--r--   0 root         (0) root         (0)    20192 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_forward.py
+-rw-r--r--   0 root         (0) root         (0)    20432 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_forward_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    12659 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_forward_curve_by_quote_reference.py
+-rw-r--r--   0 root         (0) root         (0)    12799 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_forward_curve_by_quote_reference_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    13026 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_forward_curve_data.py
+-rw-r--r--   0 root         (0) root         (0)    13186 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_forward_curve_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11327 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_forward_model_options.py
+-rw-r--r--   0 root         (0) root         (0)    11427 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_forward_model_options_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    13322 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_forward_pips_curve_data.py
+-rw-r--r--   0 root         (0) root         (0)    13482 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_forward_pips_curve_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    13194 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_forward_tenor_curve_data.py
+-rw-r--r--   0 root         (0) root         (0)    13354 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_forward_tenor_curve_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    13490 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_forward_tenor_pips_curve_data.py
+-rw-r--r--   0 root         (0) root         (0)    13650 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_forward_tenor_pips_curve_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    28087 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_option.py
+-rw-r--r--   0 root         (0) root         (0)    28447 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_option_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11021 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_swap.py
+-rw-r--r--   0 root         (0) root         (0)    11121 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_swap_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11135 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/fx_vol_surface_data.py
+-rw-r--r--   0 root         (0) root         (0)     7279 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/get_complex_market_data_response.py
+-rw-r--r--   0 root         (0) root         (0)     7088 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/get_counterparty_agreement_response.py
+-rw-r--r--   0 root         (0) root         (0)     7040 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/get_credit_support_annex_response.py
+-rw-r--r--   0 root         (0) root         (0)     7371 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/get_instruments_response.py
+-rw-r--r--   0 root         (0) root         (0)     8047 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/get_quotes_response.py
+-rw-r--r--   0 root         (0) root         (0)     5689 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/get_recipe_response.py
+-rw-r--r--   0 root         (0) root         (0)    12030 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/get_reference_portfolio_constituents_response.py
+-rw-r--r--   0 root         (0) root         (0)    12535 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/holding_adjustment.py
+-rw-r--r--   0 root         (0) root         (0)    13889 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/holding_adjustment_with_date.py
+-rw-r--r--   0 root         (0) root         (0)     4577 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/holding_context.py
+-rw-r--r--   0 root         (0) root         (0)    10491 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/holdings_adjustment.py
+-rw-r--r--   0 root         (0) root         (0)     9374 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/holdings_adjustment_header.py
+-rw-r--r--   0 root         (0) root         (0)     3970 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/i_data_record.py
+-rw-r--r--   0 root         (0) root         (0)     6778 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/i_unit_definition_dto.py
+-rw-r--r--   0 root         (0) root         (0)     7949 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/id_selector_definition.py
+-rw-r--r--   0 root         (0) root         (0)     9438 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/identifier_part_schema.py
+-rw-r--r--   0 root         (0) root         (0)    18219 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/index_convention.py
+-rw-r--r--   0 root         (0) root         (0)     7150 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/index_model_options.py
+-rw-r--r--   0 root         (0) root         (0)     7210 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/index_model_options_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7581 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/industry_classifier.py
+-rw-r--r--   0 root         (0) root         (0)    36320 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/inflation_linked_bond.py
+-rw-r--r--   0 root         (0) root         (0)    36720 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/inflation_linked_bond_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    25334 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/inflation_swap.py
+-rw-r--r--   0 root         (0) root         (0)    25634 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/inflation_swap_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10090 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/informational_error_event.py
+-rw-r--r--   0 root         (0) root         (0)    10190 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/informational_error_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    13185 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/informational_event.py
+-rw-r--r--   0 root         (0) root         (0)    13325 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/informational_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    22490 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/inline_valuation_request.py
+-rw-r--r--   0 root         (0) root         (0)     8210 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/inline_valuations_reconciliation_request.py
+-rw-r--r--   0 root         (0) root         (0)     5481 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/input_transition.py
+-rw-r--r--   0 root         (0) root         (0)    19961 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/instrument.py
+-rw-r--r--   0 root         (0) root         (0)     9470 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/instrument_definition.py
+-rw-r--r--   0 root         (0) root         (0)     8348 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/instrument_definition_format.py
+-rw-r--r--   0 root         (0) root         (0)     6924 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/instrument_event.py
+-rw-r--r--   0 root         (0) root         (0)    17157 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/instrument_event_holder.py
+-rw-r--r--   0 root         (0) root         (0)     7700 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/instrument_id_type_descriptor.py
+-rw-r--r--   0 root         (0) root         (0)     5728 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/instrument_id_value.py
+-rw-r--r--   0 root         (0) root         (0)     7134 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/instrument_leg.py
+-rw-r--r--   0 root         (0) root         (0)     6699 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/instrument_leg_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6118 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/instrument_match.py
+-rw-r--r--   0 root         (0) root         (0)     6889 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/instrument_properties.py
+-rw-r--r--   0 root         (0) root         (0)     6083 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/instrument_search_property.py
+-rw-r--r--   0 root         (0) root         (0)    14277 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/interest_rate_swap.py
+-rw-r--r--   0 root         (0) root         (0)    14417 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/interest_rate_swap_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    13510 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/interest_rate_swaption.py
+-rw-r--r--   0 root         (0) root         (0)    13650 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/interest_rate_swaption_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11120 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/ir_vol_cube_data.py
+-rw-r--r--   0 root         (0) root         (0)    11240 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/ir_vol_cube_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     5575 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/is_business_day_response.py
+-rw-r--r--   0 root         (0) root         (0)     4311 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/label_value_set.py
+-rw-r--r--   0 root         (0) root         (0)    17095 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/leg_definition.py
+-rw-r--r--   0 root         (0) root         (0)    13346 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/legal_entity.py
+-rw-r--r--   0 root         (0) root         (0)     5400 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/level_step.py
+-rw-r--r--   0 root         (0) root         (0)     8320 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/life_cycle_event_lineage.py
+-rw-r--r--   0 root         (0) root         (0)     8841 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/life_cycle_event_value.py
+-rw-r--r--   0 root         (0) root         (0)     8941 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/life_cycle_event_value_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6392 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/link.py
+-rw-r--r--   0 root         (0) root         (0)     6623 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/list_aggregation_reconciliation.py
+-rw-r--r--   0 root         (0) root         (0)    10736 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/list_aggregation_response.py
+-rw-r--r--   0 root         (0) root         (0)     8140 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/lusid_instrument.py
+-rw-r--r--   0 root         (0) root         (0)     9506 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/lusid_problem_details.py
+-rw-r--r--   0 root         (0) root         (0)     5947 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/lusid_unique_id.py
+-rw-r--r--   0 root         (0) root         (0)    10706 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/lusid_validation_problem_details.py
+-rw-r--r--   0 root         (0) root         (0)     6589 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/mapped_string.py
+-rw-r--r--   0 root         (0) root         (0)    10565 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/mapping.py
+-rw-r--r--   0 root         (0) root         (0)    10470 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/mapping_rule.py
+-rw-r--r--   0 root         (0) root         (0)     9380 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/market_context.py
+-rw-r--r--   0 root         (0) root         (0)     6867 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/market_context_suppliers.py
+-rw-r--r--   0 root         (0) root         (0)    26172 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/market_data_key_rule.py
+-rw-r--r--   0 root         (0) root         (0)     5841 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/market_data_overrides.py
+-rw-r--r--   0 root         (0) root         (0)    23809 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/market_data_specific_rule.py
+-rw-r--r--   0 root         (0) root         (0)    14880 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/market_options.py
+-rw-r--r--   0 root         (0) root         (0)     5970 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/market_quote.py
+-rw-r--r--   0 root         (0) root         (0)     4609 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/metric_value.py
+-rw-r--r--   0 root         (0) root         (0)     5992 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/model_options.py
+-rw-r--r--   0 root         (0) root         (0)     7700 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/model_property.py
+-rw-r--r--   0 root         (0) root         (0)     7505 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/model_selection.py
+-rw-r--r--   0 root         (0) root         (0)     5119 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/next_value_in_sequence_response.py
+-rw-r--r--   0 root         (0) root         (0)    11964 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/opaque_market_data.py
+-rw-r--r--   0 root         (0) root         (0)    12084 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/opaque_market_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6307 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/opaque_model_options.py
+-rw-r--r--   0 root         (0) root         (0)     6367 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/opaque_model_options_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6895 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/open_event.py
+-rw-r--r--   0 root         (0) root         (0)     6955 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/open_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     5598 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/operation.py
+-rw-r--r--   0 root         (0) root         (0)    22500 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/order.py
+-rw-r--r--   0 root         (0) root         (0)     5698 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/order_by_spec.py
+-rw-r--r--   0 root         (0) root         (0)    18756 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/order_request.py
+-rw-r--r--   0 root         (0) root         (0)     4246 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/order_set_request.py
+-rw-r--r--   0 root         (0) root         (0)     4383 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/otc_confirmation.py
+-rw-r--r--   0 root         (0) root         (0)    33018 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/output_transaction.py
+-rw-r--r--   0 root         (0) root         (0)    10332 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/output_transition.py
+-rw-r--r--   0 root         (0) root         (0)     7385 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_allocation.py
+-rw-r--r--   0 root         (0) root         (0)     7245 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_block.py
+-rw-r--r--   0 root         (0) root         (0)     7329 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_calendar.py
+-rw-r--r--   0 root         (0) root         (0)     7693 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_corporate_action_source.py
+-rw-r--r--   0 root         (0) root         (0)     7721 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_custom_entity_definition.py
+-rw-r--r--   0 root         (0) root         (0)     7665 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_custom_entity_response.py
+-rw-r--r--   0 root         (0) root         (0)     7609 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_cut_label_definition.py
+-rw-r--r--   0 root         (0) root         (0)     7525 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_data_type_summary.py
+-rw-r--r--   0 root         (0) root         (0)     7357 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_execution.py
+-rw-r--r--   0 root         (0) root         (0)     7385 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_instrument.py
+-rw-r--r--   0 root         (0) root         (0)     7693 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_instrument_event_holder.py
+-rw-r--r--   0 root         (0) root         (0)     7413 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_legal_entity.py
+-rw-r--r--   0 root         (0) root         (0)     7245 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_order.py
+-rw-r--r--   0 root         (0) root         (0)     7469 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_participation.py
+-rw-r--r--   0 root         (0) root         (0)     7273 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_person.py
+-rw-r--r--   0 root         (0) root         (0)     7833 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_portfolio_group_search_result.py
+-rw-r--r--   0 root         (0) root         (0)     7693 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_portfolio_search_result.py
+-rw-r--r--   0 root         (0) root         (0)     7945 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_property_definition_search_result.py
+-rw-r--r--   0 root         (0) root         (0)     7721 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_relationship_definition.py
+-rw-r--r--   0 root         (0) root         (0)     7609 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_sequence_definition.py
+-rw-r--r--   0 root         (0) root         (0)     7482 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/participation.py
+-rw-r--r--   0 root         (0) root         (0)     6926 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/participation_request.py
+-rw-r--r--   0 root         (0) root         (0)     4229 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/participation_set_request.py
+-rw-r--r--   0 root         (0) root         (0)     8788 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/performance_return.py
+-rw-r--r--   0 root         (0) root         (0)    10181 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/performance_returns_metric.py
+-rw-r--r--   0 root         (0) root         (0)     5213 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/perpetual_property.py
+-rw-r--r--   0 root         (0) root         (0)    11043 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/person.py
+-rw-r--r--   0 root         (0) root         (0)    21169 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/portfolio.py
+-rw-r--r--   0 root         (0) root         (0)    23700 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/portfolio_cash_flow.py
+-rw-r--r--   0 root         (0) root         (0)     8810 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/portfolio_cash_ladder.py
+-rw-r--r--   0 root         (0) root         (0)    15147 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/portfolio_details.py
+-rw-r--r--   0 root         (0) root         (0)     8460 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/portfolio_entity_id.py
+-rw-r--r--   0 root         (0) root         (0)    13607 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/portfolio_group.py
+-rw-r--r--   0 root         (0) root         (0)     6996 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/portfolio_group_properties.py
+-rw-r--r--   0 root         (0) root         (0)    12953 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/portfolio_group_search_result.py
+-rw-r--r--   0 root         (0) root         (0)    17791 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/portfolio_holding.py
+-rw-r--r--   0 root         (0) root         (0)     6863 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/portfolio_properties.py
+-rw-r--r--   0 root         (0) root         (0)     6775 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/portfolio_reconciliation_request.py
+-rw-r--r--   0 root         (0) root         (0)    17336 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/portfolio_result_data_key_rule.py
+-rw-r--r--   0 root         (0) root         (0)    17516 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/portfolio_result_data_key_rule_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    15510 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/portfolio_search_result.py
+-rw-r--r--   0 root         (0) root         (0)     7197 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/portfolios_reconciliation_request.py
+-rw-r--r--   0 root         (0) root         (0)     6022 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/premium.py
+-rw-r--r--   0 root         (0) root         (0)     9445 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/pricing_context.py
+-rw-r--r--   0 root         (0) root         (0)    27514 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/pricing_options.py
+-rw-r--r--   0 root         (0) root         (0)     7870 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/processed_command.py
+-rw-r--r--   0 root         (0) root         (0)    27010 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/property_definition.py
+-rw-r--r--   0 root         (0) root         (0)    27874 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/property_definition_search_result.py
+-rw-r--r--   0 root         (0) root         (0)     7835 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/property_filter.py
+-rw-r--r--   0 root         (0) root         (0)     7969 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/property_interval.py
+-rw-r--r--   0 root         (0) root         (0)     5265 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/property_schema.py
+-rw-r--r--   0 root         (0) root         (0)     6066 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/property_value.py
+-rw-r--r--   0 root         (0) root         (0)    10795 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/quote.py
+-rw-r--r--   0 root         (0) root         (0)     5783 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/quote_id.py
+-rw-r--r--   0 root         (0) root         (0)    14721 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/quote_series_id.py
+-rw-r--r--   0 root         (0) root         (0)    11311 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/raw_vendor_event.py
+-rw-r--r--   0 root         (0) root         (0)    11431 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/raw_vendor_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    17980 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/realised_gain_loss.py
+-rw-r--r--   0 root         (0) root         (0)     9883 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reconcile_date_time_rule.py
+-rw-r--r--   0 root         (0) root         (0)     9983 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reconcile_date_time_rule_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     9945 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reconcile_numeric_rule.py
+-rw-r--r--   0 root         (0) root         (0)    10045 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reconcile_numeric_rule_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10716 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reconcile_string_rule.py
+-rw-r--r--   0 root         (0) root         (0)    10816 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reconcile_string_rule_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7788 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reconciled_transaction.py
+-rw-r--r--   0 root         (0) root         (0)    15668 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reconciliation_break.py
+-rw-r--r--   0 root         (0) root         (0)     5468 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reconciliation_left_right_address_key_pair.py
+-rw-r--r--   0 root         (0) root         (0)     7307 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reconciliation_line.py
+-rw-r--r--   0 root         (0) root         (0)    10383 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reconciliation_request.py
+-rw-r--r--   0 root         (0) root         (0)     5245 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reconciliation_response.py
+-rw-r--r--   0 root         (0) root         (0)     5472 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reconciliation_rule.py
+-rw-r--r--   0 root         (0) root         (0)     5343 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reference_data.py
+-rw-r--r--   0 root         (0) root         (0)    11099 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reference_instrument.py
+-rw-r--r--   0 root         (0) root         (0)    11199 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reference_instrument_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11192 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reference_portfolio_constituent.py
+-rw-r--r--   0 root         (0) root         (0)     7556 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reference_portfolio_constituent_request.py
+-rw-r--r--   0 root         (0) root         (0)    12677 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/related_entity.py
+-rw-r--r--   0 root         (0) root         (0)    10235 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/relation.py
+-rw-r--r--   0 root         (0) root         (0)    13986 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/relationship.py
+-rw-r--r--   0 root         (0) root         (0)    19714 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/relationship_definition.py
+-rw-r--r--   0 root         (0) root         (0)    25564 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/repo.py
+-rw-r--r--   0 root         (0) root         (0)    25824 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/repo_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    12033 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reset_event.py
+-rw-r--r--   0 root         (0) root         (0)    12173 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/reset_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6065 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_id.py
+-rw-r--r--   0 root         (0) root         (0)     7657 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_access_controlled_resource.py
+-rw-r--r--   0 root         (0) root         (0)     7571 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_access_metadata_value_of.py
+-rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_aggregation_query.py
+-rw-r--r--   0 root         (0) root         (0)     7265 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_allocation.py
+-rw-r--r--   0 root         (0) root         (0)     7125 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_block.py
+-rw-r--r--   0 root         (0) root         (0)     7321 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_calendar_date.py
+-rw-r--r--   0 root         (0) root         (0)     7153 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_change.py
+-rw-r--r--   0 root         (0) root         (0)     7349 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_change_history.py
+-rw-r--r--   0 root         (0) root         (0)     7769 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_constituents_adjustment_header.py
+-rw-r--r--   0 root         (0) root         (0)     7405 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_corporate_action.py
+-rw-r--r--   0 root         (0) root         (0)     7209 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_data_type.py
+-rw-r--r--   0 root         (0) root         (0)     7237 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_execution.py
+-rw-r--r--   0 root         (0) root         (0)     7881 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_get_counterparty_agreement_response.py
+-rw-r--r--   0 root         (0) root         (0)     7797 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_get_credit_support_annex_response.py
+-rw-r--r--   0 root         (0) root         (0)     7461 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_get_recipe_response.py
+-rw-r--r--   0 root         (0) root         (0)     7657 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_holdings_adjustment_header.py
+-rw-r--r--   0 root         (0) root         (0)     7489 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_i_unit_definition_dto.py
+-rw-r--r--   0 root         (0) root         (0)     7713 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_instrument_id_type_descriptor.py
+-rw-r--r--   0 root         (0) root         (0)     7293 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_legal_entity.py
+-rw-r--r--   0 root         (0) root         (0)     7181 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_mapping.py
+-rw-r--r--   0 root         (0) root         (0)     7125 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_order.py
+-rw-r--r--   0 root         (0) root         (0)     7349 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_participation.py
+-rw-r--r--   0 root         (0) root         (0)     7461 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_performance_return.py
+-rw-r--r--   0 root         (0) root         (0)     7153 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_person.py
+-rw-r--r--   0 root         (0) root         (0)     7237 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_portfolio.py
+-rw-r--r--   0 root         (0) root         (0)     7461 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_portfolio_cash_flow.py
+-rw-r--r--   0 root         (0) root         (0)     7517 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_portfolio_cash_ladder.py
+-rw-r--r--   0 root         (0) root         (0)     7377 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_portfolio_group.py
+-rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_processed_command.py
+-rw-r--r--   0 root         (0) root         (0)     7229 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_property.py
+-rw-r--r--   0 root         (0) root         (0)     7489 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_property_definition.py
+-rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_property_interval.py
+-rw-r--r--   0 root         (0) root         (0)     7125 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_quote.py
+-rw-r--r--   0 root         (0) root         (0)     7517 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_reconciliation_break.py
+-rw-r--r--   0 root         (0) root         (0)     7209 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_relation.py
+-rw-r--r--   0 root         (0) root         (0)     7321 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_relationship.py
+-rw-r--r--   0 root         (0) root         (0)     7405 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_scope_definition.py
+-rw-r--r--   0 root         (0) root         (0)     7123 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_string.py
+-rw-r--r--   0 root         (0) root         (0)     7237 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/resource_list_of_value_type.py
+-rw-r--r--   0 root         (0) root         (0)     7131 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/response_meta_data.py
+-rw-r--r--   0 root         (0) root         (0)    16884 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_data_key_rule.py
+-rw-r--r--   0 root         (0) root         (0)    17064 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_data_key_rule_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6620 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_data_schema.py
+-rw-r--r--   0 root         (0) root         (0)     5593 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_key_rule.py
+-rw-r--r--   0 root         (0) root         (0)     6667 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value.py
+-rw-r--r--   0 root         (0) root         (0)     8572 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value0_d.py
+-rw-r--r--   0 root         (0) root         (0)     8672 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value0_d_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6563 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value_bool.py
+-rw-r--r--   0 root         (0) root         (0)     6623 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value_bool_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6573 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value_currency.py
+-rw-r--r--   0 root         (0) root         (0)     6633 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value_currency_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     8004 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value_date_time_offset.py
+-rw-r--r--   0 root         (0) root         (0)     8084 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value_date_time_offset_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7880 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value_decimal.py
+-rw-r--r--   0 root         (0) root         (0)     7960 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value_decimal_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6781 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value_dictionary.py
+-rw-r--r--   0 root         (0) root         (0)     6841 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value_dictionary_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7808 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value_int.py
+-rw-r--r--   0 root         (0) root         (0)     7888 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value_int_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6549 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value_string.py
+-rw-r--r--   0 root         (0) root         (0)     6609 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/result_value_string_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     5298 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/schedule.py
+-rw-r--r--   0 root         (0) root         (0)     5782 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/schema.py
+-rw-r--r--   0 root         (0) root         (0)     4421 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/scope_definition.py
+-rw-r--r--   0 root         (0) root         (0)    12312 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/sequence_definition.py
+-rw-r--r--   0 root         (0) root         (0)     4545 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/set_legal_entity_identifiers_request.py
+-rw-r--r--   0 root         (0) root         (0)     4697 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/set_legal_entity_properties_request.py
+-rw-r--r--   0 root         (0) root         (0)     4487 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/set_person_identifiers_request.py
+-rw-r--r--   0 root         (0) root         (0)     4849 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/set_person_properties_request.py
+-rw-r--r--   0 root         (0) root         (0)    11343 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/side_configuration_data.py
+-rw-r--r--   0 root         (0) root         (0)    14459 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/simple_instrument.py
+-rw-r--r--   0 root         (0) root         (0)    14599 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/simple_instrument_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     9596 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/step_schedule.py
+-rw-r--r--   0 root         (0) root         (0)     9696 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/step_schedule_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10119 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/stock_split_event.py
+-rw-r--r--   0 root         (0) root         (0)    10219 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/stock_split_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     9229 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/stream.py
+-rw-r--r--   0 root         (0) root         (0)     9013 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/supported_analytics_internal_request.py
+-rw-r--r--   0 root         (0) root         (0)     9501 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/target_tax_lot.py
+-rw-r--r--   0 root         (0) root         (0)     9697 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/target_tax_lot_request.py
+-rw-r--r--   0 root         (0) root         (0)    18130 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/term_deposit.py
+-rw-r--r--   0 root         (0) root         (0)    18290 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/term_deposit_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7853 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/touch.py
+-rw-r--r--   0 root         (0) root         (0)    30338 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transaction.py
+-rw-r--r--   0 root         (0) root         (0)     7083 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transaction_configuration_data.py
+-rw-r--r--   0 root         (0) root         (0)     7208 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transaction_configuration_data_request.py
+-rw-r--r--   0 root         (0) root         (0)    15020 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transaction_configuration_movement_data.py
+-rw-r--r--   0 root         (0) root         (0)    13934 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transaction_configuration_movement_data_request.py
+-rw-r--r--   0 root         (0) root         (0)    14164 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transaction_configuration_type_alias.py
+-rw-r--r--   0 root         (0) root         (0)     5083 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transaction_price.py
+-rw-r--r--   0 root         (0) root         (0)     6459 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transaction_property_mapping.py
+-rw-r--r--   0 root         (0) root         (0)     6568 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transaction_property_mapping_request.py
+-rw-r--r--   0 root         (0) root         (0)     9881 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transaction_query_parameters.py
+-rw-r--r--   0 root         (0) root         (0)    11041 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transaction_reconciliation_request.py
+-rw-r--r--   0 root         (0) root         (0)    25203 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transaction_request.py
+-rw-r--r--   0 root         (0) root         (0)     6795 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transaction_set_configuration_data.py
+-rw-r--r--   0 root         (0) root         (0)     5076 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transactions_reconciliations_response.py
+-rw-r--r--   0 root         (0) root         (0)    12319 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transition_event.py
+-rw-r--r--   0 root         (0) root         (0)    12479 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/transition_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    12563 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/trigger_event.py
+-rw-r--r--   0 root         (0) root         (0)    12703 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/trigger_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     9765 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/typed_resource_id.py
+-rw-r--r--   0 root         (0) root         (0)     7389 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/update_calendar_request.py
+-rw-r--r--   0 root         (0) root         (0)     8384 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/update_custom_entity_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)     8527 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/update_cut_label_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)     9293 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/update_data_type_request.py
+-rw-r--r--   0 root         (0) root         (0)     7187 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/update_instrument_identifier_request.py
+-rw-r--r--   0 root         (0) root         (0)     5732 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/update_portfolio_group_request.py
+-rw-r--r--   0 root         (0) root         (0)     5684 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/update_portfolio_request.py
+-rw-r--r--   0 root         (0) root         (0)     6201 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/update_property_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)    10184 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/update_relationship_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)     7868 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/update_unit_request.py
+-rw-r--r--   0 root         (0) root         (0)     5591 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_complex_market_data_request.py
+-rw-r--r--   0 root         (0) root         (0)    13956 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_corporate_action_request.py
+-rw-r--r--   0 root         (0) root         (0)     7350 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_corporate_actions_response.py
+-rw-r--r--   0 root         (0) root         (0)     4691 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_counterparty_agreement_request.py
+-rw-r--r--   0 root         (0) root         (0)     4423 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_credit_support_annex_request.py
+-rw-r--r--   0 root         (0) root         (0)     7423 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_custom_entities_response.py
+-rw-r--r--   0 root         (0) root         (0)     4488 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_custom_entity_access_metadata_request.py
+-rw-r--r--   0 root         (0) root         (0)    11530 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_instrument_event_request.py
+-rw-r--r--   0 root         (0) root         (0)     7374 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_instrument_events_response.py
+-rw-r--r--   0 root         (0) root         (0)     5336 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_instrument_properties_response.py
+-rw-r--r--   0 root         (0) root         (0)     7966 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_instrument_property_request.py
+-rw-r--r--   0 root         (0) root         (0)     8362 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_instruments_response.py
+-rw-r--r--   0 root         (0) root         (0)     4480 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_legal_entity_access_metadata_request.py
+-rw-r--r--   0 root         (0) root         (0)    11115 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_legal_entity_request.py
+-rw-r--r--   0 root         (0) root         (0)     4422 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_person_access_metadata_request.py
+-rw-r--r--   0 root         (0) root         (0)     9117 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_person_request.py
+-rw-r--r--   0 root         (0) root         (0)     4652 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_portfolio_access_metadata_request.py
+-rw-r--r--   0 root         (0) root         (0)     4710 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_portfolio_group_access_metadata_request.py
+-rw-r--r--   0 root         (0) root         (0)     7446 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_portfolio_transactions_response.py
+-rw-r--r--   0 root         (0) root         (0)     7602 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_quote_request.py
+-rw-r--r--   0 root         (0) root         (0)     7044 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_quotes_response.py
+-rw-r--r--   0 root         (0) root         (0)     5700 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_recipe_request.py
+-rw-r--r--   0 root         (0) root         (0)    10645 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_reference_portfolio_constituents_request.py
+-rw-r--r--   0 root         (0) root         (0)     5744 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_reference_portfolio_constituents_response.py
+-rw-r--r--   0 root         (0) root         (0)     8081 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_returns_response.py
+-rw-r--r--   0 root         (0) root         (0)     6072 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_single_structured_data_response.py
+-rw-r--r--   0 root         (0) root         (0)     7225 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_structured_data_response.py
+-rw-r--r--   0 root         (0) root         (0)     6948 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/upsert_transaction_properties_response.py
+-rw-r--r--   0 root         (0) root         (0)     3793 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/user.py
+-rw-r--r--   0 root         (0) root         (0)    21405 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/valuation_request.py
+-rw-r--r--   0 root         (0) root         (0)    13908 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/valuation_schedule.py
+-rw-r--r--   0 root         (0) root         (0)     8627 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/valuations_reconciliation_request.py
+-rw-r--r--   0 root         (0) root         (0)     4004 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/value_type.py
+-rw-r--r--   0 root         (0) root         (0)    15639 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/vendor_model_rule.py
+-rw-r--r--   0 root         (0) root         (0)    11534 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/version.py
+-rw-r--r--   0 root         (0) root         (0)     6388 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/version_summary_dto.py
+-rw-r--r--   0 root         (0) root         (0)     8591 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/versioned_resource_list_of_a2_b_data_record.py
+-rw-r--r--   0 root         (0) root         (0)     8719 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/versioned_resource_list_of_a2_b_movement_record.py
+-rw-r--r--   0 root         (0) root         (0)     8719 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/versioned_resource_list_of_output_transaction.py
+-rw-r--r--   0 root         (0) root         (0)     8687 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/versioned_resource_list_of_portfolio_holding.py
+-rw-r--r--   0 root         (0) root         (0)     8527 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/versioned_resource_list_of_transaction.py
+-rw-r--r--   0 root         (0) root         (0)     5793 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/weekend_mask.py
+-rw-r--r--   0 root         (0) root         (0)     8441 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/weighted_instrument.py
+-rw-r--r--   0 root         (0) root         (0)     4479 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/weighted_instruments.py
+-rw-r--r--   0 root         (0) root         (0)    11018 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/yield_curve_data.py
+-rw-r--r--   0 root         (0) root         (0)    11138 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/models/yield_curve_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    13517 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/rest.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:59:30.980177 lusid-sdk-1.0.9/lusid/tcp/
+-rw-r--r--   0 root         (0) root         (0)       93 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/tcp/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5321 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/tcp/tcp_keep_alive_probes.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:59:30.981177 lusid-sdk-1.0.9/lusid/utilities/
+-rw-r--r--   0 root         (0) root         (0)      432 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/utilities/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     6434 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/utilities/api_client_builder.py
+-rw-r--r--   0 root         (0) root         (0)     5397 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/utilities/api_client_factory.py
+-rw-r--r--   0 root         (0) root         (0)     3970 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/utilities/api_configuration.py
+-rw-r--r--   0 root         (0) root         (0)     4065 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/utilities/api_configuration_loader.py
+-rw-r--r--   0 root         (0) root         (0)     1030 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/utilities/config_keys.json
+-rw-r--r--   0 root         (0) root         (0)     1236 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/utilities/lusid_retry.py
+-rw-r--r--   0 root         (0) root         (0)     1725 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/utilities/proxy_config.py
+-rw-r--r--   0 root         (0) root         (0)     9701 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/lusid/utilities/refreshing_token.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:59:30.981177 lusid-sdk-1.0.9/lusid_sdk.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      309 2023-03-16 22:59:30.000000 lusid-sdk-1.0.9/lusid_sdk.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    23954 2023-03-16 22:59:30.000000 lusid-sdk-1.0.9/lusid_sdk.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-03-16 22:59:30.000000 lusid-sdk-1.0.9/lusid_sdk.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      122 2023-03-16 22:59:30.000000 lusid-sdk-1.0.9/lusid_sdk.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        6 2023-03-16 22:59:30.000000 lusid-sdk-1.0.9/lusid_sdk.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       38 2023-03-16 22:59:30.982177 lusid-sdk-1.0.9/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     2211 2023-03-16 22:44:18.000000 lusid-sdk-1.0.9/setup.py
```

### Comparing `lusid-sdk-1.0.8/README.md` & `lusid-sdk-1.0.9/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # lusid-sdk
 FINBOURNE Technology
 
 This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:
 
-- API version: 1.0.8
-- Package version: 1.0.8
+- API version: 1.0.9
+- Package version: 1.0.9
 - Build package: org.openapitools.codegen.languages.PythonLegacyClientCodegen
 For more information, please visit [https://www.finbourne.com](https://www.finbourne.com)
 
 ## Requirements.
 
 Python 2.7 and 3.4+
```

### Comparing `lusid-sdk-1.0.8/lusid/__init__.py` & `lusid-sdk-1.0.9/lusid/__init__.py`

 * *Files identical despite different names*

```diff
@@ -3,23 +3,23 @@
 # flake8: noqa
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
-__version__ = "1.0.8"
+__version__ = "1.0.9"
 
 # import apis into sdk package
 from lusid.api.aggregation_api import AggregationApi
 from lusid.api.allocations_api import AllocationsApi
 from lusid.api.application_metadata_api import ApplicationMetadataApi
 from lusid.api.blocks_api import BlocksApi
 from lusid.api.calendars_api import CalendarsApi
```

### Comparing `lusid-sdk-1.0.8/lusid/api/__init__.py` & `lusid-sdk-1.0.9/lusid/api/__init__.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-1.0.8/lusid/api/aggregation_api.py` & `lusid-sdk-1.0.9/lusid/api/aggregation_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -184,15 +184,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfAggregationQuery",
             400: "LusidValidationProblemDetails",
@@ -327,15 +327,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ListAggregationResponse",
             400: "LusidValidationProblemDetails",
@@ -470,15 +470,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ListAggregationResponse",
             400: "LusidValidationProblemDetails",
@@ -613,15 +613,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Aggregation",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/allocations_api.py` & `lusid-sdk-1.0.9/lusid/api/allocations_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -182,15 +182,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -366,15 +366,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Allocation",
             400: "LusidValidationProblemDetails",
@@ -570,15 +570,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfAllocation",
             400: "LusidValidationProblemDetails",
@@ -713,15 +713,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfAllocation",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/application_metadata_api.py` & `lusid-sdk-1.0.9/lusid/api/application_metadata_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -159,15 +159,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "FileResponse",
             400: "LusidValidationProblemDetails",
@@ -292,15 +292,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "VersionSummaryDto",
         }
@@ -439,15 +439,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfAccessControlledResource",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/blocks_api.py` & `lusid-sdk-1.0.9/lusid/api/blocks_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -182,15 +182,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -366,15 +366,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Block",
             400: "LusidValidationProblemDetails",
@@ -563,15 +563,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfBlock",
             400: "LusidValidationProblemDetails",
@@ -706,15 +706,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "ResourceListOfBlock",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/calendars_api.py` & `lusid-sdk-1.0.9/lusid/api/calendars_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -185,15 +185,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "AddBusinessDaysToDateResponse",
             400: "LusidValidationProblemDetails",
@@ -370,15 +370,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "CalendarDate",
             400: "LusidValidationProblemDetails",
@@ -517,15 +517,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Calendar",
             400: "LusidValidationProblemDetails",
@@ -688,15 +688,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Calendar",
             400: "LusidValidationProblemDetails",
@@ -878,15 +878,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "CalendarDate",
             400: "LusidValidationProblemDetails",
@@ -1051,15 +1051,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "list[datetime]",
             400: "LusidValidationProblemDetails",
@@ -1229,15 +1229,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Calendar",
             400: "LusidValidationProblemDetails",
@@ -1445,15 +1445,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfCalendarDate",
             400: "LusidValidationProblemDetails",
@@ -1634,15 +1634,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "IsBusinessDayResponse",
             400: "LusidValidationProblemDetails",
@@ -1815,15 +1815,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfCalendar",
             400: "LusidValidationProblemDetails",
@@ -2022,15 +2022,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfCalendar",
             400: "LusidValidationProblemDetails",
@@ -2207,15 +2207,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Calendar",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/complex_market_data_api.py` & `lusid-sdk-1.0.9/lusid/api/complex_market_data_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -179,15 +179,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "AnnulStructuredDataResponse",
             400: "LusidValidationProblemDetails",
@@ -374,15 +374,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "GetComplexMarketDataResponse",
             400: "LusidValidationProblemDetails",
@@ -540,15 +540,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "UpsertStructuredDataResponse",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/configuration_recipe_api.py` & `lusid-sdk-1.0.9/lusid/api/configuration_recipe_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -184,15 +184,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "AnnulSingleStructuredDataResponse",
             400: "LusidValidationProblemDetails",
@@ -362,15 +362,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "GetRecipeResponse",
             400: "LusidValidationProblemDetails",
@@ -517,15 +517,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfGetRecipeResponse",
             400: "LusidValidationProblemDetails",
@@ -664,15 +664,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "UpsertSingleStructuredDataResponse",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/corporate_action_sources_api.py` & `lusid-sdk-1.0.9/lusid/api/corporate_action_sources_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -199,15 +199,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "UpsertCorporateActionsResponse",
             400: "LusidValidationProblemDetails",
@@ -346,15 +346,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "CorporateActionSource",
             400: "LusidValidationProblemDetails",
@@ -529,15 +529,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -712,15 +712,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -950,15 +950,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfCorporateAction",
             400: "LusidValidationProblemDetails",
@@ -1165,15 +1165,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfInstrumentEventHolder",
             400: "LusidValidationProblemDetails",
@@ -1350,15 +1350,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfCorporateActionSource",
             400: "LusidValidationProblemDetails",
@@ -1531,15 +1531,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "UpsertInstrumentEventsResponse",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/counterparties_api.py` & `lusid-sdk-1.0.9/lusid/api/counterparties_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -187,15 +187,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "AnnulSingleStructuredDataResponse",
             400: "LusidValidationProblemDetails",
@@ -358,15 +358,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "AnnulSingleStructuredDataResponse",
             400: "LusidValidationProblemDetails",
@@ -536,15 +536,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "GetCounterpartyAgreementResponse",
             400: "LusidValidationProblemDetails",
@@ -714,15 +714,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "GetCreditSupportAnnexResponse",
             400: "LusidValidationProblemDetails",
@@ -854,15 +854,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfGetCounterpartyAgreementResponse",
             400: "LusidValidationProblemDetails",
@@ -994,15 +994,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfGetCreditSupportAnnexResponse",
             400: "LusidValidationProblemDetails",
@@ -1141,15 +1141,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "UpsertSingleStructuredDataResponse",
             400: "LusidValidationProblemDetails",
@@ -1288,15 +1288,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "UpsertSingleStructuredDataResponse",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/custom_entities_api.py` & `lusid-sdk-1.0.9/lusid/api/custom_entities_api.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -224,15 +224,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -466,15 +466,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -689,15 +689,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "dict(str, list[AccessMetadataValue])",
             400: "LusidValidationProblemDetails",
@@ -926,15 +926,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "CustomEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -1168,15 +1168,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "list[AccessMetadataValue]",
             400: "LusidValidationProblemDetails",
@@ -1420,15 +1420,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfRelationship",
             400: "LusidValidationProblemDetails",
@@ -1641,15 +1641,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfCustomEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -1878,15 +1878,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "dict(str, list[AccessMetadataValue])",
             400: "LusidValidationProblemDetails",
@@ -2059,15 +2059,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "UpsertCustomEntitiesResponse",
             400: "LusidValidationProblemDetails",
@@ -2223,15 +2223,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "CustomEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -2479,15 +2479,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "list[AccessMetadataValue]",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/custom_entity_definitions_api.py` & `lusid-sdk-1.0.9/lusid/api/custom_entity_definitions_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -159,15 +159,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "CustomEntityDefinition",
             400: "LusidValidationProblemDetails",
@@ -316,15 +316,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "CustomEntityDefinition",
             400: "LusidValidationProblemDetails",
@@ -497,15 +497,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfCustomEntityDefinition",
             400: "LusidValidationProblemDetails",
@@ -661,15 +661,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "CustomEntityDefinition",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/cut_label_definitions_api.py` & `lusid-sdk-1.0.9/lusid/api/cut_label_definitions_api.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -155,15 +155,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "CutLabelDefinition",
             400: "LusidValidationProblemDetails",
@@ -307,15 +307,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "datetime",
             400: "LusidValidationProblemDetails",
@@ -466,15 +466,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "CutLabelDefinition",
             400: "LusidValidationProblemDetails",
@@ -658,15 +658,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfCutLabelDefinition",
             400: "LusidValidationProblemDetails",
@@ -820,15 +820,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "CutLabelDefinition",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/data_types_api.py` & `lusid-sdk-1.0.9/lusid/api/data_types_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -158,15 +158,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "DataType",
             400: "LusidValidationProblemDetails",
@@ -336,15 +336,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DataType",
             400: "LusidValidationProblemDetails",
@@ -537,15 +537,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfIUnitDefinitionDto",
             400: "LusidValidationProblemDetails",
@@ -733,15 +733,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfDataTypeSummary",
             400: "LusidValidationProblemDetails",
@@ -936,15 +936,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfDataType",
             400: "LusidValidationProblemDetails",
@@ -1121,15 +1121,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DataType",
             400: "LusidValidationProblemDetails",
@@ -1306,15 +1306,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DataType",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/derived_transaction_portfolios_api.py` & `lusid-sdk-1.0.9/lusid/api/derived_transaction_portfolios_api.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -173,15 +173,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "Portfolio",
             400: "LusidValidationProblemDetails",
@@ -359,15 +359,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/entities_api.py` & `lusid-sdk-1.0.9/lusid/api/entities_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -187,15 +187,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             400: "LusidValidationProblemDetails",
             200: "ResourceListOfChange",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/executions_api.py` & `lusid-sdk-1.0.9/lusid/api/executions_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -182,15 +182,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -366,15 +366,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Execution",
             400: "LusidValidationProblemDetails",
@@ -563,15 +563,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfExecution",
             400: "LusidValidationProblemDetails",
@@ -706,15 +706,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "ResourceListOfExecution",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/instruments_api.py` & `lusid-sdk-1.0.9/lusid/api/instruments_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -194,15 +194,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeleteInstrumentResponse",
             400: "LusidValidationProblemDetails",
@@ -385,15 +385,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeleteInstrumentPropertiesResponse",
             400: "LusidValidationProblemDetails",
@@ -554,15 +554,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeleteInstrumentsResponse",
             400: "LusidValidationProblemDetails",
@@ -754,15 +754,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Instrument",
             400: "LusidValidationProblemDetails",
@@ -887,15 +887,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfInstrumentIdTypeDescriptor",
         }
@@ -1070,15 +1070,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "InstrumentProperties",
             400: "LusidValidationProblemDetails",
@@ -1306,15 +1306,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfPropertyInterval",
             400: "LusidValidationProblemDetails",
@@ -1537,15 +1537,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfRelationship",
             400: "LusidValidationProblemDetails",
@@ -1740,15 +1740,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "GetInstrumentsResponse",
             400: "LusidValidationProblemDetails",
@@ -1958,15 +1958,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfProperty",
             400: "LusidValidationProblemDetails",
@@ -2192,15 +2192,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfInstrument",
             400: "LusidValidationProblemDetails",
@@ -2376,15 +2376,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Instrument",
             400: "LusidValidationProblemDetails",
@@ -2538,15 +2538,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "UpsertInstrumentsResponse",
             400: "LusidValidationProblemDetails",
@@ -2700,15 +2700,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "UpsertInstrumentPropertiesResponse",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/legal_entities_api.py` & `lusid-sdk-1.0.9/lusid/api/legal_entities_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -209,15 +209,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -432,15 +432,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -639,15 +639,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -846,15 +846,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -1050,15 +1050,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "dict(str, list[AccessMetadataValue])",
             400: "LusidValidationProblemDetails",
@@ -1276,15 +1276,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "LegalEntity",
             400: "LusidValidationProblemDetails",
@@ -1499,15 +1499,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "list[AccessMetadataValue]",
             400: "LusidValidationProblemDetails",
@@ -1746,15 +1746,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfPropertyInterval",
             400: "LusidValidationProblemDetails",
@@ -1979,15 +1979,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfRelationship",
             400: "LusidValidationProblemDetails",
@@ -2183,15 +2183,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfLegalEntity",
             400: "LusidValidationProblemDetails",
@@ -2433,15 +2433,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfLegalEntity",
             400: "LusidValidationProblemDetails",
@@ -2651,15 +2651,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "dict(str, list[AccessMetadataValue])",
             400: "LusidValidationProblemDetails",
@@ -2853,15 +2853,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "LegalEntity",
             400: "LusidValidationProblemDetails",
@@ -3055,15 +3055,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "LegalEntity",
             400: "LusidValidationProblemDetails",
@@ -3202,15 +3202,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "LegalEntity",
             400: "LusidValidationProblemDetails",
@@ -3439,15 +3439,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfAccessMetadataValueOf",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/orders_api.py` & `lusid-sdk-1.0.9/lusid/api/orders_api.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -182,15 +182,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -366,15 +366,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Order",
             400: "LusidValidationProblemDetails",
@@ -570,15 +570,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfOrder",
             400: "LusidValidationProblemDetails",
@@ -713,15 +713,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "ResourceListOfOrder",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/participations_api.py` & `lusid-sdk-1.0.9/lusid/api/participations_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -182,15 +182,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -366,15 +366,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Participation",
             400: "LusidValidationProblemDetails",
@@ -563,15 +563,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfParticipation",
             400: "LusidValidationProblemDetails",
@@ -706,15 +706,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "ResourceListOfParticipation",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/persons_api.py` & `lusid-sdk-1.0.9/lusid/api/persons_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -212,15 +212,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -419,15 +419,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -628,15 +628,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -837,15 +837,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -1025,15 +1025,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "dict(str, list[AccessMetadataValue])",
             400: "LusidValidationProblemDetails",
@@ -1229,15 +1229,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Person",
             400: "LusidValidationProblemDetails",
@@ -1430,15 +1430,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "list[AccessMetadataValue]",
             400: "LusidValidationProblemDetails",
@@ -1663,15 +1663,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfPropertyInterval",
             400: "LusidValidationProblemDetails",
@@ -1874,15 +1874,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfRelation",
             400: "LusidValidationProblemDetails",
@@ -2109,15 +2109,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfRelationship",
             400: "LusidValidationProblemDetails",
@@ -2313,15 +2313,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfPerson",
             400: "LusidValidationProblemDetails",
@@ -2546,15 +2546,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfPerson",
             400: "LusidValidationProblemDetails",
@@ -2748,15 +2748,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "dict(str, list[AccessMetadataValue])",
             400: "LusidValidationProblemDetails",
@@ -2936,15 +2936,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Person",
             400: "LusidValidationProblemDetails",
@@ -3124,15 +3124,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Person",
             400: "LusidValidationProblemDetails",
@@ -3271,15 +3271,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "Person",
             400: "LusidValidationProblemDetails",
@@ -3484,15 +3484,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfAccessMetadataValueOf",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/portfolio_groups_api.py` & `lusid-sdk-1.0.9/lusid/api/portfolio_groups_api.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -225,15 +225,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "PortfolioGroup",
             400: "LusidValidationProblemDetails",
@@ -421,15 +421,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "PortfolioGroup",
             400: "LusidValidationProblemDetails",
@@ -658,15 +658,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "VersionedResourceListOfOutputTransaction",
             400: "LusidValidationProblemDetails",
@@ -820,15 +820,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "PortfolioGroup",
             400: "LusidValidationProblemDetails",
@@ -1012,15 +1012,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -1214,15 +1214,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -1438,15 +1438,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PortfolioGroup",
             400: "LusidValidationProblemDetails",
@@ -1609,15 +1609,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -1817,15 +1817,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PortfolioGroup",
             400: "LusidValidationProblemDetails",
@@ -2054,15 +2054,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "VersionedResourceListOfA2BDataRecord",
             400: "LusidValidationProblemDetails",
@@ -2239,15 +2239,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PortfolioGroupProperties",
             400: "LusidValidationProblemDetails",
@@ -2454,15 +2454,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "VersionedResourceListOfPortfolioHolding",
             400: "LusidValidationProblemDetails",
@@ -2663,15 +2663,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PortfolioGroup",
             400: "LusidValidationProblemDetails",
@@ -2865,15 +2865,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "list[AccessMetadataValue]",
             400: "LusidValidationProblemDetails",
@@ -3065,15 +3065,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfProcessedCommand",
             400: "LusidValidationProblemDetails",
@@ -3266,15 +3266,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ExpandedGroup",
             400: "LusidValidationProblemDetails",
@@ -3451,15 +3451,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "dict(str, list[AccessMetadataValue])",
             400: "LusidValidationProblemDetails",
@@ -3688,15 +3688,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfPropertyInterval",
             400: "LusidValidationProblemDetails",
@@ -3904,15 +3904,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfRelationship",
             400: "LusidValidationProblemDetails",
@@ -4148,15 +4148,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "VersionedResourceListOfTransaction",
             400: "LusidValidationProblemDetails",
@@ -4353,15 +4353,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfPortfolioGroup",
             400: "LusidValidationProblemDetails",
@@ -4552,15 +4552,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "dict(str, list[AccessMetadataValue])",
             400: "LusidValidationProblemDetails",
@@ -4748,15 +4748,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PortfolioGroup",
             400: "LusidValidationProblemDetails",
@@ -4929,15 +4929,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PortfolioGroupProperties",
             400: "LusidValidationProblemDetails",
@@ -5145,15 +5145,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfAccessMetadataValueOf",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/portfolios_api.py` & `lusid-sdk-1.0.9/lusid/api/portfolios_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -231,15 +231,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -402,15 +402,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -592,15 +592,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -830,15 +830,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -1031,15 +1031,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Portfolio",
             400: "LusidValidationProblemDetails",
@@ -1237,15 +1237,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "AggregatedReturnsResponse",
             400: "LusidValidationProblemDetails",
@@ -1463,15 +1463,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfProcessedCommand",
             400: "LusidValidationProblemDetails",
@@ -1648,15 +1648,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "dict(str, list[AccessMetadataValue])",
             400: "LusidValidationProblemDetails",
@@ -1833,15 +1833,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PortfolioProperties",
             400: "LusidValidationProblemDetails",
@@ -2070,15 +2070,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfPropertyInterval",
             400: "LusidValidationProblemDetails",
@@ -2286,15 +2286,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfRelationship",
             400: "LusidValidationProblemDetails",
@@ -2523,15 +2523,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfPerformanceReturn",
             400: "LusidValidationProblemDetails",
@@ -2725,15 +2725,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "list[AccessMetadataValue]",
             400: "LusidValidationProblemDetails",
@@ -2944,15 +2944,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfProperty",
             400: "LusidValidationProblemDetails",
@@ -3170,15 +3170,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfPortfolio",
             400: "LusidValidationProblemDetails",
@@ -3400,15 +3400,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfPortfolio",
             400: "LusidValidationProblemDetails",
@@ -3585,15 +3585,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ActionResultOfPortfolio",
             400: "LusidValidationProblemDetails",
@@ -3784,15 +3784,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "dict(str, list[AccessMetadataValue])",
             400: "LusidValidationProblemDetails",
@@ -3976,15 +3976,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Portfolio",
             400: "LusidValidationProblemDetails",
@@ -4192,15 +4192,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfAccessMetadataValueOf",
             400: "LusidValidationProblemDetails",
@@ -4377,15 +4377,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PortfolioProperties",
             400: "LusidValidationProblemDetails",
@@ -4600,15 +4600,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "UpsertReturnsResponse",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/property_definitions_api.py` & `lusid-sdk-1.0.9/lusid/api/property_definitions_api.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -161,15 +161,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "PropertyDefinition",
             400: "LusidValidationProblemDetails",
@@ -308,15 +308,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "PropertyDefinition",
             400: "LusidValidationProblemDetails",
@@ -490,15 +490,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -657,15 +657,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfPropertyDefinition",
             400: "LusidValidationProblemDetails",
@@ -846,15 +846,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PropertyDefinition",
             400: "LusidValidationProblemDetails",
@@ -1042,15 +1042,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PropertyDefinition",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/quotes_api.py` & `lusid-sdk-1.0.9/lusid/api/quotes_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -177,15 +177,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "AnnulQuotesResponse",
             400: "LusidValidationProblemDetails",
@@ -360,15 +360,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "GetQuotesResponse",
             400: "LusidValidationProblemDetails",
@@ -563,15 +563,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfQuote",
             400: "LusidValidationProblemDetails",
@@ -766,15 +766,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfQuote",
             400: "LusidValidationProblemDetails",
@@ -928,15 +928,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "UpsertQuotesResponse",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/reconciliations_api.py` & `lusid-sdk-1.0.9/lusid/api/reconciliations_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -190,15 +190,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "str",
             400: "LusidValidationProblemDetails",
@@ -361,15 +361,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Mapping",
             400: "LusidValidationProblemDetails",
@@ -501,15 +501,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfMapping",
             400: "LusidValidationProblemDetails",
@@ -644,15 +644,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ReconciliationResponse",
             400: "LusidValidationProblemDetails",
@@ -824,15 +824,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfReconciliationBreak",
             400: "LusidValidationProblemDetails",
@@ -967,15 +967,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ListAggregationReconciliation",
             400: "LusidValidationProblemDetails",
@@ -1110,15 +1110,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "TransactionsReconciliationsResponse",
             400: "LusidValidationProblemDetails",
@@ -1253,15 +1253,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ListAggregationReconciliation",
             400: "LusidValidationProblemDetails",
@@ -1396,15 +1396,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Mapping",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/reference_portfolio_api.py` & `lusid-sdk-1.0.9/lusid/api/reference_portfolio_api.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -180,15 +180,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "Portfolio",
             400: "LusidValidationProblemDetails",
@@ -373,15 +373,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "GetReferencePortfolioConstituentsResponse",
             400: "LusidValidationProblemDetails",
@@ -573,15 +573,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfConstituentsAdjustmentHeader",
             400: "LusidValidationProblemDetails",
@@ -758,15 +758,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "UpsertReferencePortfolioConstituentsResponse",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/relationship_definitions_api.py` & `lusid-sdk-1.0.9/lusid/api/relationship_definitions_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -160,15 +160,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "RelationshipDefinition",
             400: "LusidValidationProblemDetails",
@@ -331,15 +331,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -509,15 +509,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "RelationshipDefinition",
             400: "LusidValidationProblemDetails",
@@ -686,15 +686,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfRelationshipDefinition",
             400: "LusidValidationProblemDetails",
@@ -871,15 +871,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "RelationshipDefinition",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/relationships_api.py` & `lusid-sdk-1.0.9/lusid/api/relationships_api.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -197,15 +197,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "CompleteRelationship",
             400: "LusidValidationProblemDetails",
@@ -382,15 +382,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/schemas_api.py` & `lusid-sdk-1.0.9/lusid/api/schemas_api.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -164,15 +164,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Schema",
             400: "LusidValidationProblemDetails",
@@ -312,15 +312,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PropertySchema",
             400: "LusidValidationProblemDetails",
@@ -467,15 +467,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfValueType",
             400: "LusidValidationProblemDetails",
@@ -600,15 +600,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfString",
         }
```

### Comparing `lusid-sdk-1.0.8/lusid/api/scopes_api.py` & `lusid-sdk-1.0.9/lusid/api/scopes_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -157,15 +157,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfScopeDefinition",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/search_api.py` & `lusid-sdk-1.0.9/lusid/api/search_api.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -189,15 +189,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "list[InstrumentMatch]",
             400: "LusidValidationProblemDetails",
@@ -381,15 +381,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfPortfolioGroupSearchResult",
             400: "LusidValidationProblemDetails",
@@ -573,15 +573,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfPortfolioSearchResult",
             400: "LusidValidationProblemDetails",
@@ -765,15 +765,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfPropertyDefinitionSearchResult",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/sequences_api.py` & `lusid-sdk-1.0.9/lusid/api/sequences_api.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -178,15 +178,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "SequenceDefinition",
             400: "LusidValidationProblemDetails",
@@ -349,15 +349,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "SequenceDefinition",
             400: "LusidValidationProblemDetails",
@@ -523,15 +523,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfSequenceDefinition",
             400: "LusidValidationProblemDetails",
@@ -705,15 +705,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "NextValueInSequenceResponse",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/system_configuration_api.py` & `lusid-sdk-1.0.9/lusid/api/system_configuration_api.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -153,15 +153,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             201: "TransactionSetConfigurationData",
             400: "LusidValidationProblemDetails",
@@ -293,15 +293,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "TransactionSetConfigurationData",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-1.0.8/lusid/api/transaction_portfolios_api.py` & `lusid-sdk-1.0.9/lusid/api/transaction_portfolios_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 00000000: 2320 636f 6469 6e67 3a20 7574 662d 380a  # coding: utf-8.
 00000010: 0a22 2222 0a20 2020 204c 5553 4944 2041  .""".    LUSID A
 00000020: 5049 0a0a 2020 2020 4649 4e42 4f55 524e  PI..    FINBOURN
 00000030: 4520 5465 6368 6e6f 6c6f 6779 2020 2320  E Technology  # 
 00000040: 6e6f 7161 3a20 4535 3031 0a0a 2020 2020  noqa: E501..    
 00000050: 5468 6520 7665 7273 696f 6e20 6f66 2074  The version of t
 00000060: 6865 204f 7065 6e41 5049 2064 6f63 756d  he OpenAPI docum
-00000070: 656e 743a 2031 2e30 2e38 0a20 2020 2043  ent: 1.0.8.    C
+00000070: 656e 743a 2031 2e30 2e39 0a20 2020 2043  ent: 1.0.9.    C
 00000080: 6f6e 7461 6374 3a20 696e 666f 4066 696e  ontact: info@fin
 00000090: 626f 7572 6e65 2e63 6f6d 0a20 2020 2047  bourne.com.    G
 000000a0: 656e 6572 6174 6564 2062 793a 2068 7474  enerated by: htt
 000000b0: 7073 3a2f 2f6f 7065 6e61 7069 2d67 656e  ps://openapi-gen
 000000c0: 6572 6174 6f72 2e74 6563 680a 2222 220a  erator.tech.""".
 000000d0: 0a0a 6672 6f6d 205f 5f66 7574 7572 655f  ..from __future_
 000000e0: 5f20 696d 706f 7274 2061 6273 6f6c 7574  _ import absolut
@@ -952,15 +952,15 @@
 00003b70: 6865 204c 5553 4944 2068 6561 6465 720a  he LUSID header.
 00003b80: 2020 2020 2020 2020 6865 6164 6572 5f70          header_p
 00003b90: 6172 616d 735b 2758 2d4c 5553 4944 2d53  arams['X-LUSID-S
 00003ba0: 444b 2d4c 616e 6775 6167 6527 5d20 3d20  DK-Language'] = 
 00003bb0: 2750 7974 686f 6e27 0a20 2020 2020 2020  'Python'.       
 00003bc0: 2068 6561 6465 725f 7061 7261 6d73 5b27   header_params['
 00003bd0: 582d 4c55 5349 442d 5344 4b2d 5665 7273  X-LUSID-SDK-Vers
-00003be0: 696f 6e27 5d20 3d20 2731 2e30 2e38 270a  ion'] = '1.0.8'.
+00003be0: 696f 6e27 5d20 3d20 2731 2e30 2e39 270a  ion'] = '1.0.9'.
 00003bf0: 0a20 2020 2020 2020 2023 2041 7574 6865  .        # Authe
 00003c00: 6e74 6963 6174 696f 6e20 7365 7474 696e  ntication settin
 00003c10: 670a 2020 2020 2020 2020 6175 7468 5f73  g.        auth_s
 00003c20: 6574 7469 6e67 7320 3d20 5b27 6f61 7574  ettings = ['oaut
 00003c30: 6832 275d 2020 2320 6e6f 7161 3a20 4535  h2']  # noqa: E5
 00003c40: 3031 0a0a 2020 2020 2020 2020 7265 7370  01..        resp
 00003c50: 6f6e 7365 5f74 7970 6573 5f6d 6170 203d  onse_types_map =
@@ -1862,15 +1862,15 @@
 00007450: 6572 0a20 2020 2020 2020 2068 6561 6465  er.        heade
 00007460: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 00007470: 442d 5344 4b2d 4c61 6e67 7561 6765 275d  D-SDK-Language']
 00007480: 203d 2027 5079 7468 6f6e 270a 2020 2020   = 'Python'.    
 00007490: 2020 2020 6865 6164 6572 5f70 6172 616d      header_param
 000074a0: 735b 2758 2d4c 5553 4944 2d53 444b 2d56  s['X-LUSID-SDK-V
 000074b0: 6572 7369 6f6e 275d 203d 2027 312e 302e  ersion'] = '1.0.
-000074c0: 3827 0a0a 2020 2020 2020 2020 2320 4175  8'..        # Au
+000074c0: 3927 0a0a 2020 2020 2020 2020 2320 4175  9'..        # Au
 000074d0: 7468 656e 7469 6361 7469 6f6e 2073 6574  thentication set
 000074e0: 7469 6e67 0a20 2020 2020 2020 2061 7574  ting.        aut
 000074f0: 685f 7365 7474 696e 6773 203d 205b 276f  h_settings = ['o
 00007500: 6175 7468 3227 5d20 2023 206e 6f71 613a  auth2']  # noqa:
 00007510: 2045 3530 310a 0a20 2020 2020 2020 2072   E501..        r
 00007520: 6573 706f 6e73 655f 7479 7065 735f 6d61  esponse_types_ma
 00007530: 7020 3d20 7b0a 2020 2020 2020 2020 2020  p = {.          
@@ -2709,15 +2709,15 @@
 0000a940: 2068 6561 6465 720a 2020 2020 2020 2020   header.        
 0000a950: 6865 6164 6572 5f70 6172 616d 735b 2758  header_params['X
 0000a960: 2d4c 5553 4944 2d53 444b 2d4c 616e 6775  -LUSID-SDK-Langu
 0000a970: 6167 6527 5d20 3d20 2750 7974 686f 6e27  age'] = 'Python'
 0000a980: 0a20 2020 2020 2020 2068 6561 6465 725f  .        header_
 0000a990: 7061 7261 6d73 5b27 582d 4c55 5349 442d  params['X-LUSID-
 0000a9a0: 5344 4b2d 5665 7273 696f 6e27 5d20 3d20  SDK-Version'] = 
-0000a9b0: 2731 2e30 2e38 270a 0a20 2020 2020 2020  '1.0.8'..       
+0000a9b0: 2731 2e30 2e39 270a 0a20 2020 2020 2020  '1.0.9'..       
 0000a9c0: 2023 2041 7574 6865 6e74 6963 6174 696f   # Authenticatio
 0000a9d0: 6e20 7365 7474 696e 670a 2020 2020 2020  n setting.      
 0000a9e0: 2020 6175 7468 5f73 6574 7469 6e67 7320    auth_settings 
 0000a9f0: 3d20 5b27 6f61 7574 6832 275d 2020 2320  = ['oauth2']  # 
 0000aa00: 6e6f 7161 3a20 4535 3031 0a0a 2020 2020  noqa: E501..    
 0000aa10: 2020 2020 7265 7370 6f6e 7365 5f74 7970      response_typ
 0000aa20: 6573 5f6d 6170 203d 207b 0a20 2020 2020  es_map = {.     
@@ -3765,15 +3765,15 @@
 0000eb40: 6572 0a20 2020 2020 2020 2068 6561 6465  er.        heade
 0000eb50: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 0000eb60: 442d 5344 4b2d 4c61 6e67 7561 6765 275d  D-SDK-Language']
 0000eb70: 203d 2027 5079 7468 6f6e 270a 2020 2020   = 'Python'.    
 0000eb80: 2020 2020 6865 6164 6572 5f70 6172 616d      header_param
 0000eb90: 735b 2758 2d4c 5553 4944 2d53 444b 2d56  s['X-LUSID-SDK-V
 0000eba0: 6572 7369 6f6e 275d 203d 2027 312e 302e  ersion'] = '1.0.
-0000ebb0: 3827 0a0a 2020 2020 2020 2020 2320 4175  8'..        # Au
+0000ebb0: 3927 0a0a 2020 2020 2020 2020 2320 4175  9'..        # Au
 0000ebc0: 7468 656e 7469 6361 7469 6f6e 2073 6574  thentication set
 0000ebd0: 7469 6e67 0a20 2020 2020 2020 2061 7574  ting.        aut
 0000ebe0: 685f 7365 7474 696e 6773 203d 205b 276f  h_settings = ['o
 0000ebf0: 6175 7468 3227 5d20 2023 206e 6f71 613a  auth2']  # noqa:
 0000ec00: 2045 3530 310a 0a20 2020 2020 2020 2072   E501..        r
 0000ec10: 6573 706f 6e73 655f 7479 7065 735f 6d61  esponse_types_ma
 0000ec20: 7020 3d20 7b0a 2020 2020 2020 2020 2020  p = {.          
@@ -4443,15 +4443,15 @@
 000115a0: 2074 6865 204c 5553 4944 2068 6561 6465   the LUSID heade
 000115b0: 720a 2020 2020 2020 2020 6865 6164 6572  r.        header
 000115c0: 5f70 6172 616d 735b 2758 2d4c 5553 4944  _params['X-LUSID
 000115d0: 2d53 444b 2d4c 616e 6775 6167 6527 5d20  -SDK-Language'] 
 000115e0: 3d20 2750 7974 686f 6e27 0a20 2020 2020  = 'Python'.     
 000115f0: 2020 2068 6561 6465 725f 7061 7261 6d73     header_params
 00011600: 5b27 582d 4c55 5349 442d 5344 4b2d 5665  ['X-LUSID-SDK-Ve
-00011610: 7273 696f 6e27 5d20 3d20 2731 2e30 2e38  rsion'] = '1.0.8
+00011610: 7273 696f 6e27 5d20 3d20 2731 2e30 2e39  rsion'] = '1.0.9
 00011620: 270a 0a20 2020 2020 2020 2023 2041 7574  '..        # Aut
 00011630: 6865 6e74 6963 6174 696f 6e20 7365 7474  hentication sett
 00011640: 696e 670a 2020 2020 2020 2020 6175 7468  ing.        auth
 00011650: 5f73 6574 7469 6e67 7320 3d20 5b27 6f61  _settings = ['oa
 00011660: 7574 6832 275d 2020 2320 6e6f 7161 3a20  uth2']  # noqa: 
 00011670: 4535 3031 0a0a 2020 2020 2020 2020 7265  E501..        re
 00011680: 7370 6f6e 7365 5f74 7970 6573 5f6d 6170  sponse_types_map
@@ -5102,15 +5102,15 @@
 00013ed0: 6572 0a20 2020 2020 2020 2068 6561 6465  er.        heade
 00013ee0: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 00013ef0: 442d 5344 4b2d 4c61 6e67 7561 6765 275d  D-SDK-Language']
 00013f00: 203d 2027 5079 7468 6f6e 270a 2020 2020   = 'Python'.    
 00013f10: 2020 2020 6865 6164 6572 5f70 6172 616d      header_param
 00013f20: 735b 2758 2d4c 5553 4944 2d53 444b 2d56  s['X-LUSID-SDK-V
 00013f30: 6572 7369 6f6e 275d 203d 2027 312e 302e  ersion'] = '1.0.
-00013f40: 3827 0a0a 2020 2020 2020 2020 2320 4175  8'..        # Au
+00013f40: 3927 0a0a 2020 2020 2020 2020 2320 4175  9'..        # Au
 00013f50: 7468 656e 7469 6361 7469 6f6e 2073 6574  thentication set
 00013f60: 7469 6e67 0a20 2020 2020 2020 2061 7574  ting.        aut
 00013f70: 685f 7365 7474 696e 6773 203d 205b 276f  h_settings = ['o
 00013f80: 6175 7468 3227 5d20 2023 206e 6f71 613a  auth2']  # noqa:
 00013f90: 2045 3530 310a 0a20 2020 2020 2020 2072   E501..        r
 00013fa0: 6573 706f 6e73 655f 7479 7065 735f 6d61  esponse_types_ma
 00013fb0: 7020 3d20 7b0a 2020 2020 2020 2020 2020  p = {.          
@@ -5661,15 +5661,15 @@
 000161c0: 6520 4c55 5349 4420 6865 6164 6572 0a20  e LUSID header. 
 000161d0: 2020 2020 2020 2068 6561 6465 725f 7061         header_pa
 000161e0: 7261 6d73 5b27 582d 4c55 5349 442d 5344  rams['X-LUSID-SD
 000161f0: 4b2d 4c61 6e67 7561 6765 275d 203d 2027  K-Language'] = '
 00016200: 5079 7468 6f6e 270a 2020 2020 2020 2020  Python'.        
 00016210: 6865 6164 6572 5f70 6172 616d 735b 2758  header_params['X
 00016220: 2d4c 5553 4944 2d53 444b 2d56 6572 7369  -LUSID-SDK-Versi
-00016230: 6f6e 275d 203d 2027 312e 302e 3827 0a0a  on'] = '1.0.8'..
+00016230: 6f6e 275d 203d 2027 312e 302e 3927 0a0a  on'] = '1.0.9'..
 00016240: 2020 2020 2020 2020 2320 4175 7468 656e          # Authen
 00016250: 7469 6361 7469 6f6e 2073 6574 7469 6e67  tication setting
 00016260: 0a20 2020 2020 2020 2061 7574 685f 7365  .        auth_se
 00016270: 7474 696e 6773 203d 205b 276f 6175 7468  ttings = ['oauth
 00016280: 3227 5d20 2023 206e 6f71 613a 2045 3530  2']  # noqa: E50
 00016290: 310a 0a20 2020 2020 2020 2072 6573 706f  1..        respo
 000162a0: 6e73 655f 7479 7065 735f 6d61 7020 3d20  nse_types_map = 
@@ -6418,15 +6418,15 @@
 00019110: 4420 6865 6164 6572 0a20 2020 2020 2020  D header.       
 00019120: 2068 6561 6465 725f 7061 7261 6d73 5b27   header_params['
 00019130: 582d 4c55 5349 442d 5344 4b2d 4c61 6e67  X-LUSID-SDK-Lang
 00019140: 7561 6765 275d 203d 2027 5079 7468 6f6e  uage'] = 'Python
 00019150: 270a 2020 2020 2020 2020 6865 6164 6572  '.        header
 00019160: 5f70 6172 616d 735b 2758 2d4c 5553 4944  _params['X-LUSID
 00019170: 2d53 444b 2d56 6572 7369 6f6e 275d 203d  -SDK-Version'] =
-00019180: 2027 312e 302e 3827 0a0a 2020 2020 2020   '1.0.8'..      
+00019180: 2027 312e 302e 3927 0a0a 2020 2020 2020   '1.0.9'..      
 00019190: 2020 2320 4175 7468 656e 7469 6361 7469    # Authenticati
 000191a0: 6f6e 2073 6574 7469 6e67 0a20 2020 2020  on setting.     
 000191b0: 2020 2061 7574 685f 7365 7474 696e 6773     auth_settings
 000191c0: 203d 205b 276f 6175 7468 3227 5d20 2023   = ['oauth2']  #
 000191d0: 206e 6f71 613a 2045 3530 310a 0a20 2020   noqa: E501..   
 000191e0: 2020 2020 2072 6573 706f 6e73 655f 7479       response_ty
 000191f0: 7065 735f 6d61 7020 3d20 7b0a 2020 2020  pes_map = {.    
@@ -7408,15 +7408,15 @@
 0001cef0: 4944 2068 6561 6465 720a 2020 2020 2020  ID header.      
 0001cf00: 2020 6865 6164 6572 5f70 6172 616d 735b    header_params[
 0001cf10: 2758 2d4c 5553 4944 2d53 444b 2d4c 616e  'X-LUSID-SDK-Lan
 0001cf20: 6775 6167 6527 5d20 3d20 2750 7974 686f  guage'] = 'Pytho
 0001cf30: 6e27 0a20 2020 2020 2020 2068 6561 6465  n'.        heade
 0001cf40: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 0001cf50: 442d 5344 4b2d 5665 7273 696f 6e27 5d20  D-SDK-Version'] 
-0001cf60: 3d20 2731 2e30 2e38 270a 0a20 2020 2020  = '1.0.8'..     
+0001cf60: 3d20 2731 2e30 2e39 270a 0a20 2020 2020  = '1.0.9'..     
 0001cf70: 2020 2023 2041 7574 6865 6e74 6963 6174     # Authenticat
 0001cf80: 696f 6e20 7365 7474 696e 670a 2020 2020  ion setting.    
 0001cf90: 2020 2020 6175 7468 5f73 6574 7469 6e67      auth_setting
 0001cfa0: 7320 3d20 5b27 6f61 7574 6832 275d 2020  s = ['oauth2']  
 0001cfb0: 2320 6e6f 7161 3a20 4535 3031 0a0a 2020  # noqa: E501..  
 0001cfc0: 2020 2020 2020 7265 7370 6f6e 7365 5f74        response_t
 0001cfd0: 7970 6573 5f6d 6170 203d 207b 0a20 2020  ypes_map = {.   
@@ -8415,15 +8415,15 @@
 00020de0: 5553 4944 2068 6561 6465 720a 2020 2020  USID header.    
 00020df0: 2020 2020 6865 6164 6572 5f70 6172 616d      header_param
 00020e00: 735b 2758 2d4c 5553 4944 2d53 444b 2d4c  s['X-LUSID-SDK-L
 00020e10: 616e 6775 6167 6527 5d20 3d20 2750 7974  anguage'] = 'Pyt
 00020e20: 686f 6e27 0a20 2020 2020 2020 2068 6561  hon'.        hea
 00020e30: 6465 725f 7061 7261 6d73 5b27 582d 4c55  der_params['X-LU
 00020e40: 5349 442d 5344 4b2d 5665 7273 696f 6e27  SID-SDK-Version'
-00020e50: 5d20 3d20 2731 2e30 2e38 270a 0a20 2020  ] = '1.0.8'..   
+00020e50: 5d20 3d20 2731 2e30 2e39 270a 0a20 2020  ] = '1.0.9'..   
 00020e60: 2020 2020 2023 2041 7574 6865 6e74 6963       # Authentic
 00020e70: 6174 696f 6e20 7365 7474 696e 670a 2020  ation setting.  
 00020e80: 2020 2020 2020 6175 7468 5f73 6574 7469        auth_setti
 00020e90: 6e67 7320 3d20 5b27 6f61 7574 6832 275d  ngs = ['oauth2']
 00020ea0: 2020 2320 6e6f 7161 3a20 4535 3031 0a0a    # noqa: E501..
 00020eb0: 2020 2020 2020 2020 7265 7370 6f6e 7365          response
 00020ec0: 5f74 7970 6573 5f6d 6170 203d 207b 0a20  _types_map = {. 
@@ -9081,15 +9081,15 @@
 00023780: 5553 4944 2068 6561 6465 720a 2020 2020  USID header.    
 00023790: 2020 2020 6865 6164 6572 5f70 6172 616d      header_param
 000237a0: 735b 2758 2d4c 5553 4944 2d53 444b 2d4c  s['X-LUSID-SDK-L
 000237b0: 616e 6775 6167 6527 5d20 3d20 2750 7974  anguage'] = 'Pyt
 000237c0: 686f 6e27 0a20 2020 2020 2020 2068 6561  hon'.        hea
 000237d0: 6465 725f 7061 7261 6d73 5b27 582d 4c55  der_params['X-LU
 000237e0: 5349 442d 5344 4b2d 5665 7273 696f 6e27  SID-SDK-Version'
-000237f0: 5d20 3d20 2731 2e30 2e38 270a 0a20 2020  ] = '1.0.8'..   
+000237f0: 5d20 3d20 2731 2e30 2e39 270a 0a20 2020  ] = '1.0.9'..   
 00023800: 2020 2020 2023 2041 7574 6865 6e74 6963       # Authentic
 00023810: 6174 696f 6e20 7365 7474 696e 670a 2020  ation setting.  
 00023820: 2020 2020 2020 6175 7468 5f73 6574 7469        auth_setti
 00023830: 6e67 7320 3d20 5b27 6f61 7574 6832 275d  ngs = ['oauth2']
 00023840: 2020 2320 6e6f 7161 3a20 4535 3031 0a0a    # noqa: E501..
 00023850: 2020 2020 2020 2020 7265 7370 6f6e 7365          response
 00023860: 5f74 7970 6573 5f6d 6170 203d 207b 0a20  _types_map = {. 
@@ -9958,15 +9958,15 @@
 00026e50: 6865 6164 6572 0a20 2020 2020 2020 2068  header.        h
 00026e60: 6561 6465 725f 7061 7261 6d73 5b27 582d  eader_params['X-
 00026e70: 4c55 5349 442d 5344 4b2d 4c61 6e67 7561  LUSID-SDK-Langua
 00026e80: 6765 275d 203d 2027 5079 7468 6f6e 270a  ge'] = 'Python'.
 00026e90: 2020 2020 2020 2020 6865 6164 6572 5f70          header_p
 00026ea0: 6172 616d 735b 2758 2d4c 5553 4944 2d53  arams['X-LUSID-S
 00026eb0: 444b 2d56 6572 7369 6f6e 275d 203d 2027  DK-Version'] = '
-00026ec0: 312e 302e 3827 0a0a 2020 2020 2020 2020  1.0.8'..        
+00026ec0: 312e 302e 3927 0a0a 2020 2020 2020 2020  1.0.9'..        
 00026ed0: 2320 4175 7468 656e 7469 6361 7469 6f6e  # Authentication
 00026ee0: 2073 6574 7469 6e67 0a20 2020 2020 2020   setting.       
 00026ef0: 2061 7574 685f 7365 7474 696e 6773 203d   auth_settings =
 00026f00: 205b 276f 6175 7468 3227 5d20 2023 206e   ['oauth2']  # n
 00026f10: 6f71 613a 2045 3530 310a 0a20 2020 2020  oqa: E501..     
 00026f20: 2020 2072 6573 706f 6e73 655f 7479 7065     response_type
 00026f30: 735f 6d61 7020 3d20 7b0a 2020 2020 2020  s_map = {.      
@@ -10731,15 +10731,15 @@
 00029ea0: 6520 4c55 5349 4420 6865 6164 6572 0a20  e LUSID header. 
 00029eb0: 2020 2020 2020 2068 6561 6465 725f 7061         header_pa
 00029ec0: 7261 6d73 5b27 582d 4c55 5349 442d 5344  rams['X-LUSID-SD
 00029ed0: 4b2d 4c61 6e67 7561 6765 275d 203d 2027  K-Language'] = '
 00029ee0: 5079 7468 6f6e 270a 2020 2020 2020 2020  Python'.        
 00029ef0: 6865 6164 6572 5f70 6172 616d 735b 2758  header_params['X
 00029f00: 2d4c 5553 4944 2d53 444b 2d56 6572 7369  -LUSID-SDK-Versi
-00029f10: 6f6e 275d 203d 2027 312e 302e 3827 0a0a  on'] = '1.0.8'..
+00029f10: 6f6e 275d 203d 2027 312e 302e 3927 0a0a  on'] = '1.0.9'..
 00029f20: 2020 2020 2020 2020 2320 4175 7468 656e          # Authen
 00029f30: 7469 6361 7469 6f6e 2073 6574 7469 6e67  tication setting
 00029f40: 0a20 2020 2020 2020 2061 7574 685f 7365  .        auth_se
 00029f50: 7474 696e 6773 203d 205b 276f 6175 7468  ttings = ['oauth
 00029f60: 3227 5d20 2023 206e 6f71 613a 2045 3530  2']  # noqa: E50
 00029f70: 310a 0a20 2020 2020 2020 2072 6573 706f  1..        respo
 00029f80: 6e73 655f 7479 7065 735f 6d61 7020 3d20  nse_types_map = 
@@ -11897,15 +11897,15 @@
 0002e780: 6561 6465 720a 2020 2020 2020 2020 6865  eader.        he
 0002e790: 6164 6572 5f70 6172 616d 735b 2758 2d4c  ader_params['X-L
 0002e7a0: 5553 4944 2d53 444b 2d4c 616e 6775 6167  USID-SDK-Languag
 0002e7b0: 6527 5d20 3d20 2750 7974 686f 6e27 0a20  e'] = 'Python'. 
 0002e7c0: 2020 2020 2020 2068 6561 6465 725f 7061         header_pa
 0002e7d0: 7261 6d73 5b27 582d 4c55 5349 442d 5344  rams['X-LUSID-SD
 0002e7e0: 4b2d 5665 7273 696f 6e27 5d20 3d20 2731  K-Version'] = '1
-0002e7f0: 2e30 2e38 270a 0a20 2020 2020 2020 2023  .0.8'..        #
+0002e7f0: 2e30 2e39 270a 0a20 2020 2020 2020 2023  .0.9'..        #
 0002e800: 2041 7574 6865 6e74 6963 6174 696f 6e20   Authentication 
 0002e810: 7365 7474 696e 670a 2020 2020 2020 2020  setting.        
 0002e820: 6175 7468 5f73 6574 7469 6e67 7320 3d20  auth_settings = 
 0002e830: 5b27 6f61 7574 6832 275d 2020 2320 6e6f  ['oauth2']  # no
 0002e840: 7161 3a20 4535 3031 0a0a 2020 2020 2020  qa: E501..      
 0002e850: 2020 7265 7370 6f6e 7365 5f74 7970 6573    response_types
 0002e860: 5f6d 6170 203d 207b 0a20 2020 2020 2020  _map = {.       
@@ -12868,15 +12868,15 @@
 00032430: 6520 4c55 5349 4420 6865 6164 6572 0a20  e LUSID header. 
 00032440: 2020 2020 2020 2068 6561 6465 725f 7061         header_pa
 00032450: 7261 6d73 5b27 582d 4c55 5349 442d 5344  rams['X-LUSID-SD
 00032460: 4b2d 4c61 6e67 7561 6765 275d 203d 2027  K-Language'] = '
 00032470: 5079 7468 6f6e 270a 2020 2020 2020 2020  Python'.        
 00032480: 6865 6164 6572 5f70 6172 616d 735b 2758  header_params['X
 00032490: 2d4c 5553 4944 2d53 444b 2d56 6572 7369  -LUSID-SDK-Versi
-000324a0: 6f6e 275d 203d 2027 312e 302e 3827 0a0a  on'] = '1.0.8'..
+000324a0: 6f6e 275d 203d 2027 312e 302e 3927 0a0a  on'] = '1.0.9'..
 000324b0: 2020 2020 2020 2020 2320 4175 7468 656e          # Authen
 000324c0: 7469 6361 7469 6f6e 2073 6574 7469 6e67  tication setting
 000324d0: 0a20 2020 2020 2020 2061 7574 685f 7365  .        auth_se
 000324e0: 7474 696e 6773 203d 205b 276f 6175 7468  ttings = ['oauth
 000324f0: 3227 5d20 2023 206e 6f71 613a 2045 3530  2']  # noqa: E50
 00032500: 310a 0a20 2020 2020 2020 2072 6573 706f  1..        respo
 00032510: 6e73 655f 7479 7065 735f 6d61 7020 3d20  nse_types_map = 
@@ -13562,15 +13562,15 @@
 00034f90: 6520 4c55 5349 4420 6865 6164 6572 0a20  e LUSID header. 
 00034fa0: 2020 2020 2020 2068 6561 6465 725f 7061         header_pa
 00034fb0: 7261 6d73 5b27 582d 4c55 5349 442d 5344  rams['X-LUSID-SD
 00034fc0: 4b2d 4c61 6e67 7561 6765 275d 203d 2027  K-Language'] = '
 00034fd0: 5079 7468 6f6e 270a 2020 2020 2020 2020  Python'.        
 00034fe0: 6865 6164 6572 5f70 6172 616d 735b 2758  header_params['X
 00034ff0: 2d4c 5553 4944 2d53 444b 2d56 6572 7369  -LUSID-SDK-Versi
-00035000: 6f6e 275d 203d 2027 312e 302e 3827 0a0a  on'] = '1.0.8'..
+00035000: 6f6e 275d 203d 2027 312e 302e 3927 0a0a  on'] = '1.0.9'..
 00035010: 2020 2020 2020 2020 2320 4175 7468 656e          # Authen
 00035020: 7469 6361 7469 6f6e 2073 6574 7469 6e67  tication setting
 00035030: 0a20 2020 2020 2020 2061 7574 685f 7365  .        auth_se
 00035040: 7474 696e 6773 203d 205b 276f 6175 7468  ttings = ['oauth
 00035050: 3227 5d20 2023 206e 6f71 613a 2045 3530  2']  # noqa: E50
 00035060: 310a 0a20 2020 2020 2020 2072 6573 706f  1..        respo
 00035070: 6e73 655f 7479 7065 735f 6d61 7020 3d20  nse_types_map = 
@@ -14709,15 +14709,15 @@
 00039740: 6561 6465 720a 2020 2020 2020 2020 6865  eader.        he
 00039750: 6164 6572 5f70 6172 616d 735b 2758 2d4c  ader_params['X-L
 00039760: 5553 4944 2d53 444b 2d4c 616e 6775 6167  USID-SDK-Languag
 00039770: 6527 5d20 3d20 2750 7974 686f 6e27 0a20  e'] = 'Python'. 
 00039780: 2020 2020 2020 2068 6561 6465 725f 7061         header_pa
 00039790: 7261 6d73 5b27 582d 4c55 5349 442d 5344  rams['X-LUSID-SD
 000397a0: 4b2d 5665 7273 696f 6e27 5d20 3d20 2731  K-Version'] = '1
-000397b0: 2e30 2e38 270a 0a20 2020 2020 2020 2023  .0.8'..        #
+000397b0: 2e30 2e39 270a 0a20 2020 2020 2020 2023  .0.9'..        #
 000397c0: 2041 7574 6865 6e74 6963 6174 696f 6e20   Authentication 
 000397d0: 7365 7474 696e 670a 2020 2020 2020 2020  setting.        
 000397e0: 6175 7468 5f73 6574 7469 6e67 7320 3d20  auth_settings = 
 000397f0: 5b27 6f61 7574 6832 275d 2020 2320 6e6f  ['oauth2']  # no
 00039800: 7161 3a20 4535 3031 0a0a 2020 2020 2020  qa: E501..      
 00039810: 2020 7265 7370 6f6e 7365 5f74 7970 6573    response_types
 00039820: 5f6d 6170 203d 207b 0a20 2020 2020 2020  _map = {.       
@@ -15447,15 +15447,15 @@
 0003c560: 6865 6164 6572 0a20 2020 2020 2020 2068  header.        h
 0003c570: 6561 6465 725f 7061 7261 6d73 5b27 582d  eader_params['X-
 0003c580: 4c55 5349 442d 5344 4b2d 4c61 6e67 7561  LUSID-SDK-Langua
 0003c590: 6765 275d 203d 2027 5079 7468 6f6e 270a  ge'] = 'Python'.
 0003c5a0: 2020 2020 2020 2020 6865 6164 6572 5f70          header_p
 0003c5b0: 6172 616d 735b 2758 2d4c 5553 4944 2d53  arams['X-LUSID-S
 0003c5c0: 444b 2d56 6572 7369 6f6e 275d 203d 2027  DK-Version'] = '
-0003c5d0: 312e 302e 3827 0a0a 2020 2020 2020 2020  1.0.8'..        
+0003c5d0: 312e 302e 3927 0a0a 2020 2020 2020 2020  1.0.9'..        
 0003c5e0: 2320 4175 7468 656e 7469 6361 7469 6f6e  # Authentication
 0003c5f0: 2073 6574 7469 6e67 0a20 2020 2020 2020   setting.       
 0003c600: 2061 7574 685f 7365 7474 696e 6773 203d   auth_settings =
 0003c610: 205b 276f 6175 7468 3227 5d20 2023 206e   ['oauth2']  # n
 0003c620: 6f71 613a 2045 3530 310a 0a20 2020 2020  oqa: E501..     
 0003c630: 2020 2072 6573 706f 6e73 655f 7479 7065     response_type
 0003c640: 735f 6d61 7020 3d20 7b0a 2020 2020 2020  s_map = {.      
@@ -16211,15 +16211,15 @@
 0003f520: 7468 6520 4c55 5349 4420 6865 6164 6572  the LUSID header
 0003f530: 0a20 2020 2020 2020 2068 6561 6465 725f  .        header_
 0003f540: 7061 7261 6d73 5b27 582d 4c55 5349 442d  params['X-LUSID-
 0003f550: 5344 4b2d 4c61 6e67 7561 6765 275d 203d  SDK-Language'] =
 0003f560: 2027 5079 7468 6f6e 270a 2020 2020 2020   'Python'.      
 0003f570: 2020 6865 6164 6572 5f70 6172 616d 735b    header_params[
 0003f580: 2758 2d4c 5553 4944 2d53 444b 2d56 6572  'X-LUSID-SDK-Ver
-0003f590: 7369 6f6e 275d 203d 2027 312e 302e 3827  sion'] = '1.0.8'
+0003f590: 7369 6f6e 275d 203d 2027 312e 302e 3927  sion'] = '1.0.9'
 0003f5a0: 0a0a 2020 2020 2020 2020 2320 4175 7468  ..        # Auth
 0003f5b0: 656e 7469 6361 7469 6f6e 2073 6574 7469  entication setti
 0003f5c0: 6e67 0a20 2020 2020 2020 2061 7574 685f  ng.        auth_
 0003f5d0: 7365 7474 696e 6773 203d 205b 276f 6175  settings = ['oau
 0003f5e0: 7468 3227 5d20 2023 206e 6f71 613a 2045  th2']  # noqa: E
 0003f5f0: 3530 310a 0a20 2020 2020 2020 2072 6573  501..        res
 0003f600: 706f 6e73 655f 7479 7065 735f 6d61 7020  ponse_types_map 
@@ -17123,15 +17123,15 @@
 00042e20: 6465 720a 2020 2020 2020 2020 6865 6164  der.        head
 00042e30: 6572 5f70 6172 616d 735b 2758 2d4c 5553  er_params['X-LUS
 00042e40: 4944 2d53 444b 2d4c 616e 6775 6167 6527  ID-SDK-Language'
 00042e50: 5d20 3d20 2750 7974 686f 6e27 0a20 2020  ] = 'Python'.   
 00042e60: 2020 2020 2068 6561 6465 725f 7061 7261       header_para
 00042e70: 6d73 5b27 582d 4c55 5349 442d 5344 4b2d  ms['X-LUSID-SDK-
 00042e80: 5665 7273 696f 6e27 5d20 3d20 2731 2e30  Version'] = '1.0
-00042e90: 2e38 270a 0a20 2020 2020 2020 2023 2041  .8'..        # A
+00042e90: 2e39 270a 0a20 2020 2020 2020 2023 2041  .9'..        # A
 00042ea0: 7574 6865 6e74 6963 6174 696f 6e20 7365  uthentication se
 00042eb0: 7474 696e 670a 2020 2020 2020 2020 6175  tting.        au
 00042ec0: 7468 5f73 6574 7469 6e67 7320 3d20 5b27  th_settings = ['
 00042ed0: 6f61 7574 6832 275d 2020 2320 6e6f 7161  oauth2']  # noqa
 00042ee0: 3a20 4535 3031 0a0a 2020 2020 2020 2020  : E501..        
 00042ef0: 7265 7370 6f6e 7365 5f74 7970 6573 5f6d  response_types_m
 00042f00: 6170 203d 207b 0a20 2020 2020 2020 2020  ap = {.         
@@ -17943,15 +17943,15 @@
 00046160: 6465 720a 2020 2020 2020 2020 6865 6164  der.        head
 00046170: 6572 5f70 6172 616d 735b 2758 2d4c 5553  er_params['X-LUS
 00046180: 4944 2d53 444b 2d4c 616e 6775 6167 6527  ID-SDK-Language'
 00046190: 5d20 3d20 2750 7974 686f 6e27 0a20 2020  ] = 'Python'.   
 000461a0: 2020 2020 2068 6561 6465 725f 7061 7261       header_para
 000461b0: 6d73 5b27 582d 4c55 5349 442d 5344 4b2d  ms['X-LUSID-SDK-
 000461c0: 5665 7273 696f 6e27 5d20 3d20 2731 2e30  Version'] = '1.0
-000461d0: 2e38 270a 0a20 2020 2020 2020 2023 2041  .8'..        # A
+000461d0: 2e39 270a 0a20 2020 2020 2020 2023 2041  .9'..        # A
 000461e0: 7574 6865 6e74 6963 6174 696f 6e20 7365  uthentication se
 000461f0: 7474 696e 670a 2020 2020 2020 2020 6175  tting.        au
 00046200: 7468 5f73 6574 7469 6e67 7320 3d20 5b27  th_settings = ['
 00046210: 6f61 7574 6832 275d 2020 2320 6e6f 7161  oauth2']  # noqa
 00046220: 3a20 4535 3031 0a0a 2020 2020 2020 2020  : E501..        
 00046230: 7265 7370 6f6e 7365 5f74 7970 6573 5f6d  response_types_m
 00046240: 6170 203d 207b 0a20 2020 2020 2020 2020  ap = {.         
@@ -18702,15 +18702,15 @@
 000490d0: 4420 6865 6164 6572 0a20 2020 2020 2020  D header.       
 000490e0: 2068 6561 6465 725f 7061 7261 6d73 5b27   header_params['
 000490f0: 582d 4c55 5349 442d 5344 4b2d 4c61 6e67  X-LUSID-SDK-Lang
 00049100: 7561 6765 275d 203d 2027 5079 7468 6f6e  uage'] = 'Python
 00049110: 270a 2020 2020 2020 2020 6865 6164 6572  '.        header
 00049120: 5f70 6172 616d 735b 2758 2d4c 5553 4944  _params['X-LUSID
 00049130: 2d53 444b 2d56 6572 7369 6f6e 275d 203d  -SDK-Version'] =
-00049140: 2027 312e 302e 3827 0a0a 2020 2020 2020   '1.0.8'..      
+00049140: 2027 312e 302e 3927 0a0a 2020 2020 2020   '1.0.9'..      
 00049150: 2020 2320 4175 7468 656e 7469 6361 7469    # Authenticati
 00049160: 6f6e 2073 6574 7469 6e67 0a20 2020 2020  on setting.     
 00049170: 2020 2061 7574 685f 7365 7474 696e 6773     auth_settings
 00049180: 203d 205b 276f 6175 7468 3227 5d20 2023   = ['oauth2']  #
 00049190: 206e 6f71 613a 2045 3530 310a 0a20 2020   noqa: E501..   
 000491a0: 2020 2020 2072 6573 706f 6e73 655f 7479       response_ty
 000491b0: 7065 735f 6d61 7020 3d20 7b0a 2020 2020  pes_map = {.    
@@ -19468,15 +19468,15 @@
 0004c0b0: 4944 2068 6561 6465 720a 2020 2020 2020  ID header.      
 0004c0c0: 2020 6865 6164 6572 5f70 6172 616d 735b    header_params[
 0004c0d0: 2758 2d4c 5553 4944 2d53 444b 2d4c 616e  'X-LUSID-SDK-Lan
 0004c0e0: 6775 6167 6527 5d20 3d20 2750 7974 686f  guage'] = 'Pytho
 0004c0f0: 6e27 0a20 2020 2020 2020 2068 6561 6465  n'.        heade
 0004c100: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 0004c110: 442d 5344 4b2d 5665 7273 696f 6e27 5d20  D-SDK-Version'] 
-0004c120: 3d20 2731 2e30 2e38 270a 0a20 2020 2020  = '1.0.8'..     
+0004c120: 3d20 2731 2e30 2e39 270a 0a20 2020 2020  = '1.0.9'..     
 0004c130: 2020 2023 2041 7574 6865 6e74 6963 6174     # Authenticat
 0004c140: 696f 6e20 7365 7474 696e 670a 2020 2020  ion setting.    
 0004c150: 2020 2020 6175 7468 5f73 6574 7469 6e67      auth_setting
 0004c160: 7320 3d20 5b27 6f61 7574 6832 275d 2020  s = ['oauth2']  
 0004c170: 2320 6e6f 7161 3a20 4535 3031 0a0a 2020  # noqa: E501..  
 0004c180: 2020 2020 2020 7265 7370 6f6e 7365 5f74        response_t
 0004c190: 7970 6573 5f6d 6170 203d 207b 0a20 2020  ypes_map = {.   
@@ -20162,15 +20162,15 @@
 0004ec10: 6520 4c55 5349 4420 6865 6164 6572 0a20  e LUSID header. 
 0004ec20: 2020 2020 2020 2068 6561 6465 725f 7061         header_pa
 0004ec30: 7261 6d73 5b27 582d 4c55 5349 442d 5344  rams['X-LUSID-SD
 0004ec40: 4b2d 4c61 6e67 7561 6765 275d 203d 2027  K-Language'] = '
 0004ec50: 5079 7468 6f6e 270a 2020 2020 2020 2020  Python'.        
 0004ec60: 6865 6164 6572 5f70 6172 616d 735b 2758  header_params['X
 0004ec70: 2d4c 5553 4944 2d53 444b 2d56 6572 7369  -LUSID-SDK-Versi
-0004ec80: 6f6e 275d 203d 2027 312e 302e 3827 0a0a  on'] = '1.0.8'..
+0004ec80: 6f6e 275d 203d 2027 312e 302e 3927 0a0a  on'] = '1.0.9'..
 0004ec90: 2020 2020 2020 2020 2320 4175 7468 656e          # Authen
 0004eca0: 7469 6361 7469 6f6e 2073 6574 7469 6e67  tication setting
 0004ecb0: 0a20 2020 2020 2020 2061 7574 685f 7365  .        auth_se
 0004ecc0: 7474 696e 6773 203d 205b 276f 6175 7468  ttings = ['oauth
 0004ecd0: 3227 5d20 2023 206e 6f71 613a 2045 3530  2']  # noqa: E50
 0004ece0: 310a 0a20 2020 2020 2020 2072 6573 706f  1..        respo
 0004ecf0: 6e73 655f 7479 7065 735f 6d61 7020 3d20  nse_types_map =
```

### Comparing `lusid-sdk-1.0.8/lusid/api_client.py` & `lusid-sdk-1.0.9/lusid/api_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # coding: utf-8
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 from __future__ import absolute_import
 
 import atexit
@@ -75,15 +75,15 @@
 
         self.rest_client = rest.RESTClientObject(configuration)
         self.default_headers = {}
         if header_name is not None:
             self.default_headers[header_name] = header_value
         self.cookie = cookie
         # Set default User-Agent.
-        self.user_agent = 'OpenAPI-Generator/1.0.8/python'
+        self.user_agent = 'OpenAPI-Generator/1.0.9/python'
         self.client_side_validation = configuration.client_side_validation
 
     def __enter__(self):
         return self
 
     def __exit__(self, exc_type, exc_value, traceback):
         self.close()
```

### Comparing `lusid-sdk-1.0.8/lusid/configuration.py` & `lusid-sdk-1.0.9/lusid/configuration.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -392,16 +392,16 @@
         """Gets the essential information for debugging.
 
         :return: The report for debugging.
         """
         return "Python SDK Debug Report:\n"\
                "OS: {env}\n"\
                "Python Version: {pyversion}\n"\
-               "Version of the API: 1.0.8\n"\
-               "SDK Package Version: 1.0.8".\
+               "Version of the API: 1.0.9\n"\
+               "SDK Package Version: 1.0.9".\
                format(env=sys.platform, pyversion=sys.version)
 
     def get_host_settings(self):
         """Gets an array of host settings
 
         :return: An array of host settings
         """
```

### Comparing `lusid-sdk-1.0.8/lusid/exceptions.py` & `lusid-sdk-1.0.9/lusid/exceptions.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 import six
```

### Comparing `lusid-sdk-1.0.8/lusid/models/__init__.py` & `lusid-sdk-1.0.9/lusid/models/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 # flake8: noqa
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
```

### Comparing `lusid-sdk-1.0.8/lusid/models/a2_b_breakdown.py` & `lusid-sdk-1.0.9/lusid/models/a2_b_breakdown.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/a2_b_category.py` & `lusid-sdk-1.0.9/lusid/models/a2_b_category.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/a2_b_data_record.py` & `lusid-sdk-1.0.9/lusid/models/a2_b_data_record.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/a2_b_movement_record.py` & `lusid-sdk-1.0.9/lusid/models/a2_b_movement_record.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/access_controlled_action.py` & `lusid-sdk-1.0.9/lusid/models/access_controlled_action.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/access_controlled_resource.py` & `lusid-sdk-1.0.9/lusid/models/access_controlled_resource.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/access_metadata_operation.py` & `lusid-sdk-1.0.9/lusid/models/access_metadata_operation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/access_metadata_value.py` & `lusid-sdk-1.0.9/lusid/models/access_metadata_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/action_id.py` & `lusid-sdk-1.0.9/lusid/models/action_id.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/action_result_of_portfolio.py` & `lusid-sdk-1.0.9/lusid/models/action_result_of_portfolio.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/add_business_days_to_date_request.py` & `lusid-sdk-1.0.9/lusid/models/add_business_days_to_date_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/add_business_days_to_date_response.py` & `lusid-sdk-1.0.9/lusid/models/add_business_days_to_date_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/address_definition.py` & `lusid-sdk-1.0.9/lusid/models/address_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/address_key_filter.py` & `lusid-sdk-1.0.9/lusid/models/address_key_filter.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/address_key_option_definition.py` & `lusid-sdk-1.0.9/lusid/models/address_key_option_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/adjust_holding.py` & `lusid-sdk-1.0.9/lusid/models/adjust_holding.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/adjust_holding_for_date_request.py` & `lusid-sdk-1.0.9/lusid/models/adjust_holding_for_date_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/adjust_holding_request.py` & `lusid-sdk-1.0.9/lusid/models/adjust_holding_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/aggregate_spec.py` & `lusid-sdk-1.0.9/lusid/models/aggregate_spec.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/aggregated_return.py` & `lusid-sdk-1.0.9/lusid/models/aggregated_return.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/aggregated_returns_request.py` & `lusid-sdk-1.0.9/lusid/models/aggregated_returns_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/aggregated_returns_response.py` & `lusid-sdk-1.0.9/lusid/models/aggregated_returns_response.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/aggregation.py` & `lusid-sdk-1.0.9/lusid/models/aggregation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/aggregation_context.py` & `lusid-sdk-1.0.9/lusid/models/aggregation_context.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/aggregation_measure_failure_detail.py` & `lusid-sdk-1.0.9/lusid/models/aggregation_measure_failure_detail.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/aggregation_options.py` & `lusid-sdk-1.0.9/lusid/models/aggregation_options.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/aggregation_query.py` & `lusid-sdk-1.0.9/lusid/models/aggregation_query.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/allocation.py` & `lusid-sdk-1.0.9/lusid/models/allocation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/allocation_request.py` & `lusid-sdk-1.0.9/lusid/models/allocation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/allocation_set_request.py` & `lusid-sdk-1.0.9/lusid/models/allocation_set_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/amortisation_event.py` & `lusid-sdk-1.0.9/lusid/models/amortisation_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/amortisation_event_all_of.py` & `lusid-sdk-1.0.9/lusid/models/amortisation_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/annul_quotes_response.py` & `lusid-sdk-1.0.9/lusid/models/annul_quotes_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/annul_single_structured_data_response.py` & `lusid-sdk-1.0.9/lusid/models/annul_single_structured_data_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/annul_structured_data_response.py` & `lusid-sdk-1.0.9/lusid/models/annul_structured_data_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/barrier.py` & `lusid-sdk-1.0.9/lusid/models/barrier.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/basket.py` & `lusid-sdk-1.0.9/lusid/models/basket.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/basket_all_of.py` & `lusid-sdk-1.0.9/lusid/models/basket_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/basket_identifier.py` & `lusid-sdk-1.0.9/lusid/models/basket_identifier.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/batch_adjust_holdings_response.py` & `lusid-sdk-1.0.9/lusid/models/batch_adjust_holdings_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/batch_upsert_portfolio_transactions_response.py` & `lusid-sdk-1.0.9/lusid/models/batch_upsert_portfolio_transactions_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/block.py` & `lusid-sdk-1.0.9/lusid/models/block.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/block_request.py` & `lusid-sdk-1.0.9/lusid/models/block_request.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/block_set_request.py` & `lusid-sdk-1.0.9/lusid/models/block_set_request.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/bond.py` & `lusid-sdk-1.0.9/lusid/models/bond.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/bond_all_of.py` & `lusid-sdk-1.0.9/lusid/models/bond_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/bond_default_event.py` & `lusid-sdk-1.0.9/lusid/models/bond_default_event.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/bond_default_event_all_of.py` & `lusid-sdk-1.0.9/lusid/models/bond_default_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/calendar.py` & `lusid-sdk-1.0.9/lusid/models/calendar.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/calendar_date.py` & `lusid-sdk-1.0.9/lusid/models/calendar_date.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cap_floor.py` & `lusid-sdk-1.0.9/lusid/models/cap_floor.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cap_floor_all_of.py` & `lusid-sdk-1.0.9/lusid/models/cap_floor_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cash_dividend_event.py` & `lusid-sdk-1.0.9/lusid/models/cash_dividend_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cash_dividend_event_all_of.py` & `lusid-sdk-1.0.9/lusid/models/cash_dividend_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cash_flow_event.py` & `lusid-sdk-1.0.9/lusid/models/cash_flow_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cash_flow_event_all_of.py` & `lusid-sdk-1.0.9/lusid/models/cash_flow_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cash_flow_lineage.py` & `lusid-sdk-1.0.9/lusid/models/cash_flow_lineage.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cash_flow_value.py` & `lusid-sdk-1.0.9/lusid/models/cash_flow_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cash_flow_value_all_of.py` & `lusid-sdk-1.0.9/lusid/models/cash_flow_value_all_of.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cash_flow_value_set.py` & `lusid-sdk-1.0.9/lusid/models/cash_flow_value_set.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cash_flow_value_set_all_of.py` & `lusid-sdk-1.0.9/lusid/models/cash_flow_value_set_all_of.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cash_ladder_record.py` & `lusid-sdk-1.0.9/lusid/models/cash_ladder_record.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cash_perpetual.py` & `lusid-sdk-1.0.9/lusid/models/cash_perpetual.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cash_perpetual_all_of.py` & `lusid-sdk-1.0.9/lusid/models/cash_perpetual_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cds_flow_conventions.py` & `lusid-sdk-1.0.9/lusid/models/cds_flow_conventions.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cds_index.py` & `lusid-sdk-1.0.9/lusid/models/cds_index.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cds_index_all_of.py` & `lusid-sdk-1.0.9/lusid/models/cds_index_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cds_protection_detail_specification.py` & `lusid-sdk-1.0.9/lusid/models/cds_protection_detail_specification.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/change.py` & `lusid-sdk-1.0.9/lusid/models/change.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/change_history.py` & `lusid-sdk-1.0.9/lusid/models/change_history.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/change_item.py` & `lusid-sdk-1.0.9/lusid/models/change_item.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/close_event.py` & `lusid-sdk-1.0.9/lusid/models/close_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/close_event_all_of.py` & `lusid-sdk-1.0.9/lusid/models/close_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/complete_portfolio.py` & `lusid-sdk-1.0.9/lusid/models/complete_portfolio.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/complete_relationship.py` & `lusid-sdk-1.0.9/lusid/models/complete_relationship.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/complex_bond.py` & `lusid-sdk-1.0.9/lusid/models/complex_bond.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/complex_bond_all_of.py` & `lusid-sdk-1.0.9/lusid/models/complex_bond_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/complex_market_data.py` & `lusid-sdk-1.0.9/lusid/models/complex_market_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/complex_market_data_id.py` & `lusid-sdk-1.0.9/lusid/models/complex_market_data_id.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/compounding.py` & `lusid-sdk-1.0.9/lusid/models/compounding.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/configuration_recipe.py` & `lusid-sdk-1.0.9/lusid/models/configuration_recipe.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/configuration_recipe_snippet.py` & `lusid-sdk-1.0.9/lusid/models/configuration_recipe_snippet.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/constituents_adjustment_header.py` & `lusid-sdk-1.0.9/lusid/models/constituents_adjustment_header.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/contract_for_difference.py` & `lusid-sdk-1.0.9/lusid/models/contract_for_difference.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/contract_for_difference_all_of.py` & `lusid-sdk-1.0.9/lusid/models/contract_for_difference_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/corporate_action.py` & `lusid-sdk-1.0.9/lusid/models/corporate_action.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/corporate_action_source.py` & `lusid-sdk-1.0.9/lusid/models/corporate_action_source.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/corporate_action_transition.py` & `lusid-sdk-1.0.9/lusid/models/corporate_action_transition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/corporate_action_transition_component.py` & `lusid-sdk-1.0.9/lusid/models/corporate_action_transition_component.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/corporate_action_transition_component_request.py` & `lusid-sdk-1.0.9/lusid/models/corporate_action_transition_component_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/corporate_action_transition_request.py` & `lusid-sdk-1.0.9/lusid/models/corporate_action_transition_request.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/counterparty_agreement.py` & `lusid-sdk-1.0.9/lusid/models/counterparty_agreement.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/counterparty_risk_information.py` & `lusid-sdk-1.0.9/lusid/models/counterparty_risk_information.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/counterparty_signatory.py` & `lusid-sdk-1.0.9/lusid/models/counterparty_signatory.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_calendar_request.py` & `lusid-sdk-1.0.9/lusid/models/create_calendar_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_corporate_action_source_request.py` & `lusid-sdk-1.0.9/lusid/models/create_corporate_action_source_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_cut_label_definition_request.py` & `lusid-sdk-1.0.9/lusid/models/create_cut_label_definition_request.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_data_type_request.py` & `lusid-sdk-1.0.9/lusid/models/create_data_type_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_date_request.py` & `lusid-sdk-1.0.9/lusid/models/create_date_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_derived_property_definition_request.py` & `lusid-sdk-1.0.9/lusid/models/create_derived_property_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_derived_transaction_portfolio_request.py` & `lusid-sdk-1.0.9/lusid/models/create_derived_transaction_portfolio_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_portfolio_details.py` & `lusid-sdk-1.0.9/lusid/models/create_portfolio_details.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_portfolio_group_request.py` & `lusid-sdk-1.0.9/lusid/models/create_portfolio_group_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_property_definition_request.py` & `lusid-sdk-1.0.9/lusid/models/create_property_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_reference_portfolio_request.py` & `lusid-sdk-1.0.9/lusid/models/create_reference_portfolio_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_relationship_definition_request.py` & `lusid-sdk-1.0.9/lusid/models/create_relationship_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_relationship_request.py` & `lusid-sdk-1.0.9/lusid/models/create_relationship_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_sequence_request.py` & `lusid-sdk-1.0.9/lusid/models/create_sequence_request.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_transaction_portfolio_request.py` & `lusid-sdk-1.0.9/lusid/models/create_transaction_portfolio_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/create_unit_definition.py` & `lusid-sdk-1.0.9/lusid/models/create_unit_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/credit_default_swap.py` & `lusid-sdk-1.0.9/lusid/models/credit_default_swap.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/credit_default_swap_all_of.py` & `lusid-sdk-1.0.9/lusid/models/credit_default_swap_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/credit_rating.py` & `lusid-sdk-1.0.9/lusid/models/credit_rating.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/credit_spread_curve_data.py` & `lusid-sdk-1.0.9/lusid/models/credit_spread_curve_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/credit_spread_curve_data_all_of.py` & `lusid-sdk-1.0.9/lusid/models/credit_spread_curve_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/credit_support_annex.py` & `lusid-sdk-1.0.9/lusid/models/credit_support_annex.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/currency_and_amount.py` & `lusid-sdk-1.0.9/lusid/models/currency_and_amount.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/custodian_account.py` & `lusid-sdk-1.0.9/lusid/models/custodian_account.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/custom_entity_definition.py` & `lusid-sdk-1.0.9/lusid/models/custom_entity_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/custom_entity_definition_request.py` & `lusid-sdk-1.0.9/lusid/models/custom_entity_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/custom_entity_field.py` & `lusid-sdk-1.0.9/lusid/models/custom_entity_field.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/custom_entity_field_definition.py` & `lusid-sdk-1.0.9/lusid/models/custom_entity_field_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/custom_entity_id.py` & `lusid-sdk-1.0.9/lusid/models/custom_entity_id.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/custom_entity_request.py` & `lusid-sdk-1.0.9/lusid/models/custom_entity_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/custom_entity_response.py` & `lusid-sdk-1.0.9/lusid/models/custom_entity_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cut_label_definition.py` & `lusid-sdk-1.0.9/lusid/models/cut_label_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/cut_local_time.py` & `lusid-sdk-1.0.9/lusid/models/cut_local_time.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/data_type.py` & `lusid-sdk-1.0.9/lusid/models/data_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/data_type_summary.py` & `lusid-sdk-1.0.9/lusid/models/data_type_summary.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/date_attributes.py` & `lusid-sdk-1.0.9/lusid/models/date_attributes.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/date_range.py` & `lusid-sdk-1.0.9/lusid/models/date_range.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/day_of_week.py` & `lusid-sdk-1.0.9/lusid/models/day_of_week.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/delete_instrument_properties_response.py` & `lusid-sdk-1.0.9/lusid/models/delete_instrument_properties_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/delete_instrument_response.py` & `lusid-sdk-1.0.9/lusid/models/delete_instrument_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/delete_instruments_response.py` & `lusid-sdk-1.0.9/lusid/models/delete_instruments_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/delete_relationship_request.py` & `lusid-sdk-1.0.9/lusid/models/delete_relationship_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/deleted_entity_response.py` & `lusid-sdk-1.0.9/lusid/models/deleted_entity_response.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/dependency_source_filter.py` & `lusid-sdk-1.0.9/lusid/models/dependency_source_filter.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/discount_factor_curve_data.py` & `lusid-sdk-1.0.9/lusid/models/discount_factor_curve_data.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/discount_factor_curve_data_all_of.py` & `lusid-sdk-1.0.9/lusid/models/discount_factor_curve_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/economic_dependency.py` & `lusid-sdk-1.0.9/lusid/models/economic_dependency.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/economic_dependency_with_complex_market_data.py` & `lusid-sdk-1.0.9/lusid/models/economic_dependency_with_complex_market_data.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/economic_dependency_with_quote.py` & `lusid-sdk-1.0.9/lusid/models/economic_dependency_with_quote.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/empty_model_options.py` & `lusid-sdk-1.0.9/lusid/models/empty_model_options.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/empty_model_options_all_of.py` & `lusid-sdk-1.0.9/lusid/models/empty_model_options_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/entity_identifier.py` & `lusid-sdk-1.0.9/lusid/models/entity_identifier.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/equity.py` & `lusid-sdk-1.0.9/lusid/models/equity.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/equity_all_of.py` & `lusid-sdk-1.0.9/lusid/models/equity_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/equity_all_of_identifiers.py` & `lusid-sdk-1.0.9/lusid/models/equity_all_of_identifiers.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/equity_curve_by_prices_data.py` & `lusid-sdk-1.0.9/lusid/models/equity_curve_by_prices_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/equity_curve_by_prices_data_all_of.py` & `lusid-sdk-1.0.9/lusid/models/equity_curve_by_prices_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/equity_model_options.py` & `lusid-sdk-1.0.9/lusid/models/equity_model_options.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/equity_model_options_all_of.py` & `lusid-sdk-1.0.9/lusid/models/equity_model_options_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/equity_option.py` & `lusid-sdk-1.0.9/lusid/models/equity_option.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/equity_option_all_of.py` & `lusid-sdk-1.0.9/lusid/models/equity_option_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/equity_swap.py` & `lusid-sdk-1.0.9/lusid/models/equity_swap.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/equity_swap_all_of.py` & `lusid-sdk-1.0.9/lusid/models/equity_swap_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/equity_vol_surface_data.py` & `lusid-sdk-1.0.9/lusid/models/equity_vol_surface_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/equity_vol_surface_data_all_of.py` & `lusid-sdk-1.0.9/lusid/models/equity_vol_surface_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/error_detail.py` & `lusid-sdk-1.0.9/lusid/models/error_detail.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/event_date_range.py` & `lusid-sdk-1.0.9/lusid/models/event_date_range.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/exchange_traded_option.py` & `lusid-sdk-1.0.9/lusid/models/exchange_traded_option.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/exchange_traded_option_all_of.py` & `lusid-sdk-1.0.9/lusid/models/exchange_traded_option_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/exchange_traded_option_contract_details.py` & `lusid-sdk-1.0.9/lusid/models/exchange_traded_option_contract_details.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/execution.py` & `lusid-sdk-1.0.9/lusid/models/execution.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/execution_request.py` & `lusid-sdk-1.0.9/lusid/models/execution_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/execution_set_request.py` & `lusid-sdk-1.0.9/lusid/models/execution_set_request.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/exercise_event.py` & `lusid-sdk-1.0.9/lusid/models/exercise_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/exercise_event_all_of.py` & `lusid-sdk-1.0.9/lusid/models/exercise_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/exotic_instrument.py` & `lusid-sdk-1.0.9/lusid/models/exotic_instrument.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/exotic_instrument_all_of.py` & `lusid-sdk-1.0.9/lusid/models/exotic_instrument_all_of.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/expanded_group.py` & `lusid-sdk-1.0.9/lusid/models/expanded_group.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/field_definition.py` & `lusid-sdk-1.0.9/lusid/models/field_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/field_schema.py` & `lusid-sdk-1.0.9/lusid/models/field_schema.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/field_value.py` & `lusid-sdk-1.0.9/lusid/models/field_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/file_response.py` & `lusid-sdk-1.0.9/lusid/models/file_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fixed_leg.py` & `lusid-sdk-1.0.9/lusid/models/fixed_leg.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fixed_leg_all_of.py` & `lusid-sdk-1.0.9/lusid/models/fixed_leg_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fixed_leg_all_of_overrides.py` & `lusid-sdk-1.0.9/lusid/models/fixed_leg_all_of_overrides.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/floating_leg.py` & `lusid-sdk-1.0.9/lusid/models/floating_leg.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/floating_leg_all_of.py` & `lusid-sdk-1.0.9/lusid/models/floating_leg_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/flow_convention_name.py` & `lusid-sdk-1.0.9/lusid/models/flow_convention_name.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/flow_conventions.py` & `lusid-sdk-1.0.9/lusid/models/flow_conventions.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/forward_rate_agreement.py` & `lusid-sdk-1.0.9/lusid/models/forward_rate_agreement.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/forward_rate_agreement_all_of.py` & `lusid-sdk-1.0.9/lusid/models/forward_rate_agreement_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/funding_leg.py` & `lusid-sdk-1.0.9/lusid/models/funding_leg.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/funding_leg_all_of.py` & `lusid-sdk-1.0.9/lusid/models/funding_leg_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/future.py` & `lusid-sdk-1.0.9/lusid/models/future.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/future_all_of.py` & `lusid-sdk-1.0.9/lusid/models/future_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/futures_contract_details.py` & `lusid-sdk-1.0.9/lusid/models/futures_contract_details.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_forward.py` & `lusid-sdk-1.0.9/lusid/models/fx_forward.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_forward_all_of.py` & `lusid-sdk-1.0.9/lusid/models/fx_forward_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_forward_curve_by_quote_reference.py` & `lusid-sdk-1.0.9/lusid/models/fx_forward_curve_by_quote_reference.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_forward_curve_by_quote_reference_all_of.py` & `lusid-sdk-1.0.9/lusid/models/fx_forward_curve_by_quote_reference_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_forward_curve_data.py` & `lusid-sdk-1.0.9/lusid/models/fx_forward_curve_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_forward_curve_data_all_of.py` & `lusid-sdk-1.0.9/lusid/models/fx_forward_curve_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_forward_model_options.py` & `lusid-sdk-1.0.9/lusid/models/fx_forward_model_options.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_forward_model_options_all_of.py` & `lusid-sdk-1.0.9/lusid/models/fx_forward_model_options_all_of.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_forward_pips_curve_data.py` & `lusid-sdk-1.0.9/lusid/models/fx_forward_pips_curve_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_forward_pips_curve_data_all_of.py` & `lusid-sdk-1.0.9/lusid/models/fx_forward_pips_curve_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_forward_tenor_curve_data.py` & `lusid-sdk-1.0.9/lusid/models/fx_forward_tenor_curve_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_forward_tenor_curve_data_all_of.py` & `lusid-sdk-1.0.9/lusid/models/fx_forward_tenor_curve_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_forward_tenor_pips_curve_data.py` & `lusid-sdk-1.0.9/lusid/models/fx_forward_tenor_pips_curve_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_forward_tenor_pips_curve_data_all_of.py` & `lusid-sdk-1.0.9/lusid/models/fx_forward_tenor_pips_curve_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_option.py` & `lusid-sdk-1.0.9/lusid/models/fx_option.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_option_all_of.py` & `lusid-sdk-1.0.9/lusid/models/fx_option_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_swap.py` & `lusid-sdk-1.0.9/lusid/models/fx_swap.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_swap_all_of.py` & `lusid-sdk-1.0.9/lusid/models/fx_swap_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/fx_vol_surface_data.py` & `lusid-sdk-1.0.9/lusid/models/fx_vol_surface_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/get_complex_market_data_response.py` & `lusid-sdk-1.0.9/lusid/models/get_complex_market_data_response.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/get_counterparty_agreement_response.py` & `lusid-sdk-1.0.9/lusid/models/get_counterparty_agreement_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/get_credit_support_annex_response.py` & `lusid-sdk-1.0.9/lusid/models/get_credit_support_annex_response.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/get_instruments_response.py` & `lusid-sdk-1.0.9/lusid/models/get_instruments_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/get_quotes_response.py` & `lusid-sdk-1.0.9/lusid/models/get_quotes_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/get_recipe_response.py` & `lusid-sdk-1.0.9/lusid/models/get_recipe_response.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/get_reference_portfolio_constituents_response.py` & `lusid-sdk-1.0.9/lusid/models/get_reference_portfolio_constituents_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/holding_adjustment.py` & `lusid-sdk-1.0.9/lusid/models/holding_adjustment.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/holding_adjustment_with_date.py` & `lusid-sdk-1.0.9/lusid/models/holding_adjustment_with_date.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/holding_context.py` & `lusid-sdk-1.0.9/lusid/models/holding_context.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/holdings_adjustment.py` & `lusid-sdk-1.0.9/lusid/models/holdings_adjustment.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/holdings_adjustment_header.py` & `lusid-sdk-1.0.9/lusid/models/holdings_adjustment_header.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/i_data_record.py` & `lusid-sdk-1.0.9/lusid/models/i_data_record.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/i_unit_definition_dto.py` & `lusid-sdk-1.0.9/lusid/models/i_unit_definition_dto.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/id_selector_definition.py` & `lusid-sdk-1.0.9/lusid/models/id_selector_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/identifier_part_schema.py` & `lusid-sdk-1.0.9/lusid/models/identifier_part_schema.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/index_convention.py` & `lusid-sdk-1.0.9/lusid/models/index_convention.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/index_model_options.py` & `lusid-sdk-1.0.9/lusid/models/index_model_options.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/index_model_options_all_of.py` & `lusid-sdk-1.0.9/lusid/models/index_model_options_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/industry_classifier.py` & `lusid-sdk-1.0.9/lusid/models/industry_classifier.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/inflation_linked_bond.py` & `lusid-sdk-1.0.9/lusid/models/inflation_linked_bond.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/inflation_linked_bond_all_of.py` & `lusid-sdk-1.0.9/lusid/models/inflation_linked_bond_all_of.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/inflation_swap.py` & `lusid-sdk-1.0.9/lusid/models/inflation_swap.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/inflation_swap_all_of.py` & `lusid-sdk-1.0.9/lusid/models/inflation_swap_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/informational_error_event.py` & `lusid-sdk-1.0.9/lusid/models/informational_error_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/informational_error_event_all_of.py` & `lusid-sdk-1.0.9/lusid/models/informational_error_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/informational_event.py` & `lusid-sdk-1.0.9/lusid/models/informational_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/informational_event_all_of.py` & `lusid-sdk-1.0.9/lusid/models/informational_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/inline_valuation_request.py` & `lusid-sdk-1.0.9/lusid/models/inline_valuation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/inline_valuations_reconciliation_request.py` & `lusid-sdk-1.0.9/lusid/models/inline_valuations_reconciliation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/input_transition.py` & `lusid-sdk-1.0.9/lusid/models/input_transition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/instrument.py` & `lusid-sdk-1.0.9/lusid/models/instrument.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/instrument_definition.py` & `lusid-sdk-1.0.9/lusid/models/instrument_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/instrument_definition_format.py` & `lusid-sdk-1.0.9/lusid/models/instrument_definition_format.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/instrument_event.py` & `lusid-sdk-1.0.9/lusid/models/instrument_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/instrument_event_holder.py` & `lusid-sdk-1.0.9/lusid/models/instrument_event_holder.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/instrument_id_type_descriptor.py` & `lusid-sdk-1.0.9/lusid/models/instrument_id_type_descriptor.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/instrument_id_value.py` & `lusid-sdk-1.0.9/lusid/models/instrument_id_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/instrument_leg.py` & `lusid-sdk-1.0.9/lusid/models/instrument_leg.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/instrument_leg_all_of.py` & `lusid-sdk-1.0.9/lusid/models/instrument_leg_all_of.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/instrument_match.py` & `lusid-sdk-1.0.9/lusid/models/instrument_match.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/instrument_properties.py` & `lusid-sdk-1.0.9/lusid/models/instrument_properties.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/instrument_search_property.py` & `lusid-sdk-1.0.9/lusid/models/instrument_search_property.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/interest_rate_swap.py` & `lusid-sdk-1.0.9/lusid/models/interest_rate_swap.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/interest_rate_swap_all_of.py` & `lusid-sdk-1.0.9/lusid/models/interest_rate_swap_all_of.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/interest_rate_swaption.py` & `lusid-sdk-1.0.9/lusid/models/interest_rate_swaption.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/interest_rate_swaption_all_of.py` & `lusid-sdk-1.0.9/lusid/models/interest_rate_swaption_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/ir_vol_cube_data.py` & `lusid-sdk-1.0.9/lusid/models/ir_vol_cube_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/ir_vol_cube_data_all_of.py` & `lusid-sdk-1.0.9/lusid/models/ir_vol_cube_data_all_of.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/is_business_day_response.py` & `lusid-sdk-1.0.9/lusid/models/is_business_day_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/label_value_set.py` & `lusid-sdk-1.0.9/lusid/models/label_value_set.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/leg_definition.py` & `lusid-sdk-1.0.9/lusid/models/leg_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/legal_entity.py` & `lusid-sdk-1.0.9/lusid/models/legal_entity.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/level_step.py` & `lusid-sdk-1.0.9/lusid/models/level_step.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/life_cycle_event_lineage.py` & `lusid-sdk-1.0.9/lusid/models/life_cycle_event_lineage.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/life_cycle_event_value.py` & `lusid-sdk-1.0.9/lusid/models/life_cycle_event_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/life_cycle_event_value_all_of.py` & `lusid-sdk-1.0.9/lusid/models/life_cycle_event_value_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/link.py` & `lusid-sdk-1.0.9/lusid/models/link.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/list_aggregation_reconciliation.py` & `lusid-sdk-1.0.9/lusid/models/list_aggregation_reconciliation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/list_aggregation_response.py` & `lusid-sdk-1.0.9/lusid/models/list_aggregation_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/lusid_instrument.py` & `lusid-sdk-1.0.9/lusid/models/lusid_instrument.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/lusid_problem_details.py` & `lusid-sdk-1.0.9/lusid/models/lusid_problem_details.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/lusid_unique_id.py` & `lusid-sdk-1.0.9/lusid/models/lusid_unique_id.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/lusid_validation_problem_details.py` & `lusid-sdk-1.0.9/lusid/models/lusid_validation_problem_details.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/mapped_string.py` & `lusid-sdk-1.0.9/lusid/models/mapped_string.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/mapping.py` & `lusid-sdk-1.0.9/lusid/models/mapping.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/mapping_rule.py` & `lusid-sdk-1.0.9/lusid/models/mapping_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/market_context.py` & `lusid-sdk-1.0.9/lusid/models/market_context.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/market_context_suppliers.py` & `lusid-sdk-1.0.9/lusid/models/market_context_suppliers.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/market_data_key_rule.py` & `lusid-sdk-1.0.9/lusid/models/market_data_key_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/market_data_overrides.py` & `lusid-sdk-1.0.9/lusid/models/market_data_overrides.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/market_data_specific_rule.py` & `lusid-sdk-1.0.9/lusid/models/market_data_specific_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/market_options.py` & `lusid-sdk-1.0.9/lusid/models/market_options.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/market_quote.py` & `lusid-sdk-1.0.9/lusid/models/market_quote.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/metric_value.py` & `lusid-sdk-1.0.9/lusid/models/metric_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/model_options.py` & `lusid-sdk-1.0.9/lusid/models/model_options.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/model_property.py` & `lusid-sdk-1.0.9/lusid/models/model_property.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/model_selection.py` & `lusid-sdk-1.0.9/lusid/models/model_selection.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/next_value_in_sequence_response.py` & `lusid-sdk-1.0.9/lusid/models/next_value_in_sequence_response.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/opaque_market_data.py` & `lusid-sdk-1.0.9/lusid/models/opaque_market_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/opaque_market_data_all_of.py` & `lusid-sdk-1.0.9/lusid/models/opaque_market_data_all_of.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/opaque_model_options.py` & `lusid-sdk-1.0.9/lusid/models/opaque_model_options.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/opaque_model_options_all_of.py` & `lusid-sdk-1.0.9/lusid/models/opaque_model_options_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/open_event.py` & `lusid-sdk-1.0.9/lusid/models/open_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/open_event_all_of.py` & `lusid-sdk-1.0.9/lusid/models/open_event_all_of.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/operation.py` & `lusid-sdk-1.0.9/lusid/models/operation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/order.py` & `lusid-sdk-1.0.9/lusid/models/order.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/order_by_spec.py` & `lusid-sdk-1.0.9/lusid/models/order_by_spec.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/order_request.py` & `lusid-sdk-1.0.9/lusid/models/order_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/order_set_request.py` & `lusid-sdk-1.0.9/lusid/models/order_set_request.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/otc_confirmation.py` & `lusid-sdk-1.0.9/lusid/models/otc_confirmation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/output_transaction.py` & `lusid-sdk-1.0.9/lusid/models/output_transaction.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/output_transition.py` & `lusid-sdk-1.0.9/lusid/models/output_transition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_allocation.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_allocation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_block.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_block.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_calendar.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_calendar.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_corporate_action_source.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_corporate_action_source.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_custom_entity_definition.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_custom_entity_definition.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_custom_entity_response.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_custom_entity_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_cut_label_definition.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_cut_label_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_data_type_summary.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_data_type_summary.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_execution.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_execution.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_instrument.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_instrument.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_instrument_event_holder.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_instrument_event_holder.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_legal_entity.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_legal_entity.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_order.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_order.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_participation.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_participation.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_person.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_person.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_portfolio_group_search_result.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_portfolio_group_search_result.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_portfolio_search_result.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_portfolio_search_result.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_property_definition_search_result.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_property_definition_search_result.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_relationship_definition.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_relationship_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/paged_resource_list_of_sequence_definition.py` & `lusid-sdk-1.0.9/lusid/models/paged_resource_list_of_sequence_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/participation.py` & `lusid-sdk-1.0.9/lusid/models/participation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/participation_request.py` & `lusid-sdk-1.0.9/lusid/models/participation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/participation_set_request.py` & `lusid-sdk-1.0.9/lusid/models/participation_set_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/performance_return.py` & `lusid-sdk-1.0.9/lusid/models/performance_return.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/performance_returns_metric.py` & `lusid-sdk-1.0.9/lusid/models/performance_returns_metric.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/perpetual_property.py` & `lusid-sdk-1.0.9/lusid/models/perpetual_property.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/person.py` & `lusid-sdk-1.0.9/lusid/models/person.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/portfolio.py` & `lusid-sdk-1.0.9/lusid/models/portfolio.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/portfolio_cash_flow.py` & `lusid-sdk-1.0.9/lusid/models/portfolio_cash_flow.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/portfolio_cash_ladder.py` & `lusid-sdk-1.0.9/lusid/models/portfolio_cash_ladder.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/portfolio_details.py` & `lusid-sdk-1.0.9/lusid/models/portfolio_details.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/portfolio_entity_id.py` & `lusid-sdk-1.0.9/lusid/models/portfolio_entity_id.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/portfolio_group.py` & `lusid-sdk-1.0.9/lusid/models/portfolio_group.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/portfolio_group_properties.py` & `lusid-sdk-1.0.9/lusid/models/portfolio_group_properties.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/portfolio_group_search_result.py` & `lusid-sdk-1.0.9/lusid/models/portfolio_group_search_result.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/portfolio_holding.py` & `lusid-sdk-1.0.9/lusid/models/portfolio_holding.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/portfolio_properties.py` & `lusid-sdk-1.0.9/lusid/models/portfolio_properties.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/portfolio_reconciliation_request.py` & `lusid-sdk-1.0.9/lusid/models/portfolio_reconciliation_request.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/portfolio_result_data_key_rule.py` & `lusid-sdk-1.0.9/lusid/models/portfolio_result_data_key_rule.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/portfolio_result_data_key_rule_all_of.py` & `lusid-sdk-1.0.9/lusid/models/portfolio_result_data_key_rule_all_of.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/portfolio_search_result.py` & `lusid-sdk-1.0.9/lusid/models/portfolio_search_result.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/portfolios_reconciliation_request.py` & `lusid-sdk-1.0.9/lusid/models/portfolios_reconciliation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/premium.py` & `lusid-sdk-1.0.9/lusid/models/premium.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/pricing_context.py` & `lusid-sdk-1.0.9/lusid/models/pricing_context.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/pricing_options.py` & `lusid-sdk-1.0.9/lusid/models/pricing_options.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/processed_command.py` & `lusid-sdk-1.0.9/lusid/models/processed_command.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/property_definition.py` & `lusid-sdk-1.0.9/lusid/models/property_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/property_definition_search_result.py` & `lusid-sdk-1.0.9/lusid/models/property_definition_search_result.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/property_filter.py` & `lusid-sdk-1.0.9/lusid/models/property_filter.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/property_interval.py` & `lusid-sdk-1.0.9/lusid/models/property_interval.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/property_schema.py` & `lusid-sdk-1.0.9/lusid/models/property_schema.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/property_value.py` & `lusid-sdk-1.0.9/lusid/models/property_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/quote.py` & `lusid-sdk-1.0.9/lusid/models/quote.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/quote_id.py` & `lusid-sdk-1.0.9/lusid/models/quote_id.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/quote_series_id.py` & `lusid-sdk-1.0.9/lusid/models/quote_series_id.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/raw_vendor_event.py` & `lusid-sdk-1.0.9/lusid/models/raw_vendor_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/raw_vendor_event_all_of.py` & `lusid-sdk-1.0.9/lusid/models/raw_vendor_event_all_of.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/realised_gain_loss.py` & `lusid-sdk-1.0.9/lusid/models/realised_gain_loss.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reconcile_date_time_rule.py` & `lusid-sdk-1.0.9/lusid/models/reconcile_date_time_rule.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reconcile_date_time_rule_all_of.py` & `lusid-sdk-1.0.9/lusid/models/reconcile_date_time_rule_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reconcile_numeric_rule.py` & `lusid-sdk-1.0.9/lusid/models/reconcile_numeric_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reconcile_numeric_rule_all_of.py` & `lusid-sdk-1.0.9/lusid/models/reconcile_numeric_rule_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reconcile_string_rule.py` & `lusid-sdk-1.0.9/lusid/models/reconcile_string_rule.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reconcile_string_rule_all_of.py` & `lusid-sdk-1.0.9/lusid/models/reconcile_string_rule_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reconciled_transaction.py` & `lusid-sdk-1.0.9/lusid/models/reconciled_transaction.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reconciliation_break.py` & `lusid-sdk-1.0.9/lusid/models/reconciliation_break.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reconciliation_left_right_address_key_pair.py` & `lusid-sdk-1.0.9/lusid/models/reconciliation_left_right_address_key_pair.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reconciliation_line.py` & `lusid-sdk-1.0.9/lusid/models/reconciliation_line.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reconciliation_request.py` & `lusid-sdk-1.0.9/lusid/models/reconciliation_request.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reconciliation_response.py` & `lusid-sdk-1.0.9/lusid/models/reconciliation_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reconciliation_rule.py` & `lusid-sdk-1.0.9/lusid/models/reconciliation_rule.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reference_data.py` & `lusid-sdk-1.0.9/lusid/models/reference_data.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reference_instrument.py` & `lusid-sdk-1.0.9/lusid/models/reference_instrument.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reference_instrument_all_of.py` & `lusid-sdk-1.0.9/lusid/models/reference_instrument_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reference_portfolio_constituent.py` & `lusid-sdk-1.0.9/lusid/models/reference_portfolio_constituent.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reference_portfolio_constituent_request.py` & `lusid-sdk-1.0.9/lusid/models/reference_portfolio_constituent_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/related_entity.py` & `lusid-sdk-1.0.9/lusid/models/related_entity.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/relation.py` & `lusid-sdk-1.0.9/lusid/models/relation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/relationship.py` & `lusid-sdk-1.0.9/lusid/models/relationship.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/relationship_definition.py` & `lusid-sdk-1.0.9/lusid/models/relationship_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/repo.py` & `lusid-sdk-1.0.9/lusid/models/repo.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/repo_all_of.py` & `lusid-sdk-1.0.9/lusid/models/repo_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reset_event.py` & `lusid-sdk-1.0.9/lusid/models/reset_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/reset_event_all_of.py` & `lusid-sdk-1.0.9/lusid/models/reset_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_id.py` & `lusid-sdk-1.0.9/lusid/models/resource_id.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_access_controlled_resource.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_access_controlled_resource.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_access_metadata_value_of.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_access_metadata_value_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_aggregation_query.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_aggregation_query.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_allocation.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_allocation.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_block.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_block.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_calendar_date.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_calendar_date.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_change.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_change.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_change_history.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_change_history.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_constituents_adjustment_header.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_constituents_adjustment_header.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_corporate_action.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_corporate_action.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_data_type.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_data_type.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_execution.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_execution.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_get_counterparty_agreement_response.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_get_counterparty_agreement_response.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_get_credit_support_annex_response.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_get_credit_support_annex_response.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_get_recipe_response.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_get_recipe_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_holdings_adjustment_header.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_holdings_adjustment_header.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_i_unit_definition_dto.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_i_unit_definition_dto.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_instrument_id_type_descriptor.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_instrument_id_type_descriptor.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_legal_entity.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_legal_entity.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_mapping.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_mapping.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_order.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_order.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_participation.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_participation.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_performance_return.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_performance_return.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_person.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_person.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_portfolio.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_portfolio.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_portfolio_cash_flow.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_portfolio_cash_flow.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_portfolio_cash_ladder.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_portfolio_cash_ladder.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_portfolio_group.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_portfolio_group.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_processed_command.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_processed_command.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_property.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_property.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_property_definition.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_property_definition.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_property_interval.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_property_interval.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_quote.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_quote.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_reconciliation_break.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_reconciliation_break.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_relation.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_relation.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_relationship.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_relationship.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_scope_definition.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_scope_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_string.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_string.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/resource_list_of_value_type.py` & `lusid-sdk-1.0.9/lusid/models/resource_list_of_value_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/response_meta_data.py` & `lusid-sdk-1.0.9/lusid/models/response_meta_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_data_key_rule.py` & `lusid-sdk-1.0.9/lusid/models/result_data_key_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_data_key_rule_all_of.py` & `lusid-sdk-1.0.9/lusid/models/result_data_key_rule_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_data_schema.py` & `lusid-sdk-1.0.9/lusid/models/result_data_schema.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_key_rule.py` & `lusid-sdk-1.0.9/lusid/models/result_key_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value.py` & `lusid-sdk-1.0.9/lusid/models/result_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value0_d.py` & `lusid-sdk-1.0.9/lusid/models/result_value0_d.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value0_d_all_of.py` & `lusid-sdk-1.0.9/lusid/models/result_value0_d_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value_bool.py` & `lusid-sdk-1.0.9/lusid/models/result_value_bool.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value_bool_all_of.py` & `lusid-sdk-1.0.9/lusid/models/result_value_bool_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value_currency.py` & `lusid-sdk-1.0.9/lusid/models/result_value_currency.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value_currency_all_of.py` & `lusid-sdk-1.0.9/lusid/models/result_value_currency_all_of.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value_date_time_offset.py` & `lusid-sdk-1.0.9/lusid/models/result_value_date_time_offset.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value_date_time_offset_all_of.py` & `lusid-sdk-1.0.9/lusid/models/result_value_date_time_offset_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value_decimal.py` & `lusid-sdk-1.0.9/lusid/models/result_value_decimal.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value_decimal_all_of.py` & `lusid-sdk-1.0.9/lusid/models/result_value_decimal_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value_dictionary.py` & `lusid-sdk-1.0.9/lusid/models/result_value_dictionary.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value_dictionary_all_of.py` & `lusid-sdk-1.0.9/lusid/models/result_value_dictionary_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value_int.py` & `lusid-sdk-1.0.9/lusid/models/result_value_int.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value_int_all_of.py` & `lusid-sdk-1.0.9/lusid/models/result_value_int_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value_string.py` & `lusid-sdk-1.0.9/lusid/models/result_value_string.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/result_value_string_all_of.py` & `lusid-sdk-1.0.9/lusid/models/result_value_string_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/schedule.py` & `lusid-sdk-1.0.9/lusid/models/schedule.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/schema.py` & `lusid-sdk-1.0.9/lusid/models/schema.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/scope_definition.py` & `lusid-sdk-1.0.9/lusid/models/scope_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/sequence_definition.py` & `lusid-sdk-1.0.9/lusid/models/sequence_definition.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/set_legal_entity_identifiers_request.py` & `lusid-sdk-1.0.9/lusid/models/set_legal_entity_identifiers_request.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/set_legal_entity_properties_request.py` & `lusid-sdk-1.0.9/lusid/models/set_legal_entity_properties_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/set_person_identifiers_request.py` & `lusid-sdk-1.0.9/lusid/models/set_person_identifiers_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/set_person_properties_request.py` & `lusid-sdk-1.0.9/lusid/models/set_person_properties_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/side_configuration_data.py` & `lusid-sdk-1.0.9/lusid/models/side_configuration_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/simple_instrument.py` & `lusid-sdk-1.0.9/lusid/models/simple_instrument.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/simple_instrument_all_of.py` & `lusid-sdk-1.0.9/lusid/models/simple_instrument_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/step_schedule.py` & `lusid-sdk-1.0.9/lusid/models/step_schedule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/step_schedule_all_of.py` & `lusid-sdk-1.0.9/lusid/models/step_schedule_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/stock_split_event.py` & `lusid-sdk-1.0.9/lusid/models/stock_split_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/stock_split_event_all_of.py` & `lusid-sdk-1.0.9/lusid/models/stock_split_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/stream.py` & `lusid-sdk-1.0.9/lusid/models/stream.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/supported_analytics_internal_request.py` & `lusid-sdk-1.0.9/lusid/models/supported_analytics_internal_request.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/target_tax_lot.py` & `lusid-sdk-1.0.9/lusid/models/target_tax_lot.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/target_tax_lot_request.py` & `lusid-sdk-1.0.9/lusid/models/target_tax_lot_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/term_deposit.py` & `lusid-sdk-1.0.9/lusid/models/term_deposit.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/term_deposit_all_of.py` & `lusid-sdk-1.0.9/lusid/models/term_deposit_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/touch.py` & `lusid-sdk-1.0.9/lusid/models/touch.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transaction.py` & `lusid-sdk-1.0.9/lusid/models/transaction.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transaction_configuration_data.py` & `lusid-sdk-1.0.9/lusid/models/transaction_configuration_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transaction_configuration_data_request.py` & `lusid-sdk-1.0.9/lusid/models/transaction_configuration_data_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transaction_configuration_movement_data.py` & `lusid-sdk-1.0.9/lusid/models/transaction_configuration_movement_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transaction_configuration_movement_data_request.py` & `lusid-sdk-1.0.9/lusid/models/transaction_configuration_movement_data_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transaction_configuration_type_alias.py` & `lusid-sdk-1.0.9/lusid/models/transaction_configuration_type_alias.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transaction_price.py` & `lusid-sdk-1.0.9/lusid/models/transaction_price.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transaction_property_mapping.py` & `lusid-sdk-1.0.9/lusid/models/transaction_property_mapping.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transaction_property_mapping_request.py` & `lusid-sdk-1.0.9/lusid/models/transaction_property_mapping_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transaction_query_parameters.py` & `lusid-sdk-1.0.9/lusid/models/transaction_query_parameters.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transaction_reconciliation_request.py` & `lusid-sdk-1.0.9/lusid/models/transaction_reconciliation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transaction_request.py` & `lusid-sdk-1.0.9/lusid/models/transaction_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transaction_set_configuration_data.py` & `lusid-sdk-1.0.9/lusid/models/transaction_set_configuration_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transactions_reconciliations_response.py` & `lusid-sdk-1.0.9/lusid/models/transactions_reconciliations_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transition_event.py` & `lusid-sdk-1.0.9/lusid/models/transition_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/transition_event_all_of.py` & `lusid-sdk-1.0.9/lusid/models/transition_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/trigger_event.py` & `lusid-sdk-1.0.9/lusid/models/trigger_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/trigger_event_all_of.py` & `lusid-sdk-1.0.9/lusid/models/trigger_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/typed_resource_id.py` & `lusid-sdk-1.0.9/lusid/models/typed_resource_id.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/update_calendar_request.py` & `lusid-sdk-1.0.9/lusid/models/update_calendar_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/update_custom_entity_definition_request.py` & `lusid-sdk-1.0.9/lusid/models/update_custom_entity_definition_request.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/update_cut_label_definition_request.py` & `lusid-sdk-1.0.9/lusid/models/update_cut_label_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/update_data_type_request.py` & `lusid-sdk-1.0.9/lusid/models/update_data_type_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/update_instrument_identifier_request.py` & `lusid-sdk-1.0.9/lusid/models/update_instrument_identifier_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/update_portfolio_group_request.py` & `lusid-sdk-1.0.9/lusid/models/update_portfolio_group_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/update_portfolio_request.py` & `lusid-sdk-1.0.9/lusid/models/update_portfolio_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/update_property_definition_request.py` & `lusid-sdk-1.0.9/lusid/models/update_property_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/update_relationship_definition_request.py` & `lusid-sdk-1.0.9/lusid/models/update_relationship_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/update_unit_request.py` & `lusid-sdk-1.0.9/lusid/models/update_unit_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_complex_market_data_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_complex_market_data_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_corporate_action_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_corporate_action_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_corporate_actions_response.py` & `lusid-sdk-1.0.9/lusid/models/upsert_corporate_actions_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_counterparty_agreement_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_counterparty_agreement_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_credit_support_annex_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_credit_support_annex_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_custom_entities_response.py` & `lusid-sdk-1.0.9/lusid/models/upsert_custom_entities_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_custom_entity_access_metadata_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_custom_entity_access_metadata_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_instrument_event_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_instrument_event_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_instrument_events_response.py` & `lusid-sdk-1.0.9/lusid/models/upsert_instrument_events_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_instrument_properties_response.py` & `lusid-sdk-1.0.9/lusid/models/upsert_instrument_properties_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_instrument_property_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_instrument_property_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_instruments_response.py` & `lusid-sdk-1.0.9/lusid/models/upsert_instruments_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_legal_entity_access_metadata_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_legal_entity_access_metadata_request.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_legal_entity_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_legal_entity_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_person_access_metadata_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_person_access_metadata_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_person_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_person_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_portfolio_access_metadata_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_portfolio_access_metadata_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_portfolio_group_access_metadata_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_portfolio_group_access_metadata_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_portfolio_transactions_response.py` & `lusid-sdk-1.0.9/lusid/models/upsert_portfolio_transactions_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_quote_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_quote_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_quotes_response.py` & `lusid-sdk-1.0.9/lusid/models/upsert_quotes_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_recipe_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_recipe_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_reference_portfolio_constituents_request.py` & `lusid-sdk-1.0.9/lusid/models/upsert_reference_portfolio_constituents_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_reference_portfolio_constituents_response.py` & `lusid-sdk-1.0.9/lusid/models/upsert_reference_portfolio_constituents_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_returns_response.py` & `lusid-sdk-1.0.9/lusid/models/upsert_returns_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_single_structured_data_response.py` & `lusid-sdk-1.0.9/lusid/models/upsert_single_structured_data_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_structured_data_response.py` & `lusid-sdk-1.0.9/lusid/models/upsert_structured_data_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/upsert_transaction_properties_response.py` & `lusid-sdk-1.0.9/lusid/models/upsert_transaction_properties_response.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/user.py` & `lusid-sdk-1.0.9/lusid/models/user.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/valuation_request.py` & `lusid-sdk-1.0.9/lusid/models/valuation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/valuation_schedule.py` & `lusid-sdk-1.0.9/lusid/models/valuation_schedule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/valuations_reconciliation_request.py` & `lusid-sdk-1.0.9/lusid/models/valuations_reconciliation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/value_type.py` & `lusid-sdk-1.0.9/lusid/models/value_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/vendor_model_rule.py` & `lusid-sdk-1.0.9/lusid/models/vendor_model_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/version.py` & `lusid-sdk-1.0.9/lusid/models/version.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/version_summary_dto.py` & `lusid-sdk-1.0.9/lusid/models/version_summary_dto.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/versioned_resource_list_of_a2_b_data_record.py` & `lusid-sdk-1.0.9/lusid/models/versioned_resource_list_of_a2_b_data_record.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/versioned_resource_list_of_a2_b_movement_record.py` & `lusid-sdk-1.0.9/lusid/models/versioned_resource_list_of_a2_b_movement_record.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/versioned_resource_list_of_output_transaction.py` & `lusid-sdk-1.0.9/lusid/models/versioned_resource_list_of_output_transaction.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/versioned_resource_list_of_portfolio_holding.py` & `lusid-sdk-1.0.9/lusid/models/versioned_resource_list_of_portfolio_holding.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/versioned_resource_list_of_transaction.py` & `lusid-sdk-1.0.9/lusid/models/versioned_resource_list_of_transaction.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/weekend_mask.py` & `lusid-sdk-1.0.9/lusid/models/weekend_mask.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/weighted_instrument.py` & `lusid-sdk-1.0.9/lusid/models/weighted_instrument.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/weighted_instruments.py` & `lusid-sdk-1.0.9/lusid/models/weighted_instruments.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/yield_curve_data.py` & `lusid-sdk-1.0.9/lusid/models/yield_curve_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/models/yield_curve_data_all_of.py` & `lusid-sdk-1.0.9/lusid/models/yield_curve_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-1.0.8/lusid/rest.py` & `lusid-sdk-1.0.9/lusid/rest.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
```

### Comparing `lusid-sdk-1.0.8/lusid/tcp/tcp_keep_alive_probes.py` & `lusid-sdk-1.0.9/lusid/tcp/tcp_keep_alive_probes.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-1.0.8/lusid/utilities/api_client_builder.py` & `lusid-sdk-1.0.9/lusid/utilities/api_client_builder.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-1.0.8/lusid/utilities/api_client_factory.py` & `lusid-sdk-1.0.9/lusid/utilities/api_client_factory.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-1.0.8/lusid/utilities/api_configuration.py` & `lusid-sdk-1.0.9/lusid/utilities/api_configuration.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-1.0.8/lusid/utilities/api_configuration_loader.py` & `lusid-sdk-1.0.9/lusid/utilities/api_configuration_loader.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-1.0.8/lusid/utilities/config_keys.json` & `lusid-sdk-1.0.9/lusid/utilities/config_keys.json`

 * *Files identical despite different names*

### Comparing `lusid-sdk-1.0.8/lusid/utilities/lusid_retry.py` & `lusid-sdk-1.0.9/lusid/utilities/lusid_retry.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-1.0.8/lusid/utilities/proxy_config.py` & `lusid-sdk-1.0.9/lusid/utilities/proxy_config.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-1.0.8/lusid/utilities/refreshing_token.py` & `lusid-sdk-1.0.9/lusid/utilities/refreshing_token.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-1.0.8/lusid_sdk.egg-info/SOURCES.txt` & `lusid-sdk-1.0.9/lusid_sdk.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `lusid-sdk-1.0.8/setup.py` & `lusid-sdk-1.0.9/setup.py`

 * *Files identical despite different names*

