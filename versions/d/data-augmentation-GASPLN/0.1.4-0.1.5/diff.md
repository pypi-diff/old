# Comparing `tmp/data_augmentation_GASPLN-0.1.4.tar.gz` & `tmp/data_augmentation_GASPLN-0.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "data_augmentation_GASPLN-0.1.4.tar", last modified: Thu Apr  6 12:32:35 2023, max compression
+gzip compressed data, was "data_augmentation_GASPLN-0.1.5.tar", last modified: Thu Apr  6 12:41:58 2023, max compression
```

## Comparing `data_augmentation_GASPLN-0.1.4.tar` & `data_augmentation_GASPLN-0.1.5.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 12:32:35.765363 data_augmentation_GASPLN-0.1.4/
--rw-rw-rw-   0        0        0    35823 2023-04-06 12:32:05.000000 data_augmentation_GASPLN-0.1.4/LICENSE
--rw-rw-rw-   0        0        0       24 2023-04-06 12:32:05.000000 data_augmentation_GASPLN-0.1.4/MANIFEST.in
--rw-rw-rw-   0        0        0      217 2023-04-06 12:32:35.766363 data_augmentation_GASPLN-0.1.4/PKG-INFO
--rw-rw-rw-   0        0        0     1977 2023-04-06 12:32:05.000000 data_augmentation_GASPLN-0.1.4/README.md
-drwxrwxrwx   0        0        0        0 2023-04-06 12:32:35.720235 data_augmentation_GASPLN-0.1.4/data_augmentation_GASPLN/
--rw-rw-rw-   0        0        0        0 2023-04-06 12:32:05.000000 data_augmentation_GASPLN-0.1.4/data_augmentation_GASPLN/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-06 12:32:35.758365 data_augmentation_GASPLN-0.1.4/data_augmentation_GASPLN/data/
--rw-rw-rw-   0        0        0  7024004 2023-04-06 12:32:05.000000 data_augmentation_GASPLN-0.1.4/data_augmentation_GASPLN/data/synonyms_pt_BR.parquet
--rw-rw-rw-   0        0        0     2565 2023-04-06 12:32:05.000000 data_augmentation_GASPLN-0.1.4/data_augmentation_GASPLN/data_augmentation.py
-drwxrwxrwx   0        0        0        0 2023-04-06 12:32:35.757364 data_augmentation_GASPLN-0.1.4/data_augmentation_GASPLN.egg-info/
--rw-rw-rw-   0        0        0      217 2023-04-06 12:32:35.000000 data_augmentation_GASPLN-0.1.4/data_augmentation_GASPLN.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      423 2023-04-06 12:32:35.000000 data_augmentation_GASPLN-0.1.4/data_augmentation_GASPLN.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 12:32:35.000000 data_augmentation_GASPLN-0.1.4/data_augmentation_GASPLN.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       38 2023-04-06 12:32:35.000000 data_augmentation_GASPLN-0.1.4/data_augmentation_GASPLN.egg-info/requires.txt
--rw-rw-rw-   0        0        0       25 2023-04-06 12:32:35.000000 data_augmentation_GASPLN-0.1.4/data_augmentation_GASPLN.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       86 2023-04-06 12:32:35.767363 data_augmentation_GASPLN-0.1.4/setup.cfg
--rw-rw-rw-   0        0        0      512 2023-04-06 12:32:05.000000 data_augmentation_GASPLN-0.1.4/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 12:41:58.470900 data_augmentation_GASPLN-0.1.5/
+-rw-rw-rw-   0        0        0    35823 2023-04-06 12:32:05.000000 data_augmentation_GASPLN-0.1.5/LICENSE
+-rw-rw-rw-   0        0        0       24 2023-04-06 12:32:05.000000 data_augmentation_GASPLN-0.1.5/MANIFEST.in
+-rw-rw-rw-   0        0        0      217 2023-04-06 12:41:58.470900 data_augmentation_GASPLN-0.1.5/PKG-INFO
+-rw-rw-rw-   0        0        0     2135 2023-04-06 12:38:34.000000 data_augmentation_GASPLN-0.1.5/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 12:41:58.457901 data_augmentation_GASPLN-0.1.5/data_augmentation_GASPLN/
+-rw-rw-rw-   0        0        0        0 2023-04-06 12:32:05.000000 data_augmentation_GASPLN-0.1.5/data_augmentation_GASPLN/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 12:41:58.463901 data_augmentation_GASPLN-0.1.5/data_augmentation_GASPLN/data/
+-rw-rw-rw-   0        0        0  7024004 2023-04-06 12:32:05.000000 data_augmentation_GASPLN-0.1.5/data_augmentation_GASPLN/data/synonyms_pt_BR.parquet
+-rw-rw-rw-   0        0        0     2606 2023-04-06 12:41:21.000000 data_augmentation_GASPLN-0.1.5/data_augmentation_GASPLN/data_augmentation.py
+drwxrwxrwx   0        0        0        0 2023-04-06 12:41:58.462900 data_augmentation_GASPLN-0.1.5/data_augmentation_GASPLN.egg-info/
+-rw-rw-rw-   0        0        0      217 2023-04-06 12:41:58.000000 data_augmentation_GASPLN-0.1.5/data_augmentation_GASPLN.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      423 2023-04-06 12:41:58.000000 data_augmentation_GASPLN-0.1.5/data_augmentation_GASPLN.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 12:41:58.000000 data_augmentation_GASPLN-0.1.5/data_augmentation_GASPLN.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       55 2023-04-06 12:41:58.000000 data_augmentation_GASPLN-0.1.5/data_augmentation_GASPLN.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       25 2023-04-06 12:41:58.000000 data_augmentation_GASPLN-0.1.5/data_augmentation_GASPLN.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       86 2023-04-06 12:41:58.471900 data_augmentation_GASPLN-0.1.5/setup.cfg
+-rw-rw-rw-   0        0        0      553 2023-04-06 12:41:14.000000 data_augmentation_GASPLN-0.1.5/setup.py
```

### Comparing `data_augmentation_GASPLN-0.1.4/LICENSE` & `data_augmentation_GASPLN-0.1.5/LICENSE`

 * *Files identical despite different names*

### Comparing `data_augmentation_GASPLN-0.1.4/README.md` & `data_augmentation_GASPLN-0.1.5/README.md`

 * *Files 8% similar despite different names*

```diff
@@ -6,14 +6,20 @@
 
 The package is available on PyPI and can be easily installed using pip:
 
 ```bash
 pip install data_augmentation_GASPLN
 ```
 
