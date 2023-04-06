# Comparing `tmp/ifd_python-2.4.2.tar.gz` & `tmp/ifd_python-2.4.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ifd_python-2.4.2.tar", max compression
+gzip compressed data, was "ifd_python-2.4.5.tar", max compression
```

## Comparing `ifd_python-2.4.2.tar` & `ifd_python-2.4.5.tar`

### file list

```diff
@@ -1,27 +1,27 @@
--rw-r--r--   0        0        0     1093 2023-03-21 11:14:02.424248 ifd_python-2.4.2/LICENSE
--rw-r--r--   0        0        0      551 2023-03-23 09:54:10.672476 ifd_python-2.4.2/README.md
--rw-r--r--   0        0        0      283 2023-03-21 11:14:02.428248 ifd_python-2.4.2/ifd/__init__.py
--rw-r--r--   0        0        0      971 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/entities/Abstract/ADetection.py
--rw-r--r--   0        0        0       34 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/entities/Abstract/__init__.py
--rw-r--r--   0        0        0      673 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/entities/Classification.py
--rw-r--r--   0        0        0      228 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/entities/Couleur.py
--rw-r--r--   0        0        0      646 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/entities/Detection.py
--rw-r--r--   0        0        0     2089 2023-04-04 14:32:29.580891 ifd_python-2.4.2/ifd/entities/Image.py
--rw-r--r--   0        0        0     1453 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/entities/LogResult.py
--rw-r--r--   0        0        0      416 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/entities/Modele.py
--rw-r--r--   0        0        0      741 2023-04-04 14:38:21.342011 ifd_python-2.4.2/ifd/entities/OCR.py
--rw-r--r--   0        0        0      517 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/entities/RabbitMqMessage.py
--rw-r--r--   0        0        0      208 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/entities/__init__.py
--rw-r--r--   0        0        0      656 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/entities/bbox.py
--rw-r--r--   0        0        0     2162 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/repository/AmqpImageRepository.py
--rw-r--r--   0        0        0       88 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/repository/Interfaces/IImageRepository.py
--rw-r--r--   0        0        0       46 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/repository/Interfaces/__init__.py
--rw-r--r--   0        0        0      192 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/repository/MemoryImageRepository.py
--rw-r--r--   0        0        0      110 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/repository/__init__.py
--rw-r--r--   0        0        0      711 2023-04-05 07:56:47.943467 ifd_python-2.4.2/ifd/spec.py
--rw-r--r--   0        0        0      558 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/tools.py
--rw-r--r--   0        0        0       77 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/usecase/Interfaces/IFonction.py
--rw-r--r--   0        0        0       32 2023-03-23 09:54:10.672476 ifd_python-2.4.2/ifd/usecase/Interfaces/__init__.py
--rw-r--r--   0        0        0        0 2023-04-05 07:57:04.711259 ifd_python-2.4.2/ifd/usecase/__init__.py
--rw-r--r--   0        0        0      329 2023-04-05 07:57:15.111130 ifd_python-2.4.2/pyproject.toml
--rw-r--r--   0        0        0     1086 1970-01-01 00:00:00.000000 ifd_python-2.4.2/PKG-INFO
+-rw-r--r--   0        0        0     1093 2023-04-06 13:07:39.902629 ifd_python-2.4.5/LICENSE
+-rw-r--r--   0        0        0      551 2023-04-06 13:07:39.902629 ifd_python-2.4.5/README.md
+-rw-r--r--   0        0        0      283 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/__init__.py
+-rw-r--r--   0        0        0      971 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/entities/Abstract/ADetection.py
+-rw-r--r--   0        0        0       34 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/entities/Abstract/__init__.py
+-rw-r--r--   0        0        0      673 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/entities/Classification.py
+-rw-r--r--   0        0        0      228 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/entities/Couleur.py
+-rw-r--r--   0        0        0      646 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/entities/Detection.py
+-rw-r--r--   0        0        0     2089 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/entities/Image.py
+-rw-r--r--   0        0        0     1453 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/entities/LogResult.py
+-rw-r--r--   0        0        0      416 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/entities/Modele.py
+-rw-r--r--   0        0        0      741 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/entities/OCR.py
+-rw-r--r--   0        0        0      517 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/entities/RabbitMqMessage.py
+-rw-r--r--   0        0        0      208 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/entities/__init__.py
+-rw-r--r--   0        0        0      656 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/entities/bbox.py
+-rw-r--r--   0        0        0     2162 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/repository/AmqpImageRepository.py
+-rw-r--r--   0        0        0       88 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/repository/Interfaces/IImageRepository.py
+-rw-r--r--   0        0        0       46 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/repository/Interfaces/__init__.py
+-rw-r--r--   0        0        0      192 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/repository/MemoryImageRepository.py
+-rw-r--r--   0        0        0      110 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/repository/__init__.py
+-rw-r--r--   0        0        0      639 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/spec.py
+-rw-r--r--   0        0        0      558 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/tools.py
+-rw-r--r--   0        0        0       77 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/usecase/Interfaces/IFonction.py
+-rw-r--r--   0        0        0       32 2023-04-06 13:07:39.902629 ifd_python-2.4.5/ifd/usecase/Interfaces/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 14:24:33.421203 ifd_python-2.4.5/ifd/usecase/__init__.py
+-rw-r--r--   0        0        0      329 2023-04-06 14:24:42.573071 ifd_python-2.4.5/pyproject.toml
+-rw-r--r--   0        0        0     1086 1970-01-01 00:00:00.000000 ifd_python-2.4.5/PKG-INFO
```

### Comparing `ifd_python-2.4.2/LICENSE` & `ifd_python-2.4.5/LICENSE`

 * *Files identical despite different names*

### Comparing `ifd_python-2.4.2/README.md` & `ifd_python-2.4.5/README.md`

 * *Files identical despite different names*

### Comparing `ifd_python-2.4.2/ifd/entities/Abstract/ADetection.py` & `ifd_python-2.4.5/ifd/entities/Abstract/ADetection.py`

 * *Files identical despite different names*

### Comparing `ifd_python-2.4.2/ifd/entities/Classification.py` & `ifd_python-2.4.5/ifd/entities/Classification.py`

 * *Files identical despite different names*

### Comparing `ifd_python-2.4.2/ifd/entities/Detection.py` & `ifd_python-2.4.5/ifd/entities/Detection.py`

 * *Files identical despite different names*

### Comparing `ifd_python-2.4.2/ifd/entities/Image.py` & `ifd_python-2.4.5/ifd/entities/Image.py`

 * *Files identical despite different names*

### Comparing `ifd_python-2.4.2/ifd/entities/LogResult.py` & `ifd_python-2.4.5/ifd/entities/LogResult.py`

 * *Files identical despite different names*

### Comparing `ifd_python-2.4.2/ifd/entities/OCR.py` & `ifd_python-2.4.5/ifd/entities/OCR.py`

 * *Files identical despite different names*

### Comparing `ifd_python-2.4.2/ifd/entities/RabbitMqMessage.py` & `ifd_python-2.4.5/ifd/entities/RabbitMqMessage.py`

 * *Files identical despite different names*

### Comparing `ifd_python-2.4.2/ifd/entities/bbox.py` & `ifd_python-2.4.5/ifd/entities/bbox.py`

 * *Files identical despite different names*

### Comparing `ifd_python-2.4.2/ifd/repository/AmqpImageRepository.py` & `ifd_python-2.4.5/ifd/repository/AmqpImageRepository.py`

 * *Files identical despite different names*

### Comparing `ifd_python-2.4.2/ifd/tools.py` & `ifd_python-2.4.5/ifd/tools.py`

 * *Files identical despite different names*

### Comparing `ifd_python-2.4.2/PKG-INFO` & `ifd_python-2.4.5/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ifd-python
-Version: 2.4.2
+Version: 2.4.5
 Summary: 
 Author: Antonin Lemoine
 Author-email: antonin.lemoine@altitudeinfra.fr
 Requires-Python: >=3.6,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
```

