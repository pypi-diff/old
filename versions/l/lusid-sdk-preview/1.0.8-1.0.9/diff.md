# Comparing `tmp/lusid-sdk-preview-1.0.8.tar.gz` & `tmp/lusid-sdk-preview-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/lusid-sdk-preview-1.0.8.tar", last modified: Thu Mar 16 22:15:02 2023, max compression
+gzip compressed data, was "dist/lusid-sdk-preview-1.0.9.tar", last modified: Thu Mar 16 22:59:44 2023, max compression
```

## Comparing `lusid-sdk-preview-1.0.8.tar` & `lusid-sdk-preview-1.0.9.tar`

### file list

```diff
@@ -1,871 +1,871 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:15:02.783485 lusid-sdk-preview-1.0.8/
--rw-r--r--   0 root         (0) root         (0)       40 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      356 2023-03-16 22:15:02.783485 lusid-sdk-preview-1.0.8/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)   135821 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:15:02.696485 lusid-sdk-preview-1.0.8/lusid/
--rw-r--r--   0 root         (0) root         (0)    60804 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/__init__.py
--rw-r--r--   0 root         (0) root         (0)       22 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/__version__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:15:02.704486 lusid-sdk-preview-1.0.8/lusid/api/
--rw-r--r--   0 root         (0) root         (0)     3141 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/__init__.py
--rw-r--r--   0 root         (0) root         (0)    67980 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/abor_api.py
--rw-r--r--   0 root         (0) root         (0)    57048 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/abor_configuration_api.py
--rw-r--r--   0 root         (0) root         (0)    41843 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/aggregation_api.py
--rw-r--r--   0 root         (0) root         (0)    39961 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/allocations_api.py
--rw-r--r--   0 root         (0) root         (0)    21666 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/application_metadata_api.py
--rw-r--r--   0 root         (0) root         (0)    38741 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/blocks_api.py
--rw-r--r--   0 root         (0) root         (0)   128574 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/calendars_api.py
--rw-r--r--   0 root         (0) root         (0)   123254 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/chart_of_accounts_api.py
--rw-r--r--   0 root         (0) root         (0)    43662 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/complex_market_data_api.py
--rw-r--r--   0 root         (0) root         (0)    89888 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/compliance_api.py
--rw-r--r--   0 root         (0) root         (0)    37217 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/configuration_recipe_api.py
--rw-r--r--   0 root         (0) root         (0)   104789 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/conventions_api.py
--rw-r--r--   0 root         (0) root         (0)   102508 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/corporate_action_sources_api.py
--rw-r--r--   0 root         (0) root         (0)    71069 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/counterparties_api.py
--rw-r--r--   0 root         (0) root         (0)   177505 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/custom_entities_api.py
--rw-r--r--   0 root         (0) root         (0)    36859 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/custom_entity_definitions_api.py
--rw-r--r--   0 root         (0) root         (0)    42656 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/cut_label_definitions_api.py
--rw-r--r--   0 root         (0) root         (0)    74817 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/data_types_api.py
--rw-r--r--   0 root         (0) root         (0)    21097 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/derived_transaction_portfolios_api.py
--rw-r--r--   0 root         (0) root         (0)    11461 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/entities_api.py
--rw-r--r--   0 root         (0) root         (0)    39311 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/executions_api.py
--rw-r--r--   0 root         (0) root         (0)    36340 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/instrument_events_api.py
--rw-r--r--   0 root         (0) root         (0)   228924 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/instruments_api.py
--rw-r--r--   0 root         (0) root         (0)   254636 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/legal_entities_api.py
--rw-r--r--   0 root         (0) root         (0)    25684 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/order_graph_api.py
--rw-r--r--   0 root         (0) root         (0)    40371 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/order_instructions_api.py
--rw-r--r--   0 root         (0) root         (0)    39234 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/orders_api.py
--rw-r--r--   0 root         (0) root         (0)    39027 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/packages_api.py
--rw-r--r--   0 root         (0) root         (0)    39885 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/participations_api.py
--rw-r--r--   0 root         (0) root         (0)   223041 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/persons_api.py
--rw-r--r--   0 root         (0) root         (0)    39313 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/placements_api.py
--rw-r--r--   0 root         (0) root         (0)   352873 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/portfolio_groups_api.py
--rw-r--r--   0 root         (0) root         (0)   331977 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/portfolios_api.py
--rw-r--r--   0 root         (0) root         (0)    58891 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/property_definitions_api.py
--rw-r--r--   0 root         (0) root         (0)   102292 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/quotes_api.py
--rw-r--r--   0 root         (0) root         (0)    70602 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/reconciliations_api.py
--rw-r--r--   0 root         (0) root         (0)    46619 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/reference_portfolio_api.py
--rw-r--r--   0 root         (0) root         (0)    27926 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/relation_definitions_api.py
--rw-r--r--   0 root         (0) root         (0)    23551 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/relations_api.py
--rw-r--r--   0 root         (0) root         (0)    51157 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/relationship_definitions_api.py
--rw-r--r--   0 root         (0) root         (0)    22583 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/relationships_api.py
--rw-r--r--   0 root         (0) root         (0)    27642 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/schemas_api.py
--rw-r--r--   0 root         (0) root         (0)     8323 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/scopes_api.py
--rw-r--r--   0 root         (0) root         (0)    48095 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/search_api.py
--rw-r--r--   0 root         (0) root         (0)    39247 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/sequences_api.py
--rw-r--r--   0 root         (0) root         (0)    75616 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/structured_result_data_api.py
--rw-r--r--   0 root         (0) root         (0)    55507 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/system_configuration_api.py
--rw-r--r--   0 root         (0) root         (0)    48105 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/tax_rule_sets_api.py
--rw-r--r--   0 root         (0) root         (0)    47798 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/transaction_configuration_api.py
--rw-r--r--   0 root         (0) root         (0)    53858 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/transaction_fees_api.py
--rw-r--r--   0 root         (0) root         (0)   516747 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/transaction_portfolios_api.py
--rw-r--r--   0 root         (0) root         (0)    18228 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api/translation_api.py
--rw-r--r--   0 root         (0) root         (0)    27344 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/api_client.py
--rw-r--r--   0 root         (0) root         (0)    16563 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/configuration.py
--rw-r--r--   0 root         (0) root         (0)     5079 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/exceptions.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:15:02.781485 lusid-sdk-preview-1.0.8/lusid/models/
--rw-r--r--   0 root         (0) root         (0)    56960 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/__init__.py
--rw-r--r--   0 root         (0) root         (0)     6340 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/a2_b_breakdown.py
--rw-r--r--   0 root         (0) root         (0)     5185 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/a2_b_category.py
--rw-r--r--   0 root         (0) root         (0)    17994 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/a2_b_data_record.py
--rw-r--r--   0 root         (0) root         (0)    21249 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/a2_b_movement_record.py
--rw-r--r--   0 root         (0) root         (0)    10451 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/abor.py
--rw-r--r--   0 root         (0) root         (0)    11319 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/abor_configuration.py
--rw-r--r--   0 root         (0) root         (0)     7071 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/abor_configuration_properties.py
--rw-r--r--   0 root         (0) root         (0)    10944 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/abor_configuration_request.py
--rw-r--r--   0 root         (0) root         (0)     6733 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/abor_properties.py
--rw-r--r--   0 root         (0) root         (0)     9860 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/abor_request.py
--rw-r--r--   0 root         (0) root         (0)     7104 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/access_controlled_action.py
--rw-r--r--   0 root         (0) root         (0)     8867 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/access_controlled_resource.py
--rw-r--r--   0 root         (0) root         (0)     8023 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/access_metadata_operation.py
--rw-r--r--   0 root         (0) root         (0)     5784 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/access_metadata_value.py
--rw-r--r--   0 root         (0) root         (0)    11977 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/account.py
--rw-r--r--   0 root         (0) root         (0)     6811 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/account_properties.py
--rw-r--r--   0 root         (0) root         (0)     3558 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/accounting_method.py
--rw-r--r--   0 root         (0) root         (0)     6743 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/accounts_upsert_response.py
--rw-r--r--   0 root         (0) root         (0)     7198 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/action_id.py
--rw-r--r--   0 root         (0) root         (0)     4725 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/action_result_of_portfolio.py
--rw-r--r--   0 root         (0) root         (0)     7222 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/add_business_days_to_date_request.py
--rw-r--r--   0 root         (0) root         (0)     4157 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/add_business_days_to_date_response.py
--rw-r--r--   0 root         (0) root         (0)    10980 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/address_definition.py
--rw-r--r--   0 root         (0) root         (0)     6118 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/address_key_filter.py
--rw-r--r--   0 root         (0) root         (0)     9172 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/address_key_option_definition.py
--rw-r--r--   0 root         (0) root         (0)     6832 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/adjust_holding.py
--rw-r--r--   0 root         (0) root         (0)    12008 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/adjust_holding_for_date_request.py
--rw-r--r--   0 root         (0) root         (0)    10262 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/adjust_holding_request.py
--rw-r--r--   0 root         (0) root         (0)     7500 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/aggregate_spec.py
--rw-r--r--   0 root         (0) root         (0)    13024 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/aggregated_return.py
--rw-r--r--   0 root         (0) root         (0)    13772 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/aggregated_returns_request.py
--rw-r--r--   0 root         (0) root         (0)     6028 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/aggregated_returns_response.py
--rw-r--r--   0 root         (0) root         (0)    10298 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/aggregation.py
--rw-r--r--   0 root         (0) root         (0)     4009 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/aggregation_context.py
--rw-r--r--   0 root         (0) root         (0)     7085 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/aggregation_measure_failure_detail.py
--rw-r--r--   0 root         (0) root         (0)     3885 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/aggregation_op.py
--rw-r--r--   0 root         (0) root         (0)     8775 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/aggregation_options.py
--rw-r--r--   0 root         (0) root         (0)    25169 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/aggregation_query.py
--rw-r--r--   0 root         (0) root         (0)     3506 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/aggregation_type.py
--rw-r--r--   0 root         (0) root         (0)    24848 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/allocation.py
--rw-r--r--   0 root         (0) root         (0)    21188 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/allocation_request.py
--rw-r--r--   0 root         (0) root         (0)     4436 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/allocation_set_request.py
--rw-r--r--   0 root         (0) root         (0)    12994 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/amortisation_event.py
--rw-r--r--   0 root         (0) root         (0)    13134 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/amortisation_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7168 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/annul_quotes_response.py
--rw-r--r--   0 root         (0) root         (0)     6065 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/annul_single_structured_data_response.py
--rw-r--r--   0 root         (0) root         (0)     7181 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/annul_structured_data_response.py
--rw-r--r--   0 root         (0) root         (0)     3507 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/asset_class.py
--rw-r--r--   0 root         (0) root         (0)     7902 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/barrier.py
--rw-r--r--   0 root         (0) root         (0)    10814 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/basket.py
--rw-r--r--   0 root         (0) root         (0)    10914 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/basket_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7620 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/basket_identifier.py
--rw-r--r--   0 root         (0) root         (0)     7230 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/batch_adjust_holdings_response.py
--rw-r--r--   0 root         (0) root         (0)     7647 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/batch_upsert_portfolio_transactions_response.py
--rw-r--r--   0 root         (0) root         (0)    18549 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/block.py
--rw-r--r--   0 root         (0) root         (0)    15838 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/block_request.py
--rw-r--r--   0 root         (0) root         (0)     4109 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/block_set_request.py
--rw-r--r--   0 root         (0) root         (0)    22931 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/bond.py
--rw-r--r--   0 root         (0) root         (0)    23191 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/bond_all_of.py
--rw-r--r--   0 root         (0) root         (0)    14817 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/bond_default_event.py
--rw-r--r--   0 root         (0) root         (0)    14977 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/bond_default_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    23520 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/bucketed_cash_flow_request.py
--rw-r--r--   0 root         (0) root         (0)    10365 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/bucketed_cash_flow_response.py
--rw-r--r--   0 root         (0) root         (0)     7739 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/calculation_info.py
--rw-r--r--   0 root         (0) root         (0)     9031 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/calendar.py
--rw-r--r--   0 root         (0) root         (0)    13374 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/calendar_date.py
--rw-r--r--   0 root         (0) root         (0)    13183 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cap_floor.py
--rw-r--r--   0 root         (0) root         (0)    13323 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cap_floor_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7707 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cash_dependency.py
--rw-r--r--   0 root         (0) root         (0)     7787 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cash_dependency_all_of.py
--rw-r--r--   0 root         (0) root         (0)     9845 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cash_dividend_event.py
--rw-r--r--   0 root         (0) root         (0)     9945 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cash_dividend_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10169 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cash_flow_event.py
--rw-r--r--   0 root         (0) root         (0)    10269 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cash_flow_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10510 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cash_flow_lineage.py
--rw-r--r--   0 root         (0) root         (0)    11249 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cash_flow_value.py
--rw-r--r--   0 root         (0) root         (0)    11389 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cash_flow_value_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6768 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cash_flow_value_set.py
--rw-r--r--   0 root         (0) root         (0)     6828 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cash_flow_value_set_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6856 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cash_ladder_record.py
--rw-r--r--   0 root         (0) root         (0)    10170 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cash_perpetual.py
--rw-r--r--   0 root         (0) root         (0)    10270 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cash_perpetual_all_of.py
--rw-r--r--   0 root         (0) root         (0)    24112 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cds_flow_conventions.py
--rw-r--r--   0 root         (0) root         (0)    17378 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cds_index.py
--rw-r--r--   0 root         (0) root         (0)    17578 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cds_index_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10137 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cds_protection_detail_specification.py
--rw-r--r--   0 root         (0) root         (0)    11015 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/change.py
--rw-r--r--   0 root         (0) root         (0)    10714 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/change_history.py
--rw-r--r--   0 root         (0) root         (0)     3354 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/change_history_action.py
--rw-r--r--   0 root         (0) root         (0)     8704 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/change_item.py
--rw-r--r--   0 root         (0) root         (0)     9356 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/chart_of_accounts.py
--rw-r--r--   0 root         (0) root         (0)     7025 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/chart_of_accounts_properties.py
--rw-r--r--   0 root         (0) root         (0)     8946 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/chart_of_accounts_request.py
--rw-r--r--   0 root         (0) root         (0)     7846 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/close_event.py
--rw-r--r--   0 root         (0) root         (0)     7926 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/close_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    15717 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/complete_portfolio.py
--rw-r--r--   0 root         (0) root         (0)    12168 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/complete_relation.py
--rw-r--r--   0 root         (0) root         (0)    14719 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/complete_relationship.py
--rw-r--r--   0 root         (0) root         (0)    11257 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/complex_bond.py
--rw-r--r--   0 root         (0) root         (0)    11357 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/complex_bond_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7096 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/complex_market_data.py
--rw-r--r--   0 root         (0) root         (0)    11521 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/complex_market_data_id.py
--rw-r--r--   0 root         (0) root         (0)     5721 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/compliance_breached_order_info.py
--rw-r--r--   0 root         (0) root         (0)    17899 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/compliance_rule.py
--rw-r--r--   0 root         (0) root         (0)    16917 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/compliance_rule_result.py
--rw-r--r--   0 root         (0) root         (0)    19906 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/compliance_rule_upsert_request.py
--rw-r--r--   0 root         (0) root         (0)     4260 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/compliance_rule_upsert_response.py
--rw-r--r--   0 root         (0) root         (0)    13025 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/compliance_run_info.py
--rw-r--r--   0 root         (0) root         (0)    11637 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/compounding.py
--rw-r--r--   0 root         (0) root         (0)    14328 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/configuration_recipe.py
--rw-r--r--   0 root         (0) root         (0)    15247 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/configuration_recipe_snippet.py
--rw-r--r--   0 root         (0) root         (0)     6181 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/constituents_adjustment_header.py
--rw-r--r--   0 root         (0) root         (0)    19498 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/contract_for_difference.py
--rw-r--r--   0 root         (0) root         (0)    19718 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/contract_for_difference_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10863 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/corporate_action.py
--rw-r--r--   0 root         (0) root         (0)     9857 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/corporate_action_source.py
--rw-r--r--   0 root         (0) root         (0)     5718 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/corporate_action_transition.py
--rw-r--r--   0 root         (0) root         (0)    10625 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/corporate_action_transition_component.py
--rw-r--r--   0 root         (0) root         (0)     7357 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/corporate_action_transition_component_request.py
--rw-r--r--   0 root         (0) root         (0)     5646 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/corporate_action_transition_request.py
--rw-r--r--   0 root         (0) root         (0)    11822 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/counterparty_agreement.py
--rw-r--r--   0 root         (0) root         (0)     8524 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/counterparty_risk_information.py
--rw-r--r--   0 root         (0) root         (0)     6161 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/counterparty_signatory.py
--rw-r--r--   0 root         (0) root         (0)    10189 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_calendar_request.py
--rw-r--r--   0 root         (0) root         (0)    12686 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_corporate_action_source_request.py
--rw-r--r--   0 root         (0) root         (0)     9424 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_cut_label_definition_request.py
--rw-r--r--   0 root         (0) root         (0)     4774 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_data_map_request.py
--rw-r--r--   0 root         (0) root         (0)    20417 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_data_type_request.py
--rw-r--r--   0 root         (0) root         (0)    13518 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_date_request.py
--rw-r--r--   0 root         (0) root         (0)    15511 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_derived_property_definition_request.py
--rw-r--r--   0 root         (0) root         (0)    20890 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_derived_transaction_portfolio_request.py
--rw-r--r--   0 root         (0) root         (0)     4462 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_portfolio_details.py
--rw-r--r--   0 root         (0) root         (0)    12383 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_portfolio_group_request.py
--rw-r--r--   0 root         (0) root         (0)    17579 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_property_definition_request.py
--rw-r--r--   0 root         (0) root         (0)     9307 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_recipe_request.py
--rw-r--r--   0 root         (0) root         (0)    11661 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_reference_portfolio_request.py
--rw-r--r--   0 root         (0) root         (0)    17353 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_relation_definition_request.py
--rw-r--r--   0 root         (0) root         (0)     5899 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_relation_request.py
--rw-r--r--   0 root         (0) root         (0)    22106 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_relationship_definition_request.py
--rw-r--r--   0 root         (0) root         (0)    10113 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_relationship_request.py
--rw-r--r--   0 root         (0) root         (0)    11654 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_sequence_request.py
--rw-r--r--   0 root         (0) root         (0)    10254 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_tax_rule_set_request.py
--rw-r--r--   0 root         (0) root         (0)    20612 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_transaction_portfolio_request.py
--rw-r--r--   0 root         (0) root         (0)     9310 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/create_unit_definition.py
--rw-r--r--   0 root         (0) root         (0)    18199 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/credit_default_swap.py
--rw-r--r--   0 root         (0) root         (0)    18399 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/credit_default_swap_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7521 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/credit_rating.py
--rw-r--r--   0 root         (0) root         (0)    16567 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/credit_spread_curve_data.py
--rw-r--r--   0 root         (0) root         (0)    16767 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/credit_spread_curve_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)    20912 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/credit_support_annex.py
--rw-r--r--   0 root         (0) root         (0)     3450 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/criterion_type.py
--rw-r--r--   0 root         (0) root         (0)     4642 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/currency_and_amount.py
--rw-r--r--   0 root         (0) root         (0)    15766 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/custodian_account.py
--rw-r--r--   0 root         (0) root         (0)     7048 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/custodian_account_properties.py
--rw-r--r--   0 root         (0) root         (0)    18313 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/custodian_account_request.py
--rw-r--r--   0 root         (0) root         (0)     7218 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/custodian_accounts_upsert_response.py
--rw-r--r--   0 root         (0) root         (0)    11807 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/custom_entity_definition.py
--rw-r--r--   0 root         (0) root         (0)    10534 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/custom_entity_definition_request.py
--rw-r--r--   0 root         (0) root         (0)     8081 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/custom_entity_field.py
--rw-r--r--   0 root         (0) root         (0)    11325 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/custom_entity_field_definition.py
--rw-r--r--   0 root         (0) root         (0)    12486 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/custom_entity_id.py
--rw-r--r--   0 root         (0) root         (0)     8385 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/custom_entity_request.py
--rw-r--r--   0 root         (0) root         (0)    13657 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/custom_entity_response.py
--rw-r--r--   0 root         (0) root         (0)     8560 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cut_label_definition.py
--rw-r--r--   0 root         (0) root         (0)     4563 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/cut_local_time.py
--rw-r--r--   0 root         (0) root         (0)    12478 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/data_definition.py
--rw-r--r--   0 root         (0) root         (0)     6911 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/data_map_key.py
--rw-r--r--   0 root         (0) root         (0)     4637 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/data_mapping.py
--rw-r--r--   0 root         (0) root         (0)    15955 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/data_type.py
--rw-r--r--   0 root         (0) root         (0)    15138 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/data_type_summary.py
--rw-r--r--   0 root         (0) root         (0)     3314 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/data_type_value_range.py
--rw-r--r--   0 root         (0) root         (0)    14147 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/date_attributes.py
--rw-r--r--   0 root         (0) root         (0)     4864 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/date_range.py
--rw-r--r--   0 root         (0) root         (0)     3369 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/date_time_comparison_type.py
--rw-r--r--   0 root         (0) root         (0)     3458 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/day_of_week.py
--rw-r--r--   0 root         (0) root         (0)     5764 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/delete_accounts_response.py
--rw-r--r--   0 root         (0) root         (0)     6213 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/delete_custodian_accounts_response.py
--rw-r--r--   0 root         (0) root         (0)     5179 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/delete_instrument_properties_response.py
--rw-r--r--   0 root         (0) root         (0)     6116 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/delete_instrument_response.py
--rw-r--r--   0 root         (0) root         (0)     6132 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/delete_instruments_response.py
--rw-r--r--   0 root         (0) root         (0)     3280 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/delete_modes.py
--rw-r--r--   0 root         (0) root         (0)     6079 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/delete_relation_request.py
--rw-r--r--   0 root         (0) root         (0)    10335 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/delete_relationship_request.py
--rw-r--r--   0 root         (0) root         (0)     7419 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/deleted_entity_response.py
--rw-r--r--   0 root         (0) root         (0)     8387 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/dependency_source_filter.py
--rw-r--r--   0 root         (0) root         (0)     5221 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/described_address_key.py
--rw-r--r--   0 root         (0) root         (0)    11233 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/discount_factor_curve_data.py
--rw-r--r--   0 root         (0) root         (0)    11353 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/discount_factor_curve_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7837 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/discounting_dependency.py
--rw-r--r--   0 root         (0) root         (0)     7917 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/discounting_dependency_all_of.py
--rw-r--r--   0 root         (0) root         (0)     3409 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/discounting_method.py
--rw-r--r--   0 root         (0) root         (0)     6228 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/economic_dependency.py
--rw-r--r--   0 root         (0) root         (0)     3687 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/economic_dependency_type.py
--rw-r--r--   0 root         (0) root         (0)     6020 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/economic_dependency_with_complex_market_data.py
--rw-r--r--   0 root         (0) root         (0)     6830 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/economic_dependency_with_quote.py
--rw-r--r--   0 root         (0) root         (0)     5398 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/empty_model_options.py
--rw-r--r--   0 root         (0) root         (0)     5438 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/empty_model_options_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6713 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/entity_identifier.py
--rw-r--r--   0 root         (0) root         (0)     8495 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity.py
--rw-r--r--   0 root         (0) root         (0)     8575 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11924 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_all_of_identifiers.py
--rw-r--r--   0 root         (0) root         (0)    11440 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_curve_by_prices_data.py
--rw-r--r--   0 root         (0) root         (0)    11560 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_curve_by_prices_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)    12169 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_curve_dependency.py
--rw-r--r--   0 root         (0) root         (0)    12289 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_curve_dependency_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7849 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_model_options.py
--rw-r--r--   0 root         (0) root         (0)     7909 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_model_options_all_of.py
--rw-r--r--   0 root         (0) root         (0)    24187 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_option.py
--rw-r--r--   0 root         (0) root         (0)    24487 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_option_all_of.py
--rw-r--r--   0 root         (0) root         (0)    23696 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_swap.py
--rw-r--r--   0 root         (0) root         (0)    23956 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_swap_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11506 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_vol_dependency.py
--rw-r--r--   0 root         (0) root         (0)    11626 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_vol_dependency_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11231 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_vol_surface_data.py
--rw-r--r--   0 root         (0) root         (0)    11351 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/equity_vol_surface_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6806 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/error_detail.py
--rw-r--r--   0 root         (0) root         (0)     4531 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/event_date_range.py
--rw-r--r--   0 root         (0) root         (0)    11841 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/exchange_traded_option.py
--rw-r--r--   0 root         (0) root         (0)    11961 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/exchange_traded_option_all_of.py
--rw-r--r--   0 root         (0) root         (0)    23036 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/exchange_traded_option_contract_details.py
--rw-r--r--   0 root         (0) root         (0)    24122 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/execution.py
--rw-r--r--   0 root         (0) root         (0)    21469 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/execution_request.py
--rw-r--r--   0 root         (0) root         (0)     4169 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/execution_set_request.py
--rw-r--r--   0 root         (0) root         (0)    11000 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/exercise_event.py
--rw-r--r--   0 root         (0) root         (0)    11120 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/exercise_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10285 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/exotic_instrument.py
--rw-r--r--   0 root         (0) root         (0)    10365 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/exotic_instrument_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11174 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/expanded_group.py
--rw-r--r--   0 root         (0) root         (0)    21346 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fee_rule.py
--rw-r--r--   0 root         (0) root         (0)    24042 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fee_rule_upsert_request.py
--rw-r--r--   0 root         (0) root         (0)     4904 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fee_rule_upsert_response.py
--rw-r--r--   0 root         (0) root         (0)     6695 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/field_definition.py
--rw-r--r--   0 root         (0) root         (0)     8258 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/field_schema.py
--rw-r--r--   0 root         (0) root         (0)     5658 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/field_value.py
--rw-r--r--   0 root         (0) root         (0)     5781 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/file_response.py
--rw-r--r--   0 root         (0) root         (0)    13116 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fixed_leg.py
--rw-r--r--   0 root         (0) root         (0)    13256 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fixed_leg_all_of.py
--rw-r--r--   0 root         (0) root         (0)     4915 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fixed_leg_all_of_overrides.py
--rw-r--r--   0 root         (0) root         (0)    13681 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fixed_schedule.py
--rw-r--r--   0 root         (0) root         (0)    13881 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fixed_schedule_all_of.py
--rw-r--r--   0 root         (0) root         (0)    15440 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/float_schedule.py
--rw-r--r--   0 root         (0) root         (0)    15680 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/float_schedule_all_of.py
--rw-r--r--   0 root         (0) root         (0)    13373 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/floating_leg.py
--rw-r--r--   0 root         (0) root         (0)    13513 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/floating_leg_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6592 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/flow_convention_name.py
--rw-r--r--   0 root         (0) root         (0)    23990 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/flow_conventions.py
--rw-r--r--   0 root         (0) root         (0)    15807 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/forward_rate_agreement.py
--rw-r--r--   0 root         (0) root         (0)    15987 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/forward_rate_agreement_all_of.py
--rw-r--r--   0 root         (0) root         (0)    14013 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/funding_leg.py
--rw-r--r--   0 root         (0) root         (0)    14133 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/funding_leg_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7410 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/funding_leg_options.py
--rw-r--r--   0 root         (0) root         (0)     7470 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/funding_leg_options_all_of.py
--rw-r--r--   0 root         (0) root         (0)    20197 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/future.py
--rw-r--r--   0 root         (0) root         (0)    20397 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/future_all_of.py
--rw-r--r--   0 root         (0) root         (0)    21009 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/futures_contract_details.py
--rw-r--r--   0 root         (0) root         (0)     9180 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_dependency.py
--rw-r--r--   0 root         (0) root         (0)     9280 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_dependency_all_of.py
--rw-r--r--   0 root         (0) root         (0)    20192 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forward.py
--rw-r--r--   0 root         (0) root         (0)    20432 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forward_all_of.py
--rw-r--r--   0 root         (0) root         (0)    12659 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forward_curve_by_quote_reference.py
--rw-r--r--   0 root         (0) root         (0)    12799 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forward_curve_by_quote_reference_all_of.py
--rw-r--r--   0 root         (0) root         (0)    13026 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forward_curve_data.py
--rw-r--r--   0 root         (0) root         (0)    13186 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forward_curve_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11327 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forward_model_options.py
--rw-r--r--   0 root         (0) root         (0)    11427 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forward_model_options_all_of.py
--rw-r--r--   0 root         (0) root         (0)    13322 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forward_pips_curve_data.py
--rw-r--r--   0 root         (0) root         (0)    13482 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forward_pips_curve_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)    13194 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forward_tenor_curve_data.py
--rw-r--r--   0 root         (0) root         (0)    13354 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forward_tenor_curve_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)    13490 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forward_tenor_pips_curve_data.py
--rw-r--r--   0 root         (0) root         (0)    13650 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forward_tenor_pips_curve_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11788 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forwards_dependency.py
--rw-r--r--   0 root         (0) root         (0)    11908 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_forwards_dependency_all_of.py
--rw-r--r--   0 root         (0) root         (0)    28087 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_option.py
--rw-r--r--   0 root         (0) root         (0)    28447 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_option_all_of.py
--rw-r--r--   0 root         (0) root         (0)     9436 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_rate_schedule.py
--rw-r--r--   0 root         (0) root         (0)     9556 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_rate_schedule_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11021 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_swap.py
--rw-r--r--   0 root         (0) root         (0)    11121 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_swap_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11363 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_vol_dependency.py
--rw-r--r--   0 root         (0) root         (0)    11483 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_vol_dependency_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11135 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/fx_vol_surface_data.py
--rw-r--r--   0 root         (0) root         (0)     7028 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/get_cds_flow_conventions_response.py
--rw-r--r--   0 root         (0) root         (0)     7279 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/get_complex_market_data_response.py
--rw-r--r--   0 root         (0) root         (0)     7088 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/get_counterparty_agreement_response.py
--rw-r--r--   0 root         (0) root         (0)     7040 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/get_credit_support_annex_response.py
--rw-r--r--   0 root         (0) root         (0)     7046 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/get_data_map_response.py
--rw-r--r--   0 root         (0) root         (0)     6956 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/get_flow_conventions_response.py
--rw-r--r--   0 root         (0) root         (0)     6956 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/get_index_convention_response.py
--rw-r--r--   0 root         (0) root         (0)     7371 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/get_instruments_response.py
--rw-r--r--   0 root         (0) root         (0)     8047 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/get_quotes_response.py
--rw-r--r--   0 root         (0) root         (0)     5689 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/get_recipe_response.py
--rw-r--r--   0 root         (0) root         (0)    12030 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/get_reference_portfolio_constituents_response.py
--rw-r--r--   0 root         (0) root         (0)     7351 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/get_structured_result_data_response.py
--rw-r--r--   0 root         (0) root         (0)     7222 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/get_virtual_document_response.py
--rw-r--r--   0 root         (0) root         (0)     5131 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/grouped_result_of_address_key.py
--rw-r--r--   0 root         (0) root         (0)    12535 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/holding_adjustment.py
--rw-r--r--   0 root         (0) root         (0)    13889 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/holding_adjustment_with_date.py
--rw-r--r--   0 root         (0) root         (0)     4577 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/holding_context.py
--rw-r--r--   0 root         (0) root         (0)    10491 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/holdings_adjustment.py
--rw-r--r--   0 root         (0) root         (0)     9374 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/holdings_adjustment_header.py
--rw-r--r--   0 root         (0) root         (0)     3970 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/i_data_record.py
--rw-r--r--   0 root         (0) root         (0)     6778 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/i_unit_definition_dto.py
--rw-r--r--   0 root         (0) root         (0)     7949 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/id_selector_definition.py
--rw-r--r--   0 root         (0) root         (0)     9438 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/identifier_part_schema.py
--rw-r--r--   0 root         (0) root         (0)    18219 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/index_convention.py
--rw-r--r--   0 root         (0) root         (0)     7150 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/index_model_options.py
--rw-r--r--   0 root         (0) root         (0)     7210 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/index_model_options_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11786 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/index_projection_dependency.py
--rw-r--r--   0 root         (0) root         (0)    11906 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/index_projection_dependency_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7581 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/industry_classifier.py
--rw-r--r--   0 root         (0) root         (0)    36320 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/inflation_linked_bond.py
--rw-r--r--   0 root         (0) root         (0)    36720 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/inflation_linked_bond_all_of.py
--rw-r--r--   0 root         (0) root         (0)    25334 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/inflation_swap.py
--rw-r--r--   0 root         (0) root         (0)    25634 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/inflation_swap_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10090 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/informational_error_event.py
--rw-r--r--   0 root         (0) root         (0)    10190 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/informational_error_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    13185 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/informational_event.py
--rw-r--r--   0 root         (0) root         (0)    13325 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/informational_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    22490 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/inline_valuation_request.py
--rw-r--r--   0 root         (0) root         (0)     8210 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/inline_valuations_reconciliation_request.py
--rw-r--r--   0 root         (0) root         (0)     5481 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/input_transition.py
--rw-r--r--   0 root         (0) root         (0)    19961 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument.py
--rw-r--r--   0 root         (0) root         (0)    10083 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_capabilities.py
--rw-r--r--   0 root         (0) root         (0)    16808 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_cash_flow.py
--rw-r--r--   0 root         (0) root         (0)     9470 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_definition.py
--rw-r--r--   0 root         (0) root         (0)     8348 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_definition_format.py
--rw-r--r--   0 root         (0) root         (0)     3320 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_delete_modes.py
--rw-r--r--   0 root         (0) root         (0)     6924 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_event.py
--rw-r--r--   0 root         (0) root         (0)    17157 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_event_holder.py
--rw-r--r--   0 root         (0) root         (0)     4038 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_event_type.py
--rw-r--r--   0 root         (0) root         (0)     7700 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_id_type_descriptor.py
--rw-r--r--   0 root         (0) root         (0)     5728 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_id_value.py
--rw-r--r--   0 root         (0) root         (0)     7134 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_leg.py
--rw-r--r--   0 root         (0) root         (0)     6699 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_leg_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6118 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_match.py
--rw-r--r--   0 root         (0) root         (0)     9927 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_payment_diary.py
--rw-r--r--   0 root         (0) root         (0)     5114 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_payment_diary_leg.py
--rw-r--r--   0 root         (0) root         (0)    20931 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_payment_diary_row.py
--rw-r--r--   0 root         (0) root         (0)     6889 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_properties.py
--rw-r--r--   0 root         (0) root         (0)     6083 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_search_property.py
--rw-r--r--   0 root         (0) root         (0)     4837 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/instrument_type.py
--rw-r--r--   0 root         (0) root         (0)    14277 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/interest_rate_swap.py
--rw-r--r--   0 root         (0) root         (0)    14417 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/interest_rate_swap_all_of.py
--rw-r--r--   0 root         (0) root         (0)    13510 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/interest_rate_swaption.py
--rw-r--r--   0 root         (0) root         (0)    13650 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/interest_rate_swaption_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11120 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/ir_vol_cube_data.py
--rw-r--r--   0 root         (0) root         (0)    11240 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/ir_vol_cube_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)     9519 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/ir_vol_dependency.py
--rw-r--r--   0 root         (0) root         (0)     9619 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/ir_vol_dependency_all_of.py
--rw-r--r--   0 root         (0) root         (0)     5575 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/is_business_day_response.py
--rw-r--r--   0 root         (0) root         (0)    24671 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/je_lines.py
--rw-r--r--   0 root         (0) root         (0)     7963 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/je_lines_query_parameters.py
--rw-r--r--   0 root         (0) root         (0)     4311 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/label_value_set.py
--rw-r--r--   0 root         (0) root         (0)    17095 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/leg_definition.py
--rw-r--r--   0 root         (0) root         (0)    13346 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/legal_entity.py
--rw-r--r--   0 root         (0) root         (0)     5400 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/level_step.py
--rw-r--r--   0 root         (0) root         (0)     8320 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/life_cycle_event_lineage.py
--rw-r--r--   0 root         (0) root         (0)     8841 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/life_cycle_event_value.py
--rw-r--r--   0 root         (0) root         (0)     8941 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/life_cycle_event_value_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6392 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/link.py
--rw-r--r--   0 root         (0) root         (0)     6623 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/list_aggregation_reconciliation.py
--rw-r--r--   0 root         (0) root         (0)    10736 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/list_aggregation_response.py
--rw-r--r--   0 root         (0) root         (0)     6377 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/list_complex_market_data_with_meta_data_response.py
--rw-r--r--   0 root         (0) root         (0)     8140 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/lusid_instrument.py
--rw-r--r--   0 root         (0) root         (0)     9506 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/lusid_problem_details.py
--rw-r--r--   0 root         (0) root         (0)    26392 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/lusid_trade_ticket.py
--rw-r--r--   0 root         (0) root         (0)     5947 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/lusid_unique_id.py
--rw-r--r--   0 root         (0) root         (0)    10706 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/lusid_validation_problem_details.py
--rw-r--r--   0 root         (0) root         (0)     6589 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/mapped_string.py
--rw-r--r--   0 root         (0) root         (0)    10565 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/mapping.py
--rw-r--r--   0 root         (0) root         (0)    10470 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/mapping_rule.py
--rw-r--r--   0 root         (0) root         (0)     9380 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/market_context.py
--rw-r--r--   0 root         (0) root         (0)     6867 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/market_context_suppliers.py
--rw-r--r--   0 root         (0) root         (0)    26172 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/market_data_key_rule.py
--rw-r--r--   0 root         (0) root         (0)     5841 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/market_data_overrides.py
--rw-r--r--   0 root         (0) root         (0)    23809 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/market_data_specific_rule.py
--rw-r--r--   0 root         (0) root         (0)     4198 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/market_data_type.py
--rw-r--r--   0 root         (0) root         (0)     3493 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/market_observable_type.py
--rw-r--r--   0 root         (0) root         (0)    14880 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/market_options.py
--rw-r--r--   0 root         (0) root         (0)     5970 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/market_quote.py
--rw-r--r--   0 root         (0) root         (0)     5507 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/match_criterion.py
--rw-r--r--   0 root         (0) root         (0)     4609 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/metric_value.py
--rw-r--r--   0 root         (0) root         (0)     6042 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/model_options.py
--rw-r--r--   0 root         (0) root         (0)     3696 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/model_options_type.py
--rw-r--r--   0 root         (0) root         (0)     7700 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/model_property.py
--rw-r--r--   0 root         (0) root         (0)     7505 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/model_selection.py
--rw-r--r--   0 root         (0) root         (0)     4052 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/movement_type.py
--rw-r--r--   0 root         (0) root         (0)     5119 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/next_value_in_sequence_response.py
--rw-r--r--   0 root         (0) root         (0)     3431 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/numeric_comparison_type.py
--rw-r--r--   0 root         (0) root         (0)     5233 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/opaque_dependency.py
--rw-r--r--   0 root         (0) root         (0)     5273 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/opaque_dependency_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11964 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/opaque_market_data.py
--rw-r--r--   0 root         (0) root         (0)    12084 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/opaque_market_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6307 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/opaque_model_options.py
--rw-r--r--   0 root         (0) root         (0)     6367 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/opaque_model_options_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6895 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/open_event.py
--rw-r--r--   0 root         (0) root         (0)     6955 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/open_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)     3304 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/operand_type.py
--rw-r--r--   0 root         (0) root         (0)     5598 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/operation.py
--rw-r--r--   0 root         (0) root         (0)     3261 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/operation_type.py
--rw-r--r--   0 root         (0) root         (0)     3523 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/operator.py
--rw-r--r--   0 root         (0) root         (0)    22500 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order.py
--rw-r--r--   0 root         (0) root         (0)     5698 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_by_spec.py
--rw-r--r--   0 root         (0) root         (0)    11905 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_block.py
--rw-r--r--   0 root         (0) root         (0)     4124 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_allocation_detail.py
--rw-r--r--   0 root         (0) root         (0)     5714 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_allocation_synopsis.py
--rw-r--r--   0 root         (0) root         (0)     4116 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_execution_detail.py
--rw-r--r--   0 root         (0) root         (0)     5692 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_execution_synopsis.py
--rw-r--r--   0 root         (0) root         (0)     5911 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_order_detail.py
--rw-r--r--   0 root         (0) root         (0)     5658 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_order_synopsis.py
--rw-r--r--   0 root         (0) root         (0)     4116 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_placement_detail.py
--rw-r--r--   0 root         (0) root         (0)     5686 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_placement_synopsis.py
--rw-r--r--   0 root         (0) root         (0)    12421 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement.py
--rw-r--r--   0 root         (0) root         (0)     4156 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement_allocation_detail.py
--rw-r--r--   0 root         (0) root         (0)     5790 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement_allocation_synopsis.py
--rw-r--r--   0 root         (0) root         (0)     4148 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement_execution_detail.py
--rw-r--r--   0 root         (0) root         (0)     5798 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement_execution_synopsis.py
--rw-r--r--   0 root         (0) root         (0)     4116 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement_order_detail.py
--rw-r--r--   0 root         (0) root         (0)     4528 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement_order_synopsis.py
--rw-r--r--   0 root         (0) root         (0)     4410 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement_placement_synopsis.py
--rw-r--r--   0 root         (0) root         (0)     6603 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_instruction.py
--rw-r--r--   0 root         (0) root         (0)     5201 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_instruction_request.py
--rw-r--r--   0 root         (0) root         (0)     4274 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_instruction_set_request.py
--rw-r--r--   0 root         (0) root         (0)    18756 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_request.py
--rw-r--r--   0 root         (0) root         (0)     4246 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/order_set_request.py
--rw-r--r--   0 root         (0) root         (0)     4383 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/otc_confirmation.py
--rw-r--r--   0 root         (0) root         (0)    33018 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/output_transaction.py
--rw-r--r--   0 root         (0) root         (0)    10332 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/output_transition.py
--rw-r--r--   0 root         (0) root         (0)     8950 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/package.py
--rw-r--r--   0 root         (0) root         (0)     7676 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/package_request.py
--rw-r--r--   0 root         (0) root         (0)     4139 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/package_set_request.py
--rw-r--r--   0 root         (0) root         (0)     7217 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_abor.py
--rw-r--r--   0 root         (0) root         (0)     7581 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_abor_configuration.py
--rw-r--r--   0 root         (0) root         (0)     7301 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_account.py
--rw-r--r--   0 root         (0) root         (0)     7385 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_allocation.py
--rw-r--r--   0 root         (0) root         (0)     7245 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_block.py
--rw-r--r--   0 root         (0) root         (0)     7329 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_calendar.py
--rw-r--r--   0 root         (0) root         (0)     7525 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_chart_of_accounts.py
--rw-r--r--   0 root         (0) root         (0)     7693 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_corporate_action_source.py
--rw-r--r--   0 root         (0) root         (0)     7553 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_custodian_account.py
--rw-r--r--   0 root         (0) root         (0)     7721 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_custom_entity_definition.py
--rw-r--r--   0 root         (0) root         (0)     7665 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_custom_entity_response.py
--rw-r--r--   0 root         (0) root         (0)     7609 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_cut_label_definition.py
--rw-r--r--   0 root         (0) root         (0)     7525 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_data_type_summary.py
--rw-r--r--   0 root         (0) root         (0)     7357 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_execution.py
--rw-r--r--   0 root         (0) root         (0)     7385 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_instrument.py
--rw-r--r--   0 root         (0) root         (0)     7693 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_instrument_event_holder.py
--rw-r--r--   0 root         (0) root         (0)     7413 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_legal_entity.py
--rw-r--r--   0 root         (0) root         (0)     7245 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_order.py
--rw-r--r--   0 root         (0) root         (0)     7525 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_order_graph_block.py
--rw-r--r--   0 root         (0) root         (0)     7637 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_order_graph_placement.py
--rw-r--r--   0 root         (0) root         (0)     7553 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_order_instruction.py
--rw-r--r--   0 root         (0) root         (0)     7301 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_package.py
--rw-r--r--   0 root         (0) root         (0)     7469 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_participation.py
--rw-r--r--   0 root         (0) root         (0)     7273 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_person.py
--rw-r--r--   0 root         (0) root         (0)     7357 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_placement.py
--rw-r--r--   0 root         (0) root         (0)     7833 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_portfolio_group_search_result.py
--rw-r--r--   0 root         (0) root         (0)     7693 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_portfolio_search_result.py
--rw-r--r--   0 root         (0) root         (0)     7945 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_property_definition_search_result.py
--rw-r--r--   0 root         (0) root         (0)     7721 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_relationship_definition.py
--rw-r--r--   0 root         (0) root         (0)     7609 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_sequence_definition.py
--rw-r--r--   0 root         (0) root         (0)     7482 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/participation.py
--rw-r--r--   0 root         (0) root         (0)     6926 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/participation_request.py
--rw-r--r--   0 root         (0) root         (0)     4229 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/participation_set_request.py
--rw-r--r--   0 root         (0) root         (0)     8788 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/performance_return.py
--rw-r--r--   0 root         (0) root         (0)    10181 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/performance_returns_metric.py
--rw-r--r--   0 root         (0) root         (0)     3393 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/period_type.py
--rw-r--r--   0 root         (0) root         (0)     3367 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/perpetual_entity_state.py
--rw-r--r--   0 root         (0) root         (0)     5213 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/perpetual_property.py
--rw-r--r--   0 root         (0) root         (0)    11043 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/person.py
--rw-r--r--   0 root         (0) root         (0)    22633 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/placement.py
--rw-r--r--   0 root         (0) root         (0)    20489 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/placement_request.py
--rw-r--r--   0 root         (0) root         (0)     4169 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/placement_set_request.py
--rw-r--r--   0 root         (0) root         (0)    21169 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio.py
--rw-r--r--   0 root         (0) root         (0)    23700 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio_cash_flow.py
--rw-r--r--   0 root         (0) root         (0)     8810 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio_cash_ladder.py
--rw-r--r--   0 root         (0) root         (0)    15147 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio_details.py
--rw-r--r--   0 root         (0) root         (0)     8460 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio_entity_id.py
--rw-r--r--   0 root         (0) root         (0)    13607 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio_group.py
--rw-r--r--   0 root         (0) root         (0)     6996 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio_group_properties.py
--rw-r--r--   0 root         (0) root         (0)    12953 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio_group_search_result.py
--rw-r--r--   0 root         (0) root         (0)    17791 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio_holding.py
--rw-r--r--   0 root         (0) root         (0)     6863 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio_properties.py
--rw-r--r--   0 root         (0) root         (0)     6775 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio_reconciliation_request.py
--rw-r--r--   0 root         (0) root         (0)    17336 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio_result_data_key_rule.py
--rw-r--r--   0 root         (0) root         (0)    17516 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio_result_data_key_rule_all_of.py
--rw-r--r--   0 root         (0) root         (0)    15510 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio_search_result.py
--rw-r--r--   0 root         (0) root         (0)     5228 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio_trade_ticket.py
--rw-r--r--   0 root         (0) root         (0)     3390 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolio_type.py
--rw-r--r--   0 root         (0) root         (0)     7197 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/portfolios_reconciliation_request.py
--rw-r--r--   0 root         (0) root         (0)     6022 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/premium.py
--rw-r--r--   0 root         (0) root         (0)     9445 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/pricing_context.py
--rw-r--r--   0 root         (0) root         (0)     4322 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/pricing_model.py
--rw-r--r--   0 root         (0) root         (0)    27514 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/pricing_options.py
--rw-r--r--   0 root         (0) root         (0)     7870 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/processed_command.py
--rw-r--r--   0 root         (0) root         (0)    27010 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/property_definition.py
--rw-r--r--   0 root         (0) root         (0)    27874 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/property_definition_search_result.py
--rw-r--r--   0 root         (0) root         (0)     3390 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/property_definition_type.py
--rw-r--r--   0 root         (0) root         (0)     4831 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/property_domain.py
--rw-r--r--   0 root         (0) root         (0)     7835 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/property_filter.py
--rw-r--r--   0 root         (0) root         (0)     7969 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/property_interval.py
--rw-r--r--   0 root         (0) root         (0)     3336 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/property_life_time.py
--rw-r--r--   0 root         (0) root         (0)     5265 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/property_schema.py
--rw-r--r--   0 root         (0) root         (0)     3338 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/property_type.py
--rw-r--r--   0 root         (0) root         (0)     6066 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/property_value.py
--rw-r--r--   0 root         (0) root         (0)     7834 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/property_value_equals.py
--rw-r--r--   0 root         (0) root         (0)     7914 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/property_value_equals_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7309 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/property_value_in.py
--rw-r--r--   0 root         (0) root         (0)     7389 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/property_value_in_all_of.py
--rw-r--r--   0 root         (0) root         (0)    21310 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/query_bucketed_cash_flows_request.py
--rw-r--r--   0 root         (0) root         (0)    10450 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/query_cash_flows_request.py
--rw-r--r--   0 root         (0) root         (0)    12914 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/query_instrument_events_request.py
--rw-r--r--   0 root         (0) root         (0)    10552 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/query_trade_tickets_request.py
--rw-r--r--   0 root         (0) root         (0)    10795 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/quote.py
--rw-r--r--   0 root         (0) root         (0)     5483 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/quote_access_metadata_rule.py
--rw-r--r--   0 root         (0) root         (0)    15723 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/quote_access_metadata_rule_id.py
--rw-r--r--   0 root         (0) root         (0)     9612 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/quote_dependency.py
--rw-r--r--   0 root         (0) root         (0)     9712 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/quote_dependency_all_of.py
--rw-r--r--   0 root         (0) root         (0)     5783 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/quote_id.py
--rw-r--r--   0 root         (0) root         (0)     3605 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/quote_instrument_id_type.py
--rw-r--r--   0 root         (0) root         (0)    14721 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/quote_series_id.py
--rw-r--r--   0 root         (0) root         (0)     3587 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/quote_type.py
--rw-r--r--   0 root         (0) root         (0)    11311 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/raw_vendor_event.py
--rw-r--r--   0 root         (0) root         (0)    11431 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/raw_vendor_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)    17980 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/realised_gain_loss.py
--rw-r--r--   0 root         (0) root         (0)     9883 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reconcile_date_time_rule.py
--rw-r--r--   0 root         (0) root         (0)     9983 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reconcile_date_time_rule_all_of.py
--rw-r--r--   0 root         (0) root         (0)     9945 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reconcile_numeric_rule.py
--rw-r--r--   0 root         (0) root         (0)    10045 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reconcile_numeric_rule_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10716 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reconcile_string_rule.py
--rw-r--r--   0 root         (0) root         (0)    10816 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reconcile_string_rule_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7788 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reconciled_transaction.py
--rw-r--r--   0 root         (0) root         (0)    15668 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reconciliation_break.py
--rw-r--r--   0 root         (0) root         (0)     5468 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reconciliation_left_right_address_key_pair.py
--rw-r--r--   0 root         (0) root         (0)     7307 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reconciliation_line.py
--rw-r--r--   0 root         (0) root         (0)    10383 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reconciliation_request.py
--rw-r--r--   0 root         (0) root         (0)     5245 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reconciliation_response.py
--rw-r--r--   0 root         (0) root         (0)     5472 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reconciliation_rule.py
--rw-r--r--   0 root         (0) root         (0)     3546 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reconciliation_rule_type.py
--rw-r--r--   0 root         (0) root         (0)     5343 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reference_data.py
--rw-r--r--   0 root         (0) root         (0)    11099 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reference_instrument.py
--rw-r--r--   0 root         (0) root         (0)    11199 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reference_instrument_all_of.py
--rw-r--r--   0 root         (0) root         (0)    11192 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reference_portfolio_constituent.py
--rw-r--r--   0 root         (0) root         (0)     7556 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reference_portfolio_constituent_request.py
--rw-r--r--   0 root         (0) root         (0)     3408 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reference_portfolio_weight_type.py
--rw-r--r--   0 root         (0) root         (0)    12677 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/related_entity.py
--rw-r--r--   0 root         (0) root         (0)    10235 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/relation.py
--rw-r--r--   0 root         (0) root         (0)    14446 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/relation_definition.py
--rw-r--r--   0 root         (0) root         (0)    13986 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/relationship.py
--rw-r--r--   0 root         (0) root         (0)    19714 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/relationship_definition.py
--rw-r--r--   0 root         (0) root         (0)    25564 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/repo.py
--rw-r--r--   0 root         (0) root         (0)    25824 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/repo_all_of.py
--rw-r--r--   0 root         (0) root         (0)    12033 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reset_event.py
--rw-r--r--   0 root         (0) root         (0)    12173 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/reset_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6065 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_id.py
--rw-r--r--   0 root         (0) root         (0)     7657 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_access_controlled_resource.py
--rw-r--r--   0 root         (0) root         (0)     7571 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_access_metadata_value_of.py
--rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_aggregated_return.py
--rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_aggregation_query.py
--rw-r--r--   0 root         (0) root         (0)     7265 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_allocation.py
--rw-r--r--   0 root         (0) root         (0)     7125 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_block.py
--rw-r--r--   0 root         (0) root         (0)     7321 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_calendar_date.py
--rw-r--r--   0 root         (0) root         (0)     7153 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_change.py
--rw-r--r--   0 root         (0) root         (0)     7349 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_change_history.py
--rw-r--r--   0 root         (0) root         (0)     7741 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_compliance_breached_order_info.py
--rw-r--r--   0 root         (0) root         (0)     7377 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_compliance_rule.py
--rw-r--r--   0 root         (0) root         (0)     7545 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_compliance_rule_result.py
--rw-r--r--   0 root         (0) root         (0)     7461 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_compliance_run_info.py
--rw-r--r--   0 root         (0) root         (0)     7769 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_constituents_adjustment_header.py
--rw-r--r--   0 root         (0) root         (0)     7405 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_corporate_action.py
--rw-r--r--   0 root         (0) root         (0)     7209 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_data_type.py
--rw-r--r--   0 root         (0) root         (0)     7237 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_execution.py
--rw-r--r--   0 root         (0) root         (0)     7181 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_fee_rule.py
--rw-r--r--   0 root         (0) root         (0)     7797 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_get_cds_flow_conventions_response.py
--rw-r--r--   0 root         (0) root         (0)     7881 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_get_counterparty_agreement_response.py
--rw-r--r--   0 root         (0) root         (0)     7797 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_get_credit_support_annex_response.py
--rw-r--r--   0 root         (0) root         (0)     7713 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_get_flow_conventions_response.py
--rw-r--r--   0 root         (0) root         (0)     7713 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_get_index_convention_response.py
--rw-r--r--   0 root         (0) root         (0)     7461 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_get_recipe_response.py
--rw-r--r--   0 root         (0) root         (0)     7657 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_holdings_adjustment_header.py
--rw-r--r--   0 root         (0) root         (0)     7489 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_i_unit_definition_dto.py
--rw-r--r--   0 root         (0) root         (0)     7489 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_instrument_cash_flow.py
--rw-r--r--   0 root         (0) root         (0)     7573 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_instrument_event_holder.py
--rw-r--r--   0 root         (0) root         (0)     7713 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_instrument_id_type_descriptor.py
--rw-r--r--   0 root         (0) root         (0)     7293 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_legal_entity.py
--rw-r--r--   0 root         (0) root         (0)     8133 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_list_complex_market_data_with_meta_data_response.py
--rw-r--r--   0 root         (0) root         (0)     7181 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_mapping.py
--rw-r--r--   0 root         (0) root         (0)     7125 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_order.py
--rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_order_instruction.py
--rw-r--r--   0 root         (0) root         (0)     7181 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_package.py
--rw-r--r--   0 root         (0) root         (0)     7349 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_participation.py
--rw-r--r--   0 root         (0) root         (0)     7461 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_performance_return.py
--rw-r--r--   0 root         (0) root         (0)     7153 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_person.py
--rw-r--r--   0 root         (0) root         (0)     7237 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_placement.py
--rw-r--r--   0 root         (0) root         (0)     7237 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_portfolio.py
--rw-r--r--   0 root         (0) root         (0)     7461 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_portfolio_cash_flow.py
--rw-r--r--   0 root         (0) root         (0)     7517 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_portfolio_cash_ladder.py
--rw-r--r--   0 root         (0) root         (0)     7377 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_portfolio_group.py
--rw-r--r--   0 root         (0) root         (0)     7545 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_portfolio_trade_ticket.py
--rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_processed_command.py
--rw-r--r--   0 root         (0) root         (0)     7229 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_property.py
--rw-r--r--   0 root         (0) root         (0)     7489 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_property_definition.py
--rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_property_interval.py
--rw-r--r--   0 root         (0) root         (0)     7125 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_quote.py
--rw-r--r--   0 root         (0) root         (0)     7629 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_quote_access_metadata_rule.py
--rw-r--r--   0 root         (0) root         (0)     7517 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_reconciliation_break.py
--rw-r--r--   0 root         (0) root         (0)     7209 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_relation.py
--rw-r--r--   0 root         (0) root         (0)     7321 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_relationship.py
--rw-r--r--   0 root         (0) root         (0)     7405 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_scope_definition.py
--rw-r--r--   0 root         (0) root         (0)     7123 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_string.py
--rw-r--r--   0 root         (0) root         (0)     7265 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_tax_rule_set.py
--rw-r--r--   0 root         (0) root         (0)     7293 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_transaction.py
--rw-r--r--   0 root         (0) root         (0)     7237 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_value_type.py
--rw-r--r--   0 root         (0) root         (0)     7131 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/response_meta_data.py
--rw-r--r--   0 root         (0) root         (0)    16884 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_data_key_rule.py
--rw-r--r--   0 root         (0) root         (0)    17064 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_data_key_rule_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6620 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_data_schema.py
--rw-r--r--   0 root         (0) root         (0)     5593 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_key_rule.py
--rw-r--r--   0 root         (0) root         (0)     3442 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_key_rule_type.py
--rw-r--r--   0 root         (0) root         (0)     6667 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value.py
--rw-r--r--   0 root         (0) root         (0)     8572 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value0_d.py
--rw-r--r--   0 root         (0) root         (0)     8672 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value0_d_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6563 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value_bool.py
--rw-r--r--   0 root         (0) root         (0)     6623 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value_bool_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6573 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value_currency.py
--rw-r--r--   0 root         (0) root         (0)     6633 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value_currency_all_of.py
--rw-r--r--   0 root         (0) root         (0)     8004 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value_date_time_offset.py
--rw-r--r--   0 root         (0) root         (0)     8084 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value_date_time_offset_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7880 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value_decimal.py
--rw-r--r--   0 root         (0) root         (0)     7960 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value_decimal_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6781 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value_dictionary.py
--rw-r--r--   0 root         (0) root         (0)     6841 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value_dictionary_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7808 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value_int.py
--rw-r--r--   0 root         (0) root         (0)     7888 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value_int_all_of.py
--rw-r--r--   0 root         (0) root         (0)     6549 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value_string.py
--rw-r--r--   0 root         (0) root         (0)     6609 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value_string_all_of.py
--rw-r--r--   0 root         (0) root         (0)     4028 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/result_value_type.py
--rw-r--r--   0 root         (0) root         (0)     3353 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/scaling_methodology.py
--rw-r--r--   0 root         (0) root         (0)     5426 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/schedule.py
--rw-r--r--   0 root         (0) root         (0)     3458 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/schedule_type.py
--rw-r--r--   0 root         (0) root         (0)     5782 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/schema.py
--rw-r--r--   0 root         (0) root         (0)     4421 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/scope_definition.py
--rw-r--r--   0 root         (0) root         (0)    12312 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/sequence_definition.py
--rw-r--r--   0 root         (0) root         (0)     4545 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/set_legal_entity_identifiers_request.py
--rw-r--r--   0 root         (0) root         (0)     4697 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/set_legal_entity_properties_request.py
--rw-r--r--   0 root         (0) root         (0)     4487 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/set_person_identifiers_request.py
--rw-r--r--   0 root         (0) root         (0)     4849 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/set_person_properties_request.py
--rw-r--r--   0 root         (0) root         (0)    10368 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/set_transaction_configuration_alias.py
--rw-r--r--   0 root         (0) root         (0)     6684 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/set_transaction_configuration_source_request.py
--rw-r--r--   0 root         (0) root         (0)    11343 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/side_configuration_data.py
--rw-r--r--   0 root         (0) root         (0)    10811 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/side_configuration_data_request.py
--rw-r--r--   0 root         (0) root         (0)    15304 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/side_definition.py
--rw-r--r--   0 root         (0) root         (0)    13012 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/side_definition_request.py
--rw-r--r--   0 root         (0) root         (0)    14459 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/simple_instrument.py
--rw-r--r--   0 root         (0) root         (0)    14599 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/simple_instrument_all_of.py
--rw-r--r--   0 root         (0) root         (0)     3305 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/sort_order.py
--rw-r--r--   0 root         (0) root         (0)     9596 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/step_schedule.py
--rw-r--r--   0 root         (0) root         (0)     9696 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/step_schedule_all_of.py
--rw-r--r--   0 root         (0) root         (0)    10119 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/stock_split_event.py
--rw-r--r--   0 root         (0) root         (0)    10219 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/stock_split_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)     9229 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/stream.py
--rw-r--r--   0 root         (0) root         (0)     3478 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/string_comparison_type.py
--rw-r--r--   0 root         (0) root         (0)    10092 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/structured_result_data.py
--rw-r--r--   0 root         (0) root         (0)     9903 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/structured_result_data_id.py
--rw-r--r--   0 root         (0) root         (0)     7997 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/sub_holding_key_value_equals.py
--rw-r--r--   0 root         (0) root         (0)     8077 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/sub_holding_key_value_equals_all_of.py
--rw-r--r--   0 root         (0) root         (0)     9013 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/supported_analytics_internal_request.py
--rw-r--r--   0 root         (0) root         (0)     9501 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/target_tax_lot.py
--rw-r--r--   0 root         (0) root         (0)     9697 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/target_tax_lot_request.py
--rw-r--r--   0 root         (0) root         (0)     9358 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/tax_rule.py
--rw-r--r--   0 root         (0) root         (0)    12276 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/tax_rule_set.py
--rw-r--r--   0 root         (0) root         (0)    18130 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/term_deposit.py
--rw-r--r--   0 root         (0) root         (0)    18290 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/term_deposit_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7853 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/touch.py
--rw-r--r--   0 root         (0) root         (0)     4932 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/trade_ticket.py
--rw-r--r--   0 root         (0) root         (0)     3377 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/trade_ticket_type.py
--rw-r--r--   0 root         (0) root         (0)    30338 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction.py
--rw-r--r--   0 root         (0) root         (0)     7083 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_configuration_data.py
--rw-r--r--   0 root         (0) root         (0)     7208 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_configuration_data_request.py
--rw-r--r--   0 root         (0) root         (0)    15020 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_configuration_movement_data.py
--rw-r--r--   0 root         (0) root         (0)    13934 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_configuration_movement_data_request.py
--rw-r--r--   0 root         (0) root         (0)    14164 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_configuration_type_alias.py
--rw-r--r--   0 root         (0) root         (0)     5083 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_price.py
--rw-r--r--   0 root         (0) root         (0)     3352 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_price_type.py
--rw-r--r--   0 root         (0) root         (0)     6459 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_property_mapping.py
--rw-r--r--   0 root         (0) root         (0)     6568 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_property_mapping_request.py
--rw-r--r--   0 root         (0) root         (0)     3349 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_query_mode.py
--rw-r--r--   0 root         (0) root         (0)     9881 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_query_parameters.py
--rw-r--r--   0 root         (0) root         (0)    11041 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_reconciliation_request.py
--rw-r--r--   0 root         (0) root         (0)    25203 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_request.py
--rw-r--r--   0 root         (0) root         (0)     3555 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_roles.py
--rw-r--r--   0 root         (0) root         (0)     6795 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_set_configuration_data.py
--rw-r--r--   0 root         (0) root         (0)     6484 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_set_configuration_data_request.py
--rw-r--r--   0 root         (0) root         (0)     3358 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_status.py
--rw-r--r--   0 root         (0) root         (0)     7475 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_type.py
--rw-r--r--   0 root         (0) root         (0)    12110 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_type_alias.py
--rw-r--r--   0 root         (0) root         (0)    15230 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_type_movement.py
--rw-r--r--   0 root         (0) root         (0)     7286 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_type_property_mapping.py
--rw-r--r--   0 root         (0) root         (0)     6883 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transaction_type_request.py
--rw-r--r--   0 root         (0) root         (0)     5076 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transactions_reconciliations_response.py
--rw-r--r--   0 root         (0) root         (0)    12319 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transition_event.py
--rw-r--r--   0 root         (0) root         (0)    12479 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/transition_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)     7647 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/translate_instrument_definitions_request.py
--rw-r--r--   0 root         (0) root         (0)     7420 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/translate_instrument_definitions_response.py
--rw-r--r--   0 root         (0) root         (0)     7057 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/translate_trade_ticket_request.py
--rw-r--r--   0 root         (0) root         (0)     7224 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/translate_trade_tickets_response.py
--rw-r--r--   0 root         (0) root         (0)    12563 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/trigger_event.py
--rw-r--r--   0 root         (0) root         (0)    12703 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/trigger_event_all_of.py
--rw-r--r--   0 root         (0) root         (0)     9765 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/typed_resource_id.py
--rw-r--r--   0 root         (0) root         (0)     3345 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/unit_schema.py
--rw-r--r--   0 root         (0) root         (0)     3375 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/unmatched_holding_method.py
--rw-r--r--   0 root         (0) root         (0)     7389 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/update_calendar_request.py
--rw-r--r--   0 root         (0) root         (0)     8384 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/update_custom_entity_definition_request.py
--rw-r--r--   0 root         (0) root         (0)     8527 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/update_cut_label_definition_request.py
--rw-r--r--   0 root         (0) root         (0)     9293 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/update_data_type_request.py
--rw-r--r--   0 root         (0) root         (0)     7187 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/update_instrument_identifier_request.py
--rw-r--r--   0 root         (0) root         (0)     5732 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/update_portfolio_group_request.py
--rw-r--r--   0 root         (0) root         (0)     5684 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/update_portfolio_request.py
--rw-r--r--   0 root         (0) root         (0)     6201 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/update_property_definition_request.py
--rw-r--r--   0 root         (0) root         (0)    10184 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/update_relationship_definition_request.py
--rw-r--r--   0 root         (0) root         (0)     8155 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/update_tax_rule_set_request.py
--rw-r--r--   0 root         (0) root         (0)     7868 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/update_unit_request.py
--rw-r--r--   0 root         (0) root         (0)     4423 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_cds_flow_conventions_request.py
--rw-r--r--   0 root         (0) root         (0)     5591 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_complex_market_data_request.py
--rw-r--r--   0 root         (0) root         (0)    13956 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_corporate_action_request.py
--rw-r--r--   0 root         (0) root         (0)     7350 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_corporate_actions_response.py
--rw-r--r--   0 root         (0) root         (0)     4691 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_counterparty_agreement_request.py
--rw-r--r--   0 root         (0) root         (0)     4423 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_credit_support_annex_request.py
--rw-r--r--   0 root         (0) root         (0)     7423 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_custom_entities_response.py
--rw-r--r--   0 root         (0) root         (0)     4488 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_custom_entity_access_metadata_request.py
--rw-r--r--   0 root         (0) root         (0)     4292 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_flow_conventions_request.py
--rw-r--r--   0 root         (0) root         (0)     4292 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_index_convention_request.py
--rw-r--r--   0 root         (0) root         (0)    11530 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_instrument_event_request.py
--rw-r--r--   0 root         (0) root         (0)     7374 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_instrument_events_response.py
--rw-r--r--   0 root         (0) root         (0)     5336 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_instrument_properties_response.py
--rw-r--r--   0 root         (0) root         (0)     7966 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_instrument_property_request.py
--rw-r--r--   0 root         (0) root         (0)     8362 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_instruments_response.py
--rw-r--r--   0 root         (0) root         (0)     4480 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_legal_entity_access_metadata_request.py
--rw-r--r--   0 root         (0) root         (0)    11115 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_legal_entity_request.py
--rw-r--r--   0 root         (0) root         (0)     4422 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_person_access_metadata_request.py
--rw-r--r--   0 root         (0) root         (0)     9117 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_person_request.py
--rw-r--r--   0 root         (0) root         (0)     4652 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_portfolio_access_metadata_request.py
--rw-r--r--   0 root         (0) root         (0)     4710 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_portfolio_group_access_metadata_request.py
--rw-r--r--   0 root         (0) root         (0)     7446 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_portfolio_transactions_response.py
--rw-r--r--   0 root         (0) root         (0)     5639 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_quote_access_metadata_rule_request.py
--rw-r--r--   0 root         (0) root         (0)     7602 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_quote_request.py
--rw-r--r--   0 root         (0) root         (0)     7044 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_quotes_response.py
--rw-r--r--   0 root         (0) root         (0)     5700 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_recipe_request.py
--rw-r--r--   0 root         (0) root         (0)    10645 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_reference_portfolio_constituents_request.py
--rw-r--r--   0 root         (0) root         (0)     5744 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_reference_portfolio_constituents_response.py
--rw-r--r--   0 root         (0) root         (0)     7265 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_result_values_data_request.py
--rw-r--r--   0 root         (0) root         (0)     8081 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_returns_response.py
--rw-r--r--   0 root         (0) root         (0)     6072 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_single_structured_data_response.py
--rw-r--r--   0 root         (0) root         (0)     7225 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_structured_data_response.py
--rw-r--r--   0 root         (0) root         (0)     5014 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_structured_result_data_request.py
--rw-r--r--   0 root         (0) root         (0)     6948 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/upsert_transaction_properties_response.py
--rw-r--r--   0 root         (0) root         (0)     3793 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/user.py
--rw-r--r--   0 root         (0) root         (0)    21405 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/valuation_request.py
--rw-r--r--   0 root         (0) root         (0)    13908 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/valuation_schedule.py
--rw-r--r--   0 root         (0) root         (0)     8627 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/valuations_reconciliation_request.py
--rw-r--r--   0 root         (0) root         (0)     4004 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/value_type.py
--rw-r--r--   0 root         (0) root         (0)     8896 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/vendor_dependency.py
--rw-r--r--   0 root         (0) root         (0)     8996 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/vendor_dependency_all_of.py
--rw-r--r--   0 root         (0) root         (0)     3528 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/vendor_library.py
--rw-r--r--   0 root         (0) root         (0)    15639 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/vendor_model_rule.py
--rw-r--r--   0 root         (0) root         (0)    11534 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/version.py
--rw-r--r--   0 root         (0) root         (0)     6388 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/version_summary_dto.py
--rw-r--r--   0 root         (0) root         (0)     8591 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/versioned_resource_list_of_a2_b_data_record.py
--rw-r--r--   0 root         (0) root         (0)     8719 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/versioned_resource_list_of_a2_b_movement_record.py
--rw-r--r--   0 root         (0) root         (0)     8399 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/versioned_resource_list_of_je_lines.py
--rw-r--r--   0 root         (0) root         (0)     8719 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/versioned_resource_list_of_output_transaction.py
--rw-r--r--   0 root         (0) root         (0)     8687 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/versioned_resource_list_of_portfolio_holding.py
--rw-r--r--   0 root         (0) root         (0)     8527 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/versioned_resource_list_of_transaction.py
--rw-r--r--   0 root         (0) root         (0)    10455 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/versioned_resource_list_with_warnings_of_portfolio_holding.py
--rw-r--r--   0 root         (0) root         (0)     4964 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/virtual_document.py
--rw-r--r--   0 root         (0) root         (0)     5221 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/virtual_document_row.py
--rw-r--r--   0 root         (0) root         (0)     4936 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/warning.py
--rw-r--r--   0 root         (0) root         (0)     5793 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/weekend_mask.py
--rw-r--r--   0 root         (0) root         (0)     8441 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/weighted_instrument.py
--rw-r--r--   0 root         (0) root         (0)     4479 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/weighted_instruments.py
--rw-r--r--   0 root         (0) root         (0)    11018 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/yield_curve_data.py
--rw-r--r--   0 root         (0) root         (0)    11138 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/models/yield_curve_data_all_of.py
--rw-r--r--   0 root         (0) root         (0)    13517 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/rest.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:15:02.781485 lusid-sdk-preview-1.0.8/lusid/tcp/
--rw-r--r--   0 root         (0) root         (0)       93 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/tcp/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5321 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/tcp/tcp_keep_alive_probes.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:15:02.782485 lusid-sdk-preview-1.0.8/lusid/utilities/
--rw-r--r--   0 root         (0) root         (0)      432 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/utilities/__init__.py
--rw-r--r--   0 root         (0) root         (0)     6434 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/utilities/api_client_builder.py
--rw-r--r--   0 root         (0) root         (0)     5397 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/utilities/api_client_factory.py
--rw-r--r--   0 root         (0) root         (0)     3970 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/utilities/api_configuration.py
--rw-r--r--   0 root         (0) root         (0)     4065 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/utilities/api_configuration_loader.py
--rw-r--r--   0 root         (0) root         (0)     1030 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/utilities/config_keys.json
--rw-r--r--   0 root         (0) root         (0)     1236 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/utilities/lusid_retry.py
--rw-r--r--   0 root         (0) root         (0)     1725 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/utilities/proxy_config.py
--rw-r--r--   0 root         (0) root         (0)     9701 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/lusid/utilities/refreshing_token.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:15:02.783485 lusid-sdk-preview-1.0.8/lusid_sdk_preview.egg-info/
--rw-r--r--   0 root         (0) root         (0)      356 2023-03-16 22:15:02.000000 lusid-sdk-preview-1.0.8/lusid_sdk_preview.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    34520 2023-03-16 22:15:02.000000 lusid-sdk-preview-1.0.8/lusid_sdk_preview.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-03-16 22:15:02.000000 lusid-sdk-preview-1.0.8/lusid_sdk_preview.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       97 2023-03-16 22:15:02.000000 lusid-sdk-preview-1.0.8/lusid_sdk_preview.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        6 2023-03-16 22:15:02.000000 lusid-sdk-preview-1.0.8/lusid_sdk_preview.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       38 2023-03-16 22:15:02.783485 lusid-sdk-preview-1.0.8/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     2218 2023-03-16 22:07:26.000000 lusid-sdk-preview-1.0.8/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:59:44.509232 lusid-sdk-preview-1.0.9/
+-rw-r--r--   0 root         (0) root         (0)       40 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      356 2023-03-16 22:59:44.509232 lusid-sdk-preview-1.0.9/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)   135821 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:59:44.427232 lusid-sdk-preview-1.0.9/lusid/
+-rw-r--r--   0 root         (0) root         (0)    60804 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/__init__.py
+-rw-r--r--   0 root         (0) root         (0)       22 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/__version__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:59:44.435232 lusid-sdk-preview-1.0.9/lusid/api/
+-rw-r--r--   0 root         (0) root         (0)     3141 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    67980 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/abor_api.py
+-rw-r--r--   0 root         (0) root         (0)    57048 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/abor_configuration_api.py
+-rw-r--r--   0 root         (0) root         (0)    41843 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/aggregation_api.py
+-rw-r--r--   0 root         (0) root         (0)    39961 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/allocations_api.py
+-rw-r--r--   0 root         (0) root         (0)    21666 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/application_metadata_api.py
+-rw-r--r--   0 root         (0) root         (0)    38741 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/blocks_api.py
+-rw-r--r--   0 root         (0) root         (0)   128574 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/calendars_api.py
+-rw-r--r--   0 root         (0) root         (0)   123254 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/chart_of_accounts_api.py
+-rw-r--r--   0 root         (0) root         (0)    43662 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/complex_market_data_api.py
+-rw-r--r--   0 root         (0) root         (0)    89888 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/compliance_api.py
+-rw-r--r--   0 root         (0) root         (0)    37217 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/configuration_recipe_api.py
+-rw-r--r--   0 root         (0) root         (0)   104789 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/conventions_api.py
+-rw-r--r--   0 root         (0) root         (0)   102508 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/corporate_action_sources_api.py
+-rw-r--r--   0 root         (0) root         (0)    71069 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/counterparties_api.py
+-rw-r--r--   0 root         (0) root         (0)   177505 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/custom_entities_api.py
+-rw-r--r--   0 root         (0) root         (0)    36859 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/custom_entity_definitions_api.py
+-rw-r--r--   0 root         (0) root         (0)    42656 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/cut_label_definitions_api.py
+-rw-r--r--   0 root         (0) root         (0)    74817 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/data_types_api.py
+-rw-r--r--   0 root         (0) root         (0)    21097 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/derived_transaction_portfolios_api.py
+-rw-r--r--   0 root         (0) root         (0)    11461 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/entities_api.py
+-rw-r--r--   0 root         (0) root         (0)    39311 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/executions_api.py
+-rw-r--r--   0 root         (0) root         (0)    36340 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/instrument_events_api.py
+-rw-r--r--   0 root         (0) root         (0)   228924 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/instruments_api.py
+-rw-r--r--   0 root         (0) root         (0)   254636 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/legal_entities_api.py
+-rw-r--r--   0 root         (0) root         (0)    25684 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/order_graph_api.py
+-rw-r--r--   0 root         (0) root         (0)    40371 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/order_instructions_api.py
+-rw-r--r--   0 root         (0) root         (0)    39234 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/orders_api.py
+-rw-r--r--   0 root         (0) root         (0)    39027 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/packages_api.py
+-rw-r--r--   0 root         (0) root         (0)    39885 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/participations_api.py
+-rw-r--r--   0 root         (0) root         (0)   223041 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/persons_api.py
+-rw-r--r--   0 root         (0) root         (0)    39313 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/placements_api.py
+-rw-r--r--   0 root         (0) root         (0)   352873 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/portfolio_groups_api.py
+-rw-r--r--   0 root         (0) root         (0)   331977 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/portfolios_api.py
+-rw-r--r--   0 root         (0) root         (0)    58891 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/property_definitions_api.py
+-rw-r--r--   0 root         (0) root         (0)   102292 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/quotes_api.py
+-rw-r--r--   0 root         (0) root         (0)    70602 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/reconciliations_api.py
+-rw-r--r--   0 root         (0) root         (0)    46619 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/reference_portfolio_api.py
+-rw-r--r--   0 root         (0) root         (0)    27926 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/relation_definitions_api.py
+-rw-r--r--   0 root         (0) root         (0)    23551 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/relations_api.py
+-rw-r--r--   0 root         (0) root         (0)    51157 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/relationship_definitions_api.py
+-rw-r--r--   0 root         (0) root         (0)    22583 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/relationships_api.py
+-rw-r--r--   0 root         (0) root         (0)    27642 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/schemas_api.py
+-rw-r--r--   0 root         (0) root         (0)     8323 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/scopes_api.py
+-rw-r--r--   0 root         (0) root         (0)    48095 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/search_api.py
+-rw-r--r--   0 root         (0) root         (0)    39247 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/sequences_api.py
+-rw-r--r--   0 root         (0) root         (0)    75616 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/structured_result_data_api.py
+-rw-r--r--   0 root         (0) root         (0)    55507 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/system_configuration_api.py
+-rw-r--r--   0 root         (0) root         (0)    48105 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/tax_rule_sets_api.py
+-rw-r--r--   0 root         (0) root         (0)    47798 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/transaction_configuration_api.py
+-rw-r--r--   0 root         (0) root         (0)    53858 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/transaction_fees_api.py
+-rw-r--r--   0 root         (0) root         (0)   516747 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/transaction_portfolios_api.py
+-rw-r--r--   0 root         (0) root         (0)    18228 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api/translation_api.py
+-rw-r--r--   0 root         (0) root         (0)    27344 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/api_client.py
+-rw-r--r--   0 root         (0) root         (0)    16563 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/configuration.py
+-rw-r--r--   0 root         (0) root         (0)     5079 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/exceptions.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:59:44.507232 lusid-sdk-preview-1.0.9/lusid/models/
+-rw-r--r--   0 root         (0) root         (0)    56960 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     6340 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/a2_b_breakdown.py
+-rw-r--r--   0 root         (0) root         (0)     5185 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/a2_b_category.py
+-rw-r--r--   0 root         (0) root         (0)    17994 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/a2_b_data_record.py
+-rw-r--r--   0 root         (0) root         (0)    21249 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/a2_b_movement_record.py
+-rw-r--r--   0 root         (0) root         (0)    10451 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/abor.py
+-rw-r--r--   0 root         (0) root         (0)    11319 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/abor_configuration.py
+-rw-r--r--   0 root         (0) root         (0)     7071 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/abor_configuration_properties.py
+-rw-r--r--   0 root         (0) root         (0)    10944 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/abor_configuration_request.py
+-rw-r--r--   0 root         (0) root         (0)     6733 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/abor_properties.py
+-rw-r--r--   0 root         (0) root         (0)     9860 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/abor_request.py
+-rw-r--r--   0 root         (0) root         (0)     7104 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/access_controlled_action.py
+-rw-r--r--   0 root         (0) root         (0)     8867 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/access_controlled_resource.py
+-rw-r--r--   0 root         (0) root         (0)     8023 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/access_metadata_operation.py
+-rw-r--r--   0 root         (0) root         (0)     5784 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/access_metadata_value.py
+-rw-r--r--   0 root         (0) root         (0)    11977 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/account.py
+-rw-r--r--   0 root         (0) root         (0)     6811 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/account_properties.py
+-rw-r--r--   0 root         (0) root         (0)     3558 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/accounting_method.py
+-rw-r--r--   0 root         (0) root         (0)     6743 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/accounts_upsert_response.py
+-rw-r--r--   0 root         (0) root         (0)     7198 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/action_id.py
+-rw-r--r--   0 root         (0) root         (0)     4725 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/action_result_of_portfolio.py
+-rw-r--r--   0 root         (0) root         (0)     7222 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/add_business_days_to_date_request.py
+-rw-r--r--   0 root         (0) root         (0)     4157 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/add_business_days_to_date_response.py
+-rw-r--r--   0 root         (0) root         (0)    10980 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/address_definition.py
+-rw-r--r--   0 root         (0) root         (0)     6118 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/address_key_filter.py
+-rw-r--r--   0 root         (0) root         (0)     9172 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/address_key_option_definition.py
+-rw-r--r--   0 root         (0) root         (0)     6832 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/adjust_holding.py
+-rw-r--r--   0 root         (0) root         (0)    12008 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/adjust_holding_for_date_request.py
+-rw-r--r--   0 root         (0) root         (0)    10262 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/adjust_holding_request.py
+-rw-r--r--   0 root         (0) root         (0)     7500 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/aggregate_spec.py
+-rw-r--r--   0 root         (0) root         (0)    13024 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/aggregated_return.py
+-rw-r--r--   0 root         (0) root         (0)    13772 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/aggregated_returns_request.py
+-rw-r--r--   0 root         (0) root         (0)     6028 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/aggregated_returns_response.py
+-rw-r--r--   0 root         (0) root         (0)    10298 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/aggregation.py
+-rw-r--r--   0 root         (0) root         (0)     4009 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/aggregation_context.py
+-rw-r--r--   0 root         (0) root         (0)     7085 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/aggregation_measure_failure_detail.py
+-rw-r--r--   0 root         (0) root         (0)     3885 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/aggregation_op.py
+-rw-r--r--   0 root         (0) root         (0)     8775 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/aggregation_options.py
+-rw-r--r--   0 root         (0) root         (0)    25169 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/aggregation_query.py
+-rw-r--r--   0 root         (0) root         (0)     3506 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/aggregation_type.py
+-rw-r--r--   0 root         (0) root         (0)    24848 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/allocation.py
+-rw-r--r--   0 root         (0) root         (0)    21188 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/allocation_request.py
+-rw-r--r--   0 root         (0) root         (0)     4436 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/allocation_set_request.py
+-rw-r--r--   0 root         (0) root         (0)    12994 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/amortisation_event.py
+-rw-r--r--   0 root         (0) root         (0)    13134 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/amortisation_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7168 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/annul_quotes_response.py
+-rw-r--r--   0 root         (0) root         (0)     6065 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/annul_single_structured_data_response.py
+-rw-r--r--   0 root         (0) root         (0)     7181 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/annul_structured_data_response.py
+-rw-r--r--   0 root         (0) root         (0)     3507 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/asset_class.py
+-rw-r--r--   0 root         (0) root         (0)     7902 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/barrier.py
+-rw-r--r--   0 root         (0) root         (0)    10814 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/basket.py
+-rw-r--r--   0 root         (0) root         (0)    10914 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/basket_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7620 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/basket_identifier.py
+-rw-r--r--   0 root         (0) root         (0)     7230 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/batch_adjust_holdings_response.py
+-rw-r--r--   0 root         (0) root         (0)     7647 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/batch_upsert_portfolio_transactions_response.py
+-rw-r--r--   0 root         (0) root         (0)    18549 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/block.py
+-rw-r--r--   0 root         (0) root         (0)    15838 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/block_request.py
+-rw-r--r--   0 root         (0) root         (0)     4109 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/block_set_request.py
+-rw-r--r--   0 root         (0) root         (0)    22931 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/bond.py
+-rw-r--r--   0 root         (0) root         (0)    23191 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/bond_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    14817 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/bond_default_event.py
+-rw-r--r--   0 root         (0) root         (0)    14977 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/bond_default_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    23520 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/bucketed_cash_flow_request.py
+-rw-r--r--   0 root         (0) root         (0)    10365 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/bucketed_cash_flow_response.py
+-rw-r--r--   0 root         (0) root         (0)     7739 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/calculation_info.py
+-rw-r--r--   0 root         (0) root         (0)     9031 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/calendar.py
+-rw-r--r--   0 root         (0) root         (0)    13374 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/calendar_date.py
+-rw-r--r--   0 root         (0) root         (0)    13183 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cap_floor.py
+-rw-r--r--   0 root         (0) root         (0)    13323 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cap_floor_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7707 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cash_dependency.py
+-rw-r--r--   0 root         (0) root         (0)     7787 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cash_dependency_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     9845 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cash_dividend_event.py
+-rw-r--r--   0 root         (0) root         (0)     9945 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cash_dividend_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10169 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cash_flow_event.py
+-rw-r--r--   0 root         (0) root         (0)    10269 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cash_flow_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10510 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cash_flow_lineage.py
+-rw-r--r--   0 root         (0) root         (0)    11249 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cash_flow_value.py
+-rw-r--r--   0 root         (0) root         (0)    11389 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cash_flow_value_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6768 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cash_flow_value_set.py
+-rw-r--r--   0 root         (0) root         (0)     6828 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cash_flow_value_set_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6856 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cash_ladder_record.py
+-rw-r--r--   0 root         (0) root         (0)    10170 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cash_perpetual.py
+-rw-r--r--   0 root         (0) root         (0)    10270 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cash_perpetual_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    24112 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cds_flow_conventions.py
+-rw-r--r--   0 root         (0) root         (0)    17378 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cds_index.py
+-rw-r--r--   0 root         (0) root         (0)    17578 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cds_index_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10137 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cds_protection_detail_specification.py
+-rw-r--r--   0 root         (0) root         (0)    11015 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/change.py
+-rw-r--r--   0 root         (0) root         (0)    10714 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/change_history.py
+-rw-r--r--   0 root         (0) root         (0)     3354 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/change_history_action.py
+-rw-r--r--   0 root         (0) root         (0)     8704 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/change_item.py
+-rw-r--r--   0 root         (0) root         (0)     9356 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/chart_of_accounts.py
+-rw-r--r--   0 root         (0) root         (0)     7025 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/chart_of_accounts_properties.py
+-rw-r--r--   0 root         (0) root         (0)     8946 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/chart_of_accounts_request.py
+-rw-r--r--   0 root         (0) root         (0)     7846 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/close_event.py
+-rw-r--r--   0 root         (0) root         (0)     7926 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/close_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    15717 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/complete_portfolio.py
+-rw-r--r--   0 root         (0) root         (0)    12168 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/complete_relation.py
+-rw-r--r--   0 root         (0) root         (0)    14719 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/complete_relationship.py
+-rw-r--r--   0 root         (0) root         (0)    11257 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/complex_bond.py
+-rw-r--r--   0 root         (0) root         (0)    11357 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/complex_bond_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7096 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/complex_market_data.py
+-rw-r--r--   0 root         (0) root         (0)    11521 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/complex_market_data_id.py
+-rw-r--r--   0 root         (0) root         (0)     5721 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/compliance_breached_order_info.py
+-rw-r--r--   0 root         (0) root         (0)    17899 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/compliance_rule.py
+-rw-r--r--   0 root         (0) root         (0)    16917 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/compliance_rule_result.py
+-rw-r--r--   0 root         (0) root         (0)    19906 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/compliance_rule_upsert_request.py
+-rw-r--r--   0 root         (0) root         (0)     4260 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/compliance_rule_upsert_response.py
+-rw-r--r--   0 root         (0) root         (0)    13025 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/compliance_run_info.py
+-rw-r--r--   0 root         (0) root         (0)    11637 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/compounding.py
+-rw-r--r--   0 root         (0) root         (0)    14328 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/configuration_recipe.py
+-rw-r--r--   0 root         (0) root         (0)    15247 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/configuration_recipe_snippet.py
+-rw-r--r--   0 root         (0) root         (0)     6181 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/constituents_adjustment_header.py
+-rw-r--r--   0 root         (0) root         (0)    19498 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/contract_for_difference.py
+-rw-r--r--   0 root         (0) root         (0)    19718 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/contract_for_difference_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10863 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/corporate_action.py
+-rw-r--r--   0 root         (0) root         (0)     9857 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/corporate_action_source.py
+-rw-r--r--   0 root         (0) root         (0)     5718 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/corporate_action_transition.py
+-rw-r--r--   0 root         (0) root         (0)    10625 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/corporate_action_transition_component.py
+-rw-r--r--   0 root         (0) root         (0)     7357 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/corporate_action_transition_component_request.py
+-rw-r--r--   0 root         (0) root         (0)     5646 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/corporate_action_transition_request.py
+-rw-r--r--   0 root         (0) root         (0)    11822 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/counterparty_agreement.py
+-rw-r--r--   0 root         (0) root         (0)     8524 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/counterparty_risk_information.py
+-rw-r--r--   0 root         (0) root         (0)     6161 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/counterparty_signatory.py
+-rw-r--r--   0 root         (0) root         (0)    10189 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_calendar_request.py
+-rw-r--r--   0 root         (0) root         (0)    12686 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_corporate_action_source_request.py
+-rw-r--r--   0 root         (0) root         (0)     9424 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_cut_label_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)     4774 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_data_map_request.py
+-rw-r--r--   0 root         (0) root         (0)    20417 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_data_type_request.py
+-rw-r--r--   0 root         (0) root         (0)    13518 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_date_request.py
+-rw-r--r--   0 root         (0) root         (0)    15511 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_derived_property_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)    20890 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_derived_transaction_portfolio_request.py
+-rw-r--r--   0 root         (0) root         (0)     4462 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_portfolio_details.py
+-rw-r--r--   0 root         (0) root         (0)    12383 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_portfolio_group_request.py
+-rw-r--r--   0 root         (0) root         (0)    17579 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_property_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)     9307 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_recipe_request.py
+-rw-r--r--   0 root         (0) root         (0)    11661 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_reference_portfolio_request.py
+-rw-r--r--   0 root         (0) root         (0)    17353 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_relation_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)     5899 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_relation_request.py
+-rw-r--r--   0 root         (0) root         (0)    22106 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_relationship_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)    10113 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_relationship_request.py
+-rw-r--r--   0 root         (0) root         (0)    11654 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_sequence_request.py
+-rw-r--r--   0 root         (0) root         (0)    10254 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_tax_rule_set_request.py
+-rw-r--r--   0 root         (0) root         (0)    20612 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_transaction_portfolio_request.py
+-rw-r--r--   0 root         (0) root         (0)     9310 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/create_unit_definition.py
+-rw-r--r--   0 root         (0) root         (0)    18199 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/credit_default_swap.py
+-rw-r--r--   0 root         (0) root         (0)    18399 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/credit_default_swap_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7521 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/credit_rating.py
+-rw-r--r--   0 root         (0) root         (0)    16567 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/credit_spread_curve_data.py
+-rw-r--r--   0 root         (0) root         (0)    16767 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/credit_spread_curve_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    20912 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/credit_support_annex.py
+-rw-r--r--   0 root         (0) root         (0)     3450 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/criterion_type.py
+-rw-r--r--   0 root         (0) root         (0)     4642 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/currency_and_amount.py
+-rw-r--r--   0 root         (0) root         (0)    15766 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/custodian_account.py
+-rw-r--r--   0 root         (0) root         (0)     7048 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/custodian_account_properties.py
+-rw-r--r--   0 root         (0) root         (0)    18313 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/custodian_account_request.py
+-rw-r--r--   0 root         (0) root         (0)     7218 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/custodian_accounts_upsert_response.py
+-rw-r--r--   0 root         (0) root         (0)    11807 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/custom_entity_definition.py
+-rw-r--r--   0 root         (0) root         (0)    10534 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/custom_entity_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)     8081 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/custom_entity_field.py
+-rw-r--r--   0 root         (0) root         (0)    11325 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/custom_entity_field_definition.py
+-rw-r--r--   0 root         (0) root         (0)    12486 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/custom_entity_id.py
+-rw-r--r--   0 root         (0) root         (0)     8385 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/custom_entity_request.py
+-rw-r--r--   0 root         (0) root         (0)    13657 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/custom_entity_response.py
+-rw-r--r--   0 root         (0) root         (0)     8560 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cut_label_definition.py
+-rw-r--r--   0 root         (0) root         (0)     4563 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/cut_local_time.py
+-rw-r--r--   0 root         (0) root         (0)    12478 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/data_definition.py
+-rw-r--r--   0 root         (0) root         (0)     6911 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/data_map_key.py
+-rw-r--r--   0 root         (0) root         (0)     4637 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/data_mapping.py
+-rw-r--r--   0 root         (0) root         (0)    15955 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/data_type.py
+-rw-r--r--   0 root         (0) root         (0)    15138 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/data_type_summary.py
+-rw-r--r--   0 root         (0) root         (0)     3314 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/data_type_value_range.py
+-rw-r--r--   0 root         (0) root         (0)    14147 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/date_attributes.py
+-rw-r--r--   0 root         (0) root         (0)     4864 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/date_range.py
+-rw-r--r--   0 root         (0) root         (0)     3369 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/date_time_comparison_type.py
+-rw-r--r--   0 root         (0) root         (0)     3458 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/day_of_week.py
+-rw-r--r--   0 root         (0) root         (0)     5764 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/delete_accounts_response.py
+-rw-r--r--   0 root         (0) root         (0)     6213 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/delete_custodian_accounts_response.py
+-rw-r--r--   0 root         (0) root         (0)     5179 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/delete_instrument_properties_response.py
+-rw-r--r--   0 root         (0) root         (0)     6116 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/delete_instrument_response.py
+-rw-r--r--   0 root         (0) root         (0)     6132 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/delete_instruments_response.py
+-rw-r--r--   0 root         (0) root         (0)     3280 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/delete_modes.py
+-rw-r--r--   0 root         (0) root         (0)     6079 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/delete_relation_request.py
+-rw-r--r--   0 root         (0) root         (0)    10335 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/delete_relationship_request.py
+-rw-r--r--   0 root         (0) root         (0)     7419 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/deleted_entity_response.py
+-rw-r--r--   0 root         (0) root         (0)     8387 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/dependency_source_filter.py
+-rw-r--r--   0 root         (0) root         (0)     5221 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/described_address_key.py
+-rw-r--r--   0 root         (0) root         (0)    11233 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/discount_factor_curve_data.py
+-rw-r--r--   0 root         (0) root         (0)    11353 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/discount_factor_curve_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7837 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/discounting_dependency.py
+-rw-r--r--   0 root         (0) root         (0)     7917 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/discounting_dependency_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     3409 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/discounting_method.py
+-rw-r--r--   0 root         (0) root         (0)     6228 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/economic_dependency.py
+-rw-r--r--   0 root         (0) root         (0)     3687 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/economic_dependency_type.py
+-rw-r--r--   0 root         (0) root         (0)     6020 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/economic_dependency_with_complex_market_data.py
+-rw-r--r--   0 root         (0) root         (0)     6830 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/economic_dependency_with_quote.py
+-rw-r--r--   0 root         (0) root         (0)     5398 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/empty_model_options.py
+-rw-r--r--   0 root         (0) root         (0)     5438 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/empty_model_options_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6713 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/entity_identifier.py
+-rw-r--r--   0 root         (0) root         (0)     8495 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity.py
+-rw-r--r--   0 root         (0) root         (0)     8575 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11924 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_all_of_identifiers.py
+-rw-r--r--   0 root         (0) root         (0)    11440 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_curve_by_prices_data.py
+-rw-r--r--   0 root         (0) root         (0)    11560 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_curve_by_prices_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    12169 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_curve_dependency.py
+-rw-r--r--   0 root         (0) root         (0)    12289 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_curve_dependency_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7849 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_model_options.py
+-rw-r--r--   0 root         (0) root         (0)     7909 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_model_options_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    24187 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_option.py
+-rw-r--r--   0 root         (0) root         (0)    24487 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_option_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    23696 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_swap.py
+-rw-r--r--   0 root         (0) root         (0)    23956 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_swap_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11506 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_vol_dependency.py
+-rw-r--r--   0 root         (0) root         (0)    11626 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_vol_dependency_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11231 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_vol_surface_data.py
+-rw-r--r--   0 root         (0) root         (0)    11351 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/equity_vol_surface_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6806 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/error_detail.py
+-rw-r--r--   0 root         (0) root         (0)     4531 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/event_date_range.py
+-rw-r--r--   0 root         (0) root         (0)    11841 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/exchange_traded_option.py
+-rw-r--r--   0 root         (0) root         (0)    11961 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/exchange_traded_option_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    23036 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/exchange_traded_option_contract_details.py
+-rw-r--r--   0 root         (0) root         (0)    24122 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/execution.py
+-rw-r--r--   0 root         (0) root         (0)    21469 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/execution_request.py
+-rw-r--r--   0 root         (0) root         (0)     4169 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/execution_set_request.py
+-rw-r--r--   0 root         (0) root         (0)    11000 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/exercise_event.py
+-rw-r--r--   0 root         (0) root         (0)    11120 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/exercise_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10285 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/exotic_instrument.py
+-rw-r--r--   0 root         (0) root         (0)    10365 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/exotic_instrument_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11174 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/expanded_group.py
+-rw-r--r--   0 root         (0) root         (0)    21346 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fee_rule.py
+-rw-r--r--   0 root         (0) root         (0)    24042 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fee_rule_upsert_request.py
+-rw-r--r--   0 root         (0) root         (0)     4904 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fee_rule_upsert_response.py
+-rw-r--r--   0 root         (0) root         (0)     6695 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/field_definition.py
+-rw-r--r--   0 root         (0) root         (0)     8258 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/field_schema.py
+-rw-r--r--   0 root         (0) root         (0)     5658 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/field_value.py
+-rw-r--r--   0 root         (0) root         (0)     5781 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/file_response.py
+-rw-r--r--   0 root         (0) root         (0)    13116 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fixed_leg.py
+-rw-r--r--   0 root         (0) root         (0)    13256 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fixed_leg_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     4915 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fixed_leg_all_of_overrides.py
+-rw-r--r--   0 root         (0) root         (0)    13681 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fixed_schedule.py
+-rw-r--r--   0 root         (0) root         (0)    13881 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fixed_schedule_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    15440 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/float_schedule.py
+-rw-r--r--   0 root         (0) root         (0)    15680 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/float_schedule_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    13373 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/floating_leg.py
+-rw-r--r--   0 root         (0) root         (0)    13513 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/floating_leg_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6592 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/flow_convention_name.py
+-rw-r--r--   0 root         (0) root         (0)    23990 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/flow_conventions.py
+-rw-r--r--   0 root         (0) root         (0)    15807 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/forward_rate_agreement.py
+-rw-r--r--   0 root         (0) root         (0)    15987 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/forward_rate_agreement_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    14013 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/funding_leg.py
+-rw-r--r--   0 root         (0) root         (0)    14133 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/funding_leg_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7410 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/funding_leg_options.py
+-rw-r--r--   0 root         (0) root         (0)     7470 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/funding_leg_options_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    20197 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/future.py
+-rw-r--r--   0 root         (0) root         (0)    20397 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/future_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    21009 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/futures_contract_details.py
+-rw-r--r--   0 root         (0) root         (0)     9180 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_dependency.py
+-rw-r--r--   0 root         (0) root         (0)     9280 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_dependency_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    20192 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forward.py
+-rw-r--r--   0 root         (0) root         (0)    20432 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forward_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    12659 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forward_curve_by_quote_reference.py
+-rw-r--r--   0 root         (0) root         (0)    12799 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forward_curve_by_quote_reference_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    13026 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forward_curve_data.py
+-rw-r--r--   0 root         (0) root         (0)    13186 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forward_curve_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11327 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forward_model_options.py
+-rw-r--r--   0 root         (0) root         (0)    11427 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forward_model_options_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    13322 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forward_pips_curve_data.py
+-rw-r--r--   0 root         (0) root         (0)    13482 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forward_pips_curve_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    13194 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forward_tenor_curve_data.py
+-rw-r--r--   0 root         (0) root         (0)    13354 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forward_tenor_curve_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    13490 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forward_tenor_pips_curve_data.py
+-rw-r--r--   0 root         (0) root         (0)    13650 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forward_tenor_pips_curve_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11788 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forwards_dependency.py
+-rw-r--r--   0 root         (0) root         (0)    11908 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_forwards_dependency_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    28087 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_option.py
+-rw-r--r--   0 root         (0) root         (0)    28447 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_option_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     9436 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_rate_schedule.py
+-rw-r--r--   0 root         (0) root         (0)     9556 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_rate_schedule_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11021 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_swap.py
+-rw-r--r--   0 root         (0) root         (0)    11121 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_swap_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11363 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_vol_dependency.py
+-rw-r--r--   0 root         (0) root         (0)    11483 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_vol_dependency_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11135 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/fx_vol_surface_data.py
+-rw-r--r--   0 root         (0) root         (0)     7028 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/get_cds_flow_conventions_response.py
+-rw-r--r--   0 root         (0) root         (0)     7279 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/get_complex_market_data_response.py
+-rw-r--r--   0 root         (0) root         (0)     7088 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/get_counterparty_agreement_response.py
+-rw-r--r--   0 root         (0) root         (0)     7040 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/get_credit_support_annex_response.py
+-rw-r--r--   0 root         (0) root         (0)     7046 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/get_data_map_response.py
+-rw-r--r--   0 root         (0) root         (0)     6956 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/get_flow_conventions_response.py
+-rw-r--r--   0 root         (0) root         (0)     6956 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/get_index_convention_response.py
+-rw-r--r--   0 root         (0) root         (0)     7371 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/get_instruments_response.py
+-rw-r--r--   0 root         (0) root         (0)     8047 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/get_quotes_response.py
+-rw-r--r--   0 root         (0) root         (0)     5689 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/get_recipe_response.py
+-rw-r--r--   0 root         (0) root         (0)    12030 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/get_reference_portfolio_constituents_response.py
+-rw-r--r--   0 root         (0) root         (0)     7351 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/get_structured_result_data_response.py
+-rw-r--r--   0 root         (0) root         (0)     7222 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/get_virtual_document_response.py
+-rw-r--r--   0 root         (0) root         (0)     5131 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/grouped_result_of_address_key.py
+-rw-r--r--   0 root         (0) root         (0)    12535 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/holding_adjustment.py
+-rw-r--r--   0 root         (0) root         (0)    13889 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/holding_adjustment_with_date.py
+-rw-r--r--   0 root         (0) root         (0)     4577 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/holding_context.py
+-rw-r--r--   0 root         (0) root         (0)    10491 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/holdings_adjustment.py
+-rw-r--r--   0 root         (0) root         (0)     9374 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/holdings_adjustment_header.py
+-rw-r--r--   0 root         (0) root         (0)     3970 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/i_data_record.py
+-rw-r--r--   0 root         (0) root         (0)     6778 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/i_unit_definition_dto.py
+-rw-r--r--   0 root         (0) root         (0)     7949 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/id_selector_definition.py
+-rw-r--r--   0 root         (0) root         (0)     9438 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/identifier_part_schema.py
+-rw-r--r--   0 root         (0) root         (0)    18219 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/index_convention.py
+-rw-r--r--   0 root         (0) root         (0)     7150 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/index_model_options.py
+-rw-r--r--   0 root         (0) root         (0)     7210 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/index_model_options_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11786 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/index_projection_dependency.py
+-rw-r--r--   0 root         (0) root         (0)    11906 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/index_projection_dependency_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7581 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/industry_classifier.py
+-rw-r--r--   0 root         (0) root         (0)    36320 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/inflation_linked_bond.py
+-rw-r--r--   0 root         (0) root         (0)    36720 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/inflation_linked_bond_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    25334 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/inflation_swap.py
+-rw-r--r--   0 root         (0) root         (0)    25634 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/inflation_swap_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10090 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/informational_error_event.py
+-rw-r--r--   0 root         (0) root         (0)    10190 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/informational_error_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    13185 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/informational_event.py
+-rw-r--r--   0 root         (0) root         (0)    13325 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/informational_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    22490 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/inline_valuation_request.py
+-rw-r--r--   0 root         (0) root         (0)     8210 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/inline_valuations_reconciliation_request.py
+-rw-r--r--   0 root         (0) root         (0)     5481 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/input_transition.py
+-rw-r--r--   0 root         (0) root         (0)    19961 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument.py
+-rw-r--r--   0 root         (0) root         (0)    10083 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_capabilities.py
+-rw-r--r--   0 root         (0) root         (0)    16808 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_cash_flow.py
+-rw-r--r--   0 root         (0) root         (0)     9470 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_definition.py
+-rw-r--r--   0 root         (0) root         (0)     8348 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_definition_format.py
+-rw-r--r--   0 root         (0) root         (0)     3320 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_delete_modes.py
+-rw-r--r--   0 root         (0) root         (0)     6924 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_event.py
+-rw-r--r--   0 root         (0) root         (0)    17157 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_event_holder.py
+-rw-r--r--   0 root         (0) root         (0)     4038 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_event_type.py
+-rw-r--r--   0 root         (0) root         (0)     7700 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_id_type_descriptor.py
+-rw-r--r--   0 root         (0) root         (0)     5728 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_id_value.py
+-rw-r--r--   0 root         (0) root         (0)     7134 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_leg.py
+-rw-r--r--   0 root         (0) root         (0)     6699 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_leg_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6118 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_match.py
+-rw-r--r--   0 root         (0) root         (0)     9927 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_payment_diary.py
+-rw-r--r--   0 root         (0) root         (0)     5114 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_payment_diary_leg.py
+-rw-r--r--   0 root         (0) root         (0)    20931 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_payment_diary_row.py
+-rw-r--r--   0 root         (0) root         (0)     6889 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_properties.py
+-rw-r--r--   0 root         (0) root         (0)     6083 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_search_property.py
+-rw-r--r--   0 root         (0) root         (0)     4837 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/instrument_type.py
+-rw-r--r--   0 root         (0) root         (0)    14277 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/interest_rate_swap.py
+-rw-r--r--   0 root         (0) root         (0)    14417 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/interest_rate_swap_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    13510 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/interest_rate_swaption.py
+-rw-r--r--   0 root         (0) root         (0)    13650 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/interest_rate_swaption_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11120 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/ir_vol_cube_data.py
+-rw-r--r--   0 root         (0) root         (0)    11240 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/ir_vol_cube_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     9519 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/ir_vol_dependency.py
+-rw-r--r--   0 root         (0) root         (0)     9619 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/ir_vol_dependency_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     5575 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/is_business_day_response.py
+-rw-r--r--   0 root         (0) root         (0)    24671 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/je_lines.py
+-rw-r--r--   0 root         (0) root         (0)     7963 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/je_lines_query_parameters.py
+-rw-r--r--   0 root         (0) root         (0)     4311 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/label_value_set.py
+-rw-r--r--   0 root         (0) root         (0)    17095 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/leg_definition.py
+-rw-r--r--   0 root         (0) root         (0)    13346 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/legal_entity.py
+-rw-r--r--   0 root         (0) root         (0)     5400 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/level_step.py
+-rw-r--r--   0 root         (0) root         (0)     8320 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/life_cycle_event_lineage.py
+-rw-r--r--   0 root         (0) root         (0)     8841 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/life_cycle_event_value.py
+-rw-r--r--   0 root         (0) root         (0)     8941 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/life_cycle_event_value_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6392 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/link.py
+-rw-r--r--   0 root         (0) root         (0)     6623 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/list_aggregation_reconciliation.py
+-rw-r--r--   0 root         (0) root         (0)    10736 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/list_aggregation_response.py
+-rw-r--r--   0 root         (0) root         (0)     6377 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/list_complex_market_data_with_meta_data_response.py
+-rw-r--r--   0 root         (0) root         (0)     8140 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/lusid_instrument.py
+-rw-r--r--   0 root         (0) root         (0)     9506 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/lusid_problem_details.py
+-rw-r--r--   0 root         (0) root         (0)    26392 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/lusid_trade_ticket.py
+-rw-r--r--   0 root         (0) root         (0)     5947 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/lusid_unique_id.py
+-rw-r--r--   0 root         (0) root         (0)    10706 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/lusid_validation_problem_details.py
+-rw-r--r--   0 root         (0) root         (0)     6589 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/mapped_string.py
+-rw-r--r--   0 root         (0) root         (0)    10565 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/mapping.py
+-rw-r--r--   0 root         (0) root         (0)    10470 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/mapping_rule.py
+-rw-r--r--   0 root         (0) root         (0)     9380 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/market_context.py
+-rw-r--r--   0 root         (0) root         (0)     6867 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/market_context_suppliers.py
+-rw-r--r--   0 root         (0) root         (0)    26172 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/market_data_key_rule.py
+-rw-r--r--   0 root         (0) root         (0)     5841 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/market_data_overrides.py
+-rw-r--r--   0 root         (0) root         (0)    23809 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/market_data_specific_rule.py
+-rw-r--r--   0 root         (0) root         (0)     4198 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/market_data_type.py
+-rw-r--r--   0 root         (0) root         (0)     3493 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/market_observable_type.py
+-rw-r--r--   0 root         (0) root         (0)    14880 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/market_options.py
+-rw-r--r--   0 root         (0) root         (0)     5970 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/market_quote.py
+-rw-r--r--   0 root         (0) root         (0)     5507 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/match_criterion.py
+-rw-r--r--   0 root         (0) root         (0)     4609 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/metric_value.py
+-rw-r--r--   0 root         (0) root         (0)     6042 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/model_options.py
+-rw-r--r--   0 root         (0) root         (0)     3696 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/model_options_type.py
+-rw-r--r--   0 root         (0) root         (0)     7700 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/model_property.py
+-rw-r--r--   0 root         (0) root         (0)     7505 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/model_selection.py
+-rw-r--r--   0 root         (0) root         (0)     4052 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/movement_type.py
+-rw-r--r--   0 root         (0) root         (0)     5119 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/next_value_in_sequence_response.py
+-rw-r--r--   0 root         (0) root         (0)     3431 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/numeric_comparison_type.py
+-rw-r--r--   0 root         (0) root         (0)     5233 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/opaque_dependency.py
+-rw-r--r--   0 root         (0) root         (0)     5273 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/opaque_dependency_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11964 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/opaque_market_data.py
+-rw-r--r--   0 root         (0) root         (0)    12084 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/opaque_market_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6307 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/opaque_model_options.py
+-rw-r--r--   0 root         (0) root         (0)     6367 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/opaque_model_options_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6895 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/open_event.py
+-rw-r--r--   0 root         (0) root         (0)     6955 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/open_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     3304 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/operand_type.py
+-rw-r--r--   0 root         (0) root         (0)     5598 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/operation.py
+-rw-r--r--   0 root         (0) root         (0)     3261 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/operation_type.py
+-rw-r--r--   0 root         (0) root         (0)     3523 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/operator.py
+-rw-r--r--   0 root         (0) root         (0)    22500 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order.py
+-rw-r--r--   0 root         (0) root         (0)     5698 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_by_spec.py
+-rw-r--r--   0 root         (0) root         (0)    11905 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_block.py
+-rw-r--r--   0 root         (0) root         (0)     4124 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_allocation_detail.py
+-rw-r--r--   0 root         (0) root         (0)     5714 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_allocation_synopsis.py
+-rw-r--r--   0 root         (0) root         (0)     4116 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_execution_detail.py
+-rw-r--r--   0 root         (0) root         (0)     5692 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_execution_synopsis.py
+-rw-r--r--   0 root         (0) root         (0)     5911 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_order_detail.py
+-rw-r--r--   0 root         (0) root         (0)     5658 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_order_synopsis.py
+-rw-r--r--   0 root         (0) root         (0)     4116 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_placement_detail.py
+-rw-r--r--   0 root         (0) root         (0)     5686 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_placement_synopsis.py
+-rw-r--r--   0 root         (0) root         (0)    12421 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement.py
+-rw-r--r--   0 root         (0) root         (0)     4156 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement_allocation_detail.py
+-rw-r--r--   0 root         (0) root         (0)     5790 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement_allocation_synopsis.py
+-rw-r--r--   0 root         (0) root         (0)     4148 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement_execution_detail.py
+-rw-r--r--   0 root         (0) root         (0)     5798 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement_execution_synopsis.py
+-rw-r--r--   0 root         (0) root         (0)     4116 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement_order_detail.py
+-rw-r--r--   0 root         (0) root         (0)     4528 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement_order_synopsis.py
+-rw-r--r--   0 root         (0) root         (0)     4410 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement_placement_synopsis.py
+-rw-r--r--   0 root         (0) root         (0)     6603 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_instruction.py
+-rw-r--r--   0 root         (0) root         (0)     5201 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_instruction_request.py
+-rw-r--r--   0 root         (0) root         (0)     4274 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_instruction_set_request.py
+-rw-r--r--   0 root         (0) root         (0)    18756 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_request.py
+-rw-r--r--   0 root         (0) root         (0)     4246 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/order_set_request.py
+-rw-r--r--   0 root         (0) root         (0)     4383 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/otc_confirmation.py
+-rw-r--r--   0 root         (0) root         (0)    33018 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/output_transaction.py
+-rw-r--r--   0 root         (0) root         (0)    10332 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/output_transition.py
+-rw-r--r--   0 root         (0) root         (0)     8950 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/package.py
+-rw-r--r--   0 root         (0) root         (0)     7676 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/package_request.py
+-rw-r--r--   0 root         (0) root         (0)     4139 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/package_set_request.py
+-rw-r--r--   0 root         (0) root         (0)     7217 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_abor.py
+-rw-r--r--   0 root         (0) root         (0)     7581 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_abor_configuration.py
+-rw-r--r--   0 root         (0) root         (0)     7301 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_account.py
+-rw-r--r--   0 root         (0) root         (0)     7385 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_allocation.py
+-rw-r--r--   0 root         (0) root         (0)     7245 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_block.py
+-rw-r--r--   0 root         (0) root         (0)     7329 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_calendar.py
+-rw-r--r--   0 root         (0) root         (0)     7525 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_chart_of_accounts.py
+-rw-r--r--   0 root         (0) root         (0)     7693 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_corporate_action_source.py
+-rw-r--r--   0 root         (0) root         (0)     7553 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_custodian_account.py
+-rw-r--r--   0 root         (0) root         (0)     7721 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_custom_entity_definition.py
+-rw-r--r--   0 root         (0) root         (0)     7665 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_custom_entity_response.py
+-rw-r--r--   0 root         (0) root         (0)     7609 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_cut_label_definition.py
+-rw-r--r--   0 root         (0) root         (0)     7525 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_data_type_summary.py
+-rw-r--r--   0 root         (0) root         (0)     7357 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_execution.py
+-rw-r--r--   0 root         (0) root         (0)     7385 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_instrument.py
+-rw-r--r--   0 root         (0) root         (0)     7693 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_instrument_event_holder.py
+-rw-r--r--   0 root         (0) root         (0)     7413 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_legal_entity.py
+-rw-r--r--   0 root         (0) root         (0)     7245 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_order.py
+-rw-r--r--   0 root         (0) root         (0)     7525 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_order_graph_block.py
+-rw-r--r--   0 root         (0) root         (0)     7637 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_order_graph_placement.py
+-rw-r--r--   0 root         (0) root         (0)     7553 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_order_instruction.py
+-rw-r--r--   0 root         (0) root         (0)     7301 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_package.py
+-rw-r--r--   0 root         (0) root         (0)     7469 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_participation.py
+-rw-r--r--   0 root         (0) root         (0)     7273 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_person.py
+-rw-r--r--   0 root         (0) root         (0)     7357 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_placement.py
+-rw-r--r--   0 root         (0) root         (0)     7833 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_portfolio_group_search_result.py
+-rw-r--r--   0 root         (0) root         (0)     7693 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_portfolio_search_result.py
+-rw-r--r--   0 root         (0) root         (0)     7945 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_property_definition_search_result.py
+-rw-r--r--   0 root         (0) root         (0)     7721 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_relationship_definition.py
+-rw-r--r--   0 root         (0) root         (0)     7609 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_sequence_definition.py
+-rw-r--r--   0 root         (0) root         (0)     7482 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/participation.py
+-rw-r--r--   0 root         (0) root         (0)     6926 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/participation_request.py
+-rw-r--r--   0 root         (0) root         (0)     4229 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/participation_set_request.py
+-rw-r--r--   0 root         (0) root         (0)     8788 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/performance_return.py
+-rw-r--r--   0 root         (0) root         (0)    10181 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/performance_returns_metric.py
+-rw-r--r--   0 root         (0) root         (0)     3393 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/period_type.py
+-rw-r--r--   0 root         (0) root         (0)     3367 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/perpetual_entity_state.py
+-rw-r--r--   0 root         (0) root         (0)     5213 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/perpetual_property.py
+-rw-r--r--   0 root         (0) root         (0)    11043 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/person.py
+-rw-r--r--   0 root         (0) root         (0)    22633 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/placement.py
+-rw-r--r--   0 root         (0) root         (0)    20489 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/placement_request.py
+-rw-r--r--   0 root         (0) root         (0)     4169 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/placement_set_request.py
+-rw-r--r--   0 root         (0) root         (0)    21169 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio.py
+-rw-r--r--   0 root         (0) root         (0)    23700 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio_cash_flow.py
+-rw-r--r--   0 root         (0) root         (0)     8810 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio_cash_ladder.py
+-rw-r--r--   0 root         (0) root         (0)    15147 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio_details.py
+-rw-r--r--   0 root         (0) root         (0)     8460 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio_entity_id.py
+-rw-r--r--   0 root         (0) root         (0)    13607 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio_group.py
+-rw-r--r--   0 root         (0) root         (0)     6996 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio_group_properties.py
+-rw-r--r--   0 root         (0) root         (0)    12953 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio_group_search_result.py
+-rw-r--r--   0 root         (0) root         (0)    17791 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio_holding.py
+-rw-r--r--   0 root         (0) root         (0)     6863 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio_properties.py
+-rw-r--r--   0 root         (0) root         (0)     6775 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio_reconciliation_request.py
+-rw-r--r--   0 root         (0) root         (0)    17336 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio_result_data_key_rule.py
+-rw-r--r--   0 root         (0) root         (0)    17516 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio_result_data_key_rule_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    15510 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio_search_result.py
+-rw-r--r--   0 root         (0) root         (0)     5228 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio_trade_ticket.py
+-rw-r--r--   0 root         (0) root         (0)     3390 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolio_type.py
+-rw-r--r--   0 root         (0) root         (0)     7197 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/portfolios_reconciliation_request.py
+-rw-r--r--   0 root         (0) root         (0)     6022 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/premium.py
+-rw-r--r--   0 root         (0) root         (0)     9445 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/pricing_context.py
+-rw-r--r--   0 root         (0) root         (0)     4322 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/pricing_model.py
+-rw-r--r--   0 root         (0) root         (0)    27514 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/pricing_options.py
+-rw-r--r--   0 root         (0) root         (0)     7870 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/processed_command.py
+-rw-r--r--   0 root         (0) root         (0)    27010 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/property_definition.py
+-rw-r--r--   0 root         (0) root         (0)    27874 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/property_definition_search_result.py
+-rw-r--r--   0 root         (0) root         (0)     3390 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/property_definition_type.py
+-rw-r--r--   0 root         (0) root         (0)     4831 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/property_domain.py
+-rw-r--r--   0 root         (0) root         (0)     7835 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/property_filter.py
+-rw-r--r--   0 root         (0) root         (0)     7969 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/property_interval.py
+-rw-r--r--   0 root         (0) root         (0)     3336 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/property_life_time.py
+-rw-r--r--   0 root         (0) root         (0)     5265 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/property_schema.py
+-rw-r--r--   0 root         (0) root         (0)     3338 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/property_type.py
+-rw-r--r--   0 root         (0) root         (0)     6066 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/property_value.py
+-rw-r--r--   0 root         (0) root         (0)     7834 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/property_value_equals.py
+-rw-r--r--   0 root         (0) root         (0)     7914 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/property_value_equals_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7309 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/property_value_in.py
+-rw-r--r--   0 root         (0) root         (0)     7389 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/property_value_in_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    21310 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/query_bucketed_cash_flows_request.py
+-rw-r--r--   0 root         (0) root         (0)    10450 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/query_cash_flows_request.py
+-rw-r--r--   0 root         (0) root         (0)    12914 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/query_instrument_events_request.py
+-rw-r--r--   0 root         (0) root         (0)    10552 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/query_trade_tickets_request.py
+-rw-r--r--   0 root         (0) root         (0)    10795 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/quote.py
+-rw-r--r--   0 root         (0) root         (0)     5483 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/quote_access_metadata_rule.py
+-rw-r--r--   0 root         (0) root         (0)    15723 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/quote_access_metadata_rule_id.py
+-rw-r--r--   0 root         (0) root         (0)     9612 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/quote_dependency.py
+-rw-r--r--   0 root         (0) root         (0)     9712 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/quote_dependency_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     5783 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/quote_id.py
+-rw-r--r--   0 root         (0) root         (0)     3605 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/quote_instrument_id_type.py
+-rw-r--r--   0 root         (0) root         (0)    14721 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/quote_series_id.py
+-rw-r--r--   0 root         (0) root         (0)     3587 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/quote_type.py
+-rw-r--r--   0 root         (0) root         (0)    11311 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/raw_vendor_event.py
+-rw-r--r--   0 root         (0) root         (0)    11431 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/raw_vendor_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    17980 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/realised_gain_loss.py
+-rw-r--r--   0 root         (0) root         (0)     9883 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reconcile_date_time_rule.py
+-rw-r--r--   0 root         (0) root         (0)     9983 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reconcile_date_time_rule_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     9945 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reconcile_numeric_rule.py
+-rw-r--r--   0 root         (0) root         (0)    10045 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reconcile_numeric_rule_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10716 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reconcile_string_rule.py
+-rw-r--r--   0 root         (0) root         (0)    10816 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reconcile_string_rule_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7788 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reconciled_transaction.py
+-rw-r--r--   0 root         (0) root         (0)    15668 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reconciliation_break.py
+-rw-r--r--   0 root         (0) root         (0)     5468 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reconciliation_left_right_address_key_pair.py
+-rw-r--r--   0 root         (0) root         (0)     7307 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reconciliation_line.py
+-rw-r--r--   0 root         (0) root         (0)    10383 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reconciliation_request.py
+-rw-r--r--   0 root         (0) root         (0)     5245 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reconciliation_response.py
+-rw-r--r--   0 root         (0) root         (0)     5472 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reconciliation_rule.py
+-rw-r--r--   0 root         (0) root         (0)     3546 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reconciliation_rule_type.py
+-rw-r--r--   0 root         (0) root         (0)     5343 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reference_data.py
+-rw-r--r--   0 root         (0) root         (0)    11099 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reference_instrument.py
+-rw-r--r--   0 root         (0) root         (0)    11199 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reference_instrument_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    11192 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reference_portfolio_constituent.py
+-rw-r--r--   0 root         (0) root         (0)     7556 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reference_portfolio_constituent_request.py
+-rw-r--r--   0 root         (0) root         (0)     3408 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reference_portfolio_weight_type.py
+-rw-r--r--   0 root         (0) root         (0)    12677 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/related_entity.py
+-rw-r--r--   0 root         (0) root         (0)    10235 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/relation.py
+-rw-r--r--   0 root         (0) root         (0)    14446 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/relation_definition.py
+-rw-r--r--   0 root         (0) root         (0)    13986 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/relationship.py
+-rw-r--r--   0 root         (0) root         (0)    19714 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/relationship_definition.py
+-rw-r--r--   0 root         (0) root         (0)    25564 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/repo.py
+-rw-r--r--   0 root         (0) root         (0)    25824 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/repo_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    12033 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reset_event.py
+-rw-r--r--   0 root         (0) root         (0)    12173 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/reset_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6065 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_id.py
+-rw-r--r--   0 root         (0) root         (0)     7657 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_access_controlled_resource.py
+-rw-r--r--   0 root         (0) root         (0)     7571 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_access_metadata_value_of.py
+-rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_aggregated_return.py
+-rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_aggregation_query.py
+-rw-r--r--   0 root         (0) root         (0)     7265 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_allocation.py
+-rw-r--r--   0 root         (0) root         (0)     7125 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_block.py
+-rw-r--r--   0 root         (0) root         (0)     7321 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_calendar_date.py
+-rw-r--r--   0 root         (0) root         (0)     7153 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_change.py
+-rw-r--r--   0 root         (0) root         (0)     7349 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_change_history.py
+-rw-r--r--   0 root         (0) root         (0)     7741 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_compliance_breached_order_info.py
+-rw-r--r--   0 root         (0) root         (0)     7377 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_compliance_rule.py
+-rw-r--r--   0 root         (0) root         (0)     7545 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_compliance_rule_result.py
+-rw-r--r--   0 root         (0) root         (0)     7461 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_compliance_run_info.py
+-rw-r--r--   0 root         (0) root         (0)     7769 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_constituents_adjustment_header.py
+-rw-r--r--   0 root         (0) root         (0)     7405 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_corporate_action.py
+-rw-r--r--   0 root         (0) root         (0)     7209 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_data_type.py
+-rw-r--r--   0 root         (0) root         (0)     7237 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_execution.py
+-rw-r--r--   0 root         (0) root         (0)     7181 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_fee_rule.py
+-rw-r--r--   0 root         (0) root         (0)     7797 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_get_cds_flow_conventions_response.py
+-rw-r--r--   0 root         (0) root         (0)     7881 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_get_counterparty_agreement_response.py
+-rw-r--r--   0 root         (0) root         (0)     7797 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_get_credit_support_annex_response.py
+-rw-r--r--   0 root         (0) root         (0)     7713 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_get_flow_conventions_response.py
+-rw-r--r--   0 root         (0) root         (0)     7713 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_get_index_convention_response.py
+-rw-r--r--   0 root         (0) root         (0)     7461 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_get_recipe_response.py
+-rw-r--r--   0 root         (0) root         (0)     7657 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_holdings_adjustment_header.py
+-rw-r--r--   0 root         (0) root         (0)     7489 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_i_unit_definition_dto.py
+-rw-r--r--   0 root         (0) root         (0)     7489 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_instrument_cash_flow.py
+-rw-r--r--   0 root         (0) root         (0)     7573 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_instrument_event_holder.py
+-rw-r--r--   0 root         (0) root         (0)     7713 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_instrument_id_type_descriptor.py
+-rw-r--r--   0 root         (0) root         (0)     7293 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_legal_entity.py
+-rw-r--r--   0 root         (0) root         (0)     8133 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_list_complex_market_data_with_meta_data_response.py
+-rw-r--r--   0 root         (0) root         (0)     7181 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_mapping.py
+-rw-r--r--   0 root         (0) root         (0)     7125 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_order.py
+-rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_order_instruction.py
+-rw-r--r--   0 root         (0) root         (0)     7181 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_package.py
+-rw-r--r--   0 root         (0) root         (0)     7349 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_participation.py
+-rw-r--r--   0 root         (0) root         (0)     7461 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_performance_return.py
+-rw-r--r--   0 root         (0) root         (0)     7153 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_person.py
+-rw-r--r--   0 root         (0) root         (0)     7237 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_placement.py
+-rw-r--r--   0 root         (0) root         (0)     7237 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_portfolio.py
+-rw-r--r--   0 root         (0) root         (0)     7461 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_portfolio_cash_flow.py
+-rw-r--r--   0 root         (0) root         (0)     7517 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_portfolio_cash_ladder.py
+-rw-r--r--   0 root         (0) root         (0)     7377 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_portfolio_group.py
+-rw-r--r--   0 root         (0) root         (0)     7545 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_portfolio_trade_ticket.py
+-rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_processed_command.py
+-rw-r--r--   0 root         (0) root         (0)     7229 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_property.py
+-rw-r--r--   0 root         (0) root         (0)     7489 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_property_definition.py
+-rw-r--r--   0 root         (0) root         (0)     7433 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_property_interval.py
+-rw-r--r--   0 root         (0) root         (0)     7125 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_quote.py
+-rw-r--r--   0 root         (0) root         (0)     7629 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_quote_access_metadata_rule.py
+-rw-r--r--   0 root         (0) root         (0)     7517 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_reconciliation_break.py
+-rw-r--r--   0 root         (0) root         (0)     7209 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_relation.py
+-rw-r--r--   0 root         (0) root         (0)     7321 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_relationship.py
+-rw-r--r--   0 root         (0) root         (0)     7405 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_scope_definition.py
+-rw-r--r--   0 root         (0) root         (0)     7123 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_string.py
+-rw-r--r--   0 root         (0) root         (0)     7265 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_tax_rule_set.py
+-rw-r--r--   0 root         (0) root         (0)     7293 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_transaction.py
+-rw-r--r--   0 root         (0) root         (0)     7237 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_value_type.py
+-rw-r--r--   0 root         (0) root         (0)     7131 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/response_meta_data.py
+-rw-r--r--   0 root         (0) root         (0)    16884 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_data_key_rule.py
+-rw-r--r--   0 root         (0) root         (0)    17064 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_data_key_rule_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6620 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_data_schema.py
+-rw-r--r--   0 root         (0) root         (0)     5593 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_key_rule.py
+-rw-r--r--   0 root         (0) root         (0)     3442 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_key_rule_type.py
+-rw-r--r--   0 root         (0) root         (0)     6667 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value.py
+-rw-r--r--   0 root         (0) root         (0)     8572 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value0_d.py
+-rw-r--r--   0 root         (0) root         (0)     8672 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value0_d_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6563 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value_bool.py
+-rw-r--r--   0 root         (0) root         (0)     6623 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value_bool_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6573 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value_currency.py
+-rw-r--r--   0 root         (0) root         (0)     6633 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value_currency_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     8004 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value_date_time_offset.py
+-rw-r--r--   0 root         (0) root         (0)     8084 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value_date_time_offset_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7880 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value_decimal.py
+-rw-r--r--   0 root         (0) root         (0)     7960 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value_decimal_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6781 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value_dictionary.py
+-rw-r--r--   0 root         (0) root         (0)     6841 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value_dictionary_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7808 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value_int.py
+-rw-r--r--   0 root         (0) root         (0)     7888 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value_int_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     6549 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value_string.py
+-rw-r--r--   0 root         (0) root         (0)     6609 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value_string_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     4028 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/result_value_type.py
+-rw-r--r--   0 root         (0) root         (0)     3353 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/scaling_methodology.py
+-rw-r--r--   0 root         (0) root         (0)     5426 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/schedule.py
+-rw-r--r--   0 root         (0) root         (0)     3458 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/schedule_type.py
+-rw-r--r--   0 root         (0) root         (0)     5782 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/schema.py
+-rw-r--r--   0 root         (0) root         (0)     4421 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/scope_definition.py
+-rw-r--r--   0 root         (0) root         (0)    12312 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/sequence_definition.py
+-rw-r--r--   0 root         (0) root         (0)     4545 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/set_legal_entity_identifiers_request.py
+-rw-r--r--   0 root         (0) root         (0)     4697 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/set_legal_entity_properties_request.py
+-rw-r--r--   0 root         (0) root         (0)     4487 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/set_person_identifiers_request.py
+-rw-r--r--   0 root         (0) root         (0)     4849 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/set_person_properties_request.py
+-rw-r--r--   0 root         (0) root         (0)    10368 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/set_transaction_configuration_alias.py
+-rw-r--r--   0 root         (0) root         (0)     6684 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/set_transaction_configuration_source_request.py
+-rw-r--r--   0 root         (0) root         (0)    11343 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/side_configuration_data.py
+-rw-r--r--   0 root         (0) root         (0)    10811 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/side_configuration_data_request.py
+-rw-r--r--   0 root         (0) root         (0)    15304 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/side_definition.py
+-rw-r--r--   0 root         (0) root         (0)    13012 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/side_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)    14459 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/simple_instrument.py
+-rw-r--r--   0 root         (0) root         (0)    14599 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/simple_instrument_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     3305 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/sort_order.py
+-rw-r--r--   0 root         (0) root         (0)     9596 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/step_schedule.py
+-rw-r--r--   0 root         (0) root         (0)     9696 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/step_schedule_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    10119 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/stock_split_event.py
+-rw-r--r--   0 root         (0) root         (0)    10219 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/stock_split_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     9229 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/stream.py
+-rw-r--r--   0 root         (0) root         (0)     3478 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/string_comparison_type.py
+-rw-r--r--   0 root         (0) root         (0)    10092 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/structured_result_data.py
+-rw-r--r--   0 root         (0) root         (0)     9903 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/structured_result_data_id.py
+-rw-r--r--   0 root         (0) root         (0)     7997 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/sub_holding_key_value_equals.py
+-rw-r--r--   0 root         (0) root         (0)     8077 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/sub_holding_key_value_equals_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     9013 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/supported_analytics_internal_request.py
+-rw-r--r--   0 root         (0) root         (0)     9501 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/target_tax_lot.py
+-rw-r--r--   0 root         (0) root         (0)     9697 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/target_tax_lot_request.py
+-rw-r--r--   0 root         (0) root         (0)     9358 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/tax_rule.py
+-rw-r--r--   0 root         (0) root         (0)    12276 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/tax_rule_set.py
+-rw-r--r--   0 root         (0) root         (0)    18130 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/term_deposit.py
+-rw-r--r--   0 root         (0) root         (0)    18290 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/term_deposit_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7853 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/touch.py
+-rw-r--r--   0 root         (0) root         (0)     4932 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/trade_ticket.py
+-rw-r--r--   0 root         (0) root         (0)     3377 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/trade_ticket_type.py
+-rw-r--r--   0 root         (0) root         (0)    30338 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction.py
+-rw-r--r--   0 root         (0) root         (0)     7083 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_configuration_data.py
+-rw-r--r--   0 root         (0) root         (0)     7208 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_configuration_data_request.py
+-rw-r--r--   0 root         (0) root         (0)    15020 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_configuration_movement_data.py
+-rw-r--r--   0 root         (0) root         (0)    13934 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_configuration_movement_data_request.py
+-rw-r--r--   0 root         (0) root         (0)    14164 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_configuration_type_alias.py
+-rw-r--r--   0 root         (0) root         (0)     5083 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_price.py
+-rw-r--r--   0 root         (0) root         (0)     3352 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_price_type.py
+-rw-r--r--   0 root         (0) root         (0)     6459 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_property_mapping.py
+-rw-r--r--   0 root         (0) root         (0)     6568 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_property_mapping_request.py
+-rw-r--r--   0 root         (0) root         (0)     3349 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_query_mode.py
+-rw-r--r--   0 root         (0) root         (0)     9881 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_query_parameters.py
+-rw-r--r--   0 root         (0) root         (0)    11041 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_reconciliation_request.py
+-rw-r--r--   0 root         (0) root         (0)    25203 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_request.py
+-rw-r--r--   0 root         (0) root         (0)     3555 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_roles.py
+-rw-r--r--   0 root         (0) root         (0)     6795 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_set_configuration_data.py
+-rw-r--r--   0 root         (0) root         (0)     6484 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_set_configuration_data_request.py
+-rw-r--r--   0 root         (0) root         (0)     3358 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_status.py
+-rw-r--r--   0 root         (0) root         (0)     7475 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_type.py
+-rw-r--r--   0 root         (0) root         (0)    12110 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_type_alias.py
+-rw-r--r--   0 root         (0) root         (0)    15230 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_type_movement.py
+-rw-r--r--   0 root         (0) root         (0)     7286 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_type_property_mapping.py
+-rw-r--r--   0 root         (0) root         (0)     6883 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transaction_type_request.py
+-rw-r--r--   0 root         (0) root         (0)     5076 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transactions_reconciliations_response.py
+-rw-r--r--   0 root         (0) root         (0)    12319 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transition_event.py
+-rw-r--r--   0 root         (0) root         (0)    12479 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/transition_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     7647 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/translate_instrument_definitions_request.py
+-rw-r--r--   0 root         (0) root         (0)     7420 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/translate_instrument_definitions_response.py
+-rw-r--r--   0 root         (0) root         (0)     7057 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/translate_trade_ticket_request.py
+-rw-r--r--   0 root         (0) root         (0)     7224 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/translate_trade_tickets_response.py
+-rw-r--r--   0 root         (0) root         (0)    12563 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/trigger_event.py
+-rw-r--r--   0 root         (0) root         (0)    12703 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/trigger_event_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     9765 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/typed_resource_id.py
+-rw-r--r--   0 root         (0) root         (0)     3345 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/unit_schema.py
+-rw-r--r--   0 root         (0) root         (0)     3375 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/unmatched_holding_method.py
+-rw-r--r--   0 root         (0) root         (0)     7389 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/update_calendar_request.py
+-rw-r--r--   0 root         (0) root         (0)     8384 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/update_custom_entity_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)     8527 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/update_cut_label_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)     9293 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/update_data_type_request.py
+-rw-r--r--   0 root         (0) root         (0)     7187 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/update_instrument_identifier_request.py
+-rw-r--r--   0 root         (0) root         (0)     5732 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/update_portfolio_group_request.py
+-rw-r--r--   0 root         (0) root         (0)     5684 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/update_portfolio_request.py
+-rw-r--r--   0 root         (0) root         (0)     6201 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/update_property_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)    10184 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/update_relationship_definition_request.py
+-rw-r--r--   0 root         (0) root         (0)     8155 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/update_tax_rule_set_request.py
+-rw-r--r--   0 root         (0) root         (0)     7868 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/update_unit_request.py
+-rw-r--r--   0 root         (0) root         (0)     4423 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_cds_flow_conventions_request.py
+-rw-r--r--   0 root         (0) root         (0)     5591 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_complex_market_data_request.py
+-rw-r--r--   0 root         (0) root         (0)    13956 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_corporate_action_request.py
+-rw-r--r--   0 root         (0) root         (0)     7350 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_corporate_actions_response.py
+-rw-r--r--   0 root         (0) root         (0)     4691 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_counterparty_agreement_request.py
+-rw-r--r--   0 root         (0) root         (0)     4423 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_credit_support_annex_request.py
+-rw-r--r--   0 root         (0) root         (0)     7423 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_custom_entities_response.py
+-rw-r--r--   0 root         (0) root         (0)     4488 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_custom_entity_access_metadata_request.py
+-rw-r--r--   0 root         (0) root         (0)     4292 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_flow_conventions_request.py
+-rw-r--r--   0 root         (0) root         (0)     4292 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_index_convention_request.py
+-rw-r--r--   0 root         (0) root         (0)    11530 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_instrument_event_request.py
+-rw-r--r--   0 root         (0) root         (0)     7374 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_instrument_events_response.py
+-rw-r--r--   0 root         (0) root         (0)     5336 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_instrument_properties_response.py
+-rw-r--r--   0 root         (0) root         (0)     7966 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_instrument_property_request.py
+-rw-r--r--   0 root         (0) root         (0)     8362 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_instruments_response.py
+-rw-r--r--   0 root         (0) root         (0)     4480 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_legal_entity_access_metadata_request.py
+-rw-r--r--   0 root         (0) root         (0)    11115 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_legal_entity_request.py
+-rw-r--r--   0 root         (0) root         (0)     4422 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_person_access_metadata_request.py
+-rw-r--r--   0 root         (0) root         (0)     9117 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_person_request.py
+-rw-r--r--   0 root         (0) root         (0)     4652 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_portfolio_access_metadata_request.py
+-rw-r--r--   0 root         (0) root         (0)     4710 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_portfolio_group_access_metadata_request.py
+-rw-r--r--   0 root         (0) root         (0)     7446 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_portfolio_transactions_response.py
+-rw-r--r--   0 root         (0) root         (0)     5639 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_quote_access_metadata_rule_request.py
+-rw-r--r--   0 root         (0) root         (0)     7602 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_quote_request.py
+-rw-r--r--   0 root         (0) root         (0)     7044 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_quotes_response.py
+-rw-r--r--   0 root         (0) root         (0)     5700 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_recipe_request.py
+-rw-r--r--   0 root         (0) root         (0)    10645 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_reference_portfolio_constituents_request.py
+-rw-r--r--   0 root         (0) root         (0)     5744 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_reference_portfolio_constituents_response.py
+-rw-r--r--   0 root         (0) root         (0)     7265 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_result_values_data_request.py
+-rw-r--r--   0 root         (0) root         (0)     8081 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_returns_response.py
+-rw-r--r--   0 root         (0) root         (0)     6072 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_single_structured_data_response.py
+-rw-r--r--   0 root         (0) root         (0)     7225 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_structured_data_response.py
+-rw-r--r--   0 root         (0) root         (0)     5014 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_structured_result_data_request.py
+-rw-r--r--   0 root         (0) root         (0)     6948 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/upsert_transaction_properties_response.py
+-rw-r--r--   0 root         (0) root         (0)     3793 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/user.py
+-rw-r--r--   0 root         (0) root         (0)    21405 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/valuation_request.py
+-rw-r--r--   0 root         (0) root         (0)    13908 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/valuation_schedule.py
+-rw-r--r--   0 root         (0) root         (0)     8627 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/valuations_reconciliation_request.py
+-rw-r--r--   0 root         (0) root         (0)     4004 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/value_type.py
+-rw-r--r--   0 root         (0) root         (0)     8896 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/vendor_dependency.py
+-rw-r--r--   0 root         (0) root         (0)     8996 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/vendor_dependency_all_of.py
+-rw-r--r--   0 root         (0) root         (0)     3528 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/vendor_library.py
+-rw-r--r--   0 root         (0) root         (0)    15639 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/vendor_model_rule.py
+-rw-r--r--   0 root         (0) root         (0)    11534 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/version.py
+-rw-r--r--   0 root         (0) root         (0)     6388 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/version_summary_dto.py
+-rw-r--r--   0 root         (0) root         (0)     8591 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/versioned_resource_list_of_a2_b_data_record.py
+-rw-r--r--   0 root         (0) root         (0)     8719 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/versioned_resource_list_of_a2_b_movement_record.py
+-rw-r--r--   0 root         (0) root         (0)     8399 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/versioned_resource_list_of_je_lines.py
+-rw-r--r--   0 root         (0) root         (0)     8719 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/versioned_resource_list_of_output_transaction.py
+-rw-r--r--   0 root         (0) root         (0)     8687 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/versioned_resource_list_of_portfolio_holding.py
+-rw-r--r--   0 root         (0) root         (0)     8527 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/versioned_resource_list_of_transaction.py
+-rw-r--r--   0 root         (0) root         (0)    10455 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/versioned_resource_list_with_warnings_of_portfolio_holding.py
+-rw-r--r--   0 root         (0) root         (0)     4964 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/virtual_document.py
+-rw-r--r--   0 root         (0) root         (0)     5221 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/virtual_document_row.py
+-rw-r--r--   0 root         (0) root         (0)     4936 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/warning.py
+-rw-r--r--   0 root         (0) root         (0)     5793 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/weekend_mask.py
+-rw-r--r--   0 root         (0) root         (0)     8441 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/weighted_instrument.py
+-rw-r--r--   0 root         (0) root         (0)     4479 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/weighted_instruments.py
+-rw-r--r--   0 root         (0) root         (0)    11018 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/yield_curve_data.py
+-rw-r--r--   0 root         (0) root         (0)    11138 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/models/yield_curve_data_all_of.py
+-rw-r--r--   0 root         (0) root         (0)    13517 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/rest.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:59:44.507232 lusid-sdk-preview-1.0.9/lusid/tcp/
+-rw-r--r--   0 root         (0) root         (0)       93 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/tcp/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5321 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/tcp/tcp_keep_alive_probes.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:59:44.508232 lusid-sdk-preview-1.0.9/lusid/utilities/
+-rw-r--r--   0 root         (0) root         (0)      432 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/utilities/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     6434 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/utilities/api_client_builder.py
+-rw-r--r--   0 root         (0) root         (0)     5397 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/utilities/api_client_factory.py
+-rw-r--r--   0 root         (0) root         (0)     3970 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/utilities/api_configuration.py
+-rw-r--r--   0 root         (0) root         (0)     4065 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/utilities/api_configuration_loader.py
+-rw-r--r--   0 root         (0) root         (0)     1030 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/utilities/config_keys.json
+-rw-r--r--   0 root         (0) root         (0)     1236 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/utilities/lusid_retry.py
+-rw-r--r--   0 root         (0) root         (0)     1725 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/utilities/proxy_config.py
+-rw-r--r--   0 root         (0) root         (0)     9701 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/lusid/utilities/refreshing_token.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-16 22:59:44.509232 lusid-sdk-preview-1.0.9/lusid_sdk_preview.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      356 2023-03-16 22:59:44.000000 lusid-sdk-preview-1.0.9/lusid_sdk_preview.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    34520 2023-03-16 22:59:44.000000 lusid-sdk-preview-1.0.9/lusid_sdk_preview.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-03-16 22:59:44.000000 lusid-sdk-preview-1.0.9/lusid_sdk_preview.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       97 2023-03-16 22:59:44.000000 lusid-sdk-preview-1.0.9/lusid_sdk_preview.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        6 2023-03-16 22:59:44.000000 lusid-sdk-preview-1.0.9/lusid_sdk_preview.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       38 2023-03-16 22:59:44.509232 lusid-sdk-preview-1.0.9/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     2218 2023-03-16 22:42:09.000000 lusid-sdk-preview-1.0.9/setup.py
```

### Comparing `lusid-sdk-preview-1.0.8/README.md` & `lusid-sdk-preview-1.0.9/README.md`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/__init__.py` & `lusid-sdk-preview-1.0.9/lusid/__init__.py`

 * *Files 0% similar despite different names*

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
 from lusid.api.abor_api import AborApi
 from lusid.api.abor_configuration_api import AborConfigurationApi
 from lusid.api.aggregation_api import AggregationApi
 from lusid.api.allocations_api import AllocationsApi
 from lusid.api.application_metadata_api import ApplicationMetadataApi
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/__init__.py` & `lusid-sdk-preview-1.0.9/lusid/api/__init__.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/abor_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/abor_api.py`

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
             201: "Abor",
             400: "LusidValidationProblemDetails",
@@ -353,15 +353,15 @@
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
@@ -546,15 +546,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Abor",
             400: "LusidValidationProblemDetails",
@@ -760,15 +760,15 @@
 
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
             200: "VersionedResourceListOfJELines",
             400: "LusidValidationProblemDetails",
@@ -963,15 +963,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfAbor",
             400: "LusidValidationProblemDetails",
@@ -1144,15 +1144,15 @@
 
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
             200: "AborProperties",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/abor_configuration_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/abor_configuration_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
             201: "AborConfiguration",
             400: "LusidValidationProblemDetails",
@@ -351,15 +351,15 @@
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
@@ -544,15 +544,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "AborConfiguration",
             400: "LusidValidationProblemDetails",
@@ -747,15 +747,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfAborConfiguration",
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
             200: "AborConfigurationProperties",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/aggregation_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/aggregation_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
             200: "ConfigurationRecipe",
             400: "LusidValidationProblemDetails",
@@ -367,15 +367,15 @@
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
@@ -510,15 +510,15 @@
 
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
@@ -653,15 +653,15 @@
 
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
@@ -796,15 +796,15 @@
 
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/allocations_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/allocations_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/application_metadata_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/application_metadata_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/blocks_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/blocks_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/calendars_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/calendars_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/chart_of_accounts_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/chart_of_accounts_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
             201: "ChartOfAccounts",
             400: "LusidValidationProblemDetails",
@@ -377,15 +377,15 @@
 
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
             200: "DeleteAccountsResponse",
             400: "LusidValidationProblemDetails",
@@ -548,15 +548,15 @@
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
@@ -760,15 +760,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "Account",
             400: "LusidValidationProblemDetails",
@@ -953,15 +953,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ChartOfAccounts",
             400: "LusidValidationProblemDetails",
@@ -1194,15 +1194,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfAccount",
             400: "LusidValidationProblemDetails",
@@ -1397,15 +1397,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfChartOfAccounts",
             400: "LusidValidationProblemDetails",
@@ -1582,15 +1582,15 @@
 
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
             200: "AccountsUpsertResponse",
             400: "LusidValidationProblemDetails",
@@ -1782,15 +1782,15 @@
 
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
             200: "AccountProperties",
             400: "LusidValidationProblemDetails",
@@ -1963,15 +1963,15 @@
 
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
             200: "ChartOfAccountsProperties",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/complex_market_data_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/complex_market_data_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
             200: "AnnulStructuredDataResponse",
             400: "LusidValidationProblemDetails",
@@ -375,15 +375,15 @@
 
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
@@ -515,15 +515,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfListComplexMarketDataWithMetaDataResponse",
             400: "LusidValidationProblemDetails",
@@ -681,15 +681,15 @@
 
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/compliance_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/compliance_api.py`

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
 
