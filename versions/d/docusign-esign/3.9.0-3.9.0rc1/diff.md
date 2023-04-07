# Comparing `tmp/docusign-esign-3.9.0.tar.gz` & `tmp/docusign-esign-3.9.0rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/docusign-esign-3.9.0.tar", last modified: Wed Apr 28 07:34:28 2021, max compression
+gzip compressed data, was "dist/docusign-esign-3.9.0rc1.tar", last modified: Thu Apr 15 21:13:07 2021, max compression
```

## Comparing `docusign-esign-3.9.0.tar` & `docusign-esign-3.9.0rc1.tar`

### file list

```diff
@@ -1,551 +1,551 @@
-drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-28 07:34:28.000000 docusign-esign-3.9.0/
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)      395 2021-04-28 07:34:28.000000 docusign-esign-3.9.0/PKG-INFO
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5251 2021-04-15 02:17:22.000000 docusign-esign-3.9.0/README.md
-drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-28 07:34:27.000000 docusign-esign-3.9.0/docusign_esign/
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    37247 2021-04-22 22:31:53.000000 docusign-esign-3.9.0/docusign_esign/__init__.py
-drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-28 07:34:27.000000 docusign-esign-3.9.0/docusign_esign/apis/
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)      954 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/apis/__init__.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   400132 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/apis/accounts_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    36525 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/apis/authentication_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    76537 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/apis/billing_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    52353 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/apis/bulk_envelopes_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    51067 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/apis/cloud_storage_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   107859 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/apis/connect_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    26196 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/apis/custom_tabs_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6118 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/apis/data_feed_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    34477 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/apis/diagnostics_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    21447 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/apis/email_archive_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   829682 2021-04-22 22:36:26.000000 docusign-esign-3.9.0/docusign_esign/apis/envelopes_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    29255 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/apis/folders_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    53159 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/apis/groups_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    42588 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/apis/notary_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11087 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/apis/organizations_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    40194 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/apis/power_forms_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    20853 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/apis/signature_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    47054 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/apis/signing_groups_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   315090 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/apis/templates_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    25256 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/apis/trust_service_providers_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   197263 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/apis/users_api.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    66547 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/apis/workspaces_api.py
-drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-28 07:34:27.000000 docusign-esign-3.9.0/docusign_esign/client/
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)      283 2019-08-27 05:10:27.000000 docusign-esign-3.9.0/docusign_esign/client/__init__.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    35251 2020-10-30 18:33:57.000000 docusign-esign-3.9.0/docusign_esign/client/api_client.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     1503 2019-08-27 05:03:15.000000 docusign-esign-3.9.0/docusign_esign/client/api_exception.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12298 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/client/api_response.py
-drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-28 07:34:27.000000 docusign-esign-3.9.0/docusign_esign/client/auth/
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)      219 2019-08-27 05:03:15.000000 docusign-esign-3.9.0/docusign_esign/client/auth/__init__.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    14756 2020-05-12 04:24:44.000000 docusign-esign-3.9.0/docusign_esign/client/auth/oauth.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7256 2021-04-15 06:27:17.000000 docusign-esign-3.9.0/docusign_esign/client/configuration.py
-drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-28 07:34:28.000000 docusign-esign-3.9.0/docusign_esign/models/
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    35859 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/__init__.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12355 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/access_code_format.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11751 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_address.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    27820 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/account_billing_plan.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13640 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_billing_plan_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4994 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_identity_input_option.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3761 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_identity_verification_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3975 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_identity_verification_step.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9217 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_identity_verification_workflow.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    38716 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/account_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4337 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_minimum_password_length.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5010 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_notification.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4317 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_password_expire_password_days.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4485 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_password_lockout_duration_minutes.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3378 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_password_lockout_duration_type.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4325 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_password_minimum_password_age_days.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4505 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_password_questions_required.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    25020 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_password_rules.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3412 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_password_strength_type.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10377 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_password_strength_type_option.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    94250 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/account_role_settings.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3195 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_seals.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   559836 2021-04-22 22:30:22.000000 docusign-esign-3.9.0/docusign_esign/models/account_settings_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11180 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_shared_access.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    31732 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/account_signature.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    17775 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/account_signature_definition.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10153 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_signature_provider.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6328 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_signature_provider_option.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3608 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/account_signature_providers.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3588 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/account_signatures_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    37055 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/account_ui_settings.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5005 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/add_on.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9680 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/address_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5778 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/address_information_input.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7769 2019-08-27 05:03:15.000000 docusign-esign-3.9.0/docusign_esign/models/address_information_v2.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4145 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/admin_message.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    77693 2020-10-15 21:20:12.000000 docusign-esign-3.9.0/docusign_esign/models/agent.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6107 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/api_request_log.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3500 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/api_request_logs_result.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4127 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/app_store_product.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4087 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/app_store_receipt.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    84480 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/approve.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5053 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/ask_an_admin.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7644 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/attachment.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6551 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/authentication_method.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    19327 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/authentication_status.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5510 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bcc_email_address.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10461 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bcc_email_archive.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7374 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bcc_email_archive_history.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9768 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bcc_email_archive_history_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9384 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bcc_email_archive_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    16061 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/billing_charge.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3588 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_charge_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4882 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_discount.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10669 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_invoice.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6599 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_invoice_item.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5452 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_invoices_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5303 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_invoices_summary.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4732 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_payment.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6785 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_payment_item.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3657 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_payment_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3520 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_payment_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5464 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_payments_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    16650 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_plan.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    20425 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_plan_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7365 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_plan_preview.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4229 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_plan_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9712 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_plan_update_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3435 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_plans_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4899 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/billing_price.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    14463 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/brand.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5708 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/brand_email_content.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5427 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/brand_link.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4518 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/brand_logos.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3277 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/brand_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5452 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/brand_resource_urls.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9973 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/brand_resources.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3601 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/brand_resources_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3255 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/brands_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5604 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/brands_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10888 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_envelope.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    15315 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_envelope_status.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9563 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_envelopes_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    14781 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_recipient.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4047 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_recipient_signature_provider.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3939 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_recipient_tab_label.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3621 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_recipients_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9575 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_recipients_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6930 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_recipients_summary_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3255 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_recipients_update_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3307 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_send_batch_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13002 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_send_batch_status.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12060 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_send_batch_summaries.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8468 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_send_batch_summary.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4978 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_send_error_status.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4279 2020-10-15 21:20:12.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_send_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8908 2020-10-15 21:20:12.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_send_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5332 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_send_test_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6764 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_sending_copy.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3999 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_sending_copy_custom_field.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    33940 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_sending_copy_recipient.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4239 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_sending_copy_tab.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4670 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_sending_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3593 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_sending_list_summaries.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5827 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/bulk_sending_list_summary.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6540 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/captive_recipient.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3730 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/captive_recipient_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    83516 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/carbon_copy.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    83466 2020-10-15 21:20:12.000000 docusign-esign-3.9.0/docusign_esign/models/certified_delivery.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    92988 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/checkbox.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3887 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/chunked_upload_part.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4101 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/chunked_upload_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10594 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/chunked_upload_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7833 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/cloud_storage_provider.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3658 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/cloud_storage_providers.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    19339 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/comment.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5681 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/comment_history_result.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6900 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/comment_publish.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    86225 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/comment_thread.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3497 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/comments_publish.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   101786 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/commission_county.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   103402 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/commission_expiration.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   101786 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/commission_number.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   101382 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/commission_state.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    98230 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/company.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5556 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/complete_sign_hash_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9079 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/complete_sign_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8785 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/composite_template.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6062 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/conditional_recipient_rule.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5104 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/conditional_recipient_rule_condition.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7702 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/conditional_recipient_rule_filter.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4335 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/connect_config_results.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    43826 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/connect_custom_configuration.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6584 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/connect_debug_log.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4711 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/connect_event_data.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4160 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/connect_failure_filter.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6934 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/connect_failure_result.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3404 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/connect_failure_results.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    17731 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/connect_log.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5724 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/connect_logs.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8656 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/connect_salesforce_field.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9771 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/connect_salesforce_object.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6922 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/connect_user_object.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4333 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/console_view_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    35295 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/consumer_disclosure.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12836 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/contact.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9130 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/contact_get_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3353 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/contact_mod_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4097 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/contact_phone_number.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3306 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/contact_update_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6183 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/correct_view_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5384 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/country.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5359 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/credential.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8640 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/credit_card_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3381 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/credit_card_types.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   107904 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/currency.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7409 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/currency_feature_set_price.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8231 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/currency_plan_price.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8377 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/custom_field.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7023 2019-08-27 05:03:15.000000 docusign-esign-3.9.0/docusign_esign/models/custom_field_v2.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4535 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/custom_fields.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4631 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/custom_fields_envelope.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3483 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/custom_settings_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    95610 2019-12-23 20:20:06.000000 docusign-esign-3.9.0/docusign_esign/models/date.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    86650 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/date_signed.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5865 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/date_stamp_properties.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    86346 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/decline.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6354 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/diagnostics_settings_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13356 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/direct_debit_processor_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7881 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/display_appliance_account.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4296 2019-12-23 20:20:06.000000 docusign-esign-3.9.0/docusign_esign/models/display_appliance_custom_field.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12940 2019-12-23 20:20:06.000000 docusign-esign-3.9.0/docusign_esign/models/display_appliance_document.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9685 2019-08-27 05:03:35.000000 docusign-esign-3.9.0/docusign_esign/models/display_appliance_document_page.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    18516 2019-12-23 20:20:06.000000 docusign-esign-3.9.0/docusign_esign/models/display_appliance_envelope.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     2533 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/display_appliance_info.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9243 2019-12-23 20:20:06.000000 docusign-esign-3.9.0/docusign_esign/models/display_appliance_page.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     2529 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/display_appliance_pdf.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    25341 2019-12-23 20:20:06.000000 docusign-esign-3.9.0/docusign_esign/models/display_appliance_recipient.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     2581 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/display_appliance_signer_attachment.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5708 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/dob_information_input.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    26828 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/document.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4321 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/document_fields_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11943 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/document_html_collapsible_display_settings.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12672 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/document_html_definition.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5495 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/document_html_definition_original.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3614 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/document_html_definition_originals.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3469 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/document_html_definitions.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7910 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/document_html_display_anchor.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13523 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/document_html_display_settings.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4748 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/document_security_store.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7128 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/document_template.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3524 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/document_template_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8591 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/document_update_info.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6764 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/document_visibility.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3566 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/document_visibility_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4674 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/downgrad_request_billing_info_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4522 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/downgrade_billing_plan_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9490 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/downgrade_plan_update_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    76417 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/draw.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7342 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/e_note_configuration.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    75667 2020-10-15 21:20:12.000000 docusign-esign-3.9.0/docusign_esign/models/editor.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   109904 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/email.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    87362 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/email_address.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5894 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/email_settings.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    74956 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/envelope.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7184 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_attachment.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3415 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_attachments_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3431 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_attachments_result.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3367 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_audit_event.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3484 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_audit_event_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    92632 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_definition.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    25137 2021-02-26 08:17:30.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_document.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4472 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_documents_result.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4807 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_event.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9283 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_form_data.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    85144 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_id.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4507 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_ids_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5348 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_metadata.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5118 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_notification_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6446 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_purge_configuration.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7821 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_summary.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    94662 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_template.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13907 2019-08-27 05:03:15.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_template_definition.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    59810 2019-08-27 05:03:15.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_template_result.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10334 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_template_results.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7121 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_transaction_status.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10743 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_transfer_rule.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9883 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_transfer_rule_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11219 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_transfer_rule_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11501 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelope_update_summary.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13142 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/envelopes_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4050 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/error_details.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    23049 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/event_notification.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6328 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/event_result.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5825 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/expirations.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5475 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/external_claim.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5142 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/external_doc_service_error_details.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11826 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/external_document_sources.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7550 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/external_file.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11024 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/external_folder.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5316 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/favorite_templates_content_item.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5424 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/favorite_templates_info.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4190 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/feature_available_metadata.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10314 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/feature_set.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4121 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/file_type.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3330 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/file_type_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10878 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/filter.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    86294 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/first_name.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13402 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/folder.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    17939 2019-08-27 05:03:15.000000 docusign-esign-3.9.0/docusign_esign/models/folder_item.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8923 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/folder_item_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    19713 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/folder_item_v2.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9944 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/folder_items_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10836 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/folder_shared_item.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4960 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/folders_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9800 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/folders_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12885 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/forgotten_password_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6485 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/form_data_item.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   120895 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/formula_tab.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    85938 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/full_name.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4795 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/graphics_context.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7909 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/group.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5695 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/group_brands.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9172 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/group_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4802 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/id_check_configuration.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6711 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/id_check_information_input.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3279 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/id_check_security_step.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   102224 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/in_person_signer.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    77568 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/initial_here.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6425 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/inline_template.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10142 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/integrated_user_info_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    79653 2020-10-15 21:20:12.000000 docusign-esign-3.9.0/docusign_esign/models/intermediary.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11013 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/jurisdiction.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    85938 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/last_name.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7623 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/linked_external_primary_account.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    97957 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9076 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/list_custom_field.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7357 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/list_item.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    43413 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/locale_policy.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13551 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/locale_policy_tab.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10540 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/lock_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7513 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/lock_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12656 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/login_account.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4690 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/login_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6615 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/match_box.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4790 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/member_group_shared_item.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6284 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/member_shared_items.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13769 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/merge_field.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4949 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/mobile_notifier_configuration.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3940 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/mobile_notifier_configuration_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   111712 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/model_date.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4834 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/money.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5588 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/name_value.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    16510 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/new_account_definition.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9264 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/new_account_summary.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11279 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/new_user.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3325 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/new_users_definition.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3277 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/new_users_summary.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    73332 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/notarize.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5301 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/notary.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    76227 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/notary_certificate.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    71782 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/notary_host.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7548 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/notary_journal.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4905 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/notary_journal_credible_witness.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9255 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/notary_journal_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6022 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/notary_journal_meta_data.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8231 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/notary_jurisdiction.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9530 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/notary_jurisdiction_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   102829 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/notary_recipient.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3975 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/notary_result.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    75366 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/notary_seal.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    86124 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/note.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5058 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/notification.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4837 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/notification_default_settings.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4572 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/notification_defaults.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   114762 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/number.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6943 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/oauth_access.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6939 2019-12-23 20:20:06.000000 docusign-esign-3.9.0/docusign_esign/models/ocr_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8367 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/offline_attributes.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7988 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/page.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8805 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/page_images.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4027 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/page_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3588 2019-08-27 05:03:35.000000 docusign-esign-3.9.0/docusign_esign/models/page_size.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4581 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/path_extended_element.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6167 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/pay_pal_legacy_settings.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    17416 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/payment_details.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    16170 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/payment_gateway_account.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6109 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/payment_gateway_account_setting.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3706 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/payment_gateway_accounts_info.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5531 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/payment_line_item.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4168 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/payment_method_with_options.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5007 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/payment_processor_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3379 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/payment_signer_values.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8609 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/permission_profile.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3735 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/permission_profile_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    99766 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/phone_number.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8017 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/plan_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4753 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/poly_line.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    79517 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/poly_line_overlay.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    23019 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/power_form.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4433 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/power_form_form_data_envelope.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5803 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/power_form_form_data_recipient.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    16297 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/power_form_recipient.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9523 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/power_form_senders_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3420 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/power_forms_form_data_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3339 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/power_forms_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9195 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/power_forms_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6826 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/prefill_tabs.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4300 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/proof_service_resource_token.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3287 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/proof_service_view_link.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3913 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/property_metadata.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3778 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/province.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9652 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/provisioning_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10660 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/purchased_envelopes_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    52780 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/radio.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    29422 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/radio_group.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6963 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_additional_notification.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6972 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_attachment.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5669 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_domain.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10543 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_email_notification.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4903 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_event.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8820 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_form_data.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4984 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_group.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5096 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_identity_input_option.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4925 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_identity_phone_number.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4362 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_identity_verification.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5488 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_names_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7056 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_option.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12303 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_phone_authentication.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5895 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_phone_number.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11796 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_preview_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3409 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_proof_file.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3163 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_routing.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3580 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_rules.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3416 2019-08-27 05:03:15.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_saml_authentication.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5307 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_signature_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7957 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_signature_provider.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9921 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_signature_provider_options.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5051 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_sms_authentication.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6710 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_update_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    20920 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipient_view_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    15181 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/recipients.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3688 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/recipients_update_summary.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    20289 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/referral_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5943 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/reminders.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    27299 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/report_in_product_csv_run_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5591 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/report_in_product_field.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    29587 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/report_in_product_get.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3318 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/report_in_product_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    15399 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/report_in_product_list_item.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    23738 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/report_in_product_run_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9656 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/report_in_product_run_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4298 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/report_in_product_run_response_row.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   123462 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/report_in_product_run_response_row_fields.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3562 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/report_in_product_save_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4208 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/report_in_product_sent_by_details.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3316 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/resource_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4305 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/return_url_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7282 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/revision.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5227 2019-08-27 05:03:15.000000 docusign-esign-3.9.0/docusign_esign/models/saml_assertion_attribute.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4083 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/seal.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4128 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/seal_identifier.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    64893 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/seal_sign.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5097 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/seat_discount.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4132 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/sender.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    14800 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/sender_email_notifications.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4182 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/server_template.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7951 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/service_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4026 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/service_version.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7034 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/settings_metadata.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4603 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/shared_item.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9010 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/sign_hash_document.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9273 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/sign_hash_session_info_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    79439 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/sign_here.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6365 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/sign_session_info_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5353 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/signature_data_info.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4684 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/signature_group.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3926 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/signature_group_def.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3990 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/signature_properties.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4808 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/signature_provider_required_option.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3878 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/signature_type.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5330 2020-10-02 02:02:36.000000 docusign-esign-3.9.0/docusign_esign/models/signature_user.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4652 2020-10-02 02:02:37.000000 docusign-esign-3.9.0/docusign_esign/models/signature_user_def.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    99127 2020-10-15 21:20:12.000000 docusign-esign-3.9.0/docusign_esign/models/signer.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    78800 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/signer_attachment.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    20595 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/signer_email_notifications.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10543 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/signing_group.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3449 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/signing_group_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4841 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/signing_group_user.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3241 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/signing_group_users.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3871 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/smart_contract_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    83637 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/smart_section.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5531 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/smart_section_anchor_position.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11943 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/smart_section_collapsible_display_settings.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13523 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/smart_section_display_settings.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6656 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/social_account_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3414 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/social_authentication.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   109080 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/ssn.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5570 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/ssn4_information_input.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4419 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/ssn9_information_input.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    15988 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/stamp.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3308 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/supported_languages.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    45402 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/tab_account_settings.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    80728 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/tab_group.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    51758 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/tab_metadata.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3190 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/tab_metadata_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    46688 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/tabs.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4631 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/template_custom_fields.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3630 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/template_document_visibility_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4546 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/template_documents_result.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3334 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/template_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5181 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/template_match.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6061 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/template_notification_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    16133 2020-10-02 02:02:37.000000 docusign-esign-3.9.0/docusign_esign/models/template_recipients.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    22318 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/template_role.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9037 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/template_shared_item.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8881 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/template_summary.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    47968 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/template_tabs.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11501 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/template_update_summary.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   113826 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/text.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8238 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/text_custom_field.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5661 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/time_stamp_field.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    97342 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/title.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6912 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/tsp_health_check_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7650 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/tsp_health_check_status_description.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4742 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/update_transaction_request.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3447 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/update_transaction_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6283 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/usage_history.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7057 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/user.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    22840 2020-10-02 02:02:37.000000 docusign-esign-3.9.0/docusign_esign/models/user_account_management_granular_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12332 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/user_info.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3177 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/user_info_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5966 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/user_info_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    42086 2021-02-03 02:00:05.000000 docusign-esign-3.9.0/docusign_esign/models/user_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9126 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/user_information_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6274 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/user_password_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4070 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/user_password_rules.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13969 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/user_profile.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   136773 2021-04-15 06:10:00.000000 docusign-esign-3.9.0/docusign_esign/models/user_settings_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4667 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/user_shared_item.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    30219 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/user_signature.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    15662 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/user_signature_definition.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3495 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/user_signatures_information.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4573 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/user_social_id_result.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8913 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/users_response.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    85748 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/view.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3128 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/view_url.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10111 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/watermark.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    98962 2020-10-15 21:20:12.000000 docusign-esign-3.9.0/docusign_esign/models/witness.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5166 2020-10-02 02:02:37.000000 docusign-esign-3.9.0/docusign_esign/models/workflow.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9090 2020-10-02 02:02:37.000000 docusign-esign-3.9.0/docusign_esign/models/workflow_step.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    14277 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/workspace.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9839 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/workspace_folder_contents.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    22142 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/workspace_item.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3232 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/workspace_item_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7214 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/workspace_list.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3403 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/workspace_settings.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    18845 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/workspace_user.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11952 2020-06-03 00:21:08.000000 docusign-esign-3.9.0/docusign_esign/models/workspace_user_authorization.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   110544 2021-04-22 22:29:40.000000 docusign-esign-3.9.0/docusign_esign/models/zip.py
-drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-28 07:34:27.000000 docusign-esign-3.9.0/docusign_esign.egg-info/
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)      395 2021-04-28 07:34:27.000000 docusign-esign-3.9.0/docusign_esign.egg-info/PKG-INFO
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    24305 2021-04-28 07:34:27.000000 docusign-esign-3.9.0/docusign_esign.egg-info/SOURCES.txt
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        1 2021-04-28 07:34:27.000000 docusign-esign-3.9.0/docusign_esign.egg-info/dependency_links.txt
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)      131 2021-04-28 07:34:27.000000 docusign-esign-3.9.0/docusign_esign.egg-info/requires.txt
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)       20 2021-04-28 07:34:27.000000 docusign-esign-3.9.0/docusign_esign.egg-info/top_level.txt
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)       79 2021-04-28 07:34:28.000000 docusign-esign-3.9.0/setup.cfg
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     1563 2021-04-22 22:38:27.000000 docusign-esign-3.9.0/setup.py
-drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-28 07:34:28.000000 docusign-esign-3.9.0/test/
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2019-08-27 05:03:15.000000 docusign-esign-3.9.0/test/__init__.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5587 2019-08-27 05:03:15.000000 docusign-esign-3.9.0/test/test_oauth.py
--rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    32873 2021-04-15 06:43:37.000000 docusign-esign-3.9.0/test/unit_tests.py
+drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-15 21:13:07.000000 docusign-esign-3.9.0rc1/
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)      398 2021-04-15 21:13:07.000000 docusign-esign-3.9.0rc1/PKG-INFO
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5251 2021-04-15 02:17:22.000000 docusign-esign-3.9.0rc1/README.md
+drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-15 21:13:07.000000 docusign-esign-3.9.0rc1/docusign_esign/
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    37247 2021-04-15 06:19:54.000000 docusign-esign-3.9.0rc1/docusign_esign/__init__.py
+drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-15 21:13:07.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)      954 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/__init__.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   400132 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/accounts_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    36525 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/authentication_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    76537 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/billing_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    52353 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/bulk_envelopes_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    51067 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/cloud_storage_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   107859 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/connect_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    26196 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/custom_tabs_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6118 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/data_feed_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    34477 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/diagnostics_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    21447 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/email_archive_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   829682 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/envelopes_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    29255 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/folders_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    53159 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/groups_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    42588 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/notary_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11087 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/organizations_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    40194 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/power_forms_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    20853 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/signature_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    47054 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/signing_groups_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   315090 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/templates_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    25256 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/trust_service_providers_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   197263 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/users_api.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    66547 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/apis/workspaces_api.py
+drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-15 21:13:07.000000 docusign-esign-3.9.0rc1/docusign_esign/client/
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)      283 2019-08-27 05:10:27.000000 docusign-esign-3.9.0rc1/docusign_esign/client/__init__.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    35251 2020-10-30 18:33:57.000000 docusign-esign-3.9.0rc1/docusign_esign/client/api_client.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     1503 2019-08-27 05:03:15.000000 docusign-esign-3.9.0rc1/docusign_esign/client/api_exception.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12298 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/client/api_response.py
+drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-15 21:13:07.000000 docusign-esign-3.9.0rc1/docusign_esign/client/auth/
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)      219 2019-08-27 05:03:15.000000 docusign-esign-3.9.0rc1/docusign_esign/client/auth/__init__.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    14756 2020-05-12 04:24:44.000000 docusign-esign-3.9.0rc1/docusign_esign/client/auth/oauth.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7256 2021-04-15 06:27:17.000000 docusign-esign-3.9.0rc1/docusign_esign/client/configuration.py
+drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-15 21:13:07.000000 docusign-esign-3.9.0rc1/docusign_esign/models/
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    35859 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/__init__.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12355 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/access_code_format.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11751 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_address.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    27820 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_billing_plan.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13640 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_billing_plan_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4994 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_identity_input_option.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3761 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_identity_verification_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3975 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_identity_verification_step.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9217 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_identity_verification_workflow.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    38716 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4337 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_minimum_password_length.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5010 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_notification.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4317 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_password_expire_password_days.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4485 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_password_lockout_duration_minutes.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3378 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_password_lockout_duration_type.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4325 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_password_minimum_password_age_days.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4505 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_password_questions_required.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    25020 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_password_rules.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3412 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_password_strength_type.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10377 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_password_strength_type_option.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    94250 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_role_settings.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3195 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_seals.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   559836 2021-04-15 06:15:06.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_settings_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11180 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_shared_access.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    31732 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_signature.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    17775 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_signature_definition.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10153 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_signature_provider.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6328 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_signature_provider_option.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3608 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_signature_providers.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3588 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_signatures_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    37055 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/account_ui_settings.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5005 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/add_on.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9680 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/address_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5778 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/address_information_input.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7769 2019-08-27 05:03:15.000000 docusign-esign-3.9.0rc1/docusign_esign/models/address_information_v2.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4145 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/admin_message.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    77693 2020-10-15 21:20:12.000000 docusign-esign-3.9.0rc1/docusign_esign/models/agent.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6107 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/api_request_log.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3500 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/api_request_logs_result.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4127 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/app_store_product.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4087 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/app_store_receipt.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    83837 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/approve.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5053 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/ask_an_admin.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7644 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/attachment.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6551 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/authentication_method.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    19327 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/authentication_status.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5510 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bcc_email_address.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10461 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bcc_email_archive.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7374 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bcc_email_archive_history.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9768 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bcc_email_archive_history_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9384 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bcc_email_archive_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    16061 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_charge.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3588 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_charge_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4882 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_discount.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10669 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_invoice.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6599 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_invoice_item.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5452 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_invoices_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5303 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_invoices_summary.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4732 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_payment.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6785 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_payment_item.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3657 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_payment_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3520 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_payment_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5464 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_payments_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    16650 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_plan.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    20425 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_plan_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7365 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_plan_preview.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4229 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_plan_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9712 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_plan_update_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3435 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_plans_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4899 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/billing_price.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    14463 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/brand.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5708 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/brand_email_content.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5427 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/brand_link.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4518 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/brand_logos.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3277 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/brand_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5452 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/brand_resource_urls.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9973 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/brand_resources.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3601 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/brand_resources_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3255 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/brands_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5604 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/brands_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10888 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_envelope.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    15315 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_envelope_status.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9563 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_envelopes_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    14781 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_recipient.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4047 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_recipient_signature_provider.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3939 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_recipient_tab_label.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3621 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_recipients_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9575 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_recipients_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6930 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_recipients_summary_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3255 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_recipients_update_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3307 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_batch_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13002 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_batch_status.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12060 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_batch_summaries.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8468 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_batch_summary.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4978 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_error_status.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4279 2020-10-15 21:20:12.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8908 2020-10-15 21:20:12.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5332 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_test_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6764 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_sending_copy.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3999 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_sending_copy_custom_field.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    33940 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_sending_copy_recipient.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4239 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_sending_copy_tab.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4670 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_sending_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3593 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_sending_list_summaries.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5827 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/bulk_sending_list_summary.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6540 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/captive_recipient.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3730 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/captive_recipient_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    83516 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/carbon_copy.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    83466 2020-10-15 21:20:12.000000 docusign-esign-3.9.0rc1/docusign_esign/models/certified_delivery.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    92341 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/checkbox.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3887 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/chunked_upload_part.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4101 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/chunked_upload_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10594 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/chunked_upload_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7833 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/cloud_storage_provider.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3658 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/cloud_storage_providers.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    19339 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/comment.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5681 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/comment_history_result.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6900 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/comment_publish.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    85558 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/comment_thread.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3497 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/comments_publish.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   101107 2020-10-15 21:20:12.000000 docusign-esign-3.9.0rc1/docusign_esign/models/commission_county.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   102707 2020-10-15 21:20:12.000000 docusign-esign-3.9.0rc1/docusign_esign/models/commission_expiration.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   101107 2020-10-15 21:20:12.000000 docusign-esign-3.9.0rc1/docusign_esign/models/commission_number.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   100707 2020-10-15 21:20:12.000000 docusign-esign-3.9.0rc1/docusign_esign/models/commission_state.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    97587 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/company.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5556 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/complete_sign_hash_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9079 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/complete_sign_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8785 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/composite_template.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6062 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/conditional_recipient_rule.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5104 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/conditional_recipient_rule_condition.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7702 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/conditional_recipient_rule_filter.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4335 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/connect_config_results.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    43826 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/connect_custom_configuration.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6584 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/connect_debug_log.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4711 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/connect_event_data.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4160 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/connect_failure_filter.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6934 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/connect_failure_result.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3404 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/connect_failure_results.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    17731 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/connect_log.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5724 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/connect_logs.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8656 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/connect_salesforce_field.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9771 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/connect_salesforce_object.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6922 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/connect_user_object.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4333 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/console_view_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    35295 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/consumer_disclosure.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12836 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/contact.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9130 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/contact_get_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3353 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/contact_mod_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4097 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/contact_phone_number.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3306 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/contact_update_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6183 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/correct_view_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5384 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/country.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5359 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/credential.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8640 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/credit_card_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3381 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/credit_card_types.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   107257 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/currency.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7409 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/currency_feature_set_price.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8231 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/currency_plan_price.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8377 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/custom_field.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7023 2019-08-27 05:03:15.000000 docusign-esign-3.9.0rc1/docusign_esign/models/custom_field_v2.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4535 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/custom_fields.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4631 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/custom_fields_envelope.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3483 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/custom_settings_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    95610 2019-12-23 20:20:06.000000 docusign-esign-3.9.0rc1/docusign_esign/models/date.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    85995 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/date_signed.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5865 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/date_stamp_properties.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    85703 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/decline.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6354 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/diagnostics_settings_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13356 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/direct_debit_processor_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7881 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_account.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4296 2019-12-23 20:20:06.000000 docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_custom_field.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12940 2019-12-23 20:20:06.000000 docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_document.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9685 2019-08-27 05:03:35.000000 docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_document_page.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    18516 2019-12-23 20:20:06.000000 docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_envelope.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     2533 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_info.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9243 2019-12-23 20:20:06.000000 docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_page.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     2529 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_pdf.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    25341 2019-12-23 20:20:06.000000 docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_recipient.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     2581 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_signer_attachment.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5708 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/dob_information_input.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    26828 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/document.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4321 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/document_fields_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11943 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/document_html_collapsible_display_settings.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12672 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/document_html_definition.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5495 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/document_html_definition_original.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3614 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/document_html_definition_originals.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3469 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/document_html_definitions.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7910 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/document_html_display_anchor.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13523 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/document_html_display_settings.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4748 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/document_security_store.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7128 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/document_template.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3524 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/document_template_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8591 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/document_update_info.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6764 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/document_visibility.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3566 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/document_visibility_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4674 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/downgrad_request_billing_info_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4522 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/downgrade_billing_plan_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9490 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/downgrade_plan_update_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    75786 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/draw.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7342 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/e_note_configuration.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    75667 2020-10-15 21:20:12.000000 docusign-esign-3.9.0rc1/docusign_esign/models/editor.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   109269 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/email.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    86699 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/email_address.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5894 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/email_settings.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    74956 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7184 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_attachment.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3415 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_attachments_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3431 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_attachments_result.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3367 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_audit_event.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3484 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_audit_event_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    92632 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_definition.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    25137 2021-02-26 08:17:30.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_document.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4472 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_documents_result.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4807 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_event.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9283 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_form_data.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    84489 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_id.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4507 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_ids_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5348 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_metadata.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5118 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_notification_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6446 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_purge_configuration.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7821 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_summary.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    94662 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_template.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13907 2019-08-27 05:03:15.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_template_definition.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    59810 2019-08-27 05:03:15.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_template_result.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10334 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_template_results.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7121 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_transaction_status.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10743 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_transfer_rule.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9883 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_transfer_rule_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11219 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_transfer_rule_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11501 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelope_update_summary.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13142 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/envelopes_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4050 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/error_details.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    23049 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/event_notification.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6328 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/event_result.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5825 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/expirations.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5475 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/external_claim.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5142 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/external_doc_service_error_details.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11826 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/external_document_sources.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7550 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/external_file.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11024 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/external_folder.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5316 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/favorite_templates_content_item.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5424 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/favorite_templates_info.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4190 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/feature_available_metadata.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10314 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/feature_set.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4121 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/file_type.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3330 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/file_type_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10878 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/filter.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    85643 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/first_name.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13402 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/folder.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    17939 2019-08-27 05:03:15.000000 docusign-esign-3.9.0rc1/docusign_esign/models/folder_item.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8923 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/folder_item_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    19713 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/folder_item_v2.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9944 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/folder_items_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10836 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/folder_shared_item.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4960 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/folders_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9800 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/folders_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12885 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/forgotten_password_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6485 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/form_data_item.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   120240 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/formula_tab.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    85291 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/full_name.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4795 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/graphics_context.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7909 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/group.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5695 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/group_brands.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9172 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/group_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4802 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/id_check_configuration.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6711 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/id_check_information_input.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3279 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/id_check_security_step.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   102224 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/in_person_signer.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    76909 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/initial_here.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6425 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/inline_template.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10142 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/integrated_user_info_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    79653 2020-10-15 21:20:12.000000 docusign-esign-3.9.0rc1/docusign_esign/models/intermediary.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11013 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/jurisdiction.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    85291 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/last_name.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7623 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/linked_external_primary_account.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    97326 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9076 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/list_custom_field.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7357 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/list_item.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    43413 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/locale_policy.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13551 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/locale_policy_tab.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10540 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/lock_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7513 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/lock_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12656 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/login_account.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4690 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/login_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6615 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/match_box.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4790 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/member_group_shared_item.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6284 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/member_shared_items.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13769 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/merge_field.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4949 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/mobile_notifier_configuration.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3940 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/mobile_notifier_configuration_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   111061 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/model_date.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4834 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/money.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5588 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/name_value.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    16510 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/new_account_definition.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9264 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/new_account_summary.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11279 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/new_user.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3325 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/new_users_definition.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3277 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/new_users_summary.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    72685 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notarize.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5301 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notary.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    76227 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notary_certificate.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    71782 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notary_host.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7548 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notary_journal.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4905 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notary_journal_credible_witness.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9255 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notary_journal_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6022 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notary_journal_meta_data.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8231 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notary_jurisdiction.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9530 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notary_jurisdiction_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   102829 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notary_recipient.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3975 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notary_result.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    74711 2020-10-15 21:20:12.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notary_seal.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    85493 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/note.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5058 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notification.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4837 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notification_default_settings.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4572 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/notification_defaults.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   114123 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/number.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6943 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/oauth_access.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6939 2019-12-23 20:20:06.000000 docusign-esign-3.9.0rc1/docusign_esign/models/ocr_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8367 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/offline_attributes.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7988 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/page.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8805 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/page_images.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4027 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/page_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3588 2019-08-27 05:03:35.000000 docusign-esign-3.9.0rc1/docusign_esign/models/page_size.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4581 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/path_extended_element.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6167 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/pay_pal_legacy_settings.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    17416 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/payment_details.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    16170 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/payment_gateway_account.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6109 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/payment_gateway_account_setting.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3706 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/payment_gateway_accounts_info.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5531 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/payment_line_item.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4168 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/payment_method_with_options.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5007 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/payment_processor_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3379 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/payment_signer_values.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8609 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/permission_profile.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3735 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/permission_profile_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    99107 2020-10-15 21:20:12.000000 docusign-esign-3.9.0rc1/docusign_esign/models/phone_number.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8017 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/plan_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4753 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/poly_line.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    78842 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/poly_line_overlay.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    23019 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/power_form.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4433 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/power_form_form_data_envelope.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5803 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/power_form_form_data_recipient.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    16297 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/power_form_recipient.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9523 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/power_form_senders_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3420 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/power_forms_form_data_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3339 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/power_forms_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9195 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/power_forms_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6826 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/prefill_tabs.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4300 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/proof_service_resource_token.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3287 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/proof_service_view_link.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3913 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/property_metadata.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3778 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/province.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9652 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/provisioning_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10660 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/purchased_envelopes_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    52780 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/radio.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    29422 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/radio_group.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6963 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_additional_notification.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6972 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_attachment.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5669 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_domain.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10543 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_email_notification.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4903 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_event.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8820 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_form_data.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4984 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_group.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5096 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_identity_input_option.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4925 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_identity_phone_number.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4362 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_identity_verification.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5488 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_names_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7056 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_option.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12303 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_phone_authentication.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5895 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_phone_number.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11796 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_preview_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3409 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_proof_file.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3163 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_routing.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3580 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_rules.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3416 2019-08-27 05:03:15.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_saml_authentication.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5307 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_signature_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7957 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_signature_provider.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9921 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_signature_provider_options.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5051 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_sms_authentication.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6710 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_update_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    20920 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipient_view_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    15181 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipients.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3688 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/recipients_update_summary.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    20289 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/referral_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5943 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/reminders.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    27299 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_csv_run_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5591 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_field.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    29587 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_get.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3318 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    15399 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_list_item.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    23738 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_run_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9656 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_run_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4298 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_run_response_row.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   123462 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_run_response_row_fields.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3562 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_save_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4208 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_sent_by_details.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3316 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/resource_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4305 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/return_url_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7282 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/revision.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5227 2019-08-27 05:03:15.000000 docusign-esign-3.9.0rc1/docusign_esign/models/saml_assertion_attribute.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4083 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/seal.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4128 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/seal_identifier.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    64893 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/seal_sign.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5097 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/seat_discount.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4132 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/sender.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    14800 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/sender_email_notifications.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4182 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/server_template.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7951 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/service_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4026 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/service_version.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7034 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/settings_metadata.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4603 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/shared_item.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9010 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/sign_hash_document.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9273 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/sign_hash_session_info_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    78792 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/sign_here.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6365 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/sign_session_info_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5353 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/signature_data_info.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4684 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/signature_group.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3926 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/signature_group_def.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3990 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/signature_properties.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4808 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/signature_provider_required_option.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3878 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/signature_type.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5330 2020-10-02 02:02:36.000000 docusign-esign-3.9.0rc1/docusign_esign/models/signature_user.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4652 2020-10-02 02:02:37.000000 docusign-esign-3.9.0rc1/docusign_esign/models/signature_user_def.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    99127 2020-10-15 21:20:12.000000 docusign-esign-3.9.0rc1/docusign_esign/models/signer.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    78121 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/signer_attachment.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    20595 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/signer_email_notifications.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10543 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/signing_group.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3449 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/signing_group_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4841 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/signing_group_user.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3241 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/signing_group_users.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3871 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/smart_contract_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    82974 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/smart_section.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5531 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/smart_section_anchor_position.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11943 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/smart_section_collapsible_display_settings.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13523 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/smart_section_display_settings.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6656 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/social_account_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3414 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/social_authentication.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   108453 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/ssn.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5570 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/ssn4_information_input.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4419 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/ssn9_information_input.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    15988 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/stamp.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3308 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/supported_languages.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    45402 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/tab_account_settings.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    80081 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/tab_group.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    51758 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/tab_metadata.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3190 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/tab_metadata_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    46688 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/tabs.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4631 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/template_custom_fields.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3630 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/template_document_visibility_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4546 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/template_documents_result.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3334 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/template_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5181 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/template_match.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6061 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/template_notification_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    16133 2020-10-02 02:02:37.000000 docusign-esign-3.9.0rc1/docusign_esign/models/template_recipients.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    22318 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/template_role.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9037 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/template_shared_item.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8881 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/template_summary.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    47968 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/template_tabs.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11501 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/template_update_summary.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   113195 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/text.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8238 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/text_custom_field.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5661 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/time_stamp_field.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    96707 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/title.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6912 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/tsp_health_check_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7650 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/tsp_health_check_status_description.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4742 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/update_transaction_request.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3447 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/update_transaction_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6283 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/usage_history.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7057 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    22840 2020-10-02 02:02:37.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user_account_management_granular_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    12332 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user_info.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3177 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user_info_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5966 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user_info_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    42086 2021-02-03 02:00:05.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9126 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user_information_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     6274 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user_password_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4070 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user_password_rules.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    13969 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user_profile.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   136773 2021-04-15 06:10:00.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user_settings_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4667 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user_shared_item.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    30219 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user_signature.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    15662 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user_signature_definition.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3495 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user_signatures_information.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     4573 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/user_social_id_result.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     8913 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/users_response.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    85117 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/view.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3128 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/view_url.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    10111 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/watermark.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    98962 2020-10-15 21:20:12.000000 docusign-esign-3.9.0rc1/docusign_esign/models/witness.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5166 2020-10-02 02:02:37.000000 docusign-esign-3.9.0rc1/docusign_esign/models/workflow.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9090 2020-10-02 02:02:37.000000 docusign-esign-3.9.0rc1/docusign_esign/models/workflow_step.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    14277 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/workspace.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     9839 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/workspace_folder_contents.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    22142 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/workspace_item.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3232 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/workspace_item_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     7214 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/workspace_list.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     3403 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/workspace_settings.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    18845 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/workspace_user.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    11952 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/workspace_user_authorization.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)   109917 2020-06-03 00:21:08.000000 docusign-esign-3.9.0rc1/docusign_esign/models/zip.py
+drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-15 21:13:07.000000 docusign-esign-3.9.0rc1/docusign_esign.egg-info/
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)      398 2021-04-15 21:13:07.000000 docusign-esign-3.9.0rc1/docusign_esign.egg-info/PKG-INFO
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    24305 2021-04-15 21:13:07.000000 docusign-esign-3.9.0rc1/docusign_esign.egg-info/SOURCES.txt
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        1 2021-04-15 21:13:07.000000 docusign-esign-3.9.0rc1/docusign_esign.egg-info/dependency_links.txt
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)      131 2021-04-15 21:13:07.000000 docusign-esign-3.9.0rc1/docusign_esign.egg-info/requires.txt
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)       20 2021-04-15 21:13:07.000000 docusign-esign-3.9.0rc1/docusign_esign.egg-info/top_level.txt
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)       79 2021-04-15 21:13:07.000000 docusign-esign-3.9.0rc1/setup.cfg
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     1566 2021-04-15 06:12:44.000000 docusign-esign-3.9.0rc1/setup.py
+drwxr-xr-x   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2021-04-15 21:13:07.000000 docusign-esign-3.9.0rc1/test/
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)        0 2019-08-27 05:03:15.000000 docusign-esign-3.9.0rc1/test/__init__.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)     5587 2019-08-27 05:03:15.000000 docusign-esign-3.9.0rc1/test/test_oauth.py
+-rw-r--r--   0 harsharahul.boggaram (391859142) DOCUSIGNHQ\Domain Users (425918093)    32873 2021-04-15 06:43:37.000000 docusign-esign-3.9.0rc1/test/unit_tests.py
```

### Comparing `docusign-esign-3.9.0/README.md` & `docusign-esign-3.9.0rc1/README.md`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/__init__.py` & `docusign-esign-3.9.0rc1/docusign_esign/__init__.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/__init__.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/__init__.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/accounts_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/accounts_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/authentication_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/authentication_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/billing_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/billing_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/bulk_envelopes_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/bulk_envelopes_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/cloud_storage_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/cloud_storage_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/connect_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/connect_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/custom_tabs_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/custom_tabs_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/data_feed_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/data_feed_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/diagnostics_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/diagnostics_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/email_archive_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/email_archive_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/envelopes_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/envelopes_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/folders_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/folders_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/groups_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/groups_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/notary_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/notary_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/organizations_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/organizations_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/power_forms_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/power_forms_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/signature_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/signature_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/signing_groups_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/signing_groups_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/templates_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/templates_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/trust_service_providers_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/trust_service_providers_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/users_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/users_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/apis/workspaces_api.py` & `docusign-esign-3.9.0rc1/docusign_esign/apis/workspaces_api.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/client/api_client.py` & `docusign-esign-3.9.0rc1/docusign_esign/client/api_client.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/client/api_exception.py` & `docusign-esign-3.9.0rc1/docusign_esign/client/api_exception.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/client/api_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/client/api_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/client/auth/oauth.py` & `docusign-esign-3.9.0rc1/docusign_esign/client/auth/oauth.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/client/configuration.py` & `docusign-esign-3.9.0rc1/docusign_esign/client/configuration.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/__init__.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/__init__.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/access_code_format.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/access_code_format.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_address.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_address.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_billing_plan.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_billing_plan.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_billing_plan_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_billing_plan_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_identity_input_option.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_identity_input_option.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_identity_verification_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_identity_verification_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_identity_verification_step.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_identity_verification_step.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_identity_verification_workflow.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_identity_verification_workflow.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_minimum_password_length.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_minimum_password_length.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_notification.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_notification.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_password_expire_password_days.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_password_expire_password_days.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_password_lockout_duration_minutes.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_password_lockout_duration_minutes.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_password_lockout_duration_type.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_password_lockout_duration_type.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_password_minimum_password_age_days.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_password_minimum_password_age_days.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_password_questions_required.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_password_questions_required.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_password_rules.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_password_rules.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_password_strength_type.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_password_strength_type.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_password_strength_type_option.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_password_strength_type_option.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_role_settings.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_role_settings.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_seals.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_seals.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_settings_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_settings_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_shared_access.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_shared_access.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_signature.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_signature.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_signature_definition.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_signature_definition.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_signature_provider.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_signature_provider.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_signature_provider_option.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_signature_provider_option.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_signature_providers.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_signature_providers.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_signatures_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_signatures_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/account_ui_settings.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/account_ui_settings.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/add_on.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/add_on.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/address_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/address_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/address_information_input.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/address_information_input.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/address_information_v2.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/address_information_v2.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/admin_message.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/admin_message.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/agent.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/agent.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/api_request_log.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/api_request_log.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/api_request_logs_result.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/api_request_logs_result.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/app_store_product.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/app_store_product.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/app_store_receipt.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/app_store_receipt.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/approve.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/approve.py`

 * *Files 1% similar despite different names*

