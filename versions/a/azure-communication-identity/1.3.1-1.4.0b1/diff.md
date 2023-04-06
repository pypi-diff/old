# Comparing `tmp/azure-communication-identity-1.3.1.zip` & `tmp/azure-communication-identity-1.4.0b1.zip`

## zipinfo {}

```diff
@@ -1,91 +1,92 @@
-Zip file size: 114373 bytes, number of entries: 89
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-31 11:54 azure-communication-identity-1.3.1/
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-31 11:54 azure-communication-identity-1.3.1/samples/
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-31 11:54 azure-communication-identity-1.3.1/tests/
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure_communication_identity.egg-info/
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure/
--rw-rw-r--  2.0 unx      206 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/MANIFEST.in
--rw-rw-r--  2.0 unx     8981 b- defN 22-Oct-31 11:54 azure-communication-identity-1.3.1/PKG-INFO
--rw-rw-r--  2.0 unx     3885 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/CHANGELOG.md
--rw-rw-r--  2.0 unx     1073 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/LICENSE
--rw-rw-r--  2.0 unx       38 b- defN 22-Oct-31 11:54 azure-communication-identity-1.3.1/setup.cfg
--rw-rw-r--  2.0 unx     2735 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/setup.py
--rw-rw-r--  2.0 unx     8084 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/README.md
--rw-rw-r--  2.0 unx    11256 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/samples/identity_samples_async.py
--rw-rw-r--  2.0 unx    10269 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/samples/identity_samples.py
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-31 11:54 azure-communication-identity-1.3.1/tests/_shared/
--rw-rw-r--  2.0 unx     1100 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/asynctestcase.py
--rw-rw-r--  2.0 unx    18835 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/test_communication_identity_client.py
--rw-rw-r--  2.0 unx    11524 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/test_user_credential_async_with_context_manager.py
--rw-rw-r--  2.0 unx     2231 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/test_utils.py
--rw-rw-r--  2.0 unx    25964 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/test_communication_identity_client_async.py
--rw-rw-r--  2.0 unx     1005 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/utils.py
--rw-rw-r--  2.0 unx    10212 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/test_user_credential.py
--rw-rw-r--  2.0 unx    11168 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/test_user_credential_async.py
--rw-rw-r--  2.0 unx    10681 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/test_user_credential_with_context_manager.py
--rw-rw-r--  2.0 unx    11130 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/test_identifier_raw_id.py
--rw-rw-r--  2.0 unx     3161 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/testcase.py
--rw-rw-r--  2.0 unx     1074 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/_shared/asynctestcase.py
--rw-rw-r--  2.0 unx     2674 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/_shared/utils.py
--rw-rw-r--  2.0 unx      431 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/_shared/communication_service_preparer.py
--rw-rw-r--  2.0 unx      538 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/_shared/async_fake_token_credential.py
--rw-rw-r--  2.0 unx     3790 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/_shared/testcase.py
--rw-rw-r--  2.0 unx      527 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/_shared/fake_token_credential.py
--rw-rw-r--  2.0 unx     3139 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/_shared/helper.py
--rw-rw-r--  2.0 unx      325 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/tests/_shared/__init__.py
--rw-rw-r--  2.0 unx     8981 b- defN 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure_communication_identity.egg-info/PKG-INFO
--rw-rw-r--  2.0 unx        6 b- defN 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure_communication_identity.egg-info/top_level.txt
--rw-rw-r--  2.0 unx        1 b- defN 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure_communication_identity.egg-info/dependency_links.txt
--rw-rw-r--  2.0 unx     3344 b- defN 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure_communication_identity.egg-info/SOURCES.txt
--rw-rw-r--  2.0 unx       83 b- defN 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure_communication_identity.egg-info/requires.txt
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure/communication/
--rw-rw-r--  2.0 unx       65 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/__init__.py
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure/communication/identity/
--rw-rw-r--  2.0 unx       65 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/__init__.py
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure/communication/identity/_generated/
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure/communication/identity/_shared/
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure/communication/identity/aio/
--rw-rw-r--  2.0 unx      401 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_version.py
--rw-rw-r--  2.0 unx      685 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_utils.py
--rw-rw-r--  2.0 unx     9285 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_communication_identity_client.py
--rw-rw-r--  2.0 unx        0 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/py.typed
--rw-rw-r--  2.0 unx      423 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_api_versions.py
--rw-rw-r--  2.0 unx     1295 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/__init__.py
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure/communication/identity/_generated/models/
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure/communication/identity/_generated/operations/
--rw-rw-r--  2.0 unx     2695 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/_configuration.py
--rw-rw-r--  2.0 unx     1529 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/_patch.py
--rw-rw-r--  2.0 unx      843 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/_vendor.py
--rw-rw-r--  2.0 unx     3808 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/_client.py
--rw-rw-r--  2.0 unx    77452 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/_serialization.py
--rw-rw-r--  2.0 unx     3912 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/_communication_identity_client.py
--rw-rw-r--  2.0 unx      853 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/__init__.py
--rw-rw-r--  2.0 unx     9799 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/models/_models.py
--rw-rw-r--  2.0 unx    10287 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/models/_models_py3.py
--rw-rw-r--  2.0 unx      741 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/models/_communication_identity_client_enums.py
--rw-rw-r--  2.0 unx     1989 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/models/__init__.py
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-31 11:54 azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/operations/
--rw-rw-r--  2.0 unx     2712 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/_configuration.py
--rw-rw-r--  2.0 unx     1529 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/_patch.py
--rw-rw-r--  2.0 unx     3853 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/_client.py
--rw-rw-r--  2.0 unx     3758 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/_communication_identity_client.py
--rw-rw-r--  2.0 unx      853 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/__init__.py
--rw-rw-r--  2.0 unx    25338 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/operations/_operations.py
--rw-rw-r--  2.0 unx      674 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/operations/_patch.py
--rw-rw-r--  2.0 unx    15745 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/operations/_communication_identity_operations.py
--rw-rw-r--  2.0 unx      818 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/operations/__init__.py
--rw-rw-r--  2.0 unx    29808 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/operations/_operations.py
--rw-rw-r--  2.0 unx      674 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/operations/_patch.py
--rw-rw-r--  2.0 unx    21126 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/operations/_communication_identity_operations.py
--rw-rw-r--  2.0 unx      818 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_generated/operations/__init__.py
--rw-rw-r--  2.0 unx     5183 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_shared/utils.py
--rw-rw-r--  2.0 unx     3045 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_shared/policy.py
--rw-rw-r--  2.0 unx     1008 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_shared/utils_async.py
--rw-rw-r--  2.0 unx     8101 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_shared/models.py
--rw-rw-r--  2.0 unx     6682 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_shared/user_credential_async.py
--rw-rw-r--  2.0 unx     6391 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_shared/user_credential.py
--rw-rw-r--  2.0 unx      310 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/_shared/__init__.py
--rw-rw-r--  2.0 unx     9689 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/aio/_communication_identity_client_async.py
--rw-rw-r--  2.0 unx      438 b- defN 22-Oct-31 11:53 azure-communication-identity-1.3.1/azure/communication/identity/aio/__init__.py
-89 files, 453131 bytes uncompressed, 93921 bytes compressed:  79.3%
+Zip file size: 117162 bytes, number of entries: 90
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure/
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/samples/
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/tests/
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure_communication_identity.egg-info/
+-rw-rw-r--  2.0 unx     2722 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/setup.py
+-rw-rw-r--  2.0 unx       38 b- defN 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/setup.cfg
+-rw-rw-r--  2.0 unx     9043 b- defN 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/PKG-INFO
+-rw-rw-r--  2.0 unx      206 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/MANIFEST.in
+-rw-rw-r--  2.0 unx     4007 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/CHANGELOG.md
+-rw-rw-r--  2.0 unx       99 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/pyproject.toml
+-rw-rw-r--  2.0 unx     8157 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/README.md
+-rw-rw-r--  2.0 unx     1073 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/LICENSE
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure/communication/
+-rw-rw-r--  2.0 unx       65 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/__init__.py
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure/communication/identity/
+-rw-rw-r--  2.0 unx       65 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/__init__.py
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure/communication/identity/aio/
+-rw-rw-r--  2.0 unx      423 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_api_versions.py
+-rw-rw-r--  2.0 unx        0 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/py.typed
+-rw-rw-r--  2.0 unx      685 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_utils.py
+-rw-rw-r--  2.0 unx     9357 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_communication_identity_client.py
+-rw-rw-r--  2.0 unx     1411 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/__init__.py
+-rw-rw-r--  2.0 unx      403 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_version.py
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/operations/
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/models/
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/
+-rw-rw-r--  2.0 unx    77452 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_serialization.py
+-rw-rw-r--  2.0 unx      843 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_vendor.py
+-rw-rw-r--  2.0 unx     2695 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_configuration.py
+-rw-rw-r--  2.0 unx     1529 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_patch.py
+-rw-rw-r--  2.0 unx     3808 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_client.py
+-rw-rw-r--  2.0 unx     3912 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_communication_identity_client.py
+-rw-rw-r--  2.0 unx      853 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/__init__.py
+-rw-rw-r--  2.0 unx    29808 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/operations/_operations.py
+-rw-rw-r--  2.0 unx      674 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/operations/_patch.py
+-rw-rw-r--  2.0 unx    21126 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/operations/_communication_identity_operations.py
+-rw-rw-r--  2.0 unx      818 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/operations/__init__.py
+-rw-rw-r--  2.0 unx     9799 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/models/_models.py
+-rw-rw-r--  2.0 unx    10287 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/models/_models_py3.py
+-rw-rw-r--  2.0 unx      741 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/models/_communication_identity_client_enums.py
+-rw-rw-r--  2.0 unx     1989 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/models/__init__.py
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/operations/
+-rw-rw-r--  2.0 unx     2712 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/_configuration.py
+-rw-rw-r--  2.0 unx     1529 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/_patch.py
+-rw-rw-r--  2.0 unx     3853 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/_client.py
+-rw-rw-r--  2.0 unx     3758 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/_communication_identity_client.py
+-rw-rw-r--  2.0 unx      853 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/__init__.py
+-rw-rw-r--  2.0 unx    25338 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/operations/_operations.py
+-rw-rw-r--  2.0 unx      674 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/operations/_patch.py
+-rw-rw-r--  2.0 unx    15745 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/operations/_communication_identity_operations.py
+-rw-rw-r--  2.0 unx      818 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/operations/__init__.py
+-rw-rw-r--  2.0 unx     1008 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/utils_async.py
+-rw-rw-r--  2.0 unx     6391 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/user_credential.py
+-rw-rw-r--  2.0 unx     3045 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/policy.py
+-rw-rw-r--  2.0 unx      310 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/__init__.py
+-rw-rw-r--  2.0 unx     5265 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/utils.py
+-rw-rw-r--  2.0 unx     6682 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/user_credential_async.py
+-rw-rw-r--  2.0 unx    14820 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/models.py
+-rw-rw-r--  2.0 unx     9781 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/aio/_communication_identity_client_async.py
+-rw-rw-r--  2.0 unx      438 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/azure/communication/identity/aio/__init__.py
+-rw-rw-r--  2.0 unx    11256 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/samples/identity_samples_async.py
+-rw-rw-r--  2.0 unx    10269 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/samples/identity_samples.py
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/tests/_shared/
+-rw-rw-r--  2.0 unx     2231 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/test_utils.py
+-rw-rw-r--  2.0 unx    11168 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/test_user_credential_async.py
+-rw-rw-r--  2.0 unx    14335 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/test_communication_identity_client.py
+-rw-rw-r--  2.0 unx     3001 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/acs_identity_test_case.py
+-rw-rw-r--  2.0 unx    12225 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/test_user_credential_async_with_context_manager.py
+-rw-rw-r--  2.0 unx    10212 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/test_user_credential.py
+-rw-rw-r--  2.0 unx    21137 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/test_communication_identity_client_async.py
+-rw-rw-r--  2.0 unx     4175 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/conftest.py
+-rw-rw-r--  2.0 unx     1006 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/utils.py
+-rw-rw-r--  2.0 unx    11089 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/test_user_credential_with_context_manager.py
+-rw-rw-r--  2.0 unx    24148 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/test_identifier_raw_id.py
+-rw-rw-r--  2.0 unx      431 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/_shared/communication_service_preparer.py
+-rw-rw-r--  2.0 unx      538 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/_shared/async_fake_token_credential.py
+-rw-rw-r--  2.0 unx     4452 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/_shared/testcase.py
+-rw-rw-r--  2.0 unx      325 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/_shared/__init__.py
+-rw-rw-r--  2.0 unx     2674 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/_shared/utils.py
+-rw-rw-r--  2.0 unx      527 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/_shared/fake_token_credential.py
+-rw-rw-r--  2.0 unx     3139 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/_shared/helper.py
+-rw-rw-r--  2.0 unx     1074 b- defN 23-Apr-06 06:19 azure-communication-identity-1.4.0b1/tests/_shared/asynctestcase.py
+-rw-rw-r--  2.0 unx     3368 b- defN 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure_communication_identity.egg-info/SOURCES.txt
+-rw-rw-r--  2.0 unx        1 b- defN 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure_communication_identity.egg-info/dependency_links.txt
+-rw-rw-r--  2.0 unx     9043 b- defN 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure_communication_identity.egg-info/PKG-INFO
+-rw-rw-r--  2.0 unx       83 b- defN 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure_communication_identity.egg-info/requires.txt
+-rw-rw-r--  2.0 unx        6 b- defN 23-Apr-06 06:21 azure-communication-identity-1.4.0b1/azure_communication_identity.egg-info/top_level.txt
+90 files, 469021 bytes uncompressed, 96158 bytes compressed:  79.5%
```

