# Comparing `tmp/fw_utils-4.2.7-py3-none-any.whl.zip` & `tmp/fw_utils-4.2.8-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,16 +1,16 @@
-Zip file size: 21927 bytes, number of entries: 14
--rw-r--r--  2.0 unx      962 b- defN 80-Jan-01 00:00 fw_utils/__init__.py
+Zip file size: 22038 bytes, number of entries: 14
+-rw-r--r--  2.0 unx     1747 b- defN 80-Jan-01 00:00 fw_utils/__init__.py
 -rw-r--r--  2.0 unx     2914 b- defN 80-Jan-01 00:00 fw_utils/datetime.py
 -rw-r--r--  2.0 unx     3095 b- defN 80-Jan-01 00:00 fw_utils/dicts.py
--rw-r--r--  2.0 unx     5486 b- defN 80-Jan-01 00:00 fw_utils/files.py
--rw-r--r--  2.0 unx     8877 b- defN 80-Jan-01 00:00 fw_utils/filters.py
--rw-r--r--  2.0 unx    10293 b- defN 80-Jan-01 00:00 fw_utils/formatters.py
--rw-r--r--  2.0 unx    15084 b- defN 80-Jan-01 00:00 fw_utils/parsers.py
+-rw-r--r--  2.0 unx     5436 b- defN 80-Jan-01 00:00 fw_utils/files.py
+-rw-r--r--  2.0 unx     8838 b- defN 80-Jan-01 00:00 fw_utils/filters.py
+-rw-r--r--  2.0 unx    10485 b- defN 80-Jan-01 00:00 fw_utils/formatters.py
+-rw-r--r--  2.0 unx    15077 b- defN 80-Jan-01 00:00 fw_utils/parsers.py
 -rw-r--r--  2.0 unx        0 b- defN 80-Jan-01 00:00 fw_utils/py.typed
--rw-r--r--  2.0 unx     4434 b- defN 80-Jan-01 00:00 fw_utils/state.py
--rw-r--r--  2.0 unx     3279 b- defN 80-Jan-01 00:00 fw_utils/testing.py
--rw-r--r--  2.0 unx       88 b- defN 80-Jan-01 00:00 fw_utils-4.2.7.dist-info/WHEEL
--rw-r--r--  2.0 unx     1928 b- defN 80-Jan-01 00:00 fw_utils-4.2.7.dist-info/METADATA
--rw-r--r--  2.0 unx     1078 b- defN 80-Jan-01 00:00 fw_utils-4.2.7.dist-info/LICENSE
-?rw-r--r--  2.0 unx     1053 b- defN 16-Jan-01 00:00 fw_utils-4.2.7.dist-info/RECORD
-14 files, 58571 bytes uncompressed, 20215 bytes compressed:  65.5%
+-rw-r--r--  2.0 unx     4382 b- defN 80-Jan-01 00:00 fw_utils/state.py
+-rw-r--r--  2.0 unx     3063 b- defN 80-Jan-01 00:00 fw_utils/testing.py
+-rw-r--r--  2.0 unx     1078 b- defN 80-Jan-01 00:00 fw_utils-4.2.8.dist-info/LICENSE
+-rw-r--r--  2.0 unx     1928 b- defN 80-Jan-01 00:00 fw_utils-4.2.8.dist-info/METADATA
+-rw-r--r--  2.0 unx       88 b- defN 80-Jan-01 00:00 fw_utils-4.2.8.dist-info/WHEEL
+?rw-r--r--  2.0 unx     1054 b- defN 16-Jan-01 00:00 fw_utils-4.2.8.dist-info/RECORD
+14 files, 59185 bytes uncompressed, 20326 bytes compressed:  65.7%
```

## zipnote {}

```diff
@@ -24,20 +24,20 @@
 
 Filename: fw_utils/state.py
 Comment: 
 
 Filename: fw_utils/testing.py
 Comment: 
 
-Filename: fw_utils-4.2.7.dist-info/WHEEL
+Filename: fw_utils-4.2.8.dist-info/LICENSE
 Comment: 
 
-Filename: fw_utils-4.2.7.dist-info/METADATA
+Filename: fw_utils-4.2.8.dist-info/METADATA
 Comment: 
 
-Filename: fw_utils-4.2.7.dist-info/LICENSE
+Filename: fw_utils-4.2.8.dist-info/WHEEL
 Comment: 
 
