# Comparing `tmp/searchlogit-0.2.98.tar.gz` & `tmp/searchlogit-0.2.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "searchlogit-0.2.98.tar", last modified: Tue Oct 11 02:32:37 2022, max compression
+gzip compressed data, was "searchlogit-0.2.99.tar", last modified: Tue Oct 11 06:20:33 2022, max compression
```

## Comparing `searchlogit-0.2.98.tar` & `searchlogit-0.2.99.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-11 02:32:37.310261 searchlogit-0.2.98/
--rw-r--r--   0 runner    (1001) docker     (121)    35149 2022-10-11 02:32:22.000000 searchlogit-0.2.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)    10856 2022-10-11 02:32:37.310261 searchlogit-0.2.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    10474 2022-10-11 02:32:22.000000 searchlogit-0.2.98/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-11 02:32:37.310261 searchlogit-0.2.98/searchlogit/
--rw-r--r--   0 runner    (1001) docker     (121)      248 2022-10-11 02:32:23.000000 searchlogit-0.2.98/searchlogit/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    34894 2022-10-11 02:32:23.000000 searchlogit-0.2.98/searchlogit/_choice_model.py
--rw-r--r--   0 runner    (1001) docker     (121)     1920 2022-10-11 02:32:23.000000 searchlogit-0.2.98/searchlogit/_device.py
--rw-r--r--   0 runner    (1001) docker     (121)     4662 2022-10-11 02:32:23.000000 searchlogit-0.2.98/searchlogit/boxcox_functions.py
--rw-r--r--   0 runner    (1001) docker     (121)    41592 2022-10-11 02:32:23.000000 searchlogit-0.2.98/searchlogit/latent_class_mixed_model.py
--rw-r--r--   0 runner    (1001) docker     (121)    39052 2022-10-11 02:32:23.000000 searchlogit-0.2.98/searchlogit/latent_class_model.py
--rw-r--r--   0 runner    (1001) docker     (121)    57625 2022-10-11 02:32:23.000000 searchlogit-0.2.98/searchlogit/mixed_logit.py
--rw-r--r--   0 runner    (1001) docker     (121)    15621 2022-10-11 02:32:23.000000 searchlogit-0.2.98/searchlogit/multinomial_logit.py
--rw-r--r--   0 runner    (1001) docker     (121)   155603 2022-10-11 02:32:23.000000 searchlogit-0.2.98/searchlogit/search.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-11 02:32:37.310261 searchlogit-0.2.98/searchlogit.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)    10856 2022-10-11 02:32:37.000000 searchlogit-0.2.98/searchlogit.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      509 2022-10-11 02:32:37.000000 searchlogit-0.2.98/searchlogit.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-11 02:32:37.000000 searchlogit-0.2.98/searchlogit.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-11 02:32:37.000000 searchlogit-0.2.98/searchlogit.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)       27 2022-10-11 02:32:37.000000 searchlogit-0.2.98/searchlogit.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       12 2022-10-11 02:32:37.000000 searchlogit-0.2.98/searchlogit.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       79 2022-10-11 02:32:37.310261 searchlogit-0.2.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)      893 2022-10-11 02:32:23.000000 searchlogit-0.2.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-11 06:20:32.997588 searchlogit-0.2.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    35149 2022-10-11 06:20:23.000000 searchlogit-0.2.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)    10856 2022-10-11 06:20:32.997588 searchlogit-0.2.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    10474 2022-10-11 06:20:23.000000 searchlogit-0.2.99/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-11 06:20:32.997588 searchlogit-0.2.99/searchlogit/
+-rw-r--r--   0 runner    (1001) docker     (121)      248 2022-10-11 06:20:24.000000 searchlogit-0.2.99/searchlogit/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    34894 2022-10-11 06:20:24.000000 searchlogit-0.2.99/searchlogit/_choice_model.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1920 2022-10-11 06:20:24.000000 searchlogit-0.2.99/searchlogit/_device.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4662 2022-10-11 06:20:24.000000 searchlogit-0.2.99/searchlogit/boxcox_functions.py
+-rw-r--r--   0 runner    (1001) docker     (121)    41592 2022-10-11 06:20:24.000000 searchlogit-0.2.99/searchlogit/latent_class_mixed_model.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39052 2022-10-11 06:20:24.000000 searchlogit-0.2.99/searchlogit/latent_class_model.py
+-rw-r--r--   0 runner    (1001) docker     (121)    57625 2022-10-11 06:20:24.000000 searchlogit-0.2.99/searchlogit/mixed_logit.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15621 2022-10-11 06:20:24.000000 searchlogit-0.2.99/searchlogit/multinomial_logit.py
+-rw-r--r--   0 runner    (1001) docker     (121)   157220 2022-10-11 06:20:24.000000 searchlogit-0.2.99/searchlogit/search.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-11 06:20:32.997588 searchlogit-0.2.99/searchlogit.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)    10856 2022-10-11 06:20:32.000000 searchlogit-0.2.99/searchlogit.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      509 2022-10-11 06:20:32.000000 searchlogit-0.2.99/searchlogit.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-11 06:20:32.000000 searchlogit-0.2.99/searchlogit.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-11 06:20:32.000000 searchlogit-0.2.99/searchlogit.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)       27 2022-10-11 06:20:32.000000 searchlogit-0.2.99/searchlogit.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       12 2022-10-11 06:20:32.000000 searchlogit-0.2.99/searchlogit.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       79 2022-10-11 06:20:32.997588 searchlogit-0.2.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)      893 2022-10-11 06:20:24.000000 searchlogit-0.2.99/setup.py
```

### Comparing `searchlogit-0.2.98/LICENSE` & `searchlogit-0.2.99/LICENSE`

 * *Files identical despite different names*

### Comparing `searchlogit-0.2.98/PKG-INFO` & `searchlogit-0.2.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: searchlogit
-Version: 0.2.98
+Version: 0.2.99
 Summary: Extensions for a Python package for                               GPU-accelerated estimation of mixed logit models.
 Home-page: https://github.com/RyanJafefKelly/searchlogit
 Author: Ryan Kelly
 Author-email: ryan@kiiii.com
 License: MIT
 Requires-Python: >=3.5
 Description-Content-Type: text/x-rst
