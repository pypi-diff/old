# Comparing `tmp/braintree-4.8.0.tar.gz` & `tmp/braintree-4.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/braintree-4.8.0.tar", last modified: Mon Apr 12 20:45:07 2021, max compression
+gzip compressed data, was "dist/braintree-4.9.0.tar", last modified: Wed May  5 19:57:06 2021, max compression
```

## Comparing `braintree-4.8.0.tar` & `braintree-4.9.0.tar`

### file list

```diff
@@ -1,183 +1,184 @@
-drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-04-12 20:45:07.000000 braintree-4.8.0/
--rw-rw-r--   0 admin     (1000) admin     (1000)       24 2021-04-06 19:16:04.000000 braintree-4.8.0/MANIFEST.in
--rw-rw-r--   0 admin     (1000) admin     (1000)      832 2021-04-12 20:45:07.000000 braintree-4.8.0/PKG-INFO
--rw-rw-r--   0 admin     (1000) admin     (1000)     4014 2021-04-06 19:16:04.000000 braintree-4.8.0/README.md
-drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-04-12 20:45:07.000000 braintree-4.8.0/braintree/
--rw-rw-r--   0 admin     (1000) admin     (1000)     4443 2021-04-12 20:35:56.000000 braintree-4.8.0/braintree/__init__.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      585 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/account_updater_daily_report.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      243 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/ach_mandate.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      211 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/add_on.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      514 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/add_on_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     4406 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/address.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     2602 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/address_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      663 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/amex_express_checkout_card.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      836 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/android_pay_card.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1012 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/apple_pay_card.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1349 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/apple_pay_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      105 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/apple_pay_options.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1102 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/attribute_getter.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      320 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/authorization_adjustment.py
--rw-rw-r--   0 admin     (1000) admin     (1000)       97 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/bin_data.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     3717 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/braintree_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      782 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/client_token.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1149 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/client_token_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     5117 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/configuration.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      275 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/connected_merchant_paypal_status_changed.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      274 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/connected_merchant_status_transitioned.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     2026 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/credentials_parser.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     9801 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/credit_card.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     5172 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/credit_card_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     3475 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/credit_card_verification.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     3076 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/credit_card_verification_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1347 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/credit_card_verification_search.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     9843 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/customer.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     4321 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/customer_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     2146 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/customer_search.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      167 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/descriptor.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1065 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/disbursement.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      620 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/disbursement_detail.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      218 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/discount.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      537 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/discount_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     7476 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/dispute.py
-drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-04-12 20:45:07.000000 braintree-4.8.0/braintree/dispute_details/
--rw-rw-r--   0 admin     (1000) admin     (1000)      137 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/dispute_details/__init__.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      238 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/dispute_details/evidence.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      188 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/dispute_details/status_history.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     7027 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/dispute_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1219 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/dispute_search.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1461 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/document_upload.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1469 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/document_upload_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     3216 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/environment.py
--rw-rw-r--   0 admin     (1000) admin     (1000)    34032 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/error_codes.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     2482 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/error_result.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      458 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/errors.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      859 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/europe_bank_account.py
-drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-04-12 20:45:07.000000 braintree-4.8.0/braintree/exceptions/
--rw-rw-r--   0 admin     (1000) admin     (1000)     1069 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/__init__.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      404 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/authentication_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      325 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/authorization_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)       42 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/braintree_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      119 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/configuration_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      184 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/gateway_timeout_error.py
-drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-04-12 20:45:07.000000 braintree-4.8.0/braintree/exceptions/http/
--rw-rw-r--   0 admin     (1000) admin     (1000)      218 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/http/__init__.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      116 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/http/connection_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      121 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/http/invalid_response_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      214 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/http/timeout_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      119 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/invalid_challenge_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      119 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/invalid_signature_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      322 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/not_found_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      182 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/request_timeout_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      322 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/server_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      181 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/service_unavailable_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      250 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/test_operation_performed_in_production_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      196 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/too_many_requests_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      166 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/unexpected_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      295 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/exceptions/upgrade_required_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      108 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/facilitated_details.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      108 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/facilitator_details.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      268 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/granted_payment_instrument_update.py
--rw-rw-r--   0 admin     (1000) admin     (1000)       83 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/iban_bank_account.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      103 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/ids_search.py
--rw-rw-r--   0 admin     (1000) admin     (1000)       97 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/local_payment.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      348 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/local_payment_completed.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      259 2021-04-12 20:35:56.000000 braintree-4.8.0/braintree/local_payment_reversed.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      921 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/masterpass_card.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      381 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/merchant.py
-drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-04-12 20:45:07.000000 braintree-4.8.0/braintree/merchant_account/
--rw-rw-r--   0 admin     (1000) admin     (1000)      290 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/merchant_account/__init__.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      391 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/merchant_account/address_details.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      540 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/merchant_account/business_details.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      427 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/merchant_account/funding_details.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      608 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/merchant_account/individual_details.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1759 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/merchant_account/merchant_account.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     5691 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/merchant_account_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1195 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/merchant_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      240 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/modification.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      236 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/oauth_access_revocation.py
--rw-rw-r--   0 admin     (1000) admin     (1000)       84 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/oauth_credentials.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     2679 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/oauth_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      882 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/paginated_collection.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      293 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/paginated_result.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1018 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/partner_merchant.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      640 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/payment_instrument_type.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     4313 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/payment_method.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     6945 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/payment_method_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1326 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/payment_method_nonce.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     2084 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/payment_method_nonce_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     2244 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/payment_method_parser.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1061 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/paypal_account.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1814 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/paypal_account_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      185 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/paypal_here.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      730 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/plan.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      674 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/plan_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      213 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/processor_response_types.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     2516 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/resource.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1961 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/resource_collection.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      400 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/revoked_payment_method_metadata.py
--rw-rw-r--   0 admin     (1000) admin     (1000)       98 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/risk_data.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      780 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/samsung_pay_card.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     4132 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/search.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      623 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/settlement_batch_summary.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1074 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/settlement_batch_summary_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      521 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/signature_service.py
-drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-04-12 20:45:07.000000 braintree-4.8.0/braintree/ssl/
--rw-rw-r--   0 admin     (1000) admin     (1000)    14649 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/ssl/api_braintreegateway_com.ca.crt
--rw-rw-r--   0 admin     (1000) admin     (1000)      240 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/status_event.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     8991 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/subscription.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      109 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/subscription_details.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     4358 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/subscription_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      936 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/subscription_search.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      295 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/subscription_status_event.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      631 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/successful_result.py
-drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-04-12 20:45:07.000000 braintree-4.8.0/braintree/test/
--rw-rw-r--   0 admin     (1000) admin     (1000)        0 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/test/__init__.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1468 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/test/authentication_ids.py
--rw-rw-r--   0 admin     (1000) admin     (1000)       97 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/test/credit_card_defaults.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1337 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/test/credit_card_numbers.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      253 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/test/merchant_account.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     5118 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/test/nonces.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      312 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/test/venmo_sdk.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     2748 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/testing_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      106 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/three_d_secure_info.py
--rw-rw-r--   0 admin     (1000) admin     (1000)    32672 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/transaction.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      227 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/transaction_amounts.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      316 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/transaction_details.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     9674 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/transaction_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1241 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/transaction_line_item.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1168 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/transaction_line_item_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     5683 2021-04-12 20:35:56.000000 braintree-4.8.0/braintree/transaction_search.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      206 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/unknown_payment_method.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1519 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/us_bank_account.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      858 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/us_bank_account_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     2766 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/us_bank_account_verification.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     3502 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/us_bank_account_verification_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1303 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/us_bank_account_verification_search.py
-drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-04-12 20:45:07.000000 braintree-4.8.0/braintree/util/
--rw-rw-r--   0 admin     (1000) admin     (1000)      313 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/util/__init__.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      276 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/util/constants.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1224 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/util/crypto.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1063 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/util/datetime_parser.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     2454 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/util/generator.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     2860 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/util/graphql_client.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     7568 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/util/http.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     3284 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/util/parser.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      283 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/util/xml_util.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      457 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/validation_error.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     3045 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/validation_error_collection.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      429 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/venmo_account.py
--rw-rw-r--   0 admin     (1000) admin     (1000)       18 2021-04-12 20:37:45.000000 braintree-4.8.0/braintree/version.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     1233 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/visa_checkout_card.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     6615 2021-04-12 20:35:56.000000 braintree-4.8.0/braintree/webhook_notification.py
--rw-rw-r--   0 admin     (1000) admin     (1000)     2419 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/webhook_notification_gateway.py
--rw-rw-r--   0 admin     (1000) admin     (1000)      285 2021-04-06 19:16:04.000000 braintree-4.8.0/braintree/webhook_testing.py
--rw-rw-r--   0 admin     (1000) admin     (1000)    35827 2021-04-12 20:35:56.000000 braintree-4.8.0/braintree/webhook_testing_gateway.py
-drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-04-12 20:45:07.000000 braintree-4.8.0/braintree.egg-info/
--rw-rw-r--   0 admin     (1000) admin     (1000)      832 2021-04-12 20:45:07.000000 braintree-4.8.0/braintree.egg-info/PKG-INFO
--rw-rw-r--   0 admin     (1000) admin     (1000)     5757 2021-04-12 20:45:07.000000 braintree-4.8.0/braintree.egg-info/SOURCES.txt
--rw-rw-r--   0 admin     (1000) admin     (1000)        1 2021-04-12 20:45:07.000000 braintree-4.8.0/braintree.egg-info/dependency_links.txt
--rw-rw-r--   0 admin     (1000) admin     (1000)        1 2021-04-12 20:37:56.000000 braintree-4.8.0/braintree.egg-info/not-zip-safe
--rw-rw-r--   0 admin     (1000) admin     (1000)       22 2021-04-12 20:45:07.000000 braintree-4.8.0/braintree.egg-info/requires.txt
--rw-rw-r--   0 admin     (1000) admin     (1000)       10 2021-04-12 20:45:07.000000 braintree-4.8.0/braintree.egg-info/top_level.txt
--rw-rw-r--   0 admin     (1000) admin     (1000)       67 2021-04-12 20:45:07.000000 braintree-4.8.0/setup.cfg
--rw-rw-r--   0 admin     (1000) admin     (1000)     1254 2021-04-12 20:37:45.000000 braintree-4.8.0/setup.py
+drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-05-05 19:57:06.000000 braintree-4.9.0/
+-rw-rw-r--   0 admin     (1000) admin     (1000)       24 2021-05-05 19:48:42.000000 braintree-4.9.0/MANIFEST.in
+-rw-rw-r--   0 admin     (1000) admin     (1000)      832 2021-05-05 19:57:06.000000 braintree-4.9.0/PKG-INFO
+-rw-rw-r--   0 admin     (1000) admin     (1000)     4014 2021-05-05 19:48:42.000000 braintree-4.9.0/README.md
+drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-05-05 19:57:06.000000 braintree-4.9.0/braintree/
+-rw-rw-r--   0 admin     (1000) admin     (1000)     4443 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/__init__.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      585 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/account_updater_daily_report.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      243 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/ach_mandate.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      211 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/add_on.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      514 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/add_on_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     4406 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/address.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     2602 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/address_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      663 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/amex_express_checkout_card.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      836 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/android_pay_card.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1012 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/apple_pay_card.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1349 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/apple_pay_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      105 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/apple_pay_options.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1102 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/attribute_getter.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      320 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/authorization_adjustment.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)       97 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/bin_data.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     3717 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/braintree_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      782 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/client_token.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1149 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/client_token_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     5117 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/configuration.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      275 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/connected_merchant_paypal_status_changed.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      274 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/connected_merchant_status_transitioned.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     2026 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/credentials_parser.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     9801 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/credit_card.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     5172 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/credit_card_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     3475 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/credit_card_verification.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     3076 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/credit_card_verification_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1347 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/credit_card_verification_search.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     9973 2021-05-05 19:55:18.000000 braintree-4.9.0/braintree/customer.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     4321 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/customer_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     2146 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/customer_search.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      167 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/descriptor.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1065 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/disbursement.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      620 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/disbursement_detail.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      218 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/discount.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      537 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/discount_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     7714 2021-05-05 19:55:18.000000 braintree-4.9.0/braintree/dispute.py
+drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-05-05 19:57:06.000000 braintree-4.9.0/braintree/dispute_details/
+-rw-rw-r--   0 admin     (1000) admin     (1000)      211 2021-05-05 19:55:18.000000 braintree-4.9.0/braintree/dispute_details/__init__.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      238 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/dispute_details/evidence.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      188 2021-05-05 19:55:18.000000 braintree-4.9.0/braintree/dispute_details/paypal_message.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      188 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/dispute_details/status_history.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     7027 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/dispute_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1219 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/dispute_search.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1461 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/document_upload.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1469 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/document_upload_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     3216 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/environment.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)    34032 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/error_codes.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     2482 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/error_result.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      458 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/errors.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      859 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/europe_bank_account.py
+drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-05-05 19:57:06.000000 braintree-4.9.0/braintree/exceptions/
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1069 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/__init__.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      404 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/authentication_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      325 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/authorization_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)       42 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/braintree_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      119 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/configuration_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      184 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/gateway_timeout_error.py
+drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-05-05 19:57:06.000000 braintree-4.9.0/braintree/exceptions/http/
+-rw-rw-r--   0 admin     (1000) admin     (1000)      218 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/http/__init__.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      116 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/http/connection_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      121 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/http/invalid_response_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      214 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/http/timeout_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      119 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/invalid_challenge_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      119 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/invalid_signature_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      322 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/not_found_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      182 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/request_timeout_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      322 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/server_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      181 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/service_unavailable_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      250 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/test_operation_performed_in_production_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      196 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/too_many_requests_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      166 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/unexpected_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      295 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/exceptions/upgrade_required_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      108 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/facilitated_details.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      108 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/facilitator_details.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      268 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/granted_payment_instrument_update.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)       83 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/iban_bank_account.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      103 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/ids_search.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)       97 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/local_payment.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      348 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/local_payment_completed.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      259 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/local_payment_reversed.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      921 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/masterpass_card.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      381 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/merchant.py
+drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-05-05 19:57:06.000000 braintree-4.9.0/braintree/merchant_account/
+-rw-rw-r--   0 admin     (1000) admin     (1000)      290 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/merchant_account/__init__.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      391 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/merchant_account/address_details.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      540 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/merchant_account/business_details.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      427 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/merchant_account/funding_details.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      608 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/merchant_account/individual_details.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1759 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/merchant_account/merchant_account.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     5691 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/merchant_account_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1195 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/merchant_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      240 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/modification.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      236 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/oauth_access_revocation.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)       84 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/oauth_credentials.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     2679 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/oauth_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      882 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/paginated_collection.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      293 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/paginated_result.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1018 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/partner_merchant.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      640 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/payment_instrument_type.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     4313 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/payment_method.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     6945 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/payment_method_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1326 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/payment_method_nonce.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     2084 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/payment_method_nonce_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     2244 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/payment_method_parser.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1061 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/paypal_account.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1814 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/paypal_account_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      185 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/paypal_here.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      730 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/plan.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      674 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/plan_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      213 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/processor_response_types.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     2516 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/resource.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1961 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/resource_collection.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      400 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/revoked_payment_method_metadata.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)       98 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/risk_data.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      780 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/samsung_pay_card.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     4132 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/search.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      623 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/settlement_batch_summary.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1074 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/settlement_batch_summary_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      521 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/signature_service.py
+drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-05-05 19:57:06.000000 braintree-4.9.0/braintree/ssl/
+-rw-rw-r--   0 admin     (1000) admin     (1000)    14649 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/ssl/api_braintreegateway_com.ca.crt
+-rw-rw-r--   0 admin     (1000) admin     (1000)      240 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/status_event.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     8991 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/subscription.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      109 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/subscription_details.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     4358 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/subscription_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      936 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/subscription_search.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      295 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/subscription_status_event.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      631 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/successful_result.py
+drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-05-05 19:57:06.000000 braintree-4.9.0/braintree/test/
+-rw-rw-r--   0 admin     (1000) admin     (1000)        0 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/test/__init__.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1468 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/test/authentication_ids.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)       97 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/test/credit_card_defaults.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1337 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/test/credit_card_numbers.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      253 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/test/merchant_account.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     5118 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/test/nonces.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      312 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/test/venmo_sdk.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     2748 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/testing_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      106 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/three_d_secure_info.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)    32672 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/transaction.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      227 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/transaction_amounts.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      316 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/transaction_details.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     9674 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/transaction_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1241 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/transaction_line_item.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1168 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/transaction_line_item_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     5683 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/transaction_search.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      206 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/unknown_payment_method.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1519 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/us_bank_account.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      858 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/us_bank_account_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     2766 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/us_bank_account_verification.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     3502 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/us_bank_account_verification_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1303 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/us_bank_account_verification_search.py
+drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-05-05 19:57:06.000000 braintree-4.9.0/braintree/util/
+-rw-rw-r--   0 admin     (1000) admin     (1000)      313 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/util/__init__.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      276 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/util/constants.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1224 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/util/crypto.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1063 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/util/datetime_parser.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     2454 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/util/generator.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     2860 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/util/graphql_client.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     7568 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/util/http.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     3284 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/util/parser.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      283 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/util/xml_util.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      457 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/validation_error.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     3045 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/validation_error_collection.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      429 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/venmo_account.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)       18 2021-05-05 19:56:48.000000 braintree-4.9.0/braintree/version.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1233 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/visa_checkout_card.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     6615 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/webhook_notification.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)     2419 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/webhook_notification_gateway.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)      285 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/webhook_testing.py
+-rw-rw-r--   0 admin     (1000) admin     (1000)    35827 2021-05-05 19:48:42.000000 braintree-4.9.0/braintree/webhook_testing_gateway.py
+drwxrwxr-x   0 admin     (1000) admin     (1000)        0 2021-05-05 19:57:06.000000 braintree-4.9.0/braintree.egg-info/
+-rw-rw-r--   0 admin     (1000) admin     (1000)      832 2021-05-05 19:57:06.000000 braintree-4.9.0/braintree.egg-info/PKG-INFO
+-rw-rw-r--   0 admin     (1000) admin     (1000)     5801 2021-05-05 19:57:06.000000 braintree-4.9.0/braintree.egg-info/SOURCES.txt
+-rw-rw-r--   0 admin     (1000) admin     (1000)        1 2021-05-05 19:57:06.000000 braintree-4.9.0/braintree.egg-info/dependency_links.txt
+-rw-rw-r--   0 admin     (1000) admin     (1000)        1 2021-05-05 19:57:06.000000 braintree-4.9.0/braintree.egg-info/not-zip-safe
+-rw-rw-r--   0 admin     (1000) admin     (1000)       22 2021-05-05 19:57:06.000000 braintree-4.9.0/braintree.egg-info/requires.txt
+-rw-rw-r--   0 admin     (1000) admin     (1000)       10 2021-05-05 19:57:06.000000 braintree-4.9.0/braintree.egg-info/top_level.txt
+-rw-rw-r--   0 admin     (1000) admin     (1000)       67 2021-05-05 19:57:06.000000 braintree-4.9.0/setup.cfg
+-rw-rw-r--   0 admin     (1000) admin     (1000)     1254 2021-05-05 19:56:48.000000 braintree-4.9.0/setup.py
```

### Comparing `braintree-4.8.0/PKG-INFO` & `braintree-4.9.0/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: braintree
-Version: 4.8.0
+Version: 4.9.0
 Summary: Braintree Python Library
 Home-page: https://developers.braintreepayments.com/python/sdk/server/overview
 Author: Braintree
 Author-email: support@braintreepayments.com
 License: MIT
 Description: 
                 The Braintree Python SDK provides integration access to the Braintree Gateway.