-Filename: fw_utils-4.2.7.dist-info/RECORD
+Filename: fw_utils-4.2.8.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## fw_utils/__init__.py

```diff
@@ -1,13 +1,58 @@
 """Flywheel utilities and common helpers."""
 from importlib.metadata import version
 
 __version__ = version(__name__)
+__all__ = [
+    "ZoneInfo",
+    "format_datetime",
+    "get_datetime",
+    "get_tzinfo",
+    "AttrDict",
+    "attrify",
+    "flatten_dotdict",
+    "get_field",
+    "inflate_dotdict",
+    "AnyFile",
+    "AnyPath",
+    "BinFile",
+    "TempDir",
+    "TempFile",
+    "fileglob",
+    "open_any",
+    "BaseFilter",
+    "ExpressionFilter",
+    "Filters",
+    "IncludeExcludeFilter",
+    "NumberFilter",
+    "SetFilter",
+    "SizeFilter",
+    "StringFilter",
+    "TimeFilter",
+    "Template",
+    "Timer",
+    "format_query_string",
+    "format_template",
+    "format_url",
+    "hrsize",
+    "hrtime",
+    "pluralize",
+    "quantify",
+    "report_progress",
+    "Pattern",
+    "parse_field_name",
+    "parse_hrsize",
+    "parse_hrtime",
+    "parse_pattern",
+    "parse_url",
+    "Cached",
+    "TempEnv",
+    "assert_like",
+]
 
-# pylint: disable=unused-import
 from .datetime import ZoneInfo, format_datetime, get_datetime, get_tzinfo
 from .dicts import AttrDict, attrify, flatten_dotdict, get_field, inflate_dotdict
 from .files import AnyFile, AnyPath, BinFile, TempDir, TempFile, fileglob, open_any
 from .filters import (
     BaseFilter,
     ExpressionFilter,
     Filters,
```

## fw_utils/files.py

```diff
@@ -54,15 +54,15 @@
         self.file_open = False
         self.localpath = None
         self.mode = mode
         mode_func = "readable" if mode == "rb" else "writable"
         if isinstance(file, (str, Path)):
             self.file_open = True
             self.localpath = str(Path(file).resolve())
-            # pylint: disable=unspecified-encoding
+
             file = t.cast(t.BinaryIO, Path(self.localpath).open(mode=mode))
         elif isinstance(file, bytes):
             file = io.BytesIO(file)
         if not hasattr(file, mode_func) or not getattr(file, mode_func)():
             raise ValueError(f"File {file!r} is not {mode_func}")
         self.file = file
         self.metapath = metapath or self.localpath
```

## fw_utils/filters.py

```diff
@@ -106,15 +106,14 @@
             exclude: List of exclude exprs - if given, none are allowed to match.
             validate: Field name validator callback.
         """
         parse = partial(parse_filter_expression, factory=factory, validate=validate)
         self.include = [parse(expr) for expr in (include or [])]
         self.exclude = [parse(expr) for expr in (exclude or [])]
 
-    # pylint: disable=arguments-differ
     def match(self, value, exclude_only: t.List[str] = None) -> bool:
         """Return whether value matches all includes but none of the excludes.
 
         If `exclude_only` is given, only evaluate the exclude filters on those.
         """
         include = self.include
         exclude = self.exclude
```

## fw_utils/formatters.py

