# Comparing `tmp/CTADIRAC-2.2.9.tar.gz` & `tmp/CTADIRAC-2.2a3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "CTADIRAC-2.2.9.tar", last modified: Tue Apr  4 11:36:45 2023, max compression
+gzip compressed data, was "CTADIRAC-2.2a3.tar", last modified: Fri Feb 10 15:50:56 2023, max compression
```

## Comparing `CTADIRAC-2.2.9.tar` & `CTADIRAC-2.2a3.tar`

### file list

```diff
@@ -1,175 +1,170 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.211911 CTADIRAC-2.2.9/
--rw-rw-rw-   0 root         (0) root         (0)      101 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      275 2023-04-04 11:36:45.211911 CTADIRAC-2.2.9/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)      916 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/README.md
--rw-rw-rw-   0 root         (0) root         (0)     4349 2023-04-04 11:36:45.211911 CTADIRAC-2.2.9/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)      275 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.191911 CTADIRAC-2.2.9/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.191911 CTADIRAC-2.2.9/src/CTADIRAC/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.195911 CTADIRAC-2.2.9/src/CTADIRAC/ConfigurationSystem/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.195911 CTADIRAC-2.2.9/src/CTADIRAC/ConfigurationSystem/Agent/
--rw-rw-rw-   0 root         (0) root         (0)     4194 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/ConfigurationSystem/Agent/StorageMonitorAgent.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/ConfigurationSystem/Agent/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      191 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/ConfigurationSystem/ConfigTemplate.cfg
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/ConfigurationSystem/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.195911 CTADIRAC-2.2.9/src/CTADIRAC/Core/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.195911 CTADIRAC-2.2.9/src/CTADIRAC/Core/Utilities/
--rw-rw-rw-   0 root         (0) root         (0)     5192 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/Utilities/Prod3SoftwareManager.py
--rw-rw-rw-   0 root         (0) root         (0)     7416 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/Utilities/SoftwareManager.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/Utilities/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     6295 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/Utilities/tool_box.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.195911 CTADIRAC-2.2.9/src/CTADIRAC/Core/Workflow/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.195911 CTADIRAC-2.2.9/src/CTADIRAC/Core/Workflow/Modules/
--rw-rw-rw-   0 root         (0) root         (0)    11802 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/Workflow/Modules/ProdDataManager.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/Workflow/Modules/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/Workflow/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.199911 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)     1523 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_dms_check_lfn.py
--rwxrwxrwx   0 root         (0) root         (0)     8261 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_install_tornado_component.py
--rwxrwxrwx   0 root         (0) root         (0)     2012 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_add_dataset.py
--rwxrwxrwx   0 root         (0) root         (0)     1022 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_add_file.py
--rwxrwxrwx   0 root         (0) root         (0)    11654 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_add_prov.py
--rwxrwxrwx   0 root         (0) root         (0)     1949 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_check_replicas.py
--rwxrwxrwx   0 root         (0) root         (0)     1038 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_dump_dataset.py
--rwxrwxrwx   0 root         (0) root         (0)     3099 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_failure_monitor.py
--rwxrwxrwx   0 root         (0) root         (0)     1959 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_fix_nsb.py
--rwxrwxrwx   0 root         (0) root         (0)     2203 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_get_file.py
--rwxrwxrwx   0 root         (0) root         (0)     2405 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_get_merge_size.py
--rwxrwxrwx   0 root         (0) root         (0)     1153 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_get_replicas.py
--rwxrwxrwx   0 root         (0) root         (0)     1985 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_get_se_status.py
--rwxrwxrwx   0 root         (0) root         (0)      855 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_git_clone.py
--rwxrwxrwx   0 root         (0) root         (0)     5262 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_init_prov.py
--rwxrwxrwx   0 root         (0) root         (0)     2507 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_managedata.py
--rwxrwxrwx   0 root         (0) root         (0)     1195 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_mark_corrupted_DL0.py
--rwxrwxrwx   0 root         (0) root         (0)     2146 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_monitor.py
--rwxrwxrwx   0 root         (0) root         (0)     3913 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_move_dataset.py
--rwxrwxrwx   0 root         (0) root         (0)     4360 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_move_dataset_status.py
--rwxrwxrwx   0 root         (0) root         (0)     1223 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_remove_corrupted_file.py
--rwxrwxrwx   0 root         (0) root         (0)     1208 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_remove_dataset.py
--rwxrwxrwx   0 root         (0) root         (0)      904 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_remove_file.py
--rwxrwxrwx   0 root         (0) root         (0)     1066 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_replicate_lfn.py
--rwxrwxrwx   0 root         (0) root         (0)     1211 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_set_metadata.py
--rwxrwxrwx   0 root         (0) root         (0)     3682 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_setup_software.py
--rwxrwxrwx   0 root         (0) root         (0)     8494 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_show_dataset.py
--rw-rw-rw-   0 root         (0) root         (0)     5332 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_split_dataset.py
--rwxrwxrwx   0 root         (0) root         (0)     1412 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_unregister_file.py
--rwxrwxrwx   0 root         (0) root         (0)     1185 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_update_dataset.py
--rwxrwxrwx   0 root         (0) root         (0)     6558 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_verifysteps.py
--rwxrwxrwx   0 root         (0) root         (0)    10929 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_rms_request.py
--rwxrwxrwx   0 root         (0) root         (0)     1007 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_add_files.py
--rwxrwxrwx   0 root         (0) root         (0)      768 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_clean.py
--rwxrwxrwx   0 root         (0) root         (0)     1254 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_delete.py
--rwxrwxrwx   0 root         (0) root         (0)     4289 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_get_files.py
--rwxrwxrwx   0 root         (0) root         (0)     1306 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_get_tasks.py
--rwxrwxrwx   0 root         (0) root         (0)     1061 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_select.py
--rwxrwxrwx   0 root         (0) root         (0)     2362 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_show_progress.py
--rwxrwxrwx   0 root         (0) root         (0)     1400 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_treat_done_tasks.py
--rwxrwxrwx   0 root         (0) root         (0)     1454 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_treat_failed_tasks.py
--rwxrwxrwx   0 root         (0) root         (0)     2208 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_treat_incomplete_transfers.py
--rwxrwxrwx   0 root         (0) root         (0)     2444 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_treat_problematic_files.py
--rwxrwxrwx   0 root         (0) root         (0)     1569 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_user_managedata.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.203911 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.203911 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/Client/
--rw-rw-rw-   0 root         (0) root         (0)    12136 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/Client/ProvBase.py
--rw-rw-rw-   0 root         (0) root         (0)     4472 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/Client/ProvClient.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/Client/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     5144 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/Client/testProvClient_muon.py
--rw-rw-rw-   0 root         (0) root         (0)      116 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/ConfigTemplate.cfg
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.203911 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/DB/
--rw-rw-rw-   0 root         (0) root         (0)    44754 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/DB/ProvenanceDB.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/DB/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.203911 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/Service/
--rw-rw-rw-   0 root         (0) root         (0)     9013 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/Service/ProvenanceManagerHandler.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/Service/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.203911 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/Utilities/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/Utilities/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.203911 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/private/
--rw-rw-rw-   0 root         (0) root         (0)      315 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/private/JSONUtils.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/private/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.203911 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.207911 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/
--rw-rw-rw-   0 root         (0) root         (0)     3495 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/CtapipeApplyModelsJob.py
--rw-rw-rw-   0 root         (0) root         (0)     5282 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/CtapipeMergeJob.py
--rw-rw-rw-   0 root         (0) root         (0)     4273 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/CtapipeProcessJob.py
--rw-rw-rw-   0 root         (0) root         (0)     3541 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/CtapipeTrainClassifierJob.py
--rw-rw-rw-   0 root         (0) root         (0)     3636 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/CtapipeTrainEnergyJob.py
--rw-rw-rw-   0 root         (0) root         (0)     6780 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/EvnDisp4SSTJob.py
--rw-rw-rw-   0 root         (0) root         (0)     7761 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/EvnDispProd5Job.py
--rw-rw-rw-   0 root         (0) root         (0)     5879 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/EvnDispProd5SingJob.py
--rw-rw-rw-   0 root         (0) root         (0)     5856 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/EvnDispSingJob.py
--rw-rw-rw-   0 root         (0) root         (0)    13550 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/MCPipeNSBJob.py
--rw-rw-rw-   0 root         (0) root         (0)     2450 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/ProcessingJob.py
--rw-rw-rw-   0 root         (0) root         (0)    13769 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod5MCPipeNSBJob.py
--rw-rw-rw-   0 root         (0) root         (0)     7938 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod5bMCPipeAlphaDivergentJob.py
--rw-rw-rw-   0 root         (0) root         (0)     9113 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod5bMCPipeAlphaSSTsFullMoonNSBJob.py
--rw-rw-rw-   0 root         (0) root         (0)    11915 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod5bMCPipeAlphaSSTsNSBJob.py
--rw-rw-rw-   0 root         (0) root         (0)    10554 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod5bMCPipeNSBJob.py
--rw-rw-rw-   0 root         (0) root         (0)     9826 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod6MCPipeDivergentJob.py
--rw-rw-rw-   0 root         (0) root         (0)    13225 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod6MCPipeMuonJob.py
--rw-rw-rw-   0 root         (0) root         (0)    13604 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod6MCPipeNSBJob.py
--rw-rw-rw-   0 root         (0) root         (0)     5509 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/ProvCtapipeJob.py
--rw-rw-rw-   0 root         (0) root         (0)     8911 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/SimpleCtapipeJob.py
--rw-rw-rw-   0 root         (0) root         (0)     3981 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/SimtelTSJob.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.211911 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/
--rw-rw-rw-   0 root         (0) root         (0)     1375 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/DataRemovalByQueryTSExample.py
--rw-rw-rw-   0 root         (0) root         (0)     1825 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/DataRemovalTSExample.py
--rw-rw-rw-   0 root         (0) root         (0)     1989 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/DataReplicaRemovalTSExample.py
--rw-rw-rw-   0 root         (0) root         (0)     1613 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/DataReplicationByQueryTSExample.py
--rw-rw-rw-   0 root         (0) root         (0)     1886 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/DataReplicationTSExample.py
--rwxrwxrwx   0 root         (0) root         (0)     5064 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/ProvCtapipeJobExample.py
--rwxrwxrwx   0 root         (0) root         (0)     6292 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/SimpleCtapipeJobExample.py
--rwxrwxrwx   0 root         (0) root         (0)     5100 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/SimtelTSExample.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     5514 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5_ctapipe_merge_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     6191 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5_ctapipe_modeling_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     6003 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5_evndisp_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     4542 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5_mcpipe_nsb_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     6266 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5_ps_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     5162 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_alpha_divergent_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     5020 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_alpha_ssts_fullmoon_nsb_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     4967 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_alpha_ssts_nsb_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     4987 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_nsb_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     6509 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_ps_generic_stage1_merge_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     6315 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_ps_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     7714 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_ps_mcpipe_stage1_merge_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     7467 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_ps_split_stage1_merge_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     5478 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_sing_evndisp_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     5379 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod6_mcpipe_divergent_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     5532 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod6_mcpipe_muon_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     5151 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod6_mcpipe_nsb_launcher.py
--rw-rw-rw-   0 root         (0) root         (0)     4983 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod_mark_corrupted_DL0.py
--rw-rw-rw-   0 root         (0) root         (0)      411 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/testJob.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.211911 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.211911 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/Client/
--rw-rw-rw-   0 root         (0) root         (0)     3287 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/Client/CtapipeProcessingElement.py
--rw-rw-rw-   0 root         (0) root         (0)     3383 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/Client/CtapipeTrainEnergyElement.py
--rw-rw-rw-   0 root         (0) root         (0)     3473 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/Client/EvnDispElement.py
--rw-rw-rw-   0 root         (0) root         (0)     3996 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/Client/MergingElement.py
--rw-rw-rw-   0 root         (0) root         (0)     3085 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/Client/SimulationElement.py
--rw-rw-rw-   0 root         (0) root         (0)     5890 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/Client/WorkflowElement.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/Client/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.211911 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/config/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/config/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      803 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/config/processing_config_from_dataset.yml
--rw-rw-rw-   0 root         (0) root         (0)      851 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/config/processing_config_from_meta_query.yml
--rw-rw-rw-   0 root         (0) root         (0)     1007 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/config/production_config.yml
--rw-rw-rw-   0 root         (0) root         (0)      480 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/config/production_cwl.yml
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.211911 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/scripts/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 11:36:30.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/scripts/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    10732 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/scripts/cta_prod_submit.py
--rwxrwxrwx   0 root         (0) root         (0)    10696 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/scripts/cta_prod_submit_from_cwl.py
--rw-rw-rw-   0 root         (0) root         (0)      709 2023-04-04 11:36:29.000000 CTADIRAC-2.2.9/src/CTADIRAC/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 11:36:45.191911 CTADIRAC-2.2.9/src/CTADIRAC.egg-info/
--rw-r--r--   0 root         (0) root         (0)      275 2023-04-04 11:36:45.000000 CTADIRAC-2.2.9/src/CTADIRAC.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     7779 2023-04-04 11:36:45.000000 CTADIRAC-2.2.9/src/CTADIRAC.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-04 11:36:45.000000 CTADIRAC-2.2.9/src/CTADIRAC.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)     3609 2023-04-04 11:36:45.000000 CTADIRAC-2.2.9/src/CTADIRAC.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-04 11:36:45.000000 CTADIRAC-2.2.9/src/CTADIRAC.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)      135 2023-04-04 11:36:45.000000 CTADIRAC-2.2.9/src/CTADIRAC.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        9 2023-04-04 11:36:45.000000 CTADIRAC-2.2.9/src/CTADIRAC.egg-info/top_level.txt
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.086903 CTADIRAC-2.2a3/
+-rw-r--r--   0 arrabito   (503) staff       (20)      101 2022-10-18 06:41:16.000000 CTADIRAC-2.2a3/MANIFEST.in
+-rw-r--r--   0 arrabito   (503) staff       (20)      314 2023-02-10 15:50:56.087085 CTADIRAC-2.2a3/PKG-INFO
+-rw-r--r--   0 arrabito   (503) staff       (20)      833 2023-02-01 08:46:12.000000 CTADIRAC-2.2a3/README.md
+-rw-r--r--   0 arrabito   (503) staff       (20)     4017 2023-02-10 15:50:56.088187 CTADIRAC-2.2a3/setup.cfg
+-rw-r--r--   0 arrabito   (503) staff       (20)      275 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/setup.py
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.035752 CTADIRAC-2.2a3/src/
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.040093 CTADIRAC-2.2a3/src/CTADIRAC/
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.043402 CTADIRAC-2.2a3/src/CTADIRAC/ConfigurationSystem/
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.044020 CTADIRAC-2.2a3/src/CTADIRAC/ConfigurationSystem/Agent/
+-rw-r--r--   0 arrabito   (503) staff       (20)     4194 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/ConfigurationSystem/Agent/StorageMonitorAgent.py
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/ConfigurationSystem/Agent/__init__.py
+-rw-r--r--   0 arrabito   (503) staff       (20)      191 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/ConfigurationSystem/ConfigTemplate.cfg
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/ConfigurationSystem/__init__.py
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.044270 CTADIRAC-2.2a3/src/CTADIRAC/Core/
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.045635 CTADIRAC-2.2a3/src/CTADIRAC/Core/Utilities/
+-rw-r--r--   0 arrabito   (503) staff       (20)     5192 2022-01-07 10:16:54.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/Utilities/Prod3SoftwareManager.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     7416 2022-08-25 12:10:10.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/Utilities/SoftwareManager.py
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/Utilities/__init__.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     6295 2022-08-25 12:07:14.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/Utilities/tool_box.py
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.045989 CTADIRAC-2.2a3/src/CTADIRAC/Core/Workflow/
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.046666 CTADIRAC-2.2a3/src/CTADIRAC/Core/Workflow/Modules/
+-rw-r--r--   0 arrabito   (503) staff       (20)    10627 2022-11-30 07:20:26.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/Workflow/Modules/ProdDataManager.py
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/Workflow/Modules/__init__.py
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/Workflow/__init__.py
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/__init__.py
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.062674 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/__init__.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1548 2022-01-12 08:11:26.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_dms_check_lfn.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1863 2023-02-10 15:49:24.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_add_dataset.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1047 2022-04-15 08:09:48.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_add_file.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)    11654 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_add_prov.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1974 2022-01-27 13:25:27.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_check_replicas.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1038 2023-02-10 15:49:24.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_dump_dataset.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     3124 2022-01-12 08:59:57.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_failure_monitor.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1984 2022-09-15 05:58:53.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_fix_nsb.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     2228 2022-01-12 09:10:04.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_get_file.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1178 2022-01-12 11:04:12.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_get_replicas.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     2010 2022-09-15 05:58:53.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_get_se_status.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)      880 2022-01-12 09:15:45.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_git_clone.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     5262 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_init_prov.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     2532 2022-09-19 07:58:13.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_managedata.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1220 2022-09-15 05:58:53.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_mark_corrupted_DL0.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     2171 2022-01-12 08:07:52.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_monitor.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     3938 2022-01-14 16:12:30.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_move_dataset.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     4385 2022-01-17 14:18:20.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_move_dataset_status.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1248 2022-09-15 05:58:53.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_remove_corrupted_file.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1233 2022-01-12 11:26:06.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_remove_dataset.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)      904 2023-02-10 15:49:24.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_remove_file.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1091 2022-02-24 10:25:01.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_replicate_lfn.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     3707 2022-09-15 13:08:27.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_setup_software.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     8494 2023-02-10 15:49:24.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_show_dataset.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1437 2022-01-12 12:47:12.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_unregister_file.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1210 2022-01-12 12:49:18.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_update_dataset.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     6583 2022-09-15 05:58:53.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_verifysteps.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)    10954 2022-01-12 07:35:24.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_rms_request.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1007 2023-02-10 15:49:24.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_add_files.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)      793 2022-01-12 12:59:12.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_clean.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1279 2022-01-12 13:01:28.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_delete.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     4314 2022-03-23 14:32:10.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_get_files.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1331 2022-01-12 13:05:40.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_get_tasks.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1086 2022-01-12 13:07:06.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_select.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1217 2022-02-24 10:26:12.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_set_file_status.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     2387 2022-02-24 10:20:43.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_show_progress.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)      818 2022-04-11 09:27:41.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_stress_test.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1425 2022-03-23 14:34:16.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_treat_done_tasks.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1479 2022-03-23 14:34:49.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_treat_failed_tasks.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     2233 2022-01-27 13:29:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_treat_incomplete_transfers.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     2469 2022-03-23 14:35:45.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_treat_problematic_files.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     1512 2022-09-15 05:58:53.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_user_managedata.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     1195 2022-08-11 13:13:32.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/get_OSB.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     2460 2022-08-11 13:27:21.000000 CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/read_cpu.py
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.063308 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.064615 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/Client/
+-rw-r--r--   0 arrabito   (503) staff       (20)    12136 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/Client/ProvBase.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     4472 2021-12-10 08:27:18.000000 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/Client/ProvClient.py
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/Client/__init__.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     5144 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/Client/testProvClient_muon.py
+-rw-r--r--   0 arrabito   (503) staff       (20)      116 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/ConfigTemplate.cfg
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.065635 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/DB/
+-rw-r--r--   0 arrabito   (503) staff       (20)    44754 2021-12-10 08:27:18.000000 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/DB/ProvenanceDB.py
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/DB/__init__.py
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.066271 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/Service/
+-rw-r--r--   0 arrabito   (503) staff       (20)     9013 2021-12-10 08:27:18.000000 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/Service/ProvenanceManagerHandler.py
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/Service/__init__.py
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.066511 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/Utilities/
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/Utilities/__init__.py
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/__init__.py
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.067070 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/private/
+-rw-r--r--   0 arrabito   (503) staff       (20)      315 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/private/JSONUtils.py
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/private/__init__.py
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.067337 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.073762 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/
+-rw-r--r--   0 arrabito   (503) staff       (20)     6780 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/EvnDisp4SSTJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     7761 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/EvnDispProd5Job.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     5879 2022-03-25 12:33:52.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/EvnDispProd5SingJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     6449 2023-02-01 08:46:12.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/EvnDispSingJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)    14152 2023-02-10 15:22:57.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/MCPipeNSBJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     5965 2023-02-10 15:22:57.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod5CtaPipeMergeJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     5419 2022-12-01 07:22:48.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod5CtaPipeModelingJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)    13769 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod5MCPipeNSBJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     7215 2023-02-10 15:22:57.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod5Stage1Job.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     7938 2022-06-10 07:49:26.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod5bMCPipeAlphaDivergentJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     9113 2022-02-01 11:08:51.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod5bMCPipeAlphaSSTsFullMoonNSBJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)    11915 2022-02-01 10:43:25.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod5bMCPipeAlphaSSTsNSBJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)    10554 2022-06-10 07:47:59.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod5bMCPipeNSBJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     8771 2022-12-13 09:40:37.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod6MCPipeDivergentJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)    12336 2022-12-01 11:29:10.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod6MCPipeMuonJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)    12830 2022-08-25 12:32:07.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod6MCPipeNSBJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     5509 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/ProvCtapipeJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     8911 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/SimpleCtapipeJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     3981 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/SimtelTSJob.py
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/__init__.py
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/__init__.py
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.082471 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/
+-rw-r--r--   0 arrabito   (503) staff       (20)     1375 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/DataRemovalByQueryTSExample.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     1825 2022-01-07 11:15:39.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/DataRemovalTSExample.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     1989 2022-01-07 11:15:20.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/DataReplicaRemovalTSExample.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     1613 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/DataReplicationByQueryTSExample.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     1886 2022-01-07 11:16:01.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/DataReplicationTSExample.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     5064 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/ProvCtapipeJobExample.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     6292 2022-01-07 11:14:31.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/SimpleCtapipeJobExample.py
+-rwxr-xr-x   0 arrabito   (503) staff       (20)     5100 2022-01-07 11:14:54.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/SimtelTSExample.py
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/__init__.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     5207 2022-01-14 15:28:57.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/move_data_ps_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     5514 2022-06-10 07:53:58.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5_ctapipe_merge_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     6191 2022-06-10 07:53:58.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5_ctapipe_modeling_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     6003 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5_evndisp_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     4542 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5_mcpipe_nsb_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     6266 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5_ps_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     5162 2022-06-10 07:48:00.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_alpha_divergent_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     5020 2022-02-15 09:53:01.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_alpha_ssts_fullmoon_nsb_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     4967 2022-02-15 09:53:20.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_alpha_ssts_nsb_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     4987 2021-12-09 14:00:02.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_nsb_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     6509 2022-06-27 12:16:51.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_ps_generic_stage1_merge_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     6315 2022-01-14 15:22:13.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_ps_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     7714 2022-06-27 12:16:51.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_ps_mcpipe_stage1_merge_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     7467 2022-06-27 12:16:51.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_ps_split_stage1_merge_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     5478 2022-04-20 10:10:19.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_sing_evndisp_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     5282 2022-12-13 09:40:37.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod6_mcpipe_divergent_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     5532 2022-12-01 07:28:40.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod6_mcpipe_muon_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     5151 2022-08-25 12:31:51.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod6_mcpipe_nsb_launcher.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     4983 2022-02-24 10:28:56.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod_mark_corrupted_DL0.py
+-rw-r--r--   0 arrabito   (503) staff       (20)      411 2022-01-14 15:28:13.000000 CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/testJob.py
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.082755 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.084871 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/Client/
+-rw-r--r--   0 arrabito   (503) staff       (20)     3315 2023-02-01 08:46:12.000000 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/Client/CtapipeModelingElement.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     3473 2023-02-01 08:46:12.000000 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/Client/EvnDispElement.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     3968 2023-02-01 08:46:12.000000 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/Client/MergingElement.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     2973 2023-02-10 15:22:57.000000 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/Client/SimulationElement.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     5866 2023-02-10 15:49:24.000000 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/Client/WorkflowElement.py
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2022-09-16 16:46:38.000000 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/Client/__init__.py
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2022-09-16 16:41:19.000000 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/__init__.py
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.086038 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/config/
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2022-09-19 09:48:36.000000 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/config/__init__.py
+-rw-r--r--   0 arrabito   (503) staff       (20)      652 2022-11-25 07:19:12.000000 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/config/processing_config_from_dataset.yml
+-rw-r--r--   0 arrabito   (503) staff       (20)      851 2022-12-01 07:22:48.000000 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/config/processing_config_from_meta_query.yml
+-rw-r--r--   0 arrabito   (503) staff       (20)     1007 2023-02-01 08:46:12.000000 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/config/production_config.yml
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.086603 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/scripts/
+-rw-r--r--   0 arrabito   (503) staff       (20)        0 2022-09-16 16:46:14.000000 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/scripts/__init__.py
+-rw-r--r--   0 arrabito   (503) staff       (20)     9100 2023-02-10 15:49:24.000000 CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/scripts/cta_prod_submit.py
+-rw-r--r--   0 arrabito   (503) staff       (20)      709 2022-06-09 07:53:28.000000 CTADIRAC-2.2a3/src/CTADIRAC/__init__.py
+drwxr-xr-x   0 arrabito   (503) staff       (20)        0 2023-02-10 15:50:56.042571 CTADIRAC-2.2a3/src/CTADIRAC.egg-info/
+-rw-r--r--   0 arrabito   (503) staff       (20)      314 2023-02-10 15:50:55.000000 CTADIRAC-2.2a3/src/CTADIRAC.egg-info/PKG-INFO
+-rw-r--r--   0 arrabito   (503) staff       (20)     7476 2023-02-10 15:50:55.000000 CTADIRAC-2.2a3/src/CTADIRAC.egg-info/SOURCES.txt
+-rw-r--r--   0 arrabito   (503) staff       (20)        1 2023-02-10 15:50:55.000000 CTADIRAC-2.2a3/src/CTADIRAC.egg-info/dependency_links.txt
+-rw-r--r--   0 arrabito   (503) staff       (20)     3282 2023-02-10 15:50:55.000000 CTADIRAC-2.2a3/src/CTADIRAC.egg-info/entry_points.txt
+-rw-r--r--   0 arrabito   (503) staff       (20)        1 2021-12-09 14:04:37.000000 CTADIRAC-2.2a3/src/CTADIRAC.egg-info/not-zip-safe
+-rw-r--r--   0 arrabito   (503) staff       (20)      134 2023-02-10 15:50:55.000000 CTADIRAC-2.2a3/src/CTADIRAC.egg-info/requires.txt
+-rw-r--r--   0 arrabito   (503) staff       (20)        9 2023-02-10 15:50:55.000000 CTADIRAC-2.2a3/src/CTADIRAC.egg-info/top_level.txt
```

### Comparing `CTADIRAC-2.2.9/README.md` & `CTADIRAC-2.2a3/README.md`

 * *Files 11% similar despite different names*

```diff
@@ -1,20 +1,17 @@
 # CTADIRAC project
 * CTADIRAC is a customized version of the DIRAC interware. As of today, it allows an easy and optimized access to Grid resources (mainly EGI) available to the CTA Virtual Organization (vo.cta.in2p3.fr). When CTAO DPPS will be setup, CTADIRAC will serve as the Computing Ressource and Worflow Management System.
 * CTADIRAC specific documentation can be found at:
  https://redmine.cta-observatory.org/projects/cta_dirac/wiki/CTA-DIRAC_Users_Guide.
   
