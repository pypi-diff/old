# Comparing `tmp/pitchcontext-0.1.7.tar.gz` & `tmp/pitchcontext-0.1.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pitchcontext-0.1.7.tar", max compression
+gzip compressed data, was "pitchcontext-0.1.8.tar", max compression
```

## Comparing `pitchcontext-0.1.7.tar` & `pitchcontext-0.1.8.tar`

### file list

```diff
@@ -1,13 +1,13 @@
--rw-r--r--   0        0        0     1072 2022-12-16 21:51:34.158842 pitchcontext-0.1.7/LICENSE
--rw-r--r--   0        0        0     1208 2023-03-17 11:35:54.057500 pitchcontext-0.1.7/README.md
--rw-r--r--   0        0        0      681 2023-04-07 12:56:39.037316 pitchcontext-0.1.7/pyproject.toml
--rw-r--r--   0        0        0     9797 2023-04-02 19:11:53.720006 pitchcontext-0.1.7/src/pitchcontext/ComputePitchContext.py
--rw-r--r--   0        0        0     3066 2023-01-25 21:05:35.934401 pitchcontext-0.1.7/src/pitchcontext/PCParameters.py
--rw-r--r--   0        0        0       62 2022-12-16 22:10:25.821160 pitchcontext-0.1.7/src/pitchcontext/__init__.py
--rw-r--r--   0        0        0      852 2023-01-16 19:32:07.285987 pitchcontext-0.1.7/src/pitchcontext/base40.py
--rw-r--r--   0        0        0    31798 2023-04-07 00:19:25.126995 pitchcontext-0.1.7/src/pitchcontext/models.py
--rw-r--r--   0        0        0    16525 2023-03-14 19:18:30.210423 pitchcontext-0.1.7/src/pitchcontext/pitchcontext.py
--rw-r--r--   0        0        0    31046 2023-04-07 12:55:33.025340 pitchcontext-0.1.7/src/pitchcontext/song.py
--rw-r--r--   0        0        0     2304 2023-01-25 15:23:58.099005 pitchcontext-0.1.7/src/pitchcontext/visualize.py
--rw-r--r--   0        0        0     2169 1970-01-01 00:00:00.000000 pitchcontext-0.1.7/setup.py
--rw-r--r--   0        0        0     1999 1970-01-01 00:00:00.000000 pitchcontext-0.1.7/PKG-INFO
+-rw-r--r--   0        0        0     1072 2022-12-16 21:51:34.158842 pitchcontext-0.1.8/LICENSE
+-rw-r--r--   0        0        0     1208 2023-03-17 11:35:54.057500 pitchcontext-0.1.8/README.md
+-rw-r--r--   0        0        0      681 2023-04-07 13:15:02.489706 pitchcontext-0.1.8/pyproject.toml
+-rw-r--r--   0        0        0     9797 2023-04-02 19:11:53.720006 pitchcontext-0.1.8/src/pitchcontext/ComputePitchContext.py
+-rw-r--r--   0        0        0     3066 2023-01-25 21:05:35.934401 pitchcontext-0.1.8/src/pitchcontext/PCParameters.py
+-rw-r--r--   0        0        0       62 2022-12-16 22:10:25.821160 pitchcontext-0.1.8/src/pitchcontext/__init__.py
+-rw-r--r--   0        0        0      852 2023-01-16 19:32:07.285987 pitchcontext-0.1.8/src/pitchcontext/base40.py
+-rw-r--r--   0        0        0    32071 2023-04-07 13:13:15.197912 pitchcontext-0.1.8/src/pitchcontext/models.py
+-rw-r--r--   0        0        0    16525 2023-03-14 19:18:30.210423 pitchcontext-0.1.8/src/pitchcontext/pitchcontext.py
+-rw-r--r--   0        0        0    31046 2023-04-07 12:55:33.025340 pitchcontext-0.1.8/src/pitchcontext/song.py
+-rw-r--r--   0        0        0     2304 2023-01-25 15:23:58.099005 pitchcontext-0.1.8/src/pitchcontext/visualize.py
+-rw-r--r--   0        0        0     2169 1970-01-01 00:00:00.000000 pitchcontext-0.1.8/setup.py
+-rw-r--r--   0        0        0     1999 1970-01-01 00:00:00.000000 pitchcontext-0.1.8/PKG-INFO
```

### Comparing `pitchcontext-0.1.7/LICENSE` & `pitchcontext-0.1.8/LICENSE`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.7/README.md` & `pitchcontext-0.1.8/README.md`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.7/pyproject.toml` & `pitchcontext-0.1.8/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "pitchcontext"
-version = "0.1.7"
+version = "0.1.8"
 description = "Library for melody analysis based on pitch context vectors."
 authors = ["Peter van Kranenburg <peter.van.kranenburg@meertens.knaw.nl>"]
 readme = "README.md"
 packages = [{include = "pitchcontext", from = "src"}]
 
 [tool.poetry.dependencies]
 #streamlit is not compatible with Python 3.9.7
