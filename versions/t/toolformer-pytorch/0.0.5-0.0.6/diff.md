# Comparing `tmp/toolformer-pytorch-0.0.5.tar.gz` & `tmp/toolformer-pytorch-0.0.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "toolformer-pytorch-0.0.5.tar", last modified: Tue Apr  4 16:24:58 2023, max compression
+gzip compressed data, was "toolformer-pytorch-0.0.6.tar", last modified: Thu Apr  6 18:13:16 2023, max compression
```

## Comparing `toolformer-pytorch-0.0.5.tar` & `toolformer-pytorch-0.0.6.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 16:24:58.267003 toolformer-pytorch-0.0.5/
--rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-04-04 16:24:45.000000 toolformer-pytorch-0.0.5/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      639 2023-04-04 16:24:58.267003 toolformer-pytorch-0.0.5/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2551 2023-04-04 16:24:45.000000 toolformer-pytorch-0.0.5/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-04 16:24:58.267003 toolformer-pytorch-0.0.5/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      868 2023-04-04 16:24:45.000000 toolformer-pytorch-0.0.5/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 16:24:58.267003 toolformer-pytorch-0.0.5/toolformer_pytorch/
--rw-r--r--   0 runner    (1001) docker     (123)      186 2023-04-04 16:24:45.000000 toolformer-pytorch-0.0.5/toolformer_pytorch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5592 2023-04-04 16:24:45.000000 toolformer-pytorch-0.0.5/toolformer_pytorch/palm.py
--rw-r--r--   0 runner    (1001) docker     (123)     4528 2023-04-04 16:24:45.000000 toolformer-pytorch-0.0.5/toolformer_pytorch/prompts.py
--rw-r--r--   0 runner    (1001) docker     (123)    12888 2023-04-04 16:24:45.000000 toolformer-pytorch-0.0.5/toolformer_pytorch/toolformer_pytorch.py
--rw-r--r--   0 runner    (1001) docker     (123)     6578 2023-04-04 16:24:45.000000 toolformer-pytorch-0.0.5/toolformer_pytorch/tools.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 16:24:58.267003 toolformer-pytorch-0.0.5/toolformer_pytorch.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      639 2023-04-04 16:24:58.000000 toolformer-pytorch-0.0.5/toolformer_pytorch.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      392 2023-04-04 16:24:58.000000 toolformer-pytorch-0.0.5/toolformer_pytorch.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-04 16:24:58.000000 toolformer-pytorch-0.0.5/toolformer_pytorch.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       37 2023-04-04 16:24:58.000000 toolformer-pytorch-0.0.5/toolformer_pytorch.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-04 16:24:58.000000 toolformer-pytorch-0.0.5/toolformer_pytorch.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:13:16.851510 toolformer-pytorch-0.0.6/
+-rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-04-06 18:13:04.000000 toolformer-pytorch-0.0.6/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      639 2023-04-06 18:13:16.851510 toolformer-pytorch-0.0.6/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2551 2023-04-06 18:13:04.000000 toolformer-pytorch-0.0.6/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 18:13:16.851510 toolformer-pytorch-0.0.6/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      868 2023-04-06 18:13:04.000000 toolformer-pytorch-0.0.6/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:13:16.851510 toolformer-pytorch-0.0.6/toolformer_pytorch/
+-rw-r--r--   0 runner    (1001) docker     (123)      186 2023-04-06 18:13:04.000000 toolformer-pytorch-0.0.6/toolformer_pytorch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5592 2023-04-06 18:13:04.000000 toolformer-pytorch-0.0.6/toolformer_pytorch/palm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4529 2023-04-06 18:13:04.000000 toolformer-pytorch-0.0.6/toolformer_pytorch/prompts.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13015 2023-04-06 18:13:04.000000 toolformer-pytorch-0.0.6/toolformer_pytorch/toolformer_pytorch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6917 2023-04-06 18:13:04.000000 toolformer-pytorch-0.0.6/toolformer_pytorch/tools.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:13:16.851510 toolformer-pytorch-0.0.6/toolformer_pytorch.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      639 2023-04-06 18:13:16.000000 toolformer-pytorch-0.0.6/toolformer_pytorch.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      392 2023-04-06 18:13:16.000000 toolformer-pytorch-0.0.6/toolformer_pytorch.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 18:13:16.000000 toolformer-pytorch-0.0.6/toolformer_pytorch.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       37 2023-04-06 18:13:16.000000 toolformer-pytorch-0.0.6/toolformer_pytorch.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 18:13:16.000000 toolformer-pytorch-0.0.6/toolformer_pytorch.egg-info/top_level.txt
```

### Comparing `toolformer-pytorch-0.0.5/LICENSE` & `toolformer-pytorch-0.0.6/LICENSE`

 * *Files identical despite different names*

### Comparing `toolformer-pytorch-0.0.5/PKG-INFO` & `toolformer-pytorch-0.0.6/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: toolformer-pytorch
-Version: 0.0.5
+Version: 0.0.6
 Summary: Toolformer - Pytorch
 Home-page: https://github.com/lucidrains/toolformer-pytorch
 Author: Phil Wang
 Author-email: lucidrains@gmail.com
 License: MIT
 Keywords: artificial intelligence,deep learning,transformers,attention mechanism,automated-tool-use
 Classifier: Development Status :: 4 - Beta
