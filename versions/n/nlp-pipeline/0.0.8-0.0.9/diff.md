# Comparing `tmp/nlp_pipeline-0.0.8.tar.gz` & `tmp/nlp_pipeline-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/nlp_pipeline-0.0.8.tar", last modified: Wed Feb 22 13:24:46 2023, max compression
+gzip compressed data, was "dist/nlp_pipeline-0.0.9.tar", last modified: Wed Feb 22 14:29:10 2023, max compression
```

## Comparing `nlp_pipeline-0.0.8.tar` & `nlp_pipeline-0.0.9.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 danhopp    (501) staff       (20)        0 2023-02-22 13:24:46.264258 nlp_pipeline-0.0.8/
--rw-r--r--   0 danhopp    (501) staff       (20)     6368 2023-02-22 13:24:46.262734 nlp_pipeline-0.0.8/PKG-INFO
--rw-r--r--   0 danhopp    (501) staff       (20)     5043 2023-02-22 13:21:01.000000 nlp_pipeline-0.0.8/README.md
-drwxr-xr-x   0 danhopp    (501) staff       (20)        0 2023-02-22 13:24:46.253535 nlp_pipeline-0.0.8/nlp_pipeline/
--rw-r--r--   0 danhopp    (501) staff       (20)        0 2023-02-20 16:24:15.000000 nlp_pipeline-0.0.8/nlp_pipeline/__init__.py
--rw-r--r--   0 danhopp    (501) staff       (20)    12568 2023-02-20 16:31:20.000000 nlp_pipeline-0.0.8/nlp_pipeline/files_setup.py
--rw-r--r--   0 danhopp    (501) staff       (20)    24222 2023-02-22 13:10:27.000000 nlp_pipeline-0.0.8/nlp_pipeline/nlp_pipeline.py
--rw-r--r--   0 danhopp    (501) staff       (20)     4908 2023-02-22 13:03:36.000000 nlp_pipeline-0.0.8/nlp_pipeline/text_transformation.py
--rw-r--r--   0 danhopp    (501) staff       (20)     5570 2023-02-20 16:24:15.000000 nlp_pipeline-0.0.8/nlp_pipeline/visualizations.py
-drwxr-xr-x   0 danhopp    (501) staff       (20)        0 2023-02-22 13:24:46.259456 nlp_pipeline-0.0.8/nlp_pipeline.egg-info/
--rw-r--r--   0 danhopp    (501) staff       (20)     6368 2023-02-22 13:24:45.000000 nlp_pipeline-0.0.8/nlp_pipeline.egg-info/PKG-INFO
--rw-r--r--   0 danhopp    (501) staff       (20)      356 2023-02-22 13:24:45.000000 nlp_pipeline-0.0.8/nlp_pipeline.egg-info/SOURCES.txt
--rw-r--r--   0 danhopp    (501) staff       (20)        1 2023-02-22 13:24:45.000000 nlp_pipeline-0.0.8/nlp_pipeline.egg-info/dependency_links.txt
--rw-r--r--   0 danhopp    (501) staff       (20)       19 2023-02-22 13:24:45.000000 nlp_pipeline-0.0.8/nlp_pipeline.egg-info/top_level.txt
--rw-r--r--   0 danhopp    (501) staff       (20)       38 2023-02-22 13:24:46.264617 nlp_pipeline-0.0.8/setup.cfg
--rw-r--r--   0 danhopp    (501) staff       (20)      692 2023-02-22 13:23:02.000000 nlp_pipeline-0.0.8/setup.py
-drwxr-xr-x   0 danhopp    (501) staff       (20)        0 2023-02-22 13:24:46.261210 nlp_pipeline-0.0.8/tests/
--rw-r--r--   0 danhopp    (501) staff       (20)        0 2023-02-20 16:24:15.000000 nlp_pipeline-0.0.8/tests/__init__.py
--rw-r--r--   0 danhopp    (501) staff       (20)      229 2023-02-20 16:24:15.000000 nlp_pipeline-0.0.8/tests/test_nlp_pipeline.py
+drwxr-xr-x   0 danhopp    (501) staff       (20)        0 2023-02-22 14:29:10.408483 nlp_pipeline-0.0.9/
+-rw-r--r--   0 danhopp    (501) staff       (20)     6368 2023-02-22 14:29:10.407642 nlp_pipeline-0.0.9/PKG-INFO
+-rw-r--r--   0 danhopp    (501) staff       (20)     5043 2023-02-22 13:21:01.000000 nlp_pipeline-0.0.9/README.md
+drwxr-xr-x   0 danhopp    (501) staff       (20)        0 2023-02-22 14:29:10.400213 nlp_pipeline-0.0.9/nlp_pipeline/
+-rw-r--r--   0 danhopp    (501) staff       (20)        0 2023-02-20 16:24:15.000000 nlp_pipeline-0.0.9/nlp_pipeline/__init__.py
+-rw-r--r--   0 danhopp    (501) staff       (20)    12629 2023-02-22 14:16:05.000000 nlp_pipeline-0.0.9/nlp_pipeline/files_setup.py
+-rw-r--r--   0 danhopp    (501) staff       (20)    24355 2023-02-22 14:24:49.000000 nlp_pipeline-0.0.9/nlp_pipeline/nlp_pipeline.py
+-rw-r--r--   0 danhopp    (501) staff       (20)     4908 2023-02-22 13:03:36.000000 nlp_pipeline-0.0.9/nlp_pipeline/text_transformation.py
+-rw-r--r--   0 danhopp    (501) staff       (20)     5570 2023-02-20 16:24:15.000000 nlp_pipeline-0.0.9/nlp_pipeline/visualizations.py
+drwxr-xr-x   0 danhopp    (501) staff       (20)        0 2023-02-22 14:29:10.404227 nlp_pipeline-0.0.9/nlp_pipeline.egg-info/
+-rw-r--r--   0 danhopp    (501) staff       (20)     6368 2023-02-22 14:29:09.000000 nlp_pipeline-0.0.9/nlp_pipeline.egg-info/PKG-INFO
+-rw-r--r--   0 danhopp    (501) staff       (20)      356 2023-02-22 14:29:10.000000 nlp_pipeline-0.0.9/nlp_pipeline.egg-info/SOURCES.txt
+-rw-r--r--   0 danhopp    (501) staff       (20)        1 2023-02-22 14:29:09.000000 nlp_pipeline-0.0.9/nlp_pipeline.egg-info/dependency_links.txt
+-rw-r--r--   0 danhopp    (501) staff       (20)       19 2023-02-22 14:29:09.000000 nlp_pipeline-0.0.9/nlp_pipeline.egg-info/top_level.txt
+-rw-r--r--   0 danhopp    (501) staff       (20)       38 2023-02-22 14:29:10.408844 nlp_pipeline-0.0.9/setup.cfg
+-rw-r--r--   0 danhopp    (501) staff       (20)      692 2023-02-22 14:25:58.000000 nlp_pipeline-0.0.9/setup.py
+drwxr-xr-x   0 danhopp    (501) staff       (20)        0 2023-02-22 14:29:10.405929 nlp_pipeline-0.0.9/tests/
+-rw-r--r--   0 danhopp    (501) staff       (20)        0 2023-02-20 16:24:15.000000 nlp_pipeline-0.0.9/tests/__init__.py
+-rw-r--r--   0 danhopp    (501) staff       (20)      229 2023-02-20 16:24:15.000000 nlp_pipeline-0.0.9/tests/test_nlp_pipeline.py
```

### Comparing `nlp_pipeline-0.0.8/PKG-INFO` & `nlp_pipeline-0.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nlp_pipeline
-Version: 0.0.8
+Version: 0.0.9
 Summary: Pipelines and management structure for NLP analysis of a corpus of texts
 Home-page: https://github.com/dhopp1/nlp_pipeline
 Author: Daniel Hopp
 Author-email: daniel.hopp1@gmail.com
 License: UNKNOWN
 Description: # nlp_pipeline
         Collection of NLP tools for processing and analyzing text data.
