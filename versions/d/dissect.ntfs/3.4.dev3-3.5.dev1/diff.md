# Comparing `tmp/dissect.ntfs-3.4.dev3.tar.gz` & `tmp/dissect.ntfs-3.5.dev1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dissect.ntfs-3.4.dev3.tar", last modified: Thu Mar 16 13:04:12 2023, max compression
+gzip compressed data, was "dissect.ntfs-3.5.dev1.tar", last modified: Thu Apr  6 22:09:20 2023, max compression
```

## Comparing `dissect.ntfs-3.4.dev3.tar` & `dissect.ntfs-3.5.dev1.tar`

### file list

```diff
@@ -1,44 +1,44 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 13:04:12.171513 dissect.ntfs-3.4.dev3/
--rw-r--r--   0 runner    (1001) docker     (123)      299 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/COPYRIGHT
--rw-r--r--   0 runner    (1001) docker     (123)    34523 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       48 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2307 2023-03-16 13:04:12.171513 dissect.ntfs-3.4.dev3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1693 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 13:04:12.151512 dissect.ntfs-3.4.dev3/dissect/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 13:04:12.163512 dissect.ntfs-3.4.dev3/dissect/ntfs/
--rw-r--r--   0 runner    (1001) docker     (123)      683 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/dissect/ntfs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    17453 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/dissect/ntfs/attr.py
--rw-r--r--   0 runner    (1001) docker     (123)    19726 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/dissect/ntfs/c_ntfs.py
--rw-r--r--   0 runner    (1001) docker     (123)      395 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/dissect/ntfs/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    12058 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/dissect/ntfs/index.py
--rw-r--r--   0 runner    (1001) docker     (123)    16517 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/dissect/ntfs/mft.py
--rw-r--r--   0 runner    (1001) docker     (123)     6709 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/dissect/ntfs/ntfs.py
--rw-r--r--   0 runner    (1001) docker     (123)     7224 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/dissect/ntfs/secure.py
--rw-r--r--   0 runner    (1001) docker     (123)     4118 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/dissect/ntfs/stream.py
--rw-r--r--   0 runner    (1001) docker     (123)     4703 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/dissect/ntfs/usnjrnl.py
--rw-r--r--   0 runner    (1001) docker     (123)     9402 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/dissect/ntfs/util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 13:04:12.159512 dissect.ntfs-3.4.dev3/dissect.ntfs.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2307 2023-03-16 13:04:12.000000 dissect.ntfs-3.4.dev3/dissect.ntfs.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      796 2023-03-16 13:04:12.000000 dissect.ntfs-3.4.dev3/dissect.ntfs.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-16 13:04:12.000000 dissect.ntfs-3.4.dev3/dissect.ntfs.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       65 2023-03-16 13:04:12.000000 dissect.ntfs-3.4.dev3/dissect.ntfs.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        8 2023-03-16 13:04:12.000000 dissect.ntfs-3.4.dev3/dissect.ntfs.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1106 2023-03-16 13:04:02.000000 dissect.ntfs-3.4.dev3/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-16 13:04:12.171513 dissect.ntfs-3.4.dev3/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 13:04:12.167513 dissect.ntfs-3.4.dev3/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1369 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/tests/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 13:04:12.171513 dissect.ntfs-3.4.dev3/tests/data/
--rw-r--r--   0 runner    (1001) docker     (123)     5647 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/tests/data/boot_2m.bin.gz
--rw-r--r--   0 runner    (1001) docker     (123)     4290 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/tests/data/mft.bin.gz
--rw-r--r--   0 runner    (1001) docker     (123)   908628 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/tests/data/ntfs.bin.gz
--rw-r--r--   0 runner    (1001) docker     (123)     3999 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/tests/data/ntfs_fragmented_mft.csv.gz
--rw-r--r--   0 runner    (1001) docker     (123)     1243 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/tests/data/sds.bin.gz
--rw-r--r--   0 runner    (1001) docker     (123)     4528 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/tests/test_attr.py
--rw-r--r--   0 runner    (1001) docker     (123)     1977 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/tests/test_index.py
--rw-r--r--   0 runner    (1001) docker     (123)     3549 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/tests/test_mft.py
--rw-r--r--   0 runner    (1001) docker     (123)     1768 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/tests/test_ntfs.py
--rw-r--r--   0 runner    (1001) docker     (123)      976 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/tests/test_secure.py
--rw-r--r--   0 runner    (1001) docker     (123)      932 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/tests/test_usnjrnl.py
--rw-r--r--   0 runner    (1001) docker     (123)     2000 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/tests/test_util.py
--rw-r--r--   0 runner    (1001) docker     (123)     1364 2023-03-16 13:03:56.000000 dissect.ntfs-3.4.dev3/tox.ini
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:09:20.383600 dissect.ntfs-3.5.dev1/
+-rw-r--r--   0 runner    (1001) docker     (123)      299 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/COPYRIGHT
+-rw-r--r--   0 runner    (1001) docker     (123)    34523 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       48 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2307 2023-04-06 22:09:20.383600 dissect.ntfs-3.5.dev1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1693 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:09:20.375599 dissect.ntfs-3.5.dev1/dissect/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:09:20.379600 dissect.ntfs-3.5.dev1/dissect/ntfs/
+-rw-r--r--   0 runner    (1001) docker     (123)      683 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/dissect/ntfs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17453 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/dissect/ntfs/attr.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19726 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/dissect/ntfs/c_ntfs.py
+-rw-r--r--   0 runner    (1001) docker     (123)      395 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/dissect/ntfs/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12058 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/dissect/ntfs/index.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16517 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/dissect/ntfs/mft.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6726 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/dissect/ntfs/ntfs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7224 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/dissect/ntfs/secure.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4118 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/dissect/ntfs/stream.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4703 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/dissect/ntfs/usnjrnl.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9402 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/dissect/ntfs/util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:09:20.375599 dissect.ntfs-3.5.dev1/dissect.ntfs.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2307 2023-04-06 22:09:20.000000 dissect.ntfs-3.5.dev1/dissect.ntfs.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      796 2023-04-06 22:09:20.000000 dissect.ntfs-3.5.dev1/dissect.ntfs.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 22:09:20.000000 dissect.ntfs-3.5.dev1/dissect.ntfs.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       65 2023-04-06 22:09:20.000000 dissect.ntfs-3.5.dev1/dissect.ntfs.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-06 22:09:20.000000 dissect.ntfs-3.5.dev1/dissect.ntfs.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1106 2023-04-06 22:09:08.000000 dissect.ntfs-3.5.dev1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 22:09:20.383600 dissect.ntfs-3.5.dev1/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:09:20.379600 dissect.ntfs-3.5.dev1/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1369 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/tests/conftest.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:09:20.383600 dissect.ntfs-3.5.dev1/tests/data/
+-rw-r--r--   0 runner    (1001) docker     (123)     5647 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/tests/data/boot_2m.bin.gz
+-rw-r--r--   0 runner    (1001) docker     (123)     4290 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/tests/data/mft.bin.gz
+-rw-r--r--   0 runner    (1001) docker     (123)   908628 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/tests/data/ntfs.bin.gz
+-rw-r--r--   0 runner    (1001) docker     (123)     3999 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/tests/data/ntfs_fragmented_mft.csv.gz
+-rw-r--r--   0 runner    (1001) docker     (123)     1243 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/tests/data/sds.bin.gz
+-rw-r--r--   0 runner    (1001) docker     (123)     4528 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/tests/test_attr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1977 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/tests/test_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3549 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/tests/test_mft.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3051 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/tests/test_ntfs.py
+-rw-r--r--   0 runner    (1001) docker     (123)      976 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/tests/test_secure.py
+-rw-r--r--   0 runner    (1001) docker     (123)      932 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/tests/test_usnjrnl.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2000 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/tests/test_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1364 2023-04-06 22:09:03.000000 dissect.ntfs-3.5.dev1/tox.ini
```

### Comparing `dissect.ntfs-3.4.dev3/LICENSE` & `dissect.ntfs-3.5.dev1/LICENSE`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/PKG-INFO` & `dissect.ntfs-3.5.dev1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dissect.ntfs
-Version: 3.4.dev3
+Version: 3.5.dev1
 Summary: A Dissect module implementing a parser for the NTFS file system, used by the Windows operating system
 Author-email: Dissect Team <dissect@fox-it.com>
 License: Affero General Public License v3
 Project-URL: homepage, https://dissect.tools
 Project-URL: documentation, https://docs.dissect.tools/en/latest/projects/dissect.ntfs
 Project-URL: repository, https://github.com/fox-it/dissect.ntfs
 Classifier: Programming Language :: Python :: 3
```