```diff
@@ -86,15 +86,14 @@
         'page_number': 'str',
         'page_number_metadata': 'PropertyMetadata',
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -175,15 +174,14 @@
         'page_number': 'pageNumber',
         'page_number_metadata': 'pageNumberMetadata',
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -204,15 +202,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, button_text=None, button_text_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, button_text=None, button_text_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """Approve - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -266,15 +264,14 @@
         self._page_number = None
         self._page_number_metadata = None
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -413,16 +410,14 @@
             self.recipient_id_guid = recipient_id_guid
         if recipient_id_guid_metadata is not None:
             self.recipient_id_guid_metadata = recipient_id_guid_metadata
         if recipient_id_metadata is not None:
             self.recipient_id_metadata = recipient_id_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1764,37 +1759,14 @@
         :param smart_contract_information: The smart_contract_information of this Approve.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this Approve.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this Approve.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this Approve.
-
-          # noqa: E501
-
-        :param source: The source of this Approve.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this Approve.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this Approve.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/ask_an_admin.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/ask_an_admin.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/attachment.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/attachment.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/authentication_method.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/authentication_method.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/authentication_status.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/authentication_status.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bcc_email_address.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bcc_email_address.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bcc_email_archive.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bcc_email_archive.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bcc_email_archive_history.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bcc_email_archive_history.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bcc_email_archive_history_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bcc_email_archive_history_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bcc_email_archive_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bcc_email_archive_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_charge.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_charge.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_charge_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_charge_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_discount.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_discount.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_invoice.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_invoice.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_invoice_item.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_invoice_item.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_invoices_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_invoices_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_invoices_summary.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_invoices_summary.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_payment.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_payment.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_payment_item.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_payment_item.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_payment_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_payment_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_payment_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_payment_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_payments_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_payments_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_plan.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_plan.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_plan_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_plan_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_plan_preview.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_plan_preview.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_plan_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_plan_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_plan_update_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_plan_update_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_plans_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_plans_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/billing_price.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/billing_price.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/brand.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/brand.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/brand_email_content.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/brand_email_content.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/brand_link.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/brand_link.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/brand_logos.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/brand_logos.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/brand_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/brand_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/brand_resource_urls.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/brand_resource_urls.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/brand_resources.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/brand_resources.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/brand_resources_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/brand_resources_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/brands_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/brands_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/brands_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/brands_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_envelope.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_envelope.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_envelope_status.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_envelope_status.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_envelopes_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_envelopes_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_recipient.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_recipient.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_recipient_signature_provider.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_recipient_signature_provider.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_recipient_tab_label.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_recipient_tab_label.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_recipients_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_recipients_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_recipients_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_recipients_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_recipients_summary_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_recipients_summary_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_recipients_update_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_recipients_update_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_send_batch_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_batch_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_send_batch_status.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_batch_status.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_send_batch_summaries.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_batch_summaries.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_send_batch_summary.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_batch_summary.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_send_error_status.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_error_status.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_send_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_send_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_send_test_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_send_test_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_sending_copy.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_sending_copy.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_sending_copy_custom_field.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_sending_copy_custom_field.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_sending_copy_recipient.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_sending_copy_recipient.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_sending_copy_tab.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_sending_copy_tab.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_sending_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_sending_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_sending_list_summaries.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_sending_list_summaries.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/bulk_sending_list_summary.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/bulk_sending_list_summary.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/captive_recipient.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/captive_recipient.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/captive_recipient_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/captive_recipient_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/carbon_copy.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/carbon_copy.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/certified_delivery.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/certified_delivery.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/checkbox.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/checkbox.py`

 * *Files 0% similar despite different names*

