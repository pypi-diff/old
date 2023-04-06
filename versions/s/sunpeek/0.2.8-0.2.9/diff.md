# Comparing `tmp/sunpeek-0.2.8-py3-none-any.whl.zip` & `tmp/sunpeek-0.2.9-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -10,15 +10,15 @@
 -rw-r--r--  2.0 unx     2782 b- defN 80-Jan-01 00:00 sunpeek/api/routers/files.py
 -rw-r--r--  2.0 unx    13410 b- defN 80-Jan-01 00:00 sunpeek/api/routers/plant.py
 -rw-r--r--  2.0 unx      780 b- defN 80-Jan-01 00:00 sunpeek/base_model.py
 -rw-r--r--  2.0 unx      150 b- defN 80-Jan-01 00:00 sunpeek/common/__init__.py
 -rw-r--r--  2.0 unx     1248 b- defN 80-Jan-01 00:00 sunpeek/common/common_units.py
 -rw-r--r--  2.0 unx     1446 b- defN 80-Jan-01 00:00 sunpeek/common/config_parser.py
 -rw-r--r--  2.0 unx    19464 b- defN 80-Jan-01 00:00 sunpeek/common/context.py
--rw-r--r--  2.0 unx    17450 b- defN 80-Jan-01 00:00 sunpeek/common/data_uploader.py
+-rw-r--r--  2.0 unx    17482 b- defN 80-Jan-01 00:00 sunpeek/common/data_uploader.py
 -rw-r--r--  2.0 unx     1056 b- defN 80-Jan-01 00:00 sunpeek/common/errors.py
 -rw-r--r--  2.0 unx    17621 b- defN 80-Jan-01 00:00 sunpeek/common/unit_uncertainty.py
 -rw-r--r--  2.0 unx     6119 b- defN 80-Jan-01 00:00 sunpeek/common/utils.py
 -rw-r--r--  2.0 unx      960 b- defN 80-Jan-01 00:00 sunpeek/components/__init__.py
 -rw-r--r--  2.0 unx    12272 b- defN 80-Jan-01 00:00 sunpeek/components/base.py
 -rw-r--r--  2.0 unx     2763 b- defN 80-Jan-01 00:00 sunpeek/components/components_factories.py
 -rw-r--r--  2.0 unx    15276 b- defN 80-Jan-01 00:00 sunpeek/components/fluid_helpers.py
@@ -53,13 +53,13 @@
 -rw-r--r--  2.0 unx      241 b- defN 80-Jan-01 00:00 sunpeek/definitions/raw_data/FHW, Pekasolar/Pekasolar, pdf export, heat capacity.csv
 -rw-r--r--  2.0 unx      993 b- defN 80-Jan-01 00:00 sunpeek/definitions/raw_data/FHW, Pekasolar/Pekasolar, pdf export, heat capacity.onnxbytes
 -rw-r--r--  2.0 unx      528 b- defN 80-Jan-01 00:00 sunpeek/demo/__init__.py
 -rw-r--r--  2.0 unx     1371 b- defN 80-Jan-01 00:00 sunpeek/demo/demo_plant.py
 -rw-r--r--  2.0 unx     4894 b- defN 80-Jan-01 00:00 sunpeek/demo/demo_plant_script.py
 -rw-r--r--  2.0 unx     2836 b- defN 80-Jan-01 00:00 sunpeek/exporter.py
 -rw-r--r--  2.0 unx    14227 b- defN 80-Jan-01 00:00 sunpeek/serializable_models.py
--rw-r--r--  2.0 unx     7652 b- defN 80-Jan-01 00:00 sunpeek-0.2.8.dist-info/COPYING.LESSER
--rw-r--r--  2.0 unx    16989 b- defN 80-Jan-01 00:00 sunpeek-0.2.8.dist-info/METADATA
--rw-r--r--  2.0 unx       88 b- defN 80-Jan-01 00:00 sunpeek-0.2.8.dist-info/WHEEL
--rw-r--r--  2.0 unx    35149 b- defN 80-Jan-01 00:00 sunpeek-0.2.8.dist-info/COPYING
-?rw-r--r--  2.0 unx     5713 b- defN 16-Jan-01 00:00 sunpeek-0.2.8.dist-info/RECORD
-63 files, 586687 bytes uncompressed, 151636 bytes compressed:  74.2%
+-rw-r--r--  2.0 unx     7652 b- defN 80-Jan-01 00:00 sunpeek-0.2.9.dist-info/COPYING.LESSER
+-rw-r--r--  2.0 unx    16989 b- defN 80-Jan-01 00:00 sunpeek-0.2.9.dist-info/METADATA
+-rw-r--r--  2.0 unx       88 b- defN 80-Jan-01 00:00 sunpeek-0.2.9.dist-info/WHEEL
+-rw-r--r--  2.0 unx    35149 b- defN 80-Jan-01 00:00 sunpeek-0.2.9.dist-info/COPYING
+?rw-r--r--  2.0 unx     5713 b- defN 16-Jan-01 00:00 sunpeek-0.2.9.dist-info/RECORD
+63 files, 586719 bytes uncompressed, 151636 bytes compressed:  74.2%
```

## zipnote {}

```diff
@@ -168,23 +168,23 @@
 
 Filename: sunpeek/exporter.py
 Comment: 
 
 Filename: sunpeek/serializable_models.py
 Comment: 
 
