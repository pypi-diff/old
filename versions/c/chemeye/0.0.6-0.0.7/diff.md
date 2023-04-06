# Comparing `tmp/chemeye-0.0.6.tar.gz` & `tmp/chemeye-0.0.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "chemeye-0.0.6.tar", last modified: Thu Apr  6 15:25:55 2023, max compression
+gzip compressed data, was "chemeye-0.0.7.tar", last modified: Thu Apr  6 15:30:51 2023, max compression
```

## Comparing `chemeye-0.0.6.tar` & `chemeye-0.0.7.tar`

### file list

```diff
@@ -1,25 +1,25 @@
-drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:25:55.310725 chemeye-0.0.6/
--rw-r--r--   0 collabpharma   (501) staff       (20)      299 2023-04-06 15:25:55.310193 chemeye-0.0.6/PKG-INFO
--rw-r--r--   0 collabpharma   (501) staff       (20)       38 2023-04-06 15:25:55.310878 chemeye-0.0.6/setup.cfg
--rw-r--r--   0 collabpharma   (501) staff       (20)      622 2023-04-06 15:24:48.000000 chemeye-0.0.6/setup.py
-drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:25:55.281863 chemeye-0.0.6/src/
-drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:25:55.284861 chemeye-0.0.6/src/chemeye/
--rw-r--r--   0 collabpharma   (501) staff       (20)     1953 2022-12-13 20:44:35.000000 chemeye-0.0.6/src/chemeye/SimMat.py
--rw-r--r--   0 collabpharma   (501) staff       (20)     2487 2023-04-06 15:21:44.000000 chemeye-0.0.6/src/chemeye/TSNE.py
--rw-r--r--   0 collabpharma   (501) staff       (20)     2576 2022-12-13 21:04:11.000000 chemeye-0.0.6/src/chemeye/UMAP.py
--rw-r--r--   0 collabpharma   (501) staff       (20)      168 2022-07-05 18:46:34.000000 chemeye-0.0.6/src/chemeye/__asset_loader.py
--rw-r--r--   0 collabpharma   (501) staff       (20)       94 2023-04-06 15:15:30.000000 chemeye-0.0.6/src/chemeye/__init__.py
-drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:25:55.307022 chemeye-0.0.6/src/chemeye/assets/
--rw-r--r--   0 collabpharma   (501) staff       (20)        0 2022-07-05 18:46:34.000000 chemeye-0.0.6/src/chemeye/assets/__init__.py
-drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:25:55.306456 chemeye-0.0.6/src/chemeye.egg-info/
--rw-r--r--   0 collabpharma   (501) staff       (20)      299 2023-04-06 15:25:55.000000 chemeye-0.0.6/src/chemeye.egg-info/PKG-INFO
--rw-r--r--   0 collabpharma   (501) staff       (20)      442 2023-04-06 15:25:55.000000 chemeye-0.0.6/src/chemeye.egg-info/SOURCES.txt
--rw-r--r--   0 collabpharma   (501) staff       (20)        1 2023-04-06 15:25:55.000000 chemeye-0.0.6/src/chemeye.egg-info/dependency_links.txt
--rw-r--r--   0 collabpharma   (501) staff       (20)       54 2023-04-06 15:25:55.000000 chemeye-0.0.6/src/chemeye.egg-info/requires.txt
--rw-r--r--   0 collabpharma   (501) staff       (20)       13 2023-04-06 15:25:55.000000 chemeye-0.0.6/src/chemeye.egg-info/top_level.txt
-drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:25:55.309589 chemeye-0.0.6/src/test/
--rw-r--r--   0 collabpharma   (501) staff       (20)        0 2022-07-05 18:46:34.000000 chemeye-0.0.6/src/test/__init__.py
--rw-r--r--   0 collabpharma   (501) staff       (20)     1927 2022-12-13 20:27:22.000000 chemeye-0.0.6/src/test/test_arrays.py
--rw-r--r--   0 collabpharma   (501) staff       (20)     2022 2022-12-13 20:51:08.000000 chemeye-0.0.6/src/test/test_simmat.py
--rw-r--r--   0 collabpharma   (501) staff       (20)     1065 2022-12-13 21:01:50.000000 chemeye-0.0.6/src/test/test_tsne.py
--rw-r--r--   0 collabpharma   (501) staff       (20)      757 2022-12-13 20:13:25.000000 chemeye-0.0.6/src/test/test_umap.py
+drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:30:51.962288 chemeye-0.0.7/
+-rw-r--r--   0 collabpharma   (501) staff       (20)      299 2023-04-06 15:30:51.961883 chemeye-0.0.7/PKG-INFO
+-rw-r--r--   0 collabpharma   (501) staff       (20)       38 2023-04-06 15:30:51.962452 chemeye-0.0.7/setup.cfg
+-rw-r--r--   0 collabpharma   (501) staff       (20)      622 2023-04-06 15:30:30.000000 chemeye-0.0.7/setup.py
+drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:30:51.938452 chemeye-0.0.7/src/
+drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:30:51.940722 chemeye-0.0.7/src/chemeye/
+-rw-r--r--   0 collabpharma   (501) staff       (20)     1953 2022-12-13 20:44:35.000000 chemeye-0.0.7/src/chemeye/SimMat.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)     2487 2023-04-06 15:21:44.000000 chemeye-0.0.7/src/chemeye/TSNE.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)     2458 2023-04-06 15:30:16.000000 chemeye-0.0.7/src/chemeye/UMAP.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)      168 2022-07-05 18:46:34.000000 chemeye-0.0.7/src/chemeye/__asset_loader.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)       94 2023-04-06 15:15:30.000000 chemeye-0.0.7/src/chemeye/__init__.py
+drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:30:51.958798 chemeye-0.0.7/src/chemeye/assets/
+-rw-r--r--   0 collabpharma   (501) staff       (20)        0 2022-07-05 18:46:34.000000 chemeye-0.0.7/src/chemeye/assets/__init__.py
+drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:30:51.958224 chemeye-0.0.7/src/chemeye.egg-info/
+-rw-r--r--   0 collabpharma   (501) staff       (20)      299 2023-04-06 15:30:51.000000 chemeye-0.0.7/src/chemeye.egg-info/PKG-INFO
+-rw-r--r--   0 collabpharma   (501) staff       (20)      442 2023-04-06 15:30:51.000000 chemeye-0.0.7/src/chemeye.egg-info/SOURCES.txt
+-rw-r--r--   0 collabpharma   (501) staff       (20)        1 2023-04-06 15:30:51.000000 chemeye-0.0.7/src/chemeye.egg-info/dependency_links.txt
+-rw-r--r--   0 collabpharma   (501) staff       (20)       54 2023-04-06 15:30:51.000000 chemeye-0.0.7/src/chemeye.egg-info/requires.txt
+-rw-r--r--   0 collabpharma   (501) staff       (20)       13 2023-04-06 15:30:51.000000 chemeye-0.0.7/src/chemeye.egg-info/top_level.txt
+drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:30:51.961264 chemeye-0.0.7/src/test/
+-rw-r--r--   0 collabpharma   (501) staff       (20)        0 2022-07-05 18:46:34.000000 chemeye-0.0.7/src/test/__init__.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)     1927 2022-12-13 20:27:22.000000 chemeye-0.0.7/src/test/test_arrays.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)     2022 2022-12-13 20:51:08.000000 chemeye-0.0.7/src/test/test_simmat.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)     1065 2022-12-13 21:01:50.000000 chemeye-0.0.7/src/test/test_tsne.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)      757 2022-12-13 20:13:25.000000 chemeye-0.0.7/src/test/test_umap.py
```

### Comparing `chemeye-0.0.6/setup.py` & `chemeye-0.0.7/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from setuptools import setup, find_packages
 
 
 setup(
     name='chemeye',
-    version='0.0.6',
+    version='0.0.7',
     license='MIT',
     author='Jacob Gerlach',
     author_email='jwgerlach00@gmail.com',
     url='https://github.com/jwgerlach00/chemeye',
     description='Visualization toolset for small molecule drug discovery',
     packages=find_packages('src'),
     package_dir={'': 'src'},
```

### Comparing `chemeye-0.0.6/src/chemeye/SimMat.py` & `chemeye-0.0.7/src/chemeye/SimMat.py`

 * *Files identical despite different names*

### Comparing `chemeye-0.0.6/src/chemeye/TSNE.py` & `chemeye-0.0.7/src/chemeye/TSNE.py`

 * *Files identical despite different names*

### Comparing `chemeye-0.0.6/src/chemeye/UMAP.py` & `chemeye-0.0.7/src/chemeye/UMAP.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,68 +1,67 @@
-# import numpy as np
-# import plotly.express as px
-# import plotly.graph_objects as go
-# from typing import Iterable, Optional, Tuple
-# import pandas as pd
-# from matplotlib.colors import CSS4_COLORS
-# from umap import UMAP as UMAPS
+import numpy as np
+import plotly.express as px
+import plotly.graph_objects as go
+from typing import Iterable, Optional, Tuple
+import pandas as pd
+from matplotlib.colors import CSS4_COLORS
+from umap import UMAP as UMAPS
 
 
-# class UMAP:
-#     X_NAME = 'umap-x'
-#     Y_NAME = 'umap-y'
-#     RANDOM_SEED = 42
-    
-#     def __init__(self, descriptors:np.array) -> None:
-#         self.__descriptors = np.copy(descriptors)
-    
-#     @staticmethod
-#     def umap(descriptors:np.array, seed=RANDOM_SEED) -> np.array:
-#         umap = UMAPS(random_state=seed)
-#         fitted_umap = umap.fit(descriptors)
-#         return fitted_umap.transform(descriptors)
-    
-#     @staticmethod
-#     def css_color_map(color_category:Iterable) -> dict:
-#         unique_colors = set(color_category)
+class UMAP:
+    X_NAME = 'umap-x'
+    Y_NAME = 'umap-y'
+    RANDOM_SEED = 42
+    
+    def __init__(self, descriptors:np.array) -> None:
+        self.__descriptors = np.copy(descriptors)
+    
+    @staticmethod
+    def umap(descriptors:np.array, seed=RANDOM_SEED) -> np.array:
+        umap = UMAPS(random_state=seed)
+        fitted_umap = umap.fit(descriptors)
+        return fitted_umap.transform(descriptors)
+    
+    @staticmethod
+    def css_color_map(color_category:Iterable) -> dict:
+        unique_colors = set(color_category)
         
-#         css_colors = list(CSS4_COLORS.keys())
+        css_colors = list(CSS4_COLORS.keys())
         
-#         color_map = {}
-#         for i, color in enumerate(unique_colors):
-#             color_map[color] = css_colors[i]
-#         return color_map
-    
-#     @staticmethod
-#     def umap_df(descriptors, x_name:str=X_NAME, y_name:str=Y_NAME) -> pd.DataFrame:
-#         arr = UMAP.umap(descriptors)
-#         return pd.DataFrame({
-#             x_name: arr[:, 0],
-#             y_name: arr[:, 1]
-#         })
-    
-#     @staticmethod
-#     def plot(df:pd.DataFrame, x_col_name:str=X_NAME, y_col_name:str=Y_NAME, color_category:Optional[Iterable]=None,
-#              css_color_map:bool=False, opacity:float=1) -> go.Figure:
-#         color = None
+        color_map = {}
+        for i, color in enumerate(unique_colors):
+            color_map[color] = css_colors[i]
+        return color_map
+    
+    @staticmethod
+    def umap_df(descriptors, x_name:str=X_NAME, y_name:str=Y_NAME) -> pd.DataFrame:
+        arr = UMAP.umap(descriptors)
+        return pd.DataFrame({
+            x_name: arr[:, 0],
+            y_name: arr[:, 1]
+        })
+    
+    @staticmethod
+    def plot(df:pd.DataFrame, x_col_name:str=X_NAME, y_col_name:str=Y_NAME, color_category:Optional[Iterable]=None,
+             css_color_map:bool=False, opacity:float=1) -> go.Figure:
+        color = None
         
-#         if color_category:
-#             df['color'] = color_category
-#             color = 'color'
-#             df['color'] = df['color'].fillna('missing color')  # Replace NaN w/ string bc px doesn't like NaN
+        if color_category:
+            df['color'] = color_category
+            color = 'color'
+            df['color'] = df['color'].fillna('missing color')  # Replace NaN w/ string bc px doesn't like NaN
         
-#         if css_color_map:
-#             plot = px.scatter(df, x=x_col_name, y=y_col_name, color=color, render_mode='svg', opacity=opacity,
-#                               color_discrete_map=UMAP.css_color_map(color_category))
-#         else:
-#             plot = px.scatter(df, x=x_col_name, y=y_col_name, color=color, render_mode='svg', opacity=opacity,
-#                               color_discrete_sequence=px.colors.qualitative.Alphabet)
-#         plot.update_layout(title={'x': 0.5})
-#         return plot
-    
-#     def main(self, color_category:Optional[Iterable]=None, css_color_map:bool=False) -> Tuple[go.Figure, pd.DataFrame]:
-#         df = self.umap_df(self.__descriptors)
-#         return (
-#             UMAP.plot(df, color_category=color_category, css_color_map=css_color_map),
-#             df
-#         )
-        
+        if css_color_map:
+            plot = px.scatter(df, x=x_col_name, y=y_col_name, color=color, render_mode='svg', opacity=opacity,
+                              color_discrete_map=UMAP.css_color_map(color_category))
+        else:
+            plot = px.scatter(df, x=x_col_name, y=y_col_name, color=color, render_mode='svg', opacity=opacity,
+                              color_discrete_sequence=px.colors.qualitative.Alphabet)
+        plot.update_layout(title={'x': 0.5})
+        return plot
+    
+    def main(self, color_category:Optional[Iterable]=None, css_color_map:bool=False) -> Tuple[go.Figure, pd.DataFrame]:
+        df = self.umap_df(self.__descriptors)
+        return (
+            UMAP.plot(df, color_category=color_category, css_color_map=css_color_map),
+            df
+        )
```

### Comparing `chemeye-0.0.6/src/test/test_arrays.py` & `chemeye-0.0.7/src/test/test_arrays.py`

 * *Files identical despite different names*

### Comparing `chemeye-0.0.6/src/test/test_simmat.py` & `chemeye-0.0.7/src/test/test_simmat.py`

 * *Files identical despite different names*

### Comparing `chemeye-0.0.6/src/test/test_tsne.py` & `chemeye-0.0.7/src/test/test_tsne.py`

 * *Files identical despite different names*

### Comparing `chemeye-0.0.6/src/test/test_umap.py` & `chemeye-0.0.7/src/test/test_umap.py`

 * *Files identical despite different names*