@@ -188,15 +188,15 @@
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
             200: "ResourceListOfComplianceBreachedOrderInfo",
             400: "LusidValidationProblemDetails",
@@ -566,15 +566,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ComplianceRule",
             400: "LusidValidationProblemDetails",
@@ -759,15 +759,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfComplianceRuleResult",
             400: "LusidValidationProblemDetails",
@@ -947,15 +947,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfComplianceRule",
             400: "LusidValidationProblemDetails",
@@ -1128,15 +1128,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfComplianceRunInfo",
             400: "LusidValidationProblemDetails",
@@ -1313,15 +1313,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ComplianceRunInfo",
             400: "LusidValidationProblemDetails",
@@ -1467,15 +1467,15 @@
 
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
             200: "ComplianceRuleUpsertResponse",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/configuration_recipe_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/configuration_recipe_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/conventions_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/conventions_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
             200: "AnnulSingleStructuredDataResponse",
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
             200: "AnnulSingleStructuredDataResponse",
             400: "LusidValidationProblemDetails",
@@ -532,15 +532,15 @@
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
@@ -710,15 +710,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "GetCdsFlowConventionsResponse",
             400: "LusidValidationProblemDetails",
@@ -888,15 +888,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "GetFlowConventionsResponse",
             400: "LusidValidationProblemDetails",
