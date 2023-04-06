# Comparing `tmp/aibo-0.0.2-py3-none-any.whl.zip` & `tmp/aibo-0.0.3-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,16 +1,16 @@
-Zip file size: 7899 bytes, number of entries: 14
+Zip file size: 8276 bytes, number of entries: 14
 -rw-r--r--  2.0 unx       22 b- defN 23-Mar-28 03:18 aibo/__init__.py
 -rw-r--r--  2.0 unx     1508 b- defN 23-Mar-29 03:58 aibo/chat.py
--rw-r--r--  2.0 unx     1992 b- defN 23-Mar-28 13:48 aibo/config.py
--rw-r--r--  2.0 unx     2084 b- defN 23-Apr-03 14:10 aibo/main.py
+-rw-r--r--  2.0 unx     2279 b- defN 23-Apr-05 15:23 aibo/config.py
+-rw-r--r--  2.0 unx     2150 b- defN 23-Apr-05 15:06 aibo/main.py
 -rw-r--r--  2.0 unx     1860 b- defN 23-Mar-26 15:15 aibo/record.py
--rw-r--r--  2.0 unx      207 b- defN 23-Mar-26 12:34 aibo/text_to_speech.py
--rw-r--r--  2.0 unx     2034 b- defN 23-Apr-03 14:45 aibo/transcribe.py
+-rw-r--r--  2.0 unx     1003 b- defN 23-Apr-05 15:26 aibo/text_to_speech.py
+-rw-r--r--  2.0 unx     2050 b- defN 23-Apr-06 14:55 aibo/transcribe.py
 -rw-r--r--  2.0 unx        0 b- defN 23-Mar-27 12:20 tests/__init__.py
--rw-r--r--  2.0 unx     1065 b- defN 23-Apr-03 14:51 aibo-0.0.2.dist-info/LICENSE
--rw-r--r--  2.0 unx     2367 b- defN 23-Apr-03 14:51 aibo-0.0.2.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 23-Apr-03 14:51 aibo-0.0.2.dist-info/WHEEL
--rw-r--r--  2.0 unx       41 b- defN 23-Apr-03 14:51 aibo-0.0.2.dist-info/entry_points.txt
--rw-r--r--  2.0 unx        5 b- defN 23-Apr-03 14:51 aibo-0.0.2.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     1037 b- defN 23-Apr-03 14:51 aibo-0.0.2.dist-info/RECORD
-14 files, 14314 bytes uncompressed, 6201 bytes compressed:  56.7%
+-rw-r--r--  2.0 unx     1065 b- defN 23-Apr-06 14:59 aibo-0.0.3.dist-info/LICENSE
+-rw-r--r--  2.0 unx     2394 b- defN 23-Apr-06 14:59 aibo-0.0.3.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 23-Apr-06 14:59 aibo-0.0.3.dist-info/WHEEL
+-rw-r--r--  2.0 unx       40 b- defN 23-Apr-06 14:59 aibo-0.0.3.dist-info/entry_points.txt
+-rw-r--r--  2.0 unx        5 b- defN 23-Apr-06 14:59 aibo-0.0.3.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     1038 b- defN 23-Apr-06 14:59 aibo-0.0.3.dist-info/RECORD
+14 files, 15506 bytes uncompressed, 6578 bytes compressed:  57.6%
```

## zipnote {}

```diff
@@ -18,26 +18,26 @@
 
 Filename: aibo/transcribe.py
 Comment: 
 
 Filename: tests/__init__.py
 Comment: 
 
-Filename: aibo-0.0.2.dist-info/LICENSE
+Filename: aibo-0.0.3.dist-info/LICENSE
 Comment: 
 
-Filename: aibo-0.0.2.dist-info/METADATA
+Filename: aibo-0.0.3.dist-info/METADATA
 Comment: 
 
-Filename: aibo-0.0.2.dist-info/WHEEL
+Filename: aibo-0.0.3.dist-info/WHEEL
 Comment: 
 
-Filename: aibo-0.0.2.dist-info/entry_points.txt
+Filename: aibo-0.0.3.dist-info/entry_points.txt
 Comment: 
 
-Filename: aibo-0.0.2.dist-info/top_level.txt
+Filename: aibo-0.0.3.dist-info/top_level.txt
 Comment: 
 
