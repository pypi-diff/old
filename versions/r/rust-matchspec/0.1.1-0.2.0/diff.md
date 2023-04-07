# Comparing `tmp/rust_matchspec-0.1.1.tar.gz` & `tmp/rust_matchspec-0.2.0.tar.gz`

## Comparing `rust_matchspec-0.1.1.tar` & `rust_matchspec-0.2.0.tar`

### file list

```diff
@@ -1,22 +1,25 @@
--rw-r--r--   0        0        0      558 1970-01-01 00:00:00.000000 rust_matchspec-0.1.1/Cargo.toml
--rw-r--r--   0     1001      123     2770 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/.github/workflows/maturin-build.yml
--rw-r--r--   0     1001      123      580 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/.github/workflows/rust.yml
--rw-r--r--   0     1001      123       52 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/.gitignore
--rw-r--r--   0     1001      123     1522 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/LICENSE
--rw-r--r--   0     1001      123     2310 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/README.md
--rw-r--r--   0     1001      123     1624 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/benches/parsing.rs
--rw-r--r--   0     1001      123      268 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/pyproject.toml
--rw-r--r--   0     1001      123       89 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/python/rust_matchspec/__init__.py
--rw-r--r--   0     1001      123      345 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/recipe/bld.bat
--rw-r--r--   0     1001      123      369 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/recipe/build.sh
--rw-r--r--   0     1001      123      508 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/recipe/meta.yaml
--rw-r--r--   0     1001      123      318 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/src/error.rs
--rw-r--r--   0     1001      123     3406 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/src/input_table.rs
--rw-r--r--   0     1001      123      206 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/src/lib.rs
--rw-r--r--   0     1001      123    18997 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/src/matchspec.rs
--rw-r--r--   0     1001      123     1793 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/src/package_candidate.rs
--rw-r--r--   0     1001      123    19771 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/src/parsers.rs
--rw-r--r--   0     1001      123      577 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/src/python.rs
--rw-r--r--   0     1001      123  3033732 2023-04-03 22:57:25.000000 rust_matchspec-0.1.1/test_data/linux_64-depends.txt
--rw-r--r--   0     1001      123    20901 2023-04-03 22:58:38.000000 rust_matchspec-0.1.1/Cargo.lock
--rw-r--r--   0        0        0     2526 1970-01-01 00:00:00.000000 rust_matchspec-0.1.1/PKG-INFO
+-rw-r--r--   0        0        0      566 1970-01-01 00:00:00.000000 rust_matchspec-0.2.0/Cargo.toml
+-rw-r--r--   0     1001      123     2770 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/.github/workflows/maturin-build.yml
+-rw-r--r--   0     1001      123      580 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/.github/workflows/rust.yml
+-rw-r--r--   0     1001      123       60 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/.gitignore
+-rw-r--r--   0     1001      123     1522 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/LICENSE
+-rw-r--r--   0     1001      123     4100 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/README.md
+-rw-r--r--   0     1001      123     1592 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/benches/parsing.rs
+-rw-r--r--   0     1001      123     2587 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/benches/test_python.py
+-rw-r--r--   0     1001      123      104 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/environment.yml
+-rw-r--r--   0     1001      123      453 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/pyproject.toml
+-rw-r--r--   0     1001      123       81 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/python/rust_matchspec/__init__.py
+-rw-r--r--   0     1001      123      345 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/recipe/bld.bat
+-rw-r--r--   0     1001      123      369 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/recipe/build.sh
+-rw-r--r--   0     1001      123      508 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/recipe/meta.yaml
+-rw-r--r--   0     1001      123      317 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/src/error.rs
+-rw-r--r--   0     1001      123     3406 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/src/input_table.rs
+-rw-r--r--   0     1001      123      179 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/src/lib.rs
+-rw-r--r--   0     1001      123    18548 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/src/matchspec.rs
+-rw-r--r--   0     1001      123     4307 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/src/package_candidate.rs
+-rw-r--r--   0     1001      123    19616 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/src/parsers.rs
+-rw-r--r--   0     1001      123     2066 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/src/python.rs
+-rw-r--r--   0     1001      123  3033732 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/test_data/linux_64-depends.txt
+-rw-r--r--   0     1001      123 39921865 2023-04-07 03:55:09.000000 rust_matchspec-0.2.0/test_data/repodata-linux-64.json
+-rw-r--r--   0     1001      123    20901 2023-04-07 03:56:21.000000 rust_matchspec-0.2.0/Cargo.lock
+-rw-r--r--   0        0        0     4498 1970-01-01 00:00:00.000000 rust_matchspec-0.2.0/PKG-INFO
```

### Comparing `rust_matchspec-0.1.1/Cargo.toml` & `rust_matchspec-0.2.0/Cargo.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [package]
 name = "matchspec"
-version = "0.1.1"
+version = "0.2.0"
 edition = "2021"
 
 [lib]
 # This is the python target
 name = "rust_matchspec"
 crate-type = ["lib", "cdylib"]
 
@@ -16,13 +16,13 @@
 serde_json = "1.0"
 version-compare = "0.1"
 
 [dev-dependencies]
 criterion = "0.3"
 
 [features]
-default = []
+default = ["python"]
 python = ["pyo3/extension-module"]
 
 [[bench]]
 name = "parsing"
 harness = false
```

### Comparing `rust_matchspec-0.1.1/.github/workflows/maturin-build.yml` & `rust_matchspec-0.2.0/.github/workflows/maturin-build.yml`

 * *Files identical despite different names*

### Comparing `rust_matchspec-0.1.1/.github/workflows/rust.yml` & `rust_matchspec-0.2.0/.github/workflows/rust.yml`

 * *Files identical despite different names*

### Comparing `rust_matchspec-0.1.1/LICENSE` & `rust_matchspec-0.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `rust_matchspec-0.1.1/benches/parsing.rs` & `rust_matchspec-0.2.0/benches/parsing.rs`

 * *Files 9% similar despite different names*

