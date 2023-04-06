# Comparing `tmp/soundscapy-0.4.2.tar.gz` & `tmp/soundscapy-0.4.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "soundscapy-0.4.2.tar", max compression
+gzip compressed data, was "soundscapy-0.4.3.tar", max compression
```

## Comparing `soundscapy-0.4.2.tar` & `soundscapy-0.4.3.tar`

### file list

```diff
@@ -1,25 +1,25 @@
--rw-r--r--   0        0        0     1552 2023-01-03 12:15:28.169193 soundscapy-0.4.2/LICENSE
--rw-r--r--   0        0        0     1365 2023-03-30 22:15:39.941250 soundscapy-0.4.2/pyproject.toml
--rw-r--r--   0        0        0     4085 2023-02-03 21:59:24.605846 soundscapy-0.4.2/README.md
--rw-r--r--   0        0        0     6148 2023-01-03 12:15:28.208716 soundscapy-0.4.2/soundscapy/.DS_Store
--rw-r--r--   0        0        0      324 2023-03-27 22:40:11.593116 soundscapy-0.4.2/soundscapy/__init__.py
--rw-r--r--   0        0        0        0 2023-03-27 17:27:34.245604 soundscapy-0.4.2/soundscapy/analysis/__init__.py
--rw-r--r--   0        0        0     8923 2023-03-27 22:40:11.598108 soundscapy-0.4.2/soundscapy/analysis/_AnalysisSettings.py
--rw-r--r--   0        0        0    16542 2023-01-29 22:44:32.576675 soundscapy-0.4.2/soundscapy/analysis/_Binaural.py
--rw-r--r--   0        0        0    16937 2023-03-27 22:40:11.598108 soundscapy-0.4.2/soundscapy/analysis/binaural.py
--rw-r--r--   0        0        0     3178 2023-01-03 12:15:28.211719 soundscapy-0.4.2/soundscapy/analysis/default_settings.yaml
--rw-r--r--   0        0        0    12293 2023-01-29 22:44:32.460238 soundscapy-0.4.2/soundscapy/analysis/metrics.py
--rw-r--r--   0        0        0     2967 2023-03-27 22:40:11.598108 soundscapy-0.4.2/soundscapy/analysis/parallel_processing.py
--rw-r--r--   0        0        0        0 2023-01-03 12:15:28.213719 soundscapy-0.4.2/soundscapy/databases/__init__.py
--rw-r--r--   0        0        0      124 2023-01-29 22:44:32.460238 soundscapy-0.4.2/soundscapy/databases/araus.py
--rw-r--r--   0        0        0    16713 2023-01-29 22:44:32.460238 soundscapy-0.4.2/soundscapy/databases/isd.py
--rw-r--r--   0        0        0      133 2023-01-03 12:15:28.215722 soundscapy-0.4.2/soundscapy/plotting/__init__.py
--rw-r--r--   0        0        0    36479 2023-03-30 22:15:39.941250 soundscapy-0.4.2/soundscapy/plotting/circumplex.py
--rw-r--r--   0        0        0     2096 2023-01-29 22:44:32.543604 soundscapy-0.4.2/soundscapy/plotting/likert.py
--rw-r--r--   0        0        0        0 2023-01-29 22:44:32.460238 soundscapy-0.4.2/soundscapy/utils/__init__.py
--rw-r--r--   0        0        0    32537 2023-03-30 22:15:39.941250 soundscapy-0.4.2/soundscapy/utils/_sspy_accessor.py
--rw-r--r--   0        0        0     1478 2023-01-29 22:44:32.543604 soundscapy-0.4.2/soundscapy/utils/parameters.py
--rw-r--r--   0        0        0    17105 2023-01-29 22:44:32.462248 soundscapy-0.4.2/soundscapy/utils/surveys.py
--rw-r--r--   0        0        0       93 2023-03-27 22:40:11.598108 soundscapy-0.4.2/soundscapy/version.py
--rw-r--r--   0        0        0     5134 1970-01-01 00:00:00.000000 soundscapy-0.4.2/setup.py
--rw-r--r--   0        0        0     5264 1970-01-01 00:00:00.000000 soundscapy-0.4.2/PKG-INFO
+-rw-r--r--   0        0        0     1552 2023-01-03 12:15:28.169193 soundscapy-0.4.3/LICENSE
+-rw-r--r--   0        0        0     1364 2023-04-06 12:29:29.620972 soundscapy-0.4.3/pyproject.toml
+-rw-r--r--   0        0        0     4085 2023-02-03 21:59:24.605846 soundscapy-0.4.3/README.md
+-rw-r--r--   0        0        0     6148 2023-01-03 12:15:28.208716 soundscapy-0.4.3/soundscapy/.DS_Store
+-rw-r--r--   0        0        0      324 2023-03-27 22:40:11.593116 soundscapy-0.4.3/soundscapy/__init__.py
+-rw-r--r--   0        0        0        0 2023-03-27 17:27:34.245604 soundscapy-0.4.3/soundscapy/analysis/__init__.py
+-rw-r--r--   0        0        0     8923 2023-03-27 22:40:11.598108 soundscapy-0.4.3/soundscapy/analysis/_AnalysisSettings.py
+-rw-r--r--   0        0        0    16542 2023-01-29 22:44:32.576675 soundscapy-0.4.3/soundscapy/analysis/_Binaural.py
+-rw-r--r--   0        0        0    16937 2023-03-27 22:40:11.598108 soundscapy-0.4.3/soundscapy/analysis/binaural.py
+-rw-r--r--   0        0        0     3178 2023-01-03 12:15:28.211719 soundscapy-0.4.3/soundscapy/analysis/default_settings.yaml
+-rw-r--r--   0        0        0    12293 2023-01-29 22:44:32.460238 soundscapy-0.4.3/soundscapy/analysis/metrics.py
+-rw-r--r--   0        0        0     2967 2023-03-27 22:40:11.598108 soundscapy-0.4.3/soundscapy/analysis/parallel_processing.py
+-rw-r--r--   0        0        0        0 2023-01-03 12:15:28.213719 soundscapy-0.4.3/soundscapy/databases/__init__.py
+-rw-r--r--   0        0        0      124 2023-01-29 22:44:32.460238 soundscapy-0.4.3/soundscapy/databases/araus.py
+-rw-r--r--   0        0        0    16713 2023-01-29 22:44:32.460238 soundscapy-0.4.3/soundscapy/databases/isd.py
+-rw-r--r--   0        0        0      133 2023-01-03 12:15:28.215722 soundscapy-0.4.3/soundscapy/plotting/__init__.py
+-rw-r--r--   0        0        0    36479 2023-03-30 22:15:39.941250 soundscapy-0.4.3/soundscapy/plotting/circumplex.py
+-rw-r--r--   0        0        0     2096 2023-01-29 22:44:32.543604 soundscapy-0.4.3/soundscapy/plotting/likert.py
+-rw-r--r--   0        0        0        0 2023-01-29 22:44:32.460238 soundscapy-0.4.3/soundscapy/utils/__init__.py
+-rw-r--r--   0        0        0    32537 2023-03-30 22:15:39.941250 soundscapy-0.4.3/soundscapy/utils/_sspy_accessor.py
+-rw-r--r--   0        0        0     1478 2023-01-29 22:44:32.543604 soundscapy-0.4.3/soundscapy/utils/parameters.py
+-rw-r--r--   0        0        0    17105 2023-01-29 22:44:32.462248 soundscapy-0.4.3/soundscapy/utils/surveys.py
+-rw-r--r--   0        0        0       93 2023-04-06 12:29:43.293527 soundscapy-0.4.3/soundscapy/version.py
+-rw-r--r--   0        0        0     5133 1970-01-01 00:00:00.000000 soundscapy-0.4.3/setup.py
+-rw-r--r--   0        0        0     5314 1970-01-01 00:00:00.000000 soundscapy-0.4.3/PKG-INFO
```

### Comparing `soundscapy-0.4.2/LICENSE` & `soundscapy-0.4.3/LICENSE`

 * *Files identical despite different names*

### Comparing `soundscapy-0.4.2/pyproject.toml` & `soundscapy-0.4.3/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,25 +1,25 @@
 [tool.poetry]
 name = "soundscapy"
