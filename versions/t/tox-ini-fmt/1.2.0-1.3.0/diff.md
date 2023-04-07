# Comparing `tmp/tox_ini_fmt-1.2.0.tar.gz` & `tmp/tox_ini_fmt-1.3.0.tar.gz`

## Comparing `tox_ini_fmt-1.2.0.tar` & `tox_ini_fmt-1.3.0.tar`

### file list

```diff
@@ -1,26 +1,27 @@
--rw-r--r--   0        0        0     1804 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tox.ini
--rw-r--r--   0        0        0       97 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/__init__.py
--rw-r--r--   0        0        0     1927 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/__main__.py
--rw-r--r--   0        0        0     2172 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/cli.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/py.typed
--rw-r--r--   0        0        0      160 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/version.py
--rw-r--r--   0        0        0     1214 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/__init__.py
--rw-r--r--   0        0        0     1169 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/requires.py
--rw-r--r--   0        0        0     2109 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/section_order.py
--rw-r--r--   0        0        0     3123 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/test_env.py
--rw-r--r--   0        0        0     1058 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/tox_section.py
--rw-r--r--   0        0        0     5484 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/util.py
--rw-r--r--   0        0        0      165 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/conftest.py
--rw-r--r--   0        0        0     2321 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/test_cli.py
--rw-r--r--   0        0        0     2753 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/test_main.py
--rw-r--r--   0        0        0      438 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/test_tox_ini_fmt.py
--rw-r--r--   0        0        0     1699 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/formatter/test_line_endings.py
--rw-r--r--   0        0        0     1373 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/formatter/test_requires.py
--rw-r--r--   0        0        0     2667 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/formatter/test_section_order.py
--rw-r--r--   0        0        0     4277 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/formatter/test_test_env.py
--rw-r--r--   0        0        0     3511 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/tests/formatter/test_tox_section.py
--rw-r--r--   0        0        0      114 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/.gitignore
--rw-r--r--   0        0        0     1023 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/LICENSE.txt
--rw-r--r--   0        0        0     3658 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/README.md
--rw-r--r--   0        0        0     2621 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/pyproject.toml
--rw-r--r--   0        0        0     5342 2020-02-02 00:00:00.000000 tox_ini_fmt-1.2.0/PKG-INFO
+-rw-r--r--   0        0        0     1804 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/tox.ini
+-rw-r--r--   0        0        0       97 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/src/tox_ini_fmt/__init__.py
+-rw-r--r--   0        0        0     1937 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/src/tox_ini_fmt/__main__.py
+-rw-r--r--   0        0        0     2172 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/src/tox_ini_fmt/cli.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/src/tox_ini_fmt/py.typed
+-rw-r--r--   0        0        0      160 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/src/tox_ini_fmt/version.py
+-rw-r--r--   0        0        0     1214 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/src/tox_ini_fmt/formatter/__init__.py
+-rw-r--r--   0        0        0      874 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/src/tox_ini_fmt/formatter/requires.py
+-rw-r--r--   0        0        0     2053 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/src/tox_ini_fmt/formatter/section_order.py
+-rw-r--r--   0        0        0     3505 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/src/tox_ini_fmt/formatter/test_env.py
+-rw-r--r--   0        0        0     2400 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/src/tox_ini_fmt/formatter/tox_section.py
+-rw-r--r--   0        0        0     5775 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/src/tox_ini_fmt/formatter/util.py
+-rw-r--r--   0        0        0      165 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/tests/conftest.py
+-rw-r--r--   0        0        0     2321 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/tests/test_cli.py
+-rw-r--r--   0        0        0     3307 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/tests/test_main.py
+-rw-r--r--   0        0        0      438 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/tests/test_tox_ini_fmt.py
+-rw-r--r--   0        0        0      334 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/tests/test_upgrade.py
+-rw-r--r--   0        0        0     1855 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/tests/formatter/test_line_endings.py
+-rw-r--r--   0        0        0     1069 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/tests/formatter/test_requires.py
+-rw-r--r--   0        0        0     2752 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/tests/formatter/test_section_order.py
+-rw-r--r--   0        0        0     5074 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/tests/formatter/test_test_env.py
+-rw-r--r--   0        0        0     4972 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/tests/formatter/test_tox_section.py
+-rw-r--r--   0        0        0      114 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/.gitignore
+-rw-r--r--   0        0        0     1023 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/LICENSE.txt
+-rw-r--r--   0        0        0     3658 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/README.md
+-rw-r--r--   0        0        0     2659 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/pyproject.toml
+-rw-r--r--   0        0        0     5371 2020-02-02 00:00:00.000000 tox_ini_fmt-1.3.0/PKG-INFO
```