```

### Comparing `nlp_pipeline-0.0.8/README.md` & `nlp_pipeline-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `nlp_pipeline-0.0.8/nlp_pipeline/files_setup.py` & `nlp_pipeline-0.0.9/nlp_pipeline/files_setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -197,15 +197,15 @@
     
     if raw_exists:
         # first check if this file already converted
         if not(os.path.isfile(f"{data_path}txt_files/{text_id}.txt")):
             # pdf file
             if ".pdf" in raw_path:
                 return_text = parse_pdf(raw_path)
-                if (len(set(return_text.split("[newpage] "))) == 1) | ((return_text.lower().count("/g") / len(return_text)) > 0.01) | (return_text.lower().count("sqj") > 10): # if only empties, scan, needs to be OCR converted. If bunch of "/G"s, greater than 1% of all the characters, encoding error, like review of maritime transport 2006. Or if poorly digitized and a lot of 'sqj's. Force OCR.
+                if (len(set(return_text.split("[newpage] "))) == 1) | ((return_text.lower().count("/g") / len(return_text)) > 0.01) | (return_text.lower().count("_") / len(return_text) > 0.05) | (return_text.lower().count("sqj") > 10): # if only empties, scan, needs to be OCR converted. If bunch of "/G"s, greater than 1% of all the characters, encoding error, like review of maritime transport 2006. Or if poorly digitized and a lot of 'sqj's. Force OCR.
                     return_text = parse_ocr_pdf(data_path, raw_path, windows_tesseract_path, windows_poppler_path)
                     # remove temporary image files from OCR
                     for f in glob.glob(f"{data_path}*.jpg"):
                         os.remove(f)
             elif ".html" in raw_path:
                 return_text = parse_html(raw_path)
```

