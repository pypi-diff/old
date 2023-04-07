# Comparing `tmp/screcode-0.1.2.dev202304060748-py3-none-any.whl.zip` & `tmp/screcode-0.1.2.dev202304070357-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,8 +1,8 @@
-Zip file size: 118560 bytes, number of entries: 6
+Zip file size: 118804 bytes, number of entries: 6
 -rw-r--r--  2.0 unx       54 b- defN 80-Jan-01 00:00 screcode/__init__.py
 -rw-r--r--  2.0 unx   148900 b- defN 80-Jan-01 00:00 screcode/integrecode_test.ipynb
--rw-r--r--  2.0 unx    56591 b- defN 80-Jan-01 00:00 screcode/screcode.py
--rw-r--r--  2.0 unx     1244 b- defN 80-Jan-01 00:00 screcode-0.1.2.dev202304060748.dist-info/METADATA
--rw-r--r--  2.0 unx       88 b- defN 80-Jan-01 00:00 screcode-0.1.2.dev202304060748.dist-info/WHEEL
-?rw-r--r--  2.0 unx      500 b- defN 16-Jan-01 00:00 screcode-0.1.2.dev202304060748.dist-info/RECORD
-6 files, 207377 bytes uncompressed, 117656 bytes compressed:  43.3%
+-rw-r--r--  2.0 unx    57519 b- defN 80-Jan-01 00:00 screcode/screcode.py
+-rw-r--r--  2.0 unx     1244 b- defN 80-Jan-01 00:00 screcode-0.1.2.dev202304070357.dist-info/METADATA
+-rw-r--r--  2.0 unx       88 b- defN 80-Jan-01 00:00 screcode-0.1.2.dev202304070357.dist-info/WHEEL
+?rw-r--r--  2.0 unx      500 b- defN 16-Jan-01 00:00 screcode-0.1.2.dev202304070357.dist-info/RECORD
+6 files, 208305 bytes uncompressed, 117900 bytes compressed:  43.4%
```

## zipnote {}

```diff
@@ -3,17 +3,17 @@
 
 Filename: screcode/integrecode_test.ipynb
 Comment: 
 
 Filename: screcode/screcode.py
 Comment: 
 
-Filename: screcode-0.1.2.dev202304060748.dist-info/METADATA
+Filename: screcode-0.1.2.dev202304070357.dist-info/METADATA
 Comment: 
 
-Filename: screcode-0.1.2.dev202304060748.dist-info/WHEEL
+Filename: screcode-0.1.2.dev202304070357.dist-info/WHEEL
 Comment: 
 
-Filename: screcode-0.1.2.dev202304060748.dist-info/RECORD
+Filename: screcode-0.1.2.dev202304070357.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## screcode/screcode.py