-Filename: sunpeek-0.2.8.dist-info/COPYING.LESSER
+Filename: sunpeek-0.2.9.dist-info/COPYING.LESSER
 Comment: 
 
-Filename: sunpeek-0.2.8.dist-info/METADATA
+Filename: sunpeek-0.2.9.dist-info/METADATA
 Comment: 
 
-Filename: sunpeek-0.2.8.dist-info/WHEEL
+Filename: sunpeek-0.2.9.dist-info/WHEEL
 Comment: 
 
-Filename: sunpeek-0.2.8.dist-info/COPYING
+Filename: sunpeek-0.2.9.dist-info/COPYING
 Comment: 
 
-Filename: sunpeek-0.2.8.dist-info/RECORD
+Filename: sunpeek-0.2.9.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## sunpeek/common/data_uploader.py

```diff
@@ -353,17 +353,17 @@
     def _create_raw_data_table(self):
         """Creates raw data table if it does not exists in the database.
         """
         # Create database inferring runtime types
         try:
             types_dict = {DATETIME_COL_NAME: datetime.datetime}
             for sensor in self.plant.raw_sensors:
-                if sensor.sensor_type.name == 'bool':
+                if getattr(sensor.sensor_type, 'name', '') == 'bool':
                     types_dict[sensor.raw_name] = bool
-                elif sensor.sensor_type.compatible_unit_str == 'str':
+                elif getattr(sensor.sensor_type, 'compatible_unit_str', '') == 'str':
                     types_dict[sensor.raw_name] = str
                 else:
                     types_dict[sensor.raw_name] = float
 
             hit_db.create_table_dynamic(self.session.get_bind(), self.table_name, types_dict)
             self.output.db_response['new_table_created'] = True
             self.output.db_response['new_table_name'] = self.table_name
```

## Comparing `sunpeek-0.2.8.dist-info/COPYING.LESSER` & `sunpeek-0.2.9.dist-info/COPYING.LESSER`

 * *Files identical despite different names*

## Comparing `sunpeek-0.2.8.dist-info/METADATA` & `sunpeek-0.2.9.dist-info/METADATA`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sunpeek
-Version: 0.2.8
+Version: 0.2.9
 Summary: Large Solar Thermal Monitoring Tool. Implements the Performance Check Method of ISO 24194
 Home-page: https://gitlab.com/sunpeek/sunpeek
 License: LGPL-3.0-only
 Keywords: solarthermal,solar,energy,monitoring
 Author: Philip Ohnewein, Daniel Tschopp, Lukas Feierl, Marnoch Hamilton-Jones, Jonathan Cazco
 Maintainer: Marnoch Hamilton-Jones
 Maintainer-email: m.hamilton-jones@aee.at
