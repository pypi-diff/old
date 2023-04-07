# Comparing `tmp/odoo_addons_oca_purchase_workflow-16.0.20230318.0-py3-none-any.whl.zip` & `tmp/odoo_addons_oca_purchase_workflow-16.0.20230323.3-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,6 +1,6 @@
-Zip file size: 1571 bytes, number of entries: 4
--rw-r--r--  2.0 unx     1340 b- defN 23-Mar-20 07:11 odoo_addons_oca_purchase_workflow-16.0.20230318.0.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 23-Mar-20 07:11 odoo_addons_oca_purchase_workflow-16.0.20230318.0.dist-info/WHEEL
--rw-r--r--  2.0 unx        1 b- defN 23-Mar-20 07:11 odoo_addons_oca_purchase_workflow-16.0.20230318.0.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx      441 b- defN 23-Mar-20 07:11 odoo_addons_oca_purchase_workflow-16.0.20230318.0.dist-info/RECORD
-4 files, 1874 bytes uncompressed, 701 bytes compressed:  62.6%
+Zip file size: 1606 bytes, number of entries: 4
+-rw-r--r--  2.0 unx     1629 b- defN 23-Mar-24 07:33 odoo_addons_oca_purchase_workflow-16.0.20230323.3.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 23-Mar-24 07:33 odoo_addons_oca_purchase_workflow-16.0.20230323.3.dist-info/WHEEL
+-rw-r--r--  2.0 unx        1 b- defN 23-Mar-24 07:33 odoo_addons_oca_purchase_workflow-16.0.20230323.3.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx      441 b- defN 23-Mar-24 07:33 odoo_addons_oca_purchase_workflow-16.0.20230323.3.dist-info/RECORD
+4 files, 2163 bytes uncompressed, 736 bytes compressed:  66.0%
```

## zipnote {}

```diff
@@ -1,13 +1,13 @@
-Filename: odoo_addons_oca_purchase_workflow-16.0.20230318.0.dist-info/METADATA
+Filename: odoo_addons_oca_purchase_workflow-16.0.20230323.3.dist-info/METADATA
 Comment: 
 
-Filename: odoo_addons_oca_purchase_workflow-16.0.20230318.0.dist-info/WHEEL
+Filename: odoo_addons_oca_purchase_workflow-16.0.20230323.3.dist-info/WHEEL
 Comment: 
 
-Filename: odoo_addons_oca_purchase_workflow-16.0.20230318.0.dist-info/top_level.txt
+Filename: odoo_addons_oca_purchase_workflow-16.0.20230323.3.dist-info/top_level.txt
 Comment: 
 
-Filename: odoo_addons_oca_purchase_workflow-16.0.20230318.0.dist-info/RECORD
+Filename: odoo_addons_oca_purchase_workflow-16.0.20230323.3.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## Comparing `odoo_addons_oca_purchase_workflow-16.0.20230318.0.dist-info/METADATA` & `odoo_addons_oca_purchase_workflow-16.0.20230323.3.dist-info/METADATA`

 * *Files 15% similar despite different names*

```diff
@@ -1,27 +1,31 @@
 Metadata-Version: 2.1
 Name: odoo-addons-oca-purchase-workflow
-Version: 16.0.20230318.0
+Version: 16.0.20230323.3
 Summary: Meta package for oca-purchase-workflow Odoo addons
 Home-page: UNKNOWN
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python
 Classifier: Framework :: Odoo
 Classifier: Framework :: Odoo :: 16.0
 Requires-Dist: odoo-addon-purchase-advance-payment (<16.1dev,>=16.0dev)
+Requires-Dist: odoo-addon-purchase-all-shipments (<16.1dev,>=16.0dev)
 Requires-Dist: odoo-addon-purchase-allowed-product (<16.1dev,>=16.0dev)
 Requires-Dist: odoo-addon-purchase-commercial-partner (<16.1dev,>=16.0dev)
+Requires-Dist: odoo-addon-purchase-default-terms-conditions (<16.1dev,>=16.0dev)
 Requires-Dist: odoo-addon-purchase-delivery-split-date (<16.1dev,>=16.0dev)
 Requires-Dist: odoo-addon-purchase-discount (<16.1dev,>=16.0dev)
+Requires-Dist: odoo-addon-purchase-exception (<16.1dev,>=16.0dev)
 Requires-Dist: odoo-addon-purchase-force-invoiced (<16.1dev,>=16.0dev)
 Requires-Dist: odoo-addon-purchase-last-price-info (<16.1dev,>=16.0dev)
 Requires-Dist: odoo-addon-purchase-order-approved (<16.1dev,>=16.0dev)
 Requires-Dist: odoo-addon-purchase-order-line-menu (<16.1dev,>=16.0dev)
 Requires-Dist: odoo-addon-purchase-request (<16.1dev,>=16.0dev)
 Requires-Dist: odoo-addon-purchase-request-tier-validation (<16.1dev,>=16.0dev)
 Requires-Dist: odoo-addon-purchase-requisition-tier-validation (<16.1dev,>=16.0dev)
 Requires-Dist: odoo-addon-purchase-stock-packaging (<16.1dev,>=16.0dev)
 Requires-Dist: odoo-addon-purchase-tier-validation (<16.1dev,>=16.0dev)
+Requires-Dist: odoo-addon-purchase-triple-discount (<16.1dev,>=16.0dev)
 
 UNKNOWN
```

