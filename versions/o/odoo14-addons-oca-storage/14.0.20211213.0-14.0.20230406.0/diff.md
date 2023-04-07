# Comparing `tmp/odoo14_addons_oca_storage-14.0.20211213.0-py3-none-any.whl.zip` & `tmp/odoo14_addons_oca_storage-14.0.20230406.0-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,6 +1,6 @@
-Zip file size: 1415 bytes, number of entries: 4
--rw-r--r--  2.0 unx     1100 b- defN 21-Dec-14 05:10 odoo14_addons_oca_storage-14.0.20211213.0.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 21-Dec-14 05:10 odoo14_addons_oca_storage-14.0.20211213.0.dist-info/WHEEL
--rw-r--r--  2.0 unx        1 b- defN 21-Dec-14 05:10 odoo14_addons_oca_storage-14.0.20211213.0.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx      409 b- defN 21-Dec-14 05:10 odoo14_addons_oca_storage-14.0.20211213.0.dist-info/RECORD
-4 files, 1602 bytes uncompressed, 609 bytes compressed:  62.0%
+Zip file size: 1427 bytes, number of entries: 4
+-rw-r--r--  2.0 unx     1160 b- defN 23-Apr-07 08:02 odoo14_addons_oca_storage-14.0.20230406.0.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 23-Apr-07 08:02 odoo14_addons_oca_storage-14.0.20230406.0.dist-info/WHEEL
+-rw-r--r--  2.0 unx        1 b- defN 23-Apr-07 08:02 odoo14_addons_oca_storage-14.0.20230406.0.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx      409 b- defN 23-Apr-07 08:02 odoo14_addons_oca_storage-14.0.20230406.0.dist-info/RECORD
+4 files, 1662 bytes uncompressed, 621 bytes compressed:  62.6%
```

## zipnote {}

```diff
@@ -1,13 +1,13 @@
-Filename: odoo14_addons_oca_storage-14.0.20211213.0.dist-info/METADATA
+Filename: odoo14_addons_oca_storage-14.0.20230406.0.dist-info/METADATA
 Comment: 
 
-Filename: odoo14_addons_oca_storage-14.0.20211213.0.dist-info/WHEEL
+Filename: odoo14_addons_oca_storage-14.0.20230406.0.dist-info/WHEEL
 Comment: 
 
-Filename: odoo14_addons_oca_storage-14.0.20211213.0.dist-info/top_level.txt
+Filename: odoo14_addons_oca_storage-14.0.20230406.0.dist-info/top_level.txt
 Comment: 
 
-Filename: odoo14_addons_oca_storage-14.0.20211213.0.dist-info/RECORD
+Filename: odoo14_addons_oca_storage-14.0.20230406.0.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## Comparing `odoo14_addons_oca_storage-14.0.20211213.0.dist-info/METADATA` & `odoo14_addons_oca_storage-14.0.20230406.0.dist-info/METADATA`

 * *Files 27% similar despite different names*

```diff
@@ -1,23 +1,24 @@
 Metadata-Version: 2.1
 Name: odoo14-addons-oca-storage
-Version: 14.0.20211213.0
+Version: 14.0.20230406.0
 Summary: Meta package for oca-storage Odoo addons
 Home-page: UNKNOWN
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python
 Classifier: Framework :: Odoo
 Classifier: Framework :: Odoo :: 14.0
 Requires-Dist: odoo14-addon-storage-backend
 Requires-Dist: odoo14-addon-storage-backend-ftp
 Requires-Dist: odoo14-addon-storage-backend-s3
 Requires-Dist: odoo14-addon-storage-backend-sftp
 Requires-Dist: odoo14-addon-storage-file
 Requires-Dist: odoo14-addon-storage-image
+Requires-Dist: odoo14-addon-storage-image-backend-migration
 Requires-Dist: odoo14-addon-storage-image-import
 Requires-Dist: odoo14-addon-storage-image-product
 Requires-Dist: odoo14-addon-storage-image-product-brand
 Requires-Dist: odoo14-addon-storage-image-product-brand-import
 Requires-Dist: odoo14-addon-storage-image-product-import
 Requires-Dist: odoo14-addon-storage-image-product-pos
 Requires-Dist: odoo14-addon-storage-import-image-advanced
```