```diff
@@ -95,15 +95,14 @@
         'require_initial_on_shared_change': 'str',
         'require_initial_on_shared_change_metadata': 'PropertyMetadata',
         'selected': 'str',
         'selected_metadata': 'PropertyMetadata',
         'shared': 'str',
         'shared_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -193,15 +192,14 @@
         'require_initial_on_shared_change': 'requireInitialOnSharedChange',
         'require_initial_on_shared_change_metadata': 'requireInitialOnSharedChangeMetadata',
         'selected': 'selected',
         'selected_metadata': 'selectedMetadata',
         'shared': 'shared',
         'shared_metadata': 'sharedMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -222,15 +220,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locked=None, locked_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, selected=None, selected_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locked=None, locked_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, selected=None, selected_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """Checkbox - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -293,15 +291,14 @@
         self._require_initial_on_shared_change = None
         self._require_initial_on_shared_change_metadata = None
         self._selected = None
         self._selected_metadata = None
         self._shared = None
         self._shared_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -458,16 +455,14 @@
             self.selected_metadata = selected_metadata
         if shared is not None:
             self.shared = shared
         if shared_metadata is not None:
             self.shared_metadata = shared_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2008,37 +2003,14 @@
         :param smart_contract_information: The smart_contract_information of this Checkbox.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this Checkbox.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this Checkbox.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this Checkbox.
-
-          # noqa: E501
-
-        :param source: The source of this Checkbox.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this Checkbox.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this Checkbox.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/chunked_upload_part.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/chunked_upload_part.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/chunked_upload_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/chunked_upload_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/chunked_upload_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/chunked_upload_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/cloud_storage_provider.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/cloud_storage_provider.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/cloud_storage_providers.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/cloud_storage_providers.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/comment.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/comment.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/comment_history_result.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/comment_history_result.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/comment_publish.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/comment_publish.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/comment_thread.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/comment_thread.py`

 * *Files 1% similar despite different names*

