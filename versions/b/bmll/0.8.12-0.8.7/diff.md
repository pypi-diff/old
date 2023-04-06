# Comparing `tmp/bmll-0.8.12-py3-none-any.whl.zip` & `tmp/bmll-0.8.7-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,16 +1,16 @@
-Zip file size: 16255 bytes, number of entries: 14
--rw-r--r--  2.0 unx     1821 b- defN 21-Feb-09 15:33 bmll/__init__.py
--rw-r--r--  2.0 unx     1493 b- defN 21-Feb-09 15:33 bmll/_cli.py
--rw-rw-r--  2.0 unx      244 b- defN 21-Feb-09 15:33 bmll/_metadata.json
--rw-r--r--  2.0 unx    10326 b- defN 21-Feb-09 15:33 bmll/_rest.py
--rw-r--r--  2.0 unx     1033 b- defN 21-Feb-09 15:33 bmll/_utils.py
--rw-r--r--  2.0 unx      217 b- defN 21-Feb-09 15:33 bmll/exceptions.py
--rw-r--r--  2.0 unx     5593 b- defN 21-Feb-09 15:33 bmll/reference.py
--rw-r--r--  2.0 unx     6787 b- defN 21-Feb-09 15:33 bmll/time_series.py
--rw-rw-r--  2.0 unx    11358 b- defN 21-Feb-09 15:42 bmll-0.8.12.dist-info/LICENSE-2.0.txt
--rw-r--r--  2.0 unx     1548 b- defN 21-Feb-09 15:42 bmll-0.8.12.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 21-Feb-09 15:42 bmll-0.8.12.dist-info/WHEEL
--rw-r--r--  2.0 unx       41 b- defN 21-Feb-09 15:42 bmll-0.8.12.dist-info/entry_points.txt
--rw-r--r--  2.0 unx        5 b- defN 21-Feb-09 15:42 bmll-0.8.12.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     1060 b- defN 21-Feb-09 15:42 bmll-0.8.12.dist-info/RECORD
-14 files, 41618 bytes uncompressed, 14523 bytes compressed:  65.1%
+Zip file size: 16066 bytes, number of entries: 14
+-rw-r--r--  2.0 unx     1821 b- defN 20-Jun-10 14:42 bmll/__init__.py
+-rw-r--r--  2.0 unx     1493 b- defN 20-Jun-10 14:42 bmll/_cli.py
+-rw-rw-r--  2.0 unx      248 b- defN 20-Jun-10 14:42 bmll/_metadata.json
+-rw-r--r--  2.0 unx    10178 b- defN 20-Jun-10 14:42 bmll/_rest.py
+-rw-r--r--  2.0 unx      871 b- defN 20-Jun-10 14:42 bmll/_utils.py
+-rw-r--r--  2.0 unx      217 b- defN 20-Jun-10 14:42 bmll/exceptions.py
+-rw-r--r--  2.0 unx     5575 b- defN 20-Jun-10 14:42 bmll/reference.py
+-rw-r--r--  2.0 unx     6641 b- defN 20-Jun-10 14:42 bmll/time_series.py
+-rw-rw-r--  2.0 unx    11358 b- defN 20-Jun-10 14:52 bmll-0.8.7.dist-info/LICENSE-2.0.txt
+-rw-r--r--  2.0 unx     1552 b- defN 20-Jun-10 14:52 bmll-0.8.7.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 20-Jun-10 14:52 bmll-0.8.7.dist-info/WHEEL
+-rw-r--r--  2.0 unx       41 b- defN 20-Jun-10 14:52 bmll-0.8.7.dist-info/entry_points.txt
+-rw-r--r--  2.0 unx        5 b- defN 20-Jun-10 14:52 bmll-0.8.7.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     1053 b- defN 20-Jun-10 14:52 bmll-0.8.7.dist-info/RECORD
+14 files, 41145 bytes uncompressed, 14346 bytes compressed:  65.1%
```

## zipnote {}

```diff
@@ -18,26 +18,26 @@
 
 Filename: bmll/reference.py
 Comment: 
 
 Filename: bmll/time_series.py
 Comment: 
 
-Filename: bmll-0.8.12.dist-info/LICENSE-2.0.txt
+Filename: bmll-0.8.7.dist-info/LICENSE-2.0.txt
 Comment: 
 
-Filename: bmll-0.8.12.dist-info/METADATA
+Filename: bmll-0.8.7.dist-info/METADATA
 Comment: 
 
-Filename: bmll-0.8.12.dist-info/WHEEL
+Filename: bmll-0.8.7.dist-info/WHEEL
 Comment: 
 
-Filename: bmll-0.8.12.dist-info/entry_points.txt
+Filename: bmll-0.8.7.dist-info/entry_points.txt
 Comment: 
 
