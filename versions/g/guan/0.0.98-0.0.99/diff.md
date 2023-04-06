# Comparing `tmp/guan-0.0.98.tar.gz` & `tmp/guan-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "E:\archives\cloud.guanjihuan.com\Codes shared on website Ji-Huan Guan\py.guanjihuan.com\PyPI\dist\tmpqne1ag5h\guan-0.0.98.tar", last modified: Wed Jun 29 09:10:06 2022, max compression
+gzip compressed data, was "E:\archives\cloud.guanjihuan.com\Codes shared on website Ji-Huan Guan\py.guanjihuan.com\PyPI\dist\tmpq9o6wde1\guan-0.0.99.tar", last modified: Wed Jul  6 07:24:44 2022, max compression
```

## Comparing `guan-0.0.98.tar` & `guan-0.0.99.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxrwxrwx   0        0        0        0 2022-06-29 09:10:06.596257 guan-0.0.98/
--rw-rw-rw-   0        0        0    35821 2021-07-19 21:39:06.000000 guan-0.0.98/LICENSE
--rw-rw-rw-   0        0        0      991 2022-06-29 09:10:06.597253 guan-0.0.98/PKG-INFO
--rw-rw-rw-   0        0        0      487 2022-05-16 06:56:02.000000 guan-0.0.98/README.md
--rw-rw-rw-   0        0        0      108 2021-05-22 13:59:00.000000 guan-0.0.98/pyproject.toml
--rw-rw-rw-   0        0        0      641 2022-06-29 09:10:06.599537 guan-0.0.98/setup.cfg
-drwxrwxrwx   0        0        0        0 2022-06-29 09:10:06.552235 guan-0.0.98/src/
-drwxrwxrwx   0        0        0        0 2022-06-29 09:10:06.564203 guan-0.0.98/src/guan/
--rw-rw-rw-   0        0        0   117155 2022-06-29 09:08:52.000000 guan-0.0.98/src/guan/__init__.py
-drwxrwxrwx   0        0        0        0 2022-06-29 09:10:06.594261 guan-0.0.98/src/guan.egg-info/
--rw-rw-rw-   0        0        0      991 2022-06-29 09:10:05.000000 guan-0.0.98/src/guan.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      191 2022-06-29 09:10:06.000000 guan-0.0.98/src/guan.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2022-06-29 09:10:05.000000 guan-0.0.98/src/guan.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        5 2022-06-29 09:10:06.000000 guan-0.0.98/src/guan.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2022-07-06 07:24:44.110572 guan-0.0.99/
+-rw-rw-rw-   0        0        0    35821 2021-07-19 21:39:06.000000 guan-0.0.99/LICENSE
+-rw-rw-rw-   0        0        0      991 2022-07-06 07:24:44.110572 guan-0.0.99/PKG-INFO
+-rw-rw-rw-   0        0        0      487 2022-05-16 06:56:02.000000 guan-0.0.99/README.md
+-rw-rw-rw-   0        0        0      108 2021-05-22 13:59:00.000000 guan-0.0.99/pyproject.toml
+-rw-rw-rw-   0        0        0      641 2022-07-06 07:24:44.113586 guan-0.0.99/setup.cfg
+drwxrwxrwx   0        0        0        0 2022-07-06 07:24:44.060702 guan-0.0.99/src/
+drwxrwxrwx   0        0        0        0 2022-07-06 07:24:44.077660 guan-0.0.99/src/guan/
+-rw-rw-rw-   0        0        0   118380 2022-07-06 07:23:09.000000 guan-0.0.99/src/guan/__init__.py
+drwxrwxrwx   0        0        0        0 2022-07-06 07:24:44.109609 guan-0.0.99/src/guan.egg-info/
+-rw-rw-rw-   0        0        0      991 2022-07-06 07:24:44.000000 guan-0.0.99/src/guan.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      191 2022-07-06 07:24:44.000000 guan-0.0.99/src/guan.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2022-07-06 07:24:44.000000 guan-0.0.99/src/guan.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        5 2022-07-06 07:24:44.000000 guan-0.0.99/src/guan.egg-info/top_level.txt
```

### Comparing `guan-0.0.98/LICENSE` & `guan-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `guan-0.0.98/PKG-INFO` & `guan-0.0.99/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: guan
-Version: 0.0.98
+Version: 0.0.99
 Summary: An open source python package
 Home-page: https://py.guanjihuan.com
 Author: guanjihuan
 Author-email: guanjihuan@163.com
 Project-URL: Bug Tracker, https://py.guanjihuan.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
```

