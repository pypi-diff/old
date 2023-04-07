# Comparing `tmp/atflagger-0.4.5.tar.gz` & `tmp/atflagger-0.4.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "atflagger-0.4.5.tar", max compression
+gzip compressed data, was "atflagger-0.4.6.tar", max compression
```

## Comparing `atflagger-0.4.5.tar` & `atflagger-0.4.6.tar`

### file list

```diff
@@ -1,6 +1,6 @@
--rw-r--r--   0        0        0     1069 2021-12-02 09:25:14.139100 atflagger-0.4.5/LICENSE
--rw-r--r--   0        0        0     1862 2023-03-08 01:18:18.148770 atflagger-0.4.5/README.md
--rw-r--r--   0        0        0    13867 2023-03-09 00:45:19.031168 atflagger-0.4.5/atflagger.py
--rw-r--r--   0        0        0      550 2023-03-09 00:46:32.231595 atflagger-0.4.5/pyproject.toml
--rw-r--r--   0        0        0     2663 1970-01-01 00:00:00.000000 atflagger-0.4.5/setup.py
--rw-r--r--   0        0        0     2605 1970-01-01 00:00:00.000000 atflagger-0.4.5/PKG-INFO
+-rw-r--r--   0        0        0     1069 2021-12-02 09:25:14.139100 atflagger-0.4.6/LICENSE
+-rw-r--r--   0        0        0     1862 2023-03-08 01:18:18.148770 atflagger-0.4.6/README.md
+-rw-r--r--   0        0        0    13640 2023-04-07 10:25:34.297979 atflagger-0.4.6/atflagger.py
+-rw-r--r--   0        0        0      550 2023-04-07 10:25:34.298332 atflagger-0.4.6/pyproject.toml
+-rw-r--r--   0        0        0     2663 1970-01-01 00:00:00.000000 atflagger-0.4.6/setup.py
+-rw-r--r--   0        0        0     2605 1970-01-01 00:00:00.000000 atflagger-0.4.6/PKG-INFO
```

### Comparing `atflagger-0.4.5/LICENSE` & `atflagger-0.4.6/LICENSE`

 * *Files identical despite different names*

### Comparing `atflagger-0.4.5/README.md` & `atflagger-0.4.6/README.md`

 * *Files identical despite different names*

### Comparing `atflagger-0.4.5/atflagger.py` & `atflagger-0.4.6/atflagger.py`

 * *Files 6% similar despite different names*

```diff
@@ -259,69 +259,57 @@
 def main(
     filenames,
     inplace=False,
     beam_label="beam_0",
     sigma=3,
     n_windows=100,
     use_weights=False,
-    report=None,
-    cores=None,
-    threads_per_worker=None,
 ):
     args = locals()
     _ = args.pop("filenames")
     if inplace:
         logger.warning("Running in-place - this will overwrite the previous flag data!")
-    # Initialise dask
-    with LocalCluster(
-        n_workers=cores, threads_per_worker=threads_per_worker
-    ) as cluster, Client(cluster) as client, performance_report(
-        filename=report
-    ) if report else nullcontext():
-        logger.info(f"Dask running at {client.dashboard_link}")
-        if report:
-            logger.info(f"Writting report to {report}")
 
-        todos = {}
-        for filename in filenames:
-            logger.info(f"Processing file {filename}")
-            # Copy hdf5 file
-            exts = ("hdf", "hdf5", "sdhdf", "h5")
-            if not any(filename.endswith(f".{ext}") for ext in exts):
-                raise ValueError(
-                    f"I don't recognose the file extension of '{filename}' (must be one of {exts})"
-                )
-            for ext in exts:
-                if filename.endswith(f".{ext}"):
-                    break
-
-            new_filename = copy_file(filename, ext=ext) if not inplace else filename
-
-            sb_avail = get_subbands(new_filename, beam_label=beam_label)
-
-            todos[new_filename] = sb_avail
-
-        # Compute to concrete values
-        todos = compute(todos)[0]  # First elemment of single-element tuple
-
-        hists = []
-        for new_filename in todos.keys():
-            # Iterate through subbands inside flag function
-            flagged = flag(
-                new_filename,
-                todos[new_filename],
-                beam_label=beam_label,
-                sigma=sigma,
-                n_windows=n_windows,
-                use_weights=use_weights,
+    todos = {}
+    for filename in filenames:
+        logger.info(f"Processing file {filename}")
+        # Copy hdf5 file
+        exts = ("hdf", "hdf5", "sdhdf", "h5")
+        if not any(filename.endswith(f".{ext}") for ext in exts):
+            raise ValueError(
+                f"I don't recognose the file extension of '{filename}' (must be one of {exts})"
             )
-            hist = update_history(new_filename, args, flagged)
-            hists.append(hist)
+        for ext in exts:
+            if filename.endswith(f".{ext}"):
+                break
+
+        new_filename = copy_file(filename, ext=ext) if not inplace else filename
+
+        sb_avail = get_subbands(new_filename, beam_label=beam_label)
+
+        todos[new_filename] = sb_avail
+
+    # Compute to concrete values
+    todos = compute(todos)[0]  # First elemment of single-element tuple
+
+    hists = []
+    for new_filename in todos.keys():
+        # Iterate through subbands inside flag function
+        flagged = flag(
+            new_filename,
+            todos[new_filename],
+            beam_label=beam_label,
+            sigma=sigma,
+            n_windows=n_windows,
+            use_weights=use_weights,
+        )
+        hist = update_history(new_filename, args, flagged)
+        hists.append(hist)
 
-        _ = compute(hists)
+    _ = compute(hists)
 
     logger.info("Done!")
 
 
 def cli():
     """Command-line interface"""
     import argparse
@@ -370,22 +358,31 @@
         "--threads-per-worker",
         type=int,
         default=None,
         help="Number of threads per worker (default: Dask automatic configuration)",
     )
 
     args = parser.parse_args()
