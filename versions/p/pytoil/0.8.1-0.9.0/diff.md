# Comparing `tmp/pytoil-0.8.1.tar.gz` & `tmp/pytoil-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pytoil-0.8.1.tar", max compression
+gzip compressed data, was "pytoil-0.9.0.tar", max compression
```

## Comparing `pytoil-0.8.1.tar` & `pytoil-0.9.0.tar`

### file list

```diff
@@ -1,45 +1,45 @@
--rw-r--r--   0        0        0    11324 2021-07-18 11:14:56.677615 pytoil-0.8.1/LICENSE
--rw-r--r--   0        0        0     3394 2021-07-18 11:14:56.677615 pytoil-0.8.1/README.md
--rw-r--r--   0        0        0     2715 2021-07-18 11:14:56.685615 pytoil-0.8.1/pyproject.toml
--rw-r--r--   0        0        0       81 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/__init__.py
--rw-r--r--   0        0        0      140 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/__main__.py
--rw-r--r--   0        0        0      154 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/api/__init__.py
--rw-r--r--   0        0        0     4992 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/api/api.py
--rw-r--r--   0        0        0       48 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/cli/__init__.py
--rw-r--r--   0        0        0     9458 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/cli/checkout.py
--rw-r--r--   0        0        0     4668 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/cli/config.py
--rw-r--r--   0        0        0      464 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/cli/docs.py
--rw-r--r--   0        0        0     1360 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/cli/gh.py
--rw-r--r--   0        0        0     1759 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/cli/info.py
--rw-r--r--   0        0        0    10049 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/cli/new.py
--rw-r--r--   0        0        0     4823 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/cli/pull.py
--rw-r--r--   0        0        0     3317 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/cli/remove.py
--rw-r--r--   0        0        0     1536 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/cli/root.py
--rw-r--r--   0        0        0     6640 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/cli/show.py
--rw-r--r--   0        0        0     1786 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/cli/utils.py
--rw-r--r--   0        0        0     1858 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/cli/version.py
--rw-r--r--   0        0        0      120 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/config/__init__.py
--rw-r--r--   0        0        0     5056 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/config/config.py
--rw-r--r--   0        0        0     1945 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/config/defaults.py
--rw-r--r--   0        0        0      626 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/environments/__init__.py
--rw-r--r--   0        0        0     2257 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/environments/abstract.py
--rw-r--r--   0        0        0    10206 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/environments/conda.py
--rw-r--r--   0        0        0     2067 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/environments/flit.py
--rw-r--r--   0        0        0     3692 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/environments/poetry.py
--rw-r--r--   0        0        0     2021 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/environments/reqs.py
--rw-r--r--   0        0        0     5408 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/environments/virtualenv.py
--rw-r--r--   0        0        0     4127 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/exceptions.py
--rw-r--r--   0        0        0       57 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/git/__init__.py
--rw-r--r--   0        0        0     4018 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/git/git.py
--rw-r--r--   0        0        0      115 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/py.typed
--rw-r--r--   0        0        0       61 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/repo/__init__.py
--rw-r--r--   0        0        0     8482 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/repo/repo.py
--rw-r--r--   0        0        0      380 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/starters/__init__.py
--rw-r--r--   0        0        0     1949 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/starters/base.py
--rw-r--r--   0        0        0     2575 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/starters/go.py
--rw-r--r--   0        0        0     2180 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/starters/python.py
--rw-r--r--   0        0        0     2251 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/starters/rust.py
--rw-r--r--   0        0        0      127 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/vscode/__init__.py
--rw-r--r--   0        0        0     3746 2021-07-18 11:14:56.685615 pytoil-0.8.1/pytoil/vscode/vscode.py
--rw-r--r--   0        0        0     4580 2021-07-18 11:15:06.220261 pytoil-0.8.1/setup.py
--rw-r--r--   0        0        0     4860 2021-07-18 11:15:06.220737 pytoil-0.8.1/PKG-INFO
+-rw-r--r--   0        0        0    11324 2021-07-21 16:57:33.977518 pytoil-0.9.0/LICENSE
+-rw-r--r--   0        0        0     3394 2021-07-21 16:57:33.977518 pytoil-0.9.0/README.md
+-rw-r--r--   0        0        0     2716 2021-07-21 16:57:33.981518 pytoil-0.9.0/pyproject.toml
+-rw-r--r--   0        0        0       81 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/__init__.py
+-rw-r--r--   0        0        0      140 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/__main__.py
+-rw-r--r--   0        0        0      154 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/api/__init__.py
+-rw-r--r--   0        0        0     4992 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/api/api.py
+-rw-r--r--   0        0        0       48 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/cli/__init__.py
+-rw-r--r--   0        0        0     9516 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/cli/checkout.py
+-rw-r--r--   0        0        0     4668 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/cli/config.py
+-rw-r--r--   0        0        0      464 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/cli/docs.py
+-rw-r--r--   0        0        0     1360 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/cli/gh.py
+-rw-r--r--   0        0        0     1759 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/cli/info.py
+-rw-r--r--   0        0        0    10049 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/cli/new.py
+-rw-r--r--   0        0        0     7396 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/cli/pull.py
+-rw-r--r--   0        0        0     3317 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/cli/remove.py
+-rw-r--r--   0        0        0     1536 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/cli/root.py
+-rw-r--r--   0        0        0     6640 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/cli/show.py
+-rw-r--r--   0        0        0     1786 2021-07-21 16:57:33.981518 pytoil-0.9.0/pytoil/cli/utils.py
+-rw-r--r--   0        0        0     1858 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/cli/version.py
+-rw-r--r--   0        0        0      120 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/config/__init__.py
+-rw-r--r--   0        0        0     5056 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/config/config.py
+-rw-r--r--   0        0        0     1945 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/config/defaults.py
+-rw-r--r--   0        0        0      626 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/environments/__init__.py
+-rw-r--r--   0        0        0     2257 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/environments/abstract.py
+-rw-r--r--   0        0        0    10206 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/environments/conda.py
+-rw-r--r--   0        0        0     2067 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/environments/flit.py
+-rw-r--r--   0        0        0     3692 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/environments/poetry.py
+-rw-r--r--   0        0        0     2021 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/environments/reqs.py
+-rw-r--r--   0        0        0     5408 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/environments/virtualenv.py
+-rw-r--r--   0        0        0     4127 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/exceptions.py
+-rw-r--r--   0        0        0       57 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/git/__init__.py
+-rw-r--r--   0        0        0     4812 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/git/git.py
+-rw-r--r--   0        0        0      115 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/py.typed
+-rw-r--r--   0        0        0       61 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/repo/__init__.py
+-rw-r--r--   0        0        0     8482 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/repo/repo.py
+-rw-r--r--   0        0        0      380 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/starters/__init__.py
+-rw-r--r--   0        0        0     1949 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/starters/base.py
+-rw-r--r--   0        0        0     2575 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/starters/go.py
+-rw-r--r--   0        0        0     2180 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/starters/python.py
+-rw-r--r--   0        0        0     2251 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/starters/rust.py
+-rw-r--r--   0        0        0      127 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/vscode/__init__.py
+-rw-r--r--   0        0        0     3746 2021-07-21 16:57:33.985518 pytoil-0.9.0/pytoil/vscode/vscode.py
+-rw-r--r--   0        0        0     4580 2021-07-21 16:57:44.479236 pytoil-0.9.0/setup.py
+-rw-r--r--   0        0        0     4860 2021-07-21 16:57:44.479651 pytoil-0.9.0/PKG-INFO
```

### Comparing `pytoil-0.8.1/LICENSE` & `pytoil-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/README.md` & `pytoil-0.9.0/README.md`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pyproject.toml` & `pytoil-0.9.0/pyproject.toml`

 * *Files 5% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
 
 [tool.poetry]
 name = "pytoil"