+
 # Contribute to CTADIRAC:
 * To contribute to CTADIRAC, please check out the full DIRAC developers guide at:
   http://dirac.readthedocs.io/en/integration/DeveloperGuide/index.html
 
 
 # Release informations:
 * Get CTADIRAC on pypi
   https://gitlab.cta-observatory.org/cta-computing/dpps/CTADIRAC/-/packages
 
-# Deploying CTADIRAC
-
-See the [dedicated documentation](docs/install_CTADIRAC.md).
-
 # Contact Information
 * Luisa Arrabito <arrabito@in2p3.fr>
```

### Comparing `CTADIRAC-2.2.9/setup.cfg` & `CTADIRAC-2.2a3/setup.cfg`

 * *Files 3% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 [metadata]
 name = CTADIRAC
 description = CTADIRAC is the CTA extension of DIRAC
-version = 2.2.9
+version = 2.2.a3
 url = https://gitlab.cta-observatory.org/cta-computing/dpps/CTADIRAC/
 license = BSD 3-Clause License
 license_files = file: LICENSE
 
 [options]
 python_requires = >=3.9
 package_dir = 
 	=src
 packages = find:
 install_requires = 
-	DIRAC == 8.0.15
+	DIRAC == 8.0.5
 	sphinx_rtd_theme
 	pyyaml
 zip_safe = False
 include_package_data = True
 
 [options.package_data]
 * = ConfigTemplate.cfg, *.sql
@@ -37,15 +37,14 @@
 	pytest
 
 [options.entry_points]
 dirac = 
 	metadata = CTADIRAC:extension_metadata
 console_scripts = 
 	cta-dms-check-lfn = CTADIRAC.Core.scripts.cta_dms_check_lfn:main
-	cta-install-tornado-component = CTADIRAC.Core.scripts.cta_install_tornado_component:main
 	cta-prod-add-dataset = CTADIRAC.Core.scripts.cta_prod_add_dataset:main
 	cta-prod-add-file = CTADIRAC.Core.scripts.cta_prod_add_file:main
 	cta-prod-add-prov = CTADIRAC.Core.scripts.cta_prod_add_prov:main
 	cta-prod-dump-dataset = CTADIRAC.Core.scripts.cta_prod_dump_dataset:main
 	cta-prod-failure-monitor = CTADIRAC.Core.scripts.cta_prod_failure_monitor:main
 	cta-prod-fix-nsb = CTADIRAC.Core.scripts.cta_prod_fix_nsb:main
 	cta-prod-mark-corrupted-DL0 = CTADIRAC.Core.scripts.cta_prod_mark_corrupted_DL0:main
@@ -58,24 +57,21 @@
 	cta-prod-monitor = CTADIRAC.Core.scripts.cta_prod_monitor:main
 	cta-prod-move-dataset = CTADIRAC.Core.scripts.cta_prod_move_dataset:main
 	cta-prod-move-dataset-status = CTADIRAC.Core.scripts.cta_prod_move_dataset_status:main
 	cta-prod-remove-corrupted-file = CTADIRAC.Core.scripts.cta_prod_remove_corrupted_file:main
 	cta-prod-remove-dataset = CTADIRAC.Core.scripts.cta_prod_remove_dataset:main
 	cta-prod-remove-file = CTADIRAC.Core.scripts.cta_prod_remove_file:main
 	cta-prod-replicate-lfn = CTADIRAC.Core.scripts.cta_prod_replicate_lfn:main
-	cta-prod-set-metadata = CTADIRAC.Core.scripts.cta_prod_set_metadata:main
 	cta-prod-setup-software = CTADIRAC.Core.scripts.cta_prod_setup_software:main
 	cta-prod-show-dataset = CTADIRAC.Core.scripts.cta_prod_show_dataset:main
-	cta-prod-split-dataset = CTADIRAC.Core.scripts.cta_prod_split_dataset:main
 	cta-prod-unregister-file = CTADIRAC.Core.scripts.cta_prod_unregister_file:main
 	cta-prod-update-dataset = CTADIRAC.Core.scripts.cta_prod_update_dataset:main
 	cta-prod-verifysteps = CTADIRAC.Core.scripts.cta_prod_verifysteps:main
 	cta-prod-check-replicas = CTADIRAC.Core.scripts.cta_prod_check_replicas:main
 	cta-prod-submit = CTADIRAC.ProductionSystem.scripts.cta_prod_submit:main
-	cta-prod-submit-from-cwl = CTADIRAC.ProductionSystem.scripts.cta_prod_submit_from_cwl:main
 	cta-rms-request = CTADIRAC.Core.scripts.cta_rms_request:main
 	cta-transformation-add-files = CTADIRAC.Core.scripts.cta_transformation_add_files:main
 	cta-transformation-get-files = CTADIRAC.Core.scripts.cta_transformation_get_files:main
 	cta-transformation-clean = CTADIRAC.Core.scripts.cta_transformation_clean:main
 	cta-transformation-delete = CTADIRAC.Core.scripts.cta_transformation_delete:main
 	cta-transformation-get-tasks = CTADIRAC.Core.scripts.cta_transformation_get_tasks:main
 	cta-transformation-select = CTADIRAC.Core.scripts.cta_transformation_select:main
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/ConfigurationSystem/Agent/StorageMonitorAgent.py` & `CTADIRAC-2.2a3/src/CTADIRAC/ConfigurationSystem/Agent/StorageMonitorAgent.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/Utilities/Prod3SoftwareManager.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/Utilities/Prod3SoftwareManager.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/Utilities/SoftwareManager.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/Utilities/SoftwareManager.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/Utilities/tool_box.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/Utilities/tool_box.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/Workflow/Modules/ProdDataManager.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/Workflow/Modules/ProdDataManager.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-""" Manage data and meta-data
+""" Manage data and meta-data for PROD3
 """
 
 __RCSID__ = "$Id$"
 
 # generic imports
 import os
 import glob
@@ -18,303 +18,298 @@
 from DIRAC.DataManagementSystem.Client.DataManager import DataManager
 from DIRAC.Core.Utilities import List
 from DIRAC.ConfigurationSystem.Client.Helpers.Operations import Operations
 from DIRAC.Core.Utilities.SiteSEMapping import getSEsForSite
 from DIRAC.Interfaces.API.Dirac import Dirac
 
 
-class ProdDataManager:
-    """Manage data and meta-data"""
+class ProdDataManager(object):
+  """ Manage data and meta-data
+  """
+
+  def __init__(self, catalogs=['DIRACFileCatalog']):
+    """ Constructor
+
+    """
+    self.setupCatalogClient(catalogs)
+    self.printCatalogConfig(catalogs)
+    self.setupDataManagerClient(catalogs)
 
-    def __init__(self, catalogs=["DIRACFileCatalog"]):
-        """Constructor"""
-        self.setupCatalogClient(catalogs)
-        self.printCatalogConfig(catalogs)
-        self.setupDataManagerClient(catalogs)
-
-    def setupCatalogClient(self, catalogs):
-        """Init FileCatalog client
+  def setupCatalogClient(self, catalogs):
+    """ Init FileCatalog client
         Ideally we would like to use only FileCatalog but it doesn't work for setMetadata
         because the returned value has a wrong format. So use of FileCatalogClient instead
-        """
-        self.fc = FileCatalog(catalogs)
-        self.fcc = FileCatalogClient()
-
-    def printCatalogConfig(self, catalogs):
-        """Dumps catalog configuration"""
-        for catalog in catalogs:
-            res = self.fc._getCatalogConfigDetails(catalog)
-            DIRAC.gLogger.info("CatalogConfigDetails:", res)
-
-    def setupDataManagerClient(self, catalogs):
-        """Init DataManager client"""
-        self.dm = DataManager(catalogs)
-
-    def _getSEList(self, SEType="ProductionOutputs", DataType="SimtelProd"):
-        """get from CS the list of available SE for data upload"""
-        opsHelper = Operations()
-        optionName = os.path.join(SEType, DataType)
-        SEList = opsHelper.getValue(optionName, [])
-        SEList = List.randomize(SEList)
-        DIRAC.gLogger.notice(f"List of {SEType} SE: {SEList} ")
-
-        # # Check if the local SE is in the list. If yes try it first by reversing list order
-        localSEList = []
-        res = getSEsForSite(DIRAC.siteName())
-        if res["OK"]:
-            localSEList = res["Value"]
-
-        retainedlocalSEList = []
-        for localSE in localSEList:
-            if localSE in SEList:
-                DIRAC.gLogger.notice(
-                    "The local Storage Element is an available SE: ", localSE
-                )
-                retainedlocalSEList.append(localSE)
-                SEList.remove(localSE)
-
-        SEList = retainedlocalSEList + SEList
-        if len(SEList) == 0:
-            return DIRAC.S_ERROR("Error in building SEList")
-
-        return DIRAC.S_OK(SEList)
-
-    def _checkemptydir(self, path):
-        """check that the directory is not empty"""
-        if len(glob.glob(path)) == 0:
-            error = f"Empty directory: {path}"
-            return DIRAC.S_ERROR(error)
-        else:
-            return DIRAC.S_OK()
+    """
+    self.fc = FileCatalog(catalogs)
+    self.fcc = FileCatalogClient()
+
+  def printCatalogConfig(self, catalogs):
+    """ Dumps catalog configuration
+    """
+    for catalog in catalogs:
+      res = self.fc._getCatalogConfigDetails(catalog)
+      DIRAC.gLogger.info('CatalogConfigDetails:', res)
+
+  def setupDataManagerClient(self, catalogs):
+    """ Init DataManager client
+    """
+    self.dm = DataManager(catalogs)
+
+  def _getSEList(self, SEType='ProductionOutputs', DataType='SimtelProd'):
+    """ get from CS the list of available SE for data upload
+    """
+    opsHelper = Operations()
+    optionName = os.path.join(SEType, DataType)
+    SEList = opsHelper.getValue(optionName, [])
+    SEList = List.randomize(SEList)
+    DIRAC.gLogger.notice('List of %s SE: %s ' % (SEType, SEList))
+
+    # # Check if the local SE is in the list. If yes try it first by reversing list order
+    localSEList = []
+    res = getSEsForSite(DIRAC.siteName())
+    if res['OK']:
+      localSEList = res['Value']
+
+    retainedlocalSEList = []
+    for localSE in localSEList:
+      if localSE in SEList:
+        DIRAC.gLogger.notice('The local Storage Element is an available SE: ', localSE)
+        retainedlocalSEList.append(localSE)
+        SEList.remove(localSE)
+
+    SEList = retainedlocalSEList + SEList
+    if len(SEList) == 0:
+      return DIRAC.S_ERROR('Error in building SEList')
+
+    return DIRAC.S_OK(SEList)
+
+  def _checkemptydir(self, path):
+    """ check that the directory is not empty
+    """
+    if len(glob.glob(path)) == 0:
+      error = 'Empty directory: %s' % path
+      return DIRAC.S_ERROR(error)
+    else:
+      return DIRAC.S_OK()
 
-    def _getRunPath(self, filemetadata):
-        """format path to string with 1 digit precision
+  def _getRunPath(self, filemetadata):
+    """ format path to string with 1 digit precision
         run_number is taken from filemetadata
         filemetadata can be a dict or the run_number itself
-        """
-        if isinstance(filemetadata, dict):
-            run_number = int(filemetadata["runNumber"])
-        else:
-            run_number = int(filemetadata)
-        run_numberMod = run_number % 1000
-        runpath = "%03dxxx" % ((run_number - run_numberMod) / 1000)
-        return runpath
-
-    def _formatPath(self, path):
-        """format path to string with 1 digit precision"""
-        if isinstance(path, float) or isinstance(path, int):
-            path = f"{path:.1f}"
-        return str(path)
-
-    def createTarLogFiles(self, inputpath, tarname):
-        """create tar of log and histogram files"""
-        tarmode = "w:gz"
-        tar = tarfile.open(tarname, tarmode)
-
-        for subdir in ["Log/*", "Histograms/*"]:
-            logdir = os.path.join(inputpath, subdir)
-
-            res = self._checkemptydir(logdir)
-            if not res["OK"]:
-                return res
-
-            for localfile in glob.glob(logdir):
-                tar.add(localfile, arcname=localfile.split("/")[-1])
-
-        tar.close()
-
+    """
+    if isinstance(filemetadata, dict):
+      run_number = int(filemetadata['runNumber'])
+    else:
+      run_number = int(filemetadata)
+    run_numberMod = run_number % 1000
+    runpath = '%03dxxx' % ((run_number - run_numberMod) / 1000)
+    return runpath
+
+  def _formatPath(self, path):
+    """ format path to string with 1 digit precision
+    """
+    if isinstance(path, float) or isinstance(path, int):
+      path = '%.1f' % path
+    return str(path)
+
+  def createTarLogFiles(self, inputpath, tarname):
+    """ create tar of log and histogram files
+    """
+    tarmode = 'w:gz'
+    tar = tarfile.open(tarname, tarmode)
+
+    for subdir in ['Log/*', 'Histograms/*']:
+      logdir = os.path.join(inputpath, subdir)
+
+      res = self._checkemptydir(logdir)
+      if not res['OK']:
+        return res
+
+      for localfile in glob.glob(logdir):
+        tar.add(localfile, arcname=localfile.split('/')[-1])
+
+    tar.close()
+
+    return DIRAC.S_OK()
+
+  def createMDStructure(self, metadata, metadatafield, basepath, program_category):
+    """ create meta data structure
+    """
+    # ## Add metadata fields to the DFC
+    mdfield = json.loads(metadatafield)
+    for key, value in mdfield.items():
+      res = self.fc.addMetadataField(key, value)
+      if not res['OK']:
+        return res
+
+    # ## Create the directory structure
+    md = json.loads(metadata, object_pairs_hook=collections.OrderedDict)
+
+    path = basepath
+    process_program = program_category + '_prog'
+    for key, value in collections.OrderedDict((k, md[k]) for k in (
+            'MCCampaign', 'site', 'particle', process_program) if k in md).items():
+      path = os.path.join(path, self._formatPath(value))
+      res = self.fc.createDirectory(path)
+      if not res['OK']:
+        return res
+
+      # Set directory metadata for each subdir: 'site', 'particle', 'process_program'
+      res = self.fcc.setMetadata(path, {key: value})
+      if not res['OK']:
+        return res
+
+    # Create the TransformationID subdir and set MD
+    # ## Get the TransformationID
+    TransformationID = '0000' # used for local execution or submission to wms
+    if 'JOBID' in os.environ:
+      jobID = os.environ['JOBID']
+      dirac = Dirac()
+      res = dirac.getJobJDL(jobID)
+      if 'TransformationID' in res['Value']:
+        TransformationID = res['Value']['TransformationID']
+
+    path = os.path.join(path, TransformationID)
+    res = self.fc.createDirectory(path)
+    if not res['OK']:
+      return res
+
+    process_program_version = process_program + '_version'
+    res = self.fcc.setMetadata(
+        path,
+        dict(
+            (k,
+             md[k]) for k in (
+                'phiP',
+                'thetaP',
+                'array_layout',
+                process_program_version,
+                'sct') if k in md))
+    if not res['OK']:
+      return res
+
+    # Create the Data and Log subdirs and set MD
+    Transformation_path = path
+    for subdir in ['Data', 'Log']:
+      path = os.path.join(Transformation_path, subdir)
+      res = self.fc.createDirectory(path)
+      if not res['OK']:
+        return res
+
+    # Set metadata if not already defined
+      res = self.fcc.getDirectoryUserMetadata(path)
+      if not res['OK']:
+        return res
+      if 'outputType' not in res['Value']:
+        res = self.fcc.setMetadata(path, {'outputType': subdir})
+        if not res['OK']:
+          return res
+
+    # MD for the Data directory - data_level and configuration_id
+    path = os.path.join(Transformation_path, 'Data')
+    # Set metadata if not already defined
+    res = self.fcc.getDirectoryUserMetadata(path)
+    if not res['OK']:
+      return res
+    if 'data_level' or 'configuration_id' or 'merged' not in res['Value']:
+      res = self.fcc.setMetadata(path, {'data_level': md['data_level'],
+                                        'configuration_id': md['configuration_id'],
+                                        'merged': md.get('merged', 0)  # new md, not defined for older tasks
+                                        })
+      if not res['OK']:
+        return res
+
+    return DIRAC.S_OK(Transformation_path)
+
+  def putAndRegister(self, lfn, localfile, filemetadata, DataType='SimtelProd'):
+    """ put and register one file and set metadata
+    """
+    # ## Get the list of Production SE
+    res = self._getSEList('ProductionOutputs', DataType)
+    if res['OK']:
+      ProductionSEList = res['Value']
+    else:
+      return res
+
+    # ## Get the list of Failover SE
+    res = self._getSEList('ProductionOutputsFailover', DataType)
+    if res['OK']:
+      FailoverSEList = res['Value']
+    else:
+      return res
+
+    # ## Upload file to a Production SE
+    res = self._putAndRegisterToSEList(lfn, localfile, ProductionSEList)
+    if not res['OK']:
+      DIRAC.gLogger.error('Failed to upload file to any Production SE: %s' % ProductionSEList)
+      # ## Upload file to a Failover SE
+      res = self._putAndRegisterToSEList(lfn, localfile, FailoverSEList)
+      if not res['OK']:
+        return DIRAC.S_ERROR('Failed to upload file to any Failover SE: %s' % FailoverSEList)
+
+    # ## Set file metadata: jobID, subarray, sct
+    if res['OK']:
+      fmd = json.loads(filemetadata)
+      if 'JOBID' in os.environ:
+        fmd.update({'jobID': os.environ['JOBID']})
+      filename = os.path.basename(localfile)
+      # set subarray and sct md from filename
+      p = re.compile('subarray-\\d+')
+      if p.search(filename) is not None:
+        subarray = p.search(filename).group()
+        fmd.update({'subarray': subarray})
+      sct = 'False'
+      p = re.compile('nosct')
+      psct = re.compile('sct')
+      if p.search(filename) is None and psct.search(filename) is not None:
+        sct = 'True'
+      # ## Set sct flag only for production data
+      res = self.fcc.getFileUserMetadata(lfn)
+      if DataType == 'SimtelProd' and res['Value']['outputType'] == 'Data':
+        fmd.update({'sct': sct})
+      res = self.fc.setMetadata(lfn, fmd)
+      if not res['OK']:
+        return res
+
+      return DIRAC.S_OK()
+
+  def _putAndRegisterToSEList(self, lfn, localfile, SEList):
+    """ put and register one file to one SE in the SEList
+    """
+    # ## Try to upload file to a SE in the list
+    for SE in SEList:
+      msg = 'Try to upload local file: %s \nwith LFN: %s \nto %s' % (localfile, lfn, SE)
+      DIRAC.gLogger.notice(msg)
+      res = self.dm.putAndRegister(lfn, localfile, SE)
+      DIRAC.gLogger.notice(res)
+      # ##  check if failed
+      if not res['OK']:
+        DIRAC.gLogger.error('Failed to putAndRegister %s \nto %s \nwith message: %s' % (lfn, SE, res['Message']))
+        DIRAC.gLogger.notice('Trying to clean up %s' % lfn)
+        res = self.dm.removeFile(lfn)
+        if res['OK']:
+          DIRAC.gLogger.notice(
+              'Successfully removed %s \n that was not supposed to have been uploaded successfully' %
+              lfn)
+        continue
+      elif lfn in res['Value']['Failed']:
+        DIRAC.gLogger.error('Failed to putAndRegister %s to %s' % (lfn, SE))
+        DIRAC.gLogger.notice('Trying to clean up %s' % lfn)
+        res = self.dm.removeFile(lfn)
+        if res['OK']:
+          DIRAC.gLogger.notice(
+              'Successfully removed %s \n that was not supposed to have been uploaded successfully' %
+              lfn)
+        continue
+      else:
         return DIRAC.S_OK()
+    return DIRAC.S_ERROR()
 
-    def createMDStructure(self, metadata, basepath, program_category):
-        """create meta data structure"""
-
-        ### Create the directory structure
-        md = json.loads(metadata, object_pairs_hook=collections.OrderedDict)
+  def cleanLocalFiles(self, datadir, pattern='*'):
+    """ remove files matching pattern in datadir
+    """
 
-        path = basepath
-        process_program = program_category + "_prog"
-        for key, value in collections.OrderedDict(
-            (k, md[k])
-            for k in ("MCCampaign", "site", "particle", process_program)
-            if k in md
-        ).items():
-            path = os.path.join(path, self._formatPath(value))
-            res = self.fc.createDirectory(path)
-            if not res["OK"]:
-                return res
-
-            # Set directory metadata for each subdir: 'site', 'particle', 'process_program'
-            res = self.fcc.setMetadata(path, {key: value})
-            if not res["OK"]:
-                return res
-
-        # Create the TransformationID subdir and set MD
-        # ## Get the TransformationID
-        TransformationID = "0000"  # used for local execution or submission to wms
-        if "JOBID" in os.environ:
-            jobID = os.environ["JOBID"]
-            dirac = Dirac()
-            res = dirac.getJobJDL(jobID)
-            if "TransformationID" in res["Value"]:
-                TransformationID = res["Value"]["TransformationID"]
-
-        path = os.path.join(path, TransformationID)
-        res = self.fc.createDirectory(path)
-        if not res["OK"]:
-            return res
-
-        process_program_version = process_program + "_version"
-        res = self.fcc.setMetadata(
-            path,
-            {
-                k: md[k]
-                for k in (
-                    "phiP",
-                    "thetaP",
-                    "array_layout",
-                    process_program_version,
-                    "sct",
-                )
-                if k in md
-            },
-        )
-        if not res["OK"]:
-            return res
-
-        # Create the Data and Log subdirs and set MD
-        Transformation_path = path
-        for subdir in ["Data", "Log"]:
-            path = os.path.join(Transformation_path, subdir)
-            res = self.fc.createDirectory(path)
-            if not res["OK"]:
-                return res
-
-            # Set metadata if not already defined
-            res = self.fcc.getDirectoryUserMetadata(path)
-            if not res["OK"]:
-                return res
-            if "outputType" not in res["Value"]:
-                res = self.fcc.setMetadata(path, {"outputType": subdir})
-                if not res["OK"]:
-                    return res
-
-        # MD for the Data directory - data_level and configuration_id
-        path = os.path.join(Transformation_path, "Data")
-        # Set metadata if not already defined
-        res = self.fcc.getDirectoryUserMetadata(path)
-        if not res["OK"]:
-            return res
-        if "data_level" or "configuration_id" or "merged" not in res["Value"]:
-            res = self.fcc.setMetadata(
-                path,
-                {
-                    "data_level": md["data_level"],
-                    "configuration_id": md["configuration_id"],
-                    "merged": md.get(
-                        "merged", 0
-                    ),  # new md, not defined for older tasks
-                },
-            )
-            if not res["OK"]:
-                return res
-
-        return DIRAC.S_OK(Transformation_path)
-
-    def putAndRegister(self, lfn, localfile, filemetadata, DataType="SimtelProd"):
-        """put and register one file and set metadata"""
-        # ## Get the list of Production SE
-        res = self._getSEList("ProductionOutputs", DataType)
-        if res["OK"]:
-            ProductionSEList = res["Value"]
-        else:
-            return res
-
-        # ## Get the list of Failover SE
-        res = self._getSEList("ProductionOutputsFailover", DataType)
-        if res["OK"]:
-            FailoverSEList = res["Value"]
-        else:
-            return res
-
-        # ## Upload file to a Production SE
-        res = self._putAndRegisterToSEList(lfn, localfile, ProductionSEList)
-        if not res["OK"]:
-            DIRAC.gLogger.error(
-                f"Failed to upload file to any Production SE: {ProductionSEList}"
-            )
-            # ## Upload file to a Failover SE
-            res = self._putAndRegisterToSEList(lfn, localfile, FailoverSEList)
-            if not res["OK"]:
-                return DIRAC.S_ERROR(
-                    f"Failed to upload file to any Failover SE: {FailoverSEList}"
-                )
-
-        # ## Set file metadata: jobID, subarray, sct
-        if res["OK"]:
-            fmd = json.loads(filemetadata)
-            if "JOBID" in os.environ:
-                fmd.update({"jobID": os.environ["JOBID"]})
-            filename = os.path.basename(localfile)
-            # set subarray and sct md from filename
-            p = re.compile("subarray-\\d+")
-            if p.search(filename) is not None:
-                subarray = p.search(filename).group()
-                fmd.update({"subarray": subarray})
-            sct = "False"
-            p = re.compile("nosct")
-            psct = re.compile("sct")
-            if p.search(filename) is None and psct.search(filename) is not None:
-                sct = "True"
-            # ## Set sct flag only for production data
-            res = self.fcc.getFileUserMetadata(lfn)
-            if DataType == "SimtelProd" and res["Value"]["outputType"] == "Data":
-                fmd.update({"sct": sct})
-            res = self.fc.setMetadata(lfn, fmd)
-            if not res["OK"]:
-                return res
-
-            return DIRAC.S_OK()
-
-    def _putAndRegisterToSEList(self, lfn, localfile, SEList):
-        """put and register one file to one SE in the SEList"""
-        # ## Try to upload file to a SE in the list
-        for SE in SEList:
-            msg = f"Try to upload local file: {localfile} \nwith LFN: {lfn} \nto {SE}"
-            DIRAC.gLogger.notice(msg)
-            res = self.dm.putAndRegister(lfn, localfile, SE)
-            DIRAC.gLogger.notice(res)
-            # ##  check if failed
-            if not res["OK"]:
-                DIRAC.gLogger.error(
-                    "Failed to putAndRegister %s \nto %s \nwith message: %s"
-                    % (lfn, SE, res["Message"])
-                )
-                DIRAC.gLogger.notice(f"Trying to clean up {lfn}")
-                res = self.dm.removeFile(lfn)
-                if res["OK"]:
-                    DIRAC.gLogger.notice(
-                        "Successfully removed %s \n that was not supposed to have been uploaded successfully"
-                        % lfn
-                    )
-                continue
-            elif lfn in res["Value"]["Failed"]:
-                DIRAC.gLogger.error(f"Failed to putAndRegister {lfn} to {SE}")
-                DIRAC.gLogger.notice(f"Trying to clean up {lfn}")
-                res = self.dm.removeFile(lfn)
-                if res["OK"]:
-                    DIRAC.gLogger.notice(
-                        "Successfully removed %s \n that was not supposed to have been uploaded successfully"
-                        % lfn
-                    )
-                continue
-            else:
-                return DIRAC.S_OK()
-        return DIRAC.S_ERROR()
-
-    def cleanLocalFiles(self, datadir, pattern="*"):
-        """remove files matching pattern in datadir"""
-
-        for localfile in glob.glob(os.path.join(datadir, pattern)):
-            DIRAC.gLogger.notice("Removing local file: ", localfile)
-            os.remove(localfile)
+    for localfile in glob.glob(os.path.join(datadir, pattern)):
+      DIRAC.gLogger.notice('Removing local file: ', localfile)
+      os.remove(localfile)
 
-        return DIRAC.S_OK()
+    return DIRAC.S_OK()
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_dms_check_lfn.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_dms_check_lfn.py`

 * *Files 5% similar despite different names*

