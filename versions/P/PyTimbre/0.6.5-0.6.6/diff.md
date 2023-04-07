# Comparing `tmp/PyTimbre-0.6.5.tar.gz` & `tmp/PyTimbre-0.6.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "PyTimbre-0.6.5.tar", last modified: Fri Apr  7 00:32:40 2023, max compression
+gzip compressed data, was "PyTimbre-0.6.6.tar", last modified: Fri Apr  7 01:44:38 2023, max compression
```

## Comparing `PyTimbre-0.6.5.tar` & `PyTimbre-0.6.6.tar`

### file list

```diff
@@ -1,30 +1,30 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 00:32:40.103105 PyTimbre-0.6.5/
--rw-rw-rw-   0        0        0     1106 2023-02-28 16:15:07.000000 PyTimbre-0.6.5/LICENSE.txt
--rw-rw-rw-   0        0        0    12168 2023-04-07 00:32:40.101792 PyTimbre-0.6.5/PKG-INFO
--rw-rw-rw-   0        0        0     4342 2023-04-01 12:53:27.000000 PyTimbre-0.6.5/README.md
--rw-rw-rw-   0        0        0       42 2023-04-07 00:32:40.103105 PyTimbre-0.6.5/setup.cfg
--rw-rw-rw-   0        0        0     1102 2023-04-07 00:31:55.000000 PyTimbre-0.6.5/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-07 00:32:40.073022 PyTimbre-0.6.5/src/
-drwxrwxrwx   0        0        0        0 2023-04-07 00:32:40.092256 PyTimbre-0.6.5/src/PyTimbre.egg-info/
--rw-rw-rw-   0        0        0    12168 2023-04-07 00:32:39.000000 PyTimbre-0.6.5/src/PyTimbre.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      719 2023-04-07 00:32:40.000000 PyTimbre-0.6.5/src/PyTimbre.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 00:32:39.000000 PyTimbre-0.6.5/src/PyTimbre.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      115 2023-04-07 00:32:39.000000 PyTimbre-0.6.5/src/PyTimbre.egg-info/requires.txt
--rw-rw-rw-   0        0        0        9 2023-04-07 00:32:39.000000 PyTimbre-0.6.5/src/PyTimbre.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-04-07 00:32:40.095438 PyTimbre-0.6.5/src/pytimbre/
--rw-rw-rw-   0        0        0       96 2023-04-06 23:54:05.000000 PyTimbre-0.6.5/src/pytimbre/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-07 00:32:40.096620 PyTimbre-0.6.5/src/pytimbre/audio_files/
--rw-rw-rw-   0        0        0      108 2023-04-04 13:59:30.000000 PyTimbre-0.6.5/src/pytimbre/audio_files/__init__.py
--rw-rw-rw-   0        0        0    23192 2023-03-31 16:13:47.000000 PyTimbre-0.6.5/src/pytimbre/audio_files/ansi_standard_formatted_files.py
--rw-rw-rw-   0        0        0    15323 2023-04-04 13:59:30.000000 PyTimbre-0.6.5/src/pytimbre/audio_files/calibrated_binary_files.py
--rw-rw-rw-   0        0        0    70669 2023-03-31 16:13:47.000000 PyTimbre-0.6.5/src/pytimbre/audio_files/wavefile.py
-drwxrwxrwx   0        0        0        0 2023-04-07 00:32:40.101792 PyTimbre-0.6.5/src/pytimbre/spectral/
--rw-rw-rw-   0        0        0      150 2023-03-03 22:01:28.000000 PyTimbre-0.6.5/src/pytimbre/spectral/__init__.py
--rw-rw-rw-   0        0        0    16085 2023-03-31 16:13:47.000000 PyTimbre-0.6.5/src/pytimbre/spectral/acoustic_weights.py
--rw-rw-rw-   0        0        0    15571 2023-03-03 22:01:28.000000 PyTimbre-0.6.5/src/pytimbre/spectral/fractional_octave_band.py
--rw-rw-rw-   0        0        0    38821 2023-03-31 16:13:47.000000 PyTimbre-0.6.5/src/pytimbre/spectral/spectra.py
--rw-rw-rw-   0        0        0     6647 2023-03-31 16:13:47.000000 PyTimbre-0.6.5/src/pytimbre/spectral/spectrogram.py
--rw-rw-rw-   0        0        0    30872 2023-03-31 16:13:47.000000 PyTimbre-0.6.5/src/pytimbre/spectral/time_histories.py
--rw-rw-rw-   0        0        0    10655 2023-04-07 00:06:51.000000 PyTimbre-0.6.5/src/pytimbre/swipe.py
--rw-rw-rw-   0        0        0    83139 2023-04-07 00:24:11.000000 PyTimbre-0.6.5/src/pytimbre/waveform.py
--rw-rw-rw-   0        0        0     7680 2023-04-07 00:21:00.000000 PyTimbre-0.6.5/src/pytimbre/yin.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:44:38.850644 PyTimbre-0.6.6/
+-rw-rw-rw-   0        0        0     1106 2023-02-28 16:15:07.000000 PyTimbre-0.6.6/LICENSE.txt
+-rw-rw-rw-   0        0        0    12383 2023-04-07 01:44:38.849645 PyTimbre-0.6.6/PKG-INFO
+-rw-rw-rw-   0        0        0     4557 2023-04-07 01:44:36.000000 PyTimbre-0.6.6/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-07 01:44:38.850644 PyTimbre-0.6.6/setup.cfg
+-rw-rw-rw-   0        0        0     1072 2023-04-07 01:41:59.000000 PyTimbre-0.6.6/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:44:38.816634 PyTimbre-0.6.6/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 01:44:38.841322 PyTimbre-0.6.6/src/PyTimbre.egg-info/
+-rw-rw-rw-   0        0        0    12383 2023-04-07 01:44:38.000000 PyTimbre-0.6.6/src/PyTimbre.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      719 2023-04-07 01:44:38.000000 PyTimbre-0.6.6/src/PyTimbre.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 01:44:38.000000 PyTimbre-0.6.6/src/PyTimbre.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       97 2023-04-07 01:44:38.000000 PyTimbre-0.6.6/src/PyTimbre.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        9 2023-04-07 01:44:38.000000 PyTimbre-0.6.6/src/PyTimbre.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 01:44:38.844137 PyTimbre-0.6.6/src/pytimbre/
+-rw-rw-rw-   0        0        0       94 2023-04-07 01:28:28.000000 PyTimbre-0.6.6/src/pytimbre/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:44:38.846645 PyTimbre-0.6.6/src/pytimbre/audio_files/
+-rw-rw-rw-   0        0        0      108 2023-04-04 13:59:30.000000 PyTimbre-0.6.6/src/pytimbre/audio_files/__init__.py
+-rw-rw-rw-   0        0        0    23192 2023-03-31 16:13:47.000000 PyTimbre-0.6.6/src/pytimbre/audio_files/ansi_standard_formatted_files.py
+-rw-rw-rw-   0        0        0    15323 2023-04-04 13:59:30.000000 PyTimbre-0.6.6/src/pytimbre/audio_files/calibrated_binary_files.py
+-rw-rw-rw-   0        0        0    70669 2023-03-31 16:13:47.000000 PyTimbre-0.6.6/src/pytimbre/audio_files/wavefile.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:44:38.849645 PyTimbre-0.6.6/src/pytimbre/spectral/
+-rw-rw-rw-   0        0        0      150 2023-03-03 22:01:28.000000 PyTimbre-0.6.6/src/pytimbre/spectral/__init__.py
+-rw-rw-rw-   0        0        0    16085 2023-03-31 16:13:47.000000 PyTimbre-0.6.6/src/pytimbre/spectral/acoustic_weights.py
+-rw-rw-rw-   0        0        0    15571 2023-03-03 22:01:28.000000 PyTimbre-0.6.6/src/pytimbre/spectral/fractional_octave_band.py
+-rw-rw-rw-   0        0        0    38821 2023-03-31 16:13:47.000000 PyTimbre-0.6.6/src/pytimbre/spectral/spectra.py
+-rw-rw-rw-   0        0        0     6647 2023-03-31 16:13:47.000000 PyTimbre-0.6.6/src/pytimbre/spectral/spectrogram.py
+-rw-rw-rw-   0        0        0    30872 2023-03-31 16:13:47.000000 PyTimbre-0.6.6/src/pytimbre/spectral/time_histories.py
+-rw-rw-rw-   0        0        0    10655 2023-04-07 00:06:51.000000 PyTimbre-0.6.6/src/pytimbre/swipe.py
+-rw-rw-rw-   0        0        0    84900 2023-04-07 01:39:58.000000 PyTimbre-0.6.6/src/pytimbre/waveform.py
+-rw-rw-rw-   0        0        0     7680 2023-04-07 00:21:00.000000 PyTimbre-0.6.6/src/pytimbre/yin.py
```

### Comparing `PyTimbre-0.6.5/LICENSE.txt` & `PyTimbre-0.6.6/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `PyTimbre-0.6.5/PKG-INFO` & `PyTimbre-0.6.6/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: PyTimbre
-Version: 0.6.5
+Version: 0.6.6
 Summary: Python conversion of Timbre Toolbox
 Home-page: https://gitlab.com/python-audio-feature-extraction/pytimbre
 Download-URL: 
 Author: Dr. Frank Mobley
 Author-email: frank.mobley.1@afrl.af.mil
 License: MIT
 Keywords: machine learning,feature extraction,MATLAB,audio
@@ -45,15 +45,17 @@
 In addition to this code, PyTimbre has taken the code from libf0 (https://github.com/groupmm/libf0) that assists with 
 the computation of the fundamental frequency. There are a number of methods that exist within the libf0 module, but the
 package contains a number of dependencies that are not required for the other calculations and computations within
 PyTimbre. To facilitate the calculation of the fundamental frequency, the swipe class and associated functions were
 extracted and placed into PyTimbre. The code was extracted from the 1.0.2 version of the code on 1 April 2023. This is 
 based on the report: __*Justin Salamon and Emilia GÃ³mez: Melody Extraction From Polyphonic Music Signals Using Pitch 
 Contour Characteristics, IEEE Transactions on Audio, Speech, and Language Processing, vol. 20, no. 6, pp. 1759â€“1770, 
-2012.*__
+2012.*__ Unfortunately, this method became unstable with further development and required the use of librosa. Due to 
+these limitations, the yin function replaced the swipe function to determine the fundamental frequency.
+
 
 # Usage Example
 ## 1. Defining a waveform from an array of values
 
 from pytimbre.waveform import Waveform
 
 fs = 48000
@@ -87,15 +89,15 @@
 
 This software was developed in conjunction with research into the human perception of sound at the 711th Human 
 Performance Wing, Airman Systems Directorate.  
 
 It is approved for Distribution A, 88ABW-2020-2147.
 
 A series of audio files employed in classification research within the wing are provided for testing and examples of how 
-.to use the interface.
+to use the interface.
 
 # PyTimbre
 
 ## Development History
 ### 2020
 #### April 
 - Added logic to avoid adding the STFT when it is not within the input configuration
```

