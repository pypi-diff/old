# Comparing `tmp/hitchpylibrarytoolkit-0.6.7.tar.gz` & `tmp/hitchpylibrarytoolkit-0.6.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "hitchpylibrarytoolkit-0.6.7.tar", last modified: Fri Mar 31 14:43:49 2023, max compression
+gzip compressed data, was "hitchpylibrarytoolkit-0.6.9.tar", last modified: Fri Apr  7 13:57:58 2023, max compression
```

## Comparing `hitchpylibrarytoolkit-0.6.7.tar` & `hitchpylibrarytoolkit-0.6.9.tar`

### file list

```diff
@@ -1,25 +1,25 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 14:43:49.288051 hitchpylibrarytoolkit-0.6.7/
--rw-r--r--   0 root         (0) root         (0)     1057 2023-03-31 14:40:58.000000 hitchpylibrarytoolkit-0.6.7/LICENSE.txt
--rw-r--r--   0 root         (0) root         (0)       36 2023-03-31 14:40:58.000000 hitchpylibrarytoolkit-0.6.7/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      867 2023-03-31 14:43:49.288051 hitchpylibrarytoolkit-0.6.7/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      280 2023-03-31 14:40:58.000000 hitchpylibrarytoolkit-0.6.7/README.md
--rw-r--r--   0 root         (0) root         (0)        6 2023-03-31 14:40:58.000000 hitchpylibrarytoolkit-0.6.7/VERSION
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 14:43:49.288051 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/
--rw-r--r--   0 root         (0) root         (0)      240 2023-03-31 14:40:58.000000 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1696 2023-03-31 14:40:58.000000 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/deploy.py
--rw-r--r--   0 root         (0) root         (0)     5798 2023-03-31 14:40:58.000000 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/docgen.py
--rw-r--r--   0 root         (0) root         (0)     3399 2023-03-31 14:40:58.000000 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/engine.py
--rw-r--r--   0 root         (0) root         (0)     1721 2023-03-31 14:40:58.000000 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/envirotest.py
--rw-r--r--   0 root         (0) root         (0)       40 2023-03-31 14:40:58.000000 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/exceptions.py
--rw-r--r--   0 root         (0) root         (0)     4735 2023-03-31 14:40:58.000000 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/project_docs.py
--rw-r--r--   0 root         (0) root         (0)    11541 2023-03-31 14:40:58.000000 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/pyenv.py
--rw-r--r--   0 root         (0) root         (0)     8418 2023-03-31 14:40:58.000000 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/toolkit.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 14:43:49.288051 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit.egg-info/
--rw-r--r--   0 root         (0) root         (0)      867 2023-03-31 14:43:49.000000 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      593 2023-03-31 14:43:49.000000 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-03-31 14:43:49.000000 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      185 2023-03-31 14:43:49.000000 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       22 2023-03-31 14:43:49.000000 hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     1152 2023-03-31 14:40:58.000000 hitchpylibrarytoolkit-0.6.7/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2023-03-31 14:43:49.288051 hitchpylibrarytoolkit-0.6.7/setup.cfg
--rw-r--r--   0 root         (0) root         (0)       38 2023-03-31 14:40:58.000000 hitchpylibrarytoolkit-0.6.7/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 13:57:58.727133 hitchpylibrarytoolkit-0.6.9/
+-rw-r--r--   0 root         (0) root         (0)     1057 2023-04-07 13:56:16.000000 hitchpylibrarytoolkit-0.6.9/LICENSE.txt
+-rw-r--r--   0 root         (0) root         (0)       36 2023-04-07 13:56:16.000000 hitchpylibrarytoolkit-0.6.9/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      867 2023-04-07 13:57:58.727133 hitchpylibrarytoolkit-0.6.9/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      280 2023-04-07 13:56:16.000000 hitchpylibrarytoolkit-0.6.9/README.md
+-rw-r--r--   0 root         (0) root         (0)        6 2023-04-07 13:56:16.000000 hitchpylibrarytoolkit-0.6.9/VERSION
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 13:57:58.727133 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/
+-rw-r--r--   0 root         (0) root         (0)      240 2023-04-07 13:56:16.000000 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1878 2023-04-07 13:56:16.000000 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/deploy.py
+-rw-r--r--   0 root         (0) root         (0)     5798 2023-04-07 13:56:16.000000 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/docgen.py
+-rw-r--r--   0 root         (0) root         (0)     3399 2023-04-07 13:56:16.000000 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/engine.py
+-rw-r--r--   0 root         (0) root         (0)     1721 2023-04-07 13:56:16.000000 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/envirotest.py
+-rw-r--r--   0 root         (0) root         (0)       40 2023-04-07 13:56:16.000000 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/exceptions.py
+-rw-r--r--   0 root         (0) root         (0)     4804 2023-04-07 13:56:16.000000 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/project_docs.py
+-rw-r--r--   0 root         (0) root         (0)    12822 2023-04-07 13:56:16.000000 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/pyenv.py
+-rw-r--r--   0 root         (0) root         (0)     8920 2023-04-07 13:56:16.000000 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/toolkit.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 13:57:58.727133 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      867 2023-04-07 13:57:58.000000 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      593 2023-04-07 13:57:58.000000 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 13:57:58.000000 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      188 2023-04-07 13:57:58.000000 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       22 2023-04-07 13:57:58.000000 hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)     1155 2023-04-07 13:56:16.000000 hitchpylibrarytoolkit-0.6.9/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-07 13:57:58.727133 hitchpylibrarytoolkit-0.6.9/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-07 13:56:16.000000 hitchpylibrarytoolkit-0.6.9/setup.py
```

### Comparing `hitchpylibrarytoolkit-0.6.7/LICENSE.txt` & `hitchpylibrarytoolkit-0.6.9/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `hitchpylibrarytoolkit-0.6.7/PKG-INFO` & `hitchpylibrarytoolkit-0.6.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: hitchpylibrarytoolkit
-Version: 0.6.7
+Version: 0.6.9
 Summary: Build, test, documentation, linting, reformatting and specification code for hitch libraries.
 Author-email: Colm O'Connor <colm.oconnor.github@gmail.com>
 License: MIT
 Project-URL: homepage, https://hitchdev.com/
 Keywords: yaml
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/deploy.py` & `hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/deploy.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,47 +1,53 @@
 from commandlib import Command, python
 from path import Path
 import os
 
 
-def deploy(project_name, github_path, temp_path, testpypi=False):
+def deploy(project_name, github_path, temp_path, testpypi=False, dryrun=False, python_cmd=None):
     git = Command("git")
+    
+    if python_cmd is None:
+        python_cmd = python
 
     if temp_path.joinpath(project_name).exists():
         temp_path.joinpath(project_name).rmtree()
 
     Path("/root/.ssh/known_hosts").write_text(
         Command("ssh-keyscan", "github.com").output()
     )
 
     git("clone", "git@github.com:{}.git".format(github_path)).in_dir(temp_path).run()
     project = temp_path / project_name
     version = project.joinpath("VERSION").text().rstrip()
     initpy = project.joinpath(project_name, "__init__.py")
     original_initpy_contents = initpy.bytes().decode("utf8")
     initpy.write_text(original_initpy_contents.replace("DEVELOPMENT_VERSION", version))
-    python("-m", "pip", "wheel", ".", "-w", "dist").in_dir(project).run()
-    python("-m", "build", "--sdist").in_dir(project).run()
+    python_cmd("-m", "pip", "wheel", ".", "-w", "dist").in_dir(project).run()
+    python_cmd("-m", "build", "--sdist").in_dir(project).run()
     initpy.write_text(original_initpy_contents)
 
     # Upload to pypi
     wheel_args = ["-m", "twine", "upload"]
     if testpypi:
         wheel_args += ["--repository", "testpypi"]
     wheel_args += ["dist/{}-{}-py3-none-any.whl".format(project_name, version)]
 
-    python(*wheel_args).in_dir(project).with_env(
-        TWINE_USERNAME="__token__",
-        TWINE_PASSWORD=os.getenv("PYPITOKEN"),
-    ).run()
+    if not dryrun:
+        python_cmd(*wheel_args).in_dir(project).with_env(
+            TWINE_USERNAME="__token__",
+            TWINE_PASSWORD=os.getenv("PYPITOKEN"),
+        ).run()
 
     sdist_args = ["-m", "twine", "upload"]
     if testpypi:
         sdist_args += ["--repository", "testpypi"]
     sdist_args += ["dist/{0}-{1}.tar.gz".format(project_name, version)]
-    python(*sdist_args).in_dir(project).with_env(
-        TWINE_USERNAME="__token__",
-        TWINE_PASSWORD=os.getenv("PYPITOKEN"),
-    ).run()
+    
+    if not dryrun:
+        python_cmd(*sdist_args).in_dir(project).with_env(
+            TWINE_USERNAME="__token__",
+            TWINE_PASSWORD=os.getenv("PYPITOKEN"),
+        ).run()
 
     # Clean up
     temp_path.joinpath(project_name).rmtree()
```

