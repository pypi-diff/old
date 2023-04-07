# Comparing `tmp/pyonepassword-3.8.0.tar.gz` & `tmp/pyonepassword-3.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyonepassword-3.8.0.tar", last modified: Tue Mar 28 00:31:10 2023, max compression
+gzip compressed data, was "pyonepassword-3.9.0.tar", last modified: Fri Apr  7 01:06:19 2023, max compression
```

## Comparing `pyonepassword-3.8.0.tar` & `pyonepassword-3.9.0.tar`

### file list

```diff
@@ -1,135 +1,124 @@
-drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-03-28 00:31:10.883539 pyonepassword-3.8.0/
--rw-r--r--   0 zach       (502) staff       (20)     1071 2019-08-09 16:32:59.000000 pyonepassword-3.8.0/LICENSE
--rw-r--r--   0 zach       (502) staff       (20)    10393 2023-03-28 00:31:10.883603 pyonepassword-3.8.0/PKG-INFO
--rw-r--r--   0 zach       (502) staff       (20)     9932 2023-03-14 23:01:20.000000 pyonepassword-3.8.0/README.md
-drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-03-28 00:31:10.866645 pyonepassword-3.8.0/pyonepassword/
--rw-r--r--   0 zach       (502) staff       (20)      523 2023-03-28 00:30:12.000000 pyonepassword-3.8.0/pyonepassword/__about__.py
--rw-r--r--   0 zach       (502) staff       (20)      626 2023-02-07 19:47:51.000000 pyonepassword-3.8.0/pyonepassword/__init__.py
--rw-r--r--   0 zach       (502) staff       (20)     2276 2023-02-15 22:33:25.000000 pyonepassword-3.8.0/pyonepassword/_abc_meta.py
--rw-r--r--   0 zach       (502) staff       (20)      494 2022-06-22 01:21:11.000000 pyonepassword-3.8.0/pyonepassword/_api_initializer.py
--rw-r--r--   0 zach       (502) staff       (20)      871 2022-06-22 00:58:09.000000 pyonepassword-3.8.0/pyonepassword/_datetime.py
--rw-r--r--   0 zach       (502) staff       (20)    11334 2023-01-22 17:09:56.000000 pyonepassword-3.8.0/pyonepassword/_op_cli_argv.py
--rw-r--r--   0 zach       (502) staff       (20)     4406 2023-01-22 17:09:56.000000 pyonepassword-3.8.0/pyonepassword/_op_cli_config.py
--rw-r--r--   0 zach       (502) staff       (20)     3458 2023-03-28 00:30:12.000000 pyonepassword-3.8.0/pyonepassword/_py_op_cli.py
--rw-r--r--   0 zach       (502) staff       (20)    28278 2023-03-14 23:01:20.000000 pyonepassword-3.8.0/pyonepassword/_py_op_commands.py
--rw-r--r--   0 zach       (502) staff       (20)     3099 2023-01-22 17:09:56.000000 pyonepassword-3.8.0/pyonepassword/_py_op_deprecation.py
--rw-r--r--   0 zach       (502) staff       (20)     1924 2023-03-13 03:40:10.000000 pyonepassword-3.8.0/pyonepassword/account.py
-drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-03-28 00:31:10.868170 pyonepassword-3.8.0/pyonepassword/api/
--rw-r--r--   0 zach       (502) staff       (20)        0 2023-02-07 19:47:51.000000 pyonepassword-3.8.0/pyonepassword/api/__init__.py
--rw-r--r--   0 zach       (502) staff       (20)      460 2023-01-22 17:09:56.000000 pyonepassword-3.8.0/pyonepassword/api/authentication.py
--rw-r--r--   0 zach       (502) staff       (20)      432 2023-01-22 17:09:56.000000 pyonepassword-3.8.0/pyonepassword/api/constants.py
--rw-r--r--   0 zach       (502) staff       (20)      319 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/api/decorators.py
--rw-r--r--   0 zach       (502) staff       (20)     1691 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/api/descriptor_types.py
--rw-r--r--   0 zach       (502) staff       (20)     2874 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/api/exceptions.py
--rw-r--r--   0 zach       (502) staff       (20)     2698 2023-03-28 00:30:12.000000 pyonepassword-3.8.0/pyonepassword/api/object_types.py
--rw-r--r--   0 zach       (502) staff       (20)      512 2023-02-15 22:33:25.000000 pyonepassword-3.8.0/pyonepassword/api/validation.py
-drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-03-28 00:31:10.876275 pyonepassword-3.8.0/pyonepassword/data/
--rw-r--r--   0 zach       (502) staff       (20)       50 2023-02-07 19:47:51.000000 pyonepassword-3.8.0/pyonepassword/data/__init__.py
--rw-r--r--   0 zach       (502) staff       (20)      940 2023-03-27 23:10:38.000000 pyonepassword-3.8.0/pyonepassword/data/api_credential.json
--rw-r--r--   0 zach       (502) staff       (20)     1552 2023-03-27 23:10:48.000000 pyonepassword-3.8.0/pyonepassword/data/bank_account.json
--rw-r--r--   0 zach       (502) staff       (20)     3084 2023-03-27 23:10:49.000000 pyonepassword-3.8.0/pyonepassword/data/credit_card.json
--rw-r--r--   0 zach       (502) staff       (20)      701 2023-03-27 23:10:42.000000 pyonepassword-3.8.0/pyonepassword/data/crypto_wallet.json
--rw-r--r--   0 zach       (502) staff       (20)     1137 2023-03-27 23:10:45.000000 pyonepassword-3.8.0/pyonepassword/data/database.json
--rw-r--r--   0 zach       (502) staff       (20)      198 2023-03-27 23:10:43.000000 pyonepassword-3.8.0/pyonepassword/data/document.json
--rw-r--r--   0 zach       (502) staff       (20)     1384 2023-03-27 23:10:39.000000 pyonepassword-3.8.0/pyonepassword/data/driver_license.json
--rw-r--r--   0 zach       (502) staff       (20)     3125 2023-03-27 23:10:50.000000 pyonepassword-3.8.0/pyonepassword/data/email_account.json
--rw-r--r--   0 zach       (502) staff       (20)     5190 2023-03-27 23:10:39.000000 pyonepassword-3.8.0/pyonepassword/data/identity.json
--rw-r--r--   0 zach       (502) staff       (20)      536 2023-03-27 23:10:40.000000 pyonepassword-3.8.0/pyonepassword/data/login.json
--rw-r--r--   0 zach       (502) staff       (20)     1425 2023-03-27 23:10:41.000000 pyonepassword-3.8.0/pyonepassword/data/medical_record.json
--rw-r--r--   0 zach       (502) staff       (20)     1064 2023-03-27 23:10:46.000000 pyonepassword-3.8.0/pyonepassword/data/membership.json
--rw-r--r--   0 zach       (502) staff       (20)      941 2023-03-27 23:10:43.000000 pyonepassword-3.8.0/pyonepassword/data/outdoor_license.json
--rw-r--r--   0 zach       (502) staff       (20)     1404 2023-03-27 23:10:46.000000 pyonepassword-3.8.0/pyonepassword/data/passport.json
--rw-r--r--   0 zach       (502) staff       (20)      404 2023-03-27 23:10:50.000000 pyonepassword-3.8.0/pyonepassword/data/password.json
--rw-r--r--   0 zach       (502) staff       (20)     1770 2023-03-27 23:10:44.000000 pyonepassword-3.8.0/pyonepassword/data/reward_program.json
--rw-r--r--   0 zach       (502) staff       (20)      201 2023-03-27 23:10:51.000000 pyonepassword-3.8.0/pyonepassword/data/secure_note.json
--rw-r--r--   0 zach       (502) staff       (20)     2222 2023-03-27 23:10:45.000000 pyonepassword-3.8.0/pyonepassword/data/server.json
--rw-r--r--   0 zach       (502) staff       (20)      415 2023-03-27 23:10:48.000000 pyonepassword-3.8.0/pyonepassword/data/social_security_number.json
--rw-r--r--   0 zach       (502) staff       (20)     2756 2023-03-27 23:10:41.000000 pyonepassword-3.8.0/pyonepassword/data/software_license.json
--rw-r--r--   0 zach       (502) staff       (20)      309 2023-03-27 23:10:51.000000 pyonepassword-3.8.0/pyonepassword/data/ssh_key.json
--rw-r--r--   0 zach       (502) staff       (20)      829 2023-03-27 23:10:51.000000 pyonepassword-3.8.0/pyonepassword/data/template-registry.json
--rw-r--r--   0 zach       (502) staff       (20)     1165 2023-03-27 23:10:47.000000 pyonepassword-3.8.0/pyonepassword/data/wireless_router.json
--rw-r--r--   0 zach       (502) staff       (20)      257 2022-06-22 00:58:09.000000 pyonepassword-3.8.0/pyonepassword/json.py
--rw-r--r--   0 zach       (502) staff       (20)      268 2022-11-09 19:14:03.000000 pyonepassword-3.8.0/pyonepassword/logging.py
--rw-r--r--   0 zach       (502) staff       (20)     4314 2022-06-22 00:58:09.000000 pyonepassword-3.8.0/pyonepassword/op_cli_version.py
-drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-03-28 00:31:10.877625 pyonepassword-3.8.0/pyonepassword/op_items/
--rw-r--r--   0 zach       (502) staff       (20)      214 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/__init__.py
--rw-r--r--   0 zach       (502) staff       (20)      676 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/_item_descriptor_registry.py
--rw-r--r--   0 zach       (502) staff       (20)     1652 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/_item_list.py
--rw-r--r--   0 zach       (502) staff       (20)     4693 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/_item_type_registry.py
--rw-r--r--   0 zach       (502) staff       (20)     4506 2023-03-28 00:30:12.000000 pyonepassword-3.8.0/pyonepassword/op_items/_new_field_registry.py
--rw-r--r--   0 zach       (502) staff       (20)     9342 2023-03-16 01:30:37.000000 pyonepassword-3.8.0/pyonepassword/op_items/_new_item.py
--rw-r--r--   0 zach       (502) staff       (20)      907 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/field_registry.py
-drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-03-28 00:31:10.878193 pyonepassword-3.8.0/pyonepassword/op_items/fields_sections/
--rw-r--r--   0 zach       (502) staff       (20)        0 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/fields_sections/__init__.py
--rw-r--r--   0 zach       (502) staff       (20)     6801 2023-03-28 00:30:12.000000 pyonepassword-3.8.0/pyonepassword/op_items/fields_sections/_new_fields.py
--rw-r--r--   0 zach       (502) staff       (20)      519 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/fields_sections/item_field.py
--rw-r--r--   0 zach       (502) staff       (20)     1340 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/fields_sections/item_field_base.py
--rw-r--r--   0 zach       (502) staff       (20)     3702 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/fields_sections/item_section.py
-drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-03-28 00:31:10.879897 pyonepassword-3.8.0/pyonepassword/op_items/item_types/
--rw-r--r--   0 zach       (502) staff       (20)        0 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/item_types/__init__.py
--rw-r--r--   0 zach       (502) staff       (20)     8829 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/item_types/_item_base.py
--rw-r--r--   0 zach       (502) staff       (20)     1895 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/item_types/_item_descriptor_base.py
--rw-r--r--   0 zach       (502) staff       (20)     3616 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/item_types/api_credential.py
--rw-r--r--   0 zach       (502) staff       (20)     2500 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/item_types/credit_card.py
--rw-r--r--   0 zach       (502) staff       (20)     8831 2023-03-28 00:30:12.000000 pyonepassword-3.8.0/pyonepassword/op_items/item_types/database.py
--rw-r--r--   0 zach       (502) staff       (20)     1510 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/item_types/document.py
--rw-r--r--   0 zach       (502) staff       (20)     1312 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/item_types/generic_item.py
--rw-r--r--   0 zach       (502) staff       (20)      325 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/item_types/identity.py
--rw-r--r--   0 zach       (502) staff       (20)     6746 2023-03-28 00:30:12.000000 pyonepassword-3.8.0/pyonepassword/op_items/item_types/login.py
--rw-r--r--   0 zach       (502) staff       (20)     1885 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/item_types/password.py
--rw-r--r--   0 zach       (502) staff       (20)     1599 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/item_types/secure_note.py
--rw-r--r--   0 zach       (502) staff       (20)     1696 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/pyonepassword/op_items/item_types/server.py
--rw-r--r--   0 zach       (502) staff       (20)     1758 2023-03-16 01:30:37.000000 pyonepassword-3.8.0/pyonepassword/op_items/item_types/ssh_key.py
--rw-r--r--   0 zach       (502) staff       (20)     5533 2023-02-15 22:33:25.000000 pyonepassword-3.8.0/pyonepassword/op_items/item_validation_policy.py
--rw-r--r--   0 zach       (502) staff       (20)      834 2023-01-22 17:09:56.000000 pyonepassword-3.8.0/pyonepassword/op_items/password_recipe.py
--rw-r--r--   0 zach       (502) staff       (20)      519 2023-01-22 17:09:56.000000 pyonepassword-3.8.0/pyonepassword/op_items/template_directory.py
--rw-r--r--   0 zach       (502) staff       (20)      898 2022-06-22 00:58:09.000000 pyonepassword-3.8.0/pyonepassword/op_items/totp.py
--rw-r--r--   0 zach       (502) staff       (20)     1809 2023-03-16 01:30:37.000000 pyonepassword-3.8.0/pyonepassword/op_items/uuid.py
--rw-r--r--   0 zach       (502) staff       (20)    11729 2023-02-15 22:33:25.000000 pyonepassword-3.8.0/pyonepassword/op_objects.py
--rw-r--r--   0 zach       (502) staff       (20)     1710 2022-11-09 19:14:03.000000 pyonepassword-3.8.0/pyonepassword/opconfig_main.py
--rw-r--r--   0 zach       (502) staff       (20)      184 2023-01-22 17:09:56.000000 pyonepassword-3.8.0/pyonepassword/pkg_resources.py
--rw-r--r--   0 zach       (502) staff       (20)        0 2023-01-22 17:09:56.000000 pyonepassword-3.8.0/pyonepassword/py.typed
--rw-r--r--   0 zach       (502) staff       (20)     6099 2023-03-14 23:01:20.000000 pyonepassword-3.8.0/pyonepassword/py_op_exceptions.py
--rw-r--r--   0 zach       (502) staff       (20)    35790 2023-03-14 23:01:20.000000 pyonepassword-3.8.0/pyonepassword/pyonepassword.py
--rw-r--r--   0 zach       (502) staff       (20)      972 2023-01-22 17:09:56.000000 pyonepassword-3.8.0/pyonepassword/version.py
-drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-03-28 00:31:10.867304 pyonepassword-3.8.0/pyonepassword.egg-info/
--rw-r--r--   0 zach       (502) staff       (20)    10393 2023-03-28 00:31:10.000000 pyonepassword-3.8.0/pyonepassword.egg-info/PKG-INFO
--rw-r--r--   0 zach       (502) staff       (20)     4362 2023-03-28 00:31:10.000000 pyonepassword-3.8.0/pyonepassword.egg-info/SOURCES.txt
--rw-r--r--   0 zach       (502) staff       (20)        1 2023-03-28 00:31:10.000000 pyonepassword-3.8.0/pyonepassword.egg-info/dependency_links.txt
--rw-r--r--   0 zach       (502) staff       (20)       62 2023-03-28 00:31:10.000000 pyonepassword-3.8.0/pyonepassword.egg-info/entry_points.txt
--rw-r--r--   0 zach       (502) staff       (20)       54 2023-03-28 00:31:10.000000 pyonepassword-3.8.0/pyonepassword.egg-info/requires.txt
--rw-r--r--   0 zach       (502) staff       (20)       14 2023-03-28 00:31:10.000000 pyonepassword-3.8.0/pyonepassword.egg-info/top_level.txt
--rw-r--r--   0 zach       (502) staff       (20)      628 2023-03-28 00:31:10.883883 pyonepassword-3.8.0/setup.cfg
--rw-r--r--   0 zach       (502) staff       (20)     2165 2023-01-22 17:09:56.000000 pyonepassword-3.8.0/setup.py
-drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-03-28 00:31:10.882356 pyonepassword-3.8.0/tests/
--rw-r--r--   0 zach       (502) staff       (20)        0 2023-02-07 19:53:31.000000 pyonepassword-3.8.0/tests/__init__.py
--rw-r--r--   0 zach       (502) staff       (20)       54 2022-06-22 00:58:09.000000 pyonepassword-3.8.0/tests/conftest.py
--rw-r--r--   0 zach       (502) staff       (20)     1765 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/tests/test_abstract_base_meta.py
--rw-r--r--   0 zach       (502) staff       (20)     2088 2022-11-09 19:14:03.000000 pyonepassword-3.8.0/tests/test_account_list.py
--rw-r--r--   0 zach       (502) staff       (20)     2334 2022-06-22 00:58:09.000000 pyonepassword-3.8.0/tests/test_cli_version.py
--rw-r--r--   0 zach       (502) staff       (20)      806 2022-06-22 00:58:09.000000 pyonepassword-3.8.0/tests/test_datetime.py
--rw-r--r--   0 zach       (502) staff       (20)     3684 2023-01-22 17:09:56.000000 pyonepassword-3.8.0/tests/test_document_delete.py
--rw-r--r--   0 zach       (502) staff       (20)     2396 2022-06-22 01:21:11.000000 pyonepassword-3.8.0/tests/test_document_get.py
--rw-r--r--   0 zach       (502) staff       (20)     2844 2023-02-15 22:33:25.000000 pyonepassword-3.8.0/tests/test_exports.py
--rw-r--r--   0 zach       (502) staff       (20)     3652 2022-06-22 01:21:11.000000 pyonepassword-3.8.0/tests/test_group_get.py
--rw-r--r--   0 zach       (502) staff       (20)     3334 2023-01-22 17:09:56.000000 pyonepassword-3.8.0/tests/test_item_delete.py
--rw-r--r--   0 zach       (502) staff       (20)     6748 2023-03-12 00:12:37.000000 pyonepassword-3.8.0/tests/test_item_delete_multiple.py
--rw-r--r--   0 zach       (502) staff       (20)     2143 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/tests/test_item_errors.py
--rw-r--r--   0 zach       (502) staff       (20)     9706 2023-01-22 17:09:56.000000 pyonepassword-3.8.0/tests/test_item_field.py
-drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-03-28 00:31:10.883422 pyonepassword-3.8.0/tests/test_item_get/
--rw-r--r--   0 zach       (502) staff       (20)        0 2023-02-07 19:53:31.000000 pyonepassword-3.8.0/tests/test_item_get/__init__.py
--rw-r--r--   0 zach       (502) staff       (20)     5102 2023-02-15 22:33:25.000000 pyonepassword-3.8.0/tests/test_item_get/test_item_get_api_cred.py
--rw-r--r--   0 zach       (502) staff       (20)     5866 2023-02-15 22:33:25.000000 pyonepassword-3.8.0/tests/test_item_get/test_item_get_credit_card.py
--rw-r--r--   0 zach       (502) staff       (20)     7533 2023-03-10 23:45:14.000000 pyonepassword-3.8.0/tests/test_item_get/test_item_get_login.py
--rw-r--r--   0 zach       (502) staff       (20)     1205 2023-02-10 21:04:00.000000 pyonepassword-3.8.0/tests/test_item_get/test_item_get_password.py
--rw-r--r--   0 zach       (502) staff       (20)     2097 2023-02-10 21:04:03.000000 pyonepassword-3.8.0/tests/test_item_get/test_item_get_secure_note.py
--rw-r--r--   0 zach       (502) staff       (20)     5974 2023-02-10 21:04:08.000000 pyonepassword-3.8.0/tests/test_item_get/test_item_get_server.py
--rw-r--r--   0 zach       (502) staff       (20)     5401 2023-02-10 21:04:10.000000 pyonepassword-3.8.0/tests/test_item_get/test_item_get_ssh_keys.py
--rw-r--r--   0 zach       (502) staff       (20)     2964 2023-02-10 21:04:12.000000 pyonepassword-3.8.0/tests/test_item_get/test_item_get_totp.py
--rw-r--r--   0 zach       (502) staff       (20)     5293 2023-03-14 04:31:28.000000 pyonepassword-3.8.0/tests/test_item_section.py
--rw-r--r--   0 zach       (502) staff       (20)     5982 2023-02-22 03:29:40.000000 pyonepassword-3.8.0/tests/test_misc.py
--rw-r--r--   0 zach       (502) staff       (20)      501 2022-11-09 19:14:03.000000 pyonepassword-3.8.0/tests/test_op_cli.py
--rw-r--r--   0 zach       (502) staff       (20)     8367 2023-02-15 22:33:25.000000 pyonepassword-3.8.0/tests/test_op_cli_config.py
--rw-r--r--   0 zach       (502) staff       (20)      442 2023-01-22 17:09:56.000000 pyonepassword-3.8.0/tests/test_pyop_about.py
--rw-r--r--   0 zach       (502) staff       (20)     3802 2022-06-22 01:21:11.000000 pyonepassword-3.8.0/tests/test_user_get.py
--rw-r--r--   0 zach       (502) staff       (20)     6149 2022-06-22 01:21:11.000000 pyonepassword-3.8.0/tests/test_vault_get.py
+drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-04-07 01:06:19.908751 pyonepassword-3.9.0/
+-rw-r--r--   0 zach       (502) staff       (20)     1071 2019-08-09 16:32:59.000000 pyonepassword-3.9.0/LICENSE
+-rw-r--r--   0 zach       (502) staff       (20)    10393 2023-04-07 01:06:19.908826 pyonepassword-3.9.0/PKG-INFO
+-rw-r--r--   0 zach       (502) staff       (20)     9932 2023-03-14 23:01:20.000000 pyonepassword-3.9.0/README.md
+drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-04-07 01:06:19.894219 pyonepassword-3.9.0/pyonepassword/
+-rw-r--r--   0 zach       (502) staff       (20)      523 2023-04-07 01:05:30.000000 pyonepassword-3.9.0/pyonepassword/__about__.py
+-rw-r--r--   0 zach       (502) staff       (20)      626 2023-02-07 19:47:51.000000 pyonepassword-3.9.0/pyonepassword/__init__.py
+-rw-r--r--   0 zach       (502) staff       (20)     2276 2023-02-15 22:33:25.000000 pyonepassword-3.9.0/pyonepassword/_abc_meta.py
+-rw-r--r--   0 zach       (502) staff       (20)      494 2022-06-22 01:21:11.000000 pyonepassword-3.9.0/pyonepassword/_api_initializer.py
+-rw-r--r--   0 zach       (502) staff       (20)      871 2022-06-22 00:58:09.000000 pyonepassword-3.9.0/pyonepassword/_datetime.py
+-rw-r--r--   0 zach       (502) staff       (20)    11334 2023-01-22 17:09:56.000000 pyonepassword-3.9.0/pyonepassword/_op_cli_argv.py
+-rw-r--r--   0 zach       (502) staff       (20)     4406 2023-01-22 17:09:56.000000 pyonepassword-3.9.0/pyonepassword/_op_cli_config.py
+-rw-r--r--   0 zach       (502) staff       (20)     3458 2023-03-31 21:40:59.000000 pyonepassword-3.9.0/pyonepassword/_py_op_cli.py
+-rw-r--r--   0 zach       (502) staff       (20)    28278 2023-03-14 23:01:20.000000 pyonepassword-3.9.0/pyonepassword/_py_op_commands.py
+-rw-r--r--   0 zach       (502) staff       (20)     3099 2023-01-22 17:09:56.000000 pyonepassword-3.9.0/pyonepassword/_py_op_deprecation.py
+-rw-r--r--   0 zach       (502) staff       (20)     1924 2023-03-13 03:40:10.000000 pyonepassword-3.9.0/pyonepassword/account.py
+drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-04-07 01:06:19.896334 pyonepassword-3.9.0/pyonepassword/api/
+-rw-r--r--   0 zach       (502) staff       (20)        0 2023-02-07 19:47:51.000000 pyonepassword-3.9.0/pyonepassword/api/__init__.py
+-rw-r--r--   0 zach       (502) staff       (20)      460 2023-01-22 17:09:56.000000 pyonepassword-3.9.0/pyonepassword/api/authentication.py
+-rw-r--r--   0 zach       (502) staff       (20)      432 2023-01-22 17:09:56.000000 pyonepassword-3.9.0/pyonepassword/api/constants.py
+-rw-r--r--   0 zach       (502) staff       (20)      319 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/api/decorators.py
+-rw-r--r--   0 zach       (502) staff       (20)     1691 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/api/descriptor_types.py
+-rw-r--r--   0 zach       (502) staff       (20)     2874 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/api/exceptions.py
+-rw-r--r--   0 zach       (502) staff       (20)     2698 2023-03-28 00:38:01.000000 pyonepassword-3.9.0/pyonepassword/api/object_types.py
+-rw-r--r--   0 zach       (502) staff       (20)      512 2023-02-15 22:33:25.000000 pyonepassword-3.9.0/pyonepassword/api/validation.py
+drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-04-07 01:06:19.901316 pyonepassword-3.9.0/pyonepassword/data/
+-rw-r--r--   0 zach       (502) staff       (20)       50 2023-02-07 19:47:51.000000 pyonepassword-3.9.0/pyonepassword/data/__init__.py
+-rw-r--r--   0 zach       (502) staff       (20)      940 2023-03-27 23:10:38.000000 pyonepassword-3.9.0/pyonepassword/data/api_credential.json
+-rw-r--r--   0 zach       (502) staff       (20)     1552 2023-03-27 23:10:48.000000 pyonepassword-3.9.0/pyonepassword/data/bank_account.json
+-rw-r--r--   0 zach       (502) staff       (20)     3084 2023-03-27 23:10:49.000000 pyonepassword-3.9.0/pyonepassword/data/credit_card.json
+-rw-r--r--   0 zach       (502) staff       (20)      701 2023-03-27 23:10:42.000000 pyonepassword-3.9.0/pyonepassword/data/crypto_wallet.json
+-rw-r--r--   0 zach       (502) staff       (20)     1137 2023-03-27 23:10:45.000000 pyonepassword-3.9.0/pyonepassword/data/database.json
+-rw-r--r--   0 zach       (502) staff       (20)      198 2023-03-27 23:10:43.000000 pyonepassword-3.9.0/pyonepassword/data/document.json
+-rw-r--r--   0 zach       (502) staff       (20)     1384 2023-03-27 23:10:39.000000 pyonepassword-3.9.0/pyonepassword/data/driver_license.json
+-rw-r--r--   0 zach       (502) staff       (20)     3125 2023-03-27 23:10:50.000000 pyonepassword-3.9.0/pyonepassword/data/email_account.json
+-rw-r--r--   0 zach       (502) staff       (20)     5190 2023-03-27 23:10:39.000000 pyonepassword-3.9.0/pyonepassword/data/identity.json
+-rw-r--r--   0 zach       (502) staff       (20)      536 2023-03-27 23:10:40.000000 pyonepassword-3.9.0/pyonepassword/data/login.json
+-rw-r--r--   0 zach       (502) staff       (20)     1425 2023-03-27 23:10:41.000000 pyonepassword-3.9.0/pyonepassword/data/medical_record.json
+-rw-r--r--   0 zach       (502) staff       (20)     1064 2023-03-27 23:10:46.000000 pyonepassword-3.9.0/pyonepassword/data/membership.json
+-rw-r--r--   0 zach       (502) staff       (20)      941 2023-03-27 23:10:43.000000 pyonepassword-3.9.0/pyonepassword/data/outdoor_license.json
+-rw-r--r--   0 zach       (502) staff       (20)     1404 2023-03-27 23:10:46.000000 pyonepassword-3.9.0/pyonepassword/data/passport.json
+-rw-r--r--   0 zach       (502) staff       (20)      404 2023-03-27 23:10:50.000000 pyonepassword-3.9.0/pyonepassword/data/password.json
+-rw-r--r--   0 zach       (502) staff       (20)     1770 2023-03-27 23:10:44.000000 pyonepassword-3.9.0/pyonepassword/data/reward_program.json
+-rw-r--r--   0 zach       (502) staff       (20)      201 2023-03-27 23:10:51.000000 pyonepassword-3.9.0/pyonepassword/data/secure_note.json
+-rw-r--r--   0 zach       (502) staff       (20)     2222 2023-03-27 23:10:45.000000 pyonepassword-3.9.0/pyonepassword/data/server.json
+-rw-r--r--   0 zach       (502) staff       (20)      415 2023-03-27 23:10:48.000000 pyonepassword-3.9.0/pyonepassword/data/social_security_number.json
+-rw-r--r--   0 zach       (502) staff       (20)     2756 2023-03-27 23:10:41.000000 pyonepassword-3.9.0/pyonepassword/data/software_license.json
+-rw-r--r--   0 zach       (502) staff       (20)      309 2023-03-27 23:10:51.000000 pyonepassword-3.9.0/pyonepassword/data/ssh_key.json
+-rw-r--r--   0 zach       (502) staff       (20)      829 2023-03-27 23:10:51.000000 pyonepassword-3.9.0/pyonepassword/data/template-registry.json
+-rw-r--r--   0 zach       (502) staff       (20)     1165 2023-03-27 23:10:47.000000 pyonepassword-3.9.0/pyonepassword/data/wireless_router.json
+-rw-r--r--   0 zach       (502) staff       (20)      257 2022-06-22 00:58:09.000000 pyonepassword-3.9.0/pyonepassword/json.py
+-rw-r--r--   0 zach       (502) staff       (20)      268 2022-11-09 19:14:03.000000 pyonepassword-3.9.0/pyonepassword/logging.py
+-rw-r--r--   0 zach       (502) staff       (20)     4314 2022-06-22 00:58:09.000000 pyonepassword-3.9.0/pyonepassword/op_cli_version.py
+drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-04-07 01:06:19.903129 pyonepassword-3.9.0/pyonepassword/op_items/
+-rw-r--r--   0 zach       (502) staff       (20)      214 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/__init__.py
+-rw-r--r--   0 zach       (502) staff       (20)      676 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/_item_descriptor_registry.py
+-rw-r--r--   0 zach       (502) staff       (20)     1652 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/_item_list.py
+-rw-r--r--   0 zach       (502) staff       (20)     4693 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/_item_type_registry.py
+-rw-r--r--   0 zach       (502) staff       (20)     4506 2023-04-05 03:13:22.000000 pyonepassword-3.9.0/pyonepassword/op_items/_new_field_registry.py
+-rw-r--r--   0 zach       (502) staff       (20)     9342 2023-04-05 03:13:22.000000 pyonepassword-3.9.0/pyonepassword/op_items/_new_item.py
+-rw-r--r--   0 zach       (502) staff       (20)      907 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/field_registry.py
+drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-04-07 01:06:19.903798 pyonepassword-3.9.0/pyonepassword/op_items/fields_sections/
+-rw-r--r--   0 zach       (502) staff       (20)        0 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/fields_sections/__init__.py
+-rw-r--r--   0 zach       (502) staff       (20)     6801 2023-03-28 00:38:01.000000 pyonepassword-3.9.0/pyonepassword/op_items/fields_sections/_new_fields.py
+-rw-r--r--   0 zach       (502) staff       (20)      519 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/fields_sections/item_field.py
+-rw-r--r--   0 zach       (502) staff       (20)     1340 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/fields_sections/item_field_base.py
+-rw-r--r--   0 zach       (502) staff       (20)     3702 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/fields_sections/item_section.py
+drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-04-07 01:06:19.905786 pyonepassword-3.9.0/pyonepassword/op_items/item_types/
+-rw-r--r--   0 zach       (502) staff       (20)        0 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/item_types/__init__.py
+-rw-r--r--   0 zach       (502) staff       (20)     8829 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/item_types/_item_base.py
+-rw-r--r--   0 zach       (502) staff       (20)     1895 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/item_types/_item_descriptor_base.py
+-rw-r--r--   0 zach       (502) staff       (20)     3665 2023-04-07 01:05:30.000000 pyonepassword-3.9.0/pyonepassword/op_items/item_types/api_credential.py
+-rw-r--r--   0 zach       (502) staff       (20)     2550 2023-04-07 01:05:30.000000 pyonepassword-3.9.0/pyonepassword/op_items/item_types/credit_card.py
+-rw-r--r--   0 zach       (502) staff       (20)     8831 2023-03-28 00:38:01.000000 pyonepassword-3.9.0/pyonepassword/op_items/item_types/database.py
+-rw-r--r--   0 zach       (502) staff       (20)     1510 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/item_types/document.py
+-rw-r--r--   0 zach       (502) staff       (20)     1312 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/item_types/generic_item.py
+-rw-r--r--   0 zach       (502) staff       (20)      325 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/item_types/identity.py
+-rw-r--r--   0 zach       (502) staff       (20)     6746 2023-03-28 00:38:01.000000 pyonepassword-3.9.0/pyonepassword/op_items/item_types/login.py
+-rw-r--r--   0 zach       (502) staff       (20)     1885 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/item_types/password.py
+-rw-r--r--   0 zach       (502) staff       (20)     1599 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/pyonepassword/op_items/item_types/secure_note.py
+-rw-r--r--   0 zach       (502) staff       (20)     3373 2023-04-07 01:05:30.000000 pyonepassword-3.9.0/pyonepassword/op_items/item_types/server.py
+-rw-r--r--   0 zach       (502) staff       (20)     1758 2023-04-05 03:13:22.000000 pyonepassword-3.9.0/pyonepassword/op_items/item_types/ssh_key.py
+-rw-r--r--   0 zach       (502) staff       (20)     5533 2023-02-15 22:33:25.000000 pyonepassword-3.9.0/pyonepassword/op_items/item_validation_policy.py
+-rw-r--r--   0 zach       (502) staff       (20)      834 2023-01-22 17:09:56.000000 pyonepassword-3.9.0/pyonepassword/op_items/password_recipe.py
+-rw-r--r--   0 zach       (502) staff       (20)      519 2023-01-22 17:09:56.000000 pyonepassword-3.9.0/pyonepassword/op_items/template_directory.py
+-rw-r--r--   0 zach       (502) staff       (20)      898 2022-06-22 00:58:09.000000 pyonepassword-3.9.0/pyonepassword/op_items/totp.py
+-rw-r--r--   0 zach       (502) staff       (20)     1809 2023-04-05 03:13:22.000000 pyonepassword-3.9.0/pyonepassword/op_items/uuid.py
+-rw-r--r--   0 zach       (502) staff       (20)    11729 2023-02-15 22:33:25.000000 pyonepassword-3.9.0/pyonepassword/op_objects.py
+-rw-r--r--   0 zach       (502) staff       (20)     1710 2022-11-09 19:14:03.000000 pyonepassword-3.9.0/pyonepassword/opconfig_main.py
+-rw-r--r--   0 zach       (502) staff       (20)      184 2023-01-22 17:09:56.000000 pyonepassword-3.9.0/pyonepassword/pkg_resources.py
+-rw-r--r--   0 zach       (502) staff       (20)        0 2023-01-22 17:09:56.000000 pyonepassword-3.9.0/pyonepassword/py.typed
+-rw-r--r--   0 zach       (502) staff       (20)     6099 2023-03-14 23:01:20.000000 pyonepassword-3.9.0/pyonepassword/py_op_exceptions.py
+-rw-r--r--   0 zach       (502) staff       (20)    35790 2023-03-14 23:01:20.000000 pyonepassword-3.9.0/pyonepassword/pyonepassword.py
+-rw-r--r--   0 zach       (502) staff       (20)      972 2023-01-22 17:09:56.000000 pyonepassword-3.9.0/pyonepassword/version.py
+drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-04-07 01:06:19.895234 pyonepassword-3.9.0/pyonepassword.egg-info/
+-rw-r--r--   0 zach       (502) staff       (20)    10393 2023-04-07 01:06:19.000000 pyonepassword-3.9.0/pyonepassword.egg-info/PKG-INFO
+-rw-r--r--   0 zach       (502) staff       (20)     3946 2023-04-07 01:06:19.000000 pyonepassword-3.9.0/pyonepassword.egg-info/SOURCES.txt
+-rw-r--r--   0 zach       (502) staff       (20)        1 2023-04-07 01:06:19.000000 pyonepassword-3.9.0/pyonepassword.egg-info/dependency_links.txt
+-rw-r--r--   0 zach       (502) staff       (20)       62 2023-04-07 01:06:19.000000 pyonepassword-3.9.0/pyonepassword.egg-info/entry_points.txt
+-rw-r--r--   0 zach       (502) staff       (20)       54 2023-04-07 01:06:19.000000 pyonepassword-3.9.0/pyonepassword.egg-info/requires.txt
+-rw-r--r--   0 zach       (502) staff       (20)       14 2023-04-07 01:06:19.000000 pyonepassword-3.9.0/pyonepassword.egg-info/top_level.txt
+-rw-r--r--   0 zach       (502) staff       (20)      628 2023-04-07 01:06:19.909114 pyonepassword-3.9.0/setup.cfg
+-rw-r--r--   0 zach       (502) staff       (20)     2165 2023-01-22 17:09:56.000000 pyonepassword-3.9.0/setup.py
+drwxr-xr-x   0 zach       (502) staff       (20)        0 2023-04-07 01:06:19.908605 pyonepassword-3.9.0/tests/
+-rw-r--r--   0 zach       (502) staff       (20)        0 2023-02-07 19:53:31.000000 pyonepassword-3.9.0/tests/__init__.py
+-rw-r--r--   0 zach       (502) staff       (20)       54 2022-06-22 00:58:09.000000 pyonepassword-3.9.0/tests/conftest.py
+-rw-r--r--   0 zach       (502) staff       (20)     1765 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/tests/test_abstract_base_meta.py
+-rw-r--r--   0 zach       (502) staff       (20)     2088 2022-11-09 19:14:03.000000 pyonepassword-3.9.0/tests/test_account_list.py
+-rw-r--r--   0 zach       (502) staff       (20)     2334 2022-06-22 00:58:09.000000 pyonepassword-3.9.0/tests/test_cli_version.py
+-rw-r--r--   0 zach       (502) staff       (20)      806 2022-06-22 00:58:09.000000 pyonepassword-3.9.0/tests/test_datetime.py
+-rw-r--r--   0 zach       (502) staff       (20)     3684 2023-01-22 17:09:56.000000 pyonepassword-3.9.0/tests/test_document_delete.py
+-rw-r--r--   0 zach       (502) staff       (20)     2396 2022-06-22 01:21:11.000000 pyonepassword-3.9.0/tests/test_document_get.py
+-rw-r--r--   0 zach       (502) staff       (20)     2844 2023-02-15 22:33:25.000000 pyonepassword-3.9.0/tests/test_exports.py
+-rw-r--r--   0 zach       (502) staff       (20)     3652 2022-06-22 01:21:11.000000 pyonepassword-3.9.0/tests/test_group_get.py
+-rw-r--r--   0 zach       (502) staff       (20)     3334 2023-01-22 17:09:56.000000 pyonepassword-3.9.0/tests/test_item_delete.py
+-rw-r--r--   0 zach       (502) staff       (20)     6748 2023-03-12 00:12:37.000000 pyonepassword-3.9.0/tests/test_item_delete_multiple.py
+-rw-r--r--   0 zach       (502) staff       (20)     2046 2023-04-07 01:05:30.000000 pyonepassword-3.9.0/tests/test_item_errors.py
+-rw-r--r--   0 zach       (502) staff       (20)     9706 2023-01-22 17:09:56.000000 pyonepassword-3.9.0/tests/test_item_field.py
+-rw-r--r--   0 zach       (502) staff       (20)     5293 2023-03-14 04:31:28.000000 pyonepassword-3.9.0/tests/test_item_section.py
+-rw-r--r--   0 zach       (502) staff       (20)      501 2022-11-09 19:14:03.000000 pyonepassword-3.9.0/tests/test_op_cli.py
+-rw-r--r--   0 zach       (502) staff       (20)     8367 2023-02-15 22:33:25.000000 pyonepassword-3.9.0/tests/test_op_cli_config.py
+-rw-r--r--   0 zach       (502) staff       (20)      442 2023-01-22 17:09:56.000000 pyonepassword-3.9.0/tests/test_pyop_about.py
+-rw-r--r--   0 zach       (502) staff       (20)     3802 2022-06-22 01:21:11.000000 pyonepassword-3.9.0/tests/test_user_get.py
+-rw-r--r--   0 zach       (502) staff       (20)     6149 2022-06-22 01:21:11.000000 pyonepassword-3.9.0/tests/test_vault_get.py
```

### Comparing `pyonepassword-3.8.0/LICENSE` & `pyonepassword-3.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/PKG-INFO` & `pyonepassword-3.9.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyonepassword
-Version: 3.8.0
+Version: 3.9.0
 Summary: A python API to query a 1Password account using the 'op' command-line tool
 Home-page: https://github.com/zcutlip/pyonepassword
 Author: Zachary Cutlip
 License: MIT
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `pyonepassword-3.8.0/README.md` & `pyonepassword-3.9.0/README.md`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/__about__.py` & `pyonepassword-3.9.0/pyonepassword/__about__.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 __title__ = "pyonepassword"
-__version__ = "3.8.0"
+__version__ = "3.9.0"
 __summary__ = "A python API to query a 1Password account using the 'op' command-line tool"
 
 """
 See PEP 440 for version scheme
 https://www.python.org/dev/peps/pep-0440/#examples-of-compliant-version-schemes
 Examples:
```

### Comparing `pyonepassword-3.8.0/pyonepassword/__init__.py` & `pyonepassword-3.9.0/pyonepassword/__init__.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/_abc_meta.py` & `pyonepassword-3.9.0/pyonepassword/_abc_meta.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/_datetime.py` & `pyonepassword-3.9.0/pyonepassword/_datetime.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/_op_cli_argv.py` & `pyonepassword-3.9.0/pyonepassword/_op_cli_argv.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/_op_cli_config.py` & `pyonepassword-3.9.0/pyonepassword/_op_cli_config.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/_py_op_cli.py` & `pyonepassword-3.9.0/pyonepassword/_py_op_cli.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/_py_op_commands.py` & `pyonepassword-3.9.0/pyonepassword/_py_op_commands.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/_py_op_deprecation.py` & `pyonepassword-3.9.0/pyonepassword/_py_op_deprecation.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/account.py` & `pyonepassword-3.9.0/pyonepassword/account.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/api/descriptor_types.py` & `pyonepassword-3.9.0/pyonepassword/api/descriptor_types.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/api/exceptions.py` & `pyonepassword-3.9.0/pyonepassword/api/exceptions.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/api/object_types.py` & `pyonepassword-3.9.0/pyonepassword/api/object_types.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/api/validation.py` & `pyonepassword-3.9.0/pyonepassword/api/validation.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/api_credential.json` & `pyonepassword-3.9.0/pyonepassword/data/api_credential.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/bank_account.json` & `pyonepassword-3.9.0/pyonepassword/data/bank_account.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/credit_card.json` & `pyonepassword-3.9.0/pyonepassword/data/credit_card.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/crypto_wallet.json` & `pyonepassword-3.9.0/pyonepassword/data/crypto_wallet.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/database.json` & `pyonepassword-3.9.0/pyonepassword/data/database.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/driver_license.json` & `pyonepassword-3.9.0/pyonepassword/data/driver_license.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/email_account.json` & `pyonepassword-3.9.0/pyonepassword/data/email_account.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/identity.json` & `pyonepassword-3.9.0/pyonepassword/data/identity.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/login.json` & `pyonepassword-3.9.0/pyonepassword/data/login.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/medical_record.json` & `pyonepassword-3.9.0/pyonepassword/data/medical_record.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/membership.json` & `pyonepassword-3.9.0/pyonepassword/data/membership.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/outdoor_license.json` & `pyonepassword-3.9.0/pyonepassword/data/outdoor_license.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/passport.json` & `pyonepassword-3.9.0/pyonepassword/data/passport.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/reward_program.json` & `pyonepassword-3.9.0/pyonepassword/data/reward_program.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/server.json` & `pyonepassword-3.9.0/pyonepassword/data/server.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/software_license.json` & `pyonepassword-3.9.0/pyonepassword/data/software_license.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/template-registry.json` & `pyonepassword-3.9.0/pyonepassword/data/template-registry.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/data/wireless_router.json` & `pyonepassword-3.9.0/pyonepassword/data/wireless_router.json`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_cli_version.py` & `pyonepassword-3.9.0/pyonepassword/op_cli_version.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/_item_descriptor_registry.py` & `pyonepassword-3.9.0/pyonepassword/op_items/_item_descriptor_registry.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/_item_list.py` & `pyonepassword-3.9.0/pyonepassword/op_items/_item_list.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/_item_type_registry.py` & `pyonepassword-3.9.0/pyonepassword/op_items/_item_type_registry.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/_new_field_registry.py` & `pyonepassword-3.9.0/pyonepassword/op_items/_new_field_registry.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/_new_item.py` & `pyonepassword-3.9.0/pyonepassword/op_items/_new_item.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/field_registry.py` & `pyonepassword-3.9.0/pyonepassword/op_items/field_registry.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/fields_sections/_new_fields.py` & `pyonepassword-3.9.0/pyonepassword/op_items/fields_sections/_new_fields.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/fields_sections/item_field.py` & `pyonepassword-3.9.0/pyonepassword/op_items/fields_sections/item_field.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/fields_sections/item_field_base.py` & `pyonepassword-3.9.0/pyonepassword/op_items/fields_sections/item_field_base.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/fields_sections/item_section.py` & `pyonepassword-3.9.0/pyonepassword/op_items/fields_sections/item_section.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/item_types/_item_base.py` & `pyonepassword-3.9.0/pyonepassword/op_items/item_types/_item_base.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/item_types/_item_descriptor_base.py` & `pyonepassword-3.9.0/pyonepassword/op_items/item_types/_item_descriptor_base.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/item_types/api_credential.py` & `pyonepassword-3.9.0/pyonepassword/op_items/item_types/api_credential.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,9 @@
 import datetime
+from typing import Dict, Union
 
 from .._item_descriptor_registry import op_register_item_descriptor_type
 from .._item_type_registry import op_register_item_type
 from ._item_base import OPAbstractItem
 from ._item_descriptor_base import OPAbstractItemDescriptor
 
 
@@ -89,15 +90,15 @@
 """
 
 
 @op_register_item_type
 class OPAPICredentialItem(OPAbstractItem):
     CATEGORY = "API_CREDENTIAL"
 