-version = "0.8.1"
+version = "0.9.0"
 description = "CLI to automate the development workflow."
 authors = ["Tom Fleet <tomfleet2018@gmail.com>"]
 license = "Apache Software License 2.0"
 homepage = "https://github.com/FollowTheProcess/pytoil"
 readme = "README.md"
 repository = "https://github.com/FollowTheProcess/pytoil"
 documentation = "https://FollowTheProcess.github.io/pytoil/"
@@ -60,16 +60,16 @@
 nox = ">=2021.6.6"
 black = ">=21.5b2"
 pytest-cov = "^2.12.1"
 coverage-badge = "^1.0.1"
 coverage = "^5.3.0"
 toml = "^0.10.2"
 mypy = ">=0.902"
-mkdocs = "^1.2.0"
-mkdocs-material = "^7.1.7"
+mkdocs = "^1.2.2"
+mkdocs-material = "^7.1.11"
 mkdocstrings = "^0.15.1"
 markdown-include = "^0.6.0"
 livereload = "^2.6.3"
 pytest-mock = "^3.6.1"
 pytest-httpx = "^0.12.0"
 types-PyYAML = "^5.4.3"
 types-toml = "^0.1.3"
```

### Comparing `pytoil-0.8.1/pytoil/api/api.py` & `pytoil-0.9.0/pytoil/api/api.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/cli/checkout.py` & `pytoil-0.9.0/pytoil/cli/checkout.py`

 * *Files 1% similar despite different names*

```diff
@@ -124,15 +124,17 @@
         if repo.exists_local():
             # No environment or git stuff here, chances are if it exists locally
             # user has already done all this stuff
             checkout_local(repo=repo, code=code, config=config)
 
         elif repo.exists_remote(api=api):
             msg.info(f"{repo.name!r} found on GitHub. Cloning...", spaced=True)
