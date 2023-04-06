# Comparing `tmp/gitlint_core-0.20.0.dev8.tar.gz` & `tmp/gitlint_core-0.20.0.dev9.tar.gz`

## Comparing `gitlint_core-0.20.0.dev8.tar` & `gitlint_core-0.20.0.dev9.tar`

### file list

```diff
@@ -1,28 +1,28 @@
--rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/__init__.py
--rw-r--r--   0        0        0     1832 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/cache.py
--rw-r--r--   0        0        0    21324 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/cli.py
--rw-r--r--   0        0        0    22955 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/config.py
--rw-r--r--   0        0        0     1560 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/deprecation.py
--rw-r--r--   0        0        0     1259 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/display.py
--rw-r--r--   0        0        0       90 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/exception.py
--rw-r--r--   0        0        0    21093 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/git.py
--rw-r--r--   0        0        0     2619 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/hooks.py
--rw-r--r--   0        0        0     4923 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/lint.py
--rw-r--r--   0        0        0     4887 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/options.py
--rw-r--r--   0        0        0     7328 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/rule_finder.py
--rw-r--r--   0        0        0    17701 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/rules.py
--rw-r--r--   0        0        0     2195 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/shell.py
--rw-r--r--   0        0        0     3138 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/utils.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/contrib/__init__.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/contrib/rules/__init__.py
--rw-r--r--   0        0        0     1482 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/contrib/rules/authors_commit.py
--rw-r--r--   0        0        0     1269 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/contrib/rules/conventional_commit.py
--rw-r--r--   0        0        0      695 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/contrib/rules/disallow_cleanup_commits.py
--rw-r--r--   0        0        0      620 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/contrib/rules/signedoff_by.py
--rw-r--r--   0        0        0     1375 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/files/commit-msg
--rw-r--r--   0        0        0     5245 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/gitlint/files/gitlint
--rw-r--r--   0        0        0      795 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/.gitignore
--rw-r--r--   0        0        0     1081 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/LICENSE
--rw-r--r--   0        0        0     1692 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/README.md
--rw-r--r--   0        0        0     2055 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/pyproject.toml
--rw-r--r--   0        0        0     3337 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev8/PKG-INFO
+-rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/__init__.py
+-rw-r--r--   0        0        0     1896 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/cache.py
+-rw-r--r--   0        0        0    21272 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/cli.py
+-rw-r--r--   0        0        0    23105 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/config.py
+-rw-r--r--   0        0        0     1651 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/deprecation.py
+-rw-r--r--   0        0        0     1295 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/display.py
+-rw-r--r--   0        0        0       90 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/exception.py
+-rw-r--r--   0        0        0    19311 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/git.py
+-rw-r--r--   0        0        0     2619 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/hooks.py
+-rw-r--r--   0        0        0     5050 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/lint.py
+-rw-r--r--   0        0        0     4574 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/options.py
+-rw-r--r--   0        0        0     7328 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/rule_finder.py
+-rw-r--r--   0        0        0    17808 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/rules.py
+-rw-r--r--   0        0        0     2128 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/shell.py
+-rw-r--r--   0        0        0     3138 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/utils.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/contrib/__init__.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/contrib/rules/__init__.py
+-rw-r--r--   0        0        0     1482 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/contrib/rules/authors_commit.py
+-rw-r--r--   0        0        0     1269 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/contrib/rules/conventional_commit.py
+-rw-r--r--   0        0        0      695 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/contrib/rules/disallow_cleanup_commits.py
+-rw-r--r--   0        0        0      620 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/contrib/rules/signedoff_by.py
+-rw-r--r--   0        0        0     1375 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/files/commit-msg
+-rw-r--r--   0        0        0     5245 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/gitlint/files/gitlint
+-rw-r--r--   0        0        0      795 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/.gitignore
+-rw-r--r--   0        0        0     1081 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/LICENSE
+-rw-r--r--   0        0        0     1692 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/README.md
+-rw-r--r--   0        0        0     2055 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/pyproject.toml
+-rw-r--r--   0        0        0     3337 2020-02-02 00:00:00.000000 gitlint_core-0.20.0.dev9/PKG-INFO
```

### Comparing `gitlint_core-0.20.0.dev8/gitlint/cache.py` & `gitlint_core-0.20.0.dev9/gitlint/cache.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,12 +1,15 @@
+from dataclasses import dataclass, field
+
+
+@dataclass
 class PropertyCache:
     """Mixin class providing a simple cache."""
 
-    def __init__(self):
-        self._cache = {}
+    _cache: dict = field(init=False, default_factory=dict)
 
     def _try_cache(self, cache_key, cache_populate_func):
         """Tries to get a value from the cache identified by `cache_key`.
         If no value is found in the cache, do a function call to `cache_populate_func` to populate the cache
         and then return the value from the cache."""
         if cache_key not in self._cache:
             cache_populate_func()
