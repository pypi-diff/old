# Comparing `tmp/pyBibX-1.7.0.tar.gz` & `tmp/pyBibX-1.7.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\pyBibX-1.7.0.tar", last modified: Wed Mar 29 15:07:37 2023, max compression
+gzip compressed data, was "dist\pyBibX-1.7.2.tar", last modified: Fri Apr  7 14:51:42 2023, max compression
```

## Comparing `pyBibX-1.7.0.tar` & `pyBibX-1.7.2.tar`

### file list

```diff
@@ -1,40 +1,40 @@
-drwxrwxrwx   0        0        0        0 2023-03-29 15:07:37.000000 pyBibX-1.7.0/
--rw-rw-rw-   0        0        0      644 2022-03-01 19:24:07.000000 pyBibX-1.7.0/LICENSE
--rw-rw-rw-   0        0        0       40 2022-05-19 14:46:22.000000 pyBibX-1.7.0/MANIFEST.in
--rw-rw-rw-   0        0        0     8052 2023-03-29 15:07:37.000000 pyBibX-1.7.0/PKG-INFO
--rw-rw-rw-   0        0        0     7665 2023-03-29 15:05:24.000000 pyBibX-1.7.0/README.md
-drwxrwxrwx   0        0        0        0 2023-03-29 15:07:36.000000 pyBibX-1.7.0/pyBibX/
--rw-rw-rw-   0        0        0        1 2022-03-01 07:37:35.000000 pyBibX-1.7.0/pyBibX/__init__.py
-drwxrwxrwx   0        0        0        0 2023-03-29 15:07:36.000000 pyBibX-1.7.0/pyBibX/base/
--rw-rw-rw-   0        0        0       27 2022-03-16 15:26:25.000000 pyBibX-1.7.0/pyBibX/base/__init__.py
--rw-rw-rw-   0        0        0   238079 2023-03-26 16:11:34.000000 pyBibX-1.7.0/pyBibX/base/pbx.py
-drwxrwxrwx   0        0        0        0 2023-03-29 15:07:37.000000 pyBibX-1.7.0/pyBibX/base/stws/
--rw-rw-rw-   0        0        0     1287 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Arabic.txt
--rw-rw-rw-   0        0        0     1484 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Bengali.txt
--rw-rw-rw-   0        0        0     2408 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Bulgarian.txt
--rw-rw-rw-   0        0        0     1518 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Czech.txt
--rw-rw-rw-   0        0        0     4212 2017-08-01 12:33:33.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-English.txt
--rw-rw-rw-   0        0        0     6219 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Finnish.txt
--rw-rw-rw-   0        0        0     3234 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-French.txt
--rw-rw-rw-   0        0        0     4350 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-German.txt
--rw-rw-rw-   0        0        0     2065 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Hindi.txt
--rw-rw-rw-   0        0        0     5552 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Hungarian.txt
--rw-rw-rw-   0        0        0     2379 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Italian.txt
--rw-rw-rw-   0        0        0     1307 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Marathi.txt
--rw-rw-rw-   0        0        0     3274 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Persian.txt
--rw-rw-rw-   0        0        0      704 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Polish.txt
--rw-rw-rw-   0        0        0     3772 2019-05-09 13:59:54.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Portuguese-br.txt
--rw-rw-rw-   0        0        0     1926 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Romanian.txt
--rw-rw-rw-   0        0        0     4963 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Russian.txt
--rw-rw-rw-   0        0        0     2420 2017-08-01 12:33:16.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Spanish.txt
--rw-rw-rw-   0        0        0     2757 2017-07-30 20:46:06.000000 pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Swedish.txt
--rw-rw-rw-   0        0        0        1 2022-03-01 07:37:35.000000 pyBibX-1.7.0/pyBibX/base/stws/__init__.py
-drwxrwxrwx   0        0        0        0 2023-03-29 15:07:36.000000 pyBibX-1.7.0/pyBibX.egg-info/
--rw-rw-rw-   0        0        0     8052 2023-03-29 15:07:33.000000 pyBibX-1.7.0/pyBibX.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     1047 2023-03-29 15:07:34.000000 pyBibX-1.7.0/pyBibX.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-29 15:07:33.000000 pyBibX-1.7.0/pyBibX.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      198 2023-03-29 15:07:33.000000 pyBibX-1.7.0/pyBibX.egg-info/requires.txt
--rw-rw-rw-   0        0        0        7 2023-03-29 15:07:33.000000 pyBibX-1.7.0/pyBibX.egg-info/top_level.txt
--rw-rw-rw-   0        0        0        2 2023-03-29 15:07:33.000000 pyBibX-1.7.0/pyBibX.egg-info/zip-safe
--rw-rw-rw-   0        0        0       42 2023-03-29 15:07:37.000000 pyBibX-1.7.0/setup.cfg
--rw-rw-rw-   0        0        0     1016 2023-03-29 15:04:48.000000 pyBibX-1.7.0/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:51:42.000000 pyBibX-1.7.2/
+-rw-rw-rw-   0        0        0      644 2022-03-01 19:24:07.000000 pyBibX-1.7.2/LICENSE
+-rw-rw-rw-   0        0        0       40 2022-05-19 14:46:22.000000 pyBibX-1.7.2/MANIFEST.in
+-rw-rw-rw-   0        0        0     8550 2023-04-07 14:51:42.000000 pyBibX-1.7.2/PKG-INFO
+-rw-rw-rw-   0        0        0     8116 2023-04-07 14:48:33.000000 pyBibX-1.7.2/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 14:51:42.000000 pyBibX-1.7.2/pyBibX/
+-rw-rw-rw-   0        0        0        1 2022-03-01 07:37:35.000000 pyBibX-1.7.2/pyBibX/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:51:42.000000 pyBibX-1.7.2/pyBibX/base/
+-rw-rw-rw-   0        0        0       27 2022-03-16 15:26:25.000000 pyBibX-1.7.2/pyBibX/base/__init__.py
+-rw-rw-rw-   0        0        0   240751 2023-04-07 14:35:11.000000 pyBibX-1.7.2/pyBibX/base/pbx.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:51:42.000000 pyBibX-1.7.2/pyBibX/base/stws/
+-rw-rw-rw-   0        0        0     1287 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Arabic.txt
+-rw-rw-rw-   0        0        0     1484 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Bengali.txt
+-rw-rw-rw-   0        0        0     2408 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Bulgarian.txt
+-rw-rw-rw-   0        0        0     1518 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Czech.txt
+-rw-rw-rw-   0        0        0     4212 2017-08-01 12:33:33.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-English.txt
+-rw-rw-rw-   0        0        0     6219 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Finnish.txt
+-rw-rw-rw-   0        0        0     3234 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-French.txt
+-rw-rw-rw-   0        0        0     4350 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-German.txt
+-rw-rw-rw-   0        0        0     2065 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Hindi.txt
+-rw-rw-rw-   0        0        0     5552 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Hungarian.txt
+-rw-rw-rw-   0        0        0     2379 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Italian.txt
+-rw-rw-rw-   0        0        0     1307 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Marathi.txt
+-rw-rw-rw-   0        0        0     3274 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Persian.txt
+-rw-rw-rw-   0        0        0      704 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Polish.txt
+-rw-rw-rw-   0        0        0     3772 2019-05-09 13:59:54.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Portuguese-br.txt
+-rw-rw-rw-   0        0        0     1926 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Romanian.txt
+-rw-rw-rw-   0        0        0     4963 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Russian.txt
+-rw-rw-rw-   0        0        0     2420 2017-08-01 12:33:16.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Spanish.txt
+-rw-rw-rw-   0        0        0     2757 2017-07-30 20:46:06.000000 pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Swedish.txt
+-rw-rw-rw-   0        0        0        1 2022-03-01 07:37:35.000000 pyBibX-1.7.2/pyBibX/base/stws/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:51:42.000000 pyBibX-1.7.2/pyBibX.egg-info/
+-rw-rw-rw-   0        0        0     8550 2023-04-07 14:51:40.000000 pyBibX-1.7.2/pyBibX.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     1047 2023-04-07 14:51:41.000000 pyBibX-1.7.2/pyBibX.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 14:51:40.000000 pyBibX-1.7.2/pyBibX.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      204 2023-04-07 14:51:40.000000 pyBibX-1.7.2/pyBibX.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        7 2023-04-07 14:51:40.000000 pyBibX-1.7.2/pyBibX.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0        2 2023-04-07 14:51:40.000000 pyBibX-1.7.2/pyBibX.egg-info/zip-safe
+-rw-rw-rw-   0        0        0       42 2023-04-07 14:51:42.000000 pyBibX-1.7.2/setup.cfg
+-rw-rw-rw-   0        0        0     1076 2023-04-07 14:49:17.000000 pyBibX-1.7.2/setup.py
```

### Comparing `pyBibX-1.7.0/LICENSE` & `pyBibX-1.7.2/LICENSE`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/PKG-INFO` & `pyBibX-1.7.2/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 Metadata-Version: 2.1
 Name: pyBibX
-Version: 1.7.0
-Summary: A Bibliometric and Scientometric Library
+Version: 1.7.2
+Summary: A Bibliometric and Scientometric Library Powered with Artificial Intelligence Tools
 Home-page: https://github.com/Valdecy/pyBibX
 Author: Valdecy Pereira
 Author-email: valdecy.pereira@gmail.com
 License: GNU
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # pyBibX
 
 ## Introduction
 
-A Bibliometric and Scientometric python library that uses the raw files generated by **Scopus** (.bib files), **WOS (Web of Science)** (.bib files) and **PubMed** (.txt files) scientific databases. 
+A Bibliometric and Scientometric python library that uses the raw files generated by **Scopus** (.bib files), **WOS (Web of Science)** (.bib files) and **PubMed** (.txt files) scientific databases. Also Powered with Artificial Intelligence Tools to Analyze Text Data
 
 General Capabilities:
 - a) Works with **Scopus** (.bib files), **WOS** (.bib files) and **PubMed** (.txt files) databases 
 - b) Identification and Removal of duplicates
 - c) Identification of documents per type
 - d) Generates an **EDA (Exploratory Data Analysis)** Report: Publications Timespan, Total Number of Countries, Total Number of Institutions, Total Number of Sources, Total Number of References, Total Number of Languages (and also the number of docs for each language), Total Number of Documents, Average Documents per Author, Average Documents per Institution, Average Documents per Source, Average Documents per Year, Total Number of Authors, Total Number of Authors Keywords, Total Number of Authors Keywords Plus, Total Single-Authored Documents, Total Multi-Authored Documents, Average Collaboration Index, Max H-Index, Total Number of Citations, Average Citations per Author, Average Citations per Institution, Average Citations per Document, Average Citations per Source
 - e) Creates an **ID (Identification)** for each Document, Authors, Sources, Institutions, Countries, Authors' Keywords, Keywords Plus. The IDs can be used in graphs/plots to obtain a cleaner visualization
@@ -32,25 +32,26 @@
 
 Network Capabilities:
 - a) **Citation Analysis (interactive plot)** between Documents (Blue Nodes) and Citations (Red Nodes). Documents and Citations can be highlighted for better visualization
 - b) **Collaboration Analysis (interactive plot)** between Authors, Countries, Institutions or **Adjacency Analysis (interactive plot)** between Authors' Keywords or Keywords Plus. Collaboration and Adjacency can be highlighted for better visualization
 - c) **Similarity Analysis (interactive plot)** can be performed using coupling or cocitation methods
 - d) **World MAP Collaboration Analysis (interactive plot)** between Countries in a Map
 
-NLP (Natural Language Processing) Capabilities:
+Artificial Intelligence Capabilities:
 - a) **Topic Modelling** using BERTopic to cluster documents by topic
 - b) Visualize topics distribution
 - c) Visualize topics by the most representative words
 - d) Visualize documents projection and clusterization by topic
 - e) Visualize topics heatmap
 - f) Find the most representative documents from each topic
 - g) Find the most representative topics according to a word
 - h) Creates **Embeddings** from Abstracts, Titles, Authors Keywords or Keywords Plus
-- i) **Abstractive Text Summarization** using PEGASUS on a set of selected documents or all documents
-- j) **Extractive Text Summarization** using BERT on a set of selected documents or all documents
+- i) **Abstractive Text Summarization** using **PEGASUS** on a set of selected documents or all documents
+- j) **Abstractive Text Summarization** using **chatGPT** on a set of selected documents or all documents. Requires the user to have an **API key** (https://platform.openai.com/account/api-keys)
+- k) **Extractive Text Summarization** using **BERT** on a set of selected documents or all documents
 
 Correction and Manipulation Capabilities:
 - a) Filter the .bib or .txt file by Year, Sources, Bradford Law Cores, Countries, Languages and/or Abstracts (Documents with Abstracts)
 - b) Merge Authors, Institutions, Countries, Languages and/or Sources that have multiple entries 
 - c) Merge different or same database files one at a time. The preference of information preservation is given to the old database, so the order of merging matters (see Examples 04 and 05)
 
 ## Usage
@@ -61,17 +62,20 @@
 ```
 
 2. Try it in **Colab**:
 
 - Example 01: Scopus                ([ Colab Demo ](https://colab.research.google.com/drive/1yHiMMZIKa-RrarXbPB9ca0gLN9YvvtPU?usp=sharing))
 - Example 02: WOS                   ([ Colab Demo ](https://colab.research.google.com/drive/13HLjC4myTvYcjLk2XBTZKbWJ2aqZUST1?usp=sharing))
 - Example 03: PubMed                ([ Colab Demo ](https://colab.research.google.com/drive/13CU-KvZMnazga1BmQf2J8wYM9mhHL2e1?usp=sharing))
+- Example 04: Cochrane              ([ Colab Demo ]())
+- Example 05: Dimensions            ([ Colab Demo ]())
 - Example 04: Scopus + WOS          ([ Colab Demo ](https://colab.research.google.com/drive/1DqEk0_IakJPfIZDVcnTWBE_nxyhW9p-W?usp=sharing))
 - Example 05: WOS + Scopus          ([ Colab Demo ](https://colab.research.google.com/drive/12k_IOcSDwumbEtPqqSMbCIE6ZypgKAJn?usp=sharing))
 - Example 06: Scopus + WOS + Pubmed ([ Colab Demo ](https://colab.research.google.com/drive/1Ko6AibkXtB_Kwg3Eu0fhzNMVEIXPkbez?usp=sharing))
+- Example 09: Scopus + WOS + Pubmed + Cochrane  + Dimensions ([ Colab Demo ]())
 - Example 07: Your Own              ([ Colab Demo ](https://colab.research.google.com/drive/19EYjgal9V1kemmzpHnyp6MSlk9S-kGHT?usp=sharing))
 
 # Acknowledgement 
 This section indicates the libraries that inspired pyBibX
 
 * BERT (https://smrzr.io/)
 - a) Github: https://github.com/dmmiller612/bert-extractive-summarizer
```

### Comparing `pyBibX-1.7.0/README.md` & `pyBibX-1.7.2/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 # pyBibX
 
 ## Introduction
 
-A Bibliometric and Scientometric python library that uses the raw files generated by **Scopus** (.bib files), **WOS (Web of Science)** (.bib files) and **PubMed** (.txt files) scientific databases. 
+A Bibliometric and Scientometric python library that uses the raw files generated by **Scopus** (.bib files), **WOS (Web of Science)** (.bib files) and **PubMed** (.txt files) scientific databases. Also Powered with Artificial Intelligence Tools to Analyze Text Data
 
 General Capabilities:
 - a) Works with **Scopus** (.bib files), **WOS** (.bib files) and **PubMed** (.txt files) databases 
 - b) Identification and Removal of duplicates
 - c) Identification of documents per type
 - d) Generates an **EDA (Exploratory Data Analysis)** Report: Publications Timespan, Total Number of Countries, Total Number of Institutions, Total Number of Sources, Total Number of References, Total Number of Languages (and also the number of docs for each language), Total Number of Documents, Average Documents per Author, Average Documents per Institution, Average Documents per Source, Average Documents per Year, Total Number of Authors, Total Number of Authors Keywords, Total Number of Authors Keywords Plus, Total Single-Authored Documents, Total Multi-Authored Documents, Average Collaboration Index, Max H-Index, Total Number of Citations, Average Citations per Author, Average Citations per Institution, Average Citations per Document, Average Citations per Source
 - e) Creates an **ID (Identification)** for each Document, Authors, Sources, Institutions, Countries, Authors' Keywords, Keywords Plus. The IDs can be used in graphs/plots to obtain a cleaner visualization
@@ -21,25 +21,26 @@
 
 Network Capabilities:
 - a) **Citation Analysis (interactive plot)** between Documents (Blue Nodes) and Citations (Red Nodes). Documents and Citations can be highlighted for better visualization
 - b) **Collaboration Analysis (interactive plot)** between Authors, Countries, Institutions or **Adjacency Analysis (interactive plot)** between Authors' Keywords or Keywords Plus. Collaboration and Adjacency can be highlighted for better visualization
 - c) **Similarity Analysis (interactive plot)** can be performed using coupling or cocitation methods
 - d) **World MAP Collaboration Analysis (interactive plot)** between Countries in a Map
 
-NLP (Natural Language Processing) Capabilities:
+Artificial Intelligence Capabilities:
 - a) **Topic Modelling** using BERTopic to cluster documents by topic
 - b) Visualize topics distribution
 - c) Visualize topics by the most representative words
 - d) Visualize documents projection and clusterization by topic
 - e) Visualize topics heatmap
 - f) Find the most representative documents from each topic
 - g) Find the most representative topics according to a word
 - h) Creates **Embeddings** from Abstracts, Titles, Authors Keywords or Keywords Plus
