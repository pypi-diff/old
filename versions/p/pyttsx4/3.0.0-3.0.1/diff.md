# Comparing `tmp/pyttsx4-3.0.0-py3-none-any.whl.zip` & `tmp/pyttsx4-3.0.1-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,18 +1,18 @@
-Zip file size: 33526 bytes, number of entries: 16
+Zip file size: 32835 bytes, number of entries: 16
 -rw-r--r--  2.0 unx      814 b- defN 23-Apr-07 13:37 pyttsx4/__init__.py
--rw-r--r--  2.0 unx     6844 b- defN 23-Apr-07 13:37 pyttsx4/driver.py
+-rw-r--r--  2.0 unx     6878 b- defN 23-Apr-07 14:20 pyttsx4/driver.py
 -rw-r--r--  2.0 unx     7224 b- defN 23-Apr-07 13:37 pyttsx4/engine.py
 -rw-r--r--  2.0 unx    29524 b- defN 23-Apr-07 13:37 pyttsx4/six.py
 -rw-r--r--  2.0 unx      431 b- defN 23-Apr-07 13:37 pyttsx4/voice.py
 -rw-r--r--  2.0 unx      853 b- defN 23-Apr-07 13:37 pyttsx4/drivers/__init__.py
 -rw-r--r--  2.0 unx    19495 b- defN 23-Apr-07 13:37 pyttsx4/drivers/_espeak.py
 -rw-r--r--  2.0 unx     6182 b- defN 23-Apr-07 13:37 pyttsx4/drivers/dummy.py
 -rw-r--r--  2.0 unx     6801 b- defN 23-Apr-07 13:37 pyttsx4/drivers/espeak.py
 -rw-r--r--  2.0 unx     3794 b- defN 23-Apr-07 13:37 pyttsx4/drivers/nsss.py
--rw-r--r--  2.0 unx     5345 b- defN 23-Apr-07 13:37 pyttsx4/drivers/sapi5.py
--rw-r--r--  2.0 unx    17098 b- defN 23-Apr-07 13:45 pyttsx4-3.0.0.dist-info/LICENSE
--rw-r--r--  2.0 unx     4051 b- defN 23-Apr-07 13:45 pyttsx4-3.0.0.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 23-Apr-07 13:45 pyttsx4-3.0.0.dist-info/WHEEL
--rw-r--r--  2.0 unx        8 b- defN 23-Apr-07 13:45 pyttsx4-3.0.0.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     1244 b- defN 23-Apr-07 13:45 pyttsx4-3.0.0.dist-info/RECORD
-16 files, 109800 bytes uncompressed, 31506 bytes compressed:  71.3%
+-rw-r--r--  2.0 unx     5877 b- defN 23-Apr-07 14:27 pyttsx4/drivers/sapi5.py
+-rw-r--r--  2.0 unx    17098 b- defN 23-Apr-07 14:29 pyttsx4-3.0.1.dist-info/LICENSE
+-rw-r--r--  2.0 unx     1821 b- defN 23-Apr-07 14:29 pyttsx4-3.0.1.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 23-Apr-07 14:29 pyttsx4-3.0.1.dist-info/WHEEL
+-rw-r--r--  2.0 unx        8 b- defN 23-Apr-07 14:29 pyttsx4-3.0.1.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     1244 b- defN 23-Apr-07 14:29 pyttsx4-3.0.1.dist-info/RECORD
+16 files, 108136 bytes uncompressed, 30815 bytes compressed:  71.5%
```

## zipnote {}

```diff
@@ -27,23 +27,23 @@
 
 Filename: pyttsx4/drivers/nsss.py
 Comment: 
 
 Filename: pyttsx4/drivers/sapi5.py
 Comment: 
 
-Filename: pyttsx4-3.0.0.dist-info/LICENSE
+Filename: pyttsx4-3.0.1.dist-info/LICENSE
 Comment: 
 
-Filename: pyttsx4-3.0.0.dist-info/METADATA
+Filename: pyttsx4-3.0.1.dist-info/METADATA
 Comment: 
 
-Filename: pyttsx4-3.0.0.dist-info/WHEEL
+Filename: pyttsx4-3.0.1.dist-info/WHEEL
 Comment: 
 
-Filename: pyttsx4-3.0.0.dist-info/top_level.txt
+Filename: pyttsx4-3.0.1.dist-info/top_level.txt
 Comment: 
 
-Filename: pyttsx4-3.0.0.dist-info/RECORD
+Filename: pyttsx4-3.0.1.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## pyttsx4/driver.py

```diff
@@ -42,15 +42,15 @@
             if sys.platform == 'darwin':
                 driverName = 'nsss'
             elif sys.platform == 'win32':
                 driverName = 'sapi5'
             else:
                 driverName = 'espeak'
         # import driver module
-        name = 'pyttsx3.drivers.%s' % driverName
+        name = 'pyttsx4.drivers.%s' % driverName
         self._module = importlib.import_module(name)
         # build driver instance
         self._driver = self._module.buildDriver(weakref.proxy(self))
         # initialize refs
         self._engine = engine
         self._queue = []
         self._busy = True
@@ -86,14 +86,15 @@
         while (not self._busy) and len(self._queue):
             cmd = self._queue.pop(0)
             self._name = cmd[2]
             try:
                 cmd[0](*cmd[1])
             except Exception as e:
                 self.notify('error', exception=e)
+                print('ERROR',e)
                 if self._debug:
                     traceback.print_exc()
 
     def notify(self, topic, **kwargs):
         '''
         Sends a notification to the engine from the driver.
```

## pyttsx4/drivers/sapi5.py

