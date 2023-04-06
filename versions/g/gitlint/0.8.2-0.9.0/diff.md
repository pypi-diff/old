# Comparing `tmp/gitlint-0.8.2.tar.gz` & `tmp/gitlint-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/gitlint-0.8.2.tar", last modified: Tue Apr 25 11:26:40 2017, max compression
+gzip compressed data, was "dist/gitlint-0.9.0.tar", last modified: Sun Dec  3 17:48:58 2017, max compression
```

## Comparing `gitlint-0.8.2.tar` & `gitlint-0.9.0.tar`

### file list

```diff
@@ -1,29 +1,29 @@
-drwxr-xr-x   0 jroovers   (501) staff       (20)        0 2017-04-25 11:26:40.000000 gitlint-0.8.2/
-drwxr-xr-x   0 jroovers   (501) staff       (20)        0 2017-04-25 11:26:40.000000 gitlint-0.8.2/gitlint/
--rw-r--r--   0 jroovers   (501) staff       (20)       22 2017-04-25 11:03:27.000000 gitlint-0.8.2/gitlint/__init__.py
--rw-r--r--   0 jroovers   (501) staff       (20)    10009 2017-04-25 10:17:33.000000 gitlint-0.8.2/gitlint/cli.py
--rw-r--r--   0 jroovers   (501) staff       (20)    14017 2017-04-25 09:04:57.000000 gitlint-0.8.2/gitlint/config.py
--rw-r--r--   0 jroovers   (501) staff       (20)     2062 2017-01-04 11:06:24.000000 gitlint-0.8.2/gitlint/display.py
-drwxr-xr-x   0 jroovers   (501) staff       (20)        0 2017-04-25 11:26:40.000000 gitlint-0.8.2/gitlint/files/
--rw-r--r--   0 jroovers   (501) staff       (20)     2425 2016-12-01 20:37:44.000000 gitlint-0.8.2/gitlint/files/commit-msg
--rw-r--r--   0 jroovers   (501) staff       (20)     1762 2016-12-02 14:21:52.000000 gitlint-0.8.2/gitlint/files/gitlint
--rw-r--r--   0 jroovers   (501) staff       (20)     7667 2017-03-14 09:16:31.000000 gitlint-0.8.2/gitlint/git.py
--rw-r--r--   0 jroovers   (501) staff       (20)     2504 2016-12-27 16:32:58.000000 gitlint-0.8.2/gitlint/hooks.py
--rw-r--r--   0 jroovers   (501) staff       (20)     3725 2017-04-25 09:14:33.000000 gitlint-0.8.2/gitlint/lint.py
--rw-r--r--   0 jroovers   (501) staff       (20)     4141 2017-04-25 10:47:24.000000 gitlint-0.8.2/gitlint/options.py
--rw-r--r--   0 jroovers   (501) staff       (20)     9740 2016-12-30 13:24:17.000000 gitlint-0.8.2/gitlint/rules.py
--rw-r--r--   0 jroovers   (501) staff       (20)     6247 2017-04-25 10:34:00.000000 gitlint-0.8.2/gitlint/user_rules.py
--rw-r--r--   0 jroovers   (501) staff       (20)     1210 2017-04-25 10:17:39.000000 gitlint-0.8.2/gitlint/utils.py
-drwxr-xr-x   0 jroovers   (501) staff       (20)        0 2017-04-25 11:26:40.000000 gitlint-0.8.2/gitlint.egg-info/
--rw-r--r--   0 jroovers   (501) staff       (20)        1 2017-04-25 11:26:39.000000 gitlint-0.8.2/gitlint.egg-info/dependency_links.txt
--rw-r--r--   0 jroovers   (501) staff       (20)       45 2017-04-25 11:26:39.000000 gitlint-0.8.2/gitlint.egg-info/entry_points.txt
--rw-r--r--   0 jroovers   (501) staff       (20)     2294 2017-04-25 11:26:39.000000 gitlint-0.8.2/gitlint.egg-info/PKG-INFO
--rw-r--r--   0 jroovers   (501) staff       (20)      124 2017-04-25 11:26:39.000000 gitlint-0.8.2/gitlint.egg-info/requires.txt
--rw-r--r--   0 jroovers   (501) staff       (20)      478 2017-04-25 11:26:40.000000 gitlint-0.8.2/gitlint.egg-info/SOURCES.txt
--rw-r--r--   0 jroovers   (501) staff       (20)       11 2017-04-25 11:26:39.000000 gitlint-0.8.2/gitlint.egg-info/top_level.txt
--rw-r--r--   0 jroovers   (501) staff       (20)     1081 2015-11-22 14:42:03.000000 gitlint-0.8.2/LICENSE
--rw-r--r--   0 jroovers   (501) staff       (20)      164 2016-04-19 22:31:41.000000 gitlint-0.8.2/MANIFEST.in
--rw-r--r--   0 jroovers   (501) staff       (20)     2294 2017-04-25 11:26:40.000000 gitlint-0.8.2/PKG-INFO
--rw-r--r--   0 jroovers   (501) staff       (20)     1212 2017-04-05 07:42:05.000000 gitlint-0.8.2/README.md
--rw-r--r--   0 jroovers   (501) staff       (20)       88 2017-04-25 11:26:40.000000 gitlint-0.8.2/setup.cfg
--rw-r--r--   0 jroovers   (501) staff       (20)     3521 2017-03-14 09:22:45.000000 gitlint-0.8.2/setup.py
+drwxr-xr-x   0 jroovers   (501) staff       (20)        0 2017-12-03 17:48:58.000000 gitlint-0.9.0/
+drwxr-xr-x   0 jroovers   (501) staff       (20)        0 2017-12-03 17:48:58.000000 gitlint-0.9.0/gitlint/
+-rw-r--r--   0 jroovers   (501) staff       (20)       22 2017-12-03 16:56:58.000000 gitlint-0.9.0/gitlint/__init__.py
+-rw-r--r--   0 jroovers   (501) staff       (20)    11063 2017-12-03 13:31:52.000000 gitlint-0.9.0/gitlint/cli.py
+-rw-r--r--   0 jroovers   (501) staff       (20)    15137 2017-12-03 14:14:52.000000 gitlint-0.9.0/gitlint/config.py
+-rw-r--r--   0 jroovers   (501) staff       (20)     2062 2017-12-03 11:31:27.000000 gitlint-0.9.0/gitlint/display.py
+drwxr-xr-x   0 jroovers   (501) staff       (20)        0 2017-12-03 17:48:58.000000 gitlint-0.9.0/gitlint/files/
+-rw-r--r--   0 jroovers   (501) staff       (20)     2425 2017-04-27 19:24:41.000000 gitlint-0.9.0/gitlint/files/commit-msg
+-rw-r--r--   0 jroovers   (501) staff       (20)     2323 2017-12-03 14:14:52.000000 gitlint-0.9.0/gitlint/files/gitlint
+-rw-r--r--   0 jroovers   (501) staff       (20)     9911 2017-12-03 14:14:52.000000 gitlint-0.9.0/gitlint/git.py
+-rw-r--r--   0 jroovers   (501) staff       (20)     2504 2017-04-27 19:24:41.000000 gitlint-0.9.0/gitlint/hooks.py
+-rw-r--r--   0 jroovers   (501) staff       (20)     4300 2017-12-03 14:14:52.000000 gitlint-0.9.0/gitlint/lint.py
+-rw-r--r--   0 jroovers   (501) staff       (20)     4141 2017-04-27 19:24:41.000000 gitlint-0.9.0/gitlint/options.py
+-rw-r--r--   0 jroovers   (501) staff       (20)    10420 2017-05-14 00:49:09.000000 gitlint-0.9.0/gitlint/rules.py
+-rw-r--r--   0 jroovers   (501) staff       (20)     6247 2017-04-27 19:24:42.000000 gitlint-0.9.0/gitlint/user_rules.py
+-rw-r--r--   0 jroovers   (501) staff       (20)     1210 2017-04-27 19:24:42.000000 gitlint-0.9.0/gitlint/utils.py
+drwxr-xr-x   0 jroovers   (501) staff       (20)        0 2017-12-03 17:48:58.000000 gitlint-0.9.0/gitlint.egg-info/
+-rw-r--r--   0 jroovers   (501) staff       (20)        1 2017-12-03 17:48:58.000000 gitlint-0.9.0/gitlint.egg-info/dependency_links.txt
+-rw-r--r--   0 jroovers   (501) staff       (20)       45 2017-12-03 17:48:58.000000 gitlint-0.9.0/gitlint.egg-info/entry_points.txt
+-rw-r--r--   0 jroovers   (501) staff       (20)     2325 2017-12-03 17:48:58.000000 gitlint-0.9.0/gitlint.egg-info/PKG-INFO
+-rw-r--r--   0 jroovers   (501) staff       (20)      124 2017-12-03 17:48:58.000000 gitlint-0.9.0/gitlint.egg-info/requires.txt
+-rw-r--r--   0 jroovers   (501) staff       (20)      478 2017-12-03 17:48:58.000000 gitlint-0.9.0/gitlint.egg-info/SOURCES.txt
+-rw-r--r--   0 jroovers   (501) staff       (20)       11 2017-12-03 17:48:58.000000 gitlint-0.9.0/gitlint.egg-info/top_level.txt
+-rw-r--r--   0 jroovers   (501) staff       (20)     1081 2017-04-27 19:24:41.000000 gitlint-0.9.0/LICENSE
+-rw-r--r--   0 jroovers   (501) staff       (20)      164 2017-04-27 19:24:41.000000 gitlint-0.9.0/MANIFEST.in
+-rw-r--r--   0 jroovers   (501) staff       (20)     2325 2017-12-03 17:48:58.000000 gitlint-0.9.0/PKG-INFO
+-rw-r--r--   0 jroovers   (501) staff       (20)     1210 2017-12-03 14:42:12.000000 gitlint-0.9.0/README.md
+-rw-r--r--   0 jroovers   (501) staff       (20)       67 2017-12-03 17:48:58.000000 gitlint-0.9.0/setup.cfg
+-rw-r--r--   0 jroovers   (501) staff       (20)     3518 2017-12-03 16:53:25.000000 gitlint-0.9.0/setup.py
```

### Comparing `gitlint-0.8.2/gitlint/cli.py` & `gitlint-0.9.0/gitlint/cli.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 # pylint: disable=bad-option-value,wrong-import-position
 # We need to disable the import position checks because of the windows check that we need to do below
 import logging
 import os
 import platform
