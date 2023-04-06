# Comparing `tmp/label-studio-converter-0.0.9.tar.gz` & `tmp/label-studio-converter-0.48rc0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/label-studio-converter-0.0.9.tar", last modified: Fri Feb  7 16:14:04 2020, max compression
+gzip compressed data, was "dist/label-studio-converter-0.48rc0.tar", last modified: Fri Dec  2 03:42:43 2022, max compression
```

## Comparing `label-studio-converter-0.0.9.tar` & `label-studio-converter-0.48rc0.tar`

### file list

```diff
@@ -1,15 +1,36 @@
-drwxr-xr-x   0 nik        (502) staff       (20)        0 2020-02-07 16:14:04.000000 label-studio-converter-0.0.9/
--rw-r--r--   0 nik        (502) staff       (20)     8983 2020-02-07 16:14:04.000000 label-studio-converter-0.0.9/PKG-INFO
--rw-r--r--   0 nik        (502) staff       (20)     6313 2020-01-15 09:47:50.000000 label-studio-converter-0.0.9/README.md
-drwxr-xr-x   0 nik        (502) staff       (20)        0 2020-02-07 16:14:04.000000 label-studio-converter-0.0.9/label_studio_converter/
--rw-r--r--   0 nik        (502) staff       (20)       32 2020-01-15 10:01:58.000000 label-studio-converter-0.0.9/label_studio_converter/__init__.py
--rw-r--r--   0 nik        (502) staff       (20)    17598 2020-02-07 15:39:26.000000 label-studio-converter-0.0.9/label_studio_converter/converter.py
--rw-r--r--   0 nik        (502) staff       (20)     3351 2020-01-27 21:26:52.000000 label-studio-converter-0.0.9/label_studio_converter/utils.py
-drwxr-xr-x   0 nik        (502) staff       (20)        0 2020-02-07 16:14:04.000000 label-studio-converter-0.0.9/label_studio_converter.egg-info/
--rw-r--r--   0 nik        (502) staff       (20)     8983 2020-02-07 16:14:04.000000 label-studio-converter-0.0.9/label_studio_converter.egg-info/PKG-INFO
--rw-r--r--   0 nik        (502) staff       (20)      350 2020-02-07 16:14:04.000000 label-studio-converter-0.0.9/label_studio_converter.egg-info/SOURCES.txt
--rw-r--r--   0 nik        (502) staff       (20)        1 2020-02-07 16:14:04.000000 label-studio-converter-0.0.9/label_studio_converter.egg-info/dependency_links.txt
--rw-r--r--   0 nik        (502) staff       (20)       45 2020-02-07 16:14:04.000000 label-studio-converter-0.0.9/label_studio_converter.egg-info/requires.txt
--rw-r--r--   0 nik        (502) staff       (20)       23 2020-02-07 16:14:04.000000 label-studio-converter-0.0.9/label_studio_converter.egg-info/top_level.txt
--rw-r--r--   0 nik        (502) staff       (20)       38 2020-02-07 16:14:04.000000 label-studio-converter-0.0.9/setup.cfg
--rw-r--r--   0 nik        (502) staff       (20)      885 2020-02-07 16:12:31.000000 label-studio-converter-0.0.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-12-02 03:42:43.000000 label-studio-converter-0.48rc0/
+-rw-r--r--   0 runner    (1001) docker     (122)     8474 2022-12-02 03:42:43.000000 label-studio-converter-0.48rc0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     7985 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-12-02 03:42:43.000000 label-studio-converter-0.48rc0/label_studio_converter/
+-rw-r--r--   0 runner    (1001) docker     (122)      199 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1694 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/audio.py
+-rw-r--r--   0 runner    (1001) docker     (122)    13286 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/brush.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3521 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/cli.py
+-rw-r--r--   0 runner    (1001) docker     (122)    40567 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/converter.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-12-02 03:42:43.000000 label-studio-converter-0.48rc0/label_studio_converter/exports/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/exports/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2828 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/exports/csv.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2425 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/funsd.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-12-02 03:42:43.000000 label-studio-converter-0.48rc0/label_studio_converter/imports/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/imports/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9782 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/imports/coco.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3825 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/imports/colors.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1158 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/imports/label_config.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8048 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/imports/pathtrack.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5985 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/imports/yolo.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5165 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/main.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10975 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/label_studio_converter/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-12-02 03:42:43.000000 label-studio-converter-0.48rc0/label_studio_converter.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)     8474 2022-12-02 03:42:43.000000 label-studio-converter-0.48rc0/label_studio_converter.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)      979 2022-12-02 03:42:43.000000 label-studio-converter-0.48rc0/label_studio_converter.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2022-12-02 03:42:43.000000 label-studio-converter-0.48rc0/label_studio_converter.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       77 2022-12-02 03:42:43.000000 label-studio-converter-0.48rc0/label_studio_converter.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       87 2022-12-02 03:42:43.000000 label-studio-converter-0.48rc0/label_studio_converter.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       29 2022-12-02 03:42:43.000000 label-studio-converter-0.48rc0/label_studio_converter.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       38 2022-12-02 03:42:43.000000 label-studio-converter-0.48rc0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)     1215 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-12-02 03:42:43.000000 label-studio-converter-0.48rc0/tests/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1285 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/tests/test_brush.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5693 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/tests/test_converter_conll.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1177 2022-12-02 03:42:19.000000 label-studio-converter-0.48rc0/tests/test_export.py
```

### Comparing `label-studio-converter-0.0.9/PKG-INFO` & `label-studio-converter-0.48rc0/PKG-INFO`

 * *Files 24% similar despite different names*

```diff
@@ -1,288 +1,350 @@
 Metadata-Version: 2.1
 Name: label-studio-converter
-Version: 0.0.9
+Version: 0.48rc0
 Summary: Format converter add-on for Label Studio
 Home-page: https://github.com/heartexlabs/label-studio-converter
 Author: Heartex
 Author-email: hello@heartex.ai
 License: UNKNOWN