-Filename: bmll-0.8.12.dist-info/top_level.txt
+Filename: bmll-0.8.7.dist-info/top_level.txt
 Comment: 
 
-Filename: bmll-0.8.12.dist-info/RECORD
+Filename: bmll-0.8.7.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## bmll/_metadata.json

### Pretty-printed

 * *Similarity: 0.8571428571428571%*

 * *Differences: {"'url'": "'https://data.bmlltech.com'", "'version'": "'0.8.7'"}*

```diff
@@ -1,9 +1,9 @@
 {
     "author": "info@bmlltech.com",
     "author_email": "info@bmlltech.com",
     "contact": "info@bmlltech.com",
     "description": "BMLL Python SDK",
     "maintainer_email": "info@bmlltech.com",
-    "url": "https://bmlltech.com",
-    "version": "0.8.12"
+    "url": "https://data.bmlltech.com",
+    "version": "0.8.7"
 }
```

## bmll/_rest.py

```diff
@@ -237,22 +237,15 @@
             secret_key_path.read_bytes(), password=password,
             backend=default_backend(),
         )
         jws_encoded = jwt.encode(
             json_body, key=priv_rsakey, algorithm="RS256",
             headers={"kid": json_body["kid"]},
         )
-
-        if isinstance(jws_encoded, str):
-            # pyjwt >= 2.0.0
-            jws = jws_encoded
-        else:
-            # pyjwt < 2.0.0
-            jws = jws_encoded.decode()
-
+        jws = jws_encoded.decode()
         json_body["jws"] = jws
 
         response = self.execute(
             'post',
             'auth',
             '/auth/token',
             json=json_body,
```

## bmll/_utils.py

```diff
@@ -1,26 +1,20 @@
 import pandas as pd
 
 
 __all__ = ('to_pandas', 'paginate', 'to_list_of_str')
 
 
-ID_COL_TYPE = 'Int64' if pd.__version__ >= '0.24.0' else 'object'
-
-
 def to_pandas(table):
     """Return a pandas DataFrame from a Table response."""
     df = pd.DataFrame(data=table['data'], columns=table['columns'])
 
     if 'Date' in df.columns:
         df['Date'] = pd.to_datetime(df['Date'])
 
-    if 'ObjectId' in df.columns:
-        df['ObjectId'] = df['ObjectId'].astype(ID_COL_TYPE)
-
     return df
 
 
 def paginate(request):
     table = request()
     token = table.get('token')
```

## bmll/reference.py

```diff
@@ -1,13 +1,13 @@
 from functools import partial
 
 import pandas as pd
 
 from bmll._rest import DEFAULT_SESSION
-from bmll._utils import to_list_of_str, paginate, ID_COL_TYPE
+from bmll._utils import to_list_of_str, paginate
 
 __all__ = ('query', 'available_markets', 'ReferenceDataClient')
 
 
 class ReferenceDataClient:
     """
     The ReferenceDataClient provides a convenient interface to interact with the BMLL Reference Data API.
@@ -91,21 +91,20 @@
 
         bmll_index_columns = [col for col in ('ListingId', 'InstrumentId', 'MarketId')
                               if col in result['columns']]
         bool_column_map = {col: 'bool' for col in ('IsUpdate', 'IsPrimary', 'IsAlive')
                            if col in result['columns']}
 
         df = pd.DataFrame(**result).set_index(['Date'] + bmll_index_columns).sort_index()
-
         df = (
             df[sorted(df)]
             .reset_index()
             .replace({"True": True, "False": False})
             .astype({'Date': 'datetime64[ns]'})
-            .astype({index_col: ID_COL_TYPE for index_col in bmll_index_columns})
+            .astype({index_col: 'Int64' for index_col in bmll_index_columns})
             .astype(bool_column_map)  # Must be after string to bool conversion.
         )
 
         return df
 
     def available_markets(self, start_date=None, end_date=None):
         """
```

## bmll/time_series.py

```diff
@@ -133,19 +133,15 @@
             ref_data = self._reference_client.query(object_ids=object_ids,
                                                     object_type=object_type,
                                                     **constraint)
             if object_type == 'Instrument':
                 # Only use reference data from the primary exchange for Instrument metrics.
                 ref_data = ref_data.query('IsPrimary')
 
-            identifiers = (
-                ref_data[[object_column] + list(constraint)]
-                .drop_duplicates()  # no dupes
-                .dropna(subset=[object_column])  # no Nans in ListingId/InstrumentId
-            )
+            identifiers = ref_data[[object_column] + list(constraint)].drop_duplicates()
             object_ids = list(identifiers[object_column].unique())
 
             if not object_ids:
                 raise ValueError(f"No Object Ids found for given constraint. {constraint}")
 
         req = partial(self._get_page, object_ids, metric, frequency, start_date, end_date)
```

