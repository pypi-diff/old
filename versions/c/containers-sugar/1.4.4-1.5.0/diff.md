# Comparing `tmp/containers_sugar-1.4.4.tar.gz` & `tmp/containers_sugar-1.5.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "containers_sugar-1.4.4.tar", max compression
+gzip compressed data, was "containers_sugar-1.5.0.tar", max compression
```

## Comparing `containers_sugar-1.4.4.tar` & `containers_sugar-1.5.0.tar`

### file list

```diff
@@ -1,27 +1,27 @@
--rw-r--r--   0        0        0      897 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/.containers-sugar.yaml
--rw-r--r--   0        0        0       88 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/.github/FUNDING.yml
--rw-r--r--   0        0        0      327 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/.github/ISSUE_TEMPLATE.md
--rw-r--r--   0        0        0     1395 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/.github/PULL_REQUEST_TEMPLATE.md
--rw-r--r--   0        0        0     1760 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/.github/workflows/main.yaml
--rw-r--r--   0        0        0     1889 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/.github/workflows/release.yaml
--rw-r--r--   0        0        0     1799 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/.gitignore
--rw-r--r--   0        0        0     1106 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/.pre-commit-config.yaml
--rw-r--r--   0        0        0     1887 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/.releaserc.json
--rw-r--r--   0        0        0     1514 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/LICENSE
--rw-r--r--   0        0        0     3205 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/Makefile
--rw-r--r--   0        0        0     2832 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/README.md
--rw-r--r--   0        0        0      145 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/conda/dev.yaml
--rw-r--r--   0        0        0      216 2023-04-05 04:30:09.585239 containers_sugar-1.4.4/containers_sugar/__init__.py
--rw-r--r--   0        0        0     2442 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/containers_sugar/__main__.py
--rw-r--r--   0        0        0     8466 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/containers_sugar/sugar.py
--rw-r--r--   0        0        0     5436 2023-04-05 04:30:09.601239 containers_sugar-1.4.4/docs/changelog.md
--rw-r--r--   0        0        0     5038 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/docs/contributing.md
--rw-r--r--   0        0        0      956 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/docs/example.ipynb
--rw-r--r--   0        0        0    72342 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/docs/images/favicon.ico
--rw-r--r--   0        0        0    20402 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/docs/images/logo.png
--rw-r--r--   0        0        0      352 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/docs/index.md
--rw-r--r--   0        0        0     1000 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/docs/installation.md
--rw-r--r--   0        0        0     3908 2023-04-05 04:27:17.887884 containers_sugar-1.4.4/docs/mkdocs.yaml
--rw-r--r--   0        0        0   156378 2023-04-05 04:27:17.891884 containers_sugar-1.4.4/poetry.lock
--rw-r--r--   0        0        0     1572 2023-04-05 04:30:09.589239 containers_sugar-1.4.4/pyproject.toml
--rw-r--r--   0        0        0      717 1970-01-01 00:00:00.000000 containers_sugar-1.4.4/PKG-INFO
+-rw-r--r--   0        0        0      897 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/.containers-sugar.yaml
+-rw-r--r--   0        0        0       88 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/.github/FUNDING.yml
+-rw-r--r--   0        0        0      327 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/.github/ISSUE_TEMPLATE.md
+-rw-r--r--   0        0        0     1395 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/.github/PULL_REQUEST_TEMPLATE.md
+-rw-r--r--   0        0        0     1760 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/.github/workflows/main.yaml
+-rw-r--r--   0        0        0     1889 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/.github/workflows/release.yaml
+-rw-r--r--   0        0        0     1799 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/.gitignore
+-rw-r--r--   0        0        0     1106 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/.pre-commit-config.yaml
+-rw-r--r--   0        0        0     1887 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/.releaserc.json
+-rw-r--r--   0        0        0     1514 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/LICENSE
+-rw-r--r--   0        0        0     3626 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/Makefile
+-rw-r--r--   0        0        0     2801 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/README.md
+-rw-r--r--   0        0        0      145 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/conda/dev.yaml
+-rw-r--r--   0        0        0      216 2023-04-07 02:17:40.693060 containers_sugar-1.5.0/containers_sugar/__init__.py
+-rw-r--r--   0        0        0     4295 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/containers_sugar/__main__.py
+-rw-r--r--   0        0        0     9533 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/containers_sugar/sugar.py
+-rw-r--r--   0        0        0     5804 2023-04-07 02:17:40.705060 containers_sugar-1.5.0/docs/changelog.md
+-rw-r--r--   0        0        0     5038 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/docs/contributing.md
+-rw-r--r--   0        0        0      956 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/docs/example.ipynb
+-rw-r--r--   0        0        0    72342 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/docs/images/favicon.ico
+-rw-r--r--   0        0        0    20402 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/docs/images/logo.png
+-rw-r--r--   0        0        0      352 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/docs/index.md
+-rw-r--r--   0        0        0     1000 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/docs/installation.md
+-rw-r--r--   0        0        0     3908 2023-04-07 02:15:06.465567 containers_sugar-1.5.0/docs/mkdocs.yaml
+-rw-r--r--   0        0        0   156378 2023-04-07 02:15:06.469567 containers_sugar-1.5.0/poetry.lock
+-rw-r--r--   0        0        0     1572 2023-04-07 02:17:40.693060 containers_sugar-1.5.0/pyproject.toml
+-rw-r--r--   0        0        0      717 1970-01-01 00:00:00.000000 containers_sugar-1.5.0/PKG-INFO
```

### Comparing `containers_sugar-1.4.4/.containers-sugar.yaml` & `containers_sugar-1.5.0/.containers-sugar.yaml`

 * *Files identical despite different names*

### Comparing `containers_sugar-1.4.4/.github/PULL_REQUEST_TEMPLATE.md` & `containers_sugar-1.5.0/.github/PULL_REQUEST_TEMPLATE.md`

 * *Files identical despite different names*

### Comparing `containers_sugar-1.4.4/.github/workflows/main.yaml` & `containers_sugar-1.5.0/.github/workflows/main.yaml`

 * *Files identical despite different names*

### Comparing `containers_sugar-1.4.4/.github/workflows/release.yaml` & `containers_sugar-1.5.0/.github/workflows/release.yaml`

 * *Files identical despite different names*

### Comparing `containers_sugar-1.4.4/.gitignore` & `containers_sugar-1.5.0/.gitignore`

 * *Files identical despite different names*

### Comparing `containers_sugar-1.4.4/.pre-commit-config.yaml` & `containers_sugar-1.5.0/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `containers_sugar-1.4.4/.releaserc.json` & `containers_sugar-1.5.0/.releaserc.json`

 * *Files identical despite different names*

