# Comparing `tmp/oda_integral_wrapper-1.3.8.tar.gz` & `tmp/oda_integral_wrapper-1.3.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/oda_integral_wrapper-1.3.8.tar", last modified: Sun Apr  4 08:07:34 2021, max compression
+gzip compressed data, was "dist/oda_integral_wrapper-1.3.9.tar", last modified: Tue Apr 27 19:58:22 2021, max compression
```

## Comparing `oda_integral_wrapper-1.3.8.tar` & `oda_integral_wrapper-1.3.9.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxrwxr-x   0 ferrigno  (1001) ferrigno  (1001)        0 2021-04-04 08:07:34.600181 oda_integral_wrapper-1.3.8/
--rw-rw-r--   0 ferrigno  (1001) ferrigno  (1001)      367 2021-04-04 08:07:34.600181 oda_integral_wrapper-1.3.8/PKG-INFO
--rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)     1890 2021-03-04 23:47:29.000000 oda_integral_wrapper-1.3.8/README.md
-drwxrwxr-x   0 ferrigno  (1001) ferrigno  (1001)        0 2021-04-04 08:07:34.596181 oda_integral_wrapper-1.3.8/oda_integral_wrapper/
--rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)      751 2020-06-11 08:22:33.000000 oda_integral_wrapper-1.3.8/oda_integral_wrapper/__init__.py
--rw-rw-r--   0 ferrigno  (1001) ferrigno  (1001)     5988 2020-06-11 14:53:53.000000 oda_integral_wrapper-1.3.8/oda_integral_wrapper/fitimage.py
--rw-rw-r--   0 ferrigno  (1001) ferrigno  (1001)    47766 2021-04-04 07:25:12.000000 oda_integral_wrapper-1.3.8/oda_integral_wrapper/wrapper.py
-drwxrwxr-x   0 ferrigno  (1001) ferrigno  (1001)        0 2021-04-04 08:07:34.600181 oda_integral_wrapper-1.3.8/oda_integral_wrapper.egg-info/
--rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)      367 2021-04-04 08:07:34.000000 oda_integral_wrapper-1.3.8/oda_integral_wrapper.egg-info/PKG-INFO
--rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)      345 2021-04-04 08:07:34.000000 oda_integral_wrapper-1.3.8/oda_integral_wrapper.egg-info/SOURCES.txt
--rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)        1 2021-04-04 08:07:34.000000 oda_integral_wrapper-1.3.8/oda_integral_wrapper.egg-info/dependency_links.txt
--rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)       85 2021-04-04 08:07:34.000000 oda_integral_wrapper-1.3.8/oda_integral_wrapper.egg-info/requires.txt
--rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)       21 2021-04-04 08:07:34.000000 oda_integral_wrapper-1.3.8/oda_integral_wrapper.egg-info/top_level.txt
--rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)       79 2021-04-04 08:07:34.600181 oda_integral_wrapper-1.3.8/setup.cfg
--rw-rw-r--   0 ferrigno  (1001) ferrigno  (1001)     1288 2021-04-04 08:06:12.000000 oda_integral_wrapper-1.3.8/setup.py
+drwxrwxr-x   0 ferrigno  (1001) ferrigno  (1001)        0 2021-04-27 19:58:22.312028 oda_integral_wrapper-1.3.9/
+-rw-rw-r--   0 ferrigno  (1001) ferrigno  (1001)      367 2021-04-27 19:58:22.312028 oda_integral_wrapper-1.3.9/PKG-INFO
+-rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)     1890 2021-03-04 23:47:29.000000 oda_integral_wrapper-1.3.9/README.md
+drwxrwxr-x   0 ferrigno  (1001) ferrigno  (1001)        0 2021-04-27 19:58:22.312028 oda_integral_wrapper-1.3.9/oda_integral_wrapper/
+-rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)      751 2020-06-11 08:22:33.000000 oda_integral_wrapper-1.3.9/oda_integral_wrapper/__init__.py
+-rw-rw-r--   0 ferrigno  (1001) ferrigno  (1001)     5988 2020-06-11 14:53:53.000000 oda_integral_wrapper-1.3.9/oda_integral_wrapper/fitimage.py
+-rw-rw-r--   0 ferrigno  (1001) ferrigno  (1001)    49501 2021-04-27 19:56:18.000000 oda_integral_wrapper-1.3.9/oda_integral_wrapper/wrapper.py
+drwxrwxr-x   0 ferrigno  (1001) ferrigno  (1001)        0 2021-04-27 19:58:22.312028 oda_integral_wrapper-1.3.9/oda_integral_wrapper.egg-info/
+-rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)      367 2021-04-27 19:58:22.000000 oda_integral_wrapper-1.3.9/oda_integral_wrapper.egg-info/PKG-INFO
+-rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)      345 2021-04-27 19:58:22.000000 oda_integral_wrapper-1.3.9/oda_integral_wrapper.egg-info/SOURCES.txt
+-rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)        1 2021-04-27 19:58:22.000000 oda_integral_wrapper-1.3.9/oda_integral_wrapper.egg-info/dependency_links.txt
+-rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)       85 2021-04-27 19:58:22.000000 oda_integral_wrapper-1.3.9/oda_integral_wrapper.egg-info/requires.txt
+-rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)       21 2021-04-27 19:58:22.000000 oda_integral_wrapper-1.3.9/oda_integral_wrapper.egg-info/top_level.txt
+-rw-r--r--   0 ferrigno  (1001) ferrigno  (1001)       79 2021-04-27 19:58:22.312028 oda_integral_wrapper-1.3.9/setup.cfg
+-rw-rw-r--   0 ferrigno  (1001) ferrigno  (1001)     1288 2021-04-27 19:56:18.000000 oda_integral_wrapper-1.3.9/setup.py
```

### Comparing `oda_integral_wrapper-1.3.8/README.md` & `oda_integral_wrapper-1.3.9/README.md`

 * *Files identical despite different names*

### Comparing `oda_integral_wrapper-1.3.8/oda_integral_wrapper/__init__.py` & `oda_integral_wrapper-1.3.9/oda_integral_wrapper/__init__.py`

 * *Files identical despite different names*

### Comparing `oda_integral_wrapper-1.3.8/oda_integral_wrapper/fitimage.py` & `oda_integral_wrapper-1.3.9/oda_integral_wrapper/fitimage.py`

 * *Files identical despite different names*

### Comparing `oda_integral_wrapper-1.3.8/oda_integral_wrapper/wrapper.py` & `oda_integral_wrapper-1.3.9/oda_integral_wrapper/wrapper.py`

 * *Files 6% similar despite different names*

```diff
@@ -56,23 +56,41 @@
                 raise ConnectionError
 
     def long_scw_list_call(self, in_total_scw_list, s_max=50, wait=True, sleep_time=10, **arguments):
         import time
         total_scw_list = sorted(in_total_scw_list)
 
         self.product = arguments['product']
