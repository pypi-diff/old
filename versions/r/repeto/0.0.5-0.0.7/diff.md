# Comparing `tmp/repeto-0.0.5.tar.gz` & `tmp/repeto-0.0.7.tar.gz`

## Comparing `repeto-0.0.5.tar` & `repeto-0.0.7.tar`

### file list

```diff
@@ -1,19 +1,19 @@
--rw-r--r--   0        0        0      523 1970-01-01 00:00:00.000000 repeto-0.0.5/local_dependencies/repeto/Cargo.toml
--rw-rw-r--   0     1001     1001       52 2023-04-04 11:36:25.000000 repeto-0.0.5/local_dependencies/repeto/src/lib.rs
--rw-rw-r--   0     1001     1001     7633 2023-04-04 13:37:39.000000 repeto-0.0.5/local_dependencies/repeto/src/optimize/dynprog.rs
--rw-rw-r--   0     1001     1001     3489 2023-04-05 12:51:08.000000 repeto-0.0.5/local_dependencies/repeto/src/optimize/index.rs
--rw-rw-r--   0     1001     1001     8276 2023-04-04 13:37:11.000000 repeto-0.0.5/local_dependencies/repeto/src/optimize/mod.rs
--rw-rw-r--   0     1001     1001     1193 2023-02-12 13:15:56.000000 repeto-0.0.5/local_dependencies/repeto/src/optimize/trace.rs
--rw-rw-r--   0     1001     1001     2306 2023-04-04 13:06:15.000000 repeto-0.0.5/local_dependencies/repeto/src/predict.rs
--rw-rw-r--   0     1001     1001     2721 2023-04-05 13:00:28.000000 repeto-0.0.5/local_dependencies/repeto/src/repeats/inv.rs
--rw-rw-r--   0     1001     1001       13 2023-04-04 12:57:47.000000 repeto-0.0.5/local_dependencies/repeto/src/repeats/mod.rs
--rw-rw-r--   0     1001     1001       94 2023-04-04 11:37:08.000000 repeto-0.0.5/local_dependencies/repeto/tests/integration_test.rs
--rw-r--r--   0        0        0      507 1970-01-01 00:00:00.000000 repeto-0.0.5/Cargo.toml
--rw-rw-r--   0     1001     1001        0 2023-04-03 14:45:29.000000 repeto-0.0.5/README.md
--rw-rw-r--   0     1001     1001      386 2023-04-05 11:20:15.000000 repeto-0.0.5/pyproject.toml
--rw-rw-r--   0     1001     1001     4209 2023-04-05 13:02:36.000000 repeto-0.0.5/repeto.pyi
--rw-rw-r--   0     1001     1001     1363 2023-04-04 15:50:52.000000 repeto-0.0.5/src/lib.rs
--rw-rw-r--   0     1001     1001     7887 2023-04-05 13:01:06.000000 repeto-0.0.5/src/repeats.rs
--rw-rw-r--   0     1001     1001     3791 2023-04-05 13:01:06.000000 repeto-0.0.5/tests/test_py_interface.py
--rw-rw-r--   0     1001     1001    13947 2023-04-05 13:19:50.000000 repeto-0.0.5/Cargo.lock
--rw-r--r--   0        0        0      488 1970-01-01 00:00:00.000000 repeto-0.0.5/PKG-INFO
+-rw-r--r--   0        0        0      523 1970-01-01 00:00:00.000000 repeto-0.0.7/local_dependencies/repeto/Cargo.toml
+-rw-rw-r--   0     1001     1001       52 2023-04-04 11:36:25.000000 repeto-0.0.7/local_dependencies/repeto/src/lib.rs
+-rw-rw-r--   0     1001     1001     7633 2023-04-04 13:37:39.000000 repeto-0.0.7/local_dependencies/repeto/src/optimize/dynprog.rs
+-rw-rw-r--   0     1001     1001     3489 2023-04-05 12:51:08.000000 repeto-0.0.7/local_dependencies/repeto/src/optimize/index.rs
+-rw-rw-r--   0     1001     1001     8276 2023-04-04 13:37:11.000000 repeto-0.0.7/local_dependencies/repeto/src/optimize/mod.rs
+-rw-rw-r--   0     1001     1001     1193 2023-02-12 13:15:56.000000 repeto-0.0.7/local_dependencies/repeto/src/optimize/trace.rs
+-rw-rw-r--   0     1001     1001     2306 2023-04-04 13:06:15.000000 repeto-0.0.7/local_dependencies/repeto/src/predict.rs
+-rw-rw-r--   0     1001     1001     2721 2023-04-05 13:00:28.000000 repeto-0.0.7/local_dependencies/repeto/src/repeats/inv.rs
+-rw-rw-r--   0     1001     1001       13 2023-04-04 12:57:47.000000 repeto-0.0.7/local_dependencies/repeto/src/repeats/mod.rs
+-rw-rw-r--   0     1001     1001      939 2023-04-05 15:50:07.000000 repeto-0.0.7/local_dependencies/repeto/tests/integration_test.rs
+-rw-r--r--   0        0        0      507 1970-01-01 00:00:00.000000 repeto-0.0.7/Cargo.toml
+-rw-rw-r--   0     1001     1001        0 2023-04-03 14:45:29.000000 repeto-0.0.7/README.md
+-rw-rw-r--   0     1001     1001      386 2023-04-05 11:20:15.000000 repeto-0.0.7/pyproject.toml
+-rw-rw-r--   0     1001     1001     4499 2023-04-07 09:41:45.000000 repeto-0.0.7/repeto.pyi
+-rw-rw-r--   0     1001     1001     1363 2023-04-04 15:50:52.000000 repeto-0.0.7/src/lib.rs
+-rw-rw-r--   0     1001     1001     8977 2023-04-07 09:20:01.000000 repeto-0.0.7/src/repeats.rs
+-rw-rw-r--   0     1001     1001     5289 2023-04-07 10:19:01.000000 repeto-0.0.7/tests/test_py_interface.py
+-rw-rw-r--   0     1001     1001    13947 2023-04-07 14:00:10.000000 repeto-0.0.7/Cargo.lock
+-rw-r--r--   0        0        0      488 1970-01-01 00:00:00.000000 repeto-0.0.7/PKG-INFO
```