### Comparing `tox_ini_fmt-1.2.0/tox.ini` & `tox_ini_fmt-1.3.0/tox.ini`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.2.0/src/tox_ini_fmt/__main__.py` & `tox_ini_fmt-1.3.0/src/tox_ini_fmt/__main__.py`

 * *Files 6% similar despite different names*

```diff
@@ -46,16 +46,16 @@
                 name = str(tox_ini)
             diff = (
                 difflib.unified_diff(before.splitlines(), formatted.splitlines(), fromfile=name, tofile=name)
                 if changed
                 else []
             )
             if diff:
-                diff = color_diff(diff)
-                print("\n".join(diff))  # print diff on change
+                diff_text = "\n".join(color_diff(diff))
+                print(diff_text)  # print diff on change
             else:
                 print(f"no change for {name}")
     # exit with non success on change
     return 1 if changed else 0
 
 
 if __name__ == "__main__":
```

### Comparing `tox_ini_fmt-1.2.0/src/tox_ini_fmt/cli.py` & `tox_ini_fmt-1.3.0/src/tox_ini_fmt/cli.py`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/__init__.py` & `tox_ini_fmt-1.3.0/src/tox_ini_fmt/formatter/__init__.py`

 * *Ordering differences only*

 * *Files 1% similar despite different names*

```diff
@@ -19,19 +19,19 @@
     parser = ConfigParser(interpolation=None)
     if isinstance(tox_ini, Path):
         text = tox_ini.read_text()
     else:
         text = tox_ini
     parser.read_string(text)
 
-    order_sections(parser, opts.pin_toxenvs)
     format_tox_section(parser, opts.pin_toxenvs)
     for section_name in parser.sections():
         if section_name == "testenv" or section_name.startswith("testenv:"):
             format_test_env(parser, section_name)
+    order_sections(parser, opts.pin_toxenvs)
 
     return _generate_tox_ini(parser)
 
 
 def _generate_tox_ini(parser: ConfigParser) -> str:
     output = StringIO()
     parser.write(output)
```

### Comparing `tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/section_order.py` & `tox_ini_fmt-1.3.0/src/tox_ini_fmt/formatter/section_order.py`

 * *Files 2% similar despite different names*

```diff
@@ -21,16 +21,14 @@
             sections[section] = dict(parser[section])
             parser.pop(section)
     for k, v in sections.items():
         parser[k] = v
 
 
 def load_and_order_env_list(parser: ConfigParser, pin_toxenvs: list[str]) -> list[str]:
-    if not parser.has_section("tox"):
-        return []
     result: list[str] = next(
         (explode_env_list(parser["tox"][i]) for i in ("envlist", "env_list") if i in parser["tox"]),
         [],
     )
     missing = [e for e in pin_toxenvs if e not in result]
     if missing:
         raise RuntimeError(f"missing tox environment(s) to pin {', '.join(missing)}")
```

### Comparing `tox_ini_fmt-1.2.0/src/tox_ini_fmt/formatter/util.py` & `tox_ini_fmt-1.3.0/src/tox_ini_fmt/formatter/util.py`

 * *Files 4% similar despite different names*

```diff
@@ -10,16 +10,28 @@
 from .requires import requires
 
 
 def to_boolean(payload: str) -> str:
     return "true" if payload.lower() == "true" else "false"
 
 
-def fix_and_reorder(parser: ConfigParser, name: str, fix_cfg: Mapping[str, Callable[[str], str]]) -> None:
+def fix_and_reorder(
+    parser: ConfigParser,
+    name: str,
+    fix_cfg: Mapping[str, Callable[[str], str]],
+    upgrade: dict[str, str],
+) -> None:
     section = parser[name]
+    # upgrade
+    for key, to in upgrade.items():
+        if key in section:
+            if to in section:
+                raise RuntimeError(f"upgrade alias {to} also present for {key}")
+            section[to] = section.pop(key)
+    # normalize
     for key, fix in fix_cfg.items():
         if key in section:
             section[key] = fix(section[key])
     # reorder keys within section
     new_section = {k: section.pop(k) for k in fix_cfg.keys() if k in section}
     new_section.update(sorted(section.items()))  # sort any remaining keys
     parser[name] = new_section
```

