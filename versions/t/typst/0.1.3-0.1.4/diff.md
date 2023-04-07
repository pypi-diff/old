# Comparing `tmp/typst-0.1.3.tar.gz` & `tmp/typst-0.1.4.tar.gz`

## Comparing `typst-0.1.3.tar` & `typst-0.1.4.tar`

### file list

```diff
@@ -1,23 +1,27 @@
--rw-r--r--   0        0        0      664 1970-01-01 00:00:00.000000 typst-0.1.3/Cargo.toml
--rw-r--r--   0     1001      123     2752 2023-04-05 03:40:52.000000 typst-0.1.3/.github/workflows/CI.yml
--rw-r--r--   0     1001      123      685 2023-04-05 03:40:52.000000 typst-0.1.3/.gitignore
--rw-r--r--   0     1001      123     9723 2023-04-05 03:40:52.000000 typst-0.1.3/LICENSE
--rw-r--r--   0     1001      123      766 2023-04-05 03:40:52.000000 typst-0.1.3/README.md
--rw-r--r--   0     1001      123      421 2023-04-05 03:40:52.000000 typst-0.1.3/pyproject.toml
--rw-r--r--   0     1001      123       74 2023-04-05 03:40:52.000000 typst-0.1.3/python/typst/__init__.py
--rw-r--r--   0     1001      123      483 2023-04-05 03:40:52.000000 typst-0.1.3/python/typst/__init__.pyi
--rw-r--r--   0     1001      123   331992 2023-04-05 03:40:52.000000 typst-0.1.3/python/typst/fonts/DejaVuSansMono-Bold.ttf
--rw-r--r--   0     1001      123   253580 2023-04-05 03:40:52.000000 typst-0.1.3/python/typst/fonts/DejaVuSansMono-BoldOblique.ttf
--rw-r--r--   0     1001      123   251932 2023-04-05 03:40:52.000000 typst-0.1.3/python/typst/fonts/DejaVuSansMono-Oblique.ttf
--rw-r--r--   0     1001      123   340712 2023-04-05 03:40:52.000000 typst-0.1.3/python/typst/fonts/DejaVuSansMono.ttf
--rw-r--r--   0     1001      123   806856 2023-04-05 03:40:52.000000 typst-0.1.3/python/typst/fonts/LinLibertine_R.ttf
--rw-r--r--   0     1001      123   748600 2023-04-05 03:40:52.000000 typst-0.1.3/python/typst/fonts/LinLibertine_RB.ttf
--rw-r--r--   0     1001      123   533532 2023-04-05 03:40:52.000000 typst-0.1.3/python/typst/fonts/LinLibertine_RBI.ttf
--rw-r--r--   0     1001      123   721340 2023-04-05 03:40:52.000000 typst-0.1.3/python/typst/fonts/LinLibertine_RI.ttf
--rw-r--r--   0     1001      123  2161432 2023-04-05 03:40:52.000000 typst-0.1.3/python/typst/fonts/NewCMMath-Book.otf
--rw-r--r--   0     1001      123  1229208 2023-04-05 03:40:52.000000 typst-0.1.3/python/typst/fonts/NewCMMath-Regular.otf
--rw-r--r--   0     1001      123        1 2023-04-05 03:40:52.000000 typst-0.1.3/python/typst/py.typed
--rw-r--r--   0     1001      123     9407 2023-04-05 03:40:52.000000 typst-0.1.3/src/compiler.rs
--rw-r--r--   0     1001      123     3946 2023-04-05 03:40:52.000000 typst-0.1.3/src/lib.rs
--rw-r--r--   0     1001      123    38843 2023-04-05 03:40:52.000000 typst-0.1.3/Cargo.lock
--rw-r--r--   0        0        0     1228 1970-01-01 00:00:00.000000 typst-0.1.3/PKG-INFO
+-rw-r--r--   0        0        0      668 1970-01-01 00:00:00.000000 typst-0.1.4/Cargo.toml
+-rw-r--r--   0     1001      123     2752 2023-04-07 08:16:41.000000 typst-0.1.4/.github/workflows/CI.yml
+-rw-r--r--   0     1001      123      685 2023-04-07 08:16:41.000000 typst-0.1.4/.gitignore
+-rw-r--r--   0     1001      123     9723 2023-04-07 08:16:41.000000 typst-0.1.4/LICENSE
+-rw-r--r--   0     1001      123      766 2023-04-07 08:16:41.000000 typst-0.1.4/README.md
+-rw-r--r--   0     1001      123      421 2023-04-07 08:16:41.000000 typst-0.1.4/pyproject.toml
+-rw-r--r--   0     1001      123       74 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/__init__.py
+-rw-r--r--   0     1001      123      483 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/__init__.pyi
+-rw-r--r--   0     1001      123   331992 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/fonts/DejaVuSansMono-Bold.ttf
+-rw-r--r--   0     1001      123   253580 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/fonts/DejaVuSansMono-BoldOblique.ttf
+-rw-r--r--   0     1001      123   251932 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/fonts/DejaVuSansMono-Oblique.ttf
+-rw-r--r--   0     1001      123   340712 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/fonts/DejaVuSansMono.ttf
+-rw-r--r--   0     1001      123   806856 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/fonts/LinLibertine_R.ttf
+-rw-r--r--   0     1001      123   748600 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/fonts/LinLibertine_RB.ttf
+-rw-r--r--   0     1001      123   533532 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/fonts/LinLibertine_RBI.ttf
+-rw-r--r--   0     1001      123   721340 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/fonts/LinLibertine_RI.ttf
+-rw-r--r--   0     1001      123   499128 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/fonts/NewCM10-Bold.otf
+-rw-r--r--   0     1001      123   445800 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/fonts/NewCM10-BoldItalic.otf
+-rw-r--r--   0     1001      123   464808 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/fonts/NewCM10-Italic.otf
+-rw-r--r--   0     1001      123   547508 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/fonts/NewCM10-Regular.otf
+-rw-r--r--   0     1001      123  2161432 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/fonts/NewCMMath-Book.otf
+-rw-r--r--   0     1001      123  1229208 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/fonts/NewCMMath-Regular.otf
+-rw-r--r--   0     1001      123        1 2023-04-07 08:16:41.000000 typst-0.1.4/python/typst/py.typed
+-rw-r--r--   0     1001      123     9415 2023-04-07 08:16:41.000000 typst-0.1.4/src/compiler.rs
+-rw-r--r--   0     1001      123     3946 2023-04-07 08:16:41.000000 typst-0.1.4/src/lib.rs
+-rw-r--r--   0     1001      123    38849 2023-04-07 08:16:41.000000 typst-0.1.4/Cargo.lock
+-rw-r--r--   0        0        0     1228 1970-01-01 00:00:00.000000 typst-0.1.4/PKG-INFO
```

