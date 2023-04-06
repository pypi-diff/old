# Comparing `tmp/rcsb.utils.dictionary-1.7.tar.gz` & `tmp/rcsb.utils.dictionary-1.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rcsb.utils.dictionary-1.7.tar", last modified: Wed Mar 22 14:30:03 2023, max compression
+gzip compressed data, was "rcsb.utils.dictionary-1.8.tar", last modified: Thu Apr  6 11:55:17 2023, max compression
```

## Comparing `rcsb.utils.dictionary-1.7.tar` & `rcsb.utils.dictionary-1.8.tar`

### file list

```diff
@@ -1,37 +1,37 @@
-drwxr-xr-x   0 vsts      (1001) docker     (122)        0 2023-03-22 14:30:03.195326 rcsb.utils.dictionary-1.7/
--rw-r--r--   0 vsts      (1001) docker     (122)    10021 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/HISTORY.txt
--rw-r--r--   0 vsts      (1001) docker     (122)    11357 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/LICENSE
--rw-r--r--   0 vsts      (1001) docker     (122)      113 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/MANIFEST.in
--rw-r--r--   0 vsts      (1001) docker     (122)     1674 2023-03-22 14:30:03.195326 rcsb.utils.dictionary-1.7/PKG-INFO
--rw-r--r--   0 vsts      (1001) docker     (122)      986 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/README.md
-drwxr-xr-x   0 vsts      (1001) docker     (122)        0 2023-03-22 14:30:03.191326 rcsb.utils.dictionary-1.7/rcsb/
--rw-r--r--   0 vsts      (1001) docker     (122)       65 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/__init__.py
-drwxr-xr-x   0 vsts      (1001) docker     (122)        0 2023-03-22 14:30:03.195326 rcsb.utils.dictionary-1.7/rcsb/utils/
--rw-r--r--   0 vsts      (1001) docker     (122)       65 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/__init__.py
-drwxr-xr-x   0 vsts      (1001) docker     (122)        0 2023-03-22 14:30:03.195326 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/
--rw-r--r--   0 vsts      (1001) docker     (122)    38239 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodAssemblyHelper.py
--rw-r--r--   0 vsts      (1001) docker     (122)    46267 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodChemRefHelper.py
--rw-r--r--   0 vsts      (1001) docker     (122)   200580 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodCommonUtils.py
--rw-r--r--   0 vsts      (1001) docker     (122)    18142 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodCompModelHelper.py
--rw-r--r--   0 vsts      (1001) docker     (122)   136792 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodEntityHelper.py
--rw-r--r--   0 vsts      (1001) docker     (122)   143571 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodEntityInstanceHelper.py
--rw-r--r--   0 vsts      (1001) docker     (122)    65391 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodEntryHelper.py
--rw-r--r--   0 vsts      (1001) docker     (122)     6094 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodResourceCacheWorkflow.py
--rw-r--r--   0 vsts      (1001) docker     (122)    35595 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodResourceProvider.py
--rw-r--r--   0 vsts      (1001) docker     (122)     9779 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodRunner.py
--rw-r--r--   0 vsts      (1001) docker     (122)    48393 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodSecStructUtils.py
--rw-r--r--   0 vsts      (1001) docker     (122)     4097 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictionaryApiProvider.py
--rw-r--r--   0 vsts      (1001) docker     (122)     3779 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictionaryApiProviderWrapper.py
--rw-r--r--   0 vsts      (1001) docker     (122)    13373 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/NeighborInteractionProvider.py
--rw-r--r--   0 vsts      (1001) docker     (122)     4196 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/NeighborInteractionWorkflow.py
--rw-r--r--   0 vsts      (1001) docker     (122)      144 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/__init__.py
-drwxr-xr-x   0 vsts      (1001) docker     (122)        0 2023-03-22 14:30:03.191326 rcsb.utils.dictionary-1.7/rcsb.utils.dictionary.egg-info/
--rw-r--r--   0 vsts      (1001) docker     (122)     1674 2023-03-22 14:30:03.000000 rcsb.utils.dictionary-1.7/rcsb.utils.dictionary.egg-info/PKG-INFO
--rw-r--r--   0 vsts      (1001) docker     (122)     1175 2023-03-22 14:30:03.000000 rcsb.utils.dictionary-1.7/rcsb.utils.dictionary.egg-info/SOURCES.txt
--rw-r--r--   0 vsts      (1001) docker     (122)        1 2023-03-22 14:30:03.000000 rcsb.utils.dictionary-1.7/rcsb.utils.dictionary.egg-info/dependency_links.txt
--rw-r--r--   0 vsts      (1001) docker     (122)        1 2023-03-22 14:30:00.000000 rcsb.utils.dictionary-1.7/rcsb.utils.dictionary.egg-info/not-zip-safe
--rw-r--r--   0 vsts      (1001) docker     (122)      385 2023-03-22 14:30:03.000000 rcsb.utils.dictionary-1.7/rcsb.utils.dictionary.egg-info/requires.txt
--rw-r--r--   0 vsts      (1001) docker     (122)        5 2023-03-22 14:30:03.000000 rcsb.utils.dictionary-1.7/rcsb.utils.dictionary.egg-info/top_level.txt
--rw-r--r--   0 vsts      (1001) docker     (122)      374 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/requirements.txt
--rwxr-xr-x   0 vsts      (1001) docker     (122)      108 2023-03-22 14:30:03.199326 rcsb.utils.dictionary-1.7/setup.cfg
--rwxr-xr-x   0 vsts      (1001) docker     (122)     2242 2023-03-22 14:25:40.000000 rcsb.utils.dictionary-1.7/setup.py
+drwxr-xr-x   0 vsts      (1001) docker     (122)        0 2023-04-06 11:55:17.240972 rcsb.utils.dictionary-1.8/
+-rw-r--r--   0 vsts      (1001) docker     (122)    10293 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/HISTORY.txt
+-rw-r--r--   0 vsts      (1001) docker     (122)    11357 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/LICENSE
+-rw-r--r--   0 vsts      (1001) docker     (122)      113 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/MANIFEST.in
+-rw-r--r--   0 vsts      (1001) docker     (122)     1674 2023-04-06 11:55:17.240972 rcsb.utils.dictionary-1.8/PKG-INFO
+-rw-r--r--   0 vsts      (1001) docker     (122)      986 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/README.md
+drwxr-xr-x   0 vsts      (1001) docker     (122)        0 2023-04-06 11:55:17.232972 rcsb.utils.dictionary-1.8/rcsb/
+-rw-r--r--   0 vsts      (1001) docker     (122)       65 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/__init__.py
+drwxr-xr-x   0 vsts      (1001) docker     (122)        0 2023-04-06 11:55:17.236972 rcsb.utils.dictionary-1.8/rcsb/utils/
+-rw-r--r--   0 vsts      (1001) docker     (122)       65 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/__init__.py
+drwxr-xr-x   0 vsts      (1001) docker     (122)        0 2023-04-06 11:55:17.240972 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/
+-rw-r--r--   0 vsts      (1001) docker     (122)    38239 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodAssemblyHelper.py
+-rw-r--r--   0 vsts      (1001) docker     (122)    46584 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodChemRefHelper.py
+-rw-r--r--   0 vsts      (1001) docker     (122)   200580 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodCommonUtils.py
+-rw-r--r--   0 vsts      (1001) docker     (122)    20846 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodCompModelHelper.py
+-rw-r--r--   0 vsts      (1001) docker     (122)   138579 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodEntityHelper.py
+-rw-r--r--   0 vsts      (1001) docker     (122)   143571 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodEntityInstanceHelper.py
+-rw-r--r--   0 vsts      (1001) docker     (122)    65391 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodEntryHelper.py
+-rw-r--r--   0 vsts      (1001) docker     (122)     6094 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodResourceCacheWorkflow.py
+-rw-r--r--   0 vsts      (1001) docker     (122)    35595 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodResourceProvider.py
+-rw-r--r--   0 vsts      (1001) docker     (122)     9779 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodRunner.py
+-rw-r--r--   0 vsts      (1001) docker     (122)    48393 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodSecStructUtils.py
+-rw-r--r--   0 vsts      (1001) docker     (122)     4097 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictionaryApiProvider.py
+-rw-r--r--   0 vsts      (1001) docker     (122)     3783 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictionaryApiProviderWrapper.py
+-rw-r--r--   0 vsts      (1001) docker     (122)    13373 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/NeighborInteractionProvider.py
+-rw-r--r--   0 vsts      (1001) docker     (122)     4196 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/NeighborInteractionWorkflow.py
+-rw-r--r--   0 vsts      (1001) docker     (122)      144 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/__init__.py
+drwxr-xr-x   0 vsts      (1001) docker     (122)        0 2023-04-06 11:55:17.236972 rcsb.utils.dictionary-1.8/rcsb.utils.dictionary.egg-info/
+-rw-r--r--   0 vsts      (1001) docker     (122)     1674 2023-04-06 11:55:17.000000 rcsb.utils.dictionary-1.8/rcsb.utils.dictionary.egg-info/PKG-INFO
+-rw-r--r--   0 vsts      (1001) docker     (122)     1175 2023-04-06 11:55:17.000000 rcsb.utils.dictionary-1.8/rcsb.utils.dictionary.egg-info/SOURCES.txt
+-rw-r--r--   0 vsts      (1001) docker     (122)        1 2023-04-06 11:55:17.000000 rcsb.utils.dictionary-1.8/rcsb.utils.dictionary.egg-info/dependency_links.txt
+-rw-r--r--   0 vsts      (1001) docker     (122)        1 2023-04-06 11:55:14.000000 rcsb.utils.dictionary-1.8/rcsb.utils.dictionary.egg-info/not-zip-safe
+-rw-r--r--   0 vsts      (1001) docker     (122)      385 2023-04-06 11:55:17.000000 rcsb.utils.dictionary-1.8/rcsb.utils.dictionary.egg-info/requires.txt
+-rw-r--r--   0 vsts      (1001) docker     (122)        5 2023-04-06 11:55:17.000000 rcsb.utils.dictionary-1.8/rcsb.utils.dictionary.egg-info/top_level.txt
+-rw-r--r--   0 vsts      (1001) docker     (122)      374 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/requirements.txt
+-rwxr-xr-x   0 vsts      (1001) docker     (122)      108 2023-04-06 11:55:17.240972 rcsb.utils.dictionary-1.8/setup.cfg
+-rwxr-xr-x   0 vsts      (1001) docker     (122)     2242 2023-04-06 11:49:17.000000 rcsb.utils.dictionary-1.8/setup.py
```

### Comparing `rcsb.utils.dictionary-1.7/HISTORY.txt` & `rcsb.utils.dictionary-1.8/HISTORY.txt`

 * *Files 4% similar despite different names*

```diff
@@ -103,7 +103,10 @@
 21-Feb-2023 - V1.02 Update method in DictMethodEntryHelper to handle experimental resolutions properly (see RO-3559)
 03-Mar-2023 - V1.03 Standardize configuration for DictMethodResourceCacheWorkflow, add testResourceCacheWorkflow
 07-Mar-2023 - V1.04 Bug fix in DictMethodChemRefHelper;
                     Stop loading CARD data to rcsb_polymer_entity_feature
 14-Mar-2023 - V1.05 Load CARD annotation data to rcsb_polymer_entity_annotation
 16-Mar-2023 - V1.06 Update configuration of DictMethodResourceCacheWorkflow() and NeighborInteractionWorkflow() to use HERE and CACHE folder
 20-Mar-2023 - V1.07 Fix formula weight calculation of CSM polymer entities