```diff
@@ -85,15 +85,14 @@
         'page_number': 'str',
         'page_number_metadata': 'PropertyMetadata',
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -174,15 +173,14 @@
         'page_number': 'pageNumber',
         'page_number_metadata': 'pageNumberMetadata',
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -204,15 +202,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, comments=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, thread_id=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, comments=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, thread_id=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """CommentThread - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -265,15 +263,14 @@
         self._page_number = None
         self._page_number_metadata = None
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -411,16 +408,14 @@
             self.recipient_id_guid = recipient_id_guid
         if recipient_id_guid_metadata is not None:
             self.recipient_id_guid_metadata = recipient_id_guid_metadata
         if recipient_id_metadata is not None:
             self.recipient_id_metadata = recipient_id_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1743,37 +1738,14 @@
         :param smart_contract_information: The smart_contract_information of this CommentThread.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this CommentThread.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this CommentThread.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this CommentThread.
-
-          # noqa: E501
-
-        :param source: The source of this CommentThread.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this CommentThread.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this CommentThread.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/comments_publish.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/comments_publish.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/commission_county.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/commission_county.py`

 * *Files 0% similar despite different names*

```diff
@@ -98,15 +98,14 @@
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'required': 'str',
         'required_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -201,15 +200,14 @@
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'required': 'required',
         'required_metadata': 'requiredMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -232,15 +230,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """CommissionCounty - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -306,15 +304,14 @@
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._required = None
         self._required_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -479,16 +476,14 @@
             self.recipient_id_metadata = recipient_id_metadata
         if required is not None:
             self.required = required
         if required_metadata is not None:
             self.required_metadata = required_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2098,37 +2093,14 @@
         :param smart_contract_information: The smart_contract_information of this CommissionCounty.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this CommissionCounty.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this CommissionCounty.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this CommissionCounty.
-
-          # noqa: E501
-
-        :param source: The source of this CommissionCounty.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this CommissionCounty.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this CommissionCounty.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/commission_expiration.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/commission_expiration.py`

 * *Files 0% similar despite different names*

```diff
@@ -98,15 +98,14 @@
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'required': 'str',
         'required_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -201,15 +200,14 @@
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'required': 'required',
         'required_metadata': 'requiredMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -232,15 +230,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """CommissionExpiration - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -306,15 +304,14 @@
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._required = None
         self._required_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -479,16 +476,14 @@
             self.recipient_id_metadata = recipient_id_metadata
         if required is not None:
             self.required = required
         if required_metadata is not None:
             self.required_metadata = required_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2098,37 +2093,14 @@
         :param smart_contract_information: The smart_contract_information of this CommissionExpiration.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this CommissionExpiration.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this CommissionExpiration.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this CommissionExpiration.
-
-          # noqa: E501
-
-        :param source: The source of this CommissionExpiration.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this CommissionExpiration.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this CommissionExpiration.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/commission_number.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/commission_number.py`

 * *Files 1% similar despite different names*

```diff
@@ -98,15 +98,14 @@
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'required': 'str',
         'required_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -201,15 +200,14 @@
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'required': 'required',
         'required_metadata': 'requiredMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -232,15 +230,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """CommissionNumber - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -306,15 +304,14 @@
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._required = None
         self._required_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -479,16 +476,14 @@
             self.recipient_id_metadata = recipient_id_metadata
         if required is not None:
             self.required = required
         if required_metadata is not None:
             self.required_metadata = required_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2098,37 +2093,14 @@
         :param smart_contract_information: The smart_contract_information of this CommissionNumber.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this CommissionNumber.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this CommissionNumber.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this CommissionNumber.
-
-          # noqa: E501
-
-        :param source: The source of this CommissionNumber.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this CommissionNumber.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this CommissionNumber.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/commission_state.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/commission_state.py`

 * *Files 0% similar despite different names*

```diff
@@ -98,15 +98,14 @@
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'required': 'str',
         'required_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -201,15 +200,14 @@
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'required': 'required',
         'required_metadata': 'requiredMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -232,15 +230,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """CommissionState - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -306,15 +304,14 @@
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._required = None
         self._required_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -479,16 +476,14 @@
             self.recipient_id_metadata = recipient_id_metadata
         if required is not None:
             self.required = required
         if required_metadata is not None:
             self.required_metadata = required_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2098,37 +2093,14 @@
         :param smart_contract_information: The smart_contract_information of this CommissionState.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this CommissionState.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this CommissionState.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this CommissionState.
-
-          # noqa: E501
-
-        :param source: The source of this CommissionState.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this CommissionState.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this CommissionState.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/company.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/company.py`

 * *Files 2% similar despite different names*

```diff
@@ -98,15 +98,14 @@
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'required': 'str',
         'required_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -201,15 +200,14 @@
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'required': 'required',
         'required_metadata': 'requiredMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -232,15 +230,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """Company - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -306,15 +304,14 @@
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._required = None
         self._required_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -479,16 +476,14 @@
             self.recipient_id_metadata = recipient_id_metadata
         if required is not None:
             self.required = required
         if required_metadata is not None:
             self.required_metadata = required_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2098,37 +2093,14 @@
         :param smart_contract_information: The smart_contract_information of this Company.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this Company.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this Company.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this Company.
-
-          # noqa: E501
-
-        :param source: The source of this Company.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this Company.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this Company.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/complete_sign_hash_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/complete_sign_hash_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/complete_sign_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/complete_sign_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/composite_template.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/composite_template.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/conditional_recipient_rule.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/conditional_recipient_rule.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/conditional_recipient_rule_condition.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/conditional_recipient_rule_condition.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/conditional_recipient_rule_filter.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/conditional_recipient_rule_filter.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/connect_config_results.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/connect_config_results.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/connect_custom_configuration.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/connect_custom_configuration.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/connect_debug_log.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/connect_debug_log.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/connect_event_data.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/connect_event_data.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/connect_failure_filter.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/connect_failure_filter.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/connect_failure_result.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/connect_failure_result.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/connect_failure_results.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/connect_failure_results.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/connect_log.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/connect_log.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/connect_logs.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/connect_logs.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/connect_salesforce_field.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/connect_salesforce_field.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/connect_salesforce_object.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/connect_salesforce_object.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/connect_user_object.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/connect_user_object.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/console_view_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/console_view_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/consumer_disclosure.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/consumer_disclosure.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/contact.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/contact.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/contact_get_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/contact_get_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/contact_mod_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/contact_mod_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/contact_phone_number.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/contact_phone_number.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/contact_update_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/contact_update_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/correct_view_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/correct_view_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/country.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/country.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/credential.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/credential.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/credit_card_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/credit_card_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/credit_card_types.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/credit_card_types.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/currency.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/currency.py`

 * *Files 0% similar despite different names*

