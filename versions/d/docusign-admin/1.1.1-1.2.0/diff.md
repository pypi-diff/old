# Comparing `tmp/docusign-admin-1.1.1.tar.gz` & `tmp/docusign-admin-1.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/docusign-admin-1.1.1.tar", last modified: Tue Sep 20 05:26:53 2022, max compression
+gzip compressed data, was "dist/docusign-admin-1.2.0.tar", last modified: Fri Apr  7 14:21:42 2023, max compression
```

## Comparing `docusign-admin-1.1.1.tar` & `docusign-admin-1.2.0.tar`

### file list

```diff
@@ -1,141 +1,141 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-20 05:26:53.000000 docusign-admin-1.1.1/
--rwxr-xr-x   0 root         (0) root         (0)     1102 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/LICENSE
--rw-r--r--   0 root         (0) root         (0)     3745 2022-09-20 05:26:53.000000 docusign-admin-1.1.1/PKG-INFO
--rwxr-xr-x   0 root         (0) root         (0)     3510 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-20 05:26:53.000000 docusign-admin-1.1.1/docusign_admin/
--rw-r--r--   0 root         (0) root         (0)    10185 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-20 05:26:53.000000 docusign-admin-1.1.1/docusign_admin/apis/
--rw-r--r--   0 root         (0) root         (0)      470 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/apis/__init__.py
--rw-r--r--   0 root         (0) root         (0)    16921 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/apis/accounts_api.py
--rw-r--r--   0 root         (0) root         (0)    42743 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/apis/bulk_exports_api.py
--rw-r--r--   0 root         (0) root         (0)    76544 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/apis/bulk_imports_api.py
--rw-r--r--   0 root         (0) root         (0)    43217 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/apis/ds_groups_api.py
--rw-r--r--   0 root         (0) root         (0)     5808 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/apis/identity_providers_api.py
--rw-r--r--   0 root         (0) root         (0)    38443 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/apis/product_permission_profiles_api.py
--rw-r--r--   0 root         (0) root         (0)     5732 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/apis/reserved_domains_api.py
--rw-r--r--   0 root         (0) root         (0)    69337 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/apis/users_api.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-20 05:26:53.000000 docusign-admin-1.1.1/docusign_admin/client/
--rwxr-xr-x   0 root         (0) root         (0)      283 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/client/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    35251 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/client/api_client.py
--rwxr-xr-x   0 root         (0) root         (0)     1503 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/client/api_exception.py
--rwxr-xr-x   0 root         (0) root         (0)    11576 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/client/api_response.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-20 05:26:53.000000 docusign-admin-1.1.1/docusign_admin/client/auth/
--rwxr-xr-x   0 root         (0) root         (0)      219 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/client/auth/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    14756 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/client/auth/oauth.py
--rwxr-xr-x   0 root         (0) root         (0)     7297 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/client/configuration.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-20 05:26:53.000000 docusign-admin-1.1.1/docusign_admin/models/
--rw-r--r--   0 root         (0) root         (0)     9339 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4352 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/add_ds_group_and_users_response.py
--rw-r--r--   0 root         (0) root         (0)     5015 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/add_ds_group_users_response.py
--rw-r--r--   0 root         (0) root         (0)     9032 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/add_user_response.py
--rw-r--r--   0 root         (0) root         (0)     7737 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/add_user_response_account_properties.py
--rw-r--r--   0 root         (0) root         (0)     6904 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/certificate_response.py
--rw-r--r--   0 root         (0) root         (0)     3574 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/delete_membership_request.py
--rw-r--r--   0 root         (0) root         (0)     4239 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/delete_membership_response.py
--rw-r--r--   0 root         (0) root         (0)     3781 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/delete_memberships_request.py
--rw-r--r--   0 root         (0) root         (0)     4309 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/delete_memberships_response.py
--rw-r--r--   0 root         (0) root         (0)     4190 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/delete_response.py
--rw-r--r--   0 root         (0) root         (0)     3818 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/delete_user_identity_request.py
--rw-r--r--   0 root         (0) root         (0)     7543 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/domain_response.py
--rw-r--r--   0 root         (0) root         (0)     3646 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/domains_response.py
--rw-r--r--   0 root         (0) root         (0)     4404 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/ds_group_add_request.py
--rw-r--r--   0 root         (0) root         (0)     4304 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/ds_group_and_users_response.py
--rw-r--r--   0 root         (0) root         (0)     6307 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/ds_group_list_response.py
--rw-r--r--   0 root         (0) root         (0)     3673 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/ds_group_request.py
--rw-r--r--   0 root         (0) root         (0)    10917 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/ds_group_response.py
--rw-r--r--   0 root         (0) root         (0)     8458 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/ds_group_user_response.py
--rw-r--r--   0 root         (0) root         (0)     3703 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/ds_group_users_add_request.py
--rw-r--r--   0 root         (0) root         (0)     4333 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/ds_group_users_remove_request.py
--rw-r--r--   0 root         (0) root         (0)     5554 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/ds_group_users_response.py
--rw-r--r--   0 root         (0) root         (0)     4182 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/error_details.py
--rw-r--r--   0 root         (0) root         (0)     3737 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/force_activate_membership_request.py
--rw-r--r--   0 root         (0) root         (0)     4631 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/group_request.py
--rw-r--r--   0 root         (0) root         (0)     7202 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/identity_provider_response.py
--rw-r--r--   0 root         (0) root         (0)     3802 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/identity_providers_response.py
--rw-r--r--   0 root         (0) root         (0)     3912 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/link_response.py
--rw-r--r--   0 root         (0) root         (0)     4591 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/member_group_response.py
--rw-r--r--   0 root         (0) root         (0)     4235 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/member_groups_response.py
--rw-r--r--   0 root         (0) root         (0)    10291 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/membership_response.py
--rw-r--r--   0 root         (0) root         (0)    12497 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/new_account_user_request.py
--rw-r--r--   0 root         (0) root         (0)    12493 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/new_multi_product_user_add_request.py
--rw-r--r--   0 root         (0) root         (0)    11489 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/new_user_request.py
--rw-r--r--   0 root         (0) root         (0)     6892 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/new_user_request_account_properties.py
--rw-r--r--   0 root         (0) root         (0)     9032 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/new_user_response.py
--rw-r--r--   0 root         (0) root         (0)     7494 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/new_user_response_account_properties.py
--rw-r--r--   0 root         (0) root         (0)     4260 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/oasirr_error_details.py
--rw-r--r--   0 root         (0) root         (0)     7100 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/oasirr_organization_account_settings_error_data_response.py
--rw-r--r--   0 root         (0) root         (0)     4234 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/oetr_error_details.py
--rw-r--r--   0 root         (0) root         (0)     3568 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/org_export_selected_account.py
--rw-r--r--   0 root         (0) root         (0)     3487 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/org_export_selected_domain.py
--rw-r--r--   0 root         (0) root         (0)     5792 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/org_report_configuration_response.py
--rw-r--r--   0 root         (0) root         (0)     3757 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/org_report_create_response.py
--rw-r--r--   0 root         (0) root         (0)     3586 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/org_report_list_response.py
--rw-r--r--   0 root         (0) root         (0)    12629 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/org_report_list_response_org_report.py
--rw-r--r--   0 root         (0) root         (0)     4128 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/org_report_list_response_requestor.py
--rw-r--r--   0 root         (0) root         (0)     6730 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/org_report_request.py
--rw-r--r--   0 root         (0) root         (0)     3761 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_account_request.py
--rw-r--r--   0 root         (0) root         (0)     5689 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_account_response.py
--rw-r--r--   0 root         (0) root         (0)     5866 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_account_settings_import_requestor_response.py
--rw-r--r--   0 root         (0) root         (0)    15930 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_account_settings_import_response.py
--rw-r--r--   0 root         (0) root         (0)     9565 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_account_settings_import_result_response.py
--rw-r--r--   0 root         (0) root         (0)     3646 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_accounts_request.py
--rw-r--r--   0 root         (0) root         (0)     3577 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_export_account.py
--rw-r--r--   0 root         (0) root         (0)     3496 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_export_domain.py
--rw-r--r--   0 root         (0) root         (0)     5020 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_export_request.py
--rw-r--r--   0 root         (0) root         (0)     5551 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_export_requestor_response.py
--rw-r--r--   0 root         (0) root         (0)    15025 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_export_response.py
--rw-r--r--   0 root         (0) root         (0)     7199 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_export_task_response.py
--rw-r--r--   0 root         (0) root         (0)     3628 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_exports_response.py
--rw-r--r--   0 root         (0) root         (0)    26879 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_import_response.py
--rw-r--r--   0 root         (0) root         (0)     4381 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_import_response_error_rollup.py
--rw-r--r--   0 root         (0) root         (0)     5551 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_import_response_requestor.py
--rw-r--r--   0 root         (0) root         (0)     4443 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_import_response_warning_rollup.py
--rw-r--r--   0 root         (0) root         (0)     3628 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_imports_response.py
--rw-r--r--   0 root         (0) root         (0)    13757 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_response.py
--rw-r--r--   0 root         (0) root         (0)     8315 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_salesforce_account_managers_response.py
--rw-r--r--   0 root         (0) root         (0)     3442 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_simple_id_object.py
--rw-r--r--   0 root         (0) root         (0)    11100 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_user_response.py
--rw-r--r--   0 root         (0) root         (0)     4297 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organization_users_response.py
--rw-r--r--   0 root         (0) root         (0)     3664 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/organizations_response.py
--rw-r--r--   0 root         (0) root         (0)     4544 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/osamr_contact.py
--rw-r--r--   0 root         (0) root         (0)     7760 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/paging_response_properties.py
--rw-r--r--   0 root         (0) root         (0)     4209 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/permission_profile_request.py
--rw-r--r--   0 root         (0) root         (0)     4063 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/permission_profile_response.py
--rw-r--r--   0 root         (0) root         (0)     4773 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/permission_profile_response21.py
--rw-r--r--   0 root         (0) root         (0)     3625 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/permissions_response.py
--rw-r--r--   0 root         (0) root         (0)     4963 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/product_permission_profile_request.py
--rw-r--r--   0 root         (0) root         (0)     6280 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/product_permission_profile_response.py
--rw-r--r--   0 root         (0) root         (0)     4257 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/product_permission_profiles_request.py
--rw-r--r--   0 root         (0) root         (0)     4060 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/product_permission_profiles_response.py
--rw-r--r--   0 root         (0) root         (0)     4433 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/remove_ds_group_users_response.py
--rw-r--r--   0 root         (0) root         (0)     6344 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/remove_user_products_response.py
--rw-r--r--   0 root         (0) root         (0)     7036 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/required_attribute_mapping_response.py
--rw-r--r--   0 root         (0) root         (0)     6172 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/saml2_identity_provider_response.py
--rw-r--r--   0 root         (0) root         (0)     4568 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/setting_response.py
--rw-r--r--   0 root         (0) root         (0)     8423 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/update_membership_request.py
--rw-r--r--   0 root         (0) root         (0)     3406 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/update_response.py
--rw-r--r--   0 root         (0) root         (0)     5207 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/update_user_email_request.py
--rw-r--r--   0 root         (0) root         (0)    13091 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/update_user_request.py
--rw-r--r--   0 root         (0) root         (0)     3544 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/update_users_email_request.py
--rw-r--r--   0 root         (0) root         (0)     3484 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/update_users_request.py
--rw-r--r--   0 root         (0) root         (0)    16955 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/user_drilldown_response.py
--rw-r--r--   0 root         (0) root         (0)     3379 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/user_identity_request.py
--rw-r--r--   0 root         (0) root         (0)     6341 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/user_identity_response.py
--rw-r--r--   0 root         (0) root         (0)     5150 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/user_product_permission_profiles_request.py
--rw-r--r--   0 root         (0) root         (0)     5614 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/user_product_permission_profiles_response.py
--rw-r--r--   0 root         (0) root         (0)     5314 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/user_product_profile_delete_request.py
--rw-r--r--   0 root         (0) root         (0)     5437 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/user_update_response.py
--rw-r--r--   0 root         (0) root         (0)     3532 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/users_drilldown_response.py
--rw-r--r--   0 root         (0) root         (0)     4159 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/docusign_admin/models/users_update_response.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-20 05:26:53.000000 docusign-admin-1.1.1/docusign_admin.egg-info/
--rw-r--r--   0 root         (0) root         (0)     3745 2022-09-20 05:26:52.000000 docusign-admin-1.1.1/docusign_admin.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     6393 2022-09-20 05:26:53.000000 docusign-admin-1.1.1/docusign_admin.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-09-20 05:26:52.000000 docusign-admin-1.1.1/docusign_admin.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      131 2022-09-20 05:26:53.000000 docusign-admin-1.1.1/docusign_admin.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       20 2022-09-20 05:26:53.000000 docusign-admin-1.1.1/docusign_admin.egg-info/top_level.txt
--rwxr-xr-x   0 root         (0) root         (0)       79 2022-09-20 05:26:53.000000 docusign-admin-1.1.1/setup.cfg
--rwxr-xr-x   0 root         (0) root         (0)     1618 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-20 05:26:53.000000 docusign-admin-1.1.1/test/
--rwxr-xr-x   0 root         (0) root         (0)        0 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/test/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     4772 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/test/test_oauth.py
--rwxr-xr-x   0 root         (0) root         (0)     6356 2022-09-20 05:26:50.000000 docusign-admin-1.1.1/test/unit_tests.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:21:42.000000 docusign-admin-1.2.0/
+-rwxr-xr-x   0 root         (0) root         (0)     1102 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     3742 2023-04-07 14:21:42.000000 docusign-admin-1.2.0/PKG-INFO
+-rwxr-xr-x   0 root         (0) root         (0)     3507 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:21:42.000000 docusign-admin-1.2.0/docusign_admin/
+-rw-r--r--   0 root         (0) root         (0)    10185 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:21:42.000000 docusign-admin-1.2.0/docusign_admin/apis/
+-rw-r--r--   0 root         (0) root         (0)      470 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/apis/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    16921 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/apis/accounts_api.py
+-rw-r--r--   0 root         (0) root         (0)    42743 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/apis/bulk_exports_api.py
+-rw-r--r--   0 root         (0) root         (0)    77072 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/apis/bulk_imports_api.py
+-rw-r--r--   0 root         (0) root         (0)    43217 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/apis/ds_groups_api.py
+-rw-r--r--   0 root         (0) root         (0)     5808 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/apis/identity_providers_api.py
+-rw-r--r--   0 root         (0) root         (0)    38443 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/apis/product_permission_profiles_api.py
+-rw-r--r--   0 root         (0) root         (0)     5732 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/apis/reserved_domains_api.py
+-rw-r--r--   0 root         (0) root         (0)    69337 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/apis/users_api.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:21:42.000000 docusign-admin-1.2.0/docusign_admin/client/
+-rwxr-xr-x   0 root         (0) root         (0)      283 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/client/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    35251 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/client/api_client.py
+-rwxr-xr-x   0 root         (0) root         (0)     1503 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/client/api_exception.py
+-rwxr-xr-x   0 root         (0) root         (0)    11576 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/client/api_response.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:21:42.000000 docusign-admin-1.2.0/docusign_admin/client/auth/
+-rwxr-xr-x   0 root         (0) root         (0)      219 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/client/auth/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    14756 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/client/auth/oauth.py
+-rwxr-xr-x   0 root         (0) root         (0)     7297 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/client/configuration.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:21:42.000000 docusign-admin-1.2.0/docusign_admin/models/
+-rw-r--r--   0 root         (0) root         (0)     9339 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4352 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/add_ds_group_and_users_response.py
+-rw-r--r--   0 root         (0) root         (0)     5015 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/add_ds_group_users_response.py
+-rw-r--r--   0 root         (0) root         (0)     9032 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/add_user_response.py
+-rw-r--r--   0 root         (0) root         (0)     7737 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/add_user_response_account_properties.py
+-rw-r--r--   0 root         (0) root         (0)     6904 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/certificate_response.py
+-rw-r--r--   0 root         (0) root         (0)     3574 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/delete_membership_request.py
+-rw-r--r--   0 root         (0) root         (0)     4239 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/delete_membership_response.py
+-rw-r--r--   0 root         (0) root         (0)     3781 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/delete_memberships_request.py
+-rw-r--r--   0 root         (0) root         (0)     4309 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/delete_memberships_response.py
+-rw-r--r--   0 root         (0) root         (0)     4190 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/delete_response.py
+-rw-r--r--   0 root         (0) root         (0)     3818 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/delete_user_identity_request.py
+-rw-r--r--   0 root         (0) root         (0)     7543 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/domain_response.py
+-rw-r--r--   0 root         (0) root         (0)     3646 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/domains_response.py
+-rw-r--r--   0 root         (0) root         (0)     4404 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/ds_group_add_request.py
+-rw-r--r--   0 root         (0) root         (0)     4304 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/ds_group_and_users_response.py
+-rw-r--r--   0 root         (0) root         (0)     6307 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/ds_group_list_response.py
+-rw-r--r--   0 root         (0) root         (0)     3673 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/ds_group_request.py
+-rw-r--r--   0 root         (0) root         (0)    10917 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/ds_group_response.py
+-rw-r--r--   0 root         (0) root         (0)     8458 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/ds_group_user_response.py
+-rw-r--r--   0 root         (0) root         (0)     3703 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/ds_group_users_add_request.py
+-rw-r--r--   0 root         (0) root         (0)     4333 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/ds_group_users_remove_request.py
+-rw-r--r--   0 root         (0) root         (0)     5554 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/ds_group_users_response.py
+-rw-r--r--   0 root         (0) root         (0)     4182 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/error_details.py
+-rw-r--r--   0 root         (0) root         (0)     3737 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/force_activate_membership_request.py
+-rw-r--r--   0 root         (0) root         (0)     4631 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/group_request.py
+-rw-r--r--   0 root         (0) root         (0)     7202 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/identity_provider_response.py
+-rw-r--r--   0 root         (0) root         (0)     3802 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/identity_providers_response.py
+-rw-r--r--   0 root         (0) root         (0)     3912 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/link_response.py
+-rw-r--r--   0 root         (0) root         (0)     4591 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/member_group_response.py
+-rw-r--r--   0 root         (0) root         (0)     4235 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/member_groups_response.py
+-rw-r--r--   0 root         (0) root         (0)    10291 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/membership_response.py
+-rw-r--r--   0 root         (0) root         (0)    12497 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/new_account_user_request.py
+-rw-r--r--   0 root         (0) root         (0)    12493 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/new_multi_product_user_add_request.py
+-rw-r--r--   0 root         (0) root         (0)    11489 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/new_user_request.py
+-rw-r--r--   0 root         (0) root         (0)     6892 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/new_user_request_account_properties.py
+-rw-r--r--   0 root         (0) root         (0)     9032 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/new_user_response.py
+-rw-r--r--   0 root         (0) root         (0)     7494 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/new_user_response_account_properties.py
+-rw-r--r--   0 root         (0) root         (0)     4260 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/oasirr_error_details.py
+-rw-r--r--   0 root         (0) root         (0)     7100 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/oasirr_organization_account_settings_error_data_response.py
+-rw-r--r--   0 root         (0) root         (0)     4234 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/oetr_error_details.py
+-rw-r--r--   0 root         (0) root         (0)     3568 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/org_export_selected_account.py
+-rw-r--r--   0 root         (0) root         (0)     3487 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/org_export_selected_domain.py
+-rw-r--r--   0 root         (0) root         (0)     5792 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/org_report_configuration_response.py
+-rw-r--r--   0 root         (0) root         (0)     3757 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/org_report_create_response.py
+-rw-r--r--   0 root         (0) root         (0)     3586 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/org_report_list_response.py
+-rw-r--r--   0 root         (0) root         (0)    12629 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/org_report_list_response_org_report.py
+-rw-r--r--   0 root         (0) root         (0)     4128 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/org_report_list_response_requestor.py
+-rw-r--r--   0 root         (0) root         (0)     6730 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/org_report_request.py
+-rw-r--r--   0 root         (0) root         (0)     3761 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_account_request.py
+-rw-r--r--   0 root         (0) root         (0)     5689 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_account_response.py
+-rw-r--r--   0 root         (0) root         (0)     5866 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_account_settings_import_requestor_response.py
+-rw-r--r--   0 root         (0) root         (0)    15930 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_account_settings_import_response.py
+-rw-r--r--   0 root         (0) root         (0)     9565 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_account_settings_import_result_response.py
+-rw-r--r--   0 root         (0) root         (0)     3646 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_accounts_request.py
+-rw-r--r--   0 root         (0) root         (0)     3577 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_export_account.py
+-rw-r--r--   0 root         (0) root         (0)     3496 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_export_domain.py
+-rw-r--r--   0 root         (0) root         (0)     5020 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_export_request.py
+-rw-r--r--   0 root         (0) root         (0)     5551 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_export_requestor_response.py
+-rw-r--r--   0 root         (0) root         (0)    15025 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_export_response.py
+-rw-r--r--   0 root         (0) root         (0)     7199 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_export_task_response.py
+-rw-r--r--   0 root         (0) root         (0)     3628 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_exports_response.py
+-rw-r--r--   0 root         (0) root         (0)    26879 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_import_response.py
+-rw-r--r--   0 root         (0) root         (0)     4381 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_import_response_error_rollup.py
+-rw-r--r--   0 root         (0) root         (0)     5551 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_import_response_requestor.py
+-rw-r--r--   0 root         (0) root         (0)     4443 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_import_response_warning_rollup.py
+-rw-r--r--   0 root         (0) root         (0)     3628 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_imports_response.py
+-rw-r--r--   0 root         (0) root         (0)    13757 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_response.py
+-rw-r--r--   0 root         (0) root         (0)     8315 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_salesforce_account_managers_response.py
+-rw-r--r--   0 root         (0) root         (0)     3442 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_simple_id_object.py
+-rw-r--r--   0 root         (0) root         (0)    11100 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_user_response.py
+-rw-r--r--   0 root         (0) root         (0)     4297 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organization_users_response.py
+-rw-r--r--   0 root         (0) root         (0)     3664 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/organizations_response.py
+-rw-r--r--   0 root         (0) root         (0)     4544 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/osamr_contact.py
+-rw-r--r--   0 root         (0) root         (0)     7760 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/paging_response_properties.py
+-rw-r--r--   0 root         (0) root         (0)     4209 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/permission_profile_request.py
+-rw-r--r--   0 root         (0) root         (0)     4063 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/permission_profile_response.py
+-rw-r--r--   0 root         (0) root         (0)     4773 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/permission_profile_response21.py
+-rw-r--r--   0 root         (0) root         (0)     3625 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/permissions_response.py
+-rw-r--r--   0 root         (0) root         (0)     4963 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/product_permission_profile_request.py
+-rw-r--r--   0 root         (0) root         (0)     6280 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/product_permission_profile_response.py
+-rw-r--r--   0 root         (0) root         (0)     4257 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/product_permission_profiles_request.py
+-rw-r--r--   0 root         (0) root         (0)     4060 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/product_permission_profiles_response.py
+-rw-r--r--   0 root         (0) root         (0)     4433 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/remove_ds_group_users_response.py
+-rw-r--r--   0 root         (0) root         (0)     6344 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/remove_user_products_response.py
+-rw-r--r--   0 root         (0) root         (0)     7036 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/required_attribute_mapping_response.py
+-rw-r--r--   0 root         (0) root         (0)     6172 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/saml2_identity_provider_response.py
+-rw-r--r--   0 root         (0) root         (0)     4568 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/setting_response.py
+-rw-r--r--   0 root         (0) root         (0)     8423 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/update_membership_request.py
+-rw-r--r--   0 root         (0) root         (0)     3406 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/update_response.py
+-rw-r--r--   0 root         (0) root         (0)     5207 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/update_user_email_request.py
+-rw-r--r--   0 root         (0) root         (0)    13091 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/update_user_request.py
+-rw-r--r--   0 root         (0) root         (0)     3544 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/update_users_email_request.py
+-rw-r--r--   0 root         (0) root         (0)     3484 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/update_users_request.py
+-rw-r--r--   0 root         (0) root         (0)    16955 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/user_drilldown_response.py
+-rw-r--r--   0 root         (0) root         (0)     3379 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/user_identity_request.py
+-rw-r--r--   0 root         (0) root         (0)     6341 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/user_identity_response.py
+-rw-r--r--   0 root         (0) root         (0)     5150 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/user_product_permission_profiles_request.py
+-rw-r--r--   0 root         (0) root         (0)     5614 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/user_product_permission_profiles_response.py
+-rw-r--r--   0 root         (0) root         (0)     5314 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/user_product_profile_delete_request.py
+-rw-r--r--   0 root         (0) root         (0)     5437 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/user_update_response.py
+-rw-r--r--   0 root         (0) root         (0)     3532 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/users_drilldown_response.py
+-rw-r--r--   0 root         (0) root         (0)     4159 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/docusign_admin/models/users_update_response.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:21:42.000000 docusign-admin-1.2.0/docusign_admin.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     3742 2023-04-07 14:21:41.000000 docusign-admin-1.2.0/docusign_admin.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     6393 2023-04-07 14:21:42.000000 docusign-admin-1.2.0/docusign_admin.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 14:21:41.000000 docusign-admin-1.2.0/docusign_admin.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      128 2023-04-07 14:21:42.000000 docusign-admin-1.2.0/docusign_admin.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       20 2023-04-07 14:21:42.000000 docusign-admin-1.2.0/docusign_admin.egg-info/top_level.txt
+-rwxr-xr-x   0 root         (0) root         (0)       79 2023-04-07 14:21:42.000000 docusign-admin-1.2.0/setup.cfg
+-rwxr-xr-x   0 root         (0) root         (0)     1615 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:21:42.000000 docusign-admin-1.2.0/test/
+-rwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/test/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     4772 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/test/test_oauth.py
+-rwxr-xr-x   0 root         (0) root         (0)     6356 2023-04-07 14:21:38.000000 docusign-admin-1.2.0/test/unit_tests.py
```

### Comparing `docusign-admin-1.1.1/LICENSE` & `docusign-admin-1.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/PKG-INFO` & `docusign-admin-1.2.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,24 +1,24 @@
 Metadata-Version: 2.1
 Name: docusign-admin
