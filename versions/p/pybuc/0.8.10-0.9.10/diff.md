# Comparing `tmp/pybuc-0.8.10.tar.gz` & `tmp/pybuc-0.9.10.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pybuc-0.8.10.tar", max compression
+gzip compressed data, was "pybuc-0.9.10.tar", max compression
```

## Comparing `pybuc-0.8.10.tar` & `pybuc-0.9.10.tar`

### file list

```diff
@@ -1,35 +1,35 @@
--rw-r--r--   0        0        0     1478 2022-08-27 12:11:19.927238 pybuc-0.8.10/LICENSE.txt
--rw-r--r--   0        0        0    24692 2022-09-09 17:23:44.140849 pybuc-0.8.10/README.md
--rw-r--r--   0        0        0   104378 2022-09-13 17:59:00.142002 pybuc-0.8.10/pybuc/buc.py
--rw-r--r--   0        0        0     3518 2022-09-07 18:18:02.664129 pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.cpython-39.pyc
--rw-r--r--   0        0        0   730238 2022-08-31 02:33:45.538938 pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.1.nbc
--rw-r--r--   0        0        0   671886 2022-08-27 12:11:19.963238 pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.2.nbc
--rw-r--r--   0        0        0   703599 2022-08-27 12:11:19.966238 pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.3.nbc
--rw-r--r--   0        0        0     1385 2022-08-31 02:33:45.537938 pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.nbi
--rw-r--r--   0        0        0   731211 2022-09-07 05:15:56.803955 pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-60.py39.1.nbc
--rw-r--r--   0        0        0     1387 2022-09-07 05:15:56.802955 pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-60.py39.nbi
--rw-r--r--   0        0        0   707458 2022-09-07 18:18:11.637112 pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-62.py39.1.nbc
--rw-r--r--   0        0        0     1387 2022-09-07 18:18:11.636112 pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-62.py39.nbi
--rw-r--r--   0        0        0   188311 2022-09-07 18:18:08.567118 pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_fake_linear_state_space-21.py39.1.nbc
--rw-r--r--   0        0        0     1358 2022-09-07 18:18:08.567118 pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_fake_linear_state_space-21.py39.nbi
--rw-r--r--   0        0        0   178575 2022-08-31 02:33:42.427926 pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-19.py39.1.nbc
--rw-r--r--   0        0        0     1351 2022-08-31 02:33:42.427926 pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-19.py39.nbi
--rw-r--r--   0        0        0   190334 2022-09-07 05:13:31.415489 pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-21.py39.1.nbc
--rw-r--r--   0        0        0     1353 2022-09-07 05:13:31.415489 pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-21.py39.nbi
--rw-r--r--   0        0        0     2116 2022-09-07 18:18:02.648129 pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.cpython-39.pyc
--rw-r--r--   0        0        0   335763 2022-08-27 12:11:19.968238 pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-17.py39.1.nbc
--rw-r--r--   0        0        0     1331 2022-08-27 12:11:19.968238 pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-17.py39.nbi
--rw-r--r--   0        0        0   326802 2022-08-30 02:32:03.497601 pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-69.py39.1.nbc
--rw-r--r--   0        0        0   324917 2022-08-27 12:11:19.970238 pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-69.py39.2.nbc
--rw-r--r--   0        0        0     1331 2022-08-30 02:32:03.497601 pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-69.py39.nbi
--rw-r--r--   0        0        0   330518 2022-09-07 18:18:07.541120 pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-70.py39.1.nbc
--rw-r--r--   0        0        0     1333 2022-09-07 18:18:07.541120 pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-70.py39.nbi
--rw-r--r--   0        0        0     5717 2022-09-07 18:18:01.931130 pybuc-0.8.10/pybuc/statespace/durbin_koopman_smoother.py
--rw-r--r--   0        0        0     5493 2022-09-07 18:17:36.567179 pybuc-0.8.10/pybuc/statespace/kalman_filter.py
--rw-r--r--   0        0        0     1872 2022-09-02 00:27:12.568399 pybuc-0.8.10/pybuc/utils/__pycache__/array_operations.cpython-39.pyc
--rw-r--r--   0        0        0     1561 2022-09-02 00:26:58.864341 pybuc-0.8.10/pybuc/utils/array_operations.py
--rw-r--r--   0        0        0      582 2022-08-27 12:31:07.668338 pybuc-0.8.10/pybuc/vectorized/__pycache__/distributions.cpython-39.pyc
--rw-r--r--   0        0        0      303 2022-08-27 12:11:19.970238 pybuc-0.8.10/pybuc/vectorized/distributions.py
--rw-r--r--   0        0        0      690 2022-09-13 18:01:27.994417 pybuc-0.8.10/pyproject.toml
--rw-r--r--   0        0        0    26450 2022-09-13 18:04:17.217786 pybuc-0.8.10/setup.py
--rw-r--r--   0        0        0    25488 2022-09-13 18:04:17.218528 pybuc-0.8.10/PKG-INFO
+-rw-r--r--   0        0        0     1478 2022-08-27 12:11:19.927238 pybuc-0.9.10/LICENSE.txt
+-rw-r--r--   0        0        0    24565 2022-09-14 11:45:47.122327 pybuc-0.9.10/README.md
+-rw-r--r--   0        0        0   104179 2022-09-14 11:35:55.372390 pybuc-0.9.10/pybuc/buc.py
+-rw-r--r--   0        0        0     3518 2022-09-07 18:18:02.664129 pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.cpython-39.pyc
+-rw-r--r--   0        0        0   730238 2022-08-31 02:33:45.538938 pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.1.nbc
+-rw-r--r--   0        0        0   671886 2022-08-27 12:11:19.963238 pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.2.nbc
+-rw-r--r--   0        0        0   703599 2022-08-27 12:11:19.966238 pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.3.nbc
+-rw-r--r--   0        0        0     1385 2022-08-31 02:33:45.537938 pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.nbi
+-rw-r--r--   0        0        0   731211 2022-09-07 05:15:56.803955 pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-60.py39.1.nbc
+-rw-r--r--   0        0        0     1387 2022-09-07 05:15:56.802955 pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-60.py39.nbi
+-rw-r--r--   0        0        0   707458 2022-09-07 18:18:11.637112 pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-62.py39.1.nbc
+-rw-r--r--   0        0        0     1387 2022-09-07 18:18:11.636112 pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-62.py39.nbi
+-rw-r--r--   0        0        0   188311 2022-09-07 18:18:08.567118 pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_fake_linear_state_space-21.py39.1.nbc
+-rw-r--r--   0        0        0     1358 2022-09-07 18:18:08.567118 pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_fake_linear_state_space-21.py39.nbi
+-rw-r--r--   0        0        0   178575 2022-08-31 02:33:42.427926 pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-19.py39.1.nbc
+-rw-r--r--   0        0        0     1351 2022-08-31 02:33:42.427926 pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-19.py39.nbi
+-rw-r--r--   0        0        0   190334 2022-09-07 05:13:31.415489 pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-21.py39.1.nbc
+-rw-r--r--   0        0        0     1353 2022-09-07 05:13:31.415489 pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-21.py39.nbi
+-rw-r--r--   0        0        0     2116 2022-09-07 18:18:02.648129 pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.cpython-39.pyc
+-rw-r--r--   0        0        0   335763 2022-08-27 12:11:19.968238 pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-17.py39.1.nbc
+-rw-r--r--   0        0        0     1331 2022-08-27 12:11:19.968238 pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-17.py39.nbi
+-rw-r--r--   0        0        0   326802 2022-08-30 02:32:03.497601 pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-69.py39.1.nbc
+-rw-r--r--   0        0        0   324917 2022-08-27 12:11:19.970238 pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-69.py39.2.nbc
+-rw-r--r--   0        0        0     1331 2022-08-30 02:32:03.497601 pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-69.py39.nbi
+-rw-r--r--   0        0        0   330518 2022-09-07 18:18:07.541120 pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-70.py39.1.nbc
+-rw-r--r--   0        0        0     1333 2022-09-07 18:18:07.541120 pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-70.py39.nbi
+-rw-r--r--   0        0        0     5717 2022-09-07 18:18:01.931130 pybuc-0.9.10/pybuc/statespace/durbin_koopman_smoother.py
+-rw-r--r--   0        0        0     5493 2022-09-07 18:17:36.567179 pybuc-0.9.10/pybuc/statespace/kalman_filter.py
+-rw-r--r--   0        0        0     1872 2022-09-02 00:27:12.568399 pybuc-0.9.10/pybuc/utils/__pycache__/array_operations.cpython-39.pyc
+-rw-r--r--   0        0        0     1561 2022-09-02 00:26:58.864341 pybuc-0.9.10/pybuc/utils/array_operations.py
+-rw-r--r--   0        0        0      582 2022-08-27 12:31:07.668338 pybuc-0.9.10/pybuc/vectorized/__pycache__/distributions.cpython-39.pyc
+-rw-r--r--   0        0        0      303 2022-08-27 12:11:19.970238 pybuc-0.9.10/pybuc/vectorized/distributions.py
+-rw-r--r--   0        0        0      690 2022-09-14 11:47:09.053602 pybuc-0.9.10/pyproject.toml
+-rw-r--r--   0        0        0    26322 2022-09-14 11:47:24.543578 pybuc-0.9.10/setup.py
+-rw-r--r--   0        0        0    25361 2022-09-14 11:47:24.544363 pybuc-0.9.10/PKG-INFO
```

### Comparing `pybuc-0.8.10/LICENSE.txt` & `pybuc-0.9.10/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/README.md` & `pybuc-0.9.10/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -208,17 +208,16 @@
 ```
 
 As noted above, a distinguishing feature of STS/UC models is their explicit modeling of trend and seasonality. This is 
 illustrated with the components plot.
 
 Finally, the Bayesian analog of the MLE STS/UC model is demonstrated. Default parameter values are used for the priors 
 corresponding to the variance parameters in the model. If no explicit prior is given, by default each variance's prior 
-is assumed to be inverse-Gamma with shape and scale values equal to 1 and 0.01, respectively. Note that a common 
-inverse-Gamma prior for variance parameters has shape and scale values equal to 0.001. This approximates what is known 
-as Jeffreys prior, a vague/non-informative prior.
+is assumed to be inverse-Gamma with shape and scale values equal to 1e-6. This approximates what is known as Jeffreys 
+prior, a vague/non-informative prior.
 
 **Note that because computation is built on Numba, a JIT compiler, the first run of the code could take a while. 
 Subsequent runs (assuming the Python kernel isn't restarted) should execute considerably faster.**
 
 ### Bayesian Unobserved Components
 ```
 ''' Fit the airline data using Bayesian unobserved components '''