```diff
@@ -107,15 +107,14 @@
         'require_initial_on_shared_change': 'str',
         'require_initial_on_shared_change_metadata': 'PropertyMetadata',
         'sender_required': 'str',
         'sender_required_metadata': 'PropertyMetadata',
         'shared': 'str',
         'shared_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -219,15 +218,14 @@
         'require_initial_on_shared_change': 'requireInitialOnSharedChange',
         'require_initial_on_shared_change_metadata': 'requireInitialOnSharedChangeMetadata',
         'sender_required': 'senderRequired',
         'sender_required_metadata': 'senderRequiredMetadata',
         'shared': 'shared',
         'shared_metadata': 'sharedMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -250,15 +248,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, numerical_value=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, numerical_value=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """Currency - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -333,15 +331,14 @@
         self._require_initial_on_shared_change = None
         self._require_initial_on_shared_change_metadata = None
         self._sender_required = None
         self._sender_required_metadata = None
         self._shared = None
         self._shared_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -524,16 +521,14 @@
             self.sender_required_metadata = sender_required_metadata
         if shared is not None:
             self.shared = shared
         if shared_metadata is not None:
             self.shared_metadata = shared_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2342,37 +2337,14 @@
         :param smart_contract_information: The smart_contract_information of this Currency.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this Currency.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this Currency.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this Currency.
-
-          # noqa: E501
-
-        :param source: The source of this Currency.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this Currency.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this Currency.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/currency_feature_set_price.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/currency_feature_set_price.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/currency_plan_price.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/currency_plan_price.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/custom_field.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/custom_field.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/custom_field_v2.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/custom_field_v2.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/custom_fields.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/custom_fields.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/custom_fields_envelope.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/custom_fields_envelope.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/custom_settings_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/custom_settings_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/date.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/date.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/date_signed.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/date_signed.py`

 * *Files 0% similar despite different names*

```diff
@@ -86,15 +86,14 @@
         'page_number': 'str',
         'page_number_metadata': 'PropertyMetadata',
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -177,15 +176,14 @@
         'page_number': 'pageNumber',
         'page_number_metadata': 'pageNumberMetadata',
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -208,15 +206,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """DateSigned - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -270,15 +268,14 @@
         self._page_number = None
         self._page_number_metadata = None
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -419,16 +416,14 @@
             self.recipient_id_guid = recipient_id_guid
         if recipient_id_guid_metadata is not None:
             self.recipient_id_guid_metadata = recipient_id_guid_metadata
         if recipient_id_metadata is not None:
             self.recipient_id_metadata = recipient_id_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1774,37 +1769,14 @@
         :param smart_contract_information: The smart_contract_information of this DateSigned.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this DateSigned.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this DateSigned.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this DateSigned.
-
-          # noqa: E501
-
-        :param source: The source of this DateSigned.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this DateSigned.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this DateSigned.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/date_stamp_properties.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/date_stamp_properties.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/decline.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/decline.py`

 * *Files 1% similar despite different names*

```diff
@@ -88,15 +88,14 @@
         'page_number': 'str',
         'page_number_metadata': 'PropertyMetadata',
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -179,15 +178,14 @@
         'page_number': 'pageNumber',
         'page_number_metadata': 'pageNumberMetadata',
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -208,15 +206,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, button_text=None, button_text_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, decline_reason=None, decline_reason_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, button_text=None, button_text_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, decline_reason=None, decline_reason_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """Decline - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -272,15 +270,14 @@
         self._page_number = None
         self._page_number_metadata = None
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -423,16 +420,14 @@
             self.recipient_id_guid = recipient_id_guid
         if recipient_id_guid_metadata is not None:
             self.recipient_id_guid_metadata = recipient_id_guid_metadata
         if recipient_id_metadata is not None:
             self.recipient_id_metadata = recipient_id_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1818,37 +1813,14 @@
         :param smart_contract_information: The smart_contract_information of this Decline.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this Decline.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this Decline.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this Decline.
-
-          # noqa: E501
-
-        :param source: The source of this Decline.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this Decline.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this Decline.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/diagnostics_settings_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/diagnostics_settings_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/direct_debit_processor_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/direct_debit_processor_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/display_appliance_account.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_account.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/display_appliance_custom_field.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_custom_field.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/display_appliance_document.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_document.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/display_appliance_document_page.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_document_page.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/display_appliance_envelope.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_envelope.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/display_appliance_info.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_info.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/display_appliance_page.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_page.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/display_appliance_pdf.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_pdf.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/display_appliance_recipient.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_recipient.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/display_appliance_signer_attachment.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/display_appliance_signer_attachment.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/dob_information_input.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/dob_information_input.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/document.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/document.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/document_fields_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/document_fields_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/document_html_collapsible_display_settings.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/document_html_collapsible_display_settings.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/document_html_definition.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/document_html_definition.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/document_html_definition_original.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/document_html_definition_original.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/document_html_definition_originals.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/document_html_definition_originals.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/document_html_definitions.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/document_html_definitions.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/document_html_display_anchor.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/document_html_display_anchor.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/document_html_display_settings.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/document_html_display_settings.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/document_security_store.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/document_security_store.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/document_template.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/document_template.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/document_template_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/document_template_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/document_update_info.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/document_update_info.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/document_visibility.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/document_visibility.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/document_visibility_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/document_visibility_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/downgrad_request_billing_info_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/downgrad_request_billing_info_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/downgrade_billing_plan_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/downgrade_billing_plan_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/downgrade_plan_update_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/downgrade_plan_update_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/draw.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/draw.py`

 * *Files 2% similar despite different names*

```diff
@@ -80,15 +80,14 @@
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'required': 'str',
         'required_metadata': 'PropertyMetadata',
         'shared': 'str',
         'shared_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label_metadata': 'PropertyMetadata',
@@ -161,15 +160,14 @@
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'required': 'required',
         'required_metadata': 'requiredMetadata',
         'shared': 'shared',
         'shared_metadata': 'sharedMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label_metadata': 'tabLabelMetadata',
@@ -188,15 +186,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, allow_signer_upload=None, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, locked=None, locked_metadata=None, merge_field=None, merge_field_xml=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, use_background_as_canvas=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, allow_signer_upload=None, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, locked=None, locked_metadata=None, merge_field=None, merge_field_xml=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, use_background_as_canvas=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """Draw - a model defined in Swagger"""  # noqa: E501
 
         self._allow_signer_upload = None
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
@@ -244,15 +242,14 @@
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._required = None
         self._required_metadata = None
         self._shared = None
         self._shared_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label_metadata = None
@@ -377,16 +374,14 @@
             self.required_metadata = required_metadata
         if shared is not None:
             self.shared = shared
         if shared_metadata is not None:
             self.shared_metadata = shared_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1594,37 +1589,14 @@
         :param smart_contract_information: The smart_contract_information of this Draw.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this Draw.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this Draw.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this Draw.
-
-          # noqa: E501
-
-        :param source: The source of this Draw.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this Draw.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this Draw.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/e_note_configuration.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/e_note_configuration.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/editor.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/editor.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/email.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/email.py`

 * *Files 1% similar despite different names*

```diff
@@ -106,15 +106,14 @@
         'require_initial_on_shared_change': 'str',
         'require_initial_on_shared_change_metadata': 'PropertyMetadata',
         'sender_required': 'str',
         'sender_required_metadata': 'PropertyMetadata',
         'shared': 'str',
         'shared_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -221,15 +220,14 @@
         'require_initial_on_shared_change': 'requireInitialOnSharedChange',
         'require_initial_on_shared_change_metadata': 'requireInitialOnSharedChangeMetadata',
         'sender_required': 'senderRequired',
         'sender_required_metadata': 'senderRequiredMetadata',
         'shared': 'shared',
         'shared_metadata': 'sharedMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -256,15 +254,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, validation_message=None, validation_message_metadata=None, validation_pattern=None, validation_pattern_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, validation_message=None, validation_message_metadata=None, validation_pattern=None, validation_pattern_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """Email - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -338,15 +336,14 @@
         self._require_initial_on_shared_change = None
         self._require_initial_on_shared_change_metadata = None
         self._sender_required = None
         self._sender_required_metadata = None
         self._shared = None
         self._shared_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -531,16 +528,14 @@
             self.sender_required_metadata = sender_required_metadata
         if shared is not None:
             self.shared = shared
         if shared_metadata is not None:
             self.shared_metadata = shared_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2334,37 +2329,14 @@
         :param smart_contract_information: The smart_contract_information of this Email.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this Email.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this Email.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this Email.
-
-          # noqa: E501
-
-        :param source: The source of this Email.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this Email.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this Email.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/email_address.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/email_address.py`

 * *Files 2% similar despite different names*

```diff
@@ -86,15 +86,14 @@
         'page_number': 'str',
         'page_number_metadata': 'PropertyMetadata',
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -177,15 +176,14 @@
         'page_number': 'pageNumber',
         'page_number_metadata': 'pageNumberMetadata',
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -208,15 +206,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """EmailAddress - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -270,15 +268,14 @@
         self._page_number = None
         self._page_number_metadata = None
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -419,16 +416,14 @@
             self.recipient_id_guid = recipient_id_guid
         if recipient_id_guid_metadata is not None:
             self.recipient_id_guid_metadata = recipient_id_guid_metadata
         if recipient_id_metadata is not None:
             self.recipient_id_metadata = recipient_id_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1774,37 +1769,14 @@
         :param smart_contract_information: The smart_contract_information of this EmailAddress.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this EmailAddress.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this EmailAddress.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this EmailAddress.
-
-          # noqa: E501
-
-        :param source: The source of this EmailAddress.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this EmailAddress.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this EmailAddress.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/email_settings.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/email_settings.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_attachment.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_attachment.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_attachments_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_attachments_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_attachments_result.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_attachments_result.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_audit_event.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_audit_event.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_audit_event_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_audit_event_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_definition.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_definition.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_document.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_document.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_documents_result.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_documents_result.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_event.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_event.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_form_data.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_form_data.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_id.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_id.py`

 * *Files 1% similar despite different names*

```diff
@@ -86,15 +86,14 @@
         'page_number': 'str',
         'page_number_metadata': 'PropertyMetadata',
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -175,15 +174,14 @@
         'page_number': 'pageNumber',
         'page_number_metadata': 'pageNumberMetadata',
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -204,15 +202,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """EnvelopeId - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -266,15 +264,14 @@
         self._page_number = None
         self._page_number_metadata = None
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -413,16 +410,14 @@
             self.recipient_id_guid = recipient_id_guid
         if recipient_id_guid_metadata is not None:
             self.recipient_id_guid_metadata = recipient_id_guid_metadata
         if recipient_id_metadata is not None:
             self.recipient_id_metadata = recipient_id_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1764,37 +1759,14 @@
         :param smart_contract_information: The smart_contract_information of this EnvelopeId.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this EnvelopeId.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this EnvelopeId.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this EnvelopeId.
-
-          # noqa: E501
-
-        :param source: The source of this EnvelopeId.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this EnvelopeId.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this EnvelopeId.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_ids_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_ids_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_metadata.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_metadata.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_notification_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_notification_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_purge_configuration.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_purge_configuration.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_summary.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_summary.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_template.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_template.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_template_definition.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_template_definition.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_template_result.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_template_result.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_template_results.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_template_results.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_transaction_status.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_transaction_status.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_transfer_rule.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_transfer_rule.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_transfer_rule_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_transfer_rule_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_transfer_rule_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_transfer_rule_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelope_update_summary.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelope_update_summary.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/envelopes_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/envelopes_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/error_details.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/error_details.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/event_notification.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/event_notification.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/event_result.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/event_result.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/expirations.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/expirations.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/external_claim.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/external_claim.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/external_doc_service_error_details.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/external_doc_service_error_details.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/external_document_sources.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/external_document_sources.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/external_file.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/external_file.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/external_folder.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/external_folder.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/favorite_templates_content_item.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/favorite_templates_content_item.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/favorite_templates_info.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/favorite_templates_info.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/feature_available_metadata.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/feature_available_metadata.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/feature_set.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/feature_set.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/file_type.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/file_type.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/file_type_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/file_type_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/filter.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/filter.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/first_name.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/first_name.py`

 * *Files 1% similar despite different names*

```diff
@@ -86,15 +86,14 @@
         'page_number': 'str',
         'page_number_metadata': 'PropertyMetadata',
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -177,15 +176,14 @@
         'page_number': 'pageNumber',
         'page_number_metadata': 'pageNumberMetadata',
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -208,15 +206,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """FirstName - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -270,15 +268,14 @@
         self._page_number = None
         self._page_number_metadata = None
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -419,16 +416,14 @@
             self.recipient_id_guid = recipient_id_guid
         if recipient_id_guid_metadata is not None:
             self.recipient_id_guid_metadata = recipient_id_guid_metadata
         if recipient_id_metadata is not None:
             self.recipient_id_metadata = recipient_id_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1774,37 +1769,14 @@
         :param smart_contract_information: The smart_contract_information of this FirstName.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this FirstName.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this FirstName.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this FirstName.
-
-          # noqa: E501
-
-        :param source: The source of this FirstName.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this FirstName.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this FirstName.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/folder.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/folder.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/folder_item.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/folder_item.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/folder_item_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/folder_item_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/folder_item_v2.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/folder_item_v2.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/folder_items_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/folder_items_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/folder_shared_item.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/folder_shared_item.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/folders_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/folders_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/folders_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/folders_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/forgotten_password_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/forgotten_password_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/form_data_item.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/form_data_item.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/formula_tab.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/formula_tab.py`

 * *Files 1% similar despite different names*

