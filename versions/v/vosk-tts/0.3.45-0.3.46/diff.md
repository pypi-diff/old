# Comparing `tmp/vosk_tts-0.3.45-py3-none-any.whl.zip` & `tmp/vosk_tts-0.3.46-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,13 +1,13 @@
-Zip file size: 10244 bytes, number of entries: 11
+Zip file size: 10268 bytes, number of entries: 11
 -rw-r--r--  2.0 unx        0 b- defN 23-Apr-07 00:49 vosk_tts/__init__.py
 -rw-r--r--  2.0 unx     1769 b- defN 23-Apr-07 00:55 vosk_tts/cli.py
 -rw-r--r--  2.0 unx     2400 b- defN 23-Apr-07 00:49 vosk_tts/g2p.py
--rw-r--r--  2.0 unx     5516 b- defN 23-Apr-07 00:49 vosk_tts/model.py
+-rw-r--r--  2.0 unx     5586 b- defN 23-Apr-07 01:32 vosk_tts/model.py
 -rw-r--r--  2.0 unx     1740 b- defN 23-Apr-07 00:49 vosk_tts/synth.py
--rw-r--r--  2.0 unx    11357 b- defN 23-Apr-07 00:57 vosk_tts-0.3.45.dist-info/LICENSE
--rw-r--r--  2.0 unx      847 b- defN 23-Apr-07 00:57 vosk_tts-0.3.45.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 23-Apr-07 00:57 vosk_tts-0.3.45.dist-info/WHEEL
--rw-r--r--  2.0 unx       48 b- defN 23-Apr-07 00:57 vosk_tts-0.3.45.dist-info/entry_points.txt
--rw-r--r--  2.0 unx        9 b- defN 23-Apr-07 00:57 vosk_tts-0.3.45.dist-info/top_level.txt
--rw-rw-r--  2.0 unx      858 b- defN 23-Apr-07 00:57 vosk_tts-0.3.45.dist-info/RECORD
-11 files, 24636 bytes uncompressed, 8796 bytes compressed:  64.3%
+-rw-r--r--  2.0 unx    11357 b- defN 23-Apr-07 01:34 vosk_tts-0.3.46.dist-info/LICENSE
+-rw-r--r--  2.0 unx      858 b- defN 23-Apr-07 01:34 vosk_tts-0.3.46.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 23-Apr-07 01:34 vosk_tts-0.3.46.dist-info/WHEEL
+-rw-r--r--  2.0 unx       48 b- defN 23-Apr-07 01:34 vosk_tts-0.3.46.dist-info/entry_points.txt
+-rw-r--r--  2.0 unx        9 b- defN 23-Apr-07 01:34 vosk_tts-0.3.46.dist-info/top_level.txt
+-rw-rw-r--  2.0 unx      858 b- defN 23-Apr-07 01:34 vosk_tts-0.3.46.dist-info/RECORD
+11 files, 24717 bytes uncompressed, 8820 bytes compressed:  64.3%
```

## zipnote {}

```diff
@@ -9,26 +9,26 @@
 
 Filename: vosk_tts/model.py
 Comment: 
 
 Filename: vosk_tts/synth.py
 Comment: 
 
-Filename: vosk_tts-0.3.45.dist-info/LICENSE
+Filename: vosk_tts-0.3.46.dist-info/LICENSE
 Comment: 
 
-Filename: vosk_tts-0.3.45.dist-info/METADATA
+Filename: vosk_tts-0.3.46.dist-info/METADATA
 Comment: 
 
-Filename: vosk_tts-0.3.45.dist-info/WHEEL
+Filename: vosk_tts-0.3.46.dist-info/WHEEL
 Comment: 
 
-Filename: vosk_tts-0.3.45.dist-info/entry_points.txt
+Filename: vosk_tts-0.3.46.dist-info/entry_points.txt
 Comment: 
 
-Filename: vosk_tts-0.3.45.dist-info/top_level.txt
+Filename: vosk_tts-0.3.46.dist-info/top_level.txt
 Comment: 
 
-Filename: vosk_tts-0.3.45.dist-info/RECORD
+Filename: vosk_tts-0.3.46.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## vosk_tts/model.py