### Comparing `typst-0.1.3/Cargo.toml` & `typst-0.1.4/Cargo.toml`

 * *Files 21% similar despite different names*

```diff
@@ -1,24 +1,24 @@
 [package]
 name = "typst-py"
-version = "0.1.3"
+version = "0.1.4"
 edition = "2021"
 description = "Python binding to typst"
 license = "Apache-2.0"
 repository = "https://github.com/messense/typst-py"
 readme = "README.md"
 
 # See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html
 [lib]
 crate-type = ["cdylib"]
 
 [dependencies]
 pyo3 = { version = "0.18.1", features = ["abi3-py37"] }
-typst = { git = "https://github.com/typst/typst.git", tag = "v0.1" }
-typst-library = { git = "https://github.com/typst/typst.git", tag = "v0.1" }
+typst = { git = "https://github.com/typst/typst.git", tag = "v0.1.0" }
+typst-library = { git = "https://github.com/typst/typst.git", tag = "v0.1.0" }
 comemo = "0.2"
 dirs = "5"
 elsa = "1.7"
 memmap2 = "0.5"
 once_cell = "1"
 same-file = "1"
 siphasher = "0.3"
```

### Comparing `typst-0.1.3/.github/workflows/CI.yml` & `typst-0.1.4/.github/workflows/CI.yml`

 * *Files identical despite different names*