```

### Comparing `pitchcontext-0.1.7/src/pitchcontext/ComputePitchContext.py` & `pitchcontext-0.1.8/src/pitchcontext/ComputePitchContext.py`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.7/src/pitchcontext/PCParameters.py` & `pitchcontext-0.1.8/src/pitchcontext/PCParameters.py`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.7/src/pitchcontext/base40.py` & `pitchcontext-0.1.8/src/pitchcontext/base40.py`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.7/src/pitchcontext/models.py` & `pitchcontext-0.1.8/src/pitchcontext/models.py`

 * *Files 4% similar despite different names*

```diff
@@ -433,35 +433,37 @@
         for ix in range(seq_length):
             diff_prev = np.abs(ix - mostrecent[ix])
             diff_next = np.abs(mostnext[ix] - ix)
             next_ixs = np.where(diff_prev > diff_next)[0]
             prev_ixs = np.where(diff_prev <= diff_next)[0]
             #from prev context
             for scale_ix in prev_ixs:
-                p40 = self.getP40( self.wpc.ixs[ mostrecent[ix][scale_ix] ] )
-                scalemask[ix, p40] = True
-                naturals[naturalsix[p40]] = False
+                if mostrecent[ix][scale_ix] != 1000:
+                    p40 = self.getP40( self.wpc.ixs[ mostrecent[ix][scale_ix] ] )
+                    scalemask[ix, p40] = True
+                    naturals[naturalsix[p40]] = False
             #take from next context
             for scale_ix in next_ixs:
-                p40 = self.getP40( self.wpc.ixs[ mostnext[ix][scale_ix] ] )
-                scalemask[ix, p40] = True
-                naturals[naturalsix[p40]] = False
+                if mostnext[ix][scale_ix] != -1000:
+                    p40 = self.getP40( self.wpc.ixs[ mostnext[ix][scale_ix] ] )
+                    scalemask[ix, p40] = True
+                    naturals[naturalsix[p40]] = False
 
         # scalemask = np.zeros(40)
         # for ix in range(self.wpc.pitchcontext.shape[0]):
         #     p40 = (self.song.mtcsong['features']['pitch40'][ix] - 1) % 40
         #     scalemask[p40] = True
         #     naturals[naturalsix[p40]] = False
 
         # now extend each 
         # missing stem tones should be missing in all scalemasks, but addition might differ
 
         if extendToAllNaturalTones:
 
-            for ix in range(seq_length):
+            for seq_ix in range(seq_length):
 
                 #add missing tones
                 #flats
                 for ix in sorted(list(np.where(naturals)[0])): #from F->B order is important, more than one tone might be missing. first fix tones far away from C
                     #figure out whether to add flat
 
                     missing       = naturalixs[ix]
@@ -472,36 +474,36 @@
                     fifthupflat   = fifthup - 1
                     fifthupsharp  = fifthup + 1
 
                     #### SOLVE MINOR, leading tone (if not in melody)
 
                     if ix == 0:
                         #When Fb? Only if Cb is present
-                        if scalemask[ix,fifthupflat]:
-                            scalemask[ix,missingflat] = True
+                        if scalemask[seq_ix,fifthupflat]:
+                            scalemask[seq_ix,missingflat] = True
                         #when F? If no C#
-                        if not scalemask[ix,fifthupsharp]:
-                            scalemask[ix,missing] = True
+                        if not scalemask[seq_ix,fifthupsharp]:
+                            scalemask[seq_ix,missing] = True
                         continue
                     
                     if ix == 6: #Bb ?
                         #When Bb? If Eb is present or if F is present
-                        if scalemask[ix,fifthdownflat] or scalemask[ix,fifthup]:
-                            scalemask[ix,missingflat] = True
+                        if scalemask[seq_ix,fifthdownflat] or scalemask[seq_ix,fifthup]:
+                            scalemask[seq_ix,missingflat] = True
                         #when B? always - We deal with B# below
-                        scalemask[ix,missing] = True
+                        scalemask[seq_ix,missing] = True
                         continue
 
-                    if scalemask[ix,fifthdownflat]:
-                        scalemask[ix,missingflat] = True
-                    elif scalemask[ix,fifthdown] and scalemask[ix,fifthup]:
-                        scalemask[ix,missing] = True
-                    elif scalemask[ix,fifthdown] and scalemask[ix,fifthupflat]:
-                        scalemask[ix,missingflat] = True
-                        scalemask[ix,missing] = True
+                    if scalemask[seq_ix,fifthdownflat]:
+                        scalemask[seq_ix,missingflat] = True
+                    elif scalemask[seq_ix,fifthdown] and scalemask[seq_ix,fifthup]:
+                        scalemask[seq_ix,missing] = True
+                    elif scalemask[seq_ix,fifthdown] and scalemask[seq_ix,fifthupflat]:
+                        scalemask[seq_ix,missingflat] = True
+                        scalemask[seq_ix,missing] = True
 
                 #sharps
                 for ix in sorted(list(np.where(naturals)[0]), reverse=True): #from B->F order is important, more than one tone might be missing. first fix tones far away from C
                     
                     #figure out whether to add flat
 
                     missing        = naturalixs[ix]
@@ -510,37 +512,37 @@
                     fifthdownsharp = fifthdown + 1
                     fifthup        = naturalixs[(ix + 1) % 7]
                     fifthupsharp   = fifthup + 1
                     fifthupflat    = fifthup - 1
 
                     if ix == 6: # B#?
                         #when B#? If E# present
-                        if scalemask[ix,fifthdownsharp]:
-                            scalemask[ix,missingsharp] = True
+                        if scalemask[seq_ix,fifthdownsharp]:
+                            scalemask[seq_ix,missingsharp] = True
                         #when B? when No flats (i.e. no Eb)
-                        if not scalemask[ix,fifthdownflat]:
-                            scalemask[ix,missing] = True
+                        if not scalemask[seq_ix,fifthdownflat]:
+                            scalemask[seq_ix,missing] = True
                         continue
 
                     if ix == 0: # F#?
                         #when F#? If C# present or if B present
-                        if scalemask[ix,fifthupsharp] or scalemask[ix,fifthdown]:
-                            scalemask[ix,missingsharp] = True
+                        if scalemask[seq_ix,fifthupsharp] or scalemask[seq_ix,fifthdown]:
+                            scalemask[seq_ix,missingsharp] = True
                         #when F? If Bb not present (deal with Bb above)
-                        if not scalemask[ix,fifthdownflat]:
-                            scalemask[ix,missing] = True
+                        if not scalemask[seq_ix,fifthdownflat]:
+                            scalemask[seq_ix,missing] = True
                         continue
 
-                    if scalemask[ix,fifthupsharp]:
-                        scalemask[ix,missingsharp] = True
-                    elif scalemask[ix,fifthup] and scalemask[ix,fifthdown]:
-                        scalemask[ix,missing] = True
-                    elif scalemask[ix,fifthdownsharp] and scalemask[ix,fifthup]:
-                        scalemask[ix,missingsharp] = True
-                        scalemask[ix,missing] = True
+                    if scalemask[seq_ix,fifthupsharp]:
+                        scalemask[seq_ix,missingsharp] = True
+                    elif scalemask[seq_ix,fifthup] and scalemask[seq_ix,fifthdown]:
+                        scalemask[seq_ix,missing] = True
+                    elif scalemask[seq_ix,fifthdownsharp] and scalemask[seq_ix,fifthup]:
+                        scalemask[seq_ix,missingsharp] = True
+                        scalemask[seq_ix,missing] = True
 
         return scalemask
 
     def getOptimalChordSequence(self, use_scalemask=True, chordTransitionScoreFunction=None):
 
         if chordTransitionScoreFunction == None:
             chordTransitionScoreFunction = self.chordTransitionScore
```

