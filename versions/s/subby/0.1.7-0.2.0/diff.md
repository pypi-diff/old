# Comparing `tmp/subby-0.1.7.tar.gz` & `tmp/subby-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "subby-0.1.7.tar", last modified: Tue Dec 17 20:51:47 2019, max compression
+gzip compressed data, was "subby-0.2.0.tar", max compression
```

## Comparing `subby-0.1.7.tar` & `subby-0.2.0.tar`

### file list

```diff
@@ -1,9 +1,9 @@
--rw-r--r--   0        0        0      706 2019-12-17 20:51:35.576685 subby-0.1.7/CHANGES.md
--rw-r--r--   0        0        0    11357 2019-09-09 15:19:26.555177 subby-0.1.7/LICENSE
--rw-r--r--   0        0        0     5773 2019-09-15 20:14:10.262460 subby-0.1.7/README.md
--rw-r--r--   0        0        0      540 2019-09-25 02:09:13.789253 subby-0.1.7/pyproject.toml
--rw-r--r--   0        0        0     4117 2019-09-25 01:33:54.058042 subby-0.1.7/subby/__init__.py
--rw-r--r--   0        0        0    21396 2019-12-17 20:51:35.578001 subby-0.1.7/subby/core.py
--rw-r--r--   0        0        0     1082 2019-09-15 15:35:15.791328 subby-0.1.7/subby/utils.py
--rw-r--r--   0        0        0     6404 1970-01-01 00:00:00.000000 subby-0.1.7/setup.py
--rw-r--r--   0        0        0     6357 1970-01-01 00:00:00.000000 subby-0.1.7/PKG-INFO
+-rw-r--r--   0        0        0      706 2023-04-07 00:14:27.851950 subby-0.2.0/CHANGES.md
+-rw-r--r--   0        0        0    11357 2023-04-07 00:14:27.852048 subby-0.2.0/LICENSE
+-rw-r--r--   0        0        0     6122 2023-04-07 14:17:15.419113 subby-0.2.0/README.md
+-rw-r--r--   0        0        0      540 2023-04-07 14:18:34.732261 subby-0.2.0/pyproject.toml
+-rw-r--r--   0        0        0     5566 2023-04-07 14:05:24.434572 subby-0.2.0/subby/__init__.py
+-rw-r--r--   0        0        0    21396 2023-04-07 00:14:27.852504 subby-0.2.0/subby/core.py
+-rw-r--r--   0        0        0     1082 2023-04-07 00:14:27.852585 subby-0.2.0/subby/utils.py
+-rw-r--r--   0        0        0     6813 2023-04-07 14:19:26.815250 subby-0.2.0/setup.py
+-rw-r--r--   0        0        0     6857 2023-04-07 14:19:26.815700 subby-0.2.0/PKG-INFO
```

### Comparing `subby-0.1.7/CHANGES.md` & `subby-0.2.0/CHANGES.md`

 * *Files identical despite different names*

### Comparing `subby-0.1.7/LICENSE` & `subby-0.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `subby-0.1.7/README.md` & `subby-0.2.0/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 
 ## Installation
 
 `pip install subby`
 
 ## Usage
 
-Subby's primary interface is the `run` function. It takes a list of commands and executes them. If there is are multiple commands, they are chained (i.e. piped) together.
+Subby's primary interface is the `run` function. It takes a list of commands and executes them. If there is are multiple commands, they are chained (i.e., piped) together.
 
 ```python
 import subby
 
 # We can pass input to the stdin of the command as bytes
 input_str = "foo\nbar"
 
@@ -35,15 +35,15 @@
 assert p1.output == p2.output == p3.output == "1"
 ```
 
 ### Raw mode
 
 By default, text I/O is used for stdin/stdout/stderr. You can instead use raw I/O (bytes) by passing `mode=bytes`.
 
-```
+```python
 import subby
 
 assert b"1" == subby.run(
     "grep foo | wc -l", stdin="foo\nbar", mode=bytes
 ).output
 ```
 