-- i) **Abstractive Text Summarization** using PEGASUS on a set of selected documents or all documents
-- j) **Extractive Text Summarization** using BERT on a set of selected documents or all documents
+- i) **Abstractive Text Summarization** using **PEGASUS** on a set of selected documents or all documents
+- j) **Abstractive Text Summarization** using **chatGPT** on a set of selected documents or all documents. Requires the user to have an **API key** (https://platform.openai.com/account/api-keys)
+- k) **Extractive Text Summarization** using **BERT** on a set of selected documents or all documents
 
 Correction and Manipulation Capabilities:
 - a) Filter the .bib or .txt file by Year, Sources, Bradford Law Cores, Countries, Languages and/or Abstracts (Documents with Abstracts)
 - b) Merge Authors, Institutions, Countries, Languages and/or Sources that have multiple entries 
 - c) Merge different or same database files one at a time. The preference of information preservation is given to the old database, so the order of merging matters (see Examples 04 and 05)
 
 ## Usage
@@ -50,17 +51,20 @@
 ```
 
 2. Try it in **Colab**:
 
 - Example 01: Scopus                ([ Colab Demo ](https://colab.research.google.com/drive/1yHiMMZIKa-RrarXbPB9ca0gLN9YvvtPU?usp=sharing))
 - Example 02: WOS                   ([ Colab Demo ](https://colab.research.google.com/drive/13HLjC4myTvYcjLk2XBTZKbWJ2aqZUST1?usp=sharing))
 - Example 03: PubMed                ([ Colab Demo ](https://colab.research.google.com/drive/13CU-KvZMnazga1BmQf2J8wYM9mhHL2e1?usp=sharing))
+- Example 04: Cochrane              ([ Colab Demo ]())
+- Example 05: Dimensions            ([ Colab Demo ]())
 - Example 04: Scopus + WOS          ([ Colab Demo ](https://colab.research.google.com/drive/1DqEk0_IakJPfIZDVcnTWBE_nxyhW9p-W?usp=sharing))
 - Example 05: WOS + Scopus          ([ Colab Demo ](https://colab.research.google.com/drive/12k_IOcSDwumbEtPqqSMbCIE6ZypgKAJn?usp=sharing))
 - Example 06: Scopus + WOS + Pubmed ([ Colab Demo ](https://colab.research.google.com/drive/1Ko6AibkXtB_Kwg3Eu0fhzNMVEIXPkbez?usp=sharing))
+- Example 09: Scopus + WOS + Pubmed + Cochrane  + Dimensions ([ Colab Demo ]())
 - Example 07: Your Own              ([ Colab Demo ](https://colab.research.google.com/drive/19EYjgal9V1kemmzpHnyp6MSlk9S-kGHT?usp=sharing))
 
 # Acknowledgement 
 This section indicates the libraries that inspired pyBibX
 
 * BERT (https://smrzr.io/)
 - a) Github: https://github.com/dmmiller612/bert-extractive-summarizer
```

