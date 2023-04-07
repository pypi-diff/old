# Comparing `tmp/prince-0.8.3.tar.gz` & `tmp/prince-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "prince-0.8.3.tar", max compression
+gzip compressed data, was "prince-0.9.0.tar", max compression
```

## Comparing `prince-0.8.3.tar` & `prince-0.9.0.tar`

### file list

```diff
@@ -1,23 +1,23 @@
--rw-r--r--   0        0        0     1078 2023-02-26 11:12:21.275757 prince-0.8.3/LICENSE
--rw-r--r--   0        0        0      186 2023-02-26 11:12:21.290089 prince-0.8.3/prince/__init__.py
--rw-r--r--   0        0        0       63 2022-11-10 10:17:15.679231 prince-0.8.3/prince/__version__.py
--rw-r--r--   0        0        0    10002 2023-03-01 22:45:55.253507 prince-0.8.3/prince/ca.py
--rw-r--r--   0        0        0    51613 2023-02-26 11:12:21.291042 prince-0.8.3/prince/datasets/02-resultats-par-region.csv
--rw-r--r--   0        0        0   240945 2023-02-26 11:12:21.291859 prince-0.8.3/prince/datasets/beers.csv.zip
--rw-r--r--   0        0        0     3582 2023-02-26 11:12:21.291951 prince-0.8.3/prince/datasets/decathlon.csv
--rw-r--r--   0        0        0    36083 2023-02-26 11:12:21.292289 prince-0.8.3/prince/datasets/hearthstone_cards.csv
--rw-r--r--   0        0        0   342886 2023-02-26 11:12:21.293727 prince-0.8.3/prince/datasets/per-capita-energy-stacked.csv
--rw-r--r--   0        0        0      208 2023-02-26 11:12:21.293975 prince-0.8.3/prince/datasets/punctuation_marks.csv
--rw-r--r--   0        0        0   333058 2023-02-26 11:12:21.294227 prince-0.8.3/prince/datasets/resultats-par-departement.csv
--rw-r--r--   0        0        0     4272 2023-02-26 11:12:21.290472 prince-0.8.3/prince/datasets.py
--rw-r--r--   0        0        0     3974 2023-03-11 11:40:59.439864 prince-0.8.3/prince/famd.py
--rw-r--r--   0        0        0     6831 2022-11-10 10:17:15.679509 prince-0.8.3/prince/gpa.py
--rw-r--r--   0        0        0     1749 2023-02-26 11:12:21.294771 prince-0.8.3/prince/mca.py
--rw-r--r--   0        0        0     7998 2023-02-26 11:12:21.295063 prince-0.8.3/prince/mfa.py
--rwxr-xr-x   0        0        0    13141 2023-03-11 11:00:53.859325 prince-0.8.3/prince/pca.py
--rw-r--r--   0        0        0     1322 2022-11-10 10:17:15.679836 prince-0.8.3/prince/plot.py
--rw-r--r--   0        0        0     1230 2023-02-26 11:12:21.296342 prince-0.8.3/prince/svd.py
--rw-r--r--   0        0        0     3003 2023-02-26 11:12:21.297041 prince-0.8.3/prince/utils.py
--rw-r--r--   0        0        0      760 2023-03-11 11:42:35.311051 prince-0.8.3/pyproject.toml
--rw-r--r--   0        0        0      726 1970-01-01 00:00:00.000000 prince-0.8.3/setup.py
--rw-r--r--   0        0        0      587 1970-01-01 00:00:00.000000 prince-0.8.3/PKG-INFO
+-rw-r--r--   0        0        0     1078 2023-02-26 11:12:21.275757 prince-0.9.0/LICENSE
+-rw-r--r--   0        0        0      186 2023-02-26 11:12:21.290089 prince-0.9.0/prince/__init__.py
+-rw-r--r--   0        0        0       63 2022-11-10 10:17:15.679231 prince-0.9.0/prince/__version__.py
+-rw-r--r--   0        0        0    10002 2023-03-01 22:45:55.253507 prince-0.9.0/prince/ca.py
+-rw-r--r--   0        0        0    51613 2023-02-26 11:12:21.291042 prince-0.9.0/prince/datasets/02-resultats-par-region.csv
+-rw-r--r--   0        0        0   240945 2023-02-26 11:12:21.291859 prince-0.9.0/prince/datasets/beers.csv.zip
+-rw-r--r--   0        0        0     3582 2023-02-26 11:12:21.291951 prince-0.9.0/prince/datasets/decathlon.csv
+-rw-r--r--   0        0        0    36083 2023-02-26 11:12:21.292289 prince-0.9.0/prince/datasets/hearthstone_cards.csv
+-rw-r--r--   0        0        0   342886 2023-02-26 11:12:21.293727 prince-0.9.0/prince/datasets/per-capita-energy-stacked.csv
+-rw-r--r--   0        0        0      208 2023-02-26 11:12:21.293975 prince-0.9.0/prince/datasets/punctuation_marks.csv
+-rw-r--r--   0        0        0   333058 2023-02-26 11:12:21.294227 prince-0.9.0/prince/datasets/resultats-par-departement.csv
+-rw-r--r--   0        0        0     4272 2023-02-26 11:12:21.290472 prince-0.9.0/prince/datasets.py
+-rw-r--r--   0        0        0     4843 2023-03-18 13:56:58.534325 prince-0.9.0/prince/famd.py
+-rw-r--r--   0        0        0     6831 2022-11-10 10:17:15.679509 prince-0.9.0/prince/gpa.py
+-rw-r--r--   0        0        0     1749 2023-02-26 11:12:21.294771 prince-0.9.0/prince/mca.py
+-rw-r--r--   0        0        0     7998 2023-02-26 11:12:21.295063 prince-0.9.0/prince/mfa.py
+-rwxr-xr-x   0        0        0    13051 2023-03-18 13:49:45.994624 prince-0.9.0/prince/pca.py
+-rw-r--r--   0        0        0     1322 2022-11-10 10:17:15.679836 prince-0.9.0/prince/plot.py
+-rw-r--r--   0        0        0     1230 2023-02-26 11:12:21.296342 prince-0.9.0/prince/svd.py
+-rw-r--r--   0        0        0     3003 2023-02-26 11:12:21.297041 prince-0.9.0/prince/utils.py
+-rw-r--r--   0        0        0      760 2023-03-18 13:57:45.663444 prince-0.9.0/pyproject.toml
+-rw-r--r--   0        0        0      726 1970-01-01 00:00:00.000000 prince-0.9.0/setup.py
+-rw-r--r--   0        0        0      587 1970-01-01 00:00:00.000000 prince-0.9.0/PKG-INFO
```

### Comparing `prince-0.8.3/LICENSE` & `prince-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `prince-0.8.3/prince/ca.py` & `prince-0.9.0/prince/ca.py`

 * *Files identical despite different names*