@@ -74,21 +74,27 @@
 # finished and the return code is 0.
 if not p.ok:
     # The `Processes.output` and `Processes.error` properties
     # provide access to the process stdout and stderr.
     print(f"The command failed: stderr={p.error}")
 ```
 
-### Convenience method
+### Convenience methods
 
-There is also a convenience method, `sub`, equivalent to calling `run` with `mode=str` and `block=True` and returning the `output` attribute (stdout) of the resulting `Processes` object.
+There are also some convenience methods to improve the ergonomics for common scenarios.
+
+* `subby.cmd`: Run a single command. Equivalent to calling `subby.run([cmd], ...)`, where `cmd` is a string (with no '|') or list of strings.
+* `subby.sub`: Equivalent to calling `subby.run` with `mode=str` and `block=True` and returning the `output` attribute (stdout) of the resulting `Processes` object.
 
 ```python
 import subby
 
+assert subby.cmd("grep foo", stdin="foo\nbar").output == "foo"
+assert subby.cmd(["grep", "foo"], stdin="foo\nbar").output == "foo"
+
 assert subby.sub("grep foo | wc -l", stdin="foo\nbar") == "1"
 ```
 
 ### stdin/stdout/stderr
 
 Subby supports several different types of arguments for stdin, stdout, and stderr:
```

### Comparing `subby-0.1.7/pyproject.toml` & `subby-0.2.0/pyproject.toml`

 * *Files 18% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "subby"
-version = "0.1.7"
+version = "0.2.0"
 description = "Subprocesses simplified"
 license = "Apache-2.0"
 authors = ["John Didion <github@didion.net>"]
 readme = "README.md"
 homepage = "https://github.com/jdidion/subby"
 repository = "https://github.com/jdidion/subby.git"
 classifiers = ["Development Status :: 4 - Beta"]
```

### Comparing `subby-0.1.7/subby/__init__.py` & `subby-0.2.0/subby/__init__.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,20 +1,48 @@
 from typing import Optional, Sequence, Type, Union
 
-from subby.core import Mode, StdType, Processes
+from subby.core import CalledProcessError, Mode, StdType, Processes
 from subby import utils
 
 DEFAULT_EXECUTABLE = "/bin/bash"
 
 
+def cmd(
+    cmd: Sequence[str],
+    shell: Optional[Union[str, bool]] = False,
+    mode: Type[Mode] = str,
+    block: bool = True,
+    **kwargs
+) -> Processes:
+    """
+    Run a single (non-piped) command. Convenience method, equivalent to run([cmd], **kwargs).
+
+    Args:
+        cmd: A command specified as a list of strings.
+        shell: Can be a boolean specifying whether to execute the command
+            using the shell, or a string value specifying the shell executable to use
+            (which also implies shell=True). If None, the value is auto-detected - `True` if `cmds`
+            is a string otherwise `False. If `true` the command is executed via the default shell
+            (which, according to the `subprocess` docs, is `/bin/sh`).
+        mode: I/O mode; can be str (text) or bytes (raw).
+        block: Whether to block until all processes have completed.
+        kwargs: Additional keyword arguments to pass to :class:`Processes`
+            constructor.
+
+    Returns:
+        A :class:`subby.Processes` object.
+    """
+    return run([cmd], shell=shell, mode=mode, block=block, **kwargs)
+
+
 def sub(
     cmds: Union[str, Sequence[Union[str, Sequence[str]]]], **kwargs
 ) -> Optional[str]:
     """
-    Convenience method, equivalent to run(cmd, mode=str, block=True, **kwargs).
+    Convenience method, equivalent to run(cmds, mode=str, block=True, **kwargs).
 
     Args:
         cmds: The command(s) to run
         kwargs: Additional kwargs passed to `run()`
 
     Returns:
         The process stdout (if its type is PIPE or BUFFER) else None.
@@ -26,30 +54,31 @@
     p = run(cmds, **kwargs)
     if p.stdout_type in {StdType.BUFFER, StdType.PIPE}:
         return p.output
 
 
 def run(
     cmds: Union[str, Sequence[Union[str, Sequence[str]]]],
-    shell: Union[str, bool] = False,
+    shell: Optional[Union[str, bool]] = None,
     mode: Type[Mode] = str,
     block: bool = True,
     **kwargs
 ) -> Processes:
     """
     Runs several commands that pipe to each other in a python-aware way.
 
     Args:
         cmds: Any number of commands (lists or strings) to pipe together. This may be
             a string, in which case it will be split on the pipe ('|') character to
             get the component commands.
         shell: Can be a boolean specifying whether to execute the command
             using the shell, or a string value specifying the shell executable to use
