# Comparing `tmp/pitchcontext-0.1.6.tar.gz` & `tmp/pitchcontext-0.1.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pitchcontext-0.1.6.tar", max compression
+gzip compressed data, was "pitchcontext-0.1.7.tar", max compression
```

## Comparing `pitchcontext-0.1.6.tar` & `pitchcontext-0.1.7.tar`

### file list

```diff
@@ -1,13 +1,13 @@
--rw-r--r--   0        0        0     1072 2022-12-16 21:51:34.158842 pitchcontext-0.1.6/LICENSE
--rw-r--r--   0        0        0     1208 2023-03-17 11:35:54.057500 pitchcontext-0.1.6/README.md
--rw-r--r--   0        0        0      681 2023-04-07 12:04:16.619832 pitchcontext-0.1.6/pyproject.toml
--rw-r--r--   0        0        0     9797 2023-04-02 19:11:53.720006 pitchcontext-0.1.6/src/pitchcontext/ComputePitchContext.py
--rw-r--r--   0        0        0     3066 2023-01-25 21:05:35.934401 pitchcontext-0.1.6/src/pitchcontext/PCParameters.py
--rw-r--r--   0        0        0       62 2022-12-16 22:10:25.821160 pitchcontext-0.1.6/src/pitchcontext/__init__.py
--rw-r--r--   0        0        0      852 2023-01-16 19:32:07.285987 pitchcontext-0.1.6/src/pitchcontext/base40.py
--rw-r--r--   0        0        0    31798 2023-04-07 00:19:25.126995 pitchcontext-0.1.6/src/pitchcontext/models.py
--rw-r--r--   0        0        0    16525 2023-03-14 19:18:30.210423 pitchcontext-0.1.6/src/pitchcontext/pitchcontext.py
--rw-r--r--   0        0        0    30871 2023-04-07 00:34:12.110009 pitchcontext-0.1.6/src/pitchcontext/song.py
--rw-r--r--   0        0        0     2304 2023-01-25 15:23:58.099005 pitchcontext-0.1.6/src/pitchcontext/visualize.py
--rw-r--r--   0        0        0     2169 1970-01-01 00:00:00.000000 pitchcontext-0.1.6/setup.py
--rw-r--r--   0        0        0     1999 1970-01-01 00:00:00.000000 pitchcontext-0.1.6/PKG-INFO
+-rw-r--r--   0        0        0     1072 2022-12-16 21:51:34.158842 pitchcontext-0.1.7/LICENSE
+-rw-r--r--   0        0        0     1208 2023-03-17 11:35:54.057500 pitchcontext-0.1.7/README.md
+-rw-r--r--   0        0        0      681 2023-04-07 12:56:39.037316 pitchcontext-0.1.7/pyproject.toml
+-rw-r--r--   0        0        0     9797 2023-04-02 19:11:53.720006 pitchcontext-0.1.7/src/pitchcontext/ComputePitchContext.py
+-rw-r--r--   0        0        0     3066 2023-01-25 21:05:35.934401 pitchcontext-0.1.7/src/pitchcontext/PCParameters.py
+-rw-r--r--   0        0        0       62 2022-12-16 22:10:25.821160 pitchcontext-0.1.7/src/pitchcontext/__init__.py
+-rw-r--r--   0        0        0      852 2023-01-16 19:32:07.285987 pitchcontext-0.1.7/src/pitchcontext/base40.py
+-rw-r--r--   0        0        0    31798 2023-04-07 00:19:25.126995 pitchcontext-0.1.7/src/pitchcontext/models.py
+-rw-r--r--   0        0        0    16525 2023-03-14 19:18:30.210423 pitchcontext-0.1.7/src/pitchcontext/pitchcontext.py
+-rw-r--r--   0        0        0    31046 2023-04-07 12:55:33.025340 pitchcontext-0.1.7/src/pitchcontext/song.py
+-rw-r--r--   0        0        0     2304 2023-01-25 15:23:58.099005 pitchcontext-0.1.7/src/pitchcontext/visualize.py
+-rw-r--r--   0        0        0     2169 1970-01-01 00:00:00.000000 pitchcontext-0.1.7/setup.py
+-rw-r--r--   0        0        0     1999 1970-01-01 00:00:00.000000 pitchcontext-0.1.7/PKG-INFO
```

### Comparing `pitchcontext-0.1.6/LICENSE` & `pitchcontext-0.1.7/LICENSE`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.6/README.md` & `pitchcontext-0.1.7/README.md`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.6/pyproject.toml` & `pitchcontext-0.1.7/pyproject.toml`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "pitchcontext"
-version = "0.1.6"
+version = "0.1.7"
 description = "Library for melody analysis based on pitch context vectors."
 authors = ["Peter van Kranenburg <peter.van.kranenburg@meertens.knaw.nl>"]
 readme = "README.md"
 packages = [{include = "pitchcontext", from = "src"}]
 
 [tool.poetry.dependencies]
 #streamlit is not compatible with Python 3.9.7
```

