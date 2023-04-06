# Comparing `tmp/leuci-pol-0.0.8.tar.gz` & `tmp/leuci-pol-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "leuci-pol-0.0.8.tar", last modified: Wed Mar  1 12:43:47 2023, max compression
+gzip compressed data, was "leuci-pol-0.0.9.tar", last modified: Sun Mar  5 20:45:10 2023, max compression
```

## Comparing `leuci-pol-0.0.8.tar` & `leuci-pol-0.0.9.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-01 12:43:47.691494 leuci-pol-0.0.8/
--rw-r--r--   0 rachel    (1000) rachel    (1000)    35149 2023-02-26 19:14:17.000000 leuci-pol-0.0.8/LICENSE
--rw-r--r--   0 rachel    (1000) rachel    (1000)      869 2023-03-01 12:43:47.691494 leuci-pol-0.0.8/PKG-INFO
--rw-r--r--   0 rachel    (1000) rachel    (1000)      369 2023-02-27 15:49:40.000000 leuci-pol-0.0.8/README.md
--rw-r--r--   0 rachel    (1000) rachel    (1000)      104 2023-02-09 09:20:26.000000 leuci-pol-0.0.8/pyproject.toml
--rw-r--r--   0 rachel    (1000) rachel    (1000)      625 2023-03-01 12:43:47.691494 leuci-pol-0.0.8/setup.cfg
-drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-01 12:43:47.671494 leuci-pol-0.0.8/src/
-drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-01 12:43:47.691494 leuci-pol-0.0.8/src/leuci_pol/
--rw-r--r--   0 rachel    (1000) rachel    (1000)        0 2023-02-09 09:20:26.000000 leuci-pol-0.0.8/src/leuci_pol/__init__.py
--rw-r--r--   0 rachel    (1000) rachel    (1000)    57308 2023-03-01 12:42:03.000000 leuci-pol-0.0.8/src/leuci_pol/interpolator.py
--rw-r--r--   0 rachel    (1000) rachel    (1000)   160189 2023-03-01 12:25:50.000000 leuci-pol-0.0.8/src/leuci_pol/invariant.py
-drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-01 12:43:47.691494 leuci-pol-0.0.8/src/leuci_pol.egg-info/
--rw-r--r--   0 rachel    (1000) rachel    (1000)      869 2023-03-01 12:43:47.000000 leuci-pol-0.0.8/src/leuci_pol.egg-info/PKG-INFO
--rw-r--r--   0 rachel    (1000) rachel    (1000)      273 2023-03-01 12:43:47.000000 leuci-pol-0.0.8/src/leuci_pol.egg-info/SOURCES.txt
--rw-r--r--   0 rachel    (1000) rachel    (1000)        1 2023-03-01 12:43:47.000000 leuci-pol-0.0.8/src/leuci_pol.egg-info/dependency_links.txt
--rw-r--r--   0 rachel    (1000) rachel    (1000)       10 2023-03-01 12:43:47.000000 leuci-pol-0.0.8/src/leuci_pol.egg-info/top_level.txt
+drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-05 20:45:10.368777 leuci-pol-0.0.9/
+-rw-r--r--   0 rachel    (1000) rachel    (1000)    35149 2023-02-26 19:14:17.000000 leuci-pol-0.0.9/LICENSE
+-rw-r--r--   0 rachel    (1000) rachel    (1000)      869 2023-03-05 20:45:10.368777 leuci-pol-0.0.9/PKG-INFO
+-rw-r--r--   0 rachel    (1000) rachel    (1000)      369 2023-02-27 15:49:40.000000 leuci-pol-0.0.9/README.md
+-rw-r--r--   0 rachel    (1000) rachel    (1000)      104 2023-02-09 09:20:26.000000 leuci-pol-0.0.9/pyproject.toml
+-rw-r--r--   0 rachel    (1000) rachel    (1000)      625 2023-03-05 20:45:10.368777 leuci-pol-0.0.9/setup.cfg
+drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-05 20:45:10.358777 leuci-pol-0.0.9/src/
+drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-05 20:45:10.368777 leuci-pol-0.0.9/src/leuci_pol/
+-rw-r--r--   0 rachel    (1000) rachel    (1000)        0 2023-02-09 09:20:26.000000 leuci-pol-0.0.9/src/leuci_pol/__init__.py
+-rw-r--r--   0 rachel    (1000) rachel    (1000)    57646 2023-03-05 20:42:43.000000 leuci-pol-0.0.9/src/leuci_pol/interpolator.py
+-rw-r--r--   0 rachel    (1000) rachel    (1000)   160189 2023-03-01 12:25:50.000000 leuci-pol-0.0.9/src/leuci_pol/invariant.py
+drwxr-xr-x   0 rachel    (1000) rachel    (1000)        0 2023-03-05 20:45:10.368777 leuci-pol-0.0.9/src/leuci_pol.egg-info/
+-rw-r--r--   0 rachel    (1000) rachel    (1000)      869 2023-03-05 20:45:10.000000 leuci-pol-0.0.9/src/leuci_pol.egg-info/PKG-INFO
+-rw-r--r--   0 rachel    (1000) rachel    (1000)      273 2023-03-05 20:45:10.000000 leuci-pol-0.0.9/src/leuci_pol.egg-info/SOURCES.txt
+-rw-r--r--   0 rachel    (1000) rachel    (1000)        1 2023-03-05 20:45:10.000000 leuci-pol-0.0.9/src/leuci_pol.egg-info/dependency_links.txt
+-rw-r--r--   0 rachel    (1000) rachel    (1000)       10 2023-03-05 20:45:10.000000 leuci-pol-0.0.9/src/leuci_pol.egg-info/top_level.txt
```

### Comparing `leuci-pol-0.0.8/LICENSE` & `leuci-pol-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `leuci-pol-0.0.8/PKG-INFO` & `leuci-pol-0.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: leuci-pol
-Version: 0.0.8
+Version: 0.0.9
 Summary: Interpolation of 3d maps
 Home-page: https://github.com/pypa/sampleproject
 Author: Rachel Alcraft
 Author-email: rachelalcraft@gmail.com
 Project-URL: Bug Tracker, https://github.com/pypa/sampleproject/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `leuci-pol-0.0.8/setup.cfg` & `leuci-pol-0.0.9/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = leuci-pol