-            (which also implies shell=True). If None, the command is executed via the
-            default shell (which, according to the subprocess docs, is /bin/sh).
+            (which also implies shell=True). If None, the value is auto-detected - `True` if `cmds`
+            is a string otherwise `False. If `true` the command is executed via the default shell
+            (which, according to the `subprocess` docs, is `/bin/sh`).
         mode: I/O mode; can be str (text) or bytes (raw).
         block: Whether to block until all processes have completed.
         kwargs: Additional keyword arguments to pass to :class:`Processes`
             constructor.
 
     Returns:
         A :class:`subby.Processes` object.
@@ -88,33 +117,37 @@
             Traceback (most recent call last):
                   ...
             CalledProcessError: Command '['grep', 'blah']' returned non-zero
                 exit status 1
     """
     if isinstance(cmds, str):
         cmds = [c.strip() for c in cmds.split("|")]
+        if shell is None:
+            shell = True
+    else:
+        cmds = list(cmds)
+        if len(cmds) == 0:
+            raise ValueError("'cmds' cannot be an empty list")
+        if shell is None:
+            shell = False
 
     if shell is False:
         cmds = utils.command_strings_to_lists(cmds)
     else:
         cmds = utils.command_lists_to_strings(cmds)
 
     if shell is True:
         executable = DEFAULT_EXECUTABLE
     elif isinstance(shell, str):
         executable = shell
     else:
         executable = None
 
     processes = Processes(
-        cmds,
-        mode=mode,
-        shell=(shell is not False),
-        executable=executable,
-        **kwargs
+        cmds, mode=mode, shell=(shell is not False), executable=executable, **kwargs
     )
 
     if block:
         with processes:
             processes.block()
     else:
         processes.run()
```

### Comparing `subby-0.1.7/subby/core.py` & `subby-0.2.0/subby/core.py`

 * *Files identical despite different names*

### Comparing `subby-0.1.7/subby/utils.py` & `subby-0.2.0/subby/utils.py`

 * *Files identical despite different names*

### Comparing `subby-0.1.7/setup.py` & `subby-0.2.0/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,23 +1,25 @@
 # -*- coding: utf-8 -*-