### Comparing `tox_ini_fmt-1.2.0/tests/test_cli.py` & `tox_ini_fmt-1.3.0/tests/test_cli.py`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.2.0/tests/formatter/test_line_endings.py` & `tox_ini_fmt-1.3.0/tests/formatter/test_line_endings.py`

 * *Files 14% similar despite different names*

```diff
@@ -9,37 +9,37 @@
 
 
 def test_platform_default(tox_ini: Path) -> None:
     """If the ini file has no newlines, the platform default may be inserted."""
 
     tox_ini.write_bytes(b"[tox]")
     run([str(tox_ini)])
-    assert tox_ini.read_bytes() == f"[tox]{os.linesep}".encode()
+    assert tox_ini.read_bytes() == f"[tox]{os.linesep}requires ={os.linesep}    tox>=4.2{os.linesep}".encode()
 
 
 @pytest.mark.parametrize("newline", ["\r\n", "\n", "\r"])
 def test_line_endings(tox_ini: Path, newline: str) -> None:
     """The ini file's existing newlines must be respected when reformatting."""
 
-    original_text = f"[tox]{newline}envlist=py39"
-    expected_text = f"[tox]{newline}envlist ={newline}    py39{newline}"
+    original_text = f"[tox]{newline}requires ={newline}    tox>=4.2{newline}env_list=py39"
+    expected_text = f"[tox]{newline}requires ={newline}    tox>=4.2{newline}env_list ={newline}    py39{newline}"
     tox_ini.write_bytes(original_text.encode("utf8"))
     run([str(tox_ini)])
     assert tox_ini.read_bytes() == expected_text.encode("utf8")
 
 
 def test_mixed_line_endings(tox_ini: Path) -> None:
     """If mixed line endings are found, the first one in the tuple should be used.
 
     Note that this does not mean the first newline in the file will be used!
     Python does not report the newlines in the order they're encountered.
     """
 
-    original_text = "[tox]\r\n \r \nenvlist=py39"
-    expected_text = "[tox]!!envlist =!!    py39!!"
+    original_text = "[tox]\r\n \r \nenv_list=py39"
+    expected_text = "[tox]!!requires =!!    tox>=4.2!!env_list =!!    py39!!"
     tox_ini.write_bytes(original_text.encode("utf8"))
     with tox_ini.open("rt") as file:
         file.read()
         assert not isinstance(file.newlines, str)
         assert file.newlines is not None
         assert set(file.newlines) == {"\r", "\n", "\r\n"}
         first_newline = file.newlines[0]
```

### Comparing `tox_ini_fmt-1.2.0/tests/formatter/test_section_order.py` & `tox_ini_fmt-1.3.0/tests/formatter/test_section_order.py`

 * *Files 4% similar despite different names*

```diff
@@ -33,26 +33,28 @@
         a = b
         [testenv:dev]
         g = h
 
         [magic]
         i = j
         [tox]
-        envlist = py38,py37
+        env_list = py38,py37
         e = f
 
         """,
         ),
     )
     result = format_tox_ini(tox_ini)
 
     expected = dedent(
         """
         [tox]
-        envlist =
+        requires =
+            tox>=4.2
+        env_list =
             py38
             py37
         e = f
 
         [testenv]
         a = b
 
@@ -66,38 +68,40 @@
         i = j
     """,
     ).lstrip()
     assert result == expected
 
 
 def test_pin_missing(tox_ini: Path) -> None:
-    tox_ini.write_text("[tox]\nenvlist=py")
+    tox_ini.write_text("[tox]\nenv_list=py")
 
     with pytest.raises(RuntimeError, match=r"missing tox environment\(s\) to pin missing_1, missing_2"):
         format_tox_ini(tox_ini, ToxIniFmtNamespace(pin_toxenvs=["missing_1", "missing_2"]))
 
 
 def test_pin(tox_ini: Path) -> None:
     tox_ini.write_text(
-        "[tox]\nenvlist=py38,pkg,py,py39,pypy3,pypy,pin,extra\n"
+        "[tox]\nenv_list=py38,pkg,py,py39,pypy3,pypy,pin,extra\n"
         "[testenv:py38]\ne=f\n"
         "[testenv:pkg]\nc=d\n"
         "[testenv:py]\ng=h\n"
         "[testenv:py39]\ni=j\n"
         "[testenv:pypy3]\nk=l\n"
         "[testenv:pypy]\nm=n\n"
         "[testenv:pin]\na=b\n"
         "[testenv:extra]\no=p\n",
     )
     result = format_tox_ini(tox_ini, ToxIniFmtNamespace(pin_toxenvs=["pin", "pkg"]))
 
     expected = dedent(
         """
         [tox]
-        envlist =
+        requires =
+            tox>=4.2
+        env_list =
             pin
             pkg
             py39
             py38
             py
             pypy3
             pypy
```

