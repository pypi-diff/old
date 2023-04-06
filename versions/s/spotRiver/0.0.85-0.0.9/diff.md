# Comparing `tmp/spotRiver-0.0.85.tar.gz` & `tmp/spotRiver-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "spotRiver-0.0.85.tar", last modified: Thu Apr  6 13:18:33 2023, max compression
+gzip compressed data, was "spotRiver-0.0.9.tar", last modified: Sun Feb  5 11:57:55 2023, max compression
```

## Comparing `spotRiver-0.0.85.tar` & `spotRiver-0.0.9.tar`

### file list

```diff
@@ -1,45 +1,34 @@
-drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-04-06 13:18:33.255030 spotRiver-0.0.85/
--rw-r--r--   0 bartz      (501) staff       (20)     1520 2023-01-29 11:49:35.000000 spotRiver-0.0.85/LICENSE
--rw-r--r--   0 bartz      (501) staff       (20)      164 2023-03-22 20:43:16.000000 spotRiver-0.0.85/MANIFEST.in
--rw-r--r--   0 bartz      (501) staff       (20)     3383 2023-04-06 13:18:33.254875 spotRiver-0.0.85/PKG-INFO
--rw-r--r--   0 bartz      (501) staff       (20)     2912 2023-01-29 16:41:52.000000 spotRiver-0.0.85/README.md
--rw-r--r--   0 bartz      (501) staff       (20)     1046 2023-04-06 12:47:14.000000 spotRiver-0.0.85/pyproject.toml
--rw-r--r--   0 bartz      (501) staff       (20)       38 2023-04-06 13:18:33.255066 spotRiver-0.0.85/setup.cfg
-drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-04-06 13:18:33.248581 spotRiver-0.0.85/src/
-drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-04-06 13:18:33.249119 spotRiver-0.0.85/src/spotRiver/
-drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-04-06 13:18:33.252688 spotRiver-0.0.85/src/spotRiver/data/
--rw-r--r--   0 bartz      (501) staff       (20)      413 2023-01-29 11:52:00.000000 spotRiver-0.0.85/src/spotRiver/data/__init__.py
--rw-r--r--   0 bartz      (501) staff       (20)     2182 2023-01-17 12:39:58.000000 spotRiver-0.0.85/src/spotRiver/data/airline-passengers.csv
--rw-r--r--   0 bartz      (501) staff       (20)     1023 2023-03-27 20:31:30.000000 spotRiver-0.0.85/src/spotRiver/data/airline_passengers.py
--rw-r--r--   0 bartz      (501) staff       (20)    13646 2023-03-22 20:37:51.000000 spotRiver-0.0.85/src/spotRiver/data/base.py
--rw-r--r--   0 bartz      (501) staff       (20)     1113 2023-03-13 20:26:53.000000 spotRiver-0.0.85/src/spotRiver/data/bike_sharing.py
--rw-r--r--   0 bartz      (501) staff       (20)     1870 2023-03-07 16:50:39.000000 spotRiver-0.0.85/src/spotRiver/data/generic.py
--rw-r--r--   0 bartz      (501) staff       (20)     7751 2023-03-07 16:50:39.000000 spotRiver-0.0.85/src/spotRiver/data/opm.py
--rw-r--r--   0 bartz      (501) staff       (20)    11741 2023-03-29 18:13:06.000000 spotRiver-0.0.85/src/spotRiver/data/river_hyper_dict.json
--rw-r--r--   0 bartz      (501) staff       (20)      329 2023-03-31 21:04:02.000000 spotRiver-0.0.85/src/spotRiver/data/river_hyper_dict.py
-drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-04-06 13:18:33.252961 spotRiver-0.0.85/src/spotRiver/data/synth/
--rw-r--r--   0 bartz      (501) staff       (20)      328 2023-01-18 17:25:51.000000 spotRiver-0.0.85/src/spotRiver/data/synth/__init__.py
--rw-r--r--   0 bartz      (501) staff       (20)     2442 2023-02-20 15:46:37.000000 spotRiver-0.0.85/src/spotRiver/data/synth/sea.py
-drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-04-06 13:18:33.253103 spotRiver-0.0.85/src/spotRiver/drift/
--rw-r--r--   0 bartz      (501) staff       (20)      767 2023-02-20 15:46:37.000000 spotRiver-0.0.85/src/spotRiver/drift/drift_generator.py
-drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-04-06 13:18:33.253554 spotRiver-0.0.85/src/spotRiver/evaluation/
--rw-r--r--   0 bartz      (501) staff       (20)    29393 2023-04-06 12:46:27.000000 spotRiver-0.0.85/src/spotRiver/evaluation/eval_bml.py
--rw-r--r--   0 bartz      (501) staff       (20)     3958 2023-02-26 22:39:12.000000 spotRiver-0.0.85/src/spotRiver/evaluation/eval_nowcast.py
--rw-r--r--   0 bartz      (501) staff       (20)     6752 2023-04-06 12:44:54.000000 spotRiver-0.0.85/src/spotRiver/evaluation/eval_oml.py
-drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-04-06 13:18:33.253692 spotRiver-0.0.85/src/spotRiver/fun/
--rw-r--r--   0 bartz      (501) staff       (20)    27772 2023-04-06 12:48:28.000000 spotRiver-0.0.85/src/spotRiver/fun/hyperriver.py
-drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-04-06 13:18:33.253849 spotRiver-0.0.85/src/spotRiver/plot/
--rw-r--r--   0 bartz      (501) staff       (20)     1340 2023-03-11 14:52:45.000000 spotRiver-0.0.85/src/spotRiver/plot/stats.py
-drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-04-06 13:18:33.253982 spotRiver-0.0.85/src/spotRiver/preprocess/
--rw-r--r--   0 bartz      (501) staff       (20)     2488 2023-03-07 16:50:39.000000 spotRiver-0.0.85/src/spotRiver/preprocess/impute.py
-drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-04-06 13:18:33.254376 spotRiver-0.0.85/src/spotRiver/utils/
--rw-r--r--   0 bartz      (501) staff       (20)     2033 2023-04-04 17:58:20.000000 spotRiver-0.0.85/src/spotRiver/utils/data_conversion.py
--rw-r--r--   0 bartz      (501) staff       (20)      641 2023-02-04 21:33:55.000000 spotRiver-0.0.85/src/spotRiver/utils/features.py
-drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-04-06 13:18:33.250663 spotRiver-0.0.85/src/spotRiver.egg-info/
--rw-r--r--   0 bartz      (501) staff       (20)     3383 2023-04-06 13:18:33.000000 spotRiver-0.0.85/src/spotRiver.egg-info/PKG-INFO
--rw-r--r--   0 bartz      (501) staff       (20)      951 2023-04-06 13:18:33.000000 spotRiver-0.0.85/src/spotRiver.egg-info/SOURCES.txt
--rw-r--r--   0 bartz      (501) staff       (20)        1 2023-04-06 13:18:33.000000 spotRiver-0.0.85/src/spotRiver.egg-info/dependency_links.txt
--rw-r--r--   0 bartz      (501) staff       (20)       20 2023-04-06 13:18:33.000000 spotRiver-0.0.85/src/spotRiver.egg-info/requires.txt
--rw-r--r--   0 bartz      (501) staff       (20)       10 2023-04-06 13:18:33.000000 spotRiver-0.0.85/src/spotRiver.egg-info/top_level.txt
-drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-04-06 13:18:33.254510 spotRiver-0.0.85/test/
--rw-r--r--   0 bartz      (501) staff       (20)      510 2023-02-25 09:55:05.000000 spotRiver-0.0.85/test/test_features.py
+drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-02-05 11:57:55.137121 spotRiver-0.0.9/
+-rw-r--r--   0 bartz      (501) staff       (20)     1520 2023-01-29 11:49:35.000000 spotRiver-0.0.9/LICENSE
+-rw-r--r--   0 bartz      (501) staff       (20)      130 2023-01-29 16:41:52.000000 spotRiver-0.0.9/MANIFEST.in
+-rw-r--r--   0 bartz      (501) staff       (20)     3382 2023-02-05 11:57:55.136954 spotRiver-0.0.9/PKG-INFO
+-rw-r--r--   0 bartz      (501) staff       (20)     2912 2023-01-29 16:41:52.000000 spotRiver-0.0.9/README.md
+-rw-r--r--   0 bartz      (501) staff       (20)     1045 2023-02-05 11:57:26.000000 spotRiver-0.0.9/pyproject.toml
+-rw-r--r--   0 bartz      (501) staff       (20)       38 2023-02-05 11:57:55.137168 spotRiver-0.0.9/setup.cfg
+drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-02-05 11:57:55.130191 spotRiver-0.0.9/src/
+drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-02-05 11:57:55.130555 spotRiver-0.0.9/src/spotRiver/
+drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-02-05 11:57:55.134412 spotRiver-0.0.9/src/spotRiver/data/
+-rw-r--r--   0 bartz      (501) staff       (20)      413 2023-01-29 11:52:00.000000 spotRiver-0.0.9/src/spotRiver/data/__init__.py
+-rw-r--r--   0 bartz      (501) staff       (20)     2182 2023-01-17 12:39:58.000000 spotRiver-0.0.9/src/spotRiver/data/airline-passengers.csv
+-rw-r--r--   0 bartz      (501) staff       (20)     1023 2023-01-17 12:39:58.000000 spotRiver-0.0.9/src/spotRiver/data/airline_passengers.py
+-rw-r--r--   0 bartz      (501) staff       (20)    12012 2023-02-01 17:37:08.000000 spotRiver-0.0.9/src/spotRiver/data/base.py
+-rw-r--r--   0 bartz      (501) staff       (20)     1290 2023-02-05 00:56:40.000000 spotRiver-0.0.9/src/spotRiver/data/generic.py
+-rw-r--r--   0 bartz      (501) staff       (20)     6121 2023-02-04 20:16:42.000000 spotRiver-0.0.9/src/spotRiver/data/opm.py
+drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-02-05 11:57:55.135215 spotRiver-0.0.9/src/spotRiver/data/synth/
+-rw-r--r--   0 bartz      (501) staff       (20)      328 2023-01-18 17:25:51.000000 spotRiver-0.0.9/src/spotRiver/data/synth/__init__.py
+-rw-r--r--   0 bartz      (501) staff       (20)     2445 2023-01-17 12:39:58.000000 spotRiver-0.0.9/src/spotRiver/data/synth/sea.py
+drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-02-05 11:57:55.135734 spotRiver-0.0.9/src/spotRiver/evaluation/
+-rw-r--r--   0 bartz      (501) staff       (20)     3157 2023-02-04 23:14:24.000000 spotRiver-0.0.9/src/spotRiver/evaluation/eval_oml.py
+drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-02-05 11:57:55.135923 spotRiver-0.0.9/src/spotRiver/fun/
+-rw-r--r--   0 bartz      (501) staff       (20)    20018 2023-02-05 10:58:38.000000 spotRiver-0.0.9/src/spotRiver/fun/hyperriver.py
+drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-02-05 11:57:55.136579 spotRiver-0.0.9/src/spotRiver/utils/
+-rw-r--r--   0 bartz      (501) staff       (20)      641 2023-02-04 21:33:55.000000 spotRiver-0.0.9/src/spotRiver/utils/features.py
+-rw-r--r--   0 bartz      (501) staff       (20)      826 2023-02-05 00:41:06.000000 spotRiver-0.0.9/src/spotRiver/utils/selectors.py
+drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-02-05 11:57:55.132545 spotRiver-0.0.9/src/spotRiver.egg-info/
+-rw-r--r--   0 bartz      (501) staff       (20)     3382 2023-02-05 11:57:55.000000 spotRiver-0.0.9/src/spotRiver.egg-info/PKG-INFO
+-rw-r--r--   0 bartz      (501) staff       (20)      650 2023-02-05 11:57:55.000000 spotRiver-0.0.9/src/spotRiver.egg-info/SOURCES.txt
+-rw-r--r--   0 bartz      (501) staff       (20)        1 2023-02-05 11:57:55.000000 spotRiver-0.0.9/src/spotRiver.egg-info/dependency_links.txt
+-rw-r--r--   0 bartz      (501) staff       (20)       20 2023-02-05 11:57:55.000000 spotRiver-0.0.9/src/spotRiver.egg-info/requires.txt
+-rw-r--r--   0 bartz      (501) staff       (20)       10 2023-02-05 11:57:55.000000 spotRiver-0.0.9/src/spotRiver.egg-info/top_level.txt
+drwxr-xr-x   0 bartz      (501) staff       (20)        0 2023-02-05 11:57:55.136741 spotRiver-0.0.9/test/
+-rw-r--r--   0 bartz      (501) staff       (20)      511 2023-01-29 16:42:44.000000 spotRiver-0.0.9/test/test_features.py
```

### Comparing `spotRiver-0.0.85/LICENSE` & `spotRiver-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `spotRiver-0.0.85/PKG-INFO` & `spotRiver-0.0.9/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: spotRiver
-Version: 0.0.85
+Version: 0.0.9
 Summary: spotRiver - Sequential Parameter Optimization Interface to River
 Author-email: "T. Bartz-Beielstein" <tbb@bartzundbartz.de>
 Project-URL: Homepage, https://www.spotseven.de
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.10
```