```diff
@@ -6,15 +6,15 @@
   Usage:
   cta-dms-check-lfn [options] <ascii file with lfn list>
 """
 
 __RCSID__ = "$Id$"
 
 import DIRAC
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from DIRAC import gLogger
 from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient
 from CTADIRAC.Core.Utilities.tool_box import read_inputs_from_file
 
 @Script()
 def main():
   Script.parseCommandLine(ignoreErrors=True)
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_add_dataset.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_add_dataset.py`

 * *Files 12% similar despite different names*

```diff
@@ -15,61 +15,55 @@
    The file should have the .json extension, e.g. my_dataset.json
 """
 
 __RCSID__ = "$Id$"
 
 import json
 import ast
-import os
 
 import DIRAC
 from DIRAC.Core.Base.Script import Script
 from DIRAC import gLogger
 from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient
 
-
 @Script()
 def main():
-    fc = FileCatalogClient()
-    Script.parseCommandLine(ignoreErrors=True)
-    argss = Script.getPositionalArgs()
-    if len(argss) == 1:
-        inputJson = argss[0]
-        if not inputJson.endswith(".json"):
-            Script.showHelp()
-    else:
-        Script.showHelp()
-
-    # read the meta data query from json file
-    content = open(inputJson).readlines()
-    for line in content:
-        json_string = json.dumps(ast.literal_eval(line))
-
-    MDdict = json.loads(json_string)
-
-    # ensure the integer values are written in the right format
-    for key, value in MDdict.items():
-        if isinstance(value, float):
-            MDdict[key] = {"=": value}
-
-    datasetName = os.path.basename(inputJson).split(".json")[0]
-    datasetPath = os.path.join("/vo.cta.in2p3.fr/datasets/", datasetName)
-    res = fc.addDataset({datasetPath: MDdict})
-
-    if not res["OK"]:
-        gLogger.error(f"Failed to add dataset {datasetName}: {res['Message']}")
-        DIRAC.exit(-1)
-
-    if datasetName in res["Value"]["Failed"]:
-        gLogger.error(
-            "Failed to add dataset %s: %s"
-            % (datasetName, res["Value"]["Failed"][datasetName])
-        )
-        DIRAC.exit(-1)
-
-    gLogger.notice("Successfully added dataset", datasetName)
-    DIRAC.exit()
+  fc = FileCatalogClient()
+  Script.parseCommandLine(ignoreErrors=True)
+  argss = Script.getPositionalArgs()
+  if len(argss) == 1:
+    inputJson = argss[0]
+    if not inputJson.endswith(".json"):
+      Script.showHelp()
+  else:
+    Script.showHelp()
+
+  # read the meta data query from json file
+  content = open(inputJson, 'rt').readlines()
+  for line in content:
+    json_string = json.dumps(ast.literal_eval(line))
+
+  MDdict = json.loads(json_string)
+
+  # ensure the integer values are written in the right format
+  for key, value in MDdict.items():
+    if isinstance(value, float):
+      MDdict[key] = {'=': value}
+
+  datasetName = inputJson.split('.json')[0]
+  datasetPath = '/vo.cta.in2p3.fr/datasets/' + datasetName
+  res = (fc.addDataset({datasetPath: MDdict}))
+
+  if not res['OK']:
+    gLogger.error("Failed to add dataset %s: %s" % (datasetName, res['Message']))
+    DIRAC.exit(-1)
+
+  if datasetName in res['Value']['Failed']:
+    gLogger.error("Failed to add dataset %s: %s" % (datasetName, res['Value']['Failed'][datasetName]))
+    DIRAC.exit(-1)
 
+  gLogger.notice("Successfully added dataset", datasetName)
+  DIRAC.exit()
 
 ####################################################
-if __name__ == "__main__":
-    main()
+if __name__ == '__main__':
+  main()
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_add_file.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_add_file.py`

 * *Files 4% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 # generic imports
 import os
 from multiprocessing import Pool
 
 # DIRAC imports
 from DIRAC import gLogger
 from CTADIRAC.Core.Utilities.tool_box import read_inputs_from_file
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 
 Script.setUsageMessage("""
 Bulk upload of a list of local files from the current directory to a Storage Element
 Usage:
    cta-prod-add-file <ascii file with lfn list> <SE>
 """)
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_add_prov.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_add_prov.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_check_replicas.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_check_replicas.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 __RCSID__ = "$Id$"
 
 
 # DIRAC imports
 import DIRAC
 from DIRAC import gLogger
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 
 Script.setUsageMessage("""
 Check replica location against the a given SE
 Usage:
    cta-check-get-replicas <ascii file with lfn list> <destSE>
 """)
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_dump_dataset.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_dump_dataset.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_failure_monitor.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_failure_monitor.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 #!/bin/env python
 """
   Simple terminal job error summary
 """
 
 import DIRAC
 from DIRAC import gLogger
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from CTADIRAC.Core.Utilities import tool_box
 
 @Script()
 def main():
   ''' Select jobs based on conditions
   '''
   Script.registerSwitch("", "owner=", "the job owner")
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_fix_nsb.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_fix_nsb.py`

 * *Files 3% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 __RCSID__ = "$Id$"
 
 # generic imports
 import os
 import six
 
 # DIRAC imports
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 import DIRAC
 
 Script.parseCommandLine(ignoreErrors=True)
 
 from DIRAC import gLogger
 from DIRAC.Interfaces.API.Dirac import Dirac
 from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_get_file.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_get_file.py`

 * *Files 5% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 from multiprocessing import Pool
 import signal
 import os
 
 # DIRAC imports
 from DIRAC import gLogger
 from CTADIRAC.Core.Utilities.tool_box import read_inputs_from_file
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 
 Script.setUsageMessage("""
 Bulk get replicas from a list of lfns
 Usage:
    cta-prod-get-file [options] <ascii file with lfn list>
 """)
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_get_replicas.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_get_replicas.py`

 * *Files 14% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 # generic imports
 from multiprocessing import Pool
 
 # DIRAC imports
 import DIRAC
 from DIRAC import gLogger
 from CTADIRAC.Core.Utilities.tool_box import read_inputs_from_file
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 
 Script.setUsageMessage("""
 Bulk get replicas from a list of lfns
 Usage:
    cta-prod-get-replicas [options] <ascii file with lfn list>
 """)
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_get_se_status.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_get_se_status.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 #!/usr/bin/env python
 
 __RCSID__ = "$Id$"
 
 import DIRAC
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 
 Script.setUsageMessage('\n'.join(['Get storage elements usage of production SEs',
                                   'Usage:',
                                   '%s <file with output of lcg-infosites --vo vo.cta.in2p3.fr se>' % Script.scriptName,
                                   '\ne.g: %s ccsrm02.in2p3.fr (default is all SEs)' % Script.scriptName
                                   ]))
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_git_clone.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_git_clone.py`

 * *Files 3% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 __RCSID__ = "$Id$"
 
 # generic imports
 from git import Repo
 
 # DIRAC imports
 import DIRAC
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 
 @Script()
 def main():
   Script.parseCommandLine(ignoreErrors=True)
   args = Script.getPositionalArgs()
   branch = None
   if len(args) == 1:
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_init_prov.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_init_prov.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_managedata.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_managedata.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,88 +1,88 @@
 #!/usr/bin/env python
 """ Data management script for production
     create DFC MetaData structure put and register files in DFC
     should work for corsika, simtel and EventDisplay output
+    derived from cta-prod3-managedata.py and cta-analysis-managedata.py
+                    JB September 2018
 """
 
 __RCSID__ = "$Id$"
 
 # generic imports
 import os
 import glob
 import json
 
 # DIRAC imports
 import DIRAC
-from DIRAC.Core.Base.Script import Script
-
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 Script.parseCommandLine()
 
 # Specific DIRAC imports
 from CTADIRAC.Core.Utilities.tool_box import run_number_from_filename
 from CTADIRAC.Core.Workflow.Modules.ProdDataManager import ProdDataManager
 
-
 @Script()
 def main():
-    """simple wrapper to put and register all production files
-
-    Keyword arguments:
-    args -- a list of arguments in order []
-    """
-    args = Script.getPositionalArgs()
-    metadata = args[0]
-    file_metadata = args[1]
-    base_path = args[2]
-    output_pattern = args[3]
-    package = args[4]
-    program_category = args[5]
-    catalogs = args[6]
-    output_type = args[7]
-
-    # Load catalogs
-    catalogs_json = json.loads(catalogs)
-
-    # Create MD structure
-    prod_dm = ProdDataManager(catalogs_json)
-    result = prod_dm.createMDStructure(metadata, base_path, program_category)
-    if result["OK"]:
-        path = result["Value"]
-    else:
-        return result
-
-    # Check the content of the output directory
-    result = prod_dm._checkemptydir(output_pattern)
-    if not result["OK"]:
-        return result
-
-    # Dump the list of output LFNs
-    file = open("output_lfns.txt", "w")
-
-    # Loop over each file and upload and register
-    for localfile in glob.glob(output_pattern):
-        file_name = os.path.basename(localfile)
-        # Check run number, assign one as file metadata if needed
-        fmd_dict = json.loads(file_metadata)
-        try:
-            run_number = run_number_from_filename(file_name, package)
-        except BaseException:
-            run_number = -9999
-            DIRAC.gLogger.notice("Could not get a correct run number, assigning -9999")
-        fmd_dict["runNumber"] = "%08d" % int(run_number)
-        # get the output file path
-        run_path = prod_dm._getRunPath(fmd_dict)
-        lfn = os.path.join(path, output_type, run_path, file_name)
-        fmd_json = json.dumps(fmd_dict)
-        result = prod_dm.putAndRegister(lfn, localfile, fmd_json, package)
-        if not result["OK"]:
-            return result
-        file.write(lfn)
-        file.write("\n")
-    file.close()
+  """ simple wrapper to put and register all production files
 
-    DIRAC.exit()
+  Keyword arguments:
+  args -- a list of arguments in order []
+  """
+  args = Script.getPositionalArgs()
+  metadata = args[0]
+  metadata_fields = args[1]
+  file_metadata = args[2]
+  base_path = args[3]
+  output_pattern = args[4]
+  package = args[5]
+  program_category = args[6]
+  catalogs = args[7]
+  output_type = args[8]
+
+  # Load catalogs
+  catalogs_json = json.loads(catalogs)
+
+  # Create MD structure
+  prod_dm = ProdDataManager(catalogs_json)
+  result = prod_dm.createMDStructure(metadata, metadata_fields, base_path, program_category)
+  if result['OK']:
+    path = result['Value']
+  else:
+    return result
+
+  # Check the content of the output directory
+  result = prod_dm._checkemptydir(output_pattern)
+  if not result['OK']:
+    return result
+
+  # Dump the list of output LFNs
+  file = open("output_lfns.txt", 'w')
+
+  # Loop over each file and upload and register
+  for localfile in glob.glob(output_pattern):
+    file_name = os.path.basename(localfile)
+    # Check run number, assign one as file metadata if needed
+    fmd_dict = json.loads(file_metadata)
+    try:
+      run_number = run_number_from_filename(file_name, package)
+    except BaseException:
+      run_number = -9999
+      DIRAC.gLogger.notice('Could not get a correct run number, assigning -9999')
+    fmd_dict['runNumber'] = '%08d' % int(run_number)
+    # get the output file path
+    run_path = prod_dm._getRunPath(fmd_dict)
+    lfn = os.path.join(path, output_type, run_path, file_name)
+    fmd_json = json.dumps(fmd_dict)
+    result = prod_dm.putAndRegister(lfn, localfile, fmd_json, package)
+    if not result['OK']:
+      return result
+    file.write(lfn)
+    file.write('\n')
+  file.close()
 
+  DIRAC.exit()
 
 ####################################################
-if __name__ == "__main__":
-    main()
+if __name__ == '__main__':
+  main()
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_mark_corrupted_DL0.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_mark_corrupted_DL0.py`

 * *Files 8% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 __RCSID__ = "$Id$"
 
 # generic imports
 import os
 import six
 
 # DIRAC imports
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 import DIRAC
 
 Script.parseCommandLine(ignoreErrors=True)
 
 from DIRAC import gLogger
 from DIRAC.Interfaces.API.Dirac import Dirac
 from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_monitor.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_monitor.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 #!/usr/bin/env python
 """
   Simple terminal job monitoring
 """
 __RCSID__ = "$Id$"
 
 from DIRAC import gLogger
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from CTADIRAC.Core.Utilities import tool_box
 from CTADIRAC.Core.Utilities.tool_box import highlight
 
 @Script()
 def main():
   ''' Select jobs based on conditions
   '''
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_move_dataset.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_move_dataset.py`

 * *Files 3% similar despite different names*

```diff
@@ -21,15 +21,15 @@
 
 __RCSID__ = "$Id$"
 
 import os
 
 import DIRAC
 from DIRAC import gLogger
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient
 from DIRAC.TransformationSystem.Utilities.ReplicationTransformation import createDataTransformation
 from CTADIRAC.Core.Utilities.tool_box import read_inputs_from_file
 
 def get_dataset_info(dataset_name):
   """ Return essential dataset information
       Name, number of files, total size and meta query
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_move_dataset_status.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_move_dataset_status.py`

 * *Files 2% similar despite different names*

```diff
@@ -15,15 +15,15 @@
 
 __RCSID__ = "$Id$"
 
 import os
 
 import DIRAC
 from DIRAC import gLogger
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient
 from CTADIRAC.Core.Utilities.tool_box import read_inputs_from_file
 from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient
 
 def get_list_of_datasets(tag=''):
   fc = FileCatalogClient()
   dataset_tag = '*%s*' % tag
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_remove_corrupted_file.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_remove_corrupted_file.py`

 * *Files 9% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 __RCSID__ = "$Id$"
 
 # Generic imports
 import os
 
 # DIRAC imports
 import DIRAC
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 Script.parseCommandLine()
 
 # Specific DIRAC imports
 from DIRAC.DataManagementSystem.Client.DataManager import DataManager
 from DIRAC.Interfaces.API.Dirac import Dirac
 
 @Script()
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_remove_dataset.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_update_dataset.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,21 +1,22 @@
 #!/usr/bin/env python
 '''
-Remove a given dataset
+Update a given dataset or a list of datasets
 
 Usage:
-   cta-prod-remove-dataset <datasetName or ascii file with a list of datasets>
+ cta-prod-update-dataset <datasetName or ascii file with a list of datasets>
 '''
 
 __RCSID__ = "$Id$"
 
 import os
+
 import DIRAC
 from DIRAC import gLogger
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from CTADIRAC.Core.Utilities.tool_box import read_inputs_from_file
 from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient
 
 @Script()
 def main():
     Script.parseCommandLine(ignoreErrors=True)
     argss = Script.getPositionalArgs()
@@ -27,20 +28,19 @@
         datasetList = read_inputs_from_file(argss[0])
       else:
         datasetList.append(argss[0])
     else:
       Script.showHelp()
 
     for dataset in datasetList:
-      result = fc.removeDataset(dataset)
+      result = fc.updateDataset(dataset)
 
       if not result['OK']:
-        gLogger.error("Failed to remove %s: %s" % (dataset, result['Message']))
+        gLogger.error("Failed to update dataset %s: %s" % (dataset, result['Message']))
         DIRAC.exit(-1)
       else:
-        gLogger.notice("Successfully removed dataset", dataset)
+        gLogger.notice("Successfully updated dataset", dataset)
 
     DIRAC.exit()
 
-####################################################
 if __name__ == '__main__':
-  main()
+  main()
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_remove_file.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_remove_file.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_setup_software.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_setup_software.py`

 * *Files 2% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 __RCSID__ = "$Id$"
 
 # generic imports
 import os
 
 # DIRAC imports
 import DIRAC
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 
 Script.registerSwitch("p:", "Package=", "Software package name")
 Script.registerSwitch("v:", "Version=", "Base version to look for")
 Script.registerSwitch("a:", "Category=", "Program category (simulations, analysis...)")
 Script.registerSwitch("g:", "Compiler=", "Target a compiler_optimization configuration")
 Script.registerSwitch("r:", "Repository=", "Target CVMFS repository")
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_show_dataset.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_show_dataset.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_unregister_file.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_unregister_file.py`

 * *Files 13% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 
 # generic imports
 from multiprocessing import Pool
 
 # DIRAC imports
 from DIRAC import gLogger
 from CTADIRAC.Core.Utilities.tool_box import read_inputs_from_file
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 
 Script.setUsageMessage("""
 Bulk removal of a list of files from the catalog
 Usage:
    cta-prod-unregister-file <ascii file with lfn list>
 """)
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_update_dataset.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_remove_dataset.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,22 +1,21 @@
 #!/usr/bin/env python
 '''
-Update a given dataset or a list of datasets
+Remove a given dataset
 
 Usage:
- cta-prod-update-dataset <datasetName or ascii file with a list of datasets>
+   cta-prod-remove-dataset <datasetName or ascii file with a list of datasets>
 '''
 
 __RCSID__ = "$Id$"
 
 import os
-
 import DIRAC
 from DIRAC import gLogger
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from CTADIRAC.Core.Utilities.tool_box import read_inputs_from_file
 from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient
 
 @Script()
 def main():
     Script.parseCommandLine(ignoreErrors=True)
     argss = Script.getPositionalArgs()
@@ -28,19 +27,20 @@
         datasetList = read_inputs_from_file(argss[0])
       else:
         datasetList.append(argss[0])
     else:
       Script.showHelp()
 
     for dataset in datasetList:
-      result = fc.updateDataset(dataset)
+      result = fc.removeDataset(dataset)
 
       if not result['OK']:
-        gLogger.error("Failed to update dataset %s: %s" % (dataset, result['Message']))
+        gLogger.error("Failed to remove %s: %s" % (dataset, result['Message']))
         DIRAC.exit(-1)
       else:
-        gLogger.notice("Successfully updated dataset", dataset)
+        gLogger.notice("Successfully removed dataset", dataset)
 
     DIRAC.exit()
 
+####################################################
 if __name__ == '__main__':
-  main()
+  main()
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_prod_verifysteps.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_prod_verifysteps.py`

 * *Files 1% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 
 # generic imports
 import os
 import glob
 
 # DIRAC imports
 import DIRAC
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 
 Script.setUsageMessage('\n'.join([__doc__.split('\n')[1],
                                   'Usage:',
                                   '  %s stepName' % Script.scriptName,
                                   'Arguments:',
                                   '  stepName: corsika, simtel, merging',
                                   '\ne.g: %s corsika' % Script.scriptName
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_rms_request.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_rms_request.py`

 * *Files 2% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 __RCSID__ = "$Id$"
 
 import datetime
 import os
 
 import DIRAC
 from DIRAC import gLogger
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 
 Script.registerSwitch('', 'Job=', '   JobID[,jobID2,...]')
 Script.registerSwitch('', 'Transformation=', '   transformation ID')
 Script.registerSwitch('', 'Tasks=', '      Associated to --Transformation, list of taskIDs')
 Script.registerSwitch('', 'TaskStatus=', '      Associated to --Transformation')
 Script.registerSwitch('', 'Stat', '   Only print summary informations')
 Script.registerSwitch('', 'Verbose', '   Print more information')
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_add_files.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_add_files.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_clean.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_clean.py`

 * *Files 25% similar despite different names*

```diff
@@ -6,15 +6,15 @@
   Usage:
     cta-transformation-clean <transID>
 """
 
 __RCSID__ = "$Id$"
 
 import DIRAC
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient
 
 @Script()
 def main():
     Script.parseCommandLine()
     args = Script.getPositionalArgs()
     if (len(args) != 1):
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_delete.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_delete.py`

 * *Files 4% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 """
 
 __RCSID__ = "$Id$"
 
 import os
 
 import DIRAC
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient
 
 @Script()
 def main():
     Script.parseCommandLine()
     args = Script.getPositionalArgs()
     if (len(args) != 1):
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_get_files.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_get_files.py`

 * *Files 4% similar despite different names*

```diff
@@ -17,15 +17,15 @@
 
 __RCSID__ = "$Id$"
 
 import os
 
 import DIRAC
 from DIRAC import gLogger
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient
 
 @Script()
 def main():
 
   Script.registerSwitch('', 'FileStatus=', '    file status')
   Script.registerSwitch('', 'TaskStatus=', '    task status')
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_get_tasks.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_get_tasks.py`

 * *Files 3% similar despite different names*

```diff
@@ -4,15 +4,15 @@
   Get tasks attached to a transformation for a given TaskStatus
 """
 
 __RCSID__ = "$Id$"
 
 import DIRAC
 from DIRAC import gLogger
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient
 
 @Script()
 def main():
   Script.registerSwitch('', 'TransID=', 'transformation ID')
   Script.registerSwitch('', 'Status=', 'task status')
   Script.parseCommandLine()
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_select.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_select.py`

 * *Files 16% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 """
   Get transformations with a given Status
 """
 
 __RCSID__ = "$Id$"
 
 import DIRAC
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient
 
 @Script()
 def main():
 
   Script.registerSwitch('', 'Status=', 'status')
   Script.parseCommandLine()
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_show_progress.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_show_progress.py`

 * *Files 2% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 
 __RCSID__ = "$Id$"
 
 import os
 
 import DIRAC
 from DIRAC import gLogger
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient
 
 
 def get_transformation_info(transID):
 
   transClient = TransformationClient()
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_treat_done_tasks.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_treat_done_tasks.py`

 * *Files 9% similar despite different names*

```diff
@@ -8,15 +8,15 @@
     cta-transformation-treat-done-tasks <ascii file with a list of (transID, lfn)>
 """
 
 __RCSID__ = "$Id$"
 
 import DIRAC
 from DIRAC import gLogger
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient
 
 def read_inputs(file_path):
   content = open(file_path, 'rt').readlines()
   resList = []
   for line in content:
     transID = line.strip().split(" ")[0]
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_treat_failed_tasks.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_treat_failed_tasks.py`

 * *Files 4% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 """
 
 __RCSID__ = "$Id$"
 
 # DIRAC imports
 import DIRAC
 from DIRAC import gLogger
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient
 
 Script.parseCommandLine(ignoreErrors=True)
 
 def read_inputs(file_path):
   content = open(file_path, 'rt').readlines()
   resList = []
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_treat_incomplete_transfers.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_treat_incomplete_transfers.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 #!/usr/bin/env python
 
 __RCSID__ = "$Id$"
 
 # DIRAC imports
 import DIRAC
 from DIRAC import gLogger
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient
 
 Script.setUsageMessage("""
 Treat the incomplete transfers by removing the replicas at source SEs but not at the destination SE
 
 Usage:
    cta-prod-treat-incomplete-transfers <ascii file with list of (transID lfn)> <destSE>
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_transformation_treat_problematic_files.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_transformation_treat_problematic_files.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 #!/usr/bin/env python
 
 __RCSID__ = "$Id$"
 
 # DIRAC imports
 import DIRAC
 from DIRAC import gLogger
-from DIRAC.Core.Base.Script import Script
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient
 
 Script.setUsageMessage("""
 Treat problematic tasks for files with No replicas
 Unregister files from the catalog and set transformation files to Processed
 
 Usage:
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Core/scripts/cta_user_managedata.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Core/scripts/cta_user_managedata.py`

 * *Files 22% similar despite different names*