### Comparing `typst-0.1.3/.gitignore` & `typst-0.1.4/.gitignore`

 * *Files identical despite different names*

### Comparing `typst-0.1.3/LICENSE` & `typst-0.1.4/LICENSE`

 * *Files identical despite different names*

### Comparing `typst-0.1.3/README.md` & `typst-0.1.4/README.md`

 * *Files identical despite different names*

### Comparing `typst-0.1.3/python/typst/fonts/DejaVuSansMono-Bold.ttf` & `typst-0.1.4/python/typst/fonts/DejaVuSansMono-Bold.ttf`

 * *Files identical despite different names*

### Comparing `typst-0.1.3/python/typst/fonts/DejaVuSansMono-BoldOblique.ttf` & `typst-0.1.4/python/typst/fonts/DejaVuSansMono-BoldOblique.ttf`

 * *Files identical despite different names*

### Comparing `typst-0.1.3/python/typst/fonts/DejaVuSansMono-Oblique.ttf` & `typst-0.1.4/python/typst/fonts/DejaVuSansMono-Oblique.ttf`

 * *Files identical despite different names*

### Comparing `typst-0.1.3/python/typst/fonts/DejaVuSansMono.ttf` & `typst-0.1.4/python/typst/fonts/DejaVuSansMono.ttf`

 * *Files identical despite different names*

### Comparing `typst-0.1.3/python/typst/fonts/LinLibertine_R.ttf` & `typst-0.1.4/python/typst/fonts/LinLibertine_R.ttf`

 * *Files identical despite different names*

### Comparing `typst-0.1.3/python/typst/fonts/LinLibertine_RB.ttf` & `typst-0.1.4/python/typst/fonts/LinLibertine_RB.ttf`

 * *Files identical despite different names*

### Comparing `typst-0.1.3/python/typst/fonts/LinLibertine_RBI.ttf` & `typst-0.1.4/python/typst/fonts/LinLibertine_RBI.ttf`

 * *Files identical despite different names*

### Comparing `typst-0.1.3/python/typst/fonts/LinLibertine_RI.ttf` & `typst-0.1.4/python/typst/fonts/LinLibertine_RI.ttf`

 * *Files identical despite different names*

### Comparing `typst-0.1.3/python/typst/fonts/NewCMMath-Book.otf` & `typst-0.1.4/python/typst/fonts/NewCMMath-Book.otf`

 * *Files identical despite different names*

### Comparing `typst-0.1.3/python/typst/fonts/NewCMMath-Regular.otf` & `typst-0.1.4/python/typst/fonts/NewCMMath-Regular.otf`

 * *Files identical despite different names*

### Comparing `typst-0.1.3/src/compiler.rs` & `typst-0.1.4/src/compiler.rs`

 * *Files 4% similar despite different names*

```diff
@@ -236,22 +236,24 @@
     /// Search for fonts in the macOS system font directories.
     #[cfg(target_os = "macos")]
     fn search_system(&mut self) {
         self.search_dir("/Library/Fonts");
         self.search_dir("/System/Library/Fonts");
 
         // Downloadable fonts, location varies on major macOS releases
-        for entry in walkdir::WalkDir::new("/System/Library/AssetsV2").max_depth(1) {
-            let Ok(entry) = entry else { continue };
-            let Some(filename) = entry.path().file_name() else { continue };
-            if filename
-                .to_string_lossy()
-                .starts_with("com_apple_MobileAsset_Font")
-            {
-                self.search_dir(entry.path());
+        if let Ok(dir) = fs::read_dir("/System/Library/AssetsV2") {
+            for entry in dir {
+                let Ok(entry) = entry else { continue };
+                if entry
+                    .file_name()
+                    .to_string_lossy()
+                    .starts_with("com_apple_MobileAsset_Font")
+                {
+                    self.search_dir(entry.path());
+                }
             }
         }
 
         self.search_dir("/Network/Library/Fonts");
 
         if let Some(dir) = dirs::font_dir() {
             self.search_dir(dir);
```

### Comparing `typst-0.1.3/src/lib.rs` & `typst-0.1.4/src/lib.rs`

 * *Files identical despite different names*