```diff
@@ -63,15 +63,15 @@
             decimals = 0 if round(quotient) >= 10 or not round(remainder, 1) else 1
             parts.append(f"{quotient + remainder:.{decimals}f}{unit}")
         elif quotient >= 1:
             parts.append(f"{int(quotient)}{unit}")
     return " ".join(parts)
 
 
-def format_url(  # pylint: disable=too-many-arguments
+def format_url(
     *,
     scheme: str = "https",
     driver: str = None,
     username: str = None,
     password: str = None,
     host: str = "",
     port: int = None,
@@ -173,18 +173,18 @@
     def _parse(self) -> str:
         """Parse and return the f-string for the template."""
         template, pos, curly = self.template, 0, False
         fstring = ""
         regex = re.compile(
             r"(?P<field>[^/:|]+)"
             r"(?P<spec>"
-            r"(/(?P<pat>[^/]+)(/(?P<sub>[^:|]*))?)?"
-            r"(:(?P<fmt>[^|]+))?"
-            r"(\|(?P<default>.+))?"
-            r")"
+            r"((?<!\\)/(?P<pat>.+?)((?<!\\)/(?P<sub>.*?))?)?"
+            r"((?<!\\):(?P<fmt>.+?))?"
+            r"((?<!\\)\|(?P<default>.+))?"
+            r")$"
         )
         assert template, "empty template"
         assert "{}" not in template, "empty format block"
         # assume {template} is a format block if no curlies present
         if not re.search(r"(?<!\\)([{}])", template):
             template = f"{{{template}}}"  # implicit format block
         parts = [part for part in re.split(r"(?<!\\)([{}])", template) if part]
@@ -204,28 +204,33 @@
                 assert match, f"invalid format block {part!r}"
                 kwargs = match.groupdict()
                 field = kwargs.pop("field")
                 # validate field
                 field = self.validate(field) if self.validate else field
                 # validate substitution pattern
                 re.compile(kwargs["pat"] or "")
+                kwargs["pat"] = kwargs["pat"] or ""
+                kwargs["sub"] = kwargs["sub"] or ""
                 # store field, spec and dumper func for later
                 self.fields.append(field)
                 self.specs.append(kwargs.pop("spec") or "")
                 self.dumpers.append(partial(self._dump_value, **kwargs))
                 fstring += "{}"
             # literal part
             else:
                 fstring += part
             pos += len(part)
         assert not curly, f"unterminated {{ in {template!r}"
         # translate backslash-escaped curlies to f-string-style double notation
         fstring = re.sub(r"\\(\{|\})", r"\\\1\1", fstring)
         return fstring
 
+    # TODO consider supporting some bash param expansions, or making
+    # path substitutions simpler (escaping slashes is very painful...)
+    # https://wiki.bash-hackers.org/syntax/pe
     @staticmethod
     def _dump_value(
         value,
         pat: str = "",
         sub: str = "",
         fmt: str = "",
         default: str = "",
@@ -275,18 +280,17 @@
 
     if count:
         count += 1
         now = time.perf_counter()
         report()
 
 
-class Timer:  # pylint: disable=too-few-public-methods
+class Timer:
     """Timer for logging size/speed reports on file processing/transfers."""
 
-    # pylint: disable=redefined-builtin
     def __init__(self, files: int = 0, bytes: int = 0) -> None:
         """Init timer w/ current timestamp and the no. of files/bytes."""
         self.start = time.perf_counter()
         self.files = files
         self.bytes = bytes
 
     def report(self) -> str:
```

## fw_utils/parsers.py

```diff
@@ -86,21 +86,21 @@
     *,
     aliases: t.Dict[str, str] = None,
     allowed: t.List[str] = None,
 ) -> str:
     """Return canonic field from a partial/abbreviated one using hints/aliases.
 
     Args:
-        aliases Optional {pattern: replacement} mapping to enable shorthands.
+        field: The input field name to validate / resolve / canonize.
+        aliases: Optional {pattern: replacement} mapping to enable shorthands.
         allowed: Optional list of allowed fields (eg. ["project.label"]).
 
     Returns:
         The validated, canonic (potentially expanded) field.
     """
-    # pylint: disable=too-many-branches
     # replace aliases (while True allows prj -> project -> project.label)
     aliases = aliases or {}
     for _ in range(len(aliases)):
         field_ = replace(field, aliases)
         if field_ == field:
             break
         field = field_
@@ -209,15 +209,15 @@
             field = id_to_str(field)
             parser = self.loaders.get(field)
             if parser:
                 value = parser(value)
             data[field] = value
         return AttrDict.from_flat(data)
 
-    def _parse(self) -> t.Pattern:  # pylint: disable=too-many-branches, too-many-locals
+    def _parse(self) -> t.Pattern:  # noqa PLR0912
         """Parse and return the compiled regex for the pattern."""
         pattern, pos, curly = self.pattern, 0, False
         self.canonic, self.fields, regex, opts, flags, raw = "", set(), "", "", 0, False
         assert pattern, "empty pattern"
         assert "{}" not in pattern, "empty capture group"
         # parse and strip pattern!options (r=raw-regex, i=case-insensitive)
         match = re.match(r".*?(?<!\\)!(?P<opts>[a-z]+)$", pattern)
```

## fw_utils/state.py

