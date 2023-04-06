# Comparing `tmp/plagiat-0.1.4.tar.gz` & `tmp/plagiat-0.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "plagiat-0.1.4.tar", last modified: Thu Apr  6 13:15:46 2023, max compression
+gzip compressed data, was "plagiat-0.1.5.tar", last modified: Thu Apr  6 13:19:45 2023, max compression
```

## Comparing `plagiat-0.1.4.tar` & `plagiat-0.1.5.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxr-xr-x   0 novay      (501) staff       (20)        0 2023-04-06 13:15:46.435291 plagiat-0.1.4/
--rw-r--r--   0 novay      (501) staff       (20)     4081 2023-04-06 13:15:46.435135 plagiat-0.1.4/PKG-INFO
--rw-r--r--   0 novay      (501) staff       (20)     3400 2023-04-06 13:14:44.000000 plagiat-0.1.4/README.md
-drwxr-xr-x   0 novay      (501) staff       (20)        0 2023-04-06 13:15:46.434025 plagiat-0.1.4/plagiat/
--rw-r--r--   0 novay      (501) staff       (20)       68 2023-04-06 13:15:32.000000 plagiat-0.1.4/plagiat/__init__.py
--rw-r--r--   0 novay      (501) staff       (20)     1794 2023-04-06 12:58:38.000000 plagiat-0.1.4/plagiat/cosine.py
--rw-r--r--   0 novay      (501) staff       (20)     3672 2023-04-06 13:15:13.000000 plagiat-0.1.4/plagiat/deteksi.py
--rw-r--r--   0 novay      (501) staff       (20)     1226 2023-04-06 13:00:53.000000 plagiat-0.1.4/plagiat/jaccard.py
--rw-r--r--   0 novay      (501) staff       (20)     1155 2023-04-02 09:06:09.000000 plagiat-0.1.4/plagiat/rabin_karp.py
-drwxr-xr-x   0 novay      (501) staff       (20)        0 2023-04-06 13:15:46.434909 plagiat-0.1.4/plagiat.egg-info/
--rw-r--r--   0 novay      (501) staff       (20)     4081 2023-04-06 13:15:46.000000 plagiat-0.1.4/plagiat.egg-info/PKG-INFO
--rw-r--r--   0 novay      (501) staff       (20)      270 2023-04-06 13:15:46.000000 plagiat-0.1.4/plagiat.egg-info/SOURCES.txt
--rw-r--r--   0 novay      (501) staff       (20)        1 2023-04-06 13:15:46.000000 plagiat-0.1.4/plagiat.egg-info/dependency_links.txt
--rw-r--r--   0 novay      (501) staff       (20)        9 2023-04-06 13:15:46.000000 plagiat-0.1.4/plagiat.egg-info/requires.txt
--rw-r--r--   0 novay      (501) staff       (20)        8 2023-04-06 13:15:46.000000 plagiat-0.1.4/plagiat.egg-info/top_level.txt
--rw-r--r--   0 novay      (501) staff       (20)       38 2023-04-06 13:15:46.435345 plagiat-0.1.4/setup.cfg
--rw-r--r--   0 novay      (501) staff       (20)     1051 2023-04-06 13:15:27.000000 plagiat-0.1.4/setup.py
+drwxr-xr-x   0 novay      (501) staff       (20)        0 2023-04-06 13:19:45.103572 plagiat-0.1.5/
+-rw-r--r--   0 novay      (501) staff       (20)     4070 2023-04-06 13:19:45.103428 plagiat-0.1.5/PKG-INFO
+-rw-r--r--   0 novay      (501) staff       (20)     3389 2023-04-06 13:18:43.000000 plagiat-0.1.5/README.md
+drwxr-xr-x   0 novay      (501) staff       (20)        0 2023-04-06 13:19:45.102434 plagiat-0.1.5/plagiat/
+-rw-r--r--   0 novay      (501) staff       (20)       68 2023-04-06 13:19:35.000000 plagiat-0.1.5/plagiat/__init__.py
+-rw-r--r--   0 novay      (501) staff       (20)     1794 2023-04-06 12:58:38.000000 plagiat-0.1.5/plagiat/cosine.py
+-rw-r--r--   0 novay      (501) staff       (20)     3672 2023-04-06 13:15:13.000000 plagiat-0.1.5/plagiat/deteksi.py
+-rw-r--r--   0 novay      (501) staff       (20)     1226 2023-04-06 13:00:53.000000 plagiat-0.1.5/plagiat/jaccard.py
+-rw-r--r--   0 novay      (501) staff       (20)     1155 2023-04-02 09:06:09.000000 plagiat-0.1.5/plagiat/rabin_karp.py
+drwxr-xr-x   0 novay      (501) staff       (20)        0 2023-04-06 13:19:45.103212 plagiat-0.1.5/plagiat.egg-info/
+-rw-r--r--   0 novay      (501) staff       (20)     4070 2023-04-06 13:19:45.000000 plagiat-0.1.5/plagiat.egg-info/PKG-INFO
+-rw-r--r--   0 novay      (501) staff       (20)      270 2023-04-06 13:19:45.000000 plagiat-0.1.5/plagiat.egg-info/SOURCES.txt
+-rw-r--r--   0 novay      (501) staff       (20)        1 2023-04-06 13:19:45.000000 plagiat-0.1.5/plagiat.egg-info/dependency_links.txt
+-rw-r--r--   0 novay      (501) staff       (20)        9 2023-04-06 13:19:45.000000 plagiat-0.1.5/plagiat.egg-info/requires.txt
+-rw-r--r--   0 novay      (501) staff       (20)        8 2023-04-06 13:19:45.000000 plagiat-0.1.5/plagiat.egg-info/top_level.txt
+-rw-r--r--   0 novay      (501) staff       (20)       38 2023-04-06 13:19:45.103628 plagiat-0.1.5/setup.cfg
+-rw-r--r--   0 novay      (501) staff       (20)     1051 2023-04-06 13:19:31.000000 plagiat-0.1.5/setup.py
```

### Comparing `plagiat-0.1.4/PKG-INFO` & `plagiat-0.1.5/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: plagiat
-Version: 0.1.4
+Version: 0.1.5
 Summary: Library untuk memeriksa tingkat plagiarisme.
 Home-page: https://novay.web.id/
 Author: Novianto Rahmadi
 Author-email: novay@btekno.id
 License: MIT
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
@@ -15,84 +15,86 @@
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Operating System :: OS Independent
 Description-Content-Type: text/markdown
 
 # Plagiat
 
