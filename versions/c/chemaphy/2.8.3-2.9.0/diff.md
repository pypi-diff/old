# Comparing `tmp/chemaphy-2.8.3.tar.gz` & `tmp/chemaphy-2.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "chemaphy-2.8.3.tar", last modified: Sun Mar 26 14:51:49 2023, max compression
+gzip compressed data, was "chemaphy-2.9.0.tar", last modified: Sat Apr  1 18:34:45 2023, max compression
```

## Comparing `chemaphy-2.8.3.tar` & `chemaphy-2.9.0.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)        0 2023-03-26 14:51:49.058935 chemaphy-2.8.3/
--rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)    10788 2023-03-26 14:50:20.000000 chemaphy-2.8.3/CHANGELOG.txt
--rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)     1088 2023-01-14 07:37:00.000000 chemaphy-2.8.3/LICENSE.txt
--rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)       25 2022-06-03 14:27:26.000000 chemaphy-2.8.3/MANIFEST.in
--rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)      521 2023-03-26 14:51:49.047932 chemaphy-2.8.3/PKG-INFO
--rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)     1012 2023-03-26 14:51:24.000000 chemaphy-2.8.3/README.md
-drwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)        0 2023-03-26 14:51:48.663466 chemaphy-2.8.3/chemaphy/
--rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)    82406 2023-03-26 14:49:33.000000 chemaphy-2.8.3/chemaphy/__init__.py
--rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)      160 2023-03-26 14:37:38.000000 chemaphy-2.8.3/chemaphy/about.py
--rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)      728 2023-03-26 14:49:40.000000 chemaphy-2.8.3/chemaphy/test.py
-drwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)        0 2023-03-26 14:51:48.985933 chemaphy-2.8.3/chemaphy.egg-info/
--rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)      521 2023-03-26 14:51:47.000000 chemaphy-2.8.3/chemaphy.egg-info/PKG-INFO
--rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)      285 2023-03-26 14:51:48.000000 chemaphy-2.8.3/chemaphy.egg-info/SOURCES.txt
--rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)        1 2023-03-26 14:51:47.000000 chemaphy-2.8.3/chemaphy.egg-info/dependency_links.txt
--rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)       47 2023-03-26 14:51:47.000000 chemaphy-2.8.3/chemaphy.egg-info/requires.txt
--rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)        9 2023-03-26 14:51:47.000000 chemaphy-2.8.3/chemaphy.egg-info/top_level.txt
--rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)       38 2023-03-26 14:51:49.062936 chemaphy-2.8.3/setup.cfg
--rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)      758 2023-03-26 14:37:28.000000 chemaphy-2.8.3/setup.py
+drwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)        0 2023-04-01 18:34:45.422143 chemaphy-2.9.0/
+-rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)    10958 2023-04-01 18:31:56.000000 chemaphy-2.9.0/CHANGELOG.txt
+-rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)     1088 2023-01-14 07:37:00.000000 chemaphy-2.9.0/LICENSE.txt
+-rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)       25 2022-06-03 14:27:26.000000 chemaphy-2.9.0/MANIFEST.in
+-rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)      521 2023-04-01 18:34:45.406137 chemaphy-2.9.0/PKG-INFO
+-rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)     1012 2023-03-26 14:51:24.000000 chemaphy-2.9.0/README.md
+drwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)        0 2023-04-01 18:34:45.038137 chemaphy-2.9.0/chemaphy/
+-rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)    84634 2023-04-01 18:31:17.000000 chemaphy-2.9.0/chemaphy/__init__.py
+-rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)      160 2023-04-01 18:17:10.000000 chemaphy-2.9.0/chemaphy/about.py
+-rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)      917 2023-04-01 18:32:03.000000 chemaphy-2.9.0/chemaphy/test.py
+drwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)        0 2023-04-01 18:34:45.325138 chemaphy-2.9.0/chemaphy.egg-info/
+-rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)      521 2023-04-01 18:34:41.000000 chemaphy-2.9.0/chemaphy.egg-info/PKG-INFO
+-rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)      285 2023-04-01 18:34:42.000000 chemaphy-2.9.0/chemaphy.egg-info/SOURCES.txt
+-rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)        1 2023-04-01 18:34:41.000000 chemaphy-2.9.0/chemaphy.egg-info/dependency_links.txt
+-rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)       47 2023-04-01 18:34:41.000000 chemaphy-2.9.0/chemaphy.egg-info/requires.txt
+-rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)        9 2023-04-01 18:34:41.000000 chemaphy-2.9.0/chemaphy.egg-info/top_level.txt
+-rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)       38 2023-04-01 18:34:45.425139 chemaphy-2.9.0/setup.cfg
+-rwxrwxrwx   0 sahil-rajwar  (1000) sahil-rajwar  (1000)      758 2023-04-01 18:20:32.000000 chemaphy-2.9.0/setup.py
```

### Comparing `chemaphy-2.8.3/CHANGELOG.txt` & `chemaphy-2.9.0/CHANGELOG.txt`

 * *Files 1% similar despite different names*

```diff
@@ -343,7 +343,12 @@
 
 ####### version-2.8.2 is useless #######
 
 version-2.8.3 (8:26 PM 3/26/2023)
 -----------------------
  -64th release
   Update: exponential moving average
+
+version-2.9.0 (12:11 AM 4/2/2023)
+-----------------------
+  -65th release
+   Update: Sorting Algorithm are added + changes in factorial function + fibonacci series
```

### Comparing `chemaphy-2.8.3/LICENSE.txt` & `chemaphy-2.9.0/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `chemaphy-2.8.3/README.md` & `chemaphy-2.9.0/README.md`

 * *Files identical despite different names*

