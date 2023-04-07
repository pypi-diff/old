# Comparing `tmp/daemonflux-0.5.1.tar.gz` & `tmp/daemonflux-0.6.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "daemonflux-0.5.1.tar", last modified: Tue Feb 28 10:14:21 2023, max compression
+gzip compressed data, was "daemonflux-0.6.0.tar", last modified: Fri Apr  7 04:18:30 2023, max compression
```

## Comparing `daemonflux-0.5.1.tar` & `daemonflux-0.6.0.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 10:14:21.593194 daemonflux-0.5.1/
--rw-r--r--   0 runner    (1001) docker     (123)     1504 2023-02-28 10:13:54.000000 daemonflux-0.5.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     2380 2023-02-28 10:14:21.593194 daemonflux-0.5.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1338 2023-02-28 10:13:54.000000 daemonflux-0.5.1/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       86 2023-02-28 10:13:54.000000 daemonflux-0.5.1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     1249 2023-02-28 10:14:21.593194 daemonflux-0.5.1/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 10:14:21.589193 daemonflux-0.5.1/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 10:14:21.593194 daemonflux-0.5.1/src/daemonflux/
--rw-r--r--   0 runner    (1001) docker     (123)      143 2023-02-28 10:13:54.000000 daemonflux-0.5.1/src/daemonflux/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    21062 2023-02-28 10:13:54.000000 daemonflux-0.5.1/src/daemonflux/flux.py
--rw-r--r--   0 runner    (1001) docker     (123)     4648 2023-02-28 10:13:54.000000 daemonflux-0.5.1/src/daemonflux/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 10:14:21.593194 daemonflux-0.5.1/src/daemonflux.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2380 2023-02-28 10:14:21.000000 daemonflux-0.5.1/src/daemonflux.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      330 2023-02-28 10:14:21.000000 daemonflux-0.5.1/src/daemonflux.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-28 10:14:21.000000 daemonflux-0.5.1/src/daemonflux.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       55 2023-02-28 10:14:21.000000 daemonflux-0.5.1/src/daemonflux.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-02-28 10:14:21.000000 daemonflux-0.5.1/src/daemonflux.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 10:14:21.593194 daemonflux-0.5.1/tests/
--rw-r--r--   0 runner    (1001) docker     (123)    12648 2023-02-28 10:13:54.000000 daemonflux-0.5.1/tests/test_daemonflux.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:18:30.103651 daemonflux-0.6.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1504 2023-04-07 04:18:03.000000 daemonflux-0.6.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     4238 2023-04-07 04:18:30.103651 daemonflux-0.6.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3233 2023-04-07 04:18:03.000000 daemonflux-0.6.0/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-07 04:18:03.000000 daemonflux-0.6.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     1223 2023-04-07 04:18:30.103651 daemonflux-0.6.0/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:18:30.099651 daemonflux-0.6.0/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:18:30.099651 daemonflux-0.6.0/src/daemonflux/
+-rw-r--r--   0 runner    (1001) docker     (123)      143 2023-04-07 04:18:03.000000 daemonflux-0.6.0/src/daemonflux/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21621 2023-04-07 04:18:03.000000 daemonflux-0.6.0/src/daemonflux/flux.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4648 2023-04-07 04:18:03.000000 daemonflux-0.6.0/src/daemonflux/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:18:30.103651 daemonflux-0.6.0/src/daemonflux.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4238 2023-04-07 04:18:30.000000 daemonflux-0.6.0/src/daemonflux.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      330 2023-04-07 04:18:30.000000 daemonflux-0.6.0/src/daemonflux.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 04:18:30.000000 daemonflux-0.6.0/src/daemonflux.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       55 2023-04-07 04:18:30.000000 daemonflux-0.6.0/src/daemonflux.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-04-07 04:18:30.000000 daemonflux-0.6.0/src/daemonflux.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:18:30.103651 daemonflux-0.6.0/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)    13462 2023-04-07 04:18:03.000000 daemonflux-0.6.0/tests/test_daemonflux.py
```

### Comparing `daemonflux-0.5.1/LICENSE` & `daemonflux-0.6.0/LICENSE`

 * *Files identical despite different names*

### Comparing `daemonflux-0.5.1/setup.cfg` & `daemonflux-0.6.0/setup.cfg`

 * *Files 7% similar despite different names*

```diff
@@ -1,25 +1,24 @@
 [metadata]
 name = daemonflux
-version = 0.5.1
+version = 0.6.0
 author = Anatoli Fedynitch
 maintainer_email = afedynitch@gmail.com
