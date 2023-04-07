# Comparing `tmp/vcspull-1.9.0.post1.tar.gz` & `tmp/vcspull-1.9.0.post2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "vcspull-1.9.0.post1.tar", max compression
+gzip compressed data, was "vcspull-1.9.0.post2.tar", max compression
```

## Comparing `vcspull-1.9.0.post1.tar` & `vcspull-1.9.0.post2.tar`

### file list

```diff
@@ -1,28 +1,29 @@
--rw-r--r--   0        0        0     1082 2022-01-29 12:06:44.885111 vcspull-1.9.0.post1/LICENSE
--rw-r--r--   0        0        0     4948 2022-02-27 01:27:40.009120 vcspull-1.9.0.post1/README.md
--rw-r--r--   0        0        0     2374 2022-02-27 01:39:37.249120 vcspull-1.9.0.post1/pyproject.toml
--rw-r--r--   0        0        0       31 2022-01-29 12:06:44.895111 vcspull-1.9.0.post1/tests/__init__.py
--rw-r--r--   0        0        0     1521 2022-02-22 12:01:38.805766 vcspull-1.9.0.post1/tests/conftest.py
--rw-r--r--   0        0        0       28 2022-01-29 12:06:44.895111 vcspull-1.9.0.post1/tests/fixtures/__init__.py
--rw-r--r--   0        0        0      252 2022-01-29 12:06:44.895111 vcspull-1.9.0.post1/tests/fixtures/_util.py
--rw-r--r--   0        0        0     3024 2022-02-22 12:01:38.825766 vcspull-1.9.0.post1/tests/fixtures/example.py
--rw-r--r--   0        0        0      745 2022-01-29 12:06:44.895111 vcspull-1.9.0.post1/tests/fixtures/example1.yaml
--rw-r--r--   0        0        0      714 2022-01-29 12:06:44.895111 vcspull-1.9.0.post1/tests/fixtures/example2.yaml
--rw-r--r--   0        0        0      340 2022-01-29 12:06:44.895111 vcspull-1.9.0.post1/tests/fixtures/expand.json
--rw-r--r--   0        0        0      349 2022-01-29 12:06:44.895111 vcspull-1.9.0.post1/tests/fixtures/expand.yaml
--rw-r--r--   0        0        0      158 2022-01-29 12:06:44.895111 vcspull-1.9.0.post1/tests/fixtures/repoduplicate1.yaml
--rw-r--r--   0        0        0      160 2022-01-29 12:06:44.895111 vcspull-1.9.0.post1/tests/fixtures/repoduplicate2.yaml
--rw-r--r--   0        0        0     1018 2022-01-29 12:06:44.895111 vcspull-1.9.0.post1/tests/helpers.py
--rw-r--r--   0        0        0      333 2022-02-22 12:01:38.795766 vcspull-1.9.0.post1/tests/test_cli.py
--rw-r--r--   0        0        0    10534 2022-02-22 12:01:38.935766 vcspull-1.9.0.post1/tests/test_config.py
--rw-r--r--   0        0        0     9125 2022-02-22 12:01:38.905766 vcspull-1.9.0.post1/tests/test_repo_object.py
--rw-r--r--   0        0        0      476 2022-02-27 01:39:40.179120 vcspull-1.9.0.post1/vcspull/__about__.py
--rw-r--r--   0        0        0      404 2022-01-29 12:06:44.895111 vcspull-1.9.0.post1/vcspull/__init__.py
--rw-r--r--   0        0        0     5127 2022-02-22 12:01:38.865766 vcspull-1.9.0.post1/vcspull/cli.py
--rw-r--r--   0        0        0     3862 2022-02-22 12:01:38.845766 vcspull-1.9.0.post1/vcspull/cli_defaultgroup.py
--rw-r--r--   0        0        0     8988 2022-02-22 12:01:38.885766 vcspull-1.9.0.post1/vcspull/config.py
--rw-r--r--   0        0        0      230 2022-02-22 12:01:38.785766 vcspull-1.9.0.post1/vcspull/exc.py
--rw-r--r--   0        0        0     4024 2022-02-22 12:01:38.835766 vcspull-1.9.0.post1/vcspull/log.py
--rw-r--r--   0        0        0      612 2022-02-22 12:01:38.795766 vcspull-1.9.0.post1/vcspull/util.py
--rw-r--r--   0        0        0     5898 2022-02-27 01:39:41.906309 vcspull-1.9.0.post1/setup.py
--rw-r--r--   0        0        0     6409 2022-02-27 01:39:41.906633 vcspull-1.9.0.post1/PKG-INFO
+-rw-r--r--   0        0        0     1082 2022-01-29 12:06:44.885111 vcspull-1.9.0.post2/LICENSE
+-rw-r--r--   0        0        0     4957 2022-02-27 14:13:02.609120 vcspull-1.9.0.post2/README.md
+-rw-r--r--   0        0        0     2374 2022-02-27 14:13:57.059120 vcspull-1.9.0.post2/pyproject.toml
+-rw-r--r--   0        0        0       31 2022-01-29 12:06:44.895111 vcspull-1.9.0.post2/tests/__init__.py
+-rw-r--r--   0        0        0     1521 2022-02-22 12:01:38.805766 vcspull-1.9.0.post2/tests/conftest.py
+-rw-r--r--   0        0        0       28 2022-01-29 12:06:44.895111 vcspull-1.9.0.post2/tests/fixtures/__init__.py
+-rw-r--r--   0        0        0      252 2022-01-29 12:06:44.895111 vcspull-1.9.0.post2/tests/fixtures/_util.py
+-rw-r--r--   0        0        0     3024 2022-02-22 12:01:38.825766 vcspull-1.9.0.post2/tests/fixtures/example.py
+-rw-r--r--   0        0        0      745 2022-01-29 12:06:44.895111 vcspull-1.9.0.post2/tests/fixtures/example1.yaml
+-rw-r--r--   0        0        0      714 2022-01-29 12:06:44.895111 vcspull-1.9.0.post2/tests/fixtures/example2.yaml
+-rw-r--r--   0        0        0      340 2022-01-29 12:06:44.895111 vcspull-1.9.0.post2/tests/fixtures/expand.json
+-rw-r--r--   0        0        0      349 2022-01-29 12:06:44.895111 vcspull-1.9.0.post2/tests/fixtures/expand.yaml
+-rw-r--r--   0        0        0      158 2022-01-29 12:06:44.895111 vcspull-1.9.0.post2/tests/fixtures/repoduplicate1.yaml
+-rw-r--r--   0        0        0      160 2022-01-29 12:06:44.895111 vcspull-1.9.0.post2/tests/fixtures/repoduplicate2.yaml
+-rw-r--r--   0        0        0     1018 2022-01-29 12:06:44.895111 vcspull-1.9.0.post2/tests/helpers.py
+-rw-r--r--   0        0        0      333 2022-02-22 12:01:38.795766 vcspull-1.9.0.post2/tests/test_cli.py
+-rw-r--r--   0        0        0     1119 2022-02-27 11:57:02.959120 vcspull-1.9.0.post2/tests/test_config.py
+-rw-r--r--   0        0        0    10003 2022-02-27 11:57:02.959120 vcspull-1.9.0.post2/tests/test_config_file.py
+-rw-r--r--   0        0        0     9125 2022-02-22 12:01:38.905766 vcspull-1.9.0.post2/tests/test_repo_object.py
+-rw-r--r--   0        0        0      476 2022-02-27 14:13:50.729120 vcspull-1.9.0.post2/vcspull/__about__.py
+-rw-r--r--   0        0        0      404 2022-01-29 12:06:44.895111 vcspull-1.9.0.post2/vcspull/__init__.py
+-rw-r--r--   0        0        0     5127 2022-02-22 12:01:38.865766 vcspull-1.9.0.post2/vcspull/cli.py
+-rw-r--r--   0        0        0     3862 2022-02-22 12:01:38.845766 vcspull-1.9.0.post2/vcspull/cli_defaultgroup.py
+-rw-r--r--   0        0        0     8988 2022-02-22 12:01:38.885766 vcspull-1.9.0.post2/vcspull/config.py
+-rw-r--r--   0        0        0      230 2022-02-22 12:01:38.785766 vcspull-1.9.0.post2/vcspull/exc.py
+-rw-r--r--   0        0        0     4024 2022-02-22 12:01:38.835766 vcspull-1.9.0.post2/vcspull/log.py
+-rw-r--r--   0        0        0      612 2022-02-22 12:01:38.795766 vcspull-1.9.0.post2/vcspull/util.py
+-rw-r--r--   0        0        0     5907 2022-02-27 14:14:07.424807 vcspull-1.9.0.post2/setup.py
+-rw-r--r--   0        0        0     6418 2022-02-27 14:14:07.425179 vcspull-1.9.0.post2/PKG-INFO
```

### Comparing `vcspull-1.9.0.post1/LICENSE` & `vcspull-1.9.0.post2/LICENSE`

 * *Files identical despite different names*

### Comparing `vcspull-1.9.0.post1/README.md` & `vcspull-1.9.0.post2/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -52,15 +52,15 @@
     repo: "git+https://github.com/liuxinyu95/AlgoXY.git"
     remotes:
       tony: "git+ssh://git@github.com/tony/AlgoXY.git"
 ```
 
 (see the author's
 [.vcspull.yaml](https://github.com/tony/.dot-config/blob/master/.vcspull.yaml),
-more [examples](https://vcspull.git-pull.com/examples.html).)
+more [configuration](https://vcspull.git-pull.com/configuration.html))
 
 next, on other machines, copy your `$HOME/.vcspull.yaml` file or
 `$HOME/.vcspull/` directory them and you can clone your repos
 consistently. vcspull automatically handles building nested directories.
 Updating already cloned/checked out repos is done automatically if they
 already exist.
```