### Comparing `prince-0.8.3/prince/datasets/02-resultats-par-region.csv` & `prince-0.9.0/prince/datasets/02-resultats-par-region.csv`

 * *Files identical despite different names*

### Comparing `prince-0.8.3/prince/datasets/beers.csv.zip` & `prince-0.9.0/prince/datasets/beers.csv.zip`

 * *Files identical despite different names*

### Comparing `prince-0.8.3/prince/datasets/decathlon.csv` & `prince-0.9.0/prince/datasets/decathlon.csv`

 * *Files identical despite different names*

### Comparing `prince-0.8.3/prince/datasets/hearthstone_cards.csv` & `prince-0.9.0/prince/datasets/hearthstone_cards.csv`

 * *Files identical despite different names*

### Comparing `prince-0.8.3/prince/datasets/per-capita-energy-stacked.csv` & `prince-0.9.0/prince/datasets/per-capita-energy-stacked.csv`

 * *Files identical despite different names*

### Comparing `prince-0.8.3/prince/datasets/resultats-par-departement.csv` & `prince-0.9.0/prince/datasets/resultats-par-departement.csv`

 * *Files identical despite different names*

### Comparing `prince-0.8.3/prince/datasets.py` & `prince-0.9.0/prince/datasets.py`

 * *Files identical despite different names*