### Comparing `dissect.ntfs-3.4.dev3/README.md` & `dissect.ntfs-3.5.dev1/README.md`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/dissect/ntfs/__init__.py` & `dissect.ntfs-3.5.dev1/dissect/ntfs/__init__.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/dissect/ntfs/attr.py` & `dissect.ntfs-3.5.dev1/dissect/ntfs/attr.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/dissect/ntfs/c_ntfs.py` & `dissect.ntfs-3.5.dev1/dissect/ntfs/c_ntfs.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/dissect/ntfs/index.py` & `dissect.ntfs-3.5.dev1/dissect/ntfs/index.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/dissect/ntfs/mft.py` & `dissect.ntfs-3.5.dev1/dissect/ntfs/mft.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/dissect/ntfs/ntfs.py` & `dissect.ntfs-3.5.dev1/dissect/ntfs/ntfs.py`

 * *Files 2% similar despite different names*

```diff
@@ -49,18 +49,18 @@
             boot_fh.seek(0)
             self.boot_sector = c_ntfs.BOOT_SECTOR(boot_fh)
 
             if self.boot_sector.Oem != NTFS_SIGNATURE:
                 raise Error(f"Invalid NTFS magic: {self.boot_sector.Oem}")
 
             self.sector_size = self.boot_sector.Bpb.BytesPerSector
-            if self.boot_sector.Bpb.SectorsPerCluster < 0:
+            if self.boot_sector.Bpb.SectorsPerCluster & 0xFF > 0x80:
                 sectors_per_cluster = 1 << (-self.boot_sector.Bpb.SectorsPerCluster)
             else:
-                sectors_per_cluster = self.boot_sector.Bpb.SectorsPerCluster
+                sectors_per_cluster = self.boot_sector.Bpb.SectorsPerCluster & 0xFF
             self.cluster_size = sectors_per_cluster * self.sector_size
 
             if self.boot_sector.ClustersPerFileRecordSegment < 0:
                 self._record_size = 1 << (-self.boot_sector.ClustersPerFileRecordSegment)
             else:
                 self._record_size = self.boot_sector.ClustersPerFileRecordSegment * self.cluster_size
```

