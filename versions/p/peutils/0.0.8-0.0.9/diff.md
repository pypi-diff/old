# Comparing `tmp/peutils-0.0.8.tar.gz` & `tmp/peutils-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/peutils-0.0.8.tar", last modified: Mon Aug  9 08:19:53 2021, max compression
+gzip compressed data, was "dist/peutils-0.0.9.tar", last modified: Sat Sep 18 05:17:34 2021, max compression
```

## Comparing `peutils-0.0.8.tar` & `peutils-0.0.9.tar`

### file list

```diff
@@ -1,20 +1,25 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-08-09 08:19:53.000000 peutils-0.0.8/
--rw-r--r--   0 root         (0) root         (0)      358 2021-08-09 08:19:53.000000 peutils-0.0.8/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)       19 2021-08-09 08:19:43.000000 peutils-0.0.8/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-08-09 08:19:53.000000 peutils-0.0.8/peutils/
--rw-r--r--   0 root         (0) root         (0)     8441 2021-08-09 08:19:43.000000 peutils-0.0.8/peutils/comutil.py
--rw-r--r--   0 root         (0) root         (0)     5960 2021-08-09 08:19:43.000000 peutils-0.0.8/peutils/fileutil.py
--rw-r--r--   0 root         (0) root         (0)      114 2021-08-09 08:19:43.000000 peutils-0.0.8/peutils/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1443 2021-08-09 08:19:43.000000 peutils-0.0.8/peutils/datautil.py
--rw-r--r--   0 root         (0) root         (0)        0 2021-08-09 08:19:43.000000 peutils-0.0.8/peutils/gooeyutil.py
--rw-r--r--   0 root         (0) root         (0)    30281 2021-08-09 08:19:43.000000 peutils-0.0.8/peutils/pcd_py3.py
--rw-r--r--   0 root         (0) root         (0)     4647 2021-08-09 08:19:43.000000 peutils-0.0.8/peutils/image_util.py
--rw-r--r--   0 root         (0) root         (0)     5883 2021-08-09 08:19:43.000000 peutils-0.0.8/peutils/wooeyutil.py
--rw-r--r--   0 root         (0) root         (0)     1096 2021-08-09 08:19:43.000000 peutils-0.0.8/peutils/textutil.py
--rw-r--r--   0 root         (0) root         (0)      699 2021-08-09 08:19:43.000000 peutils-0.0.8/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-08-09 08:19:53.000000 peutils-0.0.8/peutils.egg-info/
--rw-r--r--   0 root         (0) root         (0)        8 2021-08-09 08:19:52.000000 peutils-0.0.8/peutils.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)      358 2021-08-09 08:19:52.000000 peutils-0.0.8/peutils.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      324 2021-08-09 08:19:53.000000 peutils-0.0.8/peutils.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2021-08-09 08:19:52.000000 peutils-0.0.8/peutils.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       38 2021-08-09 08:19:53.000000 peutils-0.0.8/setup.cfg
+drwxr-sr-x   0 root         (0)     1000        0 2021-09-18 05:17:34.000000 peutils-0.0.9/
+-rw-r--r--   0 root         (0)     1000      358 2021-09-18 05:17:34.000000 peutils-0.0.9/PKG-INFO
+-rw-r--r--   0 root         (0)     1000       19 2021-09-18 05:15:04.000000 peutils-0.0.9/README.md
+drwxr-sr-x   0 root         (0)     1000        0 2021-09-18 05:17:34.000000 peutils-0.0.9/peutils/
+-rw-r--r--   0 root         (0)     1000      694 2021-09-18 05:15:04.000000 peutils-0.0.9/peutils/toolutil.py
+-rw-r--r--   0 root         (0)     1000     8441 2021-09-18 05:15:04.000000 peutils-0.0.9/peutils/comutil.py
+-rw-r--r--   0 root         (0)     1000     5960 2021-09-18 05:15:04.000000 peutils-0.0.9/peutils/fileutil.py
+-rw-r--r--   0 root         (0)     1000      114 2021-09-18 05:15:04.000000 peutils-0.0.9/peutils/__init__.py
+-rw-r--r--   0 root         (0)     1000     1443 2021-09-18 05:15:04.000000 peutils-0.0.9/peutils/datautil.py
+drwxr-sr-x   0 root         (0)     1000        0 2021-09-18 05:17:34.000000 peutils-0.0.9/peutils/process/
+-rw-r--r--   0 root         (0)     1000        0 2021-09-18 05:15:04.000000 peutils-0.0.9/peutils/process/__init__.py
+drwxr-sr-x   0 root         (0)     1000        0 2021-09-18 05:17:34.000000 peutils-0.0.9/peutils/process/v1/
+-rw-r--r--   0 root         (0)     1000     6970 2021-09-18 05:15:04.000000 peutils-0.0.9/peutils/process/v1/__init__.py
+-rw-r--r--   0 root         (0)     1000        0 2021-09-18 05:15:04.000000 peutils-0.0.9/peutils/gooeyutil.py
+-rw-r--r--   0 root         (0)     1000    30655 2021-09-18 05:15:04.000000 peutils-0.0.9/peutils/pcd_py3.py
+-rw-r--r--   0 root         (0)     1000     4647 2021-09-18 05:15:04.000000 peutils-0.0.9/peutils/image_util.py
+-rw-r--r--   0 root         (0)     1000     5883 2021-09-18 05:15:04.000000 peutils-0.0.9/peutils/wooeyutil.py
+-rw-r--r--   0 root         (0)     1000     1096 2021-09-18 05:15:04.000000 peutils-0.0.9/peutils/textutil.py
+-rw-r--r--   0 root         (0)     1000      699 2021-09-18 05:15:04.000000 peutils-0.0.9/setup.py
+drwxr-sr-x   0 root         (0)     1000        0 2021-09-18 05:17:34.000000 peutils-0.0.9/peutils.egg-info/
+-rw-r--r--   0 root         (0)     1000        8 2021-09-18 05:17:34.000000 peutils-0.0.9/peutils.egg-info/top_level.txt
+-rw-r--r--   0 root         (0)     1000      358 2021-09-18 05:17:34.000000 peutils-0.0.9/peutils.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0)     1000      403 2021-09-18 05:17:34.000000 peutils-0.0.9/peutils.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0)     1000        1 2021-09-18 05:17:34.000000 peutils-0.0.9/peutils.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0)     1000       38 2021-09-18 05:17:34.000000 peutils-0.0.9/setup.cfg
```

### Comparing `peutils-0.0.8/peutils/comutil.py` & `peutils-0.0.9/peutils/comutil.py`

 * *Files identical despite different names*

### Comparing `peutils-0.0.8/peutils/fileutil.py` & `peutils-0.0.9/peutils/fileutil.py`

 * *Files identical despite different names*

### Comparing `peutils-0.0.8/peutils/datautil.py` & `peutils-0.0.9/peutils/datautil.py`

 * *Files identical despite different names*

### Comparing `peutils-0.0.8/peutils/pcd_py3.py` & `peutils-0.0.9/peutils/pcd_py3.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,19 +1,12 @@
 # -*- coding: utf-8 -*-
 # @Author : Thomas
 # @File : pcd_py3.py