```

### Comparing `searchlogit-0.2.98/README.rst` & `searchlogit-0.2.99/README.rst`

 * *Files identical despite different names*

### Comparing `searchlogit-0.2.98/searchlogit/_choice_model.py` & `searchlogit-0.2.99/searchlogit/_choice_model.py`

 * *Files identical despite different names*

### Comparing `searchlogit-0.2.98/searchlogit/_device.py` & `searchlogit-0.2.99/searchlogit/_device.py`

 * *Files identical despite different names*

### Comparing `searchlogit-0.2.98/searchlogit/boxcox_functions.py` & `searchlogit-0.2.99/searchlogit/boxcox_functions.py`

 * *Files identical despite different names*

### Comparing `searchlogit-0.2.98/searchlogit/latent_class_mixed_model.py` & `searchlogit-0.2.99/searchlogit/latent_class_mixed_model.py`

 * *Files identical despite different names*

### Comparing `searchlogit-0.2.98/searchlogit/latent_class_model.py` & `searchlogit-0.2.99/searchlogit/latent_class_model.py`

 * *Files identical despite different names*

### Comparing `searchlogit-0.2.98/searchlogit/mixed_logit.py` & `searchlogit-0.2.99/searchlogit/mixed_logit.py`

 * *Files identical despite different names*

### Comparing `searchlogit-0.2.98/searchlogit/multinomial_logit.py` & `searchlogit-0.2.99/searchlogit/multinomial_logit.py`

 * *Files identical despite different names*

### Comparing `searchlogit-0.2.98/searchlogit/search.py` & `searchlogit-0.2.99/searchlogit/search.py`

 * *Files 1% similar despite different names*

```diff
@@ -1673,54 +1673,75 @@
         # Create initial harmony memory
         unique_HM = []
         dummy_iter = 0  # prevent stuck in while loop
         while dummy_iter < 30000:
             dummy_iter += 1
             logger.info("Initializing harmony at iteration {}".format(dummy_iter))
             sol = self.generate_sol()
-            all_HM = HM + opp_HM
             sol, conv = self.evaluate_objective_function(sol)
 
             if conv:
                 HM.append(sol)
                 # keep only unique solutions in memory
                 used = set()
                 unique_HM = [used.add(x['bic']) or x for x in HM
                              if x['bic'] not in used]
                 unique_HM = sorted(unique_HM, key=lambda x: x['bic'])
                 logger.debug("harmony memory for iteration: {}, is: {}".format(dummy_iter, str(unique_HM)))
 
             logger.debug("estimating opposite harmony memory")
 