### Comparing `pyBibX-1.7.0/pyBibX/base/pbx.py` & `pyBibX-1.7.2/pyBibX/base/pbx.py`

 * *Files 1% similar despite different names*

```diff
@@ -8,15 +8,16 @@
 # Citation: 
 # PEREIRA, V. (2022). Project: pyBibX, File: pbibx.py, GitHub repository: <https://github.com/Valdecy/pyBibX>
 
 ############################################################################
 
 # Required Libraries
 import networkx as nx             
-import numpy as np                
+import numpy as np   
+import openai              
 import pandas as pd               
 import plotly.graph_objects as go
 import plotly.subplots as ps      
 import plotly.io as pio           
 import re                         
 import squarify                  
 import unicodedata                
@@ -600,14 +601,25 @@
                 #return min_dist(s1 + 1, s2 + 1)
             #return 1 + min(min_dist(s1, s2 + 1),      # insert character
                            #min_dist(s1 + 1, s2),      # delete character
                            #min_dist(s1 + 1, s2 + 1),  # replace character
                            #)
         #return min_dist(0, 0)
         
+    # Function: Clean DOI entries
+    def clean_doi(doi):
+        valid_chars = set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./-_:')
+        cleaned_doi = ''
+        for char in doi:
+            if char in valid_chars:
+                cleaned_doi = cleaned_doi + char
+            else:
+                break
+        return cleaned_doi
+    
     # Function: Get Duplicates Index
     def find_duplicates(self, u_list):
         duplicates = []
         indices    = []
         for i in range(0, len(u_list)):
             x = u_list[i]
             if (u_list.count(x) > 1 and x not in indices):
@@ -986,14 +998,18 @@
         labels_dict = dict(zip(labels, values))
         data        = pd.DataFrame(index = range(0, doc), columns = labels)
         count       = -1
         for i in range(0, len(rhs)):
           if (lhs[i] == 'doc_start'):
             count = count + 1
           else:
+            #if (lhs[i] == 'doi'):
+                #data.iloc[count, labels_dict[lhs[i]]] = self.clean_doi(rhs[i])
+            #else:
+                #data.iloc[count, labels_dict[lhs[i]]] = rhs[i]
             data.iloc[count, labels_dict[lhs[i]]] = rhs[i]
         entries = list(data.columns)
         
         # WoS -> Scopus
         data['document_type'] = data['document_type'].replace('Article; Early Access','Article in Press')
         data['document_type'] = data['document_type'].replace('Article; Proceedings Paper','Proceedings Paper')
         data['document_type'] = data['document_type'].replace('Article; Proceedings Paper','Proceedings Paper')
@@ -3883,14 +3899,51 @@
             tokens    = tokenizer(corpus, truncation = True, padding = 'longest', return_tensors = 'pt')
             summary   = pegasus.generate(**tokens) # max_new_tokens = 1024, max_length = 1024, 
             summary   = tokenizer.decode(summary[0])
         else:
             summary   = 'No abstracts were found in the selected set of documents'
         return summary
     
+    # Function: Abstractive Text Summarization
+    def summarize_abst_chatgpt(self, article_ids = [], join_articles = False, api_key = 'your_api_key_here', query = 'from the following scientific abstracts, summarize the main information in a single paragraph using around 250 words'):
+        def query_chatgpt(prompt, model = 'text-davinci-002', n = 1):
+            response = openai.Completion.create(
+                                                engine      = model,
+                                                prompt      = prompt,
+                                                max_tokens  = 100,
+                                                n           = n,
+                                                stop        = None,
+                                                temperature = 0.8
+                                                )
+            return response.choices[0].text.strip()
+        openai.api_key = api_key
+        abstracts      = self.data['abstract']
+        corpus         = []
+        if (len(article_ids) == 0):
+            article_ids = [i for i in range(0, abstracts.shape[0])]
+        else:
+            article_ids = [int(item) for item in article_ids]
+        for i in range(0, abstracts.shape[0]):
+            if (abstracts.iloc[i] != 'UNKNOW' and i in article_ids):
+                corpus.append('Abstract (Document ID' + str(i) + '):\n\n')
+                corpus.append(abstracts.iloc[i])
+                print('Document ID' + str(i) + ' Number of Characters: ' + str(len(abstracts.iloc[i])))
+        if (len(corpus) > 0):
+            print('')
+            print('Total Number of Valid Abstracts: ', len(corpus))
+            print('')
+            if (join_articles == False):
+                for i, abstract in enumerate(corpus):
+                    prompt = query + ':\n\n' + f'{i+1}. {corpus}\n'
+            else:    
+                corpus = ' '.join(corpus)
+                prompt = query + ':\n\n' + f'{i+1}. {corpus}\n'
+            summary = query_chatgpt(prompt)
+        return summary
+
     # Function: Extractive Text Summarization
     def summarize_ext_bert(self, article_ids = []):
         abstracts = self.data['abstract']
         corpus    = []
         if (len(article_ids) == 0):
             article_ids = [i for i in range(0, abstracts.shape[0])]
         else:
```

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Arabic.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Arabic.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Bengali.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Bengali.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Bulgarian.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Bulgarian.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Czech.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Czech.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-English.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-English.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Finnish.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Finnish.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-French.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-French.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-German.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-German.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Hindi.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Hindi.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Hungarian.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Hungarian.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Italian.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Italian.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Marathi.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Marathi.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Persian.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Persian.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Polish.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Polish.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Portuguese-br.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Portuguese-br.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Romanian.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Romanian.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Russian.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Russian.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Spanish.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Spanish.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX/base/stws/Stopwords-Swedish.txt` & `pyBibX-1.7.2/pyBibX/base/stws/Stopwords-Swedish.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/pyBibX.egg-info/PKG-INFO` & `pyBibX-1.7.2/pyBibX.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 Metadata-Version: 2.1
 Name: pyBibX