### Comparing `dissect.ntfs-3.4.dev3/dissect/ntfs/secure.py` & `dissect.ntfs-3.5.dev1/dissect/ntfs/secure.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/dissect/ntfs/stream.py` & `dissect.ntfs-3.5.dev1/dissect/ntfs/stream.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/dissect/ntfs/usnjrnl.py` & `dissect.ntfs-3.5.dev1/dissect/ntfs/usnjrnl.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/dissect/ntfs/util.py` & `dissect.ntfs-3.5.dev1/dissect/ntfs/util.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/dissect.ntfs.egg-info/PKG-INFO` & `dissect.ntfs-3.5.dev1/dissect.ntfs.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dissect.ntfs
-Version: 3.4.dev3
+Version: 3.5.dev1
 Summary: A Dissect module implementing a parser for the NTFS file system, used by the Windows operating system
 Author-email: Dissect Team <dissect@fox-it.com>
 License: Affero General Public License v3
 Project-URL: homepage, https://dissect.tools
 Project-URL: documentation, https://docs.dissect.tools/en/latest/projects/dissect.ntfs
 Project-URL: repository, https://github.com/fox-it/dissect.ntfs
 Classifier: Programming Language :: Python :: 3
```

### Comparing `dissect.ntfs-3.4.dev3/dissect.ntfs.egg-info/SOURCES.txt` & `dissect.ntfs-3.5.dev1/dissect.ntfs.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/pyproject.toml` & `dissect.ntfs-3.5.dev1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/tests/conftest.py` & `dissect.ntfs-3.5.dev1/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/tests/data/boot_2m.bin.gz` & `dissect.ntfs-3.5.dev1/tests/data/boot_2m.bin.gz`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/tests/data/mft.bin.gz` & `dissect.ntfs-3.5.dev1/tests/data/mft.bin.gz`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/tests/data/ntfs.bin.gz` & `dissect.ntfs-3.5.dev1/tests/data/ntfs.bin.gz`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/tests/data/ntfs_fragmented_mft.csv.gz` & `dissect.ntfs-3.5.dev1/tests/data/ntfs_fragmented_mft.csv.gz`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/tests/data/sds.bin.gz` & `dissect.ntfs-3.5.dev1/tests/data/sds.bin.gz`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/tests/test_attr.py` & `dissect.ntfs-3.5.dev1/tests/test_attr.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/tests/test_index.py` & `dissect.ntfs-3.5.dev1/tests/test_index.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/tests/test_mft.py` & `dissect.ntfs-3.5.dev1/tests/test_mft.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/tests/test_secure.py` & `dissect.ntfs-3.5.dev1/tests/test_secure.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/tests/test_usnjrnl.py` & `dissect.ntfs-3.5.dev1/tests/test_usnjrnl.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/tests/test_util.py` & `dissect.ntfs-3.5.dev1/tests/test_util.py`

 * *Files identical despite different names*

### Comparing `dissect.ntfs-3.4.dev3/tox.ini` & `dissect.ntfs-3.5.dev1/tox.ini`

 * *Files identical despite different names*

