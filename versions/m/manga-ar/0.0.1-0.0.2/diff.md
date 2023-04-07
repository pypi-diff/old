# Comparing `tmp/manga-ar-0.0.1.tar.gz` & `tmp/manga-ar-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "manga-ar-0.0.1.tar", last modified: Mon Apr  3 21:16:47 2023, max compression
+gzip compressed data, was "manga-ar-0.0.2.tar", last modified: Fri Apr  7 06:08:10 2023, max compression
```

## Comparing `manga-ar-0.0.1.tar` & `manga-ar-0.0.2.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxrwxrwx   0        0        0        0 2023-04-03 21:16:47.330880 manga-ar-0.0.1/
--rw-rw-rw-   0        0        0     2574 2023-04-03 21:16:47.330880 manga-ar-0.0.1/PKG-INFO
--rw-rw-rw-   0        0        0        0 2023-03-24 20:21:08.000000 manga-ar-0.0.1/README.md
--rw-rw-rw-   0        0        0       42 2023-04-03 21:16:47.331878 manga-ar-0.0.1/setup.cfg
--rw-rw-rw-   0        0        0     2893 2023-04-03 21:11:07.000000 manga-ar-0.0.1/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-03 21:16:47.302911 manga-ar-0.0.1/src/
-drwxrwxrwx   0        0        0        0 2023-04-03 21:16:47.315875 manga-ar-0.0.1/src/manga_ar/
--rw-rw-rw-   0        0        0    12114 2023-04-03 20:47:19.000000 manga-ar-0.0.1/src/manga_ar/MangaDL.py
--rw-rw-rw-   0        0        0       30 2023-04-03 20:19:53.000000 manga-ar-0.0.1/src/manga_ar/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-03 21:16:47.327860 manga-ar-0.0.1/src/manga_ar.egg-info/
--rw-rw-rw-   0        0        0     2574 2023-04-03 21:16:47.000000 manga-ar-0.0.1/src/manga_ar.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      246 2023-04-03 21:16:47.000000 manga-ar-0.0.1/src/manga_ar.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-03 21:16:47.000000 manga-ar-0.0.1/src/manga_ar.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       20 2023-04-03 21:16:47.000000 manga-ar-0.0.1/src/manga_ar.egg-info/requires.txt
--rw-rw-rw-   0        0        0        9 2023-04-03 21:16:47.000000 manga-ar-0.0.1/src/manga_ar.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 06:08:10.529254 manga-ar-0.0.2/
+-rw-rw-rw-   0        0        0     2574 2023-04-07 06:08:10.528080 manga-ar-0.0.2/PKG-INFO
+-rw-rw-rw-   0        0        0        0 2023-03-24 20:21:08.000000 manga-ar-0.0.2/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-07 06:08:10.529254 manga-ar-0.0.2/setup.cfg
+-rw-rw-rw-   0        0        0     2893 2023-04-07 06:07:38.000000 manga-ar-0.0.2/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 06:08:10.496947 manga-ar-0.0.2/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 06:08:10.512553 manga-ar-0.0.2/src/manga_ar/
+-rw-rw-rw-   0        0        0    12048 2023-04-07 06:05:57.000000 manga-ar-0.0.2/src/manga_ar/MangaDL.py
+-rw-rw-rw-   0        0        0       30 2023-04-03 20:19:53.000000 manga-ar-0.0.2/src/manga_ar/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 06:08:10.525092 manga-ar-0.0.2/src/manga_ar.egg-info/
+-rw-rw-rw-   0        0        0     2574 2023-04-07 06:08:10.000000 manga-ar-0.0.2/src/manga_ar.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      246 2023-04-07 06:08:10.000000 manga-ar-0.0.2/src/manga_ar.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 06:08:10.000000 manga-ar-0.0.2/src/manga_ar.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       20 2023-04-07 06:08:10.000000 manga-ar-0.0.2/src/manga_ar.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        9 2023-04-07 06:08:10.000000 manga-ar-0.0.2/src/manga_ar.egg-info/top_level.txt
```

### Comparing `manga-ar-0.0.1/PKG-INFO` & `manga-ar-0.0.2/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: manga-ar
-Version: 0.0.1
+Version: 0.0.2
 Summary: A Python Package To Download Manga From Arabic Site [3asq]
 Home-page: https://github.com/dexter-90/manga-dl0
 Author: Dexter
 Keywords: manga,3asq,arabic,download
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `manga-ar-0.0.1/setup.py` & `manga-ar-0.0.2/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -41,15 +41,15 @@
 * [Dexter](https://github.com/dexter-90) For [manga-ar](https://github.com/dexter-90/manga-ar)
 # 
 * ملاحظة لست مسؤولا عما تفعله بهذه المكتبة وما تقوم بتنزيله منها ولا أسامح من يحمل مانجا إباحية أو مانجا غير أخلاقية
 """
 
 setup(
     name='manga-ar',
-    version='0.0.1',
+    version='0.0.2',
     author='Dexter',
     description='A Python Package To Download Manga From Arabic Site [3asq]',
     long_description=long_description,
     long_description_content_type="text/markdown",
     url='https://github.com/dexter-90/manga-dl0',
     keywords='manga, 3asq, arabic, download',
     python_requires='>=3.7',
```