```diff
@@ -3,28 +3,28 @@
 use std::fs::File;
 use std::io::{BufRead, BufReader};
 
 fn criterion_benchmark(c: &mut Criterion) {
     c.bench_function("Package name only", |b| {
         b.iter(|| {
             // This is a complex but not unlikely matchspec
-            black_box("tzdata").parse::<MatchSpec<String>>()
+            black_box("tzdata").parse::<MatchSpec>()
         })
     });
     c.bench_function("Package name and version", |b| {
         b.iter(|| {
             // This is a complex but not unlikely matchspec
-            black_box("openssl>1.1.1g").parse::<MatchSpec<String>>()
+            black_box("openssl>1.1.1g").parse::<MatchSpec>()
         })
     });
     c.bench_function("All possible matchers", |b| {
         b.iter(|| {
             // This is a complex but not unlikely matchspec
             black_box("conda-forge/linux-64:NAMESPACE:tensorflow>=1.9.2[license=\"GPL\", subdir=\"linux-64\"]")
-                .parse::<MatchSpec<String>>()
+                .parse::<MatchSpec>()
         })
     });
 
     c.bench_function("Repodata depends", |b| {
         let depends_file = format!(
             "{}/test_data/linux_64-depends.txt",
             env!("CARGO_MANIFEST_DIR")
@@ -33,15 +33,15 @@
             BufReader::new(File::open(depends_file).expect("opening repodata depends file"));
         let depends: Vec<String> = repodata_depends_buffer
             .lines()
             .map(|l| l.unwrap())
             .collect();
         b.iter(|| {
             for d in &depends {
-                d.parse::<MatchSpec<String>>().unwrap();
+                d.parse::<MatchSpec>().unwrap();
             }
         })
     });
 }
 
 criterion_group!(benches, criterion_benchmark);
 criterion_main!(benches);
```

### Comparing `rust_matchspec-0.1.1/src/input_table.rs` & `rust_matchspec-0.2.0/src/input_table.rs`

 * *Files identical despite different names*

### Comparing `rust_matchspec-0.1.1/src/matchspec.rs` & `rust_matchspec-0.2.0/src/matchspec.rs`

 * *Files 8% similar despite different names*

```diff
@@ -1,25 +1,26 @@
-use crate::parsers::*;
-use crate::package_candidate::*;
+use crate::error::MatchSpecError;
 use crate::input_table::*;
+use crate::package_candidate::*;
+use crate::parsers::*;
 use nom::branch::alt;
 use nom::error::Error as NomError;
 use nom::Finish;
+use pyo3::prelude::*;
 use std::fmt::Debug;
 use std::str::FromStr;
 use version_compare::{compare_to, Cmp};
-use crate::error::MatchSpecError;
 
 /// Matches a string with a string (possibly) containing globs
 fn is_match_glob_str(glob_str: &str, match_str: &str) -> bool {
     let mut index: Option<usize> = Some(0);
-    let mut it = glob_str.split("*").peekable();
+    let mut it = glob_str.split('*').peekable();
     while let Some(part) = it.next() {
         index = match_str.get(index.unwrap()..).and_then(|s| s.find(part));
-        if index == None || (it.peek().is_none() && !match_str.ends_with(part)) {
+        if index.is_none() || (it.peek().is_none() && !match_str.ends_with(part)) {
             return false;
         }
     }
     true
 }
 
 /// Enum that is used for representating the selector types.
@@ -30,16 +31,16 @@
     LessThan,
     LessThanOrEqualTo,
     NotEqualTo,
     EqualTo,
 }
 
 impl<S> From<S> for Selector
-    where
-        S: AsRef<str>,
+where
+    S: AsRef<str>,
 {
     fn from(value: S) -> Self {
         match value.as_ref() {
             ">" => Self::GreaterThan,
             ">=" => Self::GreaterThanOrEqualTo,
             "<" => Self::LessThan,
             "<=" => Self::LessThanOrEqualTo,
@@ -84,16 +85,16 @@
 /// CompoundSelector is a grouping of selector and version pairs. For example, in these MatchSpecs:
 /// ```text
 ///  gcc>9|!=10.0.1 # GCC must be greater than 9.* OR not 10.0.1
 ///  python>=3.0.0,<3.7.2 # Python must be greater than or equal to 3.0.0 AND less than 3.7.2
 /// ```
 #[derive(Clone, Debug, PartialEq, Eq)]
 pub enum CompoundSelector<S>