-Filename: aibo-0.0.2.dist-info/RECORD
+Filename: aibo-0.0.3.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## aibo/config.py

```diff
@@ -12,32 +12,30 @@
             config = json.load(f)
     else:
         config = {
             "api_key": "YOUR KEY",
             "transcription_api_url": "https://api.openai.com/v1/audio/transcriptions",
             "transcription_model": "whisper-1:medium",
             "chat_api_url": "https://api.openai.com/v1/chat/completions",
-            "chat_model": "gpt-3.5-turbo"
+            "chat_model": "gpt-3.5-turbo",
+            "language": "en_US",
+            "gender": "F"
         }
 
     return config
 
 
 def ask_and_set_config(config):
-    api_key = ask_api_key(config["api_key"])
-    transcription_api_url = ask_transcription_api_url(config["transcription_api_url"])
-    transcription_model = ask_transcription_model(config["transcription_model"])
-    chat_api_url = ask_chat_api_url(config["chat_api_url"])
-    chat_model = ask_chat_model(config["chat_model"])
-
-    config["api_key"] = api_key
-    config["transcription_api_url"] = transcription_api_url
-    config["transcription_model"] = transcription_model
-    config["chat_api_url"] = chat_api_url
-    config["chat_model"] = chat_model
+    config["api_key"] = ask_api_key(config["api_key"])
+    config["transcription_api_url"] = ask_transcription_api_url(config["transcription_api_url"])
+    config["transcription_model"] = ask_transcription_model(config["transcription_model"])
+    config["chat_api_url"] = ask_chat_api_url(config["chat_api_url"])
+    config["chat_model"] = ask_chat_model(config["chat_model"])
+    config["language"] = ask_language(config["language"])
+    config["gender"] = ask_gender(config["gender"])
 
     with open(CONFIG_PATH, "w") as f:
         json.dump(config, f, indent=4)
     return config
 
 
 def ask_api_key(default):
@@ -74,7 +72,23 @@
 
 def ask_chat_model(default):
     return click.prompt(
         text="Type in your chat model",
         type=str,
         default=default
     )
+
+
+def ask_language(default):
+    return click.prompt(
+        text="Type in your speaker's language",
+        type=str,
+        default=default
+    )
+
+
+def ask_gender(default):
+    return click.prompt(
+        text="Type in your speaker's gender",
+        type=str,
+        default=default
+    )
```

## aibo/main.py

```diff
@@ -18,23 +18,23 @@
         self.config = get_config()
         args = vars(args)
         self.config = {**self.config, **args}
 
     def ask(self):
         start = time.time()
         if not self.config["silent"]:
-            call_speaker("How can I help you?")
+            call_speaker("How can I help you?", self.config)
         output_path = record_audio()
 
         text, output_path = run_whisper(output_path, self.config)
 
         text = run_chatgpt(text, output_path, self.config)
 
         if not self.config["silent"]:
-            call_speaker(text)
+            call_speaker(text, self.config)
 
         end = time.time()
         print(end - start, "sec.")
 
 
 def main():
     parser = argparse.ArgumentParser(description=None)
@@ -55,15 +55,16 @@
 
     subparsers = parser.add_subparsers()
     sub = subparsers.add_parser("init", help="initialize aibo")
     sub.set_defaults(func=cli_init)
 
     sub = subparsers.add_parser("start", help="start aibo")
     sub.add_argument('-O', '--offline', action='store_true', help='run offline')
-    sub.add_argument('-S', '--silent', action='store_true', help='run without speaker')
+    sub.add_argument('-S', '--silent', action='store_true',
+                     help='run without speaker and save your time')
     sub.set_defaults(func=cli_start)
 
     args = parser.parse_args()
     args.func(args)
 
 
 def cli_init(args):
```

## aibo/text_to_speech.py