+import select
 import sys
 
 import click
 
 # Error codes
 MAX_VIOLATION_ERROR_CODE = 252  # noqa
 USAGE_ERROR_CODE = 253  # noqa
@@ -19,15 +20,15 @@
     click.echo("Gitlint currently does not support Windows. Check out "  # noqa
                "https://github.com/jorisroovers/gitlint/issues/20 for details.", err=True)  # noqa
     exit(USAGE_ERROR_CODE)  # noqa
 
 import gitlint
 from gitlint.lint import GitLinter
 from gitlint.config import LintConfigBuilder, LintConfigError, LintConfigGenerator
-from gitlint.git import GitContext, GitContextError
+from gitlint.git import GitContext, GitContextError, git_version
 from gitlint import hooks
 from gitlint.utils import ustr, LOG_FORMAT
 
 DEFAULT_CONFIG_FILE = ".gitlint"
 
 # Since we use the return code to denote the amount of errors, we need to change the default click usage error code
 click.UsageError.exit_code = USAGE_ERROR_CODE
@@ -42,14 +43,21 @@
     handler = logging.StreamHandler()
     formatter = logging.Formatter(LOG_FORMAT)
     handler.setFormatter(formatter)
     root_log.addHandler(handler)
     root_log.setLevel(logging.ERROR)
 
 