### Comparing `manga-ar-0.0.1/src/manga_ar/MangaDL.py` & `manga-ar-0.0.2/src/manga_ar/MangaDL.py`

 * *Files 3% similar despite different names*

```diff
@@ -92,48 +92,47 @@
         """Download All Manga Chapters From 3asq"""
 
         chapters = Utility.Chapters(url=self.url)
 
         print("[$] Download..")
         for chapter in chapters:
             images = [img for img in Utility.Images(chapter)]
-            num = {str(chapter).split('/')[5]}
+            num = str(chapter).split('/')[5]
 
             print(f"[+] Found {len(images)} Image For Chapter {num}")
 
             images = [requests.get(img).content for img in images]
             print("[+] Images Downloaded Successfully !")
+            print("[+] Convert Image To PDF..")
+
             try:
-                print("[+] Convert Image To PDF..")
-                name = f"@{str(self.name).title()}{chapter}"
+                name = f"@{str(self.name).title()}" + num
                 try:
                     Utility.ConvertPDF(images, name)
                 except NameError:
                     try:
                         Utility.ConvertPDF2(images, name)
                     except:
                         raise Exception("Error With Convert To PDF !")
 
-                print("[+] Images Converted Successfully")
+                print("[+] Images Converted Successfully !")
                 print(f"[+] Chapter {num} Downloaded Successfully.\n\n")
-            except:
-                print("[+] Convert Image To PDF..")
-                a = self.url.split("/")
-                a = a[5]
+            except Exception:
+                a = chapter.split("/")
                 name = f"@{a[4]}{a[5]}"
 
                 try:
                     Utility.ConvertPDF(images, name)
                 except NameError:
                     try:
                         Utility.ConvertPDF2(images, name)
                     except:
                         raise Exception("Error With Convert To PDF !")
 
-                print("[+] Images Converted !")
+                print("[+] Images Converted Successfully !")
                 print(f"[+] Chapter {num} Downloaded Successfully.\n\n")
 
     def DownloadChapters(self):
         """Download Custom Manga Chapter From 3asq"""
 
         chapters = Utility.Chapters(url=self.url)
 
@@ -337,9 +336,8 @@
                 "Synonyms": synonyms, "Status": status, "Cover": cover, "First-Chapter": chapters[0],
                 "Last-Chapter": chapters[-1]}
 
     @staticmethod
     def Check(categories):
         """Check If The Manga Unethical"""
         if "حريم" in categories or "إيتشي" in categories['Categories']:
-            raise Exception("Sorry We Can't Help You, Because Your Manga Is An Unethical.")
-
+            raise Exception("Sorry We Can't Help You, Because Your Manga Is An Unethical.")
```

### Comparing `manga-ar-0.0.1/src/manga_ar.egg-info/PKG-INFO` & `manga-ar-0.0.2/src/manga_ar.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: manga-ar
-Version: 0.0.1
+Version: 0.0.2
 Summary: A Python Package To Download Manga From Arabic Site [3asq]
 Home-page: https://github.com/dexter-90/manga-dl0
 Author: Dexter
 Keywords: manga,3asq,arabic,download
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
```