-    where
-        S: Into<String> + AsRef<str>,
+where
+    S: Into<String> + AsRef<str>,
 {
     Single {
         selector: Selector,
         version: S,
     },
     And {
         first_selector: Selector,
@@ -125,45 +126,43 @@
 /// let cs = CompoundSelector::from((">", "1.1.1"));
 /// assert_eq!(cs, CompoundSelector::Single{
 ///     selector: Selector::GreaterThan,
 ///     version: "1.1.1".to_string(),
 /// });
 /// ```
 impl<S, V> From<(S, V)> for CompoundSelector<String>
-    where
-        S: Into<Selector>,
-        V: Into<String>,
+where
+    S: Into<Selector>,
+    V: Into<String>,
 {
     fn from(input: (S, V)) -> Self {
         CompoundSelector::Single {
             selector: input.0.into(),
             version: input.1.into(),
         }
     }
 }
 
-
 impl<S, V> From<((S, V), char, (S, V))> for CompoundSelector<String>
-    where
-        S: Into<Selector>,
-        V: Into<String>,
+where
+    S: Into<Selector>,
+    V: Into<String>,
 {
     fn from((one, boolean, two): ((S, V), char, (S, V))) -> Self {
         match boolean {
             '|' => CompoundSelector::Or { first_selector: one.0.into(), first_version: one.1.into(), second_selector: two.0.into(), second_version: two.1.into() },
             ',' => CompoundSelector::And { first_selector: one.0.into(), first_version: one.1.into(), second_selector: two.0.into(), second_version: two.1.into() },
             _ => panic!("You must use either | or , as the separator when converting into a CompoundSelector"),
         }
     }
 }
 
-
 impl<S> CompoundSelector<S>
-    where
-        S: AsRef<str> + PartialEq + Into<String>,
+where
+    S: AsRef<str> + PartialEq + Into<String>,
 {
     /// This takes a versions and tests that it falls within the constraints of this CompoundSelector
     /// ```
     ///  use rust_matchspec::{Selector, CompoundSelector};
     ///
     ///  let single = CompoundSelector::Single {
     ///     selector: Selector::GreaterThan,
@@ -196,36 +195,36 @@
     ///
     ///  assert!(or.is_match(&"3.0.0"));
     ///  assert!(or.is_match(&"0.1.1"));
     ///  assert!(!or.is_match(&"1.2.1"));
     ///  assert!(!or.is_match(&"1.1.1"));
     ///  assert!(!or.is_match(&"1.1.7"));
     ///  ```
-    pub fn is_match<V: AsRef<str> + PartialEq>(&self, other: &V) -> bool {
+    pub fn is_match(&self, other: &str) -> bool {
         match self {
             CompoundSelector::Single { selector, version } => {
-                selector.boolean_operator()(other.as_ref(), version.as_ref())
+                selector.boolean_operator()(other, version.as_ref())
             }
             CompoundSelector::And {
                 first_selector,
                 first_version,
                 second_selector,
                 second_version,
             } => {
-                first_selector.boolean_operator()(other.as_ref(), first_version.as_ref())
-                    && second_selector.boolean_operator()(other.as_ref(), second_version.as_ref())
+                first_selector.boolean_operator()(other, first_version.as_ref())
+                    && second_selector.boolean_operator()(other, second_version.as_ref())
             }
             CompoundSelector::Or {
                 first_selector,
                 first_version,
                 second_selector,
                 second_version,
             } => {
-                first_selector.boolean_operator()(other.as_ref(), first_version.as_ref())
-                    || second_selector.boolean_operator()(other.as_ref(), second_version.as_ref())
+                first_selector.boolean_operator()(other, first_version.as_ref())
+                    || second_selector.boolean_operator()(other, second_version.as_ref())
             }
         }
     }
 }
 
 /// Create a selector from a parser tuple:
 /// ```
@@ -236,17 +235,17 @@
 ///     first_selector: Selector::GreaterThan,
 ///     first_version: "1.1.1".to_string(),
 ///     second_selector: Selector::LessThan,
 ///     second_version: "3.0.0".to_string(),
 /// });
 /// ```
 impl<S, V> From<(S, V, V, S, V)> for CompoundSelector<String>
-    where
-        S: Into<Selector>,
-        V: Into<String> + AsRef<str> + PartialEq + std::fmt::Display,
+where
+    S: Into<Selector>,
+    V: Into<String> + AsRef<str> + PartialEq + std::fmt::Display,
 {
     fn from(
         (first_selector, first_version, joiner, second_selector, second_version): (S, V, V, S, V),
     ) -> Self {
         match joiner.as_ref() {
             "|" => CompoundSelector::Or {
                 first_selector: first_selector.into(),
@@ -278,128 +277,123 @@
 /// ```bash
 /// openssl>=1.1.1g
 /// openssl>=1.1.1g[platform='linux-64']
 /// tensorflow==2.9.*
 /// ```
 /// Full MatchSpec documentation is found in the code [here](https://github.com/conda/conda/blob/main/conda/models/match_spec.py)
 /// and [here](https://conda.io/projects/conda-build/en/latest/resources/package-spec.html#build-version-spec) in the spec
+#[pyclass]
 #[derive(Debug, Clone, Eq)]
-pub struct MatchSpec<S>
-    where
-        S: AsRef<str> + PartialEq + PartialOrd + Into<String>,
-{
-    pub channel: Option<S>,
-    pub subdir: Option<S>,
-    pub namespace: Option<S>,
-    pub package: S,
-    pub version: Option<CompoundSelector<S>>,
-    pub build: Option<S>,
-    pub key_value_pairs: Vec<(S, Selector, S)>,
+pub struct MatchSpec {
+    pub channel: Option<String>,
+    pub subdir: Option<String>,
+    pub namespace: Option<String>,
+    pub package: String,
+    pub version: Option<CompoundSelector<String>>,
+    pub build: Option<String>,
+    pub key_value_pairs: Vec<(String, Selector, String)>,
 }
 
 /// Custom implementation to make sure that we don't compare key_value_pairs
 /// If we don't know how to understand it, we should ignore the key value for the purpose of struct
 /// equality. Makes it simpler to handle potentially unknown future additions to the spec.
-impl<S> PartialEq for MatchSpec<S>
-    where
-        S: AsRef<str> + PartialEq + PartialOrd + Into<String>,
-{
+impl PartialEq for MatchSpec {
     fn eq(&self, other: &Self) -> bool {
         self.channel == other.channel
             && self.subdir == other.subdir
             && self.namespace == other.namespace
             && self.package == other.package
             && self.version == other.version
             && self.build == other.build
     }
 }
 
-impl Default for MatchSpec<String> {
+impl Default for MatchSpec {
     fn default() -> Self {
         MatchSpec {
             channel: None,
             subdir: None,
             namespace: None,
             package: "*".to_string(),
             version: None,
             build: None,
             key_value_pairs: Vec::new(),
         }
     }
 }
 
 /// This is where we actually do the parsing
-impl FromStr for MatchSpec<String> {
+impl FromStr for MatchSpec {
     type Err = MatchSpecError;
     fn from_str(s: &str) -> Result<Self, Self::Err> {
         match alt((implicit_matchspec_parser, full_matchspec_parser))(s).finish() {
             Ok((_, ms)) => Ok(ms),
-            Err(NomError { input, code: _ }) => Err(MatchSpecError { message: String::from(input) }),
+            Err(NomError { input, code: _ }) => Err(MatchSpecError {
+                message: String::from(input),
+            }),
         }
     }
 }
 
-impl<S> From<(S, Option<S>, Option<S>)> for MatchSpec<String>
-    where
-        S: AsRef<str> + Into<String>,
-{
-    fn from((package, version, build): (S, Option<S>, Option<S>)) -> Self {
+impl From<(&str, Option<&str>, Option<&str>)> for MatchSpec {
+    fn from((package, version, build): (&str, Option<&str>, Option<&str>)) -> Self {
         MatchSpec {
             channel: None,
             subdir: None,
             namespace: None,
             package: package.into(),
-            version: version.map(|s| CompoundSelector::Single { selector: Selector::EqualTo, version: s.into() }),
+            version: version.map(|s| CompoundSelector::Single {
+                selector: Selector::EqualTo,
+                version: s.into(),
+            }),
             build: build.map(|s| s.into()),
             key_value_pairs: Vec::new(),
         }
     }
 }
 
-impl<S>
-From<(
-    Option<S>,
-    Option<S>,
-    Option<S>,
-    S,
-    Option<CompoundSelector<String>>,
-    Option<Vec<(S, S, S)>>,
-)> for MatchSpec<String>
-    where
-        S: Into<String> + AsRef<str> + PartialEq + std::fmt::Display,
+impl
+    From<(
+        Option<&str>,
+        Option<&str>,
+        Option<&str>,
+        &str,
+        Option<CompoundSelector<String>>,
+        Option<Vec<(&str, &str, &str)>>,
+    )> for MatchSpec
 {
     fn from(
         (channel, subdir, ns, package, cs, keys): (
-            Option<S>,
-            Option<S>,
-            Option<S>,
-            S,
+            Option<&str>,
+            Option<&str>,
+            Option<&str>,
+            &str,
             Option<CompoundSelector<String>>,
-            Option<Vec<(S, S, S)>>,
+            Option<Vec<(&str, &str, &str)>>,
         ),
     ) -> Self {
         // Convert the key_value_pairs into (S, Selector, S) tuples.
         // I'm not sure its possible to have the full selector set, but this models it in a
         // pretty good way.
         let key_value_pairs: Vec<(String, Selector, String)> = keys
-            .map(|vec: Vec<(S, S, S)>| {
+            .map(|vec: Vec<(&str, &str, &str)>| {
                 vec.iter()
                     .map(|(key, selector, value)| {
                         (
-                            key.as_ref().to_string(),
+                            String::from(*key),
                             Selector::from(selector),
-                            value.as_ref().to_string(),
+                            String::from(*value),
                         )
                     })
                     .collect()
             })
             .unwrap_or_default();
 
         let namespace = if let Some(a) = ns {
-            if a.as_ref().is_empty() {
+            if a.is_empty() {
                 None
             } else {
                 Some(a.to_string())
             }
         } else {
             None
         };
@@ -429,69 +423,65 @@
 
         // Save all the key value pairs, this is done last to avoid borrow after move
         ms.key_value_pairs = key_value_pairs;
         ms
     }
 }
 
-
-impl<S: AsRef<str> + PartialOrd + PartialEq<str> + Into<String>> MatchSpec<S> {
+impl MatchSpec {
     /// Matches package names. The matchspec package may contain globs
     /// ```
     /// use rust_matchspec::matchspec::*;
     ///
-    /// let ms: MatchSpec<String> = "openssl>1.1.1a".parse().unwrap();
+    /// let ms: MatchSpec = "openssl>1.1.1a".parse().unwrap();
     /// assert!(ms.is_package_match("openssl".to_string()));
     /// ```
-    pub fn is_package_match(&self, package: S) -> bool {
-        package.as_ref().chars().all(is_alphanumeric_with_dashes)
+    pub fn is_package_match(&self, package: String) -> bool {
+        package.chars().all(is_alphanumeric_with_dashes)
             && is_match_glob_str(self.package.as_ref(), package.as_ref())
     }
 
     /// Uses the Selector embedded in the matchspec to do a match on only a version
     /// ```
     /// use rust_matchspec::matchspec::*;
     ///
-    /// let ms: MatchSpec<String> = "openssl>1.1.1a".parse().unwrap();
+    /// let ms: MatchSpec = "openssl>1.1.1a".parse().unwrap();
     /// assert!(ms.is_version_match(&"1.1.1r"));
     /// ```
-    pub fn is_version_match<V: AsRef<str> + PartialEq>(&self, version: &V) -> bool {
-        self.version.as_ref().map(|v| v.is_match(version)).unwrap_or(true)
+    pub fn is_version_match(&self, version: &str) -> bool {
+        self.version
+            .as_ref()
+            .map(|v| v.is_match(version))
+            .unwrap_or(true)
     }
 
-    pub fn is_package_version_match<V: AsRef<str> + PartialEq>(
-        &self,
-        package: &V,
-        version: &V,
-    ) -> bool {
-        package.as_ref().chars().all(is_alphanumeric_with_dashes)
-            && is_match_glob_str(self.package.as_ref(), package.as_ref())
+    pub fn is_package_version_match(&self, package: &str, version: &str) -> bool {
+        package.chars().all(is_alphanumeric_with_dashes)
+            && is_match_glob_str(self.package.as_ref(), package)
             && self.is_version_match(version)
     }
 }
 
-impl MatchSpec<String> {
+impl MatchSpec {
     pub fn is_match(&self, pc: &PackageCandidate) -> bool {
-        self.is_package_version_match(
-            &pc.name,
-            &pc.version.as_ref().unwrap_or(&String::new()))
+        self.is_package_version_match(&pc.name, pc.version.as_ref().unwrap_or(&String::new()))
             && (self.subdir.is_none() || self.subdir == pc.subdir)
             && (self.build.is_none() || self.build == pc.build)
     }
 }
 
 #[cfg(test)]
 mod test {
     #[cfg(test)]
     mod matching {
         use crate::matchspec::*;
 
         #[test]
         fn package_only() {
-            let mut ms: MatchSpec<String> = "tensorflow".parse().unwrap();
+            let mut ms: MatchSpec = "tensorflow".parse().unwrap();
 
             assert!(ms.is_package_match("tensorflow".to_string()));
             assert!(!ms.is_package_match("pytorch".to_string()));
 
             ms = "tensor*-gpu".parse().unwrap();
             assert!(ms.is_package_match("tensorflow-gpu".to_string()));
             assert!(!ms.is_package_match("tennnnsorflow-gpu".to_string()));
@@ -506,61 +496,61 @@
 
             // Illegal chars
             assert!(!ms.is_package_match("python>3.10[name=* vmd5=\"abcdef1312\"]".to_string()));
         }
 
         #[test]
         fn package_and_version_only() {
-            let ms: MatchSpec<String> = "tensorflow>1.9.2".parse().unwrap();
+            let ms: MatchSpec = "tensorflow>1.9.2".parse().unwrap();
 
-            assert!(ms.is_package_version_match(&"tensorflow", &"1.9.3"));
-            assert!(!ms.is_package_version_match(&"tensorflow", &"1.9.0"));
+            assert!(ms.is_package_version_match("tensorflow", "1.9.3"));
+            assert!(!ms.is_package_version_match("tensorflow", "1.9.0"));
         }
 
         #[test]
         fn compound_selectors() {
             let single = CompoundSelector::Single {
                 selector: Selector::GreaterThan,
                 version: "1.1.1",
             };
 
-            assert!(single.is_match(&"1.2.1"));
-            assert!(single.is_match(&"3.0.0"));
-            assert!(!single.is_match(&"1.1.1"));
-            assert!(!single.is_match(&"0.1.1"));
+            assert!(single.is_match("1.2.1"));
+            assert!(single.is_match("3.0.0"));
+            assert!(!single.is_match("1.1.1"));
+            assert!(!single.is_match("0.1.1"));
 
             let and = CompoundSelector::And {
                 first_selector: Selector::GreaterThan,
                 first_version: "1.1.1",
                 second_selector: Selector::LessThanOrEqualTo,
                 second_version: "1.2.1",
             };
 
-            assert!(and.is_match(&"1.2.1"));
-            assert!(and.is_match(&"1.1.7"));
-            assert!(!and.is_match(&"1.2.2"));
-            assert!(!and.is_match(&"0.1.1"));
+            assert!(and.is_match("1.2.1"));
+            assert!(and.is_match("1.1.7"));
+            assert!(!and.is_match("1.2.2"));
+            assert!(!and.is_match("0.1.1"));
 
             let or = CompoundSelector::Or {
                 first_selector: Selector::LessThan,
                 first_version: "1.1.1",
                 second_selector: Selector::GreaterThan,
                 second_version: "1.2.1",
             };
 
-            assert!(or.is_match(&"3.0.0"));
-            assert!(or.is_match(&"0.1.1"));
-            assert!(!or.is_match(&"1.2.1"));
-            assert!(!or.is_match(&"1.1.1"));
-            assert!(!or.is_match(&"1.1.7"));
+            assert!(or.is_match("3.0.0"));
+            assert!(or.is_match("0.1.1"));
+            assert!(!or.is_match("1.2.1"));
+            assert!(!or.is_match("1.1.1"));
+            assert!(!or.is_match("1.1.7"));
         }
 
         #[test]
         fn test_version_compare() {
-            let ms: MatchSpec<String> = "python>3.6".parse().unwrap();
-            assert!(!ms.is_package_version_match(&"python", &"3.5"));
-            assert!(ms.is_package_version_match(&"python", &"3.8"));
-            assert!(ms.is_package_version_match(&"python", &"3.9"));
-            assert!(ms.is_package_version_match(&"python", &"3.10"));
+            let ms: MatchSpec = "python>3.6".parse().unwrap();
+            assert!(!ms.is_package_version_match("python", "3.5"));
+            assert!(ms.is_package_version_match("python", "3.8"));
+            assert!(ms.is_package_version_match("python", "3.9"));
+            assert!(ms.is_package_version_match("python", "3.10"));
         }
     }
 }
```

### Comparing `rust_matchspec-0.1.1/src/parsers.rs` & `rust_matchspec-0.2.0/src/parsers.rs`

 * *Files 2% similar despite different names*

```diff
@@ -1,20 +1,22 @@
-use crate::matchspec::*;
 use crate::input_table::*;
+use crate::matchspec::*;
 use nom::error::{Error as NomError, ErrorKind};
 use nom::{
     branch::alt,
     bytes::complete::{tag, take_while, take_while1},
-    character::complete::{alphanumeric0, alphanumeric1, satisfy, multispace0, multispace1, one_of},
+    character::complete::{
+        alphanumeric0, alphanumeric1, multispace0, multispace1, one_of, satisfy,
+    },
     combinator::{complete, eof, opt, peek},
     multi::separated_list0,
     sequence::{delimited, terminated, tuple},
     IResult,
 };
-use version_compare::{Version};
+use version_compare::Version;
 
 /// Parses a version selector. Possible values:
 /// | Selector | Function                                                                   |
 /// |----------|----------------------------------------------------------------------------|
 /// | >        | Greater Than                                                               |
 /// | <        | Less Than                                                                  |
 /// | >=       | Greater Than or Equal To                                                   |
@@ -48,21 +50,19 @@
     take_while1(is_any_valid_str_with_glob)(s)
 }
 
 /// Parses the package version
 pub(crate) fn version_parser(s: &str) -> IResult<&str, &str> {
     let (remainder, version) = take_while1(is_any_valid_str_with_glob)(s)?;
     match Version::from(version) {
-        Some(_) => { Ok((remainder, version)) }
-        None => {
-            Err(nom::Err::Failure(NomError {
-                code: ErrorKind::Fail,
-                input: "Version parse failed",
-            }))
-        }
+        Some(_) => Ok((remainder, version)),
+        None => Err(nom::Err::Failure(NomError {
+            code: ErrorKind::Fail,
+            input: "Version parse failed",
+        })),
     }
 }
 
 fn version_and_selector_parser(s: &str) -> IResult<&str, (&str, &str)> {
     tuple((selector_parser, version_parser))(s)
 }
 
@@ -72,20 +72,18 @@
         delimited(multispace0, satisfy(is_comma_or_alt), multispace0),
         version_and_selector_parser,
     ))(s);
 
     // If we can parse via the more exhaustive parser, return that.
     match result {
         Ok((remainder, parsed)) => Ok((remainder, parsed.into())),
-        Err(_) => {
-            match version_and_selector_parser(s) {
-                Ok((remainder, parsed)) => Ok((remainder, parsed.into())),
-                Err(err) => Err(err),
-            }
-        }
+        Err(_) => match version_and_selector_parser(s) {
+            Ok((remainder, parsed)) => Ok((remainder, parsed.into())),
+            Err(err) => Err(err),
+        },
     }
 }
 
 /// Parses the channel
 pub(crate) fn channel_parser(s: &str) -> IResult<&str, &str> {
     terminated(take_while(is_alphanumeric_with_dashes), peek(one_of(":/")))(s)
 }
@@ -111,15 +109,15 @@
 ///
 /// ```bash
 /// zstd 1.4.5 h9ceee32_0
 /// python 2.7.*
 /// _libgcc_mutex 0.1 main
 /// backports_abc 0.5 py27h7b3c97b_0
 /// ```
-pub(crate) fn implicit_matchspec_parser(s: &str) -> IResult<&str, MatchSpec<String>> {
+pub(crate) fn implicit_matchspec_parser(s: &str) -> IResult<&str, MatchSpec> {
     let (remainder, t) = tuple((
         take_while1(is_alphanumeric_with_dashes_or_period),
         opt(delimited(multispace1, version_parser, multispace0)),
         opt(take_while1(is_alphanumeric_with_dashes_or_period)),
         eof,
     ))(s)?;
 
@@ -127,15 +125,15 @@
     Ok((remainder, output.into()))
 }
 
 /// Parses the whole matchspec using Nom, returning a `MatchSpecTuple`
 /// Assumes this format:
 /// `(channel(/subdir):(namespace):)name(version(build))[key1=value1,key2=value2]`
 /// Instead of using this directly please use the `"".parse()` style provided by FromStr
-pub(crate) fn full_matchspec_parser(s: &str) -> IResult<&str, MatchSpec<String>, NomError<&str>> {
+pub(crate) fn full_matchspec_parser(s: &str) -> IResult<&str, MatchSpec, NomError<&str>> {
     // Eats `/subdir`
     let subdir_parser = delimited(
         satisfy(is_forward_slash),
         take_while(is_alphanumeric_with_dashes),
         peek(satisfy(is_colon)),
     );
 
@@ -145,15 +143,14 @@
     // Eats `[ .. ]`
     let keys_vec_parser = delimited(
         satisfy(is_left_bracket),
         separated_list0(satisfy(is_comma), key_value_pair_parser),
         satisfy(is_right_bracket),
     );
 
-
     // Put all the parsers together
     let (remainder, t) = complete(tuple((
         opt(channel_parser),
         opt(subdir_parser),
         opt(namespace_parser),
         name_parser,
         opt(compound_selector_parser),
@@ -163,15 +160,15 @@
     Ok((remainder, t.into()))
 }
 
 #[cfg(test)]
 mod test {
     mod component_parsers {
         use crate::parsers::*;
-        use nom::error::{ErrorKind};
+        use nom::error::ErrorKind;
 
         #[test]
         fn test_channel_parser() {
             assert_eq!(
                 channel_parser("conda-forge::tensorflow >=2.9.1"),
                 Ok(("::tensorflow >=2.9.1", "conda-forge"))
             );
@@ -227,19 +224,21 @@
             assert_eq!(version_parser("5.0.0.1"), Ok(("", "5.0.0.1")));
             assert_eq!(version_parser("2022.1"), Ok(("", "2022.1")));
             assert_eq!(version_parser("1.21_5"), Ok(("", "1.21_5")));
             assert_eq!(
                 version_parser("2.9.1[subdir=linux]"),
                 Ok(("[subdir=linux]", "2.9.1"))
             );
-            assert_eq!(version_parser("not-correct-version"),
-                       Err(nom::Err::Failure(NomError {
-                           code: ErrorKind::Fail,
-                           input: "Version parse failed",
-                       })));
+            assert_eq!(
+                version_parser("not-correct-version"),
+                Err(nom::Err::Failure(NomError {
+                    code: ErrorKind::Fail,
+                    input: "Version parse failed",
+                }))
+            );
         }
 
         #[test]
         fn test_key_value_parser() {
             // Ensure we handle quoting
             assert_eq!(
                 key_value_pair_parser("subdir = 'linux-64'"),
@@ -326,64 +325,64 @@
 
     mod final_parser {
         use crate::error::MatchSpecError;
         use crate::matchspec::*;
 
         #[test]
         fn simple_package_and_version() {
-            let base: MatchSpec<String> = MatchSpec::default();
+            let base: MatchSpec = MatchSpec::default();
             let expected = MatchSpec {
                 package: "tensorflow".to_string(),
                 version: Some(CompoundSelector::Single {
                     selector: Selector::GreaterThanOrEqualTo,
                     version: "2.9.1".to_string(),
                 }),
                 ..base
             };
 
-            let ms: MatchSpec<String> = "tensorflow>=2.9.1".parse().unwrap();
+            let ms: MatchSpec = "tensorflow>=2.9.1".parse().unwrap();
 
             assert_eq!(ms, expected);
         }
 
         #[test]
         fn package_only() {
-            let result: Result<MatchSpec<String>, MatchSpecError> = "tensorflow".parse();
+            let result: Result<MatchSpec, MatchSpecError> = "tensorflow".parse();
 
             let ms = result.unwrap();
             assert_eq!(ms.subdir, None);
             assert_eq!(ms.namespace, None);
             assert_eq!(ms.package, "tensorflow");
             assert_eq!(ms.version, None);
             assert!(ms.key_value_pairs.is_empty());
         }
 
         /// Matchspecs can effectively have 2 valid representations of version and packagename
         /// matchers. The most explicit form is: `tensorflow==2.9.1`, but the other supported mode
         /// is the implicit: `tensorflow 2.9.1`. Both are supported, and they are equivalent.
         #[test]
         fn package_and_version_only() {
-            let base: MatchSpec<String> = MatchSpec::default();
+            let base: MatchSpec = MatchSpec::default();
 
             // Our output should look like this
             let expected = MatchSpec {
                 package: "tensorflow".to_string(),
                 version: Some(CompoundSelector::Single {
                     selector: Selector::EqualTo,
                     version: "2.9.1".to_string(),
                 }),
                 ..base
             };
 
             // Test the explicit matcher first
-            let explicit: MatchSpec<String> = "tensorflow==2.9.1".parse().unwrap();
+            let explicit: MatchSpec = "tensorflow==2.9.1".parse().unwrap();
             assert_eq!(explicit, expected);
 
             // Test the implicit matcher second
-            let implicit: MatchSpec<String> = "tensorflow 2.9.1".parse().unwrap();
+            let implicit: MatchSpec = "tensorflow 2.9.1".parse().unwrap();
             assert_eq!(implicit, expected);
 
             // They should both be equal
             assert_eq!(implicit, explicit);
         }
 
         /// Another common matchspec is `package version build`. Like so:
@@ -402,36 +401,34 @@
                 build: Some("mkl_py39hb9fcb14_0".to_string()),
                 channel: None,
                 subdir: None,
                 namespace: None,
             };
 
             // Test the explicit matcher first
-            let explicit: MatchSpec<String> = "tensorflow==2.9.1[build=\"mkl_py39hb9fcb14_0\"]"
+            let explicit: MatchSpec = "tensorflow==2.9.1[build=\"mkl_py39hb9fcb14_0\"]"
                 .parse()
                 .unwrap();
 
             // Test against expected
             assert_eq!(expected, explicit);
 
             // Test the implicit matcher second
-            let implicit: MatchSpec<String> =
-                "tensorflow 2.9.1 mkl_py39hb9fcb14_0".parse().unwrap();
+            let implicit: MatchSpec = "tensorflow 2.9.1 mkl_py39hb9fcb14_0".parse().unwrap();
 
             // Test against expected
             assert_eq!(expected, explicit);
 
             // They should both be equal
             assert_eq!(implicit, explicit);
         }
 
         #[test]
         fn package_and_version_with_key_values() {
-            let result: Result<MatchSpec<String>, MatchSpecError> =
-                "tensorflow>1[subdir!=win-64]".parse();
+            let result: Result<MatchSpec, MatchSpecError> = "tensorflow>1[subdir!=win-64]".parse();
 
             let ms = result.unwrap();
             assert_eq!(ms.subdir, None);
             assert_eq!(ms.namespace, None);
             assert_eq!(ms.package, "tensorflow");
             assert_eq!(
                 ms.version,
@@ -449,16 +446,15 @@
                     "win-64".to_string(),
                 ))
             );
         }
 
         #[test]
         fn package_only_with_key_values() {
-            let result: Result<MatchSpec<String>, MatchSpecError> =
-                "tensorflow[subdir=win-64]".parse();
+            let result: Result<MatchSpec, MatchSpecError> = "tensorflow[subdir=win-64]".parse();
 
             let ms = result.unwrap();
             assert_eq!(ms.subdir, Some("win-64".to_string()));
             assert_eq!(ms.namespace, None);
             assert_eq!(ms.package, "tensorflow");
             assert_eq!(ms.version, None);
             assert_eq!(ms.key_value_pairs.len(), 1);
@@ -470,15 +466,15 @@
                     "win-64".to_string(),
                 ))
             );
         }
 
         #[test]
         fn everything_except_namespace() {
-            let ms: MatchSpec<String> = "main/linux-64::pytorch>1.10.2".parse().unwrap();
+            let ms: MatchSpec = "main/linux-64::pytorch>1.10.2".parse().unwrap();
 
             let expected = MatchSpec {
                 channel: Some("main".to_string()),
                 subdir: Some("linux-64".to_string()),
                 namespace: None,
                 package: "pytorch".to_string(),
                 build: None,
@@ -505,26 +501,31 @@
                     first_version: "2.9.1".to_string(),
                     second_selector: Selector::LessThan,
                     second_version: "3.0.0".to_string(),
                 }),
                 key_value_pairs: Vec::new(),
             };
 
-            let ms: MatchSpec<String> =
+            let ms: MatchSpec =
                 "conda-forge/linux-64:UNUSED:tensorflow>2.9.1,<3.0.0[license=GPL, subdir=linux-64]"
                     .parse()
                     .unwrap();
 
             assert_eq!(expected, ms);
         }
 
         #[test]
         fn fail_on_wrong_semver_version() {
-            let ms: Result<MatchSpec<String>, MatchSpecError> = "python=wrong".parse();
-            assert_eq!(ms, Err(MatchSpecError { message: "Version parse failed".to_string() }))
+            let ms: Result<MatchSpec, MatchSpecError> = "python=wrong".parse();
+            assert_eq!(
+                ms,
+                Err(MatchSpecError {
+                    message: "Version parse failed".to_string()
+                })
+            )
         }
     }
 
     // This is a suite of tests using real data from things like the repodata.json
     #[cfg(test)]
     mod real_life {
         use crate::matchspec::MatchSpec;
@@ -547,14 +548,14 @@
                 BufReader::new(File::open(depends_file).expect("opening repodata depends file"));
             let depends: Vec<String> = repodata_depends_buffer
                 .lines()
                 .map(|l| l.unwrap())
                 .collect();
 
             for line in depends {
-                let _parsed: MatchSpec<String> = line
+                let _parsed: MatchSpec = line
                     .parse()
                     .unwrap_or_else(|_| panic!("Failed to parse: {}", line));
             }
         }
     }
 }
```

### Comparing `rust_matchspec-0.1.1/test_data/linux_64-depends.txt` & `rust_matchspec-0.2.0/test_data/linux_64-depends.txt`

 * *Files identical despite different names*

### Comparing `rust_matchspec-0.1.1/Cargo.lock` & `rust_matchspec-0.2.0/Cargo.lock`

 * *Files 1% similar despite different names*

```diff
@@ -218,17 +218,17 @@
 name = "lazy_static"
 version = "1.4.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "e2abad23fbc42b3700f2f279844dc832adb2b2eb069b2df918f455c4e18cc646"
 
 [[package]]
 name = "libc"
-version = "0.2.140"
+version = "0.2.141"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "99227334921fae1a979cf0bfdfcc6b3e5ce376ef57e16fb6fb3ea2ed6095f80c"
+checksum = "3304a64d199bb964be99741b7a14d26972741915b3649639149b2479bb46f4b5"
 
 [[package]]
 name = "lock_api"
 version = "0.4.9"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "435011366fe56583b16cf956f9df0095b405b82d76425bc8981c0e22e60ec4df"
 dependencies = [
@@ -243,15 +243,15 @@
 checksum = "abb12e687cfb44aa40f41fc3978ef76448f9b6038cad6aef4259d3c095a2382e"
 dependencies = [
  "cfg-if",
 ]
 
 [[package]]
 name = "matchspec"
-version = "0.1.1"
+version = "0.2.0"
 dependencies = [
  "criterion",
  "nom",
  "pyo3",
  "serde",
  "serde_json",
  "version-compare",
```

### Comparing `rust_matchspec-0.1.1/PKG-INFO` & `rust_matchspec-0.2.0/README.md`

 * *Files 23% similar despite different names*

```diff
@@ -1,28 +1,64 @@
-Metadata-Version: 2.1
-Name: rust_matchspec
-Version: 0.1.1
-License-File: LICENSE
-Summary: A conda matchspec written in Rust
-Requires-Python: >=3.7
-Description-Content-Type: text/markdown; charset=UTF-8; variant=GFM
-
 # MatchSpec
 
 A Conda MatchSpec implementation in pure Rust. This allows you to parse a matchspec and validate it against a package to see if it matches.
 
+# Python Library
+
+This library exposes a few simple functions:
+
+## `match_against_matchspec()`
+
+Takes a `matchspec` as a `str` and matches it against a `package_name` and `version` (both `str`). Returns a `bool`.
+
+``` python
+import rust_matchspec
+rust_matchspec.match_against_matchspec('python>=3.0', 'python', '3.10.1') # returns True
+```
+
+## `filter_package_list()`
+
+Takes a `list` of `dicts` and returns all the dicts inside that match a given matchspec. The `dicts` must have a `name` key with a `str` value, but all other fields are optional.
+
+```python
+import rust_matchspec
+list = [{'name': 'tensorflow', 'version': '2.10.0'},
+	{'name': 'pytorch', 'version': '2.0.0'},
+	{'name': 'pytorch', 'version': '1.11.1'}]
+
+rust_matchspec.filter_package_list('pytorch>1.12', list) # returns [PackageCandidate(name=pytorch)]
+```
+
+Possible keys:
+
+| Key          | Expected Type | Required? |
+|--------------|---------------|-----------|
+| name         | str           | yes       |
+| version      | str           |           |
+| build        | str           |           |
+| build_number | u32           |           |
+| depends      | [str]         |           |
+| license      | str           |           |
+| md5          | str           |           |
+| sha256       | str           |           |
+| size         | u64           |           |
+| subdir       | str           |           |
+| timestamp    | u64           |           |
+
+# Rust Library
+
 ## Example
 
 The way you instantiate a MatchSpec is by parsing a string into the type:
 
 ```rust
 use rust_matchspec::{CompoundSelector, MatchSpec, Selector};
 
 // Create the MatchSpec by parsing a String or &str
-let matchspec: MatchSpec<String> = "main/linux-64::pytorch>1.10.2".parse().unwrap();
+let matchspec: MatchSpec = "main/linux-64::pytorch>1.10.2".parse().unwrap();
 
 // You then have the data accessible inside the MatchSpec struct if you want it
 // Package name is the only mandatory field in a matchspec
 assert_eq!(&matchspec.package, "pytorch");
 
 // These are optional, so they will be wrapped in an Option
 assert_eq!(matchspec.channel, Some("main".to_string()));
@@ -37,21 +73,42 @@
 // You can also check to see if a package name and version match the spec.
 // This is a faster function that allows us to bypass some sometimes unnecessary tests like channel or subdir
 assert!(matchspec.is_package_version_match(&"pytorch", &"1.11.0"))
 ```
 
 ## Benchmarking
 
-This library contains benchmarks aimed at checking the speed of our implementation against other languages and ensure speed doesn't regress. This is a pure Rust benchmark so you'll need to view it with some skepticism if you want to compare this implementation against others. Benchmark harnesses and the data all need to be identical for a benchmark to really provide value.
+This library contains benchmarks aimed at checking the speed of our implementation against other languages and ensure speed doesn't regress. These are contrived benchmarks to test raw speed, so take them (and all benchmarks) with a bit of skepticism. Benchmark harnesses and the data all need to be identical for a benchmark to really provide value.
+
+
+### Python
 
-### Running the benchmarks
+The Python benchmarks use [pytest-benchmark](https://pytest-benchmark.readthedocs.io/en/stable/).
 
-These benchmarks use [Criterion.rs](https://bheisler.github.io/criterion.rs/book/criterion_rs.html) to provide the benchmarking framework. Its pretty easy to run the benchmarks on stable rust:
+Steps to run the benchmarks:
+
+```bash
+# Setup the conda env
+conda env create -f ./environment.yml
+conda activate rust_matchspec
+
+# Build an optimized wheel
+maturin build --release
+
+# install it
+pip install ./target/wheels/rust_matchspec*.whl
+
+# Finally, run the benchmark
+pytest
+```
+
+### Rust
+
+The Rust benchmarks use [Criterion.rs](https://bheisler.github.io/criterion.rs/book/criterion_rs.html) to provide the benchmarking framework. Its pretty easy to run the benchmarks on stable rust:
 
 ```bash
 cargo bench 
 
 # Or if you're on mac and get errors with Invalid Symbols:
 cargo bench --no-default-features
 ```
 This will automatically track benchmark timings across runs. If you do this on a laptop or workstation be aware that you may have regressions show up if you have background processes or other things happening. I would recommend always running the benchmarks at a similar level of CPU load. If you want consistent testing its probably best to quit your browser or anything in the background that might be eating CPU or doing IO.
-
```