+def log_system_info():
+    LOG.debug("Platform: %s", platform.platform())
+    LOG.debug("Python version: %s", sys.version)
+    LOG.debug("Git version: %s", git_version())
+    LOG.debug("Gitlint version: %s", gitlint.__version__)
+
+
 def build_config(ctx, target, config_path, c, extra_path, ignore, verbose, silent, debug):
     """ Creates a LintConfig object based on a set of commandline parameters. """
     config_builder = LintConfigBuilder()
     try:
         # Config precedence:
         # First, load default config or config from configfile
         if config_path:
@@ -74,73 +82,90 @@
         if target:
             config_builder.set_option('general', 'target', target)
 
         if debug:
             config_builder.set_option('general', 'debug', debug)
 
         config = config_builder.build()
-        if debug:
-            click.echo(ustr(config), nl=True)
 
         return config, config_builder
     except LintConfigError as e:
         click.echo(u"Config Error: {0}".format(ustr(e)))
     ctx.exit(CONFIG_ERROR_CODE)  # return CONFIG_ERROR_CODE on config error
 
 
+def stdin_has_data():
+    """ Helper function that indicates whether the stdin has data incoming or not """
+    # This code was taken from:
+    # https://stackoverflow.com/questions/3762881/how-do-i-check-if-stdin-has-some-data
+
+    # Caveat, this probably doesn't work on Windows because the code is dependent on the unix SELECT syscall.
+    # Details: https://docs.python.org/2/library/select.html#select.select
+    # This isn't a real problem now, because gitlint as a whole doesn't support Windows (see #20).
+    # If we ever do, we probably want to fall back to the old detection mechanism of reading from the local git repo
+    # in case there's no TTY connected to STDIN.
+    return select.select([sys.stdin, ], [], [], 0.0)[0]
+
+
 @click.group(invoke_without_command=True, epilog="When no COMMAND is specified, gitlint defaults to 'gitlint lint'.")
 @click.option('--target', type=click.Path(exists=True, resolve_path=True, file_okay=False, readable=True),
               help="Path of the target git repository. [default: current working directory]")
 @click.option('-C', '--config', type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
               help="Config file location [default: {0}]".format(DEFAULT_CONFIG_FILE))
 @click.option('-c', multiple=True,
               help="Config flags in format <rule>.<option>=<value> (e.g.: -c T1.line-length=80). " +
                    "Flag can be used multiple times to set multiple config values.")  # pylint: disable=bad-continuation
-@click.option('--commits', default="HEAD", help="The range of commits to lint. [default: HEAD]")
+@click.option('--commits', default=None, help="The range of commits to lint. [default: HEAD]")
 @click.option('-e', '--extra-path', help="Path to a directory or python module with extra user-defined rules",
               type=click.Path(exists=True, resolve_path=True, readable=True))
 @click.option('--ignore', default="", help="Ignore rules (comma-separated by id or name).")
 @click.option('-v', '--verbose', count=True, default=0,
               help="Verbosity, more v's for more verbose output (e.g.: -v, -vv, -vvv). [default: -vvv]", )
 @click.option('-s', '--silent', help="Silent mode (no output). Takes precedence over -v, -vv, -vvv.", is_flag=True)
 @click.option('-d', '--debug', help="Enable debugging output.", is_flag=True)
 @click.version_option(version=gitlint.__version__)
 @click.pass_context
 def cli(ctx, target, config, c, commits, extra_path, ignore, verbose, silent, debug):
     """ Git lint tool, checks your git commit messages for styling issues """
 
-    if debug:
-        logging.getLogger("gitlint").setLevel(logging.DEBUG)
+    try:
+        if debug:
+            logging.getLogger("gitlint").setLevel(logging.DEBUG)
+
+        log_system_info()
+
+        # Get the lint config from the commandline parameters and
+        # store it in the context (click allows storing an arbitrary object in ctx.obj).
+        config, config_builder = build_config(ctx, target, config, c, extra_path, ignore, verbose, silent, debug)
+
+        LOG.debug(u"Configuration\n%s", ustr(config))
 
-    # Get the lint config from the commandline parameters and
-    # store it in the context (click allows storing an arbitrary object in ctx.obj).
-    config, config_builder = build_config(ctx, target, config, c, extra_path, ignore, verbose, silent, debug)
-
-    ctx.obj = (config, config_builder, commits)
-
-    # If no subcommand is specified, then just lint
-    if ctx.invoked_subcommand is None:
-        ctx.invoke(lint)
+        ctx.obj = (config, config_builder, commits)
+
+        # If no subcommand is specified, then just lint
+        if ctx.invoked_subcommand is None:
+            ctx.invoke(lint)
+
+    except GitContextError as e:
+        click.echo(ustr(e))
+        ctx.exit(GIT_CONTEXT_ERROR_CODE)
 
 
 @cli.command("lint")
 @click.pass_context
 def lint(ctx):
     """ Lints a git repository [default command] """
     lint_config = ctx.obj[0]
-    try:
-        if sys.stdin.isatty():
-            # If target has not been set explicitly before, fallback to the current directory
-            gitcontext = GitContext.from_local_repository(lint_config.target, ctx.obj[2])
-        else:
-            stdin_str = ustr(sys.stdin.read())
-            gitcontext = GitContext.from_commit_msg(stdin_str)
-    except GitContextError as e:
-        click.echo(ustr(e))
-        ctx.exit(GIT_CONTEXT_ERROR_CODE)
+
+    # If we get data via stdin, then let's consider that our commit message, otherwise parse it from the local git repo.
+    if stdin_has_data():
+        stdin_str = ustr(sys.stdin.read())
+        gitcontext = GitContext.from_commit_msg(stdin_str)
+    else:
+        gitcontext = GitContext.from_local_repository(lint_config.target, ctx.obj[2])
 
     number_of_commits = len(gitcontext.commits)
     # Exit if we don't have commits in the specified range. Use a 0 exit code, since a popular use-case is one
     # where users are using --commits in a check job to check the commit messages inside a CI job. By returning 0, we
     # ensure that these jobs don't fail if for whatever reason the specified commit range is empty.
     if number_of_commits == 0:
         click.echo(u'No commits in range "{0}".'.format(ctx.obj[2]))