### Comparing `hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/docgen.py` & `hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/docgen.py`

 * *Files identical despite different names*

### Comparing `hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/engine.py` & `hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/engine.py`

 * *Files identical despite different names*

### Comparing `hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/envirotest.py` & `hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/envirotest.py`

 * *Files identical despite different names*

### Comparing `hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/project_docs.py` & `hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/project_docs.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,75 +1,83 @@
 from strictyaml import load
 from commandlib import Command, python_bin
 import hitchpylibrarytoolkit
 
 
 class ProjectDocumentation:
-    def __init__(self, storybook, project_path, publish_path, project_name, github_address, image=""):
+    def __init__(
+        self,
+        storybook,
+        project_path,
+        publish_path,
+        project_name,
+        github_address,
+        image="",
+    ):
         self._storybook = storybook
         self._project_path = project_path
         self._publish_path = publish_path
         self._project_name = project_name
         self._github_address = github_address
         self._project_slug = project_name.lower()
         self._image = image
-    
+
     def _readme_intro(self):
         return (
             "# {project_name}\n"
             "\n"
             "[![Main branch status](https://github.com/{github_address}/actions/workflows/regression.yml/badge.svg)](https://github.com/{github_address}/actions/workflows/regression.yml)"
         ).format(
             project_name=self._project_name,
             github_address=self._github_address,
         )