-            git.clone(url=repo.clone_url, check=True, cwd=config.projects_dir)
+            git.clone(
+                url=repo.clone_url, check=True, cwd=config.projects_dir, silent=False
+            )
 
             env = repo.dispatch_env()
 
             if venv:
                 handle_venv_creation(env=env, config=config, code=code)
 
             if config.vscode:
@@ -207,15 +209,15 @@
             text="Forking happens asynchronously so this is normal. "
             "Give it a few more seconds and try checking it out again.",
             exits=1,
         )
 
     # If we get here, the fork was a success
     msg.info(f"Cloning your fork: {config.username}/{name}.", spaced=True)
-    git.clone(url=fork.clone_url, cwd=config.projects_dir)
+    git.clone(url=fork.clone_url, cwd=config.projects_dir, silent=False)
 
     # Set upstream
     msg.info("Setting 'upstream' to original repo.", spaced=True)
     git.set_upstream(owner=owner, repo=name, path=fork.local_path)
 
     env = fork.dispatch_env()
```

### Comparing `pytoil-0.8.1/pytoil/cli/config.py` & `pytoil-0.9.0/pytoil/cli/config.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/cli/gh.py` & `pytoil-0.9.0/pytoil/cli/gh.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/cli/info.py` & `pytoil-0.9.0/pytoil/cli/info.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/cli/new.py` & `pytoil-0.9.0/pytoil/cli/new.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/cli/remove.py` & `pytoil-0.9.0/pytoil/cli/remove.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/cli/root.py` & `pytoil-0.9.0/pytoil/cli/root.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/cli/show.py` & `pytoil-0.9.0/pytoil/cli/show.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/cli/utils.py` & `pytoil-0.9.0/pytoil/cli/utils.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/cli/version.py` & `pytoil-0.9.0/pytoil/cli/version.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/config/config.py` & `pytoil-0.9.0/pytoil/config/config.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/config/defaults.py` & `pytoil-0.9.0/pytoil/config/defaults.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/environments/__init__.py` & `pytoil-0.9.0/pytoil/environments/__init__.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/environments/abstract.py` & `pytoil-0.9.0/pytoil/environments/abstract.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/environments/conda.py` & `pytoil-0.9.0/pytoil/environments/conda.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/environments/flit.py` & `pytoil-0.9.0/pytoil/environments/flit.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/environments/poetry.py` & `pytoil-0.9.0/pytoil/environments/poetry.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/environments/reqs.py` & `pytoil-0.9.0/pytoil/environments/reqs.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/environments/virtualenv.py` & `pytoil-0.9.0/pytoil/environments/virtualenv.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/exceptions.py` & `pytoil-0.9.0/pytoil/exceptions.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/git/git.py` & `pytoil-0.9.0/pytoil/git/git.py`

 * *Files 16% similar despite different names*

```diff
@@ -41,15 +41,19 @@
         """
         if not self.git:
             raise GitNotInstalledError(
                 "'git' executable not found on $PATH. Is git installed?"
             )
 
     def run(
-        self, *args: str, check: bool = True, cwd: Path = defaults.PROJECTS_DIR
+        self,
+        *args: str,
+        check: bool = True,
+        cwd: Path = defaults.PROJECTS_DIR,
+        silent: bool = False,
     ) -> None:
         """
         Generic method to run `git` in a subprocess.
 
         Pass any args to git via *args.
 
         e.g. 'run("clone", "https://github.com/me/repo.git")'
@@ -57,65 +61,85 @@
         Args:
             check (bool, optional): Will raise a CalledProcessError if
                 something goes wrong. Defaults to True.
 
             cwd (Path, optional): Working directory of the subprocess.
                 Defaults to defaults.PROJECTS_DIR.
 
