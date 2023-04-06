# Comparing `tmp/maturin-1.0.0b5.tar.gz` & `tmp/maturin-1.0.0b7.tar.gz`

## Comparing `maturin-1.0.0b5.tar` & `maturin-1.0.0b7.tar`

### file list

```diff
@@ -1,69 +1,69 @@
--rw-r--r--   0        0        0     4274 1970-01-01 00:00:00.000000 maturin-1.0.0b5/Cargo.toml
--rw-r--r--   0     1001      123     1966 2023-03-12 08:21:55.000000 maturin-1.0.0b5/.cirrus.yml
--rw-r--r--   0     1001      123       94 2023-03-12 08:21:55.000000 maturin-1.0.0b5/.codespellrc
--rw-r--r--   0     1001      123      252 2023-03-12 08:21:55.000000 maturin-1.0.0b5/.config/nextest.toml
--rw-r--r--   0     1001      123      180 2023-03-12 08:21:55.000000 maturin-1.0.0b5/.dockerignore
--rw-r--r--   0     1001      123      184 2023-03-12 08:21:55.000000 maturin-1.0.0b5/.gitignore
--rw-r--r--   0     1001      123    65388 2023-03-12 08:21:55.000000 maturin-1.0.0b5/Cargo.lock
--rw-r--r--   0     1001      123    54572 2023-03-12 08:21:55.000000 maturin-1.0.0b5/Changelog.md
--rw-r--r--   0     1001      123     3228 2023-03-12 08:21:55.000000 maturin-1.0.0b5/Code-of-Conduct.md
--rw-r--r--   0     1001      123     2386 2023-03-12 08:21:55.000000 maturin-1.0.0b5/Dockerfile
--rw-r--r--   0     1001      123      245 2023-03-12 08:21:55.000000 maturin-1.0.0b5/MANIFEST.in
--rw-r--r--   0     1001      123    16567 2023-03-12 08:21:55.000000 maturin-1.0.0b5/README.md
--rw-r--r--   0     1001      123       16 2023-03-12 08:21:55.000000 maturin-1.0.0b5/clippy.toml
--rw-r--r--   0     1001      123     9662 2023-03-12 08:21:55.000000 maturin-1.0.0b5/deny.toml
--rw-r--r--   0     1001      123    10847 2023-03-12 08:21:55.000000 maturin-1.0.0b5/license-apache
--rw-r--r--   0     1001      123     1051 2023-03-12 08:21:55.000000 maturin-1.0.0b5/license-mit
--rw-r--r--   0     1001      123     6236 2023-03-12 08:21:55.000000 maturin-1.0.0b5/maturin/__init__.py
--rw-r--r--   0     1001      123      956 2023-03-12 08:21:55.000000 maturin-1.0.0b5/maturin/__main__.py
--rw-r--r--   0     1001      123     5162 2023-03-12 08:21:55.000000 maturin-1.0.0b5/maturin/import_hook.py
--rw-r--r--   0     1001      123      200 2023-03-12 08:21:55.000000 maturin-1.0.0b5/netlify.toml
--rw-r--r--   0     1001      123     2170 2023-03-12 08:21:55.000000 maturin-1.0.0b5/noxfile.py
--rw-r--r--   0     1001      123     1290 2023-03-12 08:21:55.000000 maturin-1.0.0b5/pyproject.toml
--rw-r--r--   0     1001      123     2868 2023-03-12 08:21:55.000000 maturin-1.0.0b5/setup.py
--rw-r--r--   0     1001      123    19412 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/auditwheel/audit.rs
--rw-r--r--   0     1001      123    53261 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/auditwheel/manylinux-policy.json
--rw-r--r--   0     1001      123      242 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/auditwheel/mod.rs
--rw-r--r--   0     1001      123     1862 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/auditwheel/musllinux-policy.json
--rw-r--r--   0     1001      123     1389 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/auditwheel/musllinux.rs
--rw-r--r--   0     1001      123     3777 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/auditwheel/patchelf.rs
--rw-r--r--   0     1001      123     4602 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/auditwheel/platform_tag.rs
--rw-r--r--   0     1001      123     5393 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/auditwheel/policy.rs
--rw-r--r--   0     1001      123     1169 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/auditwheel/repair.rs
--rw-r--r--   0     1001      123    37504 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/build_context.rs
--rw-r--r--   0     1001      123    58819 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/build_options.rs
--rw-r--r--   0     1001      123     6163 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/cargo_toml.rs
--rw-r--r--   0     1001      123    33444 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/ci.rs
--rw-r--r--   0     1001      123    23307 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/compile.rs
--rw-r--r--   0     1001      123     8342 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/cross_compile.rs
--rw-r--r--   0     1001      123     5085 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/develop.rs
--rw-r--r--   0     1001      123     2233 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/lib.rs
--rw-r--r--   0     1001      123    18006 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/main.rs
--rw-r--r--   0     1001      123    33121 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/metadata.rs
--rw-r--r--   0     1001      123    44836 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/module_writer.rs
--rw-r--r--   0     1001      123     8203 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/new_project.rs
--rw-r--r--   0     1001      123    16557 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/project_layout.rs
--rw-r--r--   0     1001      123    14181 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/pyproject_toml.rs
--rw-r--r--   0     1001      123    10374 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/python_interpreter/config.rs
--rw-r--r--   0     1001      123     1595 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/python_interpreter/get_interpreter_metadata.py
--rw-r--r--   0     1001      123    33115 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/python_interpreter/mod.rs
--rw-r--r--   0     1001      123      443 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/python_interpreter/sysconfig-emscripten.json
--rw-r--r--   0     1001      123     3861 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/python_interpreter/sysconfig-freebsd.json
--rw-r--r--   0     1001      123    14124 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/python_interpreter/sysconfig-linux.json
--rw-r--r--   0     1001      123     3812 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/python_interpreter/sysconfig-macos.json
--rw-r--r--   0     1001      123      738 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/python_interpreter/sysconfig-netbsd.json
--rw-r--r--   0     1001      123     2353 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/python_interpreter/sysconfig-openbsd.json
--rw-r--r--   0     1001      123     3341 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/python_interpreter/sysconfig-windows.json
--rw-r--r--   0     1001      123    30697 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/source_distribution.rs
--rw-r--r--   0     1001      123    28822 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/target.rs
--rw-r--r--   0     1001      123      686 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/templates/.gitignore.j2
--rw-r--r--   0     1001      123      518 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/templates/Cargo.toml.j2
--rw-r--r--   0     1001      123      149 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/templates/__init__.py.j2
--rw-r--r--   0     1001      123      123 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/templates/build.rs.j2
--rw-r--r--   0     1001      123       47 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/templates/example.udl.j2
--rw-r--r--   0     1001      123      722 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/templates/lib.rs.j2
--rw-r--r--   0     1001      123       45 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/templates/main.rs.j2
--rw-r--r--   0     1001      123      859 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/templates/pyproject.toml.j2
--rw-r--r--   0     1001      123    20146 2023-03-12 08:21:55.000000 maturin-1.0.0b5/src/upload.rs
--rwxr-xr-x   0     1001      123      974 2023-03-12 08:21:55.000000 maturin-1.0.0b5/test-dockerfile.sh
--rw-r--r--   0        0        0    17742 1970-01-01 00:00:00.000000 maturin-1.0.0b5/PKG-INFO
+-rw-r--r--   0        0        0     4442 1970-01-01 00:00:00.000000 maturin-1.0.0b7/Cargo.toml
+-rw-r--r--   0     1001      123     1693 2023-04-05 13:40:38.000000 maturin-1.0.0b7/.cirrus.yml
+-rw-r--r--   0     1001      123       94 2023-04-05 13:40:38.000000 maturin-1.0.0b7/.codespellrc
+-rw-r--r--   0     1001      123      252 2023-04-05 13:40:38.000000 maturin-1.0.0b7/.config/nextest.toml
+-rw-r--r--   0     1001      123      180 2023-04-05 13:40:38.000000 maturin-1.0.0b7/.dockerignore
+-rw-r--r--   0     1001      123      184 2023-04-05 13:40:38.000000 maturin-1.0.0b7/.gitignore
+-rw-r--r--   0     1001      123    65636 2023-04-05 13:40:38.000000 maturin-1.0.0b7/Cargo.lock
+-rw-r--r--   0     1001      123    55213 2023-04-05 13:40:38.000000 maturin-1.0.0b7/Changelog.md
+-rw-r--r--   0     1001      123     3228 2023-04-05 13:40:38.000000 maturin-1.0.0b7/Code-of-Conduct.md
+-rw-r--r--   0     1001      123     2386 2023-04-05 13:40:38.000000 maturin-1.0.0b7/Dockerfile
+-rw-r--r--   0     1001      123      245 2023-04-05 13:40:38.000000 maturin-1.0.0b7/MANIFEST.in
+-rw-r--r--   0     1001      123    16573 2023-04-05 13:40:38.000000 maturin-1.0.0b7/README.md
+-rw-r--r--   0     1001      123       16 2023-04-05 13:40:38.000000 maturin-1.0.0b7/clippy.toml
+-rw-r--r--   0     1001      123     9664 2023-04-05 13:40:38.000000 maturin-1.0.0b7/deny.toml
+-rw-r--r--   0     1001      123    10847 2023-04-05 13:40:38.000000 maturin-1.0.0b7/license-apache
+-rw-r--r--   0     1001      123     1051 2023-04-05 13:40:38.000000 maturin-1.0.0b7/license-mit
+-rw-r--r--   0     1001      123     6236 2023-04-05 13:40:38.000000 maturin-1.0.0b7/maturin/__init__.py
+-rw-r--r--   0     1001      123      956 2023-04-05 13:40:38.000000 maturin-1.0.0b7/maturin/__main__.py
+-rw-r--r--   0     1001      123     5162 2023-04-05 13:40:38.000000 maturin-1.0.0b7/maturin/import_hook.py
+-rw-r--r--   0     1001      123      200 2023-04-05 13:40:38.000000 maturin-1.0.0b7/netlify.toml
+-rw-r--r--   0     1001      123     2170 2023-04-05 13:40:38.000000 maturin-1.0.0b7/noxfile.py
+-rw-r--r--   0     1001      123     1290 2023-04-05 13:40:38.000000 maturin-1.0.0b7/pyproject.toml
+-rw-r--r--   0     1001      123     2868 2023-04-05 13:40:38.000000 maturin-1.0.0b7/setup.py
+-rw-r--r--   0     1001      123    19412 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/auditwheel/audit.rs
+-rw-r--r--   0     1001      123    53261 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/auditwheel/manylinux-policy.json
+-rw-r--r--   0     1001      123      242 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/auditwheel/mod.rs
+-rw-r--r--   0     1001      123     1862 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/auditwheel/musllinux-policy.json
+-rw-r--r--   0     1001      123     1389 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/auditwheel/musllinux.rs
+-rw-r--r--   0     1001      123     3777 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/auditwheel/patchelf.rs
+-rw-r--r--   0     1001      123     4602 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/auditwheel/platform_tag.rs
+-rw-r--r--   0     1001      123     5393 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/auditwheel/policy.rs
+-rw-r--r--   0     1001      123     1169 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/auditwheel/repair.rs
+-rw-r--r--   0     1001      123    47514 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/build_context.rs
+-rw-r--r--   0     1001      123    57254 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/build_options.rs
+-rw-r--r--   0     1001      123     5407 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/cargo_toml.rs
+-rw-r--r--   0     1001      123    33723 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/ci.rs
+-rw-r--r--   0     1001      123    23999 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/compile.rs
+-rw-r--r--   0     1001      123     8342 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/cross_compile.rs
+-rw-r--r--   0     1001      123     6119 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/develop.rs
+-rw-r--r--   0     1001      123     2233 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/lib.rs
+-rw-r--r--   0     1001      123    17816 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/main.rs
+-rw-r--r--   0     1001      123    32034 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/metadata.rs
+-rw-r--r--   0     1001      123    44938 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/module_writer.rs
+-rw-r--r--   0     1001      123     8203 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/new_project.rs
+-rw-r--r--   0     1001      123    16142 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/project_layout.rs
+-rw-r--r--   0     1001      123    16408 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/pyproject_toml.rs
+-rw-r--r--   0     1001      123    11820 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/python_interpreter/config.rs
+-rw-r--r--   0     1001      123     1595 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/python_interpreter/get_interpreter_metadata.py
+-rw-r--r--   0     1001      123    34577 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/python_interpreter/mod.rs
+-rw-r--r--   0     1001      123      443 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/python_interpreter/sysconfig-emscripten.json
+-rw-r--r--   0     1001      123     3861 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/python_interpreter/sysconfig-freebsd.json
+-rw-r--r--   0     1001      123    14124 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/python_interpreter/sysconfig-linux.json
+-rw-r--r--   0     1001      123     3812 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/python_interpreter/sysconfig-macos.json
+-rw-r--r--   0     1001      123      738 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/python_interpreter/sysconfig-netbsd.json
+-rw-r--r--   0     1001      123     2353 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/python_interpreter/sysconfig-openbsd.json
+-rw-r--r--   0     1001      123     3341 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/python_interpreter/sysconfig-windows.json
+-rw-r--r--   0     1001      123    30697 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/source_distribution.rs
+-rw-r--r--   0     1001      123    18478 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/target.rs
+-rw-r--r--   0     1001      123      686 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/templates/.gitignore.j2
+-rw-r--r--   0     1001      123      518 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/templates/Cargo.toml.j2
+-rw-r--r--   0     1001      123      149 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/templates/__init__.py.j2
+-rw-r--r--   0     1001      123      123 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/templates/build.rs.j2
+-rw-r--r--   0     1001      123       47 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/templates/example.udl.j2
+-rw-r--r--   0     1001      123      722 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/templates/lib.rs.j2
+-rw-r--r--   0     1001      123       45 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/templates/main.rs.j2
+-rw-r--r--   0     1001      123      859 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/templates/pyproject.toml.j2
+-rw-r--r--   0     1001      123    20146 2023-04-05 13:40:38.000000 maturin-1.0.0b7/src/upload.rs
+-rwxr-xr-x   0     1001      123      974 2023-04-05 13:40:38.000000 maturin-1.0.0b7/test-dockerfile.sh
+-rw-r--r--   0        0        0    17757 1970-01-01 00:00:00.000000 maturin-1.0.0b7/PKG-INFO
```

### Comparing `maturin-1.0.0b5/Cargo.toml` & `maturin-1.0.0b7/Cargo.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 [package]
 authors = ["konstin <konstin@mailbox.org>", "messense <messense@icloud.com>"]
 name = "maturin"
-version = "1.0.0-beta.5"
+version = "1.0.0-beta.7"
 description = "Build and publish crates with pyo3, rust-cpython and cffi bindings as well as rust binaries as python packages"
 exclude = ["test-crates/**/*", "sysconfig/*", "test-data/*", "ci/*", "tests/*", "guide/*", ".github/*"]
 homepage = "https://github.com/pyo3/maturin"
 readme = "README.md"
 repository = "https://github.com/pyo3/maturin"
 license = "MIT OR Apache-2.0"
 keywords = ["python", "cffi", "packaging", "pypi", "pyo3"]
 categories = ["api-bindings", "development-tools::ffi", "command-line-utilities"]
 edition = "2021"
-rust-version = "1.63"
+rust-version = "1.64"
 
 [[bin]]
 name = "maturin"
 
 [lib]
 name = "maturin"
 
@@ -43,52 +43,55 @@
 dirs = "4.0.0"
 fs-err = "2.5.0"
 fat-macho = { version = "0.4.6", default-features = false }
 once_cell = "1.7.2"
 rustc_version = "0.4.0"
 semver = "1.0.13"
 target-lexicon = "0.12.0"
-pyproject-toml = "0.3.3"
+indexmap = "1.9.3"
+pyproject-toml = "0.5.1"
 python-pkginfo = "0.5.5"
 textwrap = "0.16.0"
 ignore = "0.4.20"
 itertools = "0.10.5"
 lddtree = "0.3.2"
 cc = "1.0.72"
 dunce = "1.0.2"
 normpath = "1.0.0"
-pep440 = "0.2.0"
+pep440_rs = { version = "0.3.3", features = ["serde"] }
+pep508_rs = { version = "0.1.1", features = ["serde"] }
 time = "0.3.17"
 
 # cli
 clap = { version = "4.0.0", features = ["derive", "env", "wrap_help"] }
-clap_complete_command = { version = "0.4.0", optional = true }
+clap_complete_command = { version = "0.5.1", optional = true }
 
 # cross compile
-cargo-zigbuild = { version = "0.16.2", default-features = false, optional = true }
-cargo-xwin = { version = "0.14.1", default-features = false, optional = true }
+cargo-zigbuild = { version = "0.16.5", default-features = false, optional = true }
+cargo-xwin = { version = "0.14.2", default-features = false, optional = true }
 
 # log
 tracing = "0.1.36"
 tracing-subscriber = { version = "0.3.15", features = ["env-filter"], optional = true }
 
 # project scaffolding, maturin new/init/generate-ci
 dialoguer = { version = "0.10.2", default-features = false, optional = true }
 console = { version = "0.15.4", optional = true }
-minijinja = { version = "0.30.2", optional = true }
+minijinja = { version = "0.31.0", optional = true }
 
 # upload
 bytesize = { version = "1.0.1", optional = true }
 configparser = { version = "3.0.0", optional = true }
 multipart = { version = "0.18.0", features = ["client"], default-features = false, optional = true }
 ureq = { version = "2.6.1", features = ["gzip", "socks-proxy"], default-features = false, optional = true }
 native-tls = { version = "0.2.8", optional = true }
 rustls = { version = "0.20.8", optional = true }
 rustls-pemfile = { version = "1.0.1", optional = true }
 keyring = { version = "2.0.0", default-features = false, features = ["linux-no-secret-service"], optional = true }
+wild = { version = "2.1.0", optional = true }
 
 [dev-dependencies]
 indoc = "2.0.0"
 pretty_assertions = "1.3.0"
 rustversion = "1.0.9"
 time = { version = "0.3.17", features = ["macros"] }
 trycmd = "0.14.11"
@@ -99,15 +102,15 @@
 
 full = ["cli-completion", "cross-compile", "log", "scaffolding", "upload"]
 
 log = ["tracing-subscriber"]
 
 cli-completion = ["dep:clap_complete_command"]
 
-upload = ["ureq", "multipart", "configparser", "bytesize", "dialoguer/password"]
+upload = ["ureq", "multipart", "configparser", "bytesize", "dialoguer/password", "wild"]
 # keyring doesn't support *BSD so it's not enabled in `full` by default
 password-storage = ["upload", "keyring"]
 
 rustls = ["dep:rustls", "ureq?/tls", "cargo-xwin?/rustls-tls", "dep:rustls-pemfile"]
 native-tls = ["dep:native-tls", "ureq?/native-tls", "cargo-xwin?/native-tls", "dep:rustls-pemfile"]
 
 # cross compile using zig or xwin
```

### Comparing `maturin-1.0.0b5/.cirrus.yml` & `maturin-1.0.0b7/.cirrus.yml`

 * *Files 20% similar despite different names*

```diff
@@ -1,9 +1,12 @@
 env:
   RUST_BACKTRACE: 1
+  CARGO_INCREMENTAL: 0
+  CARGO_TERM_COLOR: always
+  CARGO_REGISTRIES_CRATES_IO_PROTOCOL: sparse
 
 build_and_test: &BUILD_AND_TEST
   # only run tasks on pull request or bors related branches
   only_if: $CIRRUS_BRANCH == 'staging' || $CIRRUS_BRANCH == 'trying' || $CIRRUS_PR != ""
   setup_script:
     - curl https://sh.rustup.rs -sSf --output rustup.sh
     - sh rustup.sh -y --default-toolchain stable
@@ -16,19 +19,14 @@
 
 freebsd_task:
   name: Test (x86_64 FreeBSD)
   freebsd_instance:
     image_family: freebsd-13-1
   env:
     PATH: $HOME/.cargo/bin:$PATH
-  registry_cache:
-    folder: $HOME/.cargo/registry
-    fingerprint_script:
-      - echo $CIRRUS_OS
-      - cat Cargo.lock
   target_cache:
     folder: target
     fingerprint_script:
       - echo $CIRRUS_OS
       - cat Cargo.lock
   install_script:
     - pkg install -y curl bash python
@@ -37,19 +35,14 @@
 
 macos_arm64_task:
   name: Test (arm64 macOS)
   macos_instance:
     image: ghcr.io/cirruslabs/macos-monterey-xcode
   env:
     PATH: $HOME/.cargo/bin:/opt/homebrew/opt/python@3.10/bin:$PATH
-  registry_cache:
-    folder: $HOME/.cargo/registry
-    fingerprint_script:
-      - echo $CIRRUS_OS
-      - cat Cargo.lock
   target_cache:
     folder: target
     fingerprint_script:
       - echo $CIRRUS_OS
       - cat Cargo.lock
   install_script:
     - brew install python3
@@ -60,19 +53,14 @@
   name: Test (arm64 Linux)
   arm_container:
     image: python:3.11
     cpu: 4
     memory: 4G
   env:
     PATH: /root/.cargo/bin:$PATH
-  registry_cache:
-    folder: /root/.cargo/registry
-    fingerprint_script:
-      - echo $CIRRUS_OS
-      - cat Cargo.lock
   target_cache:
     folder: target
     fingerprint_script:
       - echo $CIRRUS_OS
       - cat Cargo.lock
   install_script:
     - python3 -m pip install uniffi-bindgen==0.23.0