```

### Comparing `pybuc-0.8.10/pybuc/buc.py` & `pybuc-0.9.10/pybuc/buc.py`

 * *Files 1% similar despite different names*

```diff
@@ -955,17 +955,17 @@
         # This will be used for plotting. The irregular component
         # will always be a part of the model (for now).
         components = dict()
         components['Irregular'] = dict()
 
         # Get priors for specified components
         if response_var_shape_prior is None:
-            response_var_shape_prior = 1e-4
+            response_var_shape_prior = 1e-6
         if response_var_scale_prior is None:
-            response_var_scale_prior = 1e-4
+            response_var_scale_prior = 1e-6
 
         response_var_shape_post = np.array([[response_var_shape_prior + 0.5 * n]])
         gibbs_iter0_response_error_variance = np.array([[0.01 * self.sd_response ** 2]])
 
         state_var_scale_prior = []
         state_var_shape_post = []
         init_state_variances = []
@@ -976,18 +976,18 @@
         autoreg_trend_coeff_cov_prior = None
         gibbs_iter0_autoreg_trend_coeff = None
 
         j, s = 0, 0  # j indexes the state equation, and s indexes stochastic equations
         if self.level:
             if self.stochastic_level:
                 if level_var_shape_prior is None:
-                    level_var_shape_prior = 1e-4
+                    level_var_shape_prior = 1e-6
 
                 if level_var_scale_prior is None:
-                    level_var_scale_prior = 1e-4
+                    level_var_scale_prior = 1e-6
 
                 state_var_shape_post.append(level_var_shape_prior + 0.5 * n)
                 state_var_scale_prior.append(level_var_scale_prior)
                 gibbs_iter0_state_error_var.append(0.01 * self.sd_response ** 2)
                 stochastic_index = s
                 s += 1
             else:
@@ -1010,18 +1010,18 @@
                                        stochastic=self.stochastic_level,
                                        stochastic_index=stochastic_index)
             j += 1
 
         if self.trend:
             if self.stochastic_trend:
                 if trend_var_shape_prior is None:
-                    trend_var_shape_prior = 1e-4
+                    trend_var_shape_prior = 1e-6
 
                 if trend_var_scale_prior is None:
-                    trend_var_scale_prior = 1e-4
+                    trend_var_scale_prior = 1e-6
 
                 state_var_shape_post.append(trend_var_shape_prior + 0.5 * n)
                 state_var_scale_prior.append(trend_var_scale_prior)
                 gibbs_iter0_state_error_var.append(0.01 * self.sd_response ** 2)
 
                 stochastic_index = s
                 s += 1
@@ -1050,18 +1050,18 @@
                                        stochastic=self.stochastic_trend,
                                        stochastic_index=stochastic_index)
             j += 1
 
         if len(self.dummy_seasonal) > 0:
             if True in self.stochastic_dummy_seasonal:
                 if dum_season_var_shape_prior is None:
-                    dum_season_var_shape_prior = (1e-4,) * len(self.dummy_seasonal)
+                    dum_season_var_shape_prior = (1e-6,) * len(self.dummy_seasonal)
 
                 if dum_season_var_scale_prior is None:
-                    dum_season_var_scale_prior = (1e-4,) * len(self.dummy_seasonal)
+                    dum_season_var_scale_prior = (1e-6,) * len(self.dummy_seasonal)
 
             i = j
             for c, v in enumerate(self.dummy_seasonal):
                 seasonal_period = seasonal_period + (v,)
                 if self.stochastic_dummy_seasonal[c]:
                     state_var_shape_post.append(dum_season_var_shape_prior[c] + 0.5 * n)
                     state_var_scale_prior.append(dum_season_var_scale_prior[c])
@@ -1095,18 +1095,18 @@
                 gibbs_iter0_init_state.append(k)
 
             j += self.num_dummy_seasonal_state_eqs
 
         if len(self.trig_seasonal) > 0:
             if True in self.stochastic_trig_seasonal:
                 if trig_season_var_shape_prior is None:
-                    trig_season_var_shape_prior = (1e-4,) * len(self.trig_seasonal)
+                    trig_season_var_shape_prior = (1e-6,) * len(self.trig_seasonal)
 
                 if trig_season_var_scale_prior is None:
-                    trig_season_var_scale_prior = (1e-4,) * len(self.trig_seasonal)
+                    trig_season_var_scale_prior = (1e-6,) * len(self.trig_seasonal)
 
             i = j
             for c, v in enumerate(self.trig_seasonal):
                 f, h = v
                 num_terms = 2 * h
                 seasonal_period = seasonal_period + (f,)
                 if self.stochastic_trig_seasonal[c]:
@@ -1151,15 +1151,15 @@
                                             stochastic_index=None)
             X = self.predictors
             init_state_plus_values.append(0.)
             init_state_variances.append(0.)
             gibbs_iter0_init_state.append(1.)
 
             if zellner_prior_obs is None:
-                zellner_prior_obs = 1e-4
+                zellner_prior_obs = 1e-6
 
             if reg_coeff_mean_prior is None:
                 reg_coeff_mean_prior = np.zeros((self.num_predictors, 1))
 
             if reg_coeff_precision_prior is None:
                 reg_coeff_precision_prior = zellner_prior_obs / n * (0.5 * dot(X.T, X)
                                                                      + 0.5 * np.diag(np.diag(dot(X.T, X))))
