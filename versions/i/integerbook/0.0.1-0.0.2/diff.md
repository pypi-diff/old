# Comparing `tmp/integerbook-0.0.1.tar.gz` & `tmp/integerbook-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "integerbook-0.0.1.tar", last modified: Sun Apr  2 11:44:47 2023, max compression
+gzip compressed data, was "integerbook-0.0.2.tar", last modified: Thu Apr  6 22:25:59 2023, max compression
```

## Comparing `integerbook-0.0.1.tar` & `integerbook-0.0.2.tar`

### file list

```diff
@@ -1,49 +1,49 @@
-drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-02 11:44:47.584550 integerbook-0.0.1/
--rw-r--r--   0 jvo        (501) staff       (20)    35149 2022-03-18 13:05:53.000000 integerbook-0.0.1/LICENSE
--rw-r--r--   0 jvo        (501) staff       (20)       84 2023-04-02 11:42:30.000000 integerbook-0.0.1/MANIFEST.in
--rw-r--r--   0 jvo        (501) staff       (20)    42493 2023-04-02 11:44:47.583972 integerbook-0.0.1/PKG-INFO
--rw-r--r--   0 jvo        (501) staff       (20)     1479 2023-03-21 13:10:54.000000 integerbook-0.0.1/README.md
--rw-r--r--   0 jvo        (501) staff       (20)      645 2023-04-02 11:43:44.000000 integerbook-0.0.1/pyproject.toml
--rw-r--r--   0 jvo        (501) staff       (20)       38 2023-04-02 11:44:47.584700 integerbook-0.0.1/setup.cfg
-drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-02 11:44:47.532984 integerbook-0.0.1/src/
-drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-02 11:44:47.544532 integerbook-0.0.1/src/integerbook/
--rw-r--r--   0 jvo        (501) staff       (20)     2475 2023-03-31 14:26:15.000000 integerbook-0.0.1/src/integerbook/CanvasCreator.py
--rw-r--r--   0 jvo        (501) staff       (20)     5918 2023-03-28 15:54:15.000000 integerbook-0.0.1/src/integerbook/LocationFinder.py
--rw-r--r--   0 jvo        (501) staff       (20)     9432 2023-03-31 14:52:41.000000 integerbook-0.0.1/src/integerbook/Settings.py
--rw-r--r--   0 jvo        (501) staff       (20)        0 2023-03-28 15:54:15.000000 integerbook-0.0.1/src/integerbook/__init__.py
-drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-02 11:44:47.556127 integerbook-0.0.1/src/integerbook/auxiliary_scripts/
--rw-r--r--   0 jvo        (501) staff       (20)        0 2023-03-28 15:54:15.000000 integerbook-0.0.1/src/integerbook/auxiliary_scripts/__init__.py
--rw-r--r--   0 jvo        (501) staff       (20)     6139 2023-03-28 15:54:15.000000 integerbook-0.0.1/src/integerbook/auxiliary_scripts/chordTypes.py
--rw-r--r--   0 jvo        (501) staff       (20)      680 2023-03-28 15:54:15.000000 integerbook-0.0.1/src/integerbook/auxiliary_scripts/createBatchJson.py
--rw-r--r--   0 jvo        (501) staff       (20)      173 2023-03-28 15:54:15.000000 integerbook-0.0.1/src/integerbook/auxiliary_scripts/printSettings.py
--rw-r--r--   0 jvo        (501) staff       (20)     1463 2023-03-28 15:56:16.000000 integerbook-0.0.1/src/integerbook/auxiliary_scripts/runMultiple.py
--rw-r--r--   0 jvo        (501) staff       (20)     3588 2023-03-28 15:54:15.000000 integerbook-0.0.1/src/integerbook/auxiliary_scripts/separateRealbook.py
--rw-r--r--   0 jvo        (501) staff       (20)      537 2023-03-28 15:54:15.000000 integerbook-0.0.1/src/integerbook/auxiliary_scripts/setMode.py
--rw-r--r--   0 jvo        (501) staff       (20)     1855 2023-03-28 15:56:16.000000 integerbook-0.0.1/src/integerbook/auxiliary_scripts/setModes.py
--rw-r--r--   0 jvo        (501) staff       (20)     1544 2023-03-28 15:54:15.000000 integerbook-0.0.1/src/integerbook/auxiliary_scripts/writeTexFile.py
--rw-r--r--   0 jvo        (501) staff       (20)      709 2023-03-28 15:54:15.000000 integerbook-0.0.1/src/integerbook/fontDimensions.json
--rw-r--r--   0 jvo        (501) staff       (20)     1374 2023-03-31 15:07:57.000000 integerbook-0.0.1/src/integerbook/fontSettings.json
-drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-02 11:44:47.556933 integerbook-0.0.1/src/integerbook/fonts/
--rw-r--r--   0 jvo        (501) staff       (20)     6148 2023-04-02 10:13:05.000000 integerbook-0.0.1/src/integerbook/fonts/.DS_Store
-drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-02 11:44:47.557699 integerbook-0.0.1/src/integerbook/fonts/Realbook/
--rw-r--r--   0 jvo        (501) staff       (20)    66232 2023-03-28 15:54:15.000000 integerbook-0.0.1/src/integerbook/fonts/Realbook/Realbook.ttf
-drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-02 11:44:47.561141 integerbook-0.0.1/src/integerbook/fonts/symbola/
--rw-r--r--   0 jvo        (501) staff       (20)  2240100 2023-03-28 15:54:15.000000 integerbook-0.0.1/src/integerbook/fonts/symbola/Symbola.ttf
--rw-r--r--   0 jvo        (501) staff       (20)     2205 2023-03-31 14:19:44.000000 integerbook-0.0.1/src/integerbook/main.py
-drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-02 11:44:47.581900 integerbook-0.0.1/src/integerbook/plotter/
--rw-r--r--   0 jvo        (501) staff       (20)    13336 2023-03-28 15:56:16.000000 integerbook-0.0.1/src/integerbook/plotter/PlotterBarLines.py
--rw-r--r--   0 jvo        (501) staff       (20)     1741 2023-03-28 15:54:15.000000 integerbook-0.0.1/src/integerbook/plotter/PlotterBase.py
--rw-r--r--   0 jvo        (501) staff       (20)    14194 2023-03-28 15:56:16.000000 integerbook-0.0.1/src/integerbook/plotter/PlotterChords.py
--rw-r--r--   0 jvo        (501) staff       (20)     1367 2023-03-28 15:56:16.000000 integerbook-0.0.1/src/integerbook/plotter/PlotterMain.py
--rw-r--r--   0 jvo        (501) staff       (20)     3121 2023-03-28 15:56:16.000000 integerbook-0.0.1/src/integerbook/plotter/PlotterMetadata.py
--rw-r--r--   0 jvo        (501) staff       (20)    22712 2023-03-31 15:07:40.000000 integerbook-0.0.1/src/integerbook/plotter/PlotterNotes.py
--rw-r--r--   0 jvo        (501) staff       (20)        0 2023-03-28 15:54:15.000000 integerbook-0.0.1/src/integerbook/plotter/__init__.py
--rw-r--r--   0 jvo        (501) staff       (20)    10373 2023-03-28 15:54:15.000000 integerbook-0.0.1/src/integerbook/plotter/patches.py
--rw-r--r--   0 jvo        (501) staff       (20)    10329 2023-03-31 15:06:45.000000 integerbook-0.0.1/src/integerbook/runSingle.py
--rw-r--r--   0 jvo        (501) staff       (20)     1455 2023-03-31 14:51:33.000000 integerbook-0.0.1/src/integerbook/settings.json
-drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-02 11:44:47.548002 integerbook-0.0.1/src/integerbook.egg-info/
--rw-r--r--   0 jvo        (501) staff       (20)    42493 2023-04-02 11:44:47.000000 integerbook-0.0.1/src/integerbook.egg-info/PKG-INFO
--rw-r--r--   0 jvo        (501) staff       (20)     1390 2023-04-02 11:44:47.000000 integerbook-0.0.1/src/integerbook.egg-info/SOURCES.txt
--rw-r--r--   0 jvo        (501) staff       (20)        1 2023-04-02 11:44:47.000000 integerbook-0.0.1/src/integerbook.egg-info/dependency_links.txt
--rw-r--r--   0 jvo        (501) staff       (20)       11 2023-04-02 11:44:47.000000 integerbook-0.0.1/src/integerbook.egg-info/requires.txt
--rw-r--r--   0 jvo        (501) staff       (20)       12 2023-04-02 11:44:47.000000 integerbook-0.0.1/src/integerbook.egg-info/top_level.txt
+drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-06 22:25:59.839844 integerbook-0.0.2/
+-rw-r--r--   0 jvo        (501) staff       (20)    35149 2022-03-18 13:05:53.000000 integerbook-0.0.2/LICENSE
+-rw-r--r--   0 jvo        (501) staff       (20)       84 2023-04-02 11:42:30.000000 integerbook-0.0.2/MANIFEST.in
+-rw-r--r--   0 jvo        (501) staff       (20)    42493 2023-04-06 22:25:59.839115 integerbook-0.0.2/PKG-INFO
+-rw-r--r--   0 jvo        (501) staff       (20)     1479 2023-03-21 13:10:54.000000 integerbook-0.0.2/README.md
+-rw-r--r--   0 jvo        (501) staff       (20)      645 2023-04-06 22:25:44.000000 integerbook-0.0.2/pyproject.toml
+-rw-r--r--   0 jvo        (501) staff       (20)       38 2023-04-06 22:25:59.840016 integerbook-0.0.2/setup.cfg
+drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-06 22:25:59.781892 integerbook-0.0.2/src/
+drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-06 22:25:59.793846 integerbook-0.0.2/src/integerbook/
+-rw-r--r--   0 jvo        (501) staff       (20)     2475 2023-03-31 14:26:15.000000 integerbook-0.0.2/src/integerbook/CanvasCreator.py
+-rw-r--r--   0 jvo        (501) staff       (20)     5918 2023-03-28 15:54:15.000000 integerbook-0.0.2/src/integerbook/LocationFinder.py
+-rw-r--r--   0 jvo        (501) staff       (20)     9562 2023-04-06 22:08:28.000000 integerbook-0.0.2/src/integerbook/Settings.py
+-rw-r--r--   0 jvo        (501) staff       (20)        0 2023-03-28 15:54:15.000000 integerbook-0.0.2/src/integerbook/__init__.py
+drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-06 22:25:59.806069 integerbook-0.0.2/src/integerbook/auxiliary_scripts/
+-rw-r--r--   0 jvo        (501) staff       (20)        0 2023-03-28 15:54:15.000000 integerbook-0.0.2/src/integerbook/auxiliary_scripts/__init__.py
+-rw-r--r--   0 jvo        (501) staff       (20)     6139 2023-03-28 15:54:15.000000 integerbook-0.0.2/src/integerbook/auxiliary_scripts/chordTypes.py
+-rw-r--r--   0 jvo        (501) staff       (20)      680 2023-03-28 15:54:15.000000 integerbook-0.0.2/src/integerbook/auxiliary_scripts/createBatchJson.py
+-rw-r--r--   0 jvo        (501) staff       (20)      173 2023-03-28 15:54:15.000000 integerbook-0.0.2/src/integerbook/auxiliary_scripts/printSettings.py
+-rw-r--r--   0 jvo        (501) staff       (20)     1463 2023-03-28 15:56:16.000000 integerbook-0.0.2/src/integerbook/auxiliary_scripts/runMultiple.py
+-rw-r--r--   0 jvo        (501) staff       (20)     3588 2023-03-28 15:54:15.000000 integerbook-0.0.2/src/integerbook/auxiliary_scripts/separateRealbook.py
+-rw-r--r--   0 jvo        (501) staff       (20)      537 2023-03-28 15:54:15.000000 integerbook-0.0.2/src/integerbook/auxiliary_scripts/setMode.py
+-rw-r--r--   0 jvo        (501) staff       (20)     1855 2023-03-28 15:56:16.000000 integerbook-0.0.2/src/integerbook/auxiliary_scripts/setModes.py
+-rw-r--r--   0 jvo        (501) staff       (20)     1544 2023-03-28 15:54:15.000000 integerbook-0.0.2/src/integerbook/auxiliary_scripts/writeTexFile.py
+-rw-r--r--   0 jvo        (501) staff       (20)      709 2023-03-28 15:54:15.000000 integerbook-0.0.2/src/integerbook/fontDimensions.json
+-rw-r--r--   0 jvo        (501) staff       (20)     1374 2023-03-31 15:07:57.000000 integerbook-0.0.2/src/integerbook/fontSettings.json
+drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-06 22:25:59.806887 integerbook-0.0.2/src/integerbook/fonts/
+-rw-r--r--   0 jvo        (501) staff       (20)     6148 2023-04-02 10:13:05.000000 integerbook-0.0.2/src/integerbook/fonts/.DS_Store
+drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-06 22:25:59.807965 integerbook-0.0.2/src/integerbook/fonts/Realbook/
+-rw-r--r--   0 jvo        (501) staff       (20)    66232 2023-03-28 15:54:15.000000 integerbook-0.0.2/src/integerbook/fonts/Realbook/Realbook.ttf
+drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-06 22:25:59.811404 integerbook-0.0.2/src/integerbook/fonts/symbola/
+-rw-r--r--   0 jvo        (501) staff       (20)  2240100 2023-03-28 15:54:15.000000 integerbook-0.0.2/src/integerbook/fonts/symbola/Symbola.ttf
+-rw-r--r--   0 jvo        (501) staff       (20)     2093 2023-04-06 22:23:15.000000 integerbook-0.0.2/src/integerbook/main.py
+drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-06 22:25:59.837138 integerbook-0.0.2/src/integerbook/plotter/
+-rw-r--r--   0 jvo        (501) staff       (20)    13336 2023-03-28 15:56:16.000000 integerbook-0.0.2/src/integerbook/plotter/PlotterBarLines.py
+-rw-r--r--   0 jvo        (501) staff       (20)     1741 2023-03-28 15:54:15.000000 integerbook-0.0.2/src/integerbook/plotter/PlotterBase.py
+-rw-r--r--   0 jvo        (501) staff       (20)    14194 2023-03-28 15:56:16.000000 integerbook-0.0.2/src/integerbook/plotter/PlotterChords.py
+-rw-r--r--   0 jvo        (501) staff       (20)     1367 2023-03-28 15:56:16.000000 integerbook-0.0.2/src/integerbook/plotter/PlotterMain.py
+-rw-r--r--   0 jvo        (501) staff       (20)     3121 2023-03-28 15:56:16.000000 integerbook-0.0.2/src/integerbook/plotter/PlotterMetadata.py
+-rw-r--r--   0 jvo        (501) staff       (20)    22712 2023-03-31 15:07:40.000000 integerbook-0.0.2/src/integerbook/plotter/PlotterNotes.py
+-rw-r--r--   0 jvo        (501) staff       (20)        0 2023-03-28 15:54:15.000000 integerbook-0.0.2/src/integerbook/plotter/__init__.py
+-rw-r--r--   0 jvo        (501) staff       (20)    10373 2023-03-28 15:54:15.000000 integerbook-0.0.2/src/integerbook/plotter/patches.py
+-rw-r--r--   0 jvo        (501) staff       (20)    10347 2023-04-06 22:23:15.000000 integerbook-0.0.2/src/integerbook/runSingle.py
+-rw-r--r--   0 jvo        (501) staff       (20)     1455 2023-03-31 14:51:33.000000 integerbook-0.0.2/src/integerbook/settings.json
+drwxr-xr-x   0 jvo        (501) staff       (20)        0 2023-04-06 22:25:59.797708 integerbook-0.0.2/src/integerbook.egg-info/
+-rw-r--r--   0 jvo        (501) staff       (20)    42493 2023-04-06 22:25:59.000000 integerbook-0.0.2/src/integerbook.egg-info/PKG-INFO
+-rw-r--r--   0 jvo        (501) staff       (20)     1390 2023-04-06 22:25:59.000000 integerbook-0.0.2/src/integerbook.egg-info/SOURCES.txt
+-rw-r--r--   0 jvo        (501) staff       (20)        1 2023-04-06 22:25:59.000000 integerbook-0.0.2/src/integerbook.egg-info/dependency_links.txt
+-rw-r--r--   0 jvo        (501) staff       (20)       11 2023-04-06 22:25:59.000000 integerbook-0.0.2/src/integerbook.egg-info/requires.txt
+-rw-r--r--   0 jvo        (501) staff       (20)       12 2023-04-06 22:25:59.000000 integerbook-0.0.2/src/integerbook.egg-info/top_level.txt
```

### Comparing `integerbook-0.0.1/LICENSE` & `integerbook-0.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/PKG-INFO` & `integerbook-0.0.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: integerbook
-Version: 0.0.1
+Version: 0.0.2
 Summary: sheet music converter
 Author-email: Jesse van Oostrum <integerbook@gmail.com>
 License:                     GNU GENERAL PUBLIC LICENSE
                                Version 3, 29 June 2007
         
          Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
          Everyone is permitted to copy and distribute verbatim copies
