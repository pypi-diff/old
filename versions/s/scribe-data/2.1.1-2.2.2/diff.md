# Comparing `tmp/scribe_data-2.1.1-py3-none-any.whl.zip` & `tmp/scribe_data-2.2.2-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,13 +1,13 @@
-Zip file size: 102885 bytes, number of entries: 69
+Zip file size: 103197 bytes, number of entries: 69
 -rw-r--r--  2.0 unx        0 b- defN 22-Apr-06 08:21 scribe_data/__init__.py
 -rw-r--r--  2.0 unx        0 b- defN 22-Apr-05 19:22 scribe_data/extract_transform/__init__.py
--rw-r--r--  2.0 unx    13955 b- defN 22-Oct-01 21:44 scribe_data/extract_transform/extract_wiki.py
--rw-r--r--  2.0 unx     6024 b- defN 23-Mar-04 15:35 scribe_data/extract_transform/process_unicode.py
--rw-r--r--  2.0 unx    12782 b- defN 22-Nov-06 08:44 scribe_data/extract_transform/process_wiki.py
+-rw-r--r--  2.0 unx    13956 b- defN 23-Apr-07 10:11 scribe_data/extract_transform/extract_wiki.py
+-rw-r--r--  2.0 unx     6461 b- defN 23-Apr-07 11:06 scribe_data/extract_transform/process_unicode.py
+-rw-r--r--  2.0 unx    12783 b- defN 23-Apr-07 10:12 scribe_data/extract_transform/process_wiki.py
 -rw-r--r--  2.0 unx        0 b- defN 22-Apr-05 19:24 scribe_data/extract_transform/French/__init__.py
 -rw-r--r--  2.0 unx        0 b- defN 22-Apr-05 19:41 scribe_data/extract_transform/French/nouns/__init__.py
 -rw-r--r--  2.0 unx     6162 b- defN 22-Oct-16 21:13 scribe_data/extract_transform/French/nouns/format_nouns.py
 -rw-r--r--  2.0 unx        0 b- defN 22-Apr-05 19:43 scribe_data/extract_transform/French/translations/__init__.py
 -rw-r--r--  2.0 unx     1297 b- defN 22-Oct-16 21:12 scribe_data/extract_transform/French/translations/format_translations.py
 -rw-r--r--  2.0 unx        0 b- defN 22-Apr-05 19:43 scribe_data/extract_transform/French/verbs/__init__.py
 -rw-r--r--  2.0 unx     3968 b- defN 22-Nov-04 22:50 scribe_data/extract_transform/French/verbs/format_verbs.py
@@ -58,14 +58,14 @@
 -rw-r--r--  2.0 unx        0 b- defN 22-Apr-05 19:44 scribe_data/extract_transform/Swedish/verbs/__init__.py
 -rw-r--r--  2.0 unx     3970 b- defN 22-Oct-16 21:14 scribe_data/extract_transform/Swedish/verbs/format_verbs.py
 -rw-r--r--  2.0 unx   102823 b- defN 22-Nov-23 22:13 scribe_data/extract_transform/_resources/2021_ranked.tsv
 -rw-r--r--  2.0 unx        0 b- defN 22-Nov-23 22:13 scribe_data/extract_transform/_resources/__init__.py
 -rw-r--r--  2.0 unx        0 b- defN 22-Apr-06 08:23 scribe_data/load/__init__.py
 -rw-r--r--  2.0 unx    12972 b- defN 22-Nov-04 23:06 scribe_data/load/update_data.py
 -rw-r--r--  2.0 unx     6353 b- defN 22-Nov-21 16:40 scribe_data/load/update_utils.py
