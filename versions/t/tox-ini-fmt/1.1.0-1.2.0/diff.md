# Comparing `tmp/tox_ini_fmt-1.1.0.tar.gz` & `tmp/tox_ini_fmt-1.2.0.tar.gz`

## Comparing `tox_ini_fmt-1.1.0.tar` & `tox_ini_fmt-1.2.0.tar`

### file list

```diff
@@ -1,26 +1,26 @@
--rw-r--r--   0        0        0     1804 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/tox.ini
--rw-r--r--   0        0        0       97 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/src/tox_ini_fmt/__init__.py
--rw-r--r--   0        0        0     1927 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/src/tox_ini_fmt/__main__.py
--rw-r--r--   0        0        0     2172 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/src/tox_ini_fmt/cli.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/src/tox_ini_fmt/py.typed
--rw-r--r--   0        0        0      160 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/src/tox_ini_fmt/version.py
--rw-r--r--   0        0        0     1214 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/src/tox_ini_fmt/formatter/__init__.py
--rw-r--r--   0        0        0     1169 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/src/tox_ini_fmt/formatter/requires.py
--rw-r--r--   0        0        0     2116 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/src/tox_ini_fmt/formatter/section_order.py
--rw-r--r--   0        0        0     4882 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/src/tox_ini_fmt/formatter/test_env.py
--rw-r--r--   0        0        0     3449 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/src/tox_ini_fmt/formatter/tox_section.py
--rw-r--r--   0        0        0     1214 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/src/tox_ini_fmt/formatter/util.py
--rw-r--r--   0        0        0      165 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/tests/conftest.py
--rw-r--r--   0        0        0     2321 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/tests/test_cli.py
--rw-r--r--   0        0        0     2753 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/tests/test_main.py
--rw-r--r--   0        0        0      438 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/tests/test_tox_ini_fmt.py
--rw-r--r--   0        0        0     1699 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/tests/formatter/test_line_endings.py
--rw-r--r--   0        0        0     1373 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/tests/formatter/test_requires.py
--rw-r--r--   0        0        0     2667 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/tests/formatter/test_section_order.py
--rw-r--r--   0        0        0     3761 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/tests/formatter/test_test_env.py
--rw-r--r--   0        0        0     3518 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/tests/formatter/test_tox_section.py
--rw-r--r--   0        0        0      114 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/.gitignore
--rw-r--r--   0        0        0     1023 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/LICENSE.txt
--rw-r--r--   0        0        0     3658 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/README.md
--rw-r--r--   0        0        0     2621 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/pyproject.toml
--rw-r--r--   0        0        0     5342 2020-02-02 00:00:00.000000 tox_ini_fmt-1.1.0/PKG-INFO
+-rw-r--r--   0        0        0     1804 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tox.ini
+-rw-r--r--   0        0        0       97 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/__init__.py
+-rw-r--r--   0        0        0     1927 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/__main__.py
+-rw-r--r--   0        0        0     2172 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/cli.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/py.typed
+-rw-r--r--   0        0        0      160 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/version.py
+-rw-r--r--   0        0        0     1214 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/__init__.py
+-rw-r--r--   0        0        0     1169 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/requires.py
+-rw-r--r--   0        0        0     2109 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/section_order.py
+-rw-r--r--   0        0        0     3123 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/test_env.py
+-rw-r--r--   0        0        0     1058 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/tox_section.py
+-rw-r--r--   0        0        0     5484 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/util.py
+-rw-r--r--   0        0        0      165 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/conftest.py
+-rw-r--r--   0        0        0     2321 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/test_cli.py
+-rw-r--r--   0        0        0     2753 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/test_main.py
+-rw-r--r--   0        0        0      438 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/test_tox_ini_fmt.py
+-rw-r--r--   0        0        0     1699 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/formatter/test_line_endings.py
+-rw-r--r--   0        0        0     1373 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/formatter/test_requires.py
+-rw-r--r--   0        0        0     2667 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/formatter/test_section_order.py
+-rw-r--r--   0        0        0     4277 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/formatter/test_test_env.py
+-rw-r--r--   0        0        0     3511 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/formatter/test_tox_section.py
+-rw-r--r--   0        0        0      114 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/.gitignore
+-rw-r--r--   0        0        0     1023 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/LICENSE.txt
+-rw-r--r--   0        0        0     3658 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/README.md
+-rw-r--r--   0        0        0     2621 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/pyproject.toml
+-rw-r--r--   0        0        0     5342 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/PKG-INFO
```

### Comparing `tox_ini_fmt-1.1.0/tox.ini` & `tox_ini_fmt-1.2.0/tox.ini`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.1.0/src/tox_ini_fmt/__main__.py` & `tox_ini_fmt-1.2.0/src/tox_ini_fmt/__main__.py`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.1.0/src/tox_ini_fmt/cli.py` & `tox_ini_fmt-1.2.0/src/tox_ini_fmt/cli.py`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.1.0/src/tox_ini_fmt/formatter/__init__.py` & `tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/__init__.py`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.1.0/src/tox_ini_fmt/formatter/requires.py` & `tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/requires.py`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.1.0/src/tox_ini_fmt/formatter/section_order.py` & `tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/section_order.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from __future__ import annotations
 
 import itertools
 from configparser import ConfigParser
 