-<small>Pustaka ini dibuat hanya sebagai penunjang untuk membantu saya menguji-coba dan memahami semua konsep algoritma untuk menghitung similaritas.</small>
+Library untuk memeriksa tingkat Plagiarisme atau *Similarity* menggunakan Bahasa Python. Secara default library ini akan menggunakan Algoritma Rabin Karp sebagai perhitungan utamanya.
 
-Library untuk memeriksa tingkat Plagiarisme menggunakan Bahasa Python. Secara default library ini akan menggunakan Algoritma Rabin Karp sebagai perhitungan utamanya.
-
-Referensi **Rabin Karp**:
-- **Ranti Eka Putri, Andysah Putera Utama Siahaan**<br/>https://www.researchgate.net/publication/319272358_Examination_of_Document_Similarity_Using_Rabin-Karp_Algorithm
-- **Andysah Putera Utama Siahaan, Mesran, Robbi Rahim, Dodi Siregar**<br/>https://www.ijstr.org/final-print/july2017/K-gram-As-A-Determinant-Of-Plagiarism-Level-In-Rabin-karp-Algorithm.pdf
-
-
-Penambahan Algoritma: 
-
-Referensi **Jaccard Similarity**:
-- https://en.wikipedia.org/wiki/Jaccard_index
-
-Referensi **Cosine Similarity**:
-- **Jiapeng Wang, Yihong Dong**<br/>https://www.researchgate.net/publication/344010599_Measurement_of_Text_Similarity_A_Survey
+Pustaka ini dibuat hanya sebagai penunjang untuk membantu saya menguji-coba dan memahami semua konsep algoritma untuk menghitung similaritas.
 
 ### Instalasi
 ```
 pip install plagiat
 ```
 
