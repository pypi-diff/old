# Comparing `tmp/pysqlx_core-0.1.8a0.tar.gz` & `tmp/pysqlx_core-0.1.9.tar.gz`

## Comparing `pysqlx_core-0.1.8a0.tar` & `pysqlx_core-0.1.9.tar`

### file list

```diff
@@ -1,20 +1,20 @@
--rw-r--r--   0        0        0      450 1970-01-01 00:00:00.000000 pysqlx_core-0.1.8a0/local_dependencies/py_types/Cargo.toml
--rw-r--r--   0     1001      121     2950 2022-10-22 18:18:07.000000 pysqlx_core-0.1.8a0/local_dependencies/py_types/src/errors.rs
--rw-r--r--   0     1001      121      181 2022-10-22 18:18:07.000000 pysqlx_core-0.1.8a0/local_dependencies/py_types/src/lib.rs
--rw-r--r--   0     1001      121     1901 2022-10-22 18:18:07.000000 pysqlx_core-0.1.8a0/local_dependencies/py_types/src/rows.rs
--rw-r--r--   0     1001      121     3429 2022-10-22 18:18:07.000000 pysqlx_core-0.1.8a0/local_dependencies/py_types/src/types.rs
--rw-r--r--   0        0        0      346 1970-01-01 00:00:00.000000 pysqlx_core-0.1.8a0/local_dependencies/convert/Cargo.toml
--rw-r--r--   0     1001      121     1356 2022-10-22 18:18:07.000000 pysqlx_core-0.1.8a0/local_dependencies/convert/src/columns.rs
--rw-r--r--   0     1001      121      100 2022-10-22 18:18:07.000000 pysqlx_core-0.1.8a0/local_dependencies/convert/src/lib.rs
--rw-r--r--   0     1001      121     1217 2022-10-22 18:18:07.000000 pysqlx_core-0.1.8a0/local_dependencies/convert/src/rows.rs
--rw-r--r--   0        0        0      844 1970-01-01 00:00:00.000000 pysqlx_core-0.1.8a0/local_dependencies/database/Cargo.toml
--rw-r--r--   0     1001      121     3343 2022-10-22 18:18:07.000000 pysqlx_core-0.1.8a0/local_dependencies/database/src/conn.rs
--rw-r--r--   0     1001      121       37 2022-10-22 18:18:07.000000 pysqlx_core-0.1.8a0/local_dependencies/database/src/lib.rs
--rw-r--r--   0        0        0      757 1970-01-01 00:00:00.000000 pysqlx_core-0.1.8a0/Cargo.toml
--rw-r--r--   0     1001      121     1080 2022-10-22 18:18:07.000000 pysqlx_core-0.1.8a0/LICENSE
--rw-r--r--   0     1001      121     1371 2022-10-22 18:18:07.000000 pysqlx_core-0.1.8a0/README.md
--rw-r--r--   0     1001      121     2495 2022-10-22 18:18:07.000000 pysqlx_core-0.1.8a0/pyproject.toml
--rw-r--r--   0     1001      121     3365 2022-10-22 18:18:07.000000 pysqlx_core-0.1.8a0/pysqlx_core.pyi
--rw-r--r--   0     1001      121     1193 2022-10-22 18:18:07.000000 pysqlx_core-0.1.8a0/src/lib.rs
--rw-r--r--   0     1001      121    61042 2022-10-22 18:18:07.000000 pysqlx_core-0.1.8a0/Cargo.lock
--rw-r--r--   0        0        0     3282 1970-01-01 00:00:00.000000 pysqlx_core-0.1.8a0/PKG-INFO
+-rw-r--r--   0        0        0      450 1970-01-01 00:00:00.000000 pysqlx_core-0.1.9/local_dependencies/py_types/Cargo.toml
+-rw-r--r--   0     1001      121     2950 2022-10-22 18:49:15.000000 pysqlx_core-0.1.9/local_dependencies/py_types/src/errors.rs
+-rw-r--r--   0     1001      121      181 2022-10-22 18:49:15.000000 pysqlx_core-0.1.9/local_dependencies/py_types/src/lib.rs
+-rw-r--r--   0     1001      121     1901 2022-10-22 18:49:15.000000 pysqlx_core-0.1.9/local_dependencies/py_types/src/rows.rs
+-rw-r--r--   0     1001      121     3429 2022-10-22 18:49:15.000000 pysqlx_core-0.1.9/local_dependencies/py_types/src/types.rs
+-rw-r--r--   0        0        0      346 1970-01-01 00:00:00.000000 pysqlx_core-0.1.9/local_dependencies/convert/Cargo.toml
+-rw-r--r--   0     1001      121     1356 2022-10-22 18:49:15.000000 pysqlx_core-0.1.9/local_dependencies/convert/src/columns.rs
+-rw-r--r--   0     1001      121      100 2022-10-22 18:49:15.000000 pysqlx_core-0.1.9/local_dependencies/convert/src/lib.rs
+-rw-r--r--   0     1001      121     1217 2022-10-22 18:49:15.000000 pysqlx_core-0.1.9/local_dependencies/convert/src/rows.rs
+-rw-r--r--   0        0        0      844 1970-01-01 00:00:00.000000 pysqlx_core-0.1.9/local_dependencies/database/Cargo.toml
+-rw-r--r--   0     1001      121     3343 2022-10-22 18:49:15.000000 pysqlx_core-0.1.9/local_dependencies/database/src/conn.rs
+-rw-r--r--   0     1001      121       37 2022-10-22 18:49:15.000000 pysqlx_core-0.1.9/local_dependencies/database/src/lib.rs
+-rw-r--r--   0        0        0      751 1970-01-01 00:00:00.000000 pysqlx_core-0.1.9/Cargo.toml
+-rw-r--r--   0     1001      121     1080 2022-10-22 18:49:15.000000 pysqlx_core-0.1.9/LICENSE
+-rw-r--r--   0     1001      121     1465 2022-10-22 18:49:15.000000 pysqlx_core-0.1.9/README.md
+-rw-r--r--   0     1001      121     2624 2022-10-22 18:49:15.000000 pysqlx_core-0.1.9/pyproject.toml
+-rw-r--r--   0     1001      121     3365 2022-10-22 18:49:15.000000 pysqlx_core-0.1.9/pysqlx_core.pyi
+-rw-r--r--   0     1001      121     1193 2022-10-22 18:49:15.000000 pysqlx_core-0.1.9/src/lib.rs
+-rw-r--r--   0     1001      121    61036 2022-10-22 18:49:15.000000 pysqlx_core-0.1.9/Cargo.lock
+-rw-r--r--   0        0        0     3495 1970-01-01 00:00:00.000000 pysqlx_core-0.1.9/PKG-INFO
```