-from .tox_section import order_env_list
+from .util import order_env_list
 
 
 def order_sections(parser: ConfigParser, pin_toxenvs: list[str]) -> None:
     """
     Start with tox, then testenv. The testenv elements follow the order within envlist. Then all other testenv elements,
     and end it with any other sections present in the file (e.g. pytest/mypy configuration).
     """
```

### Comparing `tox_ini_fmt-1.1.0/tests/test_cli.py` & `tox_ini_fmt-1.2.0/tests/test_cli.py`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.1.0/tests/test_main.py` & `tox_ini_fmt-1.2.0/tests/test_main.py`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.1.0/tests/formatter/test_line_endings.py` & `tox_ini_fmt-1.2.0/tests/formatter/test_line_endings.py`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.1.0/tests/formatter/test_requires.py` & `tox_ini_fmt-1.2.0/tests/formatter/test_requires.py`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.1.0/tests/formatter/test_section_order.py` & `tox_ini_fmt-1.2.0/tests/formatter/test_section_order.py`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.1.0/tests/formatter/test_test_env.py` & `tox_ini_fmt-1.2.0/tests/formatter/test_test_env.py`

 * *Files 10% similar despite different names*

```diff
@@ -2,15 +2,16 @@
 
 from pathlib import Path
 from textwrap import dedent
 
 import pytest
 
 from tox_ini_fmt.formatter import format_tox_ini
-from tox_ini_fmt.formatter.test_env import to_deps, to_ordered_list
+from tox_ini_fmt.formatter.test_env import to_ordered_list
+from tox_ini_fmt.formatter.util import to_py_dependencies
 
 
 def test_no_tox_section(tox_ini: Path) -> None:
     tox_ini.write_text("")
     assert format_tox_ini(tox_ini) == "\n"
 
 
@@ -136,17 +137,28 @@
 def test_fail_on_bad_set_env(tox_ini: Path) -> None:
     tox_ini.write_text("[testenv]\nsetenv = A")
     with pytest.raises(RuntimeError, match="invalid line A in setenv"):
         format_tox_ini(tox_ini)
 
 
 def test_deps_conditional() -> None:
-    result = to_deps(
+    result = to_py_dependencies(
         "\ncoverage,codecov: coverage\ncodecov: codecov"
         "\n-r{toxinidir}/test-requirements.txt\n-r{toxinidir}/dev-requirements.txt"
         "\nvirtue\nb",
     )
     assert (
         result == "\n-r{toxinidir}/dev-requirements.txt\n-r{toxinidir}/test-requirements.txt"
         "\nb\nvirtue"
         "\ncodecov: codecov\ncodecov, coverage: coverage"
     )
+
+
+def test_python_req_sort_by_name() -> None:
+    result = to_py_dependencies("pytest-cov\npytest\npytest-magic>=1\npytest>=1")
+    assert result == "\npytest\npytest>=1\npytest-cov\npytest-magic>=1"
+
+
+def test_depends_ordering(tox_ini: Path) -> None:
+    tox_ini.write_text("[testenv]\ndepends =\n py311\n py312\n py39\n p310")
+    outcome = format_tox_ini(tox_ini)
+    assert outcome == "[testenv]\ndepends =\n    py312\n    py311\n    py39\n    p310\n"
```

### Comparing `tox_ini_fmt-1.1.0/tests/formatter/test_tox_section.py` & `tox_ini_fmt-1.2.0/tests/formatter/test_tox_section.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 from pathlib import Path
 from textwrap import dedent
 
 import pytest
 
 from tox_ini_fmt.formatter import format_tox_ini
-from tox_ini_fmt.formatter.tox_section import order_env_list
+from tox_ini_fmt.formatter.util import order_env_list
 
 
 def test_no_tox_section(tox_ini: Path) -> None:
     tox_ini.write_text("")
     assert format_tox_ini(tox_ini) == "\n"
```

### Comparing `tox_ini_fmt-1.1.0/LICENSE.txt` & `tox_ini_fmt-1.2.0/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.1.0/README.md` & `tox_ini_fmt-1.2.0/README.md`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.1.0/pyproject.toml` & `tox_ini_fmt-1.2.0/pyproject.toml`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.1.0/PKG-INFO` & `tox_ini_fmt-1.2.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tox-ini-fmt
-Version: 1.1.0
+Version: 1.2.0
 Summary: tox is a generic virtualenv management and test command line tool
 Project-URL: Documentation, https://tox.wiki
 Project-URL: Homepage, https://github.com/tox-dev/tox-ini-fmt/blob/main/README.md#tox-ini-fmt
 Project-URL: Release Notes, https://github.com/tox-dev/tox-ini-fmt/blob/main/CHANGELOG.md
 Project-URL: Source, https://github.com/tox-dev/tox-ini-fmt
 Project-URL: Tracker, https://github.com/tox-dev/tox-ini-fmt/issues
 Maintainer-email: Bernát Gábor <gaborjbernat@gmail.com>
```