--rw-r--r--  2.0 unx      389 b- defN 22-Nov-23 22:45 scribe_data-2.1.1.data/data/requirements.txt
--rw-r--r--  2.0 unx    32472 b- defN 23-Mar-04 19:21 scribe_data-2.1.1.dist-info/LICENSE.txt
--rw-r--r--  2.0 unx    12814 b- defN 23-Mar-04 19:21 scribe_data-2.1.1.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 23-Mar-04 19:21 scribe_data-2.1.1.dist-info/WHEEL
--rw-r--r--  2.0 unx       12 b- defN 23-Mar-04 19:21 scribe_data-2.1.1.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     7566 b- defN 23-Mar-04 19:21 scribe_data-2.1.1.dist-info/RECORD
-69 files, 309109 bytes uncompressed, 90045 bytes compressed:  70.9%
+-rw-r--r--  2.0 unx      389 b- defN 22-Nov-23 22:45 scribe_data-2.2.2.data/data/requirements.txt
+-rw-r--r--  2.0 unx    32472 b- defN 23-Apr-07 11:21 scribe_data-2.2.2.dist-info/LICENSE.txt
+-rw-r--r--  2.0 unx    13440 b- defN 23-Apr-07 11:21 scribe_data-2.2.2.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 23-Apr-07 11:21 scribe_data-2.2.2.dist-info/WHEEL
+-rw-r--r--  2.0 unx       12 b- defN 23-Apr-07 11:21 scribe_data-2.2.2.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     7566 b- defN 23-Apr-07 11:21 scribe_data-2.2.2.dist-info/RECORD
+69 files, 310174 bytes uncompressed, 90357 bytes compressed:  70.9%
```

## zipnote {}

```diff
@@ -183,26 +183,26 @@
 
 Filename: scribe_data/load/update_data.py
 Comment: 
 
 Filename: scribe_data/load/update_utils.py
 Comment: 
 
-Filename: scribe_data-2.1.1.data/data/requirements.txt
+Filename: scribe_data-2.2.2.data/data/requirements.txt
 Comment: 
 
-Filename: scribe_data-2.1.1.dist-info/LICENSE.txt
+Filename: scribe_data-2.2.2.dist-info/LICENSE.txt
 Comment: 
 
-Filename: scribe_data-2.1.1.dist-info/METADATA
+Filename: scribe_data-2.2.2.dist-info/METADATA
 Comment: 
 
-Filename: scribe_data-2.1.1.dist-info/WHEEL
+Filename: scribe_data-2.2.2.dist-info/WHEEL
 Comment: 
 
-Filename: scribe_data-2.1.1.dist-info/top_level.txt
+Filename: scribe_data-2.2.2.dist-info/top_level.txt
 Comment: 
 
-Filename: scribe_data-2.1.1.dist-info/RECORD
+Filename: scribe_data-2.2.2.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## scribe_data/extract_transform/extract_wiki.py

```diff
@@ -28,17 +28,18 @@
 from multiprocessing.dummy import Pool as Threadpool
 
 import defusedxml.sax
 import mwparserfromhell
 import requests
 import tensorflow as tf
 from bs4 import BeautifulSoup
-from scribe_data.load.update_utils import get_language_iso
 from tqdm.auto import tqdm
 
+from scribe_data.load.update_utils import get_language_iso
+
 
 def download_wiki(language="en", target_dir="wiki_dump", file_limit=None, dump_id=None):
     """
     Downloads the most recent stable dump of a language's Wikipedia if it is not already present.
 
     Parameters
     ----------
```

## scribe_data/extract_transform/process_unicode.py

