# Comparing `tmp/screcode-0.1.2.dev202304070859-py3-none-any.whl.zip` & `tmp/screcode-0.1.2.dev202304071048-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,8 +1,8 @@
-Zip file size: 118810 bytes, number of entries: 6
+Zip file size: 118869 bytes, number of entries: 6
 -rw-r--r--  2.0 unx       54 b- defN 80-Jan-01 00:00 screcode/__init__.py
 -rw-r--r--  2.0 unx   148900 b- defN 80-Jan-01 00:00 screcode/integrecode_test.ipynb
--rw-r--r--  2.0 unx    57526 b- defN 80-Jan-01 00:00 screcode/screcode.py
--rw-r--r--  2.0 unx     1244 b- defN 80-Jan-01 00:00 screcode-0.1.2.dev202304070859.dist-info/METADATA
--rw-r--r--  2.0 unx       88 b- defN 80-Jan-01 00:00 screcode-0.1.2.dev202304070859.dist-info/WHEEL
-?rw-r--r--  2.0 unx      500 b- defN 16-Jan-01 00:00 screcode-0.1.2.dev202304070859.dist-info/RECORD
-6 files, 208312 bytes uncompressed, 117906 bytes compressed:  43.4%
+-rw-r--r--  2.0 unx    57492 b- defN 80-Jan-01 00:00 screcode/screcode.py
+-rw-r--r--  2.0 unx     1244 b- defN 80-Jan-01 00:00 screcode-0.1.2.dev202304071048.dist-info/METADATA
+-rw-r--r--  2.0 unx       88 b- defN 80-Jan-01 00:00 screcode-0.1.2.dev202304071048.dist-info/WHEEL
+?rw-r--r--  2.0 unx      500 b- defN 16-Jan-01 00:00 screcode-0.1.2.dev202304071048.dist-info/RECORD
+6 files, 208278 bytes uncompressed, 117965 bytes compressed:  43.4%
```

## zipnote {}

```diff
@@ -3,17 +3,17 @@
 
 Filename: screcode/integrecode_test.ipynb
 Comment: 
 
 Filename: screcode/screcode.py
 Comment: 
 
-Filename: screcode-0.1.2.dev202304070859.dist-info/METADATA
+Filename: screcode-0.1.2.dev202304071048.dist-info/METADATA
 Comment: 
 
-Filename: screcode-0.1.2.dev202304070859.dist-info/WHEEL
+Filename: screcode-0.1.2.dev202304071048.dist-info/WHEEL
 Comment: 
 
-Filename: screcode-0.1.2.dev202304070859.dist-info/RECORD
+Filename: screcode-0.1.2.dev202304071048.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## screcode/screcode.py

```diff
@@ -78,14 +78,16 @@
 		self.decimals = decimals
 		self.RECODE_key = RECODE_key
 		self.anndata_key = anndata_key
 		self.verbose = verbose
 		self.unit,self.Unit = 'gene','Gene'
 		if seq_target == 'ATAC':
 			self.unit,self.Unit = 'peak','Peak'
+		if seq_target == 'Hi-C':
+			self.unit,self.Unit = 'bin','Bin'
 		self.log_ = {}
 		self.log_['seq_target'] = self.seq_target
 		self.fit_idx = False
 		self.logger = logging.getLogger("argument checking")
 		self.logger.setLevel(logging.WARNING)
 
 	def _check_datatype(
@@ -182,17 +184,16 @@
 		Parameters
 		----------
 		X : ndarray or anndata of shape (n_samples, n_features).
 			single-cell sequencing data matrix (row:cell, culumn:gene/peak).
 
 		"""	
 		X_mat = self._check_datatype(X)
-		if X_mat.dtype == np.int64:
-			self.logger.warning("Acceleration error: the value of ell may not be optimal. Set 'fast_algorithm=False' or larger fast_algorithm_ell_ub.\n"
-			"Ex. X_new = screcode.RECODE(fast_algorithm=False).fit_transform(X)")
+		if X_mat.dtype != np.int64:
+			self.logger.warning("Warning: RECODE is applicable for count data (integer matrix). Plese make sure the data type")
 		self.idx_nonsilent = np.sum(X_mat,axis=0) > 0
 		self.X_temp = X_mat[:,self.idx_nonsilent]
 		if self.seq_target == 'ATAC':
 			self.X_temp = self._ATAC_preprocessing(self.X_temp)
 		
 		X_nUMI = np.sum(self.X_temp,axis=1)
 		X_scaled = (self.X_temp.T/X_nUMI).T
```

## Comparing `screcode-0.1.2.dev202304070859.dist-info/METADATA` & `screcode-0.1.2.dev202304071048.dist-info/METADATA`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: screcode
-Version: 0.1.2.dev202304070859
+Version: 0.1.2.dev202304071048
 Summary: RECODE - resolution of the curse of dimensionality in single-cell data analysis
 Home-page: https://github.com/yusuke-imoto-lab/RECODE
 Author: Yusuke Imoto
 Requires-Python: >=3.8,<3.11
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