### Comparing `repeto-0.0.5/local_dependencies/repeto/src/optimize/dynprog.rs` & `repeto-0.0.7/local_dependencies/repeto/src/optimize/dynprog.rs`

 * *Files identical despite different names*

### Comparing `repeto-0.0.5/local_dependencies/repeto/src/optimize/index.rs` & `repeto-0.0.7/local_dependencies/repeto/src/optimize/index.rs`

 * *Files identical despite different names*

### Comparing `repeto-0.0.5/local_dependencies/repeto/src/optimize/mod.rs` & `repeto-0.0.7/local_dependencies/repeto/src/optimize/mod.rs`

 * *Files identical despite different names*

### Comparing `repeto-0.0.5/local_dependencies/repeto/src/optimize/trace.rs` & `repeto-0.0.7/local_dependencies/repeto/src/optimize/trace.rs`

 * *Files identical despite different names*

### Comparing `repeto-0.0.5/local_dependencies/repeto/src/predict.rs` & `repeto-0.0.7/local_dependencies/repeto/src/predict.rs`

 * *Files identical despite different names*

### Comparing `repeto-0.0.5/local_dependencies/repeto/src/repeats/inv.rs` & `repeto-0.0.7/local_dependencies/repeto/src/repeats/inv.rs`

 * *Files identical despite different names*

### Comparing `repeto-0.0.5/repeto.pyi` & `repeto-0.0.7/repeto.pyi`

 * *Files 6% similar despite different names*