+        local_arguments = arguments.copy()
 
         if len(total_scw_list) > s_max:
             ind_max = int(len(total_scw_list) / s_max)
             scw_lists = [total_scw_list[i * s_max:(i + 1) * s_max] for i in range(ind_max)]
             if ind_max * s_max < len(total_scw_list):
                 scw_lists.append(total_scw_list[ind_max * s_max:])
         else:
             scw_lists = [total_scw_list]
 
+        def get_revs(loc_scw_list):
+            return np.array(sorted(list(set([int(a[0:4]) for a in loc_scw_list]))))
+
+        ## I split a list that contains revolutions before and after 1626 (start of validity of OSA11.X
+        new_scw_lists = []
+        for ss in scw_lists:
+            revs = get_revs(ss)
+            if revs.min() < 1626 and revs.max() >= 1626:
+                s1 = [s for s in ss if int(s[0:4]) < 1626]
+                s2 = [s for s in ss if int(s[0:4]) >= 1626]
+                new_scw_lists.append(s1)
+                new_scw_lists.append(s2)
+            else:
+                new_scw_lists.append(ss)
+        scw_lists = new_scw_lists
+        ##
+
         self.all_data = []
         tot_num = 0
 
         disp_by_call = {}
         data_by_call = {}
         n_poll = 0
         while True:
@@ -94,16 +112,22 @@
 
                 _disp = disp_by_call[ys]
                 #print(type(_disp))
                 data = data_by_call.get(ys, None)
 
                 if data is None or not _disp.is_failed():
                     if not _disp.is_submitted:
+                        revs = get_revs(scw_list)
+                        # Force 0SA10.2 for ISGRI before rev. 1626
+                        if revs.min() < 1626 and 'isgri' in arguments['product']:
+                            local_arguments['osa_version'] = 'OSA10.2'
+                        else:
+                            local_arguments['osa_version'] = arguments['osa_version']
                         scw_list_str = ",".join([s for s in sorted(set(scw_list))])
-                        data = _disp.get_product(scw_list=scw_list_str, **arguments)
+                        data = _disp.get_product(scw_list=scw_list_str, **local_arguments)
                     else:
                         _disp.poll()
 
                     data_by_call[ys] = data
 
                     if not _disp.is_complete:
                         continue
@@ -376,29 +400,43 @@
         x = x[ind]
         y = y[ind]
         dy = dy[ind]
 
         dy = np.sqrt(dy ** 2 + (y * systematic_fraction) ** 2)
         ind = np.logical_and(np.isfinite(y), np.isfinite(dy))
         ind = np.logical_and(ind, dy > 0)
-        return x[ind], y[ind], dy[ind]
+
+        #This could only be valid for ISGRI
+        try:
+            dt_lc =  hdu.data['XAX_E']
+            INTEGRALwrapper.__log.debug('Get time bin directly from light curve')
+        except:
+            timedel = hdu.header['TIMEDEL']
+            timepix = hdu.header['TIMEPIXR']
+            t_lc = hdu.data['TIME'] + (0.5 - timepix) * timedel
+            dt_lc = t_lc.copy() * 0.0 + timedel / 2
+            for i in range(len(t_lc) - 1):
+                dt_lc[i + 1] = min(timedel / 2, t_lc[i + 1] - t_lc[i] - dt_lc[i])
+            INTEGRALwrapper.__log.debug('Computed time bin from TIMEDEL')
+
+        return x[ind], dt_lc[ind], y[ind], dy[ind]
 
 
     @staticmethod
     def plot_lc(combined_lc, source_name, systematic_fraction=0, ng_sig_limit=3, find_excesses=False):
         from scipy import stats
-        x,y,dy = INTEGRALwrapper.get_lc(combined_lc, source_name, systematic_fraction)
+        x,dx,y,dy = INTEGRALwrapper.get_lc(combined_lc, source_name, systematic_fraction)
 
         meany = np.sum(y / dy ** 2) / np.sum(1. / dy ** 2)
         err_mean = np.sum(1 / dy ** 2)
 
         std_dev = np.std(y)
 
         fig = plt.figure()
-        _ = plt.errorbar(x, y, yerr=dy, marker='o', capsize=0, linestyle='', label='Lightcurve')
+        _ = plt.errorbar(x, y, xerr=dx, yerr=dy, marker='o', capsize=0, linestyle='', label='Lightcurve')
         _ = plt.axhline(meany, color='green', linewidth=3)
         _ = plt.xlabel('Time [IJD]')
         _ = plt.ylabel('Rate')
 
         ndof = len(y) - 1
         prob_limit = stats.norm().sf(ng_sig_limit)
         chi2_limit = stats.chi2(ndof).isf(prob_limit)
```

### Comparing `oda_integral_wrapper-1.3.8/setup.py` & `oda_integral_wrapper-1.3.9/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -15,15 +15,15 @@
 
 print ('packs',packs)
 
 include_package_data=True
 
 scripts_list = glob.glob('./bin/*')
 setup(name='oda_integral_wrapper',
-      version="1.3.8",
+      version="1.3.9",
       description='wrapper for INTEGRAL analysis using the API plugin for CDCI online data analysis',
       author='Carlo Ferrigno',
       author_email='carlo.ferrigno@unige.ch',
       url="https://gitlab.astro.unige.ch/oda/api-clients/oda_api_wrapper",
       scripts=scripts_list,
       packages=packs,
       package_data={'oda_integral_wrapper' : ['config_dir/*']},
```