```

### Comparing `braintree-4.8.0/README.md` & `braintree-4.9.0/README.md`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/__init__.py` & `braintree-4.9.0/braintree/__init__.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/account_updater_daily_report.py` & `braintree-4.9.0/braintree/account_updater_daily_report.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/add_on_gateway.py` & `braintree-4.9.0/braintree/add_on_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/address.py` & `braintree-4.9.0/braintree/address.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/address_gateway.py` & `braintree-4.9.0/braintree/address_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/amex_express_checkout_card.py` & `braintree-4.9.0/braintree/amex_express_checkout_card.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/android_pay_card.py` & `braintree-4.9.0/braintree/android_pay_card.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/apple_pay_card.py` & `braintree-4.9.0/braintree/apple_pay_card.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/apple_pay_gateway.py` & `braintree-4.9.0/braintree/apple_pay_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/attribute_getter.py` & `braintree-4.9.0/braintree/attribute_getter.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/braintree_gateway.py` & `braintree-4.9.0/braintree/braintree_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/client_token.py` & `braintree-4.9.0/braintree/client_token.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/client_token_gateway.py` & `braintree-4.9.0/braintree/client_token_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/configuration.py` & `braintree-4.9.0/braintree/configuration.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/credentials_parser.py` & `braintree-4.9.0/braintree/credentials_parser.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/credit_card.py` & `braintree-4.9.0/braintree/credit_card.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/credit_card_gateway.py` & `braintree-4.9.0/braintree/credit_card_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/credit_card_verification.py` & `braintree-4.9.0/braintree/credit_card_verification.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/credit_card_verification_gateway.py` & `braintree-4.9.0/braintree/credit_card_verification_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/credit_card_verification_search.py` & `braintree-4.9.0/braintree/credit_card_verification_search.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/customer.py` & `braintree-4.9.0/braintree/customer.py`

 * *Files 3% similar despite different names*