-# @CreateTime : 2021/6/23 10:31 上午
-# @Project: 
-# @Description :
-
-# -*- coding: utf-8 -*-
-# @Author : Thomas
-# @File : pcd_py3.py
 # @CreateTime : 2021/6/4 11:51 上午
-# @Project:
+# @Project: 
 # @Description :
 
 """
 Read and write PCL .pcd files in python.
 dimatura@cmu.edu, 2013-2018
 - TODO better API for wacky operations.
 - TODO add a cli for common operations.
@@ -285,24 +278,36 @@
     compressed_data = f.read(compressed_size)
     # TODO what to use as second argument? if buf is None
     # (compressed > uncompressed)
     # should we read buf as raw binary?
     buf = lzf.decompress(compressed_data, uncompressed_size)
     if len(buf) != uncompressed_size:
         raise IOError('Error decompressing data')
+
+    # modify by thomas for mulit height start
     # the data is stored field-by-field
-    pc_data = np.zeros(metadata['width'], dtype=dtype)
+    # pc_data = np.zeros(metadata['width'], dtype=dtype)
+    # ix = 0
+    # for dti in range(len(dtype)):
+    #     dt = dtype[dti]
+    #     bytes = dt.itemsize * metadata['width']
+    #     column = np.fromstring(buf[ix:(ix+bytes)], dt)
+    #     pc_data[dtype.names[dti]] = column
+    #     ix += bytes
+    # return pc_data
+    pc_data = np.zeros(metadata['width']*metadata['height'], dtype=dtype)
     ix = 0
     for dti in range(len(dtype)):
         dt = dtype[dti]
-        bytes = dt.itemsize * metadata['width']
+        bytes = dt.itemsize * metadata['width'] * metadata['height']
         column = np.fromstring(buf[ix:(ix+bytes)], dt)
         pc_data[dtype.names[dti]] = column
         ix += bytes
     return pc_data
+    # modify by thomas for mulit height end
 
 
 def point_cloud_from_fileobj(f):
     """ Parse pointcloud coming from file object f
     """
     header = []
     while True:
@@ -700,15 +705,15 @@
             metadata[k] = copy.copy(getattr(self, k))
         return metadata
 
     def check_sanity(self):
         # pdb.set_trace()
         md = self.get_metadata()
         assert(_metadata_is_consistent(md))
-        assert(len(self.pc_data) == self.points)
+        assert(len(self.pc_data) == self.points), "{}, {}".format(len(self.pc_data), self.points)
         assert(self.width*self.height == self.points)
         assert(len(self.fields) == len(self.count))
         assert(len(self.fields) == len(self.type))
 
 #     def save(self, fname):
 #         self.save_pcd(fname, 'ascii')
 #
```

### Comparing `peutils-0.0.8/peutils/image_util.py` & `peutils-0.0.9/peutils/image_util.py`

 * *Files identical despite different names*

### Comparing `peutils-0.0.8/peutils/wooeyutil.py` & `peutils-0.0.9/peutils/wooeyutil.py`

 * *Files identical despite different names*

### Comparing `peutils-0.0.8/peutils/textutil.py` & `peutils-0.0.9/peutils/textutil.py`

 * *Files identical despite different names*

### Comparing `peutils-0.0.8/setup.py` & `peutils-0.0.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 
 from setuptools import setup, find_packages
 
 
 
 setup(
     name = "peutils",
-    version = '0.0.8',
+    version = '0.0.9',
     keywords = ("pip3", "peutils",'henry'),
     description = "utils for text,audio,video,excel,file and so on.",
     long_description = "utils for text,audio,video,excel,file and so on,more details please visit gitlab.",
     license = "MIT Licence",
     url = "https://github.com/yunsansheng/peutils",
     author = "henry.wang",
     author_email = "shanandone@qq.com",
```

