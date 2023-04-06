# Comparing `tmp/encord-0.1.71.tar.gz` & `tmp/encord-0.1.72.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "encord-0.1.71.tar", max compression
+gzip compressed data, was "encord-0.1.72.tar", max compression
```

## Comparing `encord-0.1.71.tar` & `encord-0.1.72.tar`

### file list

```diff
@@ -1,73 +1,73 @@
--rw-r--r--   0        0        0    11330 2023-03-27 16:04:38.804113 encord-0.1.71/LICENSE
--rw-r--r--   0        0        0     2595 2023-03-27 16:04:38.804113 encord-0.1.71/README.md
--rw-r--r--   0        0        0       84 2023-03-27 16:04:38.804113 encord-0.1.71/cord/__init__.py
--rw-r--r--   0        0        0      158 2023-03-27 16:04:38.820113 encord-0.1.71/encord/__init__.py
--rw-r--r--   0        0        0      214 2023-03-27 16:04:38.820113 encord-0.1.71/encord/_version.py
--rw-r--r--   0        0        0    47243 2023-03-27 16:04:38.820113 encord-0.1.71/encord/client.py
--rw-r--r--   0        0        0    10826 2023-03-27 16:04:38.820113 encord-0.1.71/encord/configs.py
--rw-r--r--   0        0        0        0 2023-03-27 16:04:38.820113 encord-0.1.71/encord/constants/__init__.py
--rw-r--r--   0        0        0      810 2023-03-27 16:04:38.820113 encord-0.1.71/encord/constants/enums.py
--rw-r--r--   0        0        0     3211 2023-03-27 16:04:38.820113 encord-0.1.71/encord/constants/model.py
--rw-r--r--   0        0        0     6068 2023-03-27 16:04:38.820113 encord-0.1.71/encord/constants/model_weights.py
--rw-r--r--   0        0        0     1119 2023-03-27 16:04:38.820113 encord-0.1.71/encord/constants/string_constants.py
--rw-r--r--   0        0        0        0 2023-03-27 16:04:38.820113 encord-0.1.71/encord/constants/test/__init__.py
--rw-r--r--   0        0        0      634 2023-03-27 16:04:38.820113 encord-0.1.71/encord/constants/test/test_enums.py
--rw-r--r--   0        0        0    16035 2023-03-27 16:04:38.820113 encord-0.1.71/encord/dataset.py
--rw-r--r--   0        0        0     5452 2023-03-27 16:04:38.820113 encord-0.1.71/encord/exceptions.py
--rw-r--r--   0        0        0        0 2023-03-27 16:04:38.820113 encord-0.1.71/encord/http/__init__.py
--rw-r--r--   0        0        0      535 2023-03-27 16:04:38.820113 encord-0.1.71/encord/http/constants.py
--rw-r--r--   0        0        0     6275 2023-03-27 16:04:38.820113 encord-0.1.71/encord/http/error_utils.py
--rw-r--r--   0        0        0     5734 2023-03-27 16:04:38.820113 encord-0.1.71/encord/http/querier.py
--rw-r--r--   0        0        0      697 2023-03-27 16:04:38.820113 encord-0.1.71/encord/http/query_methods.py
--rw-r--r--   0        0        0     1691 2023-03-27 16:04:38.820113 encord-0.1.71/encord/http/request.py
--rw-r--r--   0        0        0     5880 2023-03-27 16:04:38.820113 encord-0.1.71/encord/http/utils.py
--rw-r--r--   0        0        0      340 2023-03-27 16:04:38.824113 encord-0.1.71/encord/objects/__init__.py
--rw-r--r--   0        0        0      145 2023-03-27 16:04:38.824113 encord-0.1.71/encord/objects/classification.py
--rw-r--r--   0        0        0    29710 2023-03-27 16:04:38.824113 encord-0.1.71/encord/objects/common.py
--rw-r--r--   0        0        0      172 2023-03-27 16:04:38.824113 encord-0.1.71/encord/objects/constants.py
--rw-r--r--   0        0        0     5631 2023-03-27 16:04:38.824113 encord-0.1.71/encord/objects/coordinates.py
--rw-r--r--   0        0        0     3419 2023-03-27 16:04:38.824113 encord-0.1.71/encord/objects/frames.py
--rw-r--r--   0        0        0    21036 2023-03-27 16:04:38.824113 encord-0.1.71/encord/objects/internal_helpers.py
--rw-r--r--   0        0        0   132198 2023-03-27 16:04:38.824113 encord-0.1.71/encord/objects/ontology_labels_impl.py
--rw-r--r--   0        0        0      137 2023-03-27 16:04:38.824113 encord-0.1.71/encord/objects/ontology_object.py
--rw-r--r--   0        0        0      148 2023-03-27 16:04:38.824113 encord-0.1.71/encord/objects/ontology_structure.py
--rw-r--r--   0        0        0      549 2023-03-27 16:04:38.824113 encord-0.1.71/encord/objects/project.py
--rw-r--r--   0        0        0     1240 2023-03-27 16:04:38.824113 encord-0.1.71/encord/objects/utils.py
--rw-r--r--   0        0        0     3430 2023-03-27 16:04:38.824113 encord-0.1.71/encord/ontology.py
--rw-r--r--   0        0        0        0 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/__init__.py
--rw-r--r--   0        0        0      982 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/api_key.py
--rw-r--r--   0        0        0     5377 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/base_orm.py
--rw-r--r--   0        0        0      111 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/cloud_integration.py
--rw-r--r--   0        0        0    32208 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/dataset.py
--rw-r--r--   0        0        0      828 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/dataset_with_user_role.py
--rw-r--r--   0        0        0      201 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/formatter.py
--rw-r--r--   0        0        0     1155 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/label_log.py
--rw-r--r--   0        0        0    11122 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/label_row.py
--rw-r--r--   0        0        0     1577 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/labeling_algorithm.py
--rw-r--r--   0        0        0     6688 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/model.py
--rw-r--r--   0        0        0      745 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/ontology.py
--rw-r--r--   0        0        0     8844 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/project.py
--rw-r--r--   0        0        0      625 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/project_api_key.py
--rw-r--r--   0        0        0      828 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/project_with_user_role.py
--rw-r--r--   0        0        0        0 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/test/__init__.py
--rw-r--r--   0        0        0      570 2023-03-27 16:04:38.824113 encord-0.1.71/encord/orm/test/test_dataset.py
--rw-r--r--   0        0        0    38214 2023-03-27 16:04:38.824113 encord-0.1.71/encord/project.py
--rw-r--r--   0        0        0        0 2023-03-27 16:04:38.824113 encord-0.1.71/encord/project_ontology/__init__.py
--rw-r--r--   0        0        0     1316 2023-03-27 16:04:38.824113 encord-0.1.71/encord/project_ontology/classification_attribute.py
--rw-r--r--   0        0        0      525 2023-03-27 16:04:38.824113 encord-0.1.71/encord/project_ontology/classification_option.py
--rw-r--r--   0        0        0      357 2023-03-27 16:04:38.824113 encord-0.1.71/encord/project_ontology/classification_type.py
--rw-r--r--   0        0        0      237 2023-03-27 16:04:38.824113 encord-0.1.71/encord/project_ontology/object_type.py
--rw-r--r--   0        0        0     9526 2023-03-27 16:04:38.824113 encord-0.1.71/encord/project_ontology/ontology.py
--rw-r--r--   0        0        0      630 2023-03-27 16:04:38.824113 encord-0.1.71/encord/project_ontology/ontology_classification.py
--rw-r--r--   0        0        0      683 2023-03-27 16:04:38.824113 encord-0.1.71/encord/project_ontology/ontology_object.py
--rw-r--r--   0        0        0    27803 2023-03-27 16:04:38.824113 encord-0.1.71/encord/user_client.py
--rw-r--r--   0        0        0        0 2023-03-27 16:04:38.824113 encord-0.1.71/encord/utilities/__init__.py
--rw-r--r--   0        0        0     4231 2023-03-27 16:04:38.824113 encord-0.1.71/encord/utilities/client_utilities.py
--rw-r--r--   0        0        0      253 2023-03-27 16:04:38.824113 encord-0.1.71/encord/utilities/common.py
--rw-r--r--   0        0        0     3270 2023-03-27 16:04:38.824113 encord-0.1.71/encord/utilities/label_utilities.py
--rw-r--r--   0        0        0      343 2023-03-27 16:04:38.824113 encord-0.1.71/encord/utilities/ontology_user.py
--rw-r--r--   0        0        0      578 2023-03-27 16:04:38.824113 encord-0.1.71/encord/utilities/project_user.py
--rw-r--r--   0        0        0      467 2023-03-27 16:04:38.824113 encord-0.1.71/encord/utilities/project_utilities.py
--rw-r--r--   0        0        0     1834 2023-03-27 16:04:38.824113 encord-0.1.71/pyproject.toml
--rw-r--r--   0        0        0     3717 2023-03-27 16:06:09.346474 encord-0.1.71/setup.py
--rw-r--r--   0        0        0     3719 2023-03-27 16:06:09.346892 encord-0.1.71/PKG-INFO
+-rw-r--r--   0        0        0    11330 2023-04-06 09:37:05.100408 encord-0.1.72/LICENSE
+-rw-r--r--   0        0        0     2595 2023-04-06 09:37:05.100408 encord-0.1.72/README.md
+-rw-r--r--   0        0        0       84 2023-04-06 09:37:05.100408 encord-0.1.72/cord/__init__.py
+-rw-r--r--   0        0        0      158 2023-04-06 09:37:05.112408 encord-0.1.72/encord/__init__.py
+-rw-r--r--   0        0        0      214 2023-04-06 09:37:05.112408 encord-0.1.72/encord/_version.py
+-rw-r--r--   0        0        0    47245 2023-04-06 09:37:05.116408 encord-0.1.72/encord/client.py
+-rw-r--r--   0        0        0    10826 2023-04-06 09:37:05.116408 encord-0.1.72/encord/configs.py
+-rw-r--r--   0        0        0        0 2023-04-06 09:37:05.116408 encord-0.1.72/encord/constants/__init__.py
+-rw-r--r--   0        0        0      810 2023-04-06 09:37:05.116408 encord-0.1.72/encord/constants/enums.py
+-rw-r--r--   0        0        0     3211 2023-04-06 09:37:05.116408 encord-0.1.72/encord/constants/model.py
+-rw-r--r--   0        0        0     6068 2023-04-06 09:37:05.116408 encord-0.1.72/encord/constants/model_weights.py
+-rw-r--r--   0        0        0     1119 2023-04-06 09:37:05.116408 encord-0.1.72/encord/constants/string_constants.py
+-rw-r--r--   0        0        0        0 2023-04-06 09:37:05.116408 encord-0.1.72/encord/constants/test/__init__.py
+-rw-r--r--   0        0        0      634 2023-04-06 09:37:05.116408 encord-0.1.72/encord/constants/test/test_enums.py
+-rw-r--r--   0        0        0    16035 2023-04-06 09:37:05.116408 encord-0.1.72/encord/dataset.py
+-rw-r--r--   0        0        0     5621 2023-04-06 09:37:05.116408 encord-0.1.72/encord/exceptions.py
+-rw-r--r--   0        0        0        0 2023-04-06 09:37:05.116408 encord-0.1.72/encord/http/__init__.py
+-rw-r--r--   0        0        0      535 2023-04-06 09:37:05.116408 encord-0.1.72/encord/http/constants.py
+-rw-r--r--   0        0        0     6275 2023-04-06 09:37:05.116408 encord-0.1.72/encord/http/error_utils.py
+-rw-r--r--   0        0        0     5999 2023-04-06 09:37:05.116408 encord-0.1.72/encord/http/querier.py
+-rw-r--r--   0        0        0      697 2023-04-06 09:37:05.116408 encord-0.1.72/encord/http/query_methods.py
+-rw-r--r--   0        0        0     1691 2023-04-06 09:37:05.116408 encord-0.1.72/encord/http/request.py
+-rw-r--r--   0        0        0     5880 2023-04-06 09:37:05.116408 encord-0.1.72/encord/http/utils.py
+-rw-r--r--   0        0        0      340 2023-04-06 09:37:05.116408 encord-0.1.72/encord/objects/__init__.py
+-rw-r--r--   0        0        0      145 2023-04-06 09:37:05.116408 encord-0.1.72/encord/objects/classification.py
+-rw-r--r--   0        0        0    29710 2023-04-06 09:37:05.116408 encord-0.1.72/encord/objects/common.py
+-rw-r--r--   0        0        0      172 2023-04-06 09:37:05.116408 encord-0.1.72/encord/objects/constants.py
+-rw-r--r--   0        0        0     5631 2023-04-06 09:37:05.116408 encord-0.1.72/encord/objects/coordinates.py
+-rw-r--r--   0        0        0     3419 2023-04-06 09:37:05.116408 encord-0.1.72/encord/objects/frames.py
+-rw-r--r--   0        0        0    21036 2023-04-06 09:37:05.116408 encord-0.1.72/encord/objects/internal_helpers.py
+-rw-r--r--   0        0        0   132198 2023-04-06 09:37:05.116408 encord-0.1.72/encord/objects/ontology_labels_impl.py
+-rw-r--r--   0        0        0      137 2023-04-06 09:37:05.116408 encord-0.1.72/encord/objects/ontology_object.py
+-rw-r--r--   0        0        0      148 2023-04-06 09:37:05.116408 encord-0.1.72/encord/objects/ontology_structure.py
+-rw-r--r--   0        0        0      549 2023-04-06 09:37:05.116408 encord-0.1.72/encord/objects/project.py
+-rw-r--r--   0        0        0     1240 2023-04-06 09:37:05.116408 encord-0.1.72/encord/objects/utils.py
+-rw-r--r--   0        0        0     3430 2023-04-06 09:37:05.116408 encord-0.1.72/encord/ontology.py
+-rw-r--r--   0        0        0        0 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/__init__.py
+-rw-r--r--   0        0        0      982 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/api_key.py
+-rw-r--r--   0        0        0     5377 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/base_orm.py
+-rw-r--r--   0        0        0      111 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/cloud_integration.py
+-rw-r--r--   0        0        0    32208 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/dataset.py
+-rw-r--r--   0        0        0      828 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/dataset_with_user_role.py
+-rw-r--r--   0        0        0      201 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/formatter.py
+-rw-r--r--   0        0        0     1155 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/label_log.py
+-rw-r--r--   0        0        0    11122 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/label_row.py
+-rw-r--r--   0        0        0     1577 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/labeling_algorithm.py
+-rw-r--r--   0        0        0     6688 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/model.py
+-rw-r--r--   0        0        0      745 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/ontology.py
+-rw-r--r--   0        0        0     8844 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/project.py
+-rw-r--r--   0        0        0      625 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/project_api_key.py
+-rw-r--r--   0        0        0      828 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/project_with_user_role.py
+-rw-r--r--   0        0        0        0 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/test/__init__.py
+-rw-r--r--   0        0        0      570 2023-04-06 09:37:05.116408 encord-0.1.72/encord/orm/test/test_dataset.py
+-rw-r--r--   0        0        0    38214 2023-04-06 09:37:05.116408 encord-0.1.72/encord/project.py
+-rw-r--r--   0        0        0        0 2023-04-06 09:37:05.116408 encord-0.1.72/encord/project_ontology/__init__.py
+-rw-r--r--   0        0        0     1316 2023-04-06 09:37:05.116408 encord-0.1.72/encord/project_ontology/classification_attribute.py
+-rw-r--r--   0        0        0      525 2023-04-06 09:37:05.116408 encord-0.1.72/encord/project_ontology/classification_option.py
+-rw-r--r--   0        0        0      357 2023-04-06 09:37:05.116408 encord-0.1.72/encord/project_ontology/classification_type.py
+-rw-r--r--   0        0        0      237 2023-04-06 09:37:05.116408 encord-0.1.72/encord/project_ontology/object_type.py
+-rw-r--r--   0        0        0     9526 2023-04-06 09:37:05.116408 encord-0.1.72/encord/project_ontology/ontology.py
+-rw-r--r--   0        0        0      630 2023-04-06 09:37:05.116408 encord-0.1.72/encord/project_ontology/ontology_classification.py
+-rw-r--r--   0        0        0      683 2023-04-06 09:37:05.116408 encord-0.1.72/encord/project_ontology/ontology_object.py
+-rw-r--r--   0        0        0    27803 2023-04-06 09:37:05.116408 encord-0.1.72/encord/user_client.py
+-rw-r--r--   0        0        0        0 2023-04-06 09:37:05.116408 encord-0.1.72/encord/utilities/__init__.py
+-rw-r--r--   0        0        0     4231 2023-04-06 09:37:05.116408 encord-0.1.72/encord/utilities/client_utilities.py
+-rw-r--r--   0        0        0      253 2023-04-06 09:37:05.116408 encord-0.1.72/encord/utilities/common.py
+-rw-r--r--   0        0        0     3270 2023-04-06 09:37:05.116408 encord-0.1.72/encord/utilities/label_utilities.py
+-rw-r--r--   0        0        0      343 2023-04-06 09:37:05.116408 encord-0.1.72/encord/utilities/ontology_user.py
+-rw-r--r--   0        0        0      578 2023-04-06 09:37:05.116408 encord-0.1.72/encord/utilities/project_user.py
+-rw-r--r--   0        0        0      467 2023-04-06 09:37:05.116408 encord-0.1.72/encord/utilities/project_utilities.py
+-rw-r--r--   0        0        0     1835 2023-04-06 09:37:05.120408 encord-0.1.72/pyproject.toml
+-rw-r--r--   0        0        0     3724 2023-04-06 09:38:22.446503 encord-0.1.72/setup.py
+-rw-r--r--   0        0        0     3726 2023-04-06 09:38:22.446895 encord-0.1.72/PKG-INFO
```

### Comparing `encord-0.1.71/LICENSE` & `encord-0.1.72/LICENSE`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/README.md` & `encord-0.1.72/README.md`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/client.py` & `encord-0.1.72/encord/client.py`

 * *Files 0% similar despite different names*

```diff
@@ -554,15 +554,15 @@
             ignore_errors,
         )
 
         res = self.add_private_data_to_dataset_get_result(upload_job_id)
 
         if res.status == LongPollingStatus.DONE:
             return AddPrivateDataResponse(dataset_data_list=res.data_hashes_with_titles)