-Version: 1.7.0
-Summary: A Bibliometric and Scientometric Library
+Version: 1.7.2
+Summary: A Bibliometric and Scientometric Library Powered with Artificial Intelligence Tools
 Home-page: https://github.com/Valdecy/pyBibX
 Author: Valdecy Pereira
 Author-email: valdecy.pereira@gmail.com
 License: GNU
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # pyBibX
 
 ## Introduction
 
-A Bibliometric and Scientometric python library that uses the raw files generated by **Scopus** (.bib files), **WOS (Web of Science)** (.bib files) and **PubMed** (.txt files) scientific databases. 
+A Bibliometric and Scientometric python library that uses the raw files generated by **Scopus** (.bib files), **WOS (Web of Science)** (.bib files) and **PubMed** (.txt files) scientific databases. Also Powered with Artificial Intelligence Tools to Analyze Text Data
 
 General Capabilities:
 - a) Works with **Scopus** (.bib files), **WOS** (.bib files) and **PubMed** (.txt files) databases 
 - b) Identification and Removal of duplicates
 - c) Identification of documents per type
 - d) Generates an **EDA (Exploratory Data Analysis)** Report: Publications Timespan, Total Number of Countries, Total Number of Institutions, Total Number of Sources, Total Number of References, Total Number of Languages (and also the number of docs for each language), Total Number of Documents, Average Documents per Author, Average Documents per Institution, Average Documents per Source, Average Documents per Year, Total Number of Authors, Total Number of Authors Keywords, Total Number of Authors Keywords Plus, Total Single-Authored Documents, Total Multi-Authored Documents, Average Collaboration Index, Max H-Index, Total Number of Citations, Average Citations per Author, Average Citations per Institution, Average Citations per Document, Average Citations per Source
 - e) Creates an **ID (Identification)** for each Document, Authors, Sources, Institutions, Countries, Authors' Keywords, Keywords Plus. The IDs can be used in graphs/plots to obtain a cleaner visualization