### Comparing `prince-0.8.3/prince/famd.py` & `prince-0.9.0/prince/famd.py`

 * *Files 17% similar despite different names*

```diff
@@ -35,37 +35,62 @@
 
     def fit(self, X, y=None):
 
         # Separate numerical columns from categorical columns
         self.num_cols_ = X.select_dtypes(np.number).columns.tolist()
         if not self.num_cols_:
             raise ValueError("All variables are qualitative: MCA should be used")
-        self.cat_cols_ = list(set(X.columns) - set(self.num_cols_))
+        self.cat_cols_ = X.columns.difference(self.num_cols_).tolist()
         if not self.cat_cols_:
             raise ValueError("All variables are quantitative: PCA should be used")
 
         # Preprocess numerical columns
         X_num = X[self.num_cols_].copy()
         self.num_scaler_ = preprocessing.StandardScaler().fit(X_num)
         X_num[:] = self.num_scaler_.transform(X_num)
 
         # Preprocess categorical columns
         X_cat = X[self.cat_cols_]
         self.cat_scaler_ = preprocessing.OneHotEncoder().fit(X_cat)
-        X_cat = pd.DataFrame.sparse.from_spmatrix(
+        X_cat_oh = pd.DataFrame.sparse.from_spmatrix(
             self.cat_scaler_.transform(X_cat),
             index=X_cat.index,
             columns=self.cat_scaler_.get_feature_names_out(self.cat_cols_),
         )
-        prop = X_cat.sum() / X_cat.sum().sum() * 2
-        X_cat = X_cat.sub(X_cat.mean(axis="rows")).div(prop**0.5, axis="columns")
-
-        Z = pd.concat([X_num, X_cat], axis=1)
+        prop = X_cat_oh.sum() / X_cat_oh.sum().sum() * 2
+        X_cat_oh_norm = X_cat_oh.sub(X_cat_oh.mean(axis="rows")).div(
+            prop**0.5, axis="columns"
+        )
+
+        Z = pd.concat([X_num, X_cat_oh_norm], axis=1)
+        super().fit(Z)
+
+        # Determine column_coordinates_
+        # This is based on line 184 in FactoMineR's famd.R file
+        rc = self.row_coordinates(X)
+        weights = np.ones(len(X_cat_oh)) / len(X_cat_oh)
+        norm = (rc**2).multiply(weights, axis=0).sum()
+        eta2 = pd.DataFrame(index=rc.columns)
+        for i, col in enumerate(self.cat_cols_):
+            # TODO: there must be a better way to select a subset of the one-hot encoded matrix
+            tt = X_cat_oh[[f"{col}_{i}" for i in self.cat_scaler_.categories_[i]]]
+            ni = (tt / len(tt)).sum()
+            eta2[col] = (
+                rc.apply(
+                    lambda x: (tt.multiply(x * weights, axis=0).sum() ** 2 / ni).sum()
+                )
+                / norm
+            ).values
+        self.column_coordinates_ = pd.concat(
+            [self.column_coordinates_.loc[self.num_cols_] ** 2, eta2.T]
+        )
+        self.column_coordinates_.columns.name = "component"
+        self.column_coordinates_.index.name = "variable"
 
-        return super().fit(Z)
+        return self
 
     def _check_input(self, X):
         if self.check_input:
             check_array(X, dtype=[str, np.number])
 
     def row_coordinates(self, X):
 
@@ -85,19 +110,14 @@
         prop = X_cat.sum() / X_cat.sum().sum() * 2
         X_cat = X_cat.sub(X_cat.mean(axis="rows")).div(prop**0.5, axis="columns")
 
         Z = pd.concat([X_num, X_cat], axis=1)
 
         return super().row_coordinates(Z)
 
-    def column_coordinates(self, X):
-        raise NotImplemented(
-            "FAMD inherits from PCA, but this method is not implemented yet"
-        )
-
     def inverse_transform(self, X):
         raise NotImplemented(
             "FAMD inherits from PCA, but this method is not implemented yet"
         )
 
     def row_standard_coordinates(self, X):
         raise NotImplemented(
@@ -117,10 +137,8 @@
     def column_cosine_similarities_(self, X):
         raise NotImplemented(
             "FAMD inherits from PCA, but this method is not implemented yet"
         )
 
     @property
     def column_contributions_(self):
-        raise NotImplemented(
-            "FAMD inherits from PCA, but this method is not implemented yet"
-        )
+        return self.column_coordinates_ / self.eigenvalues_
```

