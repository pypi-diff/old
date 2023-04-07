# Comparing `tmp/ctakesclient-2.1.1.tar.gz` & `tmp/ctakesclient-3.0.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ctakesclient-2.1.1.tar", last modified: Thu Mar 30 19:29:44 2023, max compression
+gzip compressed data, was "ctakesclient-3.0.0.tar", last modified: Fri Apr  7 14:05:48 2023, max compression
```

## Comparing `ctakesclient-2.1.1.tar` & `ctakesclient-3.0.0.tar`

### file list

```diff
@@ -1,52 +1,52 @@
--rw-r--r--   0        0        0    11357 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/LICENSE
--rw-r--r--   0        0        0     2245 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/README.md
--rw-r--r--   0        0        0      162 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/ctakesclient/__init__.py
--rw-r--r--   0        0        0     5104 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/ctakesclient/client.py
--rw-r--r--   0        0        0      534 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/ctakesclient/exceptions.py
--rw-r--r--   0        0        0     7412 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/ctakesclient/filesystem.py
--rw-r--r--   0        0        0     5469 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/ctakesclient/resources/SemGroups_2018.bsv
--rw-r--r--   0        0        0     9865 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/ctakesclient/resources/covid_symptoms.bsv
--rw-r--r--   0        0        0    16785 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/ctakesclient/text2fhir.py
--rw-r--r--   0        0        0     2424 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/ctakesclient/transformer.py
--rw-r--r--   0        0        0     8846 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/ctakesclient/typesystem.py
--rw-r--r--   0        0        0      634 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/Makefile
--rw-r--r--   0        0        0      795 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/api.md
--rw-r--r--   0        0        0     1246 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/conf.py
--rw-r--r--   0        0        0     4180 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/diagram/MatchText.png
--rw-r--r--   0        0        0     2699 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/diagram/UmlsConcept.png
--rw-r--r--   0        0        0     4791 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/diagram/begin.png
--rw-r--r--   0        0        0     4075 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/diagram/code.png
--rw-r--r--   0        0        0     3215 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/diagram/codingScheme.png
--rw-r--r--   0        0        0     2557 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/diagram/conceptAttributes.png
--rw-r--r--   0        0        0     6469 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/diagram/cui.png
--rw-r--r--   0        0        0      551 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/diagram/diagram.bnf
--rw-r--r--   0        0        0     4732 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/diagram/end.png
--rw-r--r--   0        0        0    10252 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/diagram/polarity.png
--rw-r--r--   0        0        0      755 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/diagram/rr-1.63.png
--rw-r--r--   0        0        0     3874 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/diagram/text.png
--rw-r--r--   0        0        0     4070 2023-03-30 19:29:34.881712 ctakesclient-2.1.1/docs/diagram/tui.png
--rw-r--r--   0        0        0     3528 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/docs/index.md
--rw-r--r--   0        0        0      800 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/docs/make.bat
--rw-r--r--   0        0        0     1292 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/pyproject.toml
--rwxr-xr-x   0        0        0     7211 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/scripts/polarity-diff-report.py
--rw-r--r--   0        0        0        0 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/__init__.py
--rw-r--r--   0        0        0     1258 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/conftest.py
--rw-r--r--   0        0        0        0 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/integration/__init__.py
--rw-r--r--   0        0        0     5363 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/integration/test_client_covid_symptoms.py
--rw-r--r--   0        0        0     1595 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/integration/test_client_ctakes_rest_server.py
--rw-r--r--   0        0        0     2389 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/integration/test_negation.py
--rw-r--r--   0        0        0     3284 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/integration/test_negation_transformer.py
--rw-r--r--   0        0        0      135 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/resources/concepts.bsv
--rw-r--r--   0        0        0       63 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/resources/semantics.bsv
--rw-r--r--   0        0        0     3135 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/resources/synthentic.txt
--rw-r--r--   0        0        0    58544 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/resources/synthetic.json
--rw-r--r--   0        0        0      680 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/resources/test_negation_hard.txt
--rw-r--r--   0        0        0     6699 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/resources/test_physician_note.json
--rw-r--r--   0        0        0      144 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/resources/test_physician_note.txt
--rw-r--r--   0        0        0     1464 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/test_client.py
--rw-r--r--   0        0        0     3968 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/test_filesystem.py
--rw-r--r--   0        0        0     1640 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/test_resources.py
--rw-r--r--   0        0        0    13571 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/test_text2fhir.py
--rw-r--r--   0        0        0      648 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/test_transformer.py
--rw-r--r--   0        0        0     2916 2023-03-30 19:29:34.885712 ctakesclient-2.1.1/tests/test_typesystem.py
--rw-r--r--   0        0        0     3319 1970-01-01 00:00:00.000000 ctakesclient-2.1.1/PKG-INFO
+-rw-r--r--   0        0        0    11357 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/LICENSE
+-rw-r--r--   0        0        0     2447 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/README.md
+-rw-r--r--   0        0        0      162 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/ctakesclient/__init__.py
+-rw-r--r--   0        0        0     5278 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/ctakesclient/client.py
+-rw-r--r--   0        0        0      534 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/ctakesclient/exceptions.py
+-rw-r--r--   0        0        0     7412 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/ctakesclient/filesystem.py
+-rw-r--r--   0        0        0     5469 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/ctakesclient/resources/SemGroups_2018.bsv
+-rw-r--r--   0        0        0     9865 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/ctakesclient/resources/covid_symptoms.bsv
+-rw-r--r--   0        0        0    16785 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/ctakesclient/text2fhir.py
+-rw-r--r--   0        0        0     2549 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/ctakesclient/transformer.py
+-rw-r--r--   0        0        0     8846 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/ctakesclient/typesystem.py
+-rw-r--r--   0        0        0      634 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/Makefile
+-rw-r--r--   0        0        0      795 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/api.md
+-rw-r--r--   0        0        0     1246 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/conf.py
+-rw-r--r--   0        0        0     4180 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/diagram/MatchText.png
+-rw-r--r--   0        0        0     2699 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/diagram/UmlsConcept.png
+-rw-r--r--   0        0        0     4791 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/diagram/begin.png
+-rw-r--r--   0        0        0     4075 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/diagram/code.png
+-rw-r--r--   0        0        0     3215 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/diagram/codingScheme.png
+-rw-r--r--   0        0        0     2557 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/diagram/conceptAttributes.png
+-rw-r--r--   0        0        0     6469 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/diagram/cui.png
+-rw-r--r--   0        0        0      551 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/diagram/diagram.bnf
+-rw-r--r--   0        0        0     4732 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/diagram/end.png
+-rw-r--r--   0        0        0    10252 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/diagram/polarity.png
+-rw-r--r--   0        0        0      755 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/diagram/rr-1.63.png
+-rw-r--r--   0        0        0     3874 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/diagram/text.png
+-rw-r--r--   0        0        0     4070 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/diagram/tui.png
+-rw-r--r--   0        0        0     3528 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/index.md
+-rw-r--r--   0        0        0      800 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/docs/make.bat
+-rw-r--r--   0        0        0     1302 2023-04-07 14:05:40.657647 ctakesclient-3.0.0/pyproject.toml
+-rwxr-xr-x   0        0        0     7287 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/scripts/polarity-diff-report.py
+-rw-r--r--   0        0        0        0 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/__init__.py
+-rw-r--r--   0        0        0     1258 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/conftest.py
+-rw-r--r--   0        0        0        0 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/integration/__init__.py
+-rw-r--r--   0        0        0     5440 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/integration/test_client_covid_symptoms.py
+-rw-r--r--   0        0        0     1644 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/integration/test_client_ctakes_rest_server.py
+-rw-r--r--   0        0        0     2440 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/integration/test_negation.py
+-rw-r--r--   0        0        0     3377 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/integration/test_negation_transformer.py
+-rw-r--r--   0        0        0      135 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/resources/concepts.bsv
+-rw-r--r--   0        0        0       63 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/resources/semantics.bsv
+-rw-r--r--   0        0        0     3135 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/resources/synthentic.txt
+-rw-r--r--   0        0        0    58544 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/resources/synthetic.json
+-rw-r--r--   0        0        0      680 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/resources/test_negation_hard.txt
+-rw-r--r--   0        0        0     6699 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/resources/test_physician_note.json
+-rw-r--r--   0        0        0      144 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/resources/test_physician_note.txt
+-rw-r--r--   0        0        0     1625 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/test_client.py
+-rw-r--r--   0        0        0     3968 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/test_filesystem.py
+-rw-r--r--   0        0        0     1640 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/test_resources.py
+-rw-r--r--   0        0        0    13571 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/test_text2fhir.py
+-rw-r--r--   0        0        0     1394 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/test_transformer.py
+-rw-r--r--   0        0        0     2916 2023-04-07 14:05:40.661647 ctakesclient-3.0.0/tests/test_typesystem.py
+-rw-r--r--   0        0        0     3558 1970-01-01 00:00:00.000000 ctakesclient-3.0.0/PKG-INFO
```

### Comparing `ctakesclient-2.1.1/LICENSE` & `ctakesclient-3.0.0/LICENSE`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/README.md` & `ctakesclient-3.0.0/README.md`

 * *Files 18% similar despite different names*

