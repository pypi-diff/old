# Comparing `tmp/manubot-ai-editor-0.4.1.tar.gz` & `tmp/manubot-ai-editor-0.4.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "manubot-ai-editor-0.4.1.tar", last modified: Fri Mar 17 13:07:28 2023, max compression
+gzip compressed data, was "manubot-ai-editor-0.4.2.tar", last modified: Fri Apr  7 14:54:32 2023, max compression
```

## Comparing `manubot-ai-editor-0.4.1.tar` & `manubot-ai-editor-0.4.2.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxrwxr-x   0 miltondp  (1000) miltondp  (1000)        0 2023-03-17 13:07:28.339774 manubot-ai-editor-0.4.1/
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)     2556 2023-03-17 13:07:28.339774 manubot-ai-editor-0.4.1/PKG-INFO
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)     2074 2023-03-17 13:06:41.000000 manubot-ai-editor-0.4.1/README.md
-drwxrwxr-x   0 miltondp  (1000) miltondp  (1000)        0 2023-03-17 13:07:28.335774 manubot-ai-editor-0.4.1/libs/
-drwxrwxr-x   0 miltondp  (1000) miltondp  (1000)        0 2023-03-17 13:07:28.339774 manubot-ai-editor-0.4.1/libs/manubot_ai_editor/
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)        0 2023-01-25 04:03:27.000000 manubot-ai-editor-0.4.1/libs/manubot_ai_editor/__init__.py
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)    16525 2023-03-09 16:05:14.000000 manubot-ai-editor-0.4.1/libs/manubot_ai_editor/editor.py
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)     2294 2023-03-09 14:41:07.000000 manubot-ai-editor-0.4.1/libs/manubot_ai_editor/env_vars.py
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)    19817 2023-03-17 13:06:41.000000 manubot-ai-editor-0.4.1/libs/manubot_ai_editor/models.py
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)      632 2023-01-25 04:03:27.000000 manubot-ai-editor-0.4.1/libs/manubot_ai_editor/utils.py
-drwxrwxr-x   0 miltondp  (1000) miltondp  (1000)        0 2023-03-17 13:07:28.339774 manubot-ai-editor-0.4.1/libs/manubot_ai_editor.egg-info/
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)     2556 2023-03-17 13:07:28.000000 manubot-ai-editor-0.4.1/libs/manubot_ai_editor.egg-info/PKG-INFO
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)      467 2023-03-17 13:07:28.000000 manubot-ai-editor-0.4.1/libs/manubot_ai_editor.egg-info/SOURCES.txt
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)        1 2023-03-17 13:07:28.000000 manubot-ai-editor-0.4.1/libs/manubot_ai_editor.egg-info/dependency_links.txt
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)       20 2023-03-17 13:07:28.000000 manubot-ai-editor-0.4.1/libs/manubot_ai_editor.egg-info/requires.txt
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)       19 2023-03-17 13:07:28.000000 manubot-ai-editor-0.4.1/libs/manubot_ai_editor.egg-info/top_level.txt
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)       38 2023-03-17 13:07:28.343774 manubot-ai-editor-0.4.1/setup.cfg
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)      938 2023-03-17 13:06:41.000000 manubot-ai-editor-0.4.1/setup.py
-drwxrwxr-x   0 miltondp  (1000) miltondp  (1000)        0 2023-03-17 13:07:28.339774 manubot-ai-editor-0.4.1/tests/
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)    61034 2023-03-17 13:06:41.000000 manubot-ai-editor-0.4.1/tests/test_completion_model.py
--rw-rw-r--   0 miltondp  (1000) miltondp  (1000)    38761 2023-01-25 04:03:27.000000 manubot-ai-editor-0.4.1/tests/test_editor.py
+drwxrwxr-x   0 miltondp  (1000) miltondp  (1000)        0 2023-04-07 14:54:32.087034 manubot-ai-editor-0.4.2/
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)     2556 2023-04-07 14:54:32.087034 manubot-ai-editor-0.4.2/PKG-INFO
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)     2074 2023-03-17 13:06:41.000000 manubot-ai-editor-0.4.2/README.md
+drwxrwxr-x   0 miltondp  (1000) miltondp  (1000)        0 2023-04-07 14:54:32.083034 manubot-ai-editor-0.4.2/libs/
+drwxrwxr-x   0 miltondp  (1000) miltondp  (1000)        0 2023-04-07 14:54:32.087034 manubot-ai-editor-0.4.2/libs/manubot_ai_editor/
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)        0 2023-01-25 04:03:27.000000 manubot-ai-editor-0.4.2/libs/manubot_ai_editor/__init__.py
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)    16525 2023-03-09 16:05:14.000000 manubot-ai-editor-0.4.2/libs/manubot_ai_editor/editor.py
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)     2848 2023-04-07 14:50:29.000000 manubot-ai-editor-0.4.2/libs/manubot_ai_editor/env_vars.py
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)    20101 2023-04-07 14:50:29.000000 manubot-ai-editor-0.4.2/libs/manubot_ai_editor/models.py
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)      632 2023-01-25 04:03:27.000000 manubot-ai-editor-0.4.2/libs/manubot_ai_editor/utils.py
+drwxrwxr-x   0 miltondp  (1000) miltondp  (1000)        0 2023-04-07 14:54:32.087034 manubot-ai-editor-0.4.2/libs/manubot_ai_editor.egg-info/
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)     2556 2023-04-07 14:54:32.000000 manubot-ai-editor-0.4.2/libs/manubot_ai_editor.egg-info/PKG-INFO
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)      467 2023-04-07 14:54:32.000000 manubot-ai-editor-0.4.2/libs/manubot_ai_editor.egg-info/SOURCES.txt
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)        1 2023-04-07 14:54:32.000000 manubot-ai-editor-0.4.2/libs/manubot_ai_editor.egg-info/dependency_links.txt
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)       20 2023-04-07 14:54:32.000000 manubot-ai-editor-0.4.2/libs/manubot_ai_editor.egg-info/requires.txt
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)       19 2023-04-07 14:54:32.000000 manubot-ai-editor-0.4.2/libs/manubot_ai_editor.egg-info/top_level.txt
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)       38 2023-04-07 14:54:32.087034 manubot-ai-editor-0.4.2/setup.cfg
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)      938 2023-04-07 14:52:24.000000 manubot-ai-editor-0.4.2/setup.py
+drwxrwxr-x   0 miltondp  (1000) miltondp  (1000)        0 2023-04-07 14:54:32.087034 manubot-ai-editor-0.4.2/tests/
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)    62136 2023-04-07 14:50:29.000000 manubot-ai-editor-0.4.2/tests/test_completion_model.py
+-rw-rw-r--   0 miltondp  (1000) miltondp  (1000)    38761 2023-01-25 04:03:27.000000 manubot-ai-editor-0.4.2/tests/test_editor.py
```

### Comparing `manubot-ai-editor-0.4.1/PKG-INFO` & `manubot-ai-editor-0.4.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: manubot-ai-editor
-Version: 0.4.1
+Version: 0.4.2
 Summary: A Manubot plugin to revise a manuscript using GPT-3
 Home-page: https://github.com/greenelab/manubot-ai-editor
 Author: Milton Pividori
 Author-email: miltondp@gmail.com
 License: BSD-2-Clause Plus Patent
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: BSD License
```

### Comparing `manubot-ai-editor-0.4.1/README.md` & `manubot-ai-editor-0.4.2/README.md`

 * *Files identical despite different names*

### Comparing `manubot-ai-editor-0.4.1/libs/manubot_ai_editor/editor.py` & `manubot-ai-editor-0.4.2/libs/manubot_ai_editor/editor.py`

 * *Files identical despite different names*

### Comparing `manubot-ai-editor-0.4.1/libs/manubot_ai_editor/env_vars.py` & `manubot-ai-editor-0.4.2/libs/manubot_ai_editor/env_vars.py`

 * *Files 13% similar despite different names*

```diff
@@ -47,7 +47,15 @@
 # by running again the model. The AI Editor will try five (5) times in these
 # cases. This variable allows to specify the number of retries.
 RETRY_COUNT = "AI_EDITOR_RETRY_COUNT"
 
 # If specified, only these file names will be revised. Multiple files can be
 # specified, separated by commas. For example: "01.intro.md,02.review.md"
 FILENAMES_TO_REVISE = "AI_EDITOR_FILENAMES_TO_REVISE"