```

### Comparing `gitlint-0.8.2/gitlint/config.py` & `gitlint-0.9.0/gitlint/config.py`

 * *Files 19% similar despite different names*

```diff
@@ -55,21 +55,24 @@
                             rules.TitleRegexMatches,
                             rules.BodyMaxLineLength,
                             rules.BodyMinLength,
                             rules.BodyMissing,
                             rules.BodyTrailingWhitespace,
                             rules.BodyHardTab,
                             rules.BodyFirstLineEmpty,
-                            rules.BodyChangedFileMention)
+                            rules.BodyChangedFileMention,
+                            rules.AuthorValidEmail)
 
     def __init__(self):
         # Use an ordered dict so that the order in which rules are applied is always the same
         self._rules = OrderedDict([(rule_cls.id, rule_cls()) for rule_cls in self.default_rule_classes])
         self._verbosity = options.IntOption('verbosity', 3, "Verbosity")
         self._ignore_merge_commits = options.BoolOption('ignore-merge-commits', True, "Ignore merge commits")
+        self._ignore_fixup_commits = options.BoolOption('ignore-fixup-commits', True, "Ignore fixup commits")
+        self._ignore_squash_commits = options.BoolOption('ignore-squash-commits', True, "Ignore squash commits")
         self._debug = options.BoolOption('debug', False, "Enable debug mode")
         self._extra_path = None
         target_description = "Path of the target git repository (default=current working directory)"
         self._target = options.PathOption('target', os.path.abspath(os.getcwd()), target_description)
         self._ignore = options.ListOption('ignore', [], 'List of rule-ids to ignore')
         self._config_path = None
 
@@ -99,14 +102,32 @@
 
     @ignore_merge_commits.setter
     @handle_option_error
     def ignore_merge_commits(self, value):
         return self._ignore_merge_commits.set(value)
 
     @property
+    def ignore_fixup_commits(self):
+        return self._ignore_fixup_commits.value
+
+    @ignore_fixup_commits.setter
+    @handle_option_error
+    def ignore_fixup_commits(self, value):
+        return self._ignore_fixup_commits.set(value)
+
+    @property
+    def ignore_squash_commits(self):
+        return self._ignore_squash_commits.value
+
+    @ignore_squash_commits.setter
+    @handle_option_error
+    def ignore_squash_commits(self, value):
+        return self._ignore_squash_commits.set(value)
+
+    @property
     def debug(self):
         return self._debug.value
 
     @debug.setter
     @handle_option_error
     def debug(self, value):
         return self._debug.set(value)
@@ -208,25 +229,29 @@
     def __eq__(self, other):
         return isinstance(other, LintConfig) and \
                self.rules == other.rules and \
                self.verbosity == other.verbosity and \
                self.target == other.target and \
                self.extra_path == other.extra_path and \
                self.ignore_merge_commits == other.ignore_merge_commits and \
+               self.ignore_fixup_commits == other.ignore_fixup_commits and \
+               self.ignore_squash_commits == other.ignore_squash_commits and \
                self.debug == other.debug and \
                self.ignore == other.ignore and \
                self._config_path == other._config_path  # noqa
 
     def __str__(self):
         # config-path is not a user exposed variable, so don't print it under the general section
         return_str = u"config-path: {0}\n".format(self._config_path)
         return_str += u"[GENERAL]\n"
         return_str += u"extra-path: {0}\n".format(self.extra_path)
         return_str += u"ignore: {0}\n".format(",".join(self.ignore))
         return_str += u"ignore-merge-commits: {0}\n".format(self.ignore_merge_commits)
+        return_str += u"ignore-fixup-commits: {0}\n".format(self.ignore_fixup_commits)
+        return_str += u"ignore-squash-commits: {0}\n".format(self.ignore_squash_commits)
         return_str += u"verbosity: {0}\n".format(self.verbosity)
         return_str += u"debug: {0}\n".format(self.debug)
         return_str += u"target: {0}\n".format(self.target)
         return_str += u"[RULES]\n"
         for rule in self.rules:
             return_str += u"  {0}: {1}\n".format(rule.id, rule.name)
             for option_name, option_value in rule.options.items():
```

### Comparing `gitlint-0.8.2/gitlint/display.py` & `gitlint-0.9.0/gitlint/display.py`

 * *Files identical despite different names*

### Comparing `gitlint-0.8.2/gitlint/files/commit-msg` & `gitlint-0.9.0/gitlint/files/commit-msg`

 * *Files identical despite different names*

### Comparing `gitlint-0.8.2/gitlint/files/gitlint` & `gitlint-0.9.0/gitlint/files/gitlint`

 * *Files 10% similar despite different names*

```diff
@@ -1,14 +1,24 @@
 # All these sections are optional, edit this file as you like.
 # [general]
+# Ignore certain rules, you can reference them by their id or by their full name
 # ignore=title-trailing-punctuation, T3
+
 # verbosity should be a value between 1 and 3, the commandline -v flags take precedence over this
 # verbosity = 2
+
 # By default gitlint will ignore merge commits. Set to 'false' to disable.
 # ignore-merge-commits=true
+
+# By default gitlint will ignore fixup commits. Set to 'false' to disable.
+# ignore-fixup-commits=true
+
+# By default gitlint will ignore squash commits. Set to 'false' to disable.
+# ignore-squash-commits=true
+
 # Enable debug mode (prints more output). Disabled by default.
 # debug=true
 
 # Set the extra-path where gitlint will search for user defined rules
 # See http://jorisroovers.github.io/gitlint/user_defined_rules for details
 # extra-path=examples/
 
@@ -42,7 +52,13 @@
 
 # [body-changed-file-mention]
 # List of files that need to be explicitly mentioned in the body when they are changed
 # This is useful for when developers often erroneously edit certain files or git submodules.
 # By specifying this rule, developers can only change the file when they explicitly reference
 # it in the commit message.
 # files=gitlint/rules.py,README.md
