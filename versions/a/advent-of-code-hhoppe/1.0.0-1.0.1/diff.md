# Comparing `tmp/advent-of-code-hhoppe-1.0.0.tar.gz` & `tmp/advent-of-code-hhoppe-1.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "advent-of-code-hhoppe-1.0.0.tar", last modified: Wed Apr  5 17:17:05 2023, max compression
+gzip compressed data, was "advent-of-code-hhoppe-1.0.1.tar", last modified: Fri Apr  7 14:04:12 2023, max compression
```

## Comparing `advent-of-code-hhoppe-1.0.0.tar` & `advent-of-code-hhoppe-1.0.1.tar`

### file list

```diff
@@ -1,7 +1,7 @@
--rw-r--r--   0        0        0     1069 2023-04-05 17:16:55.866562 advent-of-code-hhoppe-1.0.0/LICENSE
--rw-r--r--   0        0        0     2367 2023-04-05 17:16:55.866562 advent-of-code-hhoppe-1.0.0/README.md
--rw-r--r--   0        0        0     7670 2023-04-05 17:16:55.866562 advent-of-code-hhoppe-1.0.0/advent_of_code_hhoppe/__init__.py
--rw-r--r--   0        0        0        0 2023-04-05 17:16:55.866562 advent-of-code-hhoppe-1.0.0/advent_of_code_hhoppe/py.typed
--rw-r--r--   0        0        0      907 2023-04-05 17:16:55.866562 advent-of-code-hhoppe-1.0.0/advent_of_code_hhoppe/setup.cfg
--rw-r--r--   0        0        0     2017 2023-04-05 17:16:55.866562 advent-of-code-hhoppe-1.0.0/pyproject.toml
--rw-r--r--   0        0        0     2940 1970-01-01 00:00:00.000000 advent-of-code-hhoppe-1.0.0/PKG-INFO
+-rw-r--r--   0        0        0     1069 2023-04-07 14:04:01.110678 advent-of-code-hhoppe-1.0.1/LICENSE
+-rw-r--r--   0        0        0     2367 2023-04-07 14:04:01.110678 advent-of-code-hhoppe-1.0.1/README.md
+-rw-r--r--   0        0        0     7737 2023-04-07 14:04:01.110678 advent-of-code-hhoppe-1.0.1/advent_of_code_hhoppe/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-07 14:04:01.110678 advent-of-code-hhoppe-1.0.1/advent_of_code_hhoppe/py.typed
+-rw-r--r--   0        0        0      907 2023-04-07 14:04:01.110678 advent-of-code-hhoppe-1.0.1/advent_of_code_hhoppe/setup.cfg
+-rw-r--r--   0        0        0     2017 2023-04-07 14:04:01.110678 advent-of-code-hhoppe-1.0.1/pyproject.toml
+-rw-r--r--   0        0        0     2940 1970-01-01 00:00:00.000000 advent-of-code-hhoppe-1.0.1/PKG-INFO
```

### Comparing `advent-of-code-hhoppe-1.0.0/LICENSE` & `advent-of-code-hhoppe-1.0.1/LICENSE`

 * *Files identical despite different names*

### Comparing `advent-of-code-hhoppe-1.0.0/README.md` & `advent-of-code-hhoppe-1.0.1/README.md`

 * *Files identical despite different names*

### Comparing `advent-of-code-hhoppe-1.0.0/advent_of_code_hhoppe/__init__.py` & `advent-of-code-hhoppe-1.0.1/advent_of_code_hhoppe/__init__.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 #!/usr/bin/env python3
 """Library for Advent of Code -- Hugues Hoppe."""
 
 from __future__ import annotations
 
 __docformat__ = 'google'
-__version__ = '1.0.0'
+__version__ = '1.0.1'
 __version_info__ = tuple(int(num) for num in __version__.split('.'))
 
 from collections.abc import Callable
 import contextlib
 import dataclasses
 import numbers
 import pathlib
@@ -109,14 +109,16 @@
       with contextlib.suppress(urllib.error.HTTPError, FileNotFoundError):
         self.input = _read_contents(url).decode()
     if not self.input and self.advent.use_aocd:
       import aocd  # pylint: disable=import-error, import-outside-toplevel
 
       puz = aocd.models.Puzzle(year=self.advent.year, day=self.day)
       self.input = puz.input_data
+      if not self.input.endswith('\n'):
+        self.input += '\n'
     if not self.input:
       raise ValueError('The puzzle input cannot be determined.')
     for part in (1, 2):
       puzzle_part = self.parts[part] = PuzzlePart(self.advent, self.day, part)
       if self.advent.answer_url:
         url = self.advent.answer_url.format(
             year=self.advent.year, day=self.day, part=part, part_letter='ab'[part - 1]
```

### Comparing `advent-of-code-hhoppe-1.0.0/advent_of_code_hhoppe/setup.cfg` & `advent-of-code-hhoppe-1.0.1/advent_of_code_hhoppe/setup.cfg`

 * *Files identical despite different names*

### Comparing `advent-of-code-hhoppe-1.0.0/pyproject.toml` & `advent-of-code-hhoppe-1.0.1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `advent-of-code-hhoppe-1.0.0/PKG-INFO` & `advent-of-code-hhoppe-1.0.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: advent-of-code-hhoppe
-Version: 1.0.0
+Version: 1.0.1
 Summary: Library for Advent of Code -- Hugues Hoppe.
 Keywords: 
 Author-email: Hugues Hoppe <hhoppe@gmail.com>
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