```diff
@@ -1,15 +1,15 @@
 """
 Process Unicode
 ------------
 
-Module for processing Unicode based corpuses for autosuggestion generation.
+Module for processing Unicode based corpuses for autosuggestion and autocompletion generation.
 
 Contents:
-    gen_emoji_autosuggestions
+    gen_emoji_keywords
 """
 
 import csv
 import json
 from importlib.resources import files
 
 import emoji
@@ -21,61 +21,67 @@
     get_path_from_process_unicode,
     get_path_from_update_data,
 )
 
 from . import _resources
 
 
-def gen_emoji_autosuggestions(
+def gen_emoji_keywords(
     language="English",
     num_emojis=None,
-    num_per_keyword=None,
+    emojis_per_keyword=None,
     ignore_keywords=None,
+    export_base_rank=False,
     update_scribe_apps=False,
     verbose=True,
 ):
     """
     Generates a dictionary of keywords (keys) and emoji unicode(s) associated with them (values).
 
     Parameters
     ----------
         language : string (default=en)
-            The language autosuggestions are being generated for.
+            The language keywords are being generated for.
 
         num_emojis : int (default=None)
-            The limit for number of emojis that autosuggestions should be generated from.
+            The limit for number of emojis that keywords should be generated from.
 
-        num_per_keyword : int (default=None)
-            The limit for number of emoji autosuggestions that should be generated per keyword.
+        emojis_per_keyword : int (default=None)
+            The limit for number of emoji keywords that should be generated per keyword.
 
         ignore_keywords : str or list (default=None)
             Keywords that should be ignored.
 
+        export_base_rank : bool (default=False)
+            Whether to export whether the emojis is a base character as well as its rank.
+
         update_scribe_apps : bool (default=False)
             Saves the created dictionaries as JSONs in Scribe app directories.
 
         verbose : bool (default=True)
             Whether to show a tqdm progress bar for the process.
 
     Returns
     -------
-        Autosuggestions dictionaries for emoji keywords-to-unicode are saved locally or uploaded to Scribe apps.
+        Keywords dictionary for emoji keywords-to-unicode are saved locally or uploaded to Scribe apps.
     """
 
-    autosuggest_dict = {}
+    keyword_dict = {}
 
     iso = get_language_iso(language)
 
     if isinstance(ignore_keywords, str):
         keywords_to_ignore = [ignore_keywords]
     elif isinstance(ignore_keywords, list):
         keywords_to_ignore = ignore_keywords
     else:
         keywords_to_ignore = []
 
+    keywords_to_ignore = [k.lower() for k in keywords_to_ignore]
+
     # Pre-set up the emoji popularity data.
     popularity_dict = {}
 
     with files(_resources).joinpath("2021_ranked.tsv").open() as popularity_file:
         tsv_reader = csv.DictReader(popularity_file, delimiter="\t")
         for tsv_row in tsv_reader:
             popularity_dict[tsv_row["Emoji"]] = int(tsv_row["Rank"])
@@ -92,28 +98,25 @@
     for cldr_file_key, cldr_file_path in cldr_file_paths.items():
         with open(cldr_file_path, "r") as file:
             cldr_data = json.load(file)
 
         cldr_dict = cldr_data[cldr_file_key]["annotations"]
 
         for cldr_char in tqdm(
-            iterable=cldr_dict, 
-            desc=f"Characters processed from '{cldr_file_key}' CLDR file for {language}", 
-            unit="cldr characters", 
+            iterable=cldr_dict,
+            desc=f"Characters processed from '{cldr_file_key}' CLDR file for {language}",
+            unit="cldr characters",
             disable=not verbose,
         ):
             # Filter CLDR data for emoji characters.
             if cldr_char in emoji.EMOJI_DATA:
                 emoji_rank = popularity_dict.get(cldr_char)
 
                 # If number limit specified, filter for the highest-ranked emojis.
-                if num_emojis and (
-                    emoji_rank is None
-                    or emoji_rank > num_emojis
-                ):
+                if num_emojis and (emoji_rank is None or emoji_rank > num_emojis):
                     continue
 
                 # Process for emoji variants.
                 has_modifier_base = Char.hasBinaryProperty(
                     cldr_char, UProperty.EMOJI_MODIFIER_BASE
                 )
                 if has_modifier_base and len(cldr_char) > 1:
@@ -124,48 +127,56 @@
                 if (
                     emoji.EMOJI_DATA[cldr_char]["status"]
                     == emoji.STATUS["fully_qualified"]
                 ):
                     emoji_annotations = cldr_dict[cldr_char]
 
                     for emoji_keyword in emoji_annotations["default"]:
+                        emoji_keyword = emoji_keyword.lower()  # lower case the key
                         if (
                             # Use single-word annotations as keywords.
                             len(emoji_keyword.split()) == 1
                             and emoji_keyword not in keywords_to_ignore
                         ):
-                            autosuggest_dict.setdefault(emoji_keyword, []).append(
+                            keyword_dict.setdefault(emoji_keyword, []).append(
                                 {
                                     "emoji": cldr_char,
                                     "is_base": has_modifier_base,
                                     "rank": emoji_rank,
                                 }
                             )
 
     # Sort by rank after all emojis already found per keyword.
-    for suggestions in autosuggest_dict.values():
-        suggestions.sort(
-            key=lambda suggestion: float('inf') if suggestion["rank"] is None else suggestion["rank"]
+    for keywords in keyword_dict.values():
+        keywords.sort(
+            key=lambda suggestion: float("inf")
+            if suggestion["rank"] is None
+            else suggestion["rank"]
         )
 
         # If specified, enforce limit of emojis per keyword.
-        if num_per_keyword and len(suggestions) > num_per_keyword:
-            suggestions[:] = suggestions[:num_per_keyword]
+        if emojis_per_keyword and len(keywords) > emojis_per_keyword:
+            keywords[:] = keywords[:emojis_per_keyword]
 
     if verbose:
         print(
-            f"Number of emoji trigger keywords found for {language}: {len(autosuggest_dict)}"
+            f"Number of emoji trigger keywords found for {language}: {len(keyword_dict)}"
         )
 
+    # Remove base status and rank if not needed.
+    if not export_base_rank:
+        keyword_dict = {
+            k: [{"emoji": emoji_options["emoji"]} for emoji_options in v]
+            for k, v in keyword_dict.items()
+        }
+
     if update_scribe_apps:
-        output_path = f"{get_path_from_update_data()}/Scribe-iOS/Keyboards/LanguageKeyboards/{language.capitalize()}/Data/emoji_suggestions.json"
+        output_path = f"{get_path_from_update_data()}/Scribe-iOS/Keyboards/LanguageKeyboards/{language.capitalize()}/Data/emoji_keywords.json"
     else:
-        output_path = f"{language.lower()}_emoji_suggestions.json"
+        output_path = f"{language.lower()}_emoji_keywords.json"
 
     with open(output_path, "w", encoding="utf-8") as file:
-        json.dump(autosuggest_dict, file, ensure_ascii=False, indent=0)
+        json.dump(keyword_dict, file, ensure_ascii=False, indent=0)
 
-    print(
-        f"Emoji autosuggestions for {language} generated and saved to '{output_path}'."
-    )
+    print(f"Emoji keywords for {language} generated and saved to '{output_path}'.")
 
-    return autosuggest_dict
+    return keyword_dict
```