-Description: # Label Studio Converter
-        
-        [Website](https://labelstud.io/) • [Docs](https://labelstud.io/guide) • [Twitter](https://twitter.com/heartexlabs) • [Join Slack Community <img src="https://go.heartex.net/docs/images/slack-mini.png" width="18px"/>](https://docs.google.com/forms/d/e/1FAIpQLSdLHZx5EeT1J350JPwnY2xLanfmvplJi6VZk65C2R4XSsRBHg/viewform?usp=sf_link)
-        
-        ## Table of Contents
-        
-        - [Introduction](#introduction)
-        - [Examples](#examples)
-            - [JSON](#json)
-            - [CSV](#csv)
-            - [CoNLL 2003](#conll-2003)
-            - [COCO](#coco)
-            - [Pascal VOC XML](#pascal-voc-xml)
-        - [Contributing](#contributing)
-        - [License](#license)
-        
-        ## Introduction
-        
-        Label Studio Format Converter helps you to encode labels into the format of your favorite machine learning library.
-        
-        ## Examples
-        
-        #### JSON
-        Running from the command line:
-        ```bash
-        python backend/converter/cli.py --input examples/sentiment_analysis/completions/ --config examples/sentiment_analysis/config.xml --output tmp/output.json
-        ```
-        
-        Running from python:
-        ```python
-        from converter import Converter
-        
-        c = Converter('examples/sentiment_analysis/config.xml')
-        c.convert_to_json('examples/sentiment_analysis/completions/', 'tmp/output.json')
-        ```
-        
-        Getting output file: `tmp/output.json`
-        ```json
-        [
-          {
-            "reviewText": "Good case, Excellent value.",
-            "sentiment": "Positive"
-          },
-          {
-            "reviewText": "What a waste of money and time!",
-            "sentiment": "Negative"
-          },
-          {
-            "reviewText": "The goose neck needs a little coaxing",
-            "sentiment": "Neutral"
-          }
-        ]
-        ```
-        
-        Use cases: any tasks
-        
-        
-        #### CSV
-        Running from the command line:
-        ```bash
-        python backend/converter/cli.py --input examples/sentiment_analysis/completions/ --config examples/sentiment_analysis/config.xml --output tmp/output.tsv --format CSV --csv-separator $'\t'
-        ```
-        
-        Running from python:
-        ```python
-        from converter import Converter
-        
-        c = Converter('examples/sentiment_analysis/config.xml')
-        c.convert_to_csv('examples/sentiment_analysis/completions/', 'tmp/output.tsv', sep='\t', header=True)
-        ```
-        
-        Getting output file `tmp/output.tsv`:
-        ```tsv
-        reviewText	sentiment
-        Good case, Excellent value.	Positive
-        What a waste of money and time!	Negative
-        The goose neck needs a little coaxing	Neutral
-        ```
-        
-        Use cases: any tasks
-        
-        #### CoNLL 2003
-        
-        Running from the command line:
-        ```bash
-        python backend/converter/cli.py --input examples/named_entity/completions/ --config examples/named_entity/config.xml --output tmp/output.conll --format CONLL2003
-        ```
-        
-        Running from python:
-        ```python
-        from converter import Converter
-        
-        c = Converter('examples/named_entity/config.xml')
-        c.convert_to_conll2003('examples/named_entity/completions/', 'tmp/output.conll')
-        ```
-        
-        Getting output file `tmp/output.conll`
-        ```text
-        -DOCSTART- -X- O
-        Showers -X- _ O
-        continued -X- _ O
-        throughout -X- _ O
-        the -X- _ O
-        week -X- _ O
-        in -X- _ O
-        the -X- _ O
-        Bahia -X- _ B-Location
-        cocoa -X- _ O
-        zone, -X- _ O
-        ...
-        ```
-        
-        Use cases: text tagging
-        
-        
-        #### COCO
-        Running from the command line:
-        ```bash
-        python backend/converter/cli.py --input examples/image_bbox/completions/ --config examples/image_bbox/config.xml --output tmp/output.json --format COCO --image-dir tmp/images
-        ```
-        
-        Running from python:
-        ```python
-        from converter import Converter
-        
-        c = Converter('examples/image_bbox/config.xml')
-        c.convert_to_coco('examples/image_bbox/completions/', 'tmp/output.conll', output_image_dir='tmp/images')
-        ```
-        
-        Output images could be found in `tmp/images`
-        
-        Getting output file `tmp/output.json`
-        ```json
-        {
-          "images": [
-            {
-              "width": 800,
-              "height": 501,
-              "id": 0,
-              "file_name": "tmp/images/62a623a0d3cef27a51d3689865e7b08a"
-            }
-          ],
-          "categories": [
-            {
-              "id": 0,
-              "name": "Planet"
-            },
-            {
-              "id": 1,
-              "name": "Moonwalker"
-            }
-          ],
-          "annotations": [
-            {
-              "id": 0,
-              "image_id": 0,
-              "category_id": 0,
-              "segmentation": [],
-              "bbox": [
-                299,
-                6,
-                377,
-                260
-              ],
-              "ignore": 0,
-              "iscrowd": 0,
-              "area": 98020
-            },
-            {
-              "id": 1,
-              "image_id": 0,
-              "category_id": 1,
-              "segmentation": [],
-              "bbox": [
-                288,
-                300,
-                132,
-                90
-              ],
-              "ignore": 0,
-              "iscrowd": 0,
-              "area": 11880
-            }
-          ],
-          "info": {
-            "year": 2019,
-            "version": "1.0",
-            "contributor": "Label Studio"
-          }
-        }
-        ```
-        
-        Use cases: image object detection
-        
-        #### Pascal VOC XML
-        Running from the command line:
-        ```bash
-        python backend/converter/cli.py --input examples/image_bbox/completions/ --config examples/image_bbox/config.xml --output tmp/voc-annotations --format VOC --image-dir tmp/images
-        ```
-        
-        Running from python:
-        ```python
-        from converter import Converter
-        
-        c = Converter('examples/image_bbox/config.xml')
-        c.convert_to_voc('examples/image_bbox/completions/', 'tmp/output.conll', output_image_dir='tmp/images')
-        ```
-        
-        Output images can be found in `tmp/images`
-        
-        Corresponding annotations could be found in `tmp/voc-annotations/*.xml`:
-        ```xml
-        <?xml version="1.0" encoding="utf-8"?>
-        <annotation>
-        <folder>tmp/images</folder>
-        <filename>62a623a0d3cef27a51d3689865e7b08a</filename>
-        <source>
-        <database>MyDatabase</database>
-        <annotation>COCO2017</annotation>
-        <image>flickr</image>
-        <flickrid>NULL</flickrid>
-        </source>
-        <owner>
-        <flickrid>NULL</flickrid>
-        <name>Label Studio</name>
-        </owner>
-        <size>
-        <width>800</width>
-        <height>501</height>
-        <depth>3</depth>
-        </size>
-        <segmented>0</segmented>
-        <object>
-        <name>Planet</name>
-        <pose>Unspecified</pose>
-        <truncated>0</truncated>
-        <difficult>0</difficult>
-        <bndbox>
-        <xmin>299</xmin>
-        <ymin>6</ymin>
-        <xmax>676</xmax>
-        <ymax>266</ymax>
-        </bndbox>
-        </object>
-        <object>
-        <name>Moonwalker</name>
-        <pose>Unspecified</pose>
-        <truncated>0</truncated>
-        <difficult>0</difficult>
-        <bndbox>
-        <xmin>288</xmin>
-        <ymin>300</ymin>
-        <xmax>420</xmax>
-        <ymax>390</ymax>
-        </bndbox>
-        </object>
-        </annotation>
-        ```
-        
-        Use cases: image object detection
-        
-        ## Contributing
-        
-        We would love to get your help for creating converters to other models. Please feel free to create pull requests.
-        
-        - [Contributing Guideline](/CONTRIBUTING.md)
-        - [Code Of Conduct](/CODE_OF_CONDUCT.md)
-        
-        ## License
-        
-        This software is licensed under the [Apache 2.0 LICENSE](/LICENSE) © [Heartex](https://www.heartex.ai/). 2020
-        
-        <img src="https://github.com/heartexlabs/label-studio/blob/master/images/opossum_looking.png?raw=true" title="Hey everyone!" height="140" width="140" />
-        
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
-Classifier: License :: OSI Approved :: MIT License
+Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: OS Independent
-Requires-Python: >=3.5
+Requires-Python: >=3.6
 Description-Content-Type: text/markdown
+
+# Label Studio Converter
+
+[Website](https://labelstud.io/) • [Docs](https://labelstud.io/guide) • [Twitter](https://twitter.com/heartexlabs) • [Join Slack Community <img src="https://app.heartex.ai/docs/images/slack-mini.png" width="18px"/>](https://slack.labelstudio.heartex.com)
+
+## Table of Contents
+
+- [Introduction](#introduction)
+- [Examples](#examples)
+    - [JSON](#json)
+    - [CSV](#csv)
+    - [CoNLL 2003](#conll-2003)
+    - [COCO](#coco)
+    - [Pascal VOC XML](#pascal-voc-xml)
+- [Contributing](#contributing)
+- [License](#license)
+
+## Introduction
+
+Label Studio Format Converter helps you to encode labels into the format of your favorite machine learning library.
+
+## Examples
+
+#### JSON
+Running from the command line:
+```bash
+python label_studio_converter/cli.py --input examples/sentiment_analysis/completions/ --config examples/sentiment_analysis/config.xml --output tmp/output.json
+```
+
+Running from python:
+```python
+from label_studio_converter import Converter
+
+c = Converter('examples/sentiment_analysis/config.xml')
+c.convert_to_json('examples/sentiment_analysis/completions/', 'tmp/output.json')
+```
+
+Getting output file: `tmp/output.json`
+```json
+[
+  {
+    "reviewText": "Good case, Excellent value.",
+    "sentiment": "Positive"
+  },
+  {
+    "reviewText": "What a waste of money and time!",
+    "sentiment": "Negative"
+  },
+  {
+    "reviewText": "The goose neck needs a little coaxing",
+    "sentiment": "Neutral"
+  }
+]
+```
+
+Use cases: any tasks
+
+
+#### CSV
+Running from the command line:
+```bash
+python label_studio_converter/cli.py --input examples/sentiment_analysis/completions/ --config examples/sentiment_analysis/config.xml --output output_dir --format CSV --csv-separator $'\t'
+```
+
+Running from python:
+```python
+from label_studio_converter import Converter
+
+c = Converter('examples/sentiment_analysis/config.xml')
+c.convert_to_csv('examples/sentiment_analysis/completions/', 'output_dir', sep='\t', header=True)
+```
+
+Getting output file `tmp/output.tsv`:
+```tsv
+reviewText	sentiment
+Good case, Excellent value.	Positive
+What a waste of money and time!	Negative
+The goose neck needs a little coaxing	Neutral
+```
+
+Use cases: any tasks
+
+#### CoNLL 2003
+
+Running from the command line:
+```bash
+python label_studio_converter/cli.py --input examples/named_entity/completions/ --config examples/named_entity/config.xml --output tmp/output.conll --format CONLL2003
+```
+
+Running from python:
+```python
+from label_studio_converter import Converter
+
+c = Converter('examples/named_entity/config.xml')
+c.convert_to_conll2003('examples/named_entity/completions/', 'tmp/output.conll')
+```
+
+Getting output file `tmp/output.conll`
+```text
+-DOCSTART- -X- O
+Showers -X- _ O
+continued -X- _ O
+throughout -X- _ O
+the -X- _ O
+week -X- _ O
+in -X- _ O
+the -X- _ O
+Bahia -X- _ B-Location
+cocoa -X- _ O
+zone, -X- _ O
+...
+```
+
+Use cases: text tagging
+
+
+#### COCO
+Running from the command line:
+```bash
+python label_studio_converter/cli.py --input examples/image_bbox/completions/ --config examples/image_bbox/config.xml --output tmp/output.json --format COCO --image-dir tmp/images
+```
+
+Running from python:
+```python
+from label_studio_converter import Converter
+
+c = Converter('examples/image_bbox/config.xml')
+c.convert_to_coco('examples/image_bbox/completions/', 'tmp/output.conll', output_image_dir='tmp/images')
+```
+
+Output images could be found in `tmp/images`
+
+Getting output file `tmp/output.json`
+```json
+{
+  "images": [
+    {
+      "width": 800,
+      "height": 501,
+      "id": 0,
+      "file_name": "tmp/images/62a623a0d3cef27a51d3689865e7b08a"
+    }
+  ],
+  "categories": [
+    {
+      "id": 0,
+      "name": "Planet"
+    },
+    {
+      "id": 1,
+      "name": "Moonwalker"
+    }
+  ],
+  "annotations": [
+    {
+      "id": 0,
+      "image_id": 0,
+      "category_id": 0,
+      "segmentation": [],
+      "bbox": [
+        299,
+        6,
+        377,
+        260
+      ],
+      "ignore": 0,
+      "iscrowd": 0,
+      "area": 98020
+    },
+    {
+      "id": 1,
+      "image_id": 0,
+      "category_id": 1,
+      "segmentation": [],
+      "bbox": [
+        288,
+        300,
+        132,
+        90
+      ],
+      "ignore": 0,
+      "iscrowd": 0,
+      "area": 11880
+    }
+  ],
+  "info": {
+    "year": 2019,
+    "version": "1.0",
+    "contributor": "Label Studio"
+  }
+}
+```
+
+Use cases: image object detection
+
+#### Pascal VOC XML
+Running from the command line:
+```bash
+python label_studio_converter/cli.py --input examples/image_bbox/completions/ --config examples/image_bbox/config.xml --output tmp/voc-annotations --format VOC --image-dir tmp/images
+```
+
+Running from python:
+```python
+from label_studio_converter import Converter
+
+c = Converter('examples/image_bbox/config.xml')
+c.convert_to_voc('examples/image_bbox/completions/', 'tmp/output.conll', output_image_dir='tmp/images')
+```
+
+Output images can be found in `tmp/images`
+
+Corresponding annotations could be found in `tmp/voc-annotations/*.xml`:
+```xml
+<?xml version="1.0" encoding="utf-8"?>
+<annotation>
+<folder>tmp/images</folder>
+<filename>62a623a0d3cef27a51d3689865e7b08a</filename>
+<source>
+<database>MyDatabase</database>
+<annotation>COCO2017</annotation>
+<image>flickr</image>
+<flickrid>NULL</flickrid>
+</source>
+<owner>
+<flickrid>NULL</flickrid>
+<name>Label Studio</name>
+</owner>
+<size>
+<width>800</width>
+<height>501</height>
+<depth>3</depth>
+</size>
+<segmented>0</segmented>
+<object>
+<name>Planet</name>
+<pose>Unspecified</pose>
+<truncated>0</truncated>
+<difficult>0</difficult>
+<bndbox>
+<xmin>299</xmin>
+<ymin>6</ymin>
+<xmax>676</xmax>
+<ymax>266</ymax>
+</bndbox>
+</object>
+<object>
+<name>Moonwalker</name>
+<pose>Unspecified</pose>
+<truncated>0</truncated>
+<difficult>0</difficult>
+<bndbox>
+<xmin>288</xmin>
+<ymin>300</ymin>
+<xmax>420</xmax>
+<ymax>390</ymax>
+</bndbox>
+</object>
+</annotation>
+```
+
+Use cases: image object detection
+
+### YOLO
+
+Usage:
+
+```
+label-studio-converter import yolo -i /yolo/root/directory -o ls-tasks.json
+```
+
+Help:
+
+```
+label-studio-converter import yolo -h
+
+usage: label-studio-converter import yolo [-h] -i INPUT [-o OUTPUT]
+                                          [--to-name TO_NAME]
+                                          [--from-name FROM_NAME]
+                                          [--out-type OUT_TYPE]
+                                          [--image-root-url IMAGE_ROOT_URL]
+                                          [--image-ext IMAGE_EXT]
+
+optional arguments:
+  -h, --help            show this help message and exit
+  -i INPUT, --input INPUT
+                        directory with YOLO where images, labels, notes.json
+                        are located
+  -o OUTPUT, --output OUTPUT
+                        output file with Label Studio JSON tasks
+  --to-name TO_NAME     object name from Label Studio labeling config
+  --from-name FROM_NAME
+                        control tag name from Label Studio labeling config
+  --out-type OUT_TYPE   annotation type - "annotations" or "predictions"
+  --image-root-url IMAGE_ROOT_URL
+                        root URL path where images will be hosted, e.g.:
+                        http://example.com/images or s3://my-bucket
+  --image-ext IMAGE_EXT
+                        image extension to search: .jpg, .png
+```
+
+YOLO export folder example:
+
+```
+yolo-folder
+  images
+   - 1.jpg
+   - 2.jpg
+   - ...
+  labels
+   - 1.txt
+   - 2.txt
+
+  classes.txt
+```
+
+classes.txt example
+
+```
+Airplane
+Car
+```
+
+## Contributing
+
+We would love to get your help for creating converters to other models. Please feel free to create pull requests.
+
+- [Contributing Guideline](https://github.com/heartexlabs/label-studio/blob/develop/CONTRIBUTING.md)
+- [Code Of Conduct](https://github.com/heartexlabs/label-studio/blob/develop/CODE_OF_CONDUCT.md)
+
+## License
+
+This software is licensed under the [Apache 2.0 LICENSE](/LICENSE) © [Heartex](https://www.heartex.ai/). 2020
+
+<img src="https://github.com/heartexlabs/label-studio/blob/master/images/opossum_looking.png?raw=true" title="Hey everyone!" height="140" width="140" />
+
+
```

### Comparing `label-studio-converter-0.0.9/README.md` & `label-studio-converter-0.48rc0/README.md`

 * *Files 15% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 # Label Studio Converter
 
-[Website](https://labelstud.io/) • [Docs](https://labelstud.io/guide) • [Twitter](https://twitter.com/heartexlabs) • [Join Slack Community <img src="https://go.heartex.net/docs/images/slack-mini.png" width="18px"/>](https://docs.google.com/forms/d/e/1FAIpQLSdLHZx5EeT1J350JPwnY2xLanfmvplJi6VZk65C2R4XSsRBHg/viewform?usp=sf_link)
+[Website](https://labelstud.io/) • [Docs](https://labelstud.io/guide) • [Twitter](https://twitter.com/heartexlabs) • [Join Slack Community <img src="https://app.heartex.ai/docs/images/slack-mini.png" width="18px"/>](https://slack.labelstudio.heartex.com)
 
 ## Table of Contents
 
 - [Introduction](#introduction)
 - [Examples](#examples)
     - [JSON](#json)
     - [CSV](#csv)
@@ -19,20 +19,20 @@
 Label Studio Format Converter helps you to encode labels into the format of your favorite machine learning library.
 
 ## Examples
 
 #### JSON
 Running from the command line:
 ```bash
-python backend/converter/cli.py --input examples/sentiment_analysis/completions/ --config examples/sentiment_analysis/config.xml --output tmp/output.json
+python label_studio_converter/cli.py --input examples/sentiment_analysis/completions/ --config examples/sentiment_analysis/config.xml --output tmp/output.json
 ```
 
 Running from python:
 ```python
-from converter import Converter
+from label_studio_converter import Converter
 
 c = Converter('examples/sentiment_analysis/config.xml')
 c.convert_to_json('examples/sentiment_analysis/completions/', 'tmp/output.json')
 ```
 
 Getting output file: `tmp/output.json`
 ```json
@@ -54,23 +54,23 @@
 
 Use cases: any tasks
 
 
 #### CSV
 Running from the command line:
 ```bash
-python backend/converter/cli.py --input examples/sentiment_analysis/completions/ --config examples/sentiment_analysis/config.xml --output tmp/output.tsv --format CSV --csv-separator $'\t'
+python label_studio_converter/cli.py --input examples/sentiment_analysis/completions/ --config examples/sentiment_analysis/config.xml --output output_dir --format CSV --csv-separator $'\t'
 ```
 
 Running from python:
 ```python
-from converter import Converter
+from label_studio_converter import Converter
 
 c = Converter('examples/sentiment_analysis/config.xml')
-c.convert_to_csv('examples/sentiment_analysis/completions/', 'tmp/output.tsv', sep='\t', header=True)
+c.convert_to_csv('examples/sentiment_analysis/completions/', 'output_dir', sep='\t', header=True)
 ```
 
 Getting output file `tmp/output.tsv`:
 ```tsv
 reviewText	sentiment
 Good case, Excellent value.	Positive
 What a waste of money and time!	Negative
@@ -79,20 +79,20 @@
 
 Use cases: any tasks
 
 #### CoNLL 2003
 
 Running from the command line:
 ```bash
-python backend/converter/cli.py --input examples/named_entity/completions/ --config examples/named_entity/config.xml --output tmp/output.conll --format CONLL2003
+python label_studio_converter/cli.py --input examples/named_entity/completions/ --config examples/named_entity/config.xml --output tmp/output.conll --format CONLL2003
 ```
 
 Running from python:
 ```python
-from converter import Converter
+from label_studio_converter import Converter
 
 c = Converter('examples/named_entity/config.xml')
 c.convert_to_conll2003('examples/named_entity/completions/', 'tmp/output.conll')
 ```
 
 Getting output file `tmp/output.conll`
 ```text
@@ -112,20 +112,20 @@
 
 Use cases: text tagging
 
 
 #### COCO
 Running from the command line:
 ```bash
-python backend/converter/cli.py --input examples/image_bbox/completions/ --config examples/image_bbox/config.xml --output tmp/output.json --format COCO --image-dir tmp/images
+python label_studio_converter/cli.py --input examples/image_bbox/completions/ --config examples/image_bbox/config.xml --output tmp/output.json --format COCO --image-dir tmp/images
 ```
 
 Running from python:
 ```python
-from converter import Converter
+from label_studio_converter import Converter
 
 c = Converter('examples/image_bbox/config.xml')
 c.convert_to_coco('examples/image_bbox/completions/', 'tmp/output.conll', output_image_dir='tmp/images')
 ```
 
 Output images could be found in `tmp/images`
 
@@ -191,20 +191,20 @@
 ```
 
 Use cases: image object detection
 
 #### Pascal VOC XML
 Running from the command line:
 ```bash
-python backend/converter/cli.py --input examples/image_bbox/completions/ --config examples/image_bbox/config.xml --output tmp/voc-annotations --format VOC --image-dir tmp/images
+python label_studio_converter/cli.py --input examples/image_bbox/completions/ --config examples/image_bbox/config.xml --output tmp/voc-annotations --format VOC --image-dir tmp/images
 ```
 
 Running from python:
 ```python
-from converter import Converter
+from label_studio_converter import Converter
 
 c = Converter('examples/image_bbox/config.xml')
 c.convert_to_voc('examples/image_bbox/completions/', 'tmp/output.conll', output_image_dir='tmp/images')
 ```
 
 Output images can be found in `tmp/images`
 
@@ -255,19 +255,79 @@
 </bndbox>
 </object>
 </annotation>
 ```
 
 Use cases: image object detection
 
+### YOLO
+
+Usage:
+
+```
+label-studio-converter import yolo -i /yolo/root/directory -o ls-tasks.json
+```
+
+Help:
+
+```
+label-studio-converter import yolo -h
+
+usage: label-studio-converter import yolo [-h] -i INPUT [-o OUTPUT]
+                                          [--to-name TO_NAME]
+                                          [--from-name FROM_NAME]
+                                          [--out-type OUT_TYPE]
+                                          [--image-root-url IMAGE_ROOT_URL]
+                                          [--image-ext IMAGE_EXT]
+
+optional arguments:
+  -h, --help            show this help message and exit
+  -i INPUT, --input INPUT
+                        directory with YOLO where images, labels, notes.json
+                        are located
+  -o OUTPUT, --output OUTPUT
+                        output file with Label Studio JSON tasks
+  --to-name TO_NAME     object name from Label Studio labeling config
+  --from-name FROM_NAME
+                        control tag name from Label Studio labeling config
+  --out-type OUT_TYPE   annotation type - "annotations" or "predictions"
+  --image-root-url IMAGE_ROOT_URL
+                        root URL path where images will be hosted, e.g.:
+                        http://example.com/images or s3://my-bucket
+  --image-ext IMAGE_EXT
+                        image extension to search: .jpg, .png
+```
+
+YOLO export folder example:
+
+```
+yolo-folder
+  images
+   - 1.jpg
+   - 2.jpg
+   - ...
+  labels
+   - 1.txt
+   - 2.txt
+
+  classes.txt
+```
+
+classes.txt example
+
+```
+Airplane
+Car
+```
+
 ## Contributing
 
 We would love to get your help for creating converters to other models. Please feel free to create pull requests.
 
-- [Contributing Guideline](/CONTRIBUTING.md)
-- [Code Of Conduct](/CODE_OF_CONDUCT.md)
+- [Contributing Guideline](https://github.com/heartexlabs/label-studio/blob/develop/CONTRIBUTING.md)
+- [Code Of Conduct](https://github.com/heartexlabs/label-studio/blob/develop/CODE_OF_CONDUCT.md)
 
 ## License
 
 This software is licensed under the [Apache 2.0 LICENSE](/LICENSE) © [Heartex](https://www.heartex.ai/). 2020
 
 <img src="https://github.com/heartexlabs/label-studio/blob/master/images/opossum_looking.png?raw=true" title="Hey everyone!" height="140" width="140" />
```

### Comparing `label-studio-converter-0.0.9/label_studio_converter.egg-info/PKG-INFO` & `label-studio-converter-0.48rc0/label_studio_converter.egg-info/PKG-INFO`

 * *Files 24% similar despite different names*

```diff
@@ -1,288 +1,350 @@
 Metadata-Version: 2.1
 Name: label-studio-converter
-Version: 0.0.9
+Version: 0.48rc0
 Summary: Format converter add-on for Label Studio
 Home-page: https://github.com/heartexlabs/label-studio-converter
 Author: Heartex
 Author-email: hello@heartex.ai
 License: UNKNOWN
-Description: # Label Studio Converter
-        
-        [Website](https://labelstud.io/) • [Docs](https://labelstud.io/guide) • [Twitter](https://twitter.com/heartexlabs) • [Join Slack Community <img src="https://go.heartex.net/docs/images/slack-mini.png" width="18px"/>](https://docs.google.com/forms/d/e/1FAIpQLSdLHZx5EeT1J350JPwnY2xLanfmvplJi6VZk65C2R4XSsRBHg/viewform?usp=sf_link)
-        
-        ## Table of Contents
-        
-        - [Introduction](#introduction)
-        - [Examples](#examples)
-            - [JSON](#json)
-            - [CSV](#csv)
-            - [CoNLL 2003](#conll-2003)
-            - [COCO](#coco)
-            - [Pascal VOC XML](#pascal-voc-xml)
-        - [Contributing](#contributing)
-        - [License](#license)
-        
-        ## Introduction
-        
-        Label Studio Format Converter helps you to encode labels into the format of your favorite machine learning library.
-        
-        ## Examples
-        
-        #### JSON
-        Running from the command line:
-        ```bash
-        python backend/converter/cli.py --input examples/sentiment_analysis/completions/ --config examples/sentiment_analysis/config.xml --output tmp/output.json
-        ```
-        
-        Running from python:
-        ```python
-        from converter import Converter
-        
-        c = Converter('examples/sentiment_analysis/config.xml')
-        c.convert_to_json('examples/sentiment_analysis/completions/', 'tmp/output.json')
-        ```
-        
-        Getting output file: `tmp/output.json`
-        ```json
-        [
-          {
-            "reviewText": "Good case, Excellent value.",
-            "sentiment": "Positive"
-          },
-          {
-            "reviewText": "What a waste of money and time!",
-            "sentiment": "Negative"
-          },
-          {
-            "reviewText": "The goose neck needs a little coaxing",
-            "sentiment": "Neutral"
-          }
-        ]
-        ```
-        
-        Use cases: any tasks
-        
-        
-        #### CSV
-        Running from the command line:
-        ```bash
-        python backend/converter/cli.py --input examples/sentiment_analysis/completions/ --config examples/sentiment_analysis/config.xml --output tmp/output.tsv --format CSV --csv-separator $'\t'
-        ```
-        
-        Running from python:
-        ```python
-        from converter import Converter
-        
-        c = Converter('examples/sentiment_analysis/config.xml')
-        c.convert_to_csv('examples/sentiment_analysis/completions/', 'tmp/output.tsv', sep='\t', header=True)
-        ```
-        
-        Getting output file `tmp/output.tsv`:
-        ```tsv
-        reviewText	sentiment
-        Good case, Excellent value.	Positive
-        What a waste of money and time!	Negative
-        The goose neck needs a little coaxing	Neutral
-        ```
-        
-        Use cases: any tasks
-        
-        #### CoNLL 2003
-        
-        Running from the command line:
-        ```bash
-        python backend/converter/cli.py --input examples/named_entity/completions/ --config examples/named_entity/config.xml --output tmp/output.conll --format CONLL2003
-        ```
-        
-        Running from python:
-        ```python
-        from converter import Converter
-        
-        c = Converter('examples/named_entity/config.xml')
-        c.convert_to_conll2003('examples/named_entity/completions/', 'tmp/output.conll')
-        ```
-        
-        Getting output file `tmp/output.conll`
-        ```text
-        -DOCSTART- -X- O
-        Showers -X- _ O
-        continued -X- _ O
-        throughout -X- _ O
-        the -X- _ O
-        week -X- _ O
-        in -X- _ O
-        the -X- _ O
-        Bahia -X- _ B-Location
-        cocoa -X- _ O
-        zone, -X- _ O
-        ...
-        ```
-        
-        Use cases: text tagging
-        
-        
-        #### COCO
-        Running from the command line:
-        ```bash
-        python backend/converter/cli.py --input examples/image_bbox/completions/ --config examples/image_bbox/config.xml --output tmp/output.json --format COCO --image-dir tmp/images
-        ```
-        
-        Running from python:
-        ```python
-        from converter import Converter
-        
-        c = Converter('examples/image_bbox/config.xml')
-        c.convert_to_coco('examples/image_bbox/completions/', 'tmp/output.conll', output_image_dir='tmp/images')
-        ```
-        
-        Output images could be found in `tmp/images`
-        
-        Getting output file `tmp/output.json`
-        ```json
-        {
-          "images": [
-            {
-              "width": 800,
-              "height": 501,
-              "id": 0,
-              "file_name": "tmp/images/62a623a0d3cef27a51d3689865e7b08a"
-            }
-          ],
-          "categories": [
-            {
-              "id": 0,
-              "name": "Planet"
-            },
-            {
-              "id": 1,
-              "name": "Moonwalker"
-            }
-          ],
-          "annotations": [
-            {
-              "id": 0,
-              "image_id": 0,
-              "category_id": 0,
-              "segmentation": [],
-              "bbox": [
-                299,
-                6,
-                377,
-                260
-              ],
-              "ignore": 0,
-              "iscrowd": 0,
-              "area": 98020
-            },
-            {
-              "id": 1,
-              "image_id": 0,
-              "category_id": 1,
-              "segmentation": [],
-              "bbox": [
-                288,
-                300,
-                132,
-                90
-              ],
-              "ignore": 0,
-              "iscrowd": 0,
-              "area": 11880
-            }
-          ],
-          "info": {
-            "year": 2019,
-            "version": "1.0",
-            "contributor": "Label Studio"
-          }
-        }
-        ```
-        
-        Use cases: image object detection
-        
-        #### Pascal VOC XML
-        Running from the command line:
-        ```bash
-        python backend/converter/cli.py --input examples/image_bbox/completions/ --config examples/image_bbox/config.xml --output tmp/voc-annotations --format VOC --image-dir tmp/images
-        ```
-        
-        Running from python:
-        ```python
-        from converter import Converter
-        
-        c = Converter('examples/image_bbox/config.xml')
-        c.convert_to_voc('examples/image_bbox/completions/', 'tmp/output.conll', output_image_dir='tmp/images')
-        ```
-        
-        Output images can be found in `tmp/images`
-        
-        Corresponding annotations could be found in `tmp/voc-annotations/*.xml`:
-        ```xml
-        <?xml version="1.0" encoding="utf-8"?>
-        <annotation>
-        <folder>tmp/images</folder>
-        <filename>62a623a0d3cef27a51d3689865e7b08a</filename>
-        <source>
-        <database>MyDatabase</database>
-        <annotation>COCO2017</annotation>
-        <image>flickr</image>
-        <flickrid>NULL</flickrid>
-        </source>
-        <owner>
-        <flickrid>NULL</flickrid>
-        <name>Label Studio</name>
-        </owner>
-        <size>
-        <width>800</width>
-        <height>501</height>
-        <depth>3</depth>
-        </size>
-        <segmented>0</segmented>
-        <object>
-        <name>Planet</name>
-        <pose>Unspecified</pose>
-        <truncated>0</truncated>
-        <difficult>0</difficult>
-        <bndbox>
-        <xmin>299</xmin>
-        <ymin>6</ymin>
-        <xmax>676</xmax>
-        <ymax>266</ymax>
-        </bndbox>
-        </object>
-        <object>
-        <name>Moonwalker</name>
-        <pose>Unspecified</pose>
-        <truncated>0</truncated>
-        <difficult>0</difficult>
-        <bndbox>
-        <xmin>288</xmin>
-        <ymin>300</ymin>
-        <xmax>420</xmax>
-        <ymax>390</ymax>
-        </bndbox>
-        </object>
-        </annotation>
-        ```
-        
-        Use cases: image object detection
-        
-        ## Contributing
-        
-        We would love to get your help for creating converters to other models. Please feel free to create pull requests.
-        
-        - [Contributing Guideline](/CONTRIBUTING.md)
-        - [Code Of Conduct](/CODE_OF_CONDUCT.md)
-        
-        ## License
-        
-        This software is licensed under the [Apache 2.0 LICENSE](/LICENSE) © [Heartex](https://www.heartex.ai/). 2020
-        
-        <img src="https://github.com/heartexlabs/label-studio/blob/master/images/opossum_looking.png?raw=true" title="Hey everyone!" height="140" width="140" />
-        
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
-Classifier: License :: OSI Approved :: MIT License
+Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: OS Independent
-Requires-Python: >=3.5
+Requires-Python: >=3.6
 Description-Content-Type: text/markdown
+
+# Label Studio Converter
+
+[Website](https://labelstud.io/) • [Docs](https://labelstud.io/guide) • [Twitter](https://twitter.com/heartexlabs) • [Join Slack Community <img src="https://app.heartex.ai/docs/images/slack-mini.png" width="18px"/>](https://slack.labelstudio.heartex.com)
+
+## Table of Contents
+
+- [Introduction](#introduction)
+- [Examples](#examples)
+    - [JSON](#json)
+    - [CSV](#csv)
+    - [CoNLL 2003](#conll-2003)
+    - [COCO](#coco)
+    - [Pascal VOC XML](#pascal-voc-xml)
+- [Contributing](#contributing)
+- [License](#license)
+
+## Introduction
+
+Label Studio Format Converter helps you to encode labels into the format of your favorite machine learning library.
+
+## Examples
+
+#### JSON
+Running from the command line:
+```bash
+python label_studio_converter/cli.py --input examples/sentiment_analysis/completions/ --config examples/sentiment_analysis/config.xml --output tmp/output.json
+```
+
+Running from python:
+```python
+from label_studio_converter import Converter
+
+c = Converter('examples/sentiment_analysis/config.xml')
+c.convert_to_json('examples/sentiment_analysis/completions/', 'tmp/output.json')
+```
+
+Getting output file: `tmp/output.json`
+```json
+[
+  {
+    "reviewText": "Good case, Excellent value.",
+    "sentiment": "Positive"
+  },
+  {
+    "reviewText": "What a waste of money and time!",
+    "sentiment": "Negative"
+  },
+  {
+    "reviewText": "The goose neck needs a little coaxing",
+    "sentiment": "Neutral"
+  }
+]
+```
+
+Use cases: any tasks
+
+
+#### CSV
+Running from the command line:
+```bash
+python label_studio_converter/cli.py --input examples/sentiment_analysis/completions/ --config examples/sentiment_analysis/config.xml --output output_dir --format CSV --csv-separator $'\t'
+```
+
+Running from python:
+```python
+from label_studio_converter import Converter
+
+c = Converter('examples/sentiment_analysis/config.xml')
+c.convert_to_csv('examples/sentiment_analysis/completions/', 'output_dir', sep='\t', header=True)
+```
+
+Getting output file `tmp/output.tsv`:
+```tsv
+reviewText	sentiment
+Good case, Excellent value.	Positive
+What a waste of money and time!	Negative
+The goose neck needs a little coaxing	Neutral
+```
+
+Use cases: any tasks
+
+#### CoNLL 2003
+
+Running from the command line:
+```bash
+python label_studio_converter/cli.py --input examples/named_entity/completions/ --config examples/named_entity/config.xml --output tmp/output.conll --format CONLL2003
+```
+
+Running from python:
+```python
+from label_studio_converter import Converter
+
+c = Converter('examples/named_entity/config.xml')
+c.convert_to_conll2003('examples/named_entity/completions/', 'tmp/output.conll')
+```
+
+Getting output file `tmp/output.conll`
+```text
+-DOCSTART- -X- O
+Showers -X- _ O
+continued -X- _ O
+throughout -X- _ O
+the -X- _ O
+week -X- _ O
+in -X- _ O
+the -X- _ O
+Bahia -X- _ B-Location
+cocoa -X- _ O
+zone, -X- _ O
+...
+```
+
+Use cases: text tagging
+
+
+#### COCO
+Running from the command line:
+```bash
+python label_studio_converter/cli.py --input examples/image_bbox/completions/ --config examples/image_bbox/config.xml --output tmp/output.json --format COCO --image-dir tmp/images
+```
+
+Running from python:
+```python
+from label_studio_converter import Converter
+
+c = Converter('examples/image_bbox/config.xml')
+c.convert_to_coco('examples/image_bbox/completions/', 'tmp/output.conll', output_image_dir='tmp/images')
+```
+
+Output images could be found in `tmp/images`
+
+Getting output file `tmp/output.json`
+```json
+{
+  "images": [
+    {
+      "width": 800,
+      "height": 501,
+      "id": 0,
+      "file_name": "tmp/images/62a623a0d3cef27a51d3689865e7b08a"
+    }
+  ],
+  "categories": [
+    {
+      "id": 0,
+      "name": "Planet"
+    },
+    {
+      "id": 1,
+      "name": "Moonwalker"
+    }
+  ],
+  "annotations": [
+    {
+      "id": 0,
+      "image_id": 0,
+      "category_id": 0,
+      "segmentation": [],
+      "bbox": [
+        299,
+        6,
+        377,
+        260
+      ],
+      "ignore": 0,
+      "iscrowd": 0,
+      "area": 98020
+    },
+    {
+      "id": 1,
+      "image_id": 0,
+      "category_id": 1,
+      "segmentation": [],
+      "bbox": [
+        288,
+        300,
+        132,
+        90
+      ],
+      "ignore": 0,
+      "iscrowd": 0,
+      "area": 11880
+    }
+  ],
+  "info": {
+    "year": 2019,
+    "version": "1.0",
+    "contributor": "Label Studio"
+  }
+}
+```
+
+Use cases: image object detection
+
+#### Pascal VOC XML
+Running from the command line:
+```bash
+python label_studio_converter/cli.py --input examples/image_bbox/completions/ --config examples/image_bbox/config.xml --output tmp/voc-annotations --format VOC --image-dir tmp/images
+```
+
+Running from python:
+```python
+from label_studio_converter import Converter
+
+c = Converter('examples/image_bbox/config.xml')
+c.convert_to_voc('examples/image_bbox/completions/', 'tmp/output.conll', output_image_dir='tmp/images')
+```
+
+Output images can be found in `tmp/images`
+
+Corresponding annotations could be found in `tmp/voc-annotations/*.xml`:
+```xml
+<?xml version="1.0" encoding="utf-8"?>
+<annotation>
+<folder>tmp/images</folder>
+<filename>62a623a0d3cef27a51d3689865e7b08a</filename>
+<source>
+<database>MyDatabase</database>
+<annotation>COCO2017</annotation>
+<image>flickr</image>
+<flickrid>NULL</flickrid>
+</source>
+<owner>
+<flickrid>NULL</flickrid>
+<name>Label Studio</name>
+</owner>
+<size>
+<width>800</width>
+<height>501</height>
+<depth>3</depth>
+</size>
+<segmented>0</segmented>
+<object>
+<name>Planet</name>
+<pose>Unspecified</pose>
+<truncated>0</truncated>
+<difficult>0</difficult>
+<bndbox>
+<xmin>299</xmin>
+<ymin>6</ymin>
+<xmax>676</xmax>
+<ymax>266</ymax>
+</bndbox>
+</object>
+<object>
+<name>Moonwalker</name>
+<pose>Unspecified</pose>
+<truncated>0</truncated>
+<difficult>0</difficult>
+<bndbox>
+<xmin>288</xmin>
+<ymin>300</ymin>
+<xmax>420</xmax>
+<ymax>390</ymax>
+</bndbox>
+</object>
+</annotation>
+```
+
+Use cases: image object detection
+
+### YOLO
+
+Usage:
+
+```
+label-studio-converter import yolo -i /yolo/root/directory -o ls-tasks.json
+```
+
+Help:
+
+```
+label-studio-converter import yolo -h
+
+usage: label-studio-converter import yolo [-h] -i INPUT [-o OUTPUT]
+                                          [--to-name TO_NAME]
+                                          [--from-name FROM_NAME]
+                                          [--out-type OUT_TYPE]
+                                          [--image-root-url IMAGE_ROOT_URL]
+                                          [--image-ext IMAGE_EXT]
+
+optional arguments:
+  -h, --help            show this help message and exit
+  -i INPUT, --input INPUT
+                        directory with YOLO where images, labels, notes.json
+                        are located
+  -o OUTPUT, --output OUTPUT
+                        output file with Label Studio JSON tasks
+  --to-name TO_NAME     object name from Label Studio labeling config
+  --from-name FROM_NAME
+                        control tag name from Label Studio labeling config
+  --out-type OUT_TYPE   annotation type - "annotations" or "predictions"
+  --image-root-url IMAGE_ROOT_URL
+                        root URL path where images will be hosted, e.g.:
+                        http://example.com/images or s3://my-bucket
+  --image-ext IMAGE_EXT
+                        image extension to search: .jpg, .png
+```
+
+YOLO export folder example:
+
+```
+yolo-folder
+  images
+   - 1.jpg
+   - 2.jpg
+   - ...
+  labels
+   - 1.txt
+   - 2.txt
+
+  classes.txt
+```
+
+classes.txt example
+
+```
+Airplane
+Car
+```
+
+## Contributing
+
+We would love to get your help for creating converters to other models. Please feel free to create pull requests.
+
+- [Contributing Guideline](https://github.com/heartexlabs/label-studio/blob/develop/CONTRIBUTING.md)
+- [Code Of Conduct](https://github.com/heartexlabs/label-studio/blob/develop/CODE_OF_CONDUCT.md)
+
+## License
+
+This software is licensed under the [Apache 2.0 LICENSE](/LICENSE) © [Heartex](https://www.heartex.ai/). 2020
+
+<img src="https://github.com/heartexlabs/label-studio/blob/master/images/opossum_looking.png?raw=true" title="Hey everyone!" height="140" width="140" />
+
+
```