```

### Comparing `toolformer-pytorch-0.0.5/README.md` & `toolformer-pytorch-0.0.6/README.md`

 * *Files identical despite different names*

### Comparing `toolformer-pytorch-0.0.5/setup.py` & `toolformer-pytorch-0.0.6/setup.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from setuptools import setup, find_packages
 
 setup(
   name = 'toolformer-pytorch',
   packages = find_packages(exclude=[]),
-  version = '0.0.5',
+  version = '0.0.6',
   license='MIT',
   description = 'Toolformer - Pytorch',
   author = 'Phil Wang',
   author_email = 'lucidrains@gmail.com',
   long_description_content_type = 'text/markdown',
   url = 'https://github.com/lucidrains/toolformer-pytorch',
   keywords = [
```

### Comparing `toolformer-pytorch-0.0.5/toolformer_pytorch/palm.py` & `toolformer-pytorch-0.0.6/toolformer_pytorch/palm.py`

 * *Files identical despite different names*

### Comparing `toolformer-pytorch-0.0.5/toolformer_pytorch/prompts.py` & `toolformer-pytorch-0.0.6/toolformer_pytorch/prompts.py`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -59,8 +59,8 @@
 Output: The current day of the week is [Calendar()] Wednesday.
 Input: The number of days from now until Christmas is 30.
 Output: The number of days from now until Christmas is [Calendar()] 30.
 Input: The store is never open on the weekend, so today it is closed.
 Output: The store is never open on the weekend, so today [Calendar()] it is closed.
 Input: x
 Output:
-"""
+"""
```

### Comparing `toolformer-pytorch-0.0.5/toolformer_pytorch/toolformer_pytorch.py` & `toolformer-pytorch-0.0.6/toolformer_pytorch/toolformer_pytorch.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from functools import partial
+from functools import partial, wraps
 from collections import namedtuple
 
 import torch
 import torch.nn.functional as F
 from torch import nn, einsum
 
 from einops import rearrange, reduce
@@ -52,14 +52,18 @@
     mask = (t == token_id)
 
     has_occurred = mask.cumsum(dim = -1)
     has_occurred = F.pad(has_occurred, (1, 0), value = 0.)
 
     return (has_occurred < occurrence).sum(dim = -1).long()
 
+# invoking api call functions
+
+
+
 # sampling api related functions
 # they do greedy sampling, but encourage sampling api calls by auto-selecting <api> when that token is in the top k = 10
 
 @beartype
 @torch.no_grad()
 def sample(
     model: nn.Module,
@@ -194,15 +198,15 @@
         seq_len = seq_len,
         **kwargs
     )
 
     sampled = call_apis(sampled)
 
     sampled_seq_len = sampled.shape[-1]
-    null_positions = sampled_seq_len + 1 # handle sequences that do not have api calls
+    null_positions = sampled_seq_len # handle sequences that do not have api calls
 
     pos_starting_at_end_of_api = find_indices_of(
         sampled,
         api_end_token_id,
         occurrence = occurrence
     )
 
@@ -351,16 +355,18 @@
 
 @beartype
 class Toolformer(nn.Module):
     def __init__(
         self,
         model: nn.Module,
         tool: Callable,
-        teach_tool_prompt: str
+        teach_tool_prompt: str,
+        filters: dict[str, Callable[[str], bool]] = dict()
     ):
         super().__init__()
         self.model = model
         self.tool = tool
         self.teach_tool_prompt = teach_tool_prompt
+        self.filters = filters
 
     def forward(self):
         raise NotImplementedError
```

### Comparing `toolformer-pytorch-0.0.5/toolformer_pytorch/tools.py` & `toolformer-pytorch-0.0.6/toolformer_pytorch/tools.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,17 +1,26 @@
-import requests
-import calendar
-import wolframalpha
-import datetime
-from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
-from operator import pow, truediv, mul, add, sub  
-
-# Optional imports
-from googleapiclient.discovery import build
-    
+import os
+
+try:
+    from dotenv import load_dotenv
+    load_dotenv()
+
+    import requests
+    import calendar
+    import wolframalpha
+    import datetime
+    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
+    from operator import pow, truediv, mul, add, sub
+
+    # Optional imports
+    from googleapiclient.discovery import build
+
+except ImportError:
+    print('please run `pip install tools-requirements.txt` first at project directory')
+    exit()
 
 '''
 Calendar
 
 Uses Python's datetime and calendar libraries to retrieve the current date.
 
 input - None
@@ -49,32 +58,33 @@
 def colbertv2_get_request(url: str, query: str, k: int):
     payload = {'query': query, 'k': k}
     res = requests.get(url, params=payload)
 
     topk = res.json()['topk'][:k]
     return topk
 
-def WikiSearch(input_query: str):
-    k = 10
-    retrieval_model = ColBERTv2('http://ec2-44-228-128-229.us-west-2.compute.amazonaws.com:8893/api/search')
+def WikiSearch(
+    input_query: str,
+    url: str = 'http://ec2-44-228-128-229.us-west-2.compute.amazonaws.com:8893/api/search',
+    k: int = 10
+):
+    retrieval_model = ColBERTv2(url)
     output = retrieval_model(input_query, k)
     return output
 
-
 '''
 Machine Translation - NLLB-600M
 
 Uses HuggingFace's transformers library to translate input query to English.
 
 input_query - A string, the input query (e.g. "what is a dog?")
 
 output - A string, the translated input query.
 '''
-def MT(input_query: str):
-    model_name = "facebook/nllb-200-distilled-600M"
+def MT(input_query: str, model_name: str = "facebook/nllb-200-distilled-600M"):
     tokenizer = AutoTokenizer.from_pretrained(model_name)
     model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
     input_ids = tokenizer(input_query, return_tensors='pt')
     outputs = model.generate(
         **input_ids,
         forced_bos_token_id=tokenizer.lang_code_to_id["eng_Latn"], 
         )
@@ -121,15 +131,15 @@
 input_query - A string, the input query (e.g. "what is 2 + 2?")
 
 output - A string, the answer to the input query
 
 wolfarm_alpha_appid - your Wolfram Alpha API key
 '''
 def WolframAlphaCalculator(input_query: str):
-    wolfram_alpha_appid = 'YOUR_WOLFRAM_ALPHA_APPID'
+    wolfram_alpha_appid = os.environ.get('WOLFRAM_ALPHA_APPID')
     wolfram_client = wolframalpha.Client(wolfram_alpha_appid)
     res = wolfram_client.query(input_query)
     assumption = next(res.pods).text
     answer = next(res.results).text
     return f'Assumption: {assumption} \nAnswer: {answer}'
 
 
@@ -146,18 +156,18 @@
 output - A list of dictionaries, each dictionary is a Google Search result
 '''
 def custom_search(query, api_key, cse_id, **kwargs):
     service = build("customsearch", "v1", developerKey=api_key)
     res = service.cse().list(q=query, cx=cse_id, **kwargs).execute()
     return res['items']
 
-def google_search(input_query: str):
-    api_key = "YOUR_GOOGLE_API_KEY"
-    cse_id = 'YOUR_GOOGLE_CSE_ID' 
-    num_results = 10
+def google_search(input_query: str, num_results: int = 10):
+    api_key = os.environ.get('GOOGLE_API_KEY')
+    cse_id = os.environ.get('GOOGLE_CSE_ID')
+
     metadata_results = []
     results = custom_search(input_query, num=num_results, api_key=api_key, cse_id=cse_id)
     for result in results:
         metadata_result = {
             "snippet": result["snippet"],
             "title": result["title"],
             "link": result["link"],
@@ -173,32 +183,39 @@
 
 input_query: The query to search for.
 bing_subscription_key: Your Bing API key.
 num_results: The number of results to return.
 
 output: A list of dictionaries, each dictionary is a Bing Search result
 '''
-def _bing_search_results(search_term: str, bing_subscription_key: str, count: int):
+def _bing_search_results(
+    search_term: str,
+    bing_subscription_key: str,
+    count: int,
+    url: str = "https://api.bing.microsoft.com/v7.0/search"
+):
     headers = {"Ocp-Apim-Subscription-Key": bing_subscription_key}
     params = {
         "q": search_term,
         "count": count,
         "textDecorations": True,
         "textFormat": "HTML",
     }
     response = requests.get(
-        "https://api.bing.microsoft.com/v7.0/search", headers=headers, params=params
+        url, headers=headers, params=params
     )
     response.raise_for_status()
     search_results = response.json()
     return search_results["webPages"]["value"]
 
-def bing_search(input_query: str):
-    bing_subscription_key = "YOUR BING API KEY" 
-    num_results = 10
+def bing_search(
+    input_query: str,
+    num_results: int = 10
+):
+    bing_subscription_key = os.environ.get("BING_API_KEY")
     metadata_results = []
     results = _bing_search_results(input_query, bing_subscription_key, count=num_results)
     for result in results:
         metadata_result = {
             "snippet": result["snippet"],
             "title": result["name"],
             "link": result["url"],
@@ -213,17 +230,16 @@
 
     print(Calculator('400/1400')) # For Optional Basic Calculator
 
     print(WikiSearch('What is a dog?')) # Outputs a list of strings, each string is a Wikipedia document
 
     print(MT("Un chien c'est quoi?")) # What is a dog?
 
-
     # Optional Tools
 
     print(WolframAlphaCalculator('What is 2 + 2?')) # 4
 
     print(google_search('What is a dog?')) 
     # Outputs a list of dictionaries, each dictionary is a Google Search result
 
     print(bing_search('What is a dog?')) 
-    # Outputs a list of dictionaries, each dictionary is a Bing Search result
+    # Outputs a list of dictionaries, each dictionary is a Bing Search result
```

### Comparing `toolformer-pytorch-0.0.5/toolformer_pytorch.egg-info/PKG-INFO` & `toolformer-pytorch-0.0.6/toolformer_pytorch.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: toolformer-pytorch
-Version: 0.0.5
+Version: 0.0.6
 Summary: Toolformer - Pytorch
 Home-page: https://github.com/lucidrains/toolformer-pytorch
 Author: Phil Wang
 Author-email: lucidrains@gmail.com
 License: MIT
 Keywords: artificial intelligence,deep learning,transformers,attention mechanism,automated-tool-use
 Classifier: Development Status :: 4 - Beta
```