## Comparing `bmll-0.8.12.dist-info/LICENSE-2.0.txt` & `bmll-0.8.7.dist-info/LICENSE-2.0.txt`

 * *Files identical despite different names*

## Comparing `bmll-0.8.12.dist-info/METADATA` & `bmll-0.8.7.dist-info/METADATA`

 * *Files 10% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 Metadata-Version: 2.1
 Name: bmll
-Version: 0.8.12
+Version: 0.8.7
 Summary: BMLL Python SDK
-Home-page: https://bmlltech.com
+Home-page: https://data.bmlltech.com
 Author: info@bmlltech.com
 Author-email: info@bmlltech.com
 Maintainer-email: info@bmlltech.com
 License: Apache 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

## Comparing `bmll-0.8.12.dist-info/RECORD` & `bmll-0.8.7.dist-info/RECORD`

 * *Files 15% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 bmll/__init__.py,sha256=dCZH9iG_9aYfmsoZFjseQw3mjW8V-JTXHibqZ6Sq39w,1821
 bmll/_cli.py,sha256=vv6tIFzuSs3DMjYHqamyKZbLj36CJ83PlQHDhQhA3bw,1493
-bmll/_metadata.json,sha256=R1d4srA9Ju5OAajuVCmVBSWp-MCVRVgzm4exjcZEYrc,244
-bmll/_rest.py,sha256=VHi89Ej7JJUtbRVOl_Dxg_Zpf0V6c-UCJIgUsh2_LWg,10326
-bmll/_utils.py,sha256=aPdjnbrjNhJPUwQpkHucuio-JiTNbVORMsOrE1twhJQ,1033
+bmll/_metadata.json,sha256=36Mau5Lv1HUZscihy9cSctyhYiBQ6K4LfcVTWKcnK1w,248
+bmll/_rest.py,sha256=L9Fs--5Y1fB9j_KADxVtFeP3Xyi8FU3CwK5I0M8yxME,10178
+bmll/_utils.py,sha256=CkxqiYyxSQdcCKFxJEQJIwEcUqPhweYHh4XbOe2uchE,871
 bmll/exceptions.py,sha256=Y_ayxHH62cfw9acmzrtP4Sl1otjZMbIc-lPblaTFcWM,217
-bmll/reference.py,sha256=TQMx-SYXW4weghvXJQ31n3pjiLdgsRPH3ztBf-2c3AI,5593
-bmll/time_series.py,sha256=SFrFIACdXKwo6BtGm15F-Yn2sgE-xMyIdqzsCBD3Uzw,6787
-bmll-0.8.12.dist-info/LICENSE-2.0.txt,sha256=z8d0m5b2O9McPEK1xHG_dWgUBT6EfBDz6wA0F7xSPTA,11358
-bmll-0.8.12.dist-info/METADATA,sha256=C-S06xy-HhmPGu-slVTk4GL8hdSN_vGyzmjwd2uz4Ww,1548
-bmll-0.8.12.dist-info/WHEEL,sha256=OqRkF0eY5GHssMorFjlbTIq072vpHpF60fIQA6lS9xA,92
-bmll-0.8.12.dist-info/entry_points.txt,sha256=77DwCsQMOnySWBP2l68Iy3pR5m80tQaua4QusOFtRnQ,41
-bmll-0.8.12.dist-info/top_level.txt,sha256=X6KvsicE0PiCufuylqAC4je29BthlNK-rC2HQlzRh1Q,5
-bmll-0.8.12.dist-info/RECORD,,
+bmll/reference.py,sha256=gXP6NUjoBTY1XieWayyAXh5lAnAMgfyLNt6kw_QmtEU,5575
+bmll/time_series.py,sha256=jRoEFPWp7ZtEEW8VYqbDX--eftLXiSk8r30V7ceXp08,6641
+bmll-0.8.7.dist-info/LICENSE-2.0.txt,sha256=z8d0m5b2O9McPEK1xHG_dWgUBT6EfBDz6wA0F7xSPTA,11358
+bmll-0.8.7.dist-info/METADATA,sha256=RVNG1mkyN3GlNSkKnu3e70HWNZyzi8l3RBYuhnGQViM,1552
+bmll-0.8.7.dist-info/WHEEL,sha256=g4nMs7d-Xl9-xC9XovUrsDHGXt-FT0E17Yqo92DEfvY,92
+bmll-0.8.7.dist-info/entry_points.txt,sha256=77DwCsQMOnySWBP2l68Iy3pR5m80tQaua4QusOFtRnQ,41
+bmll-0.8.7.dist-info/top_level.txt,sha256=X6KvsicE0PiCufuylqAC4je29BthlNK-rC2HQlzRh1Q,5
+bmll-0.8.7.dist-info/RECORD,,
```