```diff
@@ -115,15 +115,14 @@
         'round_decimal_places': 'str',
         'round_decimal_places_metadata': 'PropertyMetadata',
         'sender_required': 'str',
         'sender_required_metadata': 'PropertyMetadata',
         'shared': 'str',
         'shared_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -239,15 +238,14 @@
         'round_decimal_places': 'roundDecimalPlaces',
         'round_decimal_places_metadata': 'roundDecimalPlacesMetadata',
         'sender_required': 'senderRequired',
         'sender_required_metadata': 'senderRequiredMetadata',
         'shared': 'shared',
         'shared_metadata': 'sharedMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -274,15 +272,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, formula=None, formula_metadata=None, height=None, height_metadata=None, hidden=None, hidden_metadata=None, is_payment_amount=None, is_payment_amount_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, payment_details=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, round_decimal_places=None, round_decimal_places_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, validation_message=None, validation_message_metadata=None, validation_pattern=None, validation_pattern_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, formula=None, formula_metadata=None, height=None, height_metadata=None, hidden=None, hidden_metadata=None, is_payment_amount=None, is_payment_amount_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, payment_details=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, round_decimal_places=None, round_decimal_places_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, validation_message=None, validation_message_metadata=None, validation_pattern=None, validation_pattern_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """FormulaTab - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -365,15 +363,14 @@
         self._round_decimal_places = None
         self._round_decimal_places_metadata = None
         self._sender_required = None
         self._sender_required_metadata = None
         self._shared = None
         self._shared_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -576,16 +573,14 @@
             self.sender_required_metadata = sender_required_metadata
         if shared is not None:
             self.shared = shared
         if shared_metadata is not None:
             self.shared_metadata = shared_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2576,37 +2571,14 @@
         :param smart_contract_information: The smart_contract_information of this FormulaTab.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this FormulaTab.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this FormulaTab.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this FormulaTab.
-
-          # noqa: E501
-
-        :param source: The source of this FormulaTab.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this FormulaTab.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this FormulaTab.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/full_name.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/full_name.py`

 * *Files 0% similar despite different names*

```diff
@@ -86,15 +86,14 @@
         'page_number': 'str',
         'page_number_metadata': 'PropertyMetadata',
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -177,15 +176,14 @@
         'page_number': 'pageNumber',
         'page_number_metadata': 'pageNumberMetadata',
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -208,15 +206,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """FullName - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -270,15 +268,14 @@
         self._page_number = None
         self._page_number_metadata = None
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -419,16 +416,14 @@
             self.recipient_id_guid = recipient_id_guid
         if recipient_id_guid_metadata is not None:
             self.recipient_id_guid_metadata = recipient_id_guid_metadata
         if recipient_id_metadata is not None:
             self.recipient_id_metadata = recipient_id_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1774,37 +1769,14 @@
         :param smart_contract_information: The smart_contract_information of this FullName.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this FullName.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this FullName.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this FullName.
-
-          # noqa: E501
-
-        :param source: The source of this FullName.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this FullName.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this FullName.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/graphics_context.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/graphics_context.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/group.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/group.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/group_brands.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/group_brands.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/group_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/group_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/id_check_configuration.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/id_check_configuration.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/id_check_information_input.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/id_check_information_input.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/id_check_security_step.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/id_check_security_step.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/in_person_signer.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/in_person_signer.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/initial_here.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/initial_here.py`

 * *Files 1% similar despite different names*

```diff
@@ -79,15 +79,14 @@
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'scale_value': 'str',
         'scale_value_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -159,15 +158,14 @@
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'scale_value': 'scaleValue',
         'scale_value_metadata': 'scaleValueMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -186,15 +184,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, optional=None, optional_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, scale_value=None, scale_value_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, optional=None, optional_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, scale_value=None, scale_value_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """InitialHere - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -241,15 +239,14 @@
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._scale_value = None
         self._scale_value_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -372,16 +369,14 @@
             self.recipient_id_metadata = recipient_id_metadata
         if scale_value is not None:
             self.scale_value = scale_value
         if scale_value_metadata is not None:
             self.scale_value_metadata = scale_value_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1566,37 +1561,14 @@
         :param smart_contract_information: The smart_contract_information of this InitialHere.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this InitialHere.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this InitialHere.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this InitialHere.
-
-          # noqa: E501
-
-        :param source: The source of this InitialHere.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this InitialHere.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this InitialHere.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/inline_template.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/inline_template.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/integrated_user_info_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/integrated_user_info_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/intermediary.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/intermediary.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/jurisdiction.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/jurisdiction.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/last_name.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/last_name.py`

 * *Files 0% similar despite different names*

```diff
@@ -86,15 +86,14 @@
         'page_number': 'str',
         'page_number_metadata': 'PropertyMetadata',
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -177,15 +176,14 @@
         'page_number': 'pageNumber',
         'page_number_metadata': 'pageNumberMetadata',
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -208,15 +206,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """LastName - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -270,15 +268,14 @@
         self._page_number = None
         self._page_number_metadata = None
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -419,16 +416,14 @@
             self.recipient_id_guid = recipient_id_guid
         if recipient_id_guid_metadata is not None:
             self.recipient_id_guid_metadata = recipient_id_guid_metadata
         if recipient_id_metadata is not None:
             self.recipient_id_metadata = recipient_id_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1774,37 +1769,14 @@
         :param smart_contract_information: The smart_contract_information of this LastName.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this LastName.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this LastName.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this LastName.
-
-          # noqa: E501
-
-        :param source: The source of this LastName.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this LastName.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this LastName.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/linked_external_primary_account.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/linked_external_primary_account.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/list.py`

 * *Files 1% similar despite different names*

```diff
@@ -99,15 +99,14 @@
         'require_initial_on_shared_change': 'str',
         'require_initial_on_shared_change_metadata': 'PropertyMetadata',
         'sender_required': 'str',
         'sender_required_metadata': 'PropertyMetadata',
         'shared': 'str',
         'shared_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -203,15 +202,14 @@
         'require_initial_on_shared_change': 'requireInitialOnSharedChange',
         'require_initial_on_shared_change_metadata': 'requireInitialOnSharedChangeMetadata',
         'sender_required': 'senderRequired',
         'sender_required_metadata': 'senderRequiredMetadata',
         'shared': 'shared',
         'shared_metadata': 'sharedMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -234,15 +232,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, list_items=None, list_selected_value=None, list_selected_value_metadata=None, locale_policy=None, locked=None, locked_metadata=None, merge_field=None, merge_field_xml=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, list_items=None, list_selected_value=None, list_selected_value_metadata=None, locale_policy=None, locked=None, locked_metadata=None, merge_field=None, merge_field_xml=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """List - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -309,15 +307,14 @@
         self._require_initial_on_shared_change = None
         self._require_initial_on_shared_change_metadata = None
         self._sender_required = None
         self._sender_required_metadata = None
         self._shared = None
         self._shared_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -484,16 +481,14 @@
             self.sender_required_metadata = sender_required_metadata
         if shared is not None:
             self.shared = shared
         if shared_metadata is not None:
             self.shared_metadata = shared_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2126,37 +2121,14 @@
         :param smart_contract_information: The smart_contract_information of this List.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this List.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this List.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this List.
-
-          # noqa: E501
-
-        :param source: The source of this List.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this List.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this List.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/list_custom_field.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/list_custom_field.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/list_item.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/list_item.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/locale_policy.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/locale_policy.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/locale_policy_tab.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/locale_policy_tab.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/lock_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/lock_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/lock_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/lock_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/login_account.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/login_account.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/login_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/login_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/match_box.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/match_box.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/member_group_shared_item.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/member_group_shared_item.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/member_shared_items.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/member_shared_items.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/merge_field.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/merge_field.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/mobile_notifier_configuration.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/mobile_notifier_configuration.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/mobile_notifier_configuration_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/mobile_notifier_configuration_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/model_date.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/model_date.py`

 * *Files 0% similar despite different names*

```diff
@@ -106,15 +106,14 @@
         'require_initial_on_shared_change': 'str',
         'require_initial_on_shared_change_metadata': 'PropertyMetadata',
         'sender_required': 'str',
         'sender_required_metadata': 'PropertyMetadata',
         'shared': 'str',
         'shared_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -221,15 +220,14 @@
         'require_initial_on_shared_change': 'requireInitialOnSharedChange',
         'require_initial_on_shared_change_metadata': 'requireInitialOnSharedChangeMetadata',
         'sender_required': 'senderRequired',
         'sender_required_metadata': 'senderRequiredMetadata',
         'shared': 'shared',
         'shared_metadata': 'sharedMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -256,15 +254,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, validation_message=None, validation_message_metadata=None, validation_pattern=None, validation_pattern_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, validation_message=None, validation_message_metadata=None, validation_pattern=None, validation_pattern_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """ModelDate - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -338,15 +336,14 @@
         self._require_initial_on_shared_change = None
         self._require_initial_on_shared_change_metadata = None
         self._sender_required = None
         self._sender_required_metadata = None
         self._shared = None
         self._shared_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -531,16 +528,14 @@
             self.sender_required_metadata = sender_required_metadata
         if shared is not None:
             self.shared = shared
         if shared_metadata is not None:
             self.shared_metadata = shared_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2334,37 +2329,14 @@
         :param smart_contract_information: The smart_contract_information of this ModelDate.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this ModelDate.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this ModelDate.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this ModelDate.
-
-          # noqa: E501
-
-        :param source: The source of this ModelDate.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this ModelDate.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this ModelDate.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/money.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/money.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/name_value.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/name_value.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/new_account_definition.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/new_account_definition.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/new_account_summary.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/new_account_summary.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/new_user.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/new_user.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/new_users_definition.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/new_users_definition.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/new_users_summary.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/new_users_summary.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notarize.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notarize.py`

 * *Files 1% similar despite different names*

```diff
@@ -77,15 +77,14 @@
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'required': 'str',
         'required_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_order': 'str',
@@ -153,15 +152,14 @@
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'required': 'required',
         'required_metadata': 'requiredMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_order': 'tabOrder',
@@ -178,15 +176,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, locked=None, locked_metadata=None, merge_field=None, merge_field_xml=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, locked=None, locked_metadata=None, merge_field=None, merge_field_xml=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """Notarize - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -231,15 +229,14 @@
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._required = None
         self._required_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_order = None
@@ -356,16 +353,14 @@
             self.recipient_id_metadata = recipient_id_metadata
         if required is not None:
             self.required = required
         if required_metadata is not None:
             self.required_metadata = required_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1502,37 +1497,14 @@
         :param smart_contract_information: The smart_contract_information of this Notarize.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this Notarize.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this Notarize.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this Notarize.
-
-          # noqa: E501
-
-        :param source: The source of this Notarize.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this Notarize.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this Notarize.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notary.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notary.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notary_certificate.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notary_certificate.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notary_host.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notary_host.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notary_journal.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notary_journal.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notary_journal_credible_witness.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notary_journal_credible_witness.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notary_journal_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notary_journal_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notary_journal_meta_data.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notary_journal_meta_data.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notary_jurisdiction.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notary_jurisdiction.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notary_jurisdiction_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notary_jurisdiction_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notary_recipient.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notary_recipient.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notary_result.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notary_result.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notary_seal.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notary_seal.py`

 * *Files 0% similar despite different names*

```diff
@@ -77,15 +77,14 @@
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'scale_value': 'str',
         'scale_value_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -155,15 +154,14 @@
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'scale_value': 'scaleValue',
         'scale_value_metadata': 'scaleValueMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -182,15 +180,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, scale_value=None, scale_value_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, scale_value=None, scale_value_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """NotarySeal - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -235,15 +233,14 @@
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._scale_value = None
         self._scale_value_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -362,16 +359,14 @@
             self.recipient_id_metadata = recipient_id_metadata
         if scale_value is not None:
             self.scale_value = scale_value
         if scale_value_metadata is not None:
             self.scale_value_metadata = scale_value_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1512,37 +1507,14 @@
         :param smart_contract_information: The smart_contract_information of this NotarySeal.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this NotarySeal.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this NotarySeal.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this NotarySeal.
-
-          # noqa: E501
-
-        :param source: The source of this NotarySeal.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this NotarySeal.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this NotarySeal.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/note.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/note.py`

 * *Files 0% similar despite different names*

```diff
@@ -88,15 +88,14 @@
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'shared': 'str',
         'shared_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -181,15 +180,14 @@
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'shared': 'shared',
         'shared_metadata': 'sharedMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -212,15 +210,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """Note - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -276,15 +274,14 @@
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._shared = None
         self._shared_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -429,16 +426,14 @@
             self.recipient_id_metadata = recipient_id_metadata
         if shared is not None:
             self.shared = shared
         if shared_metadata is not None:
             self.shared_metadata = shared_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1828,37 +1823,14 @@
         :param smart_contract_information: The smart_contract_information of this Note.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this Note.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this Note.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this Note.
-
-          # noqa: E501
-
-        :param source: The source of this Note.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this Note.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this Note.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notification.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notification.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notification_default_settings.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notification_default_settings.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/notification_defaults.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/notification_defaults.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/number.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/number.py`

 * *Files 0% similar despite different names*

```diff
@@ -110,15 +110,14 @@
         'require_initial_on_shared_change': 'str',
         'require_initial_on_shared_change_metadata': 'PropertyMetadata',
         'sender_required': 'str',
         'sender_required_metadata': 'PropertyMetadata',
         'shared': 'str',
         'shared_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -229,15 +228,14 @@
         'require_initial_on_shared_change': 'requireInitialOnSharedChange',
         'require_initial_on_shared_change_metadata': 'requireInitialOnSharedChangeMetadata',
         'sender_required': 'senderRequired',
         'sender_required_metadata': 'senderRequiredMetadata',
         'shared': 'shared',
         'shared_metadata': 'sharedMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -264,15 +262,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, formula=None, formula_metadata=None, height=None, height_metadata=None, is_payment_amount=None, is_payment_amount_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, validation_message=None, validation_message_metadata=None, validation_pattern=None, validation_pattern_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, formula=None, formula_metadata=None, height=None, height_metadata=None, is_payment_amount=None, is_payment_amount_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, validation_message=None, validation_message_metadata=None, validation_pattern=None, validation_pattern_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """Number - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -350,15 +348,14 @@
         self._require_initial_on_shared_change = None
         self._require_initial_on_shared_change_metadata = None
         self._sender_required = None
         self._sender_required_metadata = None
         self._shared = None
         self._shared_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -551,16 +548,14 @@
             self.sender_required_metadata = sender_required_metadata
         if shared is not None:
             self.shared = shared
         if shared_metadata is not None:
             self.shared_metadata = shared_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2442,37 +2437,14 @@
         :param smart_contract_information: The smart_contract_information of this Number.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this Number.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this Number.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this Number.
-
-          # noqa: E501
-
-        :param source: The source of this Number.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this Number.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this Number.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/oauth_access.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/oauth_access.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/ocr_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/ocr_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/offline_attributes.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/offline_attributes.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/page.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/page.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/page_images.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/page_images.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/page_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/page_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/page_size.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/page_size.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/path_extended_element.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/path_extended_element.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/pay_pal_legacy_settings.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/pay_pal_legacy_settings.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/payment_details.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/payment_details.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/payment_gateway_account.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/payment_gateway_account.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/payment_gateway_account_setting.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/payment_gateway_account_setting.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/payment_gateway_accounts_info.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/payment_gateway_accounts_info.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/payment_line_item.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/payment_line_item.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/payment_method_with_options.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/payment_method_with_options.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/payment_processor_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/payment_processor_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/payment_signer_values.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/payment_signer_values.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/permission_profile.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/permission_profile.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/permission_profile_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/permission_profile_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/phone_number.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/phone_number.py`

 * *Files 1% similar despite different names*