-    def __init__(self, item_dict):
+    def __init__(self, item_dict: Union[Dict, str]):
         super().__init__(item_dict)
 
     @property
     def username(self):
         username = self.field_value_by_id("username")
         return username
```

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/item_types/credit_card.py` & `pyonepassword-3.9.0/pyonepassword/op_items/item_types/credit_card.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,7 +1,9 @@
+from typing import Dict, Union
+
 from .._item_descriptor_registry import op_register_item_descriptor_type
 from .._item_type_registry import op_register_item_type
 from ..fields_sections.item_field_base import OPItemField
 from ..fields_sections.item_section import OPSection
 from ._item_base import OPAbstractItem
 from ._item_descriptor_base import OPAbstractItemDescriptor
 
@@ -14,15 +16,15 @@
         super().__init__(item_dict)
 
 
 @op_register_item_type
 class OPCreditCardItem(OPAbstractItem):
     CATEGORY = "CREDIT_CARD"
 
-    def __init__(self, item_dict):
+    def __init__(self, item_dict: Union[Dict, str]):
         super().__init__(item_dict)
 
     def additional_details(self) -> OPSection:
         details = self.sections_by_label("Additional Details")[0]
         return details
 
     def addl_details_item(self, field_label: str):
```

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/item_types/database.py` & `pyonepassword-3.9.0/pyonepassword/op_items/item_types/database.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/item_types/document.py` & `pyonepassword-3.9.0/pyonepassword/op_items/item_types/document.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/item_types/generic_item.py` & `pyonepassword-3.9.0/pyonepassword/op_items/item_types/generic_item.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/item_types/login.py` & `pyonepassword-3.9.0/pyonepassword/op_items/item_types/login.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/item_types/password.py` & `pyonepassword-3.9.0/pyonepassword/op_items/item_types/password.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/item_types/secure_note.py` & `pyonepassword-3.9.0/pyonepassword/op_items/item_types/secure_note.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/item_types/ssh_key.py` & `pyonepassword-3.9.0/pyonepassword/op_items/item_types/ssh_key.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/item_validation_policy.py` & `pyonepassword-3.9.0/pyonepassword/op_items/item_validation_policy.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/password_recipe.py` & `pyonepassword-3.9.0/pyonepassword/op_items/password_recipe.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/template_directory.py` & `pyonepassword-3.9.0/pyonepassword/op_items/template_directory.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/totp.py` & `pyonepassword-3.9.0/pyonepassword/op_items/totp.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_items/uuid.py` & `pyonepassword-3.9.0/pyonepassword/op_items/uuid.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/op_objects.py` & `pyonepassword-3.9.0/pyonepassword/op_objects.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/opconfig_main.py` & `pyonepassword-3.9.0/pyonepassword/opconfig_main.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/py_op_exceptions.py` & `pyonepassword-3.9.0/pyonepassword/py_op_exceptions.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/pyonepassword.py` & `pyonepassword-3.9.0/pyonepassword/pyonepassword.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword/version.py` & `pyonepassword-3.9.0/pyonepassword/version.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/pyonepassword.egg-info/PKG-INFO` & `pyonepassword-3.9.0/pyonepassword.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyonepassword
-Version: 3.8.0
+Version: 3.9.0
 Summary: A python API to query a 1Password account using the 'op' command-line tool
 Home-page: https://github.com/zcutlip/pyonepassword
 Author: Zachary Cutlip
 License: MIT
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `pyonepassword-3.8.0/pyonepassword.egg-info/SOURCES.txt` & `pyonepassword-3.9.0/pyonepassword.egg-info/SOURCES.txt`

 * *Files 5% similar despite different names*

