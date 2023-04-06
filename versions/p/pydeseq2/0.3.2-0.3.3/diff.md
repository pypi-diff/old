# Comparing `tmp/pydeseq2-0.3.2.tar.gz` & `tmp/pydeseq2-0.3.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/Users/bmuzellec/Documents/Projects/FL_genomics/PyDESeq2/dist/.tmp-cebvpl6a/pydeseq2-0.3.2.tar", last modified: Mon Apr  3 08:26:16 2023, max compression
+gzip compressed data, was "/Users/bmuzellec/Documents/Projects/FL_genomics/PyDESeq2/dist/.tmp-2p0keonu/pydeseq2-0.3.3.tar", last modified: Thu Apr  6 14:08:46 2023, max compression
```

## Comparing `pydeseq2-0.3.2.tar` & `pydeseq2-0.3.3.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxr-xr-x   0 bmuzellec   (501) staff       (20)        0 2023-04-03 08:26:16.000000 pydeseq2-0.3.2/
--rw-r--r--   0 bmuzellec   (501) staff       (20)     1062 2022-12-03 17:11:22.000000 pydeseq2-0.3.2/LICENSE
--rw-r--r--   0 bmuzellec   (501) staff       (20)     6068 2023-04-03 08:26:16.000000 pydeseq2-0.3.2/PKG-INFO
--rw-r--r--   0 bmuzellec   (501) staff       (20)     5735 2023-03-23 13:57:51.000000 pydeseq2-0.3.2/README.md
-drwxr-xr-x   0 bmuzellec   (501) staff       (20)        0 2023-04-03 08:26:16.000000 pydeseq2-0.3.2/pydeseq2/
--rw-r--r--   0 bmuzellec   (501) staff       (20)       53 2022-12-28 09:54:14.000000 pydeseq2-0.3.2/pydeseq2/__init__.py
--rw-r--r--   0 bmuzellec   (501) staff       (20)       22 2023-04-03 08:11:53.000000 pydeseq2-0.3.2/pydeseq2/__version__.py
--rw-r--r--   0 bmuzellec   (501) staff       (20)    36351 2023-04-03 08:09:14.000000 pydeseq2-0.3.2/pydeseq2/dds.py
--rw-r--r--   0 bmuzellec   (501) staff       (20)    22047 2023-03-22 10:55:46.000000 pydeseq2-0.3.2/pydeseq2/ds.py
--rw-r--r--   0 bmuzellec   (501) staff       (20)     8480 2023-03-24 14:45:04.000000 pydeseq2-0.3.2/pydeseq2/grid_search.py
--rw-r--r--   0 bmuzellec   (501) staff       (20)     1316 2023-03-15 10:56:22.000000 pydeseq2-0.3.2/pydeseq2/preprocessing.py
--rw-r--r--   0 bmuzellec   (501) staff       (20)    37362 2023-04-03 08:09:25.000000 pydeseq2-0.3.2/pydeseq2/utils.py
-drwxr-xr-x   0 bmuzellec   (501) staff       (20)        0 2023-04-03 08:26:16.000000 pydeseq2-0.3.2/pydeseq2.egg-info/
--rw-r--r--   0 bmuzellec   (501) staff       (20)     6068 2023-04-03 08:26:16.000000 pydeseq2-0.3.2/pydeseq2.egg-info/PKG-INFO
--rw-r--r--   0 bmuzellec   (501) staff       (20)      436 2023-04-03 08:26:16.000000 pydeseq2-0.3.2/pydeseq2.egg-info/SOURCES.txt
--rw-r--r--   0 bmuzellec   (501) staff       (20)        1 2023-04-03 08:26:16.000000 pydeseq2-0.3.2/pydeseq2.egg-info/dependency_links.txt
--rw-r--r--   0 bmuzellec   (501) staff       (20)      190 2023-04-03 08:26:16.000000 pydeseq2-0.3.2/pydeseq2.egg-info/requires.txt
--rw-r--r--   0 bmuzellec   (501) staff       (20)        9 2023-04-03 08:26:16.000000 pydeseq2-0.3.2/pydeseq2.egg-info/top_level.txt
--rw-r--r--   0 bmuzellec   (501) staff       (20)      408 2023-03-02 10:33:44.000000 pydeseq2-0.3.2/pyproject.toml
--rw-r--r--   0 bmuzellec   (501) staff       (20)       38 2023-04-03 08:26:16.000000 pydeseq2-0.3.2/setup.cfg
--rw-r--r--   0 bmuzellec   (501) staff       (20)     1362 2023-02-20 15:16:54.000000 pydeseq2-0.3.2/setup.py
-drwxr-xr-x   0 bmuzellec   (501) staff       (20)        0 2023-04-03 08:26:16.000000 pydeseq2-0.3.2/tests/
--rw-r--r--   0 bmuzellec   (501) staff       (20)     5654 2023-02-16 10:34:42.000000 pydeseq2-0.3.2/tests/test_docstring.py
--rw-r--r--   0 bmuzellec   (501) staff       (20)    11013 2023-03-24 14:45:04.000000 pydeseq2-0.3.2/tests/test_edge_cases.py
--rw-r--r--   0 bmuzellec   (501) staff       (20)    13353 2023-03-24 14:45:04.000000 pydeseq2-0.3.2/tests/test_pydeseq2.py
--rw-r--r--   0 bmuzellec   (501) staff       (20)     1951 2023-02-21 15:32:02.000000 pydeseq2-0.3.2/tests/test_utils.py
+drwxr-xr-x   0 bmuzellec   (501) staff       (20)        0 2023-04-06 14:08:46.000000 pydeseq2-0.3.3/
+-rw-r--r--   0 bmuzellec   (501) staff       (20)     1062 2022-12-03 17:11:22.000000 pydeseq2-0.3.3/LICENSE
+-rw-r--r--   0 bmuzellec   (501) staff       (20)     6066 2023-04-06 14:08:46.000000 pydeseq2-0.3.3/PKG-INFO
+-rw-r--r--   0 bmuzellec   (501) staff       (20)     5733 2023-04-06 08:39:13.000000 pydeseq2-0.3.3/README.md
+drwxr-xr-x   0 bmuzellec   (501) staff       (20)        0 2023-04-06 14:08:46.000000 pydeseq2-0.3.3/pydeseq2/
+-rw-r--r--   0 bmuzellec   (501) staff       (20)       53 2022-12-28 09:54:14.000000 pydeseq2-0.3.3/pydeseq2/__init__.py
+-rw-r--r--   0 bmuzellec   (501) staff       (20)       22 2023-04-06 14:03:10.000000 pydeseq2-0.3.3/pydeseq2/__version__.py
+-rw-r--r--   0 bmuzellec   (501) staff       (20)    36609 2023-04-06 14:02:20.000000 pydeseq2-0.3.3/pydeseq2/dds.py
+-rw-r--r--   0 bmuzellec   (501) staff       (20)    22038 2023-04-06 14:02:20.000000 pydeseq2-0.3.3/pydeseq2/ds.py
+-rw-r--r--   0 bmuzellec   (501) staff       (20)     8480 2023-03-24 14:45:04.000000 pydeseq2-0.3.3/pydeseq2/grid_search.py
+-rw-r--r--   0 bmuzellec   (501) staff       (20)     1316 2023-03-15 10:56:22.000000 pydeseq2-0.3.3/pydeseq2/preprocessing.py
+-rw-r--r--   0 bmuzellec   (501) staff       (20)    37616 2023-04-06 14:02:20.000000 pydeseq2-0.3.3/pydeseq2/utils.py
+drwxr-xr-x   0 bmuzellec   (501) staff       (20)        0 2023-04-06 14:08:46.000000 pydeseq2-0.3.3/pydeseq2.egg-info/
+-rw-r--r--   0 bmuzellec   (501) staff       (20)     6066 2023-04-06 14:08:45.000000 pydeseq2-0.3.3/pydeseq2.egg-info/PKG-INFO
+-rw-r--r--   0 bmuzellec   (501) staff       (20)      436 2023-04-06 14:08:45.000000 pydeseq2-0.3.3/pydeseq2.egg-info/SOURCES.txt
+-rw-r--r--   0 bmuzellec   (501) staff       (20)        1 2023-04-06 14:08:45.000000 pydeseq2-0.3.3/pydeseq2.egg-info/dependency_links.txt
+-rw-r--r--   0 bmuzellec   (501) staff       (20)      190 2023-04-06 14:08:45.000000 pydeseq2-0.3.3/pydeseq2.egg-info/requires.txt
+-rw-r--r--   0 bmuzellec   (501) staff       (20)        9 2023-04-06 14:08:45.000000 pydeseq2-0.3.3/pydeseq2.egg-info/top_level.txt
+-rw-r--r--   0 bmuzellec   (501) staff       (20)      408 2023-04-05 09:20:58.000000 pydeseq2-0.3.3/pyproject.toml
+-rw-r--r--   0 bmuzellec   (501) staff       (20)       38 2023-04-06 14:08:46.000000 pydeseq2-0.3.3/setup.cfg
+-rw-r--r--   0 bmuzellec   (501) staff       (20)     1362 2023-02-20 15:16:54.000000 pydeseq2-0.3.3/setup.py
+drwxr-xr-x   0 bmuzellec   (501) staff       (20)        0 2023-04-06 14:08:46.000000 pydeseq2-0.3.3/tests/
+-rw-r--r--   0 bmuzellec   (501) staff       (20)     5654 2023-02-16 10:34:42.000000 pydeseq2-0.3.3/tests/test_docstring.py
+-rw-r--r--   0 bmuzellec   (501) staff       (20)    11010 2023-04-06 14:02:20.000000 pydeseq2-0.3.3/tests/test_edge_cases.py
+-rw-r--r--   0 bmuzellec   (501) staff       (20)    14231 2023-04-06 14:02:20.000000 pydeseq2-0.3.3/tests/test_pydeseq2.py
+-rw-r--r--   0 bmuzellec   (501) staff       (20)     1951 2023-02-21 15:32:02.000000 pydeseq2-0.3.3/tests/test_utils.py
```

### Comparing `pydeseq2-0.3.2/LICENSE` & `pydeseq2-0.3.3/LICENSE`

 * *Files identical despite different names*

### Comparing `pydeseq2-0.3.2/PKG-INFO` & `pydeseq2-0.3.3/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pydeseq2
-Version: 0.3.2
+Version: 0.3.3
 Summary: A python implementation of DESeq2.
 Author: Boris Muzellec, Maria Telenczuk, Vincent Cabelli and Mathieu Andreux
 Author-email: boris.muzellec@owkin.com
 License: MIT
 Requires-Python: >=3.8.0
 Description-Content-Type: text/markdown
 Provides-Extra: dev