```

### Comparing `integerbook-0.0.1/README.md` & `integerbook-0.0.2/README.md`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/pyproject.toml` & `integerbook-0.0.2/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 [build-system]
 requires = ["setuptools>=61.0.0", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "integerbook"
-version = "0.0.1"
+version = "0.0.2"
 description = "sheet music converter"
 readme = "README.md"
 authors = [{ name = "Jesse van Oostrum", email = "integerbook@gmail.com" }]
 license = { file = "LICENSE" }
 classifiers = [
     "License :: OSI Approved :: MIT License",
     "Programming Language :: Python",
```

### Comparing `integerbook-0.0.1/src/integerbook/CanvasCreator.py` & `integerbook-0.0.2/src/integerbook/CanvasCreator.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/LocationFinder.py` & `integerbook-0.0.2/src/integerbook/LocationFinder.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/Settings.py` & `integerbook-0.0.2/src/integerbook/Settings.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,45 +1,24 @@
 import json
 import os
 
-from types import SimpleNamespace
 import music21
 
-from integerbook.plotter.PlotterBase import Plotter
 
+class Settings:
 
-class FontSettings:
-
-    def __init__(self, font):
-
-        pathFontDimensions = os.path.join(os.path.dirname(__file__), 'fontSettings.json')
-        f = open(pathFontDimensions)
-        fontSettings = json.load(f)
-        if font in fontSettings.keys():
-            fontSettings = fontSettings[font]
-        else:
-            fontSettings = fontSettings['DejaVu Sans']
-            print("no fontsettings available")
-
-        self.fontSizeType = fontSettings['fontSizeType']
-        self.fontSizeTypeSmall = fontSettings['fontSizeTypeSmall']
-        self.widthCharacter = fontSettings['widthCharacter']
-        self.widthMinus = fontSettings['widthMinus']
-        self.accidentalSpace = fontSettings['accidentalSpace']
-        self.accidentalSizeRelative = fontSettings["accidentalSizeRelative"]
-        self.widthDelta = fontSettings["widthDelta"]
-        self.widthCircle = fontSettings["widthCircle"]
-        self.spaceAddSus = fontSettings["spaceAddSus"]
-        self.accidentalXPositionRelative = fontSettings["accidentalXPositionRelative"]
-        self.hDistanceChordAddition = fontSettings['hDistanceChordAddition']
+    def __init__(self, streamObj, userSettings):
 