+
+# [author-valid-email]
+# python like regex (https://docs.python.org/2/library/re.html) that the
+# commit author email address should be matched to
+# For example, use the following regex if you only want to allow email addresses from foo.com
+# regex = "[^@]+@foo.com"
```

### Comparing `gitlint-0.8.2/gitlint/git.py` & `gitlint-0.9.0/gitlint/git.py`

 * *Files 18% similar despite different names*

```diff
@@ -7,42 +7,94 @@
 
 
 class GitContextError(Exception):
     """ Exception indicating there is an issue with the git context """
     pass
 
 
+class GitNotInstalledError(GitContextError):
+    def __init__(self):
+        super(GitNotInstalledError, self).__init__(
+            u"'git' command not found. You need to install git to use gitlint on a local repository. " +
+            u"See https://git-scm.com/book/en/v2/Getting-Started-Installing-Git on how to install git.")
+
+
+def _git(*command_parts, **kwargs):
+    """ Convenience function for running git commands. Automatically deals with exceptions and unicode. """
+    # Special arguments passed to sh: http://amoffat.github.io/sh/special_arguments.html
+    git_kwargs = {'_tty_out': False}
+    git_kwargs.update(kwargs)
+    try:
+        result = sh.git(*command_parts, **git_kwargs)
+        # If we reach this point and the result has an exit_code that is larger than 0, this means that we didn't
+        # get an exception (which is the default sh behavior for non-zero exit codes) and so the user is expecting
+        # a non-zero exit code -> just return the entire result
+        if hasattr(result, 'exit_code') and result.exit_code > 0:
+            return result
+        return ustr(result)
+    except CommandNotFound:
+        raise GitNotInstalledError()
+    except ErrorReturnCode as e:  # Something went wrong while executing the git command
+        error_msg = e.stderr.strip()
+        if '_cwd' in git_kwargs and b"Not a git repository" in error_msg:
+            error_msg = u"{0} is not a git repository.".format(git_kwargs['_cwd'])
+        else:
+            error_msg = u"An error occurred while executing '{0}': {1}".format(e.full_cmd, error_msg)
+        raise GitContextError(error_msg)
+
+
+def git_version():
+    """ Determine the git version installed on this host by calling git --version"""
+    return _git("--version").replace(u"\n", u"")
+
+
+def git_commentchar():
+    """ Shortcut for retrieving comment char from git config """
+    commentchar = _git("config", "--get", "core.commentchar", _ok_code=[1])
+    # git will return an exit code of 1 if it can't find a config value, in this case we fall-back to # as commentchar
+    if commentchar.exit_code == 1:  # pylint: disable=no-member
+        commentchar = "#"
+    return ustr(commentchar).replace(u"\n", u"")
+
+
 class GitCommitMessage(object):
     """ Class representing a git commit message. A commit message consists of the following:
       - original: The actual commit message as returned by `git log`
       - full: original, but stripped of any comments
       - title: the first line of full
       - body: all lines following the title
     """
+    COMMENT_CHAR = git_commentchar()
+    CUTLINE = '{0} ------------------------ >8 ------------------------'.format(COMMENT_CHAR)
 
     def __init__(self, original=None, full=None, title=None, body=None):
         self.original = original
         self.full = full
         self.title = title
         self.body = body
 
     @staticmethod
     def from_full_message(commit_msg_str):
         """  Parses a full git commit message by parsing a given string into the different parts of a commit message """
-        lines = [line for line in commit_msg_str.splitlines() if not line.startswith("#")]
+        all_lines = commit_msg_str.splitlines()
+        try:
+            cutline_index = all_lines.index(GitCommitMessage.CUTLINE)
+        except ValueError:
+            cutline_index = None
+        lines = [line for line in all_lines[:cutline_index] if not line.startswith(GitCommitMessage.COMMENT_CHAR)]
         full = "\n".join(lines)
         title = lines[0] if len(lines) > 0 else ""
         body = lines[1:] if len(lines) > 1 else []
         return GitCommitMessage(original=commit_msg_str, full=full, title=title, body=body)
 
     def __unicode__(self):
         return self.full  # pragma: no cover
 
     def __str__(self):
-        return sstr(self)  # pragma: no cover
+        return sstr(self.__unicode__())  # pragma: no cover
 
     def __repr__(self):
         return self.__str__()  # pragma: no cover
 
     def __eq__(self, other):
         return isinstance(other, GitCommitMessage) and self.original == other.original and \
                self.full == other.full and self.title == other.title and self.body == other.body  # noqa
@@ -50,44 +102,50 @@
 
 class GitCommit(object):
     """ Class representing a git commit.
         A commit consists of: context, message, author name, author email, date, list of changed files
         In the context of gitlint, only the git context and commit message are required.
     """
 
-    def __init__(self, context, message, sha=None, date=None, author_name=None, author_email=None, parents=None,
-                 is_merge_commit=False, changed_files=None):
+    def __init__(self, context, message, sha=None, date=None, author_name=None,  # pylint: disable=too-many-arguments
+                 author_email=None, parents=None, is_merge_commit=None, is_fixup_commit=None,
+                 is_squash_commit=None, changed_files=None):
         self.context = context
         self.message = message
         self.sha = sha
         self.date = date
         self.author_name = author_name
         self.author_email = author_email
         # parent commit hashes
         self.parents = parents or []
-        self.is_merge_commit = is_merge_commit
         self.changed_files = changed_files or []
 
+        # If it's not explicitely specified, we consider a commit a merge commit if its title starts with "Merge"
+        self.is_merge_commit = message.title.startswith(u"Merge") if is_merge_commit is None else is_merge_commit
+        self.is_fixup_commit = message.title.startswith(u"fixup!") if is_fixup_commit is None else is_fixup_commit
+        self.is_squash_commit = message.title.startswith(u"squash!") if is_squash_commit is None else is_squash_commit
+
     def __unicode__(self):
         format_str = u"Author: %s <%s>\nDate:   %s\n%s"  # pragma: no cover
         return format_str % (self.author_name, self.author_email, self.date, ustr(self.message))  # pragma: no cover
 
     def __str__(self):