## zipnote {}

```diff
@@ -1,268 +1,271 @@
-Filename: azure-communication-identity-1.3.1/
+Filename: azure-communication-identity-1.4.0b1/
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/samples/
+Filename: azure-communication-identity-1.4.0b1/azure/
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/
+Filename: azure-communication-identity-1.4.0b1/samples/
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure_communication_identity.egg-info/
+Filename: azure-communication-identity-1.4.0b1/tests/
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/
+Filename: azure-communication-identity-1.4.0b1/azure_communication_identity.egg-info/
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/MANIFEST.in
+Filename: azure-communication-identity-1.4.0b1/setup.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/PKG-INFO
+Filename: azure-communication-identity-1.4.0b1/setup.cfg
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/CHANGELOG.md
+Filename: azure-communication-identity-1.4.0b1/PKG-INFO
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/LICENSE
+Filename: azure-communication-identity-1.4.0b1/MANIFEST.in
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/setup.cfg
+Filename: azure-communication-identity-1.4.0b1/CHANGELOG.md
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/setup.py
+Filename: azure-communication-identity-1.4.0b1/pyproject.toml
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/README.md
+Filename: azure-communication-identity-1.4.0b1/README.md
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/samples/identity_samples_async.py
+Filename: azure-communication-identity-1.4.0b1/LICENSE
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/samples/identity_samples.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/_shared/
+Filename: azure-communication-identity-1.4.0b1/azure/__init__.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/asynctestcase.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/test_communication_identity_client.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/__init__.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/test_user_credential_async_with_context_manager.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/test_utils.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/test_communication_identity_client_async.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/aio/
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/utils.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_api_versions.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/test_user_credential.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/py.typed
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/test_user_credential_async.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_utils.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/test_user_credential_with_context_manager.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_communication_identity_client.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/test_identifier_raw_id.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/__init__.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/testcase.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_version.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/_shared/asynctestcase.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/operations/
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/_shared/utils.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/models/
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/_shared/communication_service_preparer.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/_shared/async_fake_token_credential.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_serialization.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/_shared/testcase.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_vendor.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/_shared/fake_token_credential.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_configuration.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/_shared/helper.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_patch.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/tests/_shared/__init__.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_client.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure_communication_identity.egg-info/PKG-INFO
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_communication_identity_client.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure_communication_identity.egg-info/top_level.txt
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/__init__.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure_communication_identity.egg-info/dependency_links.txt
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/operations/_operations.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure_communication_identity.egg-info/SOURCES.txt
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/operations/_patch.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure_communication_identity.egg-info/requires.txt
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/operations/_communication_identity_operations.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/operations/__init__.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/__init__.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/models/_models.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/models/_models_py3.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/__init__.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/models/_communication_identity_client_enums.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/models/__init__.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_shared/
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/operations/
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/aio/
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/_configuration.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_version.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/_patch.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_utils.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/_client.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_communication_identity_client.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/_communication_identity_client.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/py.typed
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/__init__.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_api_versions.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/operations/_operations.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/__init__.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/operations/_patch.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/models/
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/operations/_communication_identity_operations.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/operations/__init__.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/operations/
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/utils_async.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/_configuration.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/user_credential.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/_patch.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/policy.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/_vendor.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/__init__.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/_client.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/utils.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/_serialization.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/user_credential_async.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/_communication_identity_client.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/models.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/__init__.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/aio/_communication_identity_client_async.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/models/_models.py
+Filename: azure-communication-identity-1.4.0b1/azure/communication/identity/aio/__init__.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/models/_models_py3.py
+Filename: azure-communication-identity-1.4.0b1/samples/identity_samples_async.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/models/_communication_identity_client_enums.py
+Filename: azure-communication-identity-1.4.0b1/samples/identity_samples.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/models/__init__.py
+Filename: azure-communication-identity-1.4.0b1/tests/_shared/
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/operations/
+Filename: azure-communication-identity-1.4.0b1/tests/test_utils.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/_configuration.py
+Filename: azure-communication-identity-1.4.0b1/tests/test_user_credential_async.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/_patch.py
+Filename: azure-communication-identity-1.4.0b1/tests/test_communication_identity_client.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/_client.py
+Filename: azure-communication-identity-1.4.0b1/tests/acs_identity_test_case.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/_communication_identity_client.py
+Filename: azure-communication-identity-1.4.0b1/tests/test_user_credential_async_with_context_manager.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/__init__.py
+Filename: azure-communication-identity-1.4.0b1/tests/test_user_credential.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/operations/_operations.py
+Filename: azure-communication-identity-1.4.0b1/tests/test_communication_identity_client_async.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/operations/_patch.py
+Filename: azure-communication-identity-1.4.0b1/tests/conftest.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/operations/_communication_identity_operations.py
+Filename: azure-communication-identity-1.4.0b1/tests/utils.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/operations/__init__.py
+Filename: azure-communication-identity-1.4.0b1/tests/test_user_credential_with_context_manager.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/operations/_operations.py
+Filename: azure-communication-identity-1.4.0b1/tests/test_identifier_raw_id.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/operations/_patch.py
+Filename: azure-communication-identity-1.4.0b1/tests/_shared/communication_service_preparer.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/operations/_communication_identity_operations.py
+Filename: azure-communication-identity-1.4.0b1/tests/_shared/async_fake_token_credential.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_generated/operations/__init__.py
+Filename: azure-communication-identity-1.4.0b1/tests/_shared/testcase.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_shared/utils.py
+Filename: azure-communication-identity-1.4.0b1/tests/_shared/__init__.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_shared/policy.py
+Filename: azure-communication-identity-1.4.0b1/tests/_shared/utils.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_shared/utils_async.py
+Filename: azure-communication-identity-1.4.0b1/tests/_shared/fake_token_credential.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_shared/models.py
+Filename: azure-communication-identity-1.4.0b1/tests/_shared/helper.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_shared/user_credential_async.py
+Filename: azure-communication-identity-1.4.0b1/tests/_shared/asynctestcase.py
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_shared/user_credential.py
+Filename: azure-communication-identity-1.4.0b1/azure_communication_identity.egg-info/SOURCES.txt
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/_shared/__init__.py
+Filename: azure-communication-identity-1.4.0b1/azure_communication_identity.egg-info/dependency_links.txt
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/aio/_communication_identity_client_async.py
+Filename: azure-communication-identity-1.4.0b1/azure_communication_identity.egg-info/PKG-INFO
 Comment: 
 
-Filename: azure-communication-identity-1.3.1/azure/communication/identity/aio/__init__.py
+Filename: azure-communication-identity-1.4.0b1/azure_communication_identity.egg-info/requires.txt
+Comment: 
+
+Filename: azure-communication-identity-1.4.0b1/azure_communication_identity.egg-info/top_level.txt
 Comment: 
 
 Zip file comment:
```