@@ -1237,55 +1237,53 @@
                zellner_prior_obs: float = None) -> Posterior:
 
         """
 
         :param num_samp: integer > 0. Specifies the number of posterior samples to draw.
 
         :param response_var_shape_prior: float > 0. Specifies the inverse-Gamma shape prior for the
-        response error variance. Default is 1.
+        response error variance. Default is 1e-6.
 
         :param response_var_scale_prior: float > 0. Specifies the inverse-Gamma scale prior for the
-        response error variance. Default is 0.01.
+        response error variance. Default is 1e-6.
 
         :param level_var_shape_prior: float > 0. Specifies the inverse-Gamma shape prior for the
-        level state equation error variance. Default is 1.
+        level state equation error variance. Default is 1e-6.
 
         :param level_var_scale_prior: float > 0. Specifies the inverse-Gamma scale prior for the
-        level state equation error variance. Default is 0.01.
+        level state equation error variance. Default is 1e-6.
 
         :param trend_var_shape_prior: float > 0. Specifies the inverse-Gamma shape prior for the
-        trend state equation error variance. Default is 1.
+        trend state equation error variance. Default is 1e-6.
 
         :param trend_var_scale_prior: float > 0. Specifies the inverse-Gamma scale prior for the
-        trend state equation error variance. Default is 0.01.
+        trend state equation error variance. Default is 1e-6.
 
         :param autoreg_trend_coeff_mean_prior: Numpy array of dimension (1, 1). Specifies the prior
         mean for the coefficient governing the trend's AR(1) process without drift. Default is [[0.]].
 
         :param autoreg_trend_coeff_precision_prior: Numpy array of dimension (1, 1). Specifies the prior
         precision matrix for the coefficient governing the trend's an AR(1) process without drift.
         Default is [[4.]].
 
         :param dum_season_var_shape_prior: tuple of floats > 0. Specifies the inverse-Gamma shape priors
-        for each periodicity in dummy_seasonal. Default is 1 for each periodicity.
+        for each periodicity in dummy_seasonal. Default is 1e-6 for each periodicity.
 
         :param dum_season_var_scale_prior: tuple of floats > 0. Specifies the inverse-Gamma scale priors
-        for each periodicity in dummy_seasonal. Default is 0.01 for each periodicity.
+        for each periodicity in dummy_seasonal. Default is 1e-6 for each periodicity.
 
         :param trig_season_var_shape_prior: tuple of floats > 0. Specifies the inverse-Gamma shape priors
-        for each (periodicity, num_harmonics) pair in trig_seasonal. In total, there are
-        2 * SUM[num_harmonics[p]] shape priors for p=1, 2, ..., P periodicities. For example, if
-        trig_seasonal = ((12, 3), (10, 2)) and stochastic_trig_seasonal = (True, True), then there are
-        2 * 3 + 2 * 2 = 10 shape priors required. Default is 1 for each (periodicity, num_harmonics) pair.
+        for each periodicity in trig_seasonal. For example, if trig_seasonal = ((12, 3), (10, 2)) and
+        stochastic_trig_seasonal = (True, True), only two shape priors need to be specified: one for periodicity 12
+        and one for periodicity 10. Default is 1e-6 for each periodicity.
 
         :param trig_season_var_scale_prior: tuple of floats > 0. Specifies the inverse-Gamma scale priors
-        for each (periodicity, num_harmonics) pair in trig_seasonal. In total, there are
-        2 * SUM[num_harmonics[p]] scale priors for p=1, 2, ..., P periodicities. For example, if
-        trig_seasonal = ((12, 3), (10, 2)) and stochastic_trig_seasonal = (True, True), then there are
-        2 * 3 + 2 * 2 = 10 scale priors required. Default is 0.01 for each (periodicity, num_harmonics) pair.
+        for each periodicity in trig_seasonal. For example, if trig_seasonal = ((12, 3), (10, 2)) and
+        stochastic_trig_seasonal = (True, True), only two scale priors need to be specified: one for periodicity 12
+        and one for periodicity 10. Default is 1e-6 for each periodicity.
 
         :param reg_coeff_mean_prior: Numpy array of dimension (k, 1), where k is the number of predictors.
         Data type must be float64. If predictors are specified without a mean prior, a k-dimensional zero
         vector will be assumed.
 
         :param reg_coeff_precision_prior: Numpy array of dimension (k, k), where k is the number of predictors.
         Data type must be float64. If predictors are specified without a precision prior, Zellner's g-prior will
@@ -1294,15 +1292,15 @@
         it controls how much weight is given to the mean prior), n is the number of observations, X is the design
         matrix, and diag(dot(X.T, X)) is a diagonal matrix with the diagonal elements matching those of
         dot(X.T, X). The addition of the diagonal matrix to dot(X.T, X) is to guard against singularity
         (i.e., a design matrix that is not full rank). The weighting controlled by w is set to 0.5.
         
         :param zellner_prior_obs: float > 0. Relevant only if no regression precision matrix is provided.
         It controls how precise one believes their priors are for the regression coefficients, assuming no regression
-        precision matrix is provided. Default value is 1e-4, which gives little weight to the regression coefficient
+        precision matrix is provided. Default value is 1e-6, which gives little weight to the regression coefficient
         mean prior. This should approximate maximum likelihood estimation.
 
         :return: NamedTuple with the following:
         
                     num_samp: Number of posterior samples drawn
                     smoothed_state: Posterior simulated smoothed state from Durbin-Koopman smoother
                     smoothed_errors: Posterior simulated smoothed errors from Durbin-Koopman smoother
```

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.cpython-39.pyc` & `pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.cpython-39.pyc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.1.nbc` & `pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.1.nbc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.2.nbc` & `pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.2.nbc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.3.nbc` & `pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.3.nbc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.nbi` & `pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-58.py39.nbi`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-60.py39.1.nbc` & `pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-60.py39.1.nbc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-60.py39.nbi` & `pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-60.py39.nbi`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-62.py39.1.nbc` & `pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-62.py39.1.nbc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-62.py39.nbi` & `pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.dk_smoother-62.py39.nbi`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_fake_linear_state_space-21.py39.1.nbc` & `pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_fake_linear_state_space-21.py39.1.nbc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_fake_linear_state_space-21.py39.nbi` & `pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_fake_linear_state_space-21.py39.nbi`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-19.py39.1.nbc` & `pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-19.py39.1.nbc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-19.py39.nbi` & `pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-19.py39.nbi`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-21.py39.1.nbc` & `pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-21.py39.1.nbc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-21.py39.nbi` & `pybuc-0.9.10/pybuc/statespace/__pycache__/durbin_koopman_smoother.simulate_linear_state_space-21.py39.nbi`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.cpython-39.pyc` & `pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.cpython-39.pyc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-17.py39.1.nbc` & `pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-17.py39.1.nbc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-17.py39.nbi` & `pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-17.py39.nbi`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-69.py39.1.nbc` & `pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-69.py39.1.nbc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-69.py39.2.nbc` & `pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-69.py39.2.nbc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-69.py39.nbi` & `pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-69.py39.nbi`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-70.py39.1.nbc` & `pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-70.py39.1.nbc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-70.py39.nbi` & `pybuc-0.9.10/pybuc/statespace/__pycache__/kalman_filter.kalman_filter-70.py39.nbi`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/durbin_koopman_smoother.py` & `pybuc-0.9.10/pybuc/statespace/durbin_koopman_smoother.py`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/statespace/kalman_filter.py` & `pybuc-0.9.10/pybuc/statespace/kalman_filter.py`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/utils/__pycache__/array_operations.cpython-39.pyc` & `pybuc-0.9.10/pybuc/utils/__pycache__/array_operations.cpython-39.pyc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/utils/array_operations.py` & `pybuc-0.9.10/pybuc/utils/array_operations.py`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pybuc/vectorized/__pycache__/distributions.cpython-39.pyc` & `pybuc-0.9.10/pybuc/vectorized/__pycache__/distributions.cpython-39.pyc`

 * *Files identical despite different names*

### Comparing `pybuc-0.8.10/pyproject.toml` & `pybuc-0.9.10/pyproject.toml`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "pybuc"
-version = "0.8.10"
+version = "0.9.10"
 description = "Fast estimation of Bayesian structural time series models via Gibbs sampling."
 authors = ["Devin D. Garcia"]
 license = "BSD 3-Clause"
 readme = "README.md"
 keywords = ["structural time series", "unobserved components", "bayesian", "bsts"]
 
 [tool.poetry.dependencies]
```

### Comparing `pybuc-0.8.10/setup.py` & `pybuc-0.9.10/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -11,17 +11,17 @@
 ['matplotlib>=3.5.3,<4.0.0',
  'numba>=0.56.2,<0.57.0',
  'numpy>=1.23.2,<2.0.0',
  'pandas>=1.4.4,<2.0.0']
 
 setup_kwargs = {
     'name': 'pybuc',
-    'version': '0.8.10',
+    'version': '0.9.10',
     'description': 'Fast estimation of Bayesian structural time series models via Gibbs sampling.',
-    'long_description': '# pybuc\n`pybuc` ((Py)thon (B)ayesian (U)nobserved (C)omponents) is a feature-limited version of R\'s Bayesian structural time \nseries package, `bsts`, written by Steven L. Scott. The source paper can be found \n[here](https://people.ischool.berkeley.edu/~hal/Papers/2013/pred-present-with-bsts.pdf) or in the *papers* \ndirectory of this repository. While there are plans to expand the feature set of `pybuc`, currently there is no roadmap \nfor the release of new features. The syntax for using `pybuc` closely follows `statsmodels`\' `UnobservedComponents` \nmodule.\n\nThe current version of `pybuc` includes the following options for modeling and \nforecasting a structural time series: \n\n- Stochastic or non-stochastic level\n- Stochastic or non-stochastic trend\n- Damped trend <sup/>*</sup>\n- Multiple stochastic or non-stochastic "dummy" seasonality\n- Multiple stochastic or non-stochastic trigonometric seasonality\n- Regression with static coefficients<sup/>**</sup>\n\n<sup/>*</sup> `pybuc` dampens trend differently than `bsts`. The former assumes an AR(1) process **without** \ndrift for the trend state equation. The latter assumes an AR(1) **with** drift. In practice this means that the trend, \non average, will be zero with `pybuc`, whereas `bsts` allows for the mean trend to be non-zero. The reason for \nchoosing an autoregressive process without drift is to be conservative with long horizon forecasts.\n\n<sup/>**</sup> `pybuc` estimates regression coefficients differently than `bsts`. The former uses a standard Gaussian \nprior. The latter uses a Bernoulli-Gaussian mixture commonly known as the spike-and-slab prior. The main \nbenefit of using a spike-and-slab prior is its promotion of coefficient-sparse solutions, i.e., variable selection, when \nthe number of predictors in the regression component exceeds the number of observed data points.\n\nFast computation is achieved using [Numba](https://numba.pydata.org/), a high performance just-in-time (JIT) compiler \nfor Python.\n\n# Installation\n```\npip install pybuc\n```\nSee `pyproject.toml` and `poetry.lock` for dependency details. This module depends on NumPy, Numba, Pandas, and \nMatplotlib. Python 3.9 and above is supported.\n\n# Motivation\n\nThe Seasonal Autoregressive Integrated Moving Average (SARIMA) model is perhaps the most widely used class of \nstatistical time series models. By design, these models can only operate on covariance-stationary time series. \nConsequently, if a time series exhibits non-stationarity (e.g., trend and/or seasonality), then the data first have to \nbe stationarized. Transforming a non-stationary series to a stationary one requires taking local and/or seasonal \ntime-differences of the data. Whether to difference the data and to what extent is a question that is answered using \nstatistical methods. \n\nOnce a stationary series is in hand, a SARIMA specification must be identified. Identifying the "right" SARIMA \nspecification can be achieved algorithmically (e.g., see the Python package `pmdarima`) or through examination of a \nseries\' patterns. The latter involves statistical and visual inspection of a series\' autocorrelation (ACF) and partial \nautocorrelation (PACF) functions. Ultimately, the necessary condition for stationarity engenders a prerequisite for \nrigorous statistical tests. It also implies that the underlying trend and seasonality, if they exist, are eliminated in \nthe process of generating a stationary series. The underlying time components that characterize a series are, therefore, \nnot of empirical interest.\n\nAnother less commonly used class of model is structural time series (STS), also known as unobserved components (UC). \nWhereas SARIMA models abstract away from an explicit model for trend and seasonality, STS/UC models do not. Thus, it is \nnot possible to visualize the underlying components that characterize a time series using a SARIMA model, but one can do \nso with a STS/UC model.\n\nSTS/UC models also have the flexibility to accommodate multiple stochastic seasonalities. SARIMA models, in contrast, \ncan accommodate multiple seasonalities, but only one seasonality/periodicity can be treated as stochastic. For example, \ndaily data may have day-of-week and week-of-year seasonality. Under a SARIMA model, only one of these seasonalities can \nbe modeled as stochastic. The other seasonality will have to be modeled as deterministic, which amounts to creating and \nusing a set of predictors that capture said seasonality. STS/UC models, on the other hand, can accommodate both \nseasonalities as stochastic by treating each as distinct, unobserved state variables.\n\nWith the above in mind, what follows is a comparison between `statsmodels`\' `SARIMAX\'` module, `statsmodels`\' \n`UnobservedComponents` module, and `pybuc`. The distinction between `statsmodels.UnobservedComponents` and `pybuc` is \nthe former is a maximum likelihood estimator (MLE) while the latter is a Bayesian estimator. The following code \ndemonstrates the application of these methods on a data set that exhibits trend and multiplicative seasonality.\nThe STS/UC specification for `statsmodels.UnobservedComponents` and `pybuc` includes stochastic level, stochastic trend \n(trend), and stochastic trigonometric seasonality with periodicity 12 and 6 harmonics.\n\n# Usage\n\n## Example: univariate time series with level, trend, and multiplicative seasonality\n\nA canonical data set that exhibits trend and seasonality is the airline passenger data used in\nBox, G.E.P.; Jenkins, G.M.; and Reinsel, G.C. Time Series Analysis, Forecasting and Control. Series G, 1976. See plot \nbelow.\n\n![plot](./examples/images/airline_passengers.png)\n\nThis data set gave rise to what is known as the "airline model", which is a SARIMA model with first-order local and \nseasonal differencing and first-order local and seasonal moving average representations. \nMore compactly, SARIMA(0, 1, 1)(0, 1, 1) without drift.\n\nTo demonstrate the performance of the "airline model" on the airline passenger data, the data will be split into a \ntraining and test set. The former will include all observations up until the last twelve months of data, and the latter \nwill include the last twelve months of data. See code below for model assessment.\n\n### Import libraries and prepare data\n\n```\nfrom pybuc import buc\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom statsmodels.tsa.statespace.sarimax import SARIMAX\nfrom statsmodels.tsa.statespace.structural import UnobservedComponents\n\n\n# Convenience function for computing root mean squared error\ndef rmse(actual, prediction):\n    act, pred = actual.flatten(), prediction.flatten()\n    return np.sqrt(np.mean((act - pred) ** 2))\n\n\n# Import airline passenger data\nurl = "https://raw.githubusercontent.com/devindg/pybuc/master/examples/data/airline-passengers.csv"\nair = pd.read_csv(url, header=0, index_col=0)\nair = air.astype(float)\nair.index = pd.to_datetime(air.index)\nhold_out_size = 12\n\n# Create train and test sets\ny_train = air.iloc[:-hold_out_size]\ny_test = air.iloc[-hold_out_size:]\n```\n\n### SARIMA\n\n```\n\'\'\' Fit the airline data using SARIMA(0,1,1)(0,1,1) \'\'\'\nsarima = SARIMAX(y_train, order=(0, 1, 1),\n                 seasonal_order=(0, 1, 1, 12),\n                 trend=[0])\nsarima_res = sarima.fit(disp=False)\nprint(sarima_res.summary())\n\n# Plot in-sample fit against actuals\nplt.plot(y_train)\nplt.plot(sarima_res.fittedvalues)\nplt.title(\'SARIMA: In-sample\')\nplt.xticks(rotation=45, ha="right")\nplt.show()\n\n# Get and plot forecast\nsarima_forecast = sarima_res.get_forecast(hold_out_size).summary_frame(alpha=0.05)\nplt.plot(y_test)\nplt.plot(sarima_forecast[\'mean\'])\nplt.fill_between(sarima_forecast.index,\n                 sarima_forecast[\'mean_ci_lower\'],\n                 sarima_forecast[\'mean_ci_upper\'], alpha=0.2)\nplt.title(\'SARIMA: Forecast\')\nplt.legend([\'Actual\', \'Mean\', \'95% Prediction Interval\'])\nplt.show()\n\n# Print RMSE\nprint(f"SARIMA RMSE: {rmse(y_test.to_numpy(), sarima_forecast[\'mean\'].to_numpy())}")\n```\nThe SARIMA(0, 1, 1)(0, 1, 1) forecast plot and root mean squared error (RMSE) are shown below. \n\n![plot](./examples/images/airline_passengers_sarima_forecast.png)\n\n```\nSARIMA RMSE: 21.09028021383853\n```\n\n### MLE Unobserved Components\n\n```\n\'\'\' Fit the airline data using MLE unobserved components \'\'\'\nmle_uc = UnobservedComponents(y_train, exog=None, irregular=True,\n                              level=True, stochastic_level=True,\n                              trend=True, stochastic_trend=True,\n                              freq_seasonal=[{\'period\': 12, \'harmonics\': 6}],\n                              stochastic_freq_seasonal=[True])\n\n# Fit the model via maximum likelihood\nmle_uc_res = mle_uc.fit(disp=False)\nprint(mle_uc_res.summary())\n\n# Plot in-sample fit against actuals\nplt.plot(y_train)\nplt.plot(mle_uc_res.fittedvalues)\nplt.title(\'MLE UC: In-sample\')\nplt.show()\n\n# Plot time series components\nmle_uc_res.plot_components(legend_loc=\'lower right\', figsize=(15, 9), which=\'smoothed\')\nplt.show()\n\n# Get and plot forecast\nmle_uc_forecast = mle_uc_res.get_forecast(hold_out_size).summary_frame(alpha=0.05)\nplt.plot(y_test)\nplt.plot(mle_uc_forecast[\'mean\'])\nplt.fill_between(mle_uc_forecast.index,\n                 mle_uc_forecast[\'mean_ci_lower\'],\n                 mle_uc_forecast[\'mean_ci_upper\'], alpha=0.2)\nplt.title(\'MLE UC: Forecast\')\nplt.legend([\'Actual\', \'Mean\', \'95% Prediction Interval\'])\nplt.show()\n\n# Print RMSE\nprint(f"MLE UC RMSE: {rmse(y_test.to_numpy(), mle_uc_forecast[\'mean\'].to_numpy())}")\n```\n\nThe MLE Unobserved Components forecast plot, components plot, and RMSE are shown below.\n\n![plot](./examples/images/airline_passengers_mle_uc_forecast.png)\n\n![plot](./examples/images/airline_passengers_mle_uc_components.png)\n\n```\nMLE UC RMSE: 17.961873327622694\n```\n\nAs noted above, a distinguishing feature of STS/UC models is their explicit modeling of trend and seasonality. This is \nillustrated with the components plot.\n\nFinally, the Bayesian analog of the MLE STS/UC model is demonstrated. Default parameter values are used for the priors \ncorresponding to the variance parameters in the model. If no explicit prior is given, by default each variance\'s prior \nis assumed to be inverse-Gamma with shape and scale values equal to 1 and 0.01, respectively. Note that a common \ninverse-Gamma prior for variance parameters has shape and scale values equal to 0.001. This approximates what is known \nas Jeffreys prior, a vague/non-informative prior.\n\n**Note that because computation is built on Numba, a JIT compiler, the first run of the code could take a while. \nSubsequent runs (assuming the Python kernel isn\'t restarted) should execute considerably faster.**\n\n### Bayesian Unobserved Components\n```\n\'\'\' Fit the airline data using Bayesian unobserved components \'\'\'\nbayes_uc = buc.BayesianUnobservedComponents(response=y_train,\n                                                level=True, stochastic_level=True,\n                                                trend=True, stochastic_trend=True, autoregressive_trend=False,\n                                                dummy_seasonal=(), stochastic_dummy_seasonal=(),\n                                                trig_seasonal=((12, 0), ), stochastic_trig_seasonal=(True,),\n                                                seed=123)\n\npost = bayes_uc.sample(5000)\nmcmc_burn = 100\n\n# Print summary of estimated parameters\nfor key, value in bayes_uc.summary(burn=mcmc_burn).items():\n    print(key, \' : \', value)\n\n# Plot in-sample fit against actuals\nyhat = np.mean(post.filtered_prediction[mcmc_burn:], axis=0)\nplt.plot(y_train)\nplt.plot(y_train.index, yhat)\nplt.title(\'Bayesian-UC: In-sample\')\nplt.show()\n\n# Plot time series components\nbayes_uc.plot_components(burn=mcmc_burn, smoothed=True)\nplt.show()\n\n# Get and plot forecast\nforecast = bayes_uc.forecast(hold_out_size, mcmc_burn)\nforecast_mean = np.mean(forecast, axis=0)\nforecast_l95 = np.quantile(forecast, 0.025, axis=0).flatten()\nforecast_u95 = np.quantile(forecast, 0.975, axis=0).flatten()\n\nplt.plot(y_test)\nplt.plot(bayes_uc.future_time_index, forecast_mean)\nplt.fill_between(bayes_uc.future_time_index, forecast_l95, forecast_u95, alpha=0.2)\nplt.title(\'Bayesian UC: Forecast\')\nplt.legend([\'Actual\', \'Mean\', \'95% Prediction Interval\'])\nplt.show()\n\n# Print RMSE\nprint(f"BAYES-UC RMSE: {rmse(y_test.to_numpy(), forecast_mean)}")\n```\n\nThe Bayesian Unobserved Components forecast plot, components plot, and RMSE are shown below.\n\n![plot](./examples/images/airline_passengers_bayes_uc_forecast.png)\n\n![plot](./examples/images/airline_passengers_bayes_uc_components.png)\n\n```\nBAYES-UC RMSE: 17.412932828154464\n```\n\n# Model\n\nA structural time series model with level, trend, seasonal, and regression components takes the form: \n\n$$\ny_t = \\mu_t + \\gamma_t + \\mathbf x_t^\\prime \\boldsymbol{\\beta} + \\epsilon_t\n$$ \n\nwhere $\\mu_t$ specifies an unobserved dynamic level component, $\\gamma_t$ an unobserved dynamic seasonal component, \n$\\mathbf x_t^\\prime \\boldsymbol{\\beta}$ a partially unobserved regression component (the regressors $\\mathbf x_t$ are \nobserved, but the coefficients $\\boldsymbol{\\beta}$ are not), and $\\epsilon_t \\sim N(0, \\sigma_{\\epsilon}^2)$ an \nunobserved irregular component. The equation describing the outcome $y_t$ is commonly referred to as the observation \nequation, and the transition equations governing the evolution of the unobserved states are known as the state \nequations.\n\n## Level and trend\n\nThe unobserved level evolves according to the following general transition equations:\n\n$$\n\\begin{align}\n    \\mu_{t+1} &= \\mu_t + \\delta_t + \\eta_{\\mu, t} \\\\ \n    \\delta_{t+1} &= \\phi \\delta_t + \\eta_{\\delta, t} \n\\end{align}\n$$ \n\nwhere $\\eta_{\\mu, t} \\sim N(0, \\sigma_{\\eta_\\mu}^2)$ and $\\eta_{\\delta, t} \\sim N(0, \\sigma_{\\eta_\\delta}^2)$ for all \n$t$. The state equation for $\\delta_t$ represents the local trend at time $t$. \n\nThe parameter $\\phi$ represents an autoregressive coefficient. In general, $\\phi$ is expected to be in the interval \n$(-1, 1)$, which implies a stationary process for trend. In practice, however, it is possible for $\\phi$ to be \noutside the unit circle, which implies an explosive process. While it is mathematically possible for an explosive \nprocess to be stationary, the implication of such a result implies that the future predicts the past, which is not a \nrealistic assumption. \n\nIf an autoregressive trend is specified, no hard constraints (by default) are placed on the bounds of $\\phi$. Instead, \nthe default prior for $\\phi$ is $N(0, 0.25)$. Thus, -1 and 1 are within two standard deviations of the mean. It is \ntherefore possible for the Gibbs sampler to sample values outside the unit circle. If the posterior mean of $\\phi$ is \noutside the unit circle (or very close to the bounds), then an autoregressive trend is not a good assumption. If only \na "few" of the posterior samples have $\\phi$ outside the unit circle, this shouldn\'t be problematic for forecasting. \n$\\phi$ is set to 1 if a damped trend is not specified.\n\nFinally, note that if $\\sigma_{\\eta_\\mu}^2 = \\sigma_{\\eta_\\delta}^2 = 0$ and $\\phi = 1$, then the level component in \nthe observation equation, $\\mu_t$, collapses to a deterministic intercept and linear time trend.\n\n## Seasonality\n\n### Dummy form\nThe seasonal component, $\\gamma_t$, can be modeled in two ways. One way is known as the "dummy" variable approach. \nFormally, the seasonal effect on the outcome $y$ is modeled as \n\n$$\n\\sum_{j=0}^{S-1} \\gamma_{t-j} = \\eta_{\\gamma, t} \\iff \\gamma_t = -\\sum_{j=1}^{S-1} \\gamma_{t-j} + \\eta_{\\gamma, t},\n$$ \n\nwhere $j$ indexes the number of periods in a seasonal cycle, $S$ is the number of periods in a seasonal cycle, and \n$\\eta_{\\gamma, t} \\sim N(0, \\sigma_{\\eta_\\gamma}^2)$ for all $t$. Intuitively, if a time series exhibits periodicity, \nthen the sum of the periodic effects over a cycle should, on average, be zero.\n\n### Trigonometric form\nAnother way to model seasonality is through a trigonometric representation, which exploits the periodicity of sine and \ncosine functions. Specifically, seasonality is modeled as\n\n$$\n\\gamma_t = \\sum_{j=1}^h \\gamma_{j, t}\n$$\n\nwhere $j$ indexes the number of harmonics to represent seasonality of periodicity $S$ and \n$1 \\leq h \\leq \\lfloor S/2 \\rfloor$ is the highest desired number of harmonics. The state transition equations for each \nharmonic, $\\gamma_{j, t}$, are represented by a real and imaginary part, specifically\n\n$$\n\\begin{align}\n    \\gamma_{j, t+1} &= \\cos(\\lambda_j) \\gamma_{j, t} + \\sin(\\lambda_j) \\gamma_{j, t}^* + \\eta_{\\gamma_j, t} \\\\\n    \\gamma_{j, t+1}^* &= -\\sin(\\lambda_j) \\gamma_{j, t} + \\cos(\\lambda_j) \\gamma_{j, t}^* + \\eta_{\\gamma_j^* , t}\n\\end{align}\n$$\n\nwhere frequency $\\lambda_j = 2j\\pi / S$. It is assumed that $\\eta_{\\gamma_j, t}$ and $\\eta_{\\gamma_j^ * , t}$ are \ndistributed $N(0, \\sigma^2_{\\eta_\\gamma})$ for all $j, t$.\n\n## Regression\nThere are two ways to configure the model matrices to account for a regression component with static coefficients. \nThe canonical way (Method 1) is to append $\\mathbf x_t^\\prime$ to $\\mathbf Z_t$ and $\\boldsymbol{\\beta}_t$ to the \nstate vector, $\\boldsymbol{\\alpha}_t$ (see state space representation below), with the constraints \n$\\boldsymbol{\\beta}_0 = \\boldsymbol{\\beta}$ and $\\boldsymbol{\\beta}_t = \\boldsymbol{\\beta} _{t-1}$ for all $t$. \nAnother, less common way (Method 2) is to append $\\mathbf x_t^\\prime \\boldsymbol{\\beta}$ to $\\mathbf Z_t$ and 1 to the \nstate vector. \n\nWhile both methods can be accommodated by the Kalman filter, Method 1 is a direct extension of the Kalman filter as it \nmaintains the observability of $\\mathbf Z_t$ and treats the regression coefficients as unobserved states. Method 2 does \nnot fit naturally into the conventional framework of the Kalman filter, but it offers the significant advantage of only \nincreasing the size of the state vector by one. In contrast, Method 1 increases the size of the state vector by the size \nof $\\boldsymbol{\\beta}$. This is significant because computational complexity is quadratic in the size of the state \nvector but linear in the size of the observation vector.\n\nThe unobservability of $\\mathbf Z_t$ under Method 2 can be handled with maximum likelihood or Bayesian estimation by \nworking with the adjusted series \n\n$$\ny_t^* \\equiv y_t - \\tau_t = \\mathbf x_ t^\\prime \\boldsymbol{\\beta} + \\epsilon_t\n$$\n\nwhere $\\tau_t$ represents the time series component of the structural time series model. For example, assuming a level \nand seasonal component are specified, this means an initial estimate of the time series component \n$\\tau_t = \\mu_t + \\gamma_t$ and $\\boldsymbol{\\beta}$ has to be acquired first. Then $\\boldsymbol{\\beta}$ can be \nestimated conditional on \n$\\mathbf y^ * \\equiv \\left(\\begin{array}{cc} y_1^ * & y_2^ * & \\cdots & y_n^ * \\end{array}\\right)^\\prime$.\n\n`pybuc` uses Method 2 for estimating static coefficients.\n\n## State space representation (example)\nThe unobserved components model can be rewritten in state space form. For example, suppose level, trend, seasonal, \nregression, and irregular components are specified, and the seasonal component takes a trigonometric form with \nperiodicity $S=4$ and $h=2$ harmonics. Let $\\mathbf Z_t \\in \\mathbb{R}^{1 \\times m}$, \n$\\mathbf T \\in \\mathbb{R}^{m \\times m}$, $\\mathbf R \\in \\mathbb{R}^{m \\times q}$, and \n$\\boldsymbol{\\alpha}_ t \\in \\mathbb{R}^{m \\times 1}$ denote the observation matrix, state transition matrix, \nstate error transformation matrix, and unobserved state vector, respectively, where $m$ is the number of state equations \nand $q$ is the number of state parameters to be estimated (i.e., the number of stochastic state equations, \nwhich is defined by the number of positive state variance parameters). \n\nThere are $m = 1 + 1 + h * 2 + 1 = 7$ state equations and $q = 1 + 1 + h * 2 = 6$ stochastic state equations. There are \n6 stochastic state equations because the state value for the regression component is not stochastic; it is 1 for all $t$ \nby construction. The observation, state transition, and state error transformation matrices may be written as\n\n$$\n\\begin{align}\n    \\mathbf Z_t &= \\left(\\begin{array}{cc} \n                        1 & 0 & 1 & 0 & 1 & 0 & \\mathbf x_t^{\\prime} \\boldsymbol{\\beta}\n                        \\end{array}\\right) \\\\\n    \\mathbf T &= \\left(\\begin{array}{cc} \n                        1 & 1 & 0 & 0 & 0 & 0 & 0 \\\\\n                        0 & 1 & 0 & 0 & 0 & 0 & 0 \\\\\n                        0 & 0 & \\cos(2\\pi / 4) & \\sin(2\\pi / 4) & 0 & 0 & 0 \\\\\n                        0 & 0 & -\\sin(2\\pi / 4) & \\cos(2\\pi / 4) & 0 & 0 & 0 \\\\\n                        0 & 0 & 0 & 0 & \\cos(4\\pi / 4) & \\sin(4\\pi / 4) & 0 \\\\\n                        0 & 0 & 0 & 0 & -\\sin(4\\pi / 4) & \\cos(4\\pi / 4) & 0 \\\\\n                        0 & 0 & 0 & 0 & 0 & 0 & 1\n                        \\end{array}\\right) \\\\\n    \\mathbf R &= \\left(\\begin{array}{cc} \n                    1 & 0 & 0 & 0 & 0 & 0 \\\\\n                    0 & 1 & 0 & 0 & 0 & 0 \\\\\n                    0 & 0 & 1 & 0 & 0 & 0 \\\\\n                    0 & 0 & 0 & 1 & 0 & 0 \\\\\n                    0 & 0 & 0 & 0 & 1 & 0 \\\\\n                    0 & 0 & 0 & 0 & 0 & 1 \\\\\n                    0 & 0 & 0 & 0 & 0 & 0\n                    \\end{array}\\right)\n\\end{align}\n$$\n\nGiven the definitions of $\\mathbf Z_t$, $\\mathbf T$, and $\\mathbf R$, the state space representation of the unobserved \ncomponents model above can compactly be expressed as\n\n$$\n\\begin{align}\n    y_t &= \\mathbf Z_t \\boldsymbol{\\alpha}_ t + \\epsilon_t \\\\\n    \\boldsymbol{\\alpha}_ {t+1} &= \\mathbf T \\boldsymbol{\\alpha}_ t + \\mathbf R \\boldsymbol{\\eta}_ t, \\hspace{5pt} \n    t=1,2,...,n\n\\end{align}\n$$\n\nwhere\n\n$$\n\\begin{align}\n    \\boldsymbol{\\alpha}_ t &= \\left(\\begin{array}{cc} \n                            \\mu_t & \\delta_t & \\gamma_{1, t} & \\gamma_{1, t}^* & \\gamma_{2, t} & \\gamma_{2, t}^* & 1\n                            \\end{array}\\right)^\\prime \\\\\n    \\boldsymbol{\\eta}_ t &= \\left(\\begin{array}{cc} \n                            \\eta_{\\mu, t} & \\eta_{\\delta, t} & \\eta_{\\gamma_ 1, t} & \\eta_{\\gamma_ 1^\\*, t} & \n                            \\eta_{\\gamma_ 2, t} & \\eta_{\\gamma_ 2^\\*, t}\n                            \\end{array}\\right)^\\prime\n\\end{align}\n$$\n\nand \n\n$$\n\\mathrm{Cov}(\\boldsymbol{\\eta}_ t) = \\mathrm{Cov}(\\boldsymbol{\\eta}_ {t-1}) = \\boldsymbol{\\Sigma}_ \\eta = \n\\mathrm{diag}(\\sigma^2_{\\eta_\\mu}, \\sigma^2_{\\eta_\\delta}, \\sigma^2_{\\eta_{\\gamma_ 1}}, \\sigma^2_{\\eta_{\\gamma_ 1^\\*}}, \n\\sigma^2_{\\eta_{\\gamma_ 2}}, \\sigma^2_{\\eta_{\\gamma_ 2^\\*}}) \\in \\mathbb{R}^{6 \\times 6} \\hspace{5pt} \\textrm{for all } \nt=1,2,...,n\n$$\n\n# Estimation\n`pybuc` mirrors R\'s `bsts` with respect to estimation method. The observation vector, state vector, and regression \ncoefficients are assumed to be conditionally normal random variables, and the error variances are assumed to be \nconditionally independent inverse-Gamma random variables. These model assumptions imply conditional conjugacy of the \nmodel\'s parameters. Consequently, a Gibbs sampler is used to sample from each parameter\'s posterior distribution.\n\nTo achieve fast sampling, `pybuc` follows `bsts`\'s adoption of the Durbin and Koopman (2002) simulation smoother. For \nany parameter $\\theta$, let $\\theta(s)$ denote the $s$-th sample of parameter $\\theta$. Each sample $s$ is drawn by \nrepeating the following three steps:\n\n1. Draw $\\boldsymbol{\\alpha}(s)$ from \n   $p(\\boldsymbol{\\alpha} | \\mathbf y, \\boldsymbol{\\sigma}^2_\\eta(s-1), \\boldsymbol{\\beta}(s-1), \\sigma^2_\\epsilon(s-1))$ \n   using the Durbin and Koopman simulation state smoother, where \n   $\\boldsymbol{\\alpha}(s) = (\\boldsymbol{\\alpha}_ 1(s), \\boldsymbol{\\alpha}_ 2(s), \\cdots, \\boldsymbol{\\alpha}_ n(s))^\\prime$ \n   and $\\boldsymbol{\\sigma}^2_\\eta(s-1) = \\mathrm{diag}(\\boldsymbol{\\Sigma}_\\eta(s-1))$. Note that `pybuc` implements a \n   correction (based on a potential misunderstanding) for drawing $\\boldsymbol{\\alpha}(s)$ per "A note on implementing \n   the Durbin and Koopman simulation smoother" (Marek Jarocinski, 2015).\n2. Draw $\\boldsymbol{\\sigma}^2(s) = (\\sigma^2_ \\epsilon(s), \\boldsymbol{\\sigma}^2_ \\eta(s))^\\prime$ from \n   $p(\\boldsymbol{\\sigma}^2 | \\mathbf y, \\boldsymbol{\\alpha}(s), \\boldsymbol{\\beta}(s-1))$ using Durbin and Koopman\'s \n   simulation disturbance smoother.\n3. Draw $\\boldsymbol{\\beta}(s)$ from \n   $p(\\boldsymbol{\\beta} | \\mathbf y^ *, \\boldsymbol{\\alpha}(s), \\sigma^2_\\epsilon(s))$, where $\\mathbf y^ *$ is defined \n   above.\n\nBy assumption, the elements in $\\boldsymbol{\\sigma}^2(s)$ are conditionally independent inverse-Gamma distributed random \nvariables. Thus, Step 2 amounts to sampling each element in $\\boldsymbol{\\sigma}^2(s)$ independently from their \nposterior inverse-Gamma distributions.\n',
+    'long_description': '# pybuc\n`pybuc` ((Py)thon (B)ayesian (U)nobserved (C)omponents) is a feature-limited version of R\'s Bayesian structural time \nseries package, `bsts`, written by Steven L. Scott. The source paper can be found \n[here](https://people.ischool.berkeley.edu/~hal/Papers/2013/pred-present-with-bsts.pdf) or in the *papers* \ndirectory of this repository. While there are plans to expand the feature set of `pybuc`, currently there is no roadmap \nfor the release of new features. The syntax for using `pybuc` closely follows `statsmodels`\' `UnobservedComponents` \nmodule.\n\nThe current version of `pybuc` includes the following options for modeling and \nforecasting a structural time series: \n\n- Stochastic or non-stochastic level\n- Stochastic or non-stochastic trend\n- Damped trend <sup/>*</sup>\n- Multiple stochastic or non-stochastic "dummy" seasonality\n- Multiple stochastic or non-stochastic trigonometric seasonality\n- Regression with static coefficients<sup/>**</sup>\n\n<sup/>*</sup> `pybuc` dampens trend differently than `bsts`. The former assumes an AR(1) process **without** \ndrift for the trend state equation. The latter assumes an AR(1) **with** drift. In practice this means that the trend, \non average, will be zero with `pybuc`, whereas `bsts` allows for the mean trend to be non-zero. The reason for \nchoosing an autoregressive process without drift is to be conservative with long horizon forecasts.\n\n<sup/>**</sup> `pybuc` estimates regression coefficients differently than `bsts`. The former uses a standard Gaussian \nprior. The latter uses a Bernoulli-Gaussian mixture commonly known as the spike-and-slab prior. The main \nbenefit of using a spike-and-slab prior is its promotion of coefficient-sparse solutions, i.e., variable selection, when \nthe number of predictors in the regression component exceeds the number of observed data points.\n\nFast computation is achieved using [Numba](https://numba.pydata.org/), a high performance just-in-time (JIT) compiler \nfor Python.\n\n# Installation\n```\npip install pybuc\n```\nSee `pyproject.toml` and `poetry.lock` for dependency details. This module depends on NumPy, Numba, Pandas, and \nMatplotlib. Python 3.9 and above is supported.\n\n# Motivation\n\nThe Seasonal Autoregressive Integrated Moving Average (SARIMA) model is perhaps the most widely used class of \nstatistical time series models. By design, these models can only operate on covariance-stationary time series. \nConsequently, if a time series exhibits non-stationarity (e.g., trend and/or seasonality), then the data first have to \nbe stationarized. Transforming a non-stationary series to a stationary one requires taking local and/or seasonal \ntime-differences of the data. Whether to difference the data and to what extent is a question that is answered using \nstatistical methods. \n\nOnce a stationary series is in hand, a SARIMA specification must be identified. Identifying the "right" SARIMA \nspecification can be achieved algorithmically (e.g., see the Python package `pmdarima`) or through examination of a \nseries\' patterns. The latter involves statistical and visual inspection of a series\' autocorrelation (ACF) and partial \nautocorrelation (PACF) functions. Ultimately, the necessary condition for stationarity engenders a prerequisite for \nrigorous statistical tests. It also implies that the underlying trend and seasonality, if they exist, are eliminated in \nthe process of generating a stationary series. The underlying time components that characterize a series are, therefore, \nnot of empirical interest.\n\nAnother less commonly used class of model is structural time series (STS), also known as unobserved components (UC). \nWhereas SARIMA models abstract away from an explicit model for trend and seasonality, STS/UC models do not. Thus, it is \nnot possible to visualize the underlying components that characterize a time series using a SARIMA model, but one can do \nso with a STS/UC model.\n\nSTS/UC models also have the flexibility to accommodate multiple stochastic seasonalities. SARIMA models, in contrast, \ncan accommodate multiple seasonalities, but only one seasonality/periodicity can be treated as stochastic. For example, \ndaily data may have day-of-week and week-of-year seasonality. Under a SARIMA model, only one of these seasonalities can \nbe modeled as stochastic. The other seasonality will have to be modeled as deterministic, which amounts to creating and \nusing a set of predictors that capture said seasonality. STS/UC models, on the other hand, can accommodate both \nseasonalities as stochastic by treating each as distinct, unobserved state variables.\n\nWith the above in mind, what follows is a comparison between `statsmodels`\' `SARIMAX\'` module, `statsmodels`\' \n`UnobservedComponents` module, and `pybuc`. The distinction between `statsmodels.UnobservedComponents` and `pybuc` is \nthe former is a maximum likelihood estimator (MLE) while the latter is a Bayesian estimator. The following code \ndemonstrates the application of these methods on a data set that exhibits trend and multiplicative seasonality.\nThe STS/UC specification for `statsmodels.UnobservedComponents` and `pybuc` includes stochastic level, stochastic trend \n(trend), and stochastic trigonometric seasonality with periodicity 12 and 6 harmonics.\n\n# Usage\n\n## Example: univariate time series with level, trend, and multiplicative seasonality\n\nA canonical data set that exhibits trend and seasonality is the airline passenger data used in\nBox, G.E.P.; Jenkins, G.M.; and Reinsel, G.C. Time Series Analysis, Forecasting and Control. Series G, 1976. See plot \nbelow.\n\n![plot](./examples/images/airline_passengers.png)\n\nThis data set gave rise to what is known as the "airline model", which is a SARIMA model with first-order local and \nseasonal differencing and first-order local and seasonal moving average representations. \nMore compactly, SARIMA(0, 1, 1)(0, 1, 1) without drift.\n\nTo demonstrate the performance of the "airline model" on the airline passenger data, the data will be split into a \ntraining and test set. The former will include all observations up until the last twelve months of data, and the latter \nwill include the last twelve months of data. See code below for model assessment.\n\n### Import libraries and prepare data\n\n```\nfrom pybuc import buc\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom statsmodels.tsa.statespace.sarimax import SARIMAX\nfrom statsmodels.tsa.statespace.structural import UnobservedComponents\n\n\n# Convenience function for computing root mean squared error\ndef rmse(actual, prediction):\n    act, pred = actual.flatten(), prediction.flatten()\n    return np.sqrt(np.mean((act - pred) ** 2))\n\n\n# Import airline passenger data\nurl = "https://raw.githubusercontent.com/devindg/pybuc/master/examples/data/airline-passengers.csv"\nair = pd.read_csv(url, header=0, index_col=0)\nair = air.astype(float)\nair.index = pd.to_datetime(air.index)\nhold_out_size = 12\n\n# Create train and test sets\ny_train = air.iloc[:-hold_out_size]\ny_test = air.iloc[-hold_out_size:]\n```\n\n### SARIMA\n\n```\n\'\'\' Fit the airline data using SARIMA(0,1,1)(0,1,1) \'\'\'\nsarima = SARIMAX(y_train, order=(0, 1, 1),\n                 seasonal_order=(0, 1, 1, 12),\n                 trend=[0])\nsarima_res = sarima.fit(disp=False)\nprint(sarima_res.summary())\n\n# Plot in-sample fit against actuals\nplt.plot(y_train)\nplt.plot(sarima_res.fittedvalues)\nplt.title(\'SARIMA: In-sample\')\nplt.xticks(rotation=45, ha="right")\nplt.show()\n\n# Get and plot forecast\nsarima_forecast = sarima_res.get_forecast(hold_out_size).summary_frame(alpha=0.05)\nplt.plot(y_test)\nplt.plot(sarima_forecast[\'mean\'])\nplt.fill_between(sarima_forecast.index,\n                 sarima_forecast[\'mean_ci_lower\'],\n                 sarima_forecast[\'mean_ci_upper\'], alpha=0.2)\nplt.title(\'SARIMA: Forecast\')\nplt.legend([\'Actual\', \'Mean\', \'95% Prediction Interval\'])\nplt.show()\n\n# Print RMSE\nprint(f"SARIMA RMSE: {rmse(y_test.to_numpy(), sarima_forecast[\'mean\'].to_numpy())}")\n```\nThe SARIMA(0, 1, 1)(0, 1, 1) forecast plot and root mean squared error (RMSE) are shown below. \n\n![plot](./examples/images/airline_passengers_sarima_forecast.png)\n\n```\nSARIMA RMSE: 21.09028021383853\n```\n\n### MLE Unobserved Components\n\n```\n\'\'\' Fit the airline data using MLE unobserved components \'\'\'\nmle_uc = UnobservedComponents(y_train, exog=None, irregular=True,\n                              level=True, stochastic_level=True,\n                              trend=True, stochastic_trend=True,\n                              freq_seasonal=[{\'period\': 12, \'harmonics\': 6}],\n                              stochastic_freq_seasonal=[True])\n\n# Fit the model via maximum likelihood\nmle_uc_res = mle_uc.fit(disp=False)\nprint(mle_uc_res.summary())\n\n# Plot in-sample fit against actuals\nplt.plot(y_train)\nplt.plot(mle_uc_res.fittedvalues)\nplt.title(\'MLE UC: In-sample\')\nplt.show()\n\n# Plot time series components\nmle_uc_res.plot_components(legend_loc=\'lower right\', figsize=(15, 9), which=\'smoothed\')\nplt.show()\n\n# Get and plot forecast\nmle_uc_forecast = mle_uc_res.get_forecast(hold_out_size).summary_frame(alpha=0.05)\nplt.plot(y_test)\nplt.plot(mle_uc_forecast[\'mean\'])\nplt.fill_between(mle_uc_forecast.index,\n                 mle_uc_forecast[\'mean_ci_lower\'],\n                 mle_uc_forecast[\'mean_ci_upper\'], alpha=0.2)\nplt.title(\'MLE UC: Forecast\')\nplt.legend([\'Actual\', \'Mean\', \'95% Prediction Interval\'])\nplt.show()\n\n# Print RMSE\nprint(f"MLE UC RMSE: {rmse(y_test.to_numpy(), mle_uc_forecast[\'mean\'].to_numpy())}")\n```\n\nThe MLE Unobserved Components forecast plot, components plot, and RMSE are shown below.\n\n![plot](./examples/images/airline_passengers_mle_uc_forecast.png)\n\n![plot](./examples/images/airline_passengers_mle_uc_components.png)\n\n```\nMLE UC RMSE: 17.961873327622694\n```\n\nAs noted above, a distinguishing feature of STS/UC models is their explicit modeling of trend and seasonality. This is \nillustrated with the components plot.\n\nFinally, the Bayesian analog of the MLE STS/UC model is demonstrated. Default parameter values are used for the priors \ncorresponding to the variance parameters in the model. If no explicit prior is given, by default each variance\'s prior \nis assumed to be inverse-Gamma with shape and scale values equal to 1e-6. This approximates what is known as Jeffreys \nprior, a vague/non-informative prior.\n\n**Note that because computation is built on Numba, a JIT compiler, the first run of the code could take a while. \nSubsequent runs (assuming the Python kernel isn\'t restarted) should execute considerably faster.**\n\n### Bayesian Unobserved Components\n```\n\'\'\' Fit the airline data using Bayesian unobserved components \'\'\'\nbayes_uc = buc.BayesianUnobservedComponents(response=y_train,\n                                                level=True, stochastic_level=True,\n                                                trend=True, stochastic_trend=True, autoregressive_trend=False,\n                                                dummy_seasonal=(), stochastic_dummy_seasonal=(),\n                                                trig_seasonal=((12, 0), ), stochastic_trig_seasonal=(True,),\n                                                seed=123)\n\npost = bayes_uc.sample(5000)\nmcmc_burn = 100\n\n# Print summary of estimated parameters\nfor key, value in bayes_uc.summary(burn=mcmc_burn).items():\n    print(key, \' : \', value)\n\n# Plot in-sample fit against actuals\nyhat = np.mean(post.filtered_prediction[mcmc_burn:], axis=0)\nplt.plot(y_train)\nplt.plot(y_train.index, yhat)\nplt.title(\'Bayesian-UC: In-sample\')\nplt.show()\n\n# Plot time series components\nbayes_uc.plot_components(burn=mcmc_burn, smoothed=True)\nplt.show()\n\n# Get and plot forecast\nforecast = bayes_uc.forecast(hold_out_size, mcmc_burn)\nforecast_mean = np.mean(forecast, axis=0)\nforecast_l95 = np.quantile(forecast, 0.025, axis=0).flatten()\nforecast_u95 = np.quantile(forecast, 0.975, axis=0).flatten()\n\nplt.plot(y_test)\nplt.plot(bayes_uc.future_time_index, forecast_mean)\nplt.fill_between(bayes_uc.future_time_index, forecast_l95, forecast_u95, alpha=0.2)\nplt.title(\'Bayesian UC: Forecast\')\nplt.legend([\'Actual\', \'Mean\', \'95% Prediction Interval\'])\nplt.show()\n\n# Print RMSE\nprint(f"BAYES-UC RMSE: {rmse(y_test.to_numpy(), forecast_mean)}")\n```\n\nThe Bayesian Unobserved Components forecast plot, components plot, and RMSE are shown below.\n\n![plot](./examples/images/airline_passengers_bayes_uc_forecast.png)\n\n![plot](./examples/images/airline_passengers_bayes_uc_components.png)\n\n```\nBAYES-UC RMSE: 17.412932828154464\n```\n\n# Model\n\nA structural time series model with level, trend, seasonal, and regression components takes the form: \n\n$$\ny_t = \\mu_t + \\gamma_t + \\mathbf x_t^\\prime \\boldsymbol{\\beta} + \\epsilon_t\n$$ \n\nwhere $\\mu_t$ specifies an unobserved dynamic level component, $\\gamma_t$ an unobserved dynamic seasonal component, \n$\\mathbf x_t^\\prime \\boldsymbol{\\beta}$ a partially unobserved regression component (the regressors $\\mathbf x_t$ are \nobserved, but the coefficients $\\boldsymbol{\\beta}$ are not), and $\\epsilon_t \\sim N(0, \\sigma_{\\epsilon}^2)$ an \nunobserved irregular component. The equation describing the outcome $y_t$ is commonly referred to as the observation \nequation, and the transition equations governing the evolution of the unobserved states are known as the state \nequations.\n\n## Level and trend\n\nThe unobserved level evolves according to the following general transition equations:\n\n$$\n\\begin{align}\n    \\mu_{t+1} &= \\mu_t + \\delta_t + \\eta_{\\mu, t} \\\\ \n    \\delta_{t+1} &= \\phi \\delta_t + \\eta_{\\delta, t} \n\\end{align}\n$$ \n\nwhere $\\eta_{\\mu, t} \\sim N(0, \\sigma_{\\eta_\\mu}^2)$ and $\\eta_{\\delta, t} \\sim N(0, \\sigma_{\\eta_\\delta}^2)$ for all \n$t$. The state equation for $\\delta_t$ represents the local trend at time $t$. \n\nThe parameter $\\phi$ represents an autoregressive coefficient. In general, $\\phi$ is expected to be in the interval \n$(-1, 1)$, which implies a stationary process for trend. In practice, however, it is possible for $\\phi$ to be \noutside the unit circle, which implies an explosive process. While it is mathematically possible for an explosive \nprocess to be stationary, the implication of such a result implies that the future predicts the past, which is not a \nrealistic assumption. \n\nIf an autoregressive trend is specified, no hard constraints (by default) are placed on the bounds of $\\phi$. Instead, \nthe default prior for $\\phi$ is $N(0, 0.25)$. Thus, -1 and 1 are within two standard deviations of the mean. It is \ntherefore possible for the Gibbs sampler to sample values outside the unit circle. If the posterior mean of $\\phi$ is \noutside the unit circle (or very close to the bounds), then an autoregressive trend is not a good assumption. If only \na "few" of the posterior samples have $\\phi$ outside the unit circle, this shouldn\'t be problematic for forecasting. \n$\\phi$ is set to 1 if a damped trend is not specified.\n\nFinally, note that if $\\sigma_{\\eta_\\mu}^2 = \\sigma_{\\eta_\\delta}^2 = 0$ and $\\phi = 1$, then the level component in \nthe observation equation, $\\mu_t$, collapses to a deterministic intercept and linear time trend.\n\n## Seasonality\n\n### Dummy form\nThe seasonal component, $\\gamma_t$, can be modeled in two ways. One way is known as the "dummy" variable approach. \nFormally, the seasonal effect on the outcome $y$ is modeled as \n\n$$\n\\sum_{j=0}^{S-1} \\gamma_{t-j} = \\eta_{\\gamma, t} \\iff \\gamma_t = -\\sum_{j=1}^{S-1} \\gamma_{t-j} + \\eta_{\\gamma, t},\n$$ \n\nwhere $j$ indexes the number of periods in a seasonal cycle, $S$ is the number of periods in a seasonal cycle, and \n$\\eta_{\\gamma, t} \\sim N(0, \\sigma_{\\eta_\\gamma}^2)$ for all $t$. Intuitively, if a time series exhibits periodicity, \nthen the sum of the periodic effects over a cycle should, on average, be zero.\n\n### Trigonometric form\nAnother way to model seasonality is through a trigonometric representation, which exploits the periodicity of sine and \ncosine functions. Specifically, seasonality is modeled as\n\n$$\n\\gamma_t = \\sum_{j=1}^h \\gamma_{j, t}\n$$\n\nwhere $j$ indexes the number of harmonics to represent seasonality of periodicity $S$ and \n$1 \\leq h \\leq \\lfloor S/2 \\rfloor$ is the highest desired number of harmonics. The state transition equations for each \nharmonic, $\\gamma_{j, t}$, are represented by a real and imaginary part, specifically\n\n$$\n\\begin{align}\n    \\gamma_{j, t+1} &= \\cos(\\lambda_j) \\gamma_{j, t} + \\sin(\\lambda_j) \\gamma_{j, t}^* + \\eta_{\\gamma_j, t} \\\\\n    \\gamma_{j, t+1}^* &= -\\sin(\\lambda_j) \\gamma_{j, t} + \\cos(\\lambda_j) \\gamma_{j, t}^* + \\eta_{\\gamma_j^* , t}\n\\end{align}\n$$\n\nwhere frequency $\\lambda_j = 2j\\pi / S$. It is assumed that $\\eta_{\\gamma_j, t}$ and $\\eta_{\\gamma_j^ * , t}$ are \ndistributed $N(0, \\sigma^2_{\\eta_\\gamma})$ for all $j, t$.\n\n## Regression\nThere are two ways to configure the model matrices to account for a regression component with static coefficients. \nThe canonical way (Method 1) is to append $\\mathbf x_t^\\prime$ to $\\mathbf Z_t$ and $\\boldsymbol{\\beta}_t$ to the \nstate vector, $\\boldsymbol{\\alpha}_t$ (see state space representation below), with the constraints \n$\\boldsymbol{\\beta}_0 = \\boldsymbol{\\beta}$ and $\\boldsymbol{\\beta}_t = \\boldsymbol{\\beta} _{t-1}$ for all $t$. \nAnother, less common way (Method 2) is to append $\\mathbf x_t^\\prime \\boldsymbol{\\beta}$ to $\\mathbf Z_t$ and 1 to the \nstate vector. \n\nWhile both methods can be accommodated by the Kalman filter, Method 1 is a direct extension of the Kalman filter as it \nmaintains the observability of $\\mathbf Z_t$ and treats the regression coefficients as unobserved states. Method 2 does \nnot fit naturally into the conventional framework of the Kalman filter, but it offers the significant advantage of only \nincreasing the size of the state vector by one. In contrast, Method 1 increases the size of the state vector by the size \nof $\\boldsymbol{\\beta}$. This is significant because computational complexity is quadratic in the size of the state \nvector but linear in the size of the observation vector.\n\nThe unobservability of $\\mathbf Z_t$ under Method 2 can be handled with maximum likelihood or Bayesian estimation by \nworking with the adjusted series \n\n$$\ny_t^* \\equiv y_t - \\tau_t = \\mathbf x_ t^\\prime \\boldsymbol{\\beta} + \\epsilon_t\n$$\n\nwhere $\\tau_t$ represents the time series component of the structural time series model. For example, assuming a level \nand seasonal component are specified, this means an initial estimate of the time series component \n$\\tau_t = \\mu_t + \\gamma_t$ and $\\boldsymbol{\\beta}$ has to be acquired first. Then $\\boldsymbol{\\beta}$ can be \nestimated conditional on \n$\\mathbf y^ * \\equiv \\left(\\begin{array}{cc} y_1^ * & y_2^ * & \\cdots & y_n^ * \\end{array}\\right)^\\prime$.\n\n`pybuc` uses Method 2 for estimating static coefficients.\n\n## State space representation (example)\nThe unobserved components model can be rewritten in state space form. For example, suppose level, trend, seasonal, \nregression, and irregular components are specified, and the seasonal component takes a trigonometric form with \nperiodicity $S=4$ and $h=2$ harmonics. Let $\\mathbf Z_t \\in \\mathbb{R}^{1 \\times m}$, \n$\\mathbf T \\in \\mathbb{R}^{m \\times m}$, $\\mathbf R \\in \\mathbb{R}^{m \\times q}$, and \n$\\boldsymbol{\\alpha}_ t \\in \\mathbb{R}^{m \\times 1}$ denote the observation matrix, state transition matrix, \nstate error transformation matrix, and unobserved state vector, respectively, where $m$ is the number of state equations \nand $q$ is the number of state parameters to be estimated (i.e., the number of stochastic state equations, \nwhich is defined by the number of positive state variance parameters). \n\nThere are $m = 1 + 1 + h * 2 + 1 = 7$ state equations and $q = 1 + 1 + h * 2 = 6$ stochastic state equations. There are \n6 stochastic state equations because the state value for the regression component is not stochastic; it is 1 for all $t$ \nby construction. The observation, state transition, and state error transformation matrices may be written as\n\n$$\n\\begin{align}\n    \\mathbf Z_t &= \\left(\\begin{array}{cc} \n                        1 & 0 & 1 & 0 & 1 & 0 & \\mathbf x_t^{\\prime} \\boldsymbol{\\beta}\n                        \\end{array}\\right) \\\\\n    \\mathbf T &= \\left(\\begin{array}{cc} \n                        1 & 1 & 0 & 0 & 0 & 0 & 0 \\\\\n                        0 & 1 & 0 & 0 & 0 & 0 & 0 \\\\\n                        0 & 0 & \\cos(2\\pi / 4) & \\sin(2\\pi / 4) & 0 & 0 & 0 \\\\\n                        0 & 0 & -\\sin(2\\pi / 4) & \\cos(2\\pi / 4) & 0 & 0 & 0 \\\\\n                        0 & 0 & 0 & 0 & \\cos(4\\pi / 4) & \\sin(4\\pi / 4) & 0 \\\\\n                        0 & 0 & 0 & 0 & -\\sin(4\\pi / 4) & \\cos(4\\pi / 4) & 0 \\\\\n                        0 & 0 & 0 & 0 & 0 & 0 & 1\n                        \\end{array}\\right) \\\\\n    \\mathbf R &= \\left(\\begin{array}{cc} \n                    1 & 0 & 0 & 0 & 0 & 0 \\\\\n                    0 & 1 & 0 & 0 & 0 & 0 \\\\\n                    0 & 0 & 1 & 0 & 0 & 0 \\\\\n                    0 & 0 & 0 & 1 & 0 & 0 \\\\\n                    0 & 0 & 0 & 0 & 1 & 0 \\\\\n                    0 & 0 & 0 & 0 & 0 & 1 \\\\\n                    0 & 0 & 0 & 0 & 0 & 0\n                    \\end{array}\\right)\n\\end{align}\n$$\n\nGiven the definitions of $\\mathbf Z_t$, $\\mathbf T$, and $\\mathbf R$, the state space representation of the unobserved \ncomponents model above can compactly be expressed as\n\n$$\n\\begin{align}\n    y_t &= \\mathbf Z_t \\boldsymbol{\\alpha}_ t + \\epsilon_t \\\\\n    \\boldsymbol{\\alpha}_ {t+1} &= \\mathbf T \\boldsymbol{\\alpha}_ t + \\mathbf R \\boldsymbol{\\eta}_ t, \\hspace{5pt} \n    t=1,2,...,n\n\\end{align}\n$$\n\nwhere\n\n$$\n\\begin{align}\n    \\boldsymbol{\\alpha}_ t &= \\left(\\begin{array}{cc} \n                            \\mu_t & \\delta_t & \\gamma_{1, t} & \\gamma_{1, t}^* & \\gamma_{2, t} & \\gamma_{2, t}^* & 1\n                            \\end{array}\\right)^\\prime \\\\\n    \\boldsymbol{\\eta}_ t &= \\left(\\begin{array}{cc} \n                            \\eta_{\\mu, t} & \\eta_{\\delta, t} & \\eta_{\\gamma_ 1, t} & \\eta_{\\gamma_ 1^\\*, t} & \n                            \\eta_{\\gamma_ 2, t} & \\eta_{\\gamma_ 2^\\*, t}\n                            \\end{array}\\right)^\\prime\n\\end{align}\n$$\n\nand \n\n$$\n\\mathrm{Cov}(\\boldsymbol{\\eta}_ t) = \\mathrm{Cov}(\\boldsymbol{\\eta}_ {t-1}) = \\boldsymbol{\\Sigma}_ \\eta = \n\\mathrm{diag}(\\sigma^2_{\\eta_\\mu}, \\sigma^2_{\\eta_\\delta}, \\sigma^2_{\\eta_{\\gamma_ 1}}, \\sigma^2_{\\eta_{\\gamma_ 1^\\*}}, \n\\sigma^2_{\\eta_{\\gamma_ 2}}, \\sigma^2_{\\eta_{\\gamma_ 2^\\*}}) \\in \\mathbb{R}^{6 \\times 6} \\hspace{5pt} \\textrm{for all } \nt=1,2,...,n\n$$\n\n# Estimation\n`pybuc` mirrors R\'s `bsts` with respect to estimation method. The observation vector, state vector, and regression \ncoefficients are assumed to be conditionally normal random variables, and the error variances are assumed to be \nconditionally independent inverse-Gamma random variables. These model assumptions imply conditional conjugacy of the \nmodel\'s parameters. Consequently, a Gibbs sampler is used to sample from each parameter\'s posterior distribution.\n\nTo achieve fast sampling, `pybuc` follows `bsts`\'s adoption of the Durbin and Koopman (2002) simulation smoother. For \nany parameter $\\theta$, let $\\theta(s)$ denote the $s$-th sample of parameter $\\theta$. Each sample $s$ is drawn by \nrepeating the following three steps:\n\n1. Draw $\\boldsymbol{\\alpha}(s)$ from \n   $p(\\boldsymbol{\\alpha} | \\mathbf y, \\boldsymbol{\\sigma}^2_\\eta(s-1), \\boldsymbol{\\beta}(s-1), \\sigma^2_\\epsilon(s-1))$ \n   using the Durbin and Koopman simulation state smoother, where \n   $\\boldsymbol{\\alpha}(s) = (\\boldsymbol{\\alpha}_ 1(s), \\boldsymbol{\\alpha}_ 2(s), \\cdots, \\boldsymbol{\\alpha}_ n(s))^\\prime$ \n   and $\\boldsymbol{\\sigma}^2_\\eta(s-1) = \\mathrm{diag}(\\boldsymbol{\\Sigma}_\\eta(s-1))$. Note that `pybuc` implements a \n   correction (based on a potential misunderstanding) for drawing $\\boldsymbol{\\alpha}(s)$ per "A note on implementing \n   the Durbin and Koopman simulation smoother" (Marek Jarocinski, 2015).\n2. Draw $\\boldsymbol{\\sigma}^2(s) = (\\sigma^2_ \\epsilon(s), \\boldsymbol{\\sigma}^2_ \\eta(s))^\\prime$ from \n   $p(\\boldsymbol{\\sigma}^2 | \\mathbf y, \\boldsymbol{\\alpha}(s), \\boldsymbol{\\beta}(s-1))$ using Durbin and Koopman\'s \n   simulation disturbance smoother.\n3. Draw $\\boldsymbol{\\beta}(s)$ from \n   $p(\\boldsymbol{\\beta} | \\mathbf y^ *, \\boldsymbol{\\alpha}(s), \\sigma^2_\\epsilon(s))$, where $\\mathbf y^ *$ is defined \n   above.\n\nBy assumption, the elements in $\\boldsymbol{\\sigma}^2(s)$ are conditionally independent inverse-Gamma distributed random \nvariables. Thus, Step 2 amounts to sampling each element in $\\boldsymbol{\\sigma}^2(s)$ independently from their \nposterior inverse-Gamma distributions.\n',
     'author': 'Devin D. Garcia',
     'author_email': None,
     'maintainer': None,
     'maintainer_email': None,
     'url': None,
     'packages': packages,
     'package_data': package_data,
```

### Comparing `pybuc-0.8.10/PKG-INFO` & `pybuc-0.9.10/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pybuc
-Version: 0.8.10
+Version: 0.9.10
 Summary: Fast estimation of Bayesian structural time series models via Gibbs sampling.
 License: BSD 3-Clause
 Keywords: structural time series,unobserved components,bayesian,bsts
 Author: Devin D. Garcia
 Requires-Python: >=3.9,<3.11
 Classifier: License :: Other/Proprietary License
 Classifier: Programming Language :: Python :: 3
@@ -228,17 +228,16 @@
 ```
 
 As noted above, a distinguishing feature of STS/UC models is their explicit modeling of trend and seasonality. This is 
 illustrated with the components plot.
 
 Finally, the Bayesian analog of the MLE STS/UC model is demonstrated. Default parameter values are used for the priors 
 corresponding to the variance parameters in the model. If no explicit prior is given, by default each variance's prior 
-is assumed to be inverse-Gamma with shape and scale values equal to 1 and 0.01, respectively. Note that a common 
-inverse-Gamma prior for variance parameters has shape and scale values equal to 0.001. This approximates what is known 
-as Jeffreys prior, a vague/non-informative prior.
+is assumed to be inverse-Gamma with shape and scale values equal to 1e-6. This approximates what is known as Jeffreys 
+prior, a vague/non-informative prior.
 
 **Note that because computation is built on Numba, a JIT compiler, the first run of the code could take a while. 
 Subsequent runs (assuming the Python kernel isn't restarted) should execute considerably faster.**
 
 ### Bayesian Unobserved Components
 ```
 ''' Fit the airline data using Bayesian unobserved components '''
```