```

### Comparing `maturin-1.0.0b5/Cargo.lock` & `maturin-1.0.0b7/Cargo.lock`

 * *Files 1% similar despite different names*

```diff
@@ -6,23 +6,14 @@
 name = "adler"
 version = "1.0.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "f26201604c87b1e01bd3d98f8d5d9a8fcbb815e8cedb41ffccbeb4bf593a35fe"
 
 [[package]]
 name = "ahash"
-version = "0.3.8"
-source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "e8fd72866655d1904d6b0997d0b07ba561047d070fbe29de039031c641b61217"
-dependencies = [
- "const-random",
-]
-
-[[package]]
-name = "ahash"
 version = "0.7.6"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "fcb51a0695d8f838b1ee009b3fbf66bda078cd64590202a864a8f3e8c4315c47"
 dependencies = [
  "getrandom",
  "once_cell",
  "version_check",
@@ -35,31 +26,37 @@
 checksum = "cc936419f96fa211c1b9166887b38e5e40b19958e5b895be7c1f93adec7071ac"
 dependencies = [
  "memchr",
 ]
 
 [[package]]
 name = "anyhow"
-version = "1.0.69"
+version = "1.0.70"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "224afbd727c3d6e4b90103ece64b8d1b67fbb1973b1046c2281eed3f3803f800"
+checksum = "7de8ce5e0f9f8d88245311066a578d72b7af3e7088f32783804676302df237e4"
 
 [[package]]
 name = "autocfg"
 version = "1.1.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "d468802bab17cbc0cc575e9b053f41e72aa36bfa6b7f55e3529ffa43161b97fa"
 
 [[package]]
 name = "base64"
 version = "0.13.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "9e1b586273c5702936fe7b7d6896644d8be71e6314cfe09d3167c95f712589e8"
 
 [[package]]
+name = "base64"
+version = "0.21.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "a4a4ddaa51a5bc52a6948f74c06d20aaaddb71924eab79b8c97a8c556e942d6a"
+
+[[package]]
 name = "bitflags"
 version = "1.3.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "bef38d45163c2f1dde094a7dfd33ccf595c92905c8f8f4fdc18d06fb1037718a"
 
 [[package]]
 name = "block-buffer"
@@ -68,17 +65,17 @@
 checksum = "3078c7629b62d3f0439517fa394996acacc5cbc91c5a20d8c658e77abd503a71"
 dependencies = [
  "generic-array",
 ]
 
 [[package]]
 name = "bstr"
-version = "1.3.0"
+version = "1.4.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "5ffdb39cb703212f3c11973452c2861b972f757b021158f3516ba10f2fa8b2c1"
+checksum = "c3d4260bcc2e8fc9df1eac4919a720effeb63a3f0952f5bf4944adfa18897f09"
 dependencies = [
  "memchr",
  "serde",
 ]
 
 [[package]]
 name = "bumpalo"
@@ -153,15 +150,15 @@
 checksum = "0bd8e990edcbebfd43b4d62cb73d4e17e412a1c66a320a393c1de16ff7aa2137"
 dependencies = [
  "cfg-expr",
  "home",
  "once_cell",
  "serde",
  "shell-escape",
- "toml 0.7.2",
+ "toml 0.7.3",
 ]
 
 [[package]]
 name = "cargo-options"
 version = "0.6.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "9b8e8daa6b2b84aa7cccd57317d9a9b36d969d75bb95923471f4eabbd36f2955"
@@ -176,17 +173,17 @@
 checksum = "cbdb825da8a5df079a43676dbe042702f1707b1109f713a01420fbb4cc71fa27"
 dependencies = [
  "serde",
 ]
 
 [[package]]
 name = "cargo-xwin"
-version = "0.14.1"
+version = "0.14.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "ba1bcd2410f6880b9a8c78bfd84c3b2be72664dd9b030dbe367e618177f02dc9"
+checksum = "00ba77651e6b8d879367dbc0d081dbbae4f44827f0b4d59ea03a790777f5069c"
 dependencies = [
  "anyhow",
  "cargo-config2",
  "cargo-options",
  "clap",
  "dirs",
  "fs-err",
@@ -194,17 +191,17 @@
  "path-slash",
  "which",
  "xwin",
 ]
 
 [[package]]
 name = "cargo-zigbuild"
-version = "0.16.3"
+version = "0.16.5"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "a096a03500098b67a3360991910fb0578f58381a7d5a5e41ab11eaccc6a1f8f7"
+checksum = "91857f14adb5098836a45766d7194d7fa1e24cd1a749e233df843a4451b02091"
 dependencies = [
  "anyhow",
  "cargo-options",
  "cargo_metadata",
  "clap",
  "dirs",
  "fs-err",
@@ -283,91 +280,103 @@
 
 [[package]]
 name = "charset"
 version = "0.1.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "18e9079d1a12a2cc2bffb5db039c43661836ead4082120d5844f02555aca2d46"
 dependencies = [
- "base64",
+ "base64 0.13.1",
  "encoding_rs",
 ]
 
 [[package]]
 name = "chumsky"
-version = "0.8.0"
+version = "0.9.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "8d02796e4586c6c41aeb68eae9bfb4558a522c35f1430c14b40136c3706e09e4"
+checksum = "23170228b96236b5a7299057ac284a321457700bc8c41a4476052f0f4ba5349d"
 dependencies = [
- "ahash 0.3.8",
+ "hashbrown",
+ "stacker",
 ]
 
 [[package]]
 name = "clap"
-version = "4.0.32"
+version = "4.1.10"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "a7db700bc935f9e43e88d00b0850dae18a63773cfbec6d8e070fccf7fef89a39"
+checksum = "ce38afc168d8665cfc75c7b1dd9672e50716a137f433f070991619744a67342a"
 dependencies = [
  "bitflags",
  "clap_derive",
  "clap_lex",
  "is-terminal",
  "once_cell",
  "strsim",
  "termcolor",
  "terminal_size",
 ]
 
 [[package]]
 name = "clap_complete"
-version = "4.0.7"
+version = "4.1.6"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "10861370d2ba66b0f5989f83ebf35db6421713fd92351790e7fdd6c36774c56b"
+checksum = "40d3120a421cd111c43f1a6c7d0dd83bb6aaa0659c164468a1654014632a5ec6"
 dependencies = [
  "clap",
 ]
 
 [[package]]
 name = "clap_complete_command"
-version = "0.4.0"
+version = "0.5.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "4160b4a4f72ef58bd766bad27c09e6ef1cc9d82a22f6a0f55d152985a4a48e31"
+checksum = "183495371ea78d4c9ff638bfc6497d46fed2396e4f9c50aebc1278a4a9919a3d"
 dependencies = [
  "clap",
  "clap_complete",
  "clap_complete_fig",
+ "clap_complete_nushell",
 ]
 
 [[package]]
 name = "clap_complete_fig"
-version = "4.0.2"
+version = "4.1.2"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "2171bc6242ad7a1801422bff039574449b5bd832b715222e500714ce10f91a54"
+dependencies = [
+ "clap",
+ "clap_complete",
+]
+
+[[package]]
+name = "clap_complete_nushell"
+version = "0.1.10"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "46b30e010e669cd021e5004f3be26cff6b7c08d2a8a0d65b48d43a8cc0efd6c3"
+checksum = "c7fa41f5e6aa83bd151b70fd0ceaee703d68cd669522795dc812df9edad1252c"
 dependencies = [
  "clap",
  "clap_complete",
 ]
 
 [[package]]
 name = "clap_derive"
-version = "4.0.21"
+version = "4.1.9"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "0177313f9f02afc995627906bbd8967e2be069f5261954222dac78290c2b9014"
+checksum = "fddf67631444a3a3e3e5ac51c36a5e01335302de677bd78759eaa90ab1f46644"
 dependencies = [
  "heck",
  "proc-macro-error",
  "proc-macro2",
  "quote",
  "syn",
 ]
 
 [[package]]
 name = "clap_lex"
-version = "0.3.0"
+version = "0.3.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "0d4198f73e42b4936b35b5bb248d81d2b595ecb170da0bac7655c54eedfa8da8"
+checksum = "033f6b7a4acb1f358c742aaca805c939ee73b4c6209ae4318ec7aca81c42e646"
 dependencies = [
  "os_str_bytes",
 ]
 
 [[package]]
 name = "cli-table"
 version = "0.4.7"
@@ -411,36 +420,14 @@
  "lazy_static",
  "libc",
  "unicode-width",
  "windows-sys",
 ]
 
 [[package]]
-name = "const-random"
-version = "0.1.15"
-source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "368a7a772ead6ce7e1de82bfb04c485f3db8ec744f72925af5735e29a22cc18e"
-dependencies = [
- "const-random-macro",
- "proc-macro-hack",
-]
-
-[[package]]
-name = "const-random-macro"
-version = "0.1.15"
-source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "9d7d6ab3c3a2282db210df5f02c4dab6e0a7057af0fb7ebd4070f30fe05c0ddb"
-dependencies = [
- "getrandom",
- "once_cell",
- "proc-macro-hack",
- "tiny-keccak",
-]
-
-[[package]]
 name = "content_inspector"
 version = "0.2.4"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "b7bda66e858c683005a53a9a60c69a4aca7eeaa45d124526e389f7aec8e62f38"
 dependencies = [
  "memchr",
 ]
@@ -519,20 +506,14 @@
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "3c063cd8cc95f5c377ed0d4b49a4b21f632396ff690e8470c29b3359b346984b"
 dependencies = [
  "cfg-if",
 ]
 
 [[package]]
-name = "crunchy"
-version = "0.2.2"
-source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "7a81dae078cea95a014a339291cec439d2f232ebe854a9d672b796c6afafa9b7"
-
-[[package]]
 name = "crypto-common"
 version = "0.1.6"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "1bfb12502f3fc46cca1bb51ac28df9d618d813cdc3d2f25b9fe775a34af26bb3"
 dependencies = [
  "generic-array",
  "typenum",
@@ -723,17 +704,17 @@
 name = "fs-err"
 version = "2.9.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "0845fa252299212f0389d64ba26f34fa32cfe41588355f21ed507c59a0f64541"
 
 [[package]]
 name = "generic-array"
-version = "0.14.6"
+version = "0.14.7"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "bff49e947297f3312447abdca79f45f4738097cc82b06e72054d2223f601f1b9"
+checksum = "85649ca51fd72272d7821adaf274ad91c288277713d9c18820d8499a7ff69e9a"
 dependencies = [
  "typenum",
  "version_check",
 ]
 
 [[package]]
 name = "getrandom"
@@ -778,15 +759,15 @@
 
 [[package]]
 name = "hashbrown"
 version = "0.12.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "8a9ee70c43aaf417c914396645a0fa852624801b24ebb7ae78fe8272889ac888"
 dependencies = [
- "ahash 0.7.6",
+ "ahash",
 ]
 
 [[package]]
 name = "heck"
 version = "0.4.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "95505c38b4572b2d910cecb0281560f54b440a19336cbbcb27bf6ce6adc6f5a8"
@@ -850,20 +831,21 @@
  "thread_local",
  "walkdir",
  "winapi-util",
 ]
 
 [[package]]
 name = "indexmap"
-version = "1.9.2"
+version = "1.9.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "1885e79c1fc4b10f0e172c475f458b7f7b93061064d98c3293e98c5ba0c8b399"
+checksum = "bd070e393353796e801d209ad339e89596eb4c8d430d18ede6a1cced8fafbd99"
 dependencies = [
  "autocfg",
  "hashbrown",
+ "serde",
 ]
 
 [[package]]
 name = "indicatif"
 version = "0.17.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "cef509aa9bc73864d6756f0d34d35504af3cf0844373afe9b8669a5b8005a729"
@@ -1030,18 +1012,18 @@
 checksum = "8263075bb86c5a1b1427b5ae862e8889656f126e9f77c484496e8b47cf5c5558"
 dependencies = [
  "regex-automata",
 ]
 
 [[package]]
 name = "maturin"
-version = "1.0.0-beta.5"
+version = "1.0.0-beta.7"
 dependencies = [
  "anyhow",
- "base64",
+ "base64 0.13.1",
  "bytesize",
  "cargo-config2",
  "cargo-options",
  "cargo-xwin",
  "cargo-zigbuild",
  "cargo_metadata",
  "cbindgen",
@@ -1055,24 +1037,26 @@
  "dunce",
  "fat-macho",
  "flate2",
  "fs-err",
  "glob",
  "goblin",
  "ignore",
+ "indexmap",
  "indoc",
  "itertools",
  "keyring",
  "lddtree",
  "minijinja",
  "multipart",
  "native-tls",
  "normpath",
  "once_cell",
- "pep440",
+ "pep440_rs",
+ "pep508_rs",
  "platform-info",
  "pretty_assertions",
  "pyproject-toml",
  "python-pkginfo",
  "regex",
  "rustc_version",
  "rustls",
@@ -1084,21 +1068,22 @@
  "sha2",
  "tar",
  "target-lexicon",
  "tempfile",
  "textwrap",
  "thiserror",
  "time",
- "toml 0.7.2",
+ "toml 0.7.3",
  "toml_edit",
  "tracing",
  "tracing-subscriber",
  "trycmd",
  "ureq",
  "which",
+ "wild",
  "zip",
 ]
 
 [[package]]
 name = "memchr"
 version = "2.5.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
@@ -1111,33 +1096,33 @@
 checksum = "d61c719bcfbcf5d62b3a09efa6088de8c54bc0bfcd3ea7ae39fcc186108b8de1"
 dependencies = [
  "autocfg",
 ]
 
 [[package]]
 name = "mime"
-version = "0.3.16"
+version = "0.3.17"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "2a60c7ce501c71e03a9c9c0d35b861413ae925bd979cc7a4e30d060069aaac8d"
+checksum = "6877bb514081ee2a7ff5ef9de3281f14a4dd4bceac4c09388074a6b5df8a139a"
 
 [[package]]
 name = "mime_guess"
 version = "2.0.4"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "4192263c238a5f0d0c6bfd21f336a313a4ce1c450542449ca191bb657b4642ef"
 dependencies = [
  "mime",
  "unicase",
 ]
 
 [[package]]
 name = "minijinja"
-version = "0.30.6"
+version = "0.31.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "650266e616c4634fd6c188a410886e8700689fe78197f54d194a9ed560863f94"
+checksum = "673d1ece89f7e166f43270800d78f9b1a9d21fda92dbcfa3b98b21213cdccbbc"
 dependencies = [
  "serde",
 ]
 
 [[package]]
 name = "minimal-lexical"
 version = "0.2.1"
@@ -1251,17 +1236,17 @@
 name = "once_cell"
 version = "1.17.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "b7e5500299e16ebb147ae15a00a942af264cf3688f47923b8fc2cd5858f23ad3"
 
 [[package]]
 name = "openssl"
-version = "0.10.45"
+version = "0.10.48"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "b102428fd03bc5edf97f62620f7298614c45cedf287c271e7ed450bbaf83f2e1"
+checksum = "518915b97df115dd36109bfa429a48b8f737bd05508cf9588977b599648926d2"
 dependencies = [
  "bitflags",
  "cfg-if",
  "foreign-types",
  "libc",
  "once_cell",
  "openssl-macros",
@@ -1292,17 +1277,17 @@
 checksum = "1ef9a9cc6ea7d9d5e7c4a913dc4b48d0e359eddf01af1dfec96ba7064b4aba10"
 dependencies = [
  "cc",
 ]
 
 [[package]]
 name = "openssl-sys"
-version = "0.9.80"
+version = "0.9.83"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "23bbbf7854cd45b83958ebe919f0e8e516793727652e27fda10a8384cfc790b7"
+checksum = "666416d899cf077260dac8698d60a60b435a46d57e82acb1be3d0dad87284e5b"
 dependencies = [
  "autocfg",
  "cc",
  "libc",
  "openssl-src",
  "pkg-config",
  "vcpkg",
@@ -1316,17 +1301,17 @@
 dependencies = [
  "libc",
  "windows-sys",
 ]
 
 [[package]]
 name = "os_str_bytes"
-version = "6.4.1"
+version = "6.5.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "9b7820b9daea5457c9f21c69448905d723fbd21136ccf521748f23fd49e723ee"
+checksum = "ceedf44fb00f2d1984b0bc98102627ce622e083e49a5bacdb3e514fa4238e267"
 
 [[package]]
 name = "output_vt100"
 version = "0.1.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "628223faebab4e3e40667ee0b2336d34a5b960ff60ea743ddfdbcf7770bcfb66"
 dependencies = [
@@ -1365,21 +1350,40 @@
 [[package]]
 name = "path-slash"
 version = "0.2.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "1e91099d4268b0e11973f036e885d652fb0b21fedcf69738c627f94db6a44f42"
 
 [[package]]
-name = "pep440"
-version = "0.2.0"
+name = "pep440_rs"
+version = "0.3.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "8841b00ca6fabc903e8ecd496d9611db402e23f15e3d19b0b587e2ca653abd89"
+checksum = "d0cbf1fd438eeb1b1e42e8390951ec90d1cf87bbe3d3305b28551bca30b7595a"
 dependencies = [
  "lazy_static",
  "regex",
+ "serde",
+ "tracing",
+ "unicode-width",
+]
+
+[[package]]
+name = "pep508_rs"
+version = "0.1.1"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "e566191336ac8cf72db45240583769ab9fb75bd87dd9544cd96a9bc7e28585c4"
+dependencies = [
+ "once_cell",
+ "pep440_rs",
+ "regex",
+ "serde",
+ "thiserror",
+ "tracing",
+ "unicode-width",
+ "url",
 ]
 
 [[package]]
 name = "percent-encoding"
 version = "2.2.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "478c572c3d73181ff3c2539045f6eb99e5491218eae919370993b890cdbdd98e"
@@ -1457,36 +1461,42 @@
 dependencies = [
  "proc-macro2",
  "quote",
  "version_check",
 ]
 
 [[package]]
-name = "proc-macro-hack"
-version = "0.5.20+deprecated"
+name = "proc-macro2"
+version = "1.0.54"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "dc375e1527247fe1a97d8b7156678dfe7c1af2fc075c9a4db3690ecd2a148068"
+checksum = "e472a104799c74b514a57226160104aa483546de37e839ec50e3c2e41dd87534"
+dependencies = [
+ "unicode-ident",
+]
 
 [[package]]
-name = "proc-macro2"
-version = "1.0.51"
+name = "psm"
+version = "0.1.21"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "5d727cae5b39d21da60fa540906919ad737832fe0b1c165da3a34d6548c849d6"
+checksum = "5787f7cda34e3033a72192c018bc5883100330f362ef279a8cbccfce8bb4e874"
 dependencies = [
- "unicode-ident",
+ "cc",
 ]
 
 [[package]]
 name = "pyproject-toml"
-version = "0.3.3"
+version = "0.5.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "ee8476266c07b589d6ed54c761181466f4e4092107869be49ae26b3c0cdde8db"
+checksum = "71c24ad9fa3f11e0b5f45bf86ea6e1ae4dfef288fb7b077a15b6a19ebc87a37f"
 dependencies = [
+ "indexmap",
+ "pep440_rs",
+ "pep508_rs",
  "serde",
- "toml 0.7.2",
+ "toml 0.7.3",
 ]
 
 [[package]]
 name = "python-pkginfo"
 version = "0.5.5"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "0b8cf2d8981a1c967eebacac69c68a54d9786c1b84b813841d0aab2994705608"
@@ -1498,17 +1508,17 @@
  "tar",
  "thiserror",
  "zip",
 ]
 
 [[package]]
 name = "quote"
-version = "1.0.23"
+version = "1.0.26"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "8856d8364d252a14d474036ea1358d63c9e6965c8e5c1885c18f73d70bff9c7b"
+checksum = "4424af4bf778aae2051a77b60283332f386554255d722233d09fbfc7e30da2fc"
 dependencies = [
  "proc-macro2",
 ]
 
 [[package]]
 name = "quoted_printable"
 version = "0.4.7"
@@ -1585,17 +1595,17 @@
  "getrandom",
  "redox_syscall",
  "thiserror",
 ]
 
 [[package]]
 name = "regex"
-version = "1.7.1"
+version = "1.7.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "48aaa5748ba571fb95cd2c85c09f629215d3a6ece942baa100950af03a34f733"
+checksum = "8b1f693b24f6ac912f4893ef08244d70b6067480d2f1a46e950c9691e6749d1d"
 dependencies = [
  "aho-corasick",
  "memchr",
  "regex-syntax",
 ]
 
 [[package]]
@@ -1605,25 +1615,25 @@
 checksum = "6c230d73fb8d8c1b9c0b3135c5142a8acee3a0558fb8db5cf1cb65f8d7862132"
 dependencies = [
  "regex-syntax",
 ]
 
 [[package]]
 name = "regex-syntax"
-version = "0.6.28"
+version = "0.6.29"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "456c603be3e8d448b072f410900c09faf164fbce2d480456f50eea6e25f9c848"
+checksum = "f162c6dd7b008981e4d40210aca20b4bd0f9b60ca9271061b07f78537722f2e1"
 
 [[package]]
 name = "rfc2047-decoder"
-version = "0.2.1"
+version = "0.2.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "6e0df53c9deb8931ce779840148cda205fd17475ce59193ff7f8d136ef755481"
+checksum = "61fc4b4e52897c3e30b12b7e9b04461215b647fbe66f6def60dd8edbce14ec2e"
 dependencies = [
- "base64",
+ "base64 0.21.0",
  "charset",
  "chumsky",
  "memchr",
  "quoted_printable",
  "thiserror",
 ]
 
@@ -1675,19 +1685,19 @@
  "ring",
  "sct",
  "webpki",
 ]
 
 [[package]]
 name = "rustls-pemfile"
-version = "1.0.1"
+version = "1.0.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "0864aeff53f8c05aa08d86e5ef839d3dfcf07aeba2db32f12db0ef716e87bd55"
+checksum = "d194b56d58803a43635bdc398cd17e383d6f71f9182b9a192c127ca42494a59b"
 dependencies = [
- "base64",
+ "base64 0.21.0",
 ]
 
 [[package]]
 name = "rustversion"
 version = "1.0.12"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "4f3208ce4d8448b3f3e7d168a73f5e0c43a61e32930de3bceeccedb388b6bf06"
@@ -1773,17 +1783,17 @@
 dependencies = [
  "core-foundation-sys",
  "libc",
 ]
 
 [[package]]
 name = "semver"
-version = "1.0.16"
+version = "1.0.17"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "58bc9567378fc7690d6b2addae4e60ac2eeea07becb2c64b9f218b53865cba2a"
+checksum = "bebd363326d05ec3e2f532ab7660680f3b02130d780c299bca73469d521bc0ed"
 dependencies = [
  "serde",
 ]
 
 [[package]]
 name = "serde"
 version = "1.0.155"
@@ -1802,17 +1812,17 @@
  "proc-macro2",
  "quote",
  "syn",
 ]
 
 [[package]]
 name = "serde_json"
