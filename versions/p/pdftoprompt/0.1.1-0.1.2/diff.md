# Comparing `tmp/pdftoprompt-0.1.1.tar.gz` & `tmp/pdftoprompt-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pdftoprompt-0.1.1.tar", max compression
+gzip compressed data, was "pdftoprompt-0.1.2.tar", max compression
```

## Comparing `pdftoprompt-0.1.1.tar` & `pdftoprompt-0.1.2.tar`

### file list

```diff
@@ -1,5 +1,5 @@
--rw-r--r--   0        0        0      134 2023-04-05 19:47:45.239910 pdftoprompt-0.1.1/pdftoprompt/__init__.py
--rw-r--r--   0        0        0     4541 2023-04-07 04:38:13.220689 pdftoprompt-0.1.1/pdftoprompt/compressor.py
--rw-r--r--   0        0        0      603 2023-04-07 05:25:58.755383 pdftoprompt-0.1.1/pyproject.toml
--rw-r--r--   0        0        0     7591 2023-04-07 05:25:25.420610 pdftoprompt-0.1.1/README.md
--rw-r--r--   0        0        0     8253 1970-01-01 00:00:00.000000 pdftoprompt-0.1.1/PKG-INFO
+-rw-r--r--   0        0        0      134 2023-04-05 19:47:45.239910 pdftoprompt-0.1.2/pdftoprompt/__init__.py
+-rw-r--r--   0        0        0     5284 2023-04-07 13:10:26.122291 pdftoprompt-0.1.2/pdftoprompt/compressor.py
+-rw-r--r--   0        0        0      603 2023-04-07 13:29:17.955044 pdftoprompt-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0     6850 2023-04-07 13:28:59.460167 pdftoprompt-0.1.2/README.md
+-rw-r--r--   0        0        0     7499 1970-01-01 00:00:00.000000 pdftoprompt-0.1.2/PKG-INFO
```

### Comparing `pdftoprompt-0.1.1/pdftoprompt/compressor.py` & `pdftoprompt-0.1.2/pdftoprompt/compressor.py`

 * *Files 12% similar despite different names*

```diff
@@ -4,14 +4,15 @@
 from pdf2image import convert_from_path
 import openai
 from dotenv import load_dotenv
 from typing import Optional
 from tempfile import NamedTemporaryFile
 import requests
 from urllib.parse import urlparse
+import re
 
 
 def is_url(path):
     try:
         result = urlparse(path)
         return all([result.scheme, result.netloc])
     except ValueError:
@@ -74,22 +75,41 @@
 def calculate_compression_factor(text):
     tokens = len(text) // 4
     factor = tokens / 3500
     return factor
 
 
 def chunk_text(text, max_tokens=3500):
-    tokens = len(text) // 4
+    text = text.replace('\n', ' ')
+    chunk_length = max_tokens * 4
+    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
     chunks = []
