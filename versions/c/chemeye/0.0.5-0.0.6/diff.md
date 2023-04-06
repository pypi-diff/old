# Comparing `tmp/chemeye-0.0.5.tar.gz` & `tmp/chemeye-0.0.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "chemeye-0.0.5.tar", last modified: Fri Aug 19 04:44:48 2022, max compression
+gzip compressed data, was "chemeye-0.0.6.tar", last modified: Thu Apr  6 15:25:55 2023, max compression
```

## Comparing `chemeye-0.0.5.tar` & `chemeye-0.0.6.tar`

### file list

```diff
@@ -1,23 +1,25 @@
-drwxrwxr-x   0 jacob     (1000) jacob     (1000)        0 2022-08-19 04:44:48.920386 chemeye-0.0.5/
--rw-rw-r--   0 jacob     (1000) jacob     (1000)      288 2022-08-19 04:44:48.920386 chemeye-0.0.5/PKG-INFO
--rw-rw-r--   0 jacob     (1000) jacob     (1000)       38 2022-08-19 04:44:48.920386 chemeye-0.0.5/setup.cfg
--rw-rw-r--   0 jacob     (1000) jacob     (1000)      622 2022-08-19 04:44:22.000000 chemeye-0.0.5/setup.py
-drwxrwxr-x   0 jacob     (1000) jacob     (1000)        0 2022-08-19 04:44:48.920386 chemeye-0.0.5/src/
-drwxrwxr-x   0 jacob     (1000) jacob     (1000)        0 2022-08-19 04:44:48.920386 chemeye-0.0.5/src/chemeye/
--rw-rw-r--   0 jacob     (1000) jacob     (1000)     1850 2022-08-19 04:22:01.000000 chemeye-0.0.5/src/chemeye/SimMat.py
--rw-rw-r--   0 jacob     (1000) jacob     (1000)     2495 2022-08-19 04:23:11.000000 chemeye-0.0.5/src/chemeye/TSNE.py
--rw-rw-r--   0 jacob     (1000) jacob     (1000)      168 2022-08-19 04:22:01.000000 chemeye-0.0.5/src/chemeye/__asset_loader.py
--rw-rw-r--   0 jacob     (1000) jacob     (1000)       64 2022-08-19 04:22:01.000000 chemeye-0.0.5/src/chemeye/__init__.py
-drwxrwxr-x   0 jacob     (1000) jacob     (1000)        0 2022-08-19 04:44:48.920386 chemeye-0.0.5/src/chemeye/assets/
--rw-rw-r--   0 jacob     (1000) jacob     (1000)        0 2022-08-19 04:22:01.000000 chemeye-0.0.5/src/chemeye/assets/__init__.py
-drwxrwxr-x   0 jacob     (1000) jacob     (1000)        0 2022-08-19 04:44:48.920386 chemeye-0.0.5/src/chemeye.egg-info/
--rw-rw-r--   0 jacob     (1000) jacob     (1000)      288 2022-08-19 04:44:48.000000 chemeye-0.0.5/src/chemeye.egg-info/PKG-INFO
--rw-rw-r--   0 jacob     (1000) jacob     (1000)      408 2022-08-19 04:44:48.000000 chemeye-0.0.5/src/chemeye.egg-info/SOURCES.txt
--rw-rw-r--   0 jacob     (1000) jacob     (1000)        1 2022-08-19 04:44:48.000000 chemeye-0.0.5/src/chemeye.egg-info/dependency_links.txt
--rw-rw-r--   0 jacob     (1000) jacob     (1000)       54 2022-08-19 04:44:48.000000 chemeye-0.0.5/src/chemeye.egg-info/requires.txt
--rw-rw-r--   0 jacob     (1000) jacob     (1000)       13 2022-08-19 04:44:48.000000 chemeye-0.0.5/src/chemeye.egg-info/top_level.txt
-drwxrwxr-x   0 jacob     (1000) jacob     (1000)        0 2022-08-19 04:44:48.920386 chemeye-0.0.5/src/test/
--rw-rw-r--   0 jacob     (1000) jacob     (1000)        0 2022-08-19 04:22:01.000000 chemeye-0.0.5/src/test/__init__.py
--rw-rw-r--   0 jacob     (1000) jacob     (1000)     1835 2022-08-19 04:22:01.000000 chemeye-0.0.5/src/test/test_arrays.py
--rw-rw-r--   0 jacob     (1000) jacob     (1000)      573 2022-08-19 04:22:01.000000 chemeye-0.0.5/src/test/test_simmat.py
--rw-rw-r--   0 jacob     (1000) jacob     (1000)      726 2022-08-19 04:43:47.000000 chemeye-0.0.5/src/test/test_tsne_plotter.py
+drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:25:55.310725 chemeye-0.0.6/
+-rw-r--r--   0 collabpharma   (501) staff       (20)      299 2023-04-06 15:25:55.310193 chemeye-0.0.6/PKG-INFO
+-rw-r--r--   0 collabpharma   (501) staff       (20)       38 2023-04-06 15:25:55.310878 chemeye-0.0.6/setup.cfg
+-rw-r--r--   0 collabpharma   (501) staff       (20)      622 2023-04-06 15:24:48.000000 chemeye-0.0.6/setup.py
+drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:25:55.281863 chemeye-0.0.6/src/
+drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:25:55.284861 chemeye-0.0.6/src/chemeye/
+-rw-r--r--   0 collabpharma   (501) staff       (20)     1953 2022-12-13 20:44:35.000000 chemeye-0.0.6/src/chemeye/SimMat.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)     2487 2023-04-06 15:21:44.000000 chemeye-0.0.6/src/chemeye/TSNE.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)     2576 2022-12-13 21:04:11.000000 chemeye-0.0.6/src/chemeye/UMAP.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)      168 2022-07-05 18:46:34.000000 chemeye-0.0.6/src/chemeye/__asset_loader.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)       94 2023-04-06 15:15:30.000000 chemeye-0.0.6/src/chemeye/__init__.py
+drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:25:55.307022 chemeye-0.0.6/src/chemeye/assets/
+-rw-r--r--   0 collabpharma   (501) staff       (20)        0 2022-07-05 18:46:34.000000 chemeye-0.0.6/src/chemeye/assets/__init__.py
+drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:25:55.306456 chemeye-0.0.6/src/chemeye.egg-info/
+-rw-r--r--   0 collabpharma   (501) staff       (20)      299 2023-04-06 15:25:55.000000 chemeye-0.0.6/src/chemeye.egg-info/PKG-INFO
+-rw-r--r--   0 collabpharma   (501) staff       (20)      442 2023-04-06 15:25:55.000000 chemeye-0.0.6/src/chemeye.egg-info/SOURCES.txt
+-rw-r--r--   0 collabpharma   (501) staff       (20)        1 2023-04-06 15:25:55.000000 chemeye-0.0.6/src/chemeye.egg-info/dependency_links.txt
+-rw-r--r--   0 collabpharma   (501) staff       (20)       54 2023-04-06 15:25:55.000000 chemeye-0.0.6/src/chemeye.egg-info/requires.txt
+-rw-r--r--   0 collabpharma   (501) staff       (20)       13 2023-04-06 15:25:55.000000 chemeye-0.0.6/src/chemeye.egg-info/top_level.txt
+drwxr-xr-x   0 collabpharma   (501) staff       (20)        0 2023-04-06 15:25:55.309589 chemeye-0.0.6/src/test/
+-rw-r--r--   0 collabpharma   (501) staff       (20)        0 2022-07-05 18:46:34.000000 chemeye-0.0.6/src/test/__init__.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)     1927 2022-12-13 20:27:22.000000 chemeye-0.0.6/src/test/test_arrays.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)     2022 2022-12-13 20:51:08.000000 chemeye-0.0.6/src/test/test_simmat.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)     1065 2022-12-13 21:01:50.000000 chemeye-0.0.6/src/test/test_tsne.py
+-rw-r--r--   0 collabpharma   (501) staff       (20)      757 2022-12-13 20:13:25.000000 chemeye-0.0.6/src/test/test_umap.py
```

### Comparing `chemeye-0.0.5/setup.py` & `chemeye-0.0.6/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from setuptools import setup, find_packages
 
 
 setup(
     name='chemeye',
-    version='0.0.5',
+    version='0.0.6',
     license='MIT',
     author='Jacob Gerlach',
     author_email='jwgerlach00@gmail.com',
     url='https://github.com/jwgerlach00/chemeye',
     description='Visualization toolset for small molecule drug discovery',
     packages=find_packages('src'),
     package_dir={'': 'src'},
```

### Comparing `chemeye-0.0.5/src/chemeye/SimMat.py` & `chemeye-0.0.6/src/chemeye/SimMat.py`

 * *Files 13% similar despite different names*

```diff
@@ -2,15 +2,16 @@
 import numpy as np
 import plotly.graph_objects as go
 import plotly.express as px
 from rdkit import DataStructs
 
 
 class SimMat:
-    def __init__(self, row_prints:Iterable, col_prints:Iterable, key_type:str='ecfp',
+    def __init__(self, row_prints:Iterable[DataStructs.cDataStructs.ExplicitBitVect],
+                 col_prints:Iterable[DataStructs.cDataStructs.ExplicitBitVect], key_type:str='ecfp',
                  row_labels:Optional[Iterable[str]]=None, col_labels:Optional[Iterable[str]]=None) -> None:
         self.__row_prints = row_prints
         self.__col_prints = col_prints
         self.__key_type = key_type
         self.__row_labels = row_labels
         self.__col_labels = col_labels
     
@@ -34,11 +35,11 @@
     @staticmethod
     def plot(sim_arr:np.array, row_labels:Optional[Iterable[str]]=None,
              col_labels:Optional[Iterable[str]]=None) -> go.Figure:
         fig = px.imshow(sim_arr, x=row_labels, y=col_labels)
         fig.update_layout(title={ 'x': 0.5 })
         return fig
     
-    def main(self) -> Tuple[go.Figure, np.array]:
+    def main(self) -> Tuple[go.Figure, np.ndarray]:
         sim_arr = self.sim_matrix(row_prints=self.__row_prints, col_prints=self.__col_prints, key_type=self.__key_type)
         fig = self.plot(sim_arr, row_labels=self.__row_labels, col_labels=self.__col_labels)
         return (fig, sim_arr)
```

### Comparing `chemeye-0.0.5/src/chemeye/TSNE.py` & `chemeye-0.0.6/src/chemeye/TSNE.py`

 * *Files 0% similar despite different names*

```diff
@@ -60,8 +60,7 @@
     
     def main(self, color_category:Optional[Iterable]=None, css_color_map:bool=False) -> Tuple[go.Figure, pd.DataFrame]:
         df = self.tsne_df(self.__descriptors)
         return (
             TSNE.plot(df, color_category=color_category, css_color_map=css_color_map),
             df
         )
-
```

### Comparing `chemeye-0.0.5/src/test/test_arrays.py` & `chemeye-0.0.6/src/test/test_simmat.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,36 +1,43 @@
 import unittest
-import numpy as np
 import naclo
-
-from chemeye import arrays
+from chemeye import SimMat
+from plotly.graph_objects import Figure
+import numpy as np
 
 
-class TestArrays(unittest.TestCase):
+class TestSimMat(unittest.TestCase):
     @classmethod
     def setUpClass(cls) -> None:
-        cls.test_smiles = ['CN=C=O', 'CCC', 'O']
-        cls.test_mols = naclo.smiles_2_mols(cls.test_smiles)
-        cls.maccs_keys = naclo.mols_2_maccs(cls.test_mols)
-        cls.ecfp4_prints = naclo.mols_2_ecfp(cls.test_mols, radius=2, return_numpy=False)
-        cls.ecfp6_prints = naclo.mols_2_ecfp(cls.test_mols, radius=3, return_numpy=False)
-        cls.ecfp4_prints_np = naclo.mols_2_ecfp(cls.test_mols, radius=2, return_numpy=True)
+        test_smiles = [
+            'CCC',
+            'O',
+            'C',
+            'SOO'
+        ]
+        test_mols = naclo.smiles_2_mols(test_smiles)
+        
+        cls.ecfp4_prints = naclo.mols_2_ecfp(test_mols, radius=2, return_numpy=False)
+        cls.ecfp6_prints = naclo.mols_2_ecfp(test_mols, radius=3, return_numpy=False)
+        cls.maccs_keys = naclo.mols_2_maccs(test_mols)
+        
         return super().setUpClass()
     
     def test_sim_matrix(self):
-        mat_maccs = arrays.sim_matrix(self.maccs_keys, self.maccs_keys, key_type='maccs')  # Test MACCS keys
-        mat_ecfp4 = arrays.sim_matrix(self.ecfp4_prints, self.ecfp4_prints)  # Test ECFP4
-        mat_ecfp6 = arrays.sim_matrix(self.ecfp6_prints, self.ecfp6_prints)  # Test ECFP6
+        mat_maccs = SimMat.sim_matrix(self.maccs_keys, self.maccs_keys, key_type='maccs')  # Test MACCS keys
+        mat_ecfp4 = SimMat.sim_matrix(self.ecfp4_prints, self.ecfp4_prints)  # Test ECFP4
+        mat_ecfp6 = SimMat.sim_matrix(self.ecfp6_prints, self.ecfp6_prints)  # Test ECFP6
         
         # Check same molecules equal 1 in matrix in all cases (along identity)
+        arr_len = len(self.ecfp4_prints)
         np.testing.assert_array_equal(
-            mat_maccs[np.eye(3, dtype=bool)],
-            mat_ecfp4[np.eye(3, dtype=bool)],
-            mat_ecfp6[np.eye(3, dtype=bool)],
-            3*[1]
+            mat_maccs[np.eye(arr_len, dtype=bool)],
+            mat_ecfp4[np.eye(arr_len, dtype=bool)],
+            mat_ecfp6[np.eye(arr_len, dtype=bool)],
+            arr_len*[1]
         )
         
         # Check maccs is different than ecfp but ecfp4,6 are equal
         self.assertFalse(
             np.array_equal(
                 mat_maccs,
                 mat_ecfp4
@@ -39,17 +46,23 @@
         self.assertTrue(
             np.array_equal(
                 mat_ecfp4,
                 mat_ecfp6
             )
         )
         
-    def test_tsne(self):
-       out = arrays.tsne(np.array(self.ecfp4_prints_np))
-       self.assertEqual(
-           out.shape,
-           (len(self.ecfp4_prints_np), 2)
-       )
-
+    def test_main(self):
+        simmat = SimMat(self.ecfp4_prints, self.ecfp4_prints)
+        fig, sim_arr = simmat.main()
+        
+        self.assertIsInstance(
+            fig,
+            Figure
+        )
+        self.assertIsInstance(
+            sim_arr,
+            np.ndarray
+        )
 
+      
 if __name__ == '__main__':
     unittest.main()
```

### Comparing `chemeye-0.0.5/src/test/test_tsne_plotter.py` & `chemeye-0.0.6/src/test/test_umap.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,25 +1,25 @@
-import unittest
-import plotly.graph_objects as go
+# import unittest
+# import plotly.graph_objects as go
 
-import naclo
-from chemeye import TSNE
+# import naclo
+# from chemeye import UMAP
 
 
-class TestTSNE(unittest.TestCase):
-    @classmethod
-    def setUpClass(cls) -> None:
-        cls.test_smiles = ['CN=C=O', 'CCC', 'O']
-        cls.test_mols = naclo.smiles_2_mols(cls.test_smiles)
-        cls.maccs_keys = naclo.mols_2_maccs(cls.test_mols)
-        cls.ecfp4_prints = naclo.mols_2_ecfp(cls.test_mols, radius=2, return_numpy=True)
+# class TestUMAP(unittest.TestCase):
+#     @classmethod
+#     def setUpClass(cls) -> None:
+#         cls.test_smiles = ['CN=C=O', 'CCC', 'O']
+#         cls.test_mols = naclo.smiles_2_mols(cls.test_smiles)
+#         cls.maccs_keys = naclo.mols_2_maccs(cls.test_mols)
+#         cls.ecfp4_prints = naclo.mols_2_ecfp(cls.test_mols, radius=2, return_numpy=True)
         
-        cls.tsne_plotter = TSNEPlotter(cls.ecfp4_prints)
-        return super().setUpClass()
+#         cls.tsne_plotter = UMAP(cls.ecfp4_prints)
+#         return super().setUpClass()
     
-    def test_plot(self):
-        fig = self.tsne_plotter.plot('tsne1', 'tsne2', [1, 'a', True])
+#     def test_plot(self):
+#         fig = self.tsne_plotter.plot('umap1', 'umap2', [1, 'a', True])
         
-        self.assertIsInstance(
-            fig,
-            go.Figure
-        )
+#         self.assertIsInstance(
+#             fig,
+#             go.Figure
+#         )
```