```diff
@@ -3,14 +3,15 @@
     from comtypes.gen import SpeechLib  # comtypes
 except ImportError:
     # Generate the SpeechLib lib and any associated files
     engine = comtypes.client.CreateObject("SAPI.SpVoice")
     stream = comtypes.client.CreateObject("SAPI.SpFileStream")
     from comtypes.gen import SpeechLib
 
+from io import BytesIO
 import pythoncom
 import time
 import math
 import os
 import weakref
 from ..voice import Voice
 from . import toUtf8, fromUtf8
@@ -59,24 +60,38 @@
         if not self._speaking:
             return
         self._proxy.setBusy(True)
         self._stopping = True
         self._tts.Speak('', 3)
 
     def save_to_file(self, text, filename):
+        if isinstance(filename, BytesIO):
+            self.to_memory(text, filename)
+            return
+
         cwd = os.getcwd()
         stream = comtypes.client.CreateObject('SAPI.SPFileStream')
         stream.Open(filename, SpeechLib.SSFMCreateForWrite)
         temp_stream = self._tts.AudioOutputStream
         self._tts.AudioOutputStream = stream
         self._tts.Speak(fromUtf8(toUtf8(text)))
         self._tts.AudioOutputStream = temp_stream
         stream.close()
         os.chdir(cwd)
 
+    def to_memory(self, text, olist):
+        stream = comtypes.client.CreateObject('SAPI.SpMemoryStream')
+        temp_stream = self._tts.AudioOutputStream
+        self._tts.AudioOutputStream = stream
+        self._tts.Speak(fromUtf8(toUtf8(text)))
+        self._tts.AudioOutputStream = temp_stream
+        data = stream.GetData()
+        olist.write(bytes(data))
+        stream.close()
+
     def _toVoice(self, attr):
         return Voice(attr.Id, attr.GetDescription())
 
     def _tokenFromId(self, id_):
         tokens = self._tts.GetVoices()
         for token in tokens:
             if token.Id == id_:
```

## Comparing `pyttsx4-3.0.0.dist-info/LICENSE` & `pyttsx4-3.0.1.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `pyttsx4-3.0.0.dist-info/RECORD` & `pyttsx4-3.0.1.dist-info/RECORD`

 * *Files 11% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 pyttsx4/__init__.py,sha256=pO2FX679OZHgpn2vBVIZDoBQff4uOUMe6yBpNRbaw-4,814
-pyttsx4/driver.py,sha256=O13PkPZooqvS7A6lcMiDteLfG9kNuYdSk98iK5Bfpi4,6844
+pyttsx4/driver.py,sha256=GrKVB4NHUex375QjHHvC6x9vHQJzpWjqVQ1t2h1UL7U,6878
 pyttsx4/engine.py,sha256=UJBrPIcN3KXmBCABrb2uY4F_AeAaFlC5h6n_L3V0euA,7224
 pyttsx4/six.py,sha256=yVeu0rLX2Qv1P1UaJtvamDmMrjnxNsJkSuztEvVyGG8,29524
 pyttsx4/voice.py,sha256=GYZLgGtnmjLrg93Wh7_lqDcs6zMaTS_QRr3KZM7RZnY,431
 pyttsx4/drivers/__init__.py,sha256=EFf83iBpSVF4joEh4gQmq5Rl22tngVNuR1zBeWfCdjQ,853
 pyttsx4/drivers/_espeak.py,sha256=Gj0N4aFf3YGZO9fq8K5BFbiwkIExqDu1nBXUn7EZVzY,19495
 pyttsx4/drivers/dummy.py,sha256=d7K46sijjOxwmAJHbgEALwbYwGcktLfW1FcX1iG5I8E,6182
 pyttsx4/drivers/espeak.py,sha256=p2-L60Qrl6wVoSrGlQM6jWQhammXJL-UvCxsDoPZaow,6801
 pyttsx4/drivers/nsss.py,sha256=cYqbFSe4fCCJirwcB0nBLQbOb8MfGi0hTxN5bgW8QgI,3794
-pyttsx4/drivers/sapi5.py,sha256=OFJ_PB6PmeLZmd4H25EddaNaM1XrhJkM2j0hCg5PzeQ,5345
-pyttsx4-3.0.0.dist-info/LICENSE,sha256=JoTeFzAOCkNGhvHsf4r2BFIHpLRXo_4EsrnOZV58XVA,17098
-pyttsx4-3.0.0.dist-info/METADATA,sha256=NW49qnYTIWGwXVlTSOlpsDf14Dvx65HinmTA4aBVY30,4051
-pyttsx4-3.0.0.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
-pyttsx4-3.0.0.dist-info/top_level.txt,sha256=RZW_EXmaQg7go8T0q583RzqdJUlYm0NeSHGpyq92tiY,8
-pyttsx4-3.0.0.dist-info/RECORD,,
+pyttsx4/drivers/sapi5.py,sha256=_KPHJdxEUdR13vnltalb8UCWxEcldpjNm9cawYfE6T4,5877
+pyttsx4-3.0.1.dist-info/LICENSE,sha256=JoTeFzAOCkNGhvHsf4r2BFIHpLRXo_4EsrnOZV58XVA,17098
+pyttsx4-3.0.1.dist-info/METADATA,sha256=oz1paOgYI_3qYHD-WuxX4Lh2eTeSNLzk8JwmNhCFW48,1821
+pyttsx4-3.0.1.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
+pyttsx4-3.0.1.dist-info/top_level.txt,sha256=RZW_EXmaQg7go8T0q583RzqdJUlYm0NeSHGpyq92tiY,8
+pyttsx4-3.0.1.dist-info/RECORD,,
```