```diff
@@ -8,59 +8,57 @@
 # generic imports
 import os
 import glob
 import json
 
 # DIRAC imports
 import DIRAC
-from DIRAC.Core.Base.Script import Script
-
+from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
 Script.parseCommandLine()
 
 # Specific DIRAC imports
 from DIRAC.Core.Utilities import List
 from CTADIRAC.Core.Workflow.Modules.ProdDataManager import ProdDataManager
 
 ####################################################
 
-
 @Script()
 def main():
-    """simple wrapper to put and register all analysis files
+  """ simple wrapper to put and register all analysis files
 
-    Keyword arguments:
-    args -- a list of arguments in order []
-    """
-    args = Script.getPositionalArgs()
-    outputpattern = args[0]
-    outputpath = args[1]
-    SEListArg = json.loads(args[2])
-    SEList = []
-    for SE in SEListArg:
-        SEList.append(str(SE))
-    # Load catalogs
-    catalogs = args[3]
-    catalogs_json = json.loads(catalogs)
-
-    # # Init DataManager
-    prod_dm = ProdDataManager(catalogs_json)
-
-    # # Upload data files
-    res = prod_dm._checkemptydir(outputpattern)
-    if not res["OK"]:
-        return res
-
-    for localfile in glob.glob(outputpattern):
-        filename = os.path.basename(localfile)
-        lfn = os.path.join(outputpath, filename)
-        SEList = List.randomize(SEList)
-        res = prod_dm._putAndRegisterToSEList(lfn, localfile, SEList)
-        # ##  check if failed
-        if not res["OK"]:
-            return res
+  Keyword arguments:
+  args -- a list of arguments in order []
+  """
+  args = Script.getPositionalArgs()
+  outputpattern = args[0]
+  outputpath = args[1]
+  SEListArg = json.loads(args[2])
+  SEList = []
+  for SE in SEListArg:
+    SEList.append(str(SE))
+  # Load catalogs
+  catalogs = args[3]
+  catalogs_json = json.loads(catalogs)
+
+  # # Init DataManager
+  prod_dm = ProdDataManager(catalogs_json)
+
+  # # Upload data files
+  res = prod_dm._checkemptydir(outputpattern)
+  if not res['OK']:
+    return res
+
+  for localfile in glob.glob(outputpattern):
+    filename = os.path.basename(localfile)
+    lfn = os.path.join(outputpath, filename)
+    SEList = List.randomize(SEList)
+    res = prod_dm._putAndRegisterToSEList(lfn, localfile, SEList)
+    # ##  check if failed
+    if not res['OK']:
+      return res
 
-    DIRAC.exit()
+  DIRAC.exit()
 
 
 ####################################################
-if __name__ == "__main__":
-    main()
+if __name__ == '__main__':
+  main()
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/Client/ProvBase.py` & `CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/Client/ProvBase.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/Client/ProvClient.py` & `CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/Client/ProvClient.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/Client/testProvClient_muon.py` & `CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/Client/testProvClient_muon.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/DB/ProvenanceDB.py` & `CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/DB/ProvenanceDB.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/DataManagementSystem/Service/ProvenanceManagerHandler.py` & `CTADIRAC-2.2a3/src/CTADIRAC/DataManagementSystem/Service/ProvenanceManagerHandler.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/CtapipeMergeJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod5CtaPipeMergeJob.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,32 +1,37 @@
 """
-  Simple Wrapper on the Job class to run ctapipe merge
+  Simple Wrapper on the Job class to run ctapipe merging tool
 """
 
 __RCSID__ = "$Id$"
 
 # generic imports
 import json
 
 # DIRAC imports
-from CTADIRAC.Interfaces.API.ProcessingJob import ProcessingJob
+from CTADIRAC.Interfaces.API.Prod5Stage1Job import Prod5Stage1Job
 
 
-class CtapipeMergeJob(ProcessingJob):
-    """Job extension class for ctapipe merging"""
+class Prod5CtaPipeMergeJob(Prod5Stage1Job):
+    """Job extension class for ctapipe processing"""
 
-    def __init__(self, **kwargs):
-        """Constructor"""
-        super().__init__(**kwargs)
+    def __init__(self, cpuTime=432000):
+        """Constructor
+
+        Keyword arguments:
+        cpuTime -- max cpu time allowed for the job
+        """
+        Prod5Stage1Job.__init__(self)
+        self.setCPUTime(cpuTime)
+        # defaults
+        self.version = "v0.15.0"
         self.setType("Merging")
         self.setName("ctapipe_merge")
         self.prog_name = "ctapipe-merge"
-        # defaults
         self.output_data_level = 2
-        self.output_extension = "merged.DL2.h5"
         self.options = ""
 
     def set_output_metadata(self, metadata):
         """Set meta data
 
         Parameters:
         metadata -- metadata dictionary from the telescope simulation
@@ -89,55 +94,71 @@
         )
         sw_step["Value"]["name"] = "Step%i_SetupSoftware" % i_step
         sw_step["Value"]["descr_short"] = "Setup software"
         i_step += 1
 
         # step 3 run merge
         merge_step = self.setExecutable(
-            "./dirac_ctapipe-merge_wrapper",
-            arguments=f"--out_ext {self.output_extension} {self.options}",
+            "./dirac_run_stage1_merge",
+            arguments=self.options,
             logFile="ctapipe_merge_Log.txt",
         )
         merge_step["Value"]["name"] = "Step%i_ctapipe_merge" % i_step
         merge_step["Value"]["descr_short"] = "Run ctapipe merge"
         i_step += 1
 
         # step 4 set meta data and register Data
         meta_data_json = json.dumps(self.output_metadata)
         file_meta_data_json = json.dumps(self.output_file_metadata)
 
+        meta_data_field = {
+            "array_layout": "VARCHAR(128)",
+            "site": "VARCHAR(128)",
+            "particle": "VARCHAR(128)",
+            "phiP": "float",
+            "thetaP": "float",
+            "sct": "VARCHAR(128)",
+            self.program_category + "_prog": "VARCHAR(128)",
+            self.program_category + "_prog_version": "VARCHAR(128)",
+            "data_level": "int",
+            "configuration_id": "int",
+            "merged": "int",
+        }
+        meta_data_field_json = json.dumps(meta_data_field)
+
         # register Data
         data_output_pattern = "./Data/*.h5"  # %self.output_data_level
         dm_step = self.setExecutable(
             "cta-prod-managedata",
-            arguments="'%s' '%s' %s '%s' %s %s '%s' Data"
+            arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Data"
             % (
                 meta_data_json,
+                meta_data_field_json,
                 file_meta_data_json,
                 self.base_path,
                 data_output_pattern,
                 self.package,
                 self.program_category,
                 self.catalogs,
             ),
             logFile="DataManagement_Log.txt",
         )
-        dm_step["Value"]["name"] = f"Step{i_step}_DataManagement"
+        dm_step["Value"]["name"] = "Step%s_DataManagement" % i_step
         dm_step["Value"][
             "descr_short"
         ] = "Save data files to SE and register them in DFC"
         i_step += 1
 
         # step 6 failover step
         failover_step = self.setExecutable(
             "/bin/ls -l", modulesList=["Script", "FailoverRequest"]
         )
-        failover_step["Value"]["name"] = f"Step{i_step}_Failover"
+        failover_step["Value"]["name"] = "Step%s_Failover" % i_step
         failover_step["Value"]["descr_short"] = "Tag files as unused if job failed"
         i_step += 1
 
         # Step 7 - debug only
         if debug:
             ls_step = self.setExecutable("/bin/ls -Ralhtr", logFile="LS_End_Log.txt")
-            ls_step["Value"]["name"] = f"Step{i_step}_LSHOME_End"
+            ls_step["Value"]["name"] = "Step%s_LSHOME_End" % i_step
             ls_step["Value"]["descr_short"] = "list files in Home directory"
             i_step += 1
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/CtapipeTrainClassifierJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod5CtaPipeModelingJob.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,31 +1,39 @@
 """
-  Simple Wrapper on the Job class to run ctapipe-train-particle-classifier
+  Simple Wrapper on the Job class to run a ctapipe modeling job
 """
 
 __RCSID__ = "$Id$"
 
 # generic imports
 import json
 
 # DIRAC imports
-from CTADIRAC.Interfaces.API.ProcessingJob import ProcessingJob
+from CTADIRAC.Interfaces.API.Prod5Stage1Job import Prod5Stage1Job
 
 
-class CtapipeTrainClassifierJob(ProcessingJob):
-    """Job extension class for ctapipe particle classifier"""
+class Prod5CtaPipeModelingJob(Prod5Stage1Job):
+    """Job extension class for ctapipe stage1 modeling processing"""
 
-    def __init__(self, **kwargs):
-        """Constructor"""
-        super().__init__(**kwargs)
-        self.setName("ctapipe_train-particle-classifier")
-        self.setType("DL0_Reprocessing")
-        self.prog_name = "ctapipe-train-particle-classifier"
+    def __init__(self, cpuTime=432000):
+        """Constructor
+
+        Keyword arguments:
+        cpuTime -- max cpu time allowed for the job
+        """
+        Prod5Stage1Job.__init__(self)
+        self.setCPUTime(cpuTime)
         # defaults
-        self.options = ""
+        self.version = "v0.15.0"
+        self.setName("ctapipe_modeling")
+        self.setType("DL0_Reprocessing")
+        self.program_category = "stage1"
+        self.prog_name = "ctapipe-modeling"
+        self.ctapipe_base_dl2_config = "base_dl2_config.yml"
+        self.ctapipe_site_config = "prod5b_paranal_alpha_nectarcam.yml"
         self.output_data_level = 2
 
     def set_executable_sequence(self, debug=False):
         """Setup job workflow by defining the sequence of all executables
         All parameters shall have been defined before that method is called.
         """
         i_step = 0
@@ -45,55 +53,96 @@
         )
         sw_step["Value"]["name"] = "Step%i_SetupSoftware" % i_step
         sw_step["Value"]["descr_short"] = "Setup software"
         i_step += 1
 
         # step 3 run stage1
         ev_step = self.setExecutable(
-            "./dirac_ctapipe-train-particle-classifier_wrapper",
-            arguments=f"{self.options}",
-            logFile="ctapipe_train-classifier_Log.txt",
+            "./dirac_run_ctapipe_modeling",
+            arguments=f"--base_config {self.ctapipe_base_dl2_config} \
+                                             --site_config {self.ctapipe_site_config} \
+                                             --input_ext {self.simtel_ext}",
+            logFile="ctapipe_stage1_Log.txt",
         )
-        ev_step["Value"]["name"] = "Step%i_ctapipe_train_classifier" % i_step
-        ev_step["Value"]["descr_short"] = "Run ctapipe train classifier"
+        ev_step["Value"]["name"] = "Step%i_ctapipe_stage1" % i_step
+        ev_step["Value"]["descr_short"] = "Run ctapipe stage 1"
         i_step += 1
 
         # step 4 set meta data and register Data
         meta_data_json = json.dumps(self.output_metadata)
         file_meta_data_json = json.dumps(self.output_file_metadata)
 
+        meta_data_field = {
+            "array_layout": "VARCHAR(128)",
+            "site": "VARCHAR(128)",
+            "particle": "VARCHAR(128)",
+            "phiP": "float",
+            "thetaP": "float",
+            "sct": "VARCHAR(128)",
+            self.program_category + "_prog": "VARCHAR(128)",
+            self.program_category + "_prog_version": "VARCHAR(128)",
+            "data_level": "int",
+            "configuration_id": "int",
+            "merged": "int",
+        }
+        meta_data_field_json = json.dumps(meta_data_field)
+
         # register Data
-        data_output_pattern = "./Data/*.pkl"
+        data_output_pattern = "./Data/*.h5"  # %self.output_data_level
         dm_step = self.setExecutable(
             "cta-prod-managedata",
-            arguments="'%s' '%s' %s '%s' %s %s '%s' Data"
+            arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Data"
             % (
                 meta_data_json,
+                meta_data_field_json,
                 file_meta_data_json,
                 self.base_path,
                 data_output_pattern,
                 self.package,
                 self.program_category,
                 self.catalogs,
             ),
             logFile="DataManagement_Log.txt",
         )
-        dm_step["Value"]["name"] = f"Step{i_step}_DataManagement"
+        dm_step["Value"]["name"] = "Step%s_DataManagement" % i_step
         dm_step["Value"][
             "descr_short"
         ] = "Save data files to SE and register them in DFC"
         i_step += 1
 
+        # step 5 register Log
+        log_file_pattern = "./Data/*.log_and_prov.tgz"
+        file_meta_data = {}
+        file_meta_data_json = json.dumps(file_meta_data)
+        log_step = self.setExecutable(
+            "cta-prod-managedata",
+            arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Log"
+            % (
+                meta_data_json,
+                meta_data_field_json,
+                file_meta_data_json,
+                self.base_path,
+                log_file_pattern,
+                self.package,
+                self.program_category,
+                self.catalogs,
+            ),
+            logFile="LogManagement_Log.txt",
+        )
+        log_step["Value"]["name"] = "Step%s_LogManagement" % i_step
+        log_step["Value"]["descr_short"] = "Save log to SE and register them in DFC"
+        i_step += 1
+
         # step 6 failover step
         failover_step = self.setExecutable(
             "/bin/ls -l", modulesList=["Script", "FailoverRequest"]
         )
-        failover_step["Value"]["name"] = f"Step{i_step}_Failover"
+        failover_step["Value"]["name"] = "Step%s_Failover" % i_step
         failover_step["Value"]["descr_short"] = "Tag files as unused if job failed"
         i_step += 1
 
         # Step 7 - debug only
         if debug:
             ls_step = self.setExecutable("/bin/ls -Ralhtr", logFile="LS_End_Log.txt")
-            ls_step["Value"]["name"] = f"Step{i_step}_LSHOME_End"
+            ls_step["Value"]["name"] = "Step%s_LSHOME_End" % i_step
             ls_step["Value"]["descr_short"] = "list files in Home directory"
             i_step += 1
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/EvnDisp4SSTJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/EvnDisp4SSTJob.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/EvnDispProd5Job.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/EvnDispProd5Job.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/EvnDispProd5SingJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/EvnDispProd5SingJob.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/EvnDispSingJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/EvnDispSingJob.py`

 * *Files 7% similar despite different names*

```diff
@@ -109,47 +109,63 @@
         ev_step["Value"]["descr_short"] = "Run EvnDisplay"
         i_step += 1
 
         # step 4 set meta data and register Data
         meta_data_json = json.dumps(self.output_metadata)
         file_meta_data_json = json.dumps(self.output_file_metadata)
 
+        meta_data_field = {
+            "array_layout": "VARCHAR(128)",
+            "site": "VARCHAR(128)",
+            "particle": "VARCHAR(128)",
+            "phiP": "float",
+            "thetaP": "float",
+            "sct": "VARCHAR(128)",
+            self.program_category + "_prog": "VARCHAR(128)",
+            self.program_category + "_prog_version": "VARCHAR(128)",
+            "data_level": "int",
+            "configuration_id": "int",
+            "merged": "int",
+        }
+        meta_data_field_json = json.dumps(meta_data_field)
+
         # register Data
         # to be used with job.version = 'eventdisplay-cta-dl1-prod5.v04'
         # data_output_pattern = './Data/*.simtel.DL1.root'
         # to be used with job.version = 'eventdisplay-cta-dl1-prod5.v06'
         data_output_pattern = "./Data/*.simtel.DL1.tar.gz"
         dm_step = self.setExecutable(
             "cta-prod-managedata",
-            arguments="'%s' '%s' %s '%s' %s %s '%s' Data"
+            arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Data"
             % (
                 meta_data_json,
+                meta_data_field_json,
                 file_meta_data_json,
                 self.base_path,
                 data_output_pattern,
                 self.package,
                 self.program_category,
                 self.catalogs,
             ),
             logFile="DataManagement_Log.txt",
         )
-        dm_step["Value"]["name"] = f"Step{i_step}_DataManagement"
+        dm_step["Value"]["name"] = "Step%s_DataManagement" % i_step
         dm_step["Value"][
             "descr_short"
         ] = "Save data files to SE and register them in DFC"
         i_step += 1
 
         # step 5 failover step
         if not debug:
             failover_step = self.setExecutable(
                 "/bin/ls -l", modulesList=["Script", "FailoverRequest"]
             )
-            failover_step["Value"]["name"] = f"Step{i_step}_Failover"
+            failover_step["Value"]["name"] = "Step%s_Failover" % i_step
             failover_step["Value"]["descr_short"] = "Tag files as unused if job failed"
             i_step += 1
 
         # step 6 - debug only
         if debug:
             ls_step = self.setExecutable("/bin/ls -Ralhtr", logFile="LS_End_Log.txt")
-            ls_step["Value"]["name"] = f"Step{i_step}_LSHOME_End"
+            ls_step["Value"]["name"] = "Step%s_LSHOME_End" % i_step
             ls_step["Value"]["descr_short"] = "list files in Home directory"
             i_step += 1
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/MCPipeNSBJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/MCPipeNSBJob.py`

 * *Files 6% similar despite different names*

```diff
@@ -24,15 +24,15 @@
 
     def __init__(self, cpu_time=259200):
         """Constructor takes almosst everything from base class
 
         Keyword arguments:
         cpuTime -- max cpu time allowed for the job
         """
-        super().__init__()
+        Job.__init__(self)
         self.setCPUTime(cpu_time)
         self.setName("MC_Generation")
         self.setType("MCSimulation")
         self.package = "corsika_simtelarray"
         self.version = "2022-08-03"
         self.compiler = "gcc83_matchcpu"
         self.program_category = "tel_sim"
@@ -54,44 +54,44 @@
     def set_site(self, site):
         """Set the site to simulate
 
         Parameters:
         site -- a string for the site name (LaPalma)
         """
         if site in ["Paranal", "LaPalma"]:
-            DIRAC.gLogger.info(f"Set Corsika site to: {site}")
+            DIRAC.gLogger.info("Set Corsika site to: %s" % site)
             self.site = site
         else:
-            DIRAC.gLogger.error(f"Site is unknown: {site}")
+            DIRAC.gLogger.error("Site is unknown: %s" % site)
             DIRAC.exit(-1)
 
     def set_particle(self, particle):
         """Set the corsika primary particle
 
         Parameters:
         particle -- a string for the particle type/name
         """
         if particle in ["gamma", "gamma-diffuse", "electron", "proton", "helium"]:
-            DIRAC.gLogger.info(f"Set Corsika particle to: {particle}")
+            DIRAC.gLogger.info("Set Corsika particle to: %s" % particle)
             self.particle = particle
         else:
-            DIRAC.gLogger.error(f"Corsika does not know particle type: {particle}")
+            DIRAC.gLogger.error("Corsika does not know particle type: %s" % particle)
             DIRAC.exit(-1)
 
     def set_pointing_dir(self, pointing):
         """Set the pointing direction, North or South
 
         Parameters:
         pointing -- a string for the pointing direction
         """
         if pointing in ["North", "South", "East", "West"]:
-            DIRAC.gLogger.info(f"Set Pointing dir to: {pointing}")
+            DIRAC.gLogger.info("Set Pointing dir to: %s" % pointing)
             self.pointing_dir = pointing
         else:
-            DIRAC.gLogger.error(f"Unknown pointing direction: {pointing}")
+            DIRAC.gLogger.error("Unknown pointing direction: %s" % pointing)
             DIRAC.exit(-1)
 
     def set_moon(self, moon=["dark", "half", "full"]):
         """Set to simulate with various moon conditions
 
         Parameters:
         moon -- a list of moon conditions for simulation
@@ -107,29 +107,23 @@
 
         elif moon == ["dark", "half", "full"]:
             DIRAC.gLogger.info("Set simulations with full-moon conditions")
             self.moon = "--with-full-moon"
             self.output_file_metadata["nsb"] = [1, 5, 19]
         else:
             DIRAC.gLogger.error(
-                "Unknown moon option: %s. Options for simulation step are: \n [dark] \n [dark, half] \n [dark, half, "
-                "full] " % str(moon).replace("'", "")
+                "Unknown moon option: %s. Options for simulation step are: \n dark \n dark, half \n dark, half, full"
+                % moon
             )
             DIRAC.exit(-1)
 
     def set_div_ang(self, div_ang=None):
-        div_default = [
-            "0.0022",
-            "0.0043",
-            "0.008",
-            "0.01135",
-            "0.01453",
-        ]  # Default divergent angles
+        div_default = ["0.0022", "0.0043", "0.008", "0.01135", "0.01453"] # Default divergent angles
         if div_ang is not None:
-            if str(div_ang).replace(", ", ",").split(sep=",") != div_default:
+            if div_ang.replace(", ", ",").split(sep=",") != div_default:
                 DIRAC.gLogger.error(
                     "Unknown div_ang option: %s. Option for simulation step is: %s"
                     % (div_ang, ", ".join(str(x) for x in div_default))
                 )
                 DIRAC.exit(-1)
             else:
                 self.div_ang = div_default
@@ -212,15 +206,15 @@
             logFile="SetupSoftware_Log.txt",
         )
         sw_step["Value"]["name"] = "Step%i_SetupSoftware" % i_step
         sw_step["Value"]["descr_short"] = "Setup software"
         i_step += 1
 
         # step 3 - run corsika+sim_telarray
-        prod_exe = "./dirac_prod_run"
+        prod_exe = "./dirac_prod6_run"
         if self.div_ang:
             prod_args = (
                 "--start_run %s --run %s --sequential --divergent %s %s %s %s %s %s %s"
                 % (
                     self.start_run_number,
                     self.run_number,
                     self.moon,
@@ -230,15 +224,15 @@
                     self.particle,
                     self.pointing_dir,
                     self.zenith_angle,
                 )
             )
 
         else:
-            prod_args = "--start_run {} --run {} {} {} {} {} {} {} {}".format(
+            prod_args = "--start_run %s --run %s %s %s %s %s %s %s %s" % (
                 self.start_run_number,
                 self.run_number,
                 self.moon,
                 self.sct,
                 self.magic,
                 self.site,
                 self.particle,
@@ -261,17 +255,33 @@
                 "descr_short"
             ] = "list files in working directory and sub-directory"
             i_step += 1
 
         # step 5 - data management
         md_json = json.dumps(self.output_metadata)
 
+        meta_data_field = {
+            "array_layout": "VARCHAR(128)",
+            "site": "VARCHAR(128)",
+            "particle": "VARCHAR(128)",
+            "phiP": "float",
+            "thetaP": "float",
+            "sct": "VARCHAR(128)",
+            self.program_category + "_prog": "VARCHAR(128)",
+            self.program_category + "_prog_version": "VARCHAR(128)",
+            "data_level": "int",
+            "configuration_id": "int",
+            "merged": "int",
+        }
+        md_field_json = json.dumps(meta_data_field)
+
         keys = self.output_file_metadata.keys()
 
         for element in itertools.product(*self.output_file_metadata.values()):
+
             i_substep = 1
             combination = dict(zip(keys, element))
 
             # build file meta data
             file_meta_data = {
                 "runNumber": self.run_number,
             }
@@ -284,78 +294,80 @@
                 moon_str = "dark"
             if combination["nsb"] == 5:
                 moon_str = "moon"
             if combination["nsb"] == 19:
                 moon_str = "fullmoon"
 
             if combination.get("div_ang"):
-                div = f"div{combination['div_ang']}"
+                div = "div{}".format(combination["div_ang"])
                 div_str = div + "_"
             else:
                 div = ""
                 div_str = ""
 
-            data_output_pattern = f"Data/*-{div}*-{moon_str}*.simtel.zst"
+            data_output_pattern = "Data/*-{}*-{}*.simtel.zst".format(div, moon_str)
 
             # substep 1 - verify the number of events in the simtel file
             mgv_step = self.setExecutable(
                 "dirac_simtel_check",
-                arguments=f"'{data_output_pattern}'",
-                logFile=f"Verify_n_showers_{moon_str}_{div_str}Log.txt",
+                arguments="'%s'" % (data_output_pattern),
+                logFile="Verify_n_showers_{}_{}Log.txt".format(moon_str, div_str),
             )
-            mgv_step["Value"]["name"] = f"Step{i_step}.{i_substep}_VerifyNShowers"
+            mgv_step["Value"]["name"] = "Step%s.%s_VerifyNShowers" % (i_step, i_substep)
             mgv_step["Value"]["descr_short"] = "Verify number of showers"
 
             i_substep += 1
 
             # substep 2 - upload data file on SE and register in catalog
             dm_step = self.setExecutable(
                 "cta-prod-managedata",
-                arguments="'%s' '%s' %s '%s' %s %s '%s' Data"
+                arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Data"
                 % (
                     md_json,
+                    md_field_json,
                     file_md_json,
                     self.base_path,
                     data_output_pattern,
                     self.package,
                     self.program_category,
                     self.catalogs,
                 ),
-                logFile=f"DataManagement_{moon_str}_{div_str}Log.txt",
+                logFile="DataManagement_{}_{}Log.txt".format(moon_str, div_str),
             )
-            dm_step["Value"]["name"] = f"Step{i_step}.{i_substep}_DataManagement"
+            dm_step["Value"]["name"] = "Step%s.%s_DataManagement" % (i_step, i_substep)
             dm_step["Value"][
                 "descr_short"
             ] = "Save data files to SE and register them in DFC"
             i_step += 1
 
             # substep 3 - upload log and histo file on SE and register in catalog
             file_meta_data = {}
             file_md_json = json.dumps(file_meta_data)
-            log_file_pattern = f"Data/*-{div}*-{moon_str}*.log_hist.tar"
+            log_file_pattern = "Data/*-{}*-{}*.log_hist.tar".format(div, moon_str)
             log_step = self.setExecutable(
                 "cta-prod-managedata",
-                arguments="'%s' '%s' %s '%s' %s %s '%s' Log"
+                arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Log"
                 % (
                     md_json,
+                    md_field_json,
                     file_md_json,
                     self.base_path,
                     log_file_pattern,
                     self.package,
                     self.program_category,
                     self.catalogs,
                 ),
-                logFile=f"LogManagement_{moon_str}_{div_str}Log.txt",
+                logFile="LogManagement_{}_{}Log.txt".format(moon_str, div_str),
             )
-            log_step["Value"]["name"] = f"Step{i_step}.{i_substep}_LogManagement"
+            log_step["Value"]["name"] = "Step%s.%s_LogManagement" % (i_step, i_substep)
             log_step["Value"]["descr_short"] = "Save log to SE and register them in DFC"
             i_step += 1
 
         # Last step - debug only
         if debug:
             ls_step = self.setExecutable("/bin/ls -Ralhtr", logFile="LS_End_Log.txt")
-            ls_step["Value"]["name"] = f"Step{i_step}_LSHOME_End"
+            ls_step["Value"]["name"] = "Step%s_LSHOME_End" % i_step
             ls_step["Value"]["descr_short"] = "list files in Home directory"
             i_step += 1
 
         # Number of showers is passed via an environment variable
-        self.setExecutionEnv({"NSHOW": f"{self.n_shower}"})
+        self.setExecutionEnv({"NSHOW": "%s" % self.n_shower})
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod5MCPipeNSBJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod5MCPipeNSBJob.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod5bMCPipeAlphaDivergentJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod5bMCPipeAlphaDivergentJob.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod5bMCPipeAlphaSSTsFullMoonNSBJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod5bMCPipeAlphaSSTsFullMoonNSBJob.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod5bMCPipeAlphaSSTsNSBJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod5bMCPipeAlphaSSTsNSBJob.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod5bMCPipeNSBJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod5bMCPipeNSBJob.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod6MCPipeDivergentJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod6MCPipeDivergentJob.py`

 * *Files 20% similar despite different names*