### Comparing `chemaphy-2.8.3/chemaphy/__init__.py` & `chemaphy-2.9.0/chemaphy/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -390,14 +390,29 @@
 
     def qualitative_factor(R:(int|float),L:(int|float),C:(int|float)):
         Q = (1/R)*math.sqrt(L/C)
         return Q
 
 
 class Algorithm:
+    def fibonacci_series(number:int) -> int:
+        seq = [0,1]
+        if number <= 0:
+            raise ValueError("numbe must be x > 0")
+        elif number == 1:
+            return seq[0]
+        elif number == 2:
+            return seq[1]
+        else:
+            for i in range(2,number):
+                next_int = seq[i-1]+seq[i-2]
+                seq.append(next_int)
+        return seq
+
+
     def prime(lower_limit:int, upper_limit:int):
         if type(lower_limit) == type(upper_limit) == int:
             primes = []
             for i in range(lower_limit, upper_limit):
                 if i == 0 or i == 1:
                     continue
                 else:
@@ -458,14 +473,72 @@
 
     def pie(x:np.ndarray|list,labels:list,shadow=False,radius=1,a=0,b=0,labeldistance=1.1,title=None):
         plt.title(title)
         plt.pie(x,labels = labels,shadow=shadow,center=(a,b),labeldistance=labeldistance,radius=radius)
         plt.show()
 
 
+class Sort:
+    def bubble_sort(array:list) -> list:
+        for i in range(len(array)):
+            for j in range(0,len(array)-i-1):
+                if array[j] > array[j+1]:
+                    array[j],array[j+1] = array[j+1],array[j]
+        return array
+
+    def quick_sort(array:list) -> list:
+        if len(array) <= 1:
+            return array
+        flag = array[len(array)//2]
+        left = [x for x in array if x < flag]
+        mid = [x for x in array if x == flag]
+        right = [x for x in array if x > flag]
+        return Sort.quick_sort(left)+mid+Sort.quick_sort(right)
+    
+    def insertion_sort(array:list) -> list:
+        for i in range(1,len(array)):
+            key = array[i]
+            j = i - 1
+            while j >= 0 and array[j] > key:
+                array[j+1] = array[j]
+                j -= 1
+            array[j+1] = key
+        return array
+
+    def merge_sort(array:list) -> list:
+        if len(array) > 1:
+            mid = len(array)//2
+            left = array[:mid]
+            right = array[mid:]
+
+            Sort.merge_sort(left)
+            Sort.merge_sort(right)
+            i = j = k = 0
+            while i < len(left) and j < len(right):
+                if left[i] < right[j]:
+                    array[k] = left[i]
+                    i += 1
+                else:
+                    array[k] = right[j]
+                    j += 1
+                k += 1
+
+            while i < len(left):
+                array[k] = left[i]
+                i += 1
+                k += 1
+
+            while j < len(right):
+                array[k] = right[j]
+                j += 1
+                k += 1
+
+        return array
+
+
 class Statistics:
     def error(args:(list|np.ndarray),kwargs:(list|np.ndarray)):
         if len(args) == len(kwargs):
             rel = []
             for i in range(0,len(args)):
                 x = args[i]-kwargs[i]
                 rel.append(x)
@@ -532,43 +605,45 @@
         for more info: <https://www.google.com/search?q=factorial>
 
         ===========================
         Mathematical Representation
         ===========================
         `n! = n*(n-1)*(n-2)*...*1`
         """
-        return math.factorial(num)
+        if num == 0:
+            return 1
+        return num*Statistics.factorial(num-1)
 
     def permutations(n:(int|float),r:(int|float)):
         r"""
         A technique to determines the number of possible arrangements in a set when the order of the arrangements matters.
         Denoted as `nPr` where `n` is total number of objects and `r` is selected objects for arrangements
 
         for more info: <https://www.google.com/search?q=permuation>
 
         ===========================
         Mathematical Representation
         ===========================
         `nPr = n!/(n-r)!`
         """
-        return math.factorial(n)/math.factorial(n-r)
+        return Statistics.factorial(n)/Statistics.factorial(n-r)
 
     def combinations(n:(int|float),r:(int|float)):
         r"""
         An arrangement of objects where the order in which the objects are selected doesn't matter.
         Denoted as 'nCr' where `n` is total number of objects in the set and `r` number of choosing objects from the set
 
         for more info: <https://www.google.com/search?q=combination>
 
         ===========================
         Mathematical Representation
         ===========================
         `nCr = n!/r!(n-r)!`
         """
-        return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
+        return Statistics.factorial(n)/(Statistics.factorial(r)*Statistics.factorial(n-r))
 
     def quartiles(args:(list|np.ndarray)):
         r"""
         In statistics, a quartile is a type of quantile which divides the number of data points into four parts, or quarters, of more-or-less equal size
         the data must be in ascending order.
 
         for more info: <https://www.google.com/search?q=quartiles>
```

### Comparing `chemaphy-2.8.3/setup.py` & `chemaphy-2.9.0/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup,find_packages
 
 setup(
     name = "chemaphy",
-    version = "2.8.3",
+    version = "2.9.0",
     description = "Package for Scientific calculation",
     long_description = "For more info, check the github repository",
     author = "Sahil Rajwar",
     maintainer = "its_Sahil",
     author_email = "justsahilrajwar2004@gmail.com",
     packages = ["chemaphy"],
     license = "MIT",
```