```diff
@@ -5,15 +5,22 @@
 - Unified Medical Language System ([UMLS](https://nlm.nih.gov/research/umls))
 
 # Quickstart
 Clinical text fragment or entire physician note.
 
 ```python
 physician_note = 'Chief Complaint: Patient c/o cough, denies fever, recent COVID test negative. Denies smoking.'
-output = ctakesclient.client.post(physician_note)
+output = await ctakesclient.client.post(physician_note)
+```
+
+Note that `ctakesclient` uses an async API.
+If your code is not async, you can simply wrap calls in `asyncio.run()`:
+
+```python
+output = asyncio.run(ctakesclient.client.post(physician_note))
 ```
 
 # Output
 
 This client parses responses into lists of MatchText and UmlsConcept.
 
 ```
```

### Comparing `ctakesclient-2.1.1/ctakesclient/client.py` & `ctakesclient-3.0.0/ctakesclient/client.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,12 +1,14 @@
 """HTTP client for medical language"""
 
 import os
 import logging
-import requests
+
+import httpx
+
 from ctakesclient.typesystem import CtakesJSON
 
 ###############################################################################
 #
 # https://github.com/Machine-Learning-for-Medical-Language/ctakes-covid-container
 #
 # https://github.com/Machine-Learning-for-Medical-Language/cnlp_transformers#negation-api