```diff
@@ -87,14 +87,21 @@
 
     def seqranges(self) -> List[Range]:
         """
         Ordered sequence blocks, i.e. sequence ranges, that underlay the inverted repeat.
         """
         pass
 
+    def to_bed12(self, contig: str, *args,
+                 name: str = ".", score: int = 0, strand: str = ".", color: str = "0,0,0") -> str:
+        """
+        Convert inverted repeat to a BED12 record. All arguments except the contig should be passed as kwargs
+        """
+        pass
+
     def __len__(self) -> int:
         """
         The length of inverted repeats is defined as the total number of base pairs of the underlying segments.
         """
         pass
 
     def __eq__(self, other) -> bool: ...
```

### Comparing `repeto-0.0.5/src/lib.rs` & `repeto-0.0.7/src/lib.rs`

 * *Files identical despite different names*

### Comparing `repeto-0.0.5/src/repeats.rs` & `repeto-0.0.7/src/repeats.rs`

 * *Files 8% similar despite different names*

```diff
@@ -181,14 +181,38 @@
     pub fn seqranges(&self, py: Python) -> Vec<Py<Range>> {
         chain(
             self.segments.iter().map(|x| x.borrow(py).left.clone_ref(py)),
             self.segments.iter().rev().map(|x| x.borrow(py).right.clone_ref(py)),
         ).collect()
     }
 
+    #[pyo3(
+        signature = (contig, *args, name = ".", score = 0, strand = ".", color = "0,0,0"),
+        text_signature = None
+    )]
+    pub fn to_bed12(&self, py: Python, contig: &str,
+                    args: &PyTuple, name: &str, score: u16, strand: &str, color: &str) -> String {
+        assert_eq!(args.len(), 0, "to_bed12 doesn't support positional arguments except 'contig'.");
+        assert!(score <= 1000, "Score must be from 0 to 1000");
+
+        let range = self.brange(py);
+        let (block_sizes, block_starts): (Vec<usize>, Vec<isize>) = self.seqranges(py)
+            .into_iter()
+            .map(|x| (x.borrow(py).__len__(), x.borrow(py).start - range.start))
+            .unzip();
+        let block_sizes = block_sizes.into_iter().join(",");
+        let block_starts = block_starts.into_iter().join(",");
+
+        format!(
+            "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}",
+            contig, range.start, range.end, name, score, strand, range.start, range.end, color,
+            self.segments.len() * 2, block_sizes, block_starts
+        )
+    }
+
     pub fn __len__(&self, py: Python) -> usize {
         self.segments.iter().map(|x| x.borrow(py).__len__(py)).sum()
     }
 
     pub fn __richcmp__(&self, other: &Self, op: CompareOp, py: Python<'_>) -> PyResult<PyObject> {
         Ok(match op {
             CompareOp::Eq =>
```

### Comparing `repeto-0.0.5/Cargo.lock` & `repeto-0.0.7/Cargo.lock`

 * *Files 1% similar despite different names*

```diff
@@ -25,15 +25,15 @@
 version = "1.1.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "d468802bab17cbc0cc575e9b053f41e72aa36bfa6b7f55e3529ffa43161b97fa"
 
 [[package]]
 name = "biobit-alignment"
 version = "0.0.1"
-source = "git+https://github.com/nucleohub/biobit?rev=683c0fa19460c1549f98b18fdbe6b2b8152784b3#683c0fa19460c1549f98b18fdbe6b2b8152784b3"
+source = "git+https://github.com/nucleohub/biobit?rev=725c776b3b80d0c69908ddd0d697d071712e94fc#725c776b3b80d0c69908ddd0d697d071712e94fc"
 dependencies = [
  "geo",
  "itertools",
 ]
 
 [[package]]
 name = "bitflags"
@@ -325,24 +325,24 @@
 checksum = "fb5a58c1855b4b6819d59012155603f0b22ad30cad752600aadfcb695265519a"
 dependencies = [
  "bitflags",
 ]
 
 [[package]]
 name = "repeto"
-version = "0.0.5"
+version = "0.0.7"
 dependencies = [
  "biobit-alignment",
  "derive-getters",
  "itertools",
 ]
 
 [[package]]
 name = "repeto-py"
-version = "0.0.5"
+version = "0.0.7"
 dependencies = [
  "itertools",
  "pyo3",
  "repeto",
 ]
 
 [[package]]
```