@@ -1066,15 +1066,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "GetIndexConventionResponse",
             400: "LusidValidationProblemDetails",
@@ -1206,15 +1206,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfGetCdsFlowConventionsResponse",
             400: "LusidValidationProblemDetails",
@@ -1346,15 +1346,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfGetFlowConventionsResponse",
             400: "LusidValidationProblemDetails",
@@ -1486,15 +1486,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfGetIndexConventionResponse",
             400: "LusidValidationProblemDetails",
@@ -1633,15 +1633,15 @@
 
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
@@ -1780,15 +1780,15 @@
 
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
@@ -1927,15 +1927,15 @@
 
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/corporate_action_sources_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/corporate_action_sources_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
             200: "DeletedEntityResponse",
             400: "LusidValidationProblemDetails",
@@ -700,15 +700,15 @@
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
@@ -883,15 +883,15 @@
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
@@ -1121,15 +1121,15 @@
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
@@ -1336,15 +1336,15 @@
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
@@ -1521,15 +1521,15 @@
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
@@ -1702,15 +1702,15 @@
 
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/counterparties_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/counterparties_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/custom_entities_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/custom_entities_api.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/custom_entity_definitions_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/custom_entity_definitions_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/cut_label_definitions_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/cut_label_definitions_api.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/data_types_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/data_types_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/derived_transaction_portfolios_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/derived_transaction_portfolios_api.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/entities_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/entities_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/executions_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/executions_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/instrument_events_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/instrument_events_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
             200: "BucketedCashFlowResponse",
             400: "LusidValidationProblemDetails",