@@ -20,51 +22,53 @@
 
     :return: URL_CTAKES_REST env variable or default using localhost
     """
     url = os.environ.get("URL_CTAKES_REST")
     return url or "http://localhost:8080/ctakes-web-rest/service/analyze"
 
 
-def post(sentence: str, url: str = None) -> dict:
+async def post(sentence: str, url: str = None, client: httpx.AsyncClient = None) -> dict:
     """
     Sends clinical text to cTAKES for analysis and returns the raw server response
 
     You likely want the higher-level `extract` method instead of this one.
     For one, it will return a nice `CtakesJSON` object instead of raw json.
     For another, the raw cTAKES response has some oddities, like utf16-based span indexes,
     which `extract` fixes for you.
 
     :param sentence: clinical text to send to cTAKES
     :param url: cTAKES REST server fully qualified path
+    :param client: optional existing HTTPX client session
     :return: Parsed json response from cTAKES
     """
     url = url or get_url_ctakes_rest()
+    client = client or httpx.AsyncClient()
     logging.debug(url)
-    response = requests.post(
+    response = await client.post(
         url,
-        data=sentence.encode("utf8"),
+        content=sentence.encode("utf8"),
         headers={
             "Content-Type": "text/plain; charset=UTF-8",
         },
-        timeout=300,  # TODO: consider exposing a pass-through timeout parameter
     )
     response.raise_for_status()
     return response.json()
 
 
-def extract(sentence: str, url: str = None) -> CtakesJSON:
+async def extract(sentence: str, url: str = None, client: httpx.AsyncClient = None) -> CtakesJSON:
     """
     Send clinical text to cTAKES for analysis and packages the response up for you
 
     :param sentence: clinical text to send to cTAKES
     :param url: cTAKES REST server fully qualified path
+    :param client: optional existing HTTPX client session
     :return: CtakesJSON wrapper
     """
-    url = url or get_url_ctakes_rest()
-    ner = CtakesJSON(post(sentence, url))
+    response = await post(sentence, url=url, client=client)
+    ner = CtakesJSON(response)
     _adjust_character_indexes(sentence, ner)  # Fix Java character indexes into Python ones
     return ner
 
 
 ###############################################################################
 #
 # Helpers
```

### Comparing `ctakesclient-2.1.1/ctakesclient/exceptions.py` & `ctakesclient-3.0.0/ctakesclient/exceptions.py`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/ctakesclient/filesystem.py` & `ctakesclient-3.0.0/ctakesclient/filesystem.py`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/ctakesclient/resources/SemGroups_2018.bsv` & `ctakesclient-3.0.0/ctakesclient/resources/SemGroups_2018.bsv`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/ctakesclient/resources/covid_symptoms.bsv` & `ctakesclient-3.0.0/ctakesclient/resources/covid_symptoms.bsv`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/ctakesclient/text2fhir.py` & `ctakesclient-3.0.0/ctakesclient/text2fhir.py`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/ctakesclient/transformer.py` & `ctakesclient-3.0.0/ctakesclient/transformer.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,12 +1,14 @@
 """HTTP client for medical language"""
 
-from typing import List
 import os
-import requests
+from typing import List, Tuple
+
+import httpx
+
 from ctakesclient.exceptions import ClientError
 from ctakesclient.typesystem import Polarity
 
 ###############################################################################
 #
 # https://github.com/Machine-Learning-for-Medical-Language/cnlp_transformers#negation-api
 #
@@ -19,26 +21,29 @@
 
     :return: CTAKES_URL_NEGATION env variable or default using localhost
     """
     url = os.environ.get("URL_CNLP_NEGATION")
     return url or "http://localhost:8000/negation/process"
 
 
-def list_polarity(sentence: str, spans: list, url: str = None) -> List[Polarity]:
+async def list_polarity(
+    sentence: str, spans: List[Tuple[int, int]], url: str = None, client: httpx.AsyncClient = None
+) -> List[Polarity]:
     """
     :param sentence: clinical text to send to cTAKES
     :param spans: list of spans where each span is a tuple of (begin,end)
     :param url: Clinical NLP Transformer: Negation API
+    :param client: optional existing HTTPX client session
     :return: List of Polarity (positive or negated)
     """
     url = url or get_url_cnlp_negation()
-    doc = {"doc_text": sentence, "entities": spans}
+    client = client or httpx.AsyncClient()
 
-    # TODO: consider exposing a pass-through timeout parameter
-    response = requests.post(url=url, json=doc, timeout=300)
+    doc = {"doc_text": sentence, "entities": spans}
+    response = await client.post(url=url, json=doc)
     response.raise_for_status()
     response = response.json()
     polarities = []
 
     for status in response["statuses"]:
         # NOT negated (double negative)
         if status == -1:
@@ -51,22 +56,19 @@
 
     if len(spans) != len(polarities):
         raise ClientError("Number of Spans and Polarities did not match: " f"{spans}, {polarities}")
 
     return polarities
 
 