### Comparing `pysqlx_core-0.1.8a0/local_dependencies/py_types/src/errors.rs` & `pysqlx_core-0.1.9/local_dependencies/py_types/src/errors.rs`

 * *Files identical despite different names*

### Comparing `pysqlx_core-0.1.8a0/local_dependencies/py_types/src/rows.rs` & `pysqlx_core-0.1.9/local_dependencies/py_types/src/rows.rs`

 * *Files identical despite different names*

### Comparing `pysqlx_core-0.1.8a0/local_dependencies/py_types/src/types.rs` & `pysqlx_core-0.1.9/local_dependencies/py_types/src/types.rs`

 * *Files identical despite different names*

### Comparing `pysqlx_core-0.1.8a0/local_dependencies/convert/src/columns.rs` & `pysqlx_core-0.1.9/local_dependencies/convert/src/columns.rs`

 * *Files identical despite different names*

### Comparing `pysqlx_core-0.1.8a0/local_dependencies/convert/src/rows.rs` & `pysqlx_core-0.1.9/local_dependencies/convert/src/rows.rs`

 * *Files identical despite different names*

### Comparing `pysqlx_core-0.1.8a0/local_dependencies/database/Cargo.toml` & `pysqlx_core-0.1.9/local_dependencies/database/Cargo.toml`

 * *Files identical despite different names*

