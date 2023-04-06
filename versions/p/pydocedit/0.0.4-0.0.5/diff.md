# Comparing `tmp/pydocedit-0.0.4.tar.gz` & `tmp/pydocedit-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pydocedit-0.0.4.tar", last modified: Tue Apr  4 14:04:32 2023, max compression
+gzip compressed data, was "pydocedit-0.0.5.tar", last modified: Thu Apr  6 10:13:23 2023, max compression
```

## Comparing `pydocedit-0.0.4.tar` & `pydocedit-0.0.5.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxrwxrwx   0        0        0        0 2023-04-04 14:04:32.144744 pydocedit-0.0.4/
--rw-rw-rw-   0        0        0     1068 2022-09-02 09:20:59.000000 pydocedit-0.0.4/LICENSE
--rw-rw-rw-   0        0        0     1005 2023-04-04 14:04:32.143745 pydocedit-0.0.4/PKG-INFO
--rw-rw-rw-   0        0        0      467 2023-04-03 06:28:02.000000 pydocedit-0.0.4/README.md
--rw-rw-rw-   0        0        0       42 2023-04-04 14:04:32.145744 pydocedit-0.0.4/setup.cfg
--rw-rw-rw-   0        0        0      956 2023-04-04 14:03:15.000000 pydocedit-0.0.4/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-04 14:04:32.128661 pydocedit-0.0.4/src/
-drwxrwxrwx   0        0        0        0 2023-04-04 14:04:32.141220 pydocedit-0.0.4/src/pydocedit.egg-info/
--rw-rw-rw-   0        0        0     1005 2023-04-04 14:04:31.000000 pydocedit-0.0.4/src/pydocedit.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      227 2023-04-04 14:04:31.000000 pydocedit-0.0.4/src/pydocedit.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-04 14:04:31.000000 pydocedit-0.0.4/src/pydocedit.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       47 2023-04-04 14:04:31.000000 pydocedit-0.0.4/src/pydocedit.egg-info/requires.txt
--rw-rw-rw-   0        0        0       10 2023-04-04 14:04:31.000000 pydocedit-0.0.4/src/pydocedit.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     8076 2023-04-04 14:02:30.000000 pydocedit-0.0.4/src/pydocedit.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:13:23.174383 pydocedit-0.0.5/
+-rw-rw-rw-   0        0        0     1068 2022-09-02 09:20:59.000000 pydocedit-0.0.5/LICENSE
+-rw-rw-rw-   0        0        0     1005 2023-04-06 10:13:23.173383 pydocedit-0.0.5/PKG-INFO
+-rw-rw-rw-   0        0        0      467 2023-04-03 06:28:02.000000 pydocedit-0.0.5/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-06 10:13:23.175385 pydocedit-0.0.5/setup.cfg
+-rw-rw-rw-   0        0        0      973 2023-04-06 10:10:39.000000 pydocedit-0.0.5/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:13:23.161075 pydocedit-0.0.5/src/
+drwxrwxrwx   0        0        0        0 2023-04-06 10:13:23.171384 pydocedit-0.0.5/src/pydocedit.egg-info/
+-rw-rw-rw-   0        0        0     1005 2023-04-06 10:13:22.000000 pydocedit-0.0.5/src/pydocedit.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      227 2023-04-06 10:13:23.000000 pydocedit-0.0.5/src/pydocedit.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 10:13:22.000000 pydocedit-0.0.5/src/pydocedit.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       53 2023-04-06 10:13:22.000000 pydocedit-0.0.5/src/pydocedit.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       10 2023-04-06 10:13:22.000000 pydocedit-0.0.5/src/pydocedit.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     7914 2023-04-06 10:10:49.000000 pydocedit-0.0.5/src/pydocedit.py
```

### Comparing `pydocedit-0.0.4/LICENSE` & `pydocedit-0.0.5/LICENSE`

 * *Files identical despite different names*

### Comparing `pydocedit-0.0.4/PKG-INFO` & `pydocedit-0.0.5/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pydocedit
-Version: 0.0.4
+Version: 0.0.5
 Summary: A package to take edit doc/docx/trf files.
 Home-page: https://www.drateendrajha.com/projects/pydocedit
 Author: Ateendra Jha
 Author-email: ateendrajha@live.com
 Keywords: video,images,video2images,image crop
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `pydocedit-0.0.4/setup.py` & `pydocedit-0.0.5/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 import setuptools
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setup(
     name='pydocedit',
-    version='0.0.4',
+    version='0.0.5',
     description='A package to take edit doc/docx/trf files.',
     author= 'Ateendra Jha',
     author_email="ateendrajha@live.com",
     url = 'https://www.drateendrajha.com/projects/pydocedit',
     long_description_content_type="text/markdown",
     long_description = long_description,
     packages=setuptools.find_packages(),
@@ -25,10 +25,11 @@
     package_dir={'':'src'},
     install_requires = [
         'regex',
         'comtypes',
         'pillow',
         'python-docx',
         'nltk',
-        'pywin32'
+        'pywin32',
+        'glob2'
     ]
 )
```