+ 5-Apr-2023 - V1.08 Update population of provenance_source attributes for taxonomy/organism and gene categories;
+                    Correct attribute name for rcsb_chem_comp_target provenance;
+                    Stop loading rcsb_chem_comp_synonyms for type 'Brand Name'
```

### Comparing `rcsb.utils.dictionary-1.7/LICENSE` & `rcsb.utils.dictionary-1.8/LICENSE`

 * *Files identical despite different names*

### Comparing `rcsb.utils.dictionary-1.7/PKG-INFO` & `rcsb.utils.dictionary-1.8/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rcsb.utils.dictionary
-Version: 1.7
+Version: 1.8
 Summary: RCSB Python Dictionary Utility Classes
 Home-page: https://github.com/rcsb/py-rcsb_utils_dictionary
 Author: John Westbrook
 Author-email: john.westbrook@rcsb.org
 License: Apache 2.0
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
```

### Comparing `rcsb.utils.dictionary-1.7/README.md` & `rcsb.utils.dictionary-1.8/README.md`

 * *Files identical despite different names*

### Comparing `rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodAssemblyHelper.py` & `rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodAssemblyHelper.py`

 * *Files identical despite different names*

### Comparing `rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodChemRefHelper.py` & `rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodChemRefHelper.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,16 @@
 ##
 # File:    DictMethodChemRefHelper.py
 # Author:  J. Westbrook
 # Date:    16-Jul-2019
 # Version: 0.001 Initial version
 #