## scribe_data/extract_transform/process_wiki.py

```diff
@@ -14,24 +14,25 @@
 import warnings
 from collections import Counter
 from itertools import chain
 from urllib.error import HTTPError
 
 import numpy as np
 import regex
+from SPARQLWrapper import JSON, POST, SPARQLWrapper
+from tqdm.auto import tqdm
+
 from scribe_data.load.update_utils import (  # get_android_data_path, get_desktop_data_path,
     add_num_commas,
     get_ios_data_path,
     get_language_qid,
     get_language_words_to_ignore,
     get_language_words_to_remove,
     get_path_from_process_wiki,
 )
-from SPARQLWrapper import JSON, POST, SPARQLWrapper
-from tqdm.auto import tqdm
 
 warnings.filterwarnings("ignore", message=r"Passing", category=FutureWarning)
 
 # Set SPARQLWrapper query conditions.
 sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
 sparql.setReturnFormat(JSON)
 sparql.setMethod(POST)
```

## Comparing `scribe_data-2.1.1.dist-info/LICENSE.txt` & `scribe_data-2.2.2.dist-info/LICENSE.txt`

 * *Files identical despite different names*

## Comparing `scribe_data-2.1.1.dist-info/METADATA` & `scribe_data-2.2.2.dist-info/METADATA`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: scribe-data
-Version: 2.1.1
+Version: 2.2.2
 Summary: Wikidata and Wikipedia data extraction for Scribe applications
 Home-page: https://github.com/scribe-org/Scribe-Data
 Author: Andrew Tavis McAllister
 Author-email: andrew.t.mcallister@gmail.com
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: Intended Audience :: Education
@@ -32,26 +32,27 @@
 Requires-Dist: SPARQLWrapper (>=2.0.0)
 Requires-Dist: tabulate (>=0.8.9)
 Requires-Dist: tensorflow (>=2.5.1)
 Requires-Dist: tqdm (==4.56.1)
 Requires-Dist: transformers (>=4.12)
 
 <div align="center">