-    
+
     def _docs_intro(self):
         return (
             "---\n"
             "title: {project_name}\n"
             "---\n"
             "\n{image}\n\n"
-            "<img alt=\"GitHub Repo stars\" src=\"https://img.shields.io/github/stars/{github_address}?style=social\">"
-            "<img alt=\"PyPI - Downloads\" src=\"https://img.shields.io/pypi/dm/{project_slug}\">"
+            '<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/{github_address}?style=social">'
+            '<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/{project_slug}">'
         ).format(
             image=self._image,
             project_name=self._project_name,
             github_address=self._github_address,
             project_slug=self._project_slug,
         )
-    
+
     def _title(self, filepath):
         try:
             assert len(filepath.text().split("---")) >= 3, "{} doesn't have ---".format(
                 filepath
             )
             return load(filepath.text().split("---")[1]).data.get("title", "misc")
         except UnicodeDecodeError:
             return None
         except AssertionError:
             return None
-    
-    
+
     def _contents(self, main_folder, folder, readme):
         markdown = ""
         for filepath in sorted(main_folder.joinpath(folder).listdir()):
             if filepath.name != "index.md":
                 title = self._title(filepath)
 
                 if title is not None:
                     path = filepath.relpath(main_folder).stripext()
 
                     markdown += "- [{}]({})\n".format(
                         title,
-                        "https://hitchdev.com/{}/".format(self._project_slug) + path if readme else path,
+                        "https://hitchdev.com/{}/".format(self._project_slug) + path
+                        if readme
+                        else path,
                     )
         return markdown
-    
-    
+
     def generate(self, readme=False):
         dirtempl = python_bin.dirtempl.in_dir(self._project_path / "docs")
         doc_src = self._project_path / "docs" / "src"
         snippets_path = self._project_path / "docs" / "snippets"
         git = Command("git").in_dir(self._project_path)
 
         dest_path = self._publish_path
@@ -111,15 +119,15 @@
             )
 
         dirtempl("--snippets", snippets_path, doc_src, dest_path).run()
 
         dest_path.joinpath("changelog.md").write_text(
             hitchpylibrarytoolkit.docgen.changelog(self._project_path)
         )