```diff
@@ -103,22 +103,12 @@
 tests/test_exports.py
 tests/test_group_get.py
 tests/test_item_delete.py
 tests/test_item_delete_multiple.py
 tests/test_item_errors.py
 tests/test_item_field.py
 tests/test_item_section.py
-tests/test_misc.py
 tests/test_op_cli.py
 tests/test_op_cli_config.py
 tests/test_pyop_about.py
 tests/test_user_get.py
-tests/test_vault_get.py
-tests/test_item_get/__init__.py
-tests/test_item_get/test_item_get_api_cred.py
-tests/test_item_get/test_item_get_credit_card.py
-tests/test_item_get/test_item_get_login.py
-tests/test_item_get/test_item_get_password.py
-tests/test_item_get/test_item_get_secure_note.py
-tests/test_item_get/test_item_get_server.py
-tests/test_item_get/test_item_get_ssh_keys.py
-tests/test_item_get/test_item_get_totp.py
+tests/test_vault_get.py
```

### Comparing `pyonepassword-3.8.0/setup.cfg` & `pyonepassword-3.9.0/setup.cfg`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/setup.py` & `pyonepassword-3.9.0/setup.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/tests/test_abstract_base_meta.py` & `pyonepassword-3.9.0/tests/test_abstract_base_meta.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/tests/test_account_list.py` & `pyonepassword-3.9.0/tests/test_account_list.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/tests/test_cli_version.py` & `pyonepassword-3.9.0/tests/test_cli_version.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/tests/test_datetime.py` & `pyonepassword-3.9.0/tests/test_datetime.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/tests/test_document_delete.py` & `pyonepassword-3.9.0/tests/test_document_delete.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/tests/test_document_get.py` & `pyonepassword-3.9.0/tests/test_document_get.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/tests/test_exports.py` & `pyonepassword-3.9.0/tests/test_exports.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/tests/test_group_get.py` & `pyonepassword-3.9.0/tests/test_group_get.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/tests/test_item_delete.py` & `pyonepassword-3.9.0/tests/test_item_delete.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/tests/test_item_delete_multiple.py` & `pyonepassword-3.9.0/tests/test_item_delete_multiple.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/tests/test_item_errors.py` & `pyonepassword-3.9.0/tests/test_item_errors.py`

 * *Files 13% similar despite different names*

