# Comparing `tmp/filelock-3.9.0.tar.gz` & `tmp/filelock-3.9.1.tar.gz`

## Comparing `filelock-3.9.0.tar` & `filelock-3.9.1.tar`

### file list

```diff
@@ -1,15 +1,15 @@
--rw-r--r--   0        0        0     1315 2020-02-02 00:00:00.000000 filelock-3.9.0/src/filelock/__init__.py
--rw-r--r--   0        0        0     8896 2020-02-02 00:00:00.000000 filelock-3.9.0/src/filelock/_api.py
--rw-r--r--   0        0        0      399 2020-02-02 00:00:00.000000 filelock-3.9.0/src/filelock/_error.py
--rw-r--r--   0        0        0     1650 2020-02-02 00:00:00.000000 filelock-3.9.0/src/filelock/_soft.py
--rw-r--r--   0        0        0     1578 2020-02-02 00:00:00.000000 filelock-3.9.0/src/filelock/_unix.py
--rw-r--r--   0        0        0      594 2020-02-02 00:00:00.000000 filelock-3.9.0/src/filelock/_util.py
--rw-r--r--   0        0        0     1890 2020-02-02 00:00:00.000000 filelock-3.9.0/src/filelock/_windows.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 filelock-3.9.0/src/filelock/py.typed
--rw-r--r--   0        0        0      160 2020-02-02 00:00:00.000000 filelock-3.9.0/src/filelock/version.py
--rw-r--r--   0        0        0    13961 2020-02-02 00:00:00.000000 filelock-3.9.0/tests/test_filelock.py
--rw-r--r--   0        0        0      185 2020-02-02 00:00:00.000000 filelock-3.9.0/.gitignore
--rw-r--r--   0        0        0     1210 2020-02-02 00:00:00.000000 filelock-3.9.0/LICENSE
--rw-r--r--   0        0        0      860 2020-02-02 00:00:00.000000 filelock-3.9.0/README.md
--rw-r--r--   0        0        0     2234 2020-02-02 00:00:00.000000 filelock-3.9.0/pyproject.toml
--rw-r--r--   0        0        0     2329 2020-02-02 00:00:00.000000 filelock-3.9.0/PKG-INFO
+-rw-r--r--   0        0        0     1329 2020-02-02 00:00:00.000000 filelock-3.9.1/src/filelock/__init__.py
+-rw-r--r--   0        0        0     8901 2020-02-02 00:00:00.000000 filelock-3.9.1/src/filelock/_api.py
+-rw-r--r--   0        0        0      399 2020-02-02 00:00:00.000000 filelock-3.9.1/src/filelock/_error.py
+-rw-r--r--   0        0        0     1650 2020-02-02 00:00:00.000000 filelock-3.9.1/src/filelock/_soft.py
+-rw-r--r--   0        0        0     1578 2020-02-02 00:00:00.000000 filelock-3.9.1/src/filelock/_unix.py
+-rw-r--r--   0        0        0      594 2020-02-02 00:00:00.000000 filelock-3.9.1/src/filelock/_util.py
+-rw-r--r--   0        0        0     1890 2020-02-02 00:00:00.000000 filelock-3.9.1/src/filelock/_windows.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 filelock-3.9.1/src/filelock/py.typed
+-rw-r--r--   0        0        0      160 2020-02-02 00:00:00.000000 filelock-3.9.1/src/filelock/version.py
+-rw-r--r--   0        0        0    13961 2020-02-02 00:00:00.000000 filelock-3.9.1/tests/test_filelock.py
+-rw-r--r--   0        0        0      185 2020-02-02 00:00:00.000000 filelock-3.9.1/.gitignore
+-rw-r--r--   0        0        0     1210 2020-02-02 00:00:00.000000 filelock-3.9.1/LICENSE
+-rw-r--r--   0        0        0      854 2020-02-02 00:00:00.000000 filelock-3.9.1/README.md
+-rw-r--r--   0        0        0     2275 2020-02-02 00:00:00.000000 filelock-3.9.1/pyproject.toml
+-rw-r--r--   0        0        0     2362 2020-02-02 00:00:00.000000 filelock-3.9.1/PKG-INFO
```

### Comparing `filelock-3.9.0/src/filelock/__init__.py` & `filelock-3.9.1/src/filelock/__init__.py`

 * *Files 3% similar despite different names*

```diff
@@ -26,15 +26,15 @@
     _FileLock: type[BaseFileLock] = WindowsFileLock
 else:  # pragma: win32 no cover
     if has_fcntl:
         _FileLock: type[BaseFileLock] = UnixFileLock
     else:
         _FileLock = SoftFileLock
         if warnings is not None:
-            warnings.warn("only soft file lock is available")
+            warnings.warn("only soft file lock is available", stacklevel=2)
 
 #: Alias for the lock, which should be used for the current platform. On Windows, this is an alias for
 # :class:`WindowsFileLock`, on Unix for :class:`UnixFileLock` and otherwise for :class:`SoftFileLock`.
 if TYPE_CHECKING:
     FileLock = SoftFileLock
 else:
     FileLock = _FileLock
```