-version = 0.0.8
+version = 0.0.9
 author = Rachel Alcraft
 author_email = rachelalcraft@gmail.com
 description = Interpolation of 3d maps
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/pypa/sampleproject
 project_urls =
```

### Comparing `leuci-pol-0.0.8/src/leuci_pol/interpolator.py` & `leuci-pol-0.0.9/src/leuci_pol/interpolator.py`

 * *Files 0% similar despite different names*

```diff
@@ -164,25 +164,36 @@
                 yp = math.floor(y + j)
                 for k in range(int(-1*width/2 + 1), int(width/2 + 1)):          
                     zp = math.floor(z + k)                        
                     p = self.get_fms(xp, yp, zp)
                     vals.append(p)                    
         return vals
 
-    def mult_vector(self,A, V):        
-        length = len(V)
-        results = []
-        for row in range(length):        
-            sum = 0
-            for col in range(length):
-                mv = A[row,col]
-                vv = V[col]
-                sum += mv*vv                
-            results.append(sum)
-        return results
+    def mult_vector(self,A, V):     
+        use_np = True
+        if use_np:
+            vm = np.zeros(len(V))
+            for i in range(len(V)):
+                vm[i] = V[i]
+            mm= np.matmul(A, vm)
+            mv = []
+            for i in range(len(V)):
+                mv.append(mm[i])
+            return mv
+        else:   
+            length = len(V)
+            results = []
+            for row in range(length):        
+                sum = 0
+                for col in range(length):
+                    mv = A[row,col]
+                    vv = V[col]
+                    sum += mv*vv                
+                results.append(sum)
+            return results
     
 
 ####################################################################################################
 ### NEAREST NEIGHBOUR
 ####################################################################################################
 class Nearest(Interpolator):                
     def init(self):
```

### Comparing `leuci-pol-0.0.8/src/leuci_pol/invariant.py` & `leuci-pol-0.0.9/src/leuci_pol/invariant.py`

 * *Files identical despite different names*

### Comparing `leuci-pol-0.0.8/src/leuci_pol.egg-info/PKG-INFO` & `leuci-pol-0.0.9/src/leuci_pol.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: leuci-pol
-Version: 0.0.8
+Version: 0.0.9
 Summary: Interpolation of 3d maps
 Home-page: https://github.com/pypa/sampleproject
 Author: Rachel Alcraft
 Author-email: rachelalcraft@gmail.com
 Project-URL: Bug Tracker, https://github.com/pypa/sampleproject/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