## Comparing `azure-communication-identity-1.3.1/PKG-INFO` & `azure-communication-identity-1.4.0b1/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,33 +1,37 @@
 Metadata-Version: 2.1
 Name: azure-communication-identity
-Version: 1.3.1
+Version: 1.4.0b1
 Summary: Microsoft Azure Communication Identity Service Client Library for Python
 Home-page: https://github.com/Azure/azure-sdk-for-python
 Author: Microsoft Corporation
 Author-email: azuresdkengsysadmins@microsoft.com
 License: MIT License
 Project-URL: Bug Reports, https://github.com/Azure/azure-sdk-for-python/issues
 Project-URL: Source, https://github.com/Azure/azure-sdk-for-python
-Classifier: Development Status :: 5 - Production/Stable
+Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: License :: OSI Approved :: MIT License
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # Azure Communication Identity Package client library for Python
 
 Azure Communication Identity client package is intended to be used to setup the basics for opening a way to use Azure Communication Service offerings. This package helps to create identity user tokens to be used by other client packages such as chat, calling, sms.
 
-[Source code](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/communication/azure-communication-identity) | [Package (Pypi)](https://pypi.org/project/azure-communication-identity/) | [API reference documentation](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/communication/azure-communication-identity) | [Product documentation](https://docs.microsoft.com/azure/communication-services/quickstarts/access-tokens?pivots=programming-language-python)
+[Source code](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/communication/azure-communication-identity)
+| [Package (Pypi)](https://pypi.org/project/azure-communication-identity/)
+| [Package (Conda)](https://anaconda.org/microsoft/azure-communication/)
+| [API reference documentation](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/communication/azure-communication-identity)
+| [Product documentation](https://docs.microsoft.com/azure/communication-services/quickstarts/access-tokens?pivots=programming-language-python)
 
 ## _Disclaimer_
 
 _Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to https://github.com/Azure/azure-sdk-for-python/issues/20691_
 
 # Getting started
 ### Prerequisites
```

## Comparing `azure-communication-identity-1.3.1/CHANGELOG.md` & `azure-communication-identity-1.4.0b1/CHANGELOG.md`

 * *Files 4% similar despite different names*

```diff
@@ -1,9 +1,14 @@
 # Release History
 
+## 1.4.0b1 (2023-04-05)
+
+### Features Added
+- Added support for a new communication identifier `MicrosoftBotIdentifier`.
+
 ## 1.3.1 (2022-10-28)
 
 ### Bug Fixes
 
 - Fixed the logic of `PhoneNumberIdentifier` to always maintain the original phone number string whether it included the leading + sign or not.
 
 ## 1.3.0 (2022-10-13)
```

## Comparing `azure-communication-identity-1.3.1/LICENSE` & `azure-communication-identity-1.4.0b1/LICENSE`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/setup.py` & `azure-communication-identity-1.4.0b1/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -39,15 +39,15 @@
     url='https://github.com/Azure/azure-sdk-for-python',
     author='Microsoft Corporation',
     author_email='azuresdkengsysadmins@microsoft.com',
 
     license='MIT License',
     # ensure that the development status reflects the status of your package
     classifiers=[
-        "Development Status :: 5 - Production/Stable",
+        "Development Status :: 4 - Beta",
 
         'Programming Language :: Python',
         'Programming Language :: Python :: 3 :: Only',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.7',
         'Programming Language :: Python :: 3.8',
         'License :: OSI Approved :: MIT License',
```

## Comparing `azure-communication-identity-1.3.1/README.md` & `azure-communication-identity-1.4.0b1/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,16 @@
 # Azure Communication Identity Package client library for Python
 
 Azure Communication Identity client package is intended to be used to setup the basics for opening a way to use Azure Communication Service offerings. This package helps to create identity user tokens to be used by other client packages such as chat, calling, sms.
 
-[Source code](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/communication/azure-communication-identity) | [Package (Pypi)](https://pypi.org/project/azure-communication-identity/) | [API reference documentation](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/communication/azure-communication-identity) | [Product documentation](https://docs.microsoft.com/azure/communication-services/quickstarts/access-tokens?pivots=programming-language-python)
+[Source code](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/communication/azure-communication-identity)
+| [Package (Pypi)](https://pypi.org/project/azure-communication-identity/)
+| [Package (Conda)](https://anaconda.org/microsoft/azure-communication/)
+| [API reference documentation](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/communication/azure-communication-identity)
+| [Product documentation](https://docs.microsoft.com/azure/communication-services/quickstarts/access-tokens?pivots=programming-language-python)
 
 ## _Disclaimer_
 
 _Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to https://github.com/Azure/azure-sdk-for-python/issues/20691_
 
 # Getting started
 ### Prerequisites
```

## Comparing `azure-communication-identity-1.3.1/samples/identity_samples_async.py` & `azure-communication-identity-1.4.0b1/samples/identity_samples_async.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/samples/identity_samples.py` & `azure-communication-identity-1.4.0b1/samples/identity_samples.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/tests/asynctestcase.py` & `azure-communication-identity-1.4.0b1/tests/_shared/asynctestcase.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,28 +1,26 @@
-
 # coding: utf-8
 # -------------------------------------------------------------------------
 # Copyright (c) Microsoft Corporation. All rights reserved.
 # Licensed under the MIT License. See License.txt in the project root for
 # license information.
 # --------------------------------------------------------------------------
 import functools
 import asyncio
 from azure_devtools.scenario_tests.utilities import trim_kwargs_from_test_function
-from testcase import CommunicationIdentityTestCase
-
+from .testcase import CommunicationTestCase
 
-class AsyncCommunicationIdentityTestCase(CommunicationIdentityTestCase):
+class AsyncCommunicationTestCase(CommunicationTestCase):
 
     @staticmethod
     def await_prepared_test(test_fn):
         """Synchronous wrapper for async test methods. Used to avoid making changes
         upstream to AbstractPreparer (which doesn't await the functions it wraps)
         """
 
         @functools.wraps(test_fn)
         def run(test_class_instance, *args, **kwargs):
             trim_kwargs_from_test_function(test_fn, kwargs)
             loop = asyncio.get_event_loop()
             return loop.run_until_complete(test_fn(test_class_instance, **kwargs))
 
-        return run
+        return run
```

## Comparing `azure-communication-identity-1.3.1/tests/test_user_credential_async_with_context_manager.py` & `azure-communication-identity-1.4.0b1/tests/test_user_credential_async_with_context_manager.py`

 * *Files 2% similar despite different names*

```diff
@@ -69,14 +69,29 @@
         async with credential:
             access_token = await credential.get_token()
 
         refresher.assert_called_once()
         assert refreshed_token == access_token.token
 
     @pytest.mark.asyncio
+    async def test_refresher_should_be_called_immediately_with_expired_token_and_proactive_refresh(self):
+        refreshed_token = generate_token_with_custom_expiry(10 * 60)
+        refresher = MagicMock(
+            return_value=self.get_completed_future(create_access_token(refreshed_token)))
+        expired_token = generate_token_with_custom_expiry(-(5 * 60))
+
+        credential = CommunicationTokenCredential(
+            expired_token, token_refresher=refresher, proactive_refresh=True)
+        async with credential:
+            access_token = await credential.get_token()
+
+        refresher.assert_called_once()
+        assert refreshed_token == access_token.token
+
+    @pytest.mark.asyncio
     async def test_refresher_should_not_be_called_before_expiring_time(self):
         initial_token = generate_token_with_custom_expiry(15 * 60)
         refreshed_token = generate_token_with_custom_expiry(10 * 60)
         refresher = MagicMock(
             return_value=create_access_token(refreshed_token))
 
         credential = CommunicationTokenCredential(
```

## Comparing `azure-communication-identity-1.3.1/tests/test_utils.py` & `azure-communication-identity-1.4.0b1/tests/test_utils.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/tests/utils.py` & `azure-communication-identity-1.4.0b1/tests/utils.py`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -14,8 +14,8 @@
     # type: (timedelta, datetime, float) -> bool
     utc_now = datetime.now(timezone.utc)
     token_expiration = parser.parse(token_expires_in)
     token_expiration_in_seconds = (token_expiration - utc_now).total_seconds()
     expected_seconds = expected_token_expiration.total_seconds();
     time_difference = abs(expected_seconds - token_expiration_in_seconds)
     allowed_time_difference = expected_seconds * allowed_deviation
-    return time_difference < allowed_time_difference
+    return time_difference < allowed_time_difference
```

## Comparing `azure-communication-identity-1.3.1/tests/test_user_credential.py` & `azure-communication-identity-1.4.0b1/tests/test_user_credential.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/tests/test_user_credential_async.py` & `azure-communication-identity-1.4.0b1/tests/test_user_credential_async.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/tests/test_user_credential_with_context_manager.py` & `azure-communication-identity-1.4.0b1/tests/test_user_credential_with_context_manager.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,25 +1,22 @@
 # -------------------------------------------------------------------------
 # Copyright (c) Microsoft Corporation. All rights reserved.
 # Licensed under the MIT License. See License.txt in the project root for
 # license information.
 # --------------------------------------------------------------------------
-from typing import Type
-import platform
 import pytest
 from unittest import TestCase
 try:
     from unittest.mock import MagicMock, patch
 except ImportError:  # python < 3.3
     from mock import MagicMock, patch  # type: ignore
 import azure.communication.identity._shared.user_credential as user_credential
 from azure.communication.identity._shared.user_credential import CommunicationTokenCredential
 from azure.communication.identity._shared.utils import create_access_token
 from azure.communication.identity._shared.utils import get_current_utc_as_int
-from datetime import timedelta
 from _shared.helper import generate_token_with_custom_expiry_epoch, generate_token_with_custom_expiry
 
 
 class TestCommunicationTokenCredential(TestCase):
 
     @classmethod
     def setUpClass(cls):
@@ -59,14 +56,22 @@
         refresher = MagicMock(
             return_value=create_access_token(self.sample_token))
         with CommunicationTokenCredential(self.expired_token, token_refresher=refresher) as credential:
             access_token = credential.get_token()
         refresher.assert_called_once()
         self.assertEqual(access_token.token, self.sample_token)
 
+    def test_communicationtokencredential_token_expired_refresh_called_with_proactive_refresh(self):
+        refresher = MagicMock(
+            return_value=create_access_token(self.sample_token))
+        with CommunicationTokenCredential(self.expired_token, token_refresher=refresher, proactive_refresh=True) as credential:
+            access_token = credential.get_token()
+        refresher.assert_called_once()
+        self.assertEqual(access_token.token, self.sample_token)
+
     def test_communicationtokencredential_raises_if_refresher_returns_expired_token(self):
         refresher = MagicMock(
             return_value=create_access_token(self.expired_token))
         with CommunicationTokenCredential(self.expired_token, token_refresher=refresher) as credential:
             with self.assertRaises(ValueError):
                 credential.get_token()
             self.assertEqual(refresher.call_count, 1)
```

## Comparing `azure-communication-identity-1.3.1/tests/testcase.py` & `azure-communication-identity-1.4.0b1/tests/acs_identity_test_case.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,60 +1,55 @@
-
 # -------------------------------------------------------------------------
 # Copyright (c) Microsoft Corporation. All rights reserved.
 # Licensed under the MIT License. See License.txt in the project root for
 # license information.
 # --------------------------------------------------------------------------
 import os
+from devtools_testutils import AzureRecordedTestCase, is_live
 
 from azure.communication.identity._shared.utils import parse_connection_str
-from _shared.testcase import CommunicationTestCase
 from msal import PublicClientApplication
 
-class CommunicationIdentityTestCase(CommunicationTestCase):
-    
-    def __init__(self, method_name, *args, **kwargs):
-        super(CommunicationIdentityTestCase, self).__init__(method_name, *args, **kwargs)
-
+class ACSIdentityTestCase(AzureRecordedTestCase):
     def setUp(self):
-        super(CommunicationIdentityTestCase, self).setUp()
-        if self.is_playback():
+        if is_live():
+            self.connection_str = os.getenv('COMMUNICATION_LIVETEST_DYNAMIC_CONNECTION_STRING')
+            self.m365_client_id = os.getenv('COMMUNICATION_M365_APP_ID')
+            self.m365_aad_authority = os.getenv('COMMUNICATION_M365_AAD_AUTHORITY')
+            self.m365_aad_tenant = os.getenv('COMMUNICATION_M365_AAD_TENANT')
+            self.msal_username = os.getenv('COMMUNICATION_MSAL_USERNAME')
+            self.msal_password = os.getenv('COMMUNICATION_MSAL_PASSWORD')
+            self.expired_teams_token = os.getenv('COMMUNICATION_EXPIRED_TEAMS_TOKEN')
+            self.endpoint, _ = parse_connection_str(self.connection_str)
+            self._resource_name = self.endpoint.split(".")[0]
+            self.skip_get_token_for_teams_user_tests = os.getenv('SKIP_INT_IDENTITY_EXCHANGE_TOKEN_TEST')
+        else:
             self.connection_str = "endpoint=https://sanitized.communication.azure.com/;accesskey=fake==="
+            self.endpoint, _ = parse_connection_str(self.connection_str)
             self.m365_client_id = "sanitized"
             self.m365_aad_authority = "sanitized"
             self.m365_aad_tenant = "sanitized"
-            self.msal_username = "sanitized" 
+            self.msal_username = "sanitized"
             self.msal_password = "sanitized"
             self.expired_teams_token = "sanitized"
-            self.skip_get_token_for_teams_user_tests = "false"
-        else:
-            self.connection_str = os.getenv('COMMUNICATION_LIVETEST_DYNAMIC_CONNECTION_STRING')
-            self.m365_client_id = os.getenv('COMMUNICATION_M365_APP_ID') 
-            self.m365_aad_authority = os.getenv('COMMUNICATION_M365_AAD_AUTHORITY') 
-            self.m365_aad_tenant = os.getenv('COMMUNICATION_M365_AAD_TENANT')
-            self.msal_username = os.getenv('COMMUNICATION_MSAL_USERNAME') 
-            self.msal_password = os.getenv('COMMUNICATION_MSAL_PASSWORD')
-            self.expired_teams_token = os.getenv('COMMUNICATION_EXPIRED_TEAMS_TOKEN')  
-            endpoint, _ = parse_connection_str(self.connection_str)
-            self._resource_name = endpoint.split(".")[0]
-            self.scrubber.register_name_pair(self._resource_name, "sanitized")
-            self.skip_get_token_for_teams_user_tests = os.getenv('SKIP_INT_IDENTITY_EXCHANGE_TOKEN_TEST') 
+            self.skip_get_token_for_teams_user_tests = "true"
 
     def generate_teams_user_aad_token(self):
         if self.is_playback():
             teams_user_aad_token = "sanitized"
             teams_user_oid = "sanitized"
         else:
             msal_app = PublicClientApplication(
                 client_id=self.m365_client_id,
                 authority="{}/{}".format(self.m365_aad_authority, self.m365_aad_tenant))
-            scopes = [ 
+            scopes = [
                 "https://auth.msft.communication.azure.com/Teams.ManageCalls",
                 "https://auth.msft.communication.azure.com/Teams.ManageChats"
             ]
-            result = msal_app.acquire_token_by_username_password(username=self.msal_username, password=self.msal_password, scopes=scopes)
+            result = msal_app.acquire_token_by_username_password(username=self.msal_username,
+                                                                 password=self.msal_password, scopes=scopes)
             teams_user_aad_token = result["access_token"]
             teams_user_oid = result["id_token_claims"]["oid"]
-        return (teams_user_aad_token, teams_user_oid) 
+        return teams_user_aad_token, teams_user_oid
 
     def skip_get_token_for_teams_user_test(self):
-        return str(self.skip_get_token_for_teams_user_tests).lower() == 'true'
+        return str(self.skip_get_token_for_teams_user_tests).lower() == 'true'
```

## Comparing `azure-communication-identity-1.3.1/tests/_shared/utils.py` & `azure-communication-identity-1.4.0b1/tests/_shared/utils.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/tests/_shared/async_fake_token_credential.py` & `azure-communication-identity-1.4.0b1/tests/_shared/async_fake_token_credential.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/tests/_shared/fake_token_credential.py` & `azure-communication-identity-1.4.0b1/tests/_shared/fake_token_credential.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/tests/_shared/helper.py` & `azure-communication-identity-1.4.0b1/tests/_shared/helper.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure_communication_identity.egg-info/PKG-INFO` & `azure-communication-identity-1.4.0b1/azure_communication_identity.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,33 +1,37 @@
 Metadata-Version: 2.1
 Name: azure-communication-identity
-Version: 1.3.1
+Version: 1.4.0b1
 Summary: Microsoft Azure Communication Identity Service Client Library for Python
 Home-page: https://github.com/Azure/azure-sdk-for-python
 Author: Microsoft Corporation
 Author-email: azuresdkengsysadmins@microsoft.com
 License: MIT License
 Project-URL: Bug Reports, https://github.com/Azure/azure-sdk-for-python/issues
 Project-URL: Source, https://github.com/Azure/azure-sdk-for-python
-Classifier: Development Status :: 5 - Production/Stable
+Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: License :: OSI Approved :: MIT License
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # Azure Communication Identity Package client library for Python
 
 Azure Communication Identity client package is intended to be used to setup the basics for opening a way to use Azure Communication Service offerings. This package helps to create identity user tokens to be used by other client packages such as chat, calling, sms.
 
-[Source code](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/communication/azure-communication-identity) | [Package (Pypi)](https://pypi.org/project/azure-communication-identity/) | [API reference documentation](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/communication/azure-communication-identity) | [Product documentation](https://docs.microsoft.com/azure/communication-services/quickstarts/access-tokens?pivots=programming-language-python)
+[Source code](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/communication/azure-communication-identity)
+| [Package (Pypi)](https://pypi.org/project/azure-communication-identity/)
+| [Package (Conda)](https://anaconda.org/microsoft/azure-communication/)
+| [API reference documentation](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/communication/azure-communication-identity)
+| [Product documentation](https://docs.microsoft.com/azure/communication-services/quickstarts/access-tokens?pivots=programming-language-python)
 
 ## _Disclaimer_
 
 _Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to https://github.com/Azure/azure-sdk-for-python/issues/20691_
 
 # Getting started
 ### Prerequisites
```

## Comparing `azure-communication-identity-1.3.1/azure_communication_identity.egg-info/SOURCES.txt` & `azure-communication-identity-1.4.0b1/azure_communication_identity.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 CHANGELOG.md
 LICENSE
 MANIFEST.in
 README.md
+pyproject.toml
 setup.py
 azure/__init__.py
 azure/communication/__init__.py
 azure/communication/identity/__init__.py
 azure/communication/identity/_api_versions.py
 azure/communication/identity/_communication_identity_client.py
 azure/communication/identity/_utils.py
@@ -47,24 +48,24 @@
 azure_communication_identity.egg-info/PKG-INFO
 azure_communication_identity.egg-info/SOURCES.txt
 azure_communication_identity.egg-info/dependency_links.txt
 azure_communication_identity.egg-info/requires.txt
 azure_communication_identity.egg-info/top_level.txt
 samples/identity_samples.py
 samples/identity_samples_async.py
-tests/asynctestcase.py
+tests/acs_identity_test_case.py
+tests/conftest.py
 tests/test_communication_identity_client.py
 tests/test_communication_identity_client_async.py
 tests/test_identifier_raw_id.py
 tests/test_user_credential.py
 tests/test_user_credential_async.py
 tests/test_user_credential_async_with_context_manager.py
 tests/test_user_credential_with_context_manager.py
 tests/test_utils.py
-tests/testcase.py
 tests/utils.py
 tests/_shared/__init__.py
 tests/_shared/async_fake_token_credential.py
 tests/_shared/asynctestcase.py
 tests/_shared/communication_service_preparer.py
 tests/_shared/fake_token_credential.py
 tests/_shared/helper.py
```

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_utils.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_utils.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_communication_identity_client.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_communication_identity_client.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,53 +1,53 @@
 # coding=utf-8
 # ------------------------------------
 # Copyright (c) Microsoft Corporation.
 # Licensed under the MIT License.
 # ------------------------------------
 
-from typing import TYPE_CHECKING, Any, Tuple
+from typing import TYPE_CHECKING, Any, Tuple, Union
 
 from azure.core.tracing.decorator import distributed_trace
 from azure.core.credentials import AccessToken
 
 from ._generated._communication_identity_client\
     import CommunicationIdentityClient as CommunicationIdentityClientGen
 from ._shared.utils import parse_connection_str, get_authentication_policy
 from ._shared.models import CommunicationUserIdentifier
 from ._version import SDK_MONIKER
 from ._api_versions import DEFAULT_VERSION
 from ._utils import convert_timedelta_to_mins
 
 if TYPE_CHECKING:
-    from azure.core.credentials import TokenCredential
+    from azure.core.credentials import TokenCredential, AzureKeyCredential
     from ._generated.models import CommunicationTokenScope
 
 
 class CommunicationIdentityClient(object):
     """Azure Communication Services Identity client.
 
     :param str endpoint:
         The endpoint url for Azure Communication Service resource.
-    :param TokenCredential credential:
-        The TokenCredential we use to authenticate against the service.
+    :param Union[TokenCredential, AzureKeyCredential] credential:
+        The credential we use to authenticate against the service.
     :keyword api_version: Azure Communication Identity API version.
-        Default value is "2022-06-01". Note that overriding this default value may result in unsupported behavior.
+        Default value is "2022-10-01". Note that overriding this default value may result in unsupported behavior.
     :paramtype api_version: str
 
     .. admonition:: Example:
 
         .. literalinclude:: ../samples/identity_samples.py
             :language: python
             :dedent: 8
     """
 
     def __init__(
             self,
             endpoint, # type: str
-            credential, # type: TokenCredential
+            credential, # type: Union[TokenCredential, AzureKeyCredential]
             **kwargs # type: Any
         ):
         # type: (...) -> None
         try:
             if not endpoint.lower().startswith('http'):
                 endpoint = "https://" + endpoint
         except AttributeError:
@@ -226,8 +226,8 @@
             "userId": user_object_id
         }
 
         return self._identity_service_client.communication_identity.exchange_teams_user_access_token(
             body=request_body,
             cls=lambda pr, u, e: AccessToken(u['token'], u['expiresOn']),
             **kwargs)
-        
+
```

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/__init__.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/__init__.py`

 * *Files 17% similar despite different names*

```diff
@@ -15,14 +15,16 @@
     CommunicationIdentifier,
     CommunicationIdentifierKind,
     CommunicationUserIdentifier,
     CommunicationUserProperties,
     identifier_from_raw_id,
     MicrosoftTeamsUserIdentifier,
     MicrosoftTeamsUserProperties,
+    MicrosoftBotProperties,
+    MicrosoftBotIdentifier,
     PhoneNumberIdentifier,
     PhoneNumberProperties,
     UnknownIdentifier
 )
 
 __all__ = [
     'CommunicationIdentityClient',
@@ -35,11 +37,13 @@
     'CommunicationIdentifier',
     'CommunicationIdentifierKind',
     'CommunicationUserIdentifier',
     'CommunicationUserProperties',
     'identifier_from_raw_id',
     'MicrosoftTeamsUserIdentifier',
     'MicrosoftTeamsUserProperties',
+    'MicrosoftBotIdentifier',
+    'MicrosoftBotProperties',
     'PhoneNumberIdentifier',
     'PhoneNumberProperties',
     'UnknownIdentifier'
 ]
```

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/_configuration.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_configuration.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/_patch.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_patch.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/_vendor.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_vendor.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/_client.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_client.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/_serialization.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_serialization.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/_communication_identity_client.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/_communication_identity_client.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/__init__.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/__init__.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/models/_models.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/models/_models.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/models/_models_py3.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/models/_models_py3.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/models/_communication_identity_client_enums.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/models/_communication_identity_client_enums.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/models/__init__.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/models/__init__.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/_configuration.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/_configuration.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/_patch.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/_patch.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/_client.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/_client.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/_communication_identity_client.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/_communication_identity_client.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/__init__.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/__init__.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/operations/_operations.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/operations/_operations.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/operations/_patch.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/operations/_patch.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/operations/_communication_identity_operations.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/operations/_communication_identity_operations.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/aio/operations/__init__.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/operations/__init__.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/operations/_operations.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/operations/_operations.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/operations/_patch.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/operations/_patch.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/operations/_communication_identity_operations.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/operations/_communication_identity_operations.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_generated/operations/__init__.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_generated/aio/operations/__init__.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_shared/utils.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/utils.py`

 * *Files 4% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 import calendar
 from typing import (cast,
                     Tuple,
                     Union,
                     )
 from datetime import datetime
 from msrest.serialization import TZ_UTC
-from azure.core.credentials import AccessToken
+from azure.core.credentials import AccessToken, AzureKeyCredential
 
 
 def _convert_datetime_to_utc_int(input_datetime):
     """
     Converts DateTime in local time to the Epoch in UTC in second.
 
     :param input_datetime: Input datetime
@@ -95,25 +95,25 @@
                            _convert_datetime_to_utc_int(datetime.fromtimestamp(payload['exp'], TZ_UTC)))
     except ValueError as val_error:
         raise ValueError(token_parse_err_msg) from val_error
 
 
 def get_authentication_policy(
         endpoint,  # type: str
-        credential,  # type: Union[TokenCredential, str]
+        credential,  # type: Union[TokenCredential, AzureKeyCredential, str]
         decode_url=False,  # type: bool
         is_async=False,  # type: bool
 ):
     # type: (...) -> Union[BearerTokenCredentialPolicy, HMACCredentialsPolicy]
     """Returns the correct authentication policy based
     on which credential is being passed.
     :param endpoint: The endpoint to which we are authenticating to.
     :type endpoint: str
     :param credential: The credential we use to authenticate to the service
-    :type credential: Union[TokenCredential, str]
+    :type credential: Union[TokenCredential, AzureKeyCredential, str]
     :param isAsync: For async clients there is a need to decode the url
     :type bool: isAsync or str
     :rtype: ~azure.core.pipeline.policies.BearerTokenCredentialPolicy or
     ~azure.communication.chat.shared.policy.HMACCredentialsPolicy
     """
 
     if credential is None:
@@ -122,13 +122,13 @@
         if is_async:
             from azure.core.pipeline.policies import AsyncBearerTokenCredentialPolicy
             return AsyncBearerTokenCredentialPolicy(
                 credential, "https://communication.azure.com//.default")
         from azure.core.pipeline.policies import BearerTokenCredentialPolicy
         return BearerTokenCredentialPolicy(
             credential, "https://communication.azure.com//.default")
-    if isinstance(credential, str):
+    if isinstance(credential, (AzureKeyCredential, str)):
         from .._shared.policy import HMACCredentialsPolicy
         return HMACCredentialsPolicy(endpoint, credential, decode_url=decode_url)
 
     raise TypeError("Unsupported credential: {}. Use an access token string to use HMACCredentialsPolicy"
                     "or a token credential from azure.identity".format(type(credential)))
```

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_shared/policy.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/policy.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_shared/utils_async.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/utils_async.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_shared/user_credential_async.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/user_credential_async.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/_shared/user_credential.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/_shared/user_credential.py`

 * *Files identical despite different names*

## Comparing `azure-communication-identity-1.3.1/azure/communication/identity/aio/_communication_identity_client_async.py` & `azure-communication-identity-1.4.0b1/azure/communication/identity/aio/_communication_identity_client_async.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,50 +3,51 @@
 # Copyright (c) Microsoft Corporation.
 # Licensed under the MIT License.
 # ------------------------------------
 from typing import TYPE_CHECKING, Any, List, Union, Tuple
 
 from azure.core.tracing.decorator_async import distributed_trace_async
 from azure.core.credentials import AccessToken
+from azure.core.credentials_async import AsyncTokenCredential
+from azure.core.credentials import AzureKeyCredential
 
 from .._generated.aio._communication_identity_client\
     import CommunicationIdentityClient as CommunicationIdentityClientGen
 from .._shared.utils import parse_connection_str, get_authentication_policy
 from .._shared.models import CommunicationUserIdentifier
 from .._version import SDK_MONIKER
 from .._api_versions import DEFAULT_VERSION
 from .._utils import convert_timedelta_to_mins
 
 if TYPE_CHECKING:
-    from azure.core.credentials_async import AsyncTokenCredential
     from .._generated.models import CommunicationTokenScope
 
 
 class CommunicationIdentityClient:
     """Azure Communication Services Identity client.
 
     :param str endpoint:
         The endpoint url for Azure Communication Service resource.
-    :param AsyncTokenCredential credential:
-        The AsyncTokenCredential we use to authenticate against the service.
+    :param Union[AsyncTokenCredential, AzureKeyCredential] credential:
+        The credential we use to authenticate against the service.
     :keyword api_version: Azure Communication Identity API version.
         Default value is "2022-06-01". Note that overriding this default value may result in unsupported behavior.
     :paramtype api_version: str
 
     .. admonition:: Example:
 
         .. literalinclude:: ../../samples/identity_samples_async.py
             :language: python
             :dedent: 8
     """
 
     def __init__(
             self,
             endpoint: str,
-            credential: 'AsyncTokenCredential',
+            credential: Union[AsyncTokenCredential, AzureKeyCredential],
             **kwargs
         ) -> None:
         try:
             if not endpoint.lower().startswith('http'):
                 endpoint = "https://" + endpoint
         except AttributeError:
             raise ValueError("Account URL must be a string.")
```