-    main(
-        filenames=args.filenames,
-        inplace=args.inplace,
-        beam_label=args.beam,
-        sigma=args.sigma,
-        n_windows=args.n_windows,
-        use_weights=args.use_weights,
-        report=args.report,
-        cores=args.cores,
-        threads_per_worker=args.threads_per_worker,
-    )
+
+    # Initialise dask
+    with LocalCluster(
+        n_workers=args.cores, threads_per_worker=args.threads_per_worker
+    ) as cluster, Client(cluster) as client, performance_report(
+        filename=args.report
+    ) if args.report else nullcontext():
+
+        logger.info(f"Dask running at {client.dashboard_link}")
+        if args.report:
+            logger.info(f"Writting report to {args.report}")
+
+        main(
+            filenames=args.filenames,
+            inplace=args.inplace,
+            beam_label=args.beam,
+            sigma=args.sigma,
+            n_windows=args.n_windows,
+            use_weights=args.use_weights,
+        )
 
 
 if __name__ == "__main__":
     cli()
```

### Comparing `atflagger-0.4.5/pyproject.toml` & `atflagger-0.4.6/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "atflagger"
-version = "0.4.5"
+version = "0.4.6"
 description = "Simple method for flagging UWL data."
 authors = ["Alec Thomson"]
 license = "MIT"
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.8"
```

### Comparing `atflagger-0.4.5/setup.py` & `atflagger-0.4.6/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -15,15 +15,15 @@
  'xarray']
 
 entry_points = \
 {'console_scripts': ['atflagger = atflagger:cli']}
 
 setup_kwargs = {
     'name': 'atflagger',
-    'version': '0.4.5',
+    'version': '0.4.6',
     'description': 'Simple method for flagging UWL data.',
     'long_description': "# atflagger\n\nA simple flagger for continuum UWL data. Flag persistent RFI first, then run this auto-flagger.\n\n## Installation\n\nInstalling requires `pip` and `python3` (3.8 and up).\n\nStable version:\n```\npip install atflagger\n```\n\nLatest version:\n```\npip install git+https://github.com/AlecThomson/atflagger\n```\n\n## Usage\n```\n❯ atflagger -h\nusage: atflagger [-h] [-i] [-b BEAM] [-s SIGMA] [-n N_WINDOWS] [-w] [-r REPORT] [-c CORES] [-t THREADS_PER_WORKER] filenames [filenames ...]\n\natflagger - Automatic flagging of UWL data. This flagger divides each subband into a number of windows, and then uses sigma clipping to remove outliers. The number of windows is set by the 'n-windows' argument, and the number of sigma is set by the 'sigma' argument. Parallelism is handled by dask.distributed. The 'cores' argument sets the number of\nDask workers, and 'threads-per-worker' sets the number of threads. See https://docs.dask.org/en/stable/deploying-python.html#reference for more information.\n\npositional arguments:\n  filenames             Input SDHDF file(s)\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -i, --inplace         Update flags in-place (default: create new file)\n  -b BEAM, --beam BEAM  Beam label\n  -s SIGMA, --sigma SIGMA\n                        Sigma clipping threshold\n  -n N_WINDOWS, --n-windows N_WINDOWS\n                        Number of windows to use in box filter\n  -w, --use-weights     Use weights table instead of flag table\n  -r REPORT, --report REPORT\n                        Optionally save the Dask (html) report to a file\n  -c CORES, --cores CORES\n                        Number of workers to use (default: Dask automatic configuration)\n  -t THREADS_PER_WORKER, --threads-per-worker THREADS_PER_WORKER\n                        Number of threads per worker (default: Dask automatic configuration)\n```\n",
     'author': 'Alec Thomson',
     'author_email': 'None',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `atflagger-0.4.5/PKG-INFO` & `atflagger-0.4.6/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: atflagger
-Version: 0.4.5
+Version: 0.4.6
 Summary: Simple method for flagging UWL data.
 License: MIT
 Author: Alec Thomson
 Requires-Python: >=3.8,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
```