-from distutils.core import setup
+from setuptools import setup
 
 packages = \
 ['subby']
 
 package_data = \
 {'': ['*']}
 
 setup_kwargs = {
     'name': 'subby',
-    'version': '0.1.7',
+    'version': '0.2.0',
     'description': 'Subprocesses simplified',
-    'long_description': '[![Travis CI](https://travis-ci.org/jdidion/subby.svg?branch=master)](https://travis-ci.org/jdidion/subby)\n[![Code Coverage](https://codecov.io/gh/jdidion/subby/branch/master/graph/badge.svg)](https://codecov.io/gh/jdidion/subby)\n\nSubby is a small Python library with the goal of simplifying the use of subprocesses. Subby is similar to [delegator.py](https://github.com/amitt001/delegator.py), but it adds a few additional features and excludes others (e.g. no `pexpect` support).\n\n## Requirements\n\nThe only requirement is python 3.6+. There are no other 3rd-party runtime dependencies. The `pytest` and `coverage` packages are required for testing.\n\n## Installation\n\n`pip install subby`\n\n## Usage\n\nSubby\'s primary interface is the `run` function. It takes a list of commands and executes them. If there is are multiple commands, they are chained (i.e. piped) together.\n\n```python\nimport subby\n\n# We can pass input to the stdin of the command as bytes\ninput_str = "foo\\nbar"\n\n# The following three commands are equivalent; each returns a\n# `Processes` object that can be used to inspect and control\n# the process(es).\np1 = subby.run([["grep foo", "wc -l"]], stdin=input_str)\np2 = subby.run(("grep foo", "wc -l"), stdin=input_str)\np3 = subby.run("grep foo | wc -l", stdin=input_str)\n\n# The `done` property tells us whether the processes have finished\nassert p1.done and p2.done and p3.done\n\n# The `output` property provides the output of the command\nassert p1.output == p2.output == p3.output == "1"\n```\n\n### Raw mode\n\nBy default, text I/O is used for stdin/stdout/stderr. You can instead use raw I/O (bytes) by passing `mode=bytes`.\n\n```\nimport subby\n\nassert b"1" == subby.run(\n    "grep foo | wc -l", stdin="foo\\nbar", mode=bytes\n).output\n```\n\n### Non-blocking processes\n\nBy default, the `run` function blocks until the processes are finshed running. This behavior can be changed by passing `block=False`, in which case, the caller is responsible for checking the status and/or calling the `Processes.block()` method manually.\n\n```python\nimport subby\nimport time\n\np = subby.run("sleep 10", block=False)\nfor i in range(5):\n    if p.done:\n        break\n    else:\n        time.sleep(1)\nelse:\n    # A timeout can be used to kill the process if it doesn\'t\n    # complete in a certain amount of time. By default, block()\n    # raises an error if the return code is non-zero.\n    p.block(timeout=10, raise_on_error=False)\n    \n    # The process can also be killed manually.\n    p.kill()\n\n# The `Processes.ok` property is True if the processes have\n# finished and the return code is 0.\nif not p.ok:\n    # The `Processes.output` and `Processes.error` properties\n    # provide access to the process stdout and stderr.\n    print(f"The command failed: stderr={p.error}")\n```\n\n### Convenience method\n\nThere is also a convenience method, `sub`, equivalent to calling `run` with `mode=str` and `block=True` and returning the `output` attribute (stdout) of the resulting `Processes` object.\n\n```python\nimport subby\n\nassert subby.sub("grep foo | wc -l", stdin="foo\\nbar") == "1"\n```\n\n### stdin/stdout/stderr\n\nSubby supports several different types of arguments for stdin, stdout, and stderr:\n\n* A file: specified as a `pathlib.Path`; for stdin, the content is read from the file, whereas for stdout/stderr the content is written to the file (and is thus not available via the `output`/`error` properties).\n* A bytes string: for stdin, the bytes are written to a temporary file, which is passed to the process stdin.\n* One of the values provided by the `StdType` enumeration:\n    * PIPE: for stdout/stderr, `subprocess.PIPE` is used, giving the caller direct access to the process stdout/stderr streams.\n    * BUFFER: for stdout/stderr, a temporary file is used, and the contents are made available via the `output`/`error` properties after the process completes.\n    * SYS: stdin/stdout/stderr is passed through from the main process (i.e. the `sys.stdin/sys.stdout/sys.stderr` streams).\n\nBy default, the stderr streams of all processes in a chain are captured (you can disable this by passing `capture_stderr=False` to `run()`).\n\n```python\nimport subby\np = subby.run("echo -n hi | tee /dev/stderr | tee /dev/stderr")\nassert p.output == b"hi"\nassert p.get_all_stderr() == [b"", b"hi", b"hi"]\n```\n\n### Logging\n\nBy default, all executed commands are logged (with loglevel INFO). You can disable this behavior by passing `echo=False` to `run()`.\n\n```python\nimport subby\nsubby.run("touch foo")  # Echoes "touch foo" to the log with level INFO\nsubby.run("login -p mypassword", echo=False)  # Does not echo mypassword\n```\n\n### Return codes\n\nBy default, Subby treats a return code of `0` as success and all other return codes as failure. In some cases, this is not the desired behavior. A well-known example is `grep`, which has a returncode of `1` when no lines are matched. To ignore additional return codes, set the `allowed_return_codes` keyword argument to `run()`.\n\n```python\nimport subby\nsubby.run("echo foo | grep bar")  # Raises CalledProcessError\nsubby.run("echo foo | grep bar", allowed_return_codes=(0, 1))\n```\n## Contributing\n\nSubby is considered to be largely feature-complete, but if you find a bug or have a suggestion for improvement, please submit an issue (or even better, a pull request).\n\n## Acknowledgements\n\nSubby was inspired by [delegator.py](https://github.com/amitt001/delegator.py).\n\nSubby was originally written as part of the [dxpy.sugar](https://github.com/dnanexus/dx-toolkit/tree/SCI-1321_dx_sugar/src/python/dxpy/sugar) package, but because it is (hopefully) useful more generally, it is being made available as a separate package. [@Damien-Black](https://github.com/@Damien-Black) and [@msimbirsky](https://github.com/msimbirsky) contributed code and reviews.\n',
+    'long_description': '[![Travis CI](https://travis-ci.org/jdidion/subby.svg?branch=master)](https://travis-ci.org/jdidion/subby)\n[![Code Coverage](https://codecov.io/gh/jdidion/subby/branch/master/graph/badge.svg)](https://codecov.io/gh/jdidion/subby)\n\nSubby is a small Python library with the goal of simplifying the use of subprocesses. Subby is similar to [delegator.py](https://github.com/amitt001/delegator.py), but it adds a few additional features and excludes others (e.g. no `pexpect` support).\n\n## Requirements\n\nThe only requirement is python 3.6+. There are no other 3rd-party runtime dependencies. The `pytest` and `coverage` packages are required for testing.\n\n## Installation\n\n`pip install subby`\n\n## Usage\n\nSubby\'s primary interface is the `run` function. It takes a list of commands and executes them. If there is are multiple commands, they are chained (i.e., piped) together.\n\n```python\nimport subby\n\n# We can pass input to the stdin of the command as bytes\ninput_str = "foo\\nbar"\n\n# The following three commands are equivalent; each returns a\n# `Processes` object that can be used to inspect and control\n# the process(es).\np1 = subby.run([["grep foo", "wc -l"]], stdin=input_str)\np2 = subby.run(("grep foo", "wc -l"), stdin=input_str)\np3 = subby.run("grep foo | wc -l", stdin=input_str)\n\n# The `done` property tells us whether the processes have finished\nassert p1.done and p2.done and p3.done\n\n# The `output` property provides the output of the command\nassert p1.output == p2.output == p3.output == "1"\n```\n\n### Raw mode\n\nBy default, text I/O is used for stdin/stdout/stderr. You can instead use raw I/O (bytes) by passing `mode=bytes`.\n\n```python\nimport subby\n\nassert b"1" == subby.run(\n    "grep foo | wc -l", stdin="foo\\nbar", mode=bytes\n).output\n```\n\n### Non-blocking processes\n\nBy default, the `run` function blocks until the processes are finshed running. This behavior can be changed by passing `block=False`, in which case, the caller is responsible for checking the status and/or calling the `Processes.block()` method manually.\n\n```python\nimport subby\nimport time\n\np = subby.run("sleep 10", block=False)\nfor i in range(5):\n    if p.done:\n        break\n    else:\n        time.sleep(1)\nelse:\n    # A timeout can be used to kill the process if it doesn\'t\n    # complete in a certain amount of time. By default, block()\n    # raises an error if the return code is non-zero.\n    p.block(timeout=10, raise_on_error=False)\n    \n    # The process can also be killed manually.\n    p.kill()\n\n# The `Processes.ok` property is True if the processes have\n# finished and the return code is 0.\nif not p.ok:\n    # The `Processes.output` and `Processes.error` properties\n    # provide access to the process stdout and stderr.\n    print(f"The command failed: stderr={p.error}")\n```\n\n### Convenience methods\n\nThere are also some convenience methods to improve the ergonomics for common scenarios.\n\n* `subby.cmd`: Run a single command. Equivalent to calling `subby.run([cmd], ...)`, where `cmd` is a string (with no \'|\') or list of strings.\n* `subby.sub`: Equivalent to calling `subby.run` with `mode=str` and `block=True` and returning the `output` attribute (stdout) of the resulting `Processes` object.\n\n```python\nimport subby\n\nassert subby.cmd("grep foo", stdin="foo\\nbar").output == "foo"\nassert subby.cmd(["grep", "foo"], stdin="foo\\nbar").output == "foo"\n\nassert subby.sub("grep foo | wc -l", stdin="foo\\nbar") == "1"\n```\n\n### stdin/stdout/stderr\n\nSubby supports several different types of arguments for stdin, stdout, and stderr:\n\n* A file: specified as a `pathlib.Path`; for stdin, the content is read from the file, whereas for stdout/stderr the content is written to the file (and is thus not available via the `output`/`error` properties).\n* A bytes string: for stdin, the bytes are written to a temporary file, which is passed to the process stdin.\n* One of the values provided by the `StdType` enumeration:\n    * PIPE: for stdout/stderr, `subprocess.PIPE` is used, giving the caller direct access to the process stdout/stderr streams.\n    * BUFFER: for stdout/stderr, a temporary file is used, and the contents are made available via the `output`/`error` properties after the process completes.\n    * SYS: stdin/stdout/stderr is passed through from the main process (i.e. the `sys.stdin/sys.stdout/sys.stderr` streams).\n\nBy default, the stderr streams of all processes in a chain are captured (you can disable this by passing `capture_stderr=False` to `run()`).\n\n```python\nimport subby\np = subby.run("echo -n hi | tee /dev/stderr | tee /dev/stderr")\nassert p.output == b"hi"\nassert p.get_all_stderr() == [b"", b"hi", b"hi"]\n```\n\n### Logging\n\nBy default, all executed commands are logged (with loglevel INFO). You can disable this behavior by passing `echo=False` to `run()`.\n\n```python\nimport subby\nsubby.run("touch foo")  # Echoes "touch foo" to the log with level INFO\nsubby.run("login -p mypassword", echo=False)  # Does not echo mypassword\n```\n\n### Return codes\n\nBy default, Subby treats a return code of `0` as success and all other return codes as failure. In some cases, this is not the desired behavior. A well-known example is `grep`, which has a returncode of `1` when no lines are matched. To ignore additional return codes, set the `allowed_return_codes` keyword argument to `run()`.\n\n```python\nimport subby\nsubby.run("echo foo | grep bar")  # Raises CalledProcessError\nsubby.run("echo foo | grep bar", allowed_return_codes=(0, 1))\n```\n## Contributing\n\nSubby is considered to be largely feature-complete, but if you find a bug or have a suggestion for improvement, please submit an issue (or even better, a pull request).\n\n## Acknowledgements\n\nSubby was inspired by [delegator.py](https://github.com/amitt001/delegator.py).\n\nSubby was originally written as part of the [dxpy.sugar](https://github.com/dnanexus/dx-toolkit/tree/SCI-1321_dx_sugar/src/python/dxpy/sugar) package, but because it is (hopefully) useful more generally, it is being made available as a separate package. [@Damien-Black](https://github.com/@Damien-Black) and [@msimbirsky](https://github.com/msimbirsky) contributed code and reviews.\n',
     'author': 'John Didion',
     'author_email': 'github@didion.net',
+    'maintainer': None,
+    'maintainer_email': None,
     'url': 'https://github.com/jdidion/subby',
     'packages': packages,
     'package_data': package_data,
     'python_requires': '>=3.6,<4.0',
 }