```

### Comparing `gitlint_core-0.20.0.dev8/gitlint/cli.py` & `gitlint_core-0.20.0.dev9/gitlint/cli.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,19 +1,26 @@
 import copy
 import logging
 import os
 import platform
 import stat
 import sys
+from dataclasses import dataclass
+from typing import Optional
 
 import click
 
 import gitlint
 from gitlint import hooks
-from gitlint.config import LintConfigBuilder, LintConfigError, LintConfigGenerator
+from gitlint.config import (
+    LintConfig,
+    LintConfigBuilder,
+    LintConfigError,
+    LintConfigGenerator,
+)
 from gitlint.deprecation import DEPRECATED_LOG_FORMAT
 from gitlint.deprecation import LOG as DEPRECATED_LOG
 from gitlint.exception import GitlintError
 from gitlint.git import GitContext, GitContextError, git_version
 from gitlint.lint import GitLinter
 from gitlint.shell import shell
 from gitlint.utils import LOG_FORMAT
@@ -226,24 +233,24 @@
         click.echo(f"Error: {exc}")
         ctx.exit(USAGE_ERROR_CODE)
     elif isinstance(exc, LintConfigError):
         click.echo(f"Config Error: {exc}")
         ctx.exit(CONFIG_ERROR_CODE)
 
 
+@dataclass
 class ContextObj:
     """Simple class to hold data that is passed between Click commands via the Click context."""
 