+        pathSettings = os.path.join(os.path.dirname(__file__), 'settings.json')
+        f = open(pathSettings)
+        settings = json.load(f)
 
-class Settings:
+        if userSettings:
+            settings.update(userSettings)
 
-    def __init__(self, streamObj, settings):
         self.streamObj = streamObj
         self.settings = settings
 
         self.measuresPerLine = settings['measuresPerLine']
         self.subdivision = settings['subdivision']
         self.fontSizeNotes = settings['fontSizeNotes']
         self.fontSizeGraceNotesPerFontSizeNotes = settings['fontSizeGraceNotesPerFontSizeNotes']
@@ -223,8 +202,33 @@
                     maxNumLines = numLines
 
         return maxNumLines
 
 
     def _getLengthFirstMeasure(self):
         length = self.streamObj.measure(1)[music21.stream.Measure][0].quarterLength
-        return length
+        return length
+
+class FontSettings:
+
+    def __init__(self, font):
+
+        pathFontDimensions = os.path.join(os.path.dirname(__file__), 'fontSettings.json')
+        f = open(pathFontDimensions)
+        fontSettings = json.load(f)
+        if font in fontSettings.keys():
+            fontSettings = fontSettings[font]
+        else:
+            fontSettings = fontSettings['DejaVu Sans']
+            print("no fontsettings available")
+
+        self.fontSizeType = fontSettings['fontSizeType']
+        self.fontSizeTypeSmall = fontSettings['fontSizeTypeSmall']
+        self.widthCharacter = fontSettings['widthCharacter']
+        self.widthMinus = fontSettings['widthMinus']
+        self.accidentalSpace = fontSettings['accidentalSpace']
+        self.accidentalSizeRelative = fontSettings["accidentalSizeRelative"]
+        self.widthDelta = fontSettings["widthDelta"]
+        self.widthCircle = fontSettings["widthCircle"]
+        self.spaceAddSus = fontSettings["spaceAddSus"]
+        self.accidentalXPositionRelative = fontSettings["accidentalXPositionRelative"]
+        self.hDistanceChordAddition = fontSettings['hDistanceChordAddition']
```

### Comparing `integerbook-0.0.1/src/integerbook/auxiliary_scripts/chordTypes.py` & `integerbook-0.0.2/src/integerbook/auxiliary_scripts/chordTypes.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/auxiliary_scripts/createBatchJson.py` & `integerbook-0.0.2/src/integerbook/auxiliary_scripts/createBatchJson.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/auxiliary_scripts/runMultiple.py` & `integerbook-0.0.2/src/integerbook/auxiliary_scripts/runMultiple.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/auxiliary_scripts/separateRealbook.py` & `integerbook-0.0.2/src/integerbook/auxiliary_scripts/separateRealbook.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/auxiliary_scripts/setMode.py` & `integerbook-0.0.2/src/integerbook/auxiliary_scripts/setMode.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/auxiliary_scripts/setModes.py` & `integerbook-0.0.2/src/integerbook/auxiliary_scripts/setModes.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/auxiliary_scripts/writeTexFile.py` & `integerbook-0.0.2/src/integerbook/auxiliary_scripts/writeTexFile.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/fontDimensions.json` & `integerbook-0.0.2/src/integerbook/fontDimensions.json`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/fontSettings.json` & `integerbook-0.0.2/src/integerbook/fontSettings.json`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/fonts/.DS_Store` & `integerbook-0.0.2/src/integerbook/fonts/.DS_Store`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/fonts/Realbook/Realbook.ttf` & `integerbook-0.0.2/src/integerbook/fonts/Realbook/Realbook.ttf`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/fonts/symbola/Symbola.ttf` & `integerbook-0.0.2/src/integerbook/fonts/symbola/Symbola.ttf`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/main.py` & `integerbook-0.0.2/src/integerbook/main.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,54 +1,49 @@
 """Jesse van Oostrum"""
-import json
-import os
-
 import music21
 
 from integerbook.plotter.PlotterMain import PlotterMain
 from integerbook.LocationFinder import LocationFinder
 from integerbook.CanvasCreator import CanvasCreator
 from integerbook.Settings import Settings
 
 
 class Visualiser:
     """class for making visualisations from a music21 stream"""
 
-    def __init__(self, pathToSong, settings=None):
+    def __init__(self, pathToSong, userSettings=None):
 
         streamObj = music21.converter.parse(pathToSong)
 
         self.streamObj = self._preprocessStreamObj(streamObj)
 
-        if not settings:
-            pathSettings = os.path.join(os.path.dirname(__file__), 'settings.json')
-            f = open(pathSettings)
-            settings = json.load(f)
-
-        self.Settings = Settings(streamObj, settings)
+        self.Settings = Settings(streamObj, userSettings)
 
         self.LocationFinder = LocationFinder(self.streamObj, self.Settings)
 
         yPosLowest = self.LocationFinder.getYPosLineBase(-1)
         self.CanvasCreator = CanvasCreator(self.Settings, self.LocationFinder.getNumPages(), yPosLowest)
 
         self.PlotterMain = PlotterMain(streamObj, self.Settings, self.LocationFinder, self.CanvasCreator.getAxs())
 
         self.PlotterMain.plot()
 
     def getSongTitle(self):
         return self.PlotterMain.PlotterMetadata.getSongTitle()
 
     def saveFig(self, dirName=None, buffer=None):
-        if dirName:
+        if buffer:
+            self.CanvasCreator.saveFig(buffer)
+        else:
             title = self.getSongTitle()
-            pathName = dirName + '/' + title + '.pdf'
+            if not dirName:
+                pathName = title + '.pdf'
+            else:
+                pathName = dirName + '/' + title + '.pdf'
             self.CanvasCreator.saveFig(pathName)
-        elif buffer:
-            self.CanvasCreator.saveFig(buffer)
 
     def _preprocessStreamObj(self, streamObj):
 
         streamObj = self._removeBassStaff(streamObj)
 
         return streamObj
```