### Comparing `prince-0.8.3/prince/gpa.py` & `prince-0.9.0/prince/gpa.py`

 * *Files identical despite different names*

### Comparing `prince-0.8.3/prince/mca.py` & `prince-0.9.0/prince/mca.py`

 * *Files identical despite different names*

### Comparing `prince-0.8.3/prince/mfa.py` & `prince-0.9.0/prince/mfa.py`

 * *Files identical despite different names*

### Comparing `prince-0.8.3/prince/pca.py` & `prince-0.9.0/prince/pca.py`

 * *Files 1% similar despite different names*

```diff
@@ -75,16 +75,14 @@
         # https://scikit-learn.org/stable/developers/develop.html#universal-attributes
         self.feature_names_in_ = active_variables
         self.n_features_in_ = len(active_variables)
 
         X_active = X[active_variables].to_numpy(dtype=np.float64, copy=self.copy)
         if supplementary_columns:
             X_sup = X[supplementary_columns].to_numpy(dtype=np.float64, copy=self.copy)
-        # X = X.to_numpy(dtype=np.float64, copy=self.copy)
-        # self._check_input(X)
 
         # Scale datarow_contributions
         if self.rescale_with_mean or self.rescale_with_std:
             self.scaler_ = preprocessing.StandardScaler(
                 copy=self.copy,
                 with_mean=self.rescale_with_mean,
                 with_std=self.rescale_with_std,
```

### Comparing `prince-0.8.3/prince/plot.py` & `prince-0.9.0/prince/plot.py`

 * *Files identical despite different names*

### Comparing `prince-0.8.3/prince/svd.py` & `prince-0.9.0/prince/svd.py`

 * *Files identical despite different names*

### Comparing `prince-0.8.3/prince/utils.py` & `prince-0.9.0/prince/utils.py`

 * *Files identical despite different names*

### Comparing `prince-0.8.3/pyproject.toml` & `prince-0.9.0/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "prince"
-version = "0.8.3"
+version = "0.9.0"
 description = "Factor analysis in Python: PCA, CA, MCA, MFA, FAMD, GPA"
 authors = ["Max Halford <maxhalford25@gmail.com>"]
 license = "MIT"
 
 [tool.poetry.dependencies]
 python = "^3.9"
 scikit-learn = "^1.0.2"
```

### Comparing `prince-0.8.3/setup.py` & `prince-0.9.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 {'': ['*'], 'prince': ['datasets/*']}
 
 install_requires = \
 ['altair>=4.2.2,<5.0.0', 'pandas>=1.4.1,<2.0.0', 'scikit-learn>=1.0.2,<2.0.0']
 
 setup_kwargs = {
     'name': 'prince',
-    'version': '0.8.3',
+    'version': '0.9.0',
     'description': 'Factor analysis in Python: PCA, CA, MCA, MFA, FAMD, GPA',
     'long_description': 'None',
     'author': 'Max Halford',
     'author_email': 'maxhalford25@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `prince-0.8.3/PKG-INFO` & `prince-0.9.0/PKG-INFO`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: prince
-Version: 0.8.3
+Version: 0.9.0
 Summary: Factor analysis in Python: PCA, CA, MCA, MFA, FAMD, GPA
 License: MIT
 Author: Max Halford
 Author-email: maxhalford25@gmail.com
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