### Comparing `PyTimbre-0.6.5/README.md` & `PyTimbre-0.6.6/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -32,15 +32,17 @@
 In addition to this code, PyTimbre has taken the code from libf0 (https://github.com/groupmm/libf0) that assists with 
 the computation of the fundamental frequency. There are a number of methods that exist within the libf0 module, but the
 package contains a number of dependencies that are not required for the other calculations and computations within
 PyTimbre. To facilitate the calculation of the fundamental frequency, the swipe class and associated functions were
 extracted and placed into PyTimbre. The code was extracted from the 1.0.2 version of the code on 1 April 2023. This is 
 based on the report: __*Justin Salamon and Emilia Gómez: Melody Extraction From Polyphonic Music Signals Using Pitch 
 Contour Characteristics, IEEE Transactions on Audio, Speech, and Language Processing, vol. 20, no. 6, pp. 1759–1770, 
-2012.*__
+2012.*__ Unfortunately, this method became unstable with further development and required the use of librosa. Due to 
+these limitations, the yin function replaced the swipe function to determine the fundamental frequency.
+
 
 # Usage Example
 ## 1. Defining a waveform from an array of values
 
 from pytimbre.waveform import Waveform
 
 fs = 48000
@@ -74,8 +76,8 @@
 
 This software was developed in conjunction with research into the human perception of sound at the 711th Human 
 Performance Wing, Airman Systems Directorate.  
 
 It is approved for Distribution A, 88ABW-2020-2147.
 
 A series of audio files employed in classification research within the wing are provided for testing and examples of how 
-.to use the interface.
+to use the interface.
```

### Comparing `PyTimbre-0.6.5/setup.py` & `PyTimbre-0.6.6/setup.py`

 * *Files 15% similar despite different names*

```diff
@@ -7,29 +7,28 @@
         HISTORY = history_file.read()
 
         with open('LICENSE.txt') as license_file:
             LICENSE = license_file.read()
 
 setup(
     name='PyTimbre',
-    version='0.6.5',
+    version='0.6.6',
     description='Python conversion of Timbre Toolbox',
     long_description_content_type="text/markdown",
     long_description=README + '\n\n' + HISTORY + '\n\n' + LICENSE,
     license='MIT',
     packages=find_packages('src'),
     author='Dr. Frank Mobley',
     author_email='frank.mobley.1@afrl.af.mil',
     keywords=['machine learning', 'feature extraction', 'MATLAB', 'audio'],
     url='https://gitlab.com/python-audio-feature-extraction/pytimbre',
     download_url='',
     install_requires=[
-        'numpy==1.23.5',
-        'pandas==1.5.3',
-        'scipy==1.10.1',
-        'statsmodels==0.13.2',
-        'mosqito==1.0.8',
-        'colorednoise==2.1.0',
-        'clipdetect==0.1.1'
+        'numpy>=1.23.5',
+        'pandas>=1.5.3',
+        'scipy>=1.10.1',
+        'statsmodels>=0.13.2',
+        'mosqito>=1.0.8',
+        'colorednoise>=2.1.0'
     ],
     package_dir={'': 'src'}
 )
```

### Comparing `PyTimbre-0.6.5/src/PyTimbre.egg-info/PKG-INFO` & `PyTimbre-0.6.6/src/PyTimbre.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: PyTimbre
-Version: 0.6.5
+Version: 0.6.6
 Summary: Python conversion of Timbre Toolbox
 Home-page: https://gitlab.com/python-audio-feature-extraction/pytimbre
 Download-URL: 
 Author: Dr. Frank Mobley
 Author-email: frank.mobley.1@afrl.af.mil
 License: MIT
 Keywords: machine learning,feature extraction,MATLAB,audio
@@ -45,15 +45,17 @@
 In addition to this code, PyTimbre has taken the code from libf0 (https://github.com/groupmm/libf0) that assists with 
 the computation of the fundamental frequency. There are a number of methods that exist within the libf0 module, but the
 package contains a number of dependencies that are not required for the other calculations and computations within
 PyTimbre. To facilitate the calculation of the fundamental frequency, the swipe class and associated functions were
 extracted and placed into PyTimbre. The code was extracted from the 1.0.2 version of the code on 1 April 2023. This is 
 based on the report: __*Justin Salamon and Emilia GÃ³mez: Melody Extraction From Polyphonic Music Signals Using Pitch 
 Contour Characteristics, IEEE Transactions on Audio, Speech, and Language Processing, vol. 20, no. 6, pp. 1759â€“1770, 
-2012.*__
+2012.*__ Unfortunately, this method became unstable with further development and required the use of librosa. Due to 
+these limitations, the yin function replaced the swipe function to determine the fundamental frequency.
+
 
 # Usage Example
 ## 1. Defining a waveform from an array of values
 
 from pytimbre.waveform import Waveform
 
 fs = 48000
@@ -87,15 +89,15 @@
 
 This software was developed in conjunction with research into the human perception of sound at the 711th Human 
 Performance Wing, Airman Systems Directorate.  
 
 It is approved for Distribution A, 88ABW-2020-2147.
 
 A series of audio files employed in classification research within the wing are provided for testing and examples of how 
-.to use the interface.
+to use the interface.
 
 # PyTimbre
 
 ## Development History
 ### 2020
 #### April 
 - Added logic to avoid adding the STFT when it is not within the input configuration
```

### Comparing `PyTimbre-0.6.5/src/PyTimbre.egg-info/SOURCES.txt` & `PyTimbre-0.6.6/src/PyTimbre.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `PyTimbre-0.6.5/src/pytimbre/audio_files/ansi_standard_formatted_files.py` & `PyTimbre-0.6.6/src/pytimbre/audio_files/ansi_standard_formatted_files.py`

 * *Files identical despite different names*

### Comparing `PyTimbre-0.6.5/src/pytimbre/audio_files/calibrated_binary_files.py` & `PyTimbre-0.6.6/src/pytimbre/audio_files/calibrated_binary_files.py`

 * *Files identical despite different names*

### Comparing `PyTimbre-0.6.5/src/pytimbre/audio_files/wavefile.py` & `PyTimbre-0.6.6/src/pytimbre/audio_files/wavefile.py`

 * *Files identical despite different names*

### Comparing `PyTimbre-0.6.5/src/pytimbre/spectral/acoustic_weights.py` & `PyTimbre-0.6.6/src/pytimbre/spectral/acoustic_weights.py`

 * *Files identical despite different names*

### Comparing `PyTimbre-0.6.5/src/pytimbre/spectral/fractional_octave_band.py` & `PyTimbre-0.6.6/src/pytimbre/spectral/fractional_octave_band.py`

 * *Files identical despite different names*

### Comparing `PyTimbre-0.6.5/src/pytimbre/spectral/spectra.py` & `PyTimbre-0.6.6/src/pytimbre/spectral/spectra.py`

 * *Files identical despite different names*

### Comparing `PyTimbre-0.6.5/src/pytimbre/spectral/spectrogram.py` & `PyTimbre-0.6.6/src/pytimbre/spectral/spectrogram.py`

 * *Files identical despite different names*

### Comparing `PyTimbre-0.6.5/src/pytimbre/spectral/time_histories.py` & `PyTimbre-0.6.6/src/pytimbre/spectral/time_histories.py`

 * *Files identical despite different names*

### Comparing `PyTimbre-0.6.5/src/pytimbre/swipe.py` & `PyTimbre-0.6.6/src/pytimbre/swipe.py`

 * *Files identical despite different names*

### Comparing `PyTimbre-0.6.5/src/pytimbre/waveform.py` & `PyTimbre-0.6.6/src/pytimbre/waveform.py`

 * *Files 1% similar despite different names*

```diff
@@ -5,14 +5,16 @@
 from scipy.signal.windows import hamming, tukey
 import scipy.signal
 import statsmodels.api as sm
 import colorednoise as cn
 import warnings
 from .swipe import swipe
 from .yin import yin
+from typing import Dict, Tuple
+import numpy.typing as npt
 
 
 class WindowingMethods(Enum):
     """
     The available windowing methods for the waveform
     """
 
@@ -433,17 +435,15 @@
 
     @property
     def is_clipped(self):
         """
         This function attempts to determine whether there is clipping in the acoustic data represented in this waveform.
         """
 
-        from clipdetect import detect_clipping
-
-        clipped_sections, total_clipped_samples = detect_clipping(self.samples)
+        clipped_sections, total_clipped_samples = Waveform._detect_clipping(self.samples)
 
         return not ((total_clipped_samples / len(self.samples)) < 0.01)
 
     @property
     def fundamental_frequency(self):
         # return np.median(swipe(self.samples, self.sample_rate, minimum_frequency=10, maximum_frequency=10000,
         #                        strength_threshold=0.25, hop_size=0.25 * self.sample_rate)[0])
@@ -454,14 +454,51 @@
             F_max=10000,
             F_min=10,
             N=int(np.floor(self.sample_rate/10)),
             H=int(np.floor(self.sample_rate/10/4))
         )[0])
 
     # ------------------ Static functions for the calculation of filter shapes and timbre features ---------------------
+    @staticmethod
+    def _detect_clipping(
+            samples_array: npt.NDArray, max_threshold=0.995, min_threshold=0.995
+    ) -> Tuple[Dict[str, int], int]:
+        """
+        Somewhat informed from https://www.sciencedirect.com/science/article/pii/S0167639321000832
+        but without the sample-by-sample tagging. Intended to catch cases where clipped values have
+        been normalized away.
+
+        Returns the tagged clipped samples and the total number of clipped samples
+
+        2023-04-06 - FSM - This function was extracted from the clipdetect project to minimize the dependency
+        requirements of PyTimbre
+        """
+        if len(samples_array.shape) != 1:
+            raise ValueError(
+                "You must pass just the samples without any channel information"
+            )
+        max_sample = samples_array.max()
+        min_sample = samples_array.min()
+        max_threshold *= max_sample
+        min_threshold *= min_sample
+        clipping_sections = []
+        total_clipped_samples = 0
+        clip_end = 0
+        for i, sample in enumerate(samples_array):
+            if i > clip_end and sample in [max_sample, min_sample]:
+                clipping_count = 0
+                for new_sample in samples_array[i:]:
+                    if new_sample >= max_threshold or new_sample <= min_threshold:
+                        clipping_count += 1
+                    else:
+                        clipping_sections.append({"start": i, "end": i + clipping_count})
+                        total_clipped_samples += clipping_count
+                        clip_end = i + clipping_count
+                        break
+        return clipping_sections, total_clipped_samples
 
     @staticmethod
     def AC_Filter_Design(fs):
         """
         AC_Filter_Design.py
 
         Created on Mon Oct 18 19:27:36 2021
```

### Comparing `PyTimbre-0.6.5/src/pytimbre/yin.py` & `PyTimbre-0.6.6/src/pytimbre/yin.py`

 * *Files identical despite different names*