@@ -324,15 +324,15 @@
 
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
             200: "ResourceListOfInstrumentCashFlow",
             400: "LusidValidationProblemDetails",
@@ -489,15 +489,15 @@
 
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
             200: "ResourceListOfInstrumentEventHolder",
             400: "LusidValidationProblemDetails",
@@ -654,15 +654,15 @@
 
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
             200: "ResourceListOfPortfolioTradeTicket",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/instruments_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/instruments_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
@@ -388,15 +388,15 @@
 
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
@@ -557,15 +557,15 @@
 
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
@@ -709,15 +709,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "dict(str, list[str])",
             400: "LusidValidationProblemDetails",
@@ -933,15 +933,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "InstrumentCapabilities",
             400: "LusidValidationProblemDetails",
@@ -1133,15 +1133,15 @@
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
@@ -1266,15 +1266,15 @@
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
@@ -1503,15 +1503,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "InstrumentPaymentDiary",
             400: "LusidValidationProblemDetails",
@@ -1687,15 +1687,15 @@
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
@@ -1923,15 +1923,15 @@
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
@@ -2154,15 +2154,15 @@
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
@@ -2357,15 +2357,15 @@
 
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
@@ -2575,15 +2575,15 @@
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
@@ -2809,15 +2809,15 @@
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
@@ -3006,15 +3006,15 @@
 
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
             200: "InstrumentCapabilities",
             400: "LusidValidationProblemDetails",