### Comparing `containers_sugar-1.4.4/LICENSE` & `containers_sugar-1.5.0/LICENSE`

 * *Files identical despite different names*

### Comparing `containers_sugar-1.4.4/README.md` & `containers_sugar-1.5.0/README.md`

 * *Files 12% similar despite different names*

```diff
@@ -13,37 +13,37 @@
 
 Yes, and just for one project it would be good enough. But, if you maintain
 or collaborate a bunch of projects, it would be like a boiler plate.
 
 Additionally, if you are maintaining some extra scripts in order to improve
 your containers stack, these scripts would be like a boilerplate as well.
 
-So, the idea of this project is to organize your stack of containers, 
+So, the idea of this project is to organize your stack of containers,
 gathering some useful scripts and keeping this information centralized in a
 configuration file. So the command line would be very simple.
 
 
 * Free software: BSD 3 Clause
 * Documentation: https://osl-incubator.github.io/containers-sugar
 
 
 ## Features
 
 
 The commands availables now are:
   `help`, `version`, `build`, `down`, `get-ip`,
-  `logs`, `logs-follow`, `pull`, `restart`,
-  `start`, `stop`, `wait`.
+  `logs`, `pull`, `restart`, `start`, `stop`, `wait`.
 
 > Note: `get-ip` and `wait` are not yet implemented.
 
 
 ## How to use it
 
-First you need to place the config file `.containers-sugar.yaml` in the root of your project. This is an example of a configuration file:
+First you need to place the config file `.containers-sugar.yaml` in the root
+of your project. This is an example of a configuration file:
 
 ```yaml
 version: 1.0.0
 compose-app: docker-compose
 service-groups:
   - name: group1
     project-name: project1  # optional
@@ -77,17 +77,17 @@
 * build the defaults services (service1,service3) for group1:
   `containers-sugar build --group group1`
 
 * build the all services (there is no default service defined) for group2:
   `containers-sugar build --group group2`
 
 * build all services (ignore default) for group1:
-  `containers-sugar build --group group1 --service ""`
+  `containers-sugar build --group group1 --all`
 
 * start the default services for group1:
   `containers-sugar start --group group1`
 
 * restart all services (ignore defaults) for group1:
-  `containers-sugar restart --group group1 --service ""`
+  `containers-sugar restart --group group1 --all`
 
 * restart service1 and service2 for group1:
-  `containers-sugar restart --group group1 --service service1,service2`
+  `containers-sugar restart --group group1 --services service1,service2`
```

### Comparing `containers_sugar-1.4.4/containers_sugar/sugar.py` & `containers_sugar-1.5.0/containers_sugar/sugar.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,11 +1,42 @@
-"""Sugar class for containers"""
+"""
+Sugar class for containers
+
+This is the docker-compose commands signature that should be considered:
+
+docker-compose build [options] [SERVICE...]
+docker-compose bundle [options]
+docker-compose config [options]
+docker-compose create [options] [SERVICE...]
+docker-compose down [options] [--rmi type] [--volumes] [--remove-orphans]
+docker-compose events [options] [SERVICE...]
+docker-compose exec [options] SERVICE COMMAND [ARGS...]
+docker-compose images [options] [SERVICE...]
+docker-compose kill [options] [SERVICE...]
+docker-compose logs [options] [SERVICE...]
+docker-compose pause [options] SERVICE...
+docker-compose port [options] SERVICE PRIVATE_PORT
+docker-compose ps [options] [SERVICE...]
+docker-compose pull [options] [SERVICE...]
+docker-compose push [options] [SERVICE...]
+docker-compose restart [options] [SERVICE...]
+docker-compose rm [options] [-f | -s] [SERVICE...]
+docker-compose run [options] [-p TARGET...] [-v VOLUME...] [-e KEY=VAL...]
+    [-l KEY=VAL...] SERVICE [COMMAND] [ARGS...]
+docker-compose scale [options] [SERVICE=NUM...]
+docker-compose start [options] [SERVICE...]
+docker-compose stop [options] [SERVICE...]
+docker-compose top [options] [SERVICE...]
+docker-compose unpause [options] SERVICE...
+docker-compose up [options] [--scale SERVICE=NUM...] [--no-color]
+    [--quiet-pull] [SERVICE...]
+docker-compose version [options]
+"""
 import argparse
 import os
-import shlex
 import sys
 from pathlib import Path
 
 import sh
 import yaml
 from colorama import Fore
 
@@ -30,81 +61,79 @@
     ACTIONS = [
         'build',
         'config',
         'down',
         'exec',
         'get-ip',
         'logs',
-        'logs-follow',
         'pull',
         'run',
         'restart',
         'start',
         'stop',
         'wait',
     ]
 
     args: argparse.Namespace = argparse.Namespace()
     config_file: str = ''
     config: dict = {}
     # starts with a simple command
     compose_app: sh.Command = sh.echo
     compose_args: list = []
+    options_args: list = []
+    cmd_args: list = []
     service_group: dict = {}
     service_names: list = []
 
-    def __init__(self, args):
+    def __init__(
+        self,
+        args: argparse.Namespace,
+        options_args: list = [],
+        cmd_args: list = [],
+    ):
         self.args = args
+        self.options_args = options_args
+        self.cmd_args = cmd_args
         self.config_file = self.args.config_file
         self._load_config()
         self._verify_args()
         self._load_compose_app()
 
     def load_services(self):
         self._load_compose_args()
         self._verify_config()
         self._load_service_names()
 
     def _call_compose_app(
         self,
         *args,
         services: list = [],
-        cmd: str = '',
     ):
-        # note: this is very fragile, we should use a better way to do that
-        extras = self.args.extras.split(' ') if self.args.extras else []
-
         sh_extras = {
             '_in': sys.stdin,
             '_out': sys.stdout,
             '_err': sys.stderr,
             '_no_err': True,
             '_env': os.environ,
             '_bg': True,
             '_bg_exc': False,
         }
 
-        cmd_list = shlex.split(cmd) if cmd else []
+        positional_parameters = (
+            self.compose_args
+            + list(args)
+            + self.options_args
+            + services
+            + self.cmd_args
+        )
 
         if self.args.verbose:
-            print(
-                '>>>',
-                self.compose_app,
-                *self.compose_args,
-                *args,
-                *extras,
-                *services,
-                *cmd_list,
-            )
+            print('>>>', self.compose_app, *positional_parameters)
             print('-' * 80)
 
-        positional_parameters = (
-            self.compose_args + list(args) + extras + services + cmd_list
-        )
-
         p = self.compose_app(
             *positional_parameters,
             **sh_extras,
         )
 
         try:
             p.wait()
@@ -247,52 +276,44 @@
     def _exec(self):
         if not self.args.service:
             self._print_error(
                 '[EE] `exec` sub-command expected --service parameter.'
             )
             os._exit(1)
 