-    
+
     def _generate_storydocs(self, docstory, docpath, storybook):
         storydocs = storybook.with_documentation(
             docstory,
             extra={"in_interpreter": False, "include_title": True},
         )
 
         for story in storydocs.ordered_by_file():
```

### Comparing `hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/pyenv.py` & `hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/pyenv.py`

 * *Files 3% similar despite different names*

```diff
@@ -7,16 +7,19 @@
 from typing import List
 import tomli
 
 
 def package_versions_above(package_name, minimum_version):
     data = requests.get("https://pypi.org/pypi/{}/json".format(package_name)).json()
     versions = list(
-        [release for release in data["releases"].keys()
-         if "rc" not in release and "dev" not in release]
+        [
+            release
+            for release in data["releases"].keys()
+            if "rc" not in release and "dev" not in release
+        ]
     )
     versions.sort(key=StrictVersion)
 
     selected_versions = [
         version
         for version in versions
         if LooseVersion(version) >= LooseVersion(minimum_version)
@@ -111,14 +114,50 @@
                 self._test_package,
             ],
         )
         self.venv.clean()
         self.venv.ensure_built()
 
 
+class ReleaseVirtualenv(hitchbuild.HitchBuild):
+    def __init__(self, pyenv_build):
+        self._pyenv_build = pyenv_build
+    
+    @property
+    def build_path(self):
+        return self._pyenv_build.build_path / "versions" / "relenv"
+
+    @property
+    def fingerprint_path(self):
+        return self.build_path / "fingerprint.txt"
+
+    @property
+    def python_path(self):
+        return self.build_path / "bin" / "python"
+    
+    def build(self):
+        self._pyenv_build.ensure_built()
+
+        if not self.build_path.exists():
+            self.venv = ProjectVirtualenv(
+                "relenv",
+                PyVersion(
+                    self._pyenv_build,
+                    self._pyenv_build.latest_version(),
+                ),
+                packages=[
+                    PythonRequirements(
+                        ["wheel", "build", "twine"]
+                    ),
+                ],
+            )
+            self.venv.ensure_built()
+            self.refingerprint()
+
+
 class DevelopmentVirtualenv(hitchbuild.HitchBuild):
     def __init__(
         self,
         pyenv_build,
         versions_file,
         debug_requirements,
         project_path,
@@ -336,14 +375,22 @@
     def clean(self):
         self.build_path.rmtree(ignore_errors=True)
 
     @property
     def pyenv(self):
         return Command(self.bin.pyenv).with_env(PYENV_ROOT=self.build_path)
 
+    def latest_version(self):
+        return [
+            version.strip()
+            for version in self.pyenv("install", "-l").output().split("\n")
+            if version.strip().startswith("3")
+            and "dev" not in version
+        ][-2]
+
     def available_versions_above_and_including(self, minimum_version):
         return [
             version.strip()
             for version in self.pyenv("install", "-l").output().split("\n")
             if version.strip().startswith("3")
             and "dev" not in version
             and LooseVersion(version.strip()) >= LooseVersion(minimum_version)
```

### Comparing `hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit/toolkit.py` & `hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit/toolkit.py`

 * *Files 4% similar despite different names*

```diff
@@ -82,17 +82,15 @@
         # Upload to pypi
         python(
             "-m",
             "twine",
             "upload",
             "dist/{0}-{1}.tar.gz".format(self._project_name, version),
         ).in_dir(self._path.project).run()
-
-    def deploy(self, version):
-        deploy(self._path.project, self._project_name, version)
+        
 
     def lint(self, exclude=None):
         try:
             if exclude is None:
                 exclude = "__init__.py"
             python("-m", "flake8")(
                 self._path.project.joinpath(self._project_name),
@@ -154,15 +152,14 @@
             self._path.key / "story",
             self._path.gen,
             self._project_name,
             check=True,
         )
 
 
-
 class ProjectToolkitV2(ProjectToolkit):
     def __init__(self, name, slug, github_address, image=""):
         self._name = name
         self._project_name = slug
         self._github_address = github_address
         self.DIR = Directories()
         self._path = self.DIR
@@ -176,42 +173,62 @@
             self.DIR.project,
             self.DIR.project.joinpath("pyproject.toml").text(),
         )
         env.ensure_built()
         return env
 
     def deploy(self, testpypi=False):
+        relenv = pyenv.ReleaseVirtualenv(
+            pyenv.Pyenv(self.DIR.gen / "pyenv")
+        )
+        relenv.ensure_built()
+        
         hitchpylibrarytoolkit.deploy.deploy(
             self._project_name,
             self._github_address,
             self.DIR.gen,
             testpypi=testpypi,
+            dryrun=False,
+            python_cmd = Command(relenv.python_path),
         )
     
+    def package_test(self):
+        relenv = pyenv.ReleaseVirtualenv(
+            pyenv.Pyenv(self.DIR.gen / "pyenv")
+        )
+        relenv.ensure_built()
+
+        hitchpylibrarytoolkit.deploy.deploy(
+            self._project_name,
+            self._github_address,
+            self.DIR.gen,
+            testpypi=True,
+            dryrun=True,
+            python_cmd = Command(relenv.python_path),
+        )
+
     def draft_docs(self, storybook):
         ProjectDocumentation(
             storybook,
             self.DIR.project,
             self.DIR.project / "docs" / "draft",
             self._name,
             self._github_address,
             image=self._image,
         ).generate()
-    
+
     def publish(self, storybook):
         if self.DIR.gen.joinpath(self._project_name).exists():
             self.DIR.gen.joinpath(self._project_name).rmtree()
 
         Path("/root/.ssh/known_hosts").write_text(
             Command("ssh-keyscan", "github.com").output()
         )
         Command(
-            "git", "clone", "git@github.com:{}.git".format(
-                self._github_address
-            )
+            "git", "clone", "git@github.com:{}.git".format(self._github_address)
         ).in_dir(self.DIR.gen).run()
 
         git = Command("git").in_dir(self.DIR.gen / self._project_name)
         git("config", "user.name", "Bot").run()
         git("config", "user.email", "bot@hitchdev.com").run()
         git("rm", "-r", "docs/public").run()
 
@@ -219,15 +236,15 @@
             storybook,
             self.DIR.project,
             self.DIR.gen / self._project_name / "docs" / "public",
             self._name,
             self._github_address,
             image=self._image,
         ).generate()
