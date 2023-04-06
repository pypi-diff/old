# Comparing `tmp/whisper_transcribe-0.1.0.tar.gz` & `tmp/whisper_transcribe-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "whisper_transcribe-0.1.0.tar", max compression
+gzip compressed data, was "whisper_transcribe-0.1.1.tar", max compression
```

## Comparing `whisper_transcribe-0.1.0.tar` & `whisper_transcribe-0.1.1.tar`

### file list

```diff
@@ -1,7 +1,7 @@
--rw-r--r--   0        0        0     1065 2023-03-22 22:34:43.463207 whisper_transcribe-0.1.0/LICENSE
--rw-r--r--   0        0        0      977 2023-04-06 07:22:18.258458 whisper_transcribe-0.1.0/README.md
--rw-r--r--   0        0        0      551 2023-03-31 22:23:47.652063 whisper_transcribe-0.1.0/pyproject.toml
--rw-r--r--   0        0        0       30 2023-03-23 00:59:19.073098 whisper_transcribe-0.1.0/whisper_transcribe/__init__.py
--rw-r--r--   0        0        0     1002 2023-03-31 22:57:42.202065 whisper_transcribe-0.1.0/whisper_transcribe/helpers.py
--rw-r--r--   0        0        0     8258 2023-04-06 06:47:15.568455 whisper_transcribe-0.1.0/whisper_transcribe/main.py
--rw-r--r--   0        0        0     1621 1970-01-01 00:00:00.000000 whisper_transcribe-0.1.0/PKG-INFO
+-rw-r--r--   0        0        0     1065 2023-03-22 22:34:43.463207 whisper_transcribe-0.1.1/LICENSE
+-rw-r--r--   0        0        0     1030 2023-04-06 08:26:36.078463 whisper_transcribe-0.1.1/README.md
+-rw-r--r--   0        0        0      551 2023-04-06 08:31:57.718464 whisper_transcribe-0.1.1/pyproject.toml
+-rw-r--r--   0        0        0       30 2023-03-23 00:59:19.073098 whisper_transcribe-0.1.1/whisper_transcribe/__init__.py
+-rw-r--r--   0        0        0     1002 2023-03-31 22:57:42.202065 whisper_transcribe-0.1.1/whisper_transcribe/helpers.py
+-rw-r--r--   0        0        0     8258 2023-04-06 06:47:15.568455 whisper_transcribe-0.1.1/whisper_transcribe/main.py
+-rw-r--r--   0        0        0     1674 1970-01-01 00:00:00.000000 whisper_transcribe-0.1.1/PKG-INFO
```

### Comparing `whisper_transcribe-0.1.0/LICENSE` & `whisper_transcribe-0.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `whisper_transcribe-0.1.0/README.md` & `whisper_transcribe-0.1.1/README.md`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,13 @@
 # whisper-transcribe
 Python video transcriber that uses OpenAI's WhisperAI.
 
+# How to install
+    pip install whisper-transcribe
+
 # Trasncribe a video file:
     from whisper_transcribe import Transcriber
 
     api_key = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
 
     with Transcriber(api_key=api_key) as tb:
         trasncription = tb.transcribe("path/to/a/local/video.mp4")
```

### Comparing `whisper_transcribe-0.1.0/pyproject.toml` & `whisper_transcribe-0.1.1/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "whisper_transcribe"
-version = "0.1.0"
+version = "0.1.1"
 description = "Python video transcriber that uses OpenAI's WhisperAI."
 authors = ["Daniel K. Elder <elder.dk@gmail.com>"]
 license = "MIT"
 readme = "README.md"
 packages = [{include = "whisper_transcribe"}]
 
 [tool.poetry.dependencies]
```

### Comparing `whisper_transcribe-0.1.0/whisper_transcribe/helpers.py` & `whisper_transcribe-0.1.1/whisper_transcribe/helpers.py`

 * *Files identical despite different names*

### Comparing `whisper_transcribe-0.1.0/whisper_transcribe/main.py` & `whisper_transcribe-0.1.1/whisper_transcribe/main.py`

 * *Files identical despite different names*

### Comparing `whisper_transcribe-0.1.0/PKG-INFO` & `whisper_transcribe-0.1.1/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: whisper-transcribe
-Version: 0.1.0
+Version: 0.1.1
 Summary: Python video transcriber that uses OpenAI's WhisperAI.
 License: MIT
 Author: Daniel K. Elder
 Author-email: elder.dk@gmail.com
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
@@ -15,14 +15,17 @@
 Requires-Dist: tiktoken (>=0.3.2,<0.4.0)
 Requires-Dist: yt-dlp (>=2023.3.4,<2024.0.0)
 Description-Content-Type: text/markdown
 
 # whisper-transcribe
 Python video transcriber that uses OpenAI's WhisperAI.
 
+# How to install
+    pip install whisper-transcribe
+
 # Trasncribe a video file:
     from whisper_transcribe import Transcriber
 
     api_key = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
 
     with Transcriber(api_key=api_key) as tb:
         trasncription = tb.transcribe("path/to/a/local/video.mp4")
```