-        self._call_compose_app(
-            'exec',
-            services=[self.args.service],
-            cmd=self.args.cmd,
-        )
+        self._call_compose_app('exec', services=[self.args.service])
 
     def _get_ip(self):
         self._print_error('[EE] `get-ip` mot implemented yet.')
         os._exit(1)
 
     def _logs(self):
         self._call_compose_app('logs', services=self.service_names)
 
-    def _logs_follow(self):
-        self._call_compose_app('logs', '--follow', services=self.service_names)
-
     def _pull(self):
         self._call_compose_app('pull', services=self.service_names)
 
     def _restart(self):
+        options_args = self.options_args
+        self.options_args = []
         self._stop()
+        self.options_args = options_args
         self._start()
 
     def _run(self):
         if not self.args.service:
             self._print_error(
                 '[EE] `run` sub-command expected --service parameter.'
             )
             os._exit(1)
 
-        self._call_compose_app(
-            'run',
-            services=[self.args.service],
-            cmd=self.args.cmd,
-        )
+        self._call_compose_app('run', services=[self.args.service])
 
     def _start(self):
-        self._call_compose_app('up', '-d', services=self.service_names)
+        self._call_compose_app('up', services=self.service_names)
 
     def _stop(self):
         self._call_compose_app('stop', services=self.service_names)
 
     def _wait(self):
         self._print_error('[EE] `wait` not implemented yet.')
         os._exit(1)
```

### Comparing `containers_sugar-1.4.4/docs/changelog.md` & `containers_sugar-1.5.0/docs/changelog.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,17 @@
 # Release Notes
 ---
 
+# [1.5.0](https://github.com/osl-incubator/containers-sugar/compare/1.4.4...1.5.0) (2023-04-07)
+
+
+### Features
+
+* Improve the usage of parameters --cmd and --options (formerly --extras)  ([#68](https://github.com/osl-incubator/containers-sugar/issues/68)) ([cebdfd8](https://github.com/osl-incubator/containers-sugar/commit/cebdfd808449a14982ca974b24fc36d0fed5eeb7))
+
 ## [1.4.4](https://github.com/osl-incubator/containers-sugar/compare/1.4.3...1.4.4) (2023-04-05)
 
 
 ### Bug Fixes
 
 * Fix the internal usage of the value from --cmd flag ([#67](https://github.com/osl-incubator/containers-sugar/issues/67)) ([ac8a048](https://github.com/osl-incubator/containers-sugar/commit/ac8a0487f41404c52195cfcf74fa18a86f4523f8))
```

### Comparing `containers_sugar-1.4.4/docs/contributing.md` & `containers_sugar-1.5.0/docs/contributing.md`

 * *Files identical despite different names*

### Comparing `containers_sugar-1.4.4/docs/example.ipynb` & `containers_sugar-1.5.0/docs/example.ipynb`

 * *Files identical despite different names*

### Comparing `containers_sugar-1.4.4/docs/images/favicon.ico` & `containers_sugar-1.5.0/docs/images/favicon.ico`

 * *Files identical despite different names*

### Comparing `containers_sugar-1.4.4/docs/images/logo.png` & `containers_sugar-1.5.0/docs/images/logo.png`

 * *Files identical despite different names*

### Comparing `containers_sugar-1.4.4/docs/installation.md` & `containers_sugar-1.5.0/docs/installation.md`

 * *Files identical despite different names*

### Comparing `containers_sugar-1.4.4/docs/mkdocs.yaml` & `containers_sugar-1.5.0/docs/mkdocs.yaml`

 * *Files identical despite different names*

### Comparing `containers_sugar-1.4.4/poetry.lock` & `containers_sugar-1.5.0/poetry.lock`

 * *Files identical despite different names*

### Comparing `containers_sugar-1.4.4/pyproject.toml` & `containers_sugar-1.5.0/pyproject.toml`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "containers-sugar"
-version = "1.4.4"  # semantic-release
+version = "1.5.0"  # semantic-release
 description = "Simplify the usage of containers"
 authors = ["Ivan Ogasawara <ivan.ogasawara@gmail.com>"]
 license = "BSD 3 Clause"
 include = [
   "*.cfg",
   "*.ini",
   "*.js",
```

### Comparing `containers_sugar-1.4.4/PKG-INFO` & `containers_sugar-1.5.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: containers-sugar
-Version: 1.4.4
+Version: 1.5.0
 Summary: Simplify the usage of containers
 License: BSD 3 Clause
 Author: Ivan Ogasawara
 Author-email: ivan.ogasawara@gmail.com
 Requires-Python: >=3.8.1,<4.0.0
 Classifier: License :: Other/Proprietary License
 Classifier: Programming Language :: Python :: 3
```