+            silent (bool): Whether to suppress showing the clone output.
+                Defaults to False.
+
         Raises:
             subprocess.CalledProcessError: If the subprocess command fails.
         """
 
         self.raise_for_git()
 
         try:
-            subprocess.run([f"{self.git}", *args], check=check, cwd=cwd)
+            subprocess.run(
+                [f"{self.git}", *args], check=check, cwd=cwd, capture_output=silent
+            )
         except subprocess.CalledProcessError:
             raise
 
     def clone(
-        self, url: str, check: bool = True, cwd: Path = defaults.PROJECTS_DIR
+        self,
+        url: str,
+        check: bool = True,
+        cwd: Path = defaults.PROJECTS_DIR,
+        silent: bool = True,
     ) -> None:
         """
         Convenience wrapper around `self.run` to clone a repo.
 
         Args:
             url (str): The clone url of the repo.
 
             check (bool, optional): Raise CalledProcessError on failure.
                 Defaults to True.
 
             cwd (Path, optional): Working directory of the subprocess.
                 Defaults to defaults.PROJECTS_DIR.
 
+            silent (bool): Whether to suppress showing the clone output.
+                Defaults to True.
+
         Raises:
             subprocess.CalledProcessError: If the subprocess command fails.
         """
 
-        self.run("clone", url, check=check, cwd=cwd)
+        self.run("clone", url, check=check, cwd=cwd, silent=silent)
 
-    def init(self, path: Path, check: bool = True) -> None:
+    def init(self, path: Path, check: bool = True, silent: bool = False) -> None:
         """
         Convenience wrapper around `self.run` to initialise a repo.
 
         Args:
             path (Path): Root of the project to initialise
                 the repo in.
 
             check (bool, optional): Raise CalledProcessError on failure.
                 Defaults to True.
 
+            silent (bool): Whether to suppress showing the clone output.
+                Defaults to False.
+
         Raises:
             subprocess.CalledProcessError: If the subprocess command fails.
         """
 
-        self.run("init", check=check, cwd=path)
+        self.run("init", check=check, cwd=path, silent=silent)
 
     def set_upstream(
-        self, owner: str, repo: str, path: Path, check: bool = True
+        self,
+        owner: str,
+        repo: str,
+        path: Path,
+        check: bool = True,
+        silent: bool = False,
     ) -> None:
         """
         Sets the upstream repo for a local repo, e.g. on a cloned fork.
 
         Note difference between origin and upstream, origin of a cloned fork
         would be user/forked_repo where as upstream would be
         original_user/forked_repo.
@@ -123,13 +147,21 @@
         Args:
             owner (str): Owner of the upstream repo.
             repo (str): Name of the upstream repo.
             path (Path): Root of the project where the local git
                 repo is.
             check (bool, optional): Raise CalledProcessError on failure.
                 Defaults to True.