```diff
@@ -10,16 +10,14 @@
 
 T = t.TypeVar("T")
 
 
 class Cached(t.Generic[T]):
     """Descriptor for caching attributes and injecting dependencies."""
 
-    # pylint: disable=too-many-instance-attributes
-
     def __init__(
         self,
         func: t.Callable[..., T],
         thread_safe: bool = True,
         fork_safe: bool = False,
         expire_in: int = 0,
     ) -> None:
```

## fw_utils/testing.py

```diff
@@ -3,37 +3,35 @@
 from collections.abc import Callable
 from functools import singledispatch
 
 __all__ = ["assert_like"]
 
 
 @singledispatch
-def assert_like(  # pylint: disable=unused-argument
-    expected, got, allow_extra=True, loc=""
-) -> None:
+def assert_like(expected, got, allow_extra=True, loc="") -> None:
     """Check whether an object is like the expected.
 
     Supported values:
     * dict: see 'assert_like_dict'
     * list: see 'assert_like_list'
     * regex pattern: see 'assert_like_pattern'
     * callable: see 'assert_like_function'
     * everything else: simply compared using '=='
     """
-    __tracebackhide__ = True  # pylint: disable=unused-variable
+    __tracebackhide__ = True
     assert expected == got, f"{loc}: {got!r} != {expected!r}"
 
 
 @assert_like.register
 def assert_like_dict(expected: dict, got, allow_extra=True, loc="") -> None:
     """Check whether a dictionary is like the expected.
 
     'allow_extra': enable extra keys in the dictionary or not
     """
-    __tracebackhide__ = True  # pylint: disable=unused-variable
+    __tracebackhide__ = True
     assert isinstance(got, dict), f"{loc} {got.__class__.__name__} != dict"
     expected_keys = set(expected)
     got_keys = set(got)
     missing_keys = expected_keys - got_keys
     assert not missing_keys, f"{loc}: missing_keys={missing_keys}"
     if not allow_extra:
         extra_keys = got_keys - expected_keys
@@ -44,15 +42,15 @@
 
 @assert_like.register
 def assert_like_list(expected: list, got, loc="", **kwargs) -> None:
     """Check whether a list is like the expected.
 
     Ellipsis can be used for partial matching ([..., 2] == [1, 2]).
     """
-    __tracebackhide__ = True  # pylint: disable=unused-variable
+    __tracebackhide__ = True
     assert isinstance(got, list), f"{loc} {got.__class__.__name__} != list"
     got_iter = iter(got)
     ellipsis = False
     for index, value in enumerate(expected):
         loc_ = f"{loc}[{index}]"
         if value is Ellipsis:
             ellipsis = True
@@ -72,20 +70,20 @@
         extra = list(got_iter)
         assert not extra, f"{loc}: unexpected items: extra_items={extra}"
 
 
 @assert_like.register
 def assert_like_pattern(expected: re.Pattern, got, loc="", **_) -> None:
     """Check whether a string matches the given pattern."""
-    __tracebackhide__ = True  # pylint: disable=unused-variable
+    __tracebackhide__ = True
     assert expected.search(got), f"{loc}: {got} !~ {expected.pattern}"
 
 
 @assert_like.register
 def assert_like_function(expected: Callable, got, loc="", **_) -> None:
     """Check whether an object is the expected using the callback function."""
-    __tracebackhide__ = True  # pylint: disable=unused-variable
+    __tracebackhide__ = True
     try:
         assert expected(got)
     except Exception as exc:
         ctx = None if isinstance(exc, AssertionError) else exc
         raise AssertionError(f"{loc}: {got} validation failed ({exc})") from ctx
```

## Comparing `fw_utils-4.2.7.dist-info/METADATA` & `fw_utils-4.2.8.dist-info/METADATA`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fw-utils
-Version: 4.2.7
+Version: 4.2.8
 Summary: Common Flywheel helper utilities.
 Home-page: https://gitlab.com/flywheel-io/tools/lib/fw-utils
 License: MIT
 Keywords: Flywheel,helper,utility
 Author: Flywheel
 Author-email: support@flywheel.io
 Requires-Python: >=3.8,<4.0
```

## Comparing `fw_utils-4.2.7.dist-info/LICENSE` & `fw_utils-4.2.8.dist-info/LICENSE`

 * *Files identical despite different names*