-    def __init__(self, config, config_builder, commit_hash, refspec, msg_filename, gitcontext=None):
-        self.config = config
-        self.config_builder = config_builder
-        self.commit_hash = commit_hash
-        self.refspec = refspec
-        self.msg_filename = msg_filename
-        self.gitcontext = gitcontext
+    config: LintConfig
+    config_builder: LintConfigBuilder
+    commit_hash: str
+    refspec: str
+    msg_filename: str
+    gitcontext: Optional[GitContext] = None
 
 
 # fmt: off
 @click.group(invoke_without_command=True, context_settings={"max_content_width": 120},
              epilog="When no COMMAND is specified, gitlint defaults to 'gitlint lint'.")
 @click.option("--target", envvar="GITLINT_TARGET",
               type=click.Path(exists=True, resolve_path=True, file_okay=False, readable=True),
```

### Comparing `gitlint_core-0.20.0.dev8/gitlint/config.py` & `gitlint_core-0.20.0.dev9/gitlint/config.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,16 @@
 import copy
 import os
 import re
 import shutil
 from collections import OrderedDict
 from configparser import ConfigParser
 from configparser import Error as ConfigParserError
+from dataclasses import dataclass, field
+from typing import ClassVar, Optional
 
 from gitlint import (
     options,
     rule_finder,
     rules,
 )
 from gitlint.contrib import rules as contrib_rules
@@ -412,26 +414,25 @@
                     option_val_repr = option_value.value.pattern
                 else:
                     option_val_repr = option_value.value
                 return_str += f"     {option_name}={option_val_repr}\n"
         return return_str
 
 
+@dataclass
 class LintConfigBuilder:
     """Factory class that can build gitlint config.
     This is primarily useful to deal with complex configuration scenarios where configuration can be set and overridden
     from various sources (typically according to certain precedence rules) before the actual config should be
     normalized, validated and build. Example usage can be found in gitlint.cli.
     """
 
-    RULE_QUALIFIER_SYMBOL = ":"
-
-    def __init__(self):
-        self._config_blueprint = OrderedDict()
-        self._config_path = None
+    RULE_QUALIFIER_SYMBOL: ClassVar[str] = ":"
+    _config_blueprint: OrderedDict = field(init=False, default_factory=OrderedDict)
+    _config_path: Optional[str] = field(init=False, default=None)
 
     def set_option(self, section, option_name, option_value):
         if section not in self._config_blueprint:
             self._config_blueprint[section] = OrderedDict()
         self._config_blueprint[section][option_name] = option_value
 
     def set_config_from_commit(self, commit):
```

### Comparing `gitlint_core-0.20.0.dev8/gitlint/deprecation.py` & `gitlint_core-0.20.0.dev9/gitlint/deprecation.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,21 +1,22 @@
 import logging
+from typing import ClassVar, Optional, Set
 
 LOG = logging.getLogger("gitlint.deprecated")
 DEPRECATED_LOG_FORMAT = "%(levelname)s: %(message)s"
 
 
 class Deprecation:
     """Singleton class that handles deprecation warnings and behavior."""
 
     # LintConfig class that is used to determine deprecation behavior
-    config = None
+    config: ClassVar[Optional[object]] = None
 
     # Set of warning messages that have already been logged, to prevent duplicate warnings
-    warning_msgs = set()
+    warning_msgs: ClassVar[Set[str]] = set()
 
     @classmethod
     def get_regex_method(cls, rule, regex_option):
         """Returns the regex method to be used for a given rule based on general.regex-style-search option.
         Logs a warning if the deprecated re.match method is returned."""
 
         # if general.regex-style-search is set, just return re.search
```

### Comparing `gitlint_core-0.20.0.dev8/gitlint/git.py` & `gitlint_core-0.20.0.dev9/gitlint/git.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,13 @@
 import logging
 import os
+from dataclasses import dataclass, field
+from datetime import datetime
 from pathlib import Path
+from typing import Dict, List, Optional
 
 import arrow
 
 from gitlint import shell as sh
 from gitlint.cache import PropertyCache, cache
 from gitlint.exception import GitlintError
 
@@ -104,29 +107,117 @@
 
         changed_file_stat = GitChangedFileStats(line_stats[2], additions, deletions)
         changed_files_stats[line_stats[2]] = changed_file_stat
 
     return changed_files_stats
 
 
+@dataclass
+class GitContext(PropertyCache):
+    """Class representing the git context in which gitlint is operating: a data object storing information about
+    the git repository that gitlint is linting.
+    """
+
+    commits: List["GitCommit"] = field(init=False, default_factory=list)
+    repository_path: Optional[str] = None
+
+    @property
+    @cache
+    def commentchar(self):
+        return git_commentchar(self.repository_path)
+
+    @property
+    @cache
+    def current_branch(self):
+        try:
+            current_branch = _git("rev-parse", "--abbrev-ref", "HEAD", _cwd=self.repository_path).strip()
+        except GitContextError:
+            # Maybe there is no commit.  Try another way to get current branch (need Git 2.22+)
+            current_branch = _git("branch", "--show-current", _cwd=self.repository_path).strip()
+        return current_branch
+
+    @staticmethod
+    def from_commit_msg(commit_msg_str):
+        """Determines git context based on a commit message.
+        :param commit_msg_str: Full git commit message.
+        """
+        context = GitContext()
+        commit_msg_obj = GitCommitMessage.from_full_message(context, commit_msg_str)
+        commit = GitCommit(context, commit_msg_obj)
+        context.commits.append(commit)
+        return context
+
+    @staticmethod
+    def from_staged_commit(commit_msg_str, repository_path):
+        """Determines git context based on a commit message that is a staged commit for a local git repository.
+        :param commit_msg_str: Full git commit message.
+        :param repository_path: Path to the git repository to retrieve the context from
+        """
+        context = GitContext(repository_path=repository_path)
+        commit_msg_obj = GitCommitMessage.from_full_message(context, commit_msg_str)
+        commit = StagedLocalGitCommit(context, commit_msg_obj)
+        context.commits.append(commit)
+        return context
+
+    @staticmethod
+    def from_local_repository(repository_path, refspec=None, commit_hashes=None):
+        """Retrieves the git context from a local git repository.
+        :param repository_path: Path to the git repository to retrieve the context from
+        :param refspec: The commit(s) to retrieve (mutually exclusive with `commit_hash`)
+        :param commit_hash: Hash of the commit to retrieve (mutually exclusive with `refspec`)
+        """
+
+        context = GitContext(repository_path=repository_path)
+
+        if refspec:
+            sha_list = _git("rev-list", refspec, _cwd=repository_path).split()
+        elif commit_hashes:  # One or more commit hashes, just pass it to `git log -1`
+            # Even though we have already been passed the commit hash, we ask git to retrieve this hash and
+            # return it to us. This way we verify that the passed hash is a valid hash for the target repo and we
+            # also convert it to the full hash format (we might have been passed a short hash).
+            sha_list = []
+            for commit_hash in commit_hashes:
+                sha_list.append(_git("log", "-1", commit_hash, "--pretty=%H", _cwd=repository_path).replace("\n", ""))
+        else:  # If no refspec is defined, fallback to the last commit on the current branch
+            # We tried many things here e.g.: defaulting to e.g. HEAD or HEAD^... (incl. dealing with
+            # repos that only have a single commit - HEAD^... doesn't work there), but then we still get into
+            # problems with e.g. merge commits. Easiest solution is just taking the SHA from `git log -1`.
+            sha_list = [_git("log", "-1", "--pretty=%H", _cwd=repository_path).replace("\n", "")]
+
+        for sha in sha_list:
+            commit = LocalGitCommit(context, sha)
+            context.commits.append(commit)
+
+        return context
+
+    def __eq__(self, other):
+        return (
+            isinstance(other, GitContext)
+            and self.commits == other.commits
+            and self.repository_path == other.repository_path
+            and self.commentchar == other.commentchar
+            and self.current_branch == other.current_branch
+        )
+
+
+@dataclass
 class GitCommitMessage:
     """Class representing a git commit message. A commit message consists of the following:
     - context: The `GitContext` this commit message is part of
     - original: The actual commit message as returned by `git log`
     - full: original, but stripped of any comments
     - title: the first line of full
     - body: all lines following the title
     """
 
-    def __init__(self, context, original=None, full=None, title=None, body=None):
-        self.context = context
-        self.original = original
-        self.full = full
-        self.title = title
-        self.body = body
+    context: GitContext = field(compare=False)
+    original: str
+    full: str
+    title: str
+    body: List[str]
 
     @staticmethod
     def from_full_message(context, commit_msg_str):
         """Parses a full git commit message by parsing a given string into the different parts of a commit message"""
         all_lines = commit_msg_str.splitlines()
         cutline = f"{context.commentchar} ------------------------ >8 ------------------------"
         try:
@@ -138,72 +229,44 @@
         title = lines[0] if lines else ""
         body = lines[1:] if len(lines) > 1 else []
         return GitCommitMessage(context=context, original=commit_msg_str, full=full, title=title, body=body)
 
     def __str__(self):
         return self.full
 
-    def __eq__(self, other):
-        return (
-            isinstance(other, GitCommitMessage)
-            and self.original == other.original
-            and self.full == other.full
-            and self.title == other.title
-            and self.body == other.body
-        )
-
 
+@dataclass
 class GitChangedFileStats:
     """Class representing the stats for a changed file in git"""
 
-    def __init__(self, filepath, additions, deletions):
-        self.filepath = Path(filepath)
-        self.additions = additions
-        self.deletions = deletions
-
-    def __eq__(self, other):
-        return (
-            isinstance(other, GitChangedFileStats)
-            and self.filepath == other.filepath
-            and self.additions == other.additions
-            and self.deletions == other.deletions
-        )
+    filepath: Path
+    additions: int
+    deletions: int
 
     def __str__(self) -> str:
         return f"{self.filepath}: {self.additions} additions, {self.deletions} deletions"
 
 
+@dataclass
 class GitCommit:
     """Class representing a git commit.
     A commit consists of: context, message, author name, author email, date, list of parent commit shas,
     list of changed files, list of branch names.
     In the context of gitlint, only the git context and commit message are required.
     """
 
-    def __init__(
-        self,
-        context,
-        message,
-        sha=None,
-        date=None,
-        author_name=None,
-        author_email=None,
-        parents=None,
-        changed_files_stats=None,
-        branches=None,
-    ):
-        self.context = context
-        self.message = message
-        self.sha = sha
-        self.date = date
-        self.author_name = author_name
-        self.author_email = author_email
-        self.parents = parents or []  # parent commit hashes
-        self.changed_files_stats = changed_files_stats or {}
-        self.branches = branches or []
+    context: GitContext = field(compare=False)
+    message: GitCommitMessage
+    sha: Optional[str] = None
+    date: Optional[datetime] = None
+    author_name: Optional[str] = None
+    author_email: Optional[str] = None
+    parents: List[str] = field(default_factory=list)
+    changed_files_stats: Dict[str, GitChangedFileStats] = field(default_factory=dict)
+    branches: List[str] = field(default_factory=list)
 
     @property
     def is_merge_commit(self):
         return self.message.title.startswith("Merge")
 
     @property
     def is_fixup_commit(self):
@@ -246,35 +309,16 @@
             f"Parents: {self.parents}\n"
             f"Branches: {self.branches}\n"
             f"Changed Files: {self.changed_files}\n"
             f"Changed Files Stats:{changed_files_stats_str}\n"
             "-----------------------"
         )
 