-  <a href="https://github.com/scribe-org/Scribe-Data"><img src="https://raw.githubusercontent.com/scribe-org/Organization/main/logo/ScribeGitHubOrgBanner.png" width=1024 alt="Scribe Logo"></a>
+  <a href="https://github.com/scribe-org/Scribe-Data"><img src="https://raw.githubusercontent.com/scribe-org/Scribe-Data/main/.github/resources/images/ScribeDataLogo.png" height=150 alt="Scribe Logo"></a>
 </div>
 
 [![platforms](https://img.shields.io/badge/Wikidata-990000.svg?logo=wikidata&logoColor=ffffff)](https://github.com/scribe-org/Scribe-Data)
 [![issues](https://img.shields.io/github/issues/scribe-org/Scribe-Data?label=%20&logo=github)](https://github.com/scribe-org/Scribe-Data/issues)
 [![language](https://img.shields.io/badge/Python%203-306998.svg?logo=python&logoColor=ffffff)](https://github.com/scribe-org/Scribe-Data/blob/main/CONTRIBUTING.md)
 [![pypi](https://img.shields.io/pypi/v/scribe-data.svg?label=%20&color=4B8BBE)](https://pypi.org/project/scribe-data/)
 [![pypistatus](https://img.shields.io/pypi/status/scribe-data.svg?label=%20)](https://pypi.org/project/scribe-data/)
 [![license](https://img.shields.io/github/license/scribe-org/Scribe-Data.svg?label=%20)](https://github.com/scribe-org/Scribe-Data/blob/main/LICENSE.txt)
 [![coc](https://img.shields.io/badge/Contributor%20Covenant-ff69b4.svg)](https://github.com/scribe-org/Scribe-Data/blob/main/.github/CODE_OF_CONDUCT.md)
 [![twitter](https://img.shields.io/badge/Twitter-1DA1F2.svg?logo=twitter&logoColor=ffffff)](https://twitter.com/scribe_org)
 [![codestyle](https://img.shields.io/badge/black-000000.svg)](https://github.com/psf/black)
+[![matrix](https://img.shields.io/badge/Matrix-000000.svg?logo=matrix&logoColor=ffffff)](https://matrix.to/#/#scribe_community:matrix.org)
 
 ## Wikidata and Wikipedia data extraction for Scribe applications
 
 This repository contains the scripts for extracting and formatting data from [Wikidata](https://www.wikidata.org/) and [Wikipedia](https://www.wikipedia.org/) for Scribe applications. Updates to the language keyboard and interface data can be done using [scribe_data/load/update_data.py](https://github.com/scribe-org/Scribe-Data/tree/main/src/scribe_data/load/update_data.py).
 
 <a id="contents"></a>
 
@@ -70,15 +71,19 @@
 
 The ultimate goal is that this repository will house language packs that are periodically updated with new [Wikidata](https://www.wikidata.org/) lexicographical data, with these packs then being available to download by users of Scribe applications.
 
 <a id="contributing"></a>
 
 # Contributing [`⇧`](#contents)
 
-Work that is in progress or could be implemented is tracked in the [issues](https://github.com/scribe-org/Scribe-Data/issues) and [projects](https://github.com/scribe-org/Scribe-Data/projects). Please see the [contribution guidelines](https://github.com/scribe-org/Scribe-Data/blob/main/CONTRIBUTING.md) if you are interested in contributing to Scribe-Data. Also check the [`-priority-`](https://github.com/scribe-org/Scribe-Data/labels/-priority-) labels in the [issues](https://github.com/scribe-org/Scribe-Data/issues) for those that are most important, as well as those marked [`good first issue`](https://github.com/scribe-org/Scribe-Data/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) that are tailored for first time contributors.
+<a href="https://matrix.to/#/#scribe_community:matrix.org"><img src="https://raw.githubusercontent.com/scribe-org/Organization/main/resources/images/logos/MatrixLogoGrey.png" height="50" alt="Public Matrix Chat" align="right"></a>
+
+Scribe uses [Matrix](https://matrix.org/) for communications. You're more than welcome to [join us in our public chat rooms](https://matrix.to/#/#scribe_community:matrix.org) to share ideas, ask questions or just say hi :)
+
+Please see the [contribution guidelines](https://github.com/scribe-org/Scribe-Data/blob/main/CONTRIBUTING.md) if you are interested in contributing to Scribe-Data. Work that is in progress or could be implemented is tracked in the [issues](https://github.com/scribe-org/Scribe-Data/issues) and [projects](https://github.com/scribe-org/Scribe-Data/projects). Also check the [`-priority-`](https://github.com/scribe-org/Scribe-Data/labels/-priority-) labels in the [issues](https://github.com/scribe-org/Scribe-Data/issues) for those that are most important, as well as those marked [`good first issue`](https://github.com/scribe-org/Scribe-Data/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) that are tailored for first time contributors.
 
 After your first few pull requests organization members would be happy to discuss granting you further rights as a contributor, with a maintainer role then being possible after continued interest in the project. Scribe seeks to be an inclusive and supportive organization. We'd love to have you on the team!
 
 ### Ways to Help [`⇧`](#contents)
 
 - [Reporting bugs](https://github.com/scribe-org/Scribe-Data/issues/new?assignees=&labels=bug&template=bug_report.yml) as they're found 🐞
 - Working on [new features](https://github.com/scribe-org/Scribe-Data/issues?q=is%3Aissue+is%3Aopen+label%3Afeature) ✨
@@ -134,17 +139,17 @@
 - [Presentation slides](https://docs.google.com/presentation/d/16ld_rCbwJCiAdRrfhF-Fq9Wm_ciHCbk_HCzGQs6TB1Q/edit?usp=sharing) for [Wikidata Data Reuse Days 2022](https://diff.wikimedia.org/event/wikidata-data-reuse-days-2022/)
 
 </p>
 </details>
 
 <div align="center">
   <br>
-    <a href="https://tech-news.wikimedia.de/en/2022/03/18/lexicographical-data-for-language-learners-the-wikidata-based-app-scribe/"><img height="120"src="https://raw.githubusercontent.com/scribe-org/Organization/main/resources/images/wikimedia_deutschland_logo.png" alt="Wikimedia Deutschland Logo"></a>
+    <a href="https://tech-news.wikimedia.de/en/2022/03/18/lexicographical-data-for-language-learners-the-wikidata-based-app-scribe/"><img height="120"src="https://raw.githubusercontent.com/scribe-org/Organization/main/resources/images/logos/WikimediaDeutschlandLogo.png" alt="Wikimedia Deutschland Logo"></a>
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-    <a href="https://www.mediawiki.org/wiki/New_Developers"><img height="120" src="https://raw.githubusercontent.com/scribe-org/Organization/main/resources/images/mediawiki_logo.png" alt="MediaWiki logo"></a>
+    <a href="https://www.mediawiki.org/wiki/New_Developers"><img height="120" src="https://raw.githubusercontent.com/scribe-org/Organization/main/resources/images/logos/MediawikiLogo.png" alt="MediaWiki logo"></a>
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
   <br>
 </div>
 
 # Powered By
 
 ### Contributors
@@ -167,13 +172,13 @@
 </p>
 </details>
 
 ### Wikimedia Communities
 
 <div align="center">
   <br>
-  <a href="https://www.wikidata.org/"><img height="175" src="https://raw.githubusercontent.com/scribe-org/Organization/main/resources/images/wikidata_logo.png" alt="Wikidata logo"></a>
+  <a href="https://www.wikidata.org/"><img height="175" src="https://raw.githubusercontent.com/scribe-org/Organization/main/resources/images/logos/WikidataLogo.png" alt="Wikidata logo"></a>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-  <a href="https://www.wikipedia.org/"><img height="190" src="https://raw.githubusercontent.com/scribe-org/Organization/main/resources/images/wikipedia_logo.png" alt="Wikipedia logo"></a>
+  <a href="https://www.wikipedia.org/"><img height="190" src="https://raw.githubusercontent.com/scribe-org/Organization/main/resources/images/logos/WikipediaLogo.png" alt="Wikipedia logo"></a>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
   <br>
 </div>
```

### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: scribe-data Version: 2.1.1 Summary: Wikidata and
+Metadata-Version: 2.1 Name: scribe-data Version: 2.2.2 Summary: Wikidata and
 Wikipedia data extraction for Scribe applications Home-page: https://
 github.com/scribe-org/Scribe-Data Author: Andrew Tavis McAllister Author-email:
 andrew.t.mcallister@gmail.com Classifier: Development Status :: 5 - Production/
 Stable Classifier: Intended Audience :: Developers Classifier: Intended
 Audience :: Education Classifier: License :: OSI Approved :: GNU General Public
 License v3 (GPLv3) Classifier: Programming Language :: Python Classifier:
 Programming Language :: Python :: 3 Classifier: Programming Language :: Python
@@ -30,15 +30,17 @@
 (https://pypi.org/project/scribe-data/) [![license](https://img.shields.io/
 github/license/scribe-org/Scribe-Data.svg?label=%20)](https://github.com/
 scribe-org/Scribe-Data/blob/main/LICENSE.txt) [![coc](https://img.shields.io/
 badge/Contributor%20Covenant-ff69b4.svg)](https://github.com/scribe-org/Scribe-
 Data/blob/main/.github/CODE_OF_CONDUCT.md) [![twitter](https://img.shields.io/
 badge/Twitter-1DA1F2.svg?logo=twitter&logoColor=ffffff)](https://twitter.com/
 scribe_org) [![codestyle](https://img.shields.io/badge/black-000000.svg)]
-(https://github.com/psf/black) ## Wikidata and Wikipedia data extraction for
+(https://github.com/psf/black) [![matrix](https://img.shields.io/badge/Matrix-
+000000.svg?logo=matrix&logoColor=ffffff)](https://matrix.to/#/
+#scribe_community:matrix.org) ## Wikidata and Wikipedia data extraction for
 Scribe applications This repository contains the scripts for extracting and
 formatting data from [Wikidata](https://www.wikidata.org/) and [Wikipedia]
 (https://www.wikipedia.org/) for Scribe applications. Updates to the language
 keyboard and interface data can be done using [scribe_data/load/update_data.py]
 (https://github.com/scribe-org/Scribe-Data/tree/main/src/scribe_data/load/
 update_data.py).  # **Contents** - [Process](#process) - [Contributing]
 (#contributing) - [Supported Languages](#supported-languages) - [Featured By]
@@ -53,32 +55,36 @@
 effective baseline feature until natural language processing techniques are
 employed. Functions to generate autosuggestions are ran in [scribe_data/load/
 gen_autosuggestions.ipynb](https://github.com/scribe-org/Scribe-Data/blob/main/
 src/scribe_data/load/gen_autosuggestions.ipynb). The ultimate goal is that this
 repository will house language packs that are periodically updated with new
 [Wikidata](https://www.wikidata.org/) lexicographical data, with these packs
 then being available to download by users of Scribe applications.  #
-Contributing [`â§`](#contents) Work that is in progress or could be
-implemented is tracked in the [issues](https://github.com/scribe-org/Scribe-
-Data/issues) and [projects](https://github.com/scribe-org/Scribe-Data/
-projects). Please see the [contribution guidelines](https://github.com/scribe-
-org/Scribe-Data/blob/main/CONTRIBUTING.md) if you are interested in
-contributing to Scribe-Data. Also check the [`-priority-`](https://github.com/
-scribe-org/Scribe-Data/labels/-priority-) labels in the [issues](https://
-github.com/scribe-org/Scribe-Data/issues) for those that are most important, as
-well as those marked [`good first issue`](https://github.com/scribe-org/Scribe-
-Data/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) that are
-tailored for first time contributors. After your first few pull requests
-organization members would be happy to discuss granting you further rights as a
-contributor, with a maintainer role then being possible after continued
-interest in the project. Scribe seeks to be an inclusive and supportive
-organization. We'd love to have you on the team! ### Ways to Help [`â§`]
-(#contents) - [Reporting bugs](https://github.com/scribe-org/Scribe-Data/
-issues/new?assignees=&labels=bug&template=bug_report.yml) as they're found ð
-- Working on [new features](https://github.com/scribe-org/Scribe-Data/
+Contributing [`â§`](#contents) [Public_Matrix_Chat] Scribe uses [Matrix]
+(https://matrix.org/) for communications. You're more than welcome to [join us
+in our public chat rooms](https://matrix.to/#/#scribe_community:matrix.org) to
+share ideas, ask questions or just say hi :) Please see the [contribution
+guidelines](https://github.com/scribe-org/Scribe-Data/blob/main/
+CONTRIBUTING.md) if you are interested in contributing to Scribe-Data. Work
+that is in progress or could be implemented is tracked in the [issues](https://
+github.com/scribe-org/Scribe-Data/issues) and [projects](https://github.com/
+scribe-org/Scribe-Data/projects). Also check the [`-priority-`](https://
+github.com/scribe-org/Scribe-Data/labels/-priority-) labels in the [issues]
+(https://github.com/scribe-org/Scribe-Data/issues) for those that are most
+important, as well as those marked [`good first issue`](https://github.com/
+scribe-org/Scribe-Data/
+issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) that are tailored
+for first time contributors. After your first few pull requests organization
+members would be happy to discuss granting you further rights as a contributor,
+with a maintainer role then being possible after continued interest in the
+project. Scribe seeks to be an inclusive and supportive organization. We'd love
+to have you on the team! ### Ways to Help [`â§`](#contents) - [Reporting bugs]
+(https://github.com/scribe-org/Scribe-Data/issues/
+new?assignees=&labels=bug&template=bug_report.yml) as they're found ð -
+Working on [new features](https://github.com/scribe-org/Scribe-Data/
 issues?q=is%3Aissue+is%3Aopen+label%3Afeature) â¨ - [Documentation](https://
 github.com/scribe-org/Scribe-Data/
 issues?q=is%3Aissue+is%3Aopen+label%3Adocumentation) for onboarding and project
 cohesion ð - Adding language data to [Scribe-Data](https://github.com/
 scribe-org/Scribe-Data/issues) via [Wikidata](https://www.wikidata.org/)!
 ðï¸ ### Road Map [`â§`](#contents) The Scribe road map can be followed in
 the organization's [project board](https://github.com/orgs/scribe-org/projects/
```

## Comparing `scribe_data-2.1.1.dist-info/RECORD` & `scribe_data-2.2.2.dist-info/RECORD`

 * *Files 6% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 scribe_data/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 scribe_data/extract_transform/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
-scribe_data/extract_transform/extract_wiki.py,sha256=WoZy0yUk6CLVywfajcdtsJ7tSCcogXUOMX040w29GR0,13955
-scribe_data/extract_transform/process_unicode.py,sha256=J8_Bbsc5AvVjWmXQr8VU7zee5pXbo7St6OyyAs9UW4g,6024
-scribe_data/extract_transform/process_wiki.py,sha256=IeUQge4aE3g5AZTw5Eb8_1XZGMs4a9-EALlwdiW0Ag0,12782
+scribe_data/extract_transform/extract_wiki.py,sha256=YlUAy_P2AbeVIAD1n1oiL282HdmYwEkuoXvDKjqDJ8w,13956
+scribe_data/extract_transform/process_unicode.py,sha256=Cp32tkLV0yf_8x57jmyrC4ExvnwOQDD-hGgvlv4Ub9Y,6461
+scribe_data/extract_transform/process_wiki.py,sha256=b5R24sRoAVIOalTIHC_c6vk_42lAQcxKmaxTp65_mn0,12783
 scribe_data/extract_transform/French/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 scribe_data/extract_transform/French/nouns/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 scribe_data/extract_transform/French/nouns/format_nouns.py,sha256=OOeZ6GP--vp58GFvZQFdoKDY6Gpj6yYn5FHrTeekZOg,6162
 scribe_data/extract_transform/French/translations/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 scribe_data/extract_transform/French/translations/format_translations.py,sha256=1DUUd1ltSAgdim843aXzMrYTPQY4YsaQw6Qh4RPWDMg,1297
 scribe_data/extract_transform/French/verbs/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 scribe_data/extract_transform/French/verbs/format_verbs.py,sha256=ZfsPKHosPnv4iwrcSO_yTlbc8zmGtMfUaCJhw4hMeuI,3968
@@ -57,13 +57,13 @@
 scribe_data/extract_transform/Swedish/verbs/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 scribe_data/extract_transform/Swedish/verbs/format_verbs.py,sha256=OvnLKUjYfSmV5Y3ZxtEcRf3V1lKwAeMB4pODZ8JtDVs,3970
 scribe_data/extract_transform/_resources/2021_ranked.tsv,sha256=1XXrIZetJHgCBkjmfbCLhuIbO8f4FPqBRLnQ2hH74Bc,102823
 scribe_data/extract_transform/_resources/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 scribe_data/load/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 scribe_data/load/update_data.py,sha256=ouQ9WOk9sYL1kFJfQDkGos0-8jz_5th2TgYB57mtmOA,12972
 scribe_data/load/update_utils.py,sha256=WXHuMsfkFVK9cMjzfCttpOhFC118UWoZkbKTjx89hlY,6353
-scribe_data-2.1.1.data/data/requirements.txt,sha256=C13PXdDAYDT5VJjil2cnMkz4r6dMVXmI5usEZ_Khejk,389
-scribe_data-2.1.1.dist-info/LICENSE.txt,sha256=xh8S2nza1Sa9y-1HpMCmA-YNu_2vi2aTPNCI6RMsMD8,32472
-scribe_data-2.1.1.dist-info/METADATA,sha256=L1ceIGCsXpxjjM5Stw8o6Xh5McpqD4IkyZnhUeGVmQo,12814
-scribe_data-2.1.1.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
-scribe_data-2.1.1.dist-info/top_level.txt,sha256=GZ2cJsBl_mJRjLt4ZRE21TpBtIqZMjB46rmPaxur-wo,12
-scribe_data-2.1.1.dist-info/RECORD,,
+scribe_data-2.2.2.data/data/requirements.txt,sha256=C13PXdDAYDT5VJjil2cnMkz4r6dMVXmI5usEZ_Khejk,389
+scribe_data-2.2.2.dist-info/LICENSE.txt,sha256=xh8S2nza1Sa9y-1HpMCmA-YNu_2vi2aTPNCI6RMsMD8,32472
+scribe_data-2.2.2.dist-info/METADATA,sha256=B2QlEsaHBJhiPhXPHhg8iinRoSbW6sl-49BHmFo5xMc,13440
+scribe_data-2.2.2.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
+scribe_data-2.2.2.dist-info/top_level.txt,sha256=GZ2cJsBl_mJRjLt4ZRE21TpBtIqZMjB46rmPaxur-wo,12
+scribe_data-2.2.2.dist-info/RECORD,,
```