### Comparing `spotRiver-0.0.85/README.md` & `spotRiver-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `spotRiver-0.0.85/pyproject.toml` & `spotRiver-0.0.9/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -5,15 +5,15 @@
             "numpy",
             "scikit-learn",
             "matplotlib"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "spotRiver"
-version = "0.0.85"
+version = "0.0.9"
 authors = [
   { name="T. Bartz-Beielstein", email="tbb@bartzundbartz.de" }
 ]
 description = "spotRiver - Sequential Parameter Optimization Interface to River"
 readme = "README.md"
 requires-python = ">=3.10"
 classifiers = [
```

### Comparing `spotRiver-0.0.85/src/spotRiver/data/airline-passengers.csv` & `spotRiver-0.0.9/src/spotRiver/data/airline-passengers.csv`

 * *Files identical despite different names*

### Comparing `spotRiver-0.0.85/src/spotRiver/data/airline_passengers.py` & `spotRiver-0.0.9/src/spotRiver/data/airline_passengers.py`

 * *Files identical despite different names*

### Comparing `spotRiver-0.0.85/src/spotRiver/data/base.py` & `spotRiver-0.0.9/src/spotRiver/data/base.py`

 * *Files 4% similar despite different names*

```diff
@@ -44,44 +44,14 @@
     # Ensure data_home is a Path() object pointing to an absolute path
     data_home = Path(data_home).absolute()
     # Create data directory if it does not exists.
     data_home.mkdir(parents=True, exist_ok=True)
     return data_home
 
 
-class Config(abc.ABC):
-    """Base class for all configurations.
-
-    All configurations inherit from this class, be they stored in a file or generated on the fly.
-    """
-
-    def __init__(
-        self,
-    ):
-        pass
-
-    @property
-    def desc(self):
-        """Return the description from the docstring."""
-        desc = re.split(pattern=r"\w+\n\s{4}\-{3,}", string=self.__doc__, maxsplit=0)[0]
-        return inspect.cleandoc(desc)
-
-    @property
-    def _repr_content(self):
-        """The items that are displayed in the __repr__ method.
-
-        This property can be overridden in order to modify the output of the __repr__ method.
-
-        """
-
-        content = {}
-        content["Name"] = self.__class__.__name__
-        return content
-
-
 class Dataset(abc.ABC):
     """Base class for all datasets.
 
     All datasets inherit from this class, be they stored in a file or generated on the fly.
 
     Parameters
     ----------
@@ -157,14 +127,15 @@
         if self.n_classes:
             content["Classes"] = f"{self.n_classes:,}"
         content["Sparse"] = str(self.sparse)
 
         return content
 
     def __repr__(self):
+
         l_len = max(map(len, self._repr_content.keys()))
         r_len = max(map(len, self._repr_content.values()))
 
         out = f"{self.desc}\n\n" + "\n".join(
             k.rjust(l_len) + "  " + v.ljust(r_len) for k, v in self._repr_content.items()
         )
 
@@ -224,47 +195,14 @@
         return {
             name: getattr(self, name)
             for name, param in inspect.signature(self.__init__).parameters.items()  # type: ignore
             if param.kind != param.VAR_KEYWORD
         }
 
 
-class FileConfig(Config):
-    """Base class for configurations that are stored in a local file.
-
-    Parameters
-    ----------
-    filename
-        The file's name.
-    directory
-        The directory where the file is contained. Defaults to the location of the `datasets`
-        module.
-    desc
-        Extra config parameters to pass as keyword arguments.
-
-    """
-
-    def __init__(self, filename, directory=None, **desc):
-        super().__init__(**desc)
-        self.filename = filename
-        self.directory = directory
-
-    @property
-    def path(self):
-        if self.directory:
-            return pathlib.Path(self.directory).joinpath(self.filename)
-        return pathlib.Path(__file__).parent.joinpath(self.filename)
-
-    @property
-    def _repr_content(self):
-        content = super()._repr_content
-        content["Path"] = str(self.path)
-        return content
-
-
 class FileDataset(Dataset):
     """Base class for datasets that are stored in a local file.
 
     Small datasets that are part of the spotRiver package inherit from this class.
 
     Parameters
     ----------
@@ -316,36 +254,39 @@
         An optional name to given to the file if the file is unpacked.
     desc
         Extra dataset parameters to pass as keyword arguments.
 
     """
 
     def __init__(self, url, size, unpack=True, filename=None, **desc):
+
         if filename is None:
             filename = path.basename(url)
 
         super().__init__(filename=filename, **desc)
         self.url = url
         self.size = size
         self.unpack = unpack
 
     @property
     def path(self):
         return pathlib.Path(get_data_home(), self.__class__.__name__, self.filename)
 
     def download(self, force=False, verbose=True):
+
         if not force and self.is_downloaded:
             return
 
         # Determine where to download the archive
         directory = self.path.parent
         directory.mkdir(parents=True, exist_ok=True)
         archive_path = directory.joinpath(path.basename(self.url))
 
         with request.urlopen(self.url) as r:
+
             # Notify the user
             if verbose:
                 meta = r.info()
                 try:
                     n_bytes = int(meta["Content-Length"])
                     msg = f"Downloading {self.url} ({utils.pretty.humanize_bytes(n_bytes)})"
                 except KeyError:
@@ -382,14 +323,15 @@
     def _iter(self):
         pass
 
     @property
     def is_downloaded(self):
         """Indicate whether or the data has been correctly downloaded."""
         if self.path.exists():
+
             if self.path.is_file():
                 return self.path.stat().st_size == self.size
             return sum(f.stat().st_size for f in self.path.glob("**/*") if f.is_file())
 
         return False
 
     def __iter__(self):
```

### Comparing `spotRiver-0.0.85/src/spotRiver/data/opm.py` & `spotRiver-0.0.9/src/spotRiver/data/opm.py`

 * *Files 23% similar despite different names*

```diff
@@ -43,62 +43,34 @@
     *,
     data_home: Union[str, Path] = None,
     download_if_missing: bool = True,
     return_X_y: bool = False,
     include_numeric: bool = True,
     include_categorical: bool = False,
 ) -> Union[Tuple[pd.DataFrame, pd.Series], pd.DataFrame, Bunch]:
-    """Fetch the OPM dataset from the Connecticut Open Data portal.
-
+    """Load the Office of Planning and Managment dataset (regression).
     Parameters
     ----------
-    data_home : str or pathlib.Path, default=None
-        Specify another download and cache folder for the datasets. By default
-        all spotRiver data is stored in '~/spotriver_data' subfolders.
+    data_home : str or Path, default=None
+        Specify another download and cache folder for the dataset.
     download_if_missing : bool, default=True
         If False, raise an IOError if the data is not locally available
-        rather than trying to download the data from the source site.
+        instead of trying to download the data from the source site.
     return_X_y : bool, default=False
-        If True, return `(X, y)` instead of a `Bunch` object. See
-        `sklearn.utils.Bunch` for more information.
-    include_numeric : bool, default=True
-        If True, include numeric columns in the output. Numeric columns include
-        'List Year', 'Assessed Value', 'Sale Amount', 'Sales Ratio', 'lat', 'lon',
-        and 'timestamp_rec'.
-    include_categorical : bool, default=False
-        If True, include categorical columns in the output. Categorical columns
-        include 'Town', 'Address', 'Property Type', 'Residential Type',
-        'Non Use Code', 'Assessor Remarks', and 'OPM remarks'. Columns with fewer
-        than 200 unique values will be treated as categorical.
+        If True, returns ``(data.data, data.target)`` instead of a
+        :class:`~sklearn.utils.Bunch`.
 
     Returns
     -------
-    Bunch or Tuple[pd.DataFrame, pd.Series] or pd.DataFrame
-        If `return_X_y` is False, return a `Bunch` object with the following
-        attributes:
-            * data : pd.DataFrame of shape (n_samples, n_features)
-                The feature matrix.
-            * target : pd.Series of shape (n_samples,)
-                The target vector.
-            * DESCR : str
-                A short description of the dataset.
-        If `return_X_y` is True, return a tuple `(X, y)` where `X` is the feature
-        matrix and `y` is the target vector. If only numeric or categorical
-        columns are included in the output, return a pd.DataFrame instead of a
-        Bunch.
-
-    Examples
-    --------
-    >>> from spotRiver.data import fetch_opm
-        # Fetch the OPM dataset and return a pandas DataFrame
-        opm_df = fetch_opm()
-        # Fetch the OPM dataset, include categorical columns, and return a Bunch object
-        opm_data = fetch_opm(include_numeric=False, include_categorical=True, return_X_y=False)
-        # Fetch the OPM dataset, include numeric and categorical columns, and return a tuple of pandas DataFrames
-        X, y = fetch_opm(include_categorical=True, return_X_y=True)
+    dataset : :class:`~sklearn.utils.Bunch`
+        Dictionary-like object, with the following attributes.
+        data : DataFrame
+        target : Series
+    (data, target) : tuple if ``return_X_y`` is True
+        A tuple of a pandas DataFrame (the data) and a pandas Series (target).
     """
     filename = get_data_home(data_home=data_home) / "opm_2001-2020.csv"
     if not filename.is_file():
         if not download_if_missing:
             raise IOError("Data not found and `download_if_missing` is False")
         logger.info(f"Downloading OPM dataset to '{filename}'.")
         urlretrieve(url=OPM_URL, filename=filename)
@@ -175,16 +147,15 @@
             if df[cat_col].nunique() < 200:
                 df[cat_col] = df[cat_col].astype("category")
 
     if len(cols) == 0:
         raise Exception("No columns selected. Did you set both `include_numeric` and `include_categorical` to False?")
 
     X = df[cols]
-    # y = df["Sale Amount"]
-    y = X.pop("Sale Amount")
+    y = df["Sale Amount"]
 
     if return_X_y:
         return (X, y)
     return Bunch(data=X, target=y)
 
 
 __all__ = ["fetch_opm"]
```

### Comparing `spotRiver-0.0.85/src/spotRiver/data/synth/sea.py` & `spotRiver-0.0.9/src/spotRiver/data/synth/sea.py`

 * *Files 3% similar despite different names*

```diff
@@ -47,28 +47,31 @@
     References
     ----------
     [^1]: [A Streaming Ensemble Algorithm (SEA) for Large-Scale Classification](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.482.3991&rep=rep1&type=pdf)
 
     """
 
     def __init__(self, variant=0, noise=0.0, seed: int = None):
+
         super().__init__(n_features=3, task=datasets.base.BINARY_CLF)
 
         if variant not in (0, 1, 2, 3):
             raise ValueError("Unknown variant, possible choices are: 0, 1, 2, 3")
 
         self.variant = variant
         self.noise = noise
         self.seed = seed
         self._threshold = {0: 8, 1: 9, 2: 7, 3: 9.5}[variant]
 
     def __iter__(self):
+
         rng = random.Random(self.seed)
 
         while True:
+
             x = {i: rng.uniform(0, 10) for i in range(3)}
             y = x[0] + x[1] > self._threshold
 
             if self.noise and rng.random() < self.noise:
                 y = not y
 
             yield x, y
```

### Comparing `spotRiver-0.0.85/src/spotRiver/fun/hyperriver.py` & `spotRiver-0.0.9/src/spotRiver/fun/hyperriver.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,134 +1,52 @@
+import numbers
 from river import time_series
 from river import compose
 from river import linear_model
 from river import optim
 from river import preprocessing
 from river import metrics
+from river import tree
 from numpy.random import default_rng
 import numpy as np
-from numpy import array
-
 from spotRiver.utils.features import get_weekday_distances
 from spotRiver.utils.features import get_ordinal_date
 from spotRiver.utils.features import get_month_distances
 from spotRiver.utils.features import get_hour_distances
 from spotRiver.evaluation.eval_oml import fun_eval_oml_iter_progressive
 from spotRiver.evaluation.eval_oml import eval_oml_iter_progressive
-from spotRiver.evaluation.eval_bml import eval_oml_horizon
-from spotRiver.evaluation.eval_nowcast import eval_nowcast_model
-
-from spotPython.hyperparameters.values import assign_values, iterate_dict_values, convert_keys
-from spotPython.hyperparameters.values import get_dict_with_levels_and_types
-from spotPython.utils.transform import transform_hyper_parameter_values
-
-import logging
-import statistics
-from sklearn.metrics import mean_absolute_error
-
-logger = logging.getLogger(__name__)
-# configure the handler and formatter as needed
-py_handler = logging.FileHandler(f"{__name__}.log", mode="w")
-py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
-# add formatter to the handler
-py_handler.setFormatter(py_formatter)
-# add handler to the logger
-logger.addHandler(py_handler)
+from spotRiver.utils.selectors import select_splitter
+from spotRiver.utils.selectors import select_leaf_prediction
+from spotRiver.utils.selectors import select_leaf_model
+from spotRiver.utils.selectors import select_max_depth
 
 
 class HyperRiver:
     """
     Hyperparameter Tuning for River.
 
     Args:
         seed (int): seed.
             See [Numpy Random Sampling](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
 
     """
 
-    def __init__(self, seed=126, log_level=50):
+    def __init__(self, seed=126):
         self.seed = seed
         self.rng = default_rng(seed=self.seed)
-        self.fun_control = {
-            "seed": None,
-            "data": None,
-            "step": 10_000,
-            "horizon": None,
-            "grace_period": None,
-            "metric": metrics.MAE(),
-            "metric_sklearn": mean_absolute_error,
-            "weights": array([1, 0, 0]),
-            "weight_coeff": 0.0,
-            "log_level": log_level,
-            "var_name": [],
-            "var_type": [],
-            "prep_model": None,
-        }
-        self.log_level = self.fun_control["log_level"]
-        logger.setLevel(self.log_level)
-        logger.info(f"Starting the logger at level {self.log_level} for module {__name__}:")
+        self.fun_control = {"seed": None, "data": None, "horizon": None, "grace_period": None, "metric": metrics.MAE()}
 
     # def get_month_distances(x):
     #     return {
     #         calendar.month_name[month]: math.exp(-(x['month'].month - month) ** 2)
     #         for month in range(1, 13)
     #     }
 
     # def get_ordinal_date(x):
     #     return {'ordinal_date': x['month'].toordinal()}
-    def fun_nowcasting(self, X, fun_control=None):
-        """Hyperparameter Tuning of the nowcasting model.
-
-        Returns:
-            (float): objective function value. Mean of the MAEs of the predicted values.
-        """
-        self.fun_control.update(fun_control)
-
-        try:
-            X.shape[1]
-        except ValueError:
-            X = np.array([X])
-        if X.shape[1] != 5:
-            raise Exception
-        lr = X[:, 0]
-        intercept_lr = X[:, 1]
-        hour = X[:, 2]
-        weekday = X[:, 3]
-        month = X[:, 4]
-
-        z_res = np.array([], dtype=float)
-        for i in range(X.shape[0]):
-            h_i = int(hour[i])
-            w_i = int(weekday[i])
-            m_i = int(month[i])
-            # baseline:
-            extract_features = compose.TransformerUnion(get_ordinal_date)
-            if h_i:
-                extract_features = compose.TransformerUnion(get_ordinal_date, get_hour_distances)
-            if w_i:
-                extract_features = compose.TransformerUnion(extract_features, get_weekday_distances)
-            if m_i:
-                extract_features = compose.TransformerUnion(extract_features, get_month_distances)
-            model = compose.Pipeline(
-                ("features", extract_features),
-                ("scale", preprocessing.StandardScaler()),
-                (
-                    "lin_reg",
-                    linear_model.LinearRegression(
-                        intercept_init=0, optimizer=optim.SGD(float(lr[i])), intercept_lr=float(intercept_lr[i])
-                    ),
-                ),
-            )
-            # eval:
-            dates, metric, y_trues, y_preds = eval_nowcast_model(
-                model, dataset=self.fun_control["data"], time_interval="Time"
-            )
-            z = metric.get()
-            z_res = np.append(z_res, z)
-        return z_res
 
     def fun_snarimax(self, X, fun_control=None):
         """Hyperparameter Tuning of the SNARIMAX model.
             SNARIMAX stands for (S)easonal (N)on-linear (A)uto(R)egressive (I)ntegrated (M)oving-(A)verage with
             e(X)ogenous inputs model.
         This model generalizes many established time series models in a single interface that can be
         trained online. It assumes that the provided training data is ordered in time and is uniformly spaced.
@@ -297,22 +215,21 @@
                             intercept_lr=float(intercept_lr[i]),
                         ),
                     ),
                 ),
             )
             # eval:
             res = time_series.evaluate(
-                self.fun_control["data"],
-                model,
-                metric=self.fun_control["metric"],
-                horizon=self.fun_control["horizon"],
-                agg_func=statistics.mean,
+                self.fun_control["data"], model, metric=self.fun_control["metric"], horizon=self.fun_control["horizon"]
             )