+            silent (bool): Whether to suppress showing the clone output.
+            Defaults to True.
         """
         base_url = "https://github.com"
         constructed_upstream = f"{base_url}/{owner}/{repo}.git"
         self.run(
-            "remote", "add", "upstream", constructed_upstream, check=check, cwd=path
+            "remote",
+            "add",
+            "upstream",
+            constructed_upstream,
+            check=check,
+            cwd=path,
+            silent=silent,
         )
```

### Comparing `pytoil-0.8.1/pytoil/repo/repo.py` & `pytoil-0.9.0/pytoil/repo/repo.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/starters/base.py` & `pytoil-0.9.0/pytoil/starters/base.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/starters/go.py` & `pytoil-0.9.0/pytoil/starters/go.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/starters/python.py` & `pytoil-0.9.0/pytoil/starters/python.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/starters/rust.py` & `pytoil-0.9.0/pytoil/starters/rust.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/pytoil/vscode/vscode.py` & `pytoil-0.9.0/pytoil/vscode/vscode.py`

 * *Files identical despite different names*

### Comparing `pytoil-0.8.1/setup.py` & `pytoil-0.9.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -25,15 +25,15 @@
  'wasabi>=0.8.2,<0.9.0']
 
 entry_points = \
 {'console_scripts': ['pytoil = pytoil.cli.root:app']}
 
 setup_kwargs = {
     'name': 'pytoil',
-    'version': '0.8.1',
+    'version': '0.9.0',
     'description': 'CLI to automate the development workflow.',
     'long_description': "![logo](./docs/img/logo.png)\n\n[![License](https://img.shields.io/github/license/FollowTheProcess/pytoil)](https://github.com/FollowTheProcess/pytoil)\n[![PyPI](https://img.shields.io/pypi/v/pytoil.svg?logo=python)](https://pypi.python.org/pypi/pytoil)\n[![GitHub](https://img.shields.io/github/v/release/FollowTheProcess/pytoil?logo=github&sort=semver)](https://github.com/FollowTheProcess/pytoil)\n[![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/FollowTheProcess/pytoil)\n[![CI](https://github.com/FollowTheProcess/pytoil/workflows/CI/badge.svg)](https://github.com/FollowTheProcess/pytoil/actions?query=workflow%3ACI)\n[![Coverage](docs/img/coverage.svg)](https://github.com/FollowTheProcess/pytoil)\n\n*pytoil is a small, helpful CLI to help developers manage their local and remote projects with ease!*\n\n* **Source Code**: [https://github.com/FollowTheProcess/pytoil](https://github.com/FollowTheProcess/pytoil)\n\n* **Documentation**: [https://FollowTheProcess.github.io/pytoil/](https://FollowTheProcess.github.io/pytoil/)\n\n:warning: pytoil is still in Alpha and as such, the API may change without deprecation notices.\n\n## What is it?\n\n`pytoil` is a handy tool that helps you stay on top of all your projects, remote or local. It's primarily aimed at python developers but you could easily use it to manage any project!\n\npytoil is:\n\n* Easy to use :white_check_mark:\n* Easy to configure :white_check_mark:\n* Safe (it won't edit your repos at all) :white_check_mark:\n* Useful! (I hope :smiley:)\n\nSay goodbye to janky bash scripts :wave:\n\n## Installation\n\nAs pytoil is a CLI, I recommend [pipx]\n\n```shell\npipx install pytoil\n```\n\nOr just pip (but must be globally available)\n\n```shell\npip install pytoil\n```\n\n## Quickstart\n\n`pytoil` is super easy to get started with.\n\nAfter installation just run\n\n```shell\n$ pytoil config\n\nNo config file yet!\nMaking you a default one...\n```\n\nThis will create a default config file which can be found at `~/.pytoil.yml`. See the [docs] for what information you need to put in here.\n\nDon't worry though, there's only a few options to configure! :sleeping:\n\nAfter that you're good to go! You can do things like:\n\n#### See your local and remote projects\n\n```shell\npytoil show all\n```\n\n#### See which ones you have on GitHub, but not on your computer\n\n```shell\npytoil show diff\n```\n\n#### Easily grab a project, regardless of where it is\n\n```shell\npytoil checkout my_project\n```\n\n#### Create a new project and virtual environment in one go\n\n```shell\npytoil new my_project --venv venv\n\n```\n\n#### And even do this from a [cookiecutter] template\n\n```shell\npytoil new my_project --venv venv --cookie https://github.com/some/cookie.git\n```\n\nCheck out the [docs] for more :boom:\n\n### Credits\n\nThis package was created with [cookiecutter] and the [FollowTheProcess/poetry_pypackage] project template.\n\n`pytoil` has been built on top of these fantastic projects:\n\n* [Typer]\n* [cookiecutter]\n* [wasabi]\n* [httpx]\n* [pydantic]\n\n[pipx]: https://pipxproject.github.io/pipx/\n[cookiecutter]: https://cookiecutter.readthedocs.io/en/1.7.2/\n[docs]: https://FollowTheProcess.github.io/pytoil/\n[FollowTheProcess/poetry_pypackage]: https://github.com/FollowTheProcess/poetry_pypackage\n[Typer]: https://typer.tiangolo.com\n[wasabi]: https://github.com/ines/wasabi\n[httpx]: https://www.python-httpx.org\n[pydantic]: https://pydantic-docs.helpmanual.io\n",
     'author': 'Tom Fleet',
     'author_email': 'tomfleet2018@gmail.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://github.com/FollowTheProcess/pytoil',
```

### Comparing `pytoil-0.8.1/PKG-INFO` & `pytoil-0.9.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pytoil
-Version: 0.8.1
+Version: 0.9.0
 Summary: CLI to automate the development workflow.
 Home-page: https://github.com/FollowTheProcess/pytoil
 License: Apache Software License 2.0
 Keywords: cli,python,developer-tools,automation
 Author: Tom Fleet
 Author-email: tomfleet2018@gmail.com
 Requires-Python: >=3.8,<4.0
```