-    start = 0
-    for _ in range(tokens // max_tokens):
-        end = start + max_tokens * 4
-        chunks.append(text[start:end])
-        start = end
-    chunks.append(text[start:])
+    current_chunk = ""
+
+    for sentence in sentences:
+        if len(current_chunk) + len(sentence) + 1 <= chunk_length:
+            current_chunk += sentence
+            if not current_chunk.endswith(('.', '?', '!')):
+                current_chunk += ' '
+        else:
+            if current_chunk:
+                chunks.append(current_chunk.strip())
+            
+            if len(sentence) > chunk_length:
+                start = 0
+                while start < len(sentence):
+                    end = min(start + chunk_length, len(sentence))
+                    chunks.append(sentence[start:end].strip())
+                    start = end
+            else:
+                current_chunk = sentence + ' '
+
+    if current_chunk:
+        chunks.append(current_chunk.strip())
+
     return chunks
 
 
 def compress_with_gpt4(chunk_list, factor):
     openai.api_key = os.getenv('OPENAI_API_KEY')
     compressed_text = ""
     for chunk in chunk_list:
```

### Comparing `pdftoprompt-0.1.1/pyproject.toml` & `pdftoprompt-0.1.2/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "pdftoprompt"
-version = "0.1.1"
+version = "0.1.2"
 description = "Python library to abbreviate a PDF file to GPT 8k prompt length"
 authors = ["Christopher Carroll Smith <chriscarrollsmith@gmail.com>"]
 readme = "README.md"
 packages = [{include = "pdftoprompt"}]
 
 [tool.poetry.dependencies]
 python = "^3.9"
```

### Comparing `pdftoprompt-0.1.1/README.md` & `pdftoprompt-0.1.2/README.md`

 * *Files 11% similar despite different names*

```diff
@@ -46,15 +46,28 @@
 compressed_text = compress_pdf(file_path)
 print(compressed_text)
 ```
 
 
 The above code distills an academic paper titled ["PromptChainer: Chaining Large Language Model Prompts through Visual Programming"](https://arxiv.org/pdf/2203.06566.pdf) down to the following GPT-interpretable prompt:
 
-"PromptChainer: Chaining LLM Prompts through Visual Programming\nAuthors: Tongshuang Wu, Ellen Jiang, Aaron Donsbach, Jeff Gray, Alejandra Molina, Michael Terry, Carrie J. Cai\n\nABSTRACT:\nLLMs enable rapid prototyping of ML functionalities, but complex tasks need chaining multiple LLM runs. PromptChainer is an interactive interface for visually programming chains. Case studies with designers and developers show it supports building prototypes for various applications. Open questions involve scaling chains for more complex tasks and supporting low-fi chain prototyping.\n\n1 INTRODUCTION:\nLLMs like GPT-3 and Jurassic-1 allow easy customization for new tasks using natural language prompts. However, complex tasks may require chaining multiple LLM runs. PromptChainer aims to support users in authoring their own LLM chains.\n\n3 PROMPTCHAINER: INTERFACE REQUIREMENT ANALYSIS & DESIGN:\nChallenges in authoring chains include:\nC.1: Versatility of LLMs and need for data transformations\nC.2: Instability of LLM function signatures\nC.3: Likelihood of cascading errors\n\nPromptChainer addresses these challenges with a Chain View for authoring chain structure, a Node View for implementing individual nodes, and debugging features.\n\n4 CASE STUDIES: AUTHORS BUILDING LLM CHAINS:\nQualitative analysis of case studies with designers and developers reveals patterns in chain building and debugging. Open challenges include scaling chains for tasks with high interdependency or logical complexity and finding a sweet spot for prompting to quickly prototype multiple alternative chains.(Figure 1B) for single step (node) authoring and chain debugging support. Chain View: visual panel for building/viewing chains (Figure 1A). Nodes represent chain steps, edges denote connections/input-output flow. Node visualization (Figure 4): named inputs (𝑎2) and outputs (𝑎3) to connect nodes. Inspired by node-edge-based visual programming platforms2, we provide node previews for chaining transparency, including status icon (errors) (Figure 4𝑎1) and data views (𝑎3and𝑎4). Node Types (Figure 3): LLM nodes (Generic, Classifier), helper nodes (data transformation, evaluation, custom JavaScript), communication nodes (external API calls). Example gallery for versatility, prompting patterns.\n\nNode View: inspect, implement, test individual nodes (Figure 1B). PromptChainer parses input names based on LLM prompt/node type, updates global chain with local edits (addressing C.2). Interactive debugging: unit test nodes (Figure 4𝑐1), end-to-end assessment/logging (Figure 4 𝑐2), breakpoint debugging/output editing (Figure 4𝑐3).\n\nUser feedback sessions (preliminary study): 4 participants (3 designers, 1 developer) with prior non-chained prompt experience. Study focused on chaining prompts, interface tutorial, and task completion sessions. Underlying LLM: LaMDA [16] (137 billion parameters, comparable to GPT-3). Study results: users built diverse chains (branching logic, iterating content, extensible prototypes) using PromptChainer, supporting various construction strategies and multi-level debugging. Remaining challenges: coherence between interdependent sub-tasks, tracking user contributions, and supporting chain debugging.Chains with complex logic and interdependent parallel tasks can decrease coherence. P4\'s story writing chain generated a paragraph for each outline point, resulting in a less coherent essay. A similar challenge was faced by a pilot study user, prompting future investigation into methods considering inter-dependency.\n\nComplex decomposition in chains can be overwhelming to track, as seen in P1\'s music chatbot chain. Enhancing tracing capabilities and execution visualizations is a potential solution.\n\nPre-creating LLM prompts for sub-tasks might lead to users feeling invested in their chain decomposition, limiting exploration of other structures. Encouraging low-fi prototyping of multiple chains and supporting "half-baked" chain construction can improve outcomes.\n\nTime constraints and task decomposition strategies for larger, complex tasks should be explored. PromptChainer can encourage further node decomposition if extensive prompting efforts are unsuccessful."
+<blockquote>
+PromptChainer: Chaining LLM Prompts via Visual Programming by Tongshuang Wu, Ellen Jiang, Aaron Donsbach, Jeff Gray, Alejandra Molina, Michael Terry, and Carrie J.Cai explores LLM chain authoring. Pilot studies show users need support transforming data between steps and debugging chains. PromptChainer is designed to address these needs, providing an interactive interface for visually programming chains. Case studies with four designers and developers demonstrate its ability to support building prototypes for various applications. Open questions remain on scaling chains to more complex tasks and supporting low-fi chain prototyping.3.2 Interface Design
+Designing the interface in Figure 1 addresses challenges with Chain View (Figure 1A) for chain structure authoring, Node View (Figure 1B) for single step authoring, and chain debugging support. Chain View is a visual panel for building and viewing chains, with nodes representing steps and edges denoting connections. Node visualization (Figure 4) includes named inputs/outputs, status icons, and data views. Node types (Figure 3) cover diverse user needs, including Generic LLM nodes, LLM Classifier nodes, helper nodes, and communication nodes. Example gallery helps users develop mental models and prompting patterns.
+
+Node View enables node inspection, implementation, testing, and automatic input name parsing based on LLM prompts or JavaScript function signatures. Global chain consistency is ensured by automatically updating input handles when prompt templates change. Interactive debugging functionalities address cascading error challenges and enable unit testing, end-to-end assessments, and breakpoint debugging.
+
+4 USER FEEDBACK SESSIONS
+Preliminary study aimed to understand users' desired chains, PromptChainer support, and challenges faced. Users proposed diverse tasks, some with branching logic and others with iterative content. Chaining patterns included parallel logic branches and incremental iterations on content. Chaining rationales included addressing LLM limitations and making prototypes more generalizable. PromptChainer supported various chain construction strategies and multi-level debugging. Participants used predefined helper nodes more than customized JS nodes.Q: Remaining challenges in chain authoring?
+A: 1. Ensuring coherence in interdependent sub-tasks; 2. Tracking chains with complex logic.
+
+Challenges include maintaining coherence in chains with interdependent parallel tasks and tracking complex decomposition. P4's story writing chain generated a paragraph for each outline point, resulting in a final essay lacking coherence. One user created an input node to manually track previous outputs. Future work could investigate methods considering inter-dependency between parallel sub-tasks and enhancing PromptChainer's tracing capabilities. Customized chain grouping and execution visualizations may help address these issues.
+
+Study limitations: Participants may have felt invested in their pre-created prompts, making them less inclined to consider other chain structures. Prior prototyping work suggests concurrent consideration of multiple alternatives can lead to better outcomes. Future work could explore low-fi prototyping of multiple chains and task decomposition strategies for larger, more complex tasks. Encouraging users to create "half-baked" chain constructions without investing too much time in prompting upfront may also be beneficial.
+</blockquote>
 
 Note that when we ask GPT to compress the text, we specifically instruct it that the text doesn't have to be human-readable. The goal here isn't to get a shortened version that works for humans. It's to get a shortened version that works as a Large Language Model prompt.
 
 ### OCR
 
 In theory, you should be able to use OCR by setting the `compress_pdf` function's `use_ocr` argument to True, but that functionality requires that you install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and add it to your system path, and I can't vouch for this functionality because I haven't tested it yet.
```

#### encoding

```diff
@@ -1 +1 @@
-utf-8
+us-ascii
```

### Comparing `pdftoprompt-0.1.1/PKG-INFO` & `pdftoprompt-0.1.2/PKG-INFO`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pdftoprompt
-Version: 0.1.1
+Version: 0.1.2
 Summary: Python library to abbreviate a PDF file to GPT 8k prompt length
 Author: Christopher Carroll Smith
 Author-email: chriscarrollsmith@gmail.com
 Requires-Python: >=3.9,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
@@ -65,15 +65,28 @@
 compressed_text = compress_pdf(file_path)
 print(compressed_text)
 ```
 
 
 The above code distills an academic paper titled ["PromptChainer: Chaining Large Language Model Prompts through Visual Programming"](https://arxiv.org/pdf/2203.06566.pdf) down to the following GPT-interpretable prompt:
 
-"PromptChainer: Chaining LLM Prompts through Visual Programming\nAuthors: Tongshuang Wu, Ellen Jiang, Aaron Donsbach, Jeff Gray, Alejandra Molina, Michael Terry, Carrie J. Cai\n\nABSTRACT:\nLLMs enable rapid prototyping of ML functionalities, but complex tasks need chaining multiple LLM runs. PromptChainer is an interactive interface for visually programming chains. Case studies with designers and developers show it supports building prototypes for various applications. Open questions involve scaling chains for more complex tasks and supporting low-fi chain prototyping.\n\n1 INTRODUCTION:\nLLMs like GPT-3 and Jurassic-1 allow easy customization for new tasks using natural language prompts. However, complex tasks may require chaining multiple LLM runs. PromptChainer aims to support users in authoring their own LLM chains.\n\n3 PROMPTCHAINER: INTERFACE REQUIREMENT ANALYSIS & DESIGN:\nChallenges in authoring chains include:\nC.1: Versatility of LLMs and need for data transformations\nC.2: Instability of LLM function signatures\nC.3: Likelihood of cascading errors\n\nPromptChainer addresses these challenges with a Chain View for authoring chain structure, a Node View for implementing individual nodes, and debugging features.\n\n4 CASE STUDIES: AUTHORS BUILDING LLM CHAINS:\nQualitative analysis of case studies with designers and developers reveals patterns in chain building and debugging. Open challenges include scaling chains for tasks with high interdependency or logical complexity and finding a sweet spot for prompting to quickly prototype multiple alternative chains.(Figure 1B) for single step (node) authoring and chain debugging support. Chain View: visual panel for building/viewing chains (Figure 1A). Nodes represent chain steps, edges denote connections/input-output flow. Node visualization (Figure 4): named inputs (𝑎2) and outputs (𝑎3) to connect nodes. Inspired by node-edge-based visual programming platforms2, we provide node previews for chaining transparency, including status icon (errors) (Figure 4𝑎1) and data views (𝑎3and𝑎4). Node Types (Figure 3): LLM nodes (Generic, Classifier), helper nodes (data transformation, evaluation, custom JavaScript), communication nodes (external API calls). Example gallery for versatility, prompting patterns.\n\nNode View: inspect, implement, test individual nodes (Figure 1B). PromptChainer parses input names based on LLM prompt/node type, updates global chain with local edits (addressing C.2). Interactive debugging: unit test nodes (Figure 4𝑐1), end-to-end assessment/logging (Figure 4 𝑐2), breakpoint debugging/output editing (Figure 4𝑐3).\n\nUser feedback sessions (preliminary study): 4 participants (3 designers, 1 developer) with prior non-chained prompt experience. Study focused on chaining prompts, interface tutorial, and task completion sessions. Underlying LLM: LaMDA [16] (137 billion parameters, comparable to GPT-3). Study results: users built diverse chains (branching logic, iterating content, extensible prototypes) using PromptChainer, supporting various construction strategies and multi-level debugging. Remaining challenges: coherence between interdependent sub-tasks, tracking user contributions, and supporting chain debugging.Chains with complex logic and interdependent parallel tasks can decrease coherence. P4\'s story writing chain generated a paragraph for each outline point, resulting in a less coherent essay. A similar challenge was faced by a pilot study user, prompting future investigation into methods considering inter-dependency.\n\nComplex decomposition in chains can be overwhelming to track, as seen in P1\'s music chatbot chain. Enhancing tracing capabilities and execution visualizations is a potential solution.\n\nPre-creating LLM prompts for sub-tasks might lead to users feeling invested in their chain decomposition, limiting exploration of other structures. Encouraging low-fi prototyping of multiple chains and supporting "half-baked" chain construction can improve outcomes.\n\nTime constraints and task decomposition strategies for larger, complex tasks should be explored. PromptChainer can encourage further node decomposition if extensive prompting efforts are unsuccessful."
+<blockquote>
+PromptChainer: Chaining LLM Prompts via Visual Programming by Tongshuang Wu, Ellen Jiang, Aaron Donsbach, Jeff Gray, Alejandra Molina, Michael Terry, and Carrie J.Cai explores LLM chain authoring. Pilot studies show users need support transforming data between steps and debugging chains. PromptChainer is designed to address these needs, providing an interactive interface for visually programming chains. Case studies with four designers and developers demonstrate its ability to support building prototypes for various applications. Open questions remain on scaling chains to more complex tasks and supporting low-fi chain prototyping.3.2 Interface Design
+Designing the interface in Figure 1 addresses challenges with Chain View (Figure 1A) for chain structure authoring, Node View (Figure 1B) for single step authoring, and chain debugging support. Chain View is a visual panel for building and viewing chains, with nodes representing steps and edges denoting connections. Node visualization (Figure 4) includes named inputs/outputs, status icons, and data views. Node types (Figure 3) cover diverse user needs, including Generic LLM nodes, LLM Classifier nodes, helper nodes, and communication nodes. Example gallery helps users develop mental models and prompting patterns.
+
+Node View enables node inspection, implementation, testing, and automatic input name parsing based on LLM prompts or JavaScript function signatures. Global chain consistency is ensured by automatically updating input handles when prompt templates change. Interactive debugging functionalities address cascading error challenges and enable unit testing, end-to-end assessments, and breakpoint debugging.
+
+4 USER FEEDBACK SESSIONS
+Preliminary study aimed to understand users' desired chains, PromptChainer support, and challenges faced. Users proposed diverse tasks, some with branching logic and others with iterative content. Chaining patterns included parallel logic branches and incremental iterations on content. Chaining rationales included addressing LLM limitations and making prototypes more generalizable. PromptChainer supported various chain construction strategies and multi-level debugging. Participants used predefined helper nodes more than customized JS nodes.Q: Remaining challenges in chain authoring?
+A: 1. Ensuring coherence in interdependent sub-tasks; 2. Tracking chains with complex logic.
+
+Challenges include maintaining coherence in chains with interdependent parallel tasks and tracking complex decomposition. P4's story writing chain generated a paragraph for each outline point, resulting in a final essay lacking coherence. One user created an input node to manually track previous outputs. Future work could investigate methods considering inter-dependency between parallel sub-tasks and enhancing PromptChainer's tracing capabilities. Customized chain grouping and execution visualizations may help address these issues.
+
+Study limitations: Participants may have felt invested in their pre-created prompts, making them less inclined to consider other chain structures. Prior prototyping work suggests concurrent consideration of multiple alternatives can lead to better outcomes. Future work could explore low-fi prototyping of multiple chains and task decomposition strategies for larger, more complex tasks. Encouraging users to create "half-baked" chain constructions without investing too much time in prompting upfront may also be beneficial.
+</blockquote>
 
 Note that when we ask GPT to compress the text, we specifically instruct it that the text doesn't have to be human-readable. The goal here isn't to get a shortened version that works for humans. It's to get a shortened version that works as a Large Language Model prompt.
 
 ### OCR
 
 In theory, you should be able to use OCR by setting the `compress_pdf` function's `use_ocr` argument to True, but that functionality requires that you install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and add it to your system path, and I can't vouch for this functionality because I haven't tested it yet.
```

#### encoding

```diff
@@ -1 +1 @@
-utf-8
+us-ascii
```