-        if res.status == LongPollingStatus.ERROR:
+        elif res.status == LongPollingStatus.ERROR:
             raise encord.exceptions.EncordException(f"add_private_data_to_dataset errors occured {res.errors}")
         else:
             raise ValueError(f"res.status={res.status}, this should never happen")
 
     def add_private_data_to_dataset_start(
         self,
         integration_id: str,
```

### Comparing `encord-0.1.71/encord/configs.py` & `encord-0.1.72/encord/configs.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/constants/enums.py` & `encord-0.1.72/encord/constants/enums.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/constants/model.py` & `encord-0.1.72/encord/constants/model.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/constants/model_weights.py` & `encord-0.1.72/encord/constants/model_weights.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/constants/string_constants.py` & `encord-0.1.72/encord/constants/string_constants.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/constants/test/test_enums.py` & `encord-0.1.72/encord/constants/test/test_enums.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/dataset.py` & `encord-0.1.72/encord/dataset.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/exceptions.py` & `encord-0.1.72/encord/exceptions.py`

 * *Files 6% similar despite different names*

```diff
@@ -8,25 +8,29 @@
 #     http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 # License for the specific language governing permissions and limitations
 # under the License.
+import time
+from datetime import datetime, timezone
 
 
 class EncordException(Exception):
     """Base class for all exceptions."""
 
     def __init__(self, message):
         super().__init__(message)
         self.message = message
 
     def __str__(self):
-        return self.message
+        datetime_postfix = f"Error timestamp: {datetime.now(tz=timezone.utc).isoformat()}."
+
+        return f"{self.message} {datetime_postfix}"
 
 
 CordException = EncordException
 
 
 class InitialisationError(EncordException):
     """Exception thrown when API key fails to initialise."""
```

### Comparing `encord-0.1.71/encord/http/constants.py` & `encord-0.1.72/encord/http/constants.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/http/error_utils.py` & `encord-0.1.72/encord/http/error_utils.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/http/querier.py` & `encord-0.1.72/encord/http/querier.py`

 * *Files 6% similar despite different names*

```diff
@@ -10,14 +10,15 @@
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 # License for the specific language governing permissions and limitations
 # under the License.
 import dataclasses
 import logging
+import platform
 from contextlib import contextmanager
 from typing import Any, List, Optional, Type, TypeVar
 
 import requests
 import requests.exceptions
 from requests import Session
 from requests.adapters import HTTPAdapter
@@ -25,14 +26,15 @@
 
 from encord.configs import BaseConfig
 from encord.exceptions import *
 from encord.http.error_utils import check_error_response
 from encord.http.query_methods import QueryMethods
 from encord.http.request import Request
 from encord.orm.formatter import Formatter
+from encord._version import __version__ as encord_version
 
 logger = logging.getLogger(__name__)
 
 
 class Querier:
     """Querier for DB get/post requests."""
 
@@ -109,18 +111,24 @@
         res = self.execute(request, enable_logging)
 
         if res:
             return res
         else:
             raise RequestException("Setting %s with uid %s failed." % (db_object_type, uid))
 
+    @staticmethod
+    def _user_agent():
+        return f"Encord Python SDK {encord_version}; Python {platform.python_version()}"
+
     def request(self, method, db_object_type: Type[T], uid, timeout, payload=None):
         request = Request(method, db_object_type, uid, timeout, self._config.connect_timeout, payload)
 
         request.headers = self._config.define_headers(request.data)
+        request.headers["User-Agent"] = self._user_agent()
+
         return request
 
     def execute(self, request, enable_logging=True) -> Any:
         """Execute a request."""
         if enable_logging:
             logger.info("Request: %s", (request.data[:100] + "..") if len(request.data) > 100 else request.data)
```

### Comparing `encord-0.1.71/encord/http/query_methods.py` & `encord-0.1.72/encord/http/query_methods.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/http/request.py` & `encord-0.1.72/encord/http/request.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/http/utils.py` & `encord-0.1.72/encord/http/utils.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/objects/common.py` & `encord-0.1.72/encord/objects/common.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/objects/coordinates.py` & `encord-0.1.72/encord/objects/coordinates.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/objects/frames.py` & `encord-0.1.72/encord/objects/frames.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/objects/internal_helpers.py` & `encord-0.1.72/encord/objects/internal_helpers.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/objects/ontology_labels_impl.py` & `encord-0.1.72/encord/objects/ontology_labels_impl.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/objects/project.py` & `encord-0.1.72/encord/objects/project.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/objects/utils.py` & `encord-0.1.72/encord/objects/utils.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/ontology.py` & `encord-0.1.72/encord/ontology.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/orm/api_key.py` & `encord-0.1.72/encord/orm/api_key.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/orm/base_orm.py` & `encord-0.1.72/encord/orm/base_orm.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/orm/dataset.py` & `encord-0.1.72/encord/orm/dataset.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/orm/dataset_with_user_role.py` & `encord-0.1.72/encord/orm/dataset_with_user_role.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/orm/label_log.py` & `encord-0.1.72/encord/orm/label_log.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/orm/label_row.py` & `encord-0.1.72/encord/orm/label_row.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/orm/labeling_algorithm.py` & `encord-0.1.72/encord/orm/labeling_algorithm.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/orm/model.py` & `encord-0.1.72/encord/orm/model.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/orm/ontology.py` & `encord-0.1.72/encord/orm/ontology.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/orm/project.py` & `encord-0.1.72/encord/orm/project.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/orm/project_api_key.py` & `encord-0.1.72/encord/orm/project_api_key.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/orm/project_with_user_role.py` & `encord-0.1.72/encord/orm/project_with_user_role.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/orm/test/test_dataset.py` & `encord-0.1.72/encord/orm/test/test_dataset.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/project.py` & `encord-0.1.72/encord/project.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/project_ontology/classification_attribute.py` & `encord-0.1.72/encord/project_ontology/classification_attribute.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/project_ontology/classification_option.py` & `encord-0.1.72/encord/project_ontology/classification_option.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/project_ontology/ontology.py` & `encord-0.1.72/encord/project_ontology/ontology.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/project_ontology/ontology_classification.py` & `encord-0.1.72/encord/project_ontology/ontology_classification.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/project_ontology/ontology_object.py` & `encord-0.1.72/encord/project_ontology/ontology_object.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/user_client.py` & `encord-0.1.72/encord/user_client.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/utilities/client_utilities.py` & `encord-0.1.72/encord/utilities/client_utilities.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/utilities/label_utilities.py` & `encord-0.1.72/encord/utilities/label_utilities.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/encord/utilities/project_user.py` & `encord-0.1.72/encord/utilities/project_user.py`

 * *Files identical despite different names*

### Comparing `encord-0.1.71/pyproject.toml` & `encord-0.1.72/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "encord"
-version = "0.1.71"
+version = "0.1.72"
 description = "Encord Python SDK Client"
 authors = ["Cord Technologies Limited <hello@encord.com>"]
 license = "Apache Software License"
 keywords = ["cord", "encord"]
 packages = [
     { include = "cord"},
     { include = "encord"},
@@ -17,15 +17,15 @@
     "License :: OSI Approved :: Apache Software License",
     "Operating System :: OS Independent",
 ]
 
 [tool.poetry.dependencies]
 python = "^3.7"
 python-dateutil = "^2.8.2"
-requests = "2.25.0"
+requests = "^2.25.0"
 cryptography = "^3.4.8"
 tqdm = "^4.32.1"
 importlib_metadata = {version = "^6.1.0", python = "<3.8"}
 
 [tool.poetry.dev-dependencies]
 pytest = "^6.1.2"
 pre-commit = "^2.16.0"
```

### Comparing `encord-0.1.71/setup.py` & `encord-0.1.72/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -15,23 +15,23 @@
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
 ['cryptography>=3.4.8,<4.0.0',
  'python-dateutil>=2.8.2,<3.0.0',
- 'requests==2.25.0',
+ 'requests>=2.25.0,<3.0.0',
  'tqdm>=4.32.1,<5.0.0']
 
 extras_require = \
 {':python_version < "3.8"': ['importlib_metadata>=6.1.0,<7.0.0']}
 
 setup_kwargs = {
     'name': 'encord',
-    'version': '0.1.71',
+    'version': '0.1.72',
     'description': 'Encord Python SDK Client',
     'long_description': '<h1 align="center">\n  <p align="center">Encord Python API Client</p>\n  <a href="https://encord.com"><img src="./docs/_static/logo.svg" width="100" alt="Cord logo"/></a>\n</h1>\n\n[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)\n\n***The data engine for computer vision***\n\n## 💻 Features\n\n- Minimal low-level Python client that allows you to interact with Encord\'s API\n- Supports Python: `3.7`, `3.8`, `3.9`, and `3.10`\n\n## ✨ Relevant Links\n* [Encord website](https://encord.com)\n* [Encord web app](https://app.encord.com)\n* [Encord documentation](https://docs.encord.com)\n\n## 💡 Getting Started\n\nFor full documentation, please visit [Encord Python SDK](https://python.docs.encord.com/).\n\nFirst, install Encord Python API Client using the [pip](https://pip.pypa.io/en/stable/installing) package manager:\n\n```bash\npip install encord\n```\n\nThen, create an API key for authentication via the [Encord web app](https://app.encord.com). Pass the resource ID and API key as environment variables or pass them explicitly when you initialise the EncordClient object.\n\n```bash\nexport ENCORD_PROJECT_ID="<project_id>"\nexport ENCORD_API_KEY="<project_api_key>"\n```\n\nPassing the resource ID and API key as environment variables, you can initialise the Encord client directly.\n\n```python\nfrom encord.client import EncordClient\n\nclient = EncordClient.initialise()\n```\n\nIf you want to avoid setting environment variables, you can initialise the Encord client by passing the resource ID and API key as strings.\n\n```python\nfrom encord.client import EncordClient\n\nclient = EncordClient.initialise("<resource_id>", "<resource_api_key>")\n```\n\nIf you wish to instantiate several client objects and avoid passing parameters each time, you can instantiate a EncordConfig object, pass the resource ID and API key as strings, and initialise the client with the config object.\n\n```py\nfrom encord.client import EncordClient\nfrom encord.client import EncordConfig\n\nconfig = EncordConfig("<resource_id>", "<resource_api_key>")\nclient = EncordClient.initialise_with_config(config)\n```\n\nOnce you have instantiated an Encord client, it is easy to fetch information associated with the given resource ID.\n\n```py\nfrom encord.client import EncordClient\n\nclient = EncordClient.initialise()\nproject = client.get_project()\n```\n\n## 🐛 Troubleshooting\n\nPlease report bugs to [GitHub Issues](https://github.com/encord-team/encord-client-python/issues). Just make sure you read the [Encord documentation](https://docs.encord.com) and search for related issues first.\n',
     'author': 'Cord Technologies Limited',
     'author_email': 'hello@encord.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://github.com/encord-team/encord-client-python',
```

#### html2text {}

```diff
@@ -1,16 +1,16 @@
 # -*- coding: utf-8 -*- from setuptools import setup packages = \ ['cord',
 'encord', 'encord.constants', 'encord.constants.test', 'encord.http',
 'encord.objects', 'encord.orm', 'encord.orm.test', 'encord.project_ontology',
 'encord.utilities'] package_data = \ {'': ['*']} install_requires = \
 ['cryptography>=3.4.8,<4.0.0', 'python-dateutil>=2.8.2,<3.0.0',
-'requests==2.25.0', 'tqdm>=4.32.1,<5.0.0'] extras_require = \ {':python_version
-< "3.8"': ['importlib_metadata>=6.1.0,<7.0.0']} setup_kwargs = { 'name':
-'encord', 'version': '0.1.71', 'description': 'Encord Python SDK Client',
-'long_description': '
+'requests>=2.25.0,<3.0.0', 'tqdm>=4.32.1,<5.0.0'] extras_require = \ {':
+python_version < "3.8"': ['importlib_metadata>=6.1.0,<7.0.0']} setup_kwargs =
+{ 'name': 'encord', 'version': '0.1.72', 'description': 'Encord Python SDK
+Client', 'long_description': '
            ****** \nEncord Python API Client\n [Cord_logo]\n ******
 \n\n[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)]
 (https://opensource.org/licenses/Apache-2.0)\n\n***The data engine for computer
 vision***\n\n## ð» Features\n\n- Minimal low-level Python client that allows
 you to interact with Encord\'s API\n- Supports Python: `3.7`, `3.8`, `3.9`, and
 `3.10`\n\n## â¨ Relevant Links\n* [Encord website](https://encord.com)\n*
 [Encord web app](https://app.encord.com)\n* [Encord documentation](https://
```

### Comparing `encord-0.1.71/PKG-INFO` & `encord-0.1.72/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: encord
-Version: 0.1.71
+Version: 0.1.72
 Summary: Encord Python SDK Client
 Home-page: https://github.com/encord-team/encord-client-python
 License: Apache Software License
 Keywords: cord,encord
 Author: Cord Technologies Limited
 Author-email: hello@encord.com
 Requires-Python: >=3.7,<4.0
@@ -15,15 +15,15 @@
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Requires-Dist: cryptography (>=3.4.8,<4.0.0)
 Requires-Dist: importlib_metadata (>=6.1.0,<7.0.0); python_version < "3.8"
 Requires-Dist: python-dateutil (>=2.8.2,<3.0.0)
-Requires-Dist: requests (==2.25.0)
+Requires-Dist: requests (>=2.25.0,<3.0.0)
 Requires-Dist: tqdm (>=4.32.1,<5.0.0)
 Project-URL: Documentation, https://python.docs.encord.com/
 Project-URL: Repository, https://github.com/encord-team/encord-client-python
 Description-Content-Type: text/markdown
 
 <h1 align="center">
   <p align="center">Encord Python API Client</p>
```

#### html2text {}

```diff
@@ -1,20 +1,20 @@
-Metadata-Version: 2.1 Name: encord Version: 0.1.71 Summary: Encord Python SDK
+Metadata-Version: 2.1 Name: encord Version: 0.1.72 Summary: Encord Python SDK
 Client Home-page: https://github.com/encord-team/encord-client-python License:
 Apache Software License Keywords: cord,encord Author: Cord Technologies Limited
 Author-email: hello@encord.com Requires-Python: >=3.7,<4.0 Classifier: License
 :: OSI Approved :: Apache Software License Classifier: License :: Other/
 Proprietary License Classifier: Operating System :: OS Independent Classifier:
 Programming Language :: Python :: 3 Classifier: Programming Language :: Python
 :: 3.10 Classifier: Programming Language :: Python :: 3.7 Classifier:
 Programming Language :: Python :: 3.8 Classifier: Programming Language ::
 Python :: 3.9 Requires-Dist: cryptography (>=3.4.8,<4.0.0) Requires-Dist:
 importlib_metadata (>=6.1.0,<7.0.0); python_version < "3.8" Requires-Dist:
-python-dateutil (>=2.8.2,<3.0.0) Requires-Dist: requests (==2.25.0) Requires-
-Dist: tqdm (>=4.32.1,<5.0.0) Project-URL: Documentation, https://
+python-dateutil (>=2.8.2,<3.0.0) Requires-Dist: requests (>=2.25.0,<3.0.0)
+Requires-Dist: tqdm (>=4.32.1,<5.0.0) Project-URL: Documentation, https://
 python.docs.encord.com/ Project-URL: Repository, https://github.com/encord-
 team/encord-client-python Description-Content-Type: text/markdown
                ****** Encord Python API Client[Cord_logo] ******
 [![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https:
 //opensource.org/licenses/Apache-2.0) ***The data engine for computer vision***
 ## ð» Features - Minimal low-level Python client that allows you to interact
 with Encord's API - Supports Python: `3.7`, `3.8`, `3.9`, and `3.10` ## â¨
```