-### Menggunakan File .txt
+### Cara Penggunaan
+
+#### Menggunakan File .txt
 ```Python
 from plagiat.deteksi import Deteksi
 
 file_1 = '/content/kalimat-1.txt'
 file_2 = '/content/kalimat-2.txt'
 
 cek = Deteksi(file_1, file_2, url=True).hitung()
 
 print('Persentase plagiarisme = {0}%'.format(cek))
 ```
 
-### Menggunakan Text
+#### Menggunakan Text
 ```Python
 from plagiat.deteksi import Deteksi
 
 string_1 = "Aku sedang belajar kecerdasan buatan"
 string_2 = "Mahasiswa yang cerdas selalu siap menerima tantangan"
 
 cek = Deteksi(string_1, string_2, text=True).hitung()
 
 print('Persentase plagiarisme = {0}%'.format(cek))
 ```
 
-### Menggunakan URL
+#### Menggunakan URL
 ```Python
 from plagiat.deteksi import Deteksi
 
 teks_1 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-1.txt'
 teks_2 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-1.txt'
 
 cek = Deteksi(teks_1, teks_2, url=True).hitung()
 
 print('Persentase plagiarisme = {0}%'.format(cek))
 ```
 
-### Penggunaan Parameter
+#### Penggunaan Parameter
 ```Python
 from plagiat.deteksi import Deteksi
 
 Deteksi(teks_1, teks_2, text=True, url=True, bahasa='english', method='Cosine').hitung()
 ```
 **Penjelasan**<br/>
 - `text=True` digunakan untuk mendeteksi string<br/> default False
 - `url=True` digunakan untuk mendeteksi dokumen melalui URL<br/> default False
 - `bahasa='english'` digunakan untuk menentukan bahasa yang digunakan dalam proses stopwords<br/> default 'indonesian'
 - `method='Cosine'` digunakan untuk mengubah metode yang ingin digunakan<br/>default 'Rabin Karp', pilihan 'Rabin Karp', 'Cosine', 'Jaccard'
 
+### Referensi
+
+**Rabin Karp**:
+- **Ranti Eka Putri, Andysah Putera Utama Siahaan**<br/>https://www.researchgate.net/publication/319272358_Examination_of_Document_Similarity_Using_Rabin-Karp_Algorithm
+- **Andysah Putera Utama Siahaan, Mesran, Robbi Rahim, Dodi Siregar**<br/>https://www.ijstr.org/final-print/july2017/K-gram-As-A-Determinant-Of-Plagiarism-Level-In-Rabin-karp-Algorithm.pdf
+
+**Jaccard Similarity**:
+- https://en.wikipedia.org/wiki/Jaccard_index
+
+**Cosine Similarity**:
+- **Jiapeng Wang, Yihong Dong**<br/>https://www.researchgate.net/publication/344010599_Measurement_of_Text_Similarity_A_Survey
+
+
 ### Disclaimer
 Library ini di buat hanya untuk keperluan pembuatan tugas Data Science.
 
 Output mungkin saja bisa berbeda dengan pustaka lain khususnya perhitungan Cosine, karena dalam implementasinya ada variasi dalam cara perhitungan vektor TF-IDF, tokenisasi kata, dan faktor-faktor lainnya. Agar hasil lebih maksimal, lebih baik handle dulu masalah stop word, n-gram, dan normalisasi secara mandiri karena perhitungan yang dilakukan dalam pustaka ini hanya melakukan normalisasi sederhana sebelum dieksekusi.
 
 Salam hormat,<br/>
 Novianto Rahmadi (22.55.2293)
```

### Comparing `plagiat-0.1.4/README.md` & `plagiat-0.1.5/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -1,79 +1,81 @@
 # Plagiat
 