@@ -32,25 +32,26 @@
 
 Network Capabilities:
 - a) **Citation Analysis (interactive plot)** between Documents (Blue Nodes) and Citations (Red Nodes). Documents and Citations can be highlighted for better visualization
 - b) **Collaboration Analysis (interactive plot)** between Authors, Countries, Institutions or **Adjacency Analysis (interactive plot)** between Authors' Keywords or Keywords Plus. Collaboration and Adjacency can be highlighted for better visualization
 - c) **Similarity Analysis (interactive plot)** can be performed using coupling or cocitation methods
 - d) **World MAP Collaboration Analysis (interactive plot)** between Countries in a Map
 
-NLP (Natural Language Processing) Capabilities:
+Artificial Intelligence Capabilities:
 - a) **Topic Modelling** using BERTopic to cluster documents by topic
 - b) Visualize topics distribution
 - c) Visualize topics by the most representative words
 - d) Visualize documents projection and clusterization by topic
 - e) Visualize topics heatmap
 - f) Find the most representative documents from each topic
 - g) Find the most representative topics according to a word
 - h) Creates **Embeddings** from Abstracts, Titles, Authors Keywords or Keywords Plus
-- i) **Abstractive Text Summarization** using PEGASUS on a set of selected documents or all documents
-- j) **Extractive Text Summarization** using BERT on a set of selected documents or all documents
+- i) **Abstractive Text Summarization** using **PEGASUS** on a set of selected documents or all documents
+- j) **Abstractive Text Summarization** using **chatGPT** on a set of selected documents or all documents. Requires the user to have an **API key** (https://platform.openai.com/account/api-keys)
+- k) **Extractive Text Summarization** using **BERT** on a set of selected documents or all documents
 
 Correction and Manipulation Capabilities:
 - a) Filter the .bib or .txt file by Year, Sources, Bradford Law Cores, Countries, Languages and/or Abstracts (Documents with Abstracts)
 - b) Merge Authors, Institutions, Countries, Languages and/or Sources that have multiple entries 
 - c) Merge different or same database files one at a time. The preference of information preservation is given to the old database, so the order of merging matters (see Examples 04 and 05)
 
 ## Usage