-        return sstr(self)  # pragma: no cover
+        return sstr(self.__unicode__())  # pragma: no cover
 
     def __repr__(self):
         return self.__str__()  # pragma: no cover
 
     def __eq__(self, other):
         # skip checking the context as context refers back to this obj, this will trigger a cyclic dependency
         return isinstance(other, GitCommit) and self.message == other.message and \
                self.sha == other.sha and self.author_name == other.author_name and \
                self.author_email == other.author_email and \
                self.date == other.date and self.parents == other.parents and \
-               self.is_merge_commit == other.is_merge_commit and self.changed_files == other.changed_files  # noqa
+               self.is_merge_commit == other.is_merge_commit and self.is_fixup_commit == other.is_fixup_commit and \
+               self.is_squash_commit == other.is_squash_commit and self.changed_files == other.changed_files  # noqa
 
 
 class GitContext(object):
     """ Class representing the git context in which gitlint is operating: a data object storing information about
     the git repository that gitlint is linting.
     """
 
@@ -98,79 +156,61 @@
     def from_commit_msg(commit_msg_str):
         """ Determines git context based on a commit message.
         :param commit_msg_str: Full git commit message.
         """
         context = GitContext()
         commit_msg_obj = GitCommitMessage.from_full_message(commit_msg_str)
 
-        # For now, we consider a commit a merge commit if its title starts with "Merge"
-        is_merge_commit = commit_msg_obj.title.startswith("Merge")
-        commit = GitCommit(context, commit_msg_obj, is_merge_commit=is_merge_commit)
+        commit = GitCommit(context, commit_msg_obj)
 
         context.commits.append(commit)
         return context
 
     @staticmethod
-    def from_local_repository(repository_path, refspec="HEAD"):
+    def from_local_repository(repository_path, refspec=None):
         """ Retrieves the git context from a local git repository.
         :param repository_path: Path to the git repository to retrieve the context from
         :param refspec: The commit(s) to retrieve
         """
 
         context = GitContext()
-        try:
-            # Special arguments passed to sh: http://amoffat.github.io/sh/special_arguments.html
-            sh_special_args = {
-                '_tty_out': False,
-                '_cwd': repository_path
-            }
-
-            sha_list = sh.git("rev-list",
-                              # If refspec contains a dot it is a range
-                              # eg HEAD^.., upstream/master...HEAD
-                              '--max-count={0}'.format(-1 if "." in refspec else 1),
-                              refspec, **sh_special_args).split()
-
-            for sha in sha_list:
-                # Get info from the local git repository: https://git-scm.com/docs/pretty-formats
-                raw_commit = sh.git.log(sha, "-1", "--pretty=%aN,%aE,%ai,%P%n%B",
-                                        **sh_special_args).split("\n")
-
-                (name, email, date, parents), commit_msg = raw_commit[0].split(","), "\n".join(raw_commit[1:])
-
-                commit_parents = parents.split(" ")
-                commit_is_merge_commit = len(commit_parents) > 1
-
-                # changed files in last commit
-                changed_files = sh.git("diff-tree", "--no-commit-id", "--name-only",
-                                       "-r", sha, **sh_special_args).split()
-
-                # "YYYY-MM-DD HH:mm:ss Z" -> ISO 8601-like format
-                # Use arrow for datetime parsing, because apparently python is quirky around ISO-8601 dates:
-                # http://stackoverflow.com/a/30696682/381010
-                commit_date = arrow.get(ustr(date), "YYYY-MM-DD HH:mm:ss Z").datetime
-
-                # Create Git commit object with the retrieved info
-                commit_msg_obj = GitCommitMessage.from_full_message(commit_msg)
-                commit = GitCommit(context, commit_msg_obj, sha=sha, author_name=name,
-                                   author_email=email, date=commit_date, changed_files=changed_files,
-                                   parents=commit_parents, is_merge_commit=commit_is_merge_commit)
-
-                context.commits.append(commit)
-
-        except CommandNotFound:
-            raise GitContextError(
-                u"'git' command not found. You need to install git to use gitlint on a local repository. "
-                u"See https://git-scm.com/book/en/v2/Getting-Started-Installing-Git on how to install git."
-            )
-        except ErrorReturnCode as e:  # Something went wrong while executing the git command
-            error_msg = e.stderr.strip()
-            if b"Not a git repository" in error_msg:
-                error_msg = u"{0} is not a git repository.".format(repository_path)
-            else:
-                error_msg = u"An error occurred while executing '{0}': {1}".format(e.full_cmd, error_msg)
-            raise GitContextError(error_msg)
+
+        # If no refspec is defined, fallback to the last commit on the current branch
+        if refspec is None:
+            # We tried many things here e.g.: defaulting to e.g. HEAD or HEAD^... (incl. dealing with
+            # repos that only have a single commit - HEAD^... doesn't work there), but then we still get into
+            # problems with e.g. merge commits. Easiest solution is just taking the SHA from `git log -1`.
+            sha_list = [_git("log", "-1", "--pretty=%H", _cwd=repository_path).replace(u"\n", u"")]
+        else:
+            sha_list = _git("rev-list", refspec, _cwd=repository_path).split()
+
+        for sha in sha_list:
+            # Get info from the local git repository: https://git-scm.com/docs/pretty-formats
+            long_format = "--pretty=%aN%x00%aE%x00%ai%x00%P%n%B"
+            raw_commit = _git("log", sha, "-1", long_format, _cwd=repository_path).split("\n")
+
+            (name, email, date, parents), commit_msg = raw_commit[0].split('\x00'), "\n".join(raw_commit[1:])
+
+            commit_parents = parents.split(" ")
+            commit_is_merge_commit = len(commit_parents) > 1
+
+            # changed files in last commit
+            changed_files = _git("diff-tree", "--no-commit-id", "--name-only", "-r", sha, _cwd=repository_path).split()
+
+            # "YYYY-MM-DD HH:mm:ss Z" -> ISO 8601-like format
+            # Use arrow for datetime parsing, because apparently python is quirky around ISO-8601 dates:
+            # http://stackoverflow.com/a/30696682/381010
+            commit_date = arrow.get(ustr(date), "YYYY-MM-DD HH:mm:ss Z").datetime
+
+            # Create Git commit object with the retrieved info
+            commit_msg_obj = GitCommitMessage.from_full_message(commit_msg)
+
+            commit = GitCommit(context, commit_msg_obj, sha=sha, author_name=name,
+                               author_email=email, date=commit_date, changed_files=changed_files,
+                               parents=commit_parents, is_merge_commit=commit_is_merge_commit)
+
+            context.commits.append(commit)
 
         return context
 
     def __eq__(self, other):
         return isinstance(other, GitContext) and self.commits == other.commits