-<small>Pustaka ini dibuat hanya sebagai penunjang untuk membantu saya menguji-coba dan memahami semua konsep algoritma untuk menghitung similaritas.</small>
+Library untuk memeriksa tingkat Plagiarisme atau *Similarity* menggunakan Bahasa Python. Secara default library ini akan menggunakan Algoritma Rabin Karp sebagai perhitungan utamanya.
 
-Library untuk memeriksa tingkat Plagiarisme menggunakan Bahasa Python. Secara default library ini akan menggunakan Algoritma Rabin Karp sebagai perhitungan utamanya.
-
-Referensi **Rabin Karp**:
-- **Ranti Eka Putri, Andysah Putera Utama Siahaan**<br/>https://www.researchgate.net/publication/319272358_Examination_of_Document_Similarity_Using_Rabin-Karp_Algorithm
-- **Andysah Putera Utama Siahaan, Mesran, Robbi Rahim, Dodi Siregar**<br/>https://www.ijstr.org/final-print/july2017/K-gram-As-A-Determinant-Of-Plagiarism-Level-In-Rabin-karp-Algorithm.pdf
-
-
-Penambahan Algoritma: 
-
-Referensi **Jaccard Similarity**:
-- https://en.wikipedia.org/wiki/Jaccard_index
-
-Referensi **Cosine Similarity**:
-- **Jiapeng Wang, Yihong Dong**<br/>https://www.researchgate.net/publication/344010599_Measurement_of_Text_Similarity_A_Survey
+Pustaka ini dibuat hanya sebagai penunjang untuk membantu saya menguji-coba dan memahami semua konsep algoritma untuk menghitung similaritas.
 
 ### Instalasi
 ```
 pip install plagiat
 ```
 
-### Menggunakan File .txt
+### Cara Penggunaan
+
+#### Menggunakan File .txt
 ```Python
 from plagiat.deteksi import Deteksi
 
 file_1 = '/content/kalimat-1.txt'
 file_2 = '/content/kalimat-2.txt'
 
 cek = Deteksi(file_1, file_2, url=True).hitung()
 
 print('Persentase plagiarisme = {0}%'.format(cek))
 ```
 
-### Menggunakan Text
+#### Menggunakan Text
 ```Python
 from plagiat.deteksi import Deteksi
 
 string_1 = "Aku sedang belajar kecerdasan buatan"
 string_2 = "Mahasiswa yang cerdas selalu siap menerima tantangan"
 
 cek = Deteksi(string_1, string_2, text=True).hitung()
 
 print('Persentase plagiarisme = {0}%'.format(cek))
 ```
 
-### Menggunakan URL
+#### Menggunakan URL
 ```Python
 from plagiat.deteksi import Deteksi
 
 teks_1 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-1.txt'
 teks_2 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-1.txt'
 
 cek = Deteksi(teks_1, teks_2, url=True).hitung()
 
 print('Persentase plagiarisme = {0}%'.format(cek))
 ```
 
-### Penggunaan Parameter
+#### Penggunaan Parameter
 ```Python
 from plagiat.deteksi import Deteksi
 
 Deteksi(teks_1, teks_2, text=True, url=True, bahasa='english', method='Cosine').hitung()
 ```
 **Penjelasan**<br/>
 - `text=True` digunakan untuk mendeteksi string<br/> default False
 - `url=True` digunakan untuk mendeteksi dokumen melalui URL<br/> default False
 - `bahasa='english'` digunakan untuk menentukan bahasa yang digunakan dalam proses stopwords<br/> default 'indonesian'
 - `method='Cosine'` digunakan untuk mengubah metode yang ingin digunakan<br/>default 'Rabin Karp', pilihan 'Rabin Karp', 'Cosine', 'Jaccard'
 