-            z = res.get()
-            z_res = np.append(z_res, z)
+            y = res.metrics
+            z = 0.0
+            for j in range(len(y)):
+                z = z + y[j].get()
+            z_res = np.append(z_res, z / len(y))
         return z_res
 
     def fun_hw(self, X, fun_control=None):
         """Hyperparameter Tuning of the HoltWinters model.
 
             Holt-Winters forecaster. This is a standard implementation of the Holt-Winters forecasting method.
             Certain parameterizations result in special cases, such as simple exponential smoothing.
@@ -363,239 +280,151 @@
             )
             res = time_series.evaluate(
                 self.fun_control["data"],
                 model,
                 metric=self.fun_control["metric"],
                 horizon=self.fun_control["horizon"],
                 grace_period=self.fun_control["grace_period"],
-                agg_func=statistics.mean,
             )
-            z = res.get()
-            z_res = np.append(z_res, z)
+            y = res.metrics
+            z = 0.0
+            for j in range(len(y)):
+                z = z + y[j].get()
+            z_res = np.append(z_res, z / len(y))
         return z_res
 
-    # def fun_HTR_iter_progressive(self, X, fun_control=None):
-    #     """Hyperparameter Tuning of HTR model.
-    #     See: https://riverml.xyz/0.15.0/api/tree/HoeffdingTreeRegressor/
-    #     Parameters
-    #     ----------
-    #     grace_period
-    #         Number of instances a leaf should observe between split attempts.
-    #     max_depth
-    #         The maximum depth a tree can reach. If `None`, the tree will grow indefinitely.
-    #     delta
-    #         Significance level to calculate the Hoeffding bound. The significance level is given by
-    #         `1 - delta`. Values closer to zero imply longer split decision delays.
-    #     tau
-    #         Threshold below which a split will be forced to break ties.
-    #     leaf_prediction
-    #         Prediction mechanism used at leafs. NOTE: order differs from the order in river!</br>
-    #         - 'mean' - Target mean</br>
-    #         - 'adaptive' - Chooses between 'mean' and 'model' dynamically</br>
-    #         - 'model' - Uses the model defined in `leaf_model`</br>
-    #     NOT IMPLEMENTED: leaf_model
-    #         The regression model used to provide responses if `leaf_prediction='model'`. If not
-    #         provided an instance of `river.linear_model.LinearRegression` with the default
-    #         hyperparameters is used.
-    #     model_selector_decay
-    #         The exponential decaying factor applied to the learning models' squared errors, that
-    #         are monitored if `leaf_prediction='adaptive'`. Must be between `0` and `1`. The closer
-    #         to `1`, the more importance is going to be given to past observations. On the other hand,
-    #         if its value approaches `0`, the recent observed errors are going to have more influence
-    #         on the final decision.
-    #     nominal_attributes
-    #         List of Nominal attributes identifiers. If empty, then assume that all numeric attributes
-    #         should be treated as continuous.
-    #     splitter
-    #         The Splitter or Attribute Observer (AO) used to monitor the class statistics of numeric
-    #         features and perform splits. Splitters are available in the `tree.splitter` module.
-    #         Different splitters are available for classification and regression tasks. Classification
-    #         and regression splitters can be distinguished by their property `is_target_class`.
-    #         This is an advanced option. Special care must be taken when choosing different splitters.
-    #         By default, `tree.splitter.TEBSTSplitter` is used if `splitter` is `None`.
-    #     min_samples_split
-    #         The minimum number of samples every branch resulting from a split candidate must have
-    #         to be considered valid.
-    #     binary_split
-    #         If True, only allow binary splits.
-    #     max_size
-    #         The max size of the tree, in Megabytes (MB).
-    #     memory_estimate_period
-    #         Interval (number of processed instances) between memory consumption checks.
-    #     stop_mem_management
-    #         If True, stop growing as soon as memory limit is hit.
-    #     remove_poor_attrs
-    #         If True, disable poor attributes to reduce memory usage.
-    #     merit_preprune
-    #         If True, enable merit-based tree pre-pruning.
-
-    #     fun_control
-    #         Parameters that are are not tuned:
-    #             1. `horizon`: (int)
-    #             2. `grace_period`: (int) Initial period during which the metric is not updated.
-    #                     This is to fairly evaluate models which need a warming up period to start
-    #                     producing meaningful forecasts.
-    #                     The value of this parameter is equal to the `horizon` by default.
-    #             3. `data`: dataset. Default `AirlinePassengers`.
-
-    #     Returns
-    #     -------
-    #     (float): objective function value. Mean of the MAEs of the predicted values.
-    #     """
-    #     self.fun_control.update(fun_control)
-    #     try:
-    #         X.shape[1]
-    #     except ValueError:
-    #         X = np.array([X])
-    #     if X.shape[1] != 11:
-    #         raise Exception
-    #     grace_period = X[:, 0]
-    #     max_depth = X[:, 1]
-    #     delta = X[:, 2]
-    #     tau = X[:, 3]
-    #     leaf_prediction = X[:, 4]
-    #     leaf_model = X[:, 5]
-    #     model_selector_decay = X[:, 6]
-    #     splitter = X[:, 7]
-    #     min_samples_split = X[:, 8]
-    #     binary_split = X[:, 9]
-    #     max_size = X[:, 10]
-    #     z_res = np.array([], dtype=float)
-    #     dataset_list = self.fun_control["data"]
-    #     for i in range(X.shape[0]):
-    #         num = compose.SelectType(numbers.Number) | preprocessing.StandardScaler()
-    #         cat = compose.SelectType(str) | preprocessing.FeatureHasher(n_features=1000, seed=1)
-    #         try:
-    #             res = eval_oml_iter_progressive(
-    #                 dataset=dataset_list,
-    #                 step=self.fun_control["step"],
-    #                 log_level=self.fun_control["log_level"],
-    #                 metric=fun_control["metric"],
-    #                 weight_coeff=fun_control["weight_coeff"],
-    #                 models={
-    #                     "HTR": (
-    #                         (num + cat)
-    #                         | tree.HoeffdingTreeRegressor(
-    #                             grace_period=int(grace_period[i]),
-    #                             max_depth=transform_power_10(int(max_depth[i])),
-    #                             delta=float(delta[i]),
-    #                             tau=float(tau[i]),
-    #                             leaf_prediction=select_leaf_prediction(int(leaf_prediction[i])),
-    #                             leaf_model=select_leaf_model(int(leaf_model[i])),
-    #                             model_selector_decay=float(model_selector_decay[i]),
-    #                             splitter=select_splitter(int(splitter[i])),
-    #                             min_samples_split=int(min_samples_split[i]),
-    #                             binary_split=int(binary_split[i]),
-    #                             max_size=float(max_size[i]),
-    #                         )
-    #                     ),
-    #                 },
-    #             )
-    #             logger.debug("res from eval_oml_iter_progressive: %s", res)
-    #             y = fun_eval_oml_iter_progressive(res, metric=None, weights=self.fun_control["weights"])
-    #         except Exception as err:
-    #             y = np.nan
-    #             print(f"Error in fun(). Call to evaluate failed. {err=}, {type(err)=}")
-    #             print(f"Setting y to {y:.2f}.")
-    #         z_res = np.append(z_res, y / self.fun_control["n_samples"])
-    #     return z_res
+    def fun_HTR_iter_progressive(self, X, fun_control=None):
+        """Hyperparameter Tuning of HTR model.
+        See: https://riverml.xyz/0.15.0/api/tree/HoeffdingTreeRegressor/
+        Parameters
+        ----------
+        grace_period
+            Number of instances a leaf should observe between split attempts.
+        max_depth
+            The maximum depth a tree can reach. If `None`, the tree will grow indefinitely.
+        delta
+            Significance level to calculate the Hoeffding bound. The significance level is given by
+            `1 - delta`. Values closer to zero imply longer split decision delays.
+        tau
+            Threshold below which a split will be forced to break ties.
+        leaf_prediction
+            Prediction mechanism used at leafs. NOTE: order differs from the order in river!</br>
+            - 'mean' - Target mean</br>
+            - 'adaptive' - Chooses between 'mean' and 'model' dynamically</br>
+            - 'model' - Uses the model defined in `leaf_model`</br>
+        NOT IMPLEMENTED: leaf_model
+            The regression model used to provide responses if `leaf_prediction='model'`. If not
+            provided an instance of `river.linear_model.LinearRegression` with the default
+            hyperparameters is used.
+        model_selector_decay
+            The exponential decaying factor applied to the learning models' squared errors, that
+            are monitored if `leaf_prediction='adaptive'`. Must be between `0` and `1`. The closer
+            to `1`, the more importance is going to be given to past observations. On the other hand,
+            if its value approaches `0`, the recent observed errors are going to have more influence
+            on the final decision.
+        nominal_attributes
+            List of Nominal attributes identifiers. If empty, then assume that all numeric attributes
+            should be treated as continuous.
+        splitter
+            The Splitter or Attribute Observer (AO) used to monitor the class statistics of numeric
+            features and perform splits. Splitters are available in the `tree.splitter` module.
+            Different splitters are available for classification and regression tasks. Classification
+            and regression splitters can be distinguished by their property `is_target_class`.
+            This is an advanced option. Special care must be taken when choosing different splitters.
+            By default, `tree.splitter.TEBSTSplitter` is used if `splitter` is `None`.
+        min_samples_split
+            The minimum number of samples every branch resulting from a split candidate must have
+            to be considered valid.
+        binary_split
+            If True, only allow binary splits.
+        max_size
+            The max size of the tree, in Megabytes (MB).
+        memory_estimate_period
+            Interval (number of processed instances) between memory consumption checks.
+        stop_mem_management
+            If True, stop growing as soon as memory limit is hit.
+        remove_poor_attrs
+            If True, disable poor attributes to reduce memory usage.
+        merit_preprune
+            If True, enable merit-based tree pre-pruning.
+
+        fun_control
+            Parameters that are are not tuned:
+                1. `horizon`: (int)
+                2. `grace_period`: (int) Initial period during which the metric is not updated.
+                        This is to fairly evaluate models which need a warming up period to start
+                        producing meaningful forecasts.
+                        The value of this parameter is equal to the `horizon` by default.
+                3. `data`: dataset. Default `AirlinePassengers`.
 
-    def fun_oml_iter_progressive(self, X, fun_control=None):
-        """Hyperparameter Tuning of an arbitrary model.
         Returns
         -------
         (float): objective function value. Mean of the MAEs of the predicted values.
         """
         self.fun_control.update(fun_control)
         try:
             X.shape[1]
         except ValueError:
             X = np.array([X])
-        if X.shape[1] != len(self.fun_control["var_name"]):
+        if X.shape[1] != 11:
             raise Exception
-        var_dict = assign_values(X, self.fun_control["var_name"])
+        grace_period = X[:, 0]
+        max_depth = X[:, 1]
+        delta = X[:, 2]
+        tau = X[:, 3]
+        leaf_prediction = X[:, 4]
+        leaf_model = X[:, 5]
+        model_selector_decay = X[:, 6]
+        splitter = X[:, 7]
+        min_samples_split = X[:, 8]
+        binary_split = X[:, 9]
+        max_size = X[:, 10]
         z_res = np.array([], dtype=float)
-        dataset_list = self.fun_control["data"]
-        for values in iterate_dict_values(var_dict):
-            values = convert_keys(values, self.fun_control["var_type"])
-            print(values)
-            values = get_dict_with_levels_and_types(fun_control=self.fun_control, v=values)
-            values = transform_hyper_parameter_values(fun_control=self.fun_control, hyper_parameter_values=values)
-            print(values)
-            model = compose.Pipeline(self.fun_control["prep_model"], self.fun_control["core_model"](**values))
+        for i in range(X.shape[0]):
+            #
+            print("grace_period", int(grace_period[i]))
+            print("max_depth", select_max_depth(int(max_depth[i])))
+            print("delta", float(delta[i]))
+            print("tau", float(tau[i]))
+            print("leaf_prediction", select_leaf_prediction(int(leaf_prediction[i])))
+            print("leaf_model", select_leaf_model(int(leaf_model[i])))
+            print("model_selector_decay", float(model_selector_decay[i]))
+            print("splitter", select_splitter(int(splitter[i])))
+            print("min_samples_split", int(min_samples_split[i]))
+            print("binary_split", int(binary_split[i]))
+            print("max_size", float(max_size[i]))
+            #
+            num = compose.SelectType(numbers.Number) | preprocessing.StandardScaler()
+            # cat = compose.SelectType(str) | preprocessing.OneHotEncoder()
+            cat = compose.SelectType(str) | preprocessing.FeatureHasher(n_features=1000, seed=1)
             try:
                 res = eval_oml_iter_progressive(
-                    dataset=dataset_list,
-                    step=self.fun_control["step"],
-                    log_level=self.fun_control["log_level"],
-                    metric=fun_control["metric"],
-                    weight_coeff=fun_control["weight_coeff"],
+                    dataset=self.fun_control["data"],
+                    step=10000,
+                    verbose=True,
+                    metric=metrics.MAE(),
                     models={
-                        self.fun_control["model_name"]: (model),
+                        "HTR": (
+                            (num + cat)
+                            | tree.HoeffdingTreeRegressor(
+                                grace_period=int(grace_period[i]),
+                                max_depth=select_max_depth(int(max_depth[i])),
+                                delta=float(delta[i]),
+                                tau=float(tau[i]),
+                                leaf_prediction=select_leaf_prediction(int(leaf_prediction[i])),
+                                leaf_model=select_leaf_model(int(leaf_model[i])),
+                                model_selector_decay=float(model_selector_decay[i]),
+                                splitter=select_splitter(int(splitter[i])),
+                                min_samples_split=int(min_samples_split[i]),
+                                binary_split=int(binary_split[i]),
+                                max_size=float(max_size[i])
+                            )
+                        ),
                     },
                 )
-                logger.debug("res from eval_oml_iter_progressive: %s", res)
-                y = fun_eval_oml_iter_progressive(res, metric=None, weights=self.fun_control["weights"])
-            except Exception as err:
-                y = np.nan
-                print(f"Error in fun(). Call to evaluate failed. {err=}, {type(err)=}")
-                print(f"Setting y to {y:.2f}.")
-            z_res = np.append(z_res, y / self.fun_control["n_samples"])
-        return z_res
-
-    def fun_oml_horizon(self, X, fun_control=None, return_model=False, return_df=False):
-        """Hyperparameter Tuning of an arbitrary model.
-        Returns
-        -------
-        (float): objective function value. Mean of the MAEs of the predicted values.
-        """
-        self.fun_control.update(fun_control)
-        weights = self.fun_control["weights"]
-        if len(weights) != 3:
-            raise ValueError("The weights array must be of length 3.")
-        try:
-            X.shape[1]
-        except ValueError:
-            X = np.array([X])
-        if X.shape[1] != len(self.fun_control["var_name"]):
-            raise Exception
-        var_dict = assign_values(X, self.fun_control["var_name"])
-        z_res = np.array([], dtype=float)
-        for values in iterate_dict_values(var_dict):
-            values = convert_keys(values, self.fun_control["var_type"])
-            values = get_dict_with_levels_and_types(fun_control=self.fun_control, v=values)
-            values = transform_hyper_parameter_values(fun_control=self.fun_control, hyper_parameter_values=values)
-            model = compose.Pipeline(self.fun_control["prep_model"], self.fun_control["core_model"](**values))
-            if return_model:
-                return model
-            try:
-                df_eval, df_preds = eval_oml_horizon(
-                    model=model,
-                    train=self.fun_control["train"],
-                    test=self.fun_control["test"],
-                    target_column=self.fun_control["target_column"],
-                    horizon=self.fun_control["horizon"],
-                    oml_grace_period=self.fun_control["oml_grace_period"],
-                    metric=self.fun_control["metric_sklearn"],
-                )
-            except Exception as err:
-                print(f"Error in fun_oml_horizon(). Call to eval_oml_horizon failed. {err=}, {type(err)=}")
-            if return_df:
-                return df_eval, df_preds
-            try:
-                # take the mean of the MAEs/ACCs of the predicted values and ignore the NaN values
-                df_eval = df_eval.dropna()
-                y_error = df_eval["Metric"].mean()
-                logger.debug("y_error from eval_oml_horizon: %s", y_error)
-                y_r_time = df_eval["CompTime (s)"].mean()
-                logger.debug("y_r_time from eval_oml_horizon: %s", y_r_time)
-                y_memory = df_eval["Memory (MB)"].mean()
-                logger.debug("y_memory from eval_oml_horizon: %s", y_memory)
-                logger.debug("weights from eval_oml_horizon: %s", weights)
-                y = weights[0] * y_error + weights[1] * y_r_time + weights[2] * y_memory
-                logger.debug("weighted res from eval_oml_horizon: %s", y)
+                y = fun_eval_oml_iter_progressive(res, metric=None)
             except Exception as err:
                 y = np.nan
                 print(f"Error in fun(). Call to evaluate failed. {err=}, {type(err)=}")
                 print(f"Setting y to {y:.2f}.")
             z_res = np.append(z_res, y / self.fun_control["n_samples"])
         return z_res
```

### Comparing `spotRiver-0.0.85/src/spotRiver/utils/features.py` & `spotRiver-0.0.9/src/spotRiver/utils/features.py`

 * *Files identical despite different names*

### Comparing `spotRiver-0.0.85/src/spotRiver.egg-info/PKG-INFO` & `spotRiver-0.0.9/src/spotRiver.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: spotRiver
-Version: 0.0.85
+Version: 0.0.9
 Summary: spotRiver - Sequential Parameter Optimization Interface to River
 Author-email: "T. Bartz-Beielstein" <tbb@bartzundbartz.de>
 Project-URL: Homepage, https://www.spotseven.de
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.10
```

