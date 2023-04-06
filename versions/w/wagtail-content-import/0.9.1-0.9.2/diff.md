# Comparing `tmp/wagtail_content_import-0.9.1-py3-none-any.whl.zip` & `tmp/wagtail_content_import-0.9.2-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,18 +1,18 @@
-Zip file size: 38728 bytes, number of entries: 58
+Zip file size: 38911 bytes, number of entries: 58
 -rw-rw-r--  2.0 unx      104 b- defN 22-May-17 11:09 wagtail_content_import/__init__.py
 -rw-rw-r--  2.0 unx      268 b- defN 22-May-17 11:09 wagtail_content_import/admin_views.py
 -rw-rw-r--  2.0 unx      201 b- defN 22-May-17 11:09 wagtail_content_import/apps.py
 -rw-rw-r--  2.0 unx      774 b- defN 22-May-17 11:09 wagtail_content_import/models.py
 -rw-rw-r--  2.0 unx      195 b- defN 22-May-19 13:12 wagtail_content_import/urls.py
 -rw-rw-r--  2.0 unx     1255 b- defN 23-Feb-17 16:48 wagtail_content_import/utils.py
 -rw-rw-r--  2.0 unx     1024 b- defN 23-Feb-17 16:59 wagtail_content_import/wagtail_hooks.py
 -rw-rw-r--  2.0 unx      669 b- defN 22-May-17 11:09 wagtail_content_import/mappers/__init__.py
 -rw-rw-r--  2.0 unx      217 b- defN 22-May-17 11:09 wagtail_content_import/mappers/base.py
--rw-rw-r--  2.0 unx     6602 b- defN 23-Apr-06 13:01 wagtail_content_import/mappers/converters.py
+-rw-rw-r--  2.0 unx     6941 b- defN 23-Apr-06 13:03 wagtail_content_import/mappers/converters.py
 -rw-rw-r--  2.0 unx      717 b- defN 22-May-17 11:09 wagtail_content_import/mappers/streamfield.py
 -rw-rw-r--  2.0 unx     6321 b- defN 23-Feb-17 16:59 wagtail_content_import/mappers/tests.py
 -rw-rw-r--  2.0 unx     1135 b- defN 22-May-17 11:09 wagtail_content_import/migrations/0001_initial.py
 -rw-rw-r--  2.0 unx      364 b- defN 22-May-17 11:09 wagtail_content_import/migrations/0002_auto_20191009_1435.py
 -rw-rw-r--  2.0 unx        0 b- defN 22-May-17 11:09 wagtail_content_import/migrations/__init__.py
 -rw-rw-r--  2.0 unx     1235 b- defN 22-May-17 11:09 wagtail_content_import/parsers/__init__.py
 -rw-rw-r--  2.0 unx      115 b- defN 22-May-17 11:09 wagtail_content_import/parsers/base.py
@@ -49,12 +49,12 @@
 -rw-rw-r--  2.0 unx     1745 b- defN 22-May-17 11:09 wagtail_content_import/templates/wagtail_content_import/picker_buttons_base.html
 -rw-rw-r--  2.0 unx      319 b- defN 22-May-17 11:09 wagtail_content_import/templates/wagtail_content_import/picker_buttons_create.html
 -rw-rw-r--  2.0 unx      453 b- defN 22-May-17 11:09 wagtail_content_import/templates/wagtail_content_import/picker_buttons_edit.html
 -rw-rw-r--  2.0 unx      376 b- defN 22-May-17 11:09 wagtail_content_import/templates/wagtailadmin/pages/create.html
 -rw-rw-r--  2.0 unx      372 b- defN 22-May-17 11:09 wagtail_content_import/templates/wagtailadmin/pages/edit.html
 -rw-rw-r--  2.0 unx        0 b- defN 22-May-17 11:09 wagtail_content_import/templatetags/__init__.py
 -rw-rw-r--  2.0 unx     1350 b- defN 23-Feb-17 16:59 wagtail_content_import/templatetags/wagtailcontentimport_tags.py