+### Referensi
+
+**Rabin Karp**:
+- **Ranti Eka Putri, Andysah Putera Utama Siahaan**<br/>https://www.researchgate.net/publication/319272358_Examination_of_Document_Similarity_Using_Rabin-Karp_Algorithm
+- **Andysah Putera Utama Siahaan, Mesran, Robbi Rahim, Dodi Siregar**<br/>https://www.ijstr.org/final-print/july2017/K-gram-As-A-Determinant-Of-Plagiarism-Level-In-Rabin-karp-Algorithm.pdf
+
+**Jaccard Similarity**:
+- https://en.wikipedia.org/wiki/Jaccard_index
+
+**Cosine Similarity**:
+- **Jiapeng Wang, Yihong Dong**<br/>https://www.researchgate.net/publication/344010599_Measurement_of_Text_Similarity_A_Survey
+
+
 ### Disclaimer
 Library ini di buat hanya untuk keperluan pembuatan tugas Data Science.
 
 Output mungkin saja bisa berbeda dengan pustaka lain khususnya perhitungan Cosine, karena dalam implementasinya ada variasi dalam cara perhitungan vektor TF-IDF, tokenisasi kata, dan faktor-faktor lainnya. Agar hasil lebih maksimal, lebih baik handle dulu masalah stop word, n-gram, dan normalisasi secara mandiri karena perhitungan yang dilakukan dalam pustaka ini hanya melakukan normalisasi sederhana sebelum dieksekusi.
 
 Salam hormat,<br/>
 Novianto Rahmadi (22.55.2293)
```

### Comparing `plagiat-0.1.4/plagiat/cosine.py` & `plagiat-0.1.5/plagiat/cosine.py`

 * *Files identical despite different names*

### Comparing `plagiat-0.1.4/plagiat/deteksi.py` & `plagiat-0.1.5/plagiat/deteksi.py`

 * *Files identical despite different names*

### Comparing `plagiat-0.1.4/plagiat/jaccard.py` & `plagiat-0.1.5/plagiat/jaccard.py`

 * *Files identical despite different names*

### Comparing `plagiat-0.1.4/plagiat/rabin_karp.py` & `plagiat-0.1.5/plagiat/rabin_karp.py`

 * *Files identical despite different names*

### Comparing `plagiat-0.1.4/plagiat.egg-info/PKG-INFO` & `plagiat-0.1.5/plagiat.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: plagiat
-Version: 0.1.4
+Version: 0.1.5
 Summary: Library untuk memeriksa tingkat plagiarisme.
 Home-page: https://novay.web.id/
 Author: Novianto Rahmadi
 Author-email: novay@btekno.id
 License: MIT
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
@@ -15,84 +15,86 @@
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Operating System :: OS Independent
 Description-Content-Type: text/markdown
 
 # Plagiat
 
-<small>Pustaka ini dibuat hanya sebagai penunjang untuk membantu saya menguji-coba dan memahami semua konsep algoritma untuk menghitung similaritas.</small>
+Library untuk memeriksa tingkat Plagiarisme atau *Similarity* menggunakan Bahasa Python. Secara default library ini akan menggunakan Algoritma Rabin Karp sebagai perhitungan utamanya.
 
-Library untuk memeriksa tingkat Plagiarisme menggunakan Bahasa Python. Secara default library ini akan menggunakan Algoritma Rabin Karp sebagai perhitungan utamanya.
-
-Referensi **Rabin Karp**:
-- **Ranti Eka Putri, Andysah Putera Utama Siahaan**<br/>https://www.researchgate.net/publication/319272358_Examination_of_Document_Similarity_Using_Rabin-Karp_Algorithm
-- **Andysah Putera Utama Siahaan, Mesran, Robbi Rahim, Dodi Siregar**<br/>https://www.ijstr.org/final-print/july2017/K-gram-As-A-Determinant-Of-Plagiarism-Level-In-Rabin-karp-Algorithm.pdf
-
-
-Penambahan Algoritma: 
-
-Referensi **Jaccard Similarity**:
-- https://en.wikipedia.org/wiki/Jaccard_index
-
-Referensi **Cosine Similarity**:
-- **Jiapeng Wang, Yihong Dong**<br/>https://www.researchgate.net/publication/344010599_Measurement_of_Text_Similarity_A_Survey
+Pustaka ini dibuat hanya sebagai penunjang untuk membantu saya menguji-coba dan memahami semua konsep algoritma untuk menghitung similaritas.
 
 ### Instalasi
 ```
 pip install plagiat
 ```
 