@@ -61,17 +62,20 @@
 ```
 
 2. Try it in **Colab**:
 
 - Example 01: Scopus                ([ Colab Demo ](https://colab.research.google.com/drive/1yHiMMZIKa-RrarXbPB9ca0gLN9YvvtPU?usp=sharing))
 - Example 02: WOS                   ([ Colab Demo ](https://colab.research.google.com/drive/13HLjC4myTvYcjLk2XBTZKbWJ2aqZUST1?usp=sharing))
 - Example 03: PubMed                ([ Colab Demo ](https://colab.research.google.com/drive/13CU-KvZMnazga1BmQf2J8wYM9mhHL2e1?usp=sharing))
+- Example 04: Cochrane              ([ Colab Demo ]())
+- Example 05: Dimensions            ([ Colab Demo ]())
 - Example 04: Scopus + WOS          ([ Colab Demo ](https://colab.research.google.com/drive/1DqEk0_IakJPfIZDVcnTWBE_nxyhW9p-W?usp=sharing))
 - Example 05: WOS + Scopus          ([ Colab Demo ](https://colab.research.google.com/drive/12k_IOcSDwumbEtPqqSMbCIE6ZypgKAJn?usp=sharing))
 - Example 06: Scopus + WOS + Pubmed ([ Colab Demo ](https://colab.research.google.com/drive/1Ko6AibkXtB_Kwg3Eu0fhzNMVEIXPkbez?usp=sharing))
+- Example 09: Scopus + WOS + Pubmed + Cochrane  + Dimensions ([ Colab Demo ]())
 - Example 07: Your Own              ([ Colab Demo ](https://colab.research.google.com/drive/19EYjgal9V1kemmzpHnyp6MSlk9S-kGHT?usp=sharing))
 
 # Acknowledgement 
 This section indicates the libraries that inspired pyBibX
 
 * BERT (https://smrzr.io/)
 - a) Github: https://github.com/dmmiller612/bert-extractive-summarizer
```