-    def __eq__(self, other):
-        # skip checking the context as context refers back to this obj, this will trigger a cyclic dependency
-        return (
-            isinstance(other, GitCommit)
-            and self.message == other.message
-            and self.sha == other.sha
-            and self.author_name == other.author_name
-            and self.author_email == other.author_email
-            and self.date == other.date
-            and self.parents == other.parents
-            and self.is_merge_commit == other.is_merge_commit
-            and self.is_fixup_commit == other.is_fixup_commit
-            and self.is_fixup_amend_commit == other.is_fixup_amend_commit
-            and self.is_squash_commit == other.is_squash_commit
-            and self.is_revert_commit == other.is_revert_commit
-            and self.changed_files == other.changed_files
-            and self.changed_files_stats == other.changed_files_stats
-            and self.branches == other.branches
-        )
-
 
+@dataclass
 class LocalGitCommit(GitCommit, PropertyCache):
     """Class representing a git commit that exists in the local git repository.
     This class uses lazy loading: it defers reading information from the local git repository until the associated
     property is accessed for the first time. Properties are then cached for subsequent access.
 
     This approach ensures that we don't do 'expensive' git calls when certain properties are not actually used.
     In addition, reading the required info when it's needed rather than up front avoids adding delay during gitlint
@@ -362,14 +406,15 @@
                 "diff-tree", "--no-commit-id", "--numstat", "-r", "--root", self.sha, _cwd=self.context.repository_path
             )
             self._cache["changed_files_stats"] = _parse_git_changed_file_stats(changed_files_stats_raw)
 
         return self._try_cache("changed_files_stats", cache_changed_files_stats)
 
 
+@dataclass
 class StagedLocalGitCommit(GitCommit, PropertyCache):
     """Class representing a git commit that has been staged, but not committed.
 
     Other than the commit message itself (and changed files), a lot of information is actually not known at staging
     time, since the commit hasn't happened yet. However, we can make educated guesses based on existing repository
     information.
     """
@@ -415,96 +460,7 @@
     @property
     def changed_files_stats(self):
         def cache_changed_files_stats():
             changed_files_stats_raw = _git("diff", "--staged", "--numstat", "-r", _cwd=self.context.repository_path)
             self._cache["changed_files_stats"] = _parse_git_changed_file_stats(changed_files_stats_raw)
 
         return self._try_cache("changed_files_stats", cache_changed_files_stats)
-
-
-class GitContext(PropertyCache):
-    """Class representing the git context in which gitlint is operating: a data object storing information about
-    the git repository that gitlint is linting.
-    """
-
-    def __init__(self, repository_path=None):
-        PropertyCache.__init__(self)
-        self.commits = []
-        self.repository_path = repository_path
-
-    @property
-    @cache
-    def commentchar(self):
-        return git_commentchar(self.repository_path)
-
-    @property
-    @cache
-    def current_branch(self):
-        try:
-            current_branch = _git("rev-parse", "--abbrev-ref", "HEAD", _cwd=self.repository_path).strip()
-        except GitContextError:
-            # Maybe there is no commit.  Try another way to get current branch (need Git 2.22+)
-            current_branch = _git("branch", "--show-current", _cwd=self.repository_path).strip()
-        return current_branch
-
-    @staticmethod
-    def from_commit_msg(commit_msg_str):
-        """Determines git context based on a commit message.
-        :param commit_msg_str: Full git commit message.
-        """
-        context = GitContext()
-        commit_msg_obj = GitCommitMessage.from_full_message(context, commit_msg_str)
-        commit = GitCommit(context, commit_msg_obj)
-        context.commits.append(commit)
-        return context
-
-    @staticmethod
-    def from_staged_commit(commit_msg_str, repository_path):
-        """Determines git context based on a commit message that is a staged commit for a local git repository.
-        :param commit_msg_str: Full git commit message.
-        :param repository_path: Path to the git repository to retrieve the context from
-        """
-        context = GitContext(repository_path=repository_path)
-        commit_msg_obj = GitCommitMessage.from_full_message(context, commit_msg_str)
-        commit = StagedLocalGitCommit(context, commit_msg_obj)
-        context.commits.append(commit)
-        return context
-
-    @staticmethod
-    def from_local_repository(repository_path, refspec=None, commit_hashes=None):
-        """Retrieves the git context from a local git repository.
-        :param repository_path: Path to the git repository to retrieve the context from
-        :param refspec: The commit(s) to retrieve (mutually exclusive with `commit_hash`)
-        :param commit_hash: Hash of the commit to retrieve (mutually exclusive with `refspec`)
-        """
-
-        context = GitContext(repository_path=repository_path)
-
-        if refspec:
-            sha_list = _git("rev-list", refspec, _cwd=repository_path).split()
-        elif commit_hashes:  # One or more commit hashes, just pass it to `git log -1`
-            # Even though we have already been passed the commit hash, we ask git to retrieve this hash and
-            # return it to us. This way we verify that the passed hash is a valid hash for the target repo and we
-            # also convert it to the full hash format (we might have been passed a short hash).
-            sha_list = []
-            for commit_hash in commit_hashes:
-                sha_list.append(_git("log", "-1", commit_hash, "--pretty=%H", _cwd=repository_path).replace("\n", ""))
-        else:  # If no refspec is defined, fallback to the last commit on the current branch
-            # We tried many things here e.g.: defaulting to e.g. HEAD or HEAD^... (incl. dealing with
-            # repos that only have a single commit - HEAD^... doesn't work there), but then we still get into
-            # problems with e.g. merge commits. Easiest solution is just taking the SHA from `git log -1`.
-            sha_list = [_git("log", "-1", "--pretty=%H", _cwd=repository_path).replace("\n", "")]
-
-        for sha in sha_list:
-            commit = LocalGitCommit(context, sha)
-            context.commits.append(commit)
-
-        return context
-
-    def __eq__(self, other):
-        return (
-            isinstance(other, GitContext)
-            and self.commits == other.commits
-            and self.repository_path == other.repository_path
-            and self.commentchar == other.commentchar
-            and self.current_branch == other.current_branch
-        )
```

### Comparing `gitlint_core-0.20.0.dev8/gitlint/hooks.py` & `gitlint_core-0.20.0.dev9/gitlint/hooks.py`

 * *Files identical despite different names*

### Comparing `gitlint_core-0.20.0.dev8/gitlint/lint.py` & `gitlint_core-0.20.0.dev9/gitlint/lint.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,24 +1,28 @@
 import logging
+from dataclasses import dataclass, field
 
-from gitlint import display
 from gitlint import rules as gitlint_rules
+from gitlint.config import LintConfig
 from gitlint.deprecation import Deprecation
+from gitlint.display import Display
 
 LOG = logging.getLogger(__name__)
 logging.basicConfig()
 
 
+@dataclass
 class GitLinter:
     """Main linter class. This is where rules actually get applied. See the lint() method."""
 
-    def __init__(self, config):
-        self.config = config
+    config: LintConfig
+    display: Display = field(init=False)
 
-        self.display = display.Display(config)
+    def __post_init__(self):
+        self.display = Display(self.config)
 
     def should_ignore_rule(self, rule):
         """Determines whether a rule should be ignored based on the general list of commits to ignore"""
         return rule.id in self.config.ignore or rule.name in self.config.ignore
 
     @property
     def configuration_rules(self):
```

### Comparing `gitlint_core-0.20.0.dev8/gitlint/options.py` & `gitlint_core-0.20.0.dev9/gitlint/options.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,10 +1,12 @@
 import os
 import re
 from abc import abstractmethod
+from dataclasses import dataclass
+from typing import Any
 
 from gitlint.exception import GitlintError
 
 
 def allow_none(func):
     """Decorator that sets option value to None if the passed value is None, otherwise calls the regular set method"""
 
@@ -17,48 +19,47 @@
     return wrapped
 
 
 class RuleOptionError(GitlintError):
     pass
 
 
+@dataclass
 class RuleOption:
     """Base class representing a configurable part (i.e. option) of a rule (e.g. the max-length of the title-max-line
     rule).
     This class should not be used directly. Instead, use on the derived classes like StrOption, IntOption to set
     options of a particular type like int, str, etc.
     """
 
-    def __init__(self, name, value, description):
-        self.name = name
-        self.description = description
-        self.value = None
-        self.set(value)
+    name: str
+    value: Any
+    description: str
+
+    def __post_init__(self):
+        self.set(self.value)
 
     @abstractmethod
     def set(self, value):
         """Validates and sets the option's value"""
 
     def __str__(self):
         return f"({self.name}: {self.value} ({self.description}))"
 