-### Menggunakan File .txt
+### Cara Penggunaan
+
+#### Menggunakan File .txt
 ```Python
 from plagiat.deteksi import Deteksi
 
 file_1 = '/content/kalimat-1.txt'
 file_2 = '/content/kalimat-2.txt'
 
 cek = Deteksi(file_1, file_2, url=True).hitung()
 
 print('Persentase plagiarisme = {0}%'.format(cek))
 ```
 
-### Menggunakan Text
+#### Menggunakan Text
 ```Python
 from plagiat.deteksi import Deteksi
 
 string_1 = "Aku sedang belajar kecerdasan buatan"
 string_2 = "Mahasiswa yang cerdas selalu siap menerima tantangan"
 
 cek = Deteksi(string_1, string_2, text=True).hitung()
 
 print('Persentase plagiarisme = {0}%'.format(cek))
 ```
 
-### Menggunakan URL
+#### Menggunakan URL
 ```Python
 from plagiat.deteksi import Deteksi
 
 teks_1 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-1.txt'
 teks_2 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-1.txt'
 
 cek = Deteksi(teks_1, teks_2, url=True).hitung()
 
 print('Persentase plagiarisme = {0}%'.format(cek))
 ```
 
-### Penggunaan Parameter
+#### Penggunaan Parameter
 ```Python
 from plagiat.deteksi import Deteksi
 
 Deteksi(teks_1, teks_2, text=True, url=True, bahasa='english', method='Cosine').hitung()
 ```
 **Penjelasan**<br/>
 - `text=True` digunakan untuk mendeteksi string<br/> default False
 - `url=True` digunakan untuk mendeteksi dokumen melalui URL<br/> default False
 - `bahasa='english'` digunakan untuk menentukan bahasa yang digunakan dalam proses stopwords<br/> default 'indonesian'
 - `method='Cosine'` digunakan untuk mengubah metode yang ingin digunakan<br/>default 'Rabin Karp', pilihan 'Rabin Karp', 'Cosine', 'Jaccard'
 
+### Referensi
+
+**Rabin Karp**:
+- **Ranti Eka Putri, Andysah Putera Utama Siahaan**<br/>https://www.researchgate.net/publication/319272358_Examination_of_Document_Similarity_Using_Rabin-Karp_Algorithm
+- **Andysah Putera Utama Siahaan, Mesran, Robbi Rahim, Dodi Siregar**<br/>https://www.ijstr.org/final-print/july2017/K-gram-As-A-Determinant-Of-Plagiarism-Level-In-Rabin-karp-Algorithm.pdf
+
+**Jaccard Similarity**:
+- https://en.wikipedia.org/wiki/Jaccard_index
+
+**Cosine Similarity**:
+- **Jiapeng Wang, Yihong Dong**<br/>https://www.researchgate.net/publication/344010599_Measurement_of_Text_Similarity_A_Survey
+
+
 ### Disclaimer
 Library ini di buat hanya untuk keperluan pembuatan tugas Data Science.
 
 Output mungkin saja bisa berbeda dengan pustaka lain khususnya perhitungan Cosine, karena dalam implementasinya ada variasi dalam cara perhitungan vektor TF-IDF, tokenisasi kata, dan faktor-faktor lainnya. Agar hasil lebih maksimal, lebih baik handle dulu masalah stop word, n-gram, dan normalisasi secara mandiri karena perhitungan yang dilakukan dalam pustaka ini hanya melakukan normalisasi sederhana sebelum dieksekusi.
 
 Salam hormat,<br/>
 Novianto Rahmadi (22.55.2293)
```

### Comparing `plagiat-0.1.4/setup.py` & `plagiat-0.1.5/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 HERE = path.abspath(path.dirname(__file__))
 
 with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
     long_description = f.read()
     
 setup(
     name="plagiat",
-    version="0.1.4",
+    version="0.1.5",
     description="Library untuk memeriksa tingkat plagiarisme.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://novay.web.id/",
     author="Novianto Rahmadi",
     author_email="novay@btekno.id",
     license="MIT",
```