```diff
@@ -6,248 +6,183 @@
 """
 
 __RCSID__ = "$Id$"
 
 # generic imports
 import json
 import collections
-
 # DIRAC imports
-from DIRAC import gLogger
 from CTADIRAC.Interfaces.API.Prod6MCPipeNSBJob import Prod6MCPipeNSBJob
 
 
 class Prod6MCPipeDivergentJob(Prod6MCPipeNSBJob):
-    """Job extension class for Prod6 MC Divergent simulations"""
+  """ Job extension class for Prod6 MC Divergent simulations
+
+  """
 
-    def __init__(self, cpu_time=259200):
-        """Constructor takes almosst everything from base class
+  def __init__(self, cpu_time=259200):
+    """ Constructor takes almosst everything from base class
 
-        Keyword arguments:
-        cpuTime -- max cpu time allowed for the job
-        """
-        Prod6MCPipeNSBJob.__init__(self, cpu_time)
-        self.catalogs = json.dumps(["DIRACFileCatalog"])
-        self.metadata = collections.OrderedDict()
-
-    def set_half_moon(self, half_moon=False):
-        """Set if to simulate with half-moon conditions
-
-        Parameters:
-        half_moon -- a boolean for simulating with full moon conditions
-        """
-        if half_moon is True:
-            gLogger.info("Set simulations with half-moon conditions")
-            self.half_moon = "--with-half-moon"
-        else:
-            self.half_moon = ""  # We alawys at least run with half moon
+    Keyword arguments:
+    cpuTime -- max cpu time allowed for the job
+    """
+    Prod6MCPipeNSBJob.__init__(self, cpu_time)
+    self.catalogs = json.dumps(['DIRACFileCatalog'])
+    self.metadata = collections.OrderedDict()
 
-    def setupWorkflow(self, debug=False):
-        """Override the base class job workflow to adapt to divergent simulations
+  def setupWorkflow(self, debug=False):
+    """ Override the base class job workflow to adapt to divergent simulations
         All parameters shall have been defined before that method is called.
-        """
-        # step 1 - debug only
-        i_step = 1
-        if debug:
-            ls_step = self.setExecutable("/bin/ls -alhtr", logFile="LS_Init_Log.txt")
-            ls_step["Value"]["name"] = "Step%i_LS_Init" % i_step
-            ls_step["Value"]["descr_short"] = "list files in working directory"
-
-            env_step = self.setExecutable("/bin/env", logFile="Env_Log.txt")
-            env_step["Value"]["name"] = "Step%i_Env" % i_step
-            env_step["Value"]["descr_short"] = "Dump environment"
-            i_step += 1
-
-        # step 2 : use new CVMFS repo
-        sw_step = self.setExecutable(
-            "cta-prod-setup-software",
-            arguments="-p %s -v %s -a simulations -g %s"
-            % (self.package, self.version, self.compiler),
-            logFile="SetupSoftware_Log.txt",
-        )
-        sw_step["Value"]["name"] = "Step%i_SetupSoftware" % i_step
-        sw_step["Value"]["descr_short"] = "Setup software"
-        i_step += 1
-        # step 3 run corsika+sim_telarray
-        prod_exe = "./dirac_prod6_run"
-        prod_args = (
-            "--start_run %s --run %s --sequential --divergent %s %s %s %s %s %s %s"
-            % (
-                self.start_run_number,
-                self.run_number,
-                self.half_moon,
-                self.with_sct,
-                self.with_magic,
-                self.cta_site,
-                self.particle,
-                self.pointing_dir,
-                self.zenith_angle,
-            )
-        )
-
-        cs_step = self.setExecutable(
-            prod_exe, arguments=prod_args, logFile="CorsikaSimtel_Log.txt"
-        )
-        cs_step["Value"]["name"] = "Step%i_CorsikaSimtel" % i_step
-        cs_step["Value"]["descr_short"] = "Run Corsika piped into simtel"
-        i_step += 1
-
-        # step 4 - debug only
-        if debug:
-            ls_step = self.setExecutable("/bin/ls -Ralhtr", logFile="LS_End_Log.txt")
-            ls_step["Value"]["name"] = "Step%i_LS_End" % i_step
-            ls_step["Value"][
-                "descr_short"
-            ] = "list files in working directory and sub-directory"
-            i_step += 1
-
-        # step 5  verify the number of events in the simtel file and define meta data, upload file on SE and register in catalogs
-        self.set_meta_data()
-        md_json = json.dumps(self.metadata)
-
-        i_substep = 0
-        for div_ang in ["0.0022", "0.0043", "0.008", "0.01135", "0.01453"]:
-            data_output_pattern = f"Data/*-div{div_ang}*-dark*.simtel.zst"
-
-            # verify the number of events in the simtel file
-            mgv_step = self.setExecutable(
-                "dirac_simtel_check",
-                arguments=f"'{data_output_pattern}'",
-                logFile=f"Verify_n_showers_div{div_ang}_Log.txt",
-            )
-            mgv_step["Value"]["name"] = f"Step{i_step}.{i_substep}_VerifyNShowers"
-            mgv_step["Value"]["descr_short"] = "Verify number of showers"
-
-            i_substep += 1
-
-            # define meta data, upload file on SE and register in catalogs
-
-            # Upload and register data
-            file_meta_data = {
-                "runNumber": self.run_number,
-                "nsb": 1,
-                "div_ang": div_ang,
-            }  # adding a new meta data field
-            file_md_json = json.dumps(file_meta_data)
-
-            dm_step = self.setExecutable(
-                "cta-prod-managedata",
-                arguments="'%s' '%s' %s '%s' %s %s '%s' Data"
-                % (
-                    md_json,
-                    file_md_json,
-                    self.base_path,
-                    data_output_pattern,
-                    self.package,
-                    self.program_category,
-                    self.catalogs,
-                ),
-                logFile=f"DataManagement_div{div_ang}_Log.txt",
-            )
-            dm_step["Value"]["name"] = f"Step{i_step}.{i_substep}_DataManagement"
-            dm_step["Value"][
-                "descr_short"
-            ] = "Save data files to SE and register them in DFC"
-
-            i_substep += 1
-
-            # Upload and register log_and_hist file
-            file_meta_data = {}
-            file_md_json = json.dumps(file_meta_data)
-            log_file_pattern = f"Data/*-div{div_ang}*-dark*.log_hist.tar"
-            log_step = self.setExecutable(
-                "cta-prod-managedata",
-                arguments="'%s' '%s' %s '%s' %s %s '%s' Log"
-                % (
-                    md_json,
-                    file_md_json,
-                    self.base_path,
-                    log_file_pattern,
-                    self.package,
-                    self.program_category,
-                    self.catalogs,
-                ),
-                logFile=f"LogManagement_div{div_ang}_Log.txt",
-            )
-            log_step["Value"]["name"] = f"Step{i_step}.{i_substep}_LogManagement"
-            log_step["Value"]["descr_short"] = "Save log to SE and register them in DFC"
-
-            i_substep += 1
-
-            # Now switching to half moon NSB
-            if self.half_moon:
-                # Upload and register data - NSB=5 half moon
-                file_meta_data = {
-                    "runNumber": self.run_number,
-                    "nsb": 5,
-                    "div_ang": div_ang,
-                }
-                file_md_json = json.dumps(file_meta_data)
-                data_output_pattern = f"Data/*-div{div_ang}*-moon*.simtel.zst"
-                # verify the number of events in the simtel file
-                mgv_step = self.setExecutable(
-                    "dirac_simtel_check",
-                    arguments=f"'{data_output_pattern}'",
-                    logFile=f"Verify_n_showers_moon_div{div_ang}_Log.txt",
-                )
-                mgv_step["Value"]["name"] = f"Step{i_step}.{i_substep}_VerifyNShowers"
-                mgv_step["Value"]["descr_short"] = "Verify number of showers"
-
-                i_substep += 1
-
-                dm_step = self.setExecutable(
-                    "cta-prod-managedata",
-                    arguments="'%s' '%s' %s '%s' %s %s '%s' Data"
-                    % (
-                        md_json,
-                        file_md_json,
-                        self.base_path,
-                        data_output_pattern,
-                        self.package,
-                        self.program_category,
-                        self.catalogs,
-                    ),
-                    logFile=f"DataManagement_moon_div{div_ang}_Log.txt",
-                )
-                dm_step["Value"]["name"] = f"Step{i_step}.{i_substep}_DataManagement"
-                dm_step["Value"][
-                    "descr_short"
-                ] = "Save data files to SE and register them in DFC"
-
-                i_substep += 1
-
-                # Upload and register log file - NSB=5
-                file_meta_data = {}
-                file_md_json = json.dumps(file_meta_data)
-                log_file_pattern = f"Data/*-div{div_ang}*-moon*.log_hist.tar"
-                log_step = self.setExecutable(
-                    "cta-prod-managedata",
-                    arguments="'%s' '%s' %s '%s' %s %s '%s' Log"
-                    % (
-                        md_json,
-                        file_md_json,
-                        self.base_path,
-                        log_file_pattern,
-                        self.package,
-                        self.program_category,
-                        self.catalogs,
-                    ),
-                    logFile=f"LogManagement_moon_div{div_ang}_Log.txt",
-                )
-                log_step["Value"]["name"] = f"Step{i_step}.{i_substep}_LogManagement"
-                log_step["Value"][
-                    "descr_short"
-                ] = "Save log to SE and register them in DFC"
-
-                i_substep += 1
-
-        i_step += 1
-
-        # Step 6 - debug only
-        if debug:
-            ls_step = self.setExecutable("/bin/ls -Ralhtr", logFile="LS_End_Log.txt")
-            ls_step["Value"]["name"] = f"Step{i_step}_LSHOME_End"
-            ls_step["Value"]["descr_short"] = "list files in Home directory"
-            # i_step += 1
+    """
+    # step 1 - debug only
+    i_step = 1
+    if debug:
+      ls_step = self.setExecutable('/bin/ls -alhtr', logFile='LS_Init_Log.txt')
+      ls_step['Value']['name'] = 'Step%i_LS_Init' % i_step
+      ls_step['Value']['descr_short'] = 'list files in working directory'
+
+      env_step = self.setExecutable('/bin/env', logFile='Env_Log.txt')
+      env_step['Value']['name'] = 'Step%i_Env' % i_step
+      env_step['Value']['descr_short'] = 'Dump environment'
+      i_step += 1
+
+    # step 2 : use new CVMFS repo
+    sw_step = self.setExecutable('cta-prod-setup-software',
+                                 arguments='-p %s -v %s -a simulations -g %s' %
+                                 (self.package, self.version, self.compiler),
+                                 logFile='SetupSoftware_Log.txt')
+    sw_step['Value']['name'] = 'Step%i_SetupSoftware' % i_step
+    sw_step['Value']['descr_short'] = 'Setup software'
+    i_step += 1
+
+    # step 3 run corsika+sim_telarray
+    prod_exe = './dirac_prod6_run'
+    prod_args = '--start_run %s --run %s --sequential --divergent %s %s %s %s %s %s %s' % \
+                (self.start_run_number, self.run_number,
+                 self.full_moon, self.with_sct, self.with_magic,
+                 self.cta_site, self.particle, self.pointing_dir,
+                 self.zenith_angle)
+
+    cs_step = self.setExecutable(prod_exe, arguments=prod_args,
+                                 logFile='CorsikaSimtel_Log.txt')
+    cs_step['Value']['name'] = 'Step%i_CorsikaSimtel' % i_step
+    cs_step['Value']['descr_short'] = 'Run Corsika piped into simtel'
+    i_step += 1
+
+    # step 4 - debug only
+    if debug:
+      ls_step = self.setExecutable('/bin/ls -Ralhtr', logFile='LS_End_Log.txt')
+      ls_step['Value']['name'] = 'Step%i_LS_End' % i_step
+      ls_step['Value']['descr_short'] = 'list files in working directory and sub-directory'
+      i_step += 1
+
+    # step 5  verify the number of events in the simtel file and define meta data, upload file on SE and register in catalogs
+    self.set_meta_data()
+    md_json = json.dumps(self.metadata)
+    meta_data_field = {'array_layout': 'VARCHAR(128)', 'site': 'VARCHAR(128)',
+                       'particle': 'VARCHAR(128)',
+                       'phiP': 'float', 'thetaP': 'float',
+                       self.program_category + '_prog': 'VARCHAR(128)',
+                       self.program_category + '_prog_version': 'VARCHAR(128)',
+                       'data_level': 'int', 'configuration_id': 'int', 'merged': 'int'}
+    md_field_json = json.dumps(meta_data_field)
+
+    i_substep = 0
+    for div_ang in ['0.0022', '0.0043', '0.008', '0.01135', '0.01453']:
+
+      data_output_pattern = 'Data/*-div%s*-dark*.simtel.zst' % (div_ang)
+
+      #verify the number of events in the simtel file
+      mgv_step = self.setExecutable('dirac_simtel_check',
+                                    arguments="'%s'" %
+                                    (data_output_pattern),
+                                    logFile='Verify_n_showers_div%s_Log.txt' % (div_ang))
+      mgv_step['Value']['name'] = 'Step%s.%s_VerifyNShowers' % (i_step, i_substep)
+      mgv_step['Value']['descr_short'] = 'Verify number of showers'
+
+      i_substep += 1
+
+      #define meta data, upload file on SE and register in catalogs
+
+      # Upload and register data
+      file_meta_data = {'runNumber': self.run_number, 'nsb': 1, 'div_ang': div_ang}  # adding a new meta data field
+      file_md_json = json.dumps(file_meta_data)
+
+      dm_step = self.setExecutable('cta-prod-managedata',
+                                   arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Data" %
+                                   (md_json, md_field_json, file_md_json,
+                                    self.base_path, data_output_pattern, self.package,
+                                    self.program_category, self.catalogs),
+                                   logFile="DataManagement_div%s_Log.txt" % (div_ang))
+      dm_step['Value']['name'] = 'Step%s.%s_DataManagement' % (i_step, i_substep)
+      dm_step['Value']['descr_short'] = 'Save data files to SE and register them in DFC'
+
+      i_substep += 1
+
+      # Upload and register log_and_hist file
+      file_meta_data = {}
+      file_md_json = json.dumps(file_meta_data)
+      log_file_pattern = 'Data/*-div%s*-dark*.log_hist.tar' % (div_ang)
+      log_step = self.setExecutable('cta-prod-managedata',
+                                    arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Log" %
+                                    (md_json, md_field_json, file_md_json,
+                                     self.base_path, log_file_pattern, self.package,
+                                     self.program_category, self.catalogs),
+                                    logFile="LogManagement_div%s_Log.txt" % (div_ang))
+      log_step['Value']['name'] = 'Step%s.%s_LogManagement' % (i_step, i_substep)
+      log_step['Value']['descr_short'] = 'Save log to SE and register them in DFC'
+
+      i_substep += 1
+
+      # Now switching to half moon NSB
+      # Upload and register data - NSB=5 half moon
+      file_meta_data = {'runNumber': self.run_number, 'nsb': 5, 'div_ang': div_ang}
+      file_md_json = json.dumps(file_meta_data)
+      data_output_pattern = 'Data/*-div%s*-moon*.simtel.zst' % (div_ang)
+
+      #verify the number of events in the simtel file
+      mgv_step = self.setExecutable('dirac_simtel_check',
+                                    arguments="'%s'" %
+                                    (data_output_pattern),
+                                    logFile='Verify_n_showers_moon_div%s_Log.txt' % (div_ang))
+      mgv_step['Value']['name'] = 'Step%s.%s_VerifyNShowers' % (i_step, i_substep)
+      mgv_step['Value']['descr_short'] = 'Verify number of showers'
+
+      i_substep += 1
+
+      dm_step = self.setExecutable('cta-prod-managedata',
+                                   arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Data" %
+                                   (md_json, md_field_json, file_md_json,
+                                    self.base_path, data_output_pattern, self.package,
+                                    self.program_category, self.catalogs),
+                                   logFile="DataManagement_moon_div%s_Log.txt" % (div_ang))
+      dm_step['Value']['name'] = 'Step%s.%s_DataManagement' % (i_step, i_substep)
+      dm_step['Value']['descr_short'] = 'Save data files to SE and register them in DFC'
+
+      i_substep += 1
+
+      # Upload and register log file - NSB=5
+      file_meta_data = {}
+      file_md_json = json.dumps(file_meta_data)
+      log_file_pattern = 'Data/*-div%s*-moon*.log_hist.tar' % (div_ang)
+      log_step = self.setExecutable('cta-prod-managedata',
+                                    arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Log" %
+                                    (md_json, md_field_json, file_md_json,
+                                     self.base_path, log_file_pattern, self.package,
+                                     self.program_category, self.catalogs),
+                                    logFile="LogManagement_moon_div%s_Log.txt" % (div_ang))
+      log_step['Value']['name'] = 'Step%s.%s_LogManagement' % (i_step, i_substep)
+      log_step['Value']['descr_short'] = 'Save log to SE and register them in DFC'
+
+      i_substep += 1
+
+    i_step += 1
+
+    # Step 6 - debug only
+    if debug:
+      ls_step = self.setExecutable('/bin/ls -Ralhtr', logFile='LS_End_Log.txt')
+      ls_step['Value']['name'] = 'Step%s_LSHOME_End' % i_step
+      ls_step['Value']['descr_short'] = 'list files in Home directory'
+      #i_step += 1
 
-        # Number of showers is passed via an environment variable
-        self.setExecutionEnv({"NSHOW": f"{self.n_shower}"})
+    # Number of showers is passed via an environment variable
+    self.setExecutionEnv({'NSHOW': '%s' % self.n_shower})
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod6MCPipeMuonJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod6MCPipeMuonJob.py`

 * *Files 22% similar despite different names*