@@ -36,15 +36,15 @@
 method [1] for differential expression analysis (DEA) with bulk RNA-seq data, originally in R.
 It aims to facilitate DEA experiments for python users.
 
 As PyDESeq2 is a re-implementation of [DESeq2](https://bioconductor.org/packages/release/bioc/html/DESeq2.html) from 
 scratch, you may experience some differences in terms of retrieved values or available features.
 
 Currently, available features broadly correspond to the default settings of DESeq2 (v1.34.0) for single-factor 
-and paired multi-factor analysis (with bi-level factors), but we plan to implement more in the near future.
+and paired multi-factor analysis (with categorical factors), but we plan to implement more in the future.
 In case there is a feature you would particularly like to be implemented, feel free to open an issue.
 
 ## Installation
 
 `PyDESeq2` can be installed from PyPI:
 
 `pip install pydeseq2`
```

### Comparing `pydeseq2-0.3.2/README.md` & `pydeseq2-0.3.3/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -24,15 +24,15 @@
 method [1] for differential expression analysis (DEA) with bulk RNA-seq data, originally in R.
 It aims to facilitate DEA experiments for python users.
 
 As PyDESeq2 is a re-implementation of [DESeq2](https://bioconductor.org/packages/release/bioc/html/DESeq2.html) from 
 scratch, you may experience some differences in terms of retrieved values or available features.
 
 Currently, available features broadly correspond to the default settings of DESeq2 (v1.34.0) for single-factor 
-and paired multi-factor analysis (with bi-level factors), but we plan to implement more in the near future.
+and paired multi-factor analysis (with categorical factors), but we plan to implement more in the future.
 In case there is a feature you would particularly like to be implemented, feel free to open an issue.
 
 ## Installation
 
 `PyDESeq2` can be installed from PyPI:
 
 `pip install pydeseq2`
```

### Comparing `pydeseq2-0.3.2/pydeseq2/dds.py` & `pydeseq2-0.3.3/pydeseq2/dds.py`

 * *Files 1% similar despite different names*

```diff
@@ -34,15 +34,14 @@
 from pydeseq2.utils import trimmed_mean
 
 # Ignore DomainWarning raised by statsmodels when fitting a Gamma GLM with identity link.
 warnings.simplefilter("ignore", DomainWarning)
 # Ignore AnnData's FutureWarning about implicit data conversion.
 warnings.simplefilter("ignore", FutureWarning)
 
-
 # TODO: implement a quiet (non-verbose) mode ?
 
 
 class DeseqDataSet(ad.AnnData):
     r"""A class to implement dispersion and log fold-change (LFC) estimation.
 
     The DeseqDataSet extends the `AnnData class
@@ -66,18 +65,18 @@
         DataFrame containing clinical information.
         Must be indexed by sample barcodes.
 
     design_factors : str or list
         Name of the columns of clinical to be used as design variables.
         Only bi-level factors are supported. (default: ``'condition'``).
 
-    tested_level : list or None
+    ref_level : list or None
         An optional list of two strings of the form ``["factor", "test_level"]``
-        specifying the factor of interest and the (non-control) level we're testing, e.g.
-        ``["condition", "B"]``. (default: ``None``).
+        specifying the factor of interest and the reference (control) level against which
+        we're testing, e.g. ``["condition", "A"]``. (default: ``None``).
 
     min_mu : float
         Threshold for mean estimates. (default: ``0.5``).
 
     min_disp : float
         Lower threshold for dispersion parameters. (default: ``1e-8``).
 
@@ -160,15 +159,15 @@
     def __init__(
         self,
         *,
         adata: Optional[ad.AnnData] = None,
         counts: Optional[pd.DataFrame] = None,
         clinical: Optional[pd.DataFrame] = None,
         design_factors: Union[str, List[str]] = "condition",
-        tested_level: Optional[List[str]] = None,
+        ref_level: Optional[List[str]] = None,
         min_mu: float = 0.5,
         min_disp: float = 1e-8,
         max_disp: float = 10.0,
         refit_cooks: bool = True,
         min_replicates: int = 7,
         beta_tol: float = 1e-8,
         n_cpus: Optional[int] = None,
@@ -201,15 +200,15 @@
         self.obs[self.design_factors] = self.obs[self.design_factors].astype(str)
 
         # Build the design matrix
         # Stored in the obsm attribute of the dataset
         self.obsm["design_matrix"] = build_design_matrix(
             clinical_df=self.obs,
             design_factors=self.design_factors,
-            tested_level=tested_level,
+            ref_level=ref_level,
             expanded=False,
             intercept=True,
         )
 
         self.min_mu = min_mu
         self.min_disp = min_disp
         self.max_disp = np.maximum(max_disp, self.n_obs)
@@ -760,63 +759,65 @@
         self.obsm["replaceable"] = replaceable.values
 
         # Get positions of counts with cooks above threshold
         cooks_cutoff = f.ppf(0.99, num_vars, num_samples - num_vars)
         idx = self.layers["cooks"] > cooks_cutoff
         self.varm["replaced"] = idx.any(axis=0)
 
-        # Compute replacement counts: trimmed means * size_factors
-        self.counts_to_refit = self[:, self.varm["replaced"]].copy()
+        if sum(self.varm["replaced"] > 0):
+            # Compute replacement counts: trimmed means * size_factors
+            self.counts_to_refit = self[:, self.varm["replaced"]].copy()
 
-        trim_base_mean = pd.DataFrame(
-            cast(
-                np.ndarray,
-                trimmed_mean(
-                    self.counts_to_refit.X / self.obsm["size_factors"][:, None],
-                    trim=0.2,
-                    axis=0,
+            trim_base_mean = pd.DataFrame(
+                cast(
+                    np.ndarray,
+                    trimmed_mean(
+                        self.counts_to_refit.X / self.obsm["size_factors"][:, None],
+                        trim=0.2,
+                        axis=0,
+                    ),
                 ),
-            ),
-            index=self.counts_to_refit.var_names,
-        )
-
-        replacement_counts = (
-            pd.DataFrame(
-                trim_base_mean.values * self.obsm["size_factors"],
                 index=self.counts_to_refit.var_names,
-                columns=self.counts_to_refit.obs_names,
             )
-            .astype(int)
-            .T
-        )
 
-        if sum(self.varm["replaced"] > 0):
+            replacement_counts = (
+                pd.DataFrame(
+                    trim_base_mean.values * self.obsm["size_factors"],
+                    index=self.counts_to_refit.var_names,
+                    columns=self.counts_to_refit.obs_names,
+                )
+                .astype(int)
+                .T
+            )
+
             self.counts_to_refit.X[
                 self.obsm["replaceable"][:, None] & idx[:, self.varm["replaced"]]
             ] = replacement_counts.values[
                 self.obsm["replaceable"][:, None] & idx[:, self.varm["replaced"]]
             ]
 
     def _refit_without_outliers(
         self,
     ) -> None:
         """Re-run the whole DESeq2 pipeline with replaced outliers."""
         assert (
             self.refit_cooks
         ), "Trying to refit Cooks outliers but the 'refit_cooks' flag is set to False"
 
-        # Check that replaced counts are available. If not, compute them.
-        if not hasattr(self, "counts_to_refit"):
+        # Check that _replace_outliers() was previously run.
+        if "replaced" not in self.varm:
             self._replace_outliers()
 
         # Only refit genes for which replacing outliers hasn't resulted in all zeroes
         new_all_zeroes = (self.counts_to_refit.X == 0).all(axis=0)
         self.new_all_zeroes_genes = self.counts_to_refit.var_names[new_all_zeroes]
-        self.counts_to_refit = self.counts_to_refit[:, ~new_all_zeroes].copy()
+        if (~new_all_zeroes).sum() == 0:  # if no gene can be refit, we can skip
+            return
 
+        self.counts_to_refit = self.counts_to_refit[:, ~new_all_zeroes].copy()
         if isinstance(self.new_all_zeroes_genes, pd.MultiIndex):
             raise ValueError
 
         sub_dds = DeseqDataSet(
             counts=pd.DataFrame(
                 self.counts_to_refit.X,
                 index=self.counts_to_refit.obs_names,
@@ -871,18 +872,21 @@
         self.varm["dispersions"][to_replace] = sub_dds.varm["dispersions"]
 
         replace_cooks = pd.DataFrame(self.layers["cooks"].copy())
         replace_cooks.loc[self.obsm["replaceable"], to_replace] = 0.0
 
         self.layers["replace_cooks"] = replace_cooks
         # Take into account new all-zero genes
-        self[:, self.new_all_zeroes_genes].varm["_normed_means"] = np.zeros(
-            new_all_zeroes.sum()
-        )
-        self[:, self.new_all_zeroes_genes].varm["LFC"] = np.zeros(new_all_zeroes.sum())
+        if (new_all_zeroes).sum() > 0:
+            self[:, self.new_all_zeroes_genes].varm["_normed_means"] = np.zeros(
+                new_all_zeroes.sum()
+            )
+            self[:, self.new_all_zeroes_genes].varm["LFC"] = np.zeros(
+                new_all_zeroes.sum()
+            )
 
     def _fit_iterate_size_factors(self, niter: int = 10, quant: float = 0.95) -> None:
         """
         Fit size factors using the ``iterative`` method.
 
         Used when each gene has at least one zero.
```

### Comparing `pydeseq2-0.3.2/pydeseq2/ds.py` & `pydeseq2-0.3.3/pydeseq2/ds.py`

 * *Files 2% similar despite different names*

```diff
@@ -31,15 +31,15 @@
     Parameters
     ----------
     dds : DeseqDataSet
         DeseqDataSet for which dispersion and LFCs were already estimated.
 
     contrast : list or None
         A list of three strings, in the following format:
-        ``['variable_of_interest', 'tested_level', 'tested_level']``.
+        ``['variable_of_interest', 'tested_level', 'ref_level']``.
         Names must correspond to the clinical data passed to the DeseqDataSet.
         E.g., ``['condition', 'B', 'A']`` will measure the LFC of 'condition B' compared
         to 'condition A'. If None, the last variable from the design matrix is chosen
         as the variable of interest, and the reference level is picked alphabetically.
         (default: ``None``).
 
     alpha : float
@@ -273,21 +273,21 @@
         Shrinks LFCs using a heavy-tailed Cauchy prior, leaving p-values unchanged.
 
         Parameters
         ----------
         coeff : str
             The LFC coefficient to shrink.
             If the desired coefficient is not available, it may be set from the
-            :class:`pydeseq2.dds.DeseqDataSet` argument ``tested_level``.
+            :class:`pydeseq2.dds.DeseqDataSet` argument ``ref_level``.
         """
 
         if coeff not in self.LFC.columns:
             raise KeyError(
                 f"The coeff argument ('{coeff}') should be one the LFC columns. "
-                f"If not available,  it can be set from DeseqDataSet's `tested_level` "
+                f"If not available,  it can be set from DeseqDataSet's `ref_level` "
                 f"argument."
             )
 
         coeff_idx = self.LFC.columns.get_loc(coeff)
 
         size = 1.0 / self.dds.varm["dispersions"]
         offset = np.log(self.dds.obsm["size_factors"])
```

### Comparing `pydeseq2-0.3.2/pydeseq2/grid_search.py` & `pydeseq2-0.3.3/pydeseq2/grid_search.py`

 * *Files identical despite different names*

### Comparing `pydeseq2-0.3.2/pydeseq2/preprocessing.py` & `pydeseq2-0.3.3/pydeseq2/preprocessing.py`

 * *Files identical despite different names*

### Comparing `pydeseq2-0.3.2/pydeseq2/utils.py` & `pydeseq2-0.3.3/pydeseq2/utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -135,15 +135,15 @@
     if (counts < 0).any().any():
         raise ValueError("The count matrix should only contain non-negative values.")
 
 
 def build_design_matrix(
     clinical_df: pd.DataFrame,
     design_factors: Union[str, List[str]] = "condition",
-    tested_level: Optional[List[str]] = None,
+    ref_level: Optional[List[str]] = None,
     expanded: bool = False,
     intercept: bool = True,
 ) -> pd.DataFrame:
     """Build design_matrix matrix for DEA.
 
     Only single factor, 2-level designs are currently supported.
     Unless specified, the reference factor is chosen alphabetically.
@@ -155,19 +155,18 @@
         DataFrame containing clinical information.
         Must be indexed by sample barcodes.
 
     design_factors : str or list
         Name of the columns of clinical_df to be used as design_matrix variables.
         (default: ``"condition"``).
 
-    tested_level : list or None
+    ref_level : list or None
         An optional list of two strings of the form ``["factor", "ref_level"]``
         specifying the factor of interest and the desired reference level, e.g.
-        ``["condition", "A"]``.
-        (default: ``None``).
+        ``["condition", "A"]``. (default: ``None``).
 
     expanded : bool
         If true, use one column per category. Else, use a single column.
         (default: ``False``).
 
     intercept : bool
         If true, add an intercept (a column containing only ones). (default: ``True``).
@@ -190,54 +189,61 @@
             raise ValueError(
                 f"Factors should take at least two values, but {factor} "
                 f"takes the single value '{np.unique(clinical_df[factor])}'."
             )
 
     design_matrix = pd.get_dummies(clinical_df[design_factors], drop_first=not expanded)
 
-    if tested_level is not None:
-        if len(tested_level) != 2:
-            raise KeyError("The tested level should contain 2 strings.")
-        if tested_level[1] not in clinical_df[tested_level[0]].values:
+    if ref_level is not None:
+        if len(ref_level) != 2:
+            raise KeyError("The reference level should contain 2 strings.")
+        if ref_level[1] not in clinical_df[ref_level[0]].values:
             raise KeyError(
-                f"The clinical data should contain a '{tested_level[0]}' column"
-                f" with a '{tested_level[1]}' level."
+                f"The clinical data should contain a '{ref_level[0]}' column"
+                f" with a '{ref_level[1]}' level."
             )
 
-        # Check that the reference level is still in the matrix
-        test_level = "_".join(tested_level)
-        if test_level not in design_matrix.columns:
-            # Add the desired level and remove one
+        # Check that the reference level is not in the matrix (if unexpanded design)
+        ref_level_name = "_".join(ref_level)
+        if (not expanded) and ref_level_name in design_matrix.columns:
+            # Remove the reference level and add one
             factor_cols = [
-                col for col in design_matrix.columns if col.startswith(tested_level[0])
+                col for col in design_matrix.columns if col.startswith(ref_level[0])
             ]
-            design_matrix[test_level] = 1 - design_matrix[factor_cols].sum(1)
-            design_matrix.drop(factor_cols[0], axis="columns", inplace=True)
+            missing_level = next(
+                level
+                for level in np.unique(clinical_df[ref_level[0]])
+                if f"{ref_level[0]}_{level}" not in design_matrix.columns
+            )
+            design_matrix[f"{ref_level[0]}_{missing_level}"] = 1 - design_matrix[
+                factor_cols
+            ].sum(1)
+            design_matrix.drop(ref_level_name, axis="columns", inplace=True)
 
     if not expanded:
         # Add reference level as column name suffix
         for factor in design_factors:
-            if tested_level is not None and factor == tested_level[0]:
+            if ref_level is None or factor != ref_level[0]:
                 # The reference is the unique level that is no longer there
                 ref = next(
                     level
-                    for level in clinical_df[factor]
+                    for level in np.unique(clinical_df[factor])
                     if f"{factor}_{level}" not in design_matrix.columns
                 )
             else:
-                # The first level is the one that should have been dropped
-                ref = np.unique(clinical_df[factor])[0]
+                # The reference level is given as an argument
+                ref = ref_level[1]
             design_matrix.columns = [
                 f"{col}_vs_{ref}" if col.startswith(factor) else col
                 for col in design_matrix.columns
             ]
 
     if intercept:
         design_matrix.insert(0, "intercept", 1)
-    return design_matrix
+    return design_matrix.astype("int")
 
 
 def dispersion_trend(
     normed_mean: Union[float, np.ndarray],
     coeffs: Union["pd.Series[float]", np.ndarray],
 ) -> Union[float, np.ndarray]:
     r"""Return dispersion trend from normalized counts.
```

### Comparing `pydeseq2-0.3.2/pydeseq2.egg-info/PKG-INFO` & `pydeseq2-0.3.3/pydeseq2.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pydeseq2
-Version: 0.3.2
+Version: 0.3.3
 Summary: A python implementation of DESeq2.
 Author: Boris Muzellec, Maria Telenczuk, Vincent Cabelli and Mathieu Andreux
 Author-email: boris.muzellec@owkin.com
 License: MIT
 Requires-Python: >=3.8.0
 Description-Content-Type: text/markdown
 Provides-Extra: dev
@@ -36,15 +36,15 @@
 method [1] for differential expression analysis (DEA) with bulk RNA-seq data, originally in R.
 It aims to facilitate DEA experiments for python users.
 
 As PyDESeq2 is a re-implementation of [DESeq2](https://bioconductor.org/packages/release/bioc/html/DESeq2.html) from 
 scratch, you may experience some differences in terms of retrieved values or available features.
 
 Currently, available features broadly correspond to the default settings of DESeq2 (v1.34.0) for single-factor 
-and paired multi-factor analysis (with bi-level factors), but we plan to implement more in the near future.
+and paired multi-factor analysis (with categorical factors), but we plan to implement more in the future.
 In case there is a feature you would particularly like to be implemented, feel free to open an issue.
 
 ## Installation
 
 `PyDESeq2` can be installed from PyPI:
 
 `pip install pydeseq2`
```

### Comparing `pydeseq2-0.3.2/setup.py` & `pydeseq2-0.3.3/setup.py`

 * *Files identical despite different names*

### Comparing `pydeseq2-0.3.2/tests/test_docstring.py` & `pydeseq2-0.3.3/tests/test_docstring.py`

 * *Files identical despite different names*

### Comparing `pydeseq2-0.3.2/tests/test_edge_cases.py` & `pydeseq2-0.3.3/tests/test_edge_cases.py`

 * *Files 0% similar despite different names*

```diff
@@ -135,15 +135,15 @@
     clinical_df = pd.DataFrame({"condition": [0, 1]}, index=["sample1", "sample2"])
 
     with pytest.raises(KeyError):
         DeseqDataSet(
             counts=counts_df,
             clinical=clinical_df,
             design_factors="condition",
-            tested_level="control",
+            ref_level="control",
         )
 
 
 def test_lfc_shrinkage_coeff():
     """Test that a KeyError is thrown when attempting to shrink an unexisting LFC
     coefficient.
     """
```

### Comparing `pydeseq2-0.3.2/tests/test_pydeseq2.py` & `pydeseq2-0.3.3/tests/test_pydeseq2.py`

 * *Files 3% similar despite different names*

```diff
@@ -442,7 +442,41 @@
     dds = DeseqDataSet(
         counts=counts_df, clinical=clinical_df, design_factors=["condition"]
     )
     dds.vst(use_design=True)
     assert (
         np.abs(r_vst_with_design - dds.layers["vst_counts"]) / r_vst_with_design
     ).max().max() < tol
+
+
+def test_ref_level():
+    """Test that DeseqDataSet columns are created according to the passed reference
+    level, if any.
+    """
+    counts_df = load_example_data(
+        modality="raw_counts",
+        dataset="synthetic",
+        debug=False,
+    )
+
+    clinical_df = load_example_data(
+        modality="clinical",
+        dataset="synthetic",
+        debug=False,
+    )
+
+    dds = DeseqDataSet(
+        counts=counts_df,
+        clinical=clinical_df,
+        design_factors=["group", "condition"],
+        ref_level=["group", "Y"],
+    )
+
+    # Check that the column exists
+    assert "group_X_vs_Y" in dds.obsm["design_matrix"].columns
+    # Check that its content is correct
+    assert (
+        dds.obsm["design_matrix"]["group_X_vs_Y"]
+        == clinical_df["group"].apply(
+            lambda x: 1 if x == "X" else 0 if x == "Y" else np.NaN
+        )
+    ).all()
```

### Comparing `pydeseq2-0.3.2/tests/test_utils.py` & `pydeseq2-0.3.3/tests/test_utils.py`

 * *Files identical despite different names*