--rw-rw-r--  2.0 unx     2647 b- defN 23-Apr-06 13:02 wagtail_content_import-0.9.1.dist-info/METADATA
--rw-rw-r--  2.0 unx       92 b- defN 23-Apr-06 13:02 wagtail_content_import-0.9.1.dist-info/WHEEL
--rw-rw-r--  2.0 unx       23 b- defN 23-Apr-06 13:02 wagtail_content_import-0.9.1.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     6353 b- defN 23-Apr-06 13:02 wagtail_content_import-0.9.1.dist-info/RECORD
-58 files, 96981 bytes uncompressed, 28012 bytes compressed:  71.1%
+-rw-rw-r--  2.0 unx     2647 b- defN 23-Apr-06 13:04 wagtail_content_import-0.9.2.dist-info/METADATA
+-rw-rw-r--  2.0 unx       92 b- defN 23-Apr-06 13:04 wagtail_content_import-0.9.2.dist-info/WHEEL
+-rw-rw-r--  2.0 unx       23 b- defN 23-Apr-06 13:04 wagtail_content_import-0.9.2.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     6353 b- defN 23-Apr-06 13:04 wagtail_content_import-0.9.2.dist-info/RECORD
+58 files, 97320 bytes uncompressed, 28195 bytes compressed:  71.0%
```

## zipnote {}

```diff
@@ -156,20 +156,20 @@
 
 Filename: wagtail_content_import/templatetags/__init__.py
 Comment: 
 
 Filename: wagtail_content_import/templatetags/wagtailcontentimport_tags.py
 Comment: 
 
-Filename: wagtail_content_import-0.9.1.dist-info/METADATA
+Filename: wagtail_content_import-0.9.2.dist-info/METADATA
 Comment: 
 
-Filename: wagtail_content_import-0.9.1.dist-info/WHEEL
+Filename: wagtail_content_import-0.9.2.dist-info/WHEEL
 Comment: 
 
-Filename: wagtail_content_import-0.9.1.dist-info/top_level.txt
+Filename: wagtail_content_import-0.9.2.dist-info/top_level.txt
 Comment: 
 
-Filename: wagtail_content_import-0.9.1.dist-info/RECORD
+Filename: wagtail_content_import-0.9.2.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## wagtail_content_import/mappers/converters.py

```diff
@@ -134,15 +134,21 @@
         image = Image(title=title, uploaded_by_user=owner)
         image.file = ContentFile(content, name=name)
         # Set image file size
         image.file_size = image.file.size
 
         # Set image file hash
         image.file.seek(0)
-        image._set_file_hash(image.file.read())
+        try:
+            image._set_file_hash(image.file.read())
+        except TypeError:
+            # This argumentless version was introduced in Wagtail 4.2.2
+            # https://github.com/wagtail/wagtail/commit/3c0c64642b9e5b8d28b111263c7f4bddad6c3880
+            # we can probably drop this try/except pattern when it's in a new major version
+            image._set_file_hash()
         image.file.seek(0)
 
         # Before we save the image, let's check if there are any choosable images with the same hash
         # so we can avoid importing a duplicate
 
         from wagtail.images.permissions import permission_policy
```

## Comparing `wagtail_content_import-0.9.1.dist-info/METADATA` & `wagtail_content_import-0.9.2.dist-info/METADATA`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: wagtail-content-import
-Version: 0.9.1
+Version: 0.9.2
 Summary: A module for Wagtail that provides functionality for importing page content from third-party sources.
 Home-page: https://github.com/torchbox/wagtail-content-import
 Author: Samir Shah, Jacob Topp-Mugglestone, Karl Hobley, Matthew Westcott
 Author-email: jacobtm@torchbox.com
 License: BSD
 Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