```diff
@@ -1,9 +1,31 @@
 import pyttsx3
 
 
-def call_speaker(text: str):
+def call_speaker(text: str, config):
     engine = pyttsx3.init()
-    voices = engine.getProperty('voices')
-    engine.setProperty('voice', voices[0].id)
+    change_voice(engine, config["language"], config["gender"])
+
     engine.say(text)
     engine.runAndWait()
+
+
+def change_voice(engine, language="en_US", gender='F'):
+    voices = engine.getProperty('voices')
+    gender_interpreter = {"M": "VoiceGenderMale", "F": "VoiceGenderFemale"}
+    _gender = gender_interpreter[gender]
+    for voice in voices:
+        if language in voice.languages and _gender == voice.gender:
+            engine.setProperty('voice', voice.id)
+            return True
+
+    gender_dict = {"VoiceGenderMale": "M", "VoiceGenderFemale": "F"}
+    options = []
+    for voice in voices:
+        options.append((voice.languages[0], gender_dict[voice.gender]))
+    raise RuntimeError(
+        "Language '{}' for gender '{}' not found. Available options are \n {}".format(
+            language, gender, options))
+
+
+if __name__ == "__main__":
+    call_speaker("hello", {"language": "en_UK", "gender": "M"})
```

## aibo/transcribe.py

```diff
@@ -10,26 +10,25 @@
         text, output_path = run_local_whisper(path, config)
     else:
         text, output_path = call_whisper(path, config)
 
     return text, output_path
 
 
-def run_local_whisper(path, config, language="en"):
+def run_local_whisper(path, config):
     print("Transcribing...")
     MODEL = config["transcription_model"]
     MODEL, MODEL_SIZE = MODEL.split(":")
     model = whisper.load_model(MODEL_SIZE)
-    result = model.transcribe(path, language=language)
+    result = model.transcribe(path)
     print("Done.")
-    # print(result)
     if result["text"]:
         text = result["text"]
     else:
-        text = "No Result"
+        raise RuntimeError("Failed to transcribe your voice")
     print(text)
     output_path = get_output_path(path, text)
     with open(output_path, "w") as f:
         f.write(text)
     return text, output_path
 
 
@@ -53,15 +52,15 @@
     )
 
     result = response.json()
     # print(result)
     if result["text"]:
         text = result["text"]
     else:
-        text = "No Result"
+        raise RuntimeError("Failed to transcribe your voice")
     print(text)
     output_path = get_output_path(path, text)
     with open(output_path, "w") as f:
         f.write(text)
     return text, output_path
```

## Comparing `aibo-0.0.2.dist-info/LICENSE` & `aibo-0.0.3.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `aibo-0.0.2.dist-info/METADATA` & `aibo-0.0.3.dist-info/METADATA`

 * *Files 4% similar despite different names*

```diff
@@ -1,17 +1,16 @@
 Metadata-Version: 2.1
 Name: aibo
-Version: 0.0.2
+Version: 0.0.3
 Summary: aibo: AI partner that can run offline
 Home-page: https://github.com/JUO-Inc/aibo
 Author: Aibo Community
 Author-email: koki.noda.contact@gmail.com
 License: MIT
 Keywords: LLM language model offline NLP speech deep learning transformer pytorch tensorflow GPT smart speaker
-Platform: UNKNOWN
 Requires-Python: >=3.7.0
 Description-Content-Type: text/markdown
 License-File: LICENSE
 Requires-Dist: click
 Requires-Dist: pyttsx3
 Requires-Dist: pyaudio
 Requires-Dist: openai-whisper
@@ -23,17 +22,17 @@
     <p>Offline Smart Speaker Engine Powered by ChatGPT</p>
 </h3>
 
 https://user-images.githubusercontent.com/62988216/228871916-f8311a31-be59-4855-b7d9-873e3f9adc10.mov
 
 # Features
 
-- You can choose your favorite AI model as your aibo.
-- You don't need to worry about security and privacy.
-- You and Aibo can communicate by voice.
+- Voice Prompting: You and Aibo can communicate by voice.
+- Security and Privacy: You don't need to worry about security and privacy.
+- Models: You can choose your favorite AI model as your aibo.
 
 # Installation
 
 ## With pip
 
 This repository is tested on Python 3.8+, PyTorch 1.13.1+ and MacOS 11.5.2+.
 
@@ -70,9 +69,7 @@
 
 We support the following APIs for online/offline execution.
 
 | model                  | online | offline |
 | :--------------------- | :----: | :-----: |
 | ChatGPT(gpt-3.5-turbo) |  ⭕️   |   ❌    |
 | Whisper                |  ⭕️   |   ⭕️   |
-
-
```