-    def __eq__(self, other):
-        return self.name == other.name and self.description == other.description and self.value == other.value
-
 
+@dataclass
 class StrOption(RuleOption):
     @allow_none
     def set(self, value):
         self.value = str(value)
 
 
+@dataclass
 class IntOption(RuleOption):
-    def __init__(self, name, value, description, allow_negative=False):
-        self.allow_negative = allow_negative
-        super().__init__(name, value, description)
+    allow_negative: bool = False
 
     def _raise_exception(self, value):
         if self.allow_negative:
             error_msg = f"Option '{self.name}' must be an integer (current value: '{value}')"
         else:
             error_msg = f"Option '{self.name}' must be a positive integer (current value: '{value}')"
         raise RuleOptionError(error_msg)
@@ -70,42 +71,43 @@
         except ValueError:
             self._raise_exception(value)
 
         if not self.allow_negative and self.value < 0:
             self._raise_exception(value)
 
 
+@dataclass
 class BoolOption(RuleOption):
     # explicit choice to not annotate with @allow_none: Booleans must be False or True, they cannot be unset.
     def set(self, value):
         value = str(value).strip().lower()
         if value not in ["true", "false"]:
             raise RuleOptionError(f"Option '{self.name}' must be either 'true' or 'false'")
         self.value = value == "true"
 
 