+
+# It allows to specify a single, custom prompt for all sections. For example:
+# "proofread and revise the following paragraph", where the tool will automatically
+# append the characters ':\n\n' followed by the paragraph at the end of the prompt.
+# Another example is "proofread and revise the following paragraph from the section {section_name} of scientific mauscript:\n\n{paragraph_text}".
+# The complete list of placeholders is: {paragraph_text}, {section_name},
+# {manuscript_title}, {manuscript_keywords}.
+CUSTOM_PROMPT = "AI_EDITOR_CUSTOM_PROMPT"
```

### Comparing `manubot-ai-editor-0.4.1/libs/manubot_ai_editor/models.py` & `manubot-ai-editor-0.4.2/libs/manubot_ai_editor/models.py`

 * *Files 1% similar despite different names*

```diff
@@ -270,14 +270,22 @@
             It contains two paragraphs of text: the command for the model
             ("Revise...") and the paragraph to revise.
 
             If self.edit_endpoint is True, then returns a tuple with two strings:
              1) the instructions to be used by the model for the revision of the paragraph,
              2) the paragraph to revise.
         """
+
+        if env_vars.CUSTOM_PROMPT in os.environ:
+            prompt = os.environ[env_vars.CUSTOM_PROMPT]
+            print(
+                f"Using custom prompt from environment variable '{env_vars.CUSTOM_PROMPT}'"
+            )
+            return f"{prompt}:\n\n{paragraph_text}"
+
         if section_name in ("abstract",):
             prompt = f"""
                 Revise the following paragraph from the {section_name} of an academic paper (with the title '{self.title}' and keywords '{", ".join(self.keywords)}')
                 so the research problem/question is clear,
                    the solution proposed is clear,
                    the text grammar is correct, spelling errors are fixed,
                    and the text is in active voice and has a clear sentence structure