### Comparing `pitchcontext-0.1.6/src/pitchcontext/ComputePitchContext.py` & `pitchcontext-0.1.7/src/pitchcontext/ComputePitchContext.py`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.6/src/pitchcontext/PCParameters.py` & `pitchcontext-0.1.7/src/pitchcontext/PCParameters.py`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.6/src/pitchcontext/base40.py` & `pitchcontext-0.1.7/src/pitchcontext/base40.py`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.6/src/pitchcontext/models.py` & `pitchcontext-0.1.7/src/pitchcontext/models.py`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.6/src/pitchcontext/pitchcontext.py` & `pitchcontext-0.1.7/src/pitchcontext/pitchcontext.py`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.6/src/pitchcontext/song.py` & `pitchcontext-0.1.7/src/pitchcontext/song.py`

 * *Files 1% similar despite different names*

```diff
@@ -460,15 +460,15 @@
             for ix in range(len(mtcsong_new['features']['onsettick'])):
                 mtcsong_new['features']['onsettick'][ix] = int( mtcsong_new['features']['onsettick'][ix] / onsetgcd )
 
         song_new = Song(mtcsong_new, None, s_in=s_new, beatstrength_grid_in=beatstrength_grid_new)
         return song_new
 
 
-    def getColoredSong(self, colordict, lyrics=None, lyrics_ixs=None):
+    def getColoredSong(self, colordict, lyrics=None, lyrics_ixs=None, title=None):
         """Create a new music21 stream with notes colored according to `colordict`.
 
         Parameters
         ----------
         colordict : dict
             The keys are the colors, the values the indices of the notes with that color. E.g. {'red':[0,10,11],'grey':[-1]}
             colors notes at indices 0, 10, and 11 red, and the last note grey.
@@ -483,14 +483,16 @@
         music21 Stream
             music21 Stream.
         """
         if self.reduced:
             s = copy.deepcopy(self.s)
         else:
             s = self.parseMelody()
+        if title != None:
+            s.metadata.title = title
         #check for right length #if so, assume notes correspond with features
         assert self.getSongLength() == len(s.flat.notes)
         for color, ixs in colordict.items():
             for ix in ixs:
                 s.flat.notes[int(ix)].style.color = color
         #add index of note as lyric
         if lyrics == None:
@@ -588,15 +590,15 @@
             lines = [l for l in f.readlines()]
         with open(filename,'w') as f:
             for l in lines:
                 f.write(l)
                 if "\\version" in l:
                     f.write( "\paper { system-system-spacing.basic-distance = #16 }\n" )
 
-    def createColoredPDF(self, colordict, outputpath, filebasename=None, showfilename=True, lyrics=None, lyrics_ixs=None):
+    def createColoredPDF(self, colordict, outputpath, filebasename=None, showfilename=True, lyrics=None, lyrics_ixs=None, title=None):
         """Create a pdf with a score with colored notes.
 
         Parameters
         ----------
         colordict : dict
             The keys are the colors, the values the indices of the notes with that color. E.g. {'red':[0,10,11],'grey':[-1]}
             colors notes at indices 0, 10, and 11 red, and the last note grey.
@@ -611,24 +613,24 @@
         Returns
         -------
         path-like object
             Full path of the generated pdf.
         """
         if filebasename == None:
             filebasename = self.mtcsong['id']
-        s = self.getColoredSong(colordict, lyrics=lyrics, lyrics_ixs=lyrics_ixs)
+        s = self.getColoredSong(colordict, lyrics=lyrics, lyrics_ixs=lyrics_ixs, title=title)
         s.write('lily', os.path.join(outputpath, filebasename+'.ly'))
         self.formatAndRepairLy(os.path.join(outputpath, filebasename+'.ly'))
         if showfilename:
             self.insertFilenameLy(os.path.join(outputpath, filebasename+'.ly'))
         self.insertSystemSpacingLy(os.path.join(outputpath, filebasename+'.ly'))
         output = subprocess.run(["lilypond", os.path.join(outputpath, filebasename+'.ly')], cwd=outputpath, capture_output=True)
         return os.path.join(outputpath, filebasename+'.pdf')
 
-    def createColoredPNG(self, colordict, outputpath, filebasename=None, showfilename=True, lyrics=None, lyrics_ixs=None):
+    def createColoredPNG(self, colordict, outputpath, filebasename=None, showfilename=True, lyrics=None, lyrics_ixs=None, title=None):
         """Create a png with a score with colored notes.
 
         Parameters
         ----------
         colordict : dict
             The keys are the colors, the values the indices of the notes with that color. E.g. {'red':[0,10,11],'grey':[-1]}
             colors notes at indices 0, 10, and 11 red, and the last note grey.
@@ -641,20 +643,20 @@
             Include the filename in the png (lilypond opus header).
 
         Returns
         -------
         path-like object
             Full path of the generated png.
         """
-        pdf_fn = self.createColoredPDF(colordict, outputpath, filebasename, showfilename, lyrics=lyrics, lyrics_ixs=lyrics_ixs)
+        pdf_fn = self.createColoredPDF(colordict, outputpath, filebasename, showfilename, lyrics=lyrics, lyrics_ixs=lyrics_ixs, title=title)
         png_fn = pdf_fn.replace('.pdf','.png')
         output = subprocess.run(['convert', '-density', '100', pdf_fn, '-alpha', 'Remove', '-trim', png_fn], cwd=outputpath, capture_output=True)
         return png_fn
     
-    def showColoredPNG(self, colordict, outputpath, filebasename=None, showfilename=True, lyrics=None, lyrics_ixs=None):
+    def showColoredPNG(self, colordict, outputpath, filebasename=None, showfilename=True, lyrics=None, lyrics_ixs=None, title=None):
         """Show a png with a score with colored notes. For use in a Jupyter notebook.
 
         Parameters
         ----------
         colordict : dict
             The keys are the colors, the values the indices of the notes with that color. E.g. {'red':[0,10,11],'grey':[-1]}
             colors notes at indices 0, 10, and 11 red, and the last note grey.
@@ -662,25 +664,25 @@
             name of the output directory
         filebasename : str, default None
             basename of the png file to generate (without .png). If None, the identifier of the song as provided by
             MTCFeatures is used as file name.
         showfilename : bool, default True
             Include the filename in the png (lilypond opus header).
         """
-        png_fn = self.createColoredPNG(colordict, outputpath, filebasename, showfilename, lyrics=lyrics, lyrics_ixs=lyrics_ixs)
+        png_fn = self.createColoredPNG(colordict, outputpath, filebasename, showfilename, lyrics=lyrics, lyrics_ixs=lyrics_ixs, title=title)
         display.display(display.Image(png_fn))
 
     def showPNG(self, lyrics=None, lyrics_ixs=None):
         """Show a png with a score of the song. For use in a Jupyter notebook.
         """
         with tempfile.TemporaryDirectory() as tmpdirname:
             self.showColoredPNG({}, tmpdirname, showfilename=False, lyrics=lyrics, lyrics_ixs=lyrics_ixs)
     
-    def createPNG(self, outputpath, filebasename=None, showfilename=False, lyrics=None, lyrics_ixs=None):
-        return self.createColoredPNG({}, outputpath, filebasename=filebasename, showfilename=showfilename, lyrics=lyrics, lyrics_ixs=lyrics_ixs)
+    def createPNG(self, outputpath, filebasename=None, showfilename=False, lyrics=None, lyrics_ixs=None, title=None):
+        return self.createColoredPNG({}, outputpath, filebasename=filebasename, showfilename=showfilename, lyrics=lyrics, lyrics_ixs=lyrics_ixs, title=title)
 
 
     def writeMTCJSON(self, outputpath, filebasename=None):
         if filebasename == None:
             filebasename = self.mtcsong['id']        
         with open(os.path.join(outputpath,filebasename+'.json'), 'w') as f:
             json.dump(self.mtcsong, f)
```