@@ -3190,15 +3190,15 @@
 
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
@@ -3352,15 +3352,15 @@
 
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
@@ -3514,15 +3514,15 @@
 
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/legal_entities_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/legal_entities_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
 
@@ -210,15 +210,15 @@
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
@@ -433,15 +433,15 @@
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
@@ -640,15 +640,15 @@
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
@@ -847,15 +847,15 @@
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
@@ -1051,15 +1051,15 @@
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
@@ -1277,15 +1277,15 @@
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
@@ -1500,15 +1500,15 @@
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
@@ -1747,15 +1747,15 @@
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
@@ -1980,15 +1980,15 @@
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
@@ -2213,15 +2213,15 @@
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
@@ -2417,15 +2417,15 @@
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
@@ -2667,15 +2667,15 @@
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
@@ -2885,15 +2885,15 @@
 
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
@@ -3087,15 +3087,15 @@
 
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
@@ -3289,15 +3289,15 @@
 
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
@@ -3436,15 +3436,15 @@
 
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
@@ -3673,15 +3673,15 @@
 
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/order_graph_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/order_graph_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
 
@@ -207,15 +207,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfOrderGraphBlock",
             400: "LusidValidationProblemDetails",
@@ -404,15 +404,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "PagedResourceListOfOrderGraphPlacement",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/order_instructions_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/order_instructions_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
             200: "OrderInstruction",
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
             200: "PagedResourceListOfOrderInstruction",
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
             201: "ResourceListOfOrderInstruction",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/orders_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/orders_api.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/packages_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/packages_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
             200: "Package",
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
             200: "PagedResourceListOfPackage",
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
             201: "ResourceListOfPackage",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/participations_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/participations_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/persons_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/persons_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/placements_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/placements_api.py`

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
             200: "Placement",
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
             200: "PagedResourceListOfPlacement",
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
             201: "ResourceListOfPlacement",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/portfolio_groups_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/portfolio_groups_api.py`

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
 
@@ -226,15 +226,15 @@
 
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
@@ -422,15 +422,15 @@
 
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
@@ -659,15 +659,15 @@
 
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
@@ -821,15 +821,15 @@
 
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
@@ -1013,15 +1013,15 @@
 
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
@@ -1215,15 +1215,15 @@
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
@@ -1439,15 +1439,15 @@
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
@@ -1610,15 +1610,15 @@
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
@@ -1818,15 +1818,15 @@
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
@@ -2055,15 +2055,15 @@
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
@@ -2240,15 +2240,15 @@
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
@@ -2455,15 +2455,15 @@
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
@@ -2664,15 +2664,15 @@
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
@@ -2866,15 +2866,15 @@
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
@@ -3066,15 +3066,15 @@
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
@@ -3267,15 +3267,15 @@
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
@@ -3452,15 +3452,15 @@
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
@@ -3689,15 +3689,15 @@
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
@@ -3897,15 +3897,15 @@
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
@@ -4113,15 +4113,15 @@
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
@@ -4357,15 +4357,15 @@
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
@@ -4562,15 +4562,15 @@
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
@@ -4761,15 +4761,15 @@
 
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
@@ -4957,15 +4957,15 @@
 
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
@@ -5138,15 +5138,15 @@
 
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
@@ -5354,15 +5354,15 @@
 
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/portfolios_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/portfolios_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
 
@@ -233,15 +233,15 @@
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
@@ -404,15 +404,15 @@
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
@@ -594,15 +594,15 @@
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
@@ -832,15 +832,15 @@
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
@@ -1033,15 +1033,15 @@
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
@@ -1329,15 +1329,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfAggregatedReturn",
             400: "LusidValidationProblemDetails",
@@ -1535,15 +1535,15 @@
 
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
@@ -1761,15 +1761,15 @@
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
@@ -1946,15 +1946,15 @@
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
@@ -2131,15 +2131,15 @@
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
@@ -2368,15 +2368,15 @@
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
@@ -2576,15 +2576,15 @@
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
@@ -2792,15 +2792,15 @@
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
@@ -3029,15 +3029,15 @@
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
@@ -3231,15 +3231,15 @@
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
@@ -3450,15 +3450,15 @@
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
@@ -3676,15 +3676,15 @@
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
@@ -3906,15 +3906,15 @@
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
@@ -4091,15 +4091,15 @@
 
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
@@ -4290,15 +4290,15 @@
 
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
@@ -4482,15 +4482,15 @@
 
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
@@ -4698,15 +4698,15 @@
 
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
@@ -4883,15 +4883,15 @@
 
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
@@ -5106,15 +5106,15 @@
 
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/property_definitions_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/property_definitions_api.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/quotes_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/quotes_api.py`

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
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "QuoteAccessMetadataRule",
             400: "LusidValidationProblemDetails",
@@ -387,15 +387,15 @@
 
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
@@ -570,15 +570,15 @@
 
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
@@ -784,15 +784,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "QuoteAccessMetadataRule",
             400: "LusidValidationProblemDetails",
@@ -987,15 +987,15 @@
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
@@ -1146,15 +1146,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfQuoteAccessMetadataRule",
             400: "LusidValidationProblemDetails",
@@ -1349,15 +1349,15 @@
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
@@ -1529,15 +1529,15 @@
 
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
             200: "QuoteAccessMetadataRule",
             400: "LusidValidationProblemDetails",
@@ -1691,15 +1691,15 @@
 
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/reconciliations_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/reconciliations_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/reference_portfolio_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/reference_portfolio_api.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/relation_definitions_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/relation_definitions_api.py`

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
             201: "RelationDefinition",
             400: "LusidValidationProblemDetails",
@@ -329,15 +329,15 @@
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
@@ -507,15 +507,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "RelationDefinition",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/relations_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/relations_api.py`

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
 
@@ -204,15 +204,15 @@
 
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
             200: "CompleteRelation",
             400: "LusidValidationProblemDetails",
@@ -396,15 +396,15 @@
 
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/relationship_definitions_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/relationship_definitions_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/relationships_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/relationships_api.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/schemas_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/schemas_api.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/scopes_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/scopes_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/search_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/search_api.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/sequences_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/sequences_api.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/structured_result_data_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/structured_result_data_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
@@ -350,15 +350,15 @@
 
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
@@ -516,15 +516,15 @@
 
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
             200: "GetDataMapResponse",
             400: "LusidValidationProblemDetails",
@@ -696,15 +696,15 @@
 
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
             200: "GetStructuredResultDataResponse",
             400: "LusidValidationProblemDetails",
@@ -869,15 +869,15 @@
 
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
             200: "GetVirtualDocumentResponse",
             400: "LusidValidationProblemDetails",
@@ -1035,15 +1035,15 @@
 
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
@@ -1201,15 +1201,15 @@
 
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/system_configuration_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/system_configuration_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
@@ -300,15 +300,15 @@
 
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
@@ -452,15 +452,15 @@
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
@@ -611,15 +611,15 @@
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
@@ -751,15 +751,15 @@
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
@@ -894,15 +894,15 @@
 
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
             200: "TransactionSetConfigurationData",
             400: "LusidValidationProblemDetails",
@@ -1060,15 +1060,15 @@
 
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
             200: "TransactionSetConfigurationData",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/tax_rule_sets_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/tax_rule_sets_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
 
@@ -167,15 +167,15 @@
 
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
             200: "TaxRuleSet",
             400: "LusidValidationProblemDetails",
@@ -338,15 +338,15 @@
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
             200: "TaxRuleSet",
             400: "LusidValidationProblemDetails",
@@ -670,15 +670,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfTaxRuleSet",
             400: "LusidValidationProblemDetails",
@@ -862,15 +862,15 @@
 
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
             200: "TaxRuleSet",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/transaction_configuration_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/transaction_configuration_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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
             200: "DeletedEntityResponse",
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
             200: "TransactionType",
             400: "LusidValidationProblemDetails",
@@ -502,15 +502,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "dict(str, list[TransactionType])",
             400: "LusidValidationProblemDetails",
@@ -668,15 +668,15 @@
 
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
             200: "SideDefinition",
             400: "LusidValidationProblemDetails",
@@ -853,15 +853,15 @@
 
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
             200: "TransactionType",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/transaction_fees_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/transaction_fees_api.py`

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
 
@@ -165,15 +165,15 @@
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
@@ -378,15 +378,15 @@
 
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
             200: "ResourceListOfFeeRule",
             400: "LusidValidationProblemDetails",
@@ -544,15 +544,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "FeeRule",
             400: "LusidValidationProblemDetails",