```diff
@@ -4,333 +4,282 @@
 
 __RCSID__ = "$Id$"
 
 # generic imports
 import json
 import collections
 import numpy as np
-
 # DIRAC imports
 import DIRAC
 from DIRAC.Interfaces.API.Job import Job
 from CTADIRAC.Core.Utilities.tool_box import DATA_LEVEL_METADATA_ID
 
 
 class Prod6MCPipeMuonJob(Job):
-    """Job extension class for Prod5 MC NSB simulations,
-    takes care of running corsika piped into simtel
-    2 output files are created for Dark and Moon NSB
+  """ Job extension class for Prod5 MC NSB simulations,
+  takes care of running corsika piped into simtel
+  2 output files are created for Dark and Moon NSB
+  """
+
+  def __init__(self, cpu_time=259200):
+    """ Constructor takes almosst everything from base class
+
+    Keyword arguments:
+    cpuTime -- max cpu time allowed for the job
+    """
+    Job.__init__(self)
+    self.setCPUTime(cpu_time)
+    self.setName('Prod6MC_Generation')
+    self.setType('MCSimulation')
+    self.package = 'corsika_simtelarray'
+    self.version = '2022-08-03-sc'
+    self.compiler = 'gcc83_matchcpu'
+    self.program_category = 'tel_sim'
+    self.prog_name = 'sim_telarray'
+    self.configuration_id = 15
+    self.output_data_level = DATA_LEVEL_METADATA_ID['R1']
+    self.base_path = '/vo.cta.in2p3.fr/MC/PROD6/'
+    self.catalogs = json.dumps(['DIRACFileCatalog', 'TSCatalog'])
+    self.metadata = collections.OrderedDict()
+
+  def set_site(self, site):
+    """ Set the site to simulate
+
+    Parameters:
+    site -- a string for the site name (LaPalma)
+    """
+    if site in ['Paranal', 'LaPalma']:
+      DIRAC.gLogger.info('Set Corsika site to: %s' % site)
+      self.cta_site = site
+    else:
+      DIRAC.gLogger.error('Site is unknown: %s' % site)
+      DIRAC.exit(-1)
+
+  def set_telescope(self, telescope):
+    """ Set the telescope to simulate
+
+    Parameters:
+    telescope -- a string for the telescope name
+    """
+    if telescope in ['LST', 'MST-FlashCam', 'MST-NectarCam', 'SST', 'SCT']:
+      DIRAC.gLogger.info('Set telescope to: %s' % telescope)
+      self.telescope = telescope
+    else:
+      DIRAC.gLogger.error('Telescope %s is unknown, aborting' % telescope)
+      DIRAC.exit(-1)
+
+  def set_particle(self, particle):
+    """ Set the corsika primary particle
+
+    Parameters:
+    particle -- a string for the particle type/name
+    """
+    if particle in ['muon']:
+      DIRAC.gLogger.info('Set Corsika particle to: %s' % particle)
+      self.particle = particle
+    else:
+      DIRAC.gLogger.error('This script can only perform muon simulations, not %s simulations' % particle)
+      DIRAC.exit(-1)
+
+  def set_pointing_dir(self, pointing):
+    """ Set the pointing direction, North or South
+
+    Parameters:
+    pointing -- a string for the pointing direction
     """
+    if pointing in ['North', 'South', 'East', 'West']:
+      DIRAC.gLogger.info('Set Pointing dir to: %s' % pointing)
+      self.pointing_dir = pointing
+    else:
+      DIRAC.gLogger.error('Unknown pointing direction: %s' % pointing)
+      DIRAC.exit(-1)
+
+  def set_half_moon(self, half_moon=False):
+    """ Set if to simulate with full-moon conditions
 
-    def __init__(self, cpu_time=259200):
-        """Constructor takes almosst everything from base class
+    Parameters:
+    half_moon -- a boolean for simulating with half-moon conditions
+    """
+    if half_moon is True:
+      DIRAC.gLogger.info('Set simulations with half-moon conditions')
+      self.half_moon = '--with-half-moon'
+    else:
+      self.half_moon = ''
 
-        Keyword arguments:
-        cpuTime -- max cpu time allowed for the job
-        """
-        Job.__init__(self)
-        self.setCPUTime(cpu_time)
-        self.setName("Prod6MC_Generation")
-        self.setType("MCSimulation")
-        self.package = "corsika_simtelarray"
-        self.version = "2022-08-03-sc"
-        self.compiler = "gcc83_matchcpu"
-        self.program_category = "tel_sim"
-        self.prog_name = "sim_telarray"
-        self.configuration_id = 15
-        self.output_data_level = DATA_LEVEL_METADATA_ID["R1"]
-        self.base_path = "/vo.cta.in2p3.fr/MC/PROD6/"
-        self.catalogs = json.dumps(["DIRACFileCatalog", "TSCatalog"])
-        self.metadata = collections.OrderedDict()
-
-    def set_site(self, site):
-        """Set the site to simulate
-
-        Parameters:
-        site -- a string for the site name (LaPalma)
-        """
-        if site in ["Paranal", "LaPalma"]:
-            DIRAC.gLogger.info(f"Set Corsika site to: {site}")
-            self.cta_site = site
-        else:
-            DIRAC.gLogger.error(f"Site is unknown: {site}")
-            DIRAC.exit(-1)
-
-    def set_telescope(self, telescope):
-        """Set the telescope to simulate
-
-        Parameters:
-        telescope -- a string for the telescope name
-        """
-        if telescope in ["LST", "MST-FlashCam", "MST-NectarCam", "SST", "SCT"]:
-            DIRAC.gLogger.info(f"Set telescope to: {telescope}")
-            self.telescope = telescope
-        else:
-            DIRAC.gLogger.error(f"Telescope {telescope} is unknown, aborting")
-            DIRAC.exit(-1)
-
-    def set_particle(self, particle):
-        """Set the corsika primary particle
-
-        Parameters:
-        particle -- a string for the particle type/name
-        """
-        if particle in ["muon"]:
-            DIRAC.gLogger.info(f"Set Corsika particle to: {particle}")
-            self.particle = particle
-        else:
-            DIRAC.gLogger.error(
-                "This script can only perform muon simulations, not %s simulations"
-                % particle
-            )
-            DIRAC.exit(-1)
-
-    def set_pointing_dir(self, pointing):
-        """Set the pointing direction, North or South
-
-        Parameters:
-        pointing -- a string for the pointing direction
-        """
-        if pointing in ["North", "South", "East", "West"]:
-            DIRAC.gLogger.info(f"Set Pointing dir to: {pointing}")
-            self.pointing_dir = pointing
-        else:
-            DIRAC.gLogger.error(f"Unknown pointing direction: {pointing}")
-            DIRAC.exit(-1)
-
-    def set_half_moon(self, half_moon=False):
-        """Set if to simulate with full-moon conditions
-
-        Parameters:
-        half_moon -- a boolean for simulating with half-moon conditions
-        """
-        if half_moon is True:
-            DIRAC.gLogger.info("Set simulations with half-moon conditions")
-            self.half_moon = "--with-half-moon"
-        else:
-            self.half_moon = ""
-
-    def set_degraded_mirror_reflectivity(self, degraded_mirror_reflectivity=False):
-        """Set the values of degraded mirror reflectivity to simulate
-
-        Parameters:
-        degraded_mirror_reflectivity -- a boolean to set if to simulate a degraded mirror reflectivity (0.3 to 1.0 in steps of 0.05)
-        """
-        if degraded_mirror_reflectivity:
-            DIRAC.gLogger.info("Set simulations with degraded mirror reflectivities")
-            self.degraded_values = np.arange(0.3, 1.05, 0.05)
-            self.degraded_mirror = "--degraded-mirror-ref"
-        else:
-            DIRAC.gLogger.info("Set simulations without degraded mirror reflectivities")
-            self.degraded_values = [1]  # No degraded mirror reflectivity
-            self.degraded_mirror = ""
-
-    def set_meta_data(self):
-        """define the common meta data of the application"""
-        # The order of the metadata dictionary is important,
-        # since it's used to build the directory structure
-        self.metadata["array_layout"] = "Single-telescope"
-        self.metadata["site"] = self.cta_site
-        self.metadata["particle"] = self.particle
-        # for air shower simulation means North=0 and South=180
-        # but here piped into tel_sim so North=180 and South=0
-        if self.pointing_dir == "North":
-            self.metadata["phiP"] = 180
-        if self.pointing_dir == "South":
-            self.metadata["phiP"] = 0
-        self.metadata["thetaP"] = float(self.zenith_angle)
-        self.metadata[self.program_category + "_prog"] = self.prog_name
-        self.metadata[self.program_category + "_prog_version"] = "".join(
-            self.version.rsplit("-sc", 1)
-        )
-        self.metadata["data_level"] = self.output_data_level
-        self.metadata["configuration_id"] = self.configuration_id
-        if self.telescope == "SCT":
-            self.metadata["sct"] = "True"
-        else:
-            self.metadata["sct"] = "False"
+  def set_degraded_mirror_reflectivity(self, degraded_mirror_reflectivity=False):
+    """ Set the values of degraded mirror reflectivity to simulate
 
-    def setupWorkflow(self, debug=False):
-        """Override the base class job workflow to adapt to NSB test simulations
+    Parameters:
+    degraded_mirror_reflectivity -- a boolean to set if to simulate a degraded mirror reflectivity (0.3 to 1.0 in steps of 0.05)
+    """
+    if degraded_mirror_reflectivity:
+      DIRAC.gLogger.info('Set simulations with degraded mirror reflectivities')
+      self.degraded_values = np.arange(0.3, 1.05, 0.05)
+      self.degraded_mirror = '--degraded-mirror-ref'
+    else:
+      DIRAC.gLogger.info('Set simulations without degraded mirror reflectivities')
+      self.degraded_values = [1]  # No degraded mirror reflectivity
+      self.degraded_mirror = ''
+
+  def set_meta_data(self):
+    """ define the common meta data of the application
+    """
+    # The order of the metadata dictionary is important,
+    # since it's used to build the directory structure
+    self.metadata['array_layout'] = 'Single-telescope'
+    self.metadata['site'] = self.cta_site
+    self.metadata['particle'] = self.particle
+    # for air shower simulation means North=0 and South=180
+    # but here piped into tel_sim so North=180 and South=0
+    if self.pointing_dir == 'North':
+      self.metadata['phiP'] = 180
+    if self.pointing_dir == 'South':
+      self.metadata['phiP'] = 0
+    self.metadata['thetaP'] = float(self.zenith_angle)
+    self.metadata[self.program_category + '_prog'] = self.prog_name
+    self.metadata[self.program_category + '_prog_version'] = ''.join(self.version.rsplit('-sc', 1))
+    self.metadata['data_level'] = self.output_data_level
+    self.metadata['configuration_id'] = self.configuration_id
+    if self.telescope == 'SCT':
+      self.metadata['sct'] = 'True'
+    else:
+      self.metadata['sct'] = 'False'
+
+  def setupWorkflow(self, debug=False):
+    """ Override the base class job workflow to adapt to NSB test simulations
         All parameters shall have been defined before that method is called.
-        """
-        # step 1 - debug only
-        i_step = 1
-        if debug:
-            ls_step = self.setExecutable("/bin/ls -alhtr", logFile="LS_Init_Log.txt")
-            ls_step["Value"]["name"] = "Step%i_LS_Init" % i_step
-            ls_step["Value"]["descr_short"] = "list files in working directory"
-            i_step += 1
-
-            env_step = self.setExecutable("/bin/env", logFile="Env_Log.txt")
-            env_step["Value"]["name"] = "Step%i_Env" % i_step
-            env_step["Value"]["descr_short"] = "Dump environment"
-            i_step += 1
-
-        # step 2 : use new CVMFS repo
-        sw_step = self.setExecutable(
-            "cta-prod-setup-software",
-            arguments="-p %s -v %s -a simulations -g %s -r /cvmfs/sw.cta-observatory.org/software"
-            % (self.package, self.version, self.compiler),
-            logFile="SetupSoftware_Log.txt",
-        )
-        sw_step["Value"]["name"] = "Step%i_SetupSoftware" % i_step
-        sw_step["Value"]["descr_short"] = "Setup software"
-        i_step += 1
-
-        # step 3 run corsika+sim_telarray
-        prod_exe = "./dirac_prod6_muon_run"
-        prod_args = "--start_run {} --run {} {} {} {} {} {} {} {}".format(
-            self.start_run_number,
-            self.run_number,
-            self.half_moon,
-            self.degraded_mirror,
-            self.telescope,
-            self.cta_site,
-            self.particle,
-            self.pointing_dir,
-            self.zenith_angle,
-        )
-
-        cs_step = self.setExecutable(
-            prod_exe, arguments=prod_args, logFile="CorsikaSimtel_Log.txt"
-        )
-        cs_step["Value"]["name"] = "Step%i_CorsikaSimtel" % i_step
-        cs_step["Value"]["descr_short"] = "Run Corsika piped into simtel"
-        i_step += 1
-
-        # step 4 - define meta data, upload file on SE and register in catalogs
-        self.set_meta_data()
-        md_json = json.dumps(self.metadata)
-
-        i_step += 1
-        i_substep = 0
-        for degraded in self.degraded_values:
-            data_output_pattern = f"Data/*dark-ref-degraded-{degraded:.2f}.simtel.zst"
-
-            # step 5 verify the number of events in the simtel file
-            mgv_step = self.setExecutable(
-                "dirac_simtel_check",
-                arguments=f"'{data_output_pattern}'",
-                logFile="Verify_n_showers_Log.txt",
-            )
-            mgv_step["Value"]["name"] = f"Step{i_step}.{i_substep}_VerifyNShowers"
-            mgv_step["Value"]["descr_short"] = "Verify number of showers"
-
-            # Upload and register data - NSB=1 dark
-            file_meta_data = {"runNumber": self.run_number, "nsb": 1}
-            file_md_json = json.dumps(file_meta_data)
-
-            dm_step = self.setExecutable(
-                "cta-prod-managedata",
-                arguments="'%s' '%s' %s '%s' %s %s '%s' Data"
-                % (
-                    md_json,
-                    file_md_json,
-                    self.base_path,
-                    data_output_pattern,
-                    self.package,
-                    self.program_category,
-                    self.catalogs,
-                ),
-                logFile=f"DataManagement_dark_ref_degraded_{degraded:.2f}Log.txt",
-            )
-            dm_step["Value"]["name"] = f"Step{i_step}.{i_substep}_DataManagement"
-            dm_step["Value"][
-                "descr_short"
-            ] = "Save data files to SE and register them in DFC"
-            i_substep += 1
-
-            # Upload and register log and histo file - NSB=1
-            file_meta_data = {}
-            file_md_json = json.dumps(file_meta_data)
-            log_file_pattern = f"Data/*dark-ref-degraded-{degraded:.2f}.log_hist.tar"
-            log_step = self.setExecutable(
-                "cta-prod-managedata",
-                arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Log"
-                % (
-                    md_json,
-                    md_field_json,
-                    file_md_json,
-                    self.base_path,
-                    log_file_pattern,
-                    self.package,
-                    self.program_category,
-                    self.catalogs,
-                ),
-                logFile=f"LogManagement_dark_ref_degraded_{degraded:.2f}Log.txt",
-            )
-            log_step["Value"]["name"] = f"Step{i_step}.{i_substep}_LogManagement"
-            log_step["Value"]["descr_short"] = "Save log to SE and register them in DFC"
-            i_substep += 1
-
-            if self.half_moon == "--with-half-moon":
-                # Now switching to half moon NSB
-                # Upload and register data - NSB=5 half moon
-                file_meta_data = {"runNumber": self.run_number, "nsb": 5}
-                file_md_json = json.dumps(file_meta_data)
-                data_output_pattern = "Data/*moon-ref-degraded-%.2f.simtel.zst" % (
-                    degraded
-                )
-
-                dm_step = self.setExecutable(
-                    "cta-prod-managedata",
-                    arguments="'%s' '%s' %s '%s' %s %s '%s' Data"
-                    % (
-                        md_json,
-                        file_md_json,
-                        self.base_path,
-                        data_output_pattern,
-                        self.package,
-                        self.program_category,
-                        self.catalogs,
-                    ),
-                    logFile=f"DataManagement_moon_ref_degraded_{degraded:.2f}Log.txt",
-                )
-                dm_step["Value"]["name"] = f"Step{i_step}.{i_substep}_DataManagement"
-                dm_step["Value"][
-                    "descr_short"
-                ] = "Save data files to SE and register them in DFC"
-                i_substep += 1
-
-                # Upload and register log file - NSB=5
-                file_meta_data = {}
-                file_md_json = json.dumps(file_meta_data)
-                log_file_pattern = "Data/*moon-ref-degraded-%.2f.log_hist.tar" % (
-                    degraded
-                )
-                log_step = self.setExecutable(
-                    "cta-prod-managedata",
-                    arguments="'%s' '%s' %s '%s' %s %s '%s' Log"
-                    % (
-                        md_json,
-                        file_md_json,
-                        self.base_path,
-                        log_file_pattern,
-                        self.package,
-                        self.program_category,
-                        self.catalogs,
-                    ),
-                    logFile=f"LogManagement_moon_ref_degraded_{degraded:.2f}Log.txt",
-                )
-                log_step["Value"]["name"] = f"Step{i_step}.{i_substep}_LogManagement"
-                log_step["Value"][
-                    "descr_short"
-                ] = "Save log to SE and register them in DFC"
-                i_substep += 1
-
-            i_step += 1
-
-        # Step 6 - debug only
-        if debug:
-            ls_step = self.setExecutable("/bin/ls -Ralhtr", logFile="LS_End_Log.txt")
-            ls_step["Value"]["name"] = f"Step{i_step}_LSHOME_End"
-            ls_step["Value"]["descr_short"] = "list files in Home directory"
-            i_step += 1
-
-        # Number of showers is passed via an environment variable
-        self.setExecutionEnv(
-            {
-                "NSHOW": f"{self.n_shower}",
-                "CORSIKA_MULTIPLEX_SEQUENTIAL": "1",  # Set CORSIKA multipipe to run in sequential mode (better for single-slot/cpu grid jobs)
-            }
-        )
+    """
+    # step 1 - debug only
+    i_step = 1
+    if debug:
+      ls_step = self.setExecutable('/bin/ls -alhtr', logFile='LS_Init_Log.txt')
+      ls_step['Value']['name'] = 'Step%i_LS_Init' % i_step
+      ls_step['Value']['descr_short'] = 'list files in working directory'
+      i_step += 1
+
+      env_step = self.setExecutable('/bin/env', logFile='Env_Log.txt')
+      env_step['Value']['name'] = 'Step%i_Env' % i_step
+      env_step['Value']['descr_short'] = 'Dump environment'
+      i_step += 1
+
+    # step 2 : use new CVMFS repo
+    sw_step = self.setExecutable('cta-prod-setup-software',
+                                 arguments='-p %s -v %s -a simulations -g %s -r /cvmfs/sw.cta-observatory.org/software' %
+                                 (self.package, self.version, self.compiler),
+                                 logFile='SetupSoftware_Log.txt')
+    sw_step['Value']['name'] = 'Step%i_SetupSoftware' % i_step
+    sw_step['Value']['descr_short'] = 'Setup software'
+    i_step += 1
+
+    # step 3 run corsika+sim_telarray
+    prod_exe = './dirac_prod6_muon_run'
+    prod_args = '--start_run %s --run %s %s %s %s %s %s %s %s' % \
+                (self.start_run_number, self.run_number,
+                 self.half_moon, self.degraded_mirror, self.telescope,
+                 self.cta_site, self.particle, self.pointing_dir,
+                 self.zenith_angle)
+
+    cs_step = self.setExecutable(prod_exe, arguments=prod_args,
+                                 logFile='CorsikaSimtel_Log.txt')
+    cs_step['Value']['name'] = 'Step%i_CorsikaSimtel' % i_step
+    cs_step['Value']['descr_short'] = 'Run Corsika piped into simtel'
+    i_step += 1
+
+    # step 4 - define meta data, upload file on SE and register in catalogs
+    self.set_meta_data()
+    md_json = json.dumps(self.metadata)
+
+    meta_data_field = {'array_layout': 'VARCHAR(128)', 'site': 'VARCHAR(128)',
+                       'particle': 'VARCHAR(128)',
+                       'phiP': 'float', 'thetaP': 'float',
+                       self.program_category + '_prog': 'VARCHAR(128)',
+                       self.program_category + '_prog_version': 'VARCHAR(128)',
+                       'data_level': 'int', 'configuration_id': 'int', 'merged': 'int', 'sct': 'VARCHAR(128)'}
+    md_field_json = json.dumps(meta_data_field)
+    i_step += 1
+
+    i_substep = 0
+    for degraded in self.degraded_values:
+
+      data_output_pattern = 'Data/*dark-ref-degraded-%.2f.simtel.zst' % (degraded)
+
+      # step 5 verify the number of events in the simtel file
+      mgv_step = self.setExecutable('dirac_simtel_check',
+                                    arguments="'%s'" %
+                                    (data_output_pattern),
+                                    logFile='Verify_n_showers_Log.txt')
+      mgv_step['Value']['name'] = 'Step%s.%s_VerifyNShowers' % (i_step, i_substep)
+      mgv_step['Value']['descr_short'] = 'Verify number of showers'
+
+      # Upload and register data - NSB=1 dark
+      file_meta_data = {'runNumber': self.run_number, 'nsb': 1}
+      file_md_json = json.dumps(file_meta_data)
+
+      dm_step = self.setExecutable('cta-prod-managedata',
+                                   arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Data" %
+                                   (md_json, md_field_json, file_md_json,
+                                    self.base_path, data_output_pattern, self.package,
+                                    self.program_category, self.catalogs),
+                                   logFile='DataManagement_dark_ref_degraded_%.2fLog.txt' % (degraded))
+      dm_step['Value']['name'] = 'Step%s.%s_DataManagement' % (i_step, i_substep)
+      dm_step['Value']['descr_short'] = 'Save data files to SE and register them in DFC'
+      i_substep += 1
+
+      # Upload and register log and histo file - NSB=1
+      file_meta_data = {}
+      file_md_json = json.dumps(file_meta_data)
+      log_file_pattern = 'Data/*dark-ref-degraded-%.2f.log_hist.tar' % (degraded)
+      log_step = self.setExecutable('cta-prod-managedata',
+                                    arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Log" %
+                                    (md_json, md_field_json, file_md_json,
+                                     self.base_path, log_file_pattern, self.package,
+                                     self.program_category, self.catalogs),
+                                    logFile='LogManagement_dark_ref_degraded_%.2fLog.txt' % (degraded))
+      log_step['Value']['name'] = 'Step%s.%s_LogManagement' % (i_step, i_substep)
+      log_step['Value']['descr_short'] = 'Save log to SE and register them in DFC'
+      i_substep += 1
+
+      if self.half_moon == '--with-half-moon':
+        # Now switching to half moon NSB
+        # Upload and register data - NSB=5 half moon
+        file_meta_data = {'runNumber': self.run_number, 'nsb': 5}
+        file_md_json = json.dumps(file_meta_data)
+        data_output_pattern = 'Data/*moon-ref-degraded-%.2f.simtel.zst' % (degraded)
+
+        dm_step = self.setExecutable('cta-prod-managedata',
+                                     arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Data" %
+                                     (md_json, md_field_json, file_md_json,
+                                      self.base_path, data_output_pattern, self.package,
+                                      self.program_category, self.catalogs),
+                                     logFile='DataManagement_moon_ref_degraded_%.2fLog.txt' % (degraded))
+        dm_step['Value']['name'] = 'Step%s.%s_DataManagement' % (i_step, i_substep)
+        dm_step['Value']['descr_short'] = 'Save data files to SE and register them in DFC'
+        i_substep += 1
+
+        # Upload and register log file - NSB=5
+        file_meta_data = {}
+        file_md_json = json.dumps(file_meta_data)
+        log_file_pattern = 'Data/*moon-ref-degraded-%.2f.log_hist.tar' % (degraded)
+        log_step = self.setExecutable('cta-prod-managedata',
+                                      arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Log" %
+                                      (md_json, md_field_json, file_md_json,
+                                       self.base_path, log_file_pattern, self.package,
+                                       self.program_category, self.catalogs),
+                                      logFile='LogManagement_moon_ref_degraded_%.2fLog.txt' % (degraded))
+        log_step['Value']['name'] = 'Step%s.%s_LogManagement' % (i_step, i_substep)
+        log_step['Value']['descr_short'] = 'Save log to SE and register them in DFC'
+        i_substep += 1
+
+      i_step += 1
+
+    # Step 6 - debug only
+    if debug:
+      ls_step = self.setExecutable('/bin/ls -Ralhtr', logFile='LS_End_Log.txt')
+      ls_step['Value']['name'] = 'Step%s_LSHOME_End' % i_step
+      ls_step['Value']['descr_short'] = 'list files in Home directory'
+      i_step += 1
+
+    # Number of showers is passed via an environment variable
+    self.setExecutionEnv({
+      'NSHOW': '%s' % self.n_shower,
+      'CORSIKA_MULTIPLEX_SEQUENTIAL': '1'  # Set CORSIKA multipipe to run in sequential mode (better for single-slot/cpu grid jobs)
+    })
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/Prod6MCPipeNSBJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/Prod6MCPipeNSBJob.py`

 * *Files 17% similar despite different names*