+@dataclass
 class ListOption(RuleOption):
     """Option that is either a given list or a comma-separated string that can be split into a list when being set."""
 
     @allow_none
     def set(self, value):
         if isinstance(value, list):
             the_list = value
         else:
             the_list = str(value).split(",")
 
         self.value = [str(item.strip()) for item in the_list if item.strip() != ""]
 
 
+@dataclass
 class PathOption(RuleOption):
     """Option that accepts either a directory or both a directory and a file."""
 
-    def __init__(self, name, value, description, type="dir"):
-        self.type = type
-        super().__init__(name, value, description)
+    type: str = "dir"
 
     @allow_none
     def set(self, value):
         value = str(value)
 
         error_msg = ""
 
@@ -125,14 +127,15 @@
 
         if error_msg:
             raise RuleOptionError(error_msg)
 
         self.value = os.path.realpath(value)
 
 
+@dataclass
 class RegexOption(RuleOption):
     @allow_none
     def set(self, value):
         try:
             self.value = re.compile(value, re.UNICODE)
         except (re.error, TypeError) as exc:
             raise RuleOptionError(f"Invalid regular expression: '{exc}'") from exc
```

### Comparing `gitlint_core-0.20.0.dev8/gitlint/rule_finder.py` & `gitlint_core-0.20.0.dev9/gitlint/rule_finder.py`

 * *Files identical despite different names*

### Comparing `gitlint_core-0.20.0.dev8/gitlint/rules.py` & `gitlint_core-0.20.0.dev9/gitlint/rules.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,33 +1,46 @@
 import copy
 import logging
 import re