### Comparing `pydocedit-0.0.4/src/pydocedit.egg-info/PKG-INFO` & `pydocedit-0.0.5/src/pydocedit.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pydocedit
-Version: 0.0.4
+Version: 0.0.5
 Summary: A package to take edit doc/docx/trf files.
 Home-page: https://www.drateendrajha.com/projects/pydocedit
 Author: Ateendra Jha
 Author-email: ateendrajha@live.com
 Keywords: video,images,video2images,image crop
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `pydocedit-0.0.4/src/pydocedit.py` & `pydocedit-0.0.5/src/pydocedit.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 import re
 import os
 import comtypes.client
 import docx
 from nltk.stem import WordNetLemmatizer
 from docx.opc.constants import RELATIONSHIP_TYPE as RT
 import win32com.client as win32
+import glob
 
 
 
 
 # Data 
 country_data = {'Afghanistan': 'Afghan',
  'Albania': 'Albanian',
@@ -135,18 +136,22 @@
 
 formats = ["%b %d, %Y", "%Y-%m-%d", "%m/%d/%Y"]
 
 phone_pattern = re.compile(r"(\d{3}[-.\s]??\d{3}[-.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-.\s]??\d{4})|"r"(\+\d{2}\s\d{4}\s\d{4})|"r"(\+\d{1,12}(\s\d{3}){0,3})")
 
 passport_pattern = re.compile(r"\b[A-Z]+\d+[A-Z\d]*\b")
 
-name_pattern = re.compile(r"\b[A-Z][A-Za-z]+ [A-Z][A-Za-z]+\b")
-
+name_pattern = re.compile(r"\b[a-zA-Z][A-Za-z]+ [a-zA-Z][A-Za-z]+\b")
 
 def file_conv(dir_path):
+    for file in glob.glob(os.path.join(dir_path, "*.rtf")):
+        root, ext = os.path.splitext(file)
+        if ext == ".rtf":
+            new_path = root + ".doc"
+            os.rename(file, new_path)
     files = os.listdir(dir_path)
     non_inluded = []
     for f in files:
         print(f"{f} - Conversion Initiated")
         try:
             if f.endswith('.docx'):
                 pass
@@ -155,22 +160,14 @@
                 output_file = os.path.join(dir_path, f.replace('.doc', '.docx'))
                 word = comtypes.client.CreateObject("Word.Application")
                 doc = word.Documents.Open(os.path.abspath(input_file))
                 doc.SaveAs(output_file, FileFormat=12)
                 doc.Close()
                 word.Quit()
                 print(f , ": doc conversion done")
-
-            elif f.endswith('.rtf') :
-                word = win32.Dispatch("Word.Application")
-                doc = word.Documents.Open(os.path.join(dir_path,f))
-                doc.SaveAs(os.path.join(dir_path, f.replace('.rtf', '.docx')), FileFormat=12)
-                doc.Close()
-                word.Quit()
-                print(f , ": rtf conversion done")
         except:
             print(f , ": this rtf conversion failed reasons may be - File format not supported / read only document format")
             non_inluded.append(f)
     print(f'Files not included in modification : {non_inluded}')
 
 class Edit_doc():
     def __init__(self, new_in_path, out_path, name_pattern, new_name, emp_id, new_email, address):
@@ -181,36 +178,30 @@
         self.new_name = new_name
         self.emp_id = emp_id
         self.new_email = new_email
         self.address = address
 
     def edit_doc(self):
         name_list = []
-        for para in self.doc.paragraphs[:1]:
+        for para in self.doc.paragraphs[:1]+self.doc.paragraphs[-2:]:
             for run in para.runs:
                 names = self.name_pattern.findall(run.text)
                 for name in names:
                     run.text = run.text.replace(name, self.new_name)
                     name_list.append(name)
         for para in self.doc.paragraphs:
-            for run in para.runs:
                 for n in name_list:
                     for n in n.split(" "):
-                        if n in run.text.split(" "):
-                            run.text = para.text.replace(n, self.new_name.split(" ")[1])
+                        if n in para.text.split(" "):
+                            para.text = para.text.replace(n, self.new_name.split(" ")[1])
         
         header = self.doc.sections[0].header
+        # Get the first paragraph in the header
         paragraph = header.paragraphs
-        for para in paragraph:
-            for f_n in name_list:
-                for n in f_n.split(" "):
-                    if f_n in para.text:
-                        para.text = para.text.replace(f_n, self.new_name)
-                    if n in para.text:
-                        para.text = para.text.replace(n, self.new_name.split(" ")[1])
+        # Clear the existing text in the paragraph
 
         country_names = country_data.keys()
 
         for country in country_names:
             for para in self.doc.paragraphs[:5]+self.doc.paragraphs[-20:]:
                 if country in [i.capitalize().strip() for i in para.text.split(" ")]:
                     para.text = self.address
@@ -235,14 +226,19 @@
                 if rels[rel].reltype == RT.HYPERLINK:
                     rels[rel]._target =''
             if re.match(email_pattern, para.text):
                 self.doc.add_paragraph (self.new_email)
 
         for para in self.doc.paragraphs:
             for run in para.runs:
+                names = self.name_pattern.findall(run.text)
+                for name in names:
+                    run.text = run.text.replace(name, self.new_name)
+                    name_list.append(name)
+            for run in para.runs:
                 if run.text or run.element.xml.startswith('<w:drawing'):
                     continue
                 else:
                     run.element.clear()
 
         self.doc.save(self.out_path)
         return self.out_path
```

