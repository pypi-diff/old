# Comparing `tmp/mkie-0.1.6.tar.gz` & `tmp/mkie-0.1.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mkie-0.1.6.tar", max compression
+gzip compressed data, was "mkie-0.1.7.tar", max compression
```

## Comparing `mkie-0.1.6.tar` & `mkie-0.1.7.tar`

### file list

```diff
@@ -1,11 +1,10 @@
--rw-r--r--   0        0        0     1086 2022-12-02 14:37:31.276047 mkie-0.1.6/LICENSE
--rw-r--r--   0        0        0      475 2022-12-16 16:30:43.934659 mkie-0.1.6/README.md
--rw-r--r--   0        0        0        0 2022-12-16 16:30:43.936179 mkie-0.1.6/mkie/__init__.py
--rw-r--r--   0        0        0     2856 2023-02-26 12:57:05.417851 mkie-0.1.6/mkie/__main__.py
--rw-r--r--   0        0        0        0 2022-12-02 14:37:31.284770 mkie-0.1.6/mkie/core/__init__.py
--rw-r--r--   0        0        0     2196 2023-02-26 13:12:07.745456 mkie-0.1.6/mkie/core/mkdk.py
--rw-r--r--   0        0        0     8605 2023-02-26 13:12:21.017731 mkie-0.1.6/mkie/core/mkgit.py
--rw-r--r--   0        0        0     1515 2023-02-26 12:54:06.507404 mkie-0.1.6/mkie/core/toolkit.py
--rw-r--r--   0        0        0      635 2023-02-26 13:12:36.061548 mkie-0.1.6/pyproject.toml
--rw-r--r--   0        0        0     1360 1970-01-01 00:00:00.000000 mkie-0.1.6/setup.py
--rw-r--r--   0        0        0     1453 1970-01-01 00:00:00.000000 mkie-0.1.6/PKG-INFO
+-rw-r--r--   0        0        0     1086 2023-03-21 08:09:20.020758 mkie-0.1.7/LICENSE
+-rw-r--r--   0        0        0      475 2023-04-06 13:33:06.487878 mkie-0.1.7/README.md
+-rw-r--r--   0        0        0        0 2023-03-21 08:09:20.021107 mkie-0.1.7/mkie/__init__.py
+-rw-r--r--   0        0        0     3615 2023-04-04 16:06:23.720492 mkie-0.1.7/mkie/__main__.py
+-rw-r--r--   0        0        0        0 2023-03-21 08:09:20.021483 mkie-0.1.7/mkie/core/__init__.py
+-rw-r--r--   0        0        0     6252 2023-04-04 16:05:32.818417 mkie-0.1.7/mkie/core/mkdk.py
+-rw-r--r--   0        0        0    10171 2023-04-04 16:05:56.243288 mkie-0.1.7/mkie/core/mkgit.py
+-rw-r--r--   0        0        0     1515 2023-04-04 16:07:02.896812 mkie-0.1.7/mkie/core/toolkit.py
+-rw-r--r--   0        0        0      635 2023-04-06 13:33:41.593228 mkie-0.1.7/pyproject.toml
+-rw-r--r--   0        0        0     1453 1970-01-01 00:00:00.000000 mkie-0.1.7/PKG-INFO
```

### Comparing `mkie-0.1.6/LICENSE` & `mkie-0.1.7/LICENSE`

 * *Files identical despite different names*

### Comparing `mkie-0.1.6/mkie/__main__.py` & `mkie-0.1.7/mkie/__main__.py`

 * *Files 26% similar despite different names*

```diff
@@ -10,18 +10,17 @@
     |  ┃          ┏┛
     |  ┗┓┓┏━━━━┳┓┏┛
     |   ┃┫┫    ┃┫┫
     |   ┗┻┛    ┗┻┛
     God Bless,Never Bug.
 """
 import click
+import mkie
 from click_help_colors import HelpColorsCommand, HelpColorsGroup
 from importlib_metadata import version
-
-import mkie
 from mkie.core.mkdk import Mkdk
 from mkie.core.mkgit import MkGit
 
 
 class Mkie(click.MultiCommand):
 
     @click.group(
@@ -64,17 +63,18 @@
                   multiple=True)
     @click.argument('branch_name', required=True)
     def s(ignore, branch_name):
         """ Swap current branch to target branch. """
         MkGit.swap(ignore=ignore, branch_name=branch_name)
 
     @cli.command()
-    def gitpull():
+    @click.option('--init')
+    def gitpull(init):
         """ pull latest update from repo """
-        MkGit.pull()
+        MkGit.pull(init)
 
     @cli.command()
     @click.option('-f',
                   '--format',
                   help='pretty print container cols,'
                   'default:".ID.Names.Ports.Image"')
     @click.option('--pattern', help='rg pattern word container name')
@@ -85,20 +85,40 @@
     @cli.command()
     def dbu():
         """ build docker container """
         Mkdk.build()
 
     @cli.command()
     @click.argument('project', required=False)
-    def dup(project):
+    @click.option('--subpath')
+    @click.option('--filepath', help='e.q. docker-compose.yml')
+    def dup(project, subpath, filepath):
         """ start docker container """
-        Mkdk.up(project=project)
+        Mkdk.up(
+            project=project,
+            subpath=subpath,
+            filepath=filepath,
+        )
 
     @cli.command()
     @click.argument('project', required=False)
-    def dd(project):
+    @click.option('--subpath')
+    @click.option('--filepath', help='e.q. docker-compose.yml')
+    def dd(project, subpath, filepath):
         """ start docker container """
-        Mkdk.down(project=project)
+        Mkdk.down(
+            project=project,
+            subpath=subpath,
+            filepath=filepath,
+        )
+
+    @cli.command()
+    @click.argument('project', required=False)
+    @click.option('--command', help='default: bash')
+    @click.option('--list', help='list all containers', is_flag=True)
+    def drun(project, command, list):
+        """ run docker container """
+        Mkdk.run(project=project, command=command, is_list=list)
 
 
 if __name__ == '__main__':
     Mkie.cli()
```

### Comparing `mkie-0.1.6/mkie/core/mkgit.py` & `mkie-0.1.7/mkie/core/mkgit.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,11 @@
 import os
 import re
 import subprocess
+from pathlib import Path
 
 import click
 from colorama import Back, Fore, Style
 
 from .toolkit import Colored
 
 
@@ -82,16 +83,17 @@
         msg = pattern_now.sub(
             rf'{Fore.YELLOW}\1{Fore.RESET}\2{Fore.GREEN}\3{Fore.RESET}', msg)
         return msg
 
     @classmethod
     def fetch(cls, show=True):
         """ sort out current branchs """
-        prefix = Colored.get_color_prefix(color='LIGHTBLUE_EX',
-                                          color_prefix=Fore.WHITE,
+        prefix = Colored.get_color_prefix(color='YELLOW',
+                                          color_prefix=Style.RESET_ALL +
+                                          Fore.BLACK,
                                           prefix_msg='fetch')
         try:
             info = subprocess.getoutput('git fetch --prune')
         except Exception:
             print('No Git detect!')
             return
 
@@ -113,18 +115,18 @@
             print(msg)
 
     @classmethod
     def _checkout(cls, branch):
         colored_repo = Colored.get_color_prefix(color='LIGHTBLACK_EX',
                                                 color_prefix=Fore.WHITE)
         # """ check exist """
-        branchs = subprocess.getoutput(
+        branchs = set(subprocess.getoutput(
             "git for-each-ref "
-            "--sort=-committerdate refs/heads/ "
-            "--format='%(refname:short)'").splitlines()
+            "--sort=-committerdate "
+            "--format='%(refname:short)' | sed 's/^origin\///' ").splitlines())
 
         if branch in branchs:
             # """ checkout branch """
             info = subprocess.getoutput(f'git checkout {branch}')
             extra = ''
             try:
                 if 'Already on' in info:
@@ -142,16 +144,15 @@
 
             except Exception:
                 status = 'Except Error on '
                 color = Fore.RED
                 extra = f'\n{info}'
 
             print(
-                f'{colored_repo}{status}{Colored.draw(color, branch)}{extra}'
-            )
+                f'{colored_repo}{status}{Colored.draw(color, branch)}{extra}')
             return
 
         # """ create new branch """
         draw_branch = Colored.draw(Fore.CYAN, branch)
         msg = Colored.draw(Fore.RED, 'Not Exist')
         print(f'\n< Branch: {draw_branch} > {msg}.')
 
@@ -203,64 +204,92 @@
                     continue
                 try:
                     os.chdir(path)
                 except Exception:
                     continue
                 cls._checkout(branch=branch_name)
 
-    @ classmethod
-    def _init(cls):
-        if not os.path.exists(cls._PATH_MAIN_CONFIG):
-            print('No Git Config Found!')
-            return
-        cls._get_submodules()
-        if not cls._PATH_SUB:
-            return
-
+    @classmethod
+    def _check_submodule_files(cls):
         has_files = None
         for path in cls._PATH_SUB:
             try:
                 os.chdir(path)
                 has_files = False if not subprocess.getoutput('ls') else True
             except Exception:
                 return
-        if has_files:
-            return
+        return has_files
+
+    @classmethod
+    def _init(cls, init=False):
+        if not init:
+            has_git = Path(f'{cls._PATH_MAIN}/.git').exists()
+            has_config = Path(cls._PATH_MAIN_CONFIG).exists()
+
+            if not has_config and not has_git:
+                print('No Git Config Found!')
+                return
+            cls._get_submodules()
+            if not cls._PATH_SUB:
+                return
+
+            # first init check submodule
+            has_files = cls._check_submodule_files()
+            if has_files:
+                return
 
         color_prefix = Colored.get_color_prefix(color='MAGENTA',
                                                 color_prefix=Fore.WHITE,
                                                 prefix_msg='init')
         print(f'{color_prefix}Git Submodeles')
         subprocess.run('git submodule update --init --recursive', shell=True)
-        print(f'{color_prefix}Finished.\n')
+        _ = Colored.draw(color=Fore.MAGENTA, msg='---')
+        print(f'{_} Finished. {_} ')
 
-    @ staticmethod
+    @staticmethod
     def _re_pull_words(replacement, info, color):
         pattern = re.compile(rf'([{replacement}]+)([\n-)])')
         return pattern.sub(rf'{color}\1{Fore.RESET}\2', info)
 
-    @ classmethod
+    @classmethod
     def _git_pull(cls):
         info = subprocess.getoutput('git pull')
-        info = cls._re_pull_words(
-            replacement='-', info=info, color=Fore.RED)
-        info = cls._re_pull_words(
-            replacement='+', info=info, color=Fore.GREEN)
-        print(f'{info}\n')
+        info = cls._re_pull_words(replacement='-', info=info, color=Fore.RED)
+        info = cls._re_pull_words(replacement='+', info=info, color=Fore.GREEN)
+        print(f'{info}')
 
-    @ classmethod
-    def pull(cls):
+    @classmethod
+    def pull(cls, init):
         """ pull all file from Git repo """
-        cls._init()
+        cls._init(init=init)
 
         os.chdir(cls._PATH_MAIN)
         cls.fetch(show=False)
+
+        color_prefix = Style.RESET_ALL + Fore.BLACK
+        bottom_prefix = Fore.WHITE + Style.BRIGHT
+        prefix = Colored.get_color_prefix(color='CYAN',
+                                          color_prefix=color_prefix,
+                                          prefix_msg='Main Module',
+                                          bottom=True,
+                                          bottom_color='LIGHTBLUE_EX',
+                                          bottom_prefix=bottom_prefix,
+                                          bottom_msg=Path.cwd().name)
+        print(prefix)
         cls._git_pull()
 
         if not cls._PATH_SUB:
             return
         for path in cls._PATH_SUB:
             try:
                 os.chdir(path)
             except Exception:
                 continue
+            prefix = Colored.get_color_prefix(color='CYAN',
+                                              color_prefix=color_prefix,
+                                              prefix_msg=' SubModule ',
+                                              bottom=True,
+                                              bottom_color='LIGHTBLUE_EX',
+                                              bottom_prefix=bottom_prefix,
+                                              bottom_msg=Path.cwd().name)
+            print(prefix)
             cls._git_pull()
```

### Comparing `mkie-0.1.6/mkie/core/toolkit.py` & `mkie-0.1.7/mkie/core/toolkit.py`

 * *Files identical despite different names*

### Comparing `mkie-0.1.6/pyproject.toml` & `mkie-0.1.7/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = 'mkie'
-version = '0.1.6'
+version = '0.1.7'
 description = 'A useful tool for control clis in terminal.'
 license = 'MIT'
 authors = ['Michael Chou <snoopy02m@gmail.com>']
 repository = 'https://github.com/cbb23021/mkie'
 readme = 'README.md'
 classifiers = [
   'Operating System :: MacOS',
```

### Comparing `mkie-0.1.6/PKG-INFO` & `mkie-0.1.7/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mkie
-Version: 0.1.6
+Version: 0.1.7
 Summary: A useful tool for control clis in terminal.
 Home-page: https://github.com/cbb23021/mkie
 License: MIT
 Author: Michael Chou
 Author-email: snoopy02m@gmail.com
 Requires-Python: >=3.7,<4.0
 Classifier: License :: OSI Approved :: MIT License
```