### Comparing `tox_ini_fmt-1.2.0/tests/formatter/test_test_env.py` & `tox_ini_fmt-1.3.0/tests/formatter/test_test_env.py`

 * *Files 7% similar despite different names*

```diff
@@ -8,60 +8,64 @@
 from tox_ini_fmt.formatter import format_tox_ini
 from tox_ini_fmt.formatter.test_env import to_ordered_list
 from tox_ini_fmt.formatter.util import to_py_dependencies
 
 
 def test_no_tox_section(tox_ini: Path) -> None:
     tox_ini.write_text("")
-    assert format_tox_ini(tox_ini) == "\n"
+    assert format_tox_ini(tox_ini) == "[tox]\nrequires =\n    tox>=4.2\n"
 
 
 def test_format_test_env(tox_ini: Path) -> None:
     content = dedent(
         """
-    usedevelop = True
+    package = editable
     skip_install =\tFalse
     parallel_show_output = false
     commands = \te
       \tf  \\
       \t \\
       \t g
     extras = \tc,d
     description = \tdesc\t
     deps = \tb\t
       \ta\t
-    basepython=\tpython3.8\t
-    passenv=z y x
+    base_python=\tpython3.8\t
+    pass_env=z y x
     setenv= C=D
             E =F
 
             A = B
     """,
     ).strip()
     tox_ini.write_text(f"[testenv]\n{content}")
     outcome = format_tox_ini(tox_ini)
     expected = dedent(
         """
+        [tox]
+        requires =
+            tox>=4.2
+
         [testenv]
         description = desc
-        basepython = python3.8
+        base_python = python3.8
+        package = editable
         skip_install = false
-        usedevelop = true
         deps =
             a
             b
         extras =
             c
             d
         parallel_show_output = false
-        passenv =
+        pass_env =
             x
             y
             z
-        setenv =
+        set_env =
             A = B
             C = D
             E = F
         commands =
             e
             f \\
               g
@@ -89,52 +93,56 @@
     result = to_ordered_list(arg)
     assert result == output
 
 
 @pytest.mark.parametrize(
     ("key", "before", "pre", "post", "expected"),
     [
-        (
-            "setenv",
+        pytest.param(
+            "set_env",
             "\n    A = B",
             "C=D",
             "E=F",
-            "\n    {[testenv:x]X}\n    {[testenv]setenv}\n    C = D\n    E = F",
+            "\n    {[testenv:x]X}\n    {[testenv]set_env}\n    C = D\n    E = F",
+            id="setenv",
         ),
-        (
-            "passenv",
+        pytest.param(
+            "pass_env",
             "\n    A",
             "C",
             "E",
-            "\n    {[testenv:x]X}\n    {[testenv]passenv}\n    C\n    E",
+            "\n    {[testenv:x]X}\n    {[testenv]pass_env}\n    C\n    E",
+            id="pass_env",
         ),
-        (
+        pytest.param(
             "deps",
             "\n    A",
             "C",
             "B",
             "\n    {[testenv:x]X}\n    {[testenv]deps}\n    B\n    C",
+            id="deps",
         ),
-        (
+        pytest.param(
             "extras",
             "\n    A",
             "B",
             "C",
             "\n    {[testenv:x]X}\n    {[testenv]extras}\n    B\n    C",
+            id="extras",
         ),
     ],
 )
 def test_format_test_env_ref(tox_ini: Path, key: str, before: str, pre: str, post: str, expected: str) -> None:
     text = (
         f"[testenv]\n{key}={before}\n[testenv:py]"
         f"\n{key}=\n {pre}\n {{[testenv:x]X}}\n {{[testenv]{key}}}\n {post}\n"
     )
     tox_ini.write_text(text)
     outcome = format_tox_ini(tox_ini)
-    expected = f"[testenv]\n{key} ={before}\n\n[testenv:py]\n{key} ={expected}\n"
+    expected = f"[tox]\nrequires =\n    tox>=4.2\n\n[testenv]\n{key} ={before}\n\n[testenv:py]\n{key} ={expected}\n"
     assert outcome == expected
 
 
 def test_fail_on_bad_set_env(tox_ini: Path) -> None:
     tox_ini.write_text("[testenv]\nsetenv = A")
     with pytest.raises(RuntimeError, match="invalid line A in setenv"):
         format_tox_ini(tox_ini)
@@ -157,8 +165,32 @@
     result = to_py_dependencies("pytest-cov\npytest\npytest-magic>=1\npytest>=1")
     assert result == "\npytest\npytest>=1\npytest-cov\npytest-magic>=1"
 
 
 def test_depends_ordering(tox_ini: Path) -> None:
     tox_ini.write_text("[testenv]\ndepends =\n py311\n py312\n py39\n p310")
     outcome = format_tox_ini(tox_ini)
-    assert outcome == "[testenv]\ndepends =\n    py312\n    py311\n    py39\n    p310\n"
+    msg = "[tox]\nrequires =\n    tox>=4.2\n\n[testenv]\ndepends =\n    py312\n    py311\n    py39\n    p310\n"
+    assert outcome == msg
+
+
+@pytest.mark.parametrize("key", ["usedevelop", "use_develop"])
+def test_use_develop_upgrade(tox_ini: Path, key: str) -> None:
+    text = f"""\
+    [tox]
+    requires =
+        tox>=4.2
+    [testenv]
+    {key} = true
+    """
+    tox_ini.write_text(dedent(text))
+    outcome = format_tox_ini(tox_ini)
+    expected = """\
+    [tox]
+    requires =
+        tox>=4.2
+
+    [testenv]
+    package = editable
+    """
+    result = dedent(expected)
+    assert outcome == result
```