-        
+
         ProjectDocumentation(
             storybook,
             self.DIR.project,
             self.DIR.gen / self._project_name / "docs" / "draft",
             self._name,
             self._github_address,
             image="",
```

### Comparing `hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit.egg-info/PKG-INFO` & `hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: hitchpylibrarytoolkit
-Version: 0.6.7
+Version: 0.6.9
 Summary: Build, test, documentation, linting, reformatting and specification code for hitch libraries.
 Author-email: Colm O'Connor <colm.oconnor.github@gmail.com>
 License: MIT
 Project-URL: homepage, https://hitchdev.com/
 Keywords: yaml
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `hitchpylibrarytoolkit-0.6.7/hitchpylibrarytoolkit.egg-info/SOURCES.txt` & `hitchpylibrarytoolkit-0.6.9/hitchpylibrarytoolkit.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `hitchpylibrarytoolkit-0.6.7/pyproject.toml` & `hitchpylibrarytoolkit-0.6.9/pyproject.toml`

 * *Files 15% similar despite different names*

```diff
@@ -18,26 +18,26 @@
     "Programming Language :: Python :: 3",
     "License :: OSI Approved :: MIT License",
     "Topic :: Software Development :: Libraries",
     "Natural Language :: English",
 ]
 dependencies = [
     "hitchstory>=0.12.0",
-    "hitchrunpy>=0.6.1",
+    "hitchrunpy>=0.11.3",
+    "icommandlib>=0.6.0",
     "hitchbuild",
-    "dirtemplate>=0.1.4",
+    "dirtempl>=0.1.3",
     "templex>=0.2.0",
     "twine>=0.11.0",
     "flake8>=3.5.0",
     "pip-tools>=6.12.3",
     "gitpython",
     "black",
     "ipython",
     "q>=2.6",
-    "build==0.10.0",
     "wheel",
     "click",
 ]
 dynamic = ["version", "readme"]
 
 [project.urls]
 homepage = "https://hitchdev.com/"
```