```diff
@@ -3,27 +3,24 @@
 from typing import TYPE_CHECKING
 
 import pytest
 
 from pyonepassword.api.exceptions import (
     OPFieldNotFoundException,
     OPInvalidItemException,
+    OPItemFieldCollisionException,
     OPSectionCollisionException,
     OPUnknownItemTypeException
 )
+from pyonepassword.api.object_types import OPLoginItem
 from pyonepassword.op_items import OPItemFactory
-from pyonepassword.op_items.fields_sections.item_section import (
-    OPItemFieldCollisionException
-)
 
 if TYPE_CHECKING:
-    from pyonepassword import OP
-    from pyonepassword.api.object_types import OPLoginItem
-
     from .fixtures.invalid_data import InvalidData
+    from .fixtures.valid_data import ValidData
 
 
 # ensure HOME env variable is set, and there's a valid op config present
 pytestmark = pytest.mark.usefixtures("valid_op_cli_config_homedir")
 
 
 def test_unknown_item_type_01(invalid_data):
@@ -34,19 +31,18 @@
 
 def test_malformed_item_json_01(invalid_data):
     malformed_json = invalid_data.data_for_name("malformed-item-json")
     with pytest.raises(OPInvalidItemException):
         _ = OPItemFactory.op_item(malformed_json)
 
 
-def test_item_field_not_found_01(signed_in_op: OP):
-    item_name = "Example Login 1"
-    vault = "Test Data"
-    result: OPLoginItem
-    result = signed_in_op.item_get(item_name, vault=vault)
+def test_item_field_not_found_01(valid_data: ValidData):
+    item_dict = valid_data.data_for_name("example-login-1")
+    result = OPLoginItem(item_dict)
+
     with pytest.raises(OPFieldNotFoundException):
         result.field_by_id("Non-existent-field")
 
 
 def test_item_field_collision_01(invalid_data):
     field_collision_json = invalid_data.data_for_name("field-collision")
     with pytest.raises(OPItemFieldCollisionException):
```

### Comparing `pyonepassword-3.8.0/tests/test_item_field.py` & `pyonepassword-3.9.0/tests/test_item_field.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/tests/test_item_section.py` & `pyonepassword-3.9.0/tests/test_item_section.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/tests/test_op_cli_config.py` & `pyonepassword-3.9.0/tests/test_op_cli_config.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/tests/test_user_get.py` & `pyonepassword-3.9.0/tests/test_user_get.py`

 * *Files identical despite different names*

### Comparing `pyonepassword-3.8.0/tests/test_vault_get.py` & `pyonepassword-3.9.0/tests/test_vault_get.py`

 * *Files identical despite different names*