```

### Comparing `gitlint-0.8.2/gitlint/hooks.py` & `gitlint-0.9.0/gitlint/hooks.py`

 * *Files identical despite different names*

### Comparing `gitlint-0.8.2/gitlint/lint.py` & `gitlint-0.9.0/gitlint/lint.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,10 +1,11 @@
 import logging
 from gitlint import rules as gitlint_rules
 from gitlint import display
+from gitlint.utils import ustr
 
 LOG = logging.getLogger(__name__)
 logging.basicConfig()
 
 
 class GitLinter(object):
     """ Main linter class. This is where rules actually get applied. See the lint() method. """
@@ -58,31 +59,39 @@
             if violations:
                 all_violations.extend(violations)
         return all_violations
 
     def lint(self, commit):
         """ Lint the last commit in a given git context by applying all title, body and general rules. """
         LOG.debug("Linting commit %s", commit.sha or "[SHA UNKNOWN]")
-        # Skip linting if this is merge commit and if the config is set to ignore those
-        if commit.is_merge_commit and self.config.ignore_merge_commits:
-            return []
+        LOG.debug("Commit Object\n" + ustr(commit))
+
+        # Skip linting if this is a special commit type that is configured to be ignored
+        ignore_commit_types = ["merge", "squash", "fixup"]
+        for commit_type in ignore_commit_types:
+            if getattr(commit, "is_{0}_commit".format(commit_type)) and \
+               getattr(self.config, "ignore_{0}_commits".format(commit_type)):
+                return []
 
         violations = []
         # determine violations by applying all rules
         violations.extend(self._apply_line_rules([commit.message.title], commit, self.title_line_rules, 1))
         violations.extend(self._apply_line_rules(commit.message.body, commit, self.body_line_rules, 2))
         violations.extend(self._apply_commit_rules(self.commit_rules, commit))
 
-        # sort violations by line number
-        violations.sort(key=lambda v: (v.line_nr, v.rule_id))  # sort violations by line number and rule_id
+        # Sort violations by line number and rule_id. If there's no line nr specified (=common certain commit rules),
+        # we replace None with -1 so that it always get's placed first. Note that we need this to do this to support
+        # python 3, as None is not allowed in a list that is being sorted.
+        violations.sort(key=lambda v: (-1 if v.line_nr is None else v.line_nr, v.rule_id))
         return violations
 
     def print_violations(self, violations):
         """ Print a given set of violations to the standard error output """
         for v in violations:
-            self.display.e(u"{0}: {1}".format(v.line_nr, v.rule_id), exact=True)
-            self.display.ee(u"{0}: {1} {2}".format(v.line_nr, v.rule_id, v.message), exact=True)
+            line_nr = v.line_nr if v.line_nr else "-"
+            self.display.e(u"{0}: {1}".format(line_nr, v.rule_id), exact=True)
+            self.display.ee(u"{0}: {1} {2}".format(line_nr, v.rule_id, v.message), exact=True)
             if v.content:
-                self.display.eee(u"{0}: {1} {2}: \"{3}\"".format(v.line_nr, v.rule_id, v.message, v.content),
+                self.display.eee(u"{0}: {1} {2}: \"{3}\"".format(line_nr, v.rule_id, v.message, v.content),
                                  exact=True)
             else:
-                self.display.eee(u"{0}: {1} {2}".format(v.line_nr, v.rule_id, v.message), exact=True)
+                self.display.eee(u"{0}: {1} {2}".format(line_nr, v.rule_id, v.message), exact=True)
```

### Comparing `gitlint-0.8.2/gitlint/options.py` & `gitlint-0.9.0/gitlint/options.py`

 * *Files identical despite different names*

### Comparing `gitlint-0.8.2/gitlint/rules.py` & `gitlint-0.9.0/gitlint/rules.py`

 * *Files 3% similar despite different names*

```diff
@@ -282,7 +282,22 @@
             # if a file that we need to look out for is actually changed, then check whether it occurs
             # in the commit msg body
             if needs_mentioned_file in commit.changed_files:
                 if needs_mentioned_file not in " ".join(commit.message.body):
                     violation_message = u"Body does not mention changed file '{0}'".format(needs_mentioned_file)
                     violations.append(RuleViolation(self.id, violation_message, None, len(commit.message.body) + 1))
         return violations if violations else None
+
+
+class AuthorValidEmail(CommitRule):
+    name = "author-valid-email"
+    id = "M1"
+    options_spec = [StrOption('regex', "[^@ ]+@[^@ ]+\.[^@ ]+", "Regex that author email address should match")]
+
+    def validate(self, commit):
+        # Note that unicode is allowed in email addresses
+        # See http://stackoverflow.com/questions/3844431
+        # /are-email-addresses-allowed-to-contain-non-alphanumeric-characters
+        email_regex = re.compile(self.options['regex'].value, re.UNICODE)
+
+        if commit.author_email and not email_regex.match(commit.author_email):
+            return [RuleViolation(self.id, "Author email for commit is invalid", commit.author_email)]
```

### Comparing `gitlint-0.8.2/gitlint/user_rules.py` & `gitlint-0.9.0/gitlint/user_rules.py`

 * *Files identical despite different names*

### Comparing `gitlint-0.8.2/gitlint/utils.py` & `gitlint-0.9.0/gitlint/utils.py`

 * *Files identical despite different names*

### Comparing `gitlint-0.8.2/gitlint.egg-info/PKG-INFO` & `gitlint-0.9.0/gitlint.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,17 +1,18 @@
 Metadata-Version: 1.1
 Name: gitlint
-Version: 0.8.2
+Version: 0.9.0
 Summary: Git commit message linter written in python, checks your commit messages for style.
 Home-page: https://github.com/jorisroovers/gitlint
 Author: Joris Roovers
 Author-email: UNKNOWN
 License: MIT
+Description-Content-Type: UNKNOWN
 Description: 
-        Great for use as a commit-msg git hook or as part of your gating script in a CI/CD pipeline (e.g. jenkins).
+        Great for use as a commit-msg git hook or as part of your gating script in a CI pipeline (e.g. jenkins).
         Many of the gitlint validations are based on `well-known`_ community_ `standards`_, others are based on checks that
         we've found useful throughout the years. Gitlint has sane defaults, but you can also easily customize it to your
         own liking.
         
         Demo and full documentation on `jorisroovers.github.io/gitlint`_.
         To see what's new in the latest release, visit the CHANGELOG_.
```

### Comparing `gitlint-0.8.2/LICENSE` & `gitlint-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `gitlint-0.8.2/PKG-INFO` & `gitlint-0.9.0/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,17 +1,18 @@
 Metadata-Version: 1.1
 Name: gitlint
-Version: 0.8.2
+Version: 0.9.0
 Summary: Git commit message linter written in python, checks your commit messages for style.
 Home-page: https://github.com/jorisroovers/gitlint
 Author: Joris Roovers
 Author-email: UNKNOWN
 License: MIT
+Description-Content-Type: UNKNOWN
 Description: 
-        Great for use as a commit-msg git hook or as part of your gating script in a CI/CD pipeline (e.g. jenkins).
+        Great for use as a commit-msg git hook or as part of your gating script in a CI pipeline (e.g. jenkins).
         Many of the gitlint validations are based on `well-known`_ community_ `standards`_, others are based on checks that
         we've found useful throughout the years. Gitlint has sane defaults, but you can also easily customize it to your
         own liking.
         
         Demo and full documentation on `jorisroovers.github.io/gitlint`_.
         To see what's new in the latest release, visit the CHANGELOG_.
```

### Comparing `gitlint-0.8.2/README.md` & `gitlint-0.9.0/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -3,18 +3,18 @@
 [![Build Status](https://travis-ci.org/jorisroovers/gitlint.svg?branch=master)](https://travis-ci.org/jorisroovers/gitlint)
 [![Coverage Status](https://coveralls.io/repos/jorisroovers/gitlint/badge.svg?branch=master&service=github)](https://coveralls.io/github/jorisroovers/gitlint?branch=master)
 [![PyPi Package](https://img.shields.io/pypi/v/gitlint.png)](https://pypi.python.org/pypi/gitlint)
 ![Supported Python Versions](https://img.shields.io/pypi/pyversions/gitlint.svg)
 
 Git commit message linter written in python, checks your commit messages for style.
 
-**See [jorisroovers.github.io/gitlint/](http://jorisroovers.github.io/gitlint/) for full documentation.**
+**See [jorisroovers.github.io/gitlint](http://jorisroovers.github.io/gitlint/) for full documentation.**
 
 <a href="http://jorisroovers.github.io/gitlint/" target="_blank"><img src="https://asciinema.org/a/30477.png" width="640"/></a>
 
 ## Contributing ##
 All contributions are welcome and very much appreciated!
 
 See [jorisroovers.github.io/gitlint/contributing](http://jorisroovers.github.io/gitlint/contributing) for details on
-how to get started - it's easy! 
+how to get started - it's easy!
 
 FYI, we maintain a [wishlist on our wiki](https://github.com/jorisroovers/gitlint/wiki/Wishlist).
```

#### html2text {}

```diff
@@ -3,14 +3,14 @@
 gitlint.svg?branch=master)](https://travis-ci.org/jorisroovers/gitlint) [!
 [Coverage Status](https://coveralls.io/repos/jorisroovers/gitlint/
 badge.svg?branch=master&service=github)](https://coveralls.io/github/
 jorisroovers/gitlint?branch=master) [![PyPi Package](https://img.shields.io/
 pypi/v/gitlint.png)](https://pypi.python.org/pypi/gitlint) ![Supported Python
 Versions](https://img.shields.io/pypi/pyversions/gitlint.svg) Git commit
 message linter written in python, checks your commit messages for style. **See
-[jorisroovers.github.io/gitlint/](http://jorisroovers.github.io/gitlint/) for
+[jorisroovers.github.io/gitlint](http://jorisroovers.github.io/gitlint/) for
 full documentation.** [https://asciinema.org/a/30477.png] ## Contributing ##
 All contributions are welcome and very much appreciated! See
 [jorisroovers.github.io/gitlint/contributing](http://jorisroovers.github.io/
 gitlint/contributing) for details on how to get started - it's easy! FYI, we
 maintain a [wishlist on our wiki](https://github.com/jorisroovers/gitlint/wiki/
 Wishlist).
```

### Comparing `gitlint-0.8.2/setup.py` & `gitlint-0.9.0/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 try:
     del os.link
 except:
     pass # Not all OSes (e.g. windows) support os.link
 
 description = "Git commit message linter written in python, checks your commit messages for style."
 long_description = """
-Great for use as a commit-msg git hook or as part of your gating script in a CI/CD pipeline (e.g. jenkins).
+Great for use as a commit-msg git hook or as part of your gating script in a CI pipeline (e.g. jenkins).
 Many of the gitlint validations are based on `well-known`_ community_ `standards`_, others are based on checks that
 we've found useful throughout the years. Gitlint has sane defaults, but you can also easily customize it to your
 own liking.
 
 Demo and full documentation on `jorisroovers.github.io/gitlint`_.
 To see what's new in the latest release, visit the CHANGELOG_.
```