### Comparing `nlp_pipeline-0.0.8/nlp_pipeline/nlp_pipeline.py` & `nlp_pipeline-0.0.9/nlp_pipeline/nlp_pipeline.py`

 * *Files 0% similar despite different names*

```diff
@@ -293,15 +293,18 @@
                 file.close()
                 
                 # calculating sentiments
                 sentiments = [self.text_transformation.get_single_sentiment(x, sentiment_analyzer)["compound"] for x in stringx.split("|") if (len(x) > 3) & (len(x.split(" ")) > 2) & (not(x.isnumeric()))] # only do sentiment for sentences with more than 2 words and not numeric
                 
                 # adding and writing to CSV
                 csv.loc[csv.text_id == text_id, "avg_sentiment_w_neutral"] = sum(sentiments) / len(sentiments)
-                csv.loc[csv.text_id == text_id, "avg_sentiment_wo_neutral"] = sum([x for x in sentiments if x != 0.0]) / len([x for x in sentiments if x != 0.0])
+                try:
+                    csv.loc[csv.text_id == text_id, "avg_sentiment_wo_neutral"] = sum([x for x in sentiments if x != 0.0]) / len([x for x in sentiments if x != 0.0])
+                except:
+                    csv.loc[csv.text_id == text_id, "avg_sentiment_wo_neutral"] = 0
                 csv.loc[csv.text_id == text_id, "neutral_proportion"] = len([x for x in sentiments if x == 0.0]) / len(sentiments)
                 csv.to_csv(csv_path, index = False)
                 
                 
     def plot_word_occurrences(self, text_ids_list, word, path_prefix, x_labels = None, title = ""):
         """get plot of occurrences of a particular word over groups of documents. Searches for contains rather than exact matches.
         parameters:
```

### Comparing `nlp_pipeline-0.0.8/nlp_pipeline/text_transformation.py` & `nlp_pipeline-0.0.9/nlp_pipeline/text_transformation.py`

 * *Files identical despite different names*

### Comparing `nlp_pipeline-0.0.8/nlp_pipeline/visualizations.py` & `nlp_pipeline-0.0.9/nlp_pipeline/visualizations.py`

 * *Files identical despite different names*

### Comparing `nlp_pipeline-0.0.8/nlp_pipeline.egg-info/PKG-INFO` & `nlp_pipeline-0.0.9/nlp_pipeline.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nlp-pipeline
-Version: 0.0.8
+Version: 0.0.9
 Summary: Pipelines and management structure for NLP analysis of a corpus of texts
 Home-page: https://github.com/dhopp1/nlp_pipeline
 Author: Daniel Hopp
 Author-email: daniel.hopp1@gmail.com
 License: UNKNOWN
 Description: # nlp_pipeline
         Collection of NLP tools for processing and analyzing text data.
```

### Comparing `nlp_pipeline-0.0.8/setup.py` & `nlp_pipeline-0.0.9/setup.py`

 * *Ordering differences only*

 * *Files 1% similar despite different names*

```diff
@@ -1 +1 @@
-import setuptoolswith open("README.md", "r") as fh:    long_description = fh.read()setuptools.setup(    name="nlp_pipeline",    version="0.0.8",    author="Daniel Hopp",    author_email="daniel.hopp1@gmail.com",    description="Pipelines and management structure for NLP analysis of a corpus of texts",    long_description=long_description,    long_description_content_type="text/markdown",    url="https://github.com/dhopp1/nlp_pipeline",    packages=setuptools.find_packages(),    classifiers=[        "Programming Language :: Python :: 3",        "License :: OSI Approved :: MIT License",        "Operating System :: OS Independent",    ],    python_requires=">=3.6",)
+import setuptoolswith open("README.md", "r") as fh:    long_description = fh.read()setuptools.setup(    name="nlp_pipeline",    version="0.0.9",    author="Daniel Hopp",    author_email="daniel.hopp1@gmail.com",    description="Pipelines and management structure for NLP analysis of a corpus of texts",    long_description=long_description,    long_description_content_type="text/markdown",    url="https://github.com/dhopp1/nlp_pipeline",    packages=setuptools.find_packages(),    classifiers=[        "Programming Language :: Python :: 3",        "License :: OSI Approved :: MIT License",        "Operating System :: OS Independent",    ],    python_requires=">=3.6",)
```