-version = "1.0.94"
+version = "1.0.95"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "1c533a59c9d8a93a09c6ab31f0fd5e5f4dd1b8fc9434804029839884765d04ea"
+checksum = "d721eca97ac802aa7777b701877c8004d950fc142651367300d21c1cc0194744"
 dependencies = [
  "itoa",
  "ryu",
  "serde",
 ]
 
 [[package]]
@@ -1922,14 +1932,27 @@
 [[package]]
 name = "spin"
 version = "0.5.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "6e63cff320ae2c57904679ba7cb63280a3dc4613885beafb148ee7bf9aa9042d"
 
 [[package]]
+name = "stacker"
+version = "0.1.15"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "c886bd4480155fd3ef527d45e9ac8dd7118a898a46530b7b94c3e21866259fce"
+dependencies = [
+ "cc",
+ "cfg-if",
+ "libc",
+ "psm",
+ "winapi",
+]
+
+[[package]]
 name = "static_assertions"
 version = "1.1.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "a2eb9349b6444b326872e140eb1cf5e7c522154d69e7a0ffb0fb81c06b37543f"
 
 [[package]]
 name = "strsim"
@@ -2061,23 +2084,14 @@
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "fd80a657e71da814b8e5d60d3374fc6d35045062245d80224748ae522dd76f36"
 dependencies = [
  "time-core",
 ]
 
 [[package]]
-name = "tiny-keccak"
-version = "2.0.2"
-source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "2c9d3793400a45f954c52e73d068316d76b6f4e36977e3fcebb13a2721e80237"
-dependencies = [
- "crunchy",
-]
-
-[[package]]
 name = "tinyvec"
 version = "1.6.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "87cc5ceb3875bb20c2890005a4e226a4651264a5c75edb2421b52861a0a0cb50"
 dependencies = [
  "tinyvec_macros",
 ]
@@ -2095,17 +2109,17 @@
 checksum = "f4f7f0dd8d50a853a531c426359045b1998f04219d88799810762cd4ad314234"
 dependencies = [
  "serde",
 ]
 
 [[package]]
 name = "toml"
-version = "0.7.2"
+version = "0.7.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "f7afcae9e3f0fe2c370fd4657108972cbb2fa9db1b9f84849cefd80741b01cb6"
+checksum = "b403acf6f2bb0859c93c7f0d967cb4a75a7ac552100f9322faf64dc047669b21"
 dependencies = [
  "serde",
  "serde_spanned",
  "toml_datetime",
  "toml_edit",
 ]
 
@@ -2116,17 +2130,17 @@
 checksum = "3ab8ed2edee10b50132aed5f331333428b011c99402b5a534154ed15746f9622"
 dependencies = [
  "serde",
 ]
 
 [[package]]
 name = "toml_edit"
-version = "0.19.4"
+version = "0.19.8"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "9a1eb0622d28f4b9c90adc4ea4b2b46b47663fde9ac5fafcb14a1369d5508825"
+checksum = "239410c8609e8125456927e6707163a3b1fdb40561e4b803bc041f466ccfdc13"
 dependencies = [
  "indexmap",
  "serde",
  "serde_spanned",
  "toml_datetime",
  "winnow",
 ]
@@ -2134,14 +2148,15 @@
 [[package]]
 name = "tracing"
 version = "0.1.37"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "8ce8c33a8d48bd45d624a6e523445fd21ec13d3653cd51f681abf67418f54eb8"
 dependencies = [
  "cfg-if",
+ "log",
  "pin-project-lite",
  "tracing-attributes",
  "tracing-core",
 ]
 
 [[package]]
 name = "tracing-attributes"
@@ -2246,17 +2261,17 @@
 checksum = "50f37be617794602aabbeee0be4f259dc1778fabe05e2d67ee8f79326d5cb4f6"
 dependencies = [
  "version_check",
 ]
 
 [[package]]
 name = "unicode-bidi"
-version = "0.3.11"
+version = "0.3.13"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "524b68aca1d05e03fdf03fcdce2c6c94b6daf6d16861ddaa7e4f2b6638a9052c"
+checksum = "92888ba5573ff080736b3648696b70cafad7d250551175acbaa4e0385b3e1460"
 
 [[package]]
 name = "unicode-ident"
 version = "1.0.8"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "e5464a87b239f13a63a501f2701565754bae92d243d4bb7eb12f6d57d2269bf4"
 