+# Updates:
+#   29-Mar-2023 dwp Correct attribute name '_rcsb_chem_comp_target.provenance_code' to '_rcsb_chem_comp_target.provenance_source'
+#    5-Apr-2023 dwp Stop loading rcsb_chem_comp_synonyms for rcsb_chem_comp_synonyms.type 'Brand Name' (to be loaded to new separate data item later)
 ##
 """
 Helper class implements external method references supporting chemical
 reference data definitions in the RCSB dictionary extension.
 """
 __docformat__ = "google en"
 __author__ = "John Westbrook"
@@ -466,15 +469,15 @@
              _rcsb_chem_comp_target.ordinal
              _rcsb_chem_comp_target.name
              _rcsb_chem_comp_target.interaction_type
              _rcsb_chem_comp_target.target_actions
              _rcsb_chem_comp_target.organism_common_name
              _rcsb_chem_comp_target.reference_database_name
              _rcsb_chem_comp_target.reference_database_accession_code
-             _rcsb_chem_comp_target.provenance_code
+             _rcsb_chem_comp_target.provenance_source
              ATP 1 "O-phosphoseryl-tRNA(Sec) selenium transferase" target cofactor Human UniProt Q9HD40 DrugBank
 
         DrugBank target info:
         {
             "type": "target",
             "name": "Alanine--glyoxylate aminotransferase 2, mitochondrial",
             "organism": "Human",
@@ -514,21 +517,21 @@
                                 "ordinal",
                                 "name",
                                 "interaction_type",
                                 "target_actions",
                                 "organism_common_name",
                                 "reference_database_name",
                                 "reference_database_accession_code",
-                                "provenance_code",
+                                "provenance_source",
                             ],
                         )
                     )
                 wObj = dataContainer.getObj(catName)
                 logger.debug("Using DrugBank mapping length %d", len(dbMapD))