+You also need to download the Portuguese model for spaCy. To do this, run the following command:
+
+```bash
+python -m spacy download pt_core_news_sm
+```
+
 ## Usage
 
 ***PLEASE NOTE THAT THIS PROJECT IS STILL UNDER CONSTRUCTION AND NOT YET READY FOR USE***
 
 That being said, the library currently has some test functions that can be used, as shown below.
 
 To use the library, simply import it as follows:
```

### Comparing `data_augmentation_GASPLN-0.1.4/data_augmentation_GASPLN/data/synonyms_pt_BR.parquet` & `data_augmentation_GASPLN-0.1.5/data_augmentation_GASPLN/data/synonyms_pt_BR.parquet`

 * *Files identical despite different names*

### Comparing `data_augmentation_GASPLN-0.1.4/data_augmentation_GASPLN/data_augmentation.py` & `data_augmentation_GASPLN-0.1.5/data_augmentation_GASPLN/data_augmentation.py`

 * *Files 3% similar despite different names*

```diff
@@ -33,14 +33,15 @@
     nltk.download('averaged_perceptron_tagger')
     
 # load the synonyms_pt_BR.parquet file to a dataframe using pkg_resources to avoid hardcoding the path
 synonyms_df = pd.read_parquet(pkg_resources.resource_filename('data_augmentation_GASPLN', 'data/synonyms_pt_BR.parquet'))
 
 def synonyms_replacement(text, percentage=0.5):
     tokens = nltk.word_tokenize(text)
+    nlp = spacy.load('pt_core_news_sm')
     
     number_of_words = int(len(tokens) * percentage)
     indexes = np.random.choice(len(tokens), number_of_words, replace=False)
     
     for index in indexes:
         word = tokens[index]
```

### Comparing `data_augmentation_GASPLN-0.1.4/setup.py` & `data_augmentation_GASPLN-0.1.5/setup.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,19 +1,21 @@
 from setuptools import setup, find_packages
 
 setup(
     name='data_augmentation_GASPLN',
-    version='0.1.4',
+    version='0.1.5',
     author='Artur Melchiori Cerri',
     author_email='arturmelchiori@gmail.com',
     description='Data augmentation for Portuguese language',
     install_requires=[
+        "spacy",
         "nltk",
         "pandas",
         "pyarrow",
         "numpy",
         "translators",
+        "setuptools",
     ],
     packages=find_packages(),
     include_package_data=True,
     package_data={'' : ['data/synonyms_pt_BR.parquet']},
 )
```