```

### Comparing `manubot-ai-editor-0.4.1/libs/manubot_ai_editor/utils.py` & `manubot-ai-editor-0.4.2/libs/manubot_ai_editor/utils.py`

 * *Files identical despite different names*

### Comparing `manubot-ai-editor-0.4.1/libs/manubot_ai_editor.egg-info/PKG-INFO` & `manubot-ai-editor-0.4.2/libs/manubot_ai_editor.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: manubot-ai-editor
-Version: 0.4.1
+Version: 0.4.2
 Summary: A Manubot plugin to revise a manuscript using GPT-3
 Home-page: https://github.com/greenelab/manubot-ai-editor
 Author: Milton Pividori
 Author-email: miltondp@gmail.com
 License: BSD-2-Clause Plus Patent
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: BSD License
```

### Comparing `manubot-ai-editor-0.4.1/setup.py` & `manubot-ai-editor-0.4.2/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 # twine upload dist/*
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="manubot-ai-editor",
-    version="0.4.1",
+    version="0.4.2",
     author="Milton Pividori",
     author_email="miltondp@gmail.com",
     description="A Manubot plugin to revise a manuscript using GPT-3",
     license="BSD-2-Clause Plus Patent",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/greenelab/manubot-ai-editor",
```

### Comparing `manubot-ai-editor-0.4.1/tests/test_completion_model.py` & `manubot-ai-editor-0.4.2/tests/test_completion_model.py`

 * *Files 1% similar despite different names*

```diff
@@ -23,14 +23,55 @@
                 title="Test title",
                 keywords=["test", "keywords"],
             )
     finally:
         os.environ = _environ
 
 
+def test_get_prompt_no_custom_prompt():
+    model = GPT3CompletionModel(
+        title="Test title",
+        keywords=["test", "keywords"],
+    )
+
+    paragraph_text = """
+This is the first sentence.
+And this is the second sentence.
+Finally, the third sentence.
+    """.strip()
+
+    prompt = model.get_prompt(paragraph_text, "introduction")
+    assert prompt.startswith("Revise the following paragraph from the ")
+    assert prompt.endswith(paragraph_text[-20:])
+
+
+@mock.patch.dict(
+    "os.environ",
+    {env_vars.CUSTOM_PROMPT: "proofread and revise the following paragraph"},
+)
+def test_get_prompt_custom_prompt_no_placeholders():
+    model = GPT3CompletionModel(
+        title="Test title",
+        keywords=["test", "keywords"],
+    )
+
+    paragraph_text = """
+This is the first sentence.
+And this is the second sentence.
+Finally, the third sentence.
+    """.strip()
+
+    prompt = model.get_prompt(paragraph_text, "introduction")
+    assert (
+        prompt == f"proofread and revise the following paragraph:\n\n{paragraph_text}"
+    )
+
+    # TODO: add other sections, should return same output
+
+
 @mock.patch.dict("os.environ", {env_vars.OPENAI_API_KEY: "env_var_test_value"})
 def test_model_object_init_with_openai_api_key_as_environment_variable():
     GPT3CompletionModel(
         title="Test title",
         keywords=["test", "keywords"],
     )
```

### Comparing `manubot-ai-editor-0.4.1/tests/test_editor.py` & `manubot-ai-editor-0.4.2/tests/test_editor.py`

 * *Files identical despite different names*