### Comparing `pyBibX-1.7.0/pyBibX.egg-info/SOURCES.txt` & `pyBibX-1.7.2/pyBibX.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pyBibX-1.7.0/setup.py` & `pyBibX-1.7.2/setup.py`

 * *Files 7% similar despite different names*

```diff
@@ -2,27 +2,28 @@
 from pathlib import Path
 
 this_directory = Path(__file__).parent
 long_description = (this_directory / 'README.md').read_text()
 
 setup(
     name='pyBibX',
-    version='1.7.0',
+    version='1.7.2',
     license='GNU',
     author='Valdecy Pereira',
     author_email='valdecy.pereira@gmail.com',
     url='https://github.com/Valdecy/pyBibX',
     packages=find_packages(),
     include_package_data=True,
     install_requires=[
         'bertopic',
         'bert-extractive-summarizer',
         'matplotlib',
         'networkx',
         'numpy',
+        'openai'
         'pandas',
         'plotly',
         'scipy',
         'sentencepiece',
         'sentence-transformers',
         'squarify',
         'sklearn',
@@ -30,11 +31,11 @@
         'torchvision',
         'torchaudio',
         'transformers',
         'umap-learn',
         'wordcloud'
     ],
     zip_safe=True,
-    description='A Bibliometric and Scientometric Library',
+    description='A Bibliometric and Scientometric Library Powered with Artificial Intelligence Tools',
     long_description=long_description,
     long_description_content_type='text/markdown',
 )
```