@@ -2293,15 +2308,15 @@
 
 [[package]]
 name = "ureq"
 version = "2.6.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "338b31dd1314f68f3aabf3ed57ab922df95ffcd902476ca7ba3c4ce7b908c46d"
 dependencies = [
- "base64",
+ "base64 0.13.1",
  "flate2",
  "log",
  "native-tls",
  "once_cell",
  "rustls",
  "socks",
  "url",
@@ -2314,14 +2329,15 @@
 version = "2.3.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "0d68c799ae75762b8c3fe375feb6600ef5602c883c5d21eb51c09f22b83c4643"
 dependencies = [
  "form_urlencoded",
  "idna",
  "percent-encoding",
+ "serde",
 ]
 
 [[package]]
 name = "uuid"
 version = "1.3.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "1674845326ee10d37ca60470760d4288a6f80f304007d92e5c53bab78c9cfd79"
@@ -2361,20 +2377,19 @@
 checksum = "9f200f5b12eb75f8c1ed65abd4b2db8a6e1b138a20de009dacee265a2498f3f6"
 dependencies = [
  "libc",
 ]
 
 [[package]]
 name = "walkdir"
-version = "2.3.2"
+version = "2.3.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "808cf2735cd4b6866113f648b791c6adc5714537bc222d9347bb203386ffda56"
+checksum = "36df944cda56c7d8d8b7496af378e6b16de9284591917d307c9b4d313c44e698"
 dependencies = [
  "same-file",
- "winapi",
  "winapi-util",
 ]
 
 [[package]]
 name = "wasi"
 version = "0.11.0+wasi-snapshot-preview1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
@@ -2471,14 +2486,23 @@
 dependencies = [
  "either",
  "libc",
  "once_cell",
 ]
 
 [[package]]
+name = "wild"
+version = "2.1.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "05b116685a6be0c52f5a103334cbff26db643826c7b3735fc0a3ba9871310a74"
+dependencies = [
+ "glob",
+]
+
+[[package]]
 name = "winapi"
 version = "0.3.9"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "5c839a674fcd7a98952e593242ea400abe93992746761e38641405d28b00f419"
 dependencies = [
  "winapi-i686-pc-windows-gnu",
  "winapi-x86_64-pc-windows-gnu",
@@ -2518,59 +2542,59 @@
  "windows_x86_64_gnu",
  "windows_x86_64_gnullvm",
  "windows_x86_64_msvc",
 ]
 
 [[package]]
 name = "windows_aarch64_gnullvm"
-version = "0.42.1"
+version = "0.42.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "8c9864e83243fdec7fc9c5444389dcbbfd258f745e7853198f365e3c4968a608"
+checksum = "597a5118570b68bc08d8d59125332c54f1ba9d9adeedeef5b99b02ba2b0698f8"
 
 [[package]]
 name = "windows_aarch64_msvc"
-version = "0.42.1"
+version = "0.42.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "4c8b1b673ffc16c47a9ff48570a9d85e25d265735c503681332589af6253c6c7"
+checksum = "e08e8864a60f06ef0d0ff4ba04124db8b0fb3be5776a5cd47641e942e58c4d43"
 
 [[package]]
 name = "windows_i686_gnu"
-version = "0.42.1"
+version = "0.42.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "de3887528ad530ba7bdbb1faa8275ec7a1155a45ffa57c37993960277145d640"
+checksum = "c61d927d8da41da96a81f029489353e68739737d3beca43145c8afec9a31a84f"
 
 [[package]]
 name = "windows_i686_msvc"
-version = "0.42.1"
+version = "0.42.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "bf4d1122317eddd6ff351aa852118a2418ad4214e6613a50e0191f7004372605"
+checksum = "44d840b6ec649f480a41c8d80f9c65108b92d89345dd94027bfe06ac444d1060"
 
 [[package]]
 name = "windows_x86_64_gnu"
-version = "0.42.1"
+version = "0.42.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "c1040f221285e17ebccbc2591ffdc2d44ee1f9186324dd3e84e99ac68d699c45"
+checksum = "8de912b8b8feb55c064867cf047dda097f92d51efad5b491dfb98f6bbb70cb36"
 
 [[package]]
 name = "windows_x86_64_gnullvm"
-version = "0.42.1"
+version = "0.42.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "628bfdf232daa22b0d64fdb62b09fcc36bb01f05a3939e20ab73aaf9470d0463"
+checksum = "26d41b46a36d453748aedef1486d5c7a85db22e56aff34643984ea85514e94a3"
 
 [[package]]
 name = "windows_x86_64_msvc"
-version = "0.42.1"
+version = "0.42.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "447660ad36a13288b1db4d4248e857b510e8c3a225c822ba4fb748c0aafecffd"
+checksum = "9aec5da331524158c6d1a4ac0ab1541149c0b9505fde06423b02f5ef0106b9f0"
 
 [[package]]
 name = "winnow"
-version = "0.3.3"
+version = "0.4.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "faf09497b8f8b5ac5d3bb4d05c0a99be20f26fd3d5f2db7b0716e946d5103658"
+checksum = "ae8970b36c66498d8ff1d66685dc86b91b29db0c7739899012f63a63814b4b28"
 dependencies = [
  "memchr",
 ]
 
 [[package]]
 name = "xattr"
 version = "0.2.3"
@@ -2578,17 +2602,17 @@
 checksum = "6d1526bbe5aaeb5eb06885f4d987bcdfa5e23187055de9b83fe00156a821fabc"
 dependencies = [
  "libc",
 ]
 
 [[package]]
 name = "xwin"
-version = "0.2.11"
+version = "0.2.12"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "83f1b72807711ddc86bdda6f97b9bb9be127a3055604da7cdc1e6527aed1a942"
+checksum = "1f5f72397389fd26dd36b01f23e19c0608db8e764f7bb65fdc5b1e7e2aa02550"
 dependencies = [
  "anyhow",
  "bytes",
  "cab",
  "camino",
  "clap",
  "cli-table",
```

### Comparing `maturin-1.0.0b5/Changelog.md` & `maturin-1.0.0b7/Changelog.md`

 * *Files 2% similar despite different names*

```diff
@@ -10,17 +10,24 @@
 * **Breaking Change**: Build with `--no-default-features` by default when bootstrapping from sdist in [#1333](https://github.com/PyO3/maturin/pull/1333)
 * **Breaking Change**: Remove deprecated `sdist-include` option in `pyproject.toml` in [#1335](https://github.com/PyO3/maturin/pull/1335)
 * **Breaking Change**: Remove deprecated `python-source` option in `Cargo.toml` in [#1335](https://github.com/PyO3/maturin/pull/1335)
 * **Breaking Change**: Turn `patchelf` version warning into a hard error in [#1335](https://github.com/PyO3/maturin/pull/1335)
 * **Breaking Change**: [`uniffi_bindgen` CLI](https://mozilla.github.io/uniffi-rs/tutorial/Prerequisites.html#the-uniffi-bindgen-cli-tool) is required for building `uniffi` bindings wheels in [#1352](https://github.com/PyO3/maturin/pull/1352)
 * Add Cargo compile targets configuration for filtering multiple bin targets in [#1339](https://github.com/PyO3/maturin/pull/1339)
 * Respect `rustflags` settings in cargo configuration file in [#1405](https://github.com/PyO3/maturin/pull/1405)
-* Bump MSRV to 1.63.0 in [#1407](https://github.com/PyO3/maturin/pull/1407)
 * Add support for uniffi 0.23 in [#1481](https://github.com/PyO3/maturin/pull/1481)
 * Add support for custom TLS certificate authority bundle in [#1483](https://github.com/PyO3/maturin/pull/1483)
+* Bump MSRV to 1.64.0 in [#1528](https://github.com/PyO3/maturin/pull/1528)
+* Add wildcards support to publish/upload commands on Windows in [#1534](https://github.com/PyO3/maturin/pull/1534)
+* Add support for configuring macOS deployment target version in `pyproject.toml` in [#1536](https://github.com/PyO3/maturin/pull/1536)
+* Fix wrong `EXT_SUFFIX` when cross compiling musllinux wheels for Python 3.11 in [#1560](https://github.com/PyO3/maturin/pull/1560)
+
+## [0.14.16] - 2023-03-26
+
+* Deprecate `package.metadata.maturin.name` in favor of `tool.maturin.module-name` in `pyproject.toml` in [#1531](https://github.com/PyO3/maturin/pull/1531)
 
 ## [0.14.15] - 2023-03-03
 
 * Add sdist and sccache support to `generate-ci` command
 
 ## [0.14.14] - 2023-02-24
 
@@ -833,15 +840,16 @@
 
  * Show a progress bar for cargo's compile progress
 
 ## 0.1.0 - 2018-08-22
 
  * Initial Release
 
-[Unreleased]: https://github.com/pyo3/maturin/compare/v0.14.15...HEAD
+[Unreleased]: https://github.com/pyo3/maturin/compare/v0.14.16...HEAD
+[0.14.16]: https://github.com/pyo3/maturin/compare/v0.14.15...v0.14.16
 [0.14.15]: https://github.com/pyo3/maturin/compare/v0.14.14...v0.14.15
 [0.14.14]: https://github.com/pyo3/maturin/compare/v0.14.13...v0.14.14
 [0.14.13]: https://github.com/pyo3/maturin/compare/v0.14.12...v0.14.13
 [0.14.12]: https://github.com/pyo3/maturin/compare/v0.14.11...v0.14.12
 [0.14.11]: https://github.com/pyo3/maturin/compare/v0.14.10...v0.14.11
 [0.14.10]: https://github.com/pyo3/maturin/compare/v0.14.9...v0.14.10
 [0.14.9]: https://github.com/pyo3/maturin/compare/v0.14.8...v0.14.9
```

### Comparing `maturin-1.0.0b5/Code-of-Conduct.md` & `maturin-1.0.0b7/Code-of-Conduct.md`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/Dockerfile` & `maturin-1.0.0b7/Dockerfile`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/README.md` & `maturin-1.0.0b7/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -177,15 +177,15 @@
 The keys are the script names while the values are the path to the function in the format `some.module.path:class.function`, where the `class` part is optional. The function is called with no arguments. Example:
 
 ```toml
 [project.scripts]
 get_42 = "my_project:DummyClass.get_42"
 ```
 
-You can also specify [trove classifiers](https://pypi.org/classifiers/) in your Cargo.toml under `project.classifiers`:
+You can also specify [trove classifiers](https://pypi.org/classifiers/) in your `pyproject.toml` under `project.classifiers`:
 
 ```toml
 [project]
 name = "my-project"
 classifiers = ["Programming Language :: Python"]
 ```
```

### Comparing `maturin-1.0.0b5/deny.toml` & `maturin-1.0.0b7/deny.toml`

 * *Files 0% similar despite different names*

```diff
@@ -174,15 +174,15 @@
     # Wrapper crates can optionally be specified to allow the crate when it
     # is a direct dependency of the otherwise banned crate
     #{ name = "ansi_term", version = "=0.11.0", wrappers = [] },
 ]
 # Certain crates/versions that will be skipped when doing duplicate detection.
 skip = [
     #{ name = "ansi_term", version = "=0.11.0" },
-    { name = "ahash", version = "0.3.8" },
+    { name = "base64", version = "0.13.1" },
     # from cbindgen
     { name = "toml", version = "0.5.11" },
 ]
 # Similarly to `skip` allows you to skip certain crates during duplicate
 # detection. Unlike skip, it also includes the entire tree of transitive
 # dependencies starting at the specified crate, up to a certain depth, which is
 # by default infinite
```

### Comparing `maturin-1.0.0b5/license-apache` & `maturin-1.0.0b7/license-apache`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/license-mit` & `maturin-1.0.0b7/license-mit`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/maturin/__init__.py` & `maturin-1.0.0b7/maturin/__init__.py`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/maturin/__main__.py` & `maturin-1.0.0b7/maturin/__main__.py`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/maturin/import_hook.py` & `maturin-1.0.0b7/maturin/import_hook.py`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/noxfile.py` & `maturin-1.0.0b7/noxfile.py`

 * *Files 0% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 import json
 import sys
 from pathlib import Path
 
 import nox
 
 
-PYODIDE_VERSION = os.getenv("PYODIDE_VERSION", "0.22.0")
+PYODIDE_VERSION = os.getenv("PYODIDE_VERSION", "0.23.0")
 GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS")
 GITHUB_ENV = os.getenv("GITHUB_ENV")
 
 
 def append_to_github_env(name: str, value: str):
     if not GITHUB_ACTIONS or not GITHUB_ENV:
         return
```

### Comparing `maturin-1.0.0b5/pyproject.toml` & `maturin-1.0.0b7/pyproject.toml`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/setup.py` & `maturin-1.0.0b7/setup.py`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/auditwheel/audit.rs` & `maturin-1.0.0b7/src/auditwheel/audit.rs`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/auditwheel/manylinux-policy.json` & `maturin-1.0.0b7/src/auditwheel/manylinux-policy.json`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/auditwheel/musllinux-policy.json` & `maturin-1.0.0b7/src/auditwheel/musllinux-policy.json`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/auditwheel/musllinux.rs` & `maturin-1.0.0b7/src/auditwheel/musllinux.rs`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/auditwheel/patchelf.rs` & `maturin-1.0.0b7/src/auditwheel/patchelf.rs`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/auditwheel/platform_tag.rs` & `maturin-1.0.0b7/src/auditwheel/platform_tag.rs`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/auditwheel/policy.rs` & `maturin-1.0.0b7/src/auditwheel/policy.rs`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/auditwheel/repair.rs` & `maturin-1.0.0b7/src/auditwheel/repair.rs`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/build_context.rs` & `maturin-1.0.0b7/src/build_context.rs`

 * *Files 24% similar despite different names*

```diff
@@ -5,30 +5,35 @@
 use crate::module_writer::{
     add_data, write_bin, write_bindings_module, write_cffi_module, write_python_part,
     write_uniffi_module, write_wasm_launcher, WheelWriter,
 };
 use crate::project_layout::ProjectLayout;
 use crate::python_interpreter::InterpreterKind;
 use crate::source_distribution::source_distribution;
+use crate::target::{Arch, Os};
 use crate::{
     compile, pyproject_toml::Format, BuildArtifact, Metadata21, ModuleWriter, PyProjectToml,
     PythonInterpreter, Target,
 };
 use anyhow::{anyhow, bail, Context, Result};
 use cargo_metadata::Metadata;
 use fs_err as fs;
 use ignore::overrides::{Override, OverrideBuilder};
+use indexmap::IndexMap;
 use lddtree::Library;
 use normpath::PathExt;
-use regex::Regex;
+use pep508_rs::Requirement;
+use platform_info::*;
 use sha2::{Digest, Sha256};
 use std::collections::{HashMap, HashSet};
+use std::env;
 use std::fmt::{Display, Formatter};
 use std::io;
 use std::path::{Path, PathBuf};
+use std::str::FromStr;
 
 /// The way the rust code is used in the wheel
 #[derive(Clone, Debug, PartialEq, Eq)]
 pub enum BridgeModel {
     /// A rust binary to be shipped a python package
     /// The String is the name of the bindings
     /// providing crate, e.g. pyo3, the number is the minimum minor python version
@@ -96,15 +101,15 @@
             metadata21.get_distribution_escaped()
         )
     }
     if !metadata21.entry_points.is_empty() {
         bail!("You can't define entrypoints yourself for a binary project");
     }
 
-    let mut console_scripts = HashMap::new();
+    let mut console_scripts = IndexMap::new();
     for (_, bin_name) in artifacts_and_files {
         let base_name = bin_name
             .strip_suffix(".wasm")
             .context("No .wasm suffix in wasi binary")?;
         console_scripts.insert(
             base_name.to_string(),
             format!(
@@ -115,38 +120,36 @@
         );
     }
 
     metadata21
         .entry_points
         .insert("console_scripts".to_string(), console_scripts);
 
-    // A real pip version specification parser would be better, but bearing this we use this regex
-    // which tries to find the name wasmtime and then any specification
-    let wasmtime_re = Regex::new("^wasmtime[^a-zA-Z.-_]").unwrap();
+    // Add our wasmtime default version if the user didn't provide one
     if !metadata21
         .requires_dist
         .iter()
-        .any(|requirement| wasmtime_re.is_match(requirement))
+        .any(|requirement| requirement.name == "wasmtime")
     {
         // Having the wasmtime version hardcoded is not ideal, it's easy enough to overwrite
         metadata21
             .requires_dist
-            .push("wasmtime>=6.0.0,<7.0.0".to_string());
+            .push(Requirement::from_str("wasmtime>=7.0.0,<8.0.0").unwrap());
     }
 
     Ok(metadata21)
 }
 
 /// Contains all the metadata required to build the crate
 #[derive(Clone)]
 pub struct BuildContext {
     /// The platform, i.e. os and pointer width
     pub target: Target,
     /// List of Cargo targets to compile
-    pub cargo_targets: Vec<CompileTarget>,
+    pub compile_targets: Vec<CompileTarget>,
     /// Whether this project is pure rust or rust mixed with python
     pub project_layout: ProjectLayout,
     /// The path to pyproject.toml. Required for the source distribution
     pub pyproject_toml_path: PathBuf,
     /// Parsed pyproject.toml if any
     pub pyproject_toml: Option<PyProjectToml>,
     /// Python Package Metadata 2.1
@@ -249,15 +252,15 @@
 
         Ok(wheels)
     }
 
     /// Bridge model
     pub fn bridge(&self) -> &BridgeModel {
         // FIXME: currently we only allow multiple bin targets so bridges are all the same
-        &self.cargo_targets[0].1
+        &self.compile_targets[0].bridge_model
     }
 
     /// Builds a source distribution and returns the same metadata as [BuildContext::build_wheels]
     pub fn build_source_distribution(&self) -> Result<Option<BuiltWheelMetadata>> {
         fs::create_dir_all(&self.out)
             .context("Failed to create the target directory for the source distribution")?;
 
@@ -503,25 +506,152 @@
                 }
                 return Ok(Some(excludes.build()?));
             }
         }
         Ok(None)
     }
 
+    /// Returns the platform part of the tag for the wheel name
+    pub fn get_platform_tag(&self, platform_tags: &[PlatformTag]) -> Result<String> {
+        let target = &self.target;
+        let tag = match (&target.target_os(), &target.target_arch()) {
+            // Windows
+            (Os::Windows, Arch::X86) => "win32".to_string(),
+            (Os::Windows, Arch::X86_64) => "win_amd64".to_string(),
+            (Os::Windows, Arch::Aarch64) => "win_arm64".to_string(),
+            // Linux
+            (Os::Linux, _) => {
+                let arch = target.get_platform_arch()?;
+                let mut platform_tags = platform_tags.to_vec();
+                platform_tags.sort();
+                let mut tags = vec![];
+                for platform_tag in platform_tags {
+                    tags.push(format!("{platform_tag}_{arch}"));
+                    for alias in platform_tag.aliases() {
+                        tags.push(format!("{alias}_{arch}"));
+                    }
+                }
+                tags.join(".")
+            }
+            // macOS
+            (Os::Macos, Arch::X86_64) | (Os::Macos, Arch::Aarch64) => {
+                let ((x86_64_major, x86_64_minor), (arm64_major, arm64_minor)) = macosx_deployment_target(env::var("MACOSX_DEPLOYMENT_TARGET").ok().as_deref(), self.universal2)?;
+                let x86_64_tag = if let Some(deployment_target) = self.pyproject_toml.as_ref().and_then(|x| x.target_config("x86_64-apple-darwin")).and_then(|config| config.macos_deployment_target.as_ref()) {
+                    deployment_target.replace('.', "_")
+                } else {
+                    format!("{x86_64_major}_{x86_64_minor}")
+                };
+                let arm64_tag = if let Some(deployment_target) = self.pyproject_toml.as_ref().and_then(|x| x.target_config("aarch64-apple-darwin")).and_then(|config| config.macos_deployment_target.as_ref()) {
+                    deployment_target.replace('.', "_")
+                } else {
+                    format!("{arm64_major}_{arm64_minor}")
+                };
+                if self.universal2 {
+                    format!(
+                        "macosx_{x86_64_tag}_x86_64.macosx_{arm64_tag}_arm64.macosx_{x86_64_tag}_universal2"
+                    )
+                } else if target.target_arch() == Arch::Aarch64 {
+                    format!("macosx_{arm64_tag}_arm64")
+                } else {
+                    format!("macosx_{x86_64_tag}_x86_64")
+                }
+            }
+            // FreeBSD
+            (Os::FreeBsd, _)
+            // NetBSD
+            | (Os::NetBsd, _)
+            // OpenBSD
+            | (Os::OpenBsd, _) => {
+                let release = target.get_platform_release()?;
+                format!(
+                    "{}_{}_{}",
+                    target.target_os().to_string().to_ascii_lowercase(),
+                    release,
+                    target.target_arch().machine(),
+                )
+            }
+            // DragonFly
+            (Os::Dragonfly, Arch::X86_64)
+            // Haiku
+            | (Os::Haiku, Arch::X86_64) => {
+                let release = target.get_platform_release()?;
+                format!(
+                    "{}_{}_{}",
+                    target.target_os().to_string().to_ascii_lowercase(),
+                    release.to_ascii_lowercase(),
+                    "x86_64"
+                )
+            }
+            // Emscripten
+            (Os::Emscripten, Arch::Wasm32) => {
+                let release = emscripten_version()?.replace(['.', '-'], "_");
+                format!("emscripten_{release}_wasm32")
+            }
+            (Os::Wasi, Arch::Wasm32) => {
+                "any".to_string()
+            }
+            // osname_release_machine fallback for any POSIX system
+            (_, _) => {
+                let info = PlatformInfo::new()?;
+                let mut release = info.release().replace(['.', '-'], "_");
+                let mut machine = info.machine().replace([' ', '/'], "_");
+
+                let mut os = target.target_os().to_string().to_ascii_lowercase();
+                // See https://github.com/python/cpython/blob/46c8d915715aa2bd4d697482aa051fe974d440e1/Lib/sysconfig.py#L722-L730
+                if os.starts_with("sunos") {
+                    // Solaris / Illumos
+                    if let Some((major, other)) = release.split_once('_') {
+                        let major_ver: u64 = major.parse().context("illumos major version is not a number")?;
+                        if major_ver >= 5 {
+                            // SunOS 5 == Solaris 2
+                            os = "solaris".to_string();
+                            release = format!("{}_{}", major_ver - 3, other);
+                            machine = format!("{machine}_64bit");
+                        }
+                    }
+                }
+                format!(
+                    "{os}_{release}_{machine}"
+                )
+            }
+        };
+        Ok(tag)
+    }
+
+    /// Returns the tags for the WHEEL file for cffi wheels
+    pub fn get_py3_tags(&self, platform_tags: &[PlatformTag]) -> Result<Vec<String>> {
+        let tags = vec![format!(
+            "py3-none-{}",
+            self.get_platform_tag(platform_tags)?
+        )];
+        Ok(tags)
+    }
+
+    /// Returns the tags for the platform without python version
+    pub fn get_universal_tags(
+        &self,
+        platform_tags: &[PlatformTag],
+    ) -> Result<(String, Vec<String>)> {
+        let tag = format!(
+            "py3-none-{platform}",
+            platform = self.get_platform_tag(platform_tags)?
+        );
+        let tags = self.get_py3_tags(platform_tags)?;
+        Ok((tag, tags))
+    }
+
     fn write_binding_wheel_abi3(
         &self,
         artifact: BuildArtifact,
         platform_tags: &[PlatformTag],
         ext_libs: Vec<Library>,
         major: u8,
         min_minor: u8,
     ) -> Result<BuiltWheelMetadata> {
-        let platform = self
-            .target
-            .get_platform_tag(platform_tags, self.universal2)?;
+        let platform = self.get_platform_tag(platform_tags)?;
         let tag = format!("cp{major}{min_minor}-abi3-{platform}");
 
         let mut writer = WheelWriter::new(
             &tag,
             &self.out,
             &self.metadata21,
             &[tag.clone()],
@@ -592,15 +722,15 @@
     fn write_binding_wheel(
         &self,
         python_interpreter: &PythonInterpreter,
         artifact: BuildArtifact,
         platform_tags: &[PlatformTag],
         ext_libs: Vec<Library>,
     ) -> Result<BuiltWheelMetadata> {
-        let tag = python_interpreter.get_tag(&self.target, platform_tags, self.universal2)?;
+        let tag = python_interpreter.get_tag(self, platform_tags)?;
 
         let mut writer = WheelWriter::new(
             &tag,
             &self.out,
             &self.metadata21,
             &[tag.clone()],
             self.excludes(Format::Wheel)?,
@@ -678,15 +808,15 @@
     /// The module name is used to warn about missing a `PyInit_<module name>` function for
     /// bindings modules.
     pub fn compile_cdylib(
         &self,
         python_interpreter: Option<&PythonInterpreter>,
         extension_name: Option<&str>,
     ) -> Result<BuildArtifact> {
-        let artifacts = compile(self, python_interpreter, &self.cargo_targets)
+        let artifacts = compile(self, python_interpreter, &self.compile_targets)
             .context("Failed to build a native library through cargo")?;
         let error_msg = "Cargo didn't build a cdylib. Did you miss crate-type = [\"cdylib\"] \
                  in the lib section of your Cargo.toml?";
         let artifacts = artifacts.get(0).context(error_msg)?;
 
         let mut artifact = artifacts
             .get("cdylib")
@@ -714,17 +844,15 @@
 
     fn write_cffi_wheel(
         &self,
         artifact: BuildArtifact,
         platform_tags: &[PlatformTag],
         ext_libs: Vec<Library>,
     ) -> Result<BuiltWheelMetadata> {
-        let (tag, tags) = self
-            .target
-            .get_universal_tags(platform_tags, self.universal2)?;
+        let (tag, tags) = self.get_universal_tags(platform_tags)?;
 
         let mut writer = WheelWriter::new(
             &tag,
             &self.out,
             &self.metadata21,
             &tags,
             self.excludes(Format::Wheel)?,
@@ -762,15 +890,15 @@
         let (wheel_path, tag) = self.write_cffi_wheel(artifact, &platform_tags, external_libs)?;
 
         // Warn if cffi isn't specified in the requirements
         if !self
             .metadata21
             .requires_dist
             .iter()
-            .any(|dep| dep.to_ascii_lowercase().starts_with("cffi"))
+            .any(|requirement| requirement.name == "cffi")
         {
             eprintln!(
                 "⚠️  Warning: missing cffi package dependency, please add it to pyproject.toml. \
                 e.g: `dependencies = [\"cffi\"]`. This will become an error."
             );
         }
 
@@ -782,17 +910,15 @@
 
     fn write_uniffi_wheel(
         &self,
         artifact: BuildArtifact,
         platform_tags: &[PlatformTag],
         ext_libs: Vec<Library>,
     ) -> Result<BuiltWheelMetadata> {
-        let (tag, tags) = self
-            .target
-            .get_universal_tags(platform_tags, self.universal2)?;
+        let (tag, tags) = self.get_universal_tags(platform_tags)?;
 
         let mut writer = WheelWriter::new(
             &tag,
             &self.out,
             &self.metadata21,
             &tags,
             self.excludes(Format::Wheel)?,
@@ -839,20 +965,17 @@
         &self,
         python_interpreter: Option<&PythonInterpreter>,
         artifacts: &[BuildArtifact],
         platform_tags: &[PlatformTag],
         ext_libs: &[Vec<Library>],
     ) -> Result<BuiltWheelMetadata> {
         let (tag, tags) = match (self.bridge(), python_interpreter) {
-            (BridgeModel::Bin(None), _) => self
-                .target
-                .get_universal_tags(platform_tags, self.universal2)?,
+            (BridgeModel::Bin(None), _) => self.get_universal_tags(platform_tags)?,
             (BridgeModel::Bin(Some(..)), Some(python_interpreter)) => {
-                let tag =
-                    python_interpreter.get_tag(&self.target, platform_tags, self.universal2)?;
+                let tag = python_interpreter.get_tag(self, platform_tags)?;
                 (tag.clone(), vec![tag])
             }
             _ => unreachable!(),
         };
 
         if !self.metadata21.scripts.is_empty() {
             bail!("Defining scripts and working with a binary doesn't mix well");
@@ -929,15 +1052,15 @@
     ///
     /// Runs [auditwheel_rs()] if not deactivated
     pub fn build_bin_wheel(
         &self,
         python_interpreter: Option<&PythonInterpreter>,
     ) -> Result<Vec<BuiltWheelMetadata>> {
         let mut wheels = Vec::new();
-        let artifacts = compile(self, python_interpreter, &self.cargo_targets)
+        let artifacts = compile(self, python_interpreter, &self.compile_targets)
             .context("Failed to build a native library through cargo")?;
         if artifacts.is_empty() {
             bail!("Cargo didn't build a binary")
         }
 
         let mut policies = Vec::with_capacity(artifacts.len());
         let mut ext_libs = Vec::new();
@@ -991,7 +1114,144 @@
 pub fn hash_file(path: impl AsRef<Path>) -> Result<String, io::Error> {
     let mut file = fs::File::open(path.as_ref())?;
     let mut hasher = Sha256::new();
     io::copy(&mut file, &mut hasher)?;
     let hex = format!("{:x}", hasher.finalize());
     Ok(hex)
 }
+
+/// Get the default macOS deployment target version
+fn macosx_deployment_target(
+    deploy_target: Option<&str>,
+    universal2: bool,
+) -> Result<((u16, u16), (u16, u16))> {
+    let x86_64_default_rustc = rustc_macosx_target_version("x86_64-apple-darwin");
+    let x86_64_default = if universal2 && x86_64_default_rustc.1 < 9 {
+        (10, 9)
+    } else {
+        x86_64_default_rustc
+    };
+    let arm64_default = rustc_macosx_target_version("aarch64-apple-darwin");
+    let mut x86_64_ver = x86_64_default;
+    let mut arm64_ver = arm64_default;
+    if let Some(deploy_target) = deploy_target {
+        let err_ctx = "MACOSX_DEPLOYMENT_TARGET is invalid";
+        let mut parts = deploy_target.split('.');
+        let major = parts.next().context(err_ctx)?;
+        let major: u16 = major.parse().context(err_ctx)?;
+        let minor = parts.next().context(err_ctx)?;
+        let minor: u16 = minor.parse().context(err_ctx)?;
+        if (major, minor) > x86_64_default {
+            x86_64_ver = (major, minor);
+        }
+        if (major, minor) > arm64_default {
+            arm64_ver = (major, minor);
+        }
+    }
+    Ok((x86_64_ver, arm64_ver))
+}
+
+pub(crate) fn rustc_macosx_target_version(target: &str) -> (u16, u16) {
+    use std::process::Command;
+    use target_lexicon::OperatingSystem;
+
+    let fallback_version = if target == "aarch64-apple-darwin" {
+        (11, 0)
+    } else {
+        (10, 7)
+    };
+
+    let rustc_target_version = || -> Result<(u16, u16)> {
+        let cmd = Command::new("rustc")
+            .arg("-Z")
+            .arg("unstable-options")
+            .arg("--print")
+            .arg("target-spec-json")
+            .arg("--target")
+            .arg(target)
+            .env("RUSTC_BOOTSTRAP", "1")
+            .env_remove("MACOSX_DEPLOYMENT_TARGET")
+            .output()
+            .context("Failed to run rustc to get the target spec")?;
+        let stdout = String::from_utf8(cmd.stdout).context("rustc output is not valid utf-8")?;
+        let spec: serde_json::Value =
+            serde_json::from_str(&stdout).context("rustc output is not valid json")?;
+        let llvm_target = spec
+            .as_object()
+            .context("rustc output is not a json object")?
+            .get("llvm-target")
+            .context("rustc output does not contain llvm-target")?
+            .as_str()
+            .context("llvm-target is not a string")?;
+        let triple = llvm_target.parse::<target_lexicon::Triple>();
+        let (major, minor) = match triple.map(|t| t.operating_system) {
+            Ok(OperatingSystem::MacOSX { major, minor, .. }) => (major, minor),
+            _ => fallback_version,
+        };
+        Ok((major, minor))
+    };
+    rustc_target_version().unwrap_or(fallback_version)
+}
+
+/// Emscripten version
+fn emscripten_version() -> Result<String> {
+    let os_version = env::var("MATURIN_EMSCRIPTEN_VERSION");
+    let release = match os_version {
+        Ok(os_ver) => os_ver,
+        Err(_) => emcc_version()?,
+    };
+    Ok(release)
+}
+
+fn emcc_version() -> Result<String> {
+    use regex::bytes::Regex;
+    use std::process::Command;
+
+    let emcc = Command::new("emcc")
+        .arg("--version")
+        .output()
+        .context("Failed to run emcc to get the version")?;
+    let pattern = Regex::new(r"^emcc .+? (\d+\.\d+\.\d+).*").unwrap();
+    let caps = pattern
+        .captures(&emcc.stdout)
+        .context("Failed to parse emcc version")?;
+    let version = caps.get(1).context("Failed to parse emcc version")?;
+    Ok(String::from_utf8(version.as_bytes().to_vec())?)
+}
+
+#[cfg(test)]
+mod test {
+    use super::macosx_deployment_target;
+    use pretty_assertions::assert_eq;
+
+    #[test]
+    fn test_macosx_deployment_target() {
+        assert_eq!(
+            macosx_deployment_target(None, false).unwrap(),
+            ((10, 7), (11, 0))
+        );
+        assert_eq!(
+            macosx_deployment_target(None, true).unwrap(),
+            ((10, 9), (11, 0))
+        );
+        assert_eq!(
+            macosx_deployment_target(Some("10.6"), false).unwrap(),
+            ((10, 7), (11, 0))
+        );
+        assert_eq!(
+            macosx_deployment_target(Some("10.6"), true).unwrap(),
+            ((10, 9), (11, 0))
+        );
+        assert_eq!(
+            macosx_deployment_target(Some("10.9"), false).unwrap(),
+            ((10, 9), (11, 0))
+        );
+        assert_eq!(
+            macosx_deployment_target(Some("11.0.0"), false).unwrap(),
+            ((11, 0), (11, 0))
+        );
+        assert_eq!(
+            macosx_deployment_target(Some("11.1"), false).unwrap(),
+            ((11, 1), (11, 1))
+        );
+    }
+}
```

### Comparing `maturin-1.0.0b5/src/build_options.rs` & `maturin-1.0.0b7/src/build_options.rs`

 * *Files 7% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 use crate::auditwheel::PlatformTag;
 use crate::build_context::BridgeModel;
 use crate::compile::{CompileTarget, LIB_CRATE_TYPES};
 use crate::cross_compile::{find_sysconfigdata, parse_sysconfigdata};
 use crate::project_layout::ProjectResolver;
 use crate::pyproject_toml::ToolMaturin;
 use crate::python_interpreter::{InterpreterConfig, InterpreterKind, MINIMUM_PYTHON_MINOR};
-use crate::{BuildContext, Metadata21, PythonInterpreter, Target};
+use crate::{BuildContext, PythonInterpreter, Target};
 use anyhow::{bail, format_err, Context, Result};
 use cargo_metadata::{Metadata, Node};
-use regex::Regex;
+use pep440_rs::VersionSpecifiers;
 use serde::{Deserialize, Serialize};
 use std::collections::{HashMap, HashSet};
 use std::env;
 use std::ops::{Deref, DerefMut};
 use std::path::PathBuf;
 use tracing::debug;
 
@@ -212,15 +212,15 @@
 impl BuildOptions {
     /// Finds the appropriate amount for python versions for each [BridgeModel].
     fn find_interpreters(
         &self,
         bridge: &BridgeModel,
         interpreter: &[PathBuf],
         target: &Target,
-        min_python_minor: Option<usize>,
+        requires_python: Option<&VersionSpecifiers>,
         generate_import_lib: bool,
     ) -> Result<Vec<PythonInterpreter>> {
         match bridge {
             BridgeModel::Bindings(binding_name, _) | BridgeModel::Bin(Some((binding_name, _))) => {
                 let mut interpreters = Vec::new();
                 if let Some(config_file) = env::var_os("PYO3_CONFIG_FILE") {
                     if !binding_name.starts_with("pyo3") {
@@ -228,20 +228,16 @@
                     }
                     let interpreter_config =
                         InterpreterConfig::from_pyo3_config(config_file.as_ref(), target)
                             .context("Invalid PYO3_CONFIG_FILE")?;
                     interpreters.push(PythonInterpreter::from_config(interpreter_config));
                 } else if binding_name.starts_with("pyo3") && target.cross_compiling() {
                     if let Some(cross_lib_dir) = env::var_os("PYO3_CROSS_LIB_DIR") {
-                        let host_interpreters = find_interpreter_in_host(
-                            bridge,
-                            interpreter,
-                            target,
-                            min_python_minor,
-                        )?;
+                        let host_interpreters =
+                            find_interpreter_in_host(bridge, interpreter, target, requires_python)?;
                         let host_python = &host_interpreters[0];
                         eprintln!("🐍 Using host {host_python} for cross-compiling preparation");
                         // pyo3
                         env::set_var("PYO3_PYTHON", &host_python.executable);
                         // rust-cpython, and legacy pyo3 versions
                         env::set_var("PYTHON_SYS_EXECUTABLE", &host_python.executable);
 
@@ -309,22 +305,22 @@
                                 && PythonInterpreter::check_executable(interp, target, bridge)?
                                     .is_none()
                             {
                                 bail!("{} is not a valid python interpreter", interp.display());
                             }
                         }
                         interpreters =
-                            find_interpreter_in_sysconfig(interpreter, target, min_python_minor)?;
+                            find_interpreter_in_sysconfig(interpreter, target, requires_python)?;
                     }
                 } else if binding_name.starts_with("pyo3") {
                     // Only pyo3/pyo3-ffi bindings supports bundled sysconfig interpreters
-                    interpreters = find_interpreter(bridge, interpreter, target, min_python_minor)?;
+                    interpreters = find_interpreter(bridge, interpreter, target, requires_python)?;
                 } else {
                     interpreters =
-                        find_interpreter_in_host(bridge, interpreter, target, min_python_minor)?;
+                        find_interpreter_in_host(bridge, interpreter, target, requires_python)?;
                 }
 
                 let interpreters_str = interpreters
                     .iter()
                     .map(ToString::to_string)
                     .collect::<Vec<String>>()
                     .join(", ");
@@ -340,21 +336,17 @@
             }
             BridgeModel::Bin(None) | BridgeModel::UniFfi => Ok(vec![]),
             BridgeModel::BindingsAbi3(major, minor) => {
                 if target.is_windows() {
                     // Ideally, we wouldn't want to use any python interpreter without abi3 at all.
                     // Unfortunately, on windows we need one to figure out base_prefix for a linker
                     // argument.
-                    let interpreters = find_interpreter_in_host(
-                        bridge,
-                        interpreter,
-                        target,
-                        Some(*minor as usize),
-                    )
-                    .unwrap_or_default();
+                    let interpreters =
+                        find_interpreter_in_host(bridge, interpreter, target, requires_python)
+                            .unwrap_or_default();
                     if env::var_os("PYO3_CROSS_LIB_DIR").is_some() {
                         // PYO3_CROSS_LIB_DIR should point to the `libs` directory inside base_prefix
                         // when cross compiling, so we fake a python interpreter matching it
                         eprintln!("⚠️  Cross-compiling is poorly supported");
                         Ok(vec![PythonInterpreter {
                             config: InterpreterConfig {
                                 major: *major as usize,
@@ -398,34 +390,30 @@
                             implmentation_name: "cpython".to_string(),
                             soabi: None,
                         }])
                     } else {
                         bail!("Failed to find a python interpreter");
                     }
                 } else {
-                    let found_interpreters = find_interpreter_in_host(
-                        bridge,
-                        interpreter,
-                        target,
-                        Some(*minor as usize),
-                    )
-                    .or_else(|err| {
-                        let interps = find_interpreter_in_sysconfig(
-                            interpreter,
-                            target,
-                            Some(*minor as usize),
-                        )
-                        .unwrap_or_default();
-                        if interps.is_empty() && !self.interpreter.is_empty() {
-                            // Print error when user supplied `--interpreter` option
-                            Err(err)
-                        } else {
-                            Ok(interps)
-                        }
-                    })?;
+                    let found_interpreters =
+                        find_interpreter_in_host(bridge, interpreter, target, requires_python)
+                            .or_else(|err| {
+                                let interps = find_interpreter_in_sysconfig(
+                                    interpreter,
+                                    target,
+                                    requires_python,
+                                )
+                                .unwrap_or_default();
+                                if interps.is_empty() && !self.interpreter.is_empty() {
+                                    // Print error when user supplied `--interpreter` option
+                                    Err(err)
+                                } else {
+                                    Ok(interps)
+                                }
+                            })?;
                     eprintln!("🐍 Not using a specific python interpreter");
                     if self.interpreter.is_empty() {
                         // Fake one to make `BuildContext::build_wheels` happy for abi3 when no cpython/pypy found on host
                         // The python interpreter config doesn't matter, as it's not used for anything
                         Ok(vec![PythonInterpreter {
                             config: InterpreterConfig {
                                 major: *major as usize,
@@ -457,15 +445,15 @@
                         }
                         // cross compiling to PyPy with abi3 feature enabled,
                         // we cannot use host pypy so switch to bundled sysconfig instead
                         if !pypys.is_empty() {
                             interps.extend(find_interpreter_in_sysconfig(
                                 &pypys,
                                 target,
-                                min_python_minor,
+                                requires_python,
                             )?)
                         }
                         if interps.is_empty() {
                             bail!("Failed to find any python interpreter");
                         }
                         Ok(interps)
                     } else {
@@ -508,19 +496,19 @@
                         pyproject_toml_maturin_options.push("bindings");
                     }
                     x.bindings()
                 })
             }),
         )?;
 
-        if !bridge.is_bin() && module_name.contains('-') {
+        if !bridge.is_bin() && project_layout.extension_name.contains('-') {
             bail!(
                 "The module name must not contain a minus `-` \
                  (Make sure you have set an appropriate [lib] name or \
-                 [package.metadata.maturin] name in your Cargo.toml)"
+                 [tool.maturin] module-name in your pyproject.toml)"
             );
         }
 
         let mut target_triple = self.target.clone();
 
         let mut universal2 = self.universal2;
         if universal2 {
@@ -564,15 +552,15 @@
         let generate_import_lib = is_generating_import_lib(&cargo_metadata)?;
         let interpreter = if self.find_interpreter {
             // Auto-detect interpreters
             self.find_interpreters(
                 &bridge,
                 &[],
                 &target,
-                get_min_python_minor(&metadata21),
+                metadata21.requires_python.as_ref(),
                 generate_import_lib,
             )?
         } else {
             // User given list of interpreters
             let interpreter = if self.interpreter.is_empty() && !target.cross_compiling() {
                 if cfg!(test) {
                     match env::var_os("MATURIN_TEST_PYTHON") {
@@ -660,22 +648,22 @@
 
         let target_dir = self
             .cargo
             .target_dir
             .clone()
             .unwrap_or_else(|| cargo_metadata.target_directory.clone().into_std_path_buf());
 
-        let remaining_core_metadata = cargo_toml.remaining_core_metadata();
-        let config_targets = remaining_core_metadata.targets.as_deref();
-        let cargo_targets = filter_cargo_targets(&cargo_metadata, bridge, config_targets)?;
+        let config_targets = pyproject.and_then(|x| x.targets());
+        let compile_targets =
+            filter_cargo_targets(&cargo_metadata, bridge, config_targets.as_deref())?;
 
         let crate_name = cargo_toml.package.name;
         Ok(BuildContext {
             target,
-            cargo_targets,
+            compile_targets,
             project_layout,
             pyproject_toml_path,
             pyproject_toml,
             metadata21,
             crate_name,
             module_name,
             manifest_path: cargo_toml_path,
@@ -743,15 +731,15 @@
     }
     Ok(())
 }
 
 fn filter_cargo_targets(
     cargo_metadata: &Metadata,
     bridge: BridgeModel,
-    config_targets: Option<&[crate::cargo_toml::CargoTarget]>,
+    config_targets: Option<&[crate::pyproject_toml::CargoTarget]>,
 ) -> Result<Vec<CompileTarget>> {
     let root_pkg = cargo_metadata.root_package().unwrap();
     let resolved_features = cargo_metadata
         .resolve
         .as_ref()
         .and_then(|resolve| resolve.nodes.iter().find(|node| node.id == root_pkg.id))
         .map(|node| node.features.clone())
@@ -771,33 +759,39 @@
                             .required_features
                             .iter()
                             .all(|f| resolved_features.contains(f))
                 }
             }
             _ => target.kind.contains(&"cdylib".to_string()),
         })
-        .map(|target| (target.clone(), bridge.clone()))
+        .map(|target| CompileTarget {
+            target: target.clone(),
+            bridge_model: bridge.clone(),
+        })
         .collect();
     if targets.is_empty() && !bridge.is_bin() {
         // No `crate-type = ["cdylib"]` in `Cargo.toml`
         // Let's try compile one of the target with `--crate-type cdylib`
         let lib_target = root_pkg.targets.iter().find(|target| {
             target
                 .kind
                 .iter()
                 .any(|k| LIB_CRATE_TYPES.contains(&k.as_str()))
         });
         if let Some(target) = lib_target {
-            targets.push((target.clone(), bridge));
+            targets.push(CompileTarget {
+                target: target.clone(),
+                bridge_model: bridge,
+            });
         }
     }
 
     // Filter targets by config_targets
     if let Some(config_targets) = config_targets {
-        targets.retain(|(target, _)| {
+        targets.retain(|CompileTarget { target, .. }| {
             config_targets.iter().any(|config_target| {
                 let name_eq = config_target.name == target.name;
                 match &config_target.kind {
                     Some(kind) => name_eq && target.kind.contains(kind),
                     None => name_eq,
                 }
             })
@@ -805,50 +799,27 @@
         if targets.is_empty() {
             bail!(
                 "No Cargo targets matched by `package.metadata.maturin.targets`, please check your `Cargo.toml`"
             );
         } else {
             let target_names = targets
                 .iter()
-                .map(|(target, _)| target.name.as_str())
+                .map(|CompileTarget { target, .. }| target.name.as_str())
                 .collect::<Vec<_>>();
             eprintln!(
                 "🎯 Found {} Cargo targets in `Cargo.toml`: {}",
                 targets.len(),
                 target_names.join(", ")
             );
         }
     }
 
     Ok(targets)
 }
 
-/// Uses very simple PEP 440 subset parsing to determine the
-/// minimum supported python minor version for interpreter search
-fn get_min_python_minor(metadata21: &Metadata21) -> Option<usize> {
-    if let Some(requires_python) = &metadata21.requires_python {
-        let regex = Regex::new(r#">=3\.(\d+)(?:\.\d)?"#).unwrap();
-        if let Some(captures) = regex.captures(requires_python) {
-            let min_python_minor = captures[1]
-                .parse::<usize>()
-                .expect("Regex must only match usize");
-            Some(min_python_minor)
-        } else {
-            eprintln!(
-                "⚠️ Couldn't parse the value of requires-python, \
-                    not taking it into account when searching for python interpreter. \
-                    Note: Only `>=3.x.y` is currently supported."
-            );
-            None
-        }
-    } else {
-        None
-    }
-}
-
 /// pyo3 supports building abi3 wheels if the unstable-api feature is not selected
 fn has_abi3(cargo_metadata: &Metadata) -> Result<Option<(u8, u8)>> {
     let resolve = cargo_metadata
         .resolve
         .as_ref()
         .context("Expected cargo to return metadata with resolve")?;
     for &lib in PYO3_BINDING_CRATES.iter() {
@@ -1079,78 +1050,78 @@
 
 /// Find python interpreters in host machine first,
 /// fallback to bundled sysconfig if not found in host machine
 fn find_interpreter(
     bridge: &BridgeModel,
     interpreter: &[PathBuf],
     target: &Target,
-    min_python_minor: Option<usize>,
+    requires_python: Option<&VersionSpecifiers>,
 ) -> Result<Vec<PythonInterpreter>> {
     let mut interpreters = Vec::new();
     if !interpreter.is_empty() {
         let mut missing = Vec::new();
         for interp in interpreter {
             match PythonInterpreter::check_executable(interp.clone(), target, bridge) {
                 Ok(Some(interp)) => interpreters.push(interp),
                 _ => missing.push(interp.clone()),
             }
         }
         if !missing.is_empty() {
             let sysconfig_interps =
-                find_interpreter_in_sysconfig(&missing, target, min_python_minor)?;
+                find_interpreter_in_sysconfig(&missing, target, requires_python)?;
             interpreters.extend(sysconfig_interps);
         }
     } else {
-        interpreters = PythonInterpreter::find_all(target, bridge, min_python_minor)
+        interpreters = PythonInterpreter::find_all(target, bridge, requires_python)
             .context("Finding python interpreters failed")?;
     };
 
     if interpreters.is_empty() {
-        if let Some(minor) = min_python_minor {
-            bail!("Couldn't find any python interpreters with version >= 3.{}. Please specify at least one with -i", minor);
+        if let Some(requires_python) = requires_python {
+            bail!("Couldn't find any python interpreters with version {}. Please specify at least one with -i", requires_python);
         } else {
             bail!("Couldn't find any python interpreters. Please specify at least one with -i");
         }
     }
     Ok(interpreters)
 }
 
 /// Find python interpreters in the host machine
 fn find_interpreter_in_host(
     bridge: &BridgeModel,
     interpreter: &[PathBuf],
     target: &Target,
-    min_python_minor: Option<usize>,
+    requires_python: Option<&VersionSpecifiers>,
 ) -> Result<Vec<PythonInterpreter>> {
     let interpreters = if !interpreter.is_empty() {
         PythonInterpreter::check_executables(interpreter, target, bridge)
             .context("The given list of python interpreters is invalid")?
     } else {
-        PythonInterpreter::find_all(target, bridge, min_python_minor)
+        PythonInterpreter::find_all(target, bridge, requires_python)
             .context("Finding python interpreters failed")?
     };
 
     if interpreters.is_empty() {
-        if let Some(minor) = min_python_minor {
-            bail!("Couldn't find any python interpreters with version >= 3.{}. Please specify at least one with -i", minor);
+        if let Some(requires_python) = requires_python {
+            bail!("Couldn't find any python interpreters with {}. Please specify at least one with -i", requires_python);
         } else {
             bail!("Couldn't find any python interpreters. Please specify at least one with -i");
         }
     }
     Ok(interpreters)
 }
 
 /// Find python interpreters in the bundled sysconfig
 fn find_interpreter_in_sysconfig(
     interpreter: &[PathBuf],
     target: &Target,
-    min_python_minor: Option<usize>,
+    requires_python: Option<&VersionSpecifiers>,
 ) -> Result<Vec<PythonInterpreter>> {
     if interpreter.is_empty() {
-        return Ok(PythonInterpreter::find_by_target(target, min_python_minor));
+        return Ok(PythonInterpreter::find_by_target(target, requires_python));
     }
     let mut interpreters = Vec::new();
     for interp in interpreter {
         let python = interp.display().to_string();
         let (python_impl, python_ver) = if let Some(ver) = python.strip_prefix("pypy") {
             (InterpreterKind::PyPy, ver.strip_prefix('-').unwrap_or(ver))
         } else if let Some(ver) = python.strip_prefix("python") {
@@ -1174,23 +1145,18 @@
             .context("Invalid python interpreter version")?;
         let ver_major = ver_major.parse::<usize>().with_context(|| {
             format!("Invalid python interpreter major version '{ver_major}', expect a digit")
         })?;
         let ver_minor = ver_minor.parse::<usize>().with_context(|| {
             format!("Invalid python interpreter minor version '{ver_minor}', expect a digit")
         })?;
-        let sysconfig = InterpreterConfig::lookup(
-            target.target_os(),
-            target.target_arch(),
-            python_impl,
-            (ver_major, ver_minor),
-        )
-        .with_context(|| {
-            format!("Failed to find a {python_impl} {ver_major}.{ver_minor} interpreter")
-        })?;
+        let sysconfig = InterpreterConfig::lookup(target, python_impl, (ver_major, ver_minor))
+            .with_context(|| {
+                format!("Failed to find a {python_impl} {ver_major}.{ver_minor} interpreter")
+            })?;
         debug!(
             "Found {} {}.{} in bundled sysconfig",
             sysconfig.interpreter_kind, sysconfig.major, sysconfig.minor,
         );
         interpreters.push(PythonInterpreter::from_config(sysconfig.clone()));
     }
     Ok(interpreters)
@@ -1490,25 +1456,8 @@
             "other-feature",
             "-Z",
             "unstable-options",
         ];
 
         assert_eq!(extract_cargo_metadata_args(&args).unwrap(), expected);
     }
-
-    #[test]
-    fn test_get_min_python_minor() {
-        use crate::CargoToml;
-
-        // Nothing specified
-        let manifest_path = "test-crates/pyo3-pure/Cargo.toml";
-        let cargo_toml = CargoToml::from_path(manifest_path).unwrap();
-        let cargo_metadata = MetadataCommand::new()
-            .manifest_path(manifest_path)
-            .exec()
-            .unwrap();
-        let metadata21 =
-            Metadata21::from_cargo_toml(&cargo_toml, "test-crates/pyo3-pure", &cargo_metadata)
-                .unwrap();
-        assert_eq!(get_min_python_minor(&metadata21), None);
-    }
 }
```

### Comparing `maturin-1.0.0b5/src/cargo_toml.rs` & `maturin-1.0.0b7/src/cargo_toml.rs`

 * *Files 11% similar despite different names*

```diff
@@ -60,14 +60,15 @@
             maturin: Some(extra_metadata),
         }) = &self.package.metadata
         {
             let removed_keys = [
                 "scripts",
                 "classifiers",
                 "classifier",
+                "data",
                 "maintainer",
                 "maintainer-email",
                 "requires-dist",
                 "requires-python",
                 "requires-external",
                 "project-url",
                 "provides-extra",
@@ -97,36 +98,18 @@
     maturin: Option<RemainingCoreMetadata>,
 }
 
 /// The `[project.metadata.maturin]` with the maturin specific metadata
 #[derive(Serialize, Deserialize, Debug, Clone, Default)]
 #[serde(rename_all = "kebab-case")]
 pub struct RemainingCoreMetadata {
-    pub name: Option<String>,
-    /// The directory containing the wheel data
-    pub data: Option<String>,
-    /// Cargo compile targets
-    pub targets: Option<Vec<CargoTarget>>,
     #[serde(flatten)]
     pub other: HashMap<String, toml::Value>,
 }
 
-/// Cargo compile target
-#[derive(Serialize, Deserialize, Debug, Clone, Default)]
-#[serde(rename_all = "kebab-case")]
-pub struct CargoTarget {
-    /// Name as given in the `Cargo.toml` or generated from the file name
-    pub name: String,
-    /// Kind of target ("bin", "lib")
-    pub kind: Option<String>,
-    // TODO: Add bindings option
-    // Bridge model, which kind of bindings to use
-    // pub bindings: Option<String>,
-}
-
 #[cfg(test)]
 mod test {
     use super::*;
     use indoc::indoc;
 
     #[test]
     fn test_metadata_from_cargo_toml() {
@@ -156,18 +139,14 @@
             kind = "lib"
             bindings = "pyo3"
         "#
         );
 
         let cargo_toml: Result<CargoToml, _> = toml::from_str(cargo_toml);
         assert!(cargo_toml.is_ok());
-
-        let maturin = cargo_toml.unwrap().remaining_core_metadata();
-        let targets = maturin.targets.unwrap();
-        assert_eq!("pyo3_pure", targets[0].name);
     }
 
     #[test]
     fn test_metadata_from_cargo_toml_without_authors() {
         let cargo_toml = indoc!(
             r#"
             [package]
```

### Comparing `maturin-1.0.0b5/src/ci.rs` & `maturin-1.0.0b7/src/ci.rs`

 * *Files 2% similar despite different names*

```diff
@@ -147,31 +147,36 @@
                 bridge_model,
                 BridgeModel::Bin(Some(_))
                     | BridgeModel::Bindings(..)
                     | BridgeModel::BindingsAbi3(..)
                     | BridgeModel::Cffi
                     | BridgeModel::UniFfi
             );
-        let gen_cmd = std::env::args()
+        let mut gen_cmd = std::env::args()
             .enumerate()
             .map(|(i, arg)| {
                 if i == 0 {
                     env!("CARGO_PKG_NAME").to_string()
                 } else {
                     arg
                 }
             })
             .collect::<Vec<String>>()
             .join(" ");
+        if gen_cmd.starts_with("maturin new") || gen_cmd.starts_with("maturin init") {
+            gen_cmd = format!("{} generate-ci github", env!("CARGO_PKG_NAME"));
+        }
         let mut conf = format!(
             "# This file is autogenerated by maturin v{version}
 # To update, run
 #
 #    {gen_cmd}
 #
+name: CI
+
 on:
   push:
     branches:
       - main
       - master
     tags:
       - '*'
@@ -505,14 +510,16 @@
             )
             .unwrap()
             .lines()
             .skip(5)
             .collect::<Vec<_>>()
             .join("\n");
         let expected = indoc! {r#"
+            name: CI
+
             on:
               push:
                 branches:
                   - main
                   - master
                 tags:
                   - '*'
@@ -632,14 +639,16 @@
             .generate_github("example", &BridgeModel::BindingsAbi3(3, 7), false)
             .unwrap()
             .lines()
             .skip(5)
             .collect::<Vec<_>>()
             .join("\n");
         let expected = indoc! {r#"
+            name: CI
+
             on:
               push:
                 branches:
                   - main
                   - master
                 tags:
                   - '*'
@@ -753,14 +762,16 @@
             )
             .unwrap()
             .lines()
             .skip(5)
             .collect::<Vec<_>>()
             .join("\n");
         let expected = indoc! {r#"
+            name: CI
+
             on:
               push:
                 branches:
                   - main
                   - master
                 tags:
                   - '*'
@@ -919,14 +930,16 @@
             .generate_github("example", &BridgeModel::Bin(None), true)
             .unwrap()
             .lines()
             .skip(5)
             .collect::<Vec<_>>()
             .join("\n");
         let expected = indoc! {r#"
+            name: CI
+
             on:
               push:
                 branches:
                   - main
                   - master
                 tags:
                   - '*'
```

### Comparing `maturin-1.0.0b5/src/compile.rs` & `maturin-1.0.0b7/src/compile.rs`

 * *Files 2% similar despite different names*

```diff
@@ -17,15 +17,22 @@
 /// The first version of pyo3 that supports building Windows abi3 wheel
 /// without `PYO3_NO_PYTHON` environment variable
 const PYO3_ABI3_NO_PYTHON_VERSION: (u64, u64, u64) = (0, 16, 4);
 
 /// crate types excluding `bin`, `cdylib` and `proc-macro`
 pub(crate) const LIB_CRATE_TYPES: [&str; 4] = ["lib", "dylib", "rlib", "staticlib"];
 
-pub(crate) type CompileTarget = (cargo_metadata::Target, BridgeModel);
+/// A cargo target to build
+#[derive(Debug, Clone)]
+pub struct CompileTarget {
+    /// The cargo target to build
+    pub target: cargo_metadata::Target,
+    /// The bridge model to use
+    pub bridge_model: BridgeModel,
+}
 
 /// A cargo build artifact
 #[derive(Debug, Clone)]
 pub struct BuildArtifact {
     /// Path to the build artifact
     pub path: PathBuf,
     /// Array of paths to include in the library search path, as indicated by
@@ -64,15 +71,15 @@
 
     let x86_64_artifacts = compile_targets(&x86_64_context, python_interpreter, targets)
         .context("Failed to build a x86_64 library through cargo")?;
 
     let mut universal_artifacts = Vec::with_capacity(targets.len());
     for (bridge_model, (aarch64_artifact, x86_64_artifact)) in targets
         .iter()
-        .map(|(_, bridge_model)| bridge_model)
+        .map(|target| &target.bridge_model)
         .zip(aarch64_artifacts.iter().zip(&x86_64_artifacts))
     {
         let build_type = if bridge_model.is_bin() {
             "bin"
         } else {
             "cdylib"
         };
@@ -128,43 +135,38 @@
 
 fn compile_targets(
     context: &BuildContext,
     python_interpreter: Option<&PythonInterpreter>,
     targets: &[CompileTarget],
 ) -> Result<Vec<HashMap<String, BuildArtifact>>> {
     let mut artifacts = Vec::with_capacity(targets.len());
-    for (target, bridge_model) in targets {
-        artifacts.push(compile_target(
-            context,
-            python_interpreter,
-            bridge_model,
-            target,
-        )?);
+    for target in targets {
+        artifacts.push(compile_target(context, python_interpreter, target)?);
     }
     Ok(artifacts)
 }
 
 fn compile_target(
     context: &BuildContext,
     python_interpreter: Option<&PythonInterpreter>,
-    bridge_model: &BridgeModel,
-    binding_target: &cargo_metadata::Target,
+    compile_target: &CompileTarget,
 ) -> Result<HashMap<String, BuildArtifact>> {
     let target = &context.target;
 
     let mut cargo_rustc: cargo_options::Rustc = context.cargo_options.clone().into();
     cargo_rustc.message_format = vec!["json".to_string()];
 
     // --release and --profile are conflicting options
     if context.release && cargo_rustc.profile.is_none() {
         cargo_rustc.release = true;
     }
 
     // Add `--crate-type cdylib` if available
-    if binding_target
+    if compile_target
+        .target
         .kind
         .iter()
         .any(|k| LIB_CRATE_TYPES.contains(&k.as_str()))
     {
         // `--crate-type` is stable since Rust 1.64.0
         // See https://github.com/rust-lang/cargo/pull/10838
         if target.rustc_version.semver >= RUST_1_64_0 {
@@ -177,17 +179,18 @@
 
     let manifest_dir = context.manifest_path.parent().unwrap();
     let mut rustflags = cargo_config2::Config::load_with_cwd(manifest_dir)?
         .rustflags(target_triple)?
         .unwrap_or_default();
 
     // We need to pass --bin / --lib
+    let bridge_model = &compile_target.bridge_model;
     match bridge_model {
         BridgeModel::Bin(..) => {
-            cargo_rustc.bin.push(binding_target.name.clone());
+            cargo_rustc.bin.push(compile_target.target.name.clone());
         }
         BridgeModel::Cffi
         | BridgeModel::UniFfi
         | BridgeModel::Bindings(..)
         | BridgeModel::BindingsAbi3(..) => {
             cargo_rustc.lib = true;
             // https://github.com/rust-lang/rust/issues/59302#issue-422994250
@@ -404,21 +407,36 @@
 
     if let Some(lib_dir) = env::var_os("MATURIN_PYTHON_SYSCONFIGDATA_DIR") {
         build_command.env("PYO3_CROSS_LIB_DIR", lib_dir);
     }
 
     // Set default macOS deployment target version
     if target.is_macos() && env::var_os("MACOSX_DEPLOYMENT_TARGET").is_none() {
-        use crate::target::rustc_macosx_target_version;
+        use crate::build_context::rustc_macosx_target_version;
 
-        let (major, minor) = rustc_macosx_target_version(target_triple);
-        build_command.env("MACOSX_DEPLOYMENT_TARGET", format!("{major}.{minor}"));
-        eprintln!(
-            "💻 Using `MACOSX_DEPLOYMENT_TARGET={major}.{minor}` for {target_triple} by default"
-        );
+        let target_config = context
+            .pyproject_toml
+            .as_ref()
+            .and_then(|x| x.target_config(target_triple));
+        let deployment_target = if let Some(deployment_target) = target_config
+            .as_ref()
+            .and_then(|config| config.macos_deployment_target.as_ref())
+        {
+            eprintln!(
+                "💻 Using `MACOSX_DEPLOYMENT_TARGET={deployment_target}` for {target_triple} by configuration"
+            );
+            deployment_target.clone()
+        } else {
+            let (major, minor) = rustc_macosx_target_version(target_triple);
+            eprintln!(
+                "💻 Using `MACOSX_DEPLOYMENT_TARGET={major}.{minor}` for {target_triple} by default"
+            );
+            format!("{major}.{minor}")
+        };
+        build_command.env("MACOSX_DEPLOYMENT_TARGET", deployment_target);
     }
 
     debug!("Running {:?}", build_command);
 
     let mut cargo_build = build_command
         .spawn()
         .context("Failed to run `cargo rustc`")?;
```

### Comparing `maturin-1.0.0b5/src/cross_compile.rs` & `maturin-1.0.0b7/src/cross_compile.rs`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/develop.rs` & `maturin-1.0.0b7/src/develop.rs`

 * *Files 22% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 use crate::build_options::CargoOptions;
 use crate::target::Arch;
 use crate::BuildOptions;
 use crate::PlatformTag;
 use crate::PythonInterpreter;
 use crate::Target;
 use anyhow::{anyhow, bail, Context, Result};
+use pep508_rs::{MarkerExpression, MarkerOperator, MarkerTree, MarkerValue};
 use std::path::Path;
 use std::process::Command;
 use tempfile::TempDir;
 
 /// Installs a crate by compiling it and copying the shared library to site-packages.
 /// Also adds the dist-info directory to make sure pip and other tools detect the library
 ///
@@ -80,20 +81,36 @@
             "pip".to_string(),
             "install".to_string(),
             "--disable-pip-version-check".to_string(),
         ];
         args.extend(build_context.metadata21.requires_dist.iter().map(|x| {
             let mut pkg = x.clone();
             // Remove extra marker to make it installable with pip
+            // Keep in sync with `Metadata21::merge_pyproject_toml()`!
             for extra in &extras {
-                pkg = pkg
-                    .replace(&format!(" and extra == '{extra}'"), "")
-                    .replace(&format!("; extra == '{extra}'"), "");
+                pkg.marker = pkg.marker.and_then(|marker| -> Option<MarkerTree> {
+                    match marker.clone() {
+                        MarkerTree::Expression(MarkerExpression {
+                            l_value: MarkerValue::Extra,
+                            operator: MarkerOperator::Equal,
+                            r_value: MarkerValue::QuotedString(extra_value),
+                        }) if &extra_value == extra => None,
+                        MarkerTree::And(and) => match &*and {
+                            [existing, MarkerTree::Expression(MarkerExpression {
+                                l_value: MarkerValue::Extra,
+                                operator: MarkerOperator::Equal,
+                                r_value: MarkerValue::QuotedString(extra_value),
+                            })] if extra_value == extra => Some(existing.clone()),
+                            _ => Some(marker),
+                        },
+                        _ => Some(marker),
+                    }
+                });
             }
-            pkg
+            pkg.to_string()
         }));
         let status = Command::new(interpreter.executable)
             .args(&args)
             .status()
             .context("Failed to run pip install")?;
         if !status.success() {
             bail!(r#"pip install finished with "{}""#, status)
```

### Comparing `maturin-1.0.0b5/src/lib.rs` & `maturin-1.0.0b7/src/lib.rs`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/main.rs` & `maturin-1.0.0b7/src/main.rs`

 * *Files 3% similar despite different names*

```diff
@@ -272,31 +272,22 @@
         } => {
             assert_eq!(build_options.interpreter.len(), 1);
             let context = build_options.into_build_context(true, strip, false)?;
 
             // Since afaik all other PEP 517 backends also return linux tagged wheels, we do so too
             let tags = match context.bridge() {
                 BridgeModel::Bindings(..) | BridgeModel::Bin(Some(..)) => {
-                    vec![context.interpreter[0].get_tag(
-                        &context.target,
-                        &[PlatformTag::Linux],
-                        context.universal2,
-                    )?]
+                    vec![context.interpreter[0].get_tag(&context, &[PlatformTag::Linux])?]
                 }
                 BridgeModel::BindingsAbi3(major, minor) => {
-                    let platform = context
-                        .target
-                        .get_platform_tag(&[PlatformTag::Linux], context.universal2)?;
+                    let platform = context.get_platform_tag(&[PlatformTag::Linux])?;
                     vec![format!("cp{major}{minor}-abi3-{platform}")]
                 }
                 BridgeModel::Bin(None) | BridgeModel::Cffi | BridgeModel::UniFfi => {
-                    context
-                        .target
-                        .get_universal_tags(&[PlatformTag::Linux], context.universal2)?
-                        .1
+                    context.get_universal_tags(&[PlatformTag::Linux])?.1
                 }
             };
 
             let mut writer = PathWriter::from_path(metadata_directory);
             write_dist_info(&mut writer, &context.metadata21, &tags)?;
             println!("{}", context.metadata21.get_dist_info_dir().display());
         }
@@ -349,15 +340,18 @@
                 args: args.collect(),
             };
             zig.execute()?;
             return Ok(());
         }
     }
 
+    #[cfg(not(feature = "wild"))]
     let opt = Opt::parse();
+    #[cfg(feature = "wild")]
+    let opt = Opt::parse_from(wild::args_os());
 
     match opt {
         Opt::Build {
             build,
             release,
             strip,
             sdist,
```

### Comparing `maturin-1.0.0b5/src/metadata.rs` & `maturin-1.0.0b7/src/metadata.rs`

 * *Files 8% similar despite different names*

```diff
@@ -1,16 +1,20 @@
-use crate::{CargoToml, PyProjectToml};
-use anyhow::{bail, Context, Result};
+use crate::PyProjectToml;
+use anyhow::{bail, format_err, Context, Result};
 use fs_err as fs;
+use indexmap::IndexMap;
+use pep440_rs::{Version, VersionSpecifiers};
+use pep508_rs::{MarkerExpression, MarkerOperator, MarkerTree, MarkerValue, Requirement};
 use regex::Regex;
 use serde::{Deserialize, Serialize};
 use std::collections::HashMap;
 use std::fmt::Write as _;
 use std::path::{Path, PathBuf};
 use std::str;
+use std::str::FromStr;
 
 /// The metadata required to generate the .dist-info directory
 #[derive(Serialize, Deserialize, Debug, Clone, Eq, PartialEq)]
 pub struct WheelMetadata {
     /// Python Package Metadata 2.1
     pub metadata21: Metadata21,
     /// The `[console_scripts]` for the entry_points.txt
@@ -19,22 +23,22 @@
     /// because package names normally contain minuses while module names
     /// have underscores. The package name is part of metadata21
     pub module_name: String,
 }
 
 /// Python Package Metadata 2.1 as specified in
 /// https://packaging.python.org/specifications/core-metadata/
-#[derive(Serialize, Deserialize, Debug, Default, Clone, Eq, PartialEq)]
+#[derive(Serialize, Deserialize, Debug, Clone, Eq, PartialEq)]
 #[serde(rename_all = "kebab-case")]
 #[allow(missing_docs)]
 pub struct Metadata21 {
     // Mandatory fields
     pub metadata_version: String,
     pub name: String,
-    pub version: String,
+    pub version: Version,
     // Optional fields
     pub platform: Vec<String>,
     pub supported_platform: Vec<String>,
     pub summary: Option<String>,
     pub description: Option<String>,
     pub description_content_type: Option<String>,
     pub keywords: Option<String>,
@@ -44,24 +48,60 @@
     pub author_email: Option<String>,
     pub maintainer: Option<String>,
     pub maintainer_email: Option<String>,
     pub license: Option<String>,
     // https://peps.python.org/pep-0639/#license-file-multiple-use
     pub license_files: Vec<PathBuf>,
     pub classifiers: Vec<String>,
-    pub requires_dist: Vec<String>,
+    pub requires_dist: Vec<Requirement>,
     pub provides_dist: Vec<String>,
     pub obsoletes_dist: Vec<String>,
-    pub requires_python: Option<String>,
+    pub requires_python: Option<VersionSpecifiers>,
     pub requires_external: Vec<String>,
-    pub project_url: HashMap<String, String>,
+    pub project_url: IndexMap<String, String>,
     pub provides_extra: Vec<String>,
-    pub scripts: HashMap<String, String>,
-    pub gui_scripts: HashMap<String, String>,
-    pub entry_points: HashMap<String, HashMap<String, String>>,
+    pub scripts: IndexMap<String, String>,
+    pub gui_scripts: IndexMap<String, String>,
+    pub entry_points: IndexMap<String, IndexMap<String, String>>,
+}
+
+impl Metadata21 {
+    /// Initializes with name, version and otherwise the defaults
+    pub fn new(name: String, version: Version) -> Self {
+        Self {
+            metadata_version: "2.1".to_string(),
+            name,
+            version,
+            platform: vec![],
+            supported_platform: vec![],
+            summary: None,
+            description: None,
+            description_content_type: None,
+            keywords: None,
+            home_page: None,
+            download_url: None,
+            author: None,
+            author_email: None,
+            maintainer: None,
+            maintainer_email: None,
+            license: None,
+            license_files: vec![],
+            classifiers: vec![],
+            requires_dist: vec![],
+            provides_dist: vec![],
+            obsoletes_dist: vec![],
+            requires_python: None,
+            requires_external: vec![],
+            project_url: Default::default(),
+            provides_extra: vec![],
+            scripts: Default::default(),
+            gui_scripts: Default::default(),
+            entry_points: Default::default(),
+        }
+    }
 }
 
 const PLAINTEXT_CONTENT_TYPE: &str = "text/plain; charset=UTF-8";
 const GFM_CONTENT_TYPE: &str = "text/markdown; charset=UTF-8; variant=GFM";
 
 /// Guess a Description-Content-Type based on the file extension,
 /// defaulting to plaintext if extension is unknown or empty.
@@ -237,26 +277,31 @@
             }
 
             if let Some(dependencies) = &project.dependencies {
                 self.requires_dist = dependencies.clone();
             }
 
             if let Some(dependencies) = &project.optional_dependencies {
+                // Transform the extra -> deps map into the PEP 508 style `dep ; extras = ...` style
                 for (extra, deps) in dependencies {
                     self.provides_extra.push(extra.clone());
                     for dep in deps {
-                        let dist = if let Some((dep, marker)) = dep.split_once(';') {
-                            // optional dependency already has environment markers
-                            let new_marker =
-                                format!("({}) and extra == '{}'", marker.trim(), extra);
-                            format!("{dep}; {new_marker}")
+                        let mut dep = dep.clone();
+                        // Keep in sync with `develop()`!
+                        let new_extra = MarkerTree::Expression(MarkerExpression {
+                            l_value: MarkerValue::Extra,
+                            operator: MarkerOperator::Equal,
+                            r_value: MarkerValue::QuotedString(extra.to_string()),
+                        });
+                        if let Some(existing) = dep.marker.take() {
+                            dep.marker = Some(MarkerTree::And(vec![existing, new_extra]));
                         } else {
-                            format!("{dep}; extra == '{extra}'")
-                        };
-                        self.requires_dist.push(dist);
+                            dep.marker = Some(new_extra);
+                        }
+                        self.requires_dist.push(dep);
                     }
                 }
             }
 
             if let Some(scripts) = &project.scripts {
                 self.scripts = scripts.clone();
             }
@@ -277,30 +322,27 @@
         Ok(())
     }
 
     /// Uses a Cargo.toml to create the metadata for python packages
     ///
     /// manifest_path must be the directory, not the file
     pub fn from_cargo_toml(
-        cargo_toml: &CargoToml,
         manifest_path: impl AsRef<Path>,
         cargo_metadata: &cargo_metadata::Metadata,
     ) -> Result<Metadata21> {
         let package = cargo_metadata
             .root_package()
             .context("Expected cargo to return metadata with root_package")?;
         let authors = package.authors.join(", ");
         let author_email = if authors.contains('@') {
             Some(authors.clone())
         } else {
             None
         };
 
-        let extra_metadata = cargo_toml.remaining_core_metadata();
-
         let mut description: Option<String> = None;
         let mut description_content_type: Option<String> = None;
         // See https://packaging.python.org/specifications/core-metadata/#description
         // and https://doc.rust-lang.org/cargo/reference/manifest.html#the-readme-field
         if package.readme == Some("false".into()) {
             // > You can suppress this behavior by setting this field to false
         } else if let Some(ref readme) = package.readme {
@@ -325,40 +367,37 @@
                     );
                     description = Some(fs::read_to_string(&guessed_readme).context(context)?);
                     description_content_type = Some(path_to_content_type(&guessed_readme));
                     break;
                 }
             }
         };
-        let name = extra_metadata
-            .name
-            .map(|name| {
-                if let Some(pos) = name.find('.') {
-                    name.split_at(pos).0.to_string()
-                } else {
-                    name.clone()
-                }
-            })
-            .unwrap_or_else(|| package.name.clone());
-        let mut project_url = HashMap::new();
+        let name = package.name.clone();
+        let mut project_url = IndexMap::new();
         if let Some(repository) = package.repository.as_ref() {
             project_url.insert("Source Code".to_string(), repository.clone());
         }
         let license_files = if let Some(license_file) = package.license_file.as_ref() {
             vec![manifest_path.as_ref().join(license_file)]
         } else {
             Vec::new()
         };
 
+        let version = Version::from_str(&package.version.to_string()).map_err(|err| {
+            format_err!(
+                "Rust version used in Cargo.toml is not a valid python version: {}. \
+                    Note that rust uses [SemVer](https://semver.org/) while python uses \
+                    [PEP 440](https://peps.python.org/pep-0440/), which have e.g. some differences \
+                    when declaring prereleases.",
+                err
+            )
+        })?;
         let metadata = Metadata21 {
-            metadata_version: "2.1".to_owned(),
-
+            // name, version and metadata_version are added through Metadata21::new()
             // Mapped from cargo metadata
-            name,
-            version: package.version.to_string(),
             summary: package.description.clone(),
             description,
             description_content_type,
             keywords: if package.keywords.is_empty() {
                 None
             } else {
                 Some(package.keywords.join(","))
@@ -371,39 +410,46 @@
             } else {
                 Some(authors)
             },
             author_email,
             license: package.license.clone(),
             license_files,
             project_url,
-            ..Default::default()
+            ..Metadata21::new(name, version)
         };
         Ok(metadata)
     }
 
     /// Formats the metadata into a list where keys with multiple values
     /// become multiple single-valued key-value pairs. This format is needed for the pypi
     /// uploader and for the METADATA file inside wheels
     pub fn to_vec(&self) -> Vec<(String, String)> {
         let mut fields = vec![
             ("Metadata-Version", self.metadata_version.clone()),
             ("Name", self.name.clone()),
-            ("Version", self.get_pep440_version()),
+            ("Version", self.version.to_string()),
         ];
 
         let mut add_vec = |name, values: &[String]| {
             for i in values {
                 fields.push((name, i.clone()));
             }
         };
 
         add_vec("Platform", &self.platform);
         add_vec("Supported-Platform", &self.supported_platform);
         add_vec("Classifier", &self.classifiers);
-        add_vec("Requires-Dist", &self.requires_dist);
+        add_vec(
+            "Requires-Dist",
+            &self
+                .requires_dist
+                .iter()
+                .map(ToString::to_string)
+                .collect::<Vec<String>>(),
+        );
         add_vec("Provides-Dist", &self.provides_dist);
         add_vec("Obsoletes-Dist", &self.obsoletes_dist);
         add_vec("Requires-External", &self.requires_external);
         add_vec("Provides-Extra", &self.provides_extra);
 
         let license_files: Vec<String> = self
             .license_files
@@ -423,15 +469,21 @@
         add_option("Home-Page", &self.home_page);
         add_option("Download-URL", &self.download_url);
         add_option("Author", &self.author);
         add_option("Author-email", &self.author_email);
         add_option("Maintainer", &self.maintainer);
         add_option("Maintainer-email", &self.maintainer_email);
         add_option("License", &self.license.as_deref().map(fold_header));
-        add_option("Requires-Python", &self.requires_python);
+        add_option(
+            "Requires-Python",
+            &self
+                .requires_python
+                .as_ref()
+                .map(|requires_python| requires_python.to_string()),
+        );
         add_option("Description-Content-Type", &self.description_content_type);
         // Project-URL is special
         // "A string containing a browsable URL for the project and a label for it, separated by a comma."
         // `Project-URL: Bug Tracker, http://bitbucket.org/tarek/distribute/issues/`
         for (key, value) in self.project_url.iter() {
             fields.push(("Project-URL", format!("{key}, {value}")))
         }
@@ -480,29 +532,15 @@
         let re = Regex::new(r"[^\w\d.]+").unwrap();
         re.replace_all(&self.name, "_").to_string()
     }
 
     /// Returns the version encoded according to PEP 427, Section "Escaping
     /// and Unicode"
     pub fn get_version_escaped(&self) -> String {
-        self.get_pep440_version().replace('-', "_")
-    }
-
-    /// Returns the version encoded according to PEP 440
-    ///
-    /// See https://github.com/pypa/setuptools/blob/d90cf84e4890036adae403d25c8bb4ee97841bbf/pkg_resources/__init__.py#L1336-L1345
-    pub fn get_pep440_version(&self) -> String {
-        match pep440::Version::parse(&self.version) {
-            Some(ver) => ver.normalize(),
-            None => {
-                let ver = self.version.replace(' ', ".");
-                let re = Regex::new(r"[^A-Za-z0-9.]+").unwrap();
-                re.replace_all(&ver, "-").to_string()
-            }
-        }
+        self.version.to_string().replace('-', "_")
     }
 
     /// Returns the name of the .dist-info directory as defined in the wheel specification
     pub fn get_dist_info_dir(&self) -> PathBuf {
         PathBuf::from(format!(
             "{}-{}.dist-info",
             &self.get_distribution_escaped(),
@@ -558,24 +596,22 @@
         let readme_path = if cfg!(windows) {
             readme_path.to_str().unwrap().replace('\\', "/")
         } else {
             readme_path.to_str().unwrap().to_string()
         };
 
         let toml_with_path = cargo_toml.replace("REPLACE_README_PATH", &readme_path);
-        fs::write(&manifest_path, &toml_with_path).unwrap();
+        fs::write(&manifest_path, toml_with_path).unwrap();
 
-        let cargo_toml_struct: CargoToml = toml::from_str(&toml_with_path).unwrap();
         let cargo_metadata = MetadataCommand::new()
             .manifest_path(manifest_path)
             .exec()
             .unwrap();
 
-        let metadata =
-            Metadata21::from_cargo_toml(&cargo_toml_struct, crate_path, &cargo_metadata).unwrap();
+        let metadata = Metadata21::from_cargo_toml(crate_path, &cargo_metadata).unwrap();
 
         let actual = metadata.to_file_contents().unwrap();
 
         assert_eq!(
             actual.trim(),
             expected.trim(),
             "Actual metadata differed from expected\nEXPECTED:\n{}\n\nGOT:\n{}",
@@ -586,21 +622,14 @@
         // get_dist_info_dir test checks against hard-coded values - check that they are as expected in the source first
         assert!(
             cargo_toml.contains("name = \"info-project\"")
                 && cargo_toml.contains("version = \"0.1.0\""),
             "cargo_toml name and version string do not match hardcoded values, test will fail",
         );
 
-        if cargo_toml_struct.remaining_core_metadata().name.is_none() {
-            assert_eq!(
-                metadata.get_dist_info_dir(),
-                PathBuf::from("info_project-0.1.0.dist-info"),
-                "Dist info dir differed from expected"
-            );
-        }
         metadata
     }
 
     #[test]
     fn test_metadata_from_cargo_toml() {
         let readme = indoc!(
             r#"
@@ -645,67 +674,14 @@
         "#
         );
 
         assert_metadata_from_cargo_toml(readme, cargo_toml, expected);
     }
 
     #[test]
-    fn test_metadata_from_cargo_toml_name_override() {
-        let readme = indoc!(
-            r#"
-            Some test package
-            =================
-        "#
-        );
-
-        let cargo_toml = indoc!(
-            r#"
-            [package]
-            authors = ["konstin <konstin@mailbox.org>"]
-            name = "info-project"
-            version = "0.1.0"
-            description = "A test project"
-            homepage = "https://example.org"
-            readme = "REPLACE_README_PATH"
-
-            [lib]
-            crate-type = ["cdylib"]
-            name = "pyo3_pure"
-
-            [package.metadata.maturin]
-            name = "info"
-        "#
-        );
-
-        let expected = indoc!(
-            r#"
-            Metadata-Version: 2.1
-            Name: info
-            Version: 0.1.0
-            Summary: A test project
-            Home-Page: https://example.org
-            Author: konstin <konstin@mailbox.org>
-            Author-email: konstin <konstin@mailbox.org>
-            Description-Content-Type: text/markdown; charset=UTF-8; variant=GFM
-
-            Some test package
-            =================
-        "#
-        );
-
-        let metadata = assert_metadata_from_cargo_toml(readme, cargo_toml, expected);
-
-        assert_eq!(
-            metadata.get_dist_info_dir(),
-            PathBuf::from("info-0.1.0.dist-info"),
-            "Dist info dir differed from expected"
-        );
-    }
-
-    #[test]
     fn test_path_to_content_type() {
         for (filename, expected) in &[
             ("r.md", GFM_CONTENT_TYPE),
             ("r.markdown", GFM_CONTENT_TYPE),
             ("r.mArKdOwN", GFM_CONTENT_TYPE),
             ("r.rst", "text/x-rst; charset=UTF-8"),
             ("r.somethingelse", PLAINTEXT_CONTENT_TYPE),
@@ -722,22 +698,19 @@
             );
         }
     }
 
     #[test]
     fn test_merge_metadata_from_pyproject_toml() {
         let manifest_dir = PathBuf::from("test-crates").join("pyo3-pure");
-        let cargo_toml_str = fs_err::read_to_string(manifest_dir.join("Cargo.toml")).unwrap();
-        let cargo_toml: CargoToml = toml::from_str(&cargo_toml_str).unwrap();
         let cargo_metadata = MetadataCommand::new()
             .manifest_path(manifest_dir.join("Cargo.toml"))
             .exec()
             .unwrap();
-        let mut metadata =
-            Metadata21::from_cargo_toml(&cargo_toml, &manifest_dir, &cargo_metadata).unwrap();
+        let mut metadata = Metadata21::from_cargo_toml(&manifest_dir, &cargo_metadata).unwrap();
         let pyproject_toml = PyProjectToml::new(manifest_dir.join("pyproject.toml")).unwrap();
         metadata
             .merge_pyproject_toml(&manifest_dir, &pyproject_toml)
             .unwrap();
         assert_eq!(
             metadata.summary,
             Some("Implements a dummy function in Rust".to_string())
@@ -756,16 +729,17 @@
             metadata.gui_scripts["get_42_gui"],
             "pyo3_pure:DummyClass.get_42"
         );
         assert_eq!(metadata.provides_extra, &["test"]);
         assert_eq!(
             metadata.requires_dist,
             &[
-                "attrs; extra == 'test'",
-                "boltons; (sys_platform == 'win32') and extra == 'test'"
+                Requirement::from_str("attrs; extra == 'test'",).unwrap(),
+                Requirement::from_str("boltons; (sys_platform == 'win32') and extra == 'test'")
+                    .unwrap(),
             ]
         );
         assert_eq!(metadata.license.as_ref().unwrap(), "MIT");
 
         let license_file = &metadata.license_files[0];
         assert_eq!(license_file.file_name().unwrap(), "LICENSE");
 
@@ -773,22 +747,19 @@
         let pkginfo: Result<python_pkginfo::Metadata, _> = content.parse();
         assert!(pkginfo.is_ok());
     }
 
     #[test]
     fn test_merge_metadata_from_pyproject_toml_with_customized_python_source_dir() {
         let manifest_dir = PathBuf::from("test-crates").join("pyo3-mixed-py-subdir");
-        let cargo_toml_str = fs_err::read_to_string(manifest_dir.join("Cargo.toml")).unwrap();
-        let cargo_toml: CargoToml = toml::from_str(&cargo_toml_str).unwrap();
         let cargo_metadata = MetadataCommand::new()
             .manifest_path(manifest_dir.join("Cargo.toml"))
             .exec()
             .unwrap();
-        let mut metadata =
-            Metadata21::from_cargo_toml(&cargo_toml, &manifest_dir, &cargo_metadata).unwrap();
+        let mut metadata = Metadata21::from_cargo_toml(&manifest_dir, &cargo_metadata).unwrap();
         let pyproject_toml = PyProjectToml::new(manifest_dir.join("pyproject.toml")).unwrap();
         metadata
             .merge_pyproject_toml(&manifest_dir, &pyproject_toml)
             .unwrap();
         // defined in Cargo.toml
         assert_eq!(
             metadata.summary,
@@ -797,40 +768,34 @@
         // defined in pyproject.toml
         assert_eq!(metadata.scripts["get_42"], "pyo3_mixed_py_subdir:get_42");
     }
 
     #[test]
     fn test_implicit_readme() {
         let manifest_dir = PathBuf::from("test-crates").join("pyo3-mixed");
-        let cargo_toml_str = fs_err::read_to_string(manifest_dir.join("Cargo.toml")).unwrap();
-        let cargo_toml = toml::from_str(&cargo_toml_str).unwrap();
         let cargo_metadata = MetadataCommand::new()
             .manifest_path(manifest_dir.join("Cargo.toml"))
             .exec()
             .unwrap();
-        let metadata =
-            Metadata21::from_cargo_toml(&cargo_toml, &manifest_dir, &cargo_metadata).unwrap();
+        let metadata = Metadata21::from_cargo_toml(&manifest_dir, &cargo_metadata).unwrap();
         assert!(metadata.description.unwrap().starts_with("# pyo3-mixed"));
         assert_eq!(
             metadata.description_content_type.unwrap(),
             "text/markdown; charset=UTF-8; variant=GFM"
         );
     }
 
     #[test]
     fn test_merge_metadata_from_pyproject_dynamic_license_test() {
         let manifest_dir = PathBuf::from("test-crates").join("license-test");
-        let cargo_toml_str = fs_err::read_to_string(manifest_dir.join("Cargo.toml")).unwrap();
-        let cargo_toml: CargoToml = toml::from_str(&cargo_toml_str).unwrap();
         let cargo_metadata = MetadataCommand::new()
             .manifest_path(manifest_dir.join("Cargo.toml"))
             .exec()
             .unwrap();
-        let mut metadata =
-            Metadata21::from_cargo_toml(&cargo_toml, &manifest_dir, &cargo_metadata).unwrap();
+        let mut metadata = Metadata21::from_cargo_toml(&manifest_dir, &cargo_metadata).unwrap();
         let pyproject_toml = PyProjectToml::new(manifest_dir.join("pyproject.toml")).unwrap();
         metadata
             .merge_pyproject_toml(&manifest_dir, &pyproject_toml)
             .unwrap();
 
         // verify Cargo.toml value came through
         assert_eq!(metadata.license.as_ref().unwrap(), "MIT");
```

### Comparing `maturin-1.0.0b5/src/module_writer.rs` & `maturin-1.0.0b7/src/module_writer.rs`

 * *Files 2% similar despite different names*

```diff
@@ -7,14 +7,15 @@
 use anyhow::{anyhow, bail, Context, Result};
 use flate2::write::GzEncoder;
 use flate2::Compression;
 use fs_err as fs;
 use fs_err::File;
 use ignore::overrides::Override;
 use ignore::WalkBuilder;
+use indexmap::IndexMap;
 use normpath::PathExt as _;
 use sha2::{Digest, Sha256};
 use std::collections::{HashMap, HashSet};
 use std::env;
 use std::ffi::OsStr;
 use std::fmt::Write as _;
 #[cfg(target_family = "unix")]
@@ -89,15 +90,15 @@
     pub fn venv(target: &Target, venv_dir: &Path, bridge: &BridgeModel) -> Result<Self> {
         let interpreter =
             PythonInterpreter::check_executable(target.get_venv_python(venv_dir), target, bridge)?
                 .ok_or_else(|| {
                     anyhow!("Expected `python` to be a python interpreter inside a virtualenv ಠ_ಠ")
                 })?;
 
-        let base_path = target.get_venv_site_package(venv_dir, &interpreter);
+        let base_path = interpreter.get_venv_site_package(venv_dir, target);
 
         Ok(PathWriter {
             base_path,
             record: Vec::new(),
         })
     }
 
@@ -502,15 +503,15 @@
 
     Ok(wheel_file)
 }
 
 /// https://packaging.python.org/specifications/entry-points/
 fn entry_points_txt(
     entry_type: &str,
-    entrypoints: &HashMap<String, String, impl std::hash::BuildHasher>,
+    entrypoints: &IndexMap<String, String, impl std::hash::BuildHasher>,
 ) -> String {
     entrypoints
         .iter()
         .fold(format!("[{entry_type}]\n"), |text, (k, v)| {
             text + k + "=" + v + "\n"
         })
 }
@@ -1268,21 +1269,22 @@
     }
     Ok(())
 }
 
 #[cfg(test)]
 mod tests {
     use ignore::overrides::OverrideBuilder;
+    use pep440_rs::Version;
 
     use super::*;
 
     #[test]
     // The mechanism is the same for wheel_writer
     fn sdist_writer_excludes() -> Result<(), Box<dyn std::error::Error>> {
-        let metadata = Metadata21::default();
+        let metadata = Metadata21::new("dummy".to_string(), Version::from_release(vec![1, 0]));
         let perm = 0o777;
 
         // No excludes
         let tmp_dir = TempDir::new()?;
         let mut writer = SDistWriter::new(&tmp_dir, &metadata, None)?;
         assert!(writer.files.is_empty());
         writer.add_bytes_with_permissions("test", &[], perm)?;
```

### Comparing `maturin-1.0.0b5/src/new_project.rs` & `maturin-1.0.0b7/src/new_project.rs`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/project_layout.rs` & `maturin-1.0.0b7/src/project_layout.rs`

 * *Files 2% similar despite different names*

```diff
@@ -104,35 +104,35 @@
             cargo_options.merge_with_pyproject_toml(tool_maturin.clone())
         } else {
             Vec::new()
         };
 
         let cargo_metadata = Self::resolve_cargo_metadata(&manifest_file, &cargo_options)?;
 
-        let mut metadata21 =
-            Metadata21::from_cargo_toml(&cargo_toml, manifest_dir, &cargo_metadata)
-                .context("Failed to parse Cargo.toml into python metadata")?;
+        let mut metadata21 = Metadata21::from_cargo_toml(manifest_dir, &cargo_metadata)
+            .context("Failed to parse Cargo.toml into python metadata")?;
         if let Some(pyproject) = pyproject {
             let pyproject_dir = pyproject_file.parent().unwrap();
             metadata21.merge_pyproject_toml(pyproject_dir, pyproject)?;
         }
-        let extra_metadata = cargo_toml.remaining_core_metadata();
 
         let crate_name = &cargo_toml.package.name;
 
         // If the package name contains minuses, you must declare a module with
         // underscores as lib name
         let module_name = cargo_toml
             .lib
             .as_ref()
             .and_then(|lib| lib.name.as_ref())
             .unwrap_or(crate_name)
             .to_owned();
 
-        let extension_name = extra_metadata.name.as_ref().unwrap_or(&module_name);
+        let extension_name = pyproject
+            .and_then(|x| x.module_name())
+            .unwrap_or(&module_name);
 
         let project_root = if pyproject_file.is_file() {
             pyproject_file.parent().unwrap_or(manifest_dir)
         } else {
             manifest_dir
         };
         let python_packages = pyproject
@@ -164,31 +164,21 @@
                     } else {
                         project_root.to_path_buf()
                     }
                 }
                 None => project_root.to_path_buf(),
             },
         };
-        let data = match pyproject.and_then(|x| x.data()) {
-            Some(data) => {
-                if data.is_absolute() {
-                    Some(data.to_path_buf())
-                } else {
-                    Some(project_root.join(data))
-                }
+        let data = pyproject.and_then(|x| x.data()).map(|data| {
+            if data.is_absolute() {
+                data.to_path_buf()
+            } else {
+                project_root.join(data)
             }
-            None => extra_metadata.data.as_ref().map(|data| {
-                let data = Path::new(data);
-                if data.is_absolute() {
-                    data.to_path_buf()
-                } else {
-                    manifest_dir.join(data)
-                }
-            }),
-        };
+        });
         let project_layout =
             ProjectLayout::determine(project_root, extension_name, py_root, python_packages, data)?;
         Ok(Self {
             project_layout,
             cargo_toml_path: manifest_file,
             cargo_toml,
             pyproject_toml_path: pyproject_file,
```

### Comparing `maturin-1.0.0b5/src/pyproject_toml.rs` & `maturin-1.0.0b7/src/pyproject_toml.rs`

 * *Files 10% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 //! A pyproject.toml as specified in PEP 517
 
 use crate::PlatformTag;
 use anyhow::{format_err, Result};
 use fs_err as fs;
 use pyproject_toml::PyProjectToml as ProjectToml;
 use serde::{Deserialize, Serialize};
+use std::collections::HashMap;
 use std::path::{Path, PathBuf};
 
 /// The `[tool]` section of a pyproject.toml
 #[derive(Serialize, Deserialize, Debug, Clone)]
 #[serde(rename_all = "kebab-case")]
 pub struct Tool {
     maturin: Option<ToolMaturin>,
@@ -77,19 +78,43 @@
                 format: formats,
             } if formats.targets(format) => Some(path),
             _ => None,
         }
     }
 }
 
+/// Cargo compile target
+#[derive(Serialize, Deserialize, Debug, Clone, Default)]
+#[serde(rename_all = "kebab-case")]
+pub struct CargoTarget {
+    /// Name as given in the `Cargo.toml` or generated from the file name
+    pub name: String,
+    /// Kind of target ("bin", "lib")
+    pub kind: Option<String>,
+    // TODO: Add bindings option
+    // Bridge model, which kind of bindings to use
+    // pub bindings: Option<String>,
+}
+
+/// Target configuration
+#[derive(Serialize, Deserialize, Debug, Clone)]
+#[serde(rename_all = "kebab-case")]
+pub struct TargetConfig {
+    /// macOS deployment target version
+    #[serde(alias = "macosx-deployment-target")]
+    pub macos_deployment_target: Option<String>,
+}
+
 /// The `[tool.maturin]` section of a pyproject.toml
 #[derive(Serialize, Deserialize, Debug, Clone)]
 #[serde(rename_all = "kebab-case")]
 pub struct ToolMaturin {
     // maturin specific options
+    // extension module name, accepts setuptools style import name like `foo.bar`
+    module_name: Option<String>,
     include: Option<Vec<GlobPattern>>,
     exclude: Option<Vec<GlobPattern>>,
     bindings: Option<String>,
     #[serde(alias = "manylinux")]
     compatibility: Option<PlatformTag>,
     #[serde(default)]
     skip_auditwheel: bool,
@@ -97,14 +122,19 @@
     strip: bool,
     /// The directory with python module, contains `<module_name>/__init__.py`
     python_source: Option<PathBuf>,
     /// Python packages to include
     python_packages: Option<Vec<String>>,
     /// Path to the wheel directory, defaults to `<module_name>.data`
     data: Option<PathBuf>,
+    /// Cargo compile targets
+    pub targets: Option<Vec<CargoTarget>>,
+    /// Target configuration
+    #[serde(default, rename = "target")]
+    pub target_config: HashMap<String, TargetConfig>,
     // Some customizable cargo options
     /// Build artifacts with the specified Cargo profile
     pub profile: Option<String>,
     /// Space or comma separated list of features to activate
     pub features: Option<Vec<String>>,
     /// Activate all available features
     pub all_features: Option<bool>,
@@ -166,14 +196,19 @@
 
     /// Returns the values of `[tool.maturin]` in pyproject.toml
     #[inline]
     pub fn maturin(&self) -> Option<&ToolMaturin> {
         self.tool.as_ref()?.maturin.as_ref()
     }
 
+    /// Returns the value of `[tool.maturin.module-name]` in pyproject.toml
+    pub fn module_name(&self) -> Option<&str> {
+        self.maturin()?.module_name.as_deref()
+    }
+
     /// Returns the value of `[tool.maturin.include]` in pyproject.toml
     pub fn include(&self) -> Option<&[GlobPattern]> {
         self.maturin()?.include.as_ref().map(AsRef::as_ref)
     }
 
     /// Returns the value of `[tool.maturin.exclude]` in pyproject.toml
     pub fn exclude(&self) -> Option<&[GlobPattern]> {
@@ -217,14 +252,25 @@
     }
 
     /// Returns the value of `[tool.maturin.data]` in pyproject.toml
     pub fn data(&self) -> Option<&Path> {
         self.maturin().and_then(|maturin| maturin.data.as_deref())
     }
 
+    /// Returns the value of `[tool.maturin.targets]` in pyproject.toml
+    pub fn targets(&self) -> Option<Vec<CargoTarget>> {
+        self.maturin().and_then(|maturin| maturin.targets.clone())
+    }
+
+    /// Returns the value of `[tool.maturin.target.<target>]` in pyproject.toml
+    pub fn target_config(&self, target: &str) -> Option<&TargetConfig> {
+        self.maturin()
+            .and_then(|maturin| maturin.target_config.get(target))
+    }
+
     /// Returns the value of `[tool.maturin.manifest-path]` in pyproject.toml
     pub fn manifest_path(&self) -> Option<&Path> {
         self.maturin()?.manifest_path.as_deref()
     }
 
     /// Having a pyproject.toml without a version constraint is a bad idea
     /// because at some point we'll have to do breaking changes and then source
@@ -233,18 +279,18 @@
     /// Returns true if the pyproject.toml has the constraint
     pub fn warn_missing_maturin_version(&self) -> bool {
         let maturin = env!("CARGO_PKG_NAME");
         if let Some(requires_maturin) = self
             .build_system
             .requires
             .iter()
-            .find(|x| x.starts_with(maturin))
+            .find(|x| x.name == maturin)
         {
             let current_major: usize = env!("CARGO_PKG_VERSION_MAJOR").parse().unwrap();
-            if requires_maturin == maturin {
+            if requires_maturin.version_or_url.is_none() {
                 eprintln!(
                     "⚠️  Warning: Please use {maturin} in pyproject.toml with a version constraint, \
                     e.g. `requires = [\"{maturin}>={current}.0,<{next}.0\"]`. \
                     This will become an error.",
                     maturin = maturin,
                     current = current_major,
                     next = current_major + 1,
@@ -299,14 +345,22 @@
             python-packages = ["foo", "bar"]
             manifest-path = "Cargo.toml"
             profile = "dev"
             features = ["foo", "bar"]
             no-default-features = true
             locked = true
             rustc-args = ["-Z", "unstable-options"]
+
+            [[tool.maturin.targets]]
+            name = "pyo3_pure"
+            kind = "lib"
+            bindings = "pyo3"
+
+            [tool.maturin.target."x86_64-apple-darwin"]
+            macos-deployment-target = "10.12"
             "#,
         )
         .unwrap();
         let pyproject = PyProjectToml::new(pyproject_file).unwrap();
         assert_eq!(pyproject.manifest_path(), Some(Path::new("Cargo.toml")));
 
         let maturin = pyproject.maturin().unwrap();
@@ -323,14 +377,21 @@
             maturin.rustc_args,
             Some(vec!["-Z".to_string(), "unstable-options".to_string()])
         );
         assert_eq!(
             maturin.python_packages,
             Some(vec!["foo".to_string(), "bar".to_string()])
         );
+        let targets = maturin.targets.as_ref().unwrap();
+        assert_eq!("pyo3_pure", targets[0].name);
+        let target_config = pyproject.target_config("x86_64-apple-darwin").unwrap();
+        assert_eq!(
+            target_config.macos_deployment_target.as_deref(),
+            Some("10.12")
+        );
     }
 
     #[test]
     fn test_warn_missing_maturin_version() {
         let with_constraint = PyProjectToml::new("test-crates/pyo3-pure/pyproject.toml").unwrap();
         assert!(with_constraint.warn_missing_maturin_version());
         let without_constraint_dir = TempDir::new().unwrap();
```

### Comparing `maturin-1.0.0b5/src/python_interpreter/config.rs` & `maturin-1.0.0b7/src/python_interpreter/config.rs`

 * *Files 8% similar despite different names*

```diff
@@ -71,24 +71,36 @@
     /// Pointer width
     pub pointer_width: Option<usize>,
 }
 
 impl InterpreterConfig {
     /// Lookup a wellknown sysconfig for a given Python interpreter
     pub fn lookup(
-        os: Os,
-        arch: Arch,
+        target: &Target,
         python_impl: InterpreterKind,
         python_version: (usize, usize),
-    ) -> Option<&'static Self> {
+    ) -> Option<Self> {
         let (major, minor) = python_version;
-        if let Some(os_sysconfigs) = WELLKNOWN_SYSCONFIG.get(&os) {
-            if let Some(sysconfigs) = os_sysconfigs.get(&arch) {
-                return sysconfigs.iter().find(|s| {
-                    s.interpreter_kind == python_impl && s.major == major && s.minor == minor
+        if let Some(os_sysconfigs) = WELLKNOWN_SYSCONFIG.get(&target.target_os()) {
+            if let Some(sysconfigs) = os_sysconfigs.get(&target.target_arch()) {
+                return sysconfigs.iter().find_map(|s| {
+                    if s.interpreter_kind == python_impl && s.major == major && s.minor == minor {
+                        if python_version >= (3, 11) && target.is_musl_target() {
+                            // See https://github.com/pypa/auditwheel/issues/349
+                            let mut musl_config = s.clone();
+                            musl_config.ext_suffix = s
+                                .ext_suffix
+                                .replace("-gnu", &format!("-{}", target.target_env()));
+                            Some(musl_config)
+                        } else {
+                            Some(s.clone())
+                        }
+                    } else {
+                        None
+                    }
                 });
             }
         }
         None
     }
 
     /// Lookup wellknown sysconfigs for a given target
@@ -251,14 +263,31 @@
     fn test_load_sysconfig() {
         let linux_sysconfig = WELLKNOWN_SYSCONFIG.get(&Os::Linux).unwrap();
         assert!(linux_sysconfig.contains_key(&Arch::X86_64));
     }
 
     #[test]
     fn test_pyo3_config_file() {
-        let sysconfig =
-            InterpreterConfig::lookup(Os::Linux, Arch::X86_64, InterpreterKind::CPython, (3, 10))
-                .unwrap();
+        let sysconfig = InterpreterConfig::lookup(
+            &Target::from_target_triple(Some("x86_64-unknown-linux-gnu".to_string())).unwrap(),
+            InterpreterKind::CPython,
+            (3, 10),
+        )
+        .unwrap();
+        assert_eq!(sysconfig.ext_suffix, ".cpython-310-x86_64-linux-gnu.so");
         let config_file = sysconfig.pyo3_config_file();
         assert_eq!(config_file, "implementation=CPython\nversion=3.10\nshared=true\nabi3=false\nbuild_flags=WITH_THREAD\nsuppress_build_script_link_lines=false\npointer_width=64");
     }
+
+    #[test]
+    fn test_pyo3_config_file_musl_python_3_11() {
+        let sysconfig = InterpreterConfig::lookup(
+            &Target::from_target_triple(Some("x86_64-unknown-linux-musl".to_string())).unwrap(),
+            InterpreterKind::CPython,
+            (3, 11),
+        )
+        .unwrap();
+        assert_eq!(sysconfig.ext_suffix, ".cpython-311-x86_64-linux-musl.so");
+        let config_file = sysconfig.pyo3_config_file();
+        assert_eq!(config_file, "implementation=CPython\nversion=3.11\nshared=true\nabi3=false\nbuild_flags=WITH_THREAD\nsuppress_build_script_link_lines=false\npointer_width=64");
+    }
 }
```

### Comparing `maturin-1.0.0b5/src/python_interpreter/get_interpreter_metadata.py` & `maturin-1.0.0b7/src/python_interpreter/get_interpreter_metadata.py`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/python_interpreter/mod.rs` & `maturin-1.0.0b7/src/python_interpreter/mod.rs`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 pub use self::config::InterpreterConfig;
 use crate::auditwheel::PlatformTag;
-use crate::{BridgeModel, Target};
+use crate::{BridgeModel, BuildContext, Target};
 use anyhow::{bail, format_err, Context, Result};
+use pep440_rs::{Version, VersionSpecifiers};
 use regex::Regex;
 use serde::Deserialize;
 use std::collections::HashSet;
 use std::fmt;
 use std::io::{self, Write};
 use std::ops::Deref;
 use std::path::{Path, PathBuf};
@@ -26,23 +27,26 @@
 /// Identifies conditions where we do not want to build wheels
 fn windows_interpreter_no_build(
     major: usize,
     minor: usize,
     target_width: usize,
     pointer_width: usize,
     min_python_minor: usize,
+    requires_python: Option<&VersionSpecifiers>,
 ) -> bool {
-    // Python 2 support has been dropped
-    if major == 2 {
+    // Only python 3 with supported major versions
+    if major != 3 || minor < min_python_minor {
         return true;
     }
 
-    // Ignore python 3.0 - 3.5
-    if major == 3 && minor < min_python_minor {
-        return true;
+    // From requires-python in pyproject.toml
+    if let Some(requires_python) = requires_python {
+        if !requires_python.contains(&Version::from_release(vec![major, minor])) {
+            return true;
+        }
     }
 
     // There can be 32-bit installations on a 64-bit machine, but we can't link
     // those for 64-bit targets
     if pointer_width != target_width {
         eprintln!(
             "👽 {major}.{minor} is installed as {pointer_width}-bit, while the target is {target_width}-bit. Skipping."
@@ -85,15 +89,19 @@
 ///
 /// The information required can either by obtained by parsing this output directly or
 /// by invoking the interpreters to obtain the information.
 ///
 /// As well as the version numbers, etc. of the interpreters we also have to find the
 /// pointer width to make sure that the pointer width (32-bit or 64-bit) matches across
 /// platforms.
-fn find_all_windows(target: &Target, min_python_minor: usize) -> Result<Vec<String>> {
+fn find_all_windows(
+    target: &Target,
+    min_python_minor: usize,
+    requires_python: Option<&VersionSpecifiers>,
+) -> Result<Vec<String>> {
     let code = "import sys; print(sys.executable or '')";
     let mut interpreter = vec![];
     let mut versions_found = HashSet::new();
 
     // If Python is installed from Python.org it should include the "python launcher"
     // which is used to find the installed interpreters
     let execution = Command::new("cmd")
@@ -132,14 +140,15 @@
 
                     if windows_interpreter_no_build(
                         major,
                         minor,
                         target.pointer_width(),
                         pointer_width,
                         min_python_minor,
+                        requires_python,
                     ) {
                         continue;
                     }
 
                     let executable = capture.get(6).unwrap().as_str();
                     let version = format!("-{major}.{minor}-{pointer_width}");
                     let output = Command::new(executable)
@@ -188,14 +197,15 @@
             if let Some(python_info) = windows_python_info(&executable)? {
                 if windows_interpreter_no_build(
                     python_info.major,
                     python_info.minor,
                     target.pointer_width(),
                     python_info.pointer_width.unwrap(),
                     min_python_minor,
+                    requires_python,
                 ) {
                     continue;
                 }
                 interpreter.push(String::from(executable.to_str().unwrap()));
                 versions_found.insert((python_info.major, python_info.minor));
             }
         }
@@ -208,14 +218,15 @@
             if let Some(python_info) = windows_python_info(Path::new(&executable))? {
                 if windows_interpreter_no_build(
                     python_info.major,
                     python_info.minor,
                     target.pointer_width(),
                     python_info.pointer_width.unwrap(),
                     min_python_minor,
+                    requires_python,
                 ) {
                     continue;
                 }
                 interpreter.push(executable);
                 versions_found.insert((3, minor));
             }
         }
@@ -434,33 +445,29 @@
 
     /// Returns the supported python environment in the PEP 425 format used for the wheel filename:
     /// {python tag}-{abi tag}-{platform tag}
     ///
     /// Don't ask me why or how, this is just what setuptools uses so I'm also going to use
     ///
     /// If abi3 is true, cpython wheels use the generic abi3 with the given version as minimum
-    pub fn get_tag(
-        &self,
-        target: &Target,
-        platform_tags: &[PlatformTag],
-        universal2: bool,
-    ) -> Result<String> {
+    pub fn get_tag(&self, context: &BuildContext, platform_tags: &[PlatformTag]) -> Result<String> {
         // Restrict `sysconfig.get_platform()` usage to Windows and non-portable Linux only for now
         // so we don't need to deal with macOS deployment target
+        let target = &context.target;
         let use_sysconfig_platform = target.is_windows()
             || (target.is_linux() && platform_tags.iter().any(|tag| !tag.is_portable()))
             || target.is_illumos();
         let platform = if use_sysconfig_platform {
             if let Some(platform) = self.platform.clone() {
                 platform
             } else {
-                target.get_platform_tag(platform_tags, universal2)?
+                context.get_platform_tag(platform_tags)?
             }
         } else {
-            target.get_platform_tag(platform_tags, universal2)?
+            context.get_platform_tag(platform_tags)?
         };
         let tag = if self.implmentation_name.parse::<InterpreterKind>().is_err() {
             // Use generic tags when `sys.implementation.name` != `platform.python_implementation()`, for example Pyston
             // See also https://github.com/pypa/packaging/blob/0031046f7fad649580bc3127d1cef9157da0dd79/packaging/tags.py#L234-L261
             format!(
                 "{interpreter}{major}{minor}-{soabi}-{platform}",
                 interpreter = self.implmentation_name,
@@ -686,73 +693,77 @@
             soabi: None,
         }
     }
 
     /// Find all available python interpreters for a given target
     pub fn find_by_target(
         target: &Target,
-        min_python_minor: Option<usize>,
+        requires_python: Option<&VersionSpecifiers>,
     ) -> Vec<PythonInterpreter> {
         InterpreterConfig::lookup_target(target)
             .into_iter()
-            .filter_map(|config| match min_python_minor {
-                Some(min_python_minor) => {
-                    if config.minor < min_python_minor {
-                        None
-                    } else {
+            .filter_map(|config| match requires_python {
+                Some(requires_python) => {
+                    if requires_python
+                        .contains(&Version::from_release(vec![config.major, config.major]))
+                    {
                         Some(Self::from_config(config))
+                    } else {
+                        None
                     }
                 }
                 None => Some(Self::from_config(config)),
             })
             .collect()
     }
 
     /// Tries to find all installed python versions using the heuristic for the
-    /// given platform
+    /// given platform.
+    ///
+    /// We have two filters: The optional requires-python from the pyproject.toml and minimum python
+    /// minor either from the bindings (i.e. Cargo.toml `abi3-py{major}{minor}`) or the global
+    /// default minimum minor version
     pub fn find_all(
         target: &Target,
         bridge: &BridgeModel,
-        min_python_minor: Option<usize>,
+        requires_python: Option<&VersionSpecifiers>,
     ) -> Result<Vec<PythonInterpreter>> {
-        let min_python_minor = match min_python_minor {
-            Some(requires_python_minor) => match bridge {
-                BridgeModel::Bindings(bridge_name, minor)
-                | BridgeModel::Bin(Some((bridge_name, minor))) => {
-                    // requires-python minor version might be lower than bridge crate required minor version
-                    if requires_python_minor >= *minor {
-                        requires_python_minor
-                    } else {
-                        eprintln!(
-                            "⚠️  Warning: 'requires-python' (3.{}) is lower than the requirement of {} crate (3.{}).",
-                            requires_python_minor, bridge_name, *minor
-                        );
-                        *minor
-                    }
-                }
-                _ => requires_python_minor,
-            },
-            None => match bridge {
-                BridgeModel::Bindings(_, minor) | BridgeModel::Bin(Some((_, minor))) => *minor,
-                _ => MINIMUM_PYTHON_MINOR,
-            },
+        let min_python_minor = match bridge {
+            BridgeModel::Bindings(_, minor) | BridgeModel::Bin(Some((_, minor))) => *minor,
+            _ => MINIMUM_PYTHON_MINOR,
         };
         let executables = if target.is_windows() {
-            find_all_windows(target, min_python_minor)?
+            find_all_windows(target, min_python_minor, requires_python)?
         } else {
             let mut executables: Vec<String> = (min_python_minor..=MAXIMUM_PYTHON_MINOR)
+                .filter(|minor| {
+                    requires_python
+                        .map(|requires_python| {
+                            requires_python.contains(&Version::from_release(vec![3, *minor]))
+                        })
+                        .unwrap_or(true)
+                })
                 .map(|minor| format!("python3.{minor}"))
                 .collect();
             // Also try to find PyPy for cffi and pyo3 bindings
-            if matches!(bridge, BridgeModel::Cffi)
+            if *bridge == BridgeModel::Cffi
                 || bridge.is_bindings("pyo3")
                 || bridge.is_bindings("pyo3-ffi")
             {
                 executables.extend(
-                    (min_python_minor..=MAXIMUM_PYPY_MINOR).map(|minor| format!("pypy3.{minor}")),
+                    (min_python_minor..=MAXIMUM_PYPY_MINOR)
+                        .filter(|minor| {
+                            requires_python
+                                .map(|requires_python| {
+                                    requires_python
+                                        .contains(&Version::from_release(vec![3, *minor]))
+                                })
+                                .unwrap_or(true)
+                        })
+                        .map(|minor| format!("pypy3.{minor}")),
                 );
             }
             executables
         };
         let mut available_versions = Vec::new();
         for executable in executables {
             if let Some(version) = PythonInterpreter::check_executable(executable, target, bridge)?
@@ -867,14 +878,34 @@
     pub fn environment_signature(&self) -> String {
         let pointer_width = self.pointer_width.unwrap_or(64);
         format!(
             "{}-{}.{}-{}bit",
             self.implmentation_name, self.major, self.minor, pointer_width
         )
     }
+
+    /// Returns the site-packages directory inside a venv e.g.
+    /// {venv_base}/lib/python{x}.{y} on unix or {venv_base}/Lib on window
+    pub fn get_venv_site_package(&self, venv_base: impl AsRef<Path>, target: &Target) -> PathBuf {
+        if target.is_unix() {
+            match self.interpreter_kind {
+                InterpreterKind::CPython => {
+                    let python_dir = format!("python{}.{}", self.major, self.minor);
+                    venv_base
+                        .as_ref()
+                        .join("lib")
+                        .join(python_dir)
+                        .join("site-packages")
+                }
+                InterpreterKind::PyPy => venv_base.as_ref().join("site-packages"),
+            }
+        } else {
+            venv_base.as_ref().join("Lib").join("site-packages")
+        }
+    }
 }
 
 impl fmt::Display for PythonInterpreter {
     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
         if self.runnable {
             write!(
                 f,
```

### Comparing `maturin-1.0.0b5/src/python_interpreter/sysconfig-freebsd.json` & `maturin-1.0.0b7/src/python_interpreter/sysconfig-freebsd.json`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/python_interpreter/sysconfig-linux.json` & `maturin-1.0.0b7/src/python_interpreter/sysconfig-linux.json`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/python_interpreter/sysconfig-macos.json` & `maturin-1.0.0b7/src/python_interpreter/sysconfig-macos.json`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/python_interpreter/sysconfig-netbsd.json` & `maturin-1.0.0b7/src/python_interpreter/sysconfig-netbsd.json`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/python_interpreter/sysconfig-openbsd.json` & `maturin-1.0.0b7/src/python_interpreter/sysconfig-openbsd.json`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/python_interpreter/sysconfig-windows.json` & `maturin-1.0.0b7/src/python_interpreter/sysconfig-windows.json`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/source_distribution.rs` & `maturin-1.0.0b7/src/source_distribution.rs`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/templates/.gitignore.j2` & `maturin-1.0.0b7/src/templates/.gitignore.j2`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/templates/Cargo.toml.j2` & `maturin-1.0.0b7/src/templates/Cargo.toml.j2`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/templates/lib.rs.j2` & `maturin-1.0.0b7/src/templates/lib.rs.j2`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/templates/pyproject.toml.j2` & `maturin-1.0.0b7/src/templates/pyproject.toml.j2`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/src/upload.rs` & `maturin-1.0.0b7/src/upload.rs`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/test-dockerfile.sh` & `maturin-1.0.0b7/test-dockerfile.sh`

 * *Files identical despite different names*

### Comparing `maturin-1.0.0b5/PKG-INFO` & `maturin-1.0.0b7/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,31 +1,31 @@
 Metadata-Version: 2.1
 Name: maturin
-Version: 1.0.0b5
+Version: 1.0.0b7
 Classifier: Topic :: Software Development :: Build Tools
 Classifier: Programming Language :: Rust
 Classifier: Programming Language :: Python :: Implementation :: CPython
 Classifier: Programming Language :: Python :: Implementation :: PyPy
-Requires-Dist: tomli>=1.1.0 ; python_version<'3.11'
-Requires-Dist: patchelf; extra == 'patchelf'
-Requires-Dist: ziglang~=0.10.0; extra == 'zig'
-Provides-Extra: patchelf
+Requires-Dist: tomli >= 1.1.0 ; python_version < '3.11'
+Requires-Dist: ziglang ~= 0.10.0 ; extra == 'zig'
+Requires-Dist: patchelf ; extra == 'patchelf'
 Provides-Extra: zig
+Provides-Extra: patchelf
 Summary: Build and publish crates with pyo3, rust-cpython and cffi bindings as well as rust binaries as python packages
 Keywords: python,cffi,packaging,pypi,pyo3
 Home-Page: https://github.com/pyo3/maturin
 Author: konstin <konstin@mailbox.org>, messense <messense@icloud.com>
 Author-email: konstin <konstin@mailbox.org>, messense <messense@icloud.com>
 License: MIT OR Apache-2.0
-Requires-Python: >=3.7
+Requires-Python: >= 3.7
 Description-Content-Type: text/markdown; charset=UTF-8; variant=GFM
 Project-URL: Source Code, https://github.com/PyO3/maturin
-Project-URL: Changelog, https://maturin.rs/changelog.html
-Project-URL: Documentation, https://maturin.rs
 Project-URL: Issues, https://github.com/PyO3/maturin/issues
+Project-URL: Documentation, https://maturin.rs
+Project-URL: Changelog, https://maturin.rs/changelog.html
 
 # Maturin
 
 _formerly pyo3-pack_
 
 [![Actions Status](https://img.shields.io/github/actions/workflow/status/PyO3/maturin/test.yml?branch=main&logo=github&style=flat-square)](https://github.com/PyO3/maturin/actions)
 [![FreeBSD](https://img.shields.io/cirrus/github/PyO3/maturin/main?logo=CircleCI&style=flat-square)](https://cirrus-ci.com/github/PyO3/maturin)
@@ -202,15 +202,15 @@
 The keys are the script names while the values are the path to the function in the format `some.module.path:class.function`, where the `class` part is optional. The function is called with no arguments. Example:
 
 ```toml
 [project.scripts]
 get_42 = "my_project:DummyClass.get_42"
 ```
 
-You can also specify [trove classifiers](https://pypi.org/classifiers/) in your Cargo.toml under `project.classifiers`:
+You can also specify [trove classifiers](https://pypi.org/classifiers/) in your `pyproject.toml` under `project.classifiers`:
 
 ```toml
 [project]
 name = "my-project"
 classifiers = ["Programming Language :: Python"]
 ```
```

