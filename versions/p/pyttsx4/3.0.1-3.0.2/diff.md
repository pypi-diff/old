# Comparing `tmp/pyttsx4-3.0.1-py3-none-any.whl.zip` & `tmp/pyttsx4-3.0.2-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,18 +1,18 @@
-Zip file size: 32835 bytes, number of entries: 16
+Zip file size: 32814 bytes, number of entries: 16
 -rw-r--r--  2.0 unx      814 b- defN 23-Apr-07 13:37 pyttsx4/__init__.py
 -rw-r--r--  2.0 unx     6878 b- defN 23-Apr-07 14:20 pyttsx4/driver.py
 -rw-r--r--  2.0 unx     7224 b- defN 23-Apr-07 13:37 pyttsx4/engine.py
 -rw-r--r--  2.0 unx    29524 b- defN 23-Apr-07 13:37 pyttsx4/six.py
 -rw-r--r--  2.0 unx      431 b- defN 23-Apr-07 13:37 pyttsx4/voice.py
 -rw-r--r--  2.0 unx      853 b- defN 23-Apr-07 13:37 pyttsx4/drivers/__init__.py
 -rw-r--r--  2.0 unx    19495 b- defN 23-Apr-07 13:37 pyttsx4/drivers/_espeak.py
 -rw-r--r--  2.0 unx     6182 b- defN 23-Apr-07 13:37 pyttsx4/drivers/dummy.py
 -rw-r--r--  2.0 unx     6801 b- defN 23-Apr-07 13:37 pyttsx4/drivers/espeak.py
--rw-r--r--  2.0 unx     3794 b- defN 23-Apr-07 13:37 pyttsx4/drivers/nsss.py
+-rw-r--r--  2.0 unx     3729 b- defN 23-Apr-07 14:49 pyttsx4/drivers/nsss.py
 -rw-r--r--  2.0 unx     5877 b- defN 23-Apr-07 14:27 pyttsx4/drivers/sapi5.py
--rw-r--r--  2.0 unx    17098 b- defN 23-Apr-07 14:29 pyttsx4-3.0.1.dist-info/LICENSE
--rw-r--r--  2.0 unx     1821 b- defN 23-Apr-07 14:29 pyttsx4-3.0.1.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 23-Apr-07 14:29 pyttsx4-3.0.1.dist-info/WHEEL
--rw-r--r--  2.0 unx        8 b- defN 23-Apr-07 14:29 pyttsx4-3.0.1.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     1244 b- defN 23-Apr-07 14:29 pyttsx4-3.0.1.dist-info/RECORD
-16 files, 108136 bytes uncompressed, 30815 bytes compressed:  71.5%
+-rw-r--r--  2.0 unx    17098 b- defN 23-Apr-07 14:53 pyttsx4-3.0.2.dist-info/LICENSE
+-rw-r--r--  2.0 unx     1821 b- defN 23-Apr-07 14:53 pyttsx4-3.0.2.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 23-Apr-07 14:53 pyttsx4-3.0.2.dist-info/WHEEL
+-rw-r--r--  2.0 unx        8 b- defN 23-Apr-07 14:53 pyttsx4-3.0.2.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     1244 b- defN 23-Apr-07 14:53 pyttsx4-3.0.2.dist-info/RECORD
+16 files, 108071 bytes uncompressed, 30794 bytes compressed:  71.5%
```

## zipnote {}

```diff
@@ -27,23 +27,23 @@
 
 Filename: pyttsx4/drivers/nsss.py
 Comment: 
 
 Filename: pyttsx4/drivers/sapi5.py
 Comment: 
 
-Filename: pyttsx4-3.0.1.dist-info/LICENSE
+Filename: pyttsx4-3.0.2.dist-info/LICENSE
 Comment: 
 
-Filename: pyttsx4-3.0.1.dist-info/METADATA
+Filename: pyttsx4-3.0.2.dist-info/METADATA
 Comment: 
 
-Filename: pyttsx4-3.0.1.dist-info/WHEEL
+Filename: pyttsx4-3.0.2.dist-info/WHEEL
 Comment: 
 
-Filename: pyttsx4-3.0.1.dist-info/top_level.txt
+Filename: pyttsx4-3.0.2.dist-info/top_level.txt
 Comment: 
 
-Filename: pyttsx4-3.0.1.dist-info/RECORD
+Filename: pyttsx4-3.0.2.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## pyttsx4/drivers/nsss.py