```diff
@@ -5,30 +5,30 @@
 import matplotlib
 import matplotlib.pyplot as plt
 from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
 import numpy as np
 import sklearn.decomposition
 import scipy.sparse
 import seaborn as sns
-import time
-import warnings
+import logging
 
 
 
 class RECODE():
 	def __init__(
 		self,
 		fast_algorithm = True,
 		fast_algorithm_ell_ub = 1000,
 		seq_target = 'RNA',
 		version = 1,
 		stat_learning = False,
 		stat_learning_rate = 0.2,
 		stat_learning_seed = 0,
 		decimals = 5,
+		RECODE_key = 'RECODE',
 		anndata_key = 'obsm',
 		verbose = True,
 		):
 		""" 
 		RECODE (Resolution of curse of dimensionality in single-cell data analysis). A noise reduction method for single-cell sequencing data. 
 		
 		Parameters
@@ -72,36 +72,39 @@
 		self.fast_algorithm_ell_ub = fast_algorithm_ell_ub
 		self.seq_target = seq_target
 		self.version = version
 		self.stat_learning = stat_learning
 		self.stat_learning_rate = stat_learning_rate
 		self.stat_learning_seed = stat_learning_seed
 		self.decimals = decimals
+		self.RECODE_key = RECODE_key
 		self.anndata_key = anndata_key
 		self.verbose = verbose
 		self.unit,self.Unit = 'gene','Gene'
 		if seq_target == 'ATAC':
 			self.unit,self.Unit = 'peak','Peak'
 		self.log_ = {}
 		self.log_['seq_target'] = self.seq_target
 		self.fit_idx = False
+		self.logger = logging.getLogger("argument checking")
+		self.logger.setLevel(logging.WARNING)
 
 	def _check_datatype(
 		self,
 		X
 	):
 		if type(X) == anndata._core.anndata.AnnData:
 			if scipy.sparse.issparse(X.X):
 				return X.X.toarray()
 			elif type(X.X) == np.ndarray:
 				return X.X
 			else:
 				raise TypeError("Data type error: ndarray or anndata is available.")
 		elif scipy.sparse.issparse(X):
-			warnings.warn('RECODE does not support sparse input. The input and output are transformed as regular matricies. ')
+			self.logger.warning('RECODE does not support sparse input. The input and output are transformed as regular matricies. ')
 			return X.toarray()
 		elif type(X) == np.ndarray:
 			return X
 		else:
 			raise TypeError("Data type error: ndarray or anndata is available.")
 	
 
@@ -179,14 +182,17 @@
 		Parameters
 		----------
 		X : ndarray or anndata of shape (n_samples, n_features).
 			single-cell sequencing data matrix (row:cell, culumn:gene/peak).
 
 		"""	
 		X_mat = self._check_datatype(X)
+		if X_mat.dtype == np.int64:
+			self.logger.warning("Acceleration error: the value of ell may not be optimal. Set 'fast_algorithm=False' or larger fast_algorithm_ell_ub.\n"
+			"Ex. X_new = screcode.RECODE(fast_algorithm=False).fit_transform(X)")
 		self.idx_nonsilent = np.sum(X_mat,axis=0) > 0
 		self.X_temp = X_mat[:,self.idx_nonsilent]
 		if self.seq_target == 'ATAC':
 			self.X_temp = self._ATAC_preprocessing(self.X_temp)
 		
 		X_nUMI = np.sum(self.X_temp,axis=1)
 		X_scaled = (self.X_temp.T/X_nUMI).T
@@ -241,15 +247,15 @@
 		X_norm_RECODE = self.recode_.transform(X_norm)
 		X_RECODE = np.zeros(X_mat.shape,dtype=float)
 		X_RECODE[:,self.idx_nonsilent] = self._inv_noise_variance_stabilizing_normalization(X_norm_RECODE)
 		X_RECODE = np.where(X_RECODE>0,X_RECODE,0)
 		self.log_['#silent %ss' % self.unit] = sum(np.sum(X_mat,axis=0)==0)
 		self.log_['ell'] = self.recode_.ell
 		if self.recode_.ell == self.fast_algorithm_ell_ub:
-			warnings.warn("Acceleration error: the value of ell may not be optimal. Set 'fast_algorithm=False' or larger fast_algorithm_ell_ub.\n"
+			self.logger.warning("Acceleration error: the value of ell may not be optimal. Set 'fast_algorithm=False' or larger fast_algorithm_ell_ub.\n"
 			"Ex. X_new = screcode.RECODE(fast_algorithm=False).fit_transform(X)")
 		self.X_trans = np.round(X_mat,decimals=self.decimals)
 		self.X_RECODE = X_RECODE
 		self.noise_variance_ = np.zeros(X_mat.shape[1],dtype=float)
 		self.noise_variance_[self.idx_nonsilent] =  self.noise_var
 		self.normalized_variance_ = np.zeros(X_mat.shape[1],dtype=float)
 		self.normalized_variance_[self.idx_nonsilent] =  self.X_norm_var
@@ -291,19 +297,25 @@
 		X_new : ndarray/anndata (the same format as input)
 			Denoised data matrix.
 		"""
 		start_time = datetime.datetime.now()
 		if self.verbose:
 			print('start RECODE for sc%s-seq' % self.seq_target)
 		if self.stat_learning:
+			if X.shape[0] < 10000:
+				self.logger.warning("Warning: The stat_learning option is for data with a large number of cells (>20000). \n"
+				"No use of the stat_learning option is recommended to keep the accuracy.")
 			np.random.seed(self.stat_learning_seed)
 			X_mat = self._check_datatype(X)
-			cell_stat = np.random.choice(X_mat.shape[0],int(self.stat_learning_rate*X.shape[0]),replace=False)
+			cell_stat = np.random.choice(X_mat.shape[0],int(self.stat_learning_rate*X.shape[0]),replace=False)					
 			self.fit(X_mat[cell_stat])
 		else:
+			if X.shape[0] > 20000:
+				self.logger.warning("Warning: RECODE uses high computational resources for data with a large number of cells. \n"
+				"Use of the stat_learning option is recommended as \"RECODE(stat_learning=True)\". ")
 			self.fit(X)
 		X_RECODE = self.transform(X)
 		end_time = datetime.datetime.now()
 		elapsed_time = end_time - start_time
 		hours, remainder = divmod(elapsed_time.seconds, 3600)
 		minutes, seconds = divmod(remainder, 60)
 		milliseconds = int(elapsed_time.microseconds / 1000)
@@ -347,15 +359,15 @@
 		X_norm_RECODE_merge = self.harmony.Z_corr.T
 		X_RECODE = np.zeros(X_mat.shape,dtype=float)
 		X_RECODE[:,self.idx_nonsilent] = self._inv_noise_variance_stabilizing_normalization(X_norm_RECODE_merge)
 		X_RECODE = np.where(X_RECODE>0,X_RECODE,0)
 		self.log_['#silent %ss' % self.unit] = sum(np.sum(X_mat,axis=0)==0)
 		self.log_['ell'] = self.recode_.ell
 		if self.recode_.ell == self.fast_algorithm_ell_ub:
-			warnings.warn("Acceleration error: the value of ell may not be optimal. Set 'fast_algorithm=False' or larger fast_algorithm_ell_ub.\n"
+			self.logger.warning("Acceleration error: the value of ell may not be optimal. Set 'fast_algorithm=False' or larger fast_algorithm_ell_ub.\n"
 			"Ex. X_new = screcode.RECODE(fast_algorithm=False).fit_transform(X)")
 		self.X_trans = np.round(X_mat,decimals=self.decimals)
 		self.X_RECODE = X_RECODE
 		self.noise_variance_ = np.zeros(X_mat.shape[1],dtype=float)
 		self.noise_variance_[self.idx_nonsilent] =  self.noise_var
 		self.normalized_variance_ = np.zeros(X_mat.shape[1],dtype=float)
 		self.normalized_variance_[self.idx_nonsilent] =  self.X_norm_var
@@ -367,18 +379,18 @@
 		self.significance_ = np.empty(X.shape[1],dtype=object)
 		self.significance_[self.normalized_variance_==0] = 'silent'
 		self.significance_[self.normalized_variance_>0] = 'non-significant'
 		self.significance_[self.normalized_variance_>1] = 'significant'
 
 		if type(X) == anndata._core.anndata.AnnData:
 			X_out = anndata.AnnData.copy(X)
-			X_out.obsm['RECODE'] = X_RECODE
-			X_out.var['noise_variance_RECODE'] = self.noise_variance_
-			X_out.var['normalized_variance_RECODE'] = self.normalized_variance_
-			X_out.var['significance_RECODE'] = self.significance_
+			X_out.obsm[self.RECODE_key] = X_RECODE
+			X_out.var['noise_variance_%s' % self.RECODE_key] = self.noise_variance_
+			X_out.var['normalized_variance_%s' % self.RECODE_key] = self.normalized_variance_
+			X_out.var['significance_%s' % self.RECODE_key] = self.significance_
 		else:
 			X_out = X_RECODE
 
 		return X_out
 
 	def fit_transform_integration(
 			self,
@@ -1268,15 +1280,15 @@
 		ax1.set_ylabel('Coefficient of variation',fontsize=fs_label)
 		ax1.set_title(titles[1],fontsize=fs_title)
 		plt.gca().spines['right'].set_visible(False)
 		plt.gca().spines['top'].set_visible(False)
 		
 		if show_features:
 			if len(index) != self.X.shape[1]:
-				warnings.warn("Warning: no index opotion or length of index did not fit X.shape[1]. Use feature numbers")
+				self.logger.warning("Warning: no index opotion or length of index did not fit X.shape[1]. Use feature numbers")
 				index = np.arange(self.X.shape[1])+1
 			detect_rate = np.sum(np.where(self.X>0,1,0),axis=0)[self.idx_nonsilent]/self.X.shape[0]
 			idx_detect_rate_n = detect_rate <= cut_detect_rate
 			idx_detect_rate_p = detect_rate >  cut_detect_rate
 			ax1.scatter(x[idx_detect_rate_n],cv[idx_detect_rate_n],color='gray',s=ps,label='detection rate <= {:.2%}'.format(cut_detect_rate),alpha=0.5)
 			ax1.scatter(x[idx_detect_rate_p],cv[idx_detect_rate_p],color='b',s=ps,label='detection rate > {:.2%}'.format(cut_detect_rate),alpha=0.5)
 			ax1.legend(loc='upper center',bbox_to_anchor=(0.5, -0.15),ncol=2,fontsize=12,markerscale=2)
@@ -1325,15 +1337,15 @@
 		save_format : {'png', 'pdf', 'svg'}, default= 'png',
 			File format of save figure. 
 		
 		dpi: float or None, default=None
 			Dots per inch.
 		"""
 		if self.seq_target != 'ATAC':
-			warnings.warn("Error: plot_ATAC_preprocessing is an option of scATAC-seq data")
+			self.logger.warning("Error: plot_ATAC_preprocessing is an option of scATAC-seq data")
 			return
 		ps = 1
 		fs_title = 16
 		fs_label = 14
 		fs_legend = 14
 		val,count = np.unique(self.X_trans,return_counts=True)
 		idx_even = np.empty(len(val),dtype=bool)
@@ -1571,15 +1583,15 @@
 		X_var  = np.var(X,axis=0,ddof=1)
 		dim = np.sum(X_var>0)
 		noise_var = 1
 		if self.variance_estimate:
 			self.noise_var = self._noise_var_est(X)
 		thrshold = (dim-np.arange(n_pca))*noise_var
 		if np.sum(PCA_Ev_sum-thrshold<0) == 0:
-			warnings.warn("Acceleration error: the optimal value of ell is larger than fast_algorithm_ell_ub. Set larger fast_algorithm_ell_ub than %d or 'fast_algorithm=False'" % self.fast_algorithm_ell_ub)
+			self.logger.warning("Acceleration error: the optimal value of ell is larger than fast_algorithm_ell_ub. Set larger fast_algorithm_ell_ub than %d or 'fast_algorithm=False'" % self.fast_algorithm_ell_ub)
 			comp = n_pca
 		else:
 			comp = np.min(np.arange(n_pca)[PCA_Ev_sum-thrshold<0])
 		self.ell_max = np.min([n,d,np.sum(PCA_Ev>1.0e-10)])
 		self.ell = comp
 		if self.ell > self.ell_max:
 			self.ell = self.ell_max
```

## Comparing `screcode-0.1.2.dev202304060748.dist-info/METADATA` & `screcode-0.1.2.dev202304070357.dist-info/METADATA`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: screcode
-Version: 0.1.2.dev202304060748
+Version: 0.1.2.dev202304070357
 Summary: RECODE - resolution of the curse of dimensionality in single-cell data analysis
 Home-page: https://github.com/yusuke-imoto-lab/RECODE
 Author: Yusuke Imoto
 Requires-Python: >=3.8,<3.11
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