-description = Tabulated representation of a muon-calibrated neutrino flux model
+description = Tabulated representation of a muon-calibrated muon and neutrino flux model
 license = BSD 3-Clause License
 long_description = file: README.md
 long_description_content_type = text/markdown
-url = https://github.com/mceq-project/daemon
+url = https://github.com/mceq-project/daemonflux
 download_url = https://pypi.python.org/pypi/daemonflux
 classifiers = 
 	Development Status :: 4 - Beta
 	Topic :: Scientific/Engineering :: Physics
 	Intended Audience :: Science/Research
 	Programming Language :: Python
 	Programming Language :: Python :: 3
-	Programming Language :: Python :: 3.7
 	Programming Language :: Python :: 3.8
 	Programming Language :: Python :: 3.9
 	Programming Language :: Python :: 3.10
 	License :: OSI Approved :: BSD License
 	License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)
 
 [options]
```

### Comparing `daemonflux-0.5.1/src/daemonflux/flux.py` & `daemonflux-0.6.0/src/daemonflux/flux.py`

 * *Files 4% similar despite different names*

```diff
@@ -85,55 +85,67 @@
         """
         for p, pv in zip(self.known_parameters, self.values):
             yield p, pv
 
 
 class Flux:
     _default_url = (
-        "https://github.com/mceq-project/daemonflux/releases/download/v0.4.1/"
+        "https://github.com/mceq-project/daemonflux/releases/download/prerelease/"
     )
-    _default_spl_file = "daemonsplines_{0}_202303_0.pkl"
-    _default_cal_file = "daemonsplines_calibration_202303_0.pkl"
+    _default_spl_file = "daemonsplines_{location}_{rev}.pkl"
+    _default_cal_file = "daemonsplines_calibration_{rev}.pkl"
+    _revision = "202303_1"
 
     def __init__(
         self,
         location="generic",
         spl_file=None,
         cal_file=None,
         use_calibration=True,
         exclude=[],
+        keep_old_revisions=False,
         debug=1,
     ) -> None:
         self.exclude = exclude
         self._debug = debug
         spl_file = (
             spl_file
             if spl_file
             else _cached_data_dir(
-                self._default_url + self._default_spl_file.format(location)
+                self._default_url
+                + self._default_spl_file.format(location=location, rev=self._revision)
             )
         )
         if not use_calibration:
             cal_file = None
         elif use_calibration and cal_file is None:
-            cal_file = _cached_data_dir(self._default_url + self._default_cal_file)
+            cal_file = _cached_data_dir(
+                self._default_url + self._default_cal_file.format(rev=self._revision)
+            )
 
         self._load_splines(spl_file, cal_file)
+        if not keep_old_revisions:
+            self._cleanup_old_revisions()
+
+    def _cleanup_old_revisions(self):
+        import pathlib
+
+        for f in pathlib.Path(base_path / "data").glob("daemonsplines*"):
+            if self._revision not in str(f):
+                print("Removing old version", f)
+                f.unlink()
 
     def _load_splines(self, spl_file, cal_file):
         from .utils import rearrange_covariance
         from copy import deepcopy
 
         assert pathlib.Path(spl_file).is_file(), f"Spline file {spl_file} not found."
-        (
-            known_pars,
-            self._fl_spl,
-            self._jac_spl,
-            cov,
-        ) = pickle.load(open(spl_file, "rb"))
+        (known_pars, self._fl_spl, self._jac_spl, cov,) = pickle.load(
+            open(spl_file, "rb")
+        )[:4]
 
         known_parameters = []
         for k in known_pars:
             if k in self.exclude:
                 continue
             if k.startswith("total_"):
                 continue
@@ -213,17 +225,22 @@
                 self._jac_spl[exp],
                 deepcopy(params),
                 self._debug,
             )
             setattr(self, exp, subflux)
             self.supported_fluxes.append(exp)
 
-    def print_experiments(self):
+    def __repr__(self):
+        s = ""
         for exp in self._fl_spl:
-            print("{0}: [{1}]".format(exp, ", ".join(self._fl_spl[exp].keys())))
+            s += "{0}: [{1}]\n".format(exp, ", ".join(self._fl_spl[exp].keys()))
+        return s
+
+    def print_experiments(self):
+        print(self.__repr__())
 
     @property
     def zenith_angles(self, exp=""):
         if not exp and len(self.supported_fluxes) > 1:
             raise Exception("'exp' argument needs to be one of", self.supported_fluxes)
         if len(self.supported_fluxes) == 1:
             return self.__getattribute__(self.supported_fluxes[0]).zenith_angles
```

### Comparing `daemonflux-0.5.1/src/daemonflux/utils.py` & `daemonflux-0.6.0/src/daemonflux/utils.py`

 * *Files identical despite different names*