### Comparing `tox_ini_fmt-1.2.0/LICENSE.txt` & `tox_ini_fmt-1.3.0/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.2.0/README.md` & `tox_ini_fmt-1.3.0/README.md`

 * *Files identical despite different names*

### Comparing `tox_ini_fmt-1.2.0/pyproject.toml` & `tox_ini_fmt-1.3.0/pyproject.toml`

 * *Files 5% similar despite different names*

```diff
@@ -39,14 +39,17 @@
   "Topic :: Software Development :: Libraries",
   "Topic :: Software Development :: Testing",
   "Topic :: Utilities",
 ]
 dynamic = [
   "version",
 ]
+dependencies = [
+  "packaging>=23",
+]
 optional-dependencies.test = [
   "covdefaults>=2.3",
   "pytest>=7.2.2",
   "pytest-cov>=4",
 ]
 urls.Documentation = "https://tox.wiki"
 urls.Homepage = "https://github.com/tox-dev/tox-ini-fmt/blob/main/README.md#tox-ini-fmt"
```

### Comparing `tox_ini_fmt-1.2.0/PKG-INFO` & `tox_ini_fmt-1.3.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tox-ini-fmt
-Version: 1.2.0
+Version: 1.3.0
 Summary: tox is a generic virtualenv management and test command line tool
 Project-URL: Documentation, https://tox.wiki
 Project-URL: Homepage, https://github.com/tox-dev/tox-ini-fmt/blob/main/README.md#tox-ini-fmt
 Project-URL: Release Notes, https://github.com/tox-dev/tox-ini-fmt/blob/main/CHANGELOG.md
 Project-URL: Source, https://github.com/tox-dev/tox-ini-fmt
 Project-URL: Tracker, https://github.com/tox-dev/tox-ini-fmt/issues
 Maintainer-email: Bernát Gábor <gaborjbernat@gmail.com>
@@ -25,14 +25,15 @@
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Topic :: Software Development :: Libraries
 Classifier: Topic :: Software Development :: Testing
 Classifier: Topic :: Utilities
 Requires-Python: >=3.7
+Requires-Dist: packaging>=23
 Provides-Extra: test
 Requires-Dist: covdefaults>=2.3; extra == 'test'
 Requires-Dist: pytest-cov>=4; extra == 'test'
 Requires-Dist: pytest>=7.2.2; extra == 'test'
 Description-Content-Type: text/markdown
 
 # tox-ini-fmt
```