### Comparing `pysqlx_core-0.1.8a0/local_dependencies/database/src/conn.rs` & `pysqlx_core-0.1.9/local_dependencies/database/src/conn.rs`

 * *Files identical despite different names*

### Comparing `pysqlx_core-0.1.8a0/LICENSE` & `pysqlx_core-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `pysqlx_core-0.1.8a0/README.md` & `pysqlx_core-0.1.9/README.md`

 * *Files 5% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 # pysqlx-core
 
+pysqlx-core is an extremely fast Python library for communicating with various SQL databases.
 
 This package provides the core functionality for PySQLX-Engine.
 
 The package is currently a work in progress and subject to significant change.
 
 __pysqlx-core__ will be a separate package, required by `pysqlx-engine`.
```

### Comparing `pysqlx_core-0.1.8a0/pyproject.toml` & `pysqlx_core-0.1.9/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -40,14 +40,16 @@
     "Framework :: Flask",
     "Framework :: IPython",
 ]
 
 dynamic = ["version", "license", "readme", "description"]
 keywords = ["async", "database", "sql", "faster", "pysqlx"]
 
+description = "A fast and async SQL database wrapper for Python, with support for MySQL, PostgreSQL, SQLite and MS SQL Server."
+
 [project.urls]
 Homepage = "https://github.com/carlos-rian/pysqlx-core"
 Source = "https://github.com/carlos-rian/pysqlx-core"
 
 
 [tool.maturin]
 bindings = "pyo3"
```

### Comparing `pysqlx_core-0.1.8a0/pysqlx_core.pyi` & `pysqlx_core-0.1.9/pysqlx_core.pyi`

 * *Files identical despite different names*

### Comparing `pysqlx_core-0.1.8a0/src/lib.rs` & `pysqlx_core-0.1.9/src/lib.rs`

 * *Files identical despite different names*

### Comparing `pysqlx_core-0.1.8a0/Cargo.lock` & `pysqlx_core-0.1.9/Cargo.lock`

 * *Files 0% similar despite different names*

```diff
@@ -1562,15 +1562,15 @@
  "proc-macro2",
  "quote",
  "syn",
 ]
 
 [[package]]
 name = "pysqlx-core"
-version = "0.1.8-alpha"
+version = "0.1.9"
 dependencies = [
  "convert",
  "database",
  "py_types",
  "pyo3",
  "pyo3-asyncio",
 ]
```

### Comparing `pysqlx_core-0.1.8a0/PKG-INFO` & `pysqlx_core-0.1.9/PKG-INFO`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pysqlx-core
-Version: 0.1.8a0
+Version: 0.1.9
 Classifier: Development Status :: 3 - Alpha
 Classifier: Programming Language :: Rust
 Classifier: Programming Language :: Python :: Implementation :: CPython
 Classifier: Programming Language :: Python :: Implementation :: PyPy
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3 :: Only
@@ -30,23 +30,25 @@
 Classifier: Typing :: Typed
 Classifier: Framework :: AsyncIO
 Classifier: Framework :: AnyIO
 Classifier: Framework :: FastAPI
 Classifier: Framework :: Flask
 Classifier: Framework :: IPython
 License-File: LICENSE
+Summary: A fast and async SQL database wrapper for Python, with support for MySQL, PostgreSQL, SQLite and MS SQL Server.
 Keywords: async,database,sql,faster,pysqlx
 Author-email: Carlos Rian <crian.rian@gmail.com>
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown; charset=UTF-8; variant=GFM
-Project-URL: Homepage, https://github.com/carlos-rian/pysqlx-core
 Project-URL: Source, https://github.com/carlos-rian/pysqlx-core
+Project-URL: Homepage, https://github.com/carlos-rian/pysqlx-core
 
 # pysqlx-core
 
+pysqlx-core is an extremely fast Python library for communicating with various SQL databases.
 
 This package provides the core functionality for PySQLX-Engine.
 
 The package is currently a work in progress and subject to significant change.
 
 __pysqlx-core__ will be a separate package, required by `pysqlx-engine`.
```