-                rL = wObj.selectIndices("DrugBank", "provenance_code")
+                rL = wObj.selectIndices("DrugBank", "provenance_source")
                 if rL:
                     ok = wObj.removeRows(rL)
                     if not ok:
                         logger.debug("Error removing rows in %r %r", catName, rL)
                 #
                 iRow = wObj.getRowCount()
                 iRow = wObj.getRowCount()
@@ -540,15 +543,15 @@
                     if "actions" in tD and tD["actions"]:
                         wObj.setValue(";".join(tD["actions"]), "target_actions", iRow)
                     if "organism" in tD:
                         wObj.setValue(tD["organism"], "organism_common_name", iRow)
                     if "uniprot_ids" in tD:
                         wObj.setValue("UniProt", "reference_database_name", iRow)
                         wObj.setValue(tD["uniprot_ids"], "reference_database_accession_code", iRow)
-                    wObj.setValue("DrugBank", "provenance_code", iRow)
+                    wObj.setValue("DrugBank", "provenance_source", iRow)
                     iRow += 1
 
             #
             return True
         except Exception as e:
             logger.exception("For %s failing with %s", catName, str(e))
         return False
@@ -943,22 +946,22 @@
                         for nm in dbMapD[ccId]["aliases"]:
                             wObj.setValue(ccId, "comp_id", iRow)
                             wObj.setValue(str(nm).strip(), "name", iRow)
                             wObj.setValue(iRow + 1, "ordinal", iRow)
                             wObj.setValue("DrugBank", "provenance_source", iRow)
                             wObj.setValue("Synonym", "type", iRow)
                             iRow += 1
-                    if "brand_names" in dbMapD[ccId]:
-                        iRow = wObj.getRowCount()
-                        for nm in dbMapD[ccId]["brand_names"]:
-                            wObj.setValue(ccId, "comp_id", iRow)
-                            wObj.setValue(str(nm).strip(), "name", iRow)
-                            wObj.setValue(iRow + 1, "ordinal", iRow)
-                            wObj.setValue("DrugBank", "provenance_source", iRow)
-                            wObj.setValue("Brand Name", "type", iRow)
-                            iRow += 1
+                    # if "brand_names" in dbMapD[ccId]:
+                    #     iRow = wObj.getRowCount()
+                    #     for nm in dbMapD[ccId]["brand_names"]:
+                    #         wObj.setValue(ccId, "comp_id", iRow)
+                    #         wObj.setValue(str(nm).strip(), "name", iRow)
+                    #         wObj.setValue(iRow + 1, "ordinal", iRow)
+                    #         wObj.setValue("DrugBank", "provenance_source", iRow)
+                    #         wObj.setValue("Brand Name", "type", iRow)
+                    #         iRow += 1
 
             return True
         except Exception as e:
             logger.exception("For %s failing with %s", catName, str(e))
 
         return False