```diff
@@ -51,21 +51,18 @@
     def stop(self):
         if self._proxy.isBusy():
             self._completed = False
         self._tts.stopSpeaking()
 
     @objc.python_method
     def _toVoice(self, attr):
-        try:
-            lang = attr['VoiceLocaleIdentifier']
-        except KeyError:
-            lang = attr['VoiceLanguage']
-        return Voice(attr['VoiceIdentifier'], attr['VoiceName'],
-                     [lang], attr['VoiceGender'],
-                     attr['VoiceAge'])
+
+        return Voice(attr.get('VoiceIdentifier'), attr.get('VoiceName'),
+                     [attr.get('VoiceIdentifier',attr.get('VoiceLanguage'))], attr.get('VoiceGender'),
+                     attr.get('VoiceAge'))
 
     @objc.python_method
     def getProperty(self, name):
         if name == 'voices':
             return [self._toVoice(NSSpeechSynthesizer.attributesForVoice_(v))
                     for v in list(NSSpeechSynthesizer.availableVoices())]
         elif name == 'voice':
```

## Comparing `pyttsx4-3.0.1.dist-info/LICENSE` & `pyttsx4-3.0.2.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `pyttsx4-3.0.1.dist-info/METADATA` & `pyttsx4-3.0.2.dist-info/METADATA`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyttsx4
-Version: 3.0.1
+Version: 3.0.2
 Summary: Text to Speech (TTS) library for Python 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak.
 Home-page: https://github.com/Jiangshan00001/pyttsx4
 Author: Natesh M Bhat
 Author-email: 710806594@qq.com
 License: UNKNOWN
 Keywords: pyttsx,ivona,pyttsx for python3,TTS for python3,pyttsx3,text to speech for python,tts,text to speech,speech,speech synthesis,offline text to speech,offline tts,gtts
 Platform: UNKNOWN
```

## Comparing `pyttsx4-3.0.1.dist-info/RECORD` & `pyttsx4-3.0.2.dist-info/RECORD`

 * *Files 6% similar despite different names*

```diff
@@ -3,14 +3,14 @@
 pyttsx4/engine.py,sha256=UJBrPIcN3KXmBCABrb2uY4F_AeAaFlC5h6n_L3V0euA,7224
 pyttsx4/six.py,sha256=yVeu0rLX2Qv1P1UaJtvamDmMrjnxNsJkSuztEvVyGG8,29524
 pyttsx4/voice.py,sha256=GYZLgGtnmjLrg93Wh7_lqDcs6zMaTS_QRr3KZM7RZnY,431
 pyttsx4/drivers/__init__.py,sha256=EFf83iBpSVF4joEh4gQmq5Rl22tngVNuR1zBeWfCdjQ,853
 pyttsx4/drivers/_espeak.py,sha256=Gj0N4aFf3YGZO9fq8K5BFbiwkIExqDu1nBXUn7EZVzY,19495
 pyttsx4/drivers/dummy.py,sha256=d7K46sijjOxwmAJHbgEALwbYwGcktLfW1FcX1iG5I8E,6182
 pyttsx4/drivers/espeak.py,sha256=p2-L60Qrl6wVoSrGlQM6jWQhammXJL-UvCxsDoPZaow,6801
-pyttsx4/drivers/nsss.py,sha256=cYqbFSe4fCCJirwcB0nBLQbOb8MfGi0hTxN5bgW8QgI,3794
+pyttsx4/drivers/nsss.py,sha256=n849K4ugK87S4ejtc_7xYp5W__maB6vfRX_sxIWlGIU,3729
 pyttsx4/drivers/sapi5.py,sha256=_KPHJdxEUdR13vnltalb8UCWxEcldpjNm9cawYfE6T4,5877
-pyttsx4-3.0.1.dist-info/LICENSE,sha256=JoTeFzAOCkNGhvHsf4r2BFIHpLRXo_4EsrnOZV58XVA,17098
-pyttsx4-3.0.1.dist-info/METADATA,sha256=oz1paOgYI_3qYHD-WuxX4Lh2eTeSNLzk8JwmNhCFW48,1821
-pyttsx4-3.0.1.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
-pyttsx4-3.0.1.dist-info/top_level.txt,sha256=RZW_EXmaQg7go8T0q583RzqdJUlYm0NeSHGpyq92tiY,8
-pyttsx4-3.0.1.dist-info/RECORD,,
+pyttsx4-3.0.2.dist-info/LICENSE,sha256=JoTeFzAOCkNGhvHsf4r2BFIHpLRXo_4EsrnOZV58XVA,17098
+pyttsx4-3.0.2.dist-info/METADATA,sha256=5pHt2RXkqIUKRALTC06Y_lA4ZOIXfuUTJDtT5WKMF1A,1821
+pyttsx4-3.0.2.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
+pyttsx4-3.0.2.dist-info/top_level.txt,sha256=RZW_EXmaQg7go8T0q583RzqdJUlYm0NeSHGpyq92tiY,8
+pyttsx4-3.0.2.dist-info/RECORD,,
```