### Comparing `integerbook-0.0.1/src/integerbook/plotter/PlotterBarLines.py` & `integerbook-0.0.2/src/integerbook/plotter/PlotterBarLines.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/plotter/PlotterBase.py` & `integerbook-0.0.2/src/integerbook/plotter/PlotterBase.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/plotter/PlotterChords.py` & `integerbook-0.0.2/src/integerbook/plotter/PlotterChords.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/plotter/PlotterMain.py` & `integerbook-0.0.2/src/integerbook/plotter/PlotterMain.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/plotter/PlotterMetadata.py` & `integerbook-0.0.2/src/integerbook/plotter/PlotterMetadata.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/plotter/PlotterNotes.py` & `integerbook-0.0.2/src/integerbook/plotter/PlotterNotes.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/plotter/patches.py` & `integerbook-0.0.2/src/integerbook/plotter/patches.py`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook/runSingle.py` & `integerbook-0.0.2/src/integerbook/runSingle.py`

 * *Files 1% similar despite different names*

```diff
@@ -78,17 +78,18 @@
 song72 = "/Users/jvo/Downloads/Summertime in G.musicxml"
 song73 = '/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/bladmuziek/ultimate-guitar-top-100/Hallelujah__Leonard_Cohen_Lead_sheet_with_lyrics_.mxl'
 song74 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/bladmuziek/ultimate-guitar-top-100/2021 -- HALLELUJAH RJS mods.mscz"
 song75 = "/Users/jvo/Downloads/tempMxl/2021 -- HALLELUJAH RJS mods.musicxml"
 song76 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/bladmuziek/musescore/Think_About_Things_-_Iceland_Eurovision_2020_-_Dai_Freyr-Part.mscz"
 song77 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/bladmuziek/popular_sheets/All_Of_Me.musicxml"
 
-f = open('Settings.json')
-settings = json.load(f)
+# f = open('Settings.json')
+# settings = json.load(f)
 
+settings = {}
 settings["measuresPerLine"] = 4
 settings["subdivision"] = 0
 settings["setInMajorKey"] = True
 settings["lyrics"] = True
 settings['coloursVoices'] = False
 settings['coloursCircleOfFifths'] = False
 settings['thickBarlines'] = False
```

### Comparing `integerbook-0.0.1/src/integerbook/settings.json` & `integerbook-0.0.2/src/integerbook/settings.json`

 * *Files identical despite different names*

### Comparing `integerbook-0.0.1/src/integerbook.egg-info/PKG-INFO` & `integerbook-0.0.2/src/integerbook.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: integerbook
-Version: 0.0.1
+Version: 0.0.2
 Summary: sheet music converter
 Author-email: Jesse van Oostrum <integerbook@gmail.com>
 License:                     GNU GENERAL PUBLIC LICENSE
                                Version 3, 29 June 2007
         
          Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
          Everyone is permitted to copy and distribute verbatim copies
```

### Comparing `integerbook-0.0.1/src/integerbook.egg-info/SOURCES.txt` & `integerbook-0.0.2/src/integerbook.egg-info/SOURCES.txt`

 * *Files identical despite different names*