```

## Comparing `wagtail_content_import-0.9.1.dist-info/RECORD` & `wagtail_content_import-0.9.2.dist-info/RECORD`

 * *Files 4% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 wagtail_content_import/apps.py,sha256=U_N8kNFjyT2cOfE88y3rYb81TrtVr_UeOkfDdOUve_s,201
 wagtail_content_import/models.py,sha256=fs6DBHA4p9fBftv_wdgvZHnlJs043wL-2O3nDYAk8TE,774
 wagtail_content_import/urls.py,sha256=PYiBf6N1YGCEHVnSTJb0XSXHo2QJSw-uauAELGSANmU,195
 wagtail_content_import/utils.py,sha256=FMVDtKA7-Uvx4mhA9anzF-QQs_XG0HHRlIUrsEdAFHg,1255
 wagtail_content_import/wagtail_hooks.py,sha256=wxl3W_JWxsN6EgPpxXCFS1OCu0biRzZBotr0iAqDVL0,1024
 wagtail_content_import/mappers/__init__.py,sha256=ZsMJtJgER-Xct9Y7xdyYfEs4ejgSdd6yVjoHDRUvm5s,669
 wagtail_content_import/mappers/base.py,sha256=xGvs9lKHDz3f4VhA4hwDzIBE4biXRlkBZb-OgjS_sc4,217
-wagtail_content_import/mappers/converters.py,sha256=T2IZ42046b1EVR5fiFrMcUbcmiOWTXnSgxUPn4vgQOs,6602
+wagtail_content_import/mappers/converters.py,sha256=q-XqH20wX516Gr968ee-mn4dRxh1XhDz5l7w8Cvxk_0,6941
 wagtail_content_import/mappers/streamfield.py,sha256=BcNkwvOSuZkF4RJOjs0mvrtsbXN3KE7B1T_J3q1Rj74,717
 wagtail_content_import/mappers/tests.py,sha256=QH6Dmqp8mZFPZcfDXNCIwNIt_4uVE4Q6BL_xlreI5LM,6321
 wagtail_content_import/migrations/0001_initial.py,sha256=tuWpY1YlvWwEHNCYz8UYqmVj0QR1ZM_8vZZFiWT1kfg,1135
 wagtail_content_import/migrations/0002_auto_20191009_1435.py,sha256=hvGDVy1nLC5jNHNO1iqQlGAD9Vbi7Ic_G7f3LJb51_M,364
 wagtail_content_import/migrations/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 wagtail_content_import/parsers/__init__.py,sha256=Jd_GshKcWeuux_D0RA4nkIx3GEsXZpbbzohCRrzDooU,1235
 wagtail_content_import/parsers/base.py,sha256=DwFeIaxvT953QpkJjjI6WzPdlyIbC_7ipU1VTybsU8c,115
@@ -48,11 +48,11 @@
 wagtail_content_import/templates/wagtail_content_import/picker_buttons_base.html,sha256=8-fcxcK2i-n70KjbIBBXfrE-nZAzJ5AeD13355anaa8,1745
 wagtail_content_import/templates/wagtail_content_import/picker_buttons_create.html,sha256=3wJqsTbx6C6C9aerZDsAqNA7HcaIthD-BZVVgd2qVFw,319
 wagtail_content_import/templates/wagtail_content_import/picker_buttons_edit.html,sha256=4xK4odUmM1huvyoFfPG4SGbxN8DuNwVKsfqgC3Y1p0U,453
 wagtail_content_import/templates/wagtailadmin/pages/create.html,sha256=dnC0WdtaxXNQGiUdRK-mwjy7xN9qbmLEfv5JAzA7bfo,376
 wagtail_content_import/templates/wagtailadmin/pages/edit.html,sha256=fsiyXrlOu66aTkNSKX6iSLK2R3yP4W0PUCUKryA_lCA,372
 wagtail_content_import/templatetags/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 wagtail_content_import/templatetags/wagtailcontentimport_tags.py,sha256=PSqtLAsdlWFNFuYw2flAYn2gxErt5mI97IvHgT7JR98,1350
-wagtail_content_import-0.9.1.dist-info/METADATA,sha256=WBZwnCKNGkN3HARF2AnqF7g2KQPc19G7VXxfJCMk6Qc,2647
-wagtail_content_import-0.9.1.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
-wagtail_content_import-0.9.1.dist-info/top_level.txt,sha256=AFq84z2Btt4jLA4jYEpt0d_b4suv53UvEmrCb5HqBxY,23
-wagtail_content_import-0.9.1.dist-info/RECORD,,
+wagtail_content_import-0.9.2.dist-info/METADATA,sha256=YtsyzHnQdIRyOc0ECgZN42yrSCO3EG1UwA1CJucpyKo,2647
+wagtail_content_import-0.9.2.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
+wagtail_content_import-0.9.2.dist-info/top_level.txt,sha256=AFq84z2Btt4jLA4jYEpt0d_b4suv53UvEmrCb5HqBxY,23
+wagtail_content_import-0.9.2.dist-info/RECORD,,
```