-Version: 1.1.1
+Version: 1.2.0
 Summary: DocuSign Admin API
 Home-page: 
 Author-email: devcenter@docusign.com
 Keywords: Swagger,DocuSign Admin API
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # The Official DocuSign OrgAdmin Python Client
 
 [![PyPI version][pypi-image]][pypi-url]
 <!--[![PyPI downloads][downloads-image]][downloads-url]-->
 [![Build status][travis-image]][travis-url]
 
-[PyPI module](https://pypi.python.org/pypi/docusign_orgadmin) that wraps the <a href="https://www.docusign.com/products/orgadmin-for-real-estate">DocuSign OrgAdmin</a> API
+[PyPI module](https://pypi.python.org/pypi/docusign_admin) that wraps the <a href="https://www.docusign.com/products/orgadmin-for-real-estate">DocuSign OrgAdmin</a> API
 
 [Documentation about the DocuSign OrgAdmin API](https://developers.docusign.com/)
 
 ## Requirements
 
 - Python 2.7 (3.7+ recommended)
 - Free [Developer Sandbox](https://go.docusign.com/sandbox/productshot/?elqCampaignId=16531)
```

#### html2text {}

```diff
@@ -1,13 +1,13 @@
-Metadata-Version: 2.1 Name: docusign-admin Version: 1.1.1 Summary: DocuSign
+Metadata-Version: 2.1 Name: docusign-admin Version: 1.2.0 Summary: DocuSign
 Admin API Home-page: Author-email: devcenter@docusign.com Keywords:
 Swagger,DocuSign Admin API Description-Content-Type: text/markdown License-
 File: LICENSE # The Official DocuSign OrgAdmin Python Client [![PyPI version]
 [pypi-image]][pypi-url]  [![Build status][travis-image]][travis-url] [PyPI
-module](https://pypi.python.org/pypi/docusign_orgadmin) that wraps the DocuSign
+module](https://pypi.python.org/pypi/docusign_admin) that wraps the DocuSign
 OrgAdmin API [Documentation about the DocuSign OrgAdmin API](https://
 developers.docusign.com/) ## Requirements - Python 2.7 (3.7+ recommended) -
 Free [Developer Sandbox](https://go.docusign.com/sandbox/productshot/
 ?elqCampaignId=16531) ## Compatibility - Python 2.7+ ## Installation ### Path
 Setup: 1. Locate your Python installation, also referred to as a **site-
 packages** folder. This folder is usually labeled in a format of Python
 {VersionNumber}. **Examples:** - **Unix/Linux:** /usr/lib/python2.7 - **Mac:**
```

### Comparing `docusign-admin-1.1.1/README.md` & `docusign-admin-1.2.0/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # The Official DocuSign OrgAdmin Python Client
 
 [![PyPI version][pypi-image]][pypi-url]
 <!--[![PyPI downloads][downloads-image]][downloads-url]-->
 [![Build status][travis-image]][travis-url]
 
-[PyPI module](https://pypi.python.org/pypi/docusign_orgadmin) that wraps the <a href="https://www.docusign.com/products/orgadmin-for-real-estate">DocuSign OrgAdmin</a> API
+[PyPI module](https://pypi.python.org/pypi/docusign_admin) that wraps the <a href="https://www.docusign.com/products/orgadmin-for-real-estate">DocuSign OrgAdmin</a> API
 
 [Documentation about the DocuSign OrgAdmin API](https://developers.docusign.com/)
 
 ## Requirements
 
 - Python 2.7 (3.7+ recommended)
 - Free [Developer Sandbox](https://go.docusign.com/sandbox/productshot/?elqCampaignId=16531)
```

#### html2text {}

```diff
@@ -1,10 +1,10 @@
 # The Official DocuSign OrgAdmin Python Client [![PyPI version][pypi-image]]
 [pypi-url]  [![Build status][travis-image]][travis-url] [PyPI module](https://
-pypi.python.org/pypi/docusign_orgadmin) that wraps the DocuSign_OrgAdmin API
+pypi.python.org/pypi/docusign_admin) that wraps the DocuSign_OrgAdmin API
 [Documentation about the DocuSign OrgAdmin API](https://
 developers.docusign.com/) ## Requirements - Python 2.7 (3.7+ recommended) -
 Free [Developer Sandbox](https://go.docusign.com/sandbox/productshot/
 ?elqCampaignId=16531) ## Compatibility - Python 2.7+ ## Installation ### Path
 Setup: 1. Locate your Python installation, also referred to as a **site-
 packages** folder. This folder is usually labeled in a format of Python
 {VersionNumber}. **Examples:** - **Unix/Linux:** /usr/lib/python2.7 - **Mac:**
```

### Comparing `docusign-admin-1.1.1/docusign_admin/__init__.py` & `docusign-admin-1.2.0/docusign_admin/__init__.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/apis/accounts_api.py` & `docusign-admin-1.2.0/docusign_admin/apis/accounts_api.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/apis/bulk_exports_api.py` & `docusign-admin-1.2.0/docusign_admin/apis/bulk_exports_api.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/apis/bulk_imports_api.py` & `docusign-admin-1.2.0/docusign_admin/apis/bulk_imports_api.py`

 * *Files 1% similar despite different names*

```diff
@@ -264,61 +264,63 @@
                                         auth_settings=auth_settings,
                                         callback=params.get('callback'),
                                         _return_http_data_only=params.get('_return_http_data_only'),
                                         _preload_content=params.get('_preload_content', True),
                                         _request_timeout=params.get('_request_timeout'),
                                         collection_formats=collection_formats)
 
-    def create_bulk_import_close_users_request(self, organization_id, **kwargs):
+    def create_bulk_import_close_users_request(self, organization_id, file_csv, **kwargs):
         """
         Closes the Bulk User Import request
         Required scopes: user_write
         This method makes a synchronous HTTP request by default. To make an
         asynchronous HTTP request, please define a `callback` function
         to be invoked when receiving the response.
         >>> def callback_function(response):
         >>>     pprint(response)
         >>>
-        >>> thread = api.create_bulk_import_close_users_request(organization_id, callback=callback_function)
+        >>> thread = api.create_bulk_import_close_users_request(organization_id, file_csv, callback=callback_function)
 
         :param callback function: The callback function
             for asynchronous request. (optional)
         :param str organization_id: The organization ID Guid (required)
+        :param file file_csv: CSV file. (required)
         :return: OrganizationImportResponse
                  If the method is called asynchronously,
                  returns the request thread.
         """
         kwargs['_return_http_data_only'] = True
         if kwargs.get('callback'):
-            return self.create_bulk_import_close_users_request_with_http_info(organization_id, **kwargs)
+            return self.create_bulk_import_close_users_request_with_http_info(organization_id, file_csv, **kwargs)
         else:
-            (data) = self.create_bulk_import_close_users_request_with_http_info(organization_id, **kwargs)
+            (data) = self.create_bulk_import_close_users_request_with_http_info(organization_id, file_csv, **kwargs)
             return data
 
-    def create_bulk_import_close_users_request_with_http_info(self, organization_id, **kwargs):
+    def create_bulk_import_close_users_request_with_http_info(self, organization_id, file_csv, **kwargs):
         """
         Closes the Bulk User Import request
         Required scopes: user_write
         This method makes a synchronous HTTP request by default. To make an
         asynchronous HTTP request, please define a `callback` function
         to be invoked when receiving the response.
         >>> def callback_function(response):
         >>>     pprint(response)
         >>>
-        >>> thread = api.create_bulk_import_close_users_request_with_http_info(organization_id, callback=callback_function)
+        >>> thread = api.create_bulk_import_close_users_request_with_http_info(organization_id, file_csv, callback=callback_function)
 
         :param callback function: The callback function
             for asynchronous request. (optional)
         :param str organization_id: The organization ID Guid (required)
+        :param file file_csv: CSV file. (required)
         :return: OrganizationImportResponse
                  If the method is called asynchronously,
                  returns the request thread.
         """
 
-        all_params = ['organization_id']
+        all_params = ['organization_id', 'file_csv']
         all_params.append('callback')
         all_params.append('_return_http_data_only')
         all_params.append('_preload_content')
         all_params.append('_request_timeout')
 
         params = locals()
         for key, val in iteritems(params['kwargs']):
@@ -328,14 +330,17 @@
                     " to method create_bulk_import_close_users_request" % key
                 )
             params[key] = val
         del params['kwargs']
         # verify the required parameter 'organization_id' is set
         if ('organization_id' not in params) or (params['organization_id'] is None):
             raise ValueError("Missing the required parameter `organization_id` when calling `create_bulk_import_close_users_request`")
+        # verify the required parameter 'file_csv' is set
+        if ('file_csv' not in params) or (params['file_csv'] is None):
+            raise ValueError("Missing the required parameter `file_csv` when calling `create_bulk_import_close_users_request`")
 
 
         collection_formats = {}
 
         resource_path = '/v2/organizations/{organizationId}/imports/bulk_users/close'.replace('{format}', 'json')
         path_params = {}
         if 'organization_id' in params:
@@ -343,23 +348,25 @@
 
         query_params = {}
 
         header_params = {}
 
         form_params = []
         local_var_files = {}
+        if 'file_csv' in params:
+            local_var_files['file.csv'] = params['file_csv']
 
         body_params = None
         # HTTP header `Accept`
         header_params['Accept'] = self.api_client.\
             select_header_accept(['application/json'])
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.\
-            select_header_content_type(['application/json'])
+            select_header_content_type(['multipart/form-data'])
 
         # Authentication setting
         auth_settings = []
 
         return self.api_client.call_api(resource_path, 'POST',
                                         path_params,
                                         query_params,
```

### Comparing `docusign-admin-1.1.1/docusign_admin/apis/ds_groups_api.py` & `docusign-admin-1.2.0/docusign_admin/apis/ds_groups_api.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/apis/identity_providers_api.py` & `docusign-admin-1.2.0/docusign_admin/apis/identity_providers_api.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/apis/product_permission_profiles_api.py` & `docusign-admin-1.2.0/docusign_admin/apis/product_permission_profiles_api.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/apis/reserved_domains_api.py` & `docusign-admin-1.2.0/docusign_admin/apis/reserved_domains_api.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/apis/users_api.py` & `docusign-admin-1.2.0/docusign_admin/apis/users_api.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/client/api_client.py` & `docusign-admin-1.2.0/docusign_admin/client/api_client.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/client/api_exception.py` & `docusign-admin-1.2.0/docusign_admin/client/api_exception.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/client/api_response.py` & `docusign-admin-1.2.0/docusign_admin/client/api_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/client/auth/oauth.py` & `docusign-admin-1.2.0/docusign_admin/client/auth/oauth.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/client/configuration.py` & `docusign-admin-1.2.0/docusign_admin/client/configuration.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/__init__.py` & `docusign-admin-1.2.0/docusign_admin/models/__init__.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/add_ds_group_and_users_response.py` & `docusign-admin-1.2.0/docusign_admin/models/add_ds_group_and_users_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/add_ds_group_users_response.py` & `docusign-admin-1.2.0/docusign_admin/models/add_ds_group_users_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/add_user_response.py` & `docusign-admin-1.2.0/docusign_admin/models/add_user_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/add_user_response_account_properties.py` & `docusign-admin-1.2.0/docusign_admin/models/add_user_response_account_properties.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/certificate_response.py` & `docusign-admin-1.2.0/docusign_admin/models/certificate_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/delete_membership_request.py` & `docusign-admin-1.2.0/docusign_admin/models/delete_membership_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/delete_membership_response.py` & `docusign-admin-1.2.0/docusign_admin/models/delete_membership_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/delete_memberships_request.py` & `docusign-admin-1.2.0/docusign_admin/models/delete_memberships_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/delete_memberships_response.py` & `docusign-admin-1.2.0/docusign_admin/models/delete_memberships_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/delete_response.py` & `docusign-admin-1.2.0/docusign_admin/models/delete_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/delete_user_identity_request.py` & `docusign-admin-1.2.0/docusign_admin/models/delete_user_identity_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/domain_response.py` & `docusign-admin-1.2.0/docusign_admin/models/domain_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/domains_response.py` & `docusign-admin-1.2.0/docusign_admin/models/domains_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/ds_group_add_request.py` & `docusign-admin-1.2.0/docusign_admin/models/ds_group_add_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/ds_group_and_users_response.py` & `docusign-admin-1.2.0/docusign_admin/models/ds_group_and_users_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/ds_group_list_response.py` & `docusign-admin-1.2.0/docusign_admin/models/ds_group_list_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/ds_group_request.py` & `docusign-admin-1.2.0/docusign_admin/models/ds_group_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/ds_group_response.py` & `docusign-admin-1.2.0/docusign_admin/models/ds_group_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/ds_group_user_response.py` & `docusign-admin-1.2.0/docusign_admin/models/ds_group_user_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/ds_group_users_add_request.py` & `docusign-admin-1.2.0/docusign_admin/models/ds_group_users_add_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/ds_group_users_remove_request.py` & `docusign-admin-1.2.0/docusign_admin/models/ds_group_users_remove_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/ds_group_users_response.py` & `docusign-admin-1.2.0/docusign_admin/models/ds_group_users_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/error_details.py` & `docusign-admin-1.2.0/docusign_admin/models/error_details.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/force_activate_membership_request.py` & `docusign-admin-1.2.0/docusign_admin/models/force_activate_membership_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/group_request.py` & `docusign-admin-1.2.0/docusign_admin/models/group_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/identity_provider_response.py` & `docusign-admin-1.2.0/docusign_admin/models/identity_provider_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/identity_providers_response.py` & `docusign-admin-1.2.0/docusign_admin/models/identity_providers_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/link_response.py` & `docusign-admin-1.2.0/docusign_admin/models/link_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/member_group_response.py` & `docusign-admin-1.2.0/docusign_admin/models/member_group_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/member_groups_response.py` & `docusign-admin-1.2.0/docusign_admin/models/member_groups_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/membership_response.py` & `docusign-admin-1.2.0/docusign_admin/models/membership_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/new_account_user_request.py` & `docusign-admin-1.2.0/docusign_admin/models/new_account_user_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/new_multi_product_user_add_request.py` & `docusign-admin-1.2.0/docusign_admin/models/new_multi_product_user_add_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/new_user_request.py` & `docusign-admin-1.2.0/docusign_admin/models/new_user_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/new_user_request_account_properties.py` & `docusign-admin-1.2.0/docusign_admin/models/new_user_request_account_properties.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/new_user_response.py` & `docusign-admin-1.2.0/docusign_admin/models/new_user_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/new_user_response_account_properties.py` & `docusign-admin-1.2.0/docusign_admin/models/new_user_response_account_properties.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/oasirr_error_details.py` & `docusign-admin-1.2.0/docusign_admin/models/oasirr_error_details.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/oasirr_organization_account_settings_error_data_response.py` & `docusign-admin-1.2.0/docusign_admin/models/oasirr_organization_account_settings_error_data_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/oetr_error_details.py` & `docusign-admin-1.2.0/docusign_admin/models/oetr_error_details.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/org_export_selected_account.py` & `docusign-admin-1.2.0/docusign_admin/models/org_export_selected_account.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/org_export_selected_domain.py` & `docusign-admin-1.2.0/docusign_admin/models/org_export_selected_domain.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/org_report_configuration_response.py` & `docusign-admin-1.2.0/docusign_admin/models/org_report_configuration_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/org_report_create_response.py` & `docusign-admin-1.2.0/docusign_admin/models/org_report_create_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/org_report_list_response.py` & `docusign-admin-1.2.0/docusign_admin/models/org_report_list_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/org_report_list_response_org_report.py` & `docusign-admin-1.2.0/docusign_admin/models/org_report_list_response_org_report.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/org_report_list_response_requestor.py` & `docusign-admin-1.2.0/docusign_admin/models/org_report_list_response_requestor.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/org_report_request.py` & `docusign-admin-1.2.0/docusign_admin/models/org_report_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_account_request.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_account_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_account_response.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_account_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_account_settings_import_requestor_response.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_account_settings_import_requestor_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_account_settings_import_response.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_account_settings_import_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_account_settings_import_result_response.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_account_settings_import_result_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_accounts_request.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_accounts_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_export_account.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_export_account.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_export_domain.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_export_domain.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_export_request.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_export_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_export_requestor_response.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_export_requestor_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_export_response.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_export_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_export_task_response.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_export_task_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_exports_response.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_exports_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_import_response.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_import_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_import_response_error_rollup.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_import_response_error_rollup.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_import_response_requestor.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_import_response_requestor.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_import_response_warning_rollup.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_import_response_warning_rollup.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_imports_response.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_imports_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_response.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_salesforce_account_managers_response.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_salesforce_account_managers_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_simple_id_object.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_simple_id_object.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_user_response.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_user_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organization_users_response.py` & `docusign-admin-1.2.0/docusign_admin/models/organization_users_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/organizations_response.py` & `docusign-admin-1.2.0/docusign_admin/models/organizations_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/osamr_contact.py` & `docusign-admin-1.2.0/docusign_admin/models/osamr_contact.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/paging_response_properties.py` & `docusign-admin-1.2.0/docusign_admin/models/paging_response_properties.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/permission_profile_request.py` & `docusign-admin-1.2.0/docusign_admin/models/permission_profile_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/permission_profile_response.py` & `docusign-admin-1.2.0/docusign_admin/models/permission_profile_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/permission_profile_response21.py` & `docusign-admin-1.2.0/docusign_admin/models/permission_profile_response21.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/permissions_response.py` & `docusign-admin-1.2.0/docusign_admin/models/permissions_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/product_permission_profile_request.py` & `docusign-admin-1.2.0/docusign_admin/models/product_permission_profile_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/product_permission_profile_response.py` & `docusign-admin-1.2.0/docusign_admin/models/product_permission_profile_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/product_permission_profiles_request.py` & `docusign-admin-1.2.0/docusign_admin/models/product_permission_profiles_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/product_permission_profiles_response.py` & `docusign-admin-1.2.0/docusign_admin/models/product_permission_profiles_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/remove_ds_group_users_response.py` & `docusign-admin-1.2.0/docusign_admin/models/remove_ds_group_users_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/remove_user_products_response.py` & `docusign-admin-1.2.0/docusign_admin/models/remove_user_products_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/required_attribute_mapping_response.py` & `docusign-admin-1.2.0/docusign_admin/models/required_attribute_mapping_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/saml2_identity_provider_response.py` & `docusign-admin-1.2.0/docusign_admin/models/saml2_identity_provider_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/setting_response.py` & `docusign-admin-1.2.0/docusign_admin/models/setting_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/update_membership_request.py` & `docusign-admin-1.2.0/docusign_admin/models/update_membership_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/update_response.py` & `docusign-admin-1.2.0/docusign_admin/models/update_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/update_user_email_request.py` & `docusign-admin-1.2.0/docusign_admin/models/update_user_email_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/update_user_request.py` & `docusign-admin-1.2.0/docusign_admin/models/update_user_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/update_users_email_request.py` & `docusign-admin-1.2.0/docusign_admin/models/update_users_email_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/update_users_request.py` & `docusign-admin-1.2.0/docusign_admin/models/update_users_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/user_drilldown_response.py` & `docusign-admin-1.2.0/docusign_admin/models/user_drilldown_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/user_identity_request.py` & `docusign-admin-1.2.0/docusign_admin/models/user_identity_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/user_identity_response.py` & `docusign-admin-1.2.0/docusign_admin/models/user_identity_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/user_product_permission_profiles_request.py` & `docusign-admin-1.2.0/docusign_admin/models/user_product_permission_profiles_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/user_product_permission_profiles_response.py` & `docusign-admin-1.2.0/docusign_admin/models/user_product_permission_profiles_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/user_product_profile_delete_request.py` & `docusign-admin-1.2.0/docusign_admin/models/user_product_profile_delete_request.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/user_update_response.py` & `docusign-admin-1.2.0/docusign_admin/models/user_update_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/users_drilldown_response.py` & `docusign-admin-1.2.0/docusign_admin/models/users_drilldown_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin/models/users_update_response.py` & `docusign-admin-1.2.0/docusign_admin/models/users_update_response.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/docusign_admin.egg-info/PKG-INFO` & `docusign-admin-1.2.0/docusign_admin.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,24 +1,24 @@
 Metadata-Version: 2.1
 Name: docusign-admin
-Version: 1.1.1
+Version: 1.2.0
 Summary: DocuSign Admin API
 Home-page: 
 Author-email: devcenter@docusign.com
 Keywords: Swagger,DocuSign Admin API
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # The Official DocuSign OrgAdmin Python Client
 
 [![PyPI version][pypi-image]][pypi-url]
 <!--[![PyPI downloads][downloads-image]][downloads-url]-->
 [![Build status][travis-image]][travis-url]
 
-[PyPI module](https://pypi.python.org/pypi/docusign_orgadmin) that wraps the <a href="https://www.docusign.com/products/orgadmin-for-real-estate">DocuSign OrgAdmin</a> API
+[PyPI module](https://pypi.python.org/pypi/docusign_admin) that wraps the <a href="https://www.docusign.com/products/orgadmin-for-real-estate">DocuSign OrgAdmin</a> API
 
 [Documentation about the DocuSign OrgAdmin API](https://developers.docusign.com/)
 
 ## Requirements
 
 - Python 2.7 (3.7+ recommended)
 - Free [Developer Sandbox](https://go.docusign.com/sandbox/productshot/?elqCampaignId=16531)
```

#### html2text {}

```diff
@@ -1,13 +1,13 @@
-Metadata-Version: 2.1 Name: docusign-admin Version: 1.1.1 Summary: DocuSign
+Metadata-Version: 2.1 Name: docusign-admin Version: 1.2.0 Summary: DocuSign
 Admin API Home-page: Author-email: devcenter@docusign.com Keywords:
 Swagger,DocuSign Admin API Description-Content-Type: text/markdown License-
 File: LICENSE # The Official DocuSign OrgAdmin Python Client [![PyPI version]
 [pypi-image]][pypi-url]  [![Build status][travis-image]][travis-url] [PyPI
-module](https://pypi.python.org/pypi/docusign_orgadmin) that wraps the DocuSign
+module](https://pypi.python.org/pypi/docusign_admin) that wraps the DocuSign
 OrgAdmin API [Documentation about the DocuSign OrgAdmin API](https://
 developers.docusign.com/) ## Requirements - Python 2.7 (3.7+ recommended) -
 Free [Developer Sandbox](https://go.docusign.com/sandbox/productshot/
 ?elqCampaignId=16531) ## Compatibility - Python 2.7+ ## Installation ### Path
 Setup: 1. Locate your Python installation, also referred to as a **site-
 packages** folder. This folder is usually labeled in a format of Python
 {VersionNumber}. **Examples:** - **Unix/Linux:** /usr/lib/python2.7 - **Mac:**
```

### Comparing `docusign-admin-1.1.1/docusign_admin.egg-info/SOURCES.txt` & `docusign-admin-1.2.0/docusign_admin.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/setup.py` & `docusign-admin-1.2.0/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -10,23 +10,23 @@
     Generated by: https://github.com/swagger-api/swagger-codegen.git
 """
 
 
 from setuptools import setup, find_packages, Command, os  # noqa: H301	
 
 NAME = "docusign-admin"
-VERSION = "1.1.1"
+VERSION = "1.2.0"
 # To install the library, run the following
 #
 # python setup.py install
 #
 # prerequisite: setuptools
 # http://pypi.python.org/pypi/setuptools
 
-REQUIRES = ["urllib3 >= 1.15", "six >= 1.8.0", "certifi >= 14.05.14", "python-dateutil >= 2.5.3", "setuptools >= 21.0.0", "PyJWT>=1.7.1,<2", "cryptography>=2.5", "nose>=1.3.7"]
+REQUIRES = ["urllib3 >= 1.15", "six >= 1.8.0", "certifi >= 14.05.14", "python-dateutil >= 2.5.3", "setuptools >= 21.0.0", "PyJWT>=1.7.1", "cryptography>=2.5", "nose>=1.3.7"]
 
 class CleanCommand(Command):
     """Custom clean command to tidy up the project root."""
     user_options = []
     def initialize_options(self):
         pass
     def finalize_options(self):
```

### Comparing `docusign-admin-1.1.1/test/test_oauth.py` & `docusign-admin-1.2.0/test/test_oauth.py`

 * *Files identical despite different names*

### Comparing `docusign-admin-1.1.1/test/unit_tests.py` & `docusign-admin-1.2.0/test/unit_tests.py`

 * *Files identical despite different names*