### Comparing `guan-0.0.98/setup.cfg` & `guan-0.0.99/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 00000000: 5b6d 6574 6164 6174 615d 0d0a 6e61 6d65  [metadata]..name
 00000010: 203d 2067 7561 6e0d 0a76 6572 7369 6f6e   = guan..version
-00000020: 203d 2030 2e30 2e39 380d 0a61 7574 686f   = 0.0.98..autho
+00000020: 203d 2030 2e30 2e39 390d 0a61 7574 686f   = 0.0.99..autho
 00000030: 7220 3d20 6775 616e 6a69 6875 616e 0d0a  r = guanjihuan..
 00000040: 6175 7468 6f72 5f65 6d61 696c 203d 2067  author_email = g
 00000050: 7561 6e6a 6968 7561 6e40 3136 332e 636f  uanjihuan@163.co
 00000060: 6d0d 0a64 6573 6372 6970 7469 6f6e 203d  m..description =
 00000070: 2041 6e20 6f70 656e 2073 6f75 7263 6520   An open source 
 00000080: 7079 7468 6f6e 2070 6163 6b61 6765 0d0a  python package..
 00000090: 6c6f 6e67 5f64 6573 6372 6970 7469 6f6e  long_description
```

### Comparing `guan-0.0.98/src/guan/__init__.py` & `guan-0.0.99/src/guan/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 # Guan is an open-source python package developed and maintained by https://www.guanjihuan.com/about. The primary location of this package is on website https://py.guanjihuan.com.
 
 # With this package, you can calculate band structures, density of states, quantum transport and topological invariant of tight-binding models by invoking the functions you need. Other frequently used functions are also integrated in this package, such as file reading/writing, figure plotting, data processing.
 
-# The current version is guan-0.0.98, updated on June 29, 2022.
+# The current version is guan-0.0.99, updated on July 06, 2022.
 
 # Installation: pip install --upgrade guan
 
 # Modules:
 
 # # Module 1: basic functions
 # # Module 2: Fourier transform
@@ -329,14 +329,16 @@
 
 guan.str_to_audio(str='hello world', rate=125, voice=1, read=1, save=0, print_text=0)
 
 guan.txt_to_audio(txt_path, rate=125, voice=1, read=1, save=0, print_text=0)
 
 guan.pdf_to_audio(pdf_path, rate=125, voice=1, read=1, save=0, print_text=0)
 
