# Comparing `tmp/proteomicruler-0.1.2.tar.gz` & `tmp/proteomicruler-0.1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "proteomicruler-0.1.2.tar", max compression
+gzip compressed data, was "proteomicruler-0.1.4.tar", max compression
```

## Comparing `proteomicruler-0.1.2.tar` & `proteomicruler-0.1.4.tar`

### file list

```diff
@@ -1,10 +1,12 @@
--rw-r--r--   0        0        0        0 2022-08-03 13:09:18.248837 proteomicruler-0.1.2/proteomicRuler/__init__.py
--rw-r--r--   0        0        0       57 2023-03-10 15:37:30.166484 proteomicruler-0.1.2/proteomicRuler/constant.py
--rw-r--r--   0        0        0     1084 2023-03-10 15:36:19.895708 proteomicruler-0.1.2/proteomicRuler/histones.py
--rw-r--r--   0        0        0     3458 2022-08-03 13:09:18.248837 proteomicruler-0.1.2/proteomicRuler/organisms.json
--rw-r--r--   0        0        0    12866 2023-03-22 17:43:22.238625 proteomicruler-0.1.2/proteomicRuler/ruler.py
--rw-r--r--   0        0        0     1496 2023-03-22 17:49:38.008195 proteomicruler-0.1.2/proteomicRuler/test_ruler.py
--rw-r--r--   0        0        0      893 2023-03-22 17:49:07.464857 proteomicruler-0.1.2/pyproject.toml
--rw-r--r--   0        0        0     2200 2023-03-22 17:43:22.221614 proteomicruler-0.1.2/README.md
--rw-r--r--   0        0        0     3264 1970-01-01 00:00:00.000000 proteomicruler-0.1.2/setup.py
--rw-r--r--   0        0        0     3277 1970-01-01 00:00:00.000000 proteomicruler-0.1.2/PKG-INFO
+-rw-r--r--   0        0        0        0 2022-08-03 13:09:18.248837 proteomicruler-0.1.4/proteomicRuler/__init__.py
+-rw-r--r--   0        0        0     1842 2023-04-06 13:54:55.280874 proteomicruler-0.1.4/proteomicRuler/cli.py
+-rw-r--r--   0        0        0       57 2023-03-10 15:37:30.166484 proteomicruler-0.1.4/proteomicRuler/constant.py
+-rw-r--r--   0        0        0     1084 2023-03-10 15:36:19.895708 proteomicruler-0.1.4/proteomicRuler/histones.py
+-rw-r--r--   0        0        0     3458 2022-08-03 13:09:18.248837 proteomicruler-0.1.4/proteomicRuler/organisms.json
+-rw-r--r--   0        0        0    13017 2023-04-06 13:49:59.774291 proteomicruler-0.1.4/proteomicRuler/ruler.py
+-rw-r--r--   0        0        0      558 2023-04-06 13:56:39.544957 proteomicruler-0.1.4/proteomicRuler/test_cli.py
+-rw-r--r--   0        0        0     1377 2023-03-23 10:46:01.839270 proteomicruler-0.1.4/proteomicRuler/test_ruler.py
+-rw-r--r--   0        0        0      990 2023-04-06 13:57:08.228238 proteomicruler-0.1.4/pyproject.toml
+-rw-r--r--   0        0        0     2958 2023-04-06 13:56:39.539946 proteomicruler-0.1.4/README.md
+-rw-r--r--   0        0        0     4221 1970-01-01 00:00:00.000000 proteomicruler-0.1.4/setup.py
+-rw-r--r--   0        0        0     4056 1970-01-01 00:00:00.000000 proteomicruler-0.1.4/PKG-INFO
```

### Comparing `proteomicruler-0.1.2/proteomicRuler/histones.py` & `proteomicruler-0.1.4/proteomicRuler/histones.py`

 * *Files identical despite different names*

### Comparing `proteomicruler-0.1.2/proteomicRuler/organisms.json` & `proteomicruler-0.1.4/proteomicRuler/organisms.json`

 * *Files identical despite different names*

### Comparing `proteomicruler-0.1.2/proteomicRuler/ruler.py` & `proteomicruler-0.1.4/proteomicRuler/ruler.py`

 * *Files 2% similar despite different names*

```diff
@@ -213,14 +213,18 @@
     # add molecular weight column to a copy of the dataframe and return the copy
     df1 = df.copy()
     # iterate over all rows in the dataframe
     for i, r in df1.iterrows():
         seq = UniprotSequence(r[accession_id_col], True)
         if seq.accession:
             df1.at[i, "Accession"] = seq.accession