```diff
@@ -3,372 +3,298 @@
 """
 
 __RCSID__ = "$Id$"
 
 # generic imports
 import json
 import collections
-
 # DIRAC imports
 import DIRAC
 from DIRAC.Interfaces.API.Job import Job
 from CTADIRAC.Core.Utilities.tool_box import DATA_LEVEL_METADATA_ID
 
 
 class Prod6MCPipeNSBJob(Job):
-    """Job extension class for Prod5 MC NSB simulations,
-    takes care of running corsika piped into simtel
-    2 output files are created for Dark and Moon NSB
+  """ Job extension class for Prod5 MC NSB simulations,
+  takes care of running corsika piped into simtel
+  2 output files are created for Dark and Moon NSB
+  """
+
+  def __init__(self, cpu_time=259200):
+    """ Constructor takes almosst everything from base class
+
+    Keyword arguments:
+    cpuTime -- max cpu time allowed for the job
+    """
+    Job.__init__(self)
+    self.setCPUTime(cpu_time)
+    self.setName('Prod6MC_Generation')
+    self.setType('MCSimulation')
+    self.package = 'corsika_simtelarray'
+    self.version = '2022-08-03'
+    self.compiler = 'gcc83_matchcpu'
+    self.program_category = 'tel_sim'
+    self.prog_name = 'sim_telarray'
+    self.configuration_id = 15
+    self.output_data_level = DATA_LEVEL_METADATA_ID['R1']
+    self.base_path = '/vo.cta.in2p3.fr/MC/PROD6/'
+    self.catalogs = json.dumps(['DIRACFileCatalog', 'TSCatalog'])
+    self.metadata = collections.OrderedDict()
+
+  def set_site(self, site):
+    """ Set the site to simulate
+
+    Parameters:
+    site -- a string for the site name (LaPalma)
+    """
+    if site in ['Paranal', 'LaPalma']:
+      DIRAC.gLogger.info('Set Corsika site to: %s' % site)
+      self.cta_site = site
+    else:
+      DIRAC.gLogger.error('Site is unknown: %s' % site)
+      DIRAC.exit(-1)
+
+  def set_particle(self, particle):
+    """ Set the corsika primary particle
+
+    Parameters:
+    particle -- a string for the particle type/name
+    """
+    if particle in ['gamma', 'gamma-diffuse', 'electron', 'proton', 'helium']:
+      DIRAC.gLogger.info('Set Corsika particle to: %s' % particle)
+      self.particle = particle
+    else:
+      DIRAC.gLogger.error('Corsika does not know particle type: %s' % particle)
+      DIRAC.exit(-1)
+
+  def set_pointing_dir(self, pointing):
+    """ Set the pointing direction, North or South
+
+    Parameters:
+    pointing -- a string for the pointing direction
+    """
+    if pointing in ['North', 'South', 'East', 'West']:
+      DIRAC.gLogger.info('Set Pointing dir to: %s' % pointing)
+      self.pointing_dir = pointing
+    else:
+      DIRAC.gLogger.error('Unknown pointing direction: %s' % pointing)
+      DIRAC.exit(-1)
+
+  def set_full_moon(self, full_moon=False):
+    """ Set if to simulate with full-moon conditions
+
+    Parameters:
+    full_moon -- a boolean for simulating with full moon conditions
     """
+    if full_moon is True:
+      DIRAC.gLogger.info('Set simulations with full-moon conditions')
+      self.full_moon = '--with-full-moon'
+    else:
+      self.full_moon = '--with-halfmoon'  # We alawys at least run with half moon
+
+  def set_magic(self, with_magic=False):
+    """ Set if to simulate with MAGIC
 
-    def __init__(self, cpu_time=259200):
-        """Constructor takes almosst everything from base class
+    Parameters:
+    with_magic -- a boolean for simulating with MAGIC
+    """
+    if with_magic is True:
+      DIRAC.gLogger.info('Set simulations with MAGIC telescopes')
+      self.with_magic = '--with-magic'
+    else:
+      self.with_magic = ''
 
-        Keyword arguments:
-        cpuTime -- max cpu time allowed for the job
-        """
-        Job.__init__(self)
-        self.setCPUTime(cpu_time)
-        self.setName("Prod6MC_Generation")
-        self.setType("MCSimulation")
-        self.package = "corsika_simtelarray"
-        self.version = "2022-08-03"
-        self.compiler = "gcc83_matchcpu"
-        self.program_category = "tel_sim"
-        self.prog_name = "sim_telarray"
-        self.configuration_id = 15
-        self.output_data_level = DATA_LEVEL_METADATA_ID["R1"]
-        self.base_path = "/vo.cta.in2p3.fr/MC/PROD6/"
-        self.catalogs = json.dumps(["DIRACFileCatalog", "TSCatalog"])
-        self.metadata = collections.OrderedDict()
-
-    def set_site(self, site):
-        """Set the site to simulate
-
-        Parameters:
-        site -- a string for the site name (LaPalma)
-        """
-        if site in ["Paranal", "LaPalma"]:
-            DIRAC.gLogger.info(f"Set Corsika site to: {site}")
-            self.cta_site = site
-        else:
-            DIRAC.gLogger.error(f"Site is unknown: {site}")
-            DIRAC.exit(-1)
-
-    def set_particle(self, particle):
-        """Set the corsika primary particle
-
-        Parameters:
-        particle -- a string for the particle type/name
-        """
-        if particle in ["gamma", "gamma-diffuse", "electron", "proton", "helium"]:
-            DIRAC.gLogger.info(f"Set Corsika particle to: {particle}")
-            self.particle = particle
-        else:
-            DIRAC.gLogger.error(f"Corsika does not know particle type: {particle}")
-            DIRAC.exit(-1)
-
-    def set_pointing_dir(self, pointing):
-        """Set the pointing direction, North or South
-
-        Parameters:
-        pointing -- a string for the pointing direction
-        """
-        if pointing in ["North", "South", "East", "West"]:
-            DIRAC.gLogger.info(f"Set Pointing dir to: {pointing}")
-            self.pointing_dir = pointing
-        else:
-            DIRAC.gLogger.error(f"Unknown pointing direction: {pointing}")
-            DIRAC.exit(-1)
-
-    def set_full_moon(self, full_moon=False):
-        """Set if to simulate with full-moon conditions
-
-        Parameters:
-        full_moon -- a boolean for simulating with full moon conditions
-        """
-        if full_moon is True:
-            DIRAC.gLogger.info("Set simulations with full-moon conditions")
-            self.full_moon = "--with-full-moon"
-        else:
-            self.full_moon = "--with-halfmoon"  # We alawys at least run with half moon
-
-    def set_magic(self, with_magic=False):
-        """Set if to simulate with MAGIC
-
-        Parameters:
-        with_magic -- a boolean for simulating with MAGIC
-        """
-        if with_magic is True:
-            DIRAC.gLogger.info("Set simulations with MAGIC telescopes")
-            self.with_magic = "--with-magic"
-        else:
-            self.with_magic = ""
-
-    def set_sct(self, with_sct=False):
-        """Set if to include SCTs in simulations
-
-        Parameters:
-        with_sct -- a boolean if to include SCTs
-        """
-        if with_sct is True:
-            DIRAC.gLogger.info("Set to include SCTs")
-            self.with_sct = "--with-sct"
-            self.sct_metadata = "True"
-        else:
-            self.with_sct = ""
-            self.sct_metadata = "False"
-
-    def set_meta_data(self):
-        """define the common meta data of the application"""
-        # The order of the metadata dictionary is important,
-        # since it's used to build the directory structure
-        self.metadata["array_layout"] = "Prod6-Hyperarray"
-        self.metadata["site"] = self.cta_site
-        self.metadata["particle"] = self.particle
-        # for air shower simulation means North=0 and South=180
-        # but here piped into tel_sim so North=180 and South=0
-        if self.pointing_dir == "North":
-            self.metadata["phiP"] = 180
-        if self.pointing_dir == "South":
-            self.metadata["phiP"] = 0
-        self.metadata["thetaP"] = float(self.zenith_angle)
-        self.metadata[self.program_category + "_prog"] = self.prog_name
-        self.metadata[self.program_category + "_prog_version"] = "".join(
-            self.version.rsplit("-sc", 1)
-        )
-        self.metadata["data_level"] = self.output_data_level
-        self.metadata["configuration_id"] = self.configuration_id
+  def set_sct(self, with_sct=False):
+    """ Set if to include SCTs in simulations
 
-    def setupWorkflow(self, debug=False):
-        """Override the base class job workflow to adapt to NSB test simulations
+    Parameters:
+    with_sct -- a boolean if to include SCTs
+    """
+    if with_sct is True:
+      DIRAC.gLogger.info('Set to include SCTs')
+      self.with_sct = '--with-sct'
+      self.sct_metadata = 'True'
+    else:
+      self.with_sct = ''
+      self.sct_metadata = 'False'
+
+  def set_meta_data(self):
+    """ define the common meta data of the application
+    """
+    # The order of the metadata dictionary is important,
+    # since it's used to build the directory structure
+    self.metadata['array_layout'] = 'Prod6-Hyperarray'
+    self.metadata['site'] = self.cta_site
+    self.metadata['particle'] = self.particle
+    # for air shower simulation means North=0 and South=180
+    # but here piped into tel_sim so North=180 and South=0
+    if self.pointing_dir == 'North':
+      self.metadata['phiP'] = 180
+    if self.pointing_dir == 'South':
+      self.metadata['phiP'] = 0
+    self.metadata['thetaP'] = float(self.zenith_angle)
+    self.metadata[self.program_category + '_prog'] = self.prog_name
+    self.metadata[self.program_category + '_prog_version'] = ''.join(self.version.rsplit('-sc', 1))
+    self.metadata['data_level'] = self.output_data_level
+    self.metadata['configuration_id'] = self.configuration_id
+
+  def setupWorkflow(self, debug=False):
+    """ Override the base class job workflow to adapt to NSB test simulations
         All parameters shall have been defined before that method is called.
-        """
-        # step 1 - debug only
-        i_step = 1
-        if debug:
-            ls_step = self.setExecutable("/bin/ls -alhtr", logFile="LS_Init_Log.txt")
-            ls_step["Value"]["name"] = "Step%i_LS_Init" % i_step
-            ls_step["Value"]["descr_short"] = "list files in working directory"
-            i_step += 1
-
-            env_step = self.setExecutable("/bin/env", logFile="Env_Log.txt")
-            env_step["Value"]["name"] = "Step%i_Env" % i_step
-            env_step["Value"]["descr_short"] = "Dump environment"
-            i_step += 1
-
-        # step 2 : use new CVMFS repo
-        sw_step = self.setExecutable(
-            "cta-prod-setup-software",
-            arguments="-p %s -v %s -a simulations -g %s"
-            % (self.package, self.version, self.compiler),
-            logFile="SetupSoftware_Log.txt",
-        )
-        sw_step["Value"]["name"] = "Step%i_SetupSoftware" % i_step
-        sw_step["Value"]["descr_short"] = "Setup software"
-        i_step += 1
-
-        # step 3 run corsika+sim_telarray
-        prod_exe = "./dirac_prod6_run"
-        prod_args = "--start_run {} --run {} {} {} {} {} {} {} {}".format(
-            self.start_run_number,
-            self.run_number,
-            self.full_moon,
-            self.with_sct,
-            self.with_magic,
-            self.cta_site,
-            self.particle,
-            self.pointing_dir,
-            self.zenith_angle,
-        )
-
-        cs_step = self.setExecutable(
-            prod_exe, arguments=prod_args, logFile="CorsikaSimtel_Log.txt"
-        )
-        cs_step["Value"]["name"] = "Step%i_CorsikaSimtel" % i_step
-        cs_step["Value"]["descr_short"] = "Run Corsika piped into simtel"
-        i_step += 1
-
-        # step 4 verify the number of events in the simtel file
-        data_output_pattern = "Data/*.simtel.zst"
-        mgv_step = self.setExecutable(
-            "dirac_simtel_check",
-            arguments=f"'{data_output_pattern}'",
-            logFile="Verify_n_showers_Log.txt",
-        )
-        mgv_step["Value"]["name"] = "Step%i_VerifyNShowers" % i_step
-        mgv_step["Value"]["descr_short"] = "Verify number of showers"
-        i_step += 1
-
-        # step 5 - define meta data, upload file on SE and register in catalogs
-        self.set_meta_data()
-        md_json = json.dumps(self.metadata)
-
-        # Upload and register data - NSB=1 dark
-        file_meta_data = {
-            "runNumber": self.run_number,
-            "nsb": 1,
-            "sct": self.sct_metadata,
-        }
-        file_md_json = json.dumps(file_meta_data)
-        data_output_pattern = "Data/*dark*.simtel.zst"
-
-        dm_step = self.setExecutable(
-            "cta-prod-managedata",
-            arguments="'%s' '%s' %s '%s' %s %s '%s' Data"
-            % (
-                md_json,
-                file_md_json,
-                self.base_path,
-                data_output_pattern,
-                self.package,
-                self.program_category,
-                self.catalogs,
-            ),
-            logFile="DataManagement_dark_Log.txt",
-        )
-        dm_step["Value"]["name"] = f"Step{i_step}_DataManagement"
-        dm_step["Value"][
-            "descr_short"
-        ] = "Save data files to SE and register them in DFC"
-        i_step += 1
-
-        # Upload and register log and histo file - NSB=1
-        file_meta_data = {}
-        file_md_json = json.dumps(file_meta_data)
-        log_file_pattern = "Data/*dark*.log_hist.tar"
-        log_step = self.setExecutable(
-            "cta-prod-managedata",
-            arguments="'%s' '%s' %s '%s' %s %s '%s' Log"
-            % (
-                md_json,
-                file_md_json,
-                self.base_path,
-                log_file_pattern,
-                self.package,
-                self.program_category,
-                self.catalogs,
-            ),
-            logFile="LogManagement_dark_Log.txt",
-        )
-        log_step["Value"]["name"] = f"Step{i_step}_LogManagement"
-        log_step["Value"]["descr_short"] = "Save log to SE and register them in DFC"
-        i_step += 1
-
-        # Now switching to half moon NSB
-        # Upload and register data - NSB=5 half moon
-        file_meta_data = {
-            "runNumber": self.run_number,
-            "nsb": 5,
-            "sct": self.sct_metadata,
-        }
-        file_md_json = json.dumps(file_meta_data)
-        data_output_pattern = "Data/*-moon*.simtel.zst"
-
-        dm_step = self.setExecutable(
-            "cta-prod-managedata",
-            arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Data"
-            % (
-                md_json,
-                md_field_json,
-                file_md_json,
-                self.base_path,
-                data_output_pattern,
-                self.package,
-                self.program_category,
-                self.catalogs,
-            ),
-            logFile="DataManagement_moon_Log.txt",
-        )
-        dm_step["Value"]["name"] = f"Step{i_step}_DataManagement"
-        dm_step["Value"][
-            "descr_short"
-        ] = "Save data files to SE and register them in DFC"
-        i_step += 1
-
-        # Upload and register log file - NSB=5
-        file_meta_data = {}
-        file_md_json = json.dumps(file_meta_data)
-        log_file_pattern = "Data/*-moon*.log_hist.tar"
-        log_step = self.setExecutable(
-            "cta-prod-managedata",
-            arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Log"
-            % (
-                md_json,
-                md_field_json,
-                file_md_json,
-                self.base_path,
-                log_file_pattern,
-                self.package,
-                self.program_category,
-                self.catalogs,
-            ),
-            logFile="LogManagement_moon_Log.txt",
-        )
-        log_step["Value"]["name"] = f"Step{i_step}_LogManagement"
-        log_step["Value"]["descr_short"] = "Save log to SE and register them in DFC"
-        i_step += 1
-
-        if self.full_moon == "--with-full-moon":
-            # Now switching to full moon NSB
-            # Upload and register data - NSB=19 full moon
-            file_meta_data = {
-                "runNumber": self.run_number,
-                "nsb": 19,
-                "sct": self.sct_metadata,
-            }
-            file_md_json = json.dumps(file_meta_data)
-            data_output_pattern = "Data/*-fullmoon*.simtel.zst"
-
-            dm_step = self.setExecutable(
-                "cta-prod-managedata",
-                arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Data"
-                % (
-                    md_json,
-                    md_field_json,
-                    file_md_json,
-                    self.base_path,
-                    data_output_pattern,
-                    self.package,
-                    self.program_category,
-                    self.catalogs,
-                ),
-                logFile="DataManagement_fullmoon_Log.txt",
-            )
-            dm_step["Value"]["name"] = f"Step{i_step}_DataManagement"
-            dm_step["Value"][
-                "descr_short"
-            ] = "Save data files to SE and register them in DFC"
-            i_step += 1
-
-            # Upload and register log file - NSB=19
-            file_meta_data = {}
-            file_md_json = json.dumps(file_meta_data)
-            log_file_pattern = "Data/*-fullmoon*.log_hist.tar"
-            log_step = self.setExecutable(
-                "cta-prod-managedata",
-                arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Log"
-                % (
-                    md_json,
-                    md_field_json,
-                    file_md_json,
-                    self.base_path,
-                    log_file_pattern,
-                    self.package,
-                    self.program_category,
-                    self.catalogs,
-                ),
-                logFile="LogManagement_fullmoon_Log.txt",
-            )
-            log_step["Value"]["name"] = f"Step{i_step}_LogManagement"
-            log_step["Value"]["descr_short"] = "Save log to SE and register them in DFC"
-            i_step += 1
-
-        # Step 6 - debug only
-        if debug:
-            ls_step = self.setExecutable("/bin/ls -Ralhtr", logFile="LS_End_Log.txt")
-            ls_step["Value"]["name"] = f"Step{i_step}_LSHOME_End"
-            ls_step["Value"]["descr_short"] = "list files in Home directory"
-            i_step += 1
+    """
+    # step 1 - debug only
+    i_step = 1
+    if debug:
+      ls_step = self.setExecutable('/bin/ls -alhtr', logFile='LS_Init_Log.txt')
+      ls_step['Value']['name'] = 'Step%i_LS_Init' % i_step
+      ls_step['Value']['descr_short'] = 'list files in working directory'
+      i_step += 1
+
+      env_step = self.setExecutable('/bin/env', logFile='Env_Log.txt')
+      env_step['Value']['name'] = 'Step%i_Env' % i_step
+      env_step['Value']['descr_short'] = 'Dump environment'
+      i_step += 1
+
+    # step 2 : use new CVMFS repo
+    sw_step = self.setExecutable('cta-prod-setup-software',
+                                 arguments='-p %s -v %s -a simulations -g %s' %
+                                 (self.package, self.version, self.compiler),
+                                 logFile='SetupSoftware_Log.txt')
+    sw_step['Value']['name'] = 'Step%i_SetupSoftware' % i_step
+    sw_step['Value']['descr_short'] = 'Setup software'
+    i_step += 1
+
+    # step 3 run corsika+sim_telarray
+    prod_exe = './dirac_prod6_run'
+    prod_args = '--start_run %s --run %s %s %s %s %s %s %s %s' % \
+                (self.start_run_number, self.run_number,
+                 self.full_moon, self.with_sct, self.with_magic,
+                 self.cta_site, self.particle, self.pointing_dir,
+                 self.zenith_angle)
+
+    cs_step = self.setExecutable(prod_exe, arguments=prod_args,
+                                 logFile='CorsikaSimtel_Log.txt')
+    cs_step['Value']['name'] = 'Step%i_CorsikaSimtel' % i_step
+    cs_step['Value']['descr_short'] = 'Run Corsika piped into simtel'
+    i_step += 1
+
+    # step 4 verify the number of events in the simtel file
+    data_output_pattern = 'Data/*.simtel.zst'
+    mgv_step = self.setExecutable('dirac_simtel_check',
+                                  arguments="'%s'" %
+                                  (data_output_pattern),
+                                  logFile='Verify_n_showers_Log.txt')
+    mgv_step['Value']['name'] = 'Step%i_VerifyNShowers' % i_step
+    mgv_step['Value']['descr_short'] = 'Verify number of showers'
+    i_step += 1
+
+    # step 5 - define meta data, upload file on SE and register in catalogs
+    self.set_meta_data()
+    md_json = json.dumps(self.metadata)
+
+    meta_data_field = {'array_layout': 'VARCHAR(128)', 'site': 'VARCHAR(128)',
+                       'particle': 'VARCHAR(128)',
+                       'phiP': 'float', 'thetaP': 'float',
+                       self.program_category + '_prog': 'VARCHAR(128)',
+                       self.program_category + '_prog_version': 'VARCHAR(128)',
+                       'data_level': 'int', 'configuration_id': 'int', 'merged': 'int'}
+    md_field_json = json.dumps(meta_data_field)
+
+    # Upload and register data - NSB=1 dark
+    file_meta_data = {'runNumber': self.run_number, 'nsb': 1, 'sct': self.sct_metadata}
+    file_md_json = json.dumps(file_meta_data)
+    data_output_pattern = 'Data/*dark*.simtel.zst'
+
+    dm_step = self.setExecutable('cta-prod-managedata',
+                                 arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Data" %
+                                 (md_json, md_field_json, file_md_json,
+                                  self.base_path, data_output_pattern, self.package,
+                                  self.program_category, self.catalogs),
+                                 logFile='DataManagement_dark_Log.txt')
+    dm_step['Value']['name'] = 'Step%s_DataManagement' % i_step
+    dm_step['Value']['descr_short'] = 'Save data files to SE and register them in DFC'
+    i_step += 1
+
+    # Upload and register log and histo file - NSB=1
+    file_meta_data = {}
+    file_md_json = json.dumps(file_meta_data)
+    log_file_pattern = 'Data/*dark*.log_hist.tar'
+    log_step = self.setExecutable('cta-prod-managedata',
+                                  arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Log" %
+                                  (md_json, md_field_json, file_md_json,
+                                   self.base_path, log_file_pattern, self.package,
+                                   self.program_category, self.catalogs),
+                                  logFile='LogManagement_dark_Log.txt')
+    log_step['Value']['name'] = 'Step%s_LogManagement' % i_step
+    log_step['Value']['descr_short'] = 'Save log to SE and register them in DFC'
+    i_step += 1
+
+    # Now switching to half moon NSB
+    # Upload and register data - NSB=5 half moon
+    file_meta_data = {'runNumber': self.run_number, 'nsb': 5, 'sct': self.sct_metadata}
+    file_md_json = json.dumps(file_meta_data)
+    data_output_pattern = 'Data/*-moon*.simtel.zst'
+
+    dm_step = self.setExecutable('cta-prod-managedata',
+                                 arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Data" %
+                                 (md_json, md_field_json, file_md_json,
+                                  self.base_path, data_output_pattern, self.package,
+                                  self.program_category, self.catalogs),
+                                 logFile='DataManagement_moon_Log.txt')
+    dm_step['Value']['name'] = 'Step%s_DataManagement' % i_step
+    dm_step['Value']['descr_short'] = 'Save data files to SE and register them in DFC'
+    i_step += 1
+
+    # Upload and register log file - NSB=5
+    file_meta_data = {}
+    file_md_json = json.dumps(file_meta_data)
+    log_file_pattern = 'Data/*-moon*.log_hist.tar'
+    log_step = self.setExecutable('cta-prod-managedata',
+                                  arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Log" %
+                                  (md_json, md_field_json, file_md_json,
+                                   self.base_path, log_file_pattern, self.package,
+                                   self.program_category, self.catalogs),
+                                  logFile='LogManagement_moon_Log.txt')
+    log_step['Value']['name'] = 'Step%s_LogManagement' % i_step
+    log_step['Value']['descr_short'] = 'Save log to SE and register them in DFC'
+    i_step += 1
+
+    if self.full_moon == '--with-full-moon':
+      # Now switching to full moon NSB
+      # Upload and register data - NSB=19 full moon
+      file_meta_data = {'runNumber': self.run_number, 'nsb': 19, 'sct': self.sct_metadata}
+      file_md_json = json.dumps(file_meta_data)
+      data_output_pattern = 'Data/*-fullmoon*.simtel.zst'
+
+      dm_step = self.setExecutable('cta-prod-managedata',
+                                   arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Data" %
+                                   (md_json, md_field_json, file_md_json,
+                                    self.base_path, data_output_pattern, self.package,
+                                    self.program_category, self.catalogs),
+                                   logFile='DataManagement_fullmoon_Log.txt')
+      dm_step['Value']['name'] = 'Step%s_DataManagement' % i_step
+      dm_step['Value']['descr_short'] = 'Save data files to SE and register them in DFC'
+      i_step += 1
+
+      # Upload and register log file - NSB=19
+      file_meta_data = {}
+      file_md_json = json.dumps(file_meta_data)
+      log_file_pattern = 'Data/*-fullmoon*.log_hist.tar'
+      log_step = self.setExecutable('cta-prod-managedata',
+                                    arguments="'%s' '%s' '%s' %s '%s' %s %s '%s' Log" %
+                                    (md_json, md_field_json, file_md_json,
+                                     self.base_path, log_file_pattern, self.package,
+                                     self.program_category, self.catalogs),
+                                    logFile='LogManagement_fullmoon_Log.txt')
+      log_step['Value']['name'] = 'Step%s_LogManagement' % i_step
+      log_step['Value']['descr_short'] = 'Save log to SE and register them in DFC'
+      i_step += 1
+
+    # Step 6 - debug only
+    if debug:
+      ls_step = self.setExecutable('/bin/ls -Ralhtr', logFile='LS_End_Log.txt')
+      ls_step['Value']['name'] = 'Step%s_LSHOME_End' % i_step
+      ls_step['Value']['descr_short'] = 'list files in Home directory'
+      i_step += 1
 
-        # Number of showers is passed via an environment variable
-        self.setExecutionEnv({"NSHOW": f"{self.n_shower}"})
+    # Number of showers is passed via an environment variable
+    self.setExecutionEnv({'NSHOW': '%s' % self.n_shower})
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/ProvCtapipeJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/ProvCtapipeJob.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/SimpleCtapipeJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/SimpleCtapipeJob.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/API/SimtelTSJob.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/API/SimtelTSJob.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/DataRemovalByQueryTSExample.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/DataRemovalByQueryTSExample.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/DataRemovalTSExample.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/DataRemovalTSExample.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/DataReplicaRemovalTSExample.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/DataReplicaRemovalTSExample.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/DataReplicationByQueryTSExample.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/DataReplicationByQueryTSExample.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/DataReplicationTSExample.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/DataReplicationTSExample.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/ProvCtapipeJobExample.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/ProvCtapipeJobExample.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/SimpleCtapipeJobExample.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/SimpleCtapipeJobExample.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/SimtelTSExample.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/SimtelTSExample.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5_ctapipe_merge_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5_ctapipe_merge_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5_ctapipe_modeling_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5_ctapipe_modeling_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5_evndisp_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5_evndisp_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5_mcpipe_nsb_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5_mcpipe_nsb_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5_ps_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5_ps_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_alpha_divergent_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_alpha_divergent_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_alpha_ssts_fullmoon_nsb_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_alpha_ssts_fullmoon_nsb_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_alpha_ssts_nsb_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_alpha_ssts_nsb_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_nsb_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_mcpipe_nsb_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_ps_generic_stage1_merge_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_ps_generic_stage1_merge_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_ps_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_ps_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_ps_mcpipe_stage1_merge_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_ps_mcpipe_stage1_merge_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_ps_split_stage1_merge_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_ps_split_stage1_merge_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod5b_sing_evndisp_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod5b_sing_evndisp_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod6_mcpipe_divergent_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod6_mcpipe_divergent_launcher.py`

 * *Files 2% similar despite different names*

```diff
@@ -82,15 +82,14 @@
   # parameters from command line
   job.set_site(args[1])
   job.set_particle(args[2])
   job.set_pointing_dir(args[3])
   job.zenith_angle = args[4]
   job.n_shower = args[5]
 
-  job.set_half_moon(half_moon=False)  # No half moon simulations with divergent pointing for now
   job.set_full_moon(full_moon=False)  # No full moon simulations with divergent pointing for now
   job.set_sct(with_sct=False)  # No SCTs with divergent pointing for now
   job.set_magic(with_magic=False)  # No MAGIC with divergent pointing
 
 
   # output
   job.setOutputSandbox(['*Log.txt'])
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod6_mcpipe_muon_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod6_mcpipe_muon_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod6_mcpipe_nsb_launcher.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod6_mcpipe_nsb_launcher.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/Interfaces/test/prod_mark_corrupted_DL0.py` & `CTADIRAC-2.2a3/src/CTADIRAC/Interfaces/test/prod_mark_corrupted_DL0.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/Client/CtapipeProcessingElement.py` & `CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/Client/CtapipeModelingElement.py`

 * *Files 6% similar despite different names*

```diff
@@ -5,31 +5,32 @@
 __RCSID__ = "$Id$"
 
 # generic imports
 from copy import deepcopy
 import json
 
 # DIRAC imports
-from CTADIRAC.Interfaces.API.CtapipeProcessJob import CtapipeProcessJob
+import DIRAC
+from CTADIRAC.Interfaces.API.Prod5CtaPipeModelingJob import Prod5CtaPipeModelingJob
 from CTADIRAC.ProductionSystem.Client.WorkflowElement import WorkflowElement
 
 
-class CtapipeProcessingElement(WorkflowElement):
+class CtapipeModelingElement(WorkflowElement):
     """Composite class for workflow element (production step + job)"""
 
     #############################################################################
 
     def __init__(self, parent_prod_step):
         """Constructor"""
         WorkflowElement.__init__(self, parent_prod_step)
-        self.job = CtapipeProcessJob(cpuTime=259200.0)
+        self.job = Prod5CtaPipeModelingJob(cpuTime=259200.0)
         self.job.setOutputSandbox(["*Log.txt"])
         self.job.input_limit = None
         self.prod_step.Type = "DataReprocessing"
-        self.prod_step.Name = "CtapipeProcessing"
+        self.prod_step.Name = "Modeling_ctapipe"
         self.mandatory_keys = {"MCCampaign", "configuration_id", "version"}
         self.constrained_job_keys = {"catalogs", "moon", "group_size"}
         self.constrained_input_keys = {
             "pointing_dir",
             "zenith_angle",
             "moon",
             "sct",
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/Client/CtapipeTrainEnergyElement.py` & `CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/Client/EvnDispElement.py`

 * *Files 5% similar despite different names*

```diff
@@ -5,33 +5,32 @@
 __RCSID__ = "$Id$"
 
 # generic imports
 from copy import deepcopy
 import json
 
 # DIRAC imports
-from CTADIRAC.Interfaces.API.CtapipeTrainEnergyJob import CtapipeTrainEnergyJob
+import DIRAC
+from CTADIRAC.Interfaces.API.EvnDispSingJob import EvnDispSingJob
 from CTADIRAC.ProductionSystem.Client.WorkflowElement import WorkflowElement
 
 
-class CtapipeTrainEnergyElement(WorkflowElement):
+class EvnDispElement(WorkflowElement):
     """Composite class for workflow element (production step + job)"""
 
     #############################################################################
 
     def __init__(self, parent_prod_step):
         """Constructor"""
         WorkflowElement.__init__(self, parent_prod_step)
-        self.job = CtapipeTrainEnergyJob(cpuTime=259200.0)
+        self.job = EvnDispSingJob(cpuTime=259200.0)
         self.job.setOutputSandbox(["*Log.txt"])
         self.job.input_limit = None
-        self.job.merged = 0
-        # self.job.output_extension = "merged.DL2.h5"
         self.prod_step.Type = "DataReprocessing"
-        self.prod_step.Name = "CtapipeTrainEnergy"
+        self.prod_step.Name = "EvnDisp"
         self.mandatory_keys = {"MCCampaign", "configuration_id", "version"}
         self.constrained_job_keys = {"catalogs", "group_size", "moon"}
         self.constrained_input_keys = {
             "pointing_dir",
             "zenith_angle",
             "sct",
             "moon",
@@ -79,8 +78,12 @@
     def build_job_output_data(self, workflow_step):
         """Build job output meta data"""
         metadata = deepcopy(self.prod_step.Inputquery)
         for key, value in workflow_step["job_config"].items():
             metadata[key] = value
         self.job.set_output_metadata(metadata)
 
-    #############################################################################
+    def build_element_config(self):
+        """Set job and production step attributes specific to the configuration"""
+        self.prod_step.GroupSize = self.job.group_size
+        self.job.set_executable_sequence(debug=False)
+        self.prod_step.Body = self.job.workflow.toXML()
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/Client/EvnDispElement.py` & `CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/Client/MergingElement.py`

 * *Files 12% similar despite different names*