-            # TODO! NOT DONE PROPERLY? 
             # create opposite harmony memory with variables that were not included in the harmony memory's solution
 
             opp_sol = self.generate_sol()
+            # TODO: hacky approach
+            sol_keys = ['asvars', 'isvars', 'randvars', 'bcvars', 'cor_vars',
+                        'bctrans', 'cor']
+            for sol_key in sol_keys:
+                if not opp_sol[sol_key]:
+                    continue
+                if isinstance(opp_sol[sol_key], bool):
+                    continue
+                opp_sol[sol_key] = [v for v in opp_sol[sol_key] if v not in sol[sol_key]]
+
+            opp_sol['asc_ind'] = not sol['asc_ind']
+
+            if opp_sol['class_params_spec'] is not None and  sol['class_params_spec'] is not None:
+                for ii, class_param in enumerate(opp_sol['class_params_spec']):
+                    opp_sol['class_params_spec'][ii] = np.array([param_i for param_i in class_param
+                                                        if param_i not in sol['class_params_spec'][ii]])
+
+            if opp_sol['member_params_spec'] is not None and sol['member_params_spec'] is not None:
+                for ii, member_param in enumerate(opp_sol['member_params_spec']):
+                    opp_sol['member_params_spec'][ii] = np.array([param_i for param_i in member_param
+                                                        if param_i not in sol['member_params_spec'][ii]])
 
-            all_HM = HM + opp_HM
             opp_sol, opp_conv = self.evaluate_objective_function(opp_sol)
 
             unique_opp_HM = []
             if opp_conv:
                 opp_HM.append(opp_sol)
                 opp_used = set()
                 unique_opp_HM = [opp_used.add(x['bic']) or x for x in opp_HM
                                  if x['bic'] not in opp_used]
                 unique_opp_HM = sorted(unique_opp_HM, key=lambda x: x['bic'])
                 logger.debug("unique_opp_HM is for iteration: {} is: {}".format(dummy_iter, str(unique_opp_HM)))
 
-                if len(unique_opp_HM) == HMS:
-                        break
+                # if len(unique_opp_HM) == HMS:
+                #         break
 
             # Final Initial Harmony
             Init_HM = unique_HM + unique_opp_HM
 
             unique = set()
             unique_Init_HM = [unique.add(x['bic']) or x for x in Init_HM
                               if x['bic'] not in unique]
+            unique_Init_HM = [init_sol for _, init_sol in enumerate(unique_Init_HM)
+                              if np.abs(init_sol['bic']) < 1000000]
+
 
             if len(unique_Init_HM) >= HMS:
                 unique_Init_HM = unique_Init_HM[:HMS]
                 return unique_Init_HM
 
         return unique_Init_HM
 
@@ -1788,24 +1809,24 @@
             new_sol['cor_vars'] = new_corvars
 
             # Take fit_intercept from m_pos solution in memory
             intercept = har_mem[m_pos]['asc_ind']
             new_sol['asc_ind'] = intercept
 
             if har_mem[m_pos]['class_params_spec'] is not None:
-                class_params_spec = har_mem[m_pos]['class_params_spec'].copy()
+                class_params_spec = copy.deepcopy(har_mem[m_pos]['class_params_spec'])
                 for ii, class_params in enumerate(class_params_spec):
                     class_params_index = self.random_state.choice([0, 1],
                                                         size=len(class_params),
                                                         p=[1-HMCR_itr, HMCR_itr])
                     class_params_spec[ii] = np.array([i for (i, v) in zip(class_params, class_params_index) if v], dtype=class_params.dtype)
                 new_sol['class_params_spec'] = class_params_spec
 
             if har_mem[m_pos]['member_params_spec'] is not None:
-                member_params_spec = har_mem[m_pos]['member_params_spec'].copy()
+                member_params_spec = copy.deepcopy(har_mem[m_pos]['member_params_spec'])
                 for ii, member_params in enumerate(member_params_spec):
                     member_params_index = self.random_state.choice([0, 1],
                                                         size=len(member_params),
                                                         p=[1-HMCR_itr, HMCR_itr])
                     member_params_spec[ii] = np.array([i for (i, v) in zip(member_params, member_params_index) if v], dtype=member_params.dtype)
                 new_sol['member_params_spec'] = member_params_spec
 
@@ -2103,15 +2124,15 @@
 
         # Stop bug where _inter in class params but intercept is false
         asc_ind = solution['asc_ind']
 
         improved_sol, conv = self.evaluate_objective_function(solution)
 
         if conv:
-            improved_sol_copy = improved_sol.copy()
+            improved_sol_copy = copy.deepcopy(improved_sol)
             har_mem.append(improved_sol_copy)
 
         seen = set()
         seen_add = seen.add
         val_key = 'MAE' if self.multi_objective else 'loglik'
 
         new_hm = [x for x in har_mem if tuple([x['bic'], x[val_key]]) not in seen and
@@ -2136,97 +2157,107 @@
             if it is unique and provides an improved BIC
 
         Inputs:
         solution list generated from harmony consideration step
         harmony memory
         Pitch adjustment rate for the given iteration
         """
-        improved_harmony = har_mem
+        # improved_harmony = har_mem
+        # if self.random_state.rand() <= PAR_itr:
+        pa_sol = copy.deepcopy(sol)
+        if self.random_state.rand() <= PAR_itr:
+            logger.debug("pitch adjustment adding as variables")
+            pa_sol = self.add_new_asfeature(sol)
+            # improved_harmony, pa_sol = self.assess_sol(pa_sol,
+            #                                             har_mem)
+
+        if self.random_state.rand() <= PAR_itr:
+            if self.isvarnames:
+                logger.debug("pitch adjustment adding is variables")
+                pa_sol = self.add_new_isfeature(pa_sol)
+                # improved_harmony, pa_sol = self.assess_sol(pa_sol,
+                #                                             har_mem)
+
+        if self.random_state.rand() <= PAR_itr:
+            if self.ps_bctrans is None or self.ps_bctrans:
+                logger.debug("pitch adjustment adding bc variables")
+                pa_sol = self.add_new_bcfeature(pa_sol, PAR_itr)
+                # improved_harmony, pa_sol = self.assess_sol(pa_sol,
+                #                                             har_mem)
+
+        if self.random_state.rand() <= PAR_itr:
+            if self.ps_cor is None or self.ps_cor:
+                logger.debug("pitch adjustment adding cor variables")
+                pa_sol = self.add_new_corfeature(pa_sol)
+                # improved_harmony, pa_sol = self.assess_sol(pa_sol,
+                #                                             har_mem)
+
+        if self.random_state.rand() <= PAR_itr:
+            if pa_sol['class_params_spec'] is not None:
+                logger.debug("pitch adjustment adding class param variables")
+                pa_sol = self.add_new_class_paramfeature(pa_sol)
+                # improved_harmony, pa_sol = self.assess_sol(pa_sol,
+                                                            # har_mem)
+        if self.random_state.rand() <= PAR_itr:
+            if pa_sol['member_params_spec'] is not None:
+                logger.debug("pitch adjustment adding member param variables")
+                pa_sol = self.add_new_member_paramfeature(pa_sol)
+                # improved_harmony, pa_sol = self.assess_sol(pa_sol,
+                                                            # har_mem)
+        if self.random_state.rand() <= PAR_itr:
+            if self.asvarnames or sol['asvars']:
+                logger.debug("pitch adjustment by removing as variables")
+                pa_sol = self.remove_asfeature(sol)
+                # improved_harmony, pa_sol = self.assess_sol(pa_sol,
+                                                            # har_mem)
+
+        if self.random_state.rand() <= PAR_itr:
+            if self.isvarnames or sol['isvars']:
+                logger.debug("pitch adjustment by removing is variables")
+                pa_sol = self.remove_isfeature(pa_sol)
+                # improved_harmony, pa_sol = self.assess_sol(pa_sol,
+                                                            # har_mem)
+
         if self.random_state.rand() <= PAR_itr:
-            if self.random_state.randint(2):
-                logger.debug("pitch adjustment adding as variables")
-                pa_sol = self.add_new_asfeature(sol)
-                improved_harmony, current_sol = self.assess_sol(pa_sol,
-                                                                har_mem)
-
-                if self.isvarnames:
-                    logger.debug("pitch adjustment adding is variables")
-                    pa_sol = self.add_new_isfeature(pa_sol)
-                    improved_harmony, current_sol = self.assess_sol(pa_sol,
-                                                                    har_mem)
-
-                if self.ps_bctrans is None or self.ps_bctrans:
-                    logger.debug("pitch adjustment adding bc variables")
-                    pa_sol = self.add_new_bcfeature(pa_sol, PAR_itr)
-                    improved_harmony, current_sol = self.assess_sol(pa_sol,
-                                                                    har_mem)
-
-                if self.ps_cor is None or self.ps_cor:
-                    logger.debug("pitch adjustment adding cor variables")
-                    pa_sol = self.add_new_corfeature(pa_sol)
-                    improved_harmony, current_sol = self.assess_sol(pa_sol,
-                                                                    har_mem)
-
-                if pa_sol['class_params_spec'] is not None:
-                    logger.debug("pitch adjustment adding class param variables")
-                    pa_sol = self.add_new_class_paramfeature(pa_sol)
-                    improved_harmony, current_sol = self.assess_sol(pa_sol,
-                                                                    har_mem)
-
-                if pa_sol['member_params_spec'] is not None:
-                    logger.debug("pitch adjustment adding member param variables")
-                    pa_sol = self.add_new_member_paramfeature(pa_sol)
-                    improved_harmony, current_sol = self.assess_sol(pa_sol,
-                                                                    har_mem)
-
-            else:
-                if self.asvarnames or sol['asvars']:
-                    logger.debug("pitch adjustment by removing as variables")
-                    pa_sol = self.remove_asfeature(sol)
-                    improved_harmony, current_sol = self.assess_sol(pa_sol,
-                                                                har_mem)
-
-                if self.isvarnames or sol['isvars']:
-                    logger.debug("pitch adjustment by removing is variables")
-                    pa_sol = self.remove_isfeature(pa_sol)
-                    improved_harmony, current_sol = self.assess_sol(pa_sol,
-                                                                    har_mem)
-
-                if self.ps_bctrans is None or self.ps_bctrans:
-                    logger.debug("pitch adjustment by removing bc variables")
-                    pa_sol = self.remove_bcfeature(pa_sol)
-                    improved_harmony, current_sol = self.assess_sol(pa_sol,
-                                                                    har_mem)
-
-                if self.ps_cor is None or self.ps_cor:
-                    logger.debug("pitch adjustment by removing cor variables")
-                    pa_sol = self.remove_corfeature(pa_sol)
-                    improved_harmony, current_sol = self.assess_sol(pa_sol,
-                                                                    har_mem)
-
-                if pa_sol['class_params_spec'] is not None:  # check if has class_params_spec
-                    logger.debug("pitch adjustment by removing class param variables")
-                    pa_sol = self.remove_class_paramfeature(pa_sol)
-                    improved_harmony, current_sol = self.assess_sol(pa_sol,
-                                                                    har_mem)
-
-                if pa_sol['member_params_spec'] is not None:  # check if has member_params_spec
-                    logger.debug("pitch adjustment by removing member param variables")
-                    pa_sol = self.remove_member_paramfeature(pa_sol)
-                    improved_harmony, current_sol = self.assess_sol(pa_sol,
-                                                                    har_mem)
+            if self.ps_bctrans is None or self.ps_bctrans:
+                logger.debug("pitch adjustment by removing bc variables")
+                pa_sol = self.remove_bcfeature(pa_sol)
+                # improved_harmony, pa_sol = self.assess_sol(pa_sol,
+                                                            # har_mem)
+
+        if self.random_state.rand() <= PAR_itr:
+            if self.ps_cor is None or self.ps_cor:
+                logger.debug("pitch adjustment by removing cor variables")
+                pa_sol = self.remove_corfeature(pa_sol)
+                # improved_harmony, pa_sol = self.assess_sol(pa_sol,
+                                                            # har_mem)
+
+        if self.random_state.rand() <= PAR_itr:
+            if pa_sol['class_params_spec'] is not None:  # check if has class_params_spec
+                logger.debug("pitch adjustment by removing class param variables")
+                pa_sol = self.remove_class_paramfeature(pa_sol)
+                # improved_harmony, pa_sol = self.assess_sol(pa_sol,
+                                                            # har_mem)
+
+        if self.random_state.rand() <= PAR_itr:
+            if pa_sol['member_params_spec'] is not None:  # check if has member_params_spec
+                logger.debug("pitch adjustment by removing member param variables")
+                pa_sol = self.remove_member_paramfeature(pa_sol)
+                # improved_harmony, pa_sol = self.assess_sol(pa_sol,
+                                                            # har_mem)
             # else:
             #     logger.debug("pitch adjustment by adding asfeature")
             #     pa_sol = self.add_new_asfeature(sol)
             #     improved_harmony, current_sol = self.assess_sol(pa_sol,
                                                                 # har_mem)
-        else:
-            logger.debug("no pitch adjustment")
-            improved_harmony, current_sol = self.assess_sol(sol, har_mem)
-        return (improved_harmony, current_sol)
+        # else:
+        #     logger.debug("no pitch adjustment")
+        #     improved_harmony, current_sol = self.assess_sol(sol, har_mem)
+        improved_harmony, pa_sol = self.assess_sol(pa_sol, har_mem)
+        return (improved_harmony, pa_sol)
 
     def best_features(self, har_mem):
         """
         Generates lists of best features in harmony memory
         Inputs:
         Harmony memory
         """
@@ -2450,21 +2481,14 @@
                             cor_vars=best_corvars, asc_ind=asc_ind,
                             class_params_spec=best_class_params_spec,
                             member_params_spec=best_member_params_spec)
         improved_harmony, current_sol = self.assess_sol(solution,
                                                         improved_harmony)
         logger.debug("sol after local search step 10: {}".format(str(improved_harmony[0])))
 
-
-
-
-
-
-
-
         # Sort unique harmony memory from min.BIC to max. BIC
         # final_harmony_sorted = sorted(improved_harmony, key = lambda x: x[0])
         final_harmony_sorted = improved_harmony
         return (final_harmony_sorted, current_sol)
 
     # Function to conduct harmony memory consideraion, pitch adjustment and local search
     def improvise_harmony(self, HCR_max, HCR_min, PR_max, PR_min, har_mem,
@@ -2477,15 +2501,15 @@
         best_val_points = []
 
         while itr < max_itr:
             # TODO: Progress bar
             itr += 1
             logger.info("Improvising harmony at iteration {}".format(itr))
             # Estimate dynamic HMCR and PCR values for each iteration
-            HMCR_itr = (HCR_min + ((HCR_max-HCR_min)/max_itr)*itr) * max(0, np.sign(math.sin(itr)))
+            HMCR_itr = (HCR_min + ((HCR_max-HCR_min)/max_itr)*itr) * max(0, np.sign(math.sin(itr)))  # TODO: determine if sin meant to be radians or degrees...
             PAR_itr = (PR_min + ((PR_max-PR_min)/max_itr)*itr) * max(0, np.sign(math.sin(itr)))
 
             # Conduct Harmony Memory Consideration
             print('har_mem: ', len(har_mem))
             hmc_sol = self.harmony_consideration(har_mem, HMCR_itr, itr, HM)
             logger.debug("solution after HMC at iteration {}, is: {}".format(itr, str(hmc_sol)))
             # Conduct Pitch Adjustment
@@ -2691,15 +2715,14 @@
 
         asvars_new = self.remove_redundant_asvars(asvars_new,
                                                   self.trans_asvars,
                                                   self.asvarnames)
         # self.generate_sol()
 
         Init_HM = self.initialize_memory(HMS)
-        Init_HM = [init_sol for _, init_sol in enumerate(Init_HM) if np.abs(init_sol['bic']) < 1000000]
         for sol in Init_HM:
             sol.add_is_init()
 
         # Remove duplicate solutions if present
         unique = set()
         unique_HM = [unique.add(x['bic']) or x for x in Init_HM if x['bic'] not in unique]
```

### Comparing `searchlogit-0.2.98/searchlogit.egg-info/PKG-INFO` & `searchlogit-0.2.99/searchlogit.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: searchlogit
-Version: 0.2.98
+Version: 0.2.99
 Summary: Extensions for a Python package for                               GPU-accelerated estimation of mixed logit models.
 Home-page: https://github.com/RyanJafefKelly/searchlogit
 Author: Ryan Kelly
 Author-email: ryan@kiiii.com
 License: MIT
 Requires-Python: >=3.5
 Description-Content-Type: text/x-rst
```

### Comparing `searchlogit-0.2.98/setup.py` & `searchlogit-0.2.99/setup.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 import codecs
 
 with codecs.open("README.rst", encoding='utf8') as fh:
     long_description = fh.read()
 
 setuptools.setup(name='searchlogit',
-                 version='0.2.98',
+                 version='0.2.99',
                  description='Extensions for a Python package for \
                               GPU-accelerated estimation of mixed logit models.',
                  long_description=long_description,
                  long_description_content_type="text/x-rst",
                  url='https://github.com/RyanJafefKelly/searchlogit',
                  author='Ryan Kelly',
                  author_email='ryan@kiiii.com',
```