-version = "0.4.2"
+version = "0.4.3"
 description = "A python library for analysing and visualising soundscape assessments."
 authors = ["Andrew Mitchell <andrew.mitchell.18@ucl.ac.uk>"]
 readme = "README.md"
 license = "BSD-3-Clause"
 classifiers = [
     "Programming Language :: Python :: 3",
     "Operating System :: OS Independent",
     "License :: OSI Approved :: BSD License"
 ]
 keywords = ["soundscape", "psychoacoustics", "acoustics", "audio analysis"]
 repository = "https://github.com/MitchellAcoustics/Soundscapy"
 documentation = "https://soundscapy.readthedocs.io/en/latest/"
 
 [tool.poetry.dependencies]
-python = "^3.9,<3.11"
+python = "^3.9,<4.0"
 pandas = "^1.3.5"
 openpyxl = "^3.0.10"
 seaborn = "^0.12.2"
 acoustics = "^0.2.6"
 mosqito = "^1.0.8"
 PyYAML = "^6.0"
 scikit-maad = "^1.3.12"
```

### Comparing `soundscapy-0.4.2/README.md` & `soundscapy-0.4.3/README.md`

 * *Files identical despite different names*

### Comparing `soundscapy-0.4.2/soundscapy/.DS_Store` & `soundscapy-0.4.3/soundscapy/.DS_Store`

 * *Files identical despite different names*

### Comparing `soundscapy-0.4.2/soundscapy/analysis/_AnalysisSettings.py` & `soundscapy-0.4.3/soundscapy/analysis/_AnalysisSettings.py`

 * *Files identical despite different names*

### Comparing `soundscapy-0.4.2/soundscapy/analysis/_Binaural.py` & `soundscapy-0.4.3/soundscapy/analysis/_Binaural.py`

 * *Files identical despite different names*

### Comparing `soundscapy-0.4.2/soundscapy/analysis/binaural.py` & `soundscapy-0.4.3/soundscapy/analysis/binaural.py`

 * *Files identical despite different names*

### Comparing `soundscapy-0.4.2/soundscapy/analysis/default_settings.yaml` & `soundscapy-0.4.3/soundscapy/analysis/default_settings.yaml`

 * *Files identical despite different names*

### Comparing `soundscapy-0.4.2/soundscapy/analysis/metrics.py` & `soundscapy-0.4.3/soundscapy/analysis/metrics.py`

 * *Files identical despite different names*

### Comparing `soundscapy-0.4.2/soundscapy/analysis/parallel_processing.py` & `soundscapy-0.4.3/soundscapy/analysis/parallel_processing.py`

 * *Files identical despite different names*

### Comparing `soundscapy-0.4.2/soundscapy/databases/isd.py` & `soundscapy-0.4.3/soundscapy/databases/isd.py`

 * *Files identical despite different names*

### Comparing `soundscapy-0.4.2/soundscapy/plotting/circumplex.py` & `soundscapy-0.4.3/soundscapy/plotting/circumplex.py`

 * *Files identical despite different names*

### Comparing `soundscapy-0.4.2/soundscapy/plotting/likert.py` & `soundscapy-0.4.3/soundscapy/plotting/likert.py`

 * *Files identical despite different names*

### Comparing `soundscapy-0.4.2/soundscapy/utils/_sspy_accessor.py` & `soundscapy-0.4.3/soundscapy/utils/_sspy_accessor.py`

 * *Files identical despite different names*

### Comparing `soundscapy-0.4.2/soundscapy/utils/parameters.py` & `soundscapy-0.4.3/soundscapy/utils/parameters.py`

 * *Files identical despite different names*

### Comparing `soundscapy-0.4.2/soundscapy/utils/surveys.py` & `soundscapy-0.4.3/soundscapy/utils/surveys.py`

 * *Files identical despite different names*

### Comparing `soundscapy-0.4.2/setup.py` & `soundscapy-0.4.3/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -21,23 +21,23 @@
  'pytest>=7.2.2,<8.0.0',
  'scikit-maad>=1.3.12,<2.0.0',
  'seaborn>=0.12.2,<0.13.0',
  'tqdm>=4.65.0,<5.0.0']
 
 setup_kwargs = {
     'name': 'soundscapy',
-    'version': '0.4.2',
+    'version': '0.4.3',
     'description': 'A python library for analysing and visualising soundscape assessments.',
     'long_description': '<img src="https://raw.githubusercontent.com/MitchellAcoustics/Soundscapy/main/docs/logo/LightLogo.png" width="300">\n\n# Soundscapy\n\n[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MitchellAcoustics/Soundscapy/main?labpath=docs%2Ftutorials%2FHowToAnalyseAndRepresentSoundscapes.ipynb)\n\nA python library for analysing and visualising soundscape assessments. \n\n**Disclaimer:** This module is still heavily in development, and might break what you\'re working on. It will also likely require a decent amount of troubleshooting at this stage. I promise bug fixes and cleaning up is coming!\n\n## Installation\n\nThe package is still under development, but can be installed with pip:\n\n```\npip install soundscapy\n```\n\n## Examples\n\nWe are currently working on writing more comprehensive examples and documentation, please bear with us in the meantime. \n\nAn example notebook which reproduces the figures used in our recent paper "How to analyse and represent quantitative soundscape data" is provided in the `examples` folder.\n\n## Acknowledgements\n\nThe newly added Binaural analysis functionality relies directly on three acoustic analysis libraries: \n * [python-acoustics](https://github.com/python-acoustics/python-acoustics) for the standard environmental and building acoustics metrics, \n * [scikit-maad](https://github.com/scikit-maad/scikit-maad) for the bioacoustics and ecological soundscape metrics, and\n * [MoSQITo](https://github.com/Eomys/MoSQITo) for the psychoacoustics metrics. We thank each of these packages for their great work in making advanced acoustic analysis more accessible.\n\n## Citation\n\nIf you are using Soundscapy in your research, please help our scientific visibility by citing our work! Please include a citation to our accompanying paper:\n\nMitchell, A., Aletta, F., & Kang, J. (2022). How to analyse and represent quantitative soundscape data. *JASA Express Letters, 2*, 37201. [https://doi.org/10.1121/10.0009794](https://doi.org/10.1121/10.0009794)\n\n\n<!---\nBibtex:\n```\n@Article{Mitchell2022How,\n  author         = {Mitchell, Andrew and Aletta, Francesco and Kang, Jian},\n  journal        = {JASA Express Letters},\n  title          = {How to analyse and represent quantitative soundscape data},\n  year           = {2022},\n  number         = {3},\n  pages          = {037201},\n  volume         = {2},\n  doi            = {10.1121/10.0009794},\n  eprint         = {https://doi.org/10.1121/10.0009794},\n}\n\n```\n--->\n\n## Development Plans\n\nAs noted, this package is in heavy development to make it more useable, more stable, and to add features and improvements. At this stage it is mostly limited to doing basic quality checks of soundscape survey data and creating the soundscape distribution plots. Some planned improvements are:\n\n - [ ] Simplify the plotting options\n - [ ] Possibly improve how the plots and data are handled - a more OOP approach would be good.\n - [ ] Add appropriate tests and documentation.\n - [ ] Bug fixes, ~~particularly around setting color palettes.~~\n\nLarge planned feature additions are:\n\n - [ ] Add better methods for cleaning datasets, including robust outlier exclusion and imputation.\n - [x] Add handling of .wav files.\n - [x] Integrate environmental acoustic and psychoacoustic batch processing. This will involve using existing packages (e.g. MoSQito, python-acoustics) to do the metric calculations, but adding useful functionality for processing many files at once, tieing them to a specific survey response, and implementing a configuration file for maintaining consistent analysis settings.\n - [ ] Integrate the predictive modelling results from the SSID team\'s research to enable a single pipelined from recording -> psychoacoustics -> predicted soundscape perception (this is very much a pie-in-the-sky future plan, which may not be possible).\n\n### Contributing\n\nIf you would like to contribute or if you have any bugs you have found while using `Soundscapy\', please feel free to get in touch or submit an issue or pull request!\n',
     'author': 'Andrew Mitchell',
     'author_email': 'andrew.mitchell.18@ucl.ac.uk',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://github.com/MitchellAcoustics/Soundscapy',
     'packages': packages,
     'package_data': package_data,
     'install_requires': install_requires,
-    'python_requires': '>=3.9,<3.11',
+    'python_requires': '>=3.9,<4.0',
 }
 
 
 setup(**setup_kwargs)
```

### Comparing `soundscapy-0.4.2/PKG-INFO` & `soundscapy-0.4.3/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,22 +1,23 @@
 Metadata-Version: 2.1
 Name: soundscapy
-Version: 0.4.2
+Version: 0.4.3
 Summary: A python library for analysing and visualising soundscape assessments.
 Home-page: https://github.com/MitchellAcoustics/Soundscapy
 License: BSD-3-Clause
 Keywords: soundscape,psychoacoustics,acoustics,audio analysis
 Author: Andrew Mitchell
 Author-email: andrew.mitchell.18@ucl.ac.uk
-Requires-Python: >=3.9,<3.11
+Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: 3
 Requires-Dist: PyYAML (>=6.0,<7.0)
 Requires-Dist: acoustics (>=0.2.6,<0.3.0)
 Requires-Dist: mosqito (>=1.0.8,<2.0.0)
 Requires-Dist: openpyxl (>=3.0.10,<4.0.0)
 Requires-Dist: pandas (>=1.3.5,<2.0.0)
 Requires-Dist: pyjanitor (==0.23.1)
```