```

### Comparing `rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodCommonUtils.py` & `rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodCommonUtils.py`

 * *Files identical despite different names*

### Comparing `rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodCompModelHelper.py` & `rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodCompModelHelper.py`

 * *Files 10% similar despite different names*

```diff
@@ -13,14 +13,16 @@
 #   17-May-2022   bv Add method 'addStructInfo'
 #   29-Jun-2022  dwp Update method 'buildCompModelProvenance' for populating rcsb_comp_model_provenance using mapping between internal and external IDs
 #    6-Jul-2022   bv RO-3357: Fix taxonomy assignment in addPolymerEntityTaxonomy
 #    6-Jul-2022  dwp Only populate rcsb_comp_model_provenance.source_url if it exists in CSM holdings file (may not exist for all AF fragments)
 #   26-Jan-2023  dwp Update method for populating entity_src_nat for cases where CSM already contains entity_src_nat;
 #                    No longer populate _struct.pdbx_structure_determination_methodology - was made internal to wwPDB
 #   20-Mar-2023  dwp Adjust formula weight calculation of polymer entities to use weights of amino acids as they exist in a linked polymer chains
+#   28-Mar-2023  dwp Add transient '_entity_src_nat.rcsb_provenance_source' attribute to use later for populating '_rcsb_entity_source_organism.provenance_source';
+#                    Update assignment of '_entity_src_nat.pdbx_src_id'
 ##
 """
 Helper class implements computed model method references in the RCSB dictionary extension.
 
 All data accessors and structures here refer to dictionary category and attribute names.
 
 """