### Comparing `filelock-3.9.0/src/filelock/_api.py` & `filelock-3.9.1/src/filelock/_api.py`

 * *Files 2% similar despite different names*

```diff
@@ -160,29 +160,29 @@
 
         # Increment the number right at the beginning. We can still undo it, if something fails.
         with self._thread_lock:
             self._lock_counter += 1
 
         lock_id = id(self)
         lock_filename = self._lock_file
-        start_time = time.monotonic()
+        start_time = time.perf_counter()
         try:
             while True:
                 with self._thread_lock:
                     if not self.is_locked:
                         _LOGGER.debug("Attempting to acquire lock %s on %s", lock_id, lock_filename)
                         self._acquire()
 
                 if self.is_locked:
                     _LOGGER.debug("Lock %s acquired on %s", lock_id, lock_filename)
                     break
                 elif blocking is False:
                     _LOGGER.debug("Failed to immediately acquire lock %s on %s", lock_id, lock_filename)
                     raise Timeout(self._lock_file)
-                elif 0 <= timeout < time.monotonic() - start_time:
+                elif 0 <= timeout < time.perf_counter() - start_time:
                     _LOGGER.debug("Timeout on acquiring lock %s on %s", lock_id, lock_filename)
                     raise Timeout(self._lock_file)
                 else:
                     msg = "Lock %s not acquired on %s, waiting %s seconds ..."
                     _LOGGER.debug(msg, lock_id, lock_filename, poll_interval)
                     time.sleep(poll_interval)
         except BaseException:  # Something did go wrong, so decrement the counter.
@@ -195,15 +195,14 @@
         """
         Releases the file lock. Please note, that the lock is only completely released, if the lock counter is 0. Also
         note, that the lock file itself is not automatically deleted.
 
         :param force: If true, the lock counter is ignored and the lock is released in every case/
         """
         with self._thread_lock:
-
             if self.is_locked:
                 self._lock_counter -= 1
 
                 if self._lock_counter == 0 or force:
                     lock_id, lock_filename = id(self), self._lock_file
 
                     _LOGGER.debug("Attempting to release lock %s on %s", lock_id, lock_filename)
```

### Comparing `filelock-3.9.0/src/filelock/_soft.py` & `filelock-3.9.1/src/filelock/_soft.py`

 * *Files identical despite different names*

### Comparing `filelock-3.9.0/src/filelock/_unix.py` & `filelock-3.9.1/src/filelock/_unix.py`

 * *Files identical despite different names*

### Comparing `filelock-3.9.0/src/filelock/_util.py` & `filelock-3.9.1/src/filelock/_util.py`

 * *Files identical despite different names*

### Comparing `filelock-3.9.0/src/filelock/_windows.py` & `filelock-3.9.1/src/filelock/_windows.py`

 * *Files identical despite different names*

### Comparing `filelock-3.9.0/tests/test_filelock.py` & `filelock-3.9.1/tests/test_filelock.py`

 * *Files identical despite different names*

### Comparing `filelock-3.9.0/LICENSE` & `filelock-3.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `filelock-3.9.0/README.md` & `filelock-3.9.1/README.md`

 * *Files 11% similar despite different names*

```diff
@@ -3,11 +3,11 @@
 [![PyPI](https://img.shields.io/pypi/v/filelock)](https://pypi.org/project/filelock/)
 [![Supported Python
 versions](https://img.shields.io/pypi/pyversions/filelock.svg)](https://pypi.org/project/filelock/)
 [![Documentation
 status](https://readthedocs.org/projects/py-filelock/badge/?version=latest)](https://py-filelock.readthedocs.io/en/latest/?badge=latest)
 [![Code style:
 black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
-[![Downloads](https://pepy.tech/badge/filelock/month)](https://pepy.tech/project/filelock/month)
+[![Downloads](https://pepy.tech/badge/filelock/month)](https://pepy.tech/project/filelock)
 [![check](https://github.com/tox-dev/py-filelock/actions/workflows/check.yml/badge.svg)](https://github.com/tox-dev/py-filelock/actions/workflows/check.yml)
 
 For more information checkout the [official documentation](https://py-filelock.readthedocs.io/en/latest/index.html).
```

### Comparing `filelock-3.9.0/pyproject.toml` & `filelock-3.9.1/pyproject.toml`

 * *Files 7% similar despite different names*