```diff
@@ -98,15 +98,14 @@
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'required': 'str',
         'required_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -201,15 +200,14 @@
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'required': 'required',
         'required_metadata': 'requiredMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -232,15 +230,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """PhoneNumber - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -306,15 +304,14 @@
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._required = None
         self._required_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -479,16 +476,14 @@
             self.recipient_id_metadata = recipient_id_metadata
         if required is not None:
             self.required = required
         if required_metadata is not None:
             self.required_metadata = required_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2098,37 +2093,14 @@
         :param smart_contract_information: The smart_contract_information of this PhoneNumber.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this PhoneNumber.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this PhoneNumber.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this PhoneNumber.
-
-          # noqa: E501
-
-        :param source: The source of this PhoneNumber.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this PhoneNumber.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this PhoneNumber.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/plan_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/plan_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/poly_line.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/poly_line.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/poly_line_overlay.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/poly_line_overlay.py`

 * *Files 1% similar despite different names*

```diff
@@ -81,15 +81,14 @@
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'shared': 'str',
         'shared_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -162,15 +161,14 @@
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'shared': 'shared',
         'shared_metadata': 'sharedMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -188,15 +186,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, graphics_context=None, height=None, height_metadata=None, locked=None, locked_metadata=None, merge_field=None, merge_field_xml=None, overlay_type=None, overlay_type_metadata=None, page_number=None, page_number_metadata=None, poly_lines=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, graphics_context=None, height=None, height_metadata=None, locked=None, locked_metadata=None, merge_field=None, merge_field_xml=None, overlay_type=None, overlay_type_metadata=None, page_number=None, page_number_metadata=None, poly_lines=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """PolyLineOverlay - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -245,15 +243,14 @@
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._shared = None
         self._shared_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -379,16 +376,14 @@
             self.recipient_id_metadata = recipient_id_metadata
         if shared is not None:
             self.shared = shared
         if shared_metadata is not None:
             self.shared_metadata = shared_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1615,37 +1610,14 @@
         :param smart_contract_information: The smart_contract_information of this PolyLineOverlay.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this PolyLineOverlay.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this PolyLineOverlay.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this PolyLineOverlay.
-
-          # noqa: E501
-
-        :param source: The source of this PolyLineOverlay.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this PolyLineOverlay.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this PolyLineOverlay.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/power_form.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/power_form.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/power_form_form_data_envelope.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/power_form_form_data_envelope.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/power_form_form_data_recipient.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/power_form_form_data_recipient.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/power_form_recipient.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/power_form_recipient.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/power_form_senders_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/power_form_senders_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/power_forms_form_data_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/power_forms_form_data_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/power_forms_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/power_forms_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/power_forms_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/power_forms_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/prefill_tabs.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/prefill_tabs.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/proof_service_resource_token.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/proof_service_resource_token.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/proof_service_view_link.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/proof_service_view_link.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/property_metadata.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/property_metadata.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/province.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/province.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/provisioning_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/provisioning_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/purchased_envelopes_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/purchased_envelopes_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/radio.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/radio.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/radio_group.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/radio_group.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_additional_notification.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_additional_notification.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_attachment.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_attachment.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_domain.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_domain.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_email_notification.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_email_notification.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_event.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_event.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_form_data.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_form_data.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_group.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_group.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_identity_input_option.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_identity_input_option.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_identity_phone_number.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_identity_phone_number.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_identity_verification.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_identity_verification.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_names_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_names_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_option.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_option.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_phone_authentication.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_phone_authentication.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_phone_number.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_phone_number.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_preview_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_preview_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_proof_file.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_proof_file.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_routing.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_routing.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_rules.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_rules.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_saml_authentication.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_saml_authentication.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_signature_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_signature_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_signature_provider.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_signature_provider.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_signature_provider_options.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_signature_provider_options.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_sms_authentication.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_sms_authentication.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_update_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_update_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipient_view_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipient_view_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipients.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipients.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/recipients_update_summary.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/recipients_update_summary.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/referral_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/referral_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/reminders.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/reminders.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/report_in_product_csv_run_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_csv_run_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/report_in_product_field.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_field.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/report_in_product_get.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_get.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/report_in_product_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/report_in_product_list_item.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_list_item.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/report_in_product_run_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_run_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/report_in_product_run_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_run_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/report_in_product_run_response_row.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_run_response_row.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/report_in_product_run_response_row_fields.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_run_response_row_fields.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/report_in_product_save_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_save_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/report_in_product_sent_by_details.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/report_in_product_sent_by_details.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/resource_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/resource_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/return_url_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/return_url_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/revision.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/revision.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/saml_assertion_attribute.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/saml_assertion_attribute.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/seal.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/seal.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/seal_identifier.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/seal_identifier.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/seal_sign.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/seal_sign.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/seat_discount.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/seat_discount.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/sender.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/sender.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/sender_email_notifications.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/sender_email_notifications.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/server_template.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/server_template.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/service_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/service_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/service_version.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/service_version.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/settings_metadata.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/settings_metadata.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/shared_item.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/shared_item.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/sign_hash_document.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/sign_hash_document.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/sign_hash_session_info_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/sign_hash_session_info_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/sign_here.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/sign_here.py`

 * *Files 1% similar despite different names*

```diff
@@ -80,15 +80,14 @@
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'scale_value': 'str',
         'scale_value_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'stamp': 'Stamp',
         'stamp_type': 'str',
         'stamp_type_metadata': 'PropertyMetadata',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
@@ -164,15 +163,14 @@
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'scale_value': 'scaleValue',
         'scale_value_metadata': 'scaleValueMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'stamp': 'stamp',
         'stamp_type': 'stampType',
         'stamp_type_metadata': 'stampTypeMetadata',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
@@ -194,15 +192,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, is_seal_sign_tab=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, optional=None, optional_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, scale_value=None, scale_value_metadata=None, smart_contract_information=None, source=None, stamp=None, stamp_type=None, stamp_type_metadata=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, is_seal_sign_tab=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, optional=None, optional_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, scale_value=None, scale_value_metadata=None, smart_contract_information=None, stamp=None, stamp_type=None, stamp_type_metadata=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """SignHere - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -250,15 +248,14 @@
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._scale_value = None
         self._scale_value_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._stamp = None
         self._stamp_type = None
         self._stamp_type_metadata = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
@@ -386,16 +383,14 @@
             self.recipient_id_metadata = recipient_id_metadata
         if scale_value is not None:
             self.scale_value = scale_value
         if scale_value_metadata is not None:
             self.scale_value_metadata = scale_value_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if stamp is not None:
             self.stamp = stamp
         if stamp_type is not None:
             self.stamp_type = stamp_type
         if stamp_type_metadata is not None:
             self.stamp_type_metadata = stamp_type_metadata
         if status is not None:
@@ -1609,37 +1604,14 @@
         :param smart_contract_information: The smart_contract_information of this SignHere.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this SignHere.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this SignHere.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this SignHere.
-
-          # noqa: E501
-
-        :param source: The source of this SignHere.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def stamp(self):
         """Gets the stamp of this SignHere.  # noqa: E501
 
 
         :return: The stamp of this SignHere.  # noqa: E501
         :rtype: Stamp
         """
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/sign_session_info_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/sign_session_info_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/signature_data_info.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/signature_data_info.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/signature_group.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/signature_group.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/signature_group_def.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/signature_group_def.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/signature_properties.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/signature_properties.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/signature_provider_required_option.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/signature_provider_required_option.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/signature_type.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/signature_type.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/signature_user.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/signature_user.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/signature_user_def.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/signature_user_def.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/signer.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/signer.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/signer_attachment.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/signer_attachment.py`

 * *Files 0% similar despite different names*

```diff
@@ -79,15 +79,14 @@
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'scale_value': 'str',
         'scale_value_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -159,15 +158,14 @@
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'scale_value': 'scaleValue',
         'scale_value_metadata': 'scaleValueMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -186,15 +184,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, optional=None, optional_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, scale_value=None, scale_value_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, optional=None, optional_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, scale_value=None, scale_value_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """SignerAttachment - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -241,15 +239,14 @@
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._scale_value = None
         self._scale_value_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -372,16 +369,14 @@
             self.recipient_id_metadata = recipient_id_metadata
         if scale_value is not None:
             self.scale_value = scale_value
         if scale_value_metadata is not None:
             self.scale_value_metadata = scale_value_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1566,37 +1561,14 @@
         :param smart_contract_information: The smart_contract_information of this SignerAttachment.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this SignerAttachment.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this SignerAttachment.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this SignerAttachment.
-
-          # noqa: E501
-
-        :param source: The source of this SignerAttachment.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this SignerAttachment.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this SignerAttachment.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/signer_email_notifications.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/signer_email_notifications.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/signing_group.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/signing_group.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/signing_group_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/signing_group_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/signing_group_user.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/signing_group_user.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/signing_group_users.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/signing_group_users.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/smart_contract_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/smart_contract_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/smart_section.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/smart_section.py`

 * *Files 0% similar despite different names*

```diff
@@ -85,15 +85,14 @@
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'remove_end_anchor': 'bool',
         'remove_start_anchor': 'bool',
         'shared': 'str',
         'shared_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'start_anchor': 'str',
         'start_position': 'SmartSectionAnchorPosition',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
@@ -172,15 +171,14 @@
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'remove_end_anchor': 'removeEndAnchor',
         'remove_start_anchor': 'removeStartAnchor',
         'shared': 'shared',
         'shared_metadata': 'sharedMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'start_anchor': 'startAnchor',
         'start_position': 'startPosition',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
@@ -200,15 +198,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, case_sensitive=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, display_settings=None, document_id=None, document_id_metadata=None, end_anchor=None, end_position=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, locked=None, locked_metadata=None, merge_field=None, merge_field_xml=None, overlay_type=None, overlay_type_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, remove_end_anchor=None, remove_start_anchor=None, shared=None, shared_metadata=None, smart_contract_information=None, source=None, start_anchor=None, start_position=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, case_sensitive=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, display_settings=None, document_id=None, document_id_metadata=None, end_anchor=None, end_position=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, locked=None, locked_metadata=None, merge_field=None, merge_field_xml=None, overlay_type=None, overlay_type_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, remove_end_anchor=None, remove_start_anchor=None, shared=None, shared_metadata=None, smart_contract_information=None, start_anchor=None, start_position=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """SmartSection - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -261,15 +259,14 @@
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._remove_end_anchor = None
         self._remove_start_anchor = None
         self._shared = None
         self._shared_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._start_anchor = None
         self._start_position = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
@@ -405,16 +402,14 @@
             self.remove_start_anchor = remove_start_anchor
         if shared is not None:
             self.shared = shared
         if shared_metadata is not None:
             self.shared_metadata = shared_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if start_anchor is not None:
             self.start_anchor = start_anchor
         if start_position is not None:
             self.start_position = start_position
         if status is not None:
             self.status = status
         if status_metadata is not None:
@@ -1735,37 +1730,14 @@
         :param smart_contract_information: The smart_contract_information of this SmartSection.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this SmartSection.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this SmartSection.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this SmartSection.
-
-          # noqa: E501
-
-        :param source: The source of this SmartSection.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def start_anchor(self):
         """Gets the start_anchor of this SmartSection.  # noqa: E501
 
           # noqa: E501
 
         :return: The start_anchor of this SmartSection.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/smart_section_anchor_position.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/smart_section_anchor_position.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/smart_section_collapsible_display_settings.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/smart_section_collapsible_display_settings.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/smart_section_display_settings.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/smart_section_display_settings.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/social_account_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/social_account_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/social_authentication.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/social_authentication.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/ssn.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/ssn.py`

 * *Files 1% similar despite different names*

```diff
@@ -106,15 +106,14 @@
         'require_initial_on_shared_change': 'str',
         'require_initial_on_shared_change_metadata': 'PropertyMetadata',
         'sender_required': 'str',
         'sender_required_metadata': 'PropertyMetadata',
         'shared': 'str',
         'shared_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -221,15 +220,14 @@
         'require_initial_on_shared_change': 'requireInitialOnSharedChange',
         'require_initial_on_shared_change_metadata': 'requireInitialOnSharedChangeMetadata',
         'sender_required': 'senderRequired',
         'sender_required_metadata': 'senderRequiredMetadata',
         'shared': 'shared',
         'shared_metadata': 'sharedMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -256,15 +254,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, validation_message=None, validation_message_metadata=None, validation_pattern=None, validation_pattern_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, validation_message=None, validation_message_metadata=None, validation_pattern=None, validation_pattern_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """Ssn - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -338,15 +336,14 @@
         self._require_initial_on_shared_change = None
         self._require_initial_on_shared_change_metadata = None
         self._sender_required = None
         self._sender_required_metadata = None
         self._shared = None
         self._shared_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -531,16 +528,14 @@
             self.sender_required_metadata = sender_required_metadata
         if shared is not None:
             self.shared = shared
         if shared_metadata is not None:
             self.shared_metadata = shared_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2334,37 +2329,14 @@
         :param smart_contract_information: The smart_contract_information of this Ssn.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this Ssn.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this Ssn.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this Ssn.
-
-          # noqa: E501
-
-        :param source: The source of this Ssn.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this Ssn.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this Ssn.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/ssn4_information_input.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/ssn4_information_input.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/ssn9_information_input.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/ssn9_information_input.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/stamp.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/stamp.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/supported_languages.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/supported_languages.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/tab_account_settings.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/tab_account_settings.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/tab_group.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/tab_group.py`

 * *Files 2% similar despite different names*