### Comparing `typst-0.1.3/Cargo.lock` & `typst-0.1.4/Cargo.lock`

 * *Files 0% similar despite different names*

```diff
@@ -220,17 +220,17 @@
 name = "ecow"
 version = "0.1.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "e60e2840fbfc397c7972b11a6e6bd99a0248921cc1e31f293c5f6c5ac24831da"
 
 [[package]]
 name = "elsa"
-version = "1.8.0"
+version = "1.8.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "f74077c3c3aedb99a2683919698285596662518ea13e5eedcf8bdd43b0d0453b"
+checksum = "b5e0aca8dce8856e420195bd13b6a64de3334235ccc9214e824b86b12bf26283"
 dependencies = [
  "stable_deref_trait",
 ]
 
 [[package]]
 name = "fancy-regex"
 version = "0.7.1"
@@ -270,17 +270,17 @@
 checksum = "a9c384f161156f5260c24a097c56119f9be8c798586aecc13afbcbe7b7e26bf8"
 dependencies = [
  "percent-encoding",
 ]
 
 [[package]]
 name = "getrandom"
-version = "0.2.8"
+version = "0.2.9"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "c05aeb6a22b8f62540c194aac980f2115af067bfe15a0734d7277a768d396b31"
+checksum = "c85e1d9ab2eadba7e5040d4e09cbd6d072b76a557ad64e797c2cb9d4da21d7e4"
 dependencies = [
  "cfg-if",
  "libc",
  "wasi",
 ]
 
 [[package]]
@@ -1142,15 +1142,15 @@
 version = "2.0.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "6af6ae20167a9ece4bcb41af5b80f8a1f1df981f6391189ce00fd257af04126a"
 
 [[package]]
 name = "typst"
 version = "0.1.0"
-source = "git+https://github.com/typst/typst.git?tag=v0.1#b3faef4b80a674294091066e20501e3a5d0f6103"
+source = "git+https://github.com/typst/typst.git?tag=v0.1.0#b3faef4b80a674294091066e20501e3a5d0f6103"
 dependencies = [
  "bitflags",
  "bytemuck",
  "comemo",
  "ecow",
  "flate2",
  "if_chain",
@@ -1179,15 +1179,15 @@
  "usvg",
  "xmp-writer",
 ]
 
 [[package]]
 name = "typst-library"
 version = "0.1.0"
-source = "git+https://github.com/typst/typst.git?tag=v0.1#b3faef4b80a674294091066e20501e3a5d0f6103"
+source = "git+https://github.com/typst/typst.git?tag=v0.1.0#b3faef4b80a674294091066e20501e3a5d0f6103"
 dependencies = [
  "comemo",
  "csv",
  "ecow",
  "hayagriva",
  "hypher",
  "kurbo",
@@ -1209,26 +1209,26 @@
  "unicode-segmentation",
  "xi-unicode",
 ]
 
 [[package]]
 name = "typst-macros"
 version = "0.1.0"
-source = "git+https://github.com/typst/typst.git?tag=v0.1#b3faef4b80a674294091066e20501e3a5d0f6103"
+source = "git+https://github.com/typst/typst.git?tag=v0.1.0#b3faef4b80a674294091066e20501e3a5d0f6103"
 dependencies = [
  "heck",
  "proc-macro2",
  "quote",
  "syn 1.0.109",
  "unscanny",
 ]
 
 [[package]]
 name = "typst-py"
-version = "0.1.3"
+version = "0.1.4"
 dependencies = [
  "comemo",
  "dirs",
  "elsa",
  "memmap2",
  "once_cell",
  "pyo3",
```

### Comparing `typst-0.1.3/PKG-INFO` & `typst-0.1.4/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: typst
-Version: 0.1.3
+Version: 0.1.4
 Classifier: Programming Language :: Rust
 Classifier: Programming Language :: Python :: Implementation :: CPython
 Classifier: Programming Language :: Python :: Implementation :: PyPy
 License-File: LICENSE
 Summary: Python binding to typst
 License: Apache-2.0
 Requires-Python: >=3.7
```