+guan.compress_mp3(mp3_path, output_filename='a.mp3', bitrate='16k')
+
 guan.play_academic_words(reverse=0, random_on=0, bre_or_ame='ame', show_translation=1, show_link=1, translation_time=2, rest_time=1)
 
 guan.play_element_words(random_on=0, show_translation=1, show_link=1, translation_time=2, rest_time=1)
 
 '''
 
 
@@ -2352,70 +2354,91 @@
             for x in layout:
                 if isinstance(x, LTTextBox):
                     content  = content + x.get_text().strip()
     return content
 
 ## audio
 
-def str_to_audio(str='hello world', rate=125, voice=1, read=1, save=0, print_text=0):
+def str_to_audio(str='hello world', filename='str', rate=125, voice=1, read=1, save=0, compress=0, bitrate='16k', print_text=0):
     import pyttsx3
     if print_text==1:
         print(str)
     engine = pyttsx3.init()
     voices = engine.getProperty('voices')  
     engine.setProperty('voice', voices[voice].id)
     engine.setProperty("rate", rate)
     if save==1:
-        engine.save_to_file(str, 'str.mp3')
+        engine.save_to_file(str, filename+'.mp3')
         engine.runAndWait()
         print('MP3 file saved!')
+        if compress==1:
+            import os
+            os.rename(filename+'.mp3', 'temp.mp3')
+            compress_mp3('temp.mp3', output_filename=filename+'.mp3', bitrate=bitrate)
+            os.remove('temp.mp3')
     if read==1:
         engine.say(str)
         engine.runAndWait()
 
-def txt_to_audio(txt_path, rate=125, voice=1, read=1, save=0, print_text=0):
+def txt_to_audio(txt_path, rate=125, voice=1, read=1, save=0, compress=0, bitrate='16k', print_text=0):
     import pyttsx3
     f = open(txt_path, 'r', encoding ='utf-8')
     text = f.read()
     if print_text==1:
         print(text)
     engine = pyttsx3.init()
     voices = engine.getProperty('voices')  
     engine.setProperty('voice', voices[voice].id)
     engine.setProperty("rate", rate)
     if save==1:
         import re
-        file_name = re.split('[/,\\\]', txt_path)[-1][:-4]
-        engine.save_to_file(text, file_name+'.mp3')
+        filename = re.split('[/,\\\]', txt_path)[-1][:-4]
+        engine.save_to_file(text, filename+'.mp3')
         engine.runAndWait()
         print('MP3 file saved!')
+        if compress==1:
+            import os
+            os.rename(filename+'.mp3', 'temp.mp3')
+            compress_mp3('temp.mp3', output_filename=filename+'.mp3', bitrate=bitrate)
+            os.remove('temp.mp3')
     if read==1:
         engine.say(text)
         engine.runAndWait()
 
-def pdf_to_audio(pdf_path, rate=125, voice=1, read=1, save=0, print_text=0):
+def pdf_to_audio(pdf_path, rate=125, voice=1, read=1, save=0, compress=0, bitrate='16k', print_text=0):
     import pyttsx3
     text = guan.pdf_to_text(pdf_path)
     text = text.replace('\n', ' ')
     if print_text==1:
         print(text)
     engine = pyttsx3.init()
     voices = engine.getProperty('voices')  
     engine.setProperty('voice', voices[voice].id)
     engine.setProperty("rate", rate)
     if save==1:
         import re
-        file_name = re.split('[/,\\\]', pdf_path)[-1][:-4]
-        engine.save_to_file(text, file_name+'.mp3')
+        filename = re.split('[/,\\\]', pdf_path)[-1][:-4]
+        engine.save_to_file(text, filename+'.mp3')
         engine.runAndWait()
         print('MP3 file saved!')
+        if compress==1:
+            import os
+            os.rename(filename+'.mp3', 'temp.mp3')
+            compress_mp3('temp.mp3', output_filename=filename+'.mp3', bitrate=bitrate)
+            os.remove('temp.mp3')
     if read==1:
         engine.say(text)
         engine.runAndWait()
 
+def compress_mp3(mp3_path, output_filename='a.mp3', bitrate='16k'):
+    # Note: Beside the installation of pydub, you may also need download FFmpeg on http://www.ffmpeg.org/download.html and add the bin path to the environment variable.
+    from pydub import AudioSegment
+    sound = AudioSegment.from_mp3(mp3_path)
+    sound.export(output_filename,format="mp3",bitrate=bitrate)
+
 ## words
 
 def play_academic_words(reverse=0, random_on=0, bre_or_ame='ame', show_translation=1, show_link=1, translation_time=2, rest_time=1):
     from bs4 import BeautifulSoup
     import re
     import urllib.request
     import requests
```

### Comparing `guan-0.0.98/src/guan.egg-info/PKG-INFO` & `guan-0.0.99/src/guan.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: guan
-Version: 0.0.98
+Version: 0.0.99
 Summary: An open source python package
 Home-page: https://py.guanjihuan.com
 Author: guanjihuan
 Author-email: guanjihuan@163.com
 Project-URL: Bug Tracker, https://py.guanjihuan.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
```