```diff
@@ -1,44 +1,59 @@
 [build-system]
 build-backend = "hatchling.build"
-requires = ["hatchling>=1.11.1", "hatch-vcs>=0.3"]
+requires = [
+  "hatch-vcs>=0.3",
+  "hatchling>=1.13",
+]
 
 [project]
 name = "filelock"
 description = "A platform independent file lock."
 readme = "README.md"
+keywords = [
+  "application",
+  "cache",
+  "directory",
+  "log",
+  "user",
+]
 license = "Unlicense"
 maintainers = [{ name = "Bernát Gábor", email = "gaborjbernat@gmail.com" }]
-urls.Documentation = "https://py-filelock.readthedocs.io"
-urls.Homepage = "https://github.com/tox-dev/py-filelock"
-urls.Source = "https://github.com/tox-dev/py-filelock"
-urls.Tracker = "https://github.com/tox-dev/py-filelock/issues"
 requires-python = ">=3.7"
-optional-dependencies.testing = [
-  "covdefaults>=2.2.2",
-  "coverage>=7.0.1",
-  "pytest>=7.2",
-  "pytest-cov>=4",
-  "pytest-timeout>=2.1",
-]
-optional-dependencies.docs = ["furo>=2022.12.7", "sphinx>=5.3", "sphinx-autodoc-typehints>=1.19.5"]
-keywords = ["application", "cache", "directory", "log", "user"]
 classifiers = [
   "Development Status :: 5 - Production/Stable",
   "Intended Audience :: Developers",
   "License :: OSI Approved :: The Unlicense (Unlicense)",
   "Operating System :: OS Independent",
   "Programming Language :: Python",
   "Programming Language :: Python :: 3",
   "Programming Language :: Python :: 3 :: Only",
   "Topic :: Internet",
   "Topic :: Software Development :: Libraries",
   "Topic :: System",
 ]
-dynamic = ["version"]
+dynamic = [
+  "version",
+]
+optional-dependencies.docs = [
+  "furo>=2022.12.7",
+  "sphinx>=6.1.3",
+  "sphinx-autodoc-typehints!=1.23.4,>=1.22",
+]
+optional-dependencies.testing = [
+  "covdefaults>=2.3",
+  "coverage>=7.2.1",
+  "pytest>=7.2.2",
+  "pytest-cov>=4",
+  "pytest-timeout>=2.1",
+]
+urls.Documentation = "https://py-filelock.readthedocs.io"
+urls.Homepage = "https://github.com/tox-dev/py-filelock"
+urls.Source = "https://github.com/tox-dev/py-filelock"
+urls.Tracker = "https://github.com/tox-dev/py-filelock/issues"
 
 [tool.hatch]
 build.hooks.vcs.version-file = "src/filelock/version.py"
 build.targets.sdist.include = ["/src", "/tests"]
 version.source = "vcs"
 
 [tool.coverage]
```

### Comparing `filelock-3.9.0/PKG-INFO` & `filelock-3.9.1/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,16 +1,17 @@
 Metadata-Version: 2.1
 Name: filelock
-Version: 3.9.0
+Version: 3.9.1
 Summary: A platform independent file lock.
 Project-URL: Documentation, https://py-filelock.readthedocs.io
 Project-URL: Homepage, https://github.com/tox-dev/py-filelock
 Project-URL: Source, https://github.com/tox-dev/py-filelock
 Project-URL: Tracker, https://github.com/tox-dev/py-filelock/issues
 Maintainer-email: Bernát Gábor <gaborjbernat@gmail.com>
+License-Expression: Unlicense
 License-File: LICENSE
 Keywords: application,cache,directory,log,user
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: The Unlicense (Unlicense)
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
@@ -18,30 +19,30 @@
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Topic :: Internet
 Classifier: Topic :: Software Development :: Libraries
 Classifier: Topic :: System
 Requires-Python: >=3.7
 Provides-Extra: docs
 Requires-Dist: furo>=2022.12.7; extra == 'docs'
-Requires-Dist: sphinx-autodoc-typehints>=1.19.5; extra == 'docs'
-Requires-Dist: sphinx>=5.3; extra == 'docs'
+Requires-Dist: sphinx-autodoc-typehints!=1.23.4,>=1.22; extra == 'docs'
+Requires-Dist: sphinx>=6.1.3; extra == 'docs'
 Provides-Extra: testing
-Requires-Dist: covdefaults>=2.2.2; extra == 'testing'
-Requires-Dist: coverage>=7.0.1; extra == 'testing'
+Requires-Dist: covdefaults>=2.3; extra == 'testing'
+Requires-Dist: coverage>=7.2.1; extra == 'testing'
 Requires-Dist: pytest-cov>=4; extra == 'testing'
 Requires-Dist: pytest-timeout>=2.1; extra == 'testing'
-Requires-Dist: pytest>=7.2; extra == 'testing'
+Requires-Dist: pytest>=7.2.2; extra == 'testing'
 Description-Content-Type: text/markdown
 
 # py-filelock
 
 [![PyPI](https://img.shields.io/pypi/v/filelock)](https://pypi.org/project/filelock/)
 [![Supported Python
 versions](https://img.shields.io/pypi/pyversions/filelock.svg)](https://pypi.org/project/filelock/)
 [![Documentation
 status](https://readthedocs.org/projects/py-filelock/badge/?version=latest)](https://py-filelock.readthedocs.io/en/latest/?badge=latest)
 [![Code style:
 black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
-[![Downloads](https://pepy.tech/badge/filelock/month)](https://pepy.tech/project/filelock/month)
+[![Downloads](https://pepy.tech/badge/filelock/month)](https://pepy.tech/project/filelock)
 [![check](https://github.com/tox-dev/py-filelock/actions/workflows/check.yml/badge.svg)](https://github.com/tox-dev/py-filelock/actions/workflows/check.yml)
 
 For more information checkout the [official documentation](https://py-filelock.readthedocs.io/en/latest/index.html).
```