```diff
@@ -8,14 +8,16 @@
 
 from urllib.request import urlretrieve
 from zipfile import ZipFile
 from re import match
 from pathlib import Path
 from tqdm import tqdm
 
+from .g2p import convert
+
 # Remote location of the models and local folders
 MODEL_PRE_URL = "https://alphacephei.com/vosk/models/"
 MODEL_LIST_URL = MODEL_PRE_URL + "model-list.json"
 MODEL_DIRS = [os.getenv("VOSK_MODEL_PATH"), Path("/usr/share/vosk"),
         Path.home() / "AppData/Local/vosk", Path.home() / ".cache/vosk"]
 
 def list_models():
@@ -134,14 +136,15 @@
                 phonemes.extend(convert(word).split())
 
         phoneme_id_map = self.config["phoneme_id_map"]
         phoneme_ids = []
         phoneme_ids.extend(phoneme_id_map["^"])
         phoneme_ids.extend(phoneme_id_map["_"])
         for p in phonemes:
-            phoneme_ids.extend(phoneme_id_map[p])
-            phoneme_ids.extend(phoneme_id_map["_"])
+            if p in phoneme_id_map:
+                phoneme_ids.extend(phoneme_id_map[p])
+                phoneme_ids.extend(phoneme_id_map["_"])
         phoneme_ids.extend(phoneme_id_map["$"])
 
         print (text, phonemes, phoneme_ids)
 
         return phoneme_ids
```

## Comparing `vosk_tts-0.3.45.dist-info/LICENSE` & `vosk_tts-0.3.46.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `vosk_tts-0.3.45.dist-info/METADATA` & `vosk_tts-0.3.46.dist-info/METADATA`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vosk-tts
-Version: 0.3.45
+Version: 0.3.46
 Summary: Offline text to speech synthesis
 Home-page: https://github.com/alphacep/vosk-tts
 Author: Alpha Cephei Inc
 Author-email: contact@alphacephei.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
@@ -13,19 +13,20 @@
 Classifier: Operating System :: POSIX :: Linux
 Classifier: Operating System :: MacOS :: MacOS X
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 Requires-Dist: onnxruntime
 
-Vosk TTS
+# Vosk TTS
 
 Simple TTS based on VITS with some old ideas
 
-Usage:
+## Usage
 
+```
 pip3 install vosk-tts
 
 vosk-tts -n vosk-model-tts-ru-0.1-natasha --input "Привет мир!" --output ~/out.wav
-
+```
```

## Comparing `vosk_tts-0.3.45.dist-info/RECORD` & `vosk_tts-0.3.46.dist-info/RECORD`

 * *Files 9% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 vosk_tts/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 vosk_tts/cli.py,sha256=38-XjpiIuAw-9ja0W3XadRV-dI-p-GlfypdfZm-A8Pg,1769
 vosk_tts/g2p.py,sha256=u1aKRW-G3Cwmtviy3pDNePTSkNvemNKw-tQTankT9lQ,2400
-vosk_tts/model.py,sha256=dS1-uf7oVR7T-6_Hkj8QFqGfN9CKwvxQaltVnLLWHaU,5516
+vosk_tts/model.py,sha256=pa2dDNyNert6_pyKI6ouCsY4Rqze33dvQokecVJTpfw,5586
 vosk_tts/synth.py,sha256=K1VXd4D-BgHWUh-rMJh_kIbz-X0OagjNIBvdWlx-QI4,1740
-vosk_tts-0.3.45.dist-info/LICENSE,sha256=xx0jnfkXJvxRnG63LTGOxlggYnIysveWIZ6H3PNdCrQ,11357
-vosk_tts-0.3.45.dist-info/METADATA,sha256=0jlA0Pdttki0grQ7pZxlr1wbWzI756gzn6Aoexg7uDw,847
-vosk_tts-0.3.45.dist-info/WHEEL,sha256=pkctZYzUS4AYVn6dJ-7367OJZivF2e8RA9b_ZBjif18,92
-vosk_tts-0.3.45.dist-info/entry_points.txt,sha256=K-WoVxWxiIH_T7nNvqtPI5ycsSwtaNCvQXq6_r9dvlI,48
-vosk_tts-0.3.45.dist-info/top_level.txt,sha256=FaXgnbIzrcWwBJp-TwQ-5Dxee0iOHHgdNsxrdg6CQww,9
-vosk_tts-0.3.45.dist-info/RECORD,,
+vosk_tts-0.3.46.dist-info/LICENSE,sha256=xx0jnfkXJvxRnG63LTGOxlggYnIysveWIZ6H3PNdCrQ,11357
+vosk_tts-0.3.46.dist-info/METADATA,sha256=maCVyZ6vyxFKisypajNrAPtXer-bSnlnrklWn9k6J6c,858
+vosk_tts-0.3.46.dist-info/WHEEL,sha256=pkctZYzUS4AYVn6dJ-7367OJZivF2e8RA9b_ZBjif18,92
+vosk_tts-0.3.46.dist-info/entry_points.txt,sha256=K-WoVxWxiIH_T7nNvqtPI5ycsSwtaNCvQXq6_r9dvlI,48
+vosk_tts-0.3.46.dist-info/top_level.txt,sha256=FaXgnbIzrcWwBJp-TwQ-5Dxee0iOHHgdNsxrdg6CQww,9
+vosk_tts-0.3.46.dist-info/RECORD,,
```