```

## Comparing `sunpeek-0.2.8.dist-info/COPYING` & `sunpeek-0.2.9.dist-info/COPYING`

 * *Files identical despite different names*

## Comparing `sunpeek-0.2.8.dist-info/RECORD` & `sunpeek-0.2.9.dist-info/RECORD`

 * *Files 2% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 sunpeek/api/routers/files.py,sha256=kPrPUvQQRFG-aXu8oTYRvmK3yDwOHNGhQ3j19xv8yTQ,2782
 sunpeek/api/routers/plant.py,sha256=wxBPCgfcl4xfll61Ky12aXBec8vShubHGe5O83lbmXw,13410
 sunpeek/base_model.py,sha256=v3tIRStkycYr5uYReaQ7VDztTRFw0Js6j9hNtUDGUyc,780
 sunpeek/common/__init__.py,sha256=F-tVAK0f825j6YF2s2VymVDW37QVf1l_YwfGuD4AbgA,150
 sunpeek/common/common_units.py,sha256=DPykzkJEX8oGql7iw6ZK6kiI5rsoIHrR3KCXydqPbRc,1248
 sunpeek/common/config_parser.py,sha256=K333ki5NsweVTEn3M3n8iA1887tHSVzQxABgBjy4KNk,1446
 sunpeek/common/context.py,sha256=FEMY6BRd2NOKIS98-t_PcY406jy4UL7Tm9nteKoKrAs,19464
-sunpeek/common/data_uploader.py,sha256=bt9yYn-WuOIAXxyV2KbK9PnBr84lzqzMXn9LQ5PzfnU,17450
+sunpeek/common/data_uploader.py,sha256=th9sHn89N5PJo5plYUOfWjkWa1t67sAlNNVg_m-_mhM,17482
 sunpeek/common/errors.py,sha256=USCDD1EINZebhx-5n_dEK_JVzNl9GlgrjiHLv0CQFYA,1056
 sunpeek/common/unit_uncertainty.py,sha256=dSJUBRm8eQ2cC_KsL8e8OreDctiZiHfizQBXHRyywX4,17621
 sunpeek/common/utils.py,sha256=fYtfHvZqK9kxLCaBbMaQzFtg4cFj4IwxB51366hiTmg,6119
 sunpeek/components/__init__.py,sha256=_Jjf_EKQviEy0pwQQHLwdsf2jM07RdOEEls1rDWDK9A,960
 sunpeek/components/base.py,sha256=TBuDGzaemZuoOeG0ayHpd4-VwFjbD61SCYMPI03FiIM,12272
 sunpeek/components/components_factories.py,sha256=eyJJPYt-W7VdWuOtx1Ii11JZWnempLuFY1gKsrzD97c,2763
 sunpeek/components/fluid_helpers.py,sha256=sr2qkk-vv4xsxIPuQhxAku7aJcOOoqlinNAVV3X87ok,15276
@@ -52,12 +52,12 @@
 "sunpeek/definitions/raw_data/FHW, Pekasolar/Pekasolar, pdf export, heat capacity.csv",sha256=uVb9p15EsbH1Ule1VAoQfT_C1du8NP0q1YhmOMGB-lM,241
 "sunpeek/definitions/raw_data/FHW, Pekasolar/Pekasolar, pdf export, heat capacity.onnxbytes",sha256=YS5luTplfWulcE8PtHtodKcKBwjPtKCIPM16jRDydHs,993
 sunpeek/demo/__init__.py,sha256=djMLgvrYODa5bcBr2KnbPZ37s1yO_3igMAEYNXp_iPQ,528
 sunpeek/demo/demo_plant.py,sha256=DZCVSzFBOL1M3Zu6S6P0vnaTt4HvvTZgbj83MUpcaTo,1371
 sunpeek/demo/demo_plant_script.py,sha256=VIqwhCMpeFLG_VUpqVpFdSsSyuNsSww8ZsoP0ve6Lo4,4894
 sunpeek/exporter.py,sha256=z0_-ZylxNcWi-ZYYu1xByp9fDEHbJ7I6zcaAF5oYpy4,2836
 sunpeek/serializable_models.py,sha256=uKRIa6i7wLMWb9pf1svG6dJMWE4VX_PQiMnvvklEnwc,14227
-sunpeek-0.2.8.dist-info/COPYING.LESSER,sha256=46mU2C5kSwOnkqkw9XQAJlhBL2JAf1_uCD8lVcXyMRg,7652
-sunpeek-0.2.8.dist-info/METADATA,sha256=9z0RBJZ75LaW_yVBTtGTnXN3NkrqcKoKHMhJkp9h6lg,16989
-sunpeek-0.2.8.dist-info/WHEEL,sha256=vVCvjcmxuUltf8cYhJ0sJMRDLr1XsPuxEId8YDzbyCY,88
-sunpeek-0.2.8.dist-info/COPYING,sha256=OXLcl0T2SZ8Pmy2_dmlvKuetivmyPd5m1q-Gyd-zaYY,35149
-sunpeek-0.2.8.dist-info/RECORD,,
+sunpeek-0.2.9.dist-info/COPYING.LESSER,sha256=46mU2C5kSwOnkqkw9XQAJlhBL2JAf1_uCD8lVcXyMRg,7652
+sunpeek-0.2.9.dist-info/METADATA,sha256=HOII11VzvpOuBSQk939Wa7RoQprU6etD4wGH_q1SluI,16989
+sunpeek-0.2.9.dist-info/WHEEL,sha256=vVCvjcmxuUltf8cYhJ0sJMRDLr1XsPuxEId8YDzbyCY,88
+sunpeek-0.2.9.dist-info/COPYING,sha256=OXLcl0T2SZ8Pmy2_dmlvKuetivmyPd5m1q-Gyd-zaYY,35149
+sunpeek-0.2.9.dist-info/RECORD,,
```