+from dataclasses import dataclass, field
+from typing import Any, ClassVar, Dict, List, Optional
 
 from gitlint.deprecation import Deprecation
 from gitlint.exception import GitlintError
-from gitlint.options import BoolOption, IntOption, ListOption, RegexOption, StrOption
+from gitlint.options import (
+    BoolOption,
+    IntOption,
+    ListOption,
+    RegexOption,
+    RuleOption,
+    StrOption,
+)
 
 
+@dataclass
 class Rule:
     """Class representing gitlint rules."""
 
-    options_spec = []
-    id = None
-    name = None
-    target = None
-    _log = None
-    _log_deprecated_regex_style_search = None
-
-    def __init__(self, opts=None):
-        if not opts:
-            opts = {}
+    # Class attributes
+    options_spec: ClassVar[List] = []
+    id: ClassVar[str]
+    name: ClassVar[str]
+    target: ClassVar[Optional["LineRuleTarget"]] = None
+    _log: ClassVar[Optional[logging.Logger]] = None
+    _log_deprecated_regex_style_search: ClassVar[Any]
+
+    # Instance attributes
+    _raw_options: Dict[str, str] = field(default_factory=dict, compare=False)
+    options: Dict[str, RuleOption] = field(init=False)
+
+    def __post_init__(self):
         self.options = {}
         for op_spec in self.options_spec:
             self.options[op_spec.name] = copy.deepcopy(op_spec)
-            actual_option = opts.get(op_spec.name)
+            actual_option = self._raw_options.get(op_spec.name)
             if actual_option is not None:
                 self.options[op_spec.name].set(actual_option)
 
     @property
     def log(self):
         if not self._log:
             self._log = logging.getLogger(__name__)
@@ -68,28 +81,23 @@
     """Target class used for rules that apply to a commit message title"""
 
 
 class CommitMessageBody(LineRuleTarget):
     """Target class used for rules that apply to a commit message body"""
 
 
+@dataclass
 class RuleViolation:
     """Class representing a violation of a rule. I.e.: When a rule is broken, the rule will instantiate this class
     to indicate how and where the rule was broken."""
 
-    def __init__(self, rule_id, message, content=None, line_nr=None):
-        self.rule_id = rule_id
-        self.line_nr = line_nr
-        self.message = message
-        self.content = content
-
-    def __eq__(self, other):
-        equal = self.rule_id == other.rule_id and self.message == other.message
-        equal = equal and self.content == other.content and self.line_nr == other.line_nr
-        return equal
+    rule_id: str
+    message: str
+    content: Optional[str] = None
+    line_nr: Optional[int] = None
 
     def __str__(self):
         return f'{self.line_nr}: {self.rule_id} {self.message}: "{self.content}"'
 
 
 class UserRuleError(GitlintError):
     """Error used to indicate that an error occurred while trying to load a user rule"""
```

### Comparing `gitlint_core-0.20.0.dev8/gitlint/shell.py` & `gitlint_core-0.20.0.dev9/gitlint/shell.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,35 +1,36 @@
 """
 This module implements a shim for the `sh` library (https://amoffat.github.io/sh/), which gitlint used to depend on.
 We still keep the `sh` API and semantics so the rest of the gitlint codebase doesn't need to be changed.
 """
 
 import subprocess