-def map_polarity(sentence: str, spans: list, url: str = None) -> dict:
+async def map_polarity(
+    sentence: str, spans: List[Tuple[int, int]], url: str = None, client: httpx.AsyncClient = None
+) -> dict:
     """
     :param sentence: clinical text to send to cTAKES
     :param spans: list of spans where each span is a tuple of (begin,end)
     :param url: Clinical NLP Transformer: Negation API
+    :param client: optional existing HTTPX client session
     :return: Map of Polarity key=span, value=polarity
     """
-    url = url or get_url_cnlp_negation()
-    polarities = list_polarity(sentence, spans, url)
-    mapped = {}
-
-    for span, polarity in zip(spans, polarities):
-        mapped[span] = polarity
-
-    return mapped
+    polarities = await list_polarity(sentence, spans, url=url, client=client)
+    return dict(zip(spans, polarities))
```

### Comparing `ctakesclient-2.1.1/ctakesclient/typesystem.py` & `ctakesclient-3.0.0/ctakesclient/typesystem.py`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/Makefile` & `ctakesclient-3.0.0/docs/Makefile`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/api.md` & `ctakesclient-3.0.0/docs/api.md`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/conf.py` & `ctakesclient-3.0.0/docs/conf.py`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/diagram/MatchText.png` & `ctakesclient-3.0.0/docs/diagram/MatchText.png`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/diagram/UmlsConcept.png` & `ctakesclient-3.0.0/docs/diagram/UmlsConcept.png`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/diagram/begin.png` & `ctakesclient-3.0.0/docs/diagram/begin.png`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/diagram/code.png` & `ctakesclient-3.0.0/docs/diagram/code.png`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/diagram/codingScheme.png` & `ctakesclient-3.0.0/docs/diagram/codingScheme.png`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/diagram/conceptAttributes.png` & `ctakesclient-3.0.0/docs/diagram/conceptAttributes.png`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/diagram/cui.png` & `ctakesclient-3.0.0/docs/diagram/cui.png`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/diagram/diagram.bnf` & `ctakesclient-3.0.0/docs/diagram/diagram.bnf`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/diagram/end.png` & `ctakesclient-3.0.0/docs/diagram/end.png`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/diagram/polarity.png` & `ctakesclient-3.0.0/docs/diagram/polarity.png`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/diagram/rr-1.63.png` & `ctakesclient-3.0.0/docs/diagram/rr-1.63.png`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/diagram/text.png` & `ctakesclient-3.0.0/docs/diagram/text.png`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/diagram/tui.png` & `ctakesclient-3.0.0/docs/diagram/tui.png`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/index.md` & `ctakesclient-3.0.0/docs/index.md`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/docs/make.bat` & `ctakesclient-3.0.0/docs/make.bat`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/pyproject.toml` & `ctakesclient-3.0.0/pyproject.toml`

 * *Files 12% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 [project]
 name = "ctakesclient"
-requires-python = ">= 3.7"
+requires-python = ">= 3.8"
 dependencies = [
     "fhirclient >= 4.1",
-    "requests",
+    "httpx",
 ]
 authors = [
   { name="Andy McMurry, PhD", email="andrew.mcmurry@childrens.harvard.edu" },
   { name="Michael Terry", email="michael.terry@childrens.harvard.edu" },
   { name="Tim Miller", email="timothy.miller@childrens.harvard.edu" },
 ]
 description = "cTAKES client support for accessing cTAKES REST services"
@@ -47,11 +47,12 @@
     "myst-parser", # markdown support in sphinx
     "sphinx < 6",
     "sphinx-rtd-theme",
 ]
 tests = [
     "ddt",
     "pytest",
+    "respx",
 ]
 dev = [
     "pre-commit"
 ]
```

### Comparing `ctakesclient-2.1.1/scripts/polarity-diff-report.py` & `ctakesclient-3.0.0/scripts/polarity-diff-report.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 #!/usr/bin/env python3
 # pylint: disable=invalid-name
 """Generates and shows polarity difference reports between cTAKES and cNLP"""
 
 import argparse
+import asyncio
 import csv
 import json
 import os
 import sys
 import time
 from json.decoder import JSONDecodeError
 
@@ -16,24 +17,24 @@
 
 def default(parser, args):
     del args
 
     parser.print_help()
 
 
-def compare_note_polarity(text: str):
+async def compare_note_polarity(text: str):
     """
     Prints difference summary (if any)
     """
-    ner = ctakesclient.client.extract(text)
+    ner = await ctakesclient.client.extract(text)
 
     matches = ner.list_match()
     spans = ner.list_spans(matches)
 
-    polarities_cnlp = ctakesclient.transformer.list_polarity(text, spans)
+    polarities_cnlp = await ctakesclient.transformer.list_polarity(text, spans)
     if len(matches) != len(polarities_cnlp):
         raise JSONDecodeError("Polarity lists had different lengths!", text, 0)
 
     differing = []
     for i in range(len(matches)):
         if matches[i].polarity.value != polarities_cnlp[i].value:
             differing.append(
@@ -42,15 +43,15 @@
                     "match": matches[i].as_json(),
                 }
             )
 
     return differing
 
 