### Comparing `pitchcontext-0.1.6/src/pitchcontext/visualize.py` & `pitchcontext-0.1.7/src/pitchcontext/visualize.py`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.6/setup.py` & `pitchcontext-0.1.7/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -15,15 +15,15 @@
  'matplotlib>=3.3,<4.0',
  'music21>=8.0,<9.0',
  'numpy>=1.19,<2.0',
  'seaborn>=0.12.1,<0.13.0']
 
 setup_kwargs = {
     'name': 'pitchcontext',
-    'version': '0.1.6',
+    'version': '0.1.7',
     'description': 'Library for melody analysis based on pitch context vectors.',
     'long_description': '---\ncomponent-id: pitchcontext\nname: pitchcontext\ndescription: Python module for melody analysis based on pitch context vectors.\ntype: Library\nrelease-date: 2023-03-15\nrelease-number: 0.1.4\nwork-package: WP3\npilot: TUNES\nkeywords:\n  - melody\n  - pitch analysis\nchangelog:\nlicence:\nrelease link:\n--- \n\n\n# pitchcontext\nPython module for melody analysis based on pitch context vectors.\n\n## Prerequisites:\n- lilypond installed and in command line path\n- convert (ImageMagick) installed and in command line path\n- kernfiles and corresponding .json files with melodic features\n\n## Installation\nThe latest release of the pitchcontext module can be installed from pypi:\n```\n$ pip install pitchcontext\n```\n\nThe development version can be installed by cloning the repository and by using the provided pyproject.toml and poetry. In root of the rep do:\n```\n$ poetry install\n```\nThis creates a virtual environment with pitchcontext installed.\n\n## Examples\nRequires a Python3 environment with both pitchcontext and streamlit installed.\nTwo examples are provided:\n- apps/st_dissonance.py\n- apps/st_novelty.py\n\nTo run:\n```\n$ streamlit run st_dissonance.py -- -krnpath <path_to_kern_files> -jsonpath <path_to_json_files>\n```\n',
     'author': 'Peter van Kranenburg',
     'author_email': 'peter.van.kranenburg@meertens.knaw.nl',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `pitchcontext-0.1.6/PKG-INFO` & `pitchcontext-0.1.7/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pitchcontext
-Version: 0.1.6
+Version: 0.1.7
 Summary: Library for melody analysis based on pitch context vectors.
 Author: Peter van Kranenburg
 Author-email: peter.van.kranenburg@meertens.knaw.nl
 Requires-Python: >=3.8, !=2.7.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