```diff
@@ -81,15 +81,14 @@
         'page_number': 'str',
         'page_number_metadata': 'PropertyMetadata',
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_order': 'str',
@@ -165,15 +164,14 @@
         'page_number': 'pageNumber',
         'page_number_metadata': 'pageNumberMetadata',
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_order': 'tabOrder',
@@ -194,15 +192,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, group_label=None, group_label_metadata=None, group_rule=None, group_rule_metadata=None, height=None, height_metadata=None, maximum_allowed=None, maximum_allowed_metadata=None, merge_field=None, merge_field_xml=None, minimum_required=None, minimum_required_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_order=None, tab_order_metadata=None, tab_scope=None, tab_scope_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, validation_message=None, validation_message_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, group_label=None, group_label_metadata=None, group_rule=None, group_rule_metadata=None, height=None, height_metadata=None, maximum_allowed=None, maximum_allowed_metadata=None, merge_field=None, merge_field_xml=None, minimum_required=None, minimum_required_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_order=None, tab_order_metadata=None, tab_scope=None, tab_scope_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, validation_message=None, validation_message_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """TabGroup - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -251,15 +249,14 @@
         self._page_number = None
         self._page_number_metadata = None
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_order = None
@@ -388,16 +385,14 @@
             self.recipient_id_guid = recipient_id_guid
         if recipient_id_guid_metadata is not None:
             self.recipient_id_guid_metadata = recipient_id_guid_metadata
         if recipient_id_metadata is not None:
             self.recipient_id_metadata = recipient_id_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1630,37 +1625,14 @@
         :param smart_contract_information: The smart_contract_information of this TabGroup.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this TabGroup.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this TabGroup.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this TabGroup.
-
-          # noqa: E501
-
-        :param source: The source of this TabGroup.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this TabGroup.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this TabGroup.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/tab_metadata.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/tab_metadata.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/tab_metadata_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/tab_metadata_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/tabs.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/tabs.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/template_custom_fields.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/template_custom_fields.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/template_document_visibility_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/template_document_visibility_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/template_documents_result.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/template_documents_result.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/template_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/template_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/template_match.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/template_match.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/template_notification_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/template_notification_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/template_recipients.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/template_recipients.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/template_role.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/template_role.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/template_shared_item.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/template_shared_item.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/template_summary.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/template_summary.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/template_tabs.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/template_tabs.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/template_update_summary.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/template_update_summary.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/text.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/text.py`

 * *Files 0% similar despite different names*

```diff
@@ -110,15 +110,14 @@
         'require_initial_on_shared_change': 'str',
         'require_initial_on_shared_change_metadata': 'PropertyMetadata',
         'sender_required': 'str',
         'sender_required_metadata': 'PropertyMetadata',
         'shared': 'str',
         'shared_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -229,15 +228,14 @@
         'require_initial_on_shared_change': 'requireInitialOnSharedChange',
         'require_initial_on_shared_change_metadata': 'requireInitialOnSharedChangeMetadata',
         'sender_required': 'senderRequired',
         'sender_required_metadata': 'senderRequiredMetadata',
         'shared': 'shared',
         'shared_metadata': 'sharedMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -264,15 +262,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, formula=None, formula_metadata=None, height=None, height_metadata=None, is_payment_amount=None, is_payment_amount_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, validation_message=None, validation_message_metadata=None, validation_pattern=None, validation_pattern_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, formula=None, formula_metadata=None, height=None, height_metadata=None, is_payment_amount=None, is_payment_amount_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, validation_message=None, validation_message_metadata=None, validation_pattern=None, validation_pattern_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """Text - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -350,15 +348,14 @@
         self._require_initial_on_shared_change = None
         self._require_initial_on_shared_change_metadata = None
         self._sender_required = None
         self._sender_required_metadata = None
         self._shared = None
         self._shared_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -551,16 +548,14 @@
             self.sender_required_metadata = sender_required_metadata
         if shared is not None:
             self.shared = shared
         if shared_metadata is not None:
             self.shared_metadata = shared_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2442,37 +2437,14 @@
         :param smart_contract_information: The smart_contract_information of this Text.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this Text.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this Text.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this Text.
-
-          # noqa: E501
-
-        :param source: The source of this Text.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this Text.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this Text.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/text_custom_field.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/text_custom_field.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/time_stamp_field.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/time_stamp_field.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/title.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/title.py`

 * *Files 1% similar despite different names*

```diff
@@ -98,15 +98,14 @@
         'recipient_id': 'str',
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'required': 'str',
         'required_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -201,15 +200,14 @@
         'recipient_id': 'recipientId',
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'required': 'required',
         'required_metadata': 'requiredMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -232,15 +230,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """Title - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -306,15 +304,14 @@
         self._recipient_id = None
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._required = None
         self._required_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -479,16 +476,14 @@
             self.recipient_id_metadata = recipient_id_metadata
         if required is not None:
             self.required = required
         if required_metadata is not None:
             self.required_metadata = required_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2098,37 +2093,14 @@
         :param smart_contract_information: The smart_contract_information of this Title.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this Title.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this Title.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this Title.
-
-          # noqa: E501
-
-        :param source: The source of this Title.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this Title.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this Title.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/tsp_health_check_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/tsp_health_check_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/tsp_health_check_status_description.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/tsp_health_check_status_description.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/update_transaction_request.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/update_transaction_request.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/update_transaction_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/update_transaction_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/usage_history.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/usage_history.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user_account_management_granular_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user_account_management_granular_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user_info.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user_info.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user_info_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user_info_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user_info_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user_info_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user_information_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user_information_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user_password_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user_password_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user_password_rules.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user_password_rules.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user_profile.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user_profile.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user_settings_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user_settings_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user_shared_item.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user_shared_item.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user_signature.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user_signature.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user_signature_definition.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user_signature_definition.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user_signatures_information.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user_signatures_information.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/user_social_id_result.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/user_social_id_result.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/users_response.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/users_response.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/view.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/view.py`

 * *Files 0% similar despite different names*

```diff
@@ -89,15 +89,14 @@
         'recipient_id_guid': 'str',
         'recipient_id_guid_metadata': 'PropertyMetadata',
         'recipient_id_metadata': 'PropertyMetadata',
         'required': 'str',
         'required_metadata': 'PropertyMetadata',
         'required_read': 'str',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -181,15 +180,14 @@
         'recipient_id_guid': 'recipientIdGuid',
         'recipient_id_guid_metadata': 'recipientIdGuidMetadata',
         'recipient_id_metadata': 'recipientIdMetadata',
         'required': 'required',
         'required_metadata': 'requiredMetadata',
         'required_read': 'requiredRead',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -210,15 +208,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, button_text=None, button_text_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, required_read=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, button_text=None, button_text_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, merge_field=None, merge_field_xml=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, required=None, required_metadata=None, required_read=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """View - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -275,15 +273,14 @@
         self._recipient_id_guid = None
         self._recipient_id_guid_metadata = None
         self._recipient_id_metadata = None
         self._required = None
         self._required_metadata = None
         self._required_read = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -428,16 +425,14 @@
             self.required = required
         if required_metadata is not None:
             self.required_metadata = required_metadata
         if required_read is not None:
             self.required_read = required_read
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -1846,37 +1841,14 @@
         :param smart_contract_information: The smart_contract_information of this View.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this View.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this View.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this View.
-
-          # noqa: E501
-
-        :param source: The source of this View.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this View.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this View.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign/models/view_url.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/view_url.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/watermark.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/watermark.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/witness.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/witness.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/workflow.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/workflow.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/workflow_step.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/workflow_step.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/workspace.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/workspace.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/workspace_folder_contents.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/workspace_folder_contents.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/workspace_item.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/workspace_item.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/workspace_item_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/workspace_item_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/workspace_list.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/workspace_list.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/workspace_settings.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/workspace_settings.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/workspace_user.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/workspace_user.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/workspace_user_authorization.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/workspace_user_authorization.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/docusign_esign/models/zip.py` & `docusign-esign-3.9.0rc1/docusign_esign/models/zip.py`

 * *Files 1% similar despite different names*

```diff
@@ -106,15 +106,14 @@
         'require_initial_on_shared_change': 'str',
         'require_initial_on_shared_change_metadata': 'PropertyMetadata',
         'sender_required': 'str',
         'sender_required_metadata': 'PropertyMetadata',
         'shared': 'str',
         'shared_metadata': 'PropertyMetadata',
         'smart_contract_information': 'SmartContractInformation',
-        'source': 'str',
         'status': 'str',
         'status_metadata': 'PropertyMetadata',
         'tab_group_labels': 'list[str]',
         'tab_group_labels_metadata': 'PropertyMetadata',
         'tab_id': 'str',
         'tab_id_metadata': 'PropertyMetadata',
         'tab_label': 'str',
@@ -223,15 +222,14 @@
         'require_initial_on_shared_change': 'requireInitialOnSharedChange',
         'require_initial_on_shared_change_metadata': 'requireInitialOnSharedChangeMetadata',
         'sender_required': 'senderRequired',
         'sender_required_metadata': 'senderRequiredMetadata',
         'shared': 'shared',
         'shared_metadata': 'sharedMetadata',
         'smart_contract_information': 'smartContractInformation',
-        'source': 'source',
         'status': 'status',
         'status_metadata': 'statusMetadata',
         'tab_group_labels': 'tabGroupLabels',
         'tab_group_labels_metadata': 'tabGroupLabelsMetadata',
         'tab_id': 'tabId',
         'tab_id_metadata': 'tabIdMetadata',
         'tab_label': 'tabLabel',
@@ -260,15 +258,15 @@
         'width_metadata': 'widthMetadata',
         'x_position': 'xPosition',
         'x_position_metadata': 'xPositionMetadata',
         'y_position': 'yPosition',
         'y_position_metadata': 'yPositionMetadata'
     }
 
-    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, source=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, use_dash4=None, use_dash4_metadata=None, validation_message=None, validation_message_metadata=None, validation_pattern=None, validation_pattern_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
+    def __init__(self, anchor_allow_white_space_in_characters=None, anchor_allow_white_space_in_characters_metadata=None, anchor_case_sensitive=None, anchor_case_sensitive_metadata=None, anchor_horizontal_alignment=None, anchor_horizontal_alignment_metadata=None, anchor_ignore_if_not_present=None, anchor_ignore_if_not_present_metadata=None, anchor_match_whole_word=None, anchor_match_whole_word_metadata=None, anchor_string=None, anchor_string_metadata=None, anchor_tab_processor_version=None, anchor_tab_processor_version_metadata=None, anchor_units=None, anchor_units_metadata=None, anchor_x_offset=None, anchor_x_offset_metadata=None, anchor_y_offset=None, anchor_y_offset_metadata=None, bold=None, bold_metadata=None, conceal_value_on_document=None, conceal_value_on_document_metadata=None, conditional_parent_label=None, conditional_parent_label_metadata=None, conditional_parent_value=None, conditional_parent_value_metadata=None, custom_tab_id=None, custom_tab_id_metadata=None, disable_auto_size=None, disable_auto_size_metadata=None, document_id=None, document_id_metadata=None, error_details=None, font=None, font_color=None, font_color_metadata=None, font_metadata=None, font_size=None, font_size_metadata=None, form_order=None, form_order_metadata=None, form_page_label=None, form_page_label_metadata=None, form_page_number=None, form_page_number_metadata=None, height=None, height_metadata=None, italic=None, italic_metadata=None, locale_policy=None, locked=None, locked_metadata=None, max_length=None, max_length_metadata=None, merge_field=None, merge_field_xml=None, name=None, name_metadata=None, original_value=None, original_value_metadata=None, page_number=None, page_number_metadata=None, recipient_id=None, recipient_id_guid=None, recipient_id_guid_metadata=None, recipient_id_metadata=None, require_all=None, require_all_metadata=None, required=None, required_metadata=None, require_initial_on_shared_change=None, require_initial_on_shared_change_metadata=None, sender_required=None, sender_required_metadata=None, shared=None, shared_metadata=None, smart_contract_information=None, status=None, status_metadata=None, tab_group_labels=None, tab_group_labels_metadata=None, tab_id=None, tab_id_metadata=None, tab_label=None, tab_label_metadata=None, tab_order=None, tab_order_metadata=None, tab_type=None, tab_type_metadata=None, template_locked=None, template_locked_metadata=None, template_required=None, template_required_metadata=None, tooltip=None, tool_tip_metadata=None, underline=None, underline_metadata=None, use_dash4=None, use_dash4_metadata=None, validation_message=None, validation_message_metadata=None, validation_pattern=None, validation_pattern_metadata=None, value=None, value_metadata=None, width=None, width_metadata=None, x_position=None, x_position_metadata=None, y_position=None, y_position_metadata=None):  # noqa: E501
         """Zip - a model defined in Swagger"""  # noqa: E501
 
         self._anchor_allow_white_space_in_characters = None
         self._anchor_allow_white_space_in_characters_metadata = None
         self._anchor_case_sensitive = None
         self._anchor_case_sensitive_metadata = None
         self._anchor_horizontal_alignment = None
@@ -342,15 +340,14 @@
         self._require_initial_on_shared_change = None
         self._require_initial_on_shared_change_metadata = None
         self._sender_required = None
         self._sender_required_metadata = None
         self._shared = None
         self._shared_metadata = None
         self._smart_contract_information = None
-        self._source = None
         self._status = None
         self._status_metadata = None
         self._tab_group_labels = None
         self._tab_group_labels_metadata = None
         self._tab_id = None
         self._tab_id_metadata = None
         self._tab_label = None
@@ -537,16 +534,14 @@
             self.sender_required_metadata = sender_required_metadata
         if shared is not None:
             self.shared = shared
         if shared_metadata is not None:
             self.shared_metadata = shared_metadata
         if smart_contract_information is not None:
             self.smart_contract_information = smart_contract_information
-        if source is not None:
-            self.source = source
         if status is not None:
             self.status = status
         if status_metadata is not None:
             self.status_metadata = status_metadata
         if tab_group_labels is not None:
             self.tab_group_labels = tab_group_labels
         if tab_group_labels_metadata is not None:
@@ -2344,37 +2339,14 @@
         :param smart_contract_information: The smart_contract_information of this Zip.  # noqa: E501
         :type: SmartContractInformation
         """
 
         self._smart_contract_information = smart_contract_information
 
     @property
-    def source(self):
-        """Gets the source of this Zip.  # noqa: E501
-
-          # noqa: E501
-
-        :return: The source of this Zip.  # noqa: E501
-        :rtype: str
-        """
-        return self._source
-
-    @source.setter
-    def source(self, source):
-        """Sets the source of this Zip.
-
-          # noqa: E501
-
-        :param source: The source of this Zip.  # noqa: E501
-        :type: str
-        """
-
-        self._source = source
-
-    @property
     def status(self):
         """Gets the status of this Zip.  # noqa: E501
 
         Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501
 
         :return: The status of this Zip.  # noqa: E501
         :rtype: str
```

### Comparing `docusign-esign-3.9.0/docusign_esign.egg-info/SOURCES.txt` & `docusign-esign-3.9.0rc1/docusign_esign.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/setup.py` & `docusign-esign-3.9.0rc1/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -10,15 +10,15 @@
     Generated by: https://github.com/swagger-api/swagger-codegen.git
 """
 
 
 from setuptools import setup, find_packages, Command, os  # noqa: H301
 
 NAME = "docusign-esign"
-VERSION = "3.9.0"
+VERSION = "3.9.0rc1"
 # To install the library, run the following
 #
 # python setup.py install
 #
 # prerequisite: setuptools
 # http://pypi.python.org/pypi/setuptools
```

### Comparing `docusign-esign-3.9.0/test/test_oauth.py` & `docusign-esign-3.9.0rc1/test/test_oauth.py`

 * *Files identical despite different names*

### Comparing `docusign-esign-3.9.0/test/unit_tests.py` & `docusign-esign-3.9.0rc1/test/unit_tests.py`

 * *Files identical despite different names*