@@ -732,15 +732,15 @@
             ['text/plain', 'application/json', 'text/json'])  # noqa: E501
 
         header_params['Accept-Encoding'] = "gzip, deflate, br"
 
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.0.8'
+        header_params['X-LUSID-SDK-Version'] = '1.0.9'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
 
         response_types_map = {
             200: "ResourceListOfFeeRule",
             400: "LusidValidationProblemDetails",
@@ -886,15 +886,15 @@
 
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
             200: "FeeRuleUpsertResponse",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/transaction_portfolios_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/transaction_portfolios_api.py`

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
@@ -1023,15 +1023,15 @@
 00003fe0: 5349 4420 6865 6164 6572 0a20 2020 2020  SID header.     
 00003ff0: 2020 2068 6561 6465 725f 7061 7261 6d73     header_params
 00004000: 5b27 582d 4c55 5349 442d 5344 4b2d 4c61  ['X-LUSID-SDK-La
 00004010: 6e67 7561 6765 275d 203d 2027 5079 7468  nguage'] = 'Pyth
 00004020: 6f6e 270a 2020 2020 2020 2020 6865 6164  on'.        head
 00004030: 6572 5f70 6172 616d 735b 2758 2d4c 5553  er_params['X-LUS
 00004040: 4944 2d53 444b 2d56 6572 7369 6f6e 275d  ID-SDK-Version']
-00004050: 203d 2027 312e 302e 3827 0a0a 2020 2020   = '1.0.8'..    
+00004050: 203d 2027 312e 302e 3927 0a0a 2020 2020   = '1.0.9'..    
 00004060: 2020 2020 2320 4175 7468 656e 7469 6361      # Authentica
 00004070: 7469 6f6e 2073 6574 7469 6e67 0a20 2020  tion setting.   
 00004080: 2020 2020 2061 7574 685f 7365 7474 696e       auth_settin
 00004090: 6773 203d 205b 276f 6175 7468 3227 5d20  gs = ['oauth2'] 
 000040a0: 2023 206e 6f71 613a 2045 3530 310a 0a20   # noqa: E501.. 
 000040b0: 2020 2020 2020 2072 6573 706f 6e73 655f         response_
 000040c0: 7479 7065 735f 6d61 7020 3d20 7b0a 2020  types_map = {.  
@@ -1932,15 +1932,15 @@
 000078b0: 204c 5553 4944 2068 6561 6465 720a 2020   LUSID header.  
 000078c0: 2020 2020 2020 6865 6164 6572 5f70 6172        header_par
 000078d0: 616d 735b 2758 2d4c 5553 4944 2d53 444b  ams['X-LUSID-SDK
 000078e0: 2d4c 616e 6775 6167 6527 5d20 3d20 2750  -Language'] = 'P
 000078f0: 7974 686f 6e27 0a20 2020 2020 2020 2068  ython'.        h
 00007900: 6561 6465 725f 7061 7261 6d73 5b27 582d  eader_params['X-
 00007910: 4c55 5349 442d 5344 4b2d 5665 7273 696f  LUSID-SDK-Versio
-00007920: 6e27 5d20 3d20 2731 2e30 2e38 270a 0a20  n'] = '1.0.8'.. 
+00007920: 6e27 5d20 3d20 2731 2e30 2e39 270a 0a20  n'] = '1.0.9'.. 
 00007930: 2020 2020 2020 2023 2041 7574 6865 6e74         # Authent
 00007940: 6963 6174 696f 6e20 7365 7474 696e 670a  ication setting.
 00007950: 2020 2020 2020 2020 6175 7468 5f73 6574          auth_set
 00007960: 7469 6e67 7320 3d20 5b27 6f61 7574 6832  tings = ['oauth2
 00007970: 275d 2020 2320 6e6f 7161 3a20 4535 3031  ']  # noqa: E501
 00007980: 0a0a 2020 2020 2020 2020 7265 7370 6f6e  ..        respon
 00007990: 7365 5f74 7970 6573 5f6d 6170 203d 207b  se_types_map = {
@@ -2780,15 +2780,15 @@
 0000adb0: 6572 0a20 2020 2020 2020 2068 6561 6465  er.        heade
 0000adc0: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 0000add0: 442d 5344 4b2d 4c61 6e67 7561 6765 275d  D-SDK-Language']
 0000ade0: 203d 2027 5079 7468 6f6e 270a 2020 2020   = 'Python'.    
 0000adf0: 2020 2020 6865 6164 6572 5f70 6172 616d      header_param
 0000ae00: 735b 2758 2d4c 5553 4944 2d53 444b 2d56  s['X-LUSID-SDK-V
 0000ae10: 6572 7369 6f6e 275d 203d 2027 312e 302e  ersion'] = '1.0.
-0000ae20: 3827 0a0a 2020 2020 2020 2020 2320 4175  8'..        # Au
+0000ae20: 3927 0a0a 2020 2020 2020 2020 2320 4175  9'..        # Au
 0000ae30: 7468 656e 7469 6361 7469 6f6e 2073 6574  thentication set
 0000ae40: 7469 6e67 0a20 2020 2020 2020 2061 7574  ting.        aut
 0000ae50: 685f 7365 7474 696e 6773 203d 205b 276f  h_settings = ['o
 0000ae60: 6175 7468 3227 5d20 2023 206e 6f71 613a  auth2']  # noqa:
 0000ae70: 2045 3530 310a 0a20 2020 2020 2020 2072   E501..        r
 0000ae80: 6573 706f 6e73 655f 7479 7065 735f 6d61  esponse_types_ma
 0000ae90: 7020 3d20 7b0a 2020 2020 2020 2020 2020  p = {.          
@@ -3835,15 +3835,15 @@
 0000efa0: 204c 5553 4944 2068 6561 6465 720a 2020   LUSID header.  
 0000efb0: 2020 2020 2020 6865 6164 6572 5f70 6172        header_par
 0000efc0: 616d 735b 2758 2d4c 5553 4944 2d53 444b  ams['X-LUSID-SDK
 0000efd0: 2d4c 616e 6775 6167 6527 5d20 3d20 2750  -Language'] = 'P
 0000efe0: 7974 686f 6e27 0a20 2020 2020 2020 2068  ython'.        h
 0000eff0: 6561 6465 725f 7061 7261 6d73 5b27 582d  eader_params['X-
 0000f000: 4c55 5349 442d 5344 4b2d 5665 7273 696f  LUSID-SDK-Versio
-0000f010: 6e27 5d20 3d20 2731 2e30 2e38 270a 0a20  n'] = '1.0.8'.. 
+0000f010: 6e27 5d20 3d20 2731 2e30 2e39 270a 0a20  n'] = '1.0.9'.. 
 0000f020: 2020 2020 2020 2023 2041 7574 6865 6e74         # Authent
 0000f030: 6963 6174 696f 6e20 7365 7474 696e 670a  ication setting.
 0000f040: 2020 2020 2020 2020 6175 7468 5f73 6574          auth_set
 0000f050: 7469 6e67 7320 3d20 5b27 6f61 7574 6832  tings = ['oauth2
 0000f060: 275d 2020 2320 6e6f 7161 3a20 4535 3031  ']  # noqa: E501
 0000f070: 0a0a 2020 2020 2020 2020 7265 7370 6f6e  ..        respon
 0000f080: 7365 5f74 7970 6573 5f6d 6170 203d 207b  se_types_map = {
@@ -4514,15 +4514,15 @@
 00011a10: 4c55 5349 4420 6865 6164 6572 0a20 2020  LUSID header.   
 00011a20: 2020 2020 2068 6561 6465 725f 7061 7261       header_para
 00011a30: 6d73 5b27 582d 4c55 5349 442d 5344 4b2d  ms['X-LUSID-SDK-
 00011a40: 4c61 6e67 7561 6765 275d 203d 2027 5079  Language'] = 'Py
 00011a50: 7468 6f6e 270a 2020 2020 2020 2020 6865  thon'.        he
 00011a60: 6164 6572 5f70 6172 616d 735b 2758 2d4c  ader_params['X-L
 00011a70: 5553 4944 2d53 444b 2d56 6572 7369 6f6e  USID-SDK-Version
-00011a80: 275d 203d 2027 312e 302e 3827 0a0a 2020  '] = '1.0.8'..  
+00011a80: 275d 203d 2027 312e 302e 3927 0a0a 2020  '] = '1.0.9'..  
 00011a90: 2020 2020 2020 2320 4175 7468 656e 7469        # Authenti
 00011aa0: 6361 7469 6f6e 2073 6574 7469 6e67 0a20  cation setting. 
 00011ab0: 2020 2020 2020 2061 7574 685f 7365 7474         auth_sett
 00011ac0: 696e 6773 203d 205b 276f 6175 7468 3227  ings = ['oauth2'
 00011ad0: 5d20 2023 206e 6f71 613a 2045 3530 310a  ]  # noqa: E501.
 00011ae0: 0a20 2020 2020 2020 2072 6573 706f 6e73  .        respons
 00011af0: 655f 7479 7065 735f 6d61 7020 3d20 7b0a  e_types_map = {.
@@ -5172,15 +5172,15 @@
 00014330: 204c 5553 4944 2068 6561 6465 720a 2020   LUSID header.  
 00014340: 2020 2020 2020 6865 6164 6572 5f70 6172        header_par
 00014350: 616d 735b 2758 2d4c 5553 4944 2d53 444b  ams['X-LUSID-SDK
 00014360: 2d4c 616e 6775 6167 6527 5d20 3d20 2750  -Language'] = 'P
 00014370: 7974 686f 6e27 0a20 2020 2020 2020 2068  ython'.        h
 00014380: 6561 6465 725f 7061 7261 6d73 5b27 582d  eader_params['X-
 00014390: 4c55 5349 442d 5344 4b2d 5665 7273 696f  LUSID-SDK-Versio
-000143a0: 6e27 5d20 3d20 2731 2e30 2e38 270a 0a20  n'] = '1.0.8'.. 
+000143a0: 6e27 5d20 3d20 2731 2e30 2e39 270a 0a20  n'] = '1.0.9'.. 
 000143b0: 2020 2020 2020 2023 2041 7574 6865 6e74         # Authent
 000143c0: 6963 6174 696f 6e20 7365 7474 696e 670a  ication setting.
 000143d0: 2020 2020 2020 2020 6175 7468 5f73 6574          auth_set
 000143e0: 7469 6e67 7320 3d20 5b27 6f61 7574 6832  tings = ['oauth2
 000143f0: 275d 2020 2320 6e6f 7161 3a20 4535 3031  ']  # noqa: E501
 00014400: 0a0a 2020 2020 2020 2020 7265 7370 6f6e  ..        respon
 00014410: 7365 5f74 7970 6573 5f6d 6170 203d 207b  se_types_map = {
@@ -5732,15 +5732,15 @@
 00016630: 4944 2068 6561 6465 720a 2020 2020 2020  ID header.      
 00016640: 2020 6865 6164 6572 5f70 6172 616d 735b    header_params[
 00016650: 2758 2d4c 5553 4944 2d53 444b 2d4c 616e  'X-LUSID-SDK-Lan
 00016660: 6775 6167 6527 5d20 3d20 2750 7974 686f  guage'] = 'Pytho
 00016670: 6e27 0a20 2020 2020 2020 2068 6561 6465  n'.        heade
 00016680: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 00016690: 442d 5344 4b2d 5665 7273 696f 6e27 5d20  D-SDK-Version'] 
-000166a0: 3d20 2731 2e30 2e38 270a 0a20 2020 2020  = '1.0.8'..     
+000166a0: 3d20 2731 2e30 2e39 270a 0a20 2020 2020  = '1.0.9'..     
 000166b0: 2020 2023 2041 7574 6865 6e74 6963 6174     # Authenticat
 000166c0: 696f 6e20 7365 7474 696e 670a 2020 2020  ion setting.    
 000166d0: 2020 2020 6175 7468 5f73 6574 7469 6e67      auth_setting
 000166e0: 7320 3d20 5b27 6f61 7574 6832 275d 2020  s = ['oauth2']  
 000166f0: 2320 6e6f 7161 3a20 4535 3031 0a0a 2020  # noqa: E501..  
 00016700: 2020 2020 2020 7265 7370 6f6e 7365 5f74        response_t
 00016710: 7970 6573 5f6d 6170 203d 207b 0a20 2020  ypes_map = {.   
@@ -6391,15 +6391,15 @@
 00018f60: 4944 2068 6561 6465 720a 2020 2020 2020  ID header.      
 00018f70: 2020 6865 6164 6572 5f70 6172 616d 735b    header_params[
 00018f80: 2758 2d4c 5553 4944 2d53 444b 2d4c 616e  'X-LUSID-SDK-Lan
 00018f90: 6775 6167 6527 5d20 3d20 2750 7974 686f  guage'] = 'Pytho
 00018fa0: 6e27 0a20 2020 2020 2020 2068 6561 6465  n'.        heade
 00018fb0: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 00018fc0: 442d 5344 4b2d 5665 7273 696f 6e27 5d20  D-SDK-Version'] 
-00018fd0: 3d20 2731 2e30 2e38 270a 0a20 2020 2020  = '1.0.8'..     
+00018fd0: 3d20 2731 2e30 2e39 270a 0a20 2020 2020  = '1.0.9'..     
 00018fe0: 2020 2023 2041 7574 6865 6e74 6963 6174     # Authenticat
 00018ff0: 696f 6e20 7365 7474 696e 670a 2020 2020  ion setting.    
 00019000: 2020 2020 6175 7468 5f73 6574 7469 6e67      auth_setting
 00019010: 7320 3d20 5b27 6f61 7574 6832 275d 2020  s = ['oauth2']  
 00019020: 2320 6e6f 7161 3a20 4535 3031 0a0a 2020  # noqa: E501..  
 00019030: 2020 2020 2020 7265 7370 6f6e 7365 5f74        response_t
 00019040: 7970 6573 5f6d 6170 203d 207b 0a20 2020  ypes_map = {.   
@@ -7113,15 +7113,15 @@
 0001bc80: 4420 6865 6164 6572 0a20 2020 2020 2020  D header.       
 0001bc90: 2068 6561 6465 725f 7061 7261 6d73 5b27   header_params['
 0001bca0: 582d 4c55 5349 442d 5344 4b2d 4c61 6e67  X-LUSID-SDK-Lang
 0001bcb0: 7561 6765 275d 203d 2027 5079 7468 6f6e  uage'] = 'Python
 0001bcc0: 270a 2020 2020 2020 2020 6865 6164 6572  '.        header
 0001bcd0: 5f70 6172 616d 735b 2758 2d4c 5553 4944  _params['X-LUSID
 0001bce0: 2d53 444b 2d56 6572 7369 6f6e 275d 203d  -SDK-Version'] =
-0001bcf0: 2027 312e 302e 3827 0a0a 2020 2020 2020   '1.0.8'..      
+0001bcf0: 2027 312e 302e 3927 0a0a 2020 2020 2020   '1.0.9'..      
 0001bd00: 2020 2320 4175 7468 656e 7469 6361 7469    # Authenticati
 0001bd10: 6f6e 2073 6574 7469 6e67 0a20 2020 2020  on setting.     
 0001bd20: 2020 2061 7574 685f 7365 7474 696e 6773     auth_settings
 0001bd30: 203d 205b 276f 6175 7468 3227 5d20 2023   = ['oauth2']  #
 0001bd40: 206e 6f71 613a 2045 3530 310a 0a20 2020   noqa: E501..   
 0001bd50: 2020 2020 2072 6573 706f 6e73 655f 7479       response_ty
 0001bd60: 7065 735f 6d61 7020 3d20 7b0a 2020 2020  pes_map = {.    
@@ -7873,15 +7873,15 @@
 0001ec00: 4944 2068 6561 6465 720a 2020 2020 2020  ID header.      
 0001ec10: 2020 6865 6164 6572 5f70 6172 616d 735b    header_params[
 0001ec20: 2758 2d4c 5553 4944 2d53 444b 2d4c 616e  'X-LUSID-SDK-Lan
 0001ec30: 6775 6167 6527 5d20 3d20 2750 7974 686f  guage'] = 'Pytho
 0001ec40: 6e27 0a20 2020 2020 2020 2068 6561 6465  n'.        heade
 0001ec50: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 0001ec60: 442d 5344 4b2d 5665 7273 696f 6e27 5d20  D-SDK-Version'] 
-0001ec70: 3d20 2731 2e30 2e38 270a 0a20 2020 2020  = '1.0.8'..     
+0001ec70: 3d20 2731 2e30 2e39 270a 0a20 2020 2020  = '1.0.9'..     
 0001ec80: 2020 2023 2041 7574 6865 6e74 6963 6174     # Authenticat
 0001ec90: 696f 6e20 7365 7474 696e 670a 2020 2020  ion setting.    
 0001eca0: 2020 2020 6175 7468 5f73 6574 7469 6e67      auth_setting
 0001ecb0: 7320 3d20 5b27 6f61 7574 6832 275d 2020  s = ['oauth2']  
 0001ecc0: 2320 6e6f 7161 3a20 4535 3031 0a0a 2020  # noqa: E501..  
 0001ecd0: 2020 2020 2020 7265 7370 6f6e 7365 5f74        response_t
 0001ece0: 7970 6573 5f6d 6170 203d 207b 0a20 2020  ypes_map = {.   
@@ -8863,15 +8863,15 @@
 000229e0: 5349 4420 6865 6164 6572 0a20 2020 2020  SID header.     
 000229f0: 2020 2068 6561 6465 725f 7061 7261 6d73     header_params
 00022a00: 5b27 582d 4c55 5349 442d 5344 4b2d 4c61  ['X-LUSID-SDK-La
 00022a10: 6e67 7561 6765 275d 203d 2027 5079 7468  nguage'] = 'Pyth
 00022a20: 6f6e 270a 2020 2020 2020 2020 6865 6164  on'.        head
 00022a30: 6572 5f70 6172 616d 735b 2758 2d4c 5553  er_params['X-LUS
 00022a40: 4944 2d53 444b 2d56 6572 7369 6f6e 275d  ID-SDK-Version']
-00022a50: 203d 2027 312e 302e 3827 0a0a 2020 2020   = '1.0.8'..    
+00022a50: 203d 2027 312e 302e 3927 0a0a 2020 2020   = '1.0.9'..    
 00022a60: 2020 2020 2320 4175 7468 656e 7469 6361      # Authentica
 00022a70: 7469 6f6e 2073 6574 7469 6e67 0a20 2020  tion setting.   
 00022a80: 2020 2020 2061 7574 685f 7365 7474 696e       auth_settin
 00022a90: 6773 203d 205b 276f 6175 7468 3227 5d20  gs = ['oauth2'] 
 00022aa0: 2023 206e 6f71 613a 2045 3530 310a 0a20   # noqa: E501.. 
 00022ab0: 2020 2020 2020 2072 6573 706f 6e73 655f         response_
 00022ac0: 7479 7065 735f 6d61 7020 3d20 7b0a 2020  types_map = {.  
@@ -9870,15 +9870,15 @@
 000268d0: 4c55 5349 4420 6865 6164 6572 0a20 2020  LUSID header.   
 000268e0: 2020 2020 2068 6561 6465 725f 7061 7261       header_para
 000268f0: 6d73 5b27 582d 4c55 5349 442d 5344 4b2d  ms['X-LUSID-SDK-
 00026900: 4c61 6e67 7561 6765 275d 203d 2027 5079  Language'] = 'Py
 00026910: 7468 6f6e 270a 2020 2020 2020 2020 6865  thon'.        he
 00026920: 6164 6572 5f70 6172 616d 735b 2758 2d4c  ader_params['X-L
 00026930: 5553 4944 2d53 444b 2d56 6572 7369 6f6e  USID-SDK-Version
-00026940: 275d 203d 2027 312e 302e 3827 0a0a 2020  '] = '1.0.8'..  
+00026940: 275d 203d 2027 312e 302e 3927 0a0a 2020  '] = '1.0.9'..  
 00026950: 2020 2020 2020 2320 4175 7468 656e 7469        # Authenti
 00026960: 6361 7469 6f6e 2073 6574 7469 6e67 0a20  cation setting. 
 00026970: 2020 2020 2020 2061 7574 685f 7365 7474         auth_sett
 00026980: 696e 6773 203d 205b 276f 6175 7468 3227  ings = ['oauth2'
 00026990: 5d20 2023 206e 6f71 613a 2045 3530 310a  ]  # noqa: E501.
 000269a0: 0a20 2020 2020 2020 2072 6573 706f 6e73  .        respons
 000269b0: 655f 7479 7065 735f 6d61 7020 3d20 7b0a  e_types_map = {.
@@ -10557,15 +10557,15 @@
 000293c0: 4420 6865 6164 6572 0a20 2020 2020 2020  D header.       
 000293d0: 2068 6561 6465 725f 7061 7261 6d73 5b27   header_params['
 000293e0: 582d 4c55 5349 442d 5344 4b2d 4c61 6e67  X-LUSID-SDK-Lang
 000293f0: 7561 6765 275d 203d 2027 5079 7468 6f6e  uage'] = 'Python
 00029400: 270a 2020 2020 2020 2020 6865 6164 6572  '.        header
 00029410: 5f70 6172 616d 735b 2758 2d4c 5553 4944  _params['X-LUSID
 00029420: 2d53 444b 2d56 6572 7369 6f6e 275d 203d  -SDK-Version'] =
-00029430: 2027 312e 302e 3827 0a0a 2020 2020 2020   '1.0.8'..      
+00029430: 2027 312e 302e 3927 0a0a 2020 2020 2020   '1.0.9'..      
 00029440: 2020 2320 4175 7468 656e 7469 6361 7469    # Authenticati
 00029450: 6f6e 2073 6574 7469 6e67 0a20 2020 2020  on setting.     
 00029460: 2020 2061 7574 685f 7365 7474 696e 6773     auth_settings
 00029470: 203d 205b 276f 6175 7468 3227 5d20 2023   = ['oauth2']  #
 00029480: 206e 6f71 613a 2045 3530 310a 0a20 2020   noqa: E501..   
 00029490: 2020 2020 2072 6573 706f 6e73 655f 7479       response_ty
 000294a0: 7065 735f 6d61 7020 3d20 7b0a 2020 2020  pes_map = {.    
@@ -11586,15 +11586,15 @@
 0002d410: 6865 204c 5553 4944 2068 6561 6465 720a  he LUSID header.
 0002d420: 2020 2020 2020 2020 6865 6164 6572 5f70          header_p
 0002d430: 6172 616d 735b 2758 2d4c 5553 4944 2d53  arams['X-LUSID-S
 0002d440: 444b 2d4c 616e 6775 6167 6527 5d20 3d20  DK-Language'] = 
 0002d450: 2750 7974 686f 6e27 0a20 2020 2020 2020  'Python'.       
 0002d460: 2068 6561 6465 725f 7061 7261 6d73 5b27   header_params['
 0002d470: 582d 4c55 5349 442d 5344 4b2d 5665 7273  X-LUSID-SDK-Vers
-0002d480: 696f 6e27 5d20 3d20 2731 2e30 2e38 270a  ion'] = '1.0.8'.
+0002d480: 696f 6e27 5d20 3d20 2731 2e30 2e39 270a  ion'] = '1.0.9'.
 0002d490: 0a20 2020 2020 2020 2023 2041 7574 6865  .        # Authe
 0002d4a0: 6e74 6963 6174 696f 6e20 7365 7474 696e  ntication settin
 0002d4b0: 670a 2020 2020 2020 2020 6175 7468 5f73  g.        auth_s
 0002d4c0: 6574 7469 6e67 7320 3d20 5b27 6f61 7574  ettings = ['oaut
 0002d4d0: 6832 275d 2020 2320 6e6f 7161 3a20 4535  h2']  # noqa: E5
 0002d4e0: 3031 0a0a 2020 2020 2020 2020 7265 7370  01..        resp
 0002d4f0: 6f6e 7365 5f74 7970 6573 5f6d 6170 203d  onse_types_map =
@@ -12254,15 +12254,15 @@
 0002fdd0: 5553 4944 2068 6561 6465 720a 2020 2020  USID header.    
 0002fde0: 2020 2020 6865 6164 6572 5f70 6172 616d      header_param
 0002fdf0: 735b 2758 2d4c 5553 4944 2d53 444b 2d4c  s['X-LUSID-SDK-L
 0002fe00: 616e 6775 6167 6527 5d20 3d20 2750 7974  anguage'] = 'Pyt
 0002fe10: 686f 6e27 0a20 2020 2020 2020 2068 6561  hon'.        hea
 0002fe20: 6465 725f 7061 7261 6d73 5b27 582d 4c55  der_params['X-LU
 0002fe30: 5349 442d 5344 4b2d 5665 7273 696f 6e27  SID-SDK-Version'
-0002fe40: 5d20 3d20 2731 2e30 2e38 270a 0a20 2020  ] = '1.0.8'..   
+0002fe40: 5d20 3d20 2731 2e30 2e39 270a 0a20 2020  ] = '1.0.9'..   
 0002fe50: 2020 2020 2023 2041 7574 6865 6e74 6963       # Authentic
 0002fe60: 6174 696f 6e20 7365 7474 696e 670a 2020  ation setting.  
 0002fe70: 2020 2020 2020 6175 7468 5f73 6574 7469        auth_setti
 0002fe80: 6e67 7320 3d20 5b27 6f61 7574 6832 275d  ngs = ['oauth2']
 0002fe90: 2020 2320 6e6f 7161 3a20 4535 3031 0a0a    # noqa: E501..
 0002fea0: 2020 2020 2020 2020 7265 7370 6f6e 7365          response
 0002feb0: 5f74 7970 6573 5f6d 6170 203d 207b 0a20  _types_map = {. 
@@ -13131,15 +13131,15 @@
 000334a0: 6865 6164 6572 0a20 2020 2020 2020 2068  header.        h
 000334b0: 6561 6465 725f 7061 7261 6d73 5b27 582d  eader_params['X-
 000334c0: 4c55 5349 442d 5344 4b2d 4c61 6e67 7561  LUSID-SDK-Langua
 000334d0: 6765 275d 203d 2027 5079 7468 6f6e 270a  ge'] = 'Python'.
 000334e0: 2020 2020 2020 2020 6865 6164 6572 5f70          header_p
 000334f0: 6172 616d 735b 2758 2d4c 5553 4944 2d53  arams['X-LUSID-S
 00033500: 444b 2d56 6572 7369 6f6e 275d 203d 2027  DK-Version'] = '
-00033510: 312e 302e 3827 0a0a 2020 2020 2020 2020  1.0.8'..        
+00033510: 312e 302e 3927 0a0a 2020 2020 2020 2020  1.0.9'..        
 00033520: 2320 4175 7468 656e 7469 6361 7469 6f6e  # Authentication
 00033530: 2073 6574 7469 6e67 0a20 2020 2020 2020   setting.       
 00033540: 2061 7574 685f 7365 7474 696e 6773 203d   auth_settings =
 00033550: 205b 276f 6175 7468 3227 5d20 2023 206e   ['oauth2']  # n
 00033560: 6f71 613a 2045 3530 310a 0a20 2020 2020  oqa: E501..     
 00033570: 2020 2072 6573 706f 6e73 655f 7479 7065     response_type
 00033580: 735f 6d61 7020 3d20 7b0a 2020 2020 2020  s_map = {.      
@@ -13904,15 +13904,15 @@
 000364f0: 6520 4c55 5349 4420 6865 6164 6572 0a20  e LUSID header. 
 00036500: 2020 2020 2020 2068 6561 6465 725f 7061         header_pa
 00036510: 7261 6d73 5b27 582d 4c55 5349 442d 5344  rams['X-LUSID-SD
 00036520: 4b2d 4c61 6e67 7561 6765 275d 203d 2027  K-Language'] = '
 00036530: 5079 7468 6f6e 270a 2020 2020 2020 2020  Python'.        
 00036540: 6865 6164 6572 5f70 6172 616d 735b 2758  header_params['X
 00036550: 2d4c 5553 4944 2d53 444b 2d56 6572 7369  -LUSID-SDK-Versi
-00036560: 6f6e 275d 203d 2027 312e 302e 3827 0a0a  on'] = '1.0.8'..
+00036560: 6f6e 275d 203d 2027 312e 302e 3927 0a0a  on'] = '1.0.9'..
 00036570: 2020 2020 2020 2020 2320 4175 7468 656e          # Authen
 00036580: 7469 6361 7469 6f6e 2073 6574 7469 6e67  tication setting
 00036590: 0a20 2020 2020 2020 2061 7574 685f 7365  .        auth_se
 000365a0: 7474 696e 6773 203d 205b 276f 6175 7468  ttings = ['oauth
 000365b0: 3227 5d20 2023 206e 6f71 613a 2045 3530  2']  # noqa: E50
 000365c0: 310a 0a20 2020 2020 2020 2072 6573 706f  1..        respo
 000365d0: 6e73 655f 7479 7065 735f 6d61 7020 3d20  nse_types_map = 
@@ -14879,15 +14879,15 @@
 0003a1e0: 6520 4c55 5349 4420 6865 6164 6572 0a20  e LUSID header. 
 0003a1f0: 2020 2020 2020 2068 6561 6465 725f 7061         header_pa
 0003a200: 7261 6d73 5b27 582d 4c55 5349 442d 5344  rams['X-LUSID-SD
 0003a210: 4b2d 4c61 6e67 7561 6765 275d 203d 2027  K-Language'] = '
 0003a220: 5079 7468 6f6e 270a 2020 2020 2020 2020  Python'.        
 0003a230: 6865 6164 6572 5f70 6172 616d 735b 2758  header_params['X
 0003a240: 2d4c 5553 4944 2d53 444b 2d56 6572 7369  -LUSID-SDK-Versi
-0003a250: 6f6e 275d 203d 2027 312e 302e 3827 0a0a  on'] = '1.0.8'..
+0003a250: 6f6e 275d 203d 2027 312e 302e 3927 0a0a  on'] = '1.0.9'..
 0003a260: 2020 2020 2020 2020 2320 4175 7468 656e          # Authen
 0003a270: 7469 6361 7469 6f6e 2073 6574 7469 6e67  tication setting
 0003a280: 0a20 2020 2020 2020 2061 7574 685f 7365  .        auth_se
 0003a290: 7474 696e 6773 203d 205b 276f 6175 7468  ttings = ['oauth
 0003a2a0: 3227 5d20 2023 206e 6f71 613a 2045 3530  2']  # noqa: E50
 0003a2b0: 310a 0a20 2020 2020 2020 2072 6573 706f  1..        respo
 0003a2c0: 6e73 655f 7479 7065 735f 6d61 7020 3d20  nse_types_map = 
@@ -16008,15 +16008,15 @@
 0003e870: 4c55 5349 4420 6865 6164 6572 0a20 2020  LUSID header.   
 0003e880: 2020 2020 2068 6561 6465 725f 7061 7261       header_para
 0003e890: 6d73 5b27 582d 4c55 5349 442d 5344 4b2d  ms['X-LUSID-SDK-
 0003e8a0: 4c61 6e67 7561 6765 275d 203d 2027 5079  Language'] = 'Py
 0003e8b0: 7468 6f6e 270a 2020 2020 2020 2020 6865  thon'.        he
 0003e8c0: 6164 6572 5f70 6172 616d 735b 2758 2d4c  ader_params['X-L
 0003e8d0: 5553 4944 2d53 444b 2d56 6572 7369 6f6e  USID-SDK-Version
-0003e8e0: 275d 203d 2027 312e 302e 3827 0a0a 2020  '] = '1.0.8'..  
+0003e8e0: 275d 203d 2027 312e 302e 3927 0a0a 2020  '] = '1.0.9'..  
 0003e8f0: 2020 2020 2020 2320 4175 7468 656e 7469        # Authenti
 0003e900: 6361 7469 6f6e 2073 6574 7469 6e67 0a20  cation setting. 
 0003e910: 2020 2020 2020 2061 7574 685f 7365 7474         auth_sett
 0003e920: 696e 6773 203d 205b 276f 6175 7468 3227  ings = ['oauth2'
 0003e930: 5d20 2023 206e 6f71 613a 2045 3530 310a  ]  # noqa: E501.
 0003e940: 0a20 2020 2020 2020 2072 6573 706f 6e73  .        respons
 0003e950: 655f 7479 7065 735f 6d61 7020 3d20 7b0a  e_types_map = {.
@@ -17173,15 +17173,15 @@
 00043140: 4944 2068 6561 6465 720a 2020 2020 2020  ID header.      
 00043150: 2020 6865 6164 6572 5f70 6172 616d 735b    header_params[
 00043160: 2758 2d4c 5553 4944 2d53 444b 2d4c 616e  'X-LUSID-SDK-Lan
 00043170: 6775 6167 6527 5d20 3d20 2750 7974 686f  guage'] = 'Pytho
 00043180: 6e27 0a20 2020 2020 2020 2068 6561 6465  n'.        heade
 00043190: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 000431a0: 442d 5344 4b2d 5665 7273 696f 6e27 5d20  D-SDK-Version'] 
-000431b0: 3d20 2731 2e30 2e38 270a 0a20 2020 2020  = '1.0.8'..     
+000431b0: 3d20 2731 2e30 2e39 270a 0a20 2020 2020  = '1.0.9'..     
 000431c0: 2020 2023 2041 7574 6865 6e74 6963 6174     # Authenticat
 000431d0: 696f 6e20 7365 7474 696e 670a 2020 2020  ion setting.    
 000431e0: 2020 2020 6175 7468 5f73 6574 7469 6e67      auth_setting
 000431f0: 7320 3d20 5b27 6f61 7574 6832 275d 2020  s = ['oauth2']  
 00043200: 2320 6e6f 7161 3a20 4535 3031 0a0a 2020  # noqa: E501..  
 00043210: 2020 2020 2020 7265 7370 6f6e 7365 5f74        response_t
 00043220: 7970 6573 5f6d 6170 203d 207b 0a20 2020  ypes_map = {.   
@@ -18145,15 +18145,15 @@
 00046e00: 6572 0a20 2020 2020 2020 2068 6561 6465  er.        heade
 00046e10: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 00046e20: 442d 5344 4b2d 4c61 6e67 7561 6765 275d  D-SDK-Language']
 00046e30: 203d 2027 5079 7468 6f6e 270a 2020 2020   = 'Python'.    
 00046e40: 2020 2020 6865 6164 6572 5f70 6172 616d      header_param
 00046e50: 735b 2758 2d4c 5553 4944 2d53 444b 2d56  s['X-LUSID-SDK-V
 00046e60: 6572 7369 6f6e 275d 203d 2027 312e 302e  ersion'] = '1.0.
-00046e70: 3827 0a0a 2020 2020 2020 2020 2320 4175  8'..        # Au
+00046e70: 3927 0a0a 2020 2020 2020 2020 2320 4175  9'..        # Au
 00046e80: 7468 656e 7469 6361 7469 6f6e 2073 6574  thentication set
 00046e90: 7469 6e67 0a20 2020 2020 2020 2061 7574  ting.        aut
 00046ea0: 685f 7365 7474 696e 6773 203d 205b 276f  h_settings = ['o
 00046eb0: 6175 7468 3227 5d20 2023 206e 6f71 613a  auth2']  # noqa:
 00046ec0: 2045 3530 310a 0a20 2020 2020 2020 2072   E501..        r
 00046ed0: 6573 706f 6e73 655f 7479 7065 735f 6d61  esponse_types_ma
 00046ee0: 7020 3d20 7b0a 2020 2020 2020 2020 2020  p = {.          
@@ -18839,15 +18839,15 @@
 00049960: 6572 0a20 2020 2020 2020 2068 6561 6465  er.        heade
 00049970: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 00049980: 442d 5344 4b2d 4c61 6e67 7561 6765 275d  D-SDK-Language']
 00049990: 203d 2027 5079 7468 6f6e 270a 2020 2020   = 'Python'.    
 000499a0: 2020 2020 6865 6164 6572 5f70 6172 616d      header_param
 000499b0: 735b 2758 2d4c 5553 4944 2d53 444b 2d56  s['X-LUSID-SDK-V
 000499c0: 6572 7369 6f6e 275d 203d 2027 312e 302e  ersion'] = '1.0.
-000499d0: 3827 0a0a 2020 2020 2020 2020 2320 4175  8'..        # Au
+000499d0: 3927 0a0a 2020 2020 2020 2020 2320 4175  9'..        # Au
 000499e0: 7468 656e 7469 6361 7469 6f6e 2073 6574  thentication set
 000499f0: 7469 6e67 0a20 2020 2020 2020 2061 7574  ting.        aut
 00049a00: 685f 7365 7474 696e 6773 203d 205b 276f  h_settings = ['o
 00049a10: 6175 7468 3227 5d20 2023 206e 6f71 613a  auth2']  # noqa:
 00049a20: 2045 3530 310a 0a20 2020 2020 2020 2072   E501..        r
 00049a30: 6573 706f 6e73 655f 7479 7065 735f 6d61  esponse_types_ma
 00049a40: 7020 3d20 7b0a 2020 2020 2020 2020 2020  p = {.          
@@ -19985,15 +19985,15 @@
 0004e100: 4944 2068 6561 6465 720a 2020 2020 2020  ID header.      
 0004e110: 2020 6865 6164 6572 5f70 6172 616d 735b    header_params[
 0004e120: 2758 2d4c 5553 4944 2d53 444b 2d4c 616e  'X-LUSID-SDK-Lan
 0004e130: 6775 6167 6527 5d20 3d20 2750 7974 686f  guage'] = 'Pytho
 0004e140: 6e27 0a20 2020 2020 2020 2068 6561 6465  n'.        heade
 0004e150: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 0004e160: 442d 5344 4b2d 5665 7273 696f 6e27 5d20  D-SDK-Version'] 
-0004e170: 3d20 2731 2e30 2e38 270a 0a20 2020 2020  = '1.0.8'..     
+0004e170: 3d20 2731 2e30 2e39 270a 0a20 2020 2020  = '1.0.9'..     
 0004e180: 2020 2023 2041 7574 6865 6e74 6963 6174     # Authenticat
 0004e190: 696f 6e20 7365 7474 696e 670a 2020 2020  ion setting.    
 0004e1a0: 2020 2020 6175 7468 5f73 6574 7469 6e67      auth_setting
 0004e1b0: 7320 3d20 5b27 6f61 7574 6832 275d 2020  s = ['oauth2']  
 0004e1c0: 2320 6e6f 7161 3a20 4535 3031 0a0a 2020  # noqa: E501..  
 0004e1d0: 2020 2020 2020 7265 7370 6f6e 7365 5f74        response_t
 0004e1e0: 7970 6573 5f6d 6170 203d 207b 0a20 2020  ypes_map = {.   
@@ -21224,15 +21224,15 @@
 00052e70: 204c 5553 4944 2068 6561 6465 720a 2020   LUSID header.  
 00052e80: 2020 2020 2020 6865 6164 6572 5f70 6172        header_par
 00052e90: 616d 735b 2758 2d4c 5553 4944 2d53 444b  ams['X-LUSID-SDK
 00052ea0: 2d4c 616e 6775 6167 6527 5d20 3d20 2750  -Language'] = 'P
 00052eb0: 7974 686f 6e27 0a20 2020 2020 2020 2068  ython'.        h
 00052ec0: 6561 6465 725f 7061 7261 6d73 5b27 582d  eader_params['X-
 00052ed0: 4c55 5349 442d 5344 4b2d 5665 7273 696f  LUSID-SDK-Versio
-00052ee0: 6e27 5d20 3d20 2731 2e30 2e38 270a 0a20  n'] = '1.0.8'.. 
+00052ee0: 6e27 5d20 3d20 2731 2e30 2e39 270a 0a20  n'] = '1.0.9'.. 
 00052ef0: 2020 2020 2020 2023 2041 7574 6865 6e74         # Authent
 00052f00: 6963 6174 696f 6e20 7365 7474 696e 670a  ication setting.
 00052f10: 2020 2020 2020 2020 6175 7468 5f73 6574          auth_set
 00052f20: 7469 6e67 7320 3d20 5b27 6f61 7574 6832  tings = ['oauth2
 00052f30: 275d 2020 2320 6e6f 7161 3a20 4535 3031  ']  # noqa: E501
 00052f40: 0a0a 2020 2020 2020 2020 7265 7370 6f6e  ..        respon
 00052f50: 7365 5f74 7970 6573 5f6d 6170 203d 207b  se_types_map = {
@@ -22293,15 +22293,15 @@
 00057140: 6561 6465 720a 2020 2020 2020 2020 6865  eader.        he
 00057150: 6164 6572 5f70 6172 616d 735b 2758 2d4c  ader_params['X-L
 00057160: 5553 4944 2d53 444b 2d4c 616e 6775 6167  USID-SDK-Languag
 00057170: 6527 5d20 3d20 2750 7974 686f 6e27 0a20  e'] = 'Python'. 
 00057180: 2020 2020 2020 2068 6561 6465 725f 7061         header_pa
 00057190: 7261 6d73 5b27 582d 4c55 5349 442d 5344  rams['X-LUSID-SD
 000571a0: 4b2d 5665 7273 696f 6e27 5d20 3d20 2731  K-Version'] = '1
-000571b0: 2e30 2e38 270a 0a20 2020 2020 2020 2023  .0.8'..        #
+000571b0: 2e30 2e39 270a 0a20 2020 2020 2020 2023  .0.9'..        #
 000571c0: 2041 7574 6865 6e74 6963 6174 696f 6e20   Authentication 
 000571d0: 7365 7474 696e 670a 2020 2020 2020 2020  setting.        
 000571e0: 6175 7468 5f73 6574 7469 6e67 7320 3d20  auth_settings = 
 000571f0: 5b27 6f61 7574 6832 275d 2020 2320 6e6f  ['oauth2']  # no
 00057200: 7161 3a20 4535 3031 0a0a 2020 2020 2020  qa: E501..      
 00057210: 2020 7265 7370 6f6e 7365 5f74 7970 6573    response_types
 00057220: 5f6d 6170 203d 207b 0a20 2020 2020 2020  _map = {.       
@@ -23031,15 +23031,15 @@
 00059f60: 4c55 5349 4420 6865 6164 6572 0a20 2020  LUSID header.   
 00059f70: 2020 2020 2068 6561 6465 725f 7061 7261       header_para
 00059f80: 6d73 5b27 582d 4c55 5349 442d 5344 4b2d  ms['X-LUSID-SDK-
 00059f90: 4c61 6e67 7561 6765 275d 203d 2027 5079  Language'] = 'Py
 00059fa0: 7468 6f6e 270a 2020 2020 2020 2020 6865  thon'.        he
 00059fb0: 6164 6572 5f70 6172 616d 735b 2758 2d4c  ader_params['X-L
 00059fc0: 5553 4944 2d53 444b 2d56 6572 7369 6f6e  USID-SDK-Version
-00059fd0: 275d 203d 2027 312e 302e 3827 0a0a 2020  '] = '1.0.8'..  
+00059fd0: 275d 203d 2027 312e 302e 3927 0a0a 2020  '] = '1.0.9'..  
 00059fe0: 2020 2020 2020 2320 4175 7468 656e 7469        # Authenti
 00059ff0: 6361 7469 6f6e 2073 6574 7469 6e67 0a20  cation setting. 
 0005a000: 2020 2020 2020 2061 7574 685f 7365 7474         auth_sett
 0005a010: 696e 6773 203d 205b 276f 6175 7468 3227  ings = ['oauth2'
 0005a020: 5d20 2023 206e 6f71 613a 2045 3530 310a  ]  # noqa: E501.
 0005a030: 0a20 2020 2020 2020 2072 6573 706f 6e73  .        respons
 0005a040: 655f 7479 7065 735f 6d61 7020 3d20 7b0a  e_types_map = {.
@@ -24215,15 +24215,15 @@
 0005e960: 7468 6520 4c55 5349 4420 6865 6164 6572  the LUSID header
 0005e970: 0a20 2020 2020 2020 2068 6561 6465 725f  .        header_
 0005e980: 7061 7261 6d73 5b27 582d 4c55 5349 442d  params['X-LUSID-
 0005e990: 5344 4b2d 4c61 6e67 7561 6765 275d 203d  SDK-Language'] =
 0005e9a0: 2027 5079 7468 6f6e 270a 2020 2020 2020   'Python'.      
 0005e9b0: 2020 6865 6164 6572 5f70 6172 616d 735b    header_params[
 0005e9c0: 2758 2d4c 5553 4944 2d53 444b 2d56 6572  'X-LUSID-SDK-Ver
-0005e9d0: 7369 6f6e 275d 203d 2027 312e 302e 3827  sion'] = '1.0.8'
+0005e9d0: 7369 6f6e 275d 203d 2027 312e 302e 3927  sion'] = '1.0.9'
 0005e9e0: 0a0a 2020 2020 2020 2020 2320 4175 7468  ..        # Auth
 0005e9f0: 656e 7469 6361 7469 6f6e 2073 6574 7469  entication setti
 0005ea00: 6e67 0a20 2020 2020 2020 2061 7574 685f  ng.        auth_
 0005ea10: 7365 7474 696e 6773 203d 205b 276f 6175  settings = ['oau
 0005ea20: 7468 3227 5d20 2023 206e 6f71 613a 2045  th2']  # noqa: E
 0005ea30: 3530 310a 0a20 2020 2020 2020 2072 6573  501..        res
 0005ea40: 706f 6e73 655f 7479 7065 735f 6d61 7020  ponse_types_map 
@@ -25733,15 +25733,15 @@
 00064840: 5349 4420 6865 6164 6572 0a20 2020 2020  SID header.     
 00064850: 2020 2068 6561 6465 725f 7061 7261 6d73     header_params
 00064860: 5b27 582d 4c55 5349 442d 5344 4b2d 4c61  ['X-LUSID-SDK-La
 00064870: 6e67 7561 6765 275d 203d 2027 5079 7468  nguage'] = 'Pyth
 00064880: 6f6e 270a 2020 2020 2020 2020 6865 6164  on'.        head
 00064890: 6572 5f70 6172 616d 735b 2758 2d4c 5553  er_params['X-LUS
 000648a0: 4944 2d53 444b 2d56 6572 7369 6f6e 275d  ID-SDK-Version']
-000648b0: 203d 2027 312e 302e 3827 0a0a 2020 2020   = '1.0.8'..    
+000648b0: 203d 2027 312e 302e 3927 0a0a 2020 2020   = '1.0.9'..    
 000648c0: 2020 2020 2320 4175 7468 656e 7469 6361      # Authentica
 000648d0: 7469 6f6e 2073 6574 7469 6e67 0a20 2020  tion setting.   
 000648e0: 2020 2020 2061 7574 685f 7365 7474 696e       auth_settin
 000648f0: 6773 203d 205b 276f 6175 7468 3227 5d20  gs = ['oauth2'] 
 00064900: 2023 206e 6f71 613a 2045 3530 310a 0a20   # noqa: E501.. 
 00064910: 2020 2020 2020 2072 6573 706f 6e73 655f         response_
 00064920: 7479 7065 735f 6d61 7020 3d20 7b0a 2020  types_map = {.  
@@ -26498,15 +26498,15 @@
 00067810: 6865 6164 6572 0a20 2020 2020 2020 2068  header.        h
 00067820: 6561 6465 725f 7061 7261 6d73 5b27 582d  eader_params['X-
 00067830: 4c55 5349 442d 5344 4b2d 4c61 6e67 7561  LUSID-SDK-Langua
 00067840: 6765 275d 203d 2027 5079 7468 6f6e 270a  ge'] = 'Python'.
 00067850: 2020 2020 2020 2020 6865 6164 6572 5f70          header_p
 00067860: 6172 616d 735b 2758 2d4c 5553 4944 2d53  arams['X-LUSID-S
 00067870: 444b 2d56 6572 7369 6f6e 275d 203d 2027  DK-Version'] = '
-00067880: 312e 302e 3827 0a0a 2020 2020 2020 2020  1.0.8'..        
+00067880: 312e 302e 3927 0a0a 2020 2020 2020 2020  1.0.9'..        
 00067890: 2320 4175 7468 656e 7469 6361 7469 6f6e  # Authentication
 000678a0: 2073 6574 7469 6e67 0a20 2020 2020 2020   setting.       
 000678b0: 2061 7574 685f 7365 7474 696e 6773 203d   auth_settings =
 000678c0: 205b 276f 6175 7468 3227 5d20 2023 206e   ['oauth2']  # n
 000678d0: 6f71 613a 2045 3530 310a 0a20 2020 2020  oqa: E501..     
 000678e0: 2020 2072 6573 706f 6e73 655f 7479 7065     response_type
 000678f0: 735f 6d61 7020 3d20 7b0a 2020 2020 2020  s_map = {.      
@@ -27409,15 +27409,15 @@
 0006b100: 4944 2068 6561 6465 720a 2020 2020 2020  ID header.      
 0006b110: 2020 6865 6164 6572 5f70 6172 616d 735b    header_params[
 0006b120: 2758 2d4c 5553 4944 2d53 444b 2d4c 616e  'X-LUSID-SDK-Lan
 0006b130: 6775 6167 6527 5d20 3d20 2750 7974 686f  guage'] = 'Pytho
 0006b140: 6e27 0a20 2020 2020 2020 2068 6561 6465  n'.        heade
 0006b150: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 0006b160: 442d 5344 4b2d 5665 7273 696f 6e27 5d20  D-SDK-Version'] 
-0006b170: 3d20 2731 2e30 2e38 270a 0a20 2020 2020  = '1.0.8'..     
+0006b170: 3d20 2731 2e30 2e39 270a 0a20 2020 2020  = '1.0.9'..     
 0006b180: 2020 2023 2041 7574 6865 6e74 6963 6174     # Authenticat
 0006b190: 696f 6e20 7365 7474 696e 670a 2020 2020  ion setting.    
 0006b1a0: 2020 2020 6175 7468 5f73 6574 7469 6e67      auth_setting
 0006b1b0: 7320 3d20 5b27 6f61 7574 6832 275d 2020  s = ['oauth2']  
 0006b1c0: 2320 6e6f 7161 3a20 4535 3031 0a0a 2020  # noqa: E501..  
 0006b1d0: 2020 2020 2020 7265 7370 6f6e 7365 5f74        response_t
 0006b1e0: 7970 6573 5f6d 6170 203d 207b 0a20 2020  ypes_map = {.   
@@ -28229,15 +28229,15 @@
 0006e440: 4944 2068 6561 6465 720a 2020 2020 2020  ID header.      
 0006e450: 2020 6865 6164 6572 5f70 6172 616d 735b    header_params[
 0006e460: 2758 2d4c 5553 4944 2d53 444b 2d4c 616e  'X-LUSID-SDK-Lan
 0006e470: 6775 6167 6527 5d20 3d20 2750 7974 686f  guage'] = 'Pytho
 0006e480: 6e27 0a20 2020 2020 2020 2068 6561 6465  n'.        heade
 0006e490: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 0006e4a0: 442d 5344 4b2d 5665 7273 696f 6e27 5d20  D-SDK-Version'] 
-0006e4b0: 3d20 2731 2e30 2e38 270a 0a20 2020 2020  = '1.0.8'..     
+0006e4b0: 3d20 2731 2e30 2e39 270a 0a20 2020 2020  = '1.0.9'..     
 0006e4c0: 2020 2023 2041 7574 6865 6e74 6963 6174     # Authenticat
 0006e4d0: 696f 6e20 7365 7474 696e 670a 2020 2020  ion setting.    
 0006e4e0: 2020 2020 6175 7468 5f73 6574 7469 6e67      auth_setting
 0006e4f0: 7320 3d20 5b27 6f61 7574 6832 275d 2020  s = ['oauth2']  
 0006e500: 2320 6e6f 7161 3a20 4535 3031 0a0a 2020  # noqa: E501..  
 0006e510: 2020 2020 2020 7265 7370 6f6e 7365 5f74        response_t
 0006e520: 7970 6573 5f6d 6170 203d 207b 0a20 2020  ypes_map = {.   
@@ -28931,15 +28931,15 @@
 00071020: 7468 6520 4c55 5349 4420 6865 6164 6572  the LUSID header
 00071030: 0a20 2020 2020 2020 2068 6561 6465 725f  .        header_
 00071040: 7061 7261 6d73 5b27 582d 4c55 5349 442d  params['X-LUSID-
 00071050: 5344 4b2d 4c61 6e67 7561 6765 275d 203d  SDK-Language'] =
 00071060: 2027 5079 7468 6f6e 270a 2020 2020 2020   'Python'.      
 00071070: 2020 6865 6164 6572 5f70 6172 616d 735b    header_params[
 00071080: 2758 2d4c 5553 4944 2d53 444b 2d56 6572  'X-LUSID-SDK-Ver
-00071090: 7369 6f6e 275d 203d 2027 312e 302e 3827  sion'] = '1.0.8'
+00071090: 7369 6f6e 275d 203d 2027 312e 302e 3927  sion'] = '1.0.9'
 000710a0: 0a0a 2020 2020 2020 2020 2320 4175 7468  ..        # Auth
 000710b0: 656e 7469 6361 7469 6f6e 2073 6574 7469  entication setti
 000710c0: 6e67 0a20 2020 2020 2020 2061 7574 685f  ng.        auth_
 000710d0: 7365 7474 696e 6773 203d 205b 276f 6175  settings = ['oau
 000710e0: 7468 3227 5d20 2023 206e 6f71 613a 2045  th2']  # noqa: E
 000710f0: 3530 310a 0a20 2020 2020 2020 2072 6573  501..        res
 00071100: 706f 6e73 655f 7479 7065 735f 6d61 7020  ponse_types_map 
@@ -30000,15 +30000,15 @@
 000752f0: 6561 6465 720a 2020 2020 2020 2020 6865  eader.        he
 00075300: 6164 6572 5f70 6172 616d 735b 2758 2d4c  ader_params['X-L
 00075310: 5553 4944 2d53 444b 2d4c 616e 6775 6167  USID-SDK-Languag
 00075320: 6527 5d20 3d20 2750 7974 686f 6e27 0a20  e'] = 'Python'. 
 00075330: 2020 2020 2020 2068 6561 6465 725f 7061         header_pa
 00075340: 7261 6d73 5b27 582d 4c55 5349 442d 5344  rams['X-LUSID-SD
 00075350: 4b2d 5665 7273 696f 6e27 5d20 3d20 2731  K-Version'] = '1
-00075360: 2e30 2e38 270a 0a20 2020 2020 2020 2023  .0.8'..        #
+00075360: 2e30 2e39 270a 0a20 2020 2020 2020 2023  .0.9'..        #
 00075370: 2041 7574 6865 6e74 6963 6174 696f 6e20   Authentication 
 00075380: 7365 7474 696e 670a 2020 2020 2020 2020  setting.        
 00075390: 6175 7468 5f73 6574 7469 6e67 7320 3d20  auth_settings = 
 000753a0: 5b27 6f61 7574 6832 275d 2020 2320 6e6f  ['oauth2']  # no
 000753b0: 7161 3a20 4535 3031 0a0a 2020 2020 2020  qa: E501..      
 000753c0: 2020 7265 7370 6f6e 7365 5f74 7970 6573    response_types
 000753d0: 5f6d 6170 203d 207b 0a20 2020 2020 2020  _map = {.       
@@ -30765,15 +30765,15 @@
 000782c0: 6465 720a 2020 2020 2020 2020 6865 6164  der.        head
 000782d0: 6572 5f70 6172 616d 735b 2758 2d4c 5553  er_params['X-LUS
 000782e0: 4944 2d53 444b 2d4c 616e 6775 6167 6527  ID-SDK-Language'
 000782f0: 5d20 3d20 2750 7974 686f 6e27 0a20 2020  ] = 'Python'.   
 00078300: 2020 2020 2068 6561 6465 725f 7061 7261       header_para
 00078310: 6d73 5b27 582d 4c55 5349 442d 5344 4b2d  ms['X-LUSID-SDK-
 00078320: 5665 7273 696f 6e27 5d20 3d20 2731 2e30  Version'] = '1.0
-00078330: 2e38 270a 0a20 2020 2020 2020 2023 2041  .8'..        # A
+00078330: 2e39 270a 0a20 2020 2020 2020 2023 2041  .9'..        # A
 00078340: 7574 6865 6e74 6963 6174 696f 6e20 7365  uthentication se
 00078350: 7474 696e 670a 2020 2020 2020 2020 6175  tting.        au
 00078360: 7468 5f73 6574 7469 6e67 7320 3d20 5b27  th_settings = ['
 00078370: 6f61 7574 6832 275d 2020 2320 6e6f 7161  oauth2']  # noqa
 00078380: 3a20 4535 3031 0a0a 2020 2020 2020 2020  : E501..        
 00078390: 7265 7370 6f6e 7365 5f74 7970 6573 5f6d  response_types_m
 000783a0: 6170 203d 207b 0a20 2020 2020 2020 2020  ap = {.         
@@ -31531,15 +31531,15 @@
 0007b2a0: 6164 6572 0a20 2020 2020 2020 2068 6561  ader.        hea
 0007b2b0: 6465 725f 7061 7261 6d73 5b27 582d 4c55  der_params['X-LU
 0007b2c0: 5349 442d 5344 4b2d 4c61 6e67 7561 6765  SID-SDK-Language
 0007b2d0: 275d 203d 2027 5079 7468 6f6e 270a 2020  '] = 'Python'.  
 0007b2e0: 2020 2020 2020 6865 6164 6572 5f70 6172        header_par
 0007b2f0: 616d 735b 2758 2d4c 5553 4944 2d53 444b  ams['X-LUSID-SDK
 0007b300: 2d56 6572 7369 6f6e 275d 203d 2027 312e  -Version'] = '1.
-0007b310: 302e 3827 0a0a 2020 2020 2020 2020 2320  0.8'..        # 
+0007b310: 302e 3927 0a0a 2020 2020 2020 2020 2320  0.9'..        # 
 0007b320: 4175 7468 656e 7469 6361 7469 6f6e 2073  Authentication s
 0007b330: 6574 7469 6e67 0a20 2020 2020 2020 2061  etting.        a
 0007b340: 7574 685f 7365 7474 696e 6773 203d 205b  uth_settings = [
 0007b350: 276f 6175 7468 3227 5d20 2023 206e 6f71  'oauth2']  # noq
 0007b360: 613a 2045 3530 310a 0a20 2020 2020 2020  a: E501..       
 0007b370: 2072 6573 706f 6e73 655f 7479 7065 735f   response_types_
 0007b380: 6d61 7020 3d20 7b0a 2020 2020 2020 2020  map = {.        
@@ -32225,15 +32225,15 @@
 0007de00: 4944 2068 6561 6465 720a 2020 2020 2020  ID header.      
 0007de10: 2020 6865 6164 6572 5f70 6172 616d 735b    header_params[
 0007de20: 2758 2d4c 5553 4944 2d53 444b 2d4c 616e  'X-LUSID-SDK-Lan
 0007de30: 6775 6167 6527 5d20 3d20 2750 7974 686f  guage'] = 'Pytho
 0007de40: 6e27 0a20 2020 2020 2020 2068 6561 6465  n'.        heade
 0007de50: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 0007de60: 442d 5344 4b2d 5665 7273 696f 6e27 5d20  D-SDK-Version'] 
-0007de70: 3d20 2731 2e30 2e38 270a 0a20 2020 2020  = '1.0.8'..     
+0007de70: 3d20 2731 2e30 2e39 270a 0a20 2020 2020  = '1.0.9'..     
 0007de80: 2020 2023 2041 7574 6865 6e74 6963 6174     # Authenticat
 0007de90: 696f 6e20 7365 7474 696e 670a 2020 2020  ion setting.    
 0007dea0: 2020 2020 6175 7468 5f73 6574 7469 6e67      auth_setting
 0007deb0: 7320 3d20 5b27 6f61 7574 6832 275d 2020  s = ['oauth2']  
 0007dec0: 2320 6e6f 7161 3a20 4535 3031 0a0a 2020  # noqa: E501..  
 0007ded0: 2020 2020 2020 7265 7370 6f6e 7365 5f74        response_t
 0007dee0: 7970 6573 5f6d 6170 203d 207b 0a20 2020  ypes_map = {.
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api/translation_api.py` & `lusid-sdk-preview-1.0.9/lusid/api/translation_api.py`

 * *Files identical despite different names*

```diff
@@ -1,15 +1,15 @@
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
             200: "TranslateInstrumentDefinitionsResponse",
             400: "LusidValidationProblemDetails",
@@ -306,15 +306,15 @@
 
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
             200: "TranslateTradeTicketsResponse",
             400: "LusidValidationProblemDetails",
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/api_client.py` & `lusid-sdk-preview-1.0.9/lusid/api_client.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/configuration.py` & `lusid-sdk-preview-1.0.9/lusid/configuration.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/exceptions.py` & `lusid-sdk-preview-1.0.9/lusid/exceptions.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/__init__.py` & `lusid-sdk-preview-1.0.9/lusid/models/__init__.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/a2_b_breakdown.py` & `lusid-sdk-preview-1.0.9/lusid/models/a2_b_breakdown.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/a2_b_category.py` & `lusid-sdk-preview-1.0.9/lusid/models/a2_b_category.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/a2_b_data_record.py` & `lusid-sdk-preview-1.0.9/lusid/models/a2_b_data_record.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/a2_b_movement_record.py` & `lusid-sdk-preview-1.0.9/lusid/models/a2_b_movement_record.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/abor.py` & `lusid-sdk-preview-1.0.9/lusid/models/abor.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/abor_configuration.py` & `lusid-sdk-preview-1.0.9/lusid/models/abor_configuration.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/abor_configuration_properties.py` & `lusid-sdk-preview-1.0.9/lusid/models/abor_configuration_properties.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/abor_configuration_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/abor_configuration_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/abor_properties.py` & `lusid-sdk-preview-1.0.9/lusid/models/abor_properties.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/abor_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/abor_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/access_controlled_action.py` & `lusid-sdk-preview-1.0.9/lusid/models/access_controlled_action.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/access_controlled_resource.py` & `lusid-sdk-preview-1.0.9/lusid/models/access_controlled_resource.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/access_metadata_operation.py` & `lusid-sdk-preview-1.0.9/lusid/models/access_metadata_operation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/access_metadata_value.py` & `lusid-sdk-preview-1.0.9/lusid/models/access_metadata_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/account.py` & `lusid-sdk-preview-1.0.9/lusid/models/account.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/account_properties.py` & `lusid-sdk-preview-1.0.9/lusid/models/account_properties.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/accounting_method.py` & `lusid-sdk-preview-1.0.9/lusid/models/accounting_method.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/accounts_upsert_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/accounts_upsert_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/action_id.py` & `lusid-sdk-preview-1.0.9/lusid/models/action_id.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/action_result_of_portfolio.py` & `lusid-sdk-preview-1.0.9/lusid/models/action_result_of_portfolio.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/add_business_days_to_date_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/add_business_days_to_date_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/add_business_days_to_date_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/add_business_days_to_date_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/address_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/address_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/address_key_filter.py` & `lusid-sdk-preview-1.0.9/lusid/models/address_key_filter.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/address_key_option_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/address_key_option_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/adjust_holding.py` & `lusid-sdk-preview-1.0.9/lusid/models/adjust_holding.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/adjust_holding_for_date_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/adjust_holding_for_date_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/adjust_holding_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/adjust_holding_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/aggregate_spec.py` & `lusid-sdk-preview-1.0.9/lusid/models/aggregate_spec.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/aggregated_return.py` & `lusid-sdk-preview-1.0.9/lusid/models/aggregated_return.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/aggregated_returns_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/aggregated_returns_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/aggregated_returns_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/aggregated_returns_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/aggregation.py` & `lusid-sdk-preview-1.0.9/lusid/models/aggregation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/aggregation_context.py` & `lusid-sdk-preview-1.0.9/lusid/models/aggregation_context.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/aggregation_measure_failure_detail.py` & `lusid-sdk-preview-1.0.9/lusid/models/aggregation_measure_failure_detail.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/aggregation_op.py` & `lusid-sdk-preview-1.0.9/lusid/models/aggregation_op.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/aggregation_options.py` & `lusid-sdk-preview-1.0.9/lusid/models/aggregation_options.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/aggregation_query.py` & `lusid-sdk-preview-1.0.9/lusid/models/aggregation_query.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/aggregation_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/aggregation_type.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/allocation.py` & `lusid-sdk-preview-1.0.9/lusid/models/allocation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/allocation_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/allocation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/allocation_set_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/allocation_set_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/amortisation_event.py` & `lusid-sdk-preview-1.0.9/lusid/models/amortisation_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/amortisation_event_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/amortisation_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/annul_quotes_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/annul_quotes_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/annul_single_structured_data_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/annul_single_structured_data_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/annul_structured_data_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/annul_structured_data_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/asset_class.py` & `lusid-sdk-preview-1.0.9/lusid/models/asset_class.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/barrier.py` & `lusid-sdk-preview-1.0.9/lusid/models/barrier.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/basket.py` & `lusid-sdk-preview-1.0.9/lusid/models/basket.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/basket_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/basket_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/basket_identifier.py` & `lusid-sdk-preview-1.0.9/lusid/models/basket_identifier.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/batch_adjust_holdings_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/batch_adjust_holdings_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/batch_upsert_portfolio_transactions_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/batch_upsert_portfolio_transactions_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/block.py` & `lusid-sdk-preview-1.0.9/lusid/models/block.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/block_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/block_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/block_set_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/block_set_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/bond.py` & `lusid-sdk-preview-1.0.9/lusid/models/bond.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/bond_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/bond_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/bond_default_event.py` & `lusid-sdk-preview-1.0.9/lusid/models/bond_default_event.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/bond_default_event_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/bond_default_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/bucketed_cash_flow_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/bucketed_cash_flow_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/bucketed_cash_flow_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/bucketed_cash_flow_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/calculation_info.py` & `lusid-sdk-preview-1.0.9/lusid/models/calculation_info.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/calendar.py` & `lusid-sdk-preview-1.0.9/lusid/models/calendar.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/calendar_date.py` & `lusid-sdk-preview-1.0.9/lusid/models/calendar_date.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cap_floor.py` & `lusid-sdk-preview-1.0.9/lusid/models/cap_floor.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cap_floor_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/cap_floor_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cash_dependency.py` & `lusid-sdk-preview-1.0.9/lusid/models/cash_dependency.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cash_dependency_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/cash_dependency_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cash_dividend_event.py` & `lusid-sdk-preview-1.0.9/lusid/models/cash_dividend_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cash_dividend_event_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/cash_dividend_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cash_flow_event.py` & `lusid-sdk-preview-1.0.9/lusid/models/cash_flow_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cash_flow_event_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/cash_flow_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cash_flow_lineage.py` & `lusid-sdk-preview-1.0.9/lusid/models/cash_flow_lineage.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cash_flow_value.py` & `lusid-sdk-preview-1.0.9/lusid/models/cash_flow_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cash_flow_value_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/cash_flow_value_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cash_flow_value_set.py` & `lusid-sdk-preview-1.0.9/lusid/models/cash_flow_value_set.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cash_flow_value_set_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/cash_flow_value_set_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cash_ladder_record.py` & `lusid-sdk-preview-1.0.9/lusid/models/cash_ladder_record.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cash_perpetual.py` & `lusid-sdk-preview-1.0.9/lusid/models/cash_perpetual.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cash_perpetual_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/cash_perpetual_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cds_flow_conventions.py` & `lusid-sdk-preview-1.0.9/lusid/models/cds_flow_conventions.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cds_index.py` & `lusid-sdk-preview-1.0.9/lusid/models/cds_index.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cds_index_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/cds_index_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cds_protection_detail_specification.py` & `lusid-sdk-preview-1.0.9/lusid/models/cds_protection_detail_specification.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/change.py` & `lusid-sdk-preview-1.0.9/lusid/models/change.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/change_history.py` & `lusid-sdk-preview-1.0.9/lusid/models/change_history.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/change_history_action.py` & `lusid-sdk-preview-1.0.9/lusid/models/change_history_action.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/change_item.py` & `lusid-sdk-preview-1.0.9/lusid/models/change_item.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/chart_of_accounts.py` & `lusid-sdk-preview-1.0.9/lusid/models/chart_of_accounts.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/chart_of_accounts_properties.py` & `lusid-sdk-preview-1.0.9/lusid/models/chart_of_accounts_properties.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/chart_of_accounts_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/chart_of_accounts_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/close_event.py` & `lusid-sdk-preview-1.0.9/lusid/models/close_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/close_event_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/close_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/complete_portfolio.py` & `lusid-sdk-preview-1.0.9/lusid/models/complete_portfolio.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/complete_relation.py` & `lusid-sdk-preview-1.0.9/lusid/models/complete_relation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/complete_relationship.py` & `lusid-sdk-preview-1.0.9/lusid/models/complete_relationship.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/complex_bond.py` & `lusid-sdk-preview-1.0.9/lusid/models/complex_bond.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/complex_bond_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/complex_bond_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/complex_market_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/complex_market_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/complex_market_data_id.py` & `lusid-sdk-preview-1.0.9/lusid/models/complex_market_data_id.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/compliance_breached_order_info.py` & `lusid-sdk-preview-1.0.9/lusid/models/compliance_breached_order_info.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/compliance_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/compliance_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/compliance_rule_result.py` & `lusid-sdk-preview-1.0.9/lusid/models/compliance_rule_result.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/compliance_rule_upsert_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/compliance_rule_upsert_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/compliance_rule_upsert_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/compliance_rule_upsert_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/compliance_run_info.py` & `lusid-sdk-preview-1.0.9/lusid/models/compliance_run_info.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/compounding.py` & `lusid-sdk-preview-1.0.9/lusid/models/compounding.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/configuration_recipe.py` & `lusid-sdk-preview-1.0.9/lusid/models/configuration_recipe.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/configuration_recipe_snippet.py` & `lusid-sdk-preview-1.0.9/lusid/models/configuration_recipe_snippet.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/constituents_adjustment_header.py` & `lusid-sdk-preview-1.0.9/lusid/models/constituents_adjustment_header.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/contract_for_difference.py` & `lusid-sdk-preview-1.0.9/lusid/models/contract_for_difference.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/contract_for_difference_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/contract_for_difference_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/corporate_action.py` & `lusid-sdk-preview-1.0.9/lusid/models/corporate_action.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/corporate_action_source.py` & `lusid-sdk-preview-1.0.9/lusid/models/corporate_action_source.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/corporate_action_transition.py` & `lusid-sdk-preview-1.0.9/lusid/models/corporate_action_transition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/corporate_action_transition_component.py` & `lusid-sdk-preview-1.0.9/lusid/models/corporate_action_transition_component.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/corporate_action_transition_component_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/corporate_action_transition_component_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/corporate_action_transition_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/corporate_action_transition_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/counterparty_agreement.py` & `lusid-sdk-preview-1.0.9/lusid/models/counterparty_agreement.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/counterparty_risk_information.py` & `lusid-sdk-preview-1.0.9/lusid/models/counterparty_risk_information.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/counterparty_signatory.py` & `lusid-sdk-preview-1.0.9/lusid/models/counterparty_signatory.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_calendar_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_calendar_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_corporate_action_source_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_corporate_action_source_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_cut_label_definition_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_cut_label_definition_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_data_map_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_data_map_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_data_type_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_data_type_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_date_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_date_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_derived_property_definition_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_derived_property_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_derived_transaction_portfolio_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_derived_transaction_portfolio_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_portfolio_details.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_portfolio_details.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_portfolio_group_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_portfolio_group_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_property_definition_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_property_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_recipe_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_recipe_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_reference_portfolio_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_reference_portfolio_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_relation_definition_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_relation_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_relation_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_relation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_relationship_definition_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_relationship_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_relationship_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_relationship_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_sequence_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_sequence_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_tax_rule_set_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_tax_rule_set_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_transaction_portfolio_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_transaction_portfolio_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/create_unit_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/create_unit_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/credit_default_swap.py` & `lusid-sdk-preview-1.0.9/lusid/models/credit_default_swap.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/credit_default_swap_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/credit_default_swap_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/credit_rating.py` & `lusid-sdk-preview-1.0.9/lusid/models/credit_rating.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/credit_spread_curve_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/credit_spread_curve_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/credit_spread_curve_data_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/credit_spread_curve_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/credit_support_annex.py` & `lusid-sdk-preview-1.0.9/lusid/models/credit_support_annex.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/criterion_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/criterion_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/currency_and_amount.py` & `lusid-sdk-preview-1.0.9/lusid/models/currency_and_amount.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/custodian_account.py` & `lusid-sdk-preview-1.0.9/lusid/models/custodian_account.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/custodian_account_properties.py` & `lusid-sdk-preview-1.0.9/lusid/models/custodian_account_properties.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/custodian_account_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/custodian_account_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/custodian_accounts_upsert_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/custodian_accounts_upsert_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/custom_entity_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/custom_entity_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/custom_entity_definition_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/custom_entity_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/custom_entity_field.py` & `lusid-sdk-preview-1.0.9/lusid/models/custom_entity_field.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/custom_entity_field_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/custom_entity_field_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/custom_entity_id.py` & `lusid-sdk-preview-1.0.9/lusid/models/custom_entity_id.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/custom_entity_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/custom_entity_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/custom_entity_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/custom_entity_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cut_label_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/cut_label_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/cut_local_time.py` & `lusid-sdk-preview-1.0.9/lusid/models/cut_local_time.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/data_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/data_definition.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/data_map_key.py` & `lusid-sdk-preview-1.0.9/lusid/models/data_map_key.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/data_mapping.py` & `lusid-sdk-preview-1.0.9/lusid/models/data_mapping.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/data_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/data_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/data_type_summary.py` & `lusid-sdk-preview-1.0.9/lusid/models/data_type_summary.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/data_type_value_range.py` & `lusid-sdk-preview-1.0.9/lusid/models/data_type_value_range.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/date_attributes.py` & `lusid-sdk-preview-1.0.9/lusid/models/date_attributes.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/date_range.py` & `lusid-sdk-preview-1.0.9/lusid/models/date_range.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/date_time_comparison_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/date_time_comparison_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/day_of_week.py` & `lusid-sdk-preview-1.0.9/lusid/models/day_of_week.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/delete_accounts_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/delete_accounts_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/delete_custodian_accounts_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/delete_custodian_accounts_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/delete_instrument_properties_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/delete_instrument_properties_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/delete_instrument_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/delete_instrument_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/delete_instruments_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/delete_instruments_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/delete_modes.py` & `lusid-sdk-preview-1.0.9/lusid/models/delete_modes.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/delete_relation_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/delete_relation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/delete_relationship_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/delete_relationship_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/deleted_entity_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/deleted_entity_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/dependency_source_filter.py` & `lusid-sdk-preview-1.0.9/lusid/models/dependency_source_filter.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/described_address_key.py` & `lusid-sdk-preview-1.0.9/lusid/models/described_address_key.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/discount_factor_curve_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/discount_factor_curve_data.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/discount_factor_curve_data_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/discount_factor_curve_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/discounting_dependency.py` & `lusid-sdk-preview-1.0.9/lusid/models/discounting_dependency.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/discounting_dependency_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/discounting_dependency_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/discounting_method.py` & `lusid-sdk-preview-1.0.9/lusid/models/discounting_method.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/economic_dependency.py` & `lusid-sdk-preview-1.0.9/lusid/models/economic_dependency.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/economic_dependency_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/economic_dependency_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/economic_dependency_with_complex_market_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/economic_dependency_with_complex_market_data.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/economic_dependency_with_quote.py` & `lusid-sdk-preview-1.0.9/lusid/models/economic_dependency_with_quote.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/empty_model_options.py` & `lusid-sdk-preview-1.0.9/lusid/models/empty_model_options.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/empty_model_options_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/empty_model_options_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/entity_identifier.py` & `lusid-sdk-preview-1.0.9/lusid/models/entity_identifier.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_all_of_identifiers.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_all_of_identifiers.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_curve_by_prices_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_curve_by_prices_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_curve_by_prices_data_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_curve_by_prices_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_curve_dependency.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_curve_dependency.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_curve_dependency_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_curve_dependency_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_model_options.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_model_options.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_model_options_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_model_options_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_option.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_option.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_option_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_option_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_swap.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_swap.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_swap_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_swap_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_vol_dependency.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_vol_dependency.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_vol_dependency_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_vol_dependency_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_vol_surface_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_vol_surface_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/equity_vol_surface_data_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/equity_vol_surface_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/error_detail.py` & `lusid-sdk-preview-1.0.9/lusid/models/error_detail.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/event_date_range.py` & `lusid-sdk-preview-1.0.9/lusid/models/event_date_range.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/exchange_traded_option.py` & `lusid-sdk-preview-1.0.9/lusid/models/exchange_traded_option.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/exchange_traded_option_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/exchange_traded_option_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/exchange_traded_option_contract_details.py` & `lusid-sdk-preview-1.0.9/lusid/models/exchange_traded_option_contract_details.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/execution.py` & `lusid-sdk-preview-1.0.9/lusid/models/execution.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/execution_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/execution_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/execution_set_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/execution_set_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/exercise_event.py` & `lusid-sdk-preview-1.0.9/lusid/models/exercise_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/exercise_event_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/exercise_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/exotic_instrument.py` & `lusid-sdk-preview-1.0.9/lusid/models/exotic_instrument.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/exotic_instrument_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/exotic_instrument_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/expanded_group.py` & `lusid-sdk-preview-1.0.9/lusid/models/expanded_group.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fee_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/fee_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fee_rule_upsert_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/fee_rule_upsert_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fee_rule_upsert_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/fee_rule_upsert_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/field_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/field_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/field_schema.py` & `lusid-sdk-preview-1.0.9/lusid/models/field_schema.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/field_value.py` & `lusid-sdk-preview-1.0.9/lusid/models/field_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/file_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/file_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fixed_leg.py` & `lusid-sdk-preview-1.0.9/lusid/models/fixed_leg.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fixed_leg_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/fixed_leg_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fixed_leg_all_of_overrides.py` & `lusid-sdk-preview-1.0.9/lusid/models/fixed_leg_all_of_overrides.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fixed_schedule.py` & `lusid-sdk-preview-1.0.9/lusid/models/fixed_schedule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fixed_schedule_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/fixed_schedule_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/float_schedule.py` & `lusid-sdk-preview-1.0.9/lusid/models/float_schedule.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/float_schedule_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/float_schedule_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/floating_leg.py` & `lusid-sdk-preview-1.0.9/lusid/models/floating_leg.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/floating_leg_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/floating_leg_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/flow_convention_name.py` & `lusid-sdk-preview-1.0.9/lusid/models/flow_convention_name.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/flow_conventions.py` & `lusid-sdk-preview-1.0.9/lusid/models/flow_conventions.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/forward_rate_agreement.py` & `lusid-sdk-preview-1.0.9/lusid/models/forward_rate_agreement.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/forward_rate_agreement_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/forward_rate_agreement_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/funding_leg.py` & `lusid-sdk-preview-1.0.9/lusid/models/funding_leg.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/funding_leg_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/funding_leg_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/funding_leg_options.py` & `lusid-sdk-preview-1.0.9/lusid/models/funding_leg_options.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/funding_leg_options_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/funding_leg_options_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/future.py` & `lusid-sdk-preview-1.0.9/lusid/models/future.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/future_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/future_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/futures_contract_details.py` & `lusid-sdk-preview-1.0.9/lusid/models/futures_contract_details.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_dependency.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_dependency.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_dependency_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_dependency_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forward.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forward.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forward_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forward_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forward_curve_by_quote_reference.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forward_curve_by_quote_reference.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forward_curve_by_quote_reference_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forward_curve_by_quote_reference_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forward_curve_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forward_curve_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forward_curve_data_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forward_curve_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forward_model_options.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forward_model_options.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forward_model_options_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forward_model_options_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forward_pips_curve_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forward_pips_curve_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forward_pips_curve_data_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forward_pips_curve_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forward_tenor_curve_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forward_tenor_curve_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forward_tenor_curve_data_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forward_tenor_curve_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forward_tenor_pips_curve_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forward_tenor_pips_curve_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forward_tenor_pips_curve_data_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forward_tenor_pips_curve_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forwards_dependency.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forwards_dependency.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_forwards_dependency_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_forwards_dependency_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_option.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_option.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_option_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_option_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_rate_schedule.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_rate_schedule.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_rate_schedule_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_rate_schedule_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_swap.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_swap.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_swap_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_swap_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_vol_dependency.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_vol_dependency.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_vol_dependency_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_vol_dependency_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/fx_vol_surface_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/fx_vol_surface_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/get_cds_flow_conventions_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/get_cds_flow_conventions_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/get_complex_market_data_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/get_complex_market_data_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/get_counterparty_agreement_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/get_counterparty_agreement_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/get_credit_support_annex_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/get_credit_support_annex_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/get_data_map_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/get_data_map_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/get_flow_conventions_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/get_flow_conventions_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/get_index_convention_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/get_index_convention_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/get_instruments_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/get_instruments_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/get_quotes_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/get_quotes_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/get_recipe_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/get_recipe_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/get_reference_portfolio_constituents_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/get_reference_portfolio_constituents_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/get_structured_result_data_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/get_structured_result_data_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/get_virtual_document_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/get_virtual_document_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/grouped_result_of_address_key.py` & `lusid-sdk-preview-1.0.9/lusid/models/grouped_result_of_address_key.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/holding_adjustment.py` & `lusid-sdk-preview-1.0.9/lusid/models/holding_adjustment.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/holding_adjustment_with_date.py` & `lusid-sdk-preview-1.0.9/lusid/models/holding_adjustment_with_date.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/holding_context.py` & `lusid-sdk-preview-1.0.9/lusid/models/holding_context.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/holdings_adjustment.py` & `lusid-sdk-preview-1.0.9/lusid/models/holdings_adjustment.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/holdings_adjustment_header.py` & `lusid-sdk-preview-1.0.9/lusid/models/holdings_adjustment_header.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/i_data_record.py` & `lusid-sdk-preview-1.0.9/lusid/models/i_data_record.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/i_unit_definition_dto.py` & `lusid-sdk-preview-1.0.9/lusid/models/i_unit_definition_dto.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/id_selector_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/id_selector_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/identifier_part_schema.py` & `lusid-sdk-preview-1.0.9/lusid/models/identifier_part_schema.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/index_convention.py` & `lusid-sdk-preview-1.0.9/lusid/models/index_convention.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/index_model_options.py` & `lusid-sdk-preview-1.0.9/lusid/models/index_model_options.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/index_model_options_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/index_model_options_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/index_projection_dependency.py` & `lusid-sdk-preview-1.0.9/lusid/models/index_projection_dependency.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/index_projection_dependency_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/index_projection_dependency_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/industry_classifier.py` & `lusid-sdk-preview-1.0.9/lusid/models/industry_classifier.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/inflation_linked_bond.py` & `lusid-sdk-preview-1.0.9/lusid/models/inflation_linked_bond.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/inflation_linked_bond_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/inflation_linked_bond_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/inflation_swap.py` & `lusid-sdk-preview-1.0.9/lusid/models/inflation_swap.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/inflation_swap_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/inflation_swap_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/informational_error_event.py` & `lusid-sdk-preview-1.0.9/lusid/models/informational_error_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/informational_error_event_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/informational_error_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/informational_event.py` & `lusid-sdk-preview-1.0.9/lusid/models/informational_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/informational_event_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/informational_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/inline_valuation_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/inline_valuation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/inline_valuations_reconciliation_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/inline_valuations_reconciliation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/input_transition.py` & `lusid-sdk-preview-1.0.9/lusid/models/input_transition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_capabilities.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_capabilities.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_cash_flow.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_cash_flow.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_definition_format.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_definition_format.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_delete_modes.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_delete_modes.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_event.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_event_holder.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_event_holder.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_event_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_event_type.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_id_type_descriptor.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_id_type_descriptor.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_id_value.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_id_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_leg.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_leg.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_leg_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_leg_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_match.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_match.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_payment_diary.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_payment_diary.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_payment_diary_leg.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_payment_diary_leg.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_payment_diary_row.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_payment_diary_row.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_properties.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_properties.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_search_property.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_search_property.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/instrument_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/instrument_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/interest_rate_swap.py` & `lusid-sdk-preview-1.0.9/lusid/models/interest_rate_swap.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/interest_rate_swap_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/interest_rate_swap_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/interest_rate_swaption.py` & `lusid-sdk-preview-1.0.9/lusid/models/interest_rate_swaption.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/interest_rate_swaption_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/interest_rate_swaption_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/ir_vol_cube_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/ir_vol_cube_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/ir_vol_cube_data_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/ir_vol_cube_data_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/ir_vol_dependency.py` & `lusid-sdk-preview-1.0.9/lusid/models/ir_vol_dependency.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/ir_vol_dependency_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/ir_vol_dependency_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/is_business_day_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/is_business_day_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/je_lines.py` & `lusid-sdk-preview-1.0.9/lusid/models/je_lines.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/je_lines_query_parameters.py` & `lusid-sdk-preview-1.0.9/lusid/models/je_lines_query_parameters.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/label_value_set.py` & `lusid-sdk-preview-1.0.9/lusid/models/label_value_set.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/leg_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/leg_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/legal_entity.py` & `lusid-sdk-preview-1.0.9/lusid/models/legal_entity.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/level_step.py` & `lusid-sdk-preview-1.0.9/lusid/models/level_step.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/life_cycle_event_lineage.py` & `lusid-sdk-preview-1.0.9/lusid/models/life_cycle_event_lineage.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/life_cycle_event_value.py` & `lusid-sdk-preview-1.0.9/lusid/models/life_cycle_event_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/life_cycle_event_value_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/life_cycle_event_value_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/link.py` & `lusid-sdk-preview-1.0.9/lusid/models/link.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/list_aggregation_reconciliation.py` & `lusid-sdk-preview-1.0.9/lusid/models/list_aggregation_reconciliation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/list_aggregation_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/list_aggregation_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/list_complex_market_data_with_meta_data_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/list_complex_market_data_with_meta_data_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/lusid_instrument.py` & `lusid-sdk-preview-1.0.9/lusid/models/lusid_instrument.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/lusid_problem_details.py` & `lusid-sdk-preview-1.0.9/lusid/models/lusid_problem_details.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/lusid_trade_ticket.py` & `lusid-sdk-preview-1.0.9/lusid/models/lusid_trade_ticket.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/lusid_unique_id.py` & `lusid-sdk-preview-1.0.9/lusid/models/lusid_unique_id.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/lusid_validation_problem_details.py` & `lusid-sdk-preview-1.0.9/lusid/models/lusid_validation_problem_details.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/mapped_string.py` & `lusid-sdk-preview-1.0.9/lusid/models/mapped_string.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/mapping.py` & `lusid-sdk-preview-1.0.9/lusid/models/mapping.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/mapping_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/mapping_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/market_context.py` & `lusid-sdk-preview-1.0.9/lusid/models/market_context.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/market_context_suppliers.py` & `lusid-sdk-preview-1.0.9/lusid/models/market_context_suppliers.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/market_data_key_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/market_data_key_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/market_data_overrides.py` & `lusid-sdk-preview-1.0.9/lusid/models/market_data_overrides.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/market_data_specific_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/market_data_specific_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/market_data_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/market_data_type.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/market_observable_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/market_observable_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/market_options.py` & `lusid-sdk-preview-1.0.9/lusid/models/market_options.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/market_quote.py` & `lusid-sdk-preview-1.0.9/lusid/models/market_quote.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/match_criterion.py` & `lusid-sdk-preview-1.0.9/lusid/models/match_criterion.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/metric_value.py` & `lusid-sdk-preview-1.0.9/lusid/models/metric_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/model_options.py` & `lusid-sdk-preview-1.0.9/lusid/models/model_options.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/model_options_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/model_options_type.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/model_property.py` & `lusid-sdk-preview-1.0.9/lusid/models/model_property.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/model_selection.py` & `lusid-sdk-preview-1.0.9/lusid/models/model_selection.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/movement_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/movement_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/next_value_in_sequence_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/next_value_in_sequence_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/numeric_comparison_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/numeric_comparison_type.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/opaque_dependency.py` & `lusid-sdk-preview-1.0.9/lusid/models/opaque_dependency.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/opaque_dependency_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/opaque_dependency_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/opaque_market_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/opaque_market_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/opaque_market_data_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/opaque_market_data_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/opaque_model_options.py` & `lusid-sdk-preview-1.0.9/lusid/models/opaque_model_options.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/opaque_model_options_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/opaque_model_options_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/open_event.py` & `lusid-sdk-preview-1.0.9/lusid/models/open_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/open_event_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/open_event_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/operand_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/operand_type.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/operation.py` & `lusid-sdk-preview-1.0.9/lusid/models/operation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/operation_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/operation_type.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/operator.py` & `lusid-sdk-preview-1.0.9/lusid/models/operator.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order.py` & `lusid-sdk-preview-1.0.9/lusid/models/order.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_by_spec.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_by_spec.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_block.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_block.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_allocation_detail.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_allocation_detail.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_allocation_synopsis.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_allocation_synopsis.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_execution_detail.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_execution_detail.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_execution_synopsis.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_execution_synopsis.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_order_detail.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_order_detail.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_order_synopsis.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_order_synopsis.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_placement_detail.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_placement_detail.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_block_placement_synopsis.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_block_placement_synopsis.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement_allocation_detail.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement_allocation_detail.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement_allocation_synopsis.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement_allocation_synopsis.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement_execution_detail.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement_execution_detail.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement_execution_synopsis.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement_execution_synopsis.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement_order_detail.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement_order_detail.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement_order_synopsis.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement_order_synopsis.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_graph_placement_placement_synopsis.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_graph_placement_placement_synopsis.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_instruction.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_instruction.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_instruction_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_instruction_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_instruction_set_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_instruction_set_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/order_set_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/order_set_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/otc_confirmation.py` & `lusid-sdk-preview-1.0.9/lusid/models/otc_confirmation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/output_transaction.py` & `lusid-sdk-preview-1.0.9/lusid/models/output_transaction.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/output_transition.py` & `lusid-sdk-preview-1.0.9/lusid/models/output_transition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/package.py` & `lusid-sdk-preview-1.0.9/lusid/models/package.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/package_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/package_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/package_set_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/package_set_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_abor.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_abor.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_abor_configuration.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_abor_configuration.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_account.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_account.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_allocation.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_allocation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_block.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_block.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_calendar.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_calendar.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_chart_of_accounts.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_chart_of_accounts.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_corporate_action_source.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_corporate_action_source.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_custodian_account.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_custodian_account.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_custom_entity_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_custom_entity_definition.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_custom_entity_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_custom_entity_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_cut_label_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_cut_label_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_data_type_summary.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_data_type_summary.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_execution.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_execution.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_instrument.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_instrument.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_instrument_event_holder.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_instrument_event_holder.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_legal_entity.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_legal_entity.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_order.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_order.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_order_graph_block.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_order_graph_block.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_order_graph_placement.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_order_graph_placement.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_order_instruction.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_order_instruction.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_package.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_package.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_participation.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_participation.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_person.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_person.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_placement.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_placement.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_portfolio_group_search_result.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_portfolio_group_search_result.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_portfolio_search_result.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_portfolio_search_result.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_property_definition_search_result.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_property_definition_search_result.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_relationship_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_relationship_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/paged_resource_list_of_sequence_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/paged_resource_list_of_sequence_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/participation.py` & `lusid-sdk-preview-1.0.9/lusid/models/participation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/participation_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/participation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/participation_set_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/participation_set_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/performance_return.py` & `lusid-sdk-preview-1.0.9/lusid/models/performance_return.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/performance_returns_metric.py` & `lusid-sdk-preview-1.0.9/lusid/models/performance_returns_metric.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/period_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/period_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/perpetual_entity_state.py` & `lusid-sdk-preview-1.0.9/lusid/models/perpetual_entity_state.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/perpetual_property.py` & `lusid-sdk-preview-1.0.9/lusid/models/perpetual_property.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/person.py` & `lusid-sdk-preview-1.0.9/lusid/models/person.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/placement.py` & `lusid-sdk-preview-1.0.9/lusid/models/placement.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/placement_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/placement_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/placement_set_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/placement_set_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio_cash_flow.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio_cash_flow.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio_cash_ladder.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio_cash_ladder.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio_details.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio_details.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio_entity_id.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio_entity_id.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio_group.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio_group.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio_group_properties.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio_group_properties.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio_group_search_result.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio_group_search_result.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio_holding.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio_holding.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio_properties.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio_properties.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio_reconciliation_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio_reconciliation_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio_result_data_key_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio_result_data_key_rule.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio_result_data_key_rule_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio_result_data_key_rule_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio_search_result.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio_search_result.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio_trade_ticket.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio_trade_ticket.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolio_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolio_type.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/portfolios_reconciliation_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/portfolios_reconciliation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/premium.py` & `lusid-sdk-preview-1.0.9/lusid/models/premium.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/pricing_context.py` & `lusid-sdk-preview-1.0.9/lusid/models/pricing_context.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/pricing_model.py` & `lusid-sdk-preview-1.0.9/lusid/models/pricing_model.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/pricing_options.py` & `lusid-sdk-preview-1.0.9/lusid/models/pricing_options.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/processed_command.py` & `lusid-sdk-preview-1.0.9/lusid/models/processed_command.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/property_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/property_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/property_definition_search_result.py` & `lusid-sdk-preview-1.0.9/lusid/models/property_definition_search_result.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/property_definition_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/property_definition_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/property_domain.py` & `lusid-sdk-preview-1.0.9/lusid/models/property_domain.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/property_filter.py` & `lusid-sdk-preview-1.0.9/lusid/models/property_filter.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/property_interval.py` & `lusid-sdk-preview-1.0.9/lusid/models/property_interval.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/property_life_time.py` & `lusid-sdk-preview-1.0.9/lusid/models/property_life_time.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/property_schema.py` & `lusid-sdk-preview-1.0.9/lusid/models/property_schema.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/property_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/property_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/property_value.py` & `lusid-sdk-preview-1.0.9/lusid/models/property_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/property_value_equals.py` & `lusid-sdk-preview-1.0.9/lusid/models/property_value_equals.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/property_value_equals_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/property_value_equals_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/property_value_in.py` & `lusid-sdk-preview-1.0.9/lusid/models/property_value_in.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/property_value_in_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/property_value_in_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/query_bucketed_cash_flows_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/query_bucketed_cash_flows_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/query_cash_flows_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/query_cash_flows_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/query_instrument_events_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/query_instrument_events_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/query_trade_tickets_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/query_trade_tickets_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/quote.py` & `lusid-sdk-preview-1.0.9/lusid/models/quote.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/quote_access_metadata_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/quote_access_metadata_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/quote_access_metadata_rule_id.py` & `lusid-sdk-preview-1.0.9/lusid/models/quote_access_metadata_rule_id.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/quote_dependency.py` & `lusid-sdk-preview-1.0.9/lusid/models/quote_dependency.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/quote_dependency_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/quote_dependency_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/quote_id.py` & `lusid-sdk-preview-1.0.9/lusid/models/quote_id.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/quote_instrument_id_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/quote_instrument_id_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/quote_series_id.py` & `lusid-sdk-preview-1.0.9/lusid/models/quote_series_id.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/quote_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/quote_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/raw_vendor_event.py` & `lusid-sdk-preview-1.0.9/lusid/models/raw_vendor_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/raw_vendor_event_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/raw_vendor_event_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/realised_gain_loss.py` & `lusid-sdk-preview-1.0.9/lusid/models/realised_gain_loss.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reconcile_date_time_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/reconcile_date_time_rule.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reconcile_date_time_rule_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/reconcile_date_time_rule_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reconcile_numeric_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/reconcile_numeric_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reconcile_numeric_rule_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/reconcile_numeric_rule_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reconcile_string_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/reconcile_string_rule.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reconcile_string_rule_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/reconcile_string_rule_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reconciled_transaction.py` & `lusid-sdk-preview-1.0.9/lusid/models/reconciled_transaction.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reconciliation_break.py` & `lusid-sdk-preview-1.0.9/lusid/models/reconciliation_break.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reconciliation_left_right_address_key_pair.py` & `lusid-sdk-preview-1.0.9/lusid/models/reconciliation_left_right_address_key_pair.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reconciliation_line.py` & `lusid-sdk-preview-1.0.9/lusid/models/reconciliation_line.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reconciliation_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/reconciliation_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reconciliation_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/reconciliation_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reconciliation_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/reconciliation_rule.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reconciliation_rule_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/reconciliation_rule_type.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reference_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/reference_data.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reference_instrument.py` & `lusid-sdk-preview-1.0.9/lusid/models/reference_instrument.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reference_instrument_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/reference_instrument_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reference_portfolio_constituent.py` & `lusid-sdk-preview-1.0.9/lusid/models/reference_portfolio_constituent.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reference_portfolio_constituent_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/reference_portfolio_constituent_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reference_portfolio_weight_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/reference_portfolio_weight_type.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/related_entity.py` & `lusid-sdk-preview-1.0.9/lusid/models/related_entity.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/relation.py` & `lusid-sdk-preview-1.0.9/lusid/models/relation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/relation_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/relation_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/relationship.py` & `lusid-sdk-preview-1.0.9/lusid/models/relationship.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/relationship_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/relationship_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/repo.py` & `lusid-sdk-preview-1.0.9/lusid/models/repo.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/repo_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/repo_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reset_event.py` & `lusid-sdk-preview-1.0.9/lusid/models/reset_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/reset_event_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/reset_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_id.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_id.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_access_controlled_resource.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_access_controlled_resource.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_access_metadata_value_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_access_metadata_value_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_aggregated_return.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_aggregated_return.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_aggregation_query.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_aggregation_query.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_allocation.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_allocation.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_block.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_block.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_calendar_date.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_calendar_date.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_change.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_change.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_change_history.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_change_history.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_compliance_breached_order_info.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_compliance_breached_order_info.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_compliance_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_compliance_rule.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_compliance_rule_result.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_compliance_rule_result.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_compliance_run_info.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_compliance_run_info.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_constituents_adjustment_header.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_constituents_adjustment_header.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_corporate_action.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_corporate_action.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_data_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_data_type.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_execution.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_execution.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_fee_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_fee_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_get_cds_flow_conventions_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_get_cds_flow_conventions_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_get_counterparty_agreement_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_get_counterparty_agreement_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_get_credit_support_annex_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_get_credit_support_annex_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_get_flow_conventions_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_get_flow_conventions_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_get_index_convention_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_get_index_convention_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_get_recipe_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_get_recipe_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_holdings_adjustment_header.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_holdings_adjustment_header.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_i_unit_definition_dto.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_i_unit_definition_dto.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_instrument_cash_flow.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_instrument_cash_flow.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_instrument_event_holder.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_instrument_event_holder.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_instrument_id_type_descriptor.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_instrument_id_type_descriptor.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_legal_entity.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_legal_entity.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_list_complex_market_data_with_meta_data_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_list_complex_market_data_with_meta_data_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_mapping.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_mapping.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_order.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_order.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_order_instruction.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_order_instruction.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_package.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_package.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_participation.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_participation.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_performance_return.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_performance_return.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_person.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_person.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_placement.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_placement.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_portfolio.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_portfolio.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_portfolio_cash_flow.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_portfolio_cash_flow.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_portfolio_cash_ladder.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_portfolio_cash_ladder.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_portfolio_group.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_portfolio_group.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_portfolio_trade_ticket.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_portfolio_trade_ticket.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_processed_command.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_processed_command.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_property.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_property.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_property_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_property_definition.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_property_interval.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_property_interval.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_quote.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_quote.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_quote_access_metadata_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_quote_access_metadata_rule.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_reconciliation_break.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_reconciliation_break.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_relation.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_relation.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_relationship.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_relationship.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_scope_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_scope_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_string.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_string.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_tax_rule_set.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_tax_rule_set.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_transaction.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_transaction.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/resource_list_of_value_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/resource_list_of_value_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/response_meta_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/response_meta_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_data_key_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_data_key_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_data_key_rule_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_data_key_rule_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_data_schema.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_data_schema.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_key_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_key_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_key_rule_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_key_rule_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value0_d.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value0_d.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value0_d_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value0_d_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value_bool.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value_bool.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value_bool_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value_bool_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value_currency.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value_currency.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value_currency_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value_currency_all_of.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value_date_time_offset.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value_date_time_offset.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value_date_time_offset_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value_date_time_offset_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value_decimal.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value_decimal.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value_decimal_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value_decimal_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value_dictionary.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value_dictionary.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value_dictionary_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value_dictionary_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value_int.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value_int.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value_int_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value_int_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value_string.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value_string.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value_string_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value_string_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/result_value_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/result_value_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/scaling_methodology.py` & `lusid-sdk-preview-1.0.9/lusid/models/scaling_methodology.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/schedule.py` & `lusid-sdk-preview-1.0.9/lusid/models/schedule.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/schedule_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/schedule_type.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/schema.py` & `lusid-sdk-preview-1.0.9/lusid/models/schema.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/scope_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/scope_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/sequence_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/sequence_definition.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/set_legal_entity_identifiers_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/set_legal_entity_identifiers_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/set_legal_entity_properties_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/set_legal_entity_properties_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/set_person_identifiers_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/set_person_identifiers_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/set_person_properties_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/set_person_properties_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/set_transaction_configuration_alias.py` & `lusid-sdk-preview-1.0.9/lusid/models/set_transaction_configuration_alias.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/set_transaction_configuration_source_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/set_transaction_configuration_source_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/side_configuration_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/side_configuration_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/side_configuration_data_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/side_configuration_data_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/side_definition.py` & `lusid-sdk-preview-1.0.9/lusid/models/side_definition.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/side_definition_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/side_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/simple_instrument.py` & `lusid-sdk-preview-1.0.9/lusid/models/simple_instrument.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/simple_instrument_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/simple_instrument_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/sort_order.py` & `lusid-sdk-preview-1.0.9/lusid/models/sort_order.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/step_schedule.py` & `lusid-sdk-preview-1.0.9/lusid/models/step_schedule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/step_schedule_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/step_schedule_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/stock_split_event.py` & `lusid-sdk-preview-1.0.9/lusid/models/stock_split_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/stock_split_event_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/stock_split_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/stream.py` & `lusid-sdk-preview-1.0.9/lusid/models/stream.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/string_comparison_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/string_comparison_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/structured_result_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/structured_result_data.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/structured_result_data_id.py` & `lusid-sdk-preview-1.0.9/lusid/models/structured_result_data_id.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/sub_holding_key_value_equals.py` & `lusid-sdk-preview-1.0.9/lusid/models/sub_holding_key_value_equals.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/sub_holding_key_value_equals_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/sub_holding_key_value_equals_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/supported_analytics_internal_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/supported_analytics_internal_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/target_tax_lot.py` & `lusid-sdk-preview-1.0.9/lusid/models/target_tax_lot.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/target_tax_lot_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/target_tax_lot_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/tax_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/tax_rule.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/tax_rule_set.py` & `lusid-sdk-preview-1.0.9/lusid/models/tax_rule_set.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/term_deposit.py` & `lusid-sdk-preview-1.0.9/lusid/models/term_deposit.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/term_deposit_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/term_deposit_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/touch.py` & `lusid-sdk-preview-1.0.9/lusid/models/touch.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/trade_ticket.py` & `lusid-sdk-preview-1.0.9/lusid/models/trade_ticket.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/trade_ticket_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/trade_ticket_type.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_configuration_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_configuration_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_configuration_data_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_configuration_data_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_configuration_movement_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_configuration_movement_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_configuration_movement_data_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_configuration_movement_data_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_configuration_type_alias.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_configuration_type_alias.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_price.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_price.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_price_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_price_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_property_mapping.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_property_mapping.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_property_mapping_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_property_mapping_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_query_mode.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_query_mode.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_query_parameters.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_query_parameters.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_reconciliation_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_reconciliation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_roles.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_roles.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_set_configuration_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_set_configuration_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_set_configuration_data_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_set_configuration_data_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_status.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_status.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_type_alias.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_type_alias.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_type_movement.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_type_movement.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_type_property_mapping.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_type_property_mapping.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transaction_type_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/transaction_type_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transactions_reconciliations_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/transactions_reconciliations_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transition_event.py` & `lusid-sdk-preview-1.0.9/lusid/models/transition_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/transition_event_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/transition_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/translate_instrument_definitions_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/translate_instrument_definitions_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/translate_instrument_definitions_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/translate_instrument_definitions_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/translate_trade_ticket_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/translate_trade_ticket_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/translate_trade_tickets_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/translate_trade_tickets_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/trigger_event.py` & `lusid-sdk-preview-1.0.9/lusid/models/trigger_event.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/trigger_event_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/trigger_event_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/typed_resource_id.py` & `lusid-sdk-preview-1.0.9/lusid/models/typed_resource_id.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/unit_schema.py` & `lusid-sdk-preview-1.0.9/lusid/models/unit_schema.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/unmatched_holding_method.py` & `lusid-sdk-preview-1.0.9/lusid/models/unmatched_holding_method.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/update_calendar_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/update_calendar_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/update_custom_entity_definition_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/update_custom_entity_definition_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/update_cut_label_definition_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/update_cut_label_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/update_data_type_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/update_data_type_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/update_instrument_identifier_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/update_instrument_identifier_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/update_portfolio_group_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/update_portfolio_group_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/update_portfolio_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/update_portfolio_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/update_property_definition_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/update_property_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/update_relationship_definition_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/update_relationship_definition_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/update_tax_rule_set_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/update_tax_rule_set_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/update_unit_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/update_unit_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_cds_flow_conventions_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_cds_flow_conventions_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_complex_market_data_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_complex_market_data_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_corporate_action_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_corporate_action_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_corporate_actions_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_corporate_actions_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_counterparty_agreement_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_counterparty_agreement_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_credit_support_annex_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_credit_support_annex_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_custom_entities_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_custom_entities_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_custom_entity_access_metadata_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_custom_entity_access_metadata_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_flow_conventions_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_flow_conventions_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_index_convention_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_index_convention_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_instrument_event_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_instrument_event_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_instrument_events_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_instrument_events_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_instrument_properties_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_instrument_properties_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_instrument_property_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_instrument_property_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_instruments_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_instruments_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_legal_entity_access_metadata_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_legal_entity_access_metadata_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_legal_entity_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_legal_entity_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_person_access_metadata_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_person_access_metadata_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_person_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_person_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_portfolio_access_metadata_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_portfolio_access_metadata_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_portfolio_group_access_metadata_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_portfolio_group_access_metadata_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_portfolio_transactions_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_portfolio_transactions_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_quote_access_metadata_rule_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_quote_access_metadata_rule_request.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_quote_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_quote_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_quotes_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_quotes_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_recipe_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_recipe_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_reference_portfolio_constituents_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_reference_portfolio_constituents_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_reference_portfolio_constituents_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_reference_portfolio_constituents_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_result_values_data_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_result_values_data_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_returns_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_returns_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_single_structured_data_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_single_structured_data_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_structured_data_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_structured_data_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_structured_result_data_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_structured_result_data_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/upsert_transaction_properties_response.py` & `lusid-sdk-preview-1.0.9/lusid/models/upsert_transaction_properties_response.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/user.py` & `lusid-sdk-preview-1.0.9/lusid/models/user.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/valuation_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/valuation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/valuation_schedule.py` & `lusid-sdk-preview-1.0.9/lusid/models/valuation_schedule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/valuations_reconciliation_request.py` & `lusid-sdk-preview-1.0.9/lusid/models/valuations_reconciliation_request.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/value_type.py` & `lusid-sdk-preview-1.0.9/lusid/models/value_type.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/vendor_dependency.py` & `lusid-sdk-preview-1.0.9/lusid/models/vendor_dependency.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/vendor_dependency_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/vendor_dependency_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/vendor_library.py` & `lusid-sdk-preview-1.0.9/lusid/models/vendor_library.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/vendor_model_rule.py` & `lusid-sdk-preview-1.0.9/lusid/models/vendor_model_rule.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/version.py` & `lusid-sdk-preview-1.0.9/lusid/models/version.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/version_summary_dto.py` & `lusid-sdk-preview-1.0.9/lusid/models/version_summary_dto.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/versioned_resource_list_of_a2_b_data_record.py` & `lusid-sdk-preview-1.0.9/lusid/models/versioned_resource_list_of_a2_b_data_record.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/versioned_resource_list_of_a2_b_movement_record.py` & `lusid-sdk-preview-1.0.9/lusid/models/versioned_resource_list_of_a2_b_movement_record.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/versioned_resource_list_of_je_lines.py` & `lusid-sdk-preview-1.0.9/lusid/models/versioned_resource_list_of_je_lines.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/versioned_resource_list_of_output_transaction.py` & `lusid-sdk-preview-1.0.9/lusid/models/versioned_resource_list_of_output_transaction.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/versioned_resource_list_of_portfolio_holding.py` & `lusid-sdk-preview-1.0.9/lusid/models/versioned_resource_list_of_portfolio_holding.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/versioned_resource_list_of_transaction.py` & `lusid-sdk-preview-1.0.9/lusid/models/versioned_resource_list_of_transaction.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/versioned_resource_list_with_warnings_of_portfolio_holding.py` & `lusid-sdk-preview-1.0.9/lusid/models/versioned_resource_list_with_warnings_of_portfolio_holding.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/virtual_document.py` & `lusid-sdk-preview-1.0.9/lusid/models/virtual_document.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/virtual_document_row.py` & `lusid-sdk-preview-1.0.9/lusid/models/virtual_document_row.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/warning.py` & `lusid-sdk-preview-1.0.9/lusid/models/warning.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/weekend_mask.py` & `lusid-sdk-preview-1.0.9/lusid/models/weekend_mask.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/weighted_instrument.py` & `lusid-sdk-preview-1.0.9/lusid/models/weighted_instrument.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/weighted_instruments.py` & `lusid-sdk-preview-1.0.9/lusid/models/weighted_instruments.py`

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

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/yield_curve_data.py` & `lusid-sdk-preview-1.0.9/lusid/models/yield_curve_data.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/models/yield_curve_data_all_of.py` & `lusid-sdk-preview-1.0.9/lusid/models/yield_curve_data_all_of.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     LUSID API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.0.8
+    The version of the OpenAPI document: 1.0.9
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `lusid-sdk-preview-1.0.8/lusid/rest.py` & `lusid-sdk-preview-1.0.9/lusid/rest.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
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

### Comparing `lusid-sdk-preview-1.0.8/lusid/tcp/tcp_keep_alive_probes.py` & `lusid-sdk-preview-1.0.9/lusid/tcp/tcp_keep_alive_probes.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-preview-1.0.8/lusid/utilities/api_client_builder.py` & `lusid-sdk-preview-1.0.9/lusid/utilities/api_client_builder.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-preview-1.0.8/lusid/utilities/api_client_factory.py` & `lusid-sdk-preview-1.0.9/lusid/utilities/api_client_factory.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-preview-1.0.8/lusid/utilities/api_configuration.py` & `lusid-sdk-preview-1.0.9/lusid/utilities/api_configuration.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-preview-1.0.8/lusid/utilities/api_configuration_loader.py` & `lusid-sdk-preview-1.0.9/lusid/utilities/api_configuration_loader.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-preview-1.0.8/lusid/utilities/config_keys.json` & `lusid-sdk-preview-1.0.9/lusid/utilities/config_keys.json`

 * *Files identical despite different names*

### Comparing `lusid-sdk-preview-1.0.8/lusid/utilities/lusid_retry.py` & `lusid-sdk-preview-1.0.9/lusid/utilities/lusid_retry.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-preview-1.0.8/lusid/utilities/proxy_config.py` & `lusid-sdk-preview-1.0.9/lusid/utilities/proxy_config.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-preview-1.0.8/lusid/utilities/refreshing_token.py` & `lusid-sdk-preview-1.0.9/lusid/utilities/refreshing_token.py`

 * *Files identical despite different names*

### Comparing `lusid-sdk-preview-1.0.8/lusid_sdk_preview.egg-info/SOURCES.txt` & `lusid-sdk-preview-1.0.9/lusid_sdk_preview.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `lusid-sdk-preview-1.0.8/setup.py` & `lusid-sdk-preview-1.0.9/setup.py`

 * *Files identical despite different names*