```

### Comparing `subby-0.1.7/PKG-INFO` & `subby-0.2.0/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,21 +1,24 @@
 Metadata-Version: 2.1
 Name: subby
-Version: 0.1.7
+Version: 0.2.0
 Summary: Subprocesses simplified
 Home-page: https://github.com/jdidion/subby
 License: Apache-2.0
 Author: John Didion
 Author-email: github@didion.net
 Requires-Python: >=3.6,<4.0
 Classifier: Development Status :: 4 - Beta
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
 Project-URL: Repository, https://github.com/jdidion/subby.git
 Description-Content-Type: text/markdown
 
 [![Travis CI](https://travis-ci.org/jdidion/subby.svg?branch=master)](https://travis-ci.org/jdidion/subby)
 [![Code Coverage](https://codecov.io/gh/jdidion/subby/branch/master/graph/badge.svg)](https://codecov.io/gh/jdidion/subby)
 
 Subby is a small Python library with the goal of simplifying the use of subprocesses. Subby is similar to [delegator.py](https://github.com/amitt001/delegator.py), but it adds a few additional features and excludes others (e.g. no `pexpect` support).
@@ -26,15 +29,15 @@
 
 ## Installation
 
 `pip install subby`
 
 ## Usage
 
-Subby's primary interface is the `run` function. It takes a list of commands and executes them. If there is are multiple commands, they are chained (i.e. piped) together.
+Subby's primary interface is the `run` function. It takes a list of commands and executes them. If there is are multiple commands, they are chained (i.e., piped) together.
 
 ```python
 import subby
 
 # We can pass input to the stdin of the command as bytes
 input_str = "foo\nbar"
 
@@ -52,15 +55,15 @@
 assert p1.output == p2.output == p3.output == "1"
 ```
 
 ### Raw mode
 
 By default, text I/O is used for stdin/stdout/stderr. You can instead use raw I/O (bytes) by passing `mode=bytes`.
 
-```
+```python
 import subby
 
 assert b"1" == subby.run(
     "grep foo | wc -l", stdin="foo\nbar", mode=bytes
 ).output
 ```
 
@@ -91,21 +94,27 @@
 # finished and the return code is 0.
 if not p.ok:
     # The `Processes.output` and `Processes.error` properties
     # provide access to the process stdout and stderr.
     print(f"The command failed: stderr={p.error}")
 ```
 
-### Convenience method
+### Convenience methods
 
-There is also a convenience method, `sub`, equivalent to calling `run` with `mode=str` and `block=True` and returning the `output` attribute (stdout) of the resulting `Processes` object.
+There are also some convenience methods to improve the ergonomics for common scenarios.
+
+* `subby.cmd`: Run a single command. Equivalent to calling `subby.run([cmd], ...)`, where `cmd` is a string (with no '|') or list of strings.
+* `subby.sub`: Equivalent to calling `subby.run` with `mode=str` and `block=True` and returning the `output` attribute (stdout) of the resulting `Processes` object.
 
 ```python
 import subby
 
+assert subby.cmd("grep foo", stdin="foo\nbar").output == "foo"
+assert subby.cmd(["grep", "foo"], stdin="foo\nbar").output == "foo"
+
 assert subby.sub("grep foo | wc -l", stdin="foo\nbar") == "1"
 ```
 
 ### stdin/stdout/stderr
 
 Subby supports several different types of arguments for stdin, stdout, and stderr:
```