+        else:
+            print("No accession found for protein " + r[accession_id_col])
+            df1.at[i, "Accession"] = r[accession_id_col]
+
     accessions = df1["Accession"].unique()
     # create a UniprotParser object to parse the data from Uniprot
     parser = UniprotParser()
     data = []
     # iterate over all parsed data and store them in a list of dataframes
     for i in parser.parse(accessions):
         frame = pd.read_csv(StringIO(i), sep="\t")
```

### Comparing `proteomicruler-0.1.2/proteomicRuler/test_ruler.py` & `proteomicruler-0.1.4/proteomicRuler/test_ruler.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from unittest import TestCase
 
 import pandas as pd
 
-from proteomicRuler.ruler import Ruler
+from proteomicRuler.ruler import Ruler, add_mw
 
 
 class TestRuler(TestCase):
     def __init__(self, methodName: str = ...) -> None:
         super().__init__(methodName)
         self.da = pd.read_csv(
             r"\\mrc-smb.lifesci.dundee.ac.uk\mrc-group-folder\ALESSI\Toan\For copy number test\combined\txt\proteinGroups.txt",
@@ -19,18 +19,15 @@
         # ruler.load_genes()
         # ruler.df.to_csv("test.csv")
         # ruler.plot()
 
 
 class Test(TestCase):
     def test_add_mw(self):
-        from proteomicRuler.ruler import Ruler, add_mw
-        import pandas as pd
         df = pd.read_csv(r"report.pg_matrix.tsv", sep="\t")
-        accession_id_col = "Protein IDs"
         # used as unique index and to directly fetch mw data from UniProt
         mw_col = "Mass"
         # molecular weight column name
         ploidy = 2
         # ploidy number
         total_cellular_protein_concentration = 200
         intensity_columns = df.columns[5:]
```

### Comparing `proteomicruler-0.1.2/pyproject.toml` & `proteomicruler-0.1.4/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -1,24 +1,29 @@
 [tool.poetry]
 name = "proteomicruler"
-version = "0.1.2"
+version = "0.1.4"
 description = "Estimate copy number from deep profile MS experiment using the Proteomic Ruler algorithm from Wiśniewski, J. R., Hein, M. Y., Cox, J. and Mann, M. (2014) A “Proteomic Ruler” for Protein Copy Number and Concentration Estimation without Spike-in Standards. Mol Cell Proteomics 13, 3497–3506."
 authors = ["Toan K. Phung <toan.phungkhoiquoctoan@gmail.com>"]
 readme = "README.md"
 license = "MIT"
 keywords = ["proteomic", "ruler", "histone", "mass spectrometry"]
 repository = "https://github.com/noatgnu/proteomicRuler"
 
 [tool.poetry.dependencies]
 python = ">=3.9,<3.12"
 pandas = "^1.4.3"
 requests = "^2.28.1"
 scipy = "^1.9.0"
 seaborn = "^0.11.2"
 uniprotparser = "^1.0.7"
+click = "^8.1.3"
 
 [tool.poetry.dev-dependencies]
+pytest = "^7.2.2"
+
+[tool.poetry.scripts]
+ruler = "proteomicRuler.cli:main"
 
 [build-system]
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
```

### Comparing `proteomicruler-0.1.2/README.md` & `proteomicruler-0.1.4/README.md`

 * *Files 10% similar despite different names*

```diff
@@ -56,15 +56,33 @@
 from proteomicRuler.ruler import add_mw
 
 df = add_mw(df, accession_id_col)
 df = df[pd.notnull(df[mw_col])]
 df[mw_col] = df[mw_col].astype(float)
 ```
 
-The RuleR object can be created by passing the `DataFrame` object and the required parameters.
+The Ruler object can be created by passing the `DataFrame` object and the required parameters.
 
 ```python
 from proteomicRuler.ruler import Ruler
 
 ruler = Ruler(df, intensity_columns, mw_col, accession_id_col, ploidy, total_cellular_protein_concentration) #
 ruler.df.to_csv("output.txt", sep="\t", index=False)
 ```
+
+It is also possible to use the package through the command line interface.
+
+```bash
+Usage: ruler [OPTIONS]
+
+Options:
+  -i, --input FILENAME          Input file containing intensity of samples and
+                                uniprot accession ids
+  -o, --output FILENAME         Output file
+  -p, --ploidy INTEGER          Ploidy of the organism
+  -t, --total-cellular FLOAT    Total cellular protein concentration
+  -m, --mw-column TEXT          Molecular weight column name
+  -a, --accession-id-col TEXT   Accession id column name
+  -c, --intensity-columns TEXT  Intensity columns list delimited by commas
+  -g, --get-mw                  Get molecular weight from uniprot
+  --help                        Show this message and exit.
+```
```

### Comparing `proteomicruler-0.1.2/setup.py` & `proteomicruler-0.1.4/setup.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,34 +1,39 @@
 # -*- coding: utf-8 -*-
 from setuptools import setup
 
 packages = \
 ['proteomicruler']
 
 package_data = \
-{'': ['*']}
+{'': ['*'], 'proteomicruler': ['.pytest_cache/*', '.pytest_cache/v/cache/*']}
 
 install_requires = \
-['pandas>=1.4.3,<2.0.0',
+['click>=8.1.3,<9.0.0',
+ 'pandas>=1.4.3,<2.0.0',
  'requests>=2.28.1,<3.0.0',
  'scipy>=1.9.0,<2.0.0',
  'seaborn>=0.11.2,<0.12.0',
  'uniprotparser>=1.0.7,<2.0.0']
 
+entry_points = \
+{'console_scripts': ['ruler = proteomicRuler.cli:main']}
+
 setup_kwargs = {
     'name': 'proteomicruler',
-    'version': '0.1.2',
+    'version': '0.1.4',
     'description': 'Estimate copy number from deep profile MS experiment using the Proteomic Ruler algorithm from Wiśniewski, J. R., Hein, M. Y., Cox, J. and Mann, M. (2014) A “Proteomic Ruler” for Protein Copy Number and Concentration Estimation without Spike-in Standards. Mol Cell Proteomics 13, 3497–3506.',
-    'long_description': 'Proteomic Ruler\n--\n\nAn implementation of the same algorithm from Perseus `Wiśniewski, J. R., Hein, M. Y., Cox, J. and Mann, M. (2014) A “Proteomic Ruler” for Protein Copy Number and Concentration Estimation without Spike-in Standards. Mol Cell Proteomics 13, 3497–3506.` used for estimation of protein copy number from deep profile experiment.\n\nRequirements\n--\n\nPython >= 3.9\n\nInstallation\n--\n```bash\npip install proteomicruler\n```\n\nUsage\n--\n\nIn order to use the package, it is required that the input data is loaded into a `pandas.DataFrame` object. The following\nbasic parameters are also required:\n- `accession_id_col` - column name that contains protein accession ids\n- `mw_col` - column name that contains molecular weight of proteins\n- `ploidy` - ploidy number\n- `total_cellular_protein_concentration` - total cellular protein concentration used for calculation of total volume\n- `intensity_columns` - list of column names that contain sample intensities\n\n```python\nimport pandas as pd\n\naccession_id_col = "Protein IDs"\n# used as unique index and to directly fetch mw data from UniProt\n\nmw_col = "Mass"\n# molecular weight column name\n\nploidy = 2\n# ploidy number\n\ntotal_cellular_protein_concentration = 200\n# cellular protein concentration used for calculation of total volume\n\nfilename = r"example_data\\example_data.tsv" # example data from Perseus\ndf = pd.read_csv(filename, sep="\\t")\n\n# selecting intensity columns\nintensity_columns = df.columns[57:57+16] # select 16 columns starting from column 57th that contain sample intensity\n\n\n\n```\n\nIf the data does not contain molecular weight information, it is required to fetch it from UniProt.\n\n```python\nfrom proteomicRuler.ruler import add_mw\n\ndf = add_mw(df, accession_id_col)\ndf = df[pd.notnull(df[mw_col])]\ndf[mw_col] = df[mw_col].astype(float)\n```\n\nThe RuleR object can be created by passing the `DataFrame` object and the required parameters.\n\n```python\nfrom proteomicRuler.ruler import Ruler\n\nruler = Ruler(df, intensity_columns, mw_col, accession_id_col, ploidy, total_cellular_protein_concentration) #\nruler.df.to_csv("output.txt", sep="\\t", index=False)\n```\n',
+    'long_description': 'Proteomic Ruler\n--\n\nAn implementation of the same algorithm from Perseus `Wiśniewski, J. R., Hein, M. Y., Cox, J. and Mann, M. (2014) A “Proteomic Ruler” for Protein Copy Number and Concentration Estimation without Spike-in Standards. Mol Cell Proteomics 13, 3497–3506.` used for estimation of protein copy number from deep profile experiment.\n\nRequirements\n--\n\nPython >= 3.9\n\nInstallation\n--\n```bash\npip install proteomicruler\n```\n\nUsage\n--\n\nIn order to use the package, it is required that the input data is loaded into a `pandas.DataFrame` object. The following\nbasic parameters are also required:\n- `accession_id_col` - column name that contains protein accession ids\n- `mw_col` - column name that contains molecular weight of proteins\n- `ploidy` - ploidy number\n- `total_cellular_protein_concentration` - total cellular protein concentration used for calculation of total volume\n- `intensity_columns` - list of column names that contain sample intensities\n\n```python\nimport pandas as pd\n\naccession_id_col = "Protein IDs"\n# used as unique index and to directly fetch mw data from UniProt\n\nmw_col = "Mass"\n# molecular weight column name\n\nploidy = 2\n# ploidy number\n\ntotal_cellular_protein_concentration = 200\n# cellular protein concentration used for calculation of total volume\n\nfilename = r"example_data\\example_data.tsv" # example data from Perseus\ndf = pd.read_csv(filename, sep="\\t")\n\n# selecting intensity columns\nintensity_columns = df.columns[57:57+16] # select 16 columns starting from column 57th that contain sample intensity\n\n\n\n```\n\nIf the data does not contain molecular weight information, it is required to fetch it from UniProt.\n\n```python\nfrom proteomicRuler.ruler import add_mw\n\ndf = add_mw(df, accession_id_col)\ndf = df[pd.notnull(df[mw_col])]\ndf[mw_col] = df[mw_col].astype(float)\n```\n\nThe Ruler object can be created by passing the `DataFrame` object and the required parameters.\n\n```python\nfrom proteomicRuler.ruler import Ruler\n\nruler = Ruler(df, intensity_columns, mw_col, accession_id_col, ploidy, total_cellular_protein_concentration) #\nruler.df.to_csv("output.txt", sep="\\t", index=False)\n```\n\nIt is also possible to use the package through the command line interface.\n\n```bash\nUsage: ruler [OPTIONS]\n\nOptions:\n  -i, --input FILENAME          Input file containing intensity of samples and\n                                uniprot accession ids\n  -o, --output FILENAME         Output file\n  -p, --ploidy INTEGER          Ploidy of the organism\n  -t, --total-cellular FLOAT    Total cellular protein concentration\n  -m, --mw-column TEXT          Molecular weight column name\n  -a, --accession-id-col TEXT   Accession id column name\n  -c, --intensity-columns TEXT  Intensity columns list delimited by commas\n  -g, --get-mw                  Get molecular weight from uniprot\n  --help                        Show this message and exit.\n```',
     'author': 'Toan K. Phung',
     'author_email': 'toan.phungkhoiquoctoan@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://github.com/noatgnu/proteomicRuler',
     'packages': packages,
     'package_data': package_data,
     'install_requires': install_requires,
+    'entry_points': entry_points,
     'python_requires': '>=3.9,<3.12',
 }
 
 
 setup(**setup_kwargs)
```

### Comparing `proteomicruler-0.1.2/PKG-INFO` & `proteomicruler-0.1.4/PKG-INFO`

 * *Files 21% similar despite different names*

```diff
@@ -1,22 +1,23 @@
 Metadata-Version: 2.1
 Name: proteomicruler
-Version: 0.1.2
+Version: 0.1.4
 Summary: Estimate copy number from deep profile MS experiment using the Proteomic Ruler algorithm from Wiśniewski, J. R., Hein, M. Y., Cox, J. and Mann, M. (2014) A “Proteomic Ruler” for Protein Copy Number and Concentration Estimation without Spike-in Standards. Mol Cell Proteomics 13, 3497–3506.
 Home-page: https://github.com/noatgnu/proteomicRuler
 License: MIT
 Keywords: proteomic,ruler,histone,mass spectrometry
 Author: Toan K. Phung
 Author-email: toan.phungkhoiquoctoan@gmail.com
 Requires-Python: >=3.9,<3.12
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
+Requires-Dist: click (>=8.1.3,<9.0.0)
 Requires-Dist: pandas (>=1.4.3,<2.0.0)
 Requires-Dist: requests (>=2.28.1,<3.0.0)
 Requires-Dist: scipy (>=1.9.0,<2.0.0)
 Requires-Dist: seaborn (>=0.11.2,<0.12.0)
 Requires-Dist: uniprotparser (>=1.0.7,<2.0.0)
 Project-URL: Repository, https://github.com/noatgnu/proteomicRuler
 Description-Content-Type: text/markdown
@@ -79,16 +80,33 @@
 from proteomicRuler.ruler import add_mw
 
 df = add_mw(df, accession_id_col)
 df = df[pd.notnull(df[mw_col])]
 df[mw_col] = df[mw_col].astype(float)
 ```
 
-The RuleR object can be created by passing the `DataFrame` object and the required parameters.
+The Ruler object can be created by passing the `DataFrame` object and the required parameters.
 
 ```python
 from proteomicRuler.ruler import Ruler
 
 ruler = Ruler(df, intensity_columns, mw_col, accession_id_col, ploidy, total_cellular_protein_concentration) #
 ruler.df.to_csv("output.txt", sep="\t", index=False)
 ```
 
+It is also possible to use the package through the command line interface.
+
+```bash
+Usage: ruler [OPTIONS]
+
+Options:
+  -i, --input FILENAME          Input file containing intensity of samples and
+                                uniprot accession ids
+  -o, --output FILENAME         Output file
+  -p, --ploidy INTEGER          Ploidy of the organism
+  -t, --total-cellular FLOAT    Total cellular protein concentration
+  -m, --mw-column TEXT          Molecular weight column name
+  -a, --accession-id-col TEXT   Accession id column name
+  -c, --intensity-columns TEXT  Intensity columns list delimited by commas
+  -g, --get-mw                  Get molecular weight from uniprot
+  --help                        Show this message and exit.
+```
```