### Comparing `pitchcontext-0.1.7/src/pitchcontext/pitchcontext.py` & `pitchcontext-0.1.8/src/pitchcontext/pitchcontext.py`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.7/src/pitchcontext/song.py` & `pitchcontext-0.1.8/src/pitchcontext/song.py`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.7/src/pitchcontext/visualize.py` & `pitchcontext-0.1.8/src/pitchcontext/visualize.py`

 * *Files identical despite different names*

### Comparing `pitchcontext-0.1.7/setup.py` & `pitchcontext-0.1.8/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -15,15 +15,15 @@
  'matplotlib>=3.3,<4.0',
  'music21>=8.0,<9.0',
  'numpy>=1.19,<2.0',
  'seaborn>=0.12.1,<0.13.0']
 
 setup_kwargs = {
     'name': 'pitchcontext',
-    'version': '0.1.7',
+    'version': '0.1.8',
     'description': 'Library for melody analysis based on pitch context vectors.',
     'long_description': '---\ncomponent-id: pitchcontext\nname: pitchcontext\ndescription: Python module for melody analysis based on pitch context vectors.\ntype: Library\nrelease-date: 2023-03-15\nrelease-number: 0.1.4\nwork-package: WP3\npilot: TUNES\nkeywords:\n  - melody\n  - pitch analysis\nchangelog:\nlicence:\nrelease link:\n--- \n\n\n# pitchcontext\nPython module for melody analysis based on pitch context vectors.\n\n## Prerequisites:\n- lilypond installed and in command line path\n- convert (ImageMagick) installed and in command line path\n- kernfiles and corresponding .json files with melodic features\n\n## Installation\nThe latest release of the pitchcontext module can be installed from pypi:\n```\n$ pip install pitchcontext\n```\n\nThe development version can be installed by cloning the repository and by using the provided pyproject.toml and poetry. In root of the rep do:\n```\n$ poetry install\n```\nThis creates a virtual environment with pitchcontext installed.\n\n## Examples\nRequires a Python3 environment with both pitchcontext and streamlit installed.\nTwo examples are provided:\n- apps/st_dissonance.py\n- apps/st_novelty.py\n\nTo run:\n```\n$ streamlit run st_dissonance.py -- -krnpath <path_to_kern_files> -jsonpath <path_to_json_files>\n```\n',
     'author': 'Peter van Kranenburg',
     'author_email': 'peter.van.kranenburg@meertens.knaw.nl',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `pitchcontext-0.1.7/PKG-INFO` & `pitchcontext-0.1.8/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pitchcontext
-Version: 0.1.7
+Version: 0.1.8
 Summary: Library for melody analysis based on pitch context vectors.
 Author: Peter van Kranenburg
 Author-email: peter.van.kranenburg@meertens.knaw.nl
 Requires-Python: >=3.8, !=2.7.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

