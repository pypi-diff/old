# Comparing `tmp/github_rest_api-0.8.0.tar.gz` & `tmp/github_rest_api-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "github_rest_api-0.8.0.tar", max compression
+gzip compressed data, was "github_rest_api-0.9.0.tar", max compression
```

## Comparing `github_rest_api-0.8.0.tar` & `github_rest_api-0.9.0.tar`

### file list

```diff
@@ -1,8 +1,8 @@
--rw-r--r--   0        0        0      173 2023-04-03 22:44:33.688784 github_rest_api-0.8.0/README.md
--rw-r--r--   0        0        0       70 2023-04-03 22:44:33.688784 github_rest_api-0.8.0/github_rest_api/__init__.py
--rw-r--r--   0        0        0       37 2023-04-03 22:44:33.688784 github_rest_api-0.8.0/github_rest_api/actions/__init__.py
--rw-r--r--   0        0        0     6852 2023-04-03 22:44:33.688784 github_rest_api-0.8.0/github_rest_api/actions/cargo.py
--rw-r--r--   0        0        0      988 2023-04-03 22:44:33.688784 github_rest_api-0.8.0/github_rest_api/actions/utils.py
--rw-r--r--   0        0        0     3532 2023-04-03 22:44:33.688784 github_rest_api-0.8.0/github_rest_api/github.py
--rw-r--r--   0        0        0      782 2023-04-03 22:44:33.688784 github_rest_api-0.8.0/pyproject.toml
--rw-r--r--   0        0        0      579 1970-01-01 00:00:00.000000 github_rest_api-0.8.0/PKG-INFO
+-rw-r--r--   0        0        0      173 2023-04-04 01:49:50.464745 github_rest_api-0.9.0/README.md
+-rw-r--r--   0        0        0       70 2023-04-04 01:49:50.464745 github_rest_api-0.9.0/github_rest_api/__init__.py
+-rw-r--r--   0        0        0       37 2023-04-04 01:49:50.464745 github_rest_api-0.9.0/github_rest_api/actions/__init__.py
+-rw-r--r--   0        0        0     6903 2023-04-04 01:49:50.464745 github_rest_api-0.9.0/github_rest_api/actions/cargo.py
+-rw-r--r--   0        0        0     1184 2023-04-04 01:49:50.464745 github_rest_api-0.9.0/github_rest_api/actions/utils.py
+-rw-r--r--   0        0        0     3532 2023-04-04 01:49:50.464745 github_rest_api-0.9.0/github_rest_api/github.py
+-rw-r--r--   0        0        0      782 2023-04-04 01:49:50.464745 github_rest_api-0.9.0/pyproject.toml
+-rw-r--r--   0        0        0      579 1970-01-01 00:00:00.000000 github_rest_api-0.9.0/PKG-INFO
```

### Comparing `github_rest_api-0.8.0/github_rest_api/actions/cargo.py` & `github_rest_api-0.9.0/github_rest_api/actions/cargo.py`

 * *Files 2% similar despite different names*

```diff
@@ -11,21 +11,21 @@
     nums = random.sample(range(10), 10)
     return "_branch_" + "".join(str(num) for num in nums)
 
 
 def _copy_last_dev_bench() -> None:
     branch = _gen_temp_branch()
     create_branch(branch)
-    switch_branch("gh-pages")
+    switch_branch(branch="gh-pages", fetch=True)
     src = Path("dev/criterion")
     if src.is_dir():
         target = Path("target/criterion")
         target.mkdir(parents=True, exist_ok=True)
         shutil.copytree(src, target, dirs_exist_ok=True)
-    switch_branch(branch)
+    switch_branch(branch=branch, fetch=False)
 
 
 def _cargo_criterion() -> None:
     """Run `cargo criterion` to benchmark the specified branch.
 
     :param branch: The branch to benchmark.
     """
@@ -36,15 +36,15 @@
 
 def _copy_bench_results(bench_dir: Path, storage: str) -> None:
     """Copy benchmark results into the right directory.
     :param bench_dir: The root benchmark directory
     (under the gh-pages branch).
     :param pr_merge_name: The corresponding PR merge name.
     """
-    switch_branch("gh-pages")
+    switch_branch("gh-pages", fetch=True)
     src = Path("target/criterion")
     dst = bench_dir / storage / "criterion"
     dst.mkdir(parents=True, exist_ok=True)
     shutil.copytree(src, dst, dirs_exist_ok=True)
 
 
 def _git_push_gh_pages(bench_dir: Path) -> None:
```

### Comparing `github_rest_api-0.8.0/github_rest_api/actions/utils.py` & `github_rest_api-0.9.0/github_rest_api/actions/utils.py`

 * *Files 22% similar despite different names*

```diff
@@ -20,11 +20,17 @@
     """Create a new local branch.
     :param branch: The new local branch to create.
     """
     cmd = f"git checkout -b {branch}"
     sp.run(cmd, shell=True, check=True)
 
 
-def switch_branch(branch: str) -> None:
-    """Switch to another branch."""
-    cmd = f"git fetch origin {branch} && git checkout {branch}"
+def switch_branch(branch: str, fetch: bool) -> None:
+    """Switch to another branch.
+    :param branch: The branch to checkout.
+    :param fetch: If true, fetch the branch from remote first.
+    """
+    if fetch:
+        cmd = f"git fetch origin {branch}"
+        sp.run(cmd, shell=True, check=True)
+    cmd = f"git checkout {branch}"
     sp.run(cmd, shell=True, check=True)
```

### Comparing `github_rest_api-0.8.0/github_rest_api/github.py` & `github_rest_api-0.9.0/github_rest_api/github.py`

 * *Files identical despite different names*

### Comparing `github_rest_api-0.8.0/pyproject.toml` & `github_rest_api-0.9.0/pyproject.toml`

 * *Files 18% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "github_rest_api"
-version = "0.8.0"
+version = "0.9.0"
 description = "Simple wrapper of GitHub REST APIs."
 authors = ["Ben Du <longendu@yahoo.com>"]
 readme = "README.md"
 packages = [{include = "github_rest_api"}]
 
 [tool.poetry.dependencies]
 python = ">=3.10,<4"
```

### Comparing `github_rest_api-0.8.0/PKG-INFO` & `github_rest_api-0.9.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: github-rest-api
-Version: 0.8.0
+Version: 0.9.0
 Summary: Simple wrapper of GitHub REST APIs.
 Author: Ben Du
 Author-email: longendu@yahoo.com
 Requires-Python: >=3.10,<4
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
```