### Comparing `vcspull-1.9.0.post1/pyproject.toml` & `vcspull-1.9.0.post2/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "vcspull"
-version = "1.9.0post1"
+version = "1.9.0post2"
 description = "synchronize your projects via yaml / json files"
 license = "MIT"
 authors = ["Tony Narlock <tony@git-pull.com>"]
 classifiers = [
   "Development Status :: 4 - Beta",
   "License :: OSI Approved :: MIT License",
   "Environment :: Web Environment",
```

### Comparing `vcspull-1.9.0.post1/tests/conftest.py` & `vcspull-1.9.0.post2/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `vcspull-1.9.0.post1/tests/fixtures/example.py` & `vcspull-1.9.0.post2/tests/fixtures/example.py`

 * *Files identical despite different names*

### Comparing `vcspull-1.9.0.post1/tests/fixtures/example1.yaml` & `vcspull-1.9.0.post2/tests/fixtures/example1.yaml`

 * *Files identical despite different names*

### Comparing `vcspull-1.9.0.post1/tests/fixtures/example2.yaml` & `vcspull-1.9.0.post2/tests/fixtures/example2.yaml`

 * *Files identical despite different names*

### Comparing `vcspull-1.9.0.post1/tests/helpers.py` & `vcspull-1.9.0.post2/tests/helpers.py`

 * *Files identical despite different names*

### Comparing `vcspull-1.9.0.post1/tests/test_config.py` & `vcspull-1.9.0.post2/tests/test_config_file.py`

 * *Files 4% similar despite different names*

```diff
@@ -317,25 +317,7 @@
     # Duplicate path + name with different repo URL / remotes raises.
     configs = config.find_config_files(path=str(config_dir), match="repoduplicate[1-2]")
 
     assert str(config1) in configs
     assert str(config2) in configs
     with pytest.raises(Exception):
         config.load_configs(configs)
-
-
-def test_relative_dir(tmpdir):
-    arbitrary_dir = tmpdir.join("moo")
-    arbitrary_dir.mkdir()
-
-    arbitrary_dir.join("rel.yaml").write(
-        """
-./relativedir:
-  docutils: svn+http://svn.code.sf.net/p/docutils/code/trunk
-   """
-    )
-
-    configs = config.find_config_files(path=str(arbitrary_dir))
-    repos = config.load_configs(configs, str(arbitrary_dir))
-
-    assert str(arbitrary_dir.join("relativedir")) == repos[0]["parent_dir"]
-    assert str(arbitrary_dir.join("relativedir", "docutils")) == repos[0]["repo_dir"]
```

### Comparing `vcspull-1.9.0.post1/tests/test_repo_object.py` & `vcspull-1.9.0.post2/tests/test_repo_object.py`

 * *Files identical despite different names*

### Comparing `vcspull-1.9.0.post1/vcspull/cli.py` & `vcspull-1.9.0.post2/vcspull/cli.py`

 * *Files identical despite different names*

### Comparing `vcspull-1.9.0.post1/vcspull/cli_defaultgroup.py` & `vcspull-1.9.0.post2/vcspull/cli_defaultgroup.py`

 * *Files identical despite different names*

### Comparing `vcspull-1.9.0.post1/vcspull/config.py` & `vcspull-1.9.0.post2/vcspull/config.py`

 * *Files identical despite different names*

### Comparing `vcspull-1.9.0.post1/vcspull/log.py` & `vcspull-1.9.0.post2/vcspull/log.py`

 * *Files identical despite different names*

### Comparing `vcspull-1.9.0.post1/vcspull/util.py` & `vcspull-1.9.0.post2/vcspull/util.py`

 * *Files identical despite different names*

### Comparing `vcspull-1.9.0.post1/setup.py` & `vcspull-1.9.0.post2/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -11,17 +11,17 @@
 ['click>=7', 'colorama>=0.3.9', 'kaptan', 'libvcs>=0.11.0,<0.12.0']
 
 entry_points = \
 {'console_scripts': ['vcspull = vcspull:cli.cli']}
 
 setup_kwargs = {
     'name': 'vcspull',
-    'version': '1.9.0.post1',
+    'version': '1.9.0.post2',
     'description': 'synchronize your projects via yaml / json files',
-    'long_description': '`vcspull` - synchronize your repos. built on\n[libvcs](https://github.com/vcs-python/libvcs)\n\n[![Python Package](https://img.shields.io/pypi/v/vcspull.svg)](http://badge.fury.io/py/vcspull)\n[![Docs](https://github.com/vcs-python/vcspull/workflows/Publish%20Docs/badge.svg)](https://github.com/vcs-python/vcspull/actions?query=workflow%3A%22Publish+Docs%22)\n[![Build Status](https://github.com/vcs-python/vcspull/workflows/tests/badge.svg)](https://github.com/vcs-python/vcspull/actions?query=workflow%3A%22tests%22)\n[![Code Coverage](https://codecov.io/gh/vcs-python/vcspull/branch/master/graph/badge.svg)](https://codecov.io/gh/vcs-python/vcspull)\n[![License](https://img.shields.io/github/license/vcs-python/vcspull.svg)](https://github.com/vcs-python/vcspull/blob/master/LICENSE)\n\nManage your commonly used repos from YAML / JSON manifest(s). Compare to\n[myrepos](http://myrepos.branchable.com/).\n\nGreat if you use the same repos at the same locations across multiple\nmachines or want to clone / update a pattern of repos without having to\n`cd` into each one.\n\n- clone /update to the latest repos with `$ vcspull`\n- use filters to specify a location, repo url or pattern in the\n  manifest to clone / update\n- supports svn, git, hg version control systems\n- automatically checkout fresh repositories\n- [Documentation](https://vcspull.git-pull.com/),\n  [Configuration](https://vcspull.git-pull.com/configuration.html),\n  and [Config generators](https://vcspull.git-pull.com/config-generation.html)\n- supports [pip](https://pip.pypa.io/)-style URL\'s\n  ([RFC3986](https://datatracker.ietf.org/doc/html/rfc3986)-based [url\n  scheme](https://pip.pypa.io/en/latest/topics/vcs-support/))\n\n# how to\n\n## install\n\n```sh\n$ pip install --user vcspull\n```\n\n## configure\n\nadd repos you want vcspull to manage to `~/.vcspull.yaml`.\n\n_vcspull does not currently scan for repos on your system, but it may in\nthe future_\n\n```yaml\n~/code/:\n  flask: "git+https://github.com/mitsuhiko/flask.git"\n~/study/c:\n  awesome: "git+git://git.naquadah.org/awesome.git"\n~/study/data-structures-algorithms/c:\n  libds: "git+https://github.com/zhemao/libds.git"\n  algoxy:\n    repo: "git+https://github.com/liuxinyu95/AlgoXY.git"\n    remotes:\n      tony: "git+ssh://git@github.com/tony/AlgoXY.git"\n```\n\n(see the author\'s\n[.vcspull.yaml](https://github.com/tony/.dot-config/blob/master/.vcspull.yaml),\nmore [examples](https://vcspull.git-pull.com/examples.html).)\n\nnext, on other machines, copy your `$HOME/.vcspull.yaml` file or\n`$HOME/.vcspull/` directory them and you can clone your repos\nconsistently. vcspull automatically handles building nested directories.\nUpdating already cloned/checked out repos is done automatically if they\nalready exist.\n\n## clone / update your repos\n\n```bash\n$ vcspull\n```\n\nkeep nested VCS repositories updated too, lets say you have a mercurial\nor svn project with a git dependency:\n\n`external_deps.yaml` in your project root, (can be anything):\n\n```yaml\n./vendor/:\n  sdl2pp: "git+https://github.com/libSDL2pp/libSDL2pp.git"\n```\n\nclone / update repos:\n\n    $ vcspull -c external_deps.yaml\n\nSee the [Quickstart](https://vcspull.git-pull.com/quickstart.html) for\nmore.\n\n## pulling specific repos\n\nhave a lot of repos?\n\nyou can choose to update only select repos through\n[fnmatch](http://pubs.opengroup.org/onlinepubs/009695399/functions/fnmatch.html)\npatterns. remember to add the repos to your `~/.vcspull.{json,yaml}`\nfirst.\n\nThe patterns can be filtered by by directory, repo name or vcs url.\n\n```bash\n# any repo starting with "fla"\n$ vcspull "fla*"\n# any repo with django in the name\n$ vcspull "*django*"\n\n# search by vcs + url\n# since urls are in this format <vcs>+<protocol>://<url>\n$ vcspull "git+*"\n\n# any git repo with python in the vcspull\n$ vcspull "git+*python*\n\n# any git repo with django in the vcs url\n$ vcspull "git+*django*"\n\n# all repositories in your ~/code directory\n$ vcspull "$HOME/code/*"\n```\n\n<img src="https://raw.githubusercontent.com/vcs-python/vcspull/master/docs/_static/vcspull-demo.gif" class="align-center" style="width:45.0%" alt="image" />\n\n# Donations\n\nYour donations fund development of new features, testing and support.\nYour money will go directly to maintenance and development of the\nproject. If you are an individual, feel free to give whatever feels\nright for the value you get out of the project.\n\nSee donation options at <https://git-pull.com/support.html>.\n\n# More information\n\n- Python support: >= 3.7, pypy\n- VCS supported: git(1), svn(1), hg(1)\n- Source: <https://github.com/vcs-python/vcspull>\n- Docs: <https://vcspull.git-pull.com>\n- Changelog: <https://vcspull.git-pull.com/history.html>\n- API: <https://vcspull.git-pull.com/api.html>\n- Issues: <https://github.com/vcs-python/vcspull/issues>\n- Test Coverage: <https://codecov.io/gh/vcs-python/vcspull>\n- pypi: <https://pypi.python.org/pypi/vcspull>\n- Open Hub: <https://www.openhub.net/p/vcspull>\n- License: [MIT](https://opensource.org/licenses/MIT).\n',
+    'long_description': '`vcspull` - synchronize your repos. built on\n[libvcs](https://github.com/vcs-python/libvcs)\n\n[![Python Package](https://img.shields.io/pypi/v/vcspull.svg)](http://badge.fury.io/py/vcspull)\n[![Docs](https://github.com/vcs-python/vcspull/workflows/Publish%20Docs/badge.svg)](https://github.com/vcs-python/vcspull/actions?query=workflow%3A%22Publish+Docs%22)\n[![Build Status](https://github.com/vcs-python/vcspull/workflows/tests/badge.svg)](https://github.com/vcs-python/vcspull/actions?query=workflow%3A%22tests%22)\n[![Code Coverage](https://codecov.io/gh/vcs-python/vcspull/branch/master/graph/badge.svg)](https://codecov.io/gh/vcs-python/vcspull)\n[![License](https://img.shields.io/github/license/vcs-python/vcspull.svg)](https://github.com/vcs-python/vcspull/blob/master/LICENSE)\n\nManage your commonly used repos from YAML / JSON manifest(s). Compare to\n[myrepos](http://myrepos.branchable.com/).\n\nGreat if you use the same repos at the same locations across multiple\nmachines or want to clone / update a pattern of repos without having to\n`cd` into each one.\n\n- clone /update to the latest repos with `$ vcspull`\n- use filters to specify a location, repo url or pattern in the\n  manifest to clone / update\n- supports svn, git, hg version control systems\n- automatically checkout fresh repositories\n- [Documentation](https://vcspull.git-pull.com/),\n  [Configuration](https://vcspull.git-pull.com/configuration.html),\n  and [Config generators](https://vcspull.git-pull.com/config-generation.html)\n- supports [pip](https://pip.pypa.io/)-style URL\'s\n  ([RFC3986](https://datatracker.ietf.org/doc/html/rfc3986)-based [url\n  scheme](https://pip.pypa.io/en/latest/topics/vcs-support/))\n\n# how to\n\n## install\n\n```sh\n$ pip install --user vcspull\n```\n\n## configure\n\nadd repos you want vcspull to manage to `~/.vcspull.yaml`.\n\n_vcspull does not currently scan for repos on your system, but it may in\nthe future_\n\n```yaml\n~/code/:\n  flask: "git+https://github.com/mitsuhiko/flask.git"\n~/study/c:\n  awesome: "git+git://git.naquadah.org/awesome.git"\n~/study/data-structures-algorithms/c:\n  libds: "git+https://github.com/zhemao/libds.git"\n  algoxy:\n    repo: "git+https://github.com/liuxinyu95/AlgoXY.git"\n    remotes:\n      tony: "git+ssh://git@github.com/tony/AlgoXY.git"\n```\n\n(see the author\'s\n[.vcspull.yaml](https://github.com/tony/.dot-config/blob/master/.vcspull.yaml),\nmore [configuration](https://vcspull.git-pull.com/configuration.html))\n\nnext, on other machines, copy your `$HOME/.vcspull.yaml` file or\n`$HOME/.vcspull/` directory them and you can clone your repos\nconsistently. vcspull automatically handles building nested directories.\nUpdating already cloned/checked out repos is done automatically if they\nalready exist.\n\n## clone / update your repos\n\n```bash\n$ vcspull\n```\n\nkeep nested VCS repositories updated too, lets say you have a mercurial\nor svn project with a git dependency:\n\n`external_deps.yaml` in your project root, (can be anything):\n\n```yaml\n./vendor/:\n  sdl2pp: "git+https://github.com/libSDL2pp/libSDL2pp.git"\n```\n\nclone / update repos:\n\n    $ vcspull -c external_deps.yaml\n\nSee the [Quickstart](https://vcspull.git-pull.com/quickstart.html) for\nmore.\n\n## pulling specific repos\n\nhave a lot of repos?\n\nyou can choose to update only select repos through\n[fnmatch](http://pubs.opengroup.org/onlinepubs/009695399/functions/fnmatch.html)\npatterns. remember to add the repos to your `~/.vcspull.{json,yaml}`\nfirst.\n\nThe patterns can be filtered by by directory, repo name or vcs url.\n\n```bash\n# any repo starting with "fla"\n$ vcspull "fla*"\n# any repo with django in the name\n$ vcspull "*django*"\n\n# search by vcs + url\n# since urls are in this format <vcs>+<protocol>://<url>\n$ vcspull "git+*"\n\n# any git repo with python in the vcspull\n$ vcspull "git+*python*\n\n# any git repo with django in the vcs url\n$ vcspull "git+*django*"\n\n# all repositories in your ~/code directory\n$ vcspull "$HOME/code/*"\n```\n\n<img src="https://raw.githubusercontent.com/vcs-python/vcspull/master/docs/_static/vcspull-demo.gif" class="align-center" style="width:45.0%" alt="image" />\n\n# Donations\n\nYour donations fund development of new features, testing and support.\nYour money will go directly to maintenance and development of the\nproject. If you are an individual, feel free to give whatever feels\nright for the value you get out of the project.\n\nSee donation options at <https://git-pull.com/support.html>.\n\n# More information\n\n- Python support: >= 3.7, pypy\n- VCS supported: git(1), svn(1), hg(1)\n- Source: <https://github.com/vcs-python/vcspull>\n- Docs: <https://vcspull.git-pull.com>\n- Changelog: <https://vcspull.git-pull.com/history.html>\n- API: <https://vcspull.git-pull.com/api.html>\n- Issues: <https://github.com/vcs-python/vcspull/issues>\n- Test Coverage: <https://codecov.io/gh/vcs-python/vcspull>\n- pypi: <https://pypi.python.org/pypi/vcspull>\n- Open Hub: <https://www.openhub.net/p/vcspull>\n- License: [MIT](https://opensource.org/licenses/MIT).\n',
     'author': 'Tony Narlock',
     'author_email': 'tony@git-pull.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://vcspull.git-pull.com',
     'packages': packages,
     'package_data': package_data,
```

### Comparing `vcspull-1.9.0.post1/PKG-INFO` & `vcspull-1.9.0.post2/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vcspull
-Version: 1.9.0.post1
+Version: 1.9.0.post2
 Summary: synchronize your projects via yaml / json files
 Home-page: https://vcspull.git-pull.com
 License: MIT
 Keywords: vcspull,git,vcs,json,yaml
 Author: Tony Narlock
 Author-email: tony@git-pull.com
 Requires-Python: >=3.7,<4.0
@@ -91,15 +91,15 @@
     repo: "git+https://github.com/liuxinyu95/AlgoXY.git"
     remotes:
       tony: "git+ssh://git@github.com/tony/AlgoXY.git"
 ```
 
 (see the author's
 [.vcspull.yaml](https://github.com/tony/.dot-config/blob/master/.vcspull.yaml),
-more [examples](https://vcspull.git-pull.com/examples.html).)
+more [configuration](https://vcspull.git-pull.com/configuration.html))
 
 next, on other machines, copy your `$HOME/.vcspull.yaml` file or
 `$HOME/.vcspull/` directory them and you can clone your repos
 consistently. vcspull automatically handles building nested directories.
 Updating already cloned/checked out repos is done automatically if they
 already exist.
```