```diff
@@ -6,31 +6,32 @@
 
 # generic imports
 from copy import deepcopy
 import json
 
 # DIRAC imports
 import DIRAC
-from CTADIRAC.Interfaces.API.EvnDispSingJob import EvnDispSingJob
+from CTADIRAC.Interfaces.API.Prod5CtaPipeMergeJob import Prod5CtaPipeMergeJob
 from CTADIRAC.ProductionSystem.Client.WorkflowElement import WorkflowElement
 
 
-class EvnDispElement(WorkflowElement):
+class MergingElement(WorkflowElement):
     """Composite class for workflow element (production step + job)"""
 
     #############################################################################
 
     def __init__(self, parent_prod_step):
         """Constructor"""
         WorkflowElement.__init__(self, parent_prod_step)
-        self.job = EvnDispSingJob(cpuTime=259200.0)
+        self.job = Prod5CtaPipeMergeJob(cpuTime=259200.0)
         self.job.setOutputSandbox(["*Log.txt"])
         self.job.input_limit = None
+        self.job.merged = 0
         self.prod_step.Type = "DataReprocessing"
-        self.prod_step.Name = "EvnDisp"
+        self.prod_step.Name = "Merge"
         self.mandatory_keys = {"MCCampaign", "configuration_id", "version"}
         self.constrained_job_keys = {"catalogs", "group_size", "moon"}
         self.constrained_input_keys = {
             "pointing_dir",
             "zenith_angle",
             "sct",
             "moon",
@@ -76,14 +77,26 @@
             self.prod_step.Inputquery["div_ang"] = str(value)
 
     def build_job_output_data(self, workflow_step):
         """Build job output meta data"""
         metadata = deepcopy(self.prod_step.Inputquery)
         for key, value in workflow_step["job_config"].items():
             metadata[key] = value
+        merged = self.get_merging_level()
+        metadata["merged"] = merged
         self.job.set_output_metadata(metadata)
 
+    def get_merging_level(self):
+        """Get the merging level from parent step or from the user query"""
+        if self.prod_step.ParentStep:
+            merged = self.prod_step.ParentStep.Outputquery["merged"]
+        else:
+            merged = self.job.merged
+        return merged
+
     def build_element_config(self):
         """Set job and production step attributes specific to the configuration"""
         self.prod_step.GroupSize = self.job.group_size
         self.job.set_executable_sequence(debug=False)
         self.prod_step.Body = self.job.workflow.toXML()
+
+    #############################################################################
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/Client/SimulationElement.py` & `CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/Client/SimulationElement.py`

 * *Files 2% similar despite different names*

```diff
@@ -21,15 +21,15 @@
 
     def __init__(self, parent_prod_step):
         """Constructor"""
         WorkflowElement.__init__(self, parent_prod_step)
         self.job = MCPipeNSBJob()
         self.job.setOutputSandbox(["*Log.txt"])
         self.prod_step.Type = "MCSimulation"
-        self.prod_step.Name = "MCSimulation"
+        self.prod_step.Name = "MC_Simulation"
         self.mandatory_keys = {"MCCampaign", "configuration_id", "version"}
         self.constrained_job_keys = {
             "version",
             "catalogs",
             "sct",
             "particle",
             "pointing_dir",
@@ -62,18 +62,14 @@
         elif key == "div_ang":
             self.job.set_div_ang(value)
 
     def build_input_data(self, workflow_config, workflow_step):
         """Simulation Elements do not have input data"""
         self.prod_step.Inputquery = {}
 
-    def build_job_input_data(self, mode):
-        """Simulation Elements do not have input data"""
-        pass
-
     def build_output_data(self):
         """Build output data from the job metadata and the metadata added on the files"""
         self.prod_step.Outputquery = deepcopy(self.job.output_metadata)
         for key, value in self.job.output_file_metadata.items():
             if isinstance(value, list):
                 if len(value) > 1:
                     self.prod_step.Outputquery[key] = {"in": value}
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/Client/WorkflowElement.py` & `CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/Client/WorkflowElement.py`

 * *Files 2% similar despite different names*

```diff
@@ -117,15 +117,15 @@
             DIRAC.gLogger.error("No job submitted: job must have input data")
             DIRAC.exit(-1)
         if mode.lower() == "ps" and self.job.input_limit:
             f = open("test_input_data.list", "w")
             for lfn in input_data:
                 f.write(lfn + "\n")
             f.close()
-            DIRAC.gLogger.notice("\t\tInput limit found: %d files dumped to test_input_data.list" % len(input_data))
+            DIRAC.gLogger.notice("%d LFNs dumped in test_input_data.list" % len(input_data))
             self.prod_step.Inputquery = {}
 
     def build_element_config(self):
         """Set job and production step attributes specific to the configuration"""
         self.job.set_executable_sequence(debug=False)
         self.prod_step.Body = self.job.workflow.toXML()
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/config/processing_config_from_meta_query.yml` & `CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/config/processing_config_from_meta_query.yml`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/config/production_config.yml` & `CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/config/production_config.yml`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/ProductionSystem/scripts/cta_prod_submit.py` & `CTADIRAC-2.2a3/src/CTADIRAC/ProductionSystem/scripts/cta_prod_submit.py`

 * *Files 4% similar despite different names*

```diff
@@ -23,26 +23,21 @@
 
 Script.parseCommandLine()
 import DIRAC
 import yaml
 import json
 
 from DIRAC.ProductionSystem.Client.ProductionClient import ProductionClient
-from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient
 from DIRAC.Interfaces.API.Dirac import Dirac
 from CTADIRAC.ProductionSystem.Client.SimulationElement import SimulationElement
-from CTADIRAC.ProductionSystem.Client.CtapipeProcessingElement import (
-    CtapipeProcessingElement,
+from CTADIRAC.ProductionSystem.Client.CtapipeModelingElement import (
+    CtapipeModelingElement,
 )
 from CTADIRAC.ProductionSystem.Client.EvnDispElement import EvnDispElement
 from CTADIRAC.ProductionSystem.Client.MergingElement import MergingElement
-from CTADIRAC.ProductionSystem.Client.CtapipeTrainEnergyElement import (
-    CtapipeTrainEnergyElement,
-)
-from CTADIRAC.Core.Utilities.tool_box import read_inputs_from_file
 
 
 def check_id(workflow_config):
     """Check step ID values"""
     for workflow_step in workflow_config:
         if not workflow_step.get("ID"):
             DIRAC.gLogger.error("Unknown step ID")
@@ -72,21 +67,19 @@
 
 def instantiate_workflow_element_from_type(workflow_step, parent_prod_step):
     """Instantiate workflow element class based on the step type required"""
     wf_elt = None
     if workflow_step["job_config"]["type"].lower() == "mcsimulation":
         wf_elt = SimulationElement(parent_prod_step)
     elif workflow_step["job_config"]["type"].lower() == "ctapipeprocessing":
-        wf_elt = CtapipeProcessingElement(parent_prod_step)
+        wf_elt = CtapipeModelingElement(parent_prod_step)
     elif workflow_step["job_config"]["type"].lower() == "evndispprocessing":
         wf_elt = EvnDispElement(parent_prod_step)
     elif workflow_step["job_config"]["type"].lower() == "merging":
         wf_elt = MergingElement(parent_prod_step)
-    elif workflow_step["job_config"]["type"].lower() == "ctapipetrainenergy":
-        wf_elt = CtapipeTrainEnergyElement(parent_prod_step)
     else:
         DIRAC.gLogger.error("Unknown step type")
         DIRAC.exit(-1)
     return wf_elt
 
 
 def find_parent_prod_step(workflow_element_list, workflow_step):
@@ -147,15 +140,15 @@
     for workflow_step in workflow_config["ProdSteps"]:
         parent_prod_step = find_parent_prod_step(workflow_element_list, workflow_step)
         workflow_element = instantiate_workflow_element_from_type(
             workflow_step, parent_prod_step
         )
         check_destination_catalogs(workflow_element, workflow_step, parents_list)
         DIRAC.gLogger.notice(
-            f"\tBuilding Production step: {workflow_step['job_config']['type']} ..."
+            "\tBuilding Production step: %s" % workflow_step["job_config"]["type"]
         )
         # The order of the following instructions matters
         workflow_element.build_input_data(workflow_config, workflow_step)
         workflow_element.build_job_attributes(workflow_config, workflow_step)
         workflow_element.build_job_output_data(workflow_step)
         workflow_element.build_element_config()
         workflow_element.build_output_data()
@@ -183,22 +176,21 @@
     workflow_config_file = arguments[1]
     mode = "ps"
     if len(arguments) == 3:
         mode = arguments[2]
     if mode not in ["ps", "wms", "local"]:
         Script.showHelp()
 
-    with open(workflow_config_file) as stream:
+    with open(workflow_config_file, "r") as stream:
         workflow_config = yaml.safe_load(stream)
 
     ##################################
     # Create the production
-    DIRAC.gLogger.notice(f"\nBuilding new production: {prod_name}")
+    DIRAC.gLogger.notice("Building new production: %s" % prod_name)
     prod_sys_client = ProductionClient()
-    trans_client = TransformationClient()
 
     ##################################
     # Build production steps according to the workflow description
     build_workflow(workflow_config, prod_sys_client, mode)
     ##################################
 
     # The default mode is ps, i.e. submit the worflow to the Production System
@@ -214,57 +206,30 @@
         # Start the production, i.e. instantiate the transformation steps
         res = prod_sys_client.startProduction(prod_name)
 
         if not res["OK"]:
             DIRAC.gLogger.error(res["Message"])
             DIRAC.exit(-1)
 
-        DIRAC.gLogger.notice(f"\nProduction {prod_name} successfully created")
+        DIRAC.gLogger.notice("Production %s successfully created" % prod_name)
 
         # Print the submitted transformations
         res = prod_sys_client.getProductionTransformations(prod_name)
         if res["OK"]:
-            trans_list = res["Value"]
-            if not trans_list:
+            transList = res["Value"]
+            if not transList:
                 DIRAC.gLogger.notice(
-                    f"No transformation associated with production {prod_name}"
+                    "No transformation associated with production %s" % prod_name
                 )
                 DIRAC.exit(-1)
-            for trans in trans_list:
-                transID = trans["TransformationID"]
-                trans_name = trans_client.getTransformationParameters(
-                    transID, "TransformationName"
-                )["Value"]
+            for trans in transList:
                 DIRAC.gLogger.notice(
-                    f"\tSubmitted transformation: {trans_name} with transID {transID}"
+                    "Submitted transformation: %s" % trans["TransformationID"]
                 )
         else:
             DIRAC.gLogger.error(res["Message"])
             DIRAC.exit(-1)
 
-        # If input_limit is set attach testing files to the first transformation
-        prodStep0 = workflow_config["ProdSteps"][0]
-        job_config = prodStep0["job_config"]
-        if "input_limit" in job_config:
-            trans0 = trans_list[0]["TransformationID"]
-            DIRAC.gLogger.notice(
-                "Using %d input files from test_input_data.list"
-                % (job_config["input_limit"])
-            )
-            infile_list = read_inputs_from_file("test_input_data.list")
-            res = trans_client.addFilesToTransformation(
-                trans0, infile_list
-            )  # Files added here
-            if not res["OK"]:
-                DIRAC.gLogger.error(res["Message"])
-                DIRAC.exit(-1)
-            else:
-                DIRAC.gLogger.notice(
-                    "Successfully added %d files to transformation %s"
-                    % (job_config["input_limit"], trans0)
-                )
-                DIRAC.exit(0)
-
 
 ########################################################
 if __name__ == "__main__":
     main()
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC/__init__.py` & `CTADIRAC-2.2a3/src/CTADIRAC/__init__.py`

 * *Files identical despite different names*

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC.egg-info/SOURCES.txt` & `CTADIRAC-2.2a3/src/CTADIRAC.egg-info/SOURCES.txt`

 * *Files 8% similar despite different names*

```diff
@@ -20,83 +20,80 @@
 src/CTADIRAC/Core/Utilities/__init__.py
 src/CTADIRAC/Core/Utilities/tool_box.py
 src/CTADIRAC/Core/Workflow/__init__.py
 src/CTADIRAC/Core/Workflow/Modules/ProdDataManager.py
 src/CTADIRAC/Core/Workflow/Modules/__init__.py
 src/CTADIRAC/Core/scripts/__init__.py
 src/CTADIRAC/Core/scripts/cta_dms_check_lfn.py
-src/CTADIRAC/Core/scripts/cta_install_tornado_component.py
 src/CTADIRAC/Core/scripts/cta_prod_add_dataset.py
 src/CTADIRAC/Core/scripts/cta_prod_add_file.py
 src/CTADIRAC/Core/scripts/cta_prod_add_prov.py
 src/CTADIRAC/Core/scripts/cta_prod_check_replicas.py
 src/CTADIRAC/Core/scripts/cta_prod_dump_dataset.py
 src/CTADIRAC/Core/scripts/cta_prod_failure_monitor.py
 src/CTADIRAC/Core/scripts/cta_prod_fix_nsb.py
 src/CTADIRAC/Core/scripts/cta_prod_get_file.py
-src/CTADIRAC/Core/scripts/cta_prod_get_merge_size.py
 src/CTADIRAC/Core/scripts/cta_prod_get_replicas.py
 src/CTADIRAC/Core/scripts/cta_prod_get_se_status.py
 src/CTADIRAC/Core/scripts/cta_prod_git_clone.py
 src/CTADIRAC/Core/scripts/cta_prod_init_prov.py
 src/CTADIRAC/Core/scripts/cta_prod_managedata.py
 src/CTADIRAC/Core/scripts/cta_prod_mark_corrupted_DL0.py
 src/CTADIRAC/Core/scripts/cta_prod_monitor.py
 src/CTADIRAC/Core/scripts/cta_prod_move_dataset.py
 src/CTADIRAC/Core/scripts/cta_prod_move_dataset_status.py
 src/CTADIRAC/Core/scripts/cta_prod_remove_corrupted_file.py
 src/CTADIRAC/Core/scripts/cta_prod_remove_dataset.py
 src/CTADIRAC/Core/scripts/cta_prod_remove_file.py
 src/CTADIRAC/Core/scripts/cta_prod_replicate_lfn.py
-src/CTADIRAC/Core/scripts/cta_prod_set_metadata.py
 src/CTADIRAC/Core/scripts/cta_prod_setup_software.py
 src/CTADIRAC/Core/scripts/cta_prod_show_dataset.py
-src/CTADIRAC/Core/scripts/cta_prod_split_dataset.py
 src/CTADIRAC/Core/scripts/cta_prod_unregister_file.py
 src/CTADIRAC/Core/scripts/cta_prod_update_dataset.py
 src/CTADIRAC/Core/scripts/cta_prod_verifysteps.py
 src/CTADIRAC/Core/scripts/cta_rms_request.py
 src/CTADIRAC/Core/scripts/cta_transformation_add_files.py
 src/CTADIRAC/Core/scripts/cta_transformation_clean.py
 src/CTADIRAC/Core/scripts/cta_transformation_delete.py
 src/CTADIRAC/Core/scripts/cta_transformation_get_files.py
 src/CTADIRAC/Core/scripts/cta_transformation_get_tasks.py
 src/CTADIRAC/Core/scripts/cta_transformation_select.py
+src/CTADIRAC/Core/scripts/cta_transformation_set_file_status.py
 src/CTADIRAC/Core/scripts/cta_transformation_show_progress.py
+src/CTADIRAC/Core/scripts/cta_transformation_stress_test.py
 src/CTADIRAC/Core/scripts/cta_transformation_treat_done_tasks.py
 src/CTADIRAC/Core/scripts/cta_transformation_treat_failed_tasks.py
 src/CTADIRAC/Core/scripts/cta_transformation_treat_incomplete_transfers.py
 src/CTADIRAC/Core/scripts/cta_transformation_treat_problematic_files.py
 src/CTADIRAC/Core/scripts/cta_user_managedata.py
+src/CTADIRAC/Core/scripts/get_OSB.py
+src/CTADIRAC/Core/scripts/read_cpu.py
 src/CTADIRAC/DataManagementSystem/ConfigTemplate.cfg
 src/CTADIRAC/DataManagementSystem/__init__.py
 src/CTADIRAC/DataManagementSystem/Client/ProvBase.py
 src/CTADIRAC/DataManagementSystem/Client/ProvClient.py
 src/CTADIRAC/DataManagementSystem/Client/__init__.py
 src/CTADIRAC/DataManagementSystem/Client/testProvClient_muon.py
 src/CTADIRAC/DataManagementSystem/DB/ProvenanceDB.py
 src/CTADIRAC/DataManagementSystem/DB/__init__.py
 src/CTADIRAC/DataManagementSystem/Service/ProvenanceManagerHandler.py
 src/CTADIRAC/DataManagementSystem/Service/__init__.py
 src/CTADIRAC/DataManagementSystem/Utilities/__init__.py
 src/CTADIRAC/DataManagementSystem/private/JSONUtils.py
 src/CTADIRAC/DataManagementSystem/private/__init__.py
 src/CTADIRAC/Interfaces/__init__.py
-src/CTADIRAC/Interfaces/API/CtapipeApplyModelsJob.py
-src/CTADIRAC/Interfaces/API/CtapipeMergeJob.py
-src/CTADIRAC/Interfaces/API/CtapipeProcessJob.py
-src/CTADIRAC/Interfaces/API/CtapipeTrainClassifierJob.py
-src/CTADIRAC/Interfaces/API/CtapipeTrainEnergyJob.py
 src/CTADIRAC/Interfaces/API/EvnDisp4SSTJob.py
 src/CTADIRAC/Interfaces/API/EvnDispProd5Job.py
 src/CTADIRAC/Interfaces/API/EvnDispProd5SingJob.py
 src/CTADIRAC/Interfaces/API/EvnDispSingJob.py
 src/CTADIRAC/Interfaces/API/MCPipeNSBJob.py
-src/CTADIRAC/Interfaces/API/ProcessingJob.py
+src/CTADIRAC/Interfaces/API/Prod5CtaPipeMergeJob.py
+src/CTADIRAC/Interfaces/API/Prod5CtaPipeModelingJob.py
 src/CTADIRAC/Interfaces/API/Prod5MCPipeNSBJob.py
+src/CTADIRAC/Interfaces/API/Prod5Stage1Job.py
 src/CTADIRAC/Interfaces/API/Prod5bMCPipeAlphaDivergentJob.py
 src/CTADIRAC/Interfaces/API/Prod5bMCPipeAlphaSSTsFullMoonNSBJob.py
 src/CTADIRAC/Interfaces/API/Prod5bMCPipeAlphaSSTsNSBJob.py
 src/CTADIRAC/Interfaces/API/Prod5bMCPipeNSBJob.py
 src/CTADIRAC/Interfaces/API/Prod6MCPipeDivergentJob.py
 src/CTADIRAC/Interfaces/API/Prod6MCPipeMuonJob.py
 src/CTADIRAC/Interfaces/API/Prod6MCPipeNSBJob.py
@@ -109,14 +106,15 @@
 src/CTADIRAC/Interfaces/test/DataReplicaRemovalTSExample.py
 src/CTADIRAC/Interfaces/test/DataReplicationByQueryTSExample.py
 src/CTADIRAC/Interfaces/test/DataReplicationTSExample.py
 src/CTADIRAC/Interfaces/test/ProvCtapipeJobExample.py
 src/CTADIRAC/Interfaces/test/SimpleCtapipeJobExample.py
 src/CTADIRAC/Interfaces/test/SimtelTSExample.py
 src/CTADIRAC/Interfaces/test/__init__.py
+src/CTADIRAC/Interfaces/test/move_data_ps_launcher.py
 src/CTADIRAC/Interfaces/test/prod5_ctapipe_merge_launcher.py
 src/CTADIRAC/Interfaces/test/prod5_ctapipe_modeling_launcher.py
 src/CTADIRAC/Interfaces/test/prod5_evndisp_launcher.py
 src/CTADIRAC/Interfaces/test/prod5_mcpipe_nsb_launcher.py
 src/CTADIRAC/Interfaces/test/prod5_ps_launcher.py
 src/CTADIRAC/Interfaces/test/prod5b_mcpipe_alpha_divergent_launcher.py
 src/CTADIRAC/Interfaces/test/prod5b_mcpipe_alpha_ssts_fullmoon_nsb_launcher.py
@@ -129,22 +127,19 @@
 src/CTADIRAC/Interfaces/test/prod5b_sing_evndisp_launcher.py
 src/CTADIRAC/Interfaces/test/prod6_mcpipe_divergent_launcher.py
 src/CTADIRAC/Interfaces/test/prod6_mcpipe_muon_launcher.py
 src/CTADIRAC/Interfaces/test/prod6_mcpipe_nsb_launcher.py
 src/CTADIRAC/Interfaces/test/prod_mark_corrupted_DL0.py
 src/CTADIRAC/Interfaces/test/testJob.py
 src/CTADIRAC/ProductionSystem/__init__.py
-src/CTADIRAC/ProductionSystem/Client/CtapipeProcessingElement.py
-src/CTADIRAC/ProductionSystem/Client/CtapipeTrainEnergyElement.py
+src/CTADIRAC/ProductionSystem/Client/CtapipeModelingElement.py
 src/CTADIRAC/ProductionSystem/Client/EvnDispElement.py
 src/CTADIRAC/ProductionSystem/Client/MergingElement.py
 src/CTADIRAC/ProductionSystem/Client/SimulationElement.py
 src/CTADIRAC/ProductionSystem/Client/WorkflowElement.py
 src/CTADIRAC/ProductionSystem/Client/__init__.py
 src/CTADIRAC/ProductionSystem/config/__init__.py
 src/CTADIRAC/ProductionSystem/config/processing_config_from_dataset.yml
 src/CTADIRAC/ProductionSystem/config/processing_config_from_meta_query.yml
 src/CTADIRAC/ProductionSystem/config/production_config.yml
-src/CTADIRAC/ProductionSystem/config/production_cwl.yml
 src/CTADIRAC/ProductionSystem/scripts/__init__.py
-src/CTADIRAC/ProductionSystem/scripts/cta_prod_submit.py
-src/CTADIRAC/ProductionSystem/scripts/cta_prod_submit_from_cwl.py
+src/CTADIRAC/ProductionSystem/scripts/cta_prod_submit.py
```

### Comparing `CTADIRAC-2.2.9/src/CTADIRAC.egg-info/entry_points.txt` & `CTADIRAC-2.2a3/src/CTADIRAC.egg-info/entry_points.txt`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,9 @@
 [console_scripts]
 cta-dms-check-lfn = CTADIRAC.Core.scripts.cta_dms_check_lfn:main
-cta-install-tornado-component = CTADIRAC.Core.scripts.cta_install_tornado_component:main
 cta-prod-add-dataset = CTADIRAC.Core.scripts.cta_prod_add_dataset:main
 cta-prod-add-file = CTADIRAC.Core.scripts.cta_prod_add_file:main
 cta-prod-add-prov = CTADIRAC.Core.scripts.cta_prod_add_prov:main
 cta-prod-check-replicas = CTADIRAC.Core.scripts.cta_prod_check_replicas:main
 cta-prod-dump-dataset = CTADIRAC.Core.scripts.cta_prod_dump_dataset:main
 cta-prod-failure-monitor = CTADIRAC.Core.scripts.cta_prod_failure_monitor:main
 cta-prod-fix-nsb = CTADIRAC.Core.scripts.cta_prod_fix_nsb:main
@@ -18,20 +17,17 @@
 cta-prod-monitor = CTADIRAC.Core.scripts.cta_prod_monitor:main
 cta-prod-move-dataset = CTADIRAC.Core.scripts.cta_prod_move_dataset:main
 cta-prod-move-dataset-status = CTADIRAC.Core.scripts.cta_prod_move_dataset_status:main
 cta-prod-remove-corrupted-file = CTADIRAC.Core.scripts.cta_prod_remove_corrupted_file:main
 cta-prod-remove-dataset = CTADIRAC.Core.scripts.cta_prod_remove_dataset:main
 cta-prod-remove-file = CTADIRAC.Core.scripts.cta_prod_remove_file:main
 cta-prod-replicate-lfn = CTADIRAC.Core.scripts.cta_prod_replicate_lfn:main
-cta-prod-set-metadata = CTADIRAC.Core.scripts.cta_prod_set_metadata:main
 cta-prod-setup-software = CTADIRAC.Core.scripts.cta_prod_setup_software:main
 cta-prod-show-dataset = CTADIRAC.Core.scripts.cta_prod_show_dataset:main
-cta-prod-split-dataset = CTADIRAC.Core.scripts.cta_prod_split_dataset:main
 cta-prod-submit = CTADIRAC.ProductionSystem.scripts.cta_prod_submit:main
-cta-prod-submit-from-cwl = CTADIRAC.ProductionSystem.scripts.cta_prod_submit_from_cwl:main
 cta-prod-unregister-file = CTADIRAC.Core.scripts.cta_prod_unregister_file:main
 cta-prod-update-dataset = CTADIRAC.Core.scripts.cta_prod_update_dataset:main
 cta-prod-verifysteps = CTADIRAC.Core.scripts.cta_prod_verifysteps:main
 cta-rms-request = CTADIRAC.Core.scripts.cta_rms_request:main
 cta-transformation-add-files = CTADIRAC.Core.scripts.cta_transformation_add_files:main
 cta-transformation-clean = CTADIRAC.Core.scripts.cta_transformation_clean:main
 cta-transformation-delete = CTADIRAC.Core.scripts.cta_transformation_delete:main
@@ -43,7 +39,8 @@
 cta-transformation-treat-failed-tasks = CTADIRAC.Core.scripts.cta_transformation_treat_failed_tasks:main
 cta-transformation-treat-incomplete-transfers = CTADIRAC.Core.scripts.cta_transformation_treat_incomplete_transfers:main
 cta-transformation-treat-problematic-files = CTADIRAC.Core.scripts.cta_transformation_treat_problematic_files:main
 cta-user-managedata = CTADIRAC.Core.scripts.cta_user_managedata:main
 
 [dirac]
 metadata = CTADIRAC:extension_metadata
+
```