```diff
@@ -166,14 +166,15 @@
             {"three_d_secure_pass_thru": [
                 "cavv",
                 "ds_transaction_id",
                 "eci_flag",
                 "three_d_secure_version",
                 "xid",
                 ]},
+            {"tax_identifiers": ["country_code", "identifier"]},
             {"options": [{"paypal": [
                 "payee_email",
                 "order_id",
                 "custom_field",
                 "description",
                 "amount",
                 { "shipping": Address.create_signature() }
@@ -189,14 +190,15 @@
                 "cavv",
                 "ds_transaction_id",
                 "eci_flag",
                 "three_d_secure_version",
                 "xid",
                 ]},
             {"custom_fields": ["__any_key__"]},
+            {"tax_identifiers": ["country_code", "identifier"]},
             {"options": [{"paypal": [
                 "payee_email",
                 "order_id",
                 "custom_field",
                 "description",
                 "amount",
                 { "shipping": Address.create_signature() }
```

### Comparing `braintree-4.8.0/braintree/customer_gateway.py` & `braintree-4.9.0/braintree/customer_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/customer_search.py` & `braintree-4.9.0/braintree/customer_search.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/disbursement.py` & `braintree-4.9.0/braintree/disbursement.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/disbursement_detail.py` & `braintree-4.9.0/braintree/disbursement_detail.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/discount_gateway.py` & `braintree-4.9.0/braintree/discount_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/dispute.py` & `braintree-4.9.0/braintree/dispute.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from decimal import Decimal
 from braintree.attribute_getter import AttributeGetter
 from braintree.transaction_details import TransactionDetails