@@ -141,14 +143,20 @@
         except Exception as e:
             logger.exception("Failing with %s", str(e))
         return False
 
     def addPolymerEntityTaxonomy(self, dataContainer, catName, **kwargs):
         """Add unassigned polymer entity-level taxonomy (if both _ma_target_ref_db_details.ncbi_taxonomy_id and .organism_scientific are present).
 
+        Also add transient '_entity_src_nat.rcsb_provenance_source' attribute here, to use later for populating '_rcsb_entity_source_organism.provenance_source'.
+
+        Note that there are two unique situations which are currently not handled by the current logic:
+          1. If an entry containing >1 entities has a entity_src_nat section, but only populates the metadata for one entity in CIF, then taxon data would be lost for the other entity
+          2. If an entry has gene_name information in _ma_target_ref_db_details, but also has entity_src_nat, then the gene_name information will not be propagated onto source_organism
+
         Args:
             dataContainer (object): mmif.api.DataContainer object instance
             catName (str): Category name
 
         Returns:
             bool: True for success or False otherwise
 
@@ -169,51 +177,81 @@
             "pdbx_organism_scientific",
             "nat_common_name",
             "pdbx_ncbi_taxonomy_id",
             "pdbx_src_id",
             "pdbx_beg_seq_num",
             "pdbx_end_seq_num",
             "rcsb_gene_name",
+            "rcsb_provenance_source",
         ]
         logger.debug("Starting with %r %r %r", dataContainer.getName(), catName, kwargs)
         try:
-            if not (dataContainer.exists("ma_data") and dataContainer.exists("ma_target_ref_db_details")):
+            if not dataContainer.exists("ma_data"):
+                return False
+            #
+            esnFullyPopulated = False
+            if dataContainer.exists("entity_src_nat"):  # If 'entity_src_nat' already exists, check to see how complete it is
+                sObj = dataContainer.getObj("entity_src_nat")
+                if all([ai in sObj.getAttributeList() for ai in ["pdbx_ncbi_taxonomy_id", "pdbx_organism_scientific"]]):
+                    if not sObj.hasAttribute("rcsb_provenance_source"):
+                        sObj.appendAttribute("rcsb_provenance_source")
+                    for ii in range(sObj.getRowCount()):
+                        if all(sObj.getValue(at, ii) and sObj.getValue(at, ii) not in [".", "?"] for at in ["pdbx_ncbi_taxonomy_id", "pdbx_organism_scientific"]):
+                            sObj.setValue("Primary Data", "rcsb_provenance_source", ii)
+                            esnFullyPopulated = True
+                        else:
+                            sObj.setValue(None, "rcsb_provenance_source", ii)
+            #
+            if esnFullyPopulated:  # Cases where entity_src_nat is already properly populated, in which case don't proceed with overwriting values below
+                return True
+            #
+            if not dataContainer.exists("ma_target_ref_db_details"):  # Case for models such as ma-coffe-slac
                 return False
+            #
             if not all([ai in dataContainer.getObj('ma_target_ref_db_details').getAttributeList() for ai in ["ncbi_taxonomy_id", "organism_scientific"]]):
                 return False
+            #
             geneName = None
-
+            #
             epLenD = self.__commonU.getPolymerEntityLengths(dataContainer)
             tObj = dataContainer.getObj("ma_target_ref_db_details")
             if not dataContainer.exists("entity_src_nat"):
                 dataContainer.append(DataCategory("entity_src_nat", attributeNameList=atL))
             else:
                 # append additional attributes to entity_src_nat if not already present
                 esnAttrL = dataContainer.getObj('entity_src_nat').getAttributeList()
                 for ai in atL:
                     if ai not in esnAttrL:
                         dataContainer.getObj('entity_src_nat').appendAttribute(ai)
             sObj = dataContainer.getObj("entity_src_nat")
             #
             jj = 0
-            for ii in range(tObj.getRowCount()):
+            dbSrcL = []
+            for ii in range(tObj.getRowCount()):  # This will only execute if 'ma_target_ref_db_details' exists
                 taxId = tObj.getValue("ncbi_taxonomy_id", ii)
                 orgName = tObj.getValue("organism_scientific", ii)
                 entityId = tObj.getValue("target_entity_id", ii)
                 geneName = tObj.getValueOrDefault("gene_name", ii, defaultValue=None)
                 dbName = tObj.getValue("db_name", ii)
                 #
-                if dbName == "UNP":
+                if dbName in ["UNP", "Other"]:
+                    if dbName not in dbSrcL:
+                        dbSrcL.append(dbName)
+                    srcId = str(dbSrcL.index(dbName) + 1)
                     sObj.setValue(entityId, "entity_id", jj)
                     sObj.setValue(taxId, "pdbx_ncbi_taxonomy_id", jj)
                     sObj.setValue(orgName, "pdbx_organism_scientific", jj)
-                    sObj.setValue("1", "pdbx_src_id", jj)
+                    sObj.setValue(srcId, "pdbx_src_id", jj)
                     sObj.setValue("1", "pdbx_beg_seq_num", jj)
                     sObj.setValue(str(epLenD[entityId]), "pdbx_end_seq_num", jj)
                     sObj.setValue(geneName, "rcsb_gene_name", jj)
+                    if dbName == "UNP":
+                        sObj.setValue("UniProt", "rcsb_provenance_source", jj)
+                    if dbName == "Other":
+                        sObj.setValue("NCBI", "rcsb_provenance_source", jj)
                     jj += 1
             #
             return True
         except Exception as e:
             logger.exception("Failing with %s", str(e))
         return False
```

### Comparing `rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodEntityHelper.py` & `rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodEntityHelper.py`

 * *Files 1% similar despite different names*

```diff
@@ -7,14 +7,15 @@
 #  29-Apr-2022 dwp Use internal computed-model identifiers for 'rcsb_id'
 #   3-May-2022 dwp Use internal computed-model identifiers for 'entry_id' in containter_identifiers
 #  23-Jun-2022 bv  Use ma_target_ref_db_details to populate rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers for MA models
 #  29-Jun-2022 dwp Use internal computed-model identifiers everywhere (in same manner as experimental models)
 #  21-Jul-2022 dwp Fix logic for assigning reference sequence identifiers for computed models
 #   6-Mar-2023 dwp Stop loading CARD data to rcsb_polymer_entity_feature
 #  14-Mar-2023 dwp Load CARD data to rcsb_polymer_entity_annotation
+#  28-Mar-2023 dwp Populate 'rcsb_entity_source_organism.provenance_source' with transient value from 'entity_src_nat.rcsb_provenance_source' (applicable to CSMs only)
 ##
 """
 Helper class implements methods supporting entity-level item and category methods in the RCSB dictionary extension.
 
 """
 __docformat__ = "google en"
 __author__ = "John Westbrook"
@@ -493,15 +494,15 @@
             _rcsb_entity_source_organism.ncbi_taxonomy_id
             _rcsb_entity_source_organism.provenance_source
             _rcsb_entity_source_organism.beg_seq_num
             _rcsb_entity_source_organism.end_seq_num
             _rcsb_entity_source_organism.taxonomy_lineage_id
             _rcsb_entity_source_organism.taxonomy_lineage_name
             _rcsb_entity_source_organism.taxonomy_lineage_depth
-            1 1 natural 'Homo sapiens' human 9606  'PDB Primary Data' 1 202 . . .
+            1 1 natural 'Homo sapiens' human 9606  'Primary Data' 1 202 . . .
             # ... abbreviated
 
 
             loop_
             _rcsb_entity_host_organism.entity_id
             _rcsb_entity_host_organism.pdbx_src_id
             _rcsb_entity_host_organism.scientific_name
@@ -509,15 +510,15 @@
             _rcsb_entity_host_organism.ncbi_taxonomy_id
             _rcsb_entity_host_organism.provenance_source
             _rcsb_entity_host_organism.beg_seq_num
             _rcsb_entity_host_organism.end_seq_num
             _rcsb_entity_host_organism.taxonomy_lineage_id
             _rcsb_entity_host_organism.taxonomy_lineage_name
             _rcsb_entity_host_organism.taxonomy_lineage_depth
-                        1 1 'Escherichia coli' 'E. coli' 562  'PDB Primary Data' 1 102 .  . .
+                        1 1 'Escherichia coli' 'E. coli' 562  'Primary Data' 1 102 .  . .
             # ... abbreviated
 
             And two related items -
 
             _entity.rcsb_multiple_source_flag
             _entity.rcsb_source_part_count
 
@@ -601,18 +602,19 @@
                 ("beg_seq_num", "beg_seq_num"),
                 ("end_seq_num", "end_seq_num"),
             ]
             at3SL, at3L = self.__getAttribList(s3Obj, at3TupL)
             #
             eObj = dataContainer.getObj("entity")
             entityIdL = eObj.getAttributeValueList("id")
+            #
             if isCompModel:
-                provSource = "UniProt"
-            else:
-                provSource = "PDB Primary Data"
+                provSource = None  # Initialize empty provSource for CSMs (will be retrieved on a per-entity basis below)
+            if not isCompModel:
+                provSource = "Primary Data"  # For all experimental entities, use this provSource
             #
             partCountD = {}
             srcL = []
             hostL = []
             for entityId in entityIdL:
                 partCountD[entityId] = 0
                 eL = []
@@ -667,14 +669,22 @@
                     tvL = self.__normalizeCsvToList(dataContainer.getName(), tv)
                     ii = atL.index("pdbx_src_id") if "pdbx_src_id" in atL else -1
                     for jj, row in enumerate(tvL, 1):
                         row[ii] = str(jj)
                     partCountD[entityId] = len(tvL)
                 else:
                     tvL = [tv]
+                # Get provSource corresopnding to current entityId (for CSMs only. Experimental entities are always "Primary Data")
+                if isCompModel and s2Obj.hasAttribute("rcsb_provenance_source"):
+                    provSource = None  # Initialize empty provSource (reset state between each entity loop)
+                    for kk in range(s2Obj.getRowCount()):
+                        if s2Obj.getValue("entity_id", kk) == entityId:
+                            provSource = s2Obj.getValue("rcsb_provenance_source", kk)
+                            if provSource and provSource not in [".", "?"]:
+                                break  # Break after finding the first non-empty entity_nat_src.provenance_source value
                 for v in tvL:
                     cObj.setValue(sType, "source_type", iRow)
                     cObj.setValue(provSource, "provenance_source", iRow)
                     for ii, at in enumerate(atL):
                         # add check for missing values here
                         if at in ["rcsb_gene_name_value"] and v[ii] and v[ii] not in [".", "?"]:
                             tgL = v[ii].split(",")
@@ -722,14 +732,22 @@
                     tvL = self.__normalizeCsvToList(dataContainer.getName(), tv)
                     ii = atL.index("pdbx_src_id") if "pdbx_src_id" in atL else -1
                     for jj, row in enumerate(tvL, 1):
                         row[ii] = str(jj)
                     # partCountD[entityId] = len(tvL)
                 else:
                     tvL = [tv]
+                # Get provSource corresopnding to current entityId (for CSMs only. Experimental entities are always "Primary Data")
+                if isCompModel and s2Obj.hasAttribute("rcsb_provenance_source"):
+                    provSource = None  # Initialize empty provSource (reset state between each entity loop)
+                    for kk in range(s2Obj.getRowCount()):
+                        if s2Obj.getValue("entity_id", kk) == entityId:
+                            provSource = s2Obj.getValue("rcsb_provenance_source", kk)
+                            if provSource and provSource not in [".", "?"]:
+                                break  # Break after finding the first non-empty entity_nat_src.provenance_source value
                 for v in tvL:
                     hObj.setValue(provSource, "provenance_source", iRow)
                     for ii, at in enumerate(atL):
                         hObj.setValue(v[ii], at, iRow)
                         #  if at == 'ncbi_taxonomy_id' and v[ii] and v[ii] not in ['.', '?'] and v[ii].isdigit():
                         if at == "ncbi_taxonomy_id" and v[ii] and v[ii] not in [".", "?"]:
                             taxId = int(self.__reNonDigit.sub("", v[ii]))
```

### Comparing `rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodEntityInstanceHelper.py` & `rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodEntityInstanceHelper.py`

 * *Files identical despite different names*

### Comparing `rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodEntryHelper.py` & `rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodEntryHelper.py`

 * *Files identical despite different names*

### Comparing `rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodResourceCacheWorkflow.py` & `rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodResourceCacheWorkflow.py`

 * *Files identical despite different names*

### Comparing `rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodResourceProvider.py` & `rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodResourceProvider.py`

 * *Files identical despite different names*

### Comparing `rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodRunner.py` & `rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodRunner.py`

 * *Files identical despite different names*

### Comparing `rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictMethodSecStructUtils.py` & `rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictMethodSecStructUtils.py`

 * *Files identical despite different names*

### Comparing `rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictionaryApiProvider.py` & `rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictionaryApiProvider.py`

 * *Files identical despite different names*

### Comparing `rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/DictionaryApiProviderWrapper.py` & `rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/DictionaryApiProviderWrapper.py`

 * *Files 2% similar despite different names*

```diff
@@ -79,11 +79,11 @@
             logger.error("Missing dictionary locator configuration for database schema %s", databaseName)
             dictLocators = []
         else:
             dictLocators = [self.__cfgOb.getPath(configLocator, sectionName=self.__configName) for configLocator in self.__dictLocatorMap[databaseName]]
             # Example dictLocators for databaseName 'pdbx_comp_model_core':
             #  ['https://raw.githubusercontent.com/rcsb/py-rcsb_exdb_assets/master/dictionary_files/reference/mmcif_pdbx_v5_next.dic',
             #   'https://raw.githubusercontent.com/rcsb/py-rcsb_exdb_assets/master/dictionary_files/dist/rcsb_mmcif_comp_model_ext.dic',
-            #   'https://raw.githubusercontent.com/rcsb/py-rcsb_exdb_assets/master/dictionary_files/reference/mmcif_ma.dic']
+            #   'https://raw.githubusercontent.com/rcsb/py-rcsb_exdb_assets/master/dictionary_files/reference/mmcif_ma_ext.dic']
         #
         logger.debug("Fetching dictionary API for %s using %r", databaseName, dictLocators)
         return self.__dP.getApi(dictLocators, **kwargs)
```

### Comparing `rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/NeighborInteractionProvider.py` & `rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/NeighborInteractionProvider.py`

 * *Files identical despite different names*

### Comparing `rcsb.utils.dictionary-1.7/rcsb/utils/dictionary/NeighborInteractionWorkflow.py` & `rcsb.utils.dictionary-1.8/rcsb/utils/dictionary/NeighborInteractionWorkflow.py`

 * *Files identical despite different names*

### Comparing `rcsb.utils.dictionary-1.7/rcsb.utils.dictionary.egg-info/PKG-INFO` & `rcsb.utils.dictionary-1.8/rcsb.utils.dictionary.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rcsb.utils.dictionary
-Version: 1.7
+Version: 1.8
 Summary: RCSB Python Dictionary Utility Classes
 Home-page: https://github.com/rcsb/py-rcsb_utils_dictionary
 Author: John Westbrook
 Author-email: john.westbrook@rcsb.org
 License: Apache 2.0
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
```

### Comparing `rcsb.utils.dictionary-1.7/rcsb.utils.dictionary.egg-info/SOURCES.txt` & `rcsb.utils.dictionary-1.8/rcsb.utils.dictionary.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `rcsb.utils.dictionary-1.7/setup.py` & `rcsb.utils.dictionary-1.8/setup.py`

 * *Files identical despite different names*