+from dataclasses import dataclass
 
 from gitlint.utils import TERMINAL_ENCODING
 
 
 def shell(cmd):
     """Convenience function that opens a given command in a shell. Does not use 'sh' library."""
     with subprocess.Popen(cmd, shell=True) as p:
         p.communicate()
 
 
 class CommandNotFound(Exception):
     """Exception indicating a command was not found during execution"""
 
 
+@dataclass
 class ShResult:
     """Result wrapper class"""
 
-    def __init__(self, full_cmd, stdout, stderr="", exitcode=0):
-        self.full_cmd = full_cmd
-        self.stdout = stdout
-        self.stderr = stderr
-        self.exit_code = exitcode
+    full_cmd: str
+    stdout: str
+    stderr: str = ""
+    exit_code: int = 0
 
     def __str__(self):
         return self.stdout
 
 
 class ErrorReturnCode(ShResult, Exception):
     """ShResult subclass for unexpected results (acts as an exception)."""
```

### Comparing `gitlint_core-0.20.0.dev8/gitlint/utils.py` & `gitlint_core-0.20.0.dev9/gitlint/utils.py`

 * *Files identical despite different names*

### Comparing `gitlint_core-0.20.0.dev8/gitlint/contrib/rules/authors_commit.py` & `gitlint_core-0.20.0.dev9/gitlint/contrib/rules/authors_commit.py`

 * *Files identical despite different names*

### Comparing `gitlint_core-0.20.0.dev8/gitlint/contrib/rules/conventional_commit.py` & `gitlint_core-0.20.0.dev9/gitlint/contrib/rules/conventional_commit.py`

 * *Files identical despite different names*

### Comparing `gitlint_core-0.20.0.dev8/gitlint/contrib/rules/disallow_cleanup_commits.py` & `gitlint_core-0.20.0.dev9/gitlint/contrib/rules/disallow_cleanup_commits.py`

 * *Files identical despite different names*

### Comparing `gitlint_core-0.20.0.dev8/gitlint/contrib/rules/signedoff_by.py` & `gitlint_core-0.20.0.dev9/gitlint/contrib/rules/signedoff_by.py`

 * *Files identical despite different names*

### Comparing `gitlint_core-0.20.0.dev8/gitlint/files/commit-msg` & `gitlint_core-0.20.0.dev9/gitlint/files/commit-msg`

 * *Files identical despite different names*

### Comparing `gitlint_core-0.20.0.dev8/gitlint/files/gitlint` & `gitlint_core-0.20.0.dev9/gitlint/files/gitlint`

 * *Files identical despite different names*

### Comparing `gitlint_core-0.20.0.dev8/.gitignore` & `gitlint_core-0.20.0.dev9/.gitignore`

 * *Files identical despite different names*

### Comparing `gitlint_core-0.20.0.dev8/LICENSE` & `gitlint_core-0.20.0.dev9/LICENSE`

 * *Files identical despite different names*

### Comparing `gitlint_core-0.20.0.dev8/README.md` & `gitlint_core-0.20.0.dev9/README.md`

 * *Files identical despite different names*

### Comparing `gitlint_core-0.20.0.dev8/pyproject.toml` & `gitlint_core-0.20.0.dev9/pyproject.toml`

 * *Files identical despite different names*

### Comparing `gitlint_core-0.20.0.dev8/PKG-INFO` & `gitlint_core-0.20.0.dev9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gitlint-core
-Version: 0.20.0.dev8
+Version: 0.20.0.dev9
 Summary: Git commit message linter written in python, checks your commit messages for style.
 Project-URL: Homepage, https://jorisroovers.github.io/gitlint
 Project-URL: Documentation, https://jorisroovers.github.io/gitlint
 Project-URL: Source, https://github.com/jorisroovers/gitlint/tree/main/gitlint-core
 Project-URL: Changelog, https://github.com/jorisroovers/gitlint/blob/main/CHANGELOG.md
 Author: Joris Roovers
 License-Expression: MIT
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: gitlint-core Version: 0.20.0.dev8 Summary: Git
+Metadata-Version: 2.1 Name: gitlint-core Version: 0.20.0.dev9 Summary: Git
 commit message linter written in python, checks your commit messages for style.
 Project-URL: Homepage, https://jorisroovers.github.io/gitlint Project-URL:
 Documentation, https://jorisroovers.github.io/gitlint Project-URL: Source,
 https://github.com/jorisroovers/gitlint/tree/main/gitlint-core Project-URL:
 Changelog, https://github.com/jorisroovers/gitlint/blob/main/CHANGELOG.md
 Author: Joris Roovers License-Expression: MIT License-File: LICENSE Keywords:
 git,gitlint,lint Classifier: Development Status :: 5 - Production/Stable
```