-def calculate(parser, args):
+async def calculate(parser, args):
     del parser
 
     output_path = os.path.splitext(args.notes_path)[0] + ".pdr.ndjson"
     if os.path.exists(output_path) and not args.resume:
         print("Output file already exists. Use --continue if this is intended.", file=sys.stderr)
         sys.exit(1)
 
@@ -80,15 +81,15 @@
                     if note["INSTANCE_NUM"] == start_processing_after:
                         start_processing_after = None
                     continue
 
                 note_tic = time.perf_counter()
                 try:
                     error = None
-                    differences = compare_note_polarity(note["OBSERVATION_BLOB"])
+                    differences = await compare_note_polarity(note["OBSERVATION_BLOB"])
                 except JSONDecodeError as e:
                     error = str(e)
                     differences = []
 
                 json.dump(
                     {
                         # Save the instance id for later sanity checking
@@ -155,15 +156,15 @@
         print("Context:", note_context(note["note"], m))
         found_any = True
 
     if not found_any:
         print("No matching differences found!")
 
 
-def report(parser, args):
+async def report(parser, args):
     del parser
 
     if args.note and args.instance:
         print("You can only specify a note number or an instance number but " "not both", file=sys.stderr)
         sys.exit(1)
 
     if not args.note and not args.instance:
@@ -182,15 +183,15 @@
                 show_note(args, note_data)
                 return
 
     print("Note not found!", file=sys.stderr)
     sys.exit(1)
 
 
-def main():
+async def main():
     parser = argparse.ArgumentParser()
     subparsers = parser.add_subparsers()
 
     parser.set_defaults(func=default)
 
     calculate_parser = subparsers.add_parser("calculate")
     calculate_parser.add_argument("notes_path", metavar="notes.csv")
@@ -204,12 +205,12 @@
     report_parser.add_argument("--note", type=int, action="store", help="only show differences for this note number")
     report_parser.add_argument("--instance", type=int, action="store", help="only show differences for this note ID")
     report_parser.add_argument("--diff", type=int, action="store", help="only show this specific difference number")
     report_parser.add_argument("--mention", action="append", default=[], help="only show these mention types")
     report_parser.set_defaults(func=report)
 
     args = parser.parse_args()
-    args.func(parser, args)
+    await args.func(parser, args)
 
 
 if __name__ == "__main__":
-    main()
+    asyncio.run(main())
```

### Comparing `ctakesclient-2.1.1/tests/conftest.py` & `ctakesclient-3.0.0/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/tests/integration/test_client_covid_symptoms.py` & `ctakesclient-3.0.0/tests/integration/test_client_covid_symptoms.py`

 * *Files 2% similar despite different names*

```diff
@@ -28,25 +28,25 @@
     Headache = ["R51.9", "R51", "Headache", "Headaches", "HA"]
     Dyspnea = ["R06.0", "SOB", "Short of Breath"]
     Aches = ["Myalgias", "Muscle Aches"]
     Anosmia = ["R43", "R43.0", "Loss of smell", "loss of taste"]
 
 
 @ddt.ddt
-class TestCtakesClient(unittest.TestCase):
+class TestCtakesClient(unittest.IsolatedAsyncioTestCase):
     """Test case for ctakes client extracting covid symptoms"""
 
-    def test_chief_complaint_is_symptom(self):
+    async def test_chief_complaint_is_symptom(self):
         for bsv in covid_symptoms():
 
             chief_complaint = f"Chief Complaint: {bsv.text.lower()} ."
 
             print(f"{chief_complaint}")
 
-            res = ctakesclient.client.extract(bsv.text)
+            res = await ctakesclient.client.extract(bsv.text)
 
             ss_list = res.list_sign_symptom()
             match_list = res.list_match()
 
             # validated manually
             excludes = [
                 "nasal congestion",  # Nasal (anatomic site)
@@ -75,26 +75,27 @@
                 "muscle pains",  # muscle (anatomic site)
                 "muscle soreness",
             ]  # muscle (anatomic site)
 
             if bsv.text.lower() not in excludes:
                 self.assertDictEqual({"root": match_list}, {"root": ss_list})
 
-    def test_covid_symptoms_medical_synonyms(self):
+    async def test_covid_symptoms_medical_synonyms(self):
         """
         Test if COVID19 symptom synonyms are mapped in the BSV dictionary.
         """
         expected = []
         miss_icd = []
         actual = []
         for symptom in Symptom:
             for synonym in symptom.value:
 
                 text = f"Chief Complaint: {synonym}"
-                found = ctakesclient.client.extract(text).list_match_text()
+                ner = await ctakesclient.client.extract(text)
+                found = ner.list_match_text()
                 found = [hit.title() for hit in found]
 
                 if synonym.title() in found:
                     expected.append(synonym.title())
                     actual.append(synonym.title())
                 elif len(synonym) < 3:
                     miss_icd.append(synonym)
@@ -106,15 +107,15 @@
         diff = set(expected).difference(set(actual))
 
         self.assertEqual(set(), diff, "diff should be empty, missing")
 
     @ddt.data(
         *ctakesclient.filesystem.covid_symptoms(),
     )
-    def test_covid_symptoms_exist_in_response(self, bsv):
+    async def test_covid_symptoms_exist_in_response(self, bsv):
         """
         Symptoms of COVID-19
         https://www.cdc.gov/coronavirus/2019-ncov/symptoms-testing/symptoms.html
 
         Test if every COVID symptom is found in server dictionary.
         https://github.com/Machine-Learning-for-Medical-Language/ctakes-client-py/blob/main/ctakesclient/resources/covid_symptoms.bsv
         -->
@@ -129,15 +130,15 @@
             "R53.81",
             "R53.83",
             "R68.83",
         ]
         if bsv.text in known_issues:
             pytest.xfail(f"Known cTAKES failure with {bsv.text}")
 
-        ner = ctakesclient.client.extract(bsv.text)
+        ner = await ctakesclient.client.extract(bsv.text)
 
         cui_list = []
         text_list = []
 
         for match in ner.list_sign_symptom():
             text_list.append(match.text)
             for concept in match.conceptAttributes:
```

### Comparing `ctakesclient-2.1.1/tests/integration/test_client_ctakes_rest_server.py` & `ctakesclient-3.0.0/tests/integration/test_client_ctakes_rest_server.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,38 +1,38 @@
 """Tests for the cTAKES REST API"""
 
 import unittest
 import ctakesclient
 from tests.test_resources import LoadResource
 
 
-class TestClientCtakesRestServer(unittest.TestCase):
+class TestClientCtakesRestServer(unittest.IsolatedAsyncioTestCase):
     """Test case for REST requests"""
 
-    def test_physician_note(self):
+    async def test_physician_note(self):
         """
         Test calling REST server returns JSON that matches expected.
         Strong typing (Polarity, MatchText, UmlsConcept) enforced during
         serialization.
         """
         physician_note = LoadResource.PHYSICIAN_NOTE_TEXT.value
         expected = LoadResource.PHYSICIAN_NOTE_JSON.value
 
-        actual1 = ctakesclient.client.extract(physician_note).as_json()
-        actual2 = ctakesclient.client.extract(physician_note).as_json()
+        actual1 = (await ctakesclient.client.extract(physician_note)).as_json()
+        actual2 = (await ctakesclient.client.extract(physician_note)).as_json()
 
         unittest.TestCase.maxDiff = None
 
         self.assertDictEqual(expected, actual1, "JSON did not match round trip serialization")
         self.assertDictEqual(actual1, actual2, "calling service twice produces same results")
 
-    def test_unicode(self):
+    async def test_unicode(self):
         """Ensure that we handle utf8/unicode correctly"""
         # First, make sure we don't blow up just by sending it
-        ner = ctakesclient.client.extract("patient feels 🤒 with fever")
+        ner = await ctakesclient.client.extract("patient feels 🤒 with fever")
 
         # Then confirm that our spans are correct (0-based and character-based)
         self.assertLess(0, len(ner.list_sign_symptom()))
         for symptom in ner.list_sign_symptom():  # sometimes cTAKES breaks it into multiple matches
             self.assertEqual("fever", symptom.text)
             self.assertEqual(21, symptom.begin)
             self.assertEqual(26, symptom.end)
```

### Comparing `ctakesclient-2.1.1/tests/integration/test_negation.py` & `ctakesclient-3.0.0/tests/integration/test_negation.py`

 * *Files 14% similar despite different names*

```diff
@@ -26,21 +26,21 @@
     return "The patient has a sore knee and headache but denies nausea " "and has no anosmia."
 
 
 def pretty(result: dict) -> str:
     return json.dumps(result, indent=4)
 
 
-class TestNegationCtakesDefaultContext(unittest.TestCase):
+class TestNegationCtakesDefaultContext(unittest.IsolatedAsyncioTestCase):
     """
     https://cwiki.apache.org/confluence/display/CTAKES/cTAKES+3.0+-+NE+Contexts
     """
 
-    def test_ctakes_covid_symptoms(self):
-        ner = ctakesclient.client.extract(note_negated_ros_review_of_symptoms())
+    async def test_ctakes_covid_symptoms(self):
+        ner = await ctakesclient.client.extract(note_negated_ros_review_of_symptoms())
 
         symptoms_dict = ctakesclient.filesystem.covid_symptoms()
         symptoms_fp = []
 
         for match in ner.list_match(Polarity.pos):
             for concept in match.conceptAttributes:
                 if concept.cui in symptoms_dict:
@@ -50,26 +50,26 @@
             [],
             symptoms_fp,
             ("false positives found in purely NEGATED physician " f"note review of systems {symptoms_fp}"),
         )
 
     # pylint: disable-next=line-too-long
     @unittest.skip("https://github.com/Machine-Learning-for-Medical-Language/ctakes-client-py/issues/8")
-    def test_patient_denies(self):
+    async def test_patient_denies(self):
         """
         Test everything in this example note is negated.
         Unfortunately ctakes negation algorithm is not perfect.
         See linked issue above.
         """
         text = note_negated_denies()
-        ner = ctakesclient.client.extract(text)
+        ner = await ctakesclient.client.extract(text)
         false_positives = ner.list_match_text(Polarity.pos)
         self.assertEqual([], false_positives)
 
-    def test_history_of_headache(self):
+    async def test_history_of_headache(self):
         text = note_positive_headache()
-        ner = ctakesclient.client.extract(text)
+        ner = await ctakesclient.client.extract(text)
         self.assertIn("headache", ner.list_match_text())
 
 
 if __name__ == "__main__":
     unittest.main()
```

### Comparing `ctakesclient-2.1.1/tests/integration/test_negation_transformer.py` & `ctakesclient-3.0.0/tests/integration/test_negation_transformer.py`

 * *Files 20% similar despite different names*

```diff
@@ -7,90 +7,90 @@
 from .test_negation import (
     note_negated_denies,
     note_negated_ros_review_of_symptoms,
     note_negation_api_example,
 )
 
 
-def list_false_positive_ss(physician_note: str) -> List[str]:
+async def list_false_positive_ss(physician_note: str) -> List[str]:
     """
     :param physician_note: note containing negated entries.
     :return: strings of symptoms that were actually marked *Polarity.pos*
     """
-    ner = ctakesclient.client.extract(physician_note)
+    ner = await ctakesclient.client.extract(physician_note)
     symptoms = ner.list_sign_symptom()
     spans = ner.list_spans(symptoms)
-    polarities_cnlp = ctakesclient.transformer.list_polarity(sentence=physician_note, spans=spans)
+    polarities_cnlp = await ctakesclient.transformer.list_polarity(sentence=physician_note, spans=spans)
 
     fp = []
 
     for index in range(0, len(symptoms)):
         polarity = polarities_cnlp[index]
 
         if polarity != Polarity.neg:
             fp.append(symptoms[index].text)
             # print(f'symptoms={symptoms}, polarities={polarities_cnlp}, '
             #       f'text={note}')
     return fp
 
 
-def debug_helper(physician_note: str):
+async def debug_helper(physician_note: str):
     print("##################################################################")
     print(physician_note)
 
-    ner = ctakesclient.client.extract(physician_note)
+    ner = await ctakesclient.client.extract(physician_note)
 
     matches = ner.list_match()
     spans = ner.list_spans(matches)
 
     for match in matches:
         print(f"{match.polarity.name}\t{match.span()}\t{match.text}\t\t" f"{match.type.value}")
 
-    polarities_cnlp = ctakesclient.transformer.list_polarity(physician_note, spans)
+    polarities_cnlp = await ctakesclient.transformer.list_polarity(physician_note, spans)
     polarities_ctakes = ner.list_polarity(spans)
 
     print("##################################################################")
     print("cNLP=")
     print(polarities_cnlp)
 
     print("##################################################################")
     print("cTAKES=")
     print(polarities_ctakes)
 
 
-class TestNegationTransformer(unittest.TestCase):
+class TestNegationTransformer(unittest.IsolatedAsyncioTestCase):
     """Test case for the machine learning negation API"""
 
     def test_negation_api_example(self):
         """
         Test negation using the example provided by upstream.
         (the author of the server library, Tim Miller, PhD)
         """
         self.assertPolarityCompatible(note_negation_api_example())
 
-    def test_negated_denies(self):
+    async def test_negated_denies(self):
         """
         Test simple 'patient denies' type statements.
         """
-        self.assertEqual([], list_false_positive_ss(note_negated_denies()))
+        self.assertEqual([], await list_false_positive_ss(note_negated_denies()))
 
     # pylint: disable-next=line-too-long
     @unittest.skip("https://github.com/Machine-Learning-for-Medical-Language/ctakes-client-py/issues/8")
-    def test_negated_review_of_symptoms(self):
+    async def test_negated_review_of_symptoms(self):
         """
         Test hard ROS section of a medical note.
         This is not yet 100% accurate and will take consider time to be perfect.
         Negation is not a solved problem in NLP community.
         """
-        self.assertEqual([], list_false_positive_ss(note_negated_ros_review_of_symptoms()))
+        self.assertEqual([], await list_false_positive_ss(note_negated_ros_review_of_symptoms()))
 
-    def assertPolarityCompatible(self, text: str):
-        ner = ctakesclient.client.extract(text)
+    async def assertPolarityCompatible(self, text: str):
+        ner = await ctakesclient.client.extract(text)
         symptoms = ner.list_sign_symptom()
         polarities_ctakes = ner.list_polarity(symptoms)
-        polarities_cnlp = ctakesclient.transformer.list_polarity(text, ner.list_spans(symptoms))
+        polarities_cnlp = await ctakesclient.transformer.list_polarity(text, ner.list_spans(symptoms))
 
         self.assertEqual(polarities_ctakes, polarities_cnlp, text)
 
 
 if __name__ == "__main__":
     unittest.main()
```

### Comparing `ctakesclient-2.1.1/tests/resources/synthentic.txt` & `ctakesclient-3.0.0/tests/resources/synthentic.txt`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/tests/resources/synthetic.json` & `ctakesclient-3.0.0/tests/resources/synthetic.json`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/tests/resources/test_negation_hard.txt` & `ctakesclient-3.0.0/tests/resources/test_negation_hard.txt`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/tests/resources/test_physician_note.json` & `ctakesclient-3.0.0/tests/resources/test_physician_note.json`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/tests/test_client.py` & `ctakesclient-3.0.0/tests/test_client.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,36 +1,45 @@
 """Tests for the client module"""
 
 import os
 import unittest
 from unittest import mock
 
+import respx
+
 from ctakesclient import client
 from ctakesclient.typesystem import Polarity
 
 from tests.test_resources import LoadResource
 
 
-class TestClient(unittest.TestCase):
+class TestClient(unittest.IsolatedAsyncioTestCase):
     """Test case for client cTAKES extraction"""
 
     @mock.patch.dict(os.environ, {"URL_CTAKES_REST": ""})
     def test_server_url_default(self):
         self.assertEqual(client.get_url_ctakes_rest(), "http://localhost:8080/ctakes-web-rest/service/analyze")
 
     @mock.patch.dict(os.environ, {"URL_CTAKES_REST": "http://example.com:2002/blarg"})
     def test_server_url_override(self):
         self.assertEqual(client.get_url_ctakes_rest(), "http://example.com:2002/blarg")
 
-    @mock.patch("ctakesclient.client.requests.post")
-    def test_simple_extract(self, mock_post):
+    @respx.mock
+    async def test_simple_extract(self):
         """Confirm that a call to extract() gives us the expected CtakesJSON object"""
-        mock_response = mock.MagicMock()
-        mock_response.json.return_value = LoadResource.PHYSICIAN_NOTE_JSON.value
-        mock_post.return_value = mock_response
-        ner = client.extract("input text does not matter")
+        sentence = "input text sentence"
+
+        # Prepare mocked response
+        respx.post(
+            "http://localhost:8080/ctakes-web-rest/service/analyze",
+            headers={"Content-Type": "text/plain; charset=UTF-8"},
+            content=sentence,
+        ).respond(json=LoadResource.PHYSICIAN_NOTE_JSON.value)
+
+        # Make the actual call
+        ner = await client.extract(sentence)
 
         # CtakesJSON is tested more fully in test_typesystem.py.
         # We just want to make sure that we did actually load the json here.
         expected = {"Diarrhea", "cough"}
         sign_symptom_pos = [m.text for m in ner.list_sign_symptom(Polarity.pos)]
         self.assertEqual(expected, set(sign_symptom_pos))
```

### Comparing `ctakesclient-2.1.1/tests/test_filesystem.py` & `ctakesclient-3.0.0/tests/test_filesystem.py`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/tests/test_resources.py` & `ctakesclient-3.0.0/tests/test_resources.py`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/tests/test_text2fhir.py` & `ctakesclient-3.0.0/tests/test_text2fhir.py`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/tests/test_typesystem.py` & `ctakesclient-3.0.0/tests/test_typesystem.py`

 * *Files identical despite different names*

### Comparing `ctakesclient-2.1.1/PKG-INFO` & `ctakesclient-3.0.0/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,26 +1,27 @@
 Metadata-Version: 2.1
 Name: ctakesclient
-Version: 2.1.1
+Version: 3.0.0
 Summary: cTAKES client support for accessing cTAKES REST services
 Author-email: "Andy McMurry, PhD" <andrew.mcmurry@childrens.harvard.edu>, Michael Terry <michael.terry@childrens.harvard.edu>, Tim Miller <timothy.miller@childrens.harvard.edu>
-Requires-Python: >= 3.7
+Requires-Python: >= 3.8
 Description-Content-Type: text/markdown
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
 Requires-Dist: fhirclient >= 4.1
-Requires-Dist: requests
+Requires-Dist: httpx
 Requires-Dist: pre-commit ; extra == "dev"
 Requires-Dist: myst-parser ; extra == "docs"
 Requires-Dist: sphinx < 6 ; extra == "docs"
 Requires-Dist: sphinx-rtd-theme ; extra == "docs"
 Requires-Dist: ddt ; extra == "tests"
 Requires-Dist: pytest ; extra == "tests"
+Requires-Dist: respx ; extra == "tests"
 Project-URL: Homepage, https://github.com/Machine-Learning-for-Medical-Language/ctakes-client-py
 Provides-Extra: dev
 Provides-Extra: docs
 Provides-Extra: tests
 
 # Purpose: Extract Medical Concepts from Physician Notes
 This package simplifies communication with cTAKES NLP servers which produce matches with UMLS Concepts.
@@ -29,15 +30,22 @@
 - Unified Medical Language System ([UMLS](https://nlm.nih.gov/research/umls))
 
 # Quickstart
 Clinical text fragment or entire physician note.
 
 ```python
 physician_note = 'Chief Complaint: Patient c/o cough, denies fever, recent COVID test negative. Denies smoking.'
-output = ctakesclient.client.post(physician_note)
+output = await ctakesclient.client.post(physician_note)
+```
+
+Note that `ctakesclient` uses an async API.
+If your code is not async, you can simply wrap calls in `asyncio.run()`:
+
+```python
+output = asyncio.run(ctakesclient.client.post(physician_note))
 ```
 
 # Output
 
 This client parses responses into lists of MatchText and UmlsConcept.
 
 ```
```