-from braintree.dispute_details import DisputeEvidence, DisputeStatusHistory
+from braintree.dispute_details import DisputeEvidence, DisputeStatusHistory, DisputePayPalMessage
 from braintree.configuration import Configuration
 
 class Dispute(AttributeGetter):
     # NEXT_MAJOR_VERSION this can be an enum! they were added as of python 3.4 and we support 3.5+
     class Status(object):
         """
         Constants representing dispute statuses. Available types are:
@@ -172,11 +172,13 @@
         if "amount_won" in attributes and getattr(self, "amount_won", None) is not None:
             self.amount_won = Decimal(self.amount_won)
         if "transaction" in attributes:
             self.transaction_details = TransactionDetails(attributes.pop("transaction"))
             self.transaction = self.transaction_details
         if "evidence" in attributes and getattr(self, "evidence", None) is not None:
             self.evidence = [DisputeEvidence(evidence) for evidence in self.evidence]
+        if "paypal_messages" in attributes and getattr(self, "paypal_messages", None) is not None:
+            self.paypal_messages = [DisputePayPalMessage(paypal_message) for paypal_message in self.paypal_messages]
         if "status_history" in attributes and getattr(self, "status_history", None) is not None:
             self.status_history = [DisputeStatusHistory(status_history) for status_history in self.status_history]
         if "processor_comments" in attributes and self.processor_comments is not None:
             self.forwarded_comments = self.processor_comments
```

### Comparing `braintree-4.8.0/braintree/dispute_gateway.py` & `braintree-4.9.0/braintree/dispute_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/dispute_search.py` & `braintree-4.9.0/braintree/dispute_search.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/document_upload.py` & `braintree-4.9.0/braintree/document_upload.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/document_upload_gateway.py` & `braintree-4.9.0/braintree/document_upload_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/environment.py` & `braintree-4.9.0/braintree/environment.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/error_codes.py` & `braintree-4.9.0/braintree/error_codes.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/error_result.py` & `braintree-4.9.0/braintree/error_result.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/europe_bank_account.py` & `braintree-4.9.0/braintree/europe_bank_account.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/exceptions/__init__.py` & `braintree-4.9.0/braintree/exceptions/__init__.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/masterpass_card.py` & `braintree-4.9.0/braintree/masterpass_card.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/merchant_account/business_details.py` & `braintree-4.9.0/braintree/merchant_account/business_details.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/merchant_account/individual_details.py` & `braintree-4.9.0/braintree/merchant_account/individual_details.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/merchant_account/merchant_account.py` & `braintree-4.9.0/braintree/merchant_account/merchant_account.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/merchant_account_gateway.py` & `braintree-4.9.0/braintree/merchant_account_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/merchant_gateway.py` & `braintree-4.9.0/braintree/merchant_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/oauth_gateway.py` & `braintree-4.9.0/braintree/oauth_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/paginated_collection.py` & `braintree-4.9.0/braintree/paginated_collection.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/partner_merchant.py` & `braintree-4.9.0/braintree/partner_merchant.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/payment_instrument_type.py` & `braintree-4.9.0/braintree/payment_instrument_type.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/payment_method.py` & `braintree-4.9.0/braintree/payment_method.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/payment_method_gateway.py` & `braintree-4.9.0/braintree/payment_method_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/payment_method_nonce.py` & `braintree-4.9.0/braintree/payment_method_nonce.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/payment_method_nonce_gateway.py` & `braintree-4.9.0/braintree/payment_method_nonce_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/payment_method_parser.py` & `braintree-4.9.0/braintree/payment_method_parser.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/paypal_account.py` & `braintree-4.9.0/braintree/paypal_account.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/paypal_account_gateway.py` & `braintree-4.9.0/braintree/paypal_account_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/plan.py` & `braintree-4.9.0/braintree/plan.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/plan_gateway.py` & `braintree-4.9.0/braintree/plan_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/resource.py` & `braintree-4.9.0/braintree/resource.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/resource_collection.py` & `braintree-4.9.0/braintree/resource_collection.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/samsung_pay_card.py` & `braintree-4.9.0/braintree/samsung_pay_card.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/search.py` & `braintree-4.9.0/braintree/search.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/settlement_batch_summary.py` & `braintree-4.9.0/braintree/settlement_batch_summary.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/settlement_batch_summary_gateway.py` & `braintree-4.9.0/braintree/settlement_batch_summary_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/signature_service.py` & `braintree-4.9.0/braintree/signature_service.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/ssl/api_braintreegateway_com.ca.crt` & `braintree-4.9.0/braintree/ssl/api_braintreegateway_com.ca.crt`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/subscription.py` & `braintree-4.9.0/braintree/subscription.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/subscription_gateway.py` & `braintree-4.9.0/braintree/subscription_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/subscription_search.py` & `braintree-4.9.0/braintree/subscription_search.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/successful_result.py` & `braintree-4.9.0/braintree/successful_result.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/test/authentication_ids.py` & `braintree-4.9.0/braintree/test/authentication_ids.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/test/credit_card_numbers.py` & `braintree-4.9.0/braintree/test/credit_card_numbers.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/test/nonces.py` & `braintree-4.9.0/braintree/test/nonces.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/testing_gateway.py` & `braintree-4.9.0/braintree/testing_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/transaction.py` & `braintree-4.9.0/braintree/transaction.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/transaction_gateway.py` & `braintree-4.9.0/braintree/transaction_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/transaction_line_item.py` & `braintree-4.9.0/braintree/transaction_line_item.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/transaction_line_item_gateway.py` & `braintree-4.9.0/braintree/transaction_line_item_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/transaction_search.py` & `braintree-4.9.0/braintree/transaction_search.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/us_bank_account.py` & `braintree-4.9.0/braintree/us_bank_account.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/us_bank_account_gateway.py` & `braintree-4.9.0/braintree/us_bank_account_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/us_bank_account_verification.py` & `braintree-4.9.0/braintree/us_bank_account_verification.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/us_bank_account_verification_gateway.py` & `braintree-4.9.0/braintree/us_bank_account_verification_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/us_bank_account_verification_search.py` & `braintree-4.9.0/braintree/us_bank_account_verification_search.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/util/crypto.py` & `braintree-4.9.0/braintree/util/crypto.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/util/datetime_parser.py` & `braintree-4.9.0/braintree/util/datetime_parser.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/util/generator.py` & `braintree-4.9.0/braintree/util/generator.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/util/graphql_client.py` & `braintree-4.9.0/braintree/util/graphql_client.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/util/http.py` & `braintree-4.9.0/braintree/util/http.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/util/parser.py` & `braintree-4.9.0/braintree/util/parser.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/validation_error_collection.py` & `braintree-4.9.0/braintree/validation_error_collection.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/visa_checkout_card.py` & `braintree-4.9.0/braintree/visa_checkout_card.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/webhook_notification.py` & `braintree-4.9.0/braintree/webhook_notification.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/webhook_notification_gateway.py` & `braintree-4.9.0/braintree/webhook_notification_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree/webhook_testing_gateway.py` & `braintree-4.9.0/braintree/webhook_testing_gateway.py`

 * *Files identical despite different names*

### Comparing `braintree-4.8.0/braintree.egg-info/PKG-INFO` & `braintree-4.9.0/braintree.egg-info/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: braintree
-Version: 4.8.0
+Version: 4.9.0
 Summary: Braintree Python Library
 Home-page: https://developers.braintreepayments.com/python/sdk/server/overview
 Author: Braintree
 Author-email: support@braintreepayments.com
 License: MIT
 Description: 
                 The Braintree Python SDK provides integration access to the Braintree Gateway.
```

### Comparing `braintree-4.8.0/braintree.egg-info/SOURCES.txt` & `braintree-4.9.0/braintree.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -122,14 +122,15 @@
 braintree.egg-info/SOURCES.txt
 braintree.egg-info/dependency_links.txt
 braintree.egg-info/not-zip-safe
 braintree.egg-info/requires.txt
 braintree.egg-info/top_level.txt
 braintree/dispute_details/__init__.py
 braintree/dispute_details/evidence.py
+braintree/dispute_details/paypal_message.py
 braintree/dispute_details/status_history.py
 braintree/exceptions/__init__.py
 braintree/exceptions/authentication_error.py
 braintree/exceptions/authorization_error.py
 braintree/exceptions/braintree_error.py
 braintree/exceptions/configuration_error.py
 braintree/exceptions/gateway_timeout_error.py
```

### Comparing `braintree-4.8.0/setup.py` & `braintree-4.9.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 
         1. https://github.com/braintree/braintree_python - README and Samples
         2. https://developers.braintreepayments.com/python/sdk/server/overview - API Reference
       """
 
 setup(
     name="braintree",
-    version="4.8.0",
+    version="4.9.0",
     description="Braintree Python Library",
     long_description=long_description,
     author="Braintree",
     author_email="support@braintreepayments.com",
     url="https://developers.braintreepayments.com/python/sdk/server/overview",
     packages=["braintree", "braintree.dispute_details", "braintree.exceptions", "braintree.exceptions.http", "braintree.merchant_account", "braintree.util", "braintree.test"],
     package_data={"braintree": ["ssl/*"]},
```

