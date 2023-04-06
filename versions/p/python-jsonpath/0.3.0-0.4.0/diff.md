# Comparing `tmp/python_jsonpath-0.3.0.tar.gz` & `tmp/python_jsonpath-0.4.0.tar.gz`

## Comparing `python_jsonpath-0.3.0.tar` & `python_jsonpath-0.4.0.tar`

### file list

```diff
@@ -1,1509 +1,1522 @@
--rw-r--r--   0        0        0     1124 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/CHANGELOG.md
--rw-r--r--   0        0        0     1234 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath.bnf
--rw-r--r--   0        0        0     1559 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/mkdocs.yml
--rw-r--r--   0        0        0      413 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.github/workflows/lint.yaml
--rw-r--r--   0        0        0      807 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.github/workflows/tests.yaml
--rw-r--r--   0        0        0      417 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.github/workflows/typing.yaml
--rw-r--r--   0        0        0       34 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/.gitignore
--rw-r--r--   0        0        0      190 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/CACHEDIR.TAG
--rw-r--r--   0        0        0        2 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/@plugins_snapshot.json
--rw-r--r--   0        0        0     8535 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/__future__.data.json
--rw-r--r--   0        0        0     1713 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/__future__.meta.json
--rw-r--r--   0        0        0   193712 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_ast.data.json
--rw-r--r--   0        0        0     1801 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_ast.meta.json
--rw-r--r--   0        0        0    47115 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_bisect.data.json
--rw-r--r--   0        0        0     1738 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_bisect.meta.json
--rw-r--r--   0        0        0    57332 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_codecs.data.json
--rw-r--r--   0        0        0     1847 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_codecs.meta.json
--rw-r--r--   0        0        0    19805 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_collections_abc.data.json
--rw-r--r--   0        0        0     1755 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_collections_abc.meta.json
--rw-r--r--   0        0        0     3218 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_ctypes.data.json
--rw-r--r--   0        0        0     1757 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_ctypes.meta.json
--rw-r--r--   0        0        0   186645 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_decimal.data.json
--rw-r--r--   0        0        0     1802 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_decimal.meta.json
--rw-r--r--   0        0        0   122132 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_operator.data.json
--rw-r--r--   0        0        0     1769 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_operator.meta.json
--rw-r--r--   0        0        0   148486 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_socket.data.json
--rw-r--r--   0        0        0     1831 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_socket.meta.json
--rw-r--r--   0        0        0    21638 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_stat.data.json
--rw-r--r--   0        0        0     1718 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_stat.meta.json
--rw-r--r--   0        0        0    26002 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_thread.data.json
--rw-r--r--   0        0        0     1799 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_thread.meta.json
--rw-r--r--   0        0        0     8915 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_tracemalloc.data.json
--rw-r--r--   0        0        0     1770 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_tracemalloc.meta.json
--rw-r--r--   0        0        0    14348 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_warnings.data.json
--rw-r--r--   0        0        0     1684 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_warnings.meta.json
--rw-r--r--   0        0        0    30014 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_weakref.data.json
--rw-r--r--   0        0        0     1783 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_weakref.meta.json
--rw-r--r--   0        0        0    55254 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_weakrefset.data.json
--rw-r--r--   0        0        0     1789 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_weakrefset.meta.json
--rw-r--r--   0        0        0    22400 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/abc.data.json
--rw-r--r--   0        0        0     1743 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/abc.meta.json
--rw-r--r--   0        0        0   165861 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/argparse.data.json
--rw-r--r--   0        0        0     1846 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/argparse.meta.json
--rw-r--r--   0        0        0    66417 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/array.data.json
--rw-r--r--   0        0        0     1810 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/array.meta.json
--rw-r--r--   0        0        0   149485 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/ast.data.json
--rw-r--r--   0        0        0     1850 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/ast.meta.json
--rw-r--r--   0        0        0     8975 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/atexit.data.json
--rw-r--r--   0        0        0     1729 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/atexit.meta.json
--rw-r--r--   0        0        0    53914 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/bdb.data.json
--rw-r--r--   0        0        0     1772 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/bdb.meta.json
--rw-r--r--   0        0        0    12244 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/bisect.data.json
--rw-r--r--   0        0        0     1714 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/bisect.meta.json
--rw-r--r--   0        0        0  1141249 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/builtins.data.json
--rw-r--r--   0        0        0     1907 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/builtins.meta.json
--rw-r--r--   0        0        0    22205 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/cmd.data.json
--rw-r--r--   0        0        0     1724 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/cmd.meta.json
--rw-r--r--   0        0        0   134253 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/codecs.data.json
--rw-r--r--   0        0        0     1861 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/codecs.meta.json
--rw-r--r--   0        0        0    12403 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/compliance.data.json
--rw-r--r--   0        0        0     1983 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/compliance.meta.json
--rw-r--r--   0        0        0    15816 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/consensus.data.json
--rw-r--r--   0        0        0     1940 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/consensus.meta.json
--rw-r--r--   0        0        0   113711 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/contextlib.data.json
--rw-r--r--   0        0        0     1785 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/contextlib.meta.json
--rw-r--r--   0        0        0    41360 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/contextvars.data.json
--rw-r--r--   0        0        0     1789 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/contextvars.meta.json
--rw-r--r--   0        0        0     5983 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/copy.data.json
--rw-r--r--   0        0        0     1673 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/copy.meta.json
--rw-r--r--   0        0        0    13020 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/copyreg.data.json
--rw-r--r--   0        0        0     1751 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/copyreg.meta.json
--rw-r--r--   0        0        0    63291 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/dataclasses.data.json
--rw-r--r--   0        0        0     1803 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/dataclasses.meta.json
--rw-r--r--   0        0        0   154597 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/datetime.data.json
--rw-r--r--   0        0        0     1757 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/datetime.meta.json
--rw-r--r--   0        0        0     5339 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/decimal.data.json
--rw-r--r--   0        0        0     1698 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/decimal.meta.json
--rw-r--r--   0        0        0     2117 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/dev.data.json
--rw-r--r--   0        0        0     1671 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/dev.meta.json
--rw-r--r--   0        0        0    63798 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/difflib.data.json
--rw-r--r--   0        0        0     1754 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/difflib.meta.json
--rw-r--r--   0        0        0    44123 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/dis.data.json
--rw-r--r--   0        0        0     1790 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/dis.meta.json
--rw-r--r--   0        0        0    76249 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/doctest.data.json
--rw-r--r--   0        0        0     1835 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/doctest.meta.json
--rw-r--r--   0        0        0    66880 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/enum.data.json
--rw-r--r--   0        0        0     1775 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/enum.meta.json
--rw-r--r--   0        0        0    29939 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/errno.data.json
--rw-r--r--   0        0        0     1716 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/errno.meta.json
--rw-r--r--   0        0        0     6704 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/fnmatch.data.json
--rw-r--r--   0        0        0     1704 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/fnmatch.meta.json
--rw-r--r--   0        0        0   139324 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/functools.data.json
--rw-r--r--   0        0        0     1784 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/functools.meta.json
--rw-r--r--   0        0        0    17520 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/gc.data.json
--rw-r--r--   0        0        0     1756 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/gc.meta.json
--rw-r--r--   0        0        0    24440 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/genericpath.data.json
--rw-r--r--   0        0        0     1772 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/genericpath.meta.json
--rw-r--r--   0        0        0     4120 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/getpass.data.json
--rw-r--r--   0        0        0     1679 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/getpass.meta.json
--rw-r--r--   0        0        0    58379 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/gettext.data.json
--rw-r--r--   0        0        0     1778 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/gettext.meta.json
--rw-r--r--   0        0        0    10325 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/glob.data.json
--rw-r--r--   0        0        0     1732 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/glob.meta.json
--rw-r--r--   0        0        0   370622 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/inspect.data.json
--rw-r--r--   0        0        0     1834 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/inspect.meta.json
--rw-r--r--   0        0        0    93299 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/io.data.json
--rw-r--r--   0        0        0     1866 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/io.meta.json
--rw-r--r--   0        0        0   292389 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/itertools.data.json
--rw-r--r--   0        0        0     1786 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/itertools.meta.json
--rw-r--r--   0        0        0     7024 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/marshal.data.json
--rw-r--r--   0        0        0     1807 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/marshal.meta.json
--rw-r--r--   0        0        0    56214 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/math.data.json
--rw-r--r--   0        0        0     1760 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/math.meta.json
--rw-r--r--   0        0        0    31546 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/mmap.data.json
--rw-r--r--   0        0        0     1809 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/mmap.meta.json
--rw-r--r--   0        0        0    86304 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/numbers.data.json
--rw-r--r--   0        0        0     1679 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/numbers.meta.json
--rw-r--r--   0        0        0     6702 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/opcode.data.json
--rw-r--r--   0        0        0     1740 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/opcode.meta.json
--rw-r--r--   0        0        0    51078 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/operator.data.json
--rw-r--r--   0        0        0     1764 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/operator.meta.json
--rw-r--r--   0        0        0    96614 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/pathlib.data.json
--rw-r--r--   0        0        0     1875 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/pathlib.meta.json
--rw-r--r--   0        0        0   102193 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/pdb.data.json
--rw-r--r--   0        0        0     1862 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/pdb.meta.json
--rw-r--r--   0        0        0    48580 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/pickle.data.json
--rw-r--r--   0        0        0     1811 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/pickle.meta.json
--rw-r--r--   0        0        0    34256 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/pkgutil.data.json
--rw-r--r--   0        0        0     1781 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/pkgutil.meta.json
--rw-r--r--   0        0        0    38196 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/platform.data.json
--rw-r--r--   0        0        0     1716 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/platform.meta.json
--rw-r--r--   0        0        0    82148 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/posixpath.data.json
--rw-r--r--   0        0        0     1805 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/posixpath.meta.json
--rw-r--r--   0        0        0    13186 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/pprint.data.json
--rw-r--r--   0        0        0     1712 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/pprint.meta.json
--rw-r--r--   0        0        0    33321 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/queue.data.json
--rw-r--r--   0        0        0     1744 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/queue.meta.json
--rw-r--r--   0        0        0   182961 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/re.data.json
--rw-r--r--   0        0        0     1897 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/re.meta.json
--rw-r--r--   0        0        0    18012 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/reprlib.data.json
--rw-r--r--   0        0        0     1768 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/reprlib.meta.json
--rw-r--r--   0        0        0    65874 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/selectors.data.json
--rw-r--r--   0        0        0     1833 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/selectors.meta.json
--rw-r--r--   0        0        0    17830 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/shlex.data.json
--rw-r--r--   0        0        0     1762 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/shlex.meta.json
--rw-r--r--   0        0        0    77644 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/shutil.data.json
--rw-r--r--   0        0        0     1776 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/shutil.meta.json
--rw-r--r--   0        0        0    53861 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/signal.data.json
--rw-r--r--   0        0        0     1792 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/signal.meta.json
--rw-r--r--   0        0        0   125447 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/socket.data.json
--rw-r--r--   0        0        0     1884 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/socket.meta.json
--rw-r--r--   0        0        0    15243 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/sre_compile.data.json
--rw-r--r--   0        0        0     1741 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/sre_compile.meta.json
--rw-r--r--   0        0        0    30297 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/sre_constants.data.json
--rw-r--r--   0        0        0     1753 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/sre_constants.meta.json
--rw-r--r--   0        0        0    53747 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/sre_parse.data.json
--rw-r--r--   0        0        0     1805 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/sre_parse.meta.json
--rw-r--r--   0        0        0   205017 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/ssl.data.json
--rw-r--r--   0        0        0     1886 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/ssl.meta.json
--rw-r--r--   0        0        0     7133 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/stat.data.json
--rw-r--r--   0        0        0     1688 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/stat.meta.json
--rw-r--r--   0        0        0    28945 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/string.data.json
--rw-r--r--   0        0        0     1790 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/string.meta.json
--rw-r--r--   0        0        0    16774 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/struct.data.json
--rw-r--r--   0        0        0     1787 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/struct.meta.json
--rw-r--r--   0        0        0   173213 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/subprocess.data.json
--rw-r--r--   0        0        0     1865 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/subprocess.meta.json
--rw-r--r--   0        0        0   152190 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/sys.data.json
--rw-r--r--   0        0        0     1844 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/sys.meta.json
--rw-r--r--   0        0        0    15836 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/sysconfig.data.json
--rw-r--r--   0        0        0     1745 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/sysconfig.meta.json
--rw-r--r--   0        0        0   130364 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tempfile.data.json
--rw-r--r--   0        0        0     1809 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tempfile.meta.json
--rw-r--r--   0        0        0    16115 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/test_consensus.data.json
--rw-r--r--   0        0        0     2152 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/test_consensus.meta.json
--rw-r--r--   0        0        0    21205 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/textwrap.data.json
--rw-r--r--   0        0        0     1720 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/textwrap.meta.json
--rw-r--r--   0        0        0    70568 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/threading.data.json
--rw-r--r--   0        0        0     1775 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/threading.meta.json
--rw-r--r--   0        0        0    47500 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/time.data.json
--rw-r--r--   0        0        0     1734 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/time.meta.json
--rw-r--r--   0        0        0    16377 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/token.data.json
--rw-r--r--   0        0        0     1711 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/token.meta.json
--rw-r--r--   0        0        0    53730 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tokenize.data.json
--rw-r--r--   0        0        0     1807 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tokenize.meta.json
--rw-r--r--   0        0        0    56302 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/traceback.data.json
--rw-r--r--   0        0        0     1784 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/traceback.meta.json
--rw-r--r--   0        0        0    53926 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tracemalloc.data.json
--rw-r--r--   0        0        0     1796 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tracemalloc.meta.json
--rw-r--r--   0        0        0   248547 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/types.data.json
--rw-r--r--   0        0        0     1816 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/types.meta.json
--rw-r--r--   0        0        0   444992 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/typing.data.json
--rw-r--r--   0        0        0     1882 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/typing.meta.json
--rw-r--r--   0        0        0    73995 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/typing_extensions.data.json
--rw-r--r--   0        0        0     1806 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/typing_extensions.meta.json
--rw-r--r--   0        0        0    46044 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unicodedata.data.json
--rw-r--r--   0        0        0     1748 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unicodedata.meta.json
--rw-r--r--   0        0        0    36731 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/uuid.data.json
--rw-r--r--   0        0        0     1814 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/uuid.meta.json
--rw-r--r--   0        0        0    24199 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/warnings.data.json
--rw-r--r--   0        0        0     1802 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/warnings.meta.json
--rw-r--r--   0        0        0   156354 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/weakref.data.json
--rw-r--r--   0        0        0     1808 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/weakref.meta.json
--rw-r--r--   0        0        0     2310 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/__init__.data.json
--rw-r--r--   0        0        0     1693 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/__init__.meta.json
--rw-r--r--   0        0        0     6551 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_argcomplete.data.json
--rw-r--r--   0        0        0     1868 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_argcomplete.meta.json
--rw-r--r--   0        0        0     2910 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_version.data.json
--rw-r--r--   0        0        0     1676 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_version.meta.json
--rw-r--r--   0        0        0    54695 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/cacheprovider.data.json
--rw-r--r--   0        0        0     2614 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/cacheprovider.meta.json
--rw-r--r--   0        0        0   134350 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/capture.data.json
--rw-r--r--   0        0        0     2152 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/capture.meta.json
--rw-r--r--   0        0        0    34465 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/compat.data.json
--rw-r--r--   0        0        0     2085 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/compat.meta.json
--rw-r--r--   0        0        0    34297 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/debugging.data.json
--rw-r--r--   0        0        0     2362 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/debugging.meta.json
--rw-r--r--   0        0        0     8472 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/deprecated.data.json
--rw-r--r--   0        0        0     1752 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/deprecated.meta.json
--rw-r--r--   0        0        0    55831 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/doctest.data.json
--rw-r--r--   0        0        0     2502 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/doctest.meta.json
--rw-r--r--   0        0        0   191946 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/fixtures.data.json
--rw-r--r--   0        0        0     2638 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/fixtures.meta.json
--rw-r--r--   0        0        0     3599 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/freeze_support.data.json
--rw-r--r--   0        0        0     1885 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/freeze_support.meta.json
--rw-r--r--   0        0        0    10149 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/helpconfig.data.json
--rw-r--r--   0        0        0     2023 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/helpconfig.meta.json
--rw-r--r--   0        0        0    63301 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/hookspec.data.json
--rw-r--r--   0        0        0     2269 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/hookspec.meta.json
--rw-r--r--   0        0        0    75498 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/legacypath.data.json
--rw-r--r--   0        0        0     2270 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/legacypath.meta.json
--rw-r--r--   0        0        0    81215 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/logging.data.json
--rw-r--r--   0        0        0     2418 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/logging.meta.json
--rw-r--r--   0        0        0    57129 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/main.data.json
--rw-r--r--   0        0        0     2512 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/main.meta.json
--rw-r--r--   0        0        0    27956 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/monkeypatch.data.json
--rw-r--r--   0        0        0     2086 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/monkeypatch.meta.json
--rw-r--r--   0        0        0    62800 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/nodes.data.json
--rw-r--r--   0        0        0     2329 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/nodes.meta.json
--rw-r--r--   0        0        0    32446 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/outcomes.data.json
--rw-r--r--   0        0        0     2068 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/outcomes.meta.json
--rw-r--r--   0        0        0    36764 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/pathlib.data.json
--rw-r--r--   0        0        0     2308 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/pathlib.meta.json
--rw-r--r--   0        0        0   142763 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/pytester.data.json
--rw-r--r--   0        0        0     2846 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/pytester.meta.json
--rw-r--r--   0        0        0     5212 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/pytester_assertions.data.json
--rw-r--r--   0        0        0     1724 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/pytester_assertions.meta.json
--rw-r--r--   0        0        0   146190 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/python.data.json
--rw-r--r--   0        0        0     2713 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/python.meta.json
--rw-r--r--   0        0        0    55712 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/python_api.data.json
--rw-r--r--   0        0        0     2158 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/python_api.meta.json
--rw-r--r--   0        0        0    33297 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/recwarn.data.json
--rw-r--r--   0        0        0     2036 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/recwarn.meta.json
--rw-r--r--   0        0        0    53707 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/reports.data.json
--rw-r--r--   0        0        0     2190 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/reports.meta.json
--rw-r--r--   0        0        0    55987 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/runner.data.json
--rw-r--r--   0        0        0     2395 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/runner.meta.json
--rw-r--r--   0        0        0    12375 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/scope.data.json
--rw-r--r--   0        0        0     1763 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/scope.meta.json
--rw-r--r--   0        0        0    15317 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/stash.data.json
--rw-r--r--   0        0        0     1670 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/stash.meta.json
--rw-r--r--   0        0        0   109160 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/terminal.data.json
--rw-r--r--   0        0        0     2675 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/terminal.meta.json
--rw-r--r--   0        0        0     2132 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/timing.data.json
--rw-r--r--   0        0        0     1686 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/timing.meta.json
--rw-r--r--   0        0        0    26596 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/tmpdir.data.json
--rw-r--r--   0        0        0     2134 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/tmpdir.meta.json
--rw-r--r--   0        0        0    36750 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/warning_types.data.json
--rw-r--r--   0        0        0     1821 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/warning_types.meta.json
--rw-r--r--   0        0        0    13986 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/warnings.data.json
--rw-r--r--   0        0        0     2160 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/warnings.meta.json
--rw-r--r--   0        0        0     3113 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_code/__init__.data.json
--rw-r--r--   0        0        0     1737 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_code/__init__.meta.json
--rw-r--r--   0        0        0   220670 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_code/code.data.json
--rw-r--r--   0        0        0     2321 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_code/code.meta.json
--rw-r--r--   0        0        0    20336 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_code/source.data.json
--rw-r--r--   0        0        0     1964 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_code/source.meta.json
--rw-r--r--   0        0        0     2386 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/__init__.data.json
--rw-r--r--   0        0        0     1711 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/__init__.meta.json
--rw-r--r--   0        0        0    13443 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/saferepr.data.json
--rw-r--r--   0        0        0     1739 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/saferepr.meta.json
--rw-r--r--   0        0        0    17507 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/terminalwriter.data.json
--rw-r--r--   0        0        0     2073 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/terminalwriter.meta.json
--rw-r--r--   0        0        0     3326 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/wcwidth.data.json
--rw-r--r--   0        0        0     1724 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/wcwidth.meta.json
--rw-r--r--   0        0        0    13939 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/__init__.data.json
--rw-r--r--   0        0        0     2142 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/__init__.meta.json
--rw-r--r--   0        0        0    64849 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/rewrite.data.json
--rw-r--r--   0        0        0     2563 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/rewrite.meta.json
--rw-r--r--   0        0        0     6505 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/truncate.data.json
--rw-r--r--   0        0        0     1890 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/truncate.meta.json
--rw-r--r--   0        0        0    25159 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/util.data.json
--rw-r--r--   0        0        0     2172 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/util.meta.json
--rw-r--r--   0        0        0   117357 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/__init__.data.json
--rw-r--r--   0        0        0     3075 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/__init__.meta.json
--rw-r--r--   0        0        0    43203 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/argparsing.data.json
--rw-r--r--   0        0        0     2209 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/argparsing.meta.json
--rw-r--r--   0        0        0     5229 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/compat.data.json
--rw-r--r--   0        0        0     1902 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/compat.meta.json
--rw-r--r--   0        0        0     3322 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/exceptions.data.json
--rw-r--r--   0        0        0     1718 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/exceptions.meta.json
--rw-r--r--   0        0        0    10905 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/findpaths.data.json
--rw-r--r--   0        0        0     2093 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/findpaths.meta.json
--rw-r--r--   0        0        0    38199 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/mark/__init__.data.json
--rw-r--r--   0        0        0     2184 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/mark/__init__.meta.json
--rw-r--r--   0        0        0    39511 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/mark/expression.data.json
--rw-r--r--   0        0        0     1827 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/mark/expression.meta.json
--rw-r--r--   0        0        0   138467 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/mark/structures.data.json
--rw-r--r--   0        0        0     2271 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/mark/structures.meta.json
--rw-r--r--   0        0        0    97015 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_typeshed/__init__.data.json
--rw-r--r--   0        0        0     1879 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/_typeshed/__init__.meta.json
--rw-r--r--   0        0        0    11611 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/__init__.data.json
--rw-r--r--   0        0        0     2123 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/__init__.meta.json
--rw-r--r--   0        0        0   108565 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/base_events.data.json
--rw-r--r--   0        0        0     2070 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/base_events.meta.json
--rw-r--r--   0        0        0    27668 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/coroutines.data.json
--rw-r--r--   0        0        0     1788 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/coroutines.meta.json
--rw-r--r--   0        0        0   210033 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/events.data.json
--rw-r--r--   0        0        0     2108 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/events.meta.json
--rw-r--r--   0        0        0     9805 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/exceptions.data.json
--rw-r--r--   0        0        0     1737 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/exceptions.meta.json
--rw-r--r--   0        0        0    40154 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/futures.data.json
--rw-r--r--   0        0        0     1928 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/futures.meta.json
--rw-r--r--   0        0        0    29214 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/locks.data.json
--rw-r--r--   0        0        0     1879 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/locks.meta.json
--rw-r--r--   0        0        0    18741 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/protocols.data.json
--rw-r--r--   0        0        0     1831 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/protocols.meta.json
--rw-r--r--   0        0        0    25228 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/queues.data.json
--rw-r--r--   0        0        0     1767 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/queues.meta.json
--rw-r--r--   0        0        0     5102 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/runners.data.json
--rw-r--r--   0        0        0     1826 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/runners.meta.json
--rw-r--r--   0        0        0     4174 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/selector_events.data.json
--rw-r--r--   0        0        0     1805 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/selector_events.meta.json
--rw-r--r--   0        0        0    37974 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/streams.data.json
--rw-r--r--   0        0        0     1937 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/streams.meta.json
--rw-r--r--   0        0        0    26112 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/subprocess.data.json
--rw-r--r--   0        0        0     1947 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/subprocess.meta.json
--rw-r--r--   0        0        0   109223 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/tasks.data.json
--rw-r--r--   0        0        0     1928 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/tasks.meta.json
--rw-r--r--   0        0        0     6126 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/threads.data.json
--rw-r--r--   0        0        0     1747 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/threads.meta.json
--rw-r--r--   0        0        0    29802 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/transports.data.json
--rw-r--r--   0        0        0     1794 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/transports.meta.json
--rw-r--r--   0        0        0    63978 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/unix_events.data.json
--rw-r--r--   0        0        0     1912 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/unix_events.meta.json
--rw-r--r--   0        0        0   223623 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/__init__.data.json
--rw-r--r--   0        0        0     1920 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/__init__.meta.json
--rw-r--r--   0        0        0     4322 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/_cmp.data.json
--rw-r--r--   0        0        0     1662 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/_cmp.meta.json
--rw-r--r--   0        0        0     3313 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/_typing_compat.data.json
--rw-r--r--   0        0        0     1682 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/_typing_compat.meta.json
--rw-r--r--   0        0        0     7639 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/_version_info.data.json
--rw-r--r--   0        0        0     1681 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/_version_info.meta.json
--rw-r--r--   0        0        0     9100 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/converters.data.json
--rw-r--r--   0        0        0     1688 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/converters.meta.json
--rw-r--r--   0        0        0    11101 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/exceptions.data.json
--rw-r--r--   0        0        0     1674 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/exceptions.meta.json
--rw-r--r--   0        0        0     3906 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/filters.data.json
--rw-r--r--   0        0        0     1682 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/filters.meta.json
--rw-r--r--   0        0        0     8438 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/setters.data.json
--rw-r--r--   0        0        0     1682 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/setters.meta.json
--rw-r--r--   0        0        0    45673 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/validators.data.json
--rw-r--r--   0        0        0     1724 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/attr/validators.meta.json
--rw-r--r--   0        0        0   446306 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/collections/__init__.data.json
--rw-r--r--   0        0        0     1890 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/collections/__init__.meta.json
--rw-r--r--   0        0        0     4080 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/collections/abc.data.json
--rw-r--r--   0        0        0     1721 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/collections/abc.meta.json
--rw-r--r--   0        0        0     1703 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/__init__.data.json
--rw-r--r--   0        0        0     1693 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/__init__.meta.json
--rw-r--r--   0        0        0     4944 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/__init__.data.json
--rw-r--r--   0        0        0     1852 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/__init__.meta.json
--rw-r--r--   0        0        0    65942 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/_base.data.json
--rw-r--r--   0        0        0     1851 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/_base.meta.json
--rw-r--r--   0        0        0    65238 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/process.data.json
--rw-r--r--   0        0        0     2095 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/process.meta.json
--rw-r--r--   0        0        0    23847 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/thread.data.json
--rw-r--r--   0        0        0     1896 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/thread.meta.json
--rw-r--r--   0        0        0   140979 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/ctypes/__init__.data.json
--rw-r--r--   0        0        0     1853 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/ctypes/__init__.meta.json
--rw-r--r--   0        0        0     8166 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/email/__init__.data.json
--rw-r--r--   0        0        0     1782 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/email/__init__.meta.json
--rw-r--r--   0        0        0    13318 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/email/charset.data.json
--rw-r--r--   0        0        0     1718 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/email/charset.meta.json
--rw-r--r--   0        0        0     7940 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/email/contentmanager.data.json
--rw-r--r--   0        0        0     1753 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/email/contentmanager.meta.json
--rw-r--r--   0        0        0    27031 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/email/errors.data.json
--rw-r--r--   0        0        0     1725 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/email/errors.meta.json
--rw-r--r--   0        0        0    10032 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/email/header.data.json
--rw-r--r--   0        0        0     1738 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/email/header.meta.json
--rw-r--r--   0        0        0    86534 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/email/message.data.json
--rw-r--r--   0        0        0     1856 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/email/message.meta.json
--rw-r--r--   0        0        0    33617 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/email/policy.data.json
--rw-r--r--   0        0        0     1811 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/email/policy.meta.json
--rw-r--r--   0        0        0     3541 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/__init__.data.json
--rw-r--r--   0        0        0     1870 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/__init__.meta.json
--rw-r--r--   0        0        0     9643 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_catch.data.json
--rw-r--r--   0        0        0     1837 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_catch.meta.json
--rw-r--r--   0        0        0    72892 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_exceptions.data.json
--rw-r--r--   0        0        0     1858 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_exceptions.meta.json
--rw-r--r--   0        0        0    24915 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_formatting.data.json
--rw-r--r--   0        0        0     2006 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_formatting.meta.json
--rw-r--r--   0        0        0     2987 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_version.data.json
--rw-r--r--   0        0        0     1690 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_version.meta.json
--rw-r--r--   0        0        0     6726 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/__init__.data.json
--rw-r--r--   0        0        0     1756 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/__init__.meta.json
--rw-r--r--   0        0        0    75571 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/abc.data.json
--rw-r--r--   0        0        0     1904 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/abc.meta.json
--rw-r--r--   0        0        0    69972 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/machinery.data.json
--rw-r--r--   0        0        0     1915 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/machinery.meta.json
--rw-r--r--   0        0        0    23604 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/util.data.json
--rw-r--r--   0        0        0     1920 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/util.meta.json
--rw-r--r--   0        0        0    97938 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/metadata/__init__.data.json
--rw-r--r--   0        0        0     1921 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/metadata/__init__.meta.json
--rw-r--r--   0        0        0    12976 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/metadata/_meta.data.json
--rw-r--r--   0        0        0     1738 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/metadata/_meta.meta.json
--rw-r--r--   0        0        0    49033 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/iniconfig/__init__.data.json
--rw-r--r--   0        0        0     1825 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/iniconfig/__init__.meta.json
--rw-r--r--   0        0        0    24799 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/iniconfig/_parse.data.json
--rw-r--r--   0        0        0     1754 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/iniconfig/_parse.meta.json
--rw-r--r--   0        0        0     5089 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/iniconfig/exceptions.data.json
--rw-r--r--   0        0        0     1731 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/iniconfig/exceptions.meta.json
--rw-r--r--   0        0        0    16901 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/json/__init__.data.json
--rw-r--r--   0        0        0     1771 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/json/__init__.meta.json
--rw-r--r--   0        0        0    15868 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/json/decoder.data.json
--rw-r--r--   0        0        0     1715 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/json/decoder.meta.json
--rw-r--r--   0        0        0    11890 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/json/encoder.data.json
--rw-r--r--   0        0        0     1727 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/json/encoder.meta.json
--rw-r--r--   0        0        0     1662 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/__about__.data.json
--rw-r--r--   0        0        0     1623 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/__about__.meta.json
--rw-r--r--   0        0        0     9974 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/__init__.data.json
--rw-r--r--   0        0        0     1760 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/__init__.meta.json
--rw-r--r--   0        0        0    30097 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/cache.data.json
--rw-r--r--   0        0        0     1699 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/cache.meta.json
--rw-r--r--   0        0        0    23898 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/env.data.json
--rw-r--r--   0        0        0     2253 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/env.meta.json
--rw-r--r--   0        0        0    10482 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/exceptions.data.json
--rw-r--r--   0        0        0     1697 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/exceptions.meta.json
--rw-r--r--   0        0        0    79263 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/filter.data.json
--rw-r--r--   0        0        0     1905 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/filter.meta.json
--rw-r--r--   0        0        0    18309 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/lex.data.json
--rw-r--r--   0        0        0     1776 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/lex.meta.json
--rw-r--r--   0        0        0    30729 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/lru_cache.data.json
--rw-r--r--   0        0        0     1707 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/lru_cache.meta.json
--rw-r--r--   0        0        0    11601 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/match.data.json
--rw-r--r--   0        0        0     1727 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/match.meta.json
--rw-r--r--   0        0        0    38082 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/parse.data.json
--rw-r--r--   0        0        0     1996 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/parse.meta.json
--rw-r--r--   0        0        0    27075 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/path.data.json
--rw-r--r--   0        0        0     1851 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/path.meta.json
--rw-r--r--   0        0        0    52302 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/selectors.data.json
--rw-r--r--   0        0        0     1900 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/selectors.meta.json
--rw-r--r--   0        0        0    15219 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/stream.data.json
--rw-r--r--   0        0        0     1730 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/stream.meta.json
--rw-r--r--   0        0        0    21620 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/token.data.json
--rw-r--r--   0        0        0     1672 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/token.meta.json
--rw-r--r--   0        0        0     2635 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/function_extensions/__init__.data.json
--rw-r--r--   0        0        0     1739 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/function_extensions/__init__.meta.json
--rw-r--r--   0        0        0     2774 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/function_extensions/keys.data.json
--rw-r--r--   0        0        0     1651 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/function_extensions/keys.meta.json
--rw-r--r--   0        0        0     2515 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/function_extensions/length.data.json
--rw-r--r--   0        0        0     1680 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/function_extensions/length.meta.json
--rw-r--r--   0        0        0   154308 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/logging/__init__.data.json
--rw-r--r--   0        0        0     1879 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/logging/__init__.meta.json
--rw-r--r--   0        0        0    34085 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/__init__.data.json
--rw-r--r--   0        0        0     2164 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/__init__.meta.json
--rw-r--r--   0        0        0    33275 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/connection.data.json
--rw-r--r--   0        0        0     1919 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/connection.meta.json
--rw-r--r--   0        0        0   103634 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/context.data.json
--rw-r--r--   0        0        0     2328 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/context.meta.json
--rw-r--r--   0        0        0   160927 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/managers.data.json
--rw-r--r--   0        0        0     1961 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/managers.meta.json
--rw-r--r--   0        0        0    56176 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/pool.data.json
--rw-r--r--   0        0        0     1807 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/pool.meta.json
--rw-r--r--   0        0        0     9823 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_fork.data.json
--rw-r--r--   0        0        0     1794 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_fork.meta.json
--rw-r--r--   0        0        0     6247 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_forkserver.data.json
--rw-r--r--   0        0        0     1836 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_forkserver.meta.json
--rw-r--r--   0        0        0     6968 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_spawn_posix.data.json
--rw-r--r--   0        0        0     1838 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_spawn_posix.meta.json
--rw-r--r--   0        0        0     2176 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_spawn_win32.data.json
--rw-r--r--   0        0        0     1808 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_spawn_win32.meta.json
--rw-r--r--   0        0        0    19246 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/process.data.json
--rw-r--r--   0        0        0     1771 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/process.meta.json
--rw-r--r--   0        0        0    21492 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/queues.data.json
--rw-r--r--   0        0        0     1775 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/queues.meta.json
--rw-r--r--   0        0        0    31449 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/reduction.data.json
--rw-r--r--   0        0        0     1981 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/reduction.meta.json
--rw-r--r--   0        0        0    31860 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/shared_memory.data.json
--rw-r--r--   0        0        0     1825 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/shared_memory.meta.json
--rw-r--r--   0        0        0    73309 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/sharedctypes.data.json
--rw-r--r--   0        0        0     1896 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/sharedctypes.meta.json
--rw-r--r--   0        0        0    10735 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/spawn.data.json
--rw-r--r--   0        0        0     1747 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/spawn.meta.json
--rw-r--r--   0        0        0    27932 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/synchronize.data.json
--rw-r--r--   0        0        0     1861 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/synchronize.meta.json
--rw-r--r--   0        0        0    25682 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/util.data.json
--rw-r--r--   0        0        0     1879 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/util.meta.json
--rw-r--r--   0        0        0   382629 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/os/__init__.data.json
--rw-r--r--   0        0        0     1924 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/os/__init__.meta.json
--rw-r--r--   0        0        0     5359 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/os/path.data.json
--rw-r--r--   0        0        0     1713 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/os/path.meta.json
--rw-r--r--   0        0        0     3505 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/__init__.data.json
--rw-r--r--   0        0        0     1671 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/__init__.meta.json
--rw-r--r--   0        0        0    15307 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_elffile.data.json
--rw-r--r--   0        0        0     1822 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_elffile.meta.json
--rw-r--r--   0        0        0    29701 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_manylinux.data.json
--rw-r--r--   0        0        0     2034 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_manylinux.meta.json
--rw-r--r--   0        0        0    20244 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_musllinux.data.json
--rw-r--r--   0        0        0     1945 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_musllinux.meta.json
--rw-r--r--   0        0        0    48258 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_parser.data.json
--rw-r--r--   0        0        0     1865 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_parser.meta.json
--rw-r--r--   0        0        0    15161 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_structures.data.json
--rw-r--r--   0        0        0     1703 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_structures.meta.json
--rw-r--r--   0        0        0    19444 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_tokenizer.data.json
--rw-r--r--   0        0        0     1811 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_tokenizer.meta.json
--rw-r--r--   0        0        0    19626 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/markers.data.json
--rw-r--r--   0        0        0     1980 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/markers.meta.json
--rw-r--r--   0        0        0     9773 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/requirements.data.json
--rw-r--r--   0        0        0     1945 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/requirements.meta.json
--rw-r--r--   0        0        0    61359 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/specifiers.data.json
--rw-r--r--   0        0        0     1920 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/specifiers.meta.json
--rw-r--r--   0        0        0    31130 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/tags.data.json
--rw-r--r--   0        0        0     2010 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/tags.meta.json
--rw-r--r--   0        0        0    11150 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/utils.data.json
--rw-r--r--   0        0        0     1882 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/utils.meta.json
--rw-r--r--   0        0        0    71300 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/version.data.json
--rw-r--r--   0        0        0     1914 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/version.meta.json
--rw-r--r--   0        0        0    12002 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/pytest/__init__.data.json
--rw-r--r--   0        0        0     2384 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/pytest/__init__.meta.json
--rw-r--r--   0        0        0     1584 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/__init__.data.json
--rw-r--r--   0        0        0     1605 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/__init__.meta.json
--rw-r--r--   0        0        0    12577 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/compliance.data.json
--rw-r--r--   0        0        0     1995 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/compliance.meta.json
--rw-r--r--   0        0        0    16020 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/consensus.data.json
--rw-r--r--   0        0        0     1952 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/consensus.meta.json
--rw-r--r--   0        0        0     8519 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_async.data.json
--rw-r--r--   0        0        0     1676 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_async.meta.json
--rw-r--r--   0        0        0     9885 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_compare.data.json
--rw-r--r--   0        0        0     1870 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_compare.meta.json
--rw-r--r--   0        0        0     9095 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_compound_path.data.json
--rw-r--r--   0        0        0     1971 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_compound_path.meta.json
--rw-r--r--   0        0        0    13101 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_concrete_path.data.json
--rw-r--r--   0        0        0     1948 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_concrete_path.meta.json
--rw-r--r--   0        0        0    12323 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_env.data.json
--rw-r--r--   0        0        0     1786 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_env.meta.json
--rw-r--r--   0        0        0     5445 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_errors.data.json
--rw-r--r--   0        0        0     1943 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_errors.meta.json
--rw-r--r--   0        0        0    13512 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_find.data.json
--rw-r--r--   0        0        0     1907 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_find.meta.json
--rw-r--r--   0        0        0    14142 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_find_compound_path.data.json
--rw-r--r--   0        0        0     1960 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_find_compound_path.meta.json
--rw-r--r--   0        0        0    14360 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_find_reference.data.json
--rw-r--r--   0        0        0     1928 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_find_reference.meta.json
--rw-r--r--   0        0        0    13985 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_ietf.data.json
--rw-r--r--   0        0        0     1912 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_ietf.meta.json
--rw-r--r--   0        0        0    10659 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_ietf_comparison.data.json
--rw-r--r--   0        0        0     1916 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_ietf_comparison.meta.json
--rw-r--r--   0        0        0    15542 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_lex.data.json
--rw-r--r--   0        0        0     2054 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_lex.meta.json
--rw-r--r--   0        0        0     4926 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_match_api.data.json
--rw-r--r--   0        0        0     1737 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_match_api.meta.json
--rw-r--r--   0        0        0     8852 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_parse.data.json
--rw-r--r--   0        0        0     1955 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_parse.meta.json
--rw-r--r--   0        0        0     9251 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_parse_compound_path.data.json
--rw-r--r--   0        0        0     1983 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_parse_compound_path.meta.json
--rw-r--r--   0        0        0    13562 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_re.data.json
--rw-r--r--   0        0        0     1901 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_re.meta.json
--rw-r--r--   0        0        0     2823 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/__init__.data.json
--rw-r--r--   0        0        0     1686 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/__init__.meta.json
--rw-r--r--   0        0        0    57353 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/_parser.data.json
--rw-r--r--   0        0        0     1937 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/_parser.meta.json
--rw-r--r--   0        0        0     7696 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/_re.data.json
--rw-r--r--   0        0        0     1884 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/_re.meta.json
--rw-r--r--   0        0        0     2994 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/_types.data.json
--rw-r--r--   0        0        0     1780 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/_types.meta.json
--rw-r--r--   0        0        0     6509 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/__init__.data.json
--rw-r--r--   0        0        0     1933 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/__init__.meta.json
--rw-r--r--   0        0        0    26185 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/_log.data.json
--rw-r--r--   0        0        0     1781 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/_log.meta.json
--rw-r--r--   0        0        0     8320 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/async_case.data.json
--rw-r--r--   0        0        0     1812 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/async_case.meta.json
--rw-r--r--   0        0        0   225927 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/case.data.json
--rw-r--r--   0        0        0     1932 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/case.meta.json
--rw-r--r--   0        0        0    15920 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/loader.data.json
--rw-r--r--   0        0        0     1843 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/loader.meta.json
--rw-r--r--   0        0        0    12793 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/main.data.json
--rw-r--r--   0        0        0     1852 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/main.meta.json
--rw-r--r--   0        0        0    22448 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/result.data.json
--rw-r--r--   0        0        0     1799 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/result.meta.json
--rw-r--r--   0        0        0    11709 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/runner.data.json
--rw-r--r--   0        0        0     1842 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/runner.meta.json
--rw-r--r--   0        0        0    12371 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/signals.data.json
--rw-r--r--   0        0        0     1794 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/signals.meta.json
--rw-r--r--   0        0        0    12264 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/suite.data.json
--rw-r--r--   0        0        0     1815 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/suite.meta.json
--rw-r--r--   0        0        0     1671 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/urllib/__init__.data.json
--rw-r--r--   0        0        0     1685 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/urllib/__init__.meta.json
--rw-r--r--   0        0        0   166629 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/urllib/parse.data.json
--rw-r--r--   0        0        0     1791 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/urllib/parse.meta.json
--rw-r--r--   0        0        0   121554 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/__init__.data.json
--rw-r--r--   0        0        0     2140 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/__init__.meta.json
--rw-r--r--   0        0        0    24543 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/_yaml.data.json
--rw-r--r--   0        0        0     1777 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/_yaml.meta.json
--rw-r--r--   0        0        0    11530 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/composer.data.json
--rw-r--r--   0        0        0     1716 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/composer.meta.json
--rw-r--r--   0        0        0    49399 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/constructor.data.json
--rw-r--r--   0        0        0     1984 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/constructor.meta.json
--rw-r--r--   0        0        0    21339 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/cyaml.data.json
--rw-r--r--   0        0        0     1837 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/cyaml.meta.json
--rw-r--r--   0        0        0    13980 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/dumper.data.json
--rw-r--r--   0        0        0     1886 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/dumper.meta.json
--rw-r--r--   0        0        0    40195 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/emitter.data.json
--rw-r--r--   0        0        0     1695 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/emitter.meta.json
--rw-r--r--   0        0        0     9503 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/error.data.json
--rw-r--r--   0        0        0     1671 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/error.meta.json
--rw-r--r--   0        0        0    29716 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/events.data.json
--rw-r--r--   0        0        0     1673 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/events.meta.json
--rw-r--r--   0        0        0    12948 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/loader.data.json
--rw-r--r--   0        0        0     1857 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/loader.meta.json
--rw-r--r--   0        0        0    11495 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/nodes.data.json
--rw-r--r--   0        0        0     1691 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/nodes.meta.json
--rw-r--r--   0        0        0    15809 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/parser.data.json
--rw-r--r--   0        0        0     1693 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/parser.meta.json
--rw-r--r--   0        0        0    13816 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/reader.data.json
--rw-r--r--   0        0        0     1739 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/reader.meta.json
--rw-r--r--   0        0        0    45238 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/representer.data.json
--rw-r--r--   0        0        0     1866 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/representer.meta.json
--rw-r--r--   0        0        0    11407 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/resolver.data.json
--rw-r--r--   0        0        0     1696 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/resolver.meta.json
--rw-r--r--   0        0        0    33040 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/scanner.data.json
--rw-r--r--   0        0        0     1695 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/scanner.meta.json
--rw-r--r--   0        0        0    10954 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/serializer.data.json
--rw-r--r--   0        0        0     1720 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/serializer.meta.json
--rw-r--r--   0        0        0    37858 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/tokens.data.json
--rw-r--r--   0        0        0     1673 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/tokens.meta.json
--rw-r--r--   0        0        0        1 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/.gitignore
--rw-r--r--   0        0        0       43 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/CACHEDIR.TAG
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1086d708790bd7cb
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1095cfed48560a97
--rw-r--r--   0        0        0      418 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/111b0167a96f6cc7
--rw-r--r--   0        0        0      701 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/113169384d5668bc
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/118e0978578f504e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1194388bc2c6baed
--rw-r--r--   0        0        0      172 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/12377713d939dcce
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/12400f2018249ea1
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1258567092747a21
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1270beb4a704eea6
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1299bbf057d49d1b
--rw-r--r--   0        0        0      949 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/135ad1453038c1a4
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/136827364eb7fe04
--rw-r--r--   0        0        0      619 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1398303151225940
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/141ec2f392f2feeb
--rw-r--r--   0        0        0      542 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/146653dc356f145a
--rw-r--r--   0        0        0      418 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/14dd1f452892a317
--rw-r--r--   0        0        0      806 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/15a3b5713a8c7860
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/15b9c3a8a742cdc4
--rw-r--r--   0        0        0     1950 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1627d49e057ce6ef
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/16ea129bd35da7e5
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/16f052bbad634acd
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/16f894a8f3d0ffa
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1798db5f67f7f187
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/183eb2a303a637d1
--rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/18865323e91b9a48
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/18f9cfd05e11f802
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1912fc58846c4806
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/19251d1cac3e6a15
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/19f9dbab59d2f02
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1a4b835101dd193a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1a64b11bec7288b2
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1aa5f6cdf3cdc302
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1ab58d9baeae7870
--rw-r--r--   0        0        0      933 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1acf71e60d0cb21f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1b87153e310c0754
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1ba222bd6e162120
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1c2dad708442985
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1c406ce7037979ad
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1cad9d23fc0d3206
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1cd53a45ebc7a75a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1d937bc359ec3abd
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1df5534d9f64a95c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1e427db86b0cd407
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1e51102ab3677167
--rw-r--r--   0        0        0      572 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1f12aa22fe2f769c
--rw-r--r--   0        0        0     2890 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1f3b04ff651c8c80
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/1f720660e81d1e1d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/209d42dd15df5c72
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/20e120991f075171
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/20f16d13ac88b02e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2111b4b6f4a44c5f
--rw-r--r--   0        0        0     1950 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/213493565c60d69e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2152120114ecb71
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/216a9723a151eed9
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2170e3da77488531
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/217fbafea45e521e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/21de75bac5dc9797
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/229b06339539ba4a
--rw-r--r--   0        0        0      418 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/22a642bcc6ca170
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/22ed7c05b59c4cad
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/23d3de9fa792bee6
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/248a178f46f844ae
--rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/24a2cbc527b75aca
--rw-r--r--   0        0        0     1076 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/253e03a0e43afe2
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2544df6ae7edeccc
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/255187ca88b13246
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/258699e02b41255a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/25e251f9e5aaa70e
--rw-r--r--   0        0        0     1740 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/26a981bb502f16f
--rw-r--r--   0        0        0      437 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/26bce6500eb7b3ce
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/27100733e2a4621b
--rw-r--r--   0        0        0      370 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2720ed943792ec88
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/277c0cc985f81327
--rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2781e76e5ea0bbd7
--rw-r--r--   0        0        0      959 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/279262a136b9c91b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/27fc17fc71036c10
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2892468c677836ba
--rw-r--r--   0        0        0      740 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/28b9e8854f3bba14
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/28f3c9bf44f18483
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2900d3b370e1865
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/291d0ac06dd74aeb
--rw-r--r--   0        0        0      204 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/29771511a6d4c073
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/29ac638f5175988a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/29ad0a3a3ff1699
--rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/29c2a04fee34345e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2a061adb62b9481
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2a16c0754fecdcf8
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2a22c874601c5ca7
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2ac255a8c1f48cdc
--rw-r--r--   0        0        0      978 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2b1ae2f56430e88e
--rw-r--r--   0        0        0      418 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2b1b36045a55211
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2b394cbcee977c74
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2b41efeadbe99433
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2b4673461b969d8c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2b4da1c4e5824b85
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2b4fc49dfe9f187
--rw-r--r--   0        0        0     2328 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2b9fda870d662d61
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2bde3cdc25b7d710
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2bebb327b756c7fb
--rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2cd4097fac035fda
--rw-r--r--   0        0        0      192 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2ce97208c008f223
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2cf0e9bbd2feb95c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2d2e35e1b6bf4cc3
--rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2d32ff4c07d4445b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2d5ac14578beee6f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2e4034ac2f40858b
--rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2e8fc72ab83c7ee4
--rw-r--r--   0        0        0     3175 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2ea0f9311fceda9f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2eb3a5b114e26e97
--rw-r--r--   0        0        0      162 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2ec8cb89e5035179
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2ee6d2d6297778d4
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2f13cf8b06bed35c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2f79b37103e9badf
--rw-r--r--   0        0        0      562 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2f7a4bad2663cc7a
--rw-r--r--   0        0        0      959 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2f7a9dea88b592c6
--rw-r--r--   0        0        0      214 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2f9146e9f9c91006
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2fb02999c97ff934
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2fb7c2500f2ffd3f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2fe66c4c0f4b723
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/2fed8ec074fc58e0
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/30171b9362f7f695
--rw-r--r--   0        0        0     2150 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3064bcb187e4005b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/306810d0d5443a1b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/30be7b7f111100ba
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/31110c4d4e4f9ac5
--rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/31281e8df2fc9f77
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/31e1f054541ab85
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/323a3f35d70bff79
--rw-r--r--   0        0        0      757 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/325e27582ba6b00b
--rw-r--r--   0        0        0      619 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3278cae1025f408d
--rw-r--r--   0        0        0      210 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/32c1a82391d8367b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/33480e6566e1d7c1
--rw-r--r--   0        0        0      208 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3358f600210bb04a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3441b738d2b0768b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/34a7385bd4a66d39
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/34d6a99ba114971
--rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/34e6cdb48c8892b
--rw-r--r--   0        0        0      245 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/35040e5c80ebeb9e
--rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/354222da09a71a22
--rw-r--r--   0        0        0      619 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/35570cbe6251c078
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/358e4f0467afdb30
--rw-r--r--   0        0        0     2807 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/35acb2ea313c1f4f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/36091467cb493eb8
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/36494dfc908b7300
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3666724fba65f564
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3735dc080d45a6b3
--rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/37825382b5dfcb8d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/378a61082f794bdf
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/379721ba1b034669
--rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/37bba804cab5dbb7
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/37be7672ebb3934f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/383b28009a5701d6
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/384d04ecd4e021b4
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/389bf92f08a98081
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/38a2aa5ed389e590
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/397154cc7b2781
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/39f2b6610b879568
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3ae2176d9bcce237
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3b9460a7c0321145
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3bd9178cfbe94bfa
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3bfe16a0c38493c1
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3c0aa158352075c8
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3c516481a66f5cd9
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3ca80de959c93950
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3cd3e0fbac79ac0d
--rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3d1f764c0b668f34
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3d4aeb1458f80400
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3d5e480abdb6a621
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3d9e19973cc2bae
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3da8a47ff799c54
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3daf1415edc12a26
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3db75912b5c24118
--rw-r--r--   0        0        0      415 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3e789340219028bd
--rw-r--r--   0        0        0      395 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3ec6c72e84642dcb
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3ef2e5d227900cdf
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3efad478150dd3aa
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3f7fb0dc065162de
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3f8ac2e7add0dc8e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3fbb4a2ee4e9615d
--rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/3fc5b0398b43cb60
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4018c951df86c3a3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/40beb5d646e80b08
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/41015793dc1b0750
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4104307b2b3f3735
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/411cbeb7fcb715fc
--rw-r--r--   0        0        0      227 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/412bd35d840f2795
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/414641f0374b0b77
--rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4169c686ca27018c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/416fffc67f569700
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/417079b15ca0f5fc
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/41f0c083b0a1a031
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/420cb90c9ca663e9
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/420fc333c545e403
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4229f954fa4105b0
--rw-r--r--   0        0        0      172 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4295e7e21d302771
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/42ae413f64cff3ab
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/42e698f34ac38404
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/43d71279a69c387a
--rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/44ddbc02cc145fa
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/44dfaa68f2ba2228
--rw-r--r--   0        0        0      352 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4536802fc67ba11c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/461a0932070c0e05
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4657d4c259f5984d
--rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/47f87d838c0e9070
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4814c2acf8896584
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4832d7b52b9d9234
--rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/483b7bbda285fbb7
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/48bedf78c55dae3e
--rw-r--r--   0        0        0      162 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/48fb486af7dae3e6
--rw-r--r--   0        0        0      572 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/492ebdc8ce6d7aaa
--rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/493a5437e25c6d20
--rw-r--r--   0        0        0      211 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/49c438c12f0b8c7e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4a32f124e06b5b01
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4a865a25bc9574c3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4ab4ba297550d4c7
--rw-r--r--   0        0        0      256 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4b155c6e55c6d7ca
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4b32c4463816c77c
--rw-r--r--   0        0        0      959 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4c10a12091591533
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4c5bcee61357273e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4c6f9e4364a16a1b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4d19bb63ef7037ee
--rw-r--r--   0        0        0      204 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4d6c12702373cc27
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4edd21956339b566
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4ef388ab14295e2d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4ef7138cff1b40c0
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4f1e1949fdb71b59
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4f4a24feeb57f841
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4f98d65b183ac998
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/4fc48ee6c13f2e3c
--rw-r--r--   0        0        0      954 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/501fd54946953b5c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5031198fa0e3d1cc
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/50597d25025e0e26
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/50c72d73128ddbe6
--rw-r--r--   0        0        0     1576 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/510acc3260e58d67
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/515fa1c3637379ca
--rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/51a39a4ab0b9e5a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/51acea567b417629
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/52065d40a908b367
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/52425e9a986550b5
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5263b01b3d3daa77
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/529476b9008473e2
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/52d60cf06915d9e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/53095686dc94179a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/534c1288997f241a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/53a9f56c3efc5e48
--rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/540a4ae1823a85e7
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/54a82afe60eb64df
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/54b58d54bee394af
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/54c99a8f739a1a59
--rw-r--r--   0        0        0      172 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/551e44d1d3ec5665
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/55f6e65978cfb075
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/55f81727c24ac0a4
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/56147e569457954c
--rw-r--r--   0        0        0      190 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/571181d5345e2050
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/57eb892b6c4c3c1b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/580b1aa14be37639
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/58171af34ea511ef
--rw-r--r--   0        0        0     2150 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/582fc01eaccf9d11
--rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/58e0fd9241ecf02e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5a1be3b2245cd0f2
--rw-r--r--   0        0        0      223 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5a24ded2aa2852d
--rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5a396375009eba92
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5b8c4c1ad20e5f75
--rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5c6e80b5464ae96
--rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5cacc766c4597689
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5cd52bc852538304
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5d23cbb3e545c0c9
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5d5b4dcbf5bc4b45
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5d6de0ef8fd1c8c3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5df021e329be9624
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5dfa93b6e0c2e6c6
--rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5e29d098bb1ecc0a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5e61bd53ae508a35
--rw-r--r--   0        0        0      198 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5e977bb5e72fd54c
--rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5e9e67c9beead0c5
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5f6b0ae9017aec8
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5f78b9f97703b97b
--rw-r--r--   0        0        0      554 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5f8db1660501e234
--rw-r--r--   0        0        0      418 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/5feb5ced1cfb0726
--rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/60943986c63e73b3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/60c8a925b11d461a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6159341561bf659f
--rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6164c8374827eb66
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/618068a750f4b11f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/618d0b6aa2a4dee7
--rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/619d75195853621
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6266f52e9af39a30
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/62cb483937d88136
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6316e7293ca1b89e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6365bd43ffa9ce0d
--rw-r--r--   0        0        0      217 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/63b5f94b5de23e99
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/63ffc2691e47cd87
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/64b11b6f95257cb2
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/64d0f72357941326
--rw-r--r--   0        0        0      246 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6508c3c5487ab075
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6536d4c143f8be91
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/65728b52f41bc9ba
--rw-r--r--   0        0        0      806 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6576547c7f4694be
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6644763f109bdd6b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/669dd8c8a39698b7
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/66ac2324e22de590
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/66d089a8df35552b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/66d111006494eb36
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/66dc710e3f81dd1b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/670150825a70ddd
--rw-r--r--   0        0        0      390 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6716dc831f36b4e
--rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/67464bd807747cd7
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6746ada4d0522944
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/67b5326d54837deb
--rw-r--r--   0        0        0      578 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/682188a646d78c0
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/682860051556cf7c
--rw-r--r--   0        0        0      446 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6890ca733e8cb4fd
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/68d3fe72b76a4597
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6917d2cd5cad8ce8
--rw-r--r--   0        0        0      933 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/695170c6d345cb58
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/696b5d905cecae9e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/698e80c153c0e564
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/69a1b64825d36650
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/69c0b99e6a3612ac
--rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6a1d1822013c9bc0
--rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6a6a4fb6f8a50947
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6a8150cb8ef00174
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6b2c7e5abafb43d5
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6ba094ed40da3dfe
--rw-r--r--   0        0        0      246 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6bac0870e1bfe66b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6bd4c791fee019e1
--rw-r--r--   0        0        0      619 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6c8242c16814d970
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6c96f471c4bbea32
--rw-r--r--   0        0        0      172 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6ca0e41194c8d88a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6ca8d392710dcad0
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6cec0d8c6e537732
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6cfb413da2d3a9d7
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6d33cc2bdaf5b388
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6d6e3ff4d34fb67c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6ddf9f070f5ea610
--rw-r--r--   0        0        0      262 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6de8d7c51d326383
--rw-r--r--   0        0        0     1237 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6e342654a00b5817
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6e419bf1baa2b856
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6e9399320683c7f8
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6edfe3868f20ef5b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6f69ef19acc74949
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6f79223032f285e6
--rw-r--r--   0        0        0     1532 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6fb452c5ea33322
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/6fd67a6c4d9402cd
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7066a7cfa126658c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/70a3c394403b13e
--rw-r--r--   0        0        0      418 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/70a527efdfe96d9e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/70bda471d8e83aca
--rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/70f00010df65f78f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/70f76aadc859c727
--rw-r--r--   0        0        0     2150 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/71373ffe75246f00
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/714586f9c795411b
--rw-r--r--   0        0        0      790 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/715499bd1eb26466
--rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/715dbd085d13932
--rw-r--r--   0        0        0      247 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7166400981c965aa
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/71c1374790d60ec7
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/71e60efbcd179c8b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/71fdde3839d3392e
--rw-r--r--   0        0        0     2150 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/72499df899c54a45
--rw-r--r--   0        0        0      406 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/726d869eaad7cbd2
--rw-r--r--   0        0        0      790 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7281991b04dc372b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/72dae9b85aedb727
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/72fc43b5409abc5d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7419ca5c5d9d3576
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/749c16d9b38ea10b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/75093b69707477c7
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7564f23bf736124e
--rw-r--r--   0        0        0      227 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/75df3e0ec74f7a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/760a90d18d7a043d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/762424f77d674629
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7698193a2f2fd3b3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/76accb1814a3a13
--rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7764d0a3ebbd15f1
--rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/777056ba87a3db44
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/77fa35a0d4a775fa
--rw-r--r--   0        0        0      248 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/784a7e6082e35f79
--rw-r--r--   0        0        0     1950 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7861f5cb2966565a
--rw-r--r--   0        0        0     1576 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/79d8b31a7196e404
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7a693d4a4965f3ee
--rw-r--r--   0        0        0      811 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7abafe920dd77a92
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7ac0bc918b5c67c6
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7ae7caba07deb51b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7ae90594605c72c7
--rw-r--r--   0        0        0     1156 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7bbfd8c3690b5a75
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7c1fa8b9eb0b1811
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7c8218be60001dda
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7cd8c0f02c8d8d24
--rw-r--r--   0        0        0      418 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7cdbd1dc60e81b96
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7d17b9c40a45bd56
--rw-r--r--   0        0        0      923 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7d958009b81b0dd7
--rw-r--r--   0        0        0      429 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7db8793f8e021f80
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7dfeddee84e5b438
--rw-r--r--   0        0        0     2738 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7e39743b5037bb34
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7e6d64b78cc2e356
--rw-r--r--   0        0        0      211 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7ee528fc74afd046
--rw-r--r--   0        0        0      187 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7f04363dd1b7eb25
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7f463249d43ddcd9
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7f7fb29c4cc7e61e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7fb9a965e8077e1d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/7fcbd52f3630686c
--rw-r--r--   0        0        0     3851 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/80e739b3e52c2ee9
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/81441640090c5bc
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8192e3658d123572
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/81f1f9db8376452e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8201bdd1e24ea9f5
--rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/824ad90d2e4a90c4
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/82cdac5a72987b8b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8315b0d8c1b5a7b7
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8354d9ea10984822
--rw-r--r--   0        0        0      572 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8377c8be88accd28
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8437018678492400
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/844797c614a2a016
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8461e9c9048d50f4
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/84c6b4671f5829bc
--rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/84dc23112959bef3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/851a246705623ed8
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/85724e9e4780a371
--rw-r--r--   0        0        0      923 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/857ff98531f4bd4a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/85a48e1aa08f497c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8776f9eabe3609af
--rw-r--r--   0        0        0      223 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/87cc41cfe62706e5
--rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/87e6069b6dae1d69
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/87e61854cba9e459
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/884f329d76b22a81
--rw-r--r--   0        0        0      199 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/88597d00446c39ae
--rw-r--r--   0        0        0      172 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/88784a30b1e3325e
--rw-r--r--   0        0        0     1576 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8880e918cb120ec7
--rw-r--r--   0        0        0      572 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/88b37c139c075c2c
--rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/89afb837dfa217c6
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/89ba1e99f76a5c1
--rw-r--r--   0        0        0      204 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8a4b5ac208fc8176
--rw-r--r--   0        0        0     1576 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8a5fbc233bbd1ad6
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8ad87f05d43f1e0f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8b1b566e67aaf911
--rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8bcea5aeb8b26f31
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8c74538d4cf25bb
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8cc3d1a83e269152
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8cef7199f6258137
--rw-r--r--   0        0        0      222 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8d593356a0ee5072
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8de59f96561d71d1
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8e0583fbc62b6104
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8ec74aec9c1c01c3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8f27d152d90364e2
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8f2f2a38cdcfe630
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8f4cac62f4e5196b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8f6de574c26679a1
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8f847a3b90cf5ddc
--rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/8fff743c3d8501f3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/903c523f0f7ea349
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/90fb0f25b4b1982a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/91113ba4b61e6442
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9138673748b10d05
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/916ee4c97ed80a01
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9259fd33f76abb9d
--rw-r--r--   0        0        0      216 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/92bf0c830b819795
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/931740d8b0e88b6d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/94031dc00bdc7467
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/941e004fb7846f51
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9468053cffed6ac5
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/94be5a333382332f
--rw-r--r--   0        0        0     1156 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/950808b1e26775ec
--rw-r--r--   0        0        0      933 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/95267216d1d74c9
--rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9564ef73b0f0b9bd
--rw-r--r--   0        0        0      192 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/958da252825b59cd
--rw-r--r--   0        0        0      324 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/95ff4d1cc696af6a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/978a175054cecb8b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/97daea7f24aa497e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/97f7ba029545af94
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/97f7c0439761be0d
--rw-r--r--   0        0        0     1278 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/986b503a8f13eaa
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9876f7de98fece8c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9884392ab8835283
--rw-r--r--   0        0        0      370 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/98aaf65343e92671
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/98c41673fbe3aac0
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/991c1dd22bfb5cc3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/99276b2ef50b24b7
--rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/99a1f744d7a3bce0
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/99e38be04ae3e738
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9a451b726d896a13
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9a88e788c8f6af81
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9ad03463c6a71b94
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9b12802ae3321a54
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9b5c71f22528b824
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9be1c788122ea694
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9c6f167fdeb3d317
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9cc25f96d447d297
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9cd3a936f82c6065
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9cf608a32b424228
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9d338bcb6840debe
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9d98fab6fcbebc62
--rw-r--r--   0        0        0      712 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9dfd1a4c1d6c5611
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9e2ebe40a64a3056
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9e67d8e3d44a52a9
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9e7b258c9d6ada25
--rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9f615ba52e97076c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9f7b87a7b8718ae0
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9f7cc6a7e28d672
--rw-r--r--   0        0        0     1237 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/9f86a234993ab90f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a032fe5373e2f566
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a06743363ba17397
--rw-r--r--   0        0        0      562 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a09ca4d68f7f7a6d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a0c9760cf9c8d13f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a110a12cfc697e8c
--rw-r--r--   0        0        0      192 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a115a02d1705e6ae
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a1269bab7695230b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a1e338582ecefbf2
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a1ed812d84ff228e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a1fe17a030762aaa
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a259354f3f0a0f79
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a29252e225ecf2b8
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a296aa250618c000
--rw-r--r--   0        0        0      928 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a296e558a05a4446
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a362b930d2a8e71d
--rw-r--r--   0        0        0      923 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a3930f42fc0d5727
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a3b6ce8deae08464
--rw-r--r--   0        0        0      192 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a3d5954e9452da4b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a3fadb7adae4063f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a45a31edda7a8cbe
--rw-r--r--   0        0        0      211 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a468e101c105ae0c
--rw-r--r--   0        0        0      162 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a527cc0152cf02a6
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a539593321e14fe6
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a53ebc83330776b3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a6018ee5d12eb85
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a6a5b65691bdc39d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a79f9aa8e748cb3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a83b403ed1f478a7
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/a96fec08236817b0
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/aa36cf81253e9663
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/aa6af830d5cfbd13
--rw-r--r--   0        0        0    10127 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/aa737b2f5fb8e71d
--rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/aa820a19cfc27687
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/aa890592ef42784a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/aa96346bdbbbadca
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/aac63e41a0f74317
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/aad6c3b1b7e2d037
--rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ab5f6078817c2fb0
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ab8fdf5c743c1460
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/abf597b97b538b40
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ac080e6c34953966
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ac0cb2254a297d
--rw-r--r--   0        0        0      542 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ac31423108a9860
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ac6883549bcf0e93
--rw-r--r--   0        0        0      189 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/acab2a9223b5295f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/accdce480aaedfb0
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/acd588827dbb0371
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ad8acc49cd946a33
--rw-r--r--   0        0        0     6366 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/adfdc55c283c3c0f
--rw-r--r--   0        0        0     5626 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ae81d3744b93d310
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/aec7218dad196161
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/aee942293e1feefc
--rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/af31928a32d7994d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/af3b44be2117df44
--rw-r--r--   0        0        0      261 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/af3d20cf6acc98a6
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/af639254e5e42638
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/af7a06e1e348d184
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/af96474e5d6d8a79
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/afd67290197a0223
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/afe1f6cc2e2294ad
--rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b050a7831c5ff26d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b053f453ef051223
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b0c9aee3bae2a40b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b0df4ef10e21bb3c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b1169fed645c89dc
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b11f56fb8ba4fb52
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b137cb9f0209e163
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b14a58826252ad27
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b15bcf7cae7464a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b1900434fd007335
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b19c390aae16d2dc
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b1c77fe3fc4341a5
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b2025744040ed5ba
--rw-r--r--   0        0        0     3552 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b2c510e6d789bae1
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b34662c19e9588ec
--rw-r--r--   0        0        0     1285 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b34b2d8198704c68
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b3aed5ec6805bd41
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b4be0b529d02420d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b51cbd48e85a6f4
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b5e0e18c9d78783d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b607c010d16d520
--rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b60c1e8ff4f16c7f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b635aef0cfca1d11
--rw-r--r--   0        0        0    11806 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b69b1ed3056953ee
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b6a34dd9c878d92d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b6bee2f03daf9855
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b6e3c2953538738a
--rw-r--r--   0        0        0      928 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b72ce555d5fa6a8e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b74f84f806ad6859
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b78fb2ccf62a3b95
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b790864dd0cce062
--rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b8230cee1f524ad1
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b87649c3116f2170
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b8f42454cd24a1c0
--rw-r--r--   0        0        0      806 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/b925dc8a594b869a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bb211b609a91c7c1
--rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bb4fde2c72d4315a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bb873e4145d79e46
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bc42a7d33ea0b947
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bc491c862523b5dc
--rw-r--r--   0        0        0      256 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bd3f48f796fd95ab
--rw-r--r--   0        0        0      247 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bd491c1f1af4d251
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bd65255aefe18e02
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bd6b97d43aac146b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bda1b20e60f34b7b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bdbd414788569a24
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/be1c34972d748a4b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/be3e726596e949c3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/be47b2cc4ed456b0
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bed7c7f59683f6f5
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bf9182473114ba35
--rw-r--r--   0        0        0     1196 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bfaa6c8b09ea7082
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bfae5ad2c3b5210
--rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bfbe152080b709d9
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bfc4bac36774d7bb
--rw-r--r--   0        0        0     1504 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/bfeb6ff39293ca1d
--rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c0005c6bd945f3d2
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c011ea061e4dbce8
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c074f80fa39459e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c092633ea9a2dd8e
--rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c10cd88b4285ff0b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c197af6f2829b65c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c20c4bd79e0975ca
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c25fd4073dd7ecf9
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c31b8c89c9b388cb
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c32da9b0188c78e4
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c36fe33676ead07d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c3b14714ff33ec1b
--rw-r--r--   0        0        0      246 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c3b73e0e8aa099fa
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c424ef13bc66b049
--rw-r--r--   0        0        0     1576 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c467bf0cef9b03ab
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c4b8f6b6883cea1e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c4c45ce4e9c2687d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c4d961ac35f46220
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c5211d60a6641a73
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c6035b26f69105fd
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c703a54a942d3a36
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c728c63863b8abf6
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c7a9f3f0ec2d6133
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c7c66d7c506eb23a
--rw-r--r--   0        0        0      190 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c7dd7c9490ed7a40
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c822b670428f7480
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c83c52eb724c117e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c85a4601697418f5
--rw-r--r--   0        0        0      978 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c8959c42754024d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/c9ff1b4f31e033c5
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ca234d38b42ec57b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ca7961b45cdda322
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/cb243904781569bd
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/cb82637251df8fa
--rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/cbbc258be108b7df
--rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/cc64ecd0f9bc901b
--rw-r--r--   0        0        0      180 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ccdf86f0f4ac4b9e
--rw-r--r--   0        0        0     1950 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/cd4f7faa7a866ead
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/cd5351001df3ccf
--rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/cdbdecacd11dee93
--rw-r--r--   0        0        0      393 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/cdc1b0fec16a36a4
--rw-r--r--   0        0        0      811 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ce1f45bc791cd4ab
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ce796a3ed9297b64
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/cf715425db3a674c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/cfadb0829958f9d9
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/cfcf9cde33efb6e4
--rw-r--r--   0        0        0     1003 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/cfe8a804b0d1388d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d086374488e821f0
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d0c7070297416579
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d0fdd17ab30a03f9
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d15ddb6f796adbef
--rw-r--r--   0        0        0     1003 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d17b1a6a05c0a1a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d18fd7fba26847c9
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d1ad5c9d4566c827
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d1d7baf09faee281
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d2af16d8d7f9174d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d34ea1a3ec3db7c1
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d372d2005aaadcc5
--rw-r--r--   0        0        0      949 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d42b3f28fcca5b92
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d4444ea5bb9c09f8
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d450efd73e841dd1
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d4bb1954ad7242a0
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d4dbb067d602bd38
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d4fc57c121dc2867
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d5185db4ee908681
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d52af40654063af
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d5daf3e0eed7c527
--rw-r--r--   0        0        0     1022 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d5ff022c78ca8bdb
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d66827ce10c895f0
--rw-r--r--   0        0        0      521 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d698a764e2eee095
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d6a88f5f9a69ced
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d825dcc04fc84017
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d838119720bbe81e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d8409cdd3a3a5ff5
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d88af436755e2ce7
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d89a35229fdffab8
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d8b6767dcbee3959
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d92eaed61f00fb5e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d95942274c7caab6
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d959ea6f9a7b172d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/d9aa7d658e741c8b
--rw-r--r--   0        0        0      222 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/da311db2c2885ddd
--rw-r--r--   0        0        0     1003 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/da69e5397a61483b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/da792f8304aff60e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/da9579b8a4f6e6a5
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/daba82336d911f70
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/dac8be7552f4da53
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/dad5a9437ebeb23e
--rw-r--r--   0        0        0     5907 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/dafc0b9cca5a6ec0
--rw-r--r--   0        0        0      427 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/db55ac649ddc5bc2
--rw-r--r--   0        0        0      223 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/db8c48b8f9904250
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/dba5980c5e43519e
--rw-r--r--   0        0        0      324 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/dbd9b4486b3f7673
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/dc6453836ca97a38
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/dc75b3850b1552d6
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/dcbc6da792fb572e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/dd24c73ffa57d7b8
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/dd28e794e49ef05f
--rw-r--r--   0        0        0      324 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/de34d3f79e397211
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/de5b4b6d7c7a4aa0
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/de5b5e9ce0b9af7d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/dee68a08a191d3dc
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/df33118cc8090b02
--rw-r--r--   0        0        0      189 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/df398fd32ef122ec
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/dfbbd2e1ba64adf6
--rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/dff7ac6c8a6da66c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e04122854c1cdee3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e09308b4ad85cda3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e0d2ef3bc1e7748c
--rw-r--r--   0        0        0      172 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e0d536a62d4b470d
--rw-r--r--   0        0        0      210 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e1127e7f518921db
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e150df48399fd335
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e1547d911a29d9df
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e1a0c2e5096f3d5c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e26a4475b9aa0279
--rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e2cf30a40920587a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e2f43c625119ce8
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e2f687397586dd67
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e385bf01937d83f2
--rw-r--r--   0        0        0     3333 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e4058c4aa5da08b2
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e43dee8732cf87c4
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e488b6a1db32f142
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e49cb12e33716f16
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e51cbefebee20fe0
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e5660ca00fa1ccbd
--rw-r--r--   0        0        0      203 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e581852ab9f8268f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e58836765de2dd81
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e5a6c45715c7a4d9
--rw-r--r--   0        0        0      183 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e61a13825345f735
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e628e6fd4e068805
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e64422ad5d7ea0b1
--rw-r--r--   0        0        0      928 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e656067c10d75580
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e68083d35c65831
--rw-r--r--   0        0        0      188 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e73885481f7ea5c3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e7b15d127175a559
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e7c36298702e21d5
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e818ac81e2a75d37
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e841a3b032a527d8
--rw-r--r--   0        0        0      557 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e8bd3b3a333c4df1
--rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e90daf111409ff81
--rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e91d6b7e7d2fe82e
--rw-r--r--   0        0        0      562 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e985bcee084c8ec0
--rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e9b4fe44bf585a4f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/e9dfaf5afeb9bdc5
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ea05db2f6aa05fae
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ea334dfd69e05bd2
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/eaa421c01061b53d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ead128675b3e9163
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/eae976d1ed869354
--rw-r--r--   0        0        0      954 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/eaefa94a9823b2f1
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/eb2da57998ce572a
--rw-r--r--   0        0        0      554 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/eb3d0304cfb9339f
--rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/eba7f2c4ec33748f
--rw-r--r--   0        0        0      252 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ebfabd2d8a1d96f2
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ec0de8a1a9566d0c
--rw-r--r--   0        0        0      757 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ec4d305e85bb4e19
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ec6de6d844bd2657
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ec993b2a0e0b8300
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ec9b28fb8aa4bcd6
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/eca1bc5b38404158
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ed9171a9cc866187
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/edae5907d9b5b7a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/edfc7f2712830945
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ee203332d31c95f1
--rw-r--r--   0        0        0      949 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ee2d09ff4551420d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ee44296492d931ad
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ee5b2f072fe78193
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/efb26f5bf720fc9a
--rw-r--r--   0        0        0      811 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f041520f880369c3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f067cfe7bb78a01
--rw-r--r--   0        0        0      352 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f0a156575a2b5e8f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f0ec8a0f8effcbd
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f144cf764e4cf18f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f1733439bbd00169
--rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f189d1426bad3cc2
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f2147a78b279223d
--rw-r--r--   0        0        0      954 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f22550a5656ee20f
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f226e4fbf4b5a3b3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f241190fc668086f
--rw-r--r--   0        0        0      978 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f27f3c06aa306cb3
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f2fb18698297b6ce
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f3568936f3dedd34
--rw-r--r--   0        0        0     2816 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f387f65a58ab496e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f40ecc88d42de5c7
--rw-r--r--   0        0        0     1156 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f48e1807643594f1
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f5957d85667f204a
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f5ab751f18d8a1e5
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f5f041602121135c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f6213731e01b317c
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f6845a2d4aa7b059
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f6898e64650c2687
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f749c3bb69352870
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f76aeec8a998ee3d
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f7a4501c62c233d4
--rw-r--r--   0        0        0      258 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f805ca4622aaebba
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f93d05bb52180f75
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f9871edc06decb6e
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/f998083de33b36a6
--rw-r--r--   0        0        0      790 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/fa02e62e08abbadb
--rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/fa4db5da0ded9759
--rw-r--r--   0        0        0     2120 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/fa5ccd5562187a1b
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/fa76990547589722
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/fb678d0d18138d93
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/fb734b6eb7cb3578
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/fba563e6c89b93c7
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/fbbdd65488ef4b02
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/fc34d2b3d6a084dd
--rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/fd1bd27b9ad4c831
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/fd90e548022ed645
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.ruff_cache/content/ffa0e62887131f81
--rw-r--r--   0        0        0       17 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/docs/advanced.md
--rw-r--r--   0        0        0      211 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/docs/api.md
--rw-r--r--   0        0        0       14 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/docs/async.md
--rw-r--r--   0        0        0       32 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/docs/custom_api.md
--rw-r--r--   0        0        0       41 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/docs/exceptions.md
--rw-r--r--   0        0        0     2354 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/docs/index.md
--rw-r--r--   0        0        0       20 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/docs/quickstart.md
--rw-r--r--   0        0        0      911 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/docs/css/style.css
--rw-r--r--   0        0        0      132 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/__about__.py
--rw-r--r--   0        0        0     1023 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/__init__.py
--rw-r--r--   0        0        0    14371 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/env.py
--rw-r--r--   0        0        0     1796 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/exceptions.py
--rw-r--r--   0        0        0    11518 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/filter.py
--rw-r--r--   0        0        0    11085 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/lex.py
--rw-r--r--   0        0        0     2513 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/match.py
--rw-r--r--   0        0        0    17562 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/parse.py
--rw-r--r--   0        0        0    11286 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/path.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/py.typed
--rw-r--r--   0        0        0    20229 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/selectors.py
--rw-r--r--   0        0        0     2567 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/stream.py
--rw-r--r--   0        0        0     3650 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/token.py
--rw-r--r--   0        0        0      104 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/function_extensions/__init__.py
--rw-r--r--   0        0        0      364 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/function_extensions/keys.py
--rw-r--r--   0        0        0      313 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/jsonpath/function_extensions/length.py
--rw-r--r--   0        0        0      110 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/__init__.py
--rw-r--r--   0        0        0     2036 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/compliance.py
--rw-r--r--   0        0        0     2550 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/consensus.py
--rw-r--r--   0        0        0     1236 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/test_async.py
--rw-r--r--   0        0        0     1818 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/test_compare.py
--rw-r--r--   0        0        0     1733 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/test_concrete_path.py
--rw-r--r--   0        0        0     3989 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/test_env.py
--rw-r--r--   0        0        0      747 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/test_errors.py
--rw-r--r--   0        0        0     1376 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/test_find.py
--rw-r--r--   0        0        0     2459 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/test_find_compound_path.py
--rw-r--r--   0        0        0    15182 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/test_find_reference.py
--rw-r--r--   0        0        0    12396 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/test_ietf.py
--rw-r--r--   0        0        0     6415 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/test_ietf_comparison.py
--rw-r--r--   0        0        0    38409 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/test_lex.py
--rw-r--r--   0        0        0     1438 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/test_match_api.py
--rw-r--r--   0        0        0     6138 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/test_parse.py
--rw-r--r--   0        0        0     1109 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/test_parse_compound_path.py
--rw-r--r--   0        0        0     1609 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/tests/test_re.py
--rw-r--r--   0        0        0      968 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/.gitignore
--rw-r--r--   0        0        0     1102 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/LICENSE.txt
--rw-r--r--   0        0        0    11215 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/README.md
--rw-r--r--   0        0        0     3575 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/pyproject.toml
--rw-r--r--   0        0        0    12267 2020-02-02 00:00:00.000000 python_jsonpath-0.3.0/PKG-INFO
+-rw-r--r--   0        0        0     1466 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/CHANGELOG.md
+-rw-r--r--   0        0        0     1234 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath.bnf
+-rw-r--r--   0        0        0     1638 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/mkdocs.yml
+-rw-r--r--   0        0        0      413 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.github/workflows/lint.yaml
+-rw-r--r--   0        0        0      807 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.github/workflows/tests.yaml
+-rw-r--r--   0        0        0      417 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.github/workflows/typing.yaml
+-rw-r--r--   0        0        0       34 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/.gitignore
+-rw-r--r--   0        0        0      190 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/CACHEDIR.TAG
+-rw-r--r--   0        0        0        2 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/@plugins_snapshot.json
+-rw-r--r--   0        0        0     8535 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/__future__.data.json
+-rw-r--r--   0        0        0     1713 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/__future__.meta.json
+-rw-r--r--   0        0        0   193712 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_ast.data.json
+-rw-r--r--   0        0        0     1801 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_ast.meta.json
+-rw-r--r--   0        0        0    47115 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_bisect.data.json
+-rw-r--r--   0        0        0     1738 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_bisect.meta.json
+-rw-r--r--   0        0        0    57332 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_codecs.data.json
+-rw-r--r--   0        0        0     1847 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_codecs.meta.json
+-rw-r--r--   0        0        0    19805 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_collections_abc.data.json
+-rw-r--r--   0        0        0     1755 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_collections_abc.meta.json
+-rw-r--r--   0        0        0     3218 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_ctypes.data.json
+-rw-r--r--   0        0        0     1757 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_ctypes.meta.json
+-rw-r--r--   0        0        0   186645 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_decimal.data.json
+-rw-r--r--   0        0        0     1802 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_decimal.meta.json
+-rw-r--r--   0        0        0   122132 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_operator.data.json
+-rw-r--r--   0        0        0     1769 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_operator.meta.json
+-rw-r--r--   0        0        0   148486 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_socket.data.json
+-rw-r--r--   0        0        0     1831 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_socket.meta.json
+-rw-r--r--   0        0        0    21638 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_stat.data.json
+-rw-r--r--   0        0        0     1718 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_stat.meta.json
+-rw-r--r--   0        0        0    26002 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_thread.data.json
+-rw-r--r--   0        0        0     1799 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_thread.meta.json
+-rw-r--r--   0        0        0     8915 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_tracemalloc.data.json
+-rw-r--r--   0        0        0     1770 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_tracemalloc.meta.json
+-rw-r--r--   0        0        0    14348 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_warnings.data.json
+-rw-r--r--   0        0        0     1684 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_warnings.meta.json
+-rw-r--r--   0        0        0    30014 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_weakref.data.json
+-rw-r--r--   0        0        0     1783 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_weakref.meta.json
+-rw-r--r--   0        0        0    55254 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_weakrefset.data.json
+-rw-r--r--   0        0        0     1789 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_weakrefset.meta.json
+-rw-r--r--   0        0        0    22400 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/abc.data.json
+-rw-r--r--   0        0        0     1743 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/abc.meta.json
+-rw-r--r--   0        0        0   165861 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/argparse.data.json
+-rw-r--r--   0        0        0     1846 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/argparse.meta.json
+-rw-r--r--   0        0        0    66417 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/array.data.json
+-rw-r--r--   0        0        0     1810 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/array.meta.json
+-rw-r--r--   0        0        0   149485 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/ast.data.json
+-rw-r--r--   0        0        0     1850 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/ast.meta.json
+-rw-r--r--   0        0        0     8975 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/atexit.data.json
+-rw-r--r--   0        0        0     1729 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/atexit.meta.json
+-rw-r--r--   0        0        0    53914 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/bdb.data.json
+-rw-r--r--   0        0        0     1772 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/bdb.meta.json
+-rw-r--r--   0        0        0    12244 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/bisect.data.json
+-rw-r--r--   0        0        0     1714 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/bisect.meta.json
+-rw-r--r--   0        0        0  1141249 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/builtins.data.json
+-rw-r--r--   0        0        0     1907 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/builtins.meta.json
+-rw-r--r--   0        0        0    22205 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/cmd.data.json
+-rw-r--r--   0        0        0     1724 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/cmd.meta.json
+-rw-r--r--   0        0        0   134253 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/codecs.data.json
+-rw-r--r--   0        0        0     1861 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/codecs.meta.json
+-rw-r--r--   0        0        0    12403 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/compliance.data.json
+-rw-r--r--   0        0        0     1983 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/compliance.meta.json
+-rw-r--r--   0        0        0    15816 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/consensus.data.json
+-rw-r--r--   0        0        0     1940 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/consensus.meta.json
+-rw-r--r--   0        0        0   113711 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/contextlib.data.json
+-rw-r--r--   0        0        0     1785 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/contextlib.meta.json
+-rw-r--r--   0        0        0    41360 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/contextvars.data.json
+-rw-r--r--   0        0        0     1789 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/contextvars.meta.json
+-rw-r--r--   0        0        0     5983 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/copy.data.json
+-rw-r--r--   0        0        0     1673 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/copy.meta.json
+-rw-r--r--   0        0        0    13020 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/copyreg.data.json
+-rw-r--r--   0        0        0     1751 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/copyreg.meta.json
+-rw-r--r--   0        0        0    63291 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/dataclasses.data.json
+-rw-r--r--   0        0        0     1803 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/dataclasses.meta.json
+-rw-r--r--   0        0        0   154597 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/datetime.data.json
+-rw-r--r--   0        0        0     1757 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/datetime.meta.json
+-rw-r--r--   0        0        0     5339 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/decimal.data.json
+-rw-r--r--   0        0        0     1698 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/decimal.meta.json
+-rw-r--r--   0        0        0     2141 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/dev.data.json
+-rw-r--r--   0        0        0     1671 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/dev.meta.json
+-rw-r--r--   0        0        0    63798 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/difflib.data.json
+-rw-r--r--   0        0        0     1754 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/difflib.meta.json
+-rw-r--r--   0        0        0    44123 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/dis.data.json
+-rw-r--r--   0        0        0     1790 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/dis.meta.json
+-rw-r--r--   0        0        0    76249 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/doctest.data.json
+-rw-r--r--   0        0        0     1835 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/doctest.meta.json
+-rw-r--r--   0        0        0    66880 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/enum.data.json
+-rw-r--r--   0        0        0     1775 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/enum.meta.json
+-rw-r--r--   0        0        0    29939 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/errno.data.json
+-rw-r--r--   0        0        0     1716 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/errno.meta.json
+-rw-r--r--   0        0        0     6704 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/fnmatch.data.json
+-rw-r--r--   0        0        0     1704 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/fnmatch.meta.json
+-rw-r--r--   0        0        0   139324 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/functools.data.json
+-rw-r--r--   0        0        0     1784 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/functools.meta.json
+-rw-r--r--   0        0        0    17520 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/gc.data.json
+-rw-r--r--   0        0        0     1756 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/gc.meta.json
+-rw-r--r--   0        0        0    24440 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/genericpath.data.json
+-rw-r--r--   0        0        0     1772 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/genericpath.meta.json
+-rw-r--r--   0        0        0     4120 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/getpass.data.json
+-rw-r--r--   0        0        0     1679 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/getpass.meta.json
+-rw-r--r--   0        0        0    58379 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/gettext.data.json
+-rw-r--r--   0        0        0     1778 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/gettext.meta.json
+-rw-r--r--   0        0        0    10325 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/glob.data.json
+-rw-r--r--   0        0        0     1732 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/glob.meta.json
+-rw-r--r--   0        0        0   370622 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/inspect.data.json
+-rw-r--r--   0        0        0     1834 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/inspect.meta.json
+-rw-r--r--   0        0        0    93299 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/io.data.json
+-rw-r--r--   0        0        0     1866 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/io.meta.json
+-rw-r--r--   0        0        0   292389 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/itertools.data.json
+-rw-r--r--   0        0        0     1786 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/itertools.meta.json
+-rw-r--r--   0        0        0     7024 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/marshal.data.json
+-rw-r--r--   0        0        0     1807 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/marshal.meta.json
+-rw-r--r--   0        0        0    56214 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/math.data.json
+-rw-r--r--   0        0        0     1760 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/math.meta.json
+-rw-r--r--   0        0        0    31546 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/mmap.data.json
+-rw-r--r--   0        0        0     1809 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/mmap.meta.json
+-rw-r--r--   0        0        0    86304 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/numbers.data.json
+-rw-r--r--   0        0        0     1679 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/numbers.meta.json
+-rw-r--r--   0        0        0     6702 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/opcode.data.json
+-rw-r--r--   0        0        0     1740 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/opcode.meta.json
+-rw-r--r--   0        0        0    51078 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/operator.data.json
+-rw-r--r--   0        0        0     1764 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/operator.meta.json
+-rw-r--r--   0        0        0    96614 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/pathlib.data.json
+-rw-r--r--   0        0        0     1875 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/pathlib.meta.json
+-rw-r--r--   0        0        0   102193 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/pdb.data.json
+-rw-r--r--   0        0        0     1862 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/pdb.meta.json
+-rw-r--r--   0        0        0    48580 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/pickle.data.json
+-rw-r--r--   0        0        0     1811 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/pickle.meta.json
+-rw-r--r--   0        0        0    34256 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/pkgutil.data.json
+-rw-r--r--   0        0        0     1781 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/pkgutil.meta.json
+-rw-r--r--   0        0        0    38196 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/platform.data.json
+-rw-r--r--   0        0        0     1716 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/platform.meta.json
+-rw-r--r--   0        0        0    82148 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/posixpath.data.json
+-rw-r--r--   0        0        0     1805 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/posixpath.meta.json
+-rw-r--r--   0        0        0    13186 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/pprint.data.json
+-rw-r--r--   0        0        0     1712 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/pprint.meta.json
+-rw-r--r--   0        0        0    33321 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/queue.data.json
+-rw-r--r--   0        0        0     1744 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/queue.meta.json
+-rw-r--r--   0        0        0   182961 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/re.data.json
+-rw-r--r--   0        0        0     1897 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/re.meta.json
+-rw-r--r--   0        0        0    18012 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/reprlib.data.json
+-rw-r--r--   0        0        0     1768 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/reprlib.meta.json
+-rw-r--r--   0        0        0    65874 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/selectors.data.json
+-rw-r--r--   0        0        0     1833 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/selectors.meta.json
+-rw-r--r--   0        0        0    17830 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/shlex.data.json
+-rw-r--r--   0        0        0     1762 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/shlex.meta.json
+-rw-r--r--   0        0        0    77644 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/shutil.data.json
+-rw-r--r--   0        0        0     1776 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/shutil.meta.json
+-rw-r--r--   0        0        0    53861 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/signal.data.json
+-rw-r--r--   0        0        0     1792 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/signal.meta.json
+-rw-r--r--   0        0        0   125447 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/socket.data.json
+-rw-r--r--   0        0        0     1884 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/socket.meta.json
+-rw-r--r--   0        0        0    15243 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/sre_compile.data.json
+-rw-r--r--   0        0        0     1741 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/sre_compile.meta.json
+-rw-r--r--   0        0        0    30297 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/sre_constants.data.json
+-rw-r--r--   0        0        0     1753 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/sre_constants.meta.json
+-rw-r--r--   0        0        0    53747 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/sre_parse.data.json
+-rw-r--r--   0        0        0     1805 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/sre_parse.meta.json
+-rw-r--r--   0        0        0   205017 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/ssl.data.json
+-rw-r--r--   0        0        0     1886 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/ssl.meta.json
+-rw-r--r--   0        0        0     7133 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/stat.data.json
+-rw-r--r--   0        0        0     1688 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/stat.meta.json
+-rw-r--r--   0        0        0    28945 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/string.data.json
+-rw-r--r--   0        0        0     1790 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/string.meta.json
+-rw-r--r--   0        0        0    16774 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/struct.data.json
+-rw-r--r--   0        0        0     1787 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/struct.meta.json
+-rw-r--r--   0        0        0   173213 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/subprocess.data.json
+-rw-r--r--   0        0        0     1865 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/subprocess.meta.json
+-rw-r--r--   0        0        0   152190 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/sys.data.json
+-rw-r--r--   0        0        0     1844 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/sys.meta.json
+-rw-r--r--   0        0        0    15836 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/sysconfig.data.json
+-rw-r--r--   0        0        0     1745 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/sysconfig.meta.json
+-rw-r--r--   0        0        0   130364 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tempfile.data.json
+-rw-r--r--   0        0        0     1809 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tempfile.meta.json
+-rw-r--r--   0        0        0    16115 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/test_consensus.data.json
+-rw-r--r--   0        0        0     2152 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/test_consensus.meta.json
+-rw-r--r--   0        0        0    21205 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/textwrap.data.json
+-rw-r--r--   0        0        0     1720 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/textwrap.meta.json
+-rw-r--r--   0        0        0    70568 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/threading.data.json
+-rw-r--r--   0        0        0     1775 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/threading.meta.json
+-rw-r--r--   0        0        0    47500 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/time.data.json
+-rw-r--r--   0        0        0     1734 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/time.meta.json
+-rw-r--r--   0        0        0    16377 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/token.data.json
+-rw-r--r--   0        0        0     1711 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/token.meta.json
+-rw-r--r--   0        0        0    53730 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tokenize.data.json
+-rw-r--r--   0        0        0     1807 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tokenize.meta.json
+-rw-r--r--   0        0        0    56302 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/traceback.data.json
+-rw-r--r--   0        0        0     1784 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/traceback.meta.json
+-rw-r--r--   0        0        0    53926 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tracemalloc.data.json
+-rw-r--r--   0        0        0     1796 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tracemalloc.meta.json
+-rw-r--r--   0        0        0   248547 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/types.data.json
+-rw-r--r--   0        0        0     1816 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/types.meta.json
+-rw-r--r--   0        0        0   444992 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/typing.data.json
+-rw-r--r--   0        0        0     1882 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/typing.meta.json
+-rw-r--r--   0        0        0    73995 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/typing_extensions.data.json
+-rw-r--r--   0        0        0     1806 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/typing_extensions.meta.json
+-rw-r--r--   0        0        0    46044 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unicodedata.data.json
+-rw-r--r--   0        0        0     1748 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unicodedata.meta.json
+-rw-r--r--   0        0        0    36731 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/uuid.data.json
+-rw-r--r--   0        0        0     1814 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/uuid.meta.json
+-rw-r--r--   0        0        0    24199 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/warnings.data.json
+-rw-r--r--   0        0        0     1802 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/warnings.meta.json
+-rw-r--r--   0        0        0   156354 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/weakref.data.json
+-rw-r--r--   0        0        0     1808 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/weakref.meta.json
+-rw-r--r--   0        0        0     2310 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/__init__.data.json
+-rw-r--r--   0        0        0     1693 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/__init__.meta.json
+-rw-r--r--   0        0        0     6551 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_argcomplete.data.json
+-rw-r--r--   0        0        0     1868 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_argcomplete.meta.json
+-rw-r--r--   0        0        0     2910 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_version.data.json
+-rw-r--r--   0        0        0     1676 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_version.meta.json
+-rw-r--r--   0        0        0    54695 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/cacheprovider.data.json
+-rw-r--r--   0        0        0     2614 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/cacheprovider.meta.json
+-rw-r--r--   0        0        0   134350 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/capture.data.json
+-rw-r--r--   0        0        0     2152 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/capture.meta.json
+-rw-r--r--   0        0        0    34465 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/compat.data.json
+-rw-r--r--   0        0        0     2085 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/compat.meta.json
+-rw-r--r--   0        0        0    34297 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/debugging.data.json
+-rw-r--r--   0        0        0     2362 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/debugging.meta.json
+-rw-r--r--   0        0        0     8472 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/deprecated.data.json
+-rw-r--r--   0        0        0     1752 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/deprecated.meta.json
+-rw-r--r--   0        0        0    55831 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/doctest.data.json
+-rw-r--r--   0        0        0     2502 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/doctest.meta.json
+-rw-r--r--   0        0        0   191946 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/fixtures.data.json
+-rw-r--r--   0        0        0     2638 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/fixtures.meta.json
+-rw-r--r--   0        0        0     3599 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/freeze_support.data.json
+-rw-r--r--   0        0        0     1885 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/freeze_support.meta.json
+-rw-r--r--   0        0        0    10149 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/helpconfig.data.json
+-rw-r--r--   0        0        0     2023 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/helpconfig.meta.json
+-rw-r--r--   0        0        0    63301 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/hookspec.data.json
+-rw-r--r--   0        0        0     2269 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/hookspec.meta.json
+-rw-r--r--   0        0        0    75498 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/legacypath.data.json
+-rw-r--r--   0        0        0     2270 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/legacypath.meta.json
+-rw-r--r--   0        0        0    81215 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/logging.data.json
+-rw-r--r--   0        0        0     2418 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/logging.meta.json
+-rw-r--r--   0        0        0    57129 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/main.data.json
+-rw-r--r--   0        0        0     2512 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/main.meta.json
+-rw-r--r--   0        0        0    27956 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/monkeypatch.data.json
+-rw-r--r--   0        0        0     2086 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/monkeypatch.meta.json
+-rw-r--r--   0        0        0    62800 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/nodes.data.json
+-rw-r--r--   0        0        0     2329 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/nodes.meta.json
+-rw-r--r--   0        0        0    32446 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/outcomes.data.json
+-rw-r--r--   0        0        0     2068 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/outcomes.meta.json
+-rw-r--r--   0        0        0    36764 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/pathlib.data.json
+-rw-r--r--   0        0        0     2308 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/pathlib.meta.json
+-rw-r--r--   0        0        0   142763 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/pytester.data.json
+-rw-r--r--   0        0        0     2846 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/pytester.meta.json
+-rw-r--r--   0        0        0     5212 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/pytester_assertions.data.json
+-rw-r--r--   0        0        0     1724 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/pytester_assertions.meta.json
+-rw-r--r--   0        0        0   146190 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/python.data.json
+-rw-r--r--   0        0        0     2713 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/python.meta.json
+-rw-r--r--   0        0        0    55712 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/python_api.data.json
+-rw-r--r--   0        0        0     2158 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/python_api.meta.json
+-rw-r--r--   0        0        0    33297 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/recwarn.data.json
+-rw-r--r--   0        0        0     2036 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/recwarn.meta.json
+-rw-r--r--   0        0        0    53707 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/reports.data.json
+-rw-r--r--   0        0        0     2190 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/reports.meta.json
+-rw-r--r--   0        0        0    55987 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/runner.data.json
+-rw-r--r--   0        0        0     2395 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/runner.meta.json
+-rw-r--r--   0        0        0    12375 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/scope.data.json
+-rw-r--r--   0        0        0     1763 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/scope.meta.json
+-rw-r--r--   0        0        0    15317 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/stash.data.json
+-rw-r--r--   0        0        0     1670 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/stash.meta.json
+-rw-r--r--   0        0        0   109160 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/terminal.data.json
+-rw-r--r--   0        0        0     2675 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/terminal.meta.json
+-rw-r--r--   0        0        0     2132 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/timing.data.json
+-rw-r--r--   0        0        0     1686 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/timing.meta.json
+-rw-r--r--   0        0        0    26596 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/tmpdir.data.json
+-rw-r--r--   0        0        0     2134 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/tmpdir.meta.json
+-rw-r--r--   0        0        0    36750 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/warning_types.data.json
+-rw-r--r--   0        0        0     1821 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/warning_types.meta.json
+-rw-r--r--   0        0        0    13986 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/warnings.data.json
+-rw-r--r--   0        0        0     2160 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/warnings.meta.json
+-rw-r--r--   0        0        0     3113 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_code/__init__.data.json
+-rw-r--r--   0        0        0     1737 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_code/__init__.meta.json
+-rw-r--r--   0        0        0   220670 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_code/code.data.json
+-rw-r--r--   0        0        0     2321 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_code/code.meta.json
+-rw-r--r--   0        0        0    20336 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_code/source.data.json
+-rw-r--r--   0        0        0     1964 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_code/source.meta.json
+-rw-r--r--   0        0        0     2386 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/__init__.data.json
+-rw-r--r--   0        0        0     1711 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/__init__.meta.json
+-rw-r--r--   0        0        0    13443 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/saferepr.data.json
+-rw-r--r--   0        0        0     1739 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/saferepr.meta.json
+-rw-r--r--   0        0        0    17507 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/terminalwriter.data.json
+-rw-r--r--   0        0        0     2073 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/terminalwriter.meta.json
+-rw-r--r--   0        0        0     3326 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/wcwidth.data.json
+-rw-r--r--   0        0        0     1724 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/wcwidth.meta.json
+-rw-r--r--   0        0        0    13939 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/__init__.data.json
+-rw-r--r--   0        0        0     2142 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/__init__.meta.json
+-rw-r--r--   0        0        0    64849 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/rewrite.data.json
+-rw-r--r--   0        0        0     2563 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/rewrite.meta.json
+-rw-r--r--   0        0        0     6505 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/truncate.data.json
+-rw-r--r--   0        0        0     1890 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/truncate.meta.json
+-rw-r--r--   0        0        0    25159 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/util.data.json
+-rw-r--r--   0        0        0     2172 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/util.meta.json
+-rw-r--r--   0        0        0   117357 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/__init__.data.json
+-rw-r--r--   0        0        0     3075 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/__init__.meta.json
+-rw-r--r--   0        0        0    43203 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/argparsing.data.json
+-rw-r--r--   0        0        0     2209 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/argparsing.meta.json
+-rw-r--r--   0        0        0     5229 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/compat.data.json
+-rw-r--r--   0        0        0     1902 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/compat.meta.json
+-rw-r--r--   0        0        0     3322 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/exceptions.data.json
+-rw-r--r--   0        0        0     1718 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/exceptions.meta.json
+-rw-r--r--   0        0        0    10905 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/findpaths.data.json
+-rw-r--r--   0        0        0     2093 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/findpaths.meta.json
+-rw-r--r--   0        0        0    38199 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/mark/__init__.data.json
+-rw-r--r--   0        0        0     2184 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/mark/__init__.meta.json
+-rw-r--r--   0        0        0    39511 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/mark/expression.data.json
+-rw-r--r--   0        0        0     1827 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/mark/expression.meta.json
+-rw-r--r--   0        0        0   138467 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/mark/structures.data.json
+-rw-r--r--   0        0        0     2271 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/mark/structures.meta.json
+-rw-r--r--   0        0        0    97015 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_typeshed/__init__.data.json
+-rw-r--r--   0        0        0     1879 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/_typeshed/__init__.meta.json
+-rw-r--r--   0        0        0    11611 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/__init__.data.json
+-rw-r--r--   0        0        0     2123 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/__init__.meta.json
+-rw-r--r--   0        0        0   108565 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/base_events.data.json
+-rw-r--r--   0        0        0     2070 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/base_events.meta.json
+-rw-r--r--   0        0        0    27668 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/coroutines.data.json
+-rw-r--r--   0        0        0     1788 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/coroutines.meta.json
+-rw-r--r--   0        0        0   210033 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/events.data.json
+-rw-r--r--   0        0        0     2108 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/events.meta.json
+-rw-r--r--   0        0        0     9805 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/exceptions.data.json
+-rw-r--r--   0        0        0     1737 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/exceptions.meta.json
+-rw-r--r--   0        0        0    40154 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/futures.data.json
+-rw-r--r--   0        0        0     1928 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/futures.meta.json
+-rw-r--r--   0        0        0    29214 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/locks.data.json
+-rw-r--r--   0        0        0     1879 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/locks.meta.json
+-rw-r--r--   0        0        0    18741 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/protocols.data.json
+-rw-r--r--   0        0        0     1831 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/protocols.meta.json
+-rw-r--r--   0        0        0    25228 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/queues.data.json
+-rw-r--r--   0        0        0     1767 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/queues.meta.json
+-rw-r--r--   0        0        0     5102 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/runners.data.json
+-rw-r--r--   0        0        0     1826 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/runners.meta.json
+-rw-r--r--   0        0        0     4174 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/selector_events.data.json
+-rw-r--r--   0        0        0     1805 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/selector_events.meta.json
+-rw-r--r--   0        0        0    37974 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/streams.data.json
+-rw-r--r--   0        0        0     1937 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/streams.meta.json
+-rw-r--r--   0        0        0    26112 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/subprocess.data.json
+-rw-r--r--   0        0        0     1947 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/subprocess.meta.json
+-rw-r--r--   0        0        0   109223 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/tasks.data.json
+-rw-r--r--   0        0        0     1928 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/tasks.meta.json
+-rw-r--r--   0        0        0     6126 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/threads.data.json
+-rw-r--r--   0        0        0     1747 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/threads.meta.json
+-rw-r--r--   0        0        0    29802 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/transports.data.json
+-rw-r--r--   0        0        0     1794 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/transports.meta.json
+-rw-r--r--   0        0        0    63978 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/unix_events.data.json
+-rw-r--r--   0        0        0     1912 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/unix_events.meta.json
+-rw-r--r--   0        0        0   223623 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/__init__.data.json
+-rw-r--r--   0        0        0     1920 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/__init__.meta.json
+-rw-r--r--   0        0        0     4322 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/_cmp.data.json
+-rw-r--r--   0        0        0     1662 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/_cmp.meta.json
+-rw-r--r--   0        0        0     3313 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/_typing_compat.data.json
+-rw-r--r--   0        0        0     1682 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/_typing_compat.meta.json
+-rw-r--r--   0        0        0     7639 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/_version_info.data.json
+-rw-r--r--   0        0        0     1681 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/_version_info.meta.json
+-rw-r--r--   0        0        0     9100 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/converters.data.json
+-rw-r--r--   0        0        0     1688 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/converters.meta.json
+-rw-r--r--   0        0        0    11101 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/exceptions.data.json
+-rw-r--r--   0        0        0     1674 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/exceptions.meta.json
+-rw-r--r--   0        0        0     3906 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/filters.data.json
+-rw-r--r--   0        0        0     1682 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/filters.meta.json
+-rw-r--r--   0        0        0     8438 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/setters.data.json
+-rw-r--r--   0        0        0     1682 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/setters.meta.json
+-rw-r--r--   0        0        0    45673 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/validators.data.json
+-rw-r--r--   0        0        0     1724 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/attr/validators.meta.json
+-rw-r--r--   0        0        0   446306 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/collections/__init__.data.json
+-rw-r--r--   0        0        0     1890 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/collections/__init__.meta.json
+-rw-r--r--   0        0        0     4080 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/collections/abc.data.json
+-rw-r--r--   0        0        0     1721 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/collections/abc.meta.json
+-rw-r--r--   0        0        0     1703 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/__init__.data.json
+-rw-r--r--   0        0        0     1693 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/__init__.meta.json
+-rw-r--r--   0        0        0     4944 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/__init__.data.json
+-rw-r--r--   0        0        0     1852 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/__init__.meta.json
+-rw-r--r--   0        0        0    65942 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/_base.data.json
+-rw-r--r--   0        0        0     1851 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/_base.meta.json
+-rw-r--r--   0        0        0    65238 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/process.data.json
+-rw-r--r--   0        0        0     2095 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/process.meta.json
+-rw-r--r--   0        0        0    23847 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/thread.data.json
+-rw-r--r--   0        0        0     1896 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/thread.meta.json
+-rw-r--r--   0        0        0   140979 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/ctypes/__init__.data.json
+-rw-r--r--   0        0        0     1853 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/ctypes/__init__.meta.json
+-rw-r--r--   0        0        0     8166 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/email/__init__.data.json
+-rw-r--r--   0        0        0     1782 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/email/__init__.meta.json
+-rw-r--r--   0        0        0    13318 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/email/charset.data.json
+-rw-r--r--   0        0        0     1718 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/email/charset.meta.json
+-rw-r--r--   0        0        0     7940 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/email/contentmanager.data.json
+-rw-r--r--   0        0        0     1753 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/email/contentmanager.meta.json
+-rw-r--r--   0        0        0    27031 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/email/errors.data.json
+-rw-r--r--   0        0        0     1725 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/email/errors.meta.json
+-rw-r--r--   0        0        0    10032 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/email/header.data.json
+-rw-r--r--   0        0        0     1738 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/email/header.meta.json
+-rw-r--r--   0        0        0    86534 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/email/message.data.json
+-rw-r--r--   0        0        0     1856 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/email/message.meta.json
+-rw-r--r--   0        0        0    33617 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/email/policy.data.json
+-rw-r--r--   0        0        0     1811 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/email/policy.meta.json
+-rw-r--r--   0        0        0     3541 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/__init__.data.json
+-rw-r--r--   0        0        0     1870 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/__init__.meta.json
+-rw-r--r--   0        0        0     9643 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_catch.data.json
+-rw-r--r--   0        0        0     1837 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_catch.meta.json
+-rw-r--r--   0        0        0    72892 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_exceptions.data.json
+-rw-r--r--   0        0        0     1858 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_exceptions.meta.json
+-rw-r--r--   0        0        0    24915 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_formatting.data.json
+-rw-r--r--   0        0        0     2006 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_formatting.meta.json
+-rw-r--r--   0        0        0     2987 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_version.data.json
+-rw-r--r--   0        0        0     1690 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_version.meta.json
+-rw-r--r--   0        0        0     6726 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/__init__.data.json
+-rw-r--r--   0        0        0     1756 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/__init__.meta.json
+-rw-r--r--   0        0        0    75571 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/abc.data.json
+-rw-r--r--   0        0        0     1839 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/abc.meta.json
+-rw-r--r--   0        0        0    69972 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/machinery.data.json
+-rw-r--r--   0        0        0     1915 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/machinery.meta.json
+-rw-r--r--   0        0        0    23604 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/util.data.json
+-rw-r--r--   0        0        0     1920 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/util.meta.json
+-rw-r--r--   0        0        0    97938 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/metadata/__init__.data.json
+-rw-r--r--   0        0        0     1921 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/metadata/__init__.meta.json
+-rw-r--r--   0        0        0    12976 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/metadata/_meta.data.json
+-rw-r--r--   0        0        0     1738 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/metadata/_meta.meta.json
+-rw-r--r--   0        0        0    49033 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/iniconfig/__init__.data.json
+-rw-r--r--   0        0        0     1825 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/iniconfig/__init__.meta.json
+-rw-r--r--   0        0        0    24799 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/iniconfig/_parse.data.json
+-rw-r--r--   0        0        0     1754 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/iniconfig/_parse.meta.json
+-rw-r--r--   0        0        0     5089 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/iniconfig/exceptions.data.json
+-rw-r--r--   0        0        0     1731 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/iniconfig/exceptions.meta.json
+-rw-r--r--   0        0        0    16901 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/json/__init__.data.json
+-rw-r--r--   0        0        0     1771 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/json/__init__.meta.json
+-rw-r--r--   0        0        0    15868 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/json/decoder.data.json
+-rw-r--r--   0        0        0     1715 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/json/decoder.meta.json
+-rw-r--r--   0        0        0    11890 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/json/encoder.data.json
+-rw-r--r--   0        0        0     1727 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/json/encoder.meta.json
+-rw-r--r--   0        0        0     1662 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/__about__.data.json
+-rw-r--r--   0        0        0     1623 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/__about__.meta.json
+-rw-r--r--   0        0        0     9974 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/__init__.data.json
+-rw-r--r--   0        0        0     1760 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/__init__.meta.json
+-rw-r--r--   0        0        0    30097 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/cache.data.json
+-rw-r--r--   0        0        0     1699 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/cache.meta.json
+-rw-r--r--   0        0        0    23898 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/env.data.json
+-rw-r--r--   0        0        0     2253 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/env.meta.json
+-rw-r--r--   0        0        0    10482 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/exceptions.data.json
+-rw-r--r--   0        0        0     1697 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/exceptions.meta.json
+-rw-r--r--   0        0        0    79386 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/filter.data.json
+-rw-r--r--   0        0        0     1943 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/filter.meta.json
+-rw-r--r--   0        0        0    18309 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/lex.data.json
+-rw-r--r--   0        0        0     1776 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/lex.meta.json
+-rw-r--r--   0        0        0    30729 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/lru_cache.data.json
+-rw-r--r--   0        0        0     1707 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/lru_cache.meta.json
+-rw-r--r--   0        0        0    11601 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/match.data.json
+-rw-r--r--   0        0        0     1727 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/match.meta.json
+-rw-r--r--   0        0        0    38082 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/parse.data.json
+-rw-r--r--   0        0        0     1996 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/parse.meta.json
+-rw-r--r--   0        0        0    27075 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/path.data.json
+-rw-r--r--   0        0        0     1851 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/path.meta.json
+-rw-r--r--   0        0        0    52302 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/selectors.data.json
+-rw-r--r--   0        0        0     1900 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/selectors.meta.json
+-rw-r--r--   0        0        0    15219 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/stream.data.json
+-rw-r--r--   0        0        0     1730 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/stream.meta.json
+-rw-r--r--   0        0        0    21620 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/token.data.json
+-rw-r--r--   0        0        0     1672 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/token.meta.json
+-rw-r--r--   0        0        0     2635 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/function_extensions/__init__.data.json
+-rw-r--r--   0        0        0     1739 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/function_extensions/__init__.meta.json
+-rw-r--r--   0        0        0     2774 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/function_extensions/keys.data.json
+-rw-r--r--   0        0        0     1651 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/function_extensions/keys.meta.json
+-rw-r--r--   0        0        0     2515 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/function_extensions/length.data.json
+-rw-r--r--   0        0        0     1680 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/function_extensions/length.meta.json
+-rw-r--r--   0        0        0   154308 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/logging/__init__.data.json
+-rw-r--r--   0        0        0     1879 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/logging/__init__.meta.json
+-rw-r--r--   0        0        0    34085 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/__init__.data.json
+-rw-r--r--   0        0        0     2164 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/__init__.meta.json
+-rw-r--r--   0        0        0    33275 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/connection.data.json
+-rw-r--r--   0        0        0     1919 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/connection.meta.json
+-rw-r--r--   0        0        0   103634 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/context.data.json
+-rw-r--r--   0        0        0     2328 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/context.meta.json
+-rw-r--r--   0        0        0   160927 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/managers.data.json
+-rw-r--r--   0        0        0     1961 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/managers.meta.json
+-rw-r--r--   0        0        0    56176 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/pool.data.json
+-rw-r--r--   0        0        0     1807 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/pool.meta.json
+-rw-r--r--   0        0        0     9823 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_fork.data.json
+-rw-r--r--   0        0        0     1794 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_fork.meta.json
+-rw-r--r--   0        0        0     6247 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_forkserver.data.json
+-rw-r--r--   0        0        0     1836 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_forkserver.meta.json
+-rw-r--r--   0        0        0     6968 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_spawn_posix.data.json
+-rw-r--r--   0        0        0     1838 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_spawn_posix.meta.json
+-rw-r--r--   0        0        0     2176 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_spawn_win32.data.json
+-rw-r--r--   0        0        0     1808 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_spawn_win32.meta.json
+-rw-r--r--   0        0        0    19246 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/process.data.json
+-rw-r--r--   0        0        0     1771 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/process.meta.json
+-rw-r--r--   0        0        0    21492 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/queues.data.json
+-rw-r--r--   0        0        0     1775 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/queues.meta.json
+-rw-r--r--   0        0        0    31449 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/reduction.data.json
+-rw-r--r--   0        0        0     1981 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/reduction.meta.json
+-rw-r--r--   0        0        0    31860 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/shared_memory.data.json
+-rw-r--r--   0        0        0     1825 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/shared_memory.meta.json
+-rw-r--r--   0        0        0    73309 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/sharedctypes.data.json
+-rw-r--r--   0        0        0     1896 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/sharedctypes.meta.json
+-rw-r--r--   0        0        0    10735 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/spawn.data.json
+-rw-r--r--   0        0        0     1747 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/spawn.meta.json
+-rw-r--r--   0        0        0    27932 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/synchronize.data.json
+-rw-r--r--   0        0        0     1861 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/synchronize.meta.json
+-rw-r--r--   0        0        0    25682 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/util.data.json
+-rw-r--r--   0        0        0     1879 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/util.meta.json
+-rw-r--r--   0        0        0   382629 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/os/__init__.data.json
+-rw-r--r--   0        0        0     1924 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/os/__init__.meta.json
+-rw-r--r--   0        0        0     5359 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/os/path.data.json
+-rw-r--r--   0        0        0     1713 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/os/path.meta.json
+-rw-r--r--   0        0        0     3505 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/__init__.data.json
+-rw-r--r--   0        0        0     1671 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/__init__.meta.json
+-rw-r--r--   0        0        0    15307 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_elffile.data.json
+-rw-r--r--   0        0        0     1822 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_elffile.meta.json
+-rw-r--r--   0        0        0    29701 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_manylinux.data.json
+-rw-r--r--   0        0        0     2034 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_manylinux.meta.json
+-rw-r--r--   0        0        0    20244 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_musllinux.data.json
+-rw-r--r--   0        0        0     1945 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_musllinux.meta.json
+-rw-r--r--   0        0        0    48258 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_parser.data.json
+-rw-r--r--   0        0        0     1865 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_parser.meta.json
+-rw-r--r--   0        0        0    15161 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_structures.data.json
+-rw-r--r--   0        0        0     1703 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_structures.meta.json
+-rw-r--r--   0        0        0    19444 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_tokenizer.data.json
+-rw-r--r--   0        0        0     1811 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_tokenizer.meta.json
+-rw-r--r--   0        0        0    19626 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/markers.data.json
+-rw-r--r--   0        0        0     1980 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/markers.meta.json
+-rw-r--r--   0        0        0     9773 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/requirements.data.json
+-rw-r--r--   0        0        0     1945 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/requirements.meta.json
+-rw-r--r--   0        0        0    61359 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/specifiers.data.json
+-rw-r--r--   0        0        0     1920 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/specifiers.meta.json
+-rw-r--r--   0        0        0    31130 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/tags.data.json
+-rw-r--r--   0        0        0     2010 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/tags.meta.json
+-rw-r--r--   0        0        0    11150 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/utils.data.json
+-rw-r--r--   0        0        0     1882 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/utils.meta.json
+-rw-r--r--   0        0        0    71300 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/version.data.json
+-rw-r--r--   0        0        0     1914 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/version.meta.json
+-rw-r--r--   0        0        0    12002 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/pytest/__init__.data.json
+-rw-r--r--   0        0        0     2384 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/pytest/__init__.meta.json
+-rw-r--r--   0        0        0     1584 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/__init__.data.json
+-rw-r--r--   0        0        0     1605 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/__init__.meta.json
+-rw-r--r--   0        0        0    12577 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/compliance.data.json
+-rw-r--r--   0        0        0     1951 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/compliance.meta.json
+-rw-r--r--   0        0        0    16020 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/consensus.data.json
+-rw-r--r--   0        0        0     1952 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/consensus.meta.json
+-rw-r--r--   0        0        0     8519 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_async.data.json
+-rw-r--r--   0        0        0     1676 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_async.meta.json
+-rw-r--r--   0        0        0     9885 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_compare.data.json
+-rw-r--r--   0        0        0     1870 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_compare.meta.json
+-rw-r--r--   0        0        0     9095 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_compound_path.data.json
+-rw-r--r--   0        0        0     1971 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_compound_path.meta.json
+-rw-r--r--   0        0        0    13101 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_concrete_path.data.json
+-rw-r--r--   0        0        0     1948 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_concrete_path.meta.json
+-rw-r--r--   0        0        0    12323 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_env.data.json
+-rw-r--r--   0        0        0     1786 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_env.meta.json
+-rw-r--r--   0        0        0     5445 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_errors.data.json
+-rw-r--r--   0        0        0     1943 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_errors.meta.json
+-rw-r--r--   0        0        0    13512 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_find.data.json
+-rw-r--r--   0        0        0     1907 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_find.meta.json
+-rw-r--r--   0        0        0    14142 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_find_compound_path.data.json
+-rw-r--r--   0        0        0     1960 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_find_compound_path.meta.json
+-rw-r--r--   0        0        0    14360 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_find_reference.data.json
+-rw-r--r--   0        0        0     1928 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_find_reference.meta.json
+-rw-r--r--   0        0        0    13985 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_ietf.data.json
+-rw-r--r--   0        0        0     1912 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_ietf.meta.json
+-rw-r--r--   0        0        0    10659 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_ietf_comparison.data.json
+-rw-r--r--   0        0        0     1916 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_ietf_comparison.meta.json
+-rw-r--r--   0        0        0    15542 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_lex.data.json
+-rw-r--r--   0        0        0     2054 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_lex.meta.json
+-rw-r--r--   0        0        0     4926 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_match_api.data.json
+-rw-r--r--   0        0        0     1737 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_match_api.meta.json
+-rw-r--r--   0        0        0     8852 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_parse.data.json
+-rw-r--r--   0        0        0     1955 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_parse.meta.json
+-rw-r--r--   0        0        0     9251 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_parse_compound_path.data.json
+-rw-r--r--   0        0        0     1983 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_parse_compound_path.meta.json
+-rw-r--r--   0        0        0    13562 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_re.data.json
+-rw-r--r--   0        0        0     1903 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_re.meta.json
+-rw-r--r--   0        0        0     2823 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/__init__.data.json
+-rw-r--r--   0        0        0     1686 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/__init__.meta.json
+-rw-r--r--   0        0        0    57353 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/_parser.data.json
+-rw-r--r--   0        0        0     1937 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/_parser.meta.json
+-rw-r--r--   0        0        0     7696 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/_re.data.json
+-rw-r--r--   0        0        0     1884 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/_re.meta.json
+-rw-r--r--   0        0        0     2994 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/_types.data.json
+-rw-r--r--   0        0        0     1780 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/_types.meta.json
+-rw-r--r--   0        0        0     6509 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/__init__.data.json
+-rw-r--r--   0        0        0     1933 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/__init__.meta.json
+-rw-r--r--   0        0        0    26185 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/_log.data.json
+-rw-r--r--   0        0        0     1781 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/_log.meta.json
+-rw-r--r--   0        0        0     8320 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/async_case.data.json
+-rw-r--r--   0        0        0     1812 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/async_case.meta.json
+-rw-r--r--   0        0        0   225927 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/case.data.json
+-rw-r--r--   0        0        0     1932 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/case.meta.json
+-rw-r--r--   0        0        0    15920 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/loader.data.json
+-rw-r--r--   0        0        0     1843 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/loader.meta.json
+-rw-r--r--   0        0        0    12793 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/main.data.json
+-rw-r--r--   0        0        0     1852 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/main.meta.json
+-rw-r--r--   0        0        0    22448 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/result.data.json
+-rw-r--r--   0        0        0     1799 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/result.meta.json
+-rw-r--r--   0        0        0    11709 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/runner.data.json
+-rw-r--r--   0        0        0     1842 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/runner.meta.json
+-rw-r--r--   0        0        0    12371 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/signals.data.json
+-rw-r--r--   0        0        0     1794 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/signals.meta.json
+-rw-r--r--   0        0        0    12264 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/suite.data.json
+-rw-r--r--   0        0        0     1815 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/suite.meta.json
+-rw-r--r--   0        0        0     1671 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/urllib/__init__.data.json
+-rw-r--r--   0        0        0     1685 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/urllib/__init__.meta.json
+-rw-r--r--   0        0        0   166629 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/urllib/parse.data.json
+-rw-r--r--   0        0        0     1791 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/urllib/parse.meta.json
+-rw-r--r--   0        0        0   121554 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/__init__.data.json
+-rw-r--r--   0        0        0     2140 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/__init__.meta.json
+-rw-r--r--   0        0        0    24543 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/_yaml.data.json
+-rw-r--r--   0        0        0     1777 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/_yaml.meta.json
+-rw-r--r--   0        0        0    11530 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/composer.data.json
+-rw-r--r--   0        0        0     1716 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/composer.meta.json
+-rw-r--r--   0        0        0    49399 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/constructor.data.json
+-rw-r--r--   0        0        0     1984 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/constructor.meta.json
+-rw-r--r--   0        0        0    21339 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/cyaml.data.json
+-rw-r--r--   0        0        0     1837 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/cyaml.meta.json
+-rw-r--r--   0        0        0    13980 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/dumper.data.json
+-rw-r--r--   0        0        0     1886 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/dumper.meta.json
+-rw-r--r--   0        0        0    40195 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/emitter.data.json
+-rw-r--r--   0        0        0     1695 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/emitter.meta.json
+-rw-r--r--   0        0        0     9503 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/error.data.json
+-rw-r--r--   0        0        0     1671 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/error.meta.json
+-rw-r--r--   0        0        0    29716 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/events.data.json
+-rw-r--r--   0        0        0     1673 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/events.meta.json
+-rw-r--r--   0        0        0    12948 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/loader.data.json
+-rw-r--r--   0        0        0     1857 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/loader.meta.json
+-rw-r--r--   0        0        0    11495 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/nodes.data.json
+-rw-r--r--   0        0        0     1691 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/nodes.meta.json
+-rw-r--r--   0        0        0    15809 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/parser.data.json
+-rw-r--r--   0        0        0     1693 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/parser.meta.json
+-rw-r--r--   0        0        0    13816 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/reader.data.json
+-rw-r--r--   0        0        0     1739 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/reader.meta.json
+-rw-r--r--   0        0        0    45238 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/representer.data.json
+-rw-r--r--   0        0        0     1866 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/representer.meta.json
+-rw-r--r--   0        0        0    11407 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/resolver.data.json
+-rw-r--r--   0        0        0     1696 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/resolver.meta.json
+-rw-r--r--   0        0        0    33040 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/scanner.data.json
+-rw-r--r--   0        0        0     1695 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/scanner.meta.json
+-rw-r--r--   0        0        0    10954 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/serializer.data.json
+-rw-r--r--   0        0        0     1720 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/serializer.meta.json
+-rw-r--r--   0        0        0    37858 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/tokens.data.json
+-rw-r--r--   0        0        0     1673 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/tokens.meta.json
+-rw-r--r--   0        0        0        1 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/.gitignore
+-rw-r--r--   0        0        0       43 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/CACHEDIR.TAG
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1086d708790bd7cb
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1095cfed48560a97
+-rw-r--r--   0        0        0      418 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/111b0167a96f6cc7
+-rw-r--r--   0        0        0      701 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/113169384d5668bc
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/118e0978578f504e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1194388bc2c6baed
+-rw-r--r--   0        0        0      172 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/12377713d939dcce
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/12400f2018249ea1
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1258567092747a21
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1270beb4a704eea6
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1299bbf057d49d1b
+-rw-r--r--   0        0        0      949 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/135ad1453038c1a4
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/136827364eb7fe04
+-rw-r--r--   0        0        0      619 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1398303151225940
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/141ec2f392f2feeb
+-rw-r--r--   0        0        0      542 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/146653dc356f145a
+-rw-r--r--   0        0        0      418 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/14dd1f452892a317
+-rw-r--r--   0        0        0      806 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/15a3b5713a8c7860
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/15b9c3a8a742cdc4
+-rw-r--r--   0        0        0     1950 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1627d49e057ce6ef
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/16ea129bd35da7e5
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/16f052bbad634acd
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/16f894a8f3d0ffa
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1798db5f67f7f187
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/183eb2a303a637d1
+-rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/18865323e91b9a48
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/18f9cfd05e11f802
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1912fc58846c4806
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/19251d1cac3e6a15
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/19f9dbab59d2f02
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1a4b835101dd193a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1a64b11bec7288b2
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1aa5f6cdf3cdc302
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1ab58d9baeae7870
+-rw-r--r--   0        0        0      933 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1acf71e60d0cb21f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1b87153e310c0754
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1ba222bd6e162120
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1c2dad708442985
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1c406ce7037979ad
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1cad9d23fc0d3206
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1cd53a45ebc7a75a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1d937bc359ec3abd
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1df5534d9f64a95c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1e427db86b0cd407
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1e51102ab3677167
+-rw-r--r--   0        0        0      572 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1f12aa22fe2f769c
+-rw-r--r--   0        0        0     2890 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1f3b04ff651c8c80
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/1f720660e81d1e1d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/209d42dd15df5c72
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/20e120991f075171
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/20f16d13ac88b02e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2111b4b6f4a44c5f
+-rw-r--r--   0        0        0     1950 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/213493565c60d69e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2152120114ecb71
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/216a9723a151eed9
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2170e3da77488531
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/217fbafea45e521e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/21de75bac5dc9797
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/229b06339539ba4a
+-rw-r--r--   0        0        0      418 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/22a642bcc6ca170
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/22ed7c05b59c4cad
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/23d3de9fa792bee6
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/248a178f46f844ae
+-rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/24a2cbc527b75aca
+-rw-r--r--   0        0        0     1076 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/253e03a0e43afe2
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2544df6ae7edeccc
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/255187ca88b13246
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/258699e02b41255a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/25e251f9e5aaa70e
+-rw-r--r--   0        0        0     1740 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/26a981bb502f16f
+-rw-r--r--   0        0        0      437 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/26bce6500eb7b3ce
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/27100733e2a4621b
+-rw-r--r--   0        0        0      370 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2720ed943792ec88
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/277c0cc985f81327
+-rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2781e76e5ea0bbd7
+-rw-r--r--   0        0        0      959 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/279262a136b9c91b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/27fc17fc71036c10
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2892468c677836ba
+-rw-r--r--   0        0        0      740 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/28b9e8854f3bba14
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/28f3c9bf44f18483
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2900d3b370e1865
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/291d0ac06dd74aeb
+-rw-r--r--   0        0        0      204 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/29771511a6d4c073
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/29ac638f5175988a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/29ad0a3a3ff1699
+-rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/29c2a04fee34345e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2a061adb62b9481
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2a16c0754fecdcf8
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2a22c874601c5ca7
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2ac255a8c1f48cdc
+-rw-r--r--   0        0        0      978 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2b1ae2f56430e88e
+-rw-r--r--   0        0        0      418 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2b1b36045a55211
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2b394cbcee977c74
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2b41efeadbe99433
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2b4673461b969d8c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2b4da1c4e5824b85
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2b4fc49dfe9f187
+-rw-r--r--   0        0        0     2328 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2b9fda870d662d61
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2bde3cdc25b7d710
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2bebb327b756c7fb
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2c428dcdacbe94cf
+-rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2cd4097fac035fda
+-rw-r--r--   0        0        0      192 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2ce97208c008f223
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2cf0e9bbd2feb95c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2d2e35e1b6bf4cc3
+-rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2d32ff4c07d4445b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2d5ac14578beee6f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2e4034ac2f40858b
+-rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2e8fc72ab83c7ee4
+-rw-r--r--   0        0        0     3175 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2ea0f9311fceda9f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2eb3a5b114e26e97
+-rw-r--r--   0        0        0      162 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2ec8cb89e5035179
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2ee6d2d6297778d4
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2f13cf8b06bed35c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2f79b37103e9badf
+-rw-r--r--   0        0        0      562 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2f7a4bad2663cc7a
+-rw-r--r--   0        0        0      959 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2f7a9dea88b592c6
+-rw-r--r--   0        0        0      214 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2f9146e9f9c91006
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2fb02999c97ff934
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2fb7c2500f2ffd3f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2fe66c4c0f4b723
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/2fed8ec074fc58e0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/30171b9362f7f695
+-rw-r--r--   0        0        0     2150 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3064bcb187e4005b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/306810d0d5443a1b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/30be7b7f111100ba
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/31110c4d4e4f9ac5
+-rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/31281e8df2fc9f77
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/31e1f054541ab85
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/323a3f35d70bff79
+-rw-r--r--   0        0        0      757 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/325e27582ba6b00b
+-rw-r--r--   0        0        0      619 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3278cae1025f408d
+-rw-r--r--   0        0        0      210 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/32c1a82391d8367b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/33480e6566e1d7c1
+-rw-r--r--   0        0        0      208 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3358f600210bb04a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3441b738d2b0768b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/34a7385bd4a66d39
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/34d6a99ba114971
+-rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/34e6cdb48c8892b
+-rw-r--r--   0        0        0      245 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/35040e5c80ebeb9e
+-rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/354222da09a71a22
+-rw-r--r--   0        0        0      619 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/35570cbe6251c078
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/358e4f0467afdb30
+-rw-r--r--   0        0        0     2807 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/35acb2ea313c1f4f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/36091467cb493eb8
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/36494dfc908b7300
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3666724fba65f564
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3735dc080d45a6b3
+-rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/37825382b5dfcb8d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/378a61082f794bdf
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/379721ba1b034669
+-rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/37bba804cab5dbb7
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/37be7672ebb3934f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/383b28009a5701d6
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/384d04ecd4e021b4
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/389bf92f08a98081
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/38a2aa5ed389e590
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/397154cc7b2781
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/39f2b6610b879568
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3ae2176d9bcce237
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3b9460a7c0321145
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3bd9178cfbe94bfa
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3bfe16a0c38493c1
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3c0aa158352075c8
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3c516481a66f5cd9
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3ca80de959c93950
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3cd3e0fbac79ac0d
+-rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3d1f764c0b668f34
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3d4aeb1458f80400
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3d5e480abdb6a621
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3d9e19973cc2bae
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3da8a47ff799c54
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3daf1415edc12a26
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3db75912b5c24118
+-rw-r--r--   0        0        0      415 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3e789340219028bd
+-rw-r--r--   0        0        0      395 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3ec6c72e84642dcb
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3ef2e5d227900cdf
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3efad478150dd3aa
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3f7fb0dc065162de
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3f8ac2e7add0dc8e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3fbb4a2ee4e9615d
+-rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/3fc5b0398b43cb60
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4018c951df86c3a3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/40beb5d646e80b08
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/41015793dc1b0750
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4104307b2b3f3735
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/411cbeb7fcb715fc
+-rw-r--r--   0        0        0      227 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/412bd35d840f2795
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/414641f0374b0b77
+-rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4169c686ca27018c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/416fffc67f569700
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/417079b15ca0f5fc
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/41f0c083b0a1a031
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/420cb90c9ca663e9
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/420fc333c545e403
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4229f954fa4105b0
+-rw-r--r--   0        0        0      172 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4295e7e21d302771
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/42ae413f64cff3ab
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/42e698f34ac38404
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/43d71279a69c387a
+-rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/44ddbc02cc145fa
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/44dfaa68f2ba2228
+-rw-r--r--   0        0        0      352 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4536802fc67ba11c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/461a0932070c0e05
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4657d4c259f5984d
+-rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/47f87d838c0e9070
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4814c2acf8896584
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4832d7b52b9d9234
+-rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/483b7bbda285fbb7
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/48bedf78c55dae3e
+-rw-r--r--   0        0        0      162 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/48fb486af7dae3e6
+-rw-r--r--   0        0        0      572 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/492ebdc8ce6d7aaa
+-rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/493a5437e25c6d20
+-rw-r--r--   0        0        0      211 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/49c438c12f0b8c7e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4a32f124e06b5b01
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4a865a25bc9574c3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4ab4ba297550d4c7
+-rw-r--r--   0        0        0      256 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4b155c6e55c6d7ca
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4b32c4463816c77c
+-rw-r--r--   0        0        0      959 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4c10a12091591533
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4c5bcee61357273e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4c6f9e4364a16a1b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4d19bb63ef7037ee
+-rw-r--r--   0        0        0      204 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4d6c12702373cc27
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4edd21956339b566
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4ef388ab14295e2d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4ef7138cff1b40c0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4f1e1949fdb71b59
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4f4a24feeb57f841
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4f98d65b183ac998
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/4fc48ee6c13f2e3c
+-rw-r--r--   0        0        0      954 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/501fd54946953b5c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5031198fa0e3d1cc
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/50597d25025e0e26
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/50c72d73128ddbe6
+-rw-r--r--   0        0        0     1576 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/510acc3260e58d67
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/515fa1c3637379ca
+-rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/51a39a4ab0b9e5a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/51acea567b417629
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/52065d40a908b367
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/52425e9a986550b5
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5263b01b3d3daa77
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/529476b9008473e2
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/52d60cf06915d9e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/53095686dc94179a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/534c1288997f241a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/53a9f56c3efc5e48
+-rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/540a4ae1823a85e7
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/54a82afe60eb64df
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/54b58d54bee394af
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/54c99a8f739a1a59
+-rw-r--r--   0        0        0      172 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/551e44d1d3ec5665
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/55f6e65978cfb075
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/55f81727c24ac0a4
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/56147e569457954c
+-rw-r--r--   0        0        0      190 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/571181d5345e2050
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/57eb892b6c4c3c1b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/580b1aa14be37639
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/58171af34ea511ef
+-rw-r--r--   0        0        0     2150 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/582fc01eaccf9d11
+-rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/58e0fd9241ecf02e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5a1be3b2245cd0f2
+-rw-r--r--   0        0        0      223 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5a24ded2aa2852d
+-rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5a396375009eba92
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5b8c4c1ad20e5f75
+-rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5c6e80b5464ae96
+-rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5cacc766c4597689
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5cd52bc852538304
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5d23cbb3e545c0c9
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5d5b4dcbf5bc4b45
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5d6de0ef8fd1c8c3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5df021e329be9624
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5dfa93b6e0c2e6c6
+-rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5e29d098bb1ecc0a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5e61bd53ae508a35
+-rw-r--r--   0        0        0      198 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5e977bb5e72fd54c
+-rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5e9e67c9beead0c5
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5f6b0ae9017aec8
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5f78b9f97703b97b
+-rw-r--r--   0        0        0      554 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5f8db1660501e234
+-rw-r--r--   0        0        0      418 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/5feb5ced1cfb0726
+-rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/60943986c63e73b3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/60c8a925b11d461a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6159341561bf659f
+-rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6164c8374827eb66
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/618068a750f4b11f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/618d0b6aa2a4dee7
+-rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/619d75195853621
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6266f52e9af39a30
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/62cb483937d88136
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6316e7293ca1b89e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6365bd43ffa9ce0d
+-rw-r--r--   0        0        0      217 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/63b5f94b5de23e99
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/63ffc2691e47cd87
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/64b11b6f95257cb2
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/64d0f72357941326
+-rw-r--r--   0        0        0      246 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6508c3c5487ab075
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6536d4c143f8be91
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/65728b52f41bc9ba
+-rw-r--r--   0        0        0      806 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6576547c7f4694be
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6644763f109bdd6b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/669dd8c8a39698b7
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/66ac2324e22de590
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/66d089a8df35552b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/66d111006494eb36
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/66dc710e3f81dd1b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/670150825a70ddd
+-rw-r--r--   0        0        0      390 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6716dc831f36b4e
+-rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/67464bd807747cd7
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6746ada4d0522944
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/67b5326d54837deb
+-rw-r--r--   0        0        0      578 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/682188a646d78c0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/682860051556cf7c
+-rw-r--r--   0        0        0      446 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6890ca733e8cb4fd
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/68d3fe72b76a4597
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6917d2cd5cad8ce8
+-rw-r--r--   0        0        0      933 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/695170c6d345cb58
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/696b5d905cecae9e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/698e80c153c0e564
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/69a1b64825d36650
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/69c0b99e6a3612ac
+-rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6a1d1822013c9bc0
+-rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6a6a4fb6f8a50947
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6a8150cb8ef00174
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6b2c7e5abafb43d5
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6ba094ed40da3dfe
+-rw-r--r--   0        0        0      246 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6bac0870e1bfe66b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6bd4c791fee019e1
+-rw-r--r--   0        0        0      619 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6c8242c16814d970
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6c96f471c4bbea32
+-rw-r--r--   0        0        0      172 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6ca0e41194c8d88a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6ca8d392710dcad0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6cec0d8c6e537732
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6cfb413da2d3a9d7
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6d33cc2bdaf5b388
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6d6e3ff4d34fb67c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6ddf9f070f5ea610
+-rw-r--r--   0        0        0      262 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6de8d7c51d326383
+-rw-r--r--   0        0        0     1237 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6e342654a00b5817
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6e419bf1baa2b856
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6e9399320683c7f8
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6edfe3868f20ef5b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6f69ef19acc74949
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6f79223032f285e6
+-rw-r--r--   0        0        0     1532 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6fb452c5ea33322
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/6fd67a6c4d9402cd
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7066a7cfa126658c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/70a3c394403b13e
+-rw-r--r--   0        0        0      418 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/70a527efdfe96d9e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/70bda471d8e83aca
+-rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/70f00010df65f78f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/70f76aadc859c727
+-rw-r--r--   0        0        0     2150 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/71373ffe75246f00
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/714586f9c795411b
+-rw-r--r--   0        0        0      790 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/715499bd1eb26466
+-rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/715dbd085d13932
+-rw-r--r--   0        0        0      247 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7166400981c965aa
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/71c1374790d60ec7
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/71e60efbcd179c8b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/71fdde3839d3392e
+-rw-r--r--   0        0        0     2150 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/72499df899c54a45
+-rw-r--r--   0        0        0      406 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/726d869eaad7cbd2
+-rw-r--r--   0        0        0      790 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7281991b04dc372b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/72dae9b85aedb727
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/72fc43b5409abc5d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7419ca5c5d9d3576
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/749c16d9b38ea10b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/75093b69707477c7
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7564f23bf736124e
+-rw-r--r--   0        0        0      227 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/75df3e0ec74f7a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/760a90d18d7a043d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/762424f77d674629
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7698193a2f2fd3b3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/76accb1814a3a13
+-rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7764d0a3ebbd15f1
+-rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/777056ba87a3db44
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/77fa35a0d4a775fa
+-rw-r--r--   0        0        0      248 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/784a7e6082e35f79
+-rw-r--r--   0        0        0     1950 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7861f5cb2966565a
+-rw-r--r--   0        0        0     1576 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/79d8b31a7196e404
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7a693d4a4965f3ee
+-rw-r--r--   0        0        0      811 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7abafe920dd77a92
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7ac0bc918b5c67c6
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7ae7caba07deb51b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7ae90594605c72c7
+-rw-r--r--   0        0        0     1156 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7bbfd8c3690b5a75
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7c1fa8b9eb0b1811
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7c8218be60001dda
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7cd8c0f02c8d8d24
+-rw-r--r--   0        0        0      418 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7cdbd1dc60e81b96
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7d17b9c40a45bd56
+-rw-r--r--   0        0        0      923 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7d958009b81b0dd7
+-rw-r--r--   0        0        0      429 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7db8793f8e021f80
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7dfeddee84e5b438
+-rw-r--r--   0        0        0     2738 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7e39743b5037bb34
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7e6d64b78cc2e356
+-rw-r--r--   0        0        0      211 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7ee528fc74afd046
+-rw-r--r--   0        0        0      187 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7f04363dd1b7eb25
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7f463249d43ddcd9
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7f7fb29c4cc7e61e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7fb9a965e8077e1d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/7fcbd52f3630686c
+-rw-r--r--   0        0        0     3851 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/80e739b3e52c2ee9
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/81441640090c5bc
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8192e3658d123572
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/81f1f9db8376452e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8201bdd1e24ea9f5
+-rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/824ad90d2e4a90c4
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/82ca4d31739adaaf
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/82cdac5a72987b8b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8315b0d8c1b5a7b7
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8354d9ea10984822
+-rw-r--r--   0        0        0      572 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8377c8be88accd28
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8437018678492400
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/844797c614a2a016
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8461e9c9048d50f4
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/84c6b4671f5829bc
+-rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/84dc23112959bef3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/851a246705623ed8
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/85724e9e4780a371
+-rw-r--r--   0        0        0      923 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/857ff98531f4bd4a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/85a48e1aa08f497c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8776f9eabe3609af
+-rw-r--r--   0        0        0      223 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/87cc41cfe62706e5
+-rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/87e6069b6dae1d69
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/87e61854cba9e459
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/884f329d76b22a81
+-rw-r--r--   0        0        0      199 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/88597d00446c39ae
+-rw-r--r--   0        0        0      172 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/88784a30b1e3325e
+-rw-r--r--   0        0        0     1576 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8880e918cb120ec7
+-rw-r--r--   0        0        0      572 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/88b37c139c075c2c
+-rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/89afb837dfa217c6
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/89ba1e99f76a5c1
+-rw-r--r--   0        0        0      204 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8a4b5ac208fc8176
+-rw-r--r--   0        0        0     1576 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8a5fbc233bbd1ad6
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8ad87f05d43f1e0f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8b1b566e67aaf911
+-rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8bcea5aeb8b26f31
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8c74538d4cf25bb
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8cc3d1a83e269152
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8cef7199f6258137
+-rw-r--r--   0        0        0      222 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8d593356a0ee5072
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8de59f96561d71d1
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8e0583fbc62b6104
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8ec74aec9c1c01c3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8f27d152d90364e2
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8f2f2a38cdcfe630
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8f4cac62f4e5196b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8f6de574c26679a1
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8f847a3b90cf5ddc
+-rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/8fff743c3d8501f3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/903c523f0f7ea349
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/90fb0f25b4b1982a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/91113ba4b61e6442
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9138673748b10d05
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/916ee4c97ed80a01
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9259fd33f76abb9d
+-rw-r--r--   0        0        0      216 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/92bf0c830b819795
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/931740d8b0e88b6d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/94031dc00bdc7467
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/941e004fb7846f51
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9468053cffed6ac5
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/94be5a333382332f
+-rw-r--r--   0        0        0     1156 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/950808b1e26775ec
+-rw-r--r--   0        0        0      933 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/95267216d1d74c9
+-rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9564ef73b0f0b9bd
+-rw-r--r--   0        0        0      192 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/958da252825b59cd
+-rw-r--r--   0        0        0      324 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/95ff4d1cc696af6a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/96abd569caa882ae
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/978a175054cecb8b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/97daea7f24aa497e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/97f7ba029545af94
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/97f7c0439761be0d
+-rw-r--r--   0        0        0     1278 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/986b503a8f13eaa
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9876f7de98fece8c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9884392ab8835283
+-rw-r--r--   0        0        0      370 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/98aaf65343e92671
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/98c41673fbe3aac0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/991c1dd22bfb5cc3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/99276b2ef50b24b7
+-rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/99a1f744d7a3bce0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/99e38be04ae3e738
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9a451b726d896a13
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9a88e788c8f6af81
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9ad03463c6a71b94
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9b12802ae3321a54
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9b5c71f22528b824
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9be1c788122ea694
+-rw-r--r--   0        0        0      348 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9c6bf0cf3433024a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9c6f167fdeb3d317
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9cc25f96d447d297
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9cd3a936f82c6065
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9cf608a32b424228
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9d338bcb6840debe
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9d98fab6fcbebc62
+-rw-r--r--   0        0        0      712 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9dfd1a4c1d6c5611
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9e2ebe40a64a3056
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9e67d8e3d44a52a9
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9e7b258c9d6ada25
+-rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9f615ba52e97076c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9f62c4dcda39e0ed
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9f7b87a7b8718ae0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9f7cc6a7e28d672
+-rw-r--r--   0        0        0     1237 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/9f86a234993ab90f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a032fe5373e2f566
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a06743363ba17397
+-rw-r--r--   0        0        0      562 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a09ca4d68f7f7a6d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a0c9760cf9c8d13f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a110a12cfc697e8c
+-rw-r--r--   0        0        0      192 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a115a02d1705e6ae
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a1269bab7695230b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a1e338582ecefbf2
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a1ed812d84ff228e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a1fe17a030762aaa
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a259354f3f0a0f79
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a29252e225ecf2b8
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a296aa250618c000
+-rw-r--r--   0        0        0      928 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a296e558a05a4446
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a362b930d2a8e71d
+-rw-r--r--   0        0        0      923 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a3930f42fc0d5727
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a3b6ce8deae08464
+-rw-r--r--   0        0        0      192 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a3d5954e9452da4b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a3fadb7adae4063f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a45a31edda7a8cbe
+-rw-r--r--   0        0        0      211 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a468e101c105ae0c
+-rw-r--r--   0        0        0      162 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a527cc0152cf02a6
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a539593321e14fe6
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a53ebc83330776b3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a6018ee5d12eb85
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a6a5b65691bdc39d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a79f9aa8e748cb3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a83b403ed1f478a7
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/a96fec08236817b0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/aa36cf81253e9663
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/aa6af830d5cfbd13
+-rw-r--r--   0        0        0    10127 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/aa737b2f5fb8e71d
+-rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/aa820a19cfc27687
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/aa890592ef42784a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/aa96346bdbbbadca
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/aac63e41a0f74317
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/aad6c3b1b7e2d037
+-rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ab5f6078817c2fb0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ab8fdf5c743c1460
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/abf597b97b538b40
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ac080e6c34953966
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ac0cb2254a297d
+-rw-r--r--   0        0        0      542 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ac31423108a9860
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ac6883549bcf0e93
+-rw-r--r--   0        0        0      189 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/acab2a9223b5295f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/accdce480aaedfb0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/acd588827dbb0371
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ad8acc49cd946a33
+-rw-r--r--   0        0        0     6366 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/adfdc55c283c3c0f
+-rw-r--r--   0        0        0     5626 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ae81d3744b93d310
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/aec7218dad196161
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/aee942293e1feefc
+-rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/af31928a32d7994d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/af3b44be2117df44
+-rw-r--r--   0        0        0      261 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/af3d20cf6acc98a6
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/af639254e5e42638
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/af7a06e1e348d184
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/af96474e5d6d8a79
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/afd67290197a0223
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/afe1f6cc2e2294ad
+-rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b050a7831c5ff26d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b053f453ef051223
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b0c9aee3bae2a40b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b0df4ef10e21bb3c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b1169fed645c89dc
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b11f56fb8ba4fb52
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b137cb9f0209e163
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b14a58826252ad27
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b15bcf7cae7464a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b1900434fd007335
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b19c390aae16d2dc
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b1c77fe3fc4341a5
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b2025744040ed5ba
+-rw-r--r--   0        0        0     3552 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b2c510e6d789bae1
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b34662c19e9588ec
+-rw-r--r--   0        0        0     1285 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b34b2d8198704c68
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b3aed5ec6805bd41
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b4be0b529d02420d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b51cbd48e85a6f4
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b5e0e18c9d78783d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b5edb9177631d138
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b607c010d16d520
+-rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b60c1e8ff4f16c7f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b635aef0cfca1d11
+-rw-r--r--   0        0        0    11806 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b69b1ed3056953ee
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b6a34dd9c878d92d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b6bee2f03daf9855
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b6e3c2953538738a
+-rw-r--r--   0        0        0      928 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b72ce555d5fa6a8e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b74f84f806ad6859
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b78151ec2ea7549b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b78fb2ccf62a3b95
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b790864dd0cce062
+-rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b8230cee1f524ad1
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b87649c3116f2170
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b8f42454cd24a1c0
+-rw-r--r--   0        0        0      806 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b925dc8a594b869a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/b9b0685daf49c3cb
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bb211b609a91c7c1
+-rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bb4fde2c72d4315a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bb873e4145d79e46
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bc42a7d33ea0b947
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bc491c862523b5dc
+-rw-r--r--   0        0        0      256 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bd3f48f796fd95ab
+-rw-r--r--   0        0        0      247 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bd491c1f1af4d251
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bd65255aefe18e02
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bd6b97d43aac146b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bda1b20e60f34b7b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bdbd414788569a24
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bdee6fadb8f06f0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/be1c34972d748a4b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/be3e726596e949c3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/be47b2cc4ed456b0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bed7c7f59683f6f5
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bf9182473114ba35
+-rw-r--r--   0        0        0     1196 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bfaa6c8b09ea7082
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bfae5ad2c3b5210
+-rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bfbe152080b709d9
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bfc4bac36774d7bb
+-rw-r--r--   0        0        0     1504 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/bfeb6ff39293ca1d
+-rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c0005c6bd945f3d2
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c011ea061e4dbce8
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c074f80fa39459e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c092633ea9a2dd8e
+-rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c10cd88b4285ff0b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c197af6f2829b65c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c20c4bd79e0975ca
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c25fd4073dd7ecf9
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c31b8c89c9b388cb
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c32da9b0188c78e4
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c36fe33676ead07d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c3b14714ff33ec1b
+-rw-r--r--   0        0        0      246 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c3b73e0e8aa099fa
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c424ef13bc66b049
+-rw-r--r--   0        0        0     1576 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c467bf0cef9b03ab
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c4b8f6b6883cea1e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c4c45ce4e9c2687d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c4d961ac35f46220
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c5211d60a6641a73
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c6035b26f69105fd
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c703a54a942d3a36
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c728c63863b8abf6
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c7a9f3f0ec2d6133
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c7c66d7c506eb23a
+-rw-r--r--   0        0        0      190 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c7dd7c9490ed7a40
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c822b670428f7480
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c83c52eb724c117e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c85a4601697418f5
+-rw-r--r--   0        0        0      978 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c8959c42754024d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/c9ff1b4f31e033c5
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ca234d38b42ec57b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ca7961b45cdda322
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/cb243904781569bd
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/cb82637251df8fa
+-rw-r--r--   0        0        0      414 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/cbbc258be108b7df
+-rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/cc64ecd0f9bc901b
+-rw-r--r--   0        0        0      180 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ccdf86f0f4ac4b9e
+-rw-r--r--   0        0        0     1950 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/cd4f7faa7a866ead
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/cd5351001df3ccf
+-rw-r--r--   0        0        0      212 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/cdbdecacd11dee93
+-rw-r--r--   0        0        0      393 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/cdc1b0fec16a36a4
+-rw-r--r--   0        0        0      811 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ce1f45bc791cd4ab
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ce796a3ed9297b64
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/cf715425db3a674c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/cfadb0829958f9d9
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/cfcf9cde33efb6e4
+-rw-r--r--   0        0        0     1003 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/cfe8a804b0d1388d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d086374488e821f0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d0c7070297416579
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d0fdd17ab30a03f9
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d15ddb6f796adbef
+-rw-r--r--   0        0        0     1003 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d17b1a6a05c0a1a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d18fd7fba26847c9
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d1ad5c9d4566c827
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d1d7baf09faee281
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d2af16d8d7f9174d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d34ea1a3ec3db7c1
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d372d2005aaadcc5
+-rw-r--r--   0        0        0      949 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d42b3f28fcca5b92
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d4444ea5bb9c09f8
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d450efd73e841dd1
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d4bb1954ad7242a0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d4dbb067d602bd38
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d4fc57c121dc2867
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d5185db4ee908681
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d52af40654063af
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d5daf3e0eed7c527
+-rw-r--r--   0        0        0     1022 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d5ff022c78ca8bdb
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d66827ce10c895f0
+-rw-r--r--   0        0        0      521 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d698a764e2eee095
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d6a88f5f9a69ced
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d825dcc04fc84017
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d838119720bbe81e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d8409cdd3a3a5ff5
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d88af436755e2ce7
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d89a35229fdffab8
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d8b6767dcbee3959
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d92eaed61f00fb5e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d95942274c7caab6
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d959ea6f9a7b172d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/d9aa7d658e741c8b
+-rw-r--r--   0        0        0      222 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/da311db2c2885ddd
+-rw-r--r--   0        0        0     1003 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/da69e5397a61483b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/da792f8304aff60e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/da9579b8a4f6e6a5
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/daba82336d911f70
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/dac8be7552f4da53
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/dad5a9437ebeb23e
+-rw-r--r--   0        0        0     5907 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/dafc0b9cca5a6ec0
+-rw-r--r--   0        0        0      427 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/db55ac649ddc5bc2
+-rw-r--r--   0        0        0      223 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/db8c48b8f9904250
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/dba5980c5e43519e
+-rw-r--r--   0        0        0      324 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/dbd9b4486b3f7673
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/dc6453836ca97a38
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/dc75b3850b1552d6
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/dc866f1a282d9e99
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/dcbc6da792fb572e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/dd24c73ffa57d7b8
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/dd28e794e49ef05f
+-rw-r--r--   0        0        0      324 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/de34d3f79e397211
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/de5b4b6d7c7a4aa0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/de5b5e9ce0b9af7d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/dee68a08a191d3dc
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/df33118cc8090b02
+-rw-r--r--   0        0        0      189 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/df398fd32ef122ec
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/dfbbd2e1ba64adf6
+-rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/dff7ac6c8a6da66c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e04122854c1cdee3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e09308b4ad85cda3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e0d2ef3bc1e7748c
+-rw-r--r--   0        0        0      172 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e0d536a62d4b470d
+-rw-r--r--   0        0        0      210 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e1127e7f518921db
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e150df48399fd335
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e1547d911a29d9df
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e1a0c2e5096f3d5c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e26a4475b9aa0279
+-rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e2cf30a40920587a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e2f43c625119ce8
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e2f687397586dd67
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e385bf01937d83f2
+-rw-r--r--   0        0        0     3333 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e4058c4aa5da08b2
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e43dee8732cf87c4
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e488b6a1db32f142
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e49cb12e33716f16
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e50d15191aadec14
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e51cbefebee20fe0
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e5660ca00fa1ccbd
+-rw-r--r--   0        0        0      203 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e581852ab9f8268f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e58836765de2dd81
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e5a6c45715c7a4d9
+-rw-r--r--   0        0        0      183 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e61a13825345f735
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e628e6fd4e068805
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e64422ad5d7ea0b1
+-rw-r--r--   0        0        0      928 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e656067c10d75580
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e68083d35c65831
+-rw-r--r--   0        0        0      188 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e73885481f7ea5c3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e7b15d127175a559
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e7c36298702e21d5
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e818ac81e2a75d37
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e841a3b032a527d8
+-rw-r--r--   0        0        0      557 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e8bd3b3a333c4df1
+-rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e90daf111409ff81
+-rw-r--r--   0        0        0      215 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e91d6b7e7d2fe82e
+-rw-r--r--   0        0        0      562 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e985bcee084c8ec0
+-rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e9b4fe44bf585a4f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/e9dfaf5afeb9bdc5
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ea05db2f6aa05fae
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ea334dfd69e05bd2
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/eaa421c01061b53d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ead128675b3e9163
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/eae976d1ed869354
+-rw-r--r--   0        0        0      954 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/eaefa94a9823b2f1
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/eb2da57998ce572a
+-rw-r--r--   0        0        0      554 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/eb3d0304cfb9339f
+-rw-r--r--   0        0        0      213 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/eba7f2c4ec33748f
+-rw-r--r--   0        0        0      252 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ebfabd2d8a1d96f2
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ec0de8a1a9566d0c
+-rw-r--r--   0        0        0      757 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ec4d305e85bb4e19
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ec6de6d844bd2657
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ec993b2a0e0b8300
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ec9b28fb8aa4bcd6
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/eca1bc5b38404158
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ed9171a9cc866187
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/edae5907d9b5b7a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/edfc7f2712830945
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ee203332d31c95f1
+-rw-r--r--   0        0        0      949 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ee2d09ff4551420d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ee44296492d931ad
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ee5b2f072fe78193
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/efb26f5bf720fc9a
+-rw-r--r--   0        0        0      811 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f041520f880369c3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f067cfe7bb78a01
+-rw-r--r--   0        0        0      352 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f0a156575a2b5e8f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f0ec8a0f8effcbd
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f144cf764e4cf18f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f1733439bbd00169
+-rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f189d1426bad3cc2
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f2147a78b279223d
+-rw-r--r--   0        0        0      954 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f22550a5656ee20f
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f226e4fbf4b5a3b3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f241190fc668086f
+-rw-r--r--   0        0        0      978 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f27f3c06aa306cb3
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f2fb18698297b6ce
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f3568936f3dedd34
+-rw-r--r--   0        0        0     2816 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f387f65a58ab496e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f40ecc88d42de5c7
+-rw-r--r--   0        0        0     1156 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f48e1807643594f1
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f5957d85667f204a
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f5ab751f18d8a1e5
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f5f041602121135c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f6213731e01b317c
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f6845a2d4aa7b059
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f6898e64650c2687
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f749c3bb69352870
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f76aeec8a998ee3d
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f7a4501c62c233d4
+-rw-r--r--   0        0        0      258 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f805ca4622aaebba
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f93d05bb52180f75
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f9871edc06decb6e
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/f998083de33b36a6
+-rw-r--r--   0        0        0      790 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/fa02e62e08abbadb
+-rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/fa4db5da0ded9759
+-rw-r--r--   0        0        0     2120 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/fa5ccd5562187a1b
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/fa76990547589722
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/fb678d0d18138d93
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/fb734b6eb7cb3578
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/fba563e6c89b93c7
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/fbbdd65488ef4b02
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/fc34d2b3d6a084dd
+-rw-r--r--   0        0        0      207 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/fd1bd27b9ad4c831
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/fd90e548022ed645
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.ruff_cache/content/ffa0e62887131f81
+-rw-r--r--   0        0        0       17 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/docs/advanced.md
+-rw-r--r--   0        0        0      211 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/docs/api.md
+-rw-r--r--   0        0        0       28 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/docs/async.md
+-rw-r--r--   0        0        0       32 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/docs/custom_api.md
+-rw-r--r--   0        0        0       41 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/docs/exceptions.md
+-rw-r--r--   0        0        0       48 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/docs/functions.md
+-rw-r--r--   0        0        0     2428 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/docs/index.md
+-rw-r--r--   0        0        0     4433 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/docs/quickstart.md
+-rw-r--r--   0        0        0     6929 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/docs/syntax.md
+-rw-r--r--   0        0        0      911 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/docs/css/style.css
+-rw-r--r--   0        0        0      132 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/__about__.py
+-rw-r--r--   0        0        0     1023 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/__init__.py
+-rw-r--r--   0        0        0    14371 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/env.py
+-rw-r--r--   0        0        0     1796 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/exceptions.py
+-rw-r--r--   0        0        0    11536 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/filter.py
+-rw-r--r--   0        0        0    11085 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/lex.py
+-rw-r--r--   0        0        0     2513 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/match.py
+-rw-r--r--   0        0        0    17562 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/parse.py
+-rw-r--r--   0        0        0    11371 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/path.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/py.typed
+-rw-r--r--   0        0        0    21397 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/selectors.py
+-rw-r--r--   0        0        0     2567 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/stream.py
+-rw-r--r--   0        0        0     3650 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/token.py
+-rw-r--r--   0        0        0      104 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/function_extensions/__init__.py
+-rw-r--r--   0        0        0      364 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/function_extensions/keys.py
+-rw-r--r--   0        0        0      313 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/jsonpath/function_extensions/length.py
+-rw-r--r--   0        0        0      110 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/__init__.py
+-rw-r--r--   0        0        0     1677 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/compliance.py
+-rw-r--r--   0        0        0     2329 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/consensus.py
+-rw-r--r--   0        0        0     1236 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/test_async.py
+-rw-r--r--   0        0        0     1818 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/test_compare.py
+-rw-r--r--   0        0        0     1733 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/test_concrete_path.py
+-rw-r--r--   0        0        0     4025 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/test_env.py
+-rw-r--r--   0        0        0      747 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/test_errors.py
+-rw-r--r--   0        0        0     1376 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/test_find.py
+-rw-r--r--   0        0        0     2459 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/test_find_compound_path.py
+-rw-r--r--   0        0        0    15182 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/test_find_reference.py
+-rw-r--r--   0        0        0    12342 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/test_ietf.py
+-rw-r--r--   0        0        0     6415 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/test_ietf_comparison.py
+-rw-r--r--   0        0        0    38409 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/test_lex.py
+-rw-r--r--   0        0        0     1438 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/test_match_api.py
+-rw-r--r--   0        0        0     6138 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/test_parse.py
+-rw-r--r--   0        0        0     1109 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/test_parse_compound_path.py
+-rw-r--r--   0        0        0     1615 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/tests/test_re.py
+-rw-r--r--   0        0        0      968 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/.gitignore
+-rw-r--r--   0        0        0     1102 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/LICENSE.txt
+-rw-r--r--   0        0        0    11024 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/README.md
+-rw-r--r--   0        0        0     3575 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/pyproject.toml
+-rw-r--r--   0        0        0    12076 2020-02-02 00:00:00.000000 python_jsonpath-0.4.0/PKG-INFO
```

### Comparing `python_jsonpath-0.3.0/CHANGELOG.md` & `python_jsonpath-0.4.0/CHANGELOG.md`

 * *Files 22% similar despite different names*

```diff
@@ -1,9 +1,15 @@
 # Python JSONPath Change Log
 
+## Version 0.4.0
+
+**IETF JSONPath Draft compliance**
+
+- **Behavioral change.** When applied to a JSON object, filters now have an implicit preceding wildcard selector and the "current" (`@`) object is set to each of the object's values. This is now consistent with applying filters to arrays and adheres to the IETF JSONPath Internet Draft.
+
 ## Version 0.3.0
 
 **IETF JSONPath Draft compliance**
 
 - Added support for function extensions.
 - Added the built-in `length()` function.
 - Added the built-in `count()` function. `count()` is an alias for `length()`.
```

### Comparing `python_jsonpath-0.3.0/jsonpath.bnf` & `python_jsonpath-0.4.0/jsonpath.bnf`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/mkdocs.yml` & `python_jsonpath-0.4.0/mkdocs.yml`

 * *Files 13% similar despite different names*

```diff
@@ -37,17 +37,19 @@
             separate_signature: true
             docstring_section_style: "spacy"
   - autorefs
 
 nav:
   - Introduction: "index.md"
   - Usage:
-      - QuickStart: "quickstart.md"
+      - Quick Start: "quickstart.md"
       - Advanced Usage: "advanced.md"
   - Guides:
+      - JSONPath Syntax: "syntax.md"
+      - Filter Functions: "functions.md"
       - Async Support: "async.md"
   - API Reference:
       - High Level API: "api.md"
       - Low Level API: "custom_api.md"
       - Exceptions: "exceptions.md"
 
 markdown_extensions:
```

### Comparing `python_jsonpath-0.3.0/.github/workflows/tests.yaml` & `python_jsonpath-0.4.0/.github/workflows/tests.yaml`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/__future__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/__future__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/__future__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/__future__.meta.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_ast.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_ast.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_ast.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_ast.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
         2,
         3,
         1,
         1,
         1,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_bisect.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_bisect.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_bisect.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_bisect.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_codecs.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_codecs.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_codecs.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_codecs.meta.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         4,
         1,
         2,
         3,
         5,
         6,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_collections_abc.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_collections_abc.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_collections_abc.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_collections_abc.meta.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
         2,
         3,
         32,
         1,
         1
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_ctypes.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_ctypes.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_ctypes.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/resolver.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7121693121693121%*

 * *Differences: {"'data_mtime'": '1680012434',*

 * * "'dep_lines'": '{delete: [3, 1, 0]}',*

 * * "'dep_prios'": '{delete: [5, 4, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'yaml.error'), (1, 'typing')], delete: [6, 4, 2, 1, 0]}",*

 * * "'hash'": "'6ff3245b99546e2d2707eb2d24702846303b100ada1a698bb1a7c14fd387e738'",*

 * * "'id'": "'yaml.resolver'",*

 * * "'interface_hash'": "'105e16a344e082e452f9af00235921431d09c5841ca21b6839dfffc3354cceac'",*

 * * "'mtime'": '1680012426',*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/pyth […]*

```diff
@@ -1,41 +1,32 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680012434,
     "dep_lines": [
-        1,
-        2,
         3,
         1,
         1,
-        1,
         1
     ],
     "dep_prios": [
-        10,
         5,
         5,
         5,
-        30,
-        30,
         30
     ],
     "dependencies": [
-        "sys",
-        "ctypes",
-        "typing_extensions",
+        "yaml.error",
+        "typing",
         "builtins",
-        "_typeshed",
-        "abc",
-        "typing"
+        "abc"
     ],
-    "hash": "f3f569576a38ac44f7351d80826ca0da2673c3895b9278a10d671615e6388fc9",
-    "id": "_ctypes",
+    "hash": "6ff3245b99546e2d2707eb2d24702846303b100ada1a698bb1a7c14fd387e738",
+    "id": "yaml.resolver",
     "ignore_all": true,
-    "interface_hash": "a73ffbaace30e4490abd6ee944ca165a73ced1f43d6dbf8606cea4c57eed0181",
-    "mtime": 1679496944,
+    "interface_hash": "105e16a344e082e452f9af00235921431d09c5841ca21b6839dfffc3354cceac",
+    "mtime": 1680012426,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -69,13 +60,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/_ctypes.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/resolver.pyi",
     "plugin_data": null,
-    "size": 829,
+    "size": 787,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_decimal.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_decimal.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_decimal.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_decimal.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_operator.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_operator.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_operator.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_operator.meta.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         3,
         1,
         2,
         4,
         5,
         1,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_socket.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_socket.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_socket.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_socket.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_stat.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_stat.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_stat.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_stat.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_thread.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_thread.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_thread.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_thread.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_tracemalloc.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_tracemalloc.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_tracemalloc.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_tracemalloc.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_warnings.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_warnings.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_warnings.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_warnings.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_weakref.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_weakref.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_weakref.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_weakref.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_weakrefset.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_weakrefset.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_weakrefset.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_weakrefset.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/abc.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/abc.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/abc.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/wcwidth.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7283333333333334%*

 * *Differences: {"'data_mtime'": '1680278525',*

 * * "'dep_lines'": '{insert: [(2, 1), (3, 1)], delete: [4, 3, 0]}',*

 * * "'dep_prios'": '{insert: [(3, 30), (4, 30)], delete: [3, 1, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'unicodedata'), (1, 'functools'), (3, 'abc'), (4, 'typing')], "*

 * *                   'delete: [4, 3, 2, 1, 0]}',*

 * * "'hash'": "'6211374e8faf048eee74bb55e01fa0fb4e12de5f15a110f9922f77e508a99890'",*

 * * "'id'": "'_pytest._io.wcwidth'",*

 * * "'interface_hash'": "'ff785b55f64db0077c07b259a0e7bd5a4b46efddfeb79e1eaebcc7226e39c7c5'" […]*

```diff
@@ -1,37 +1,34 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680278525,
     "dep_lines": [
-        4,
         1,
         2,
-        5,
-        6,
+        1,
+        1,
         1
     ],
     "dep_prios": [
-        5,
-        5,
         10,
         5,
         5,
-        5
+        30,
+        30
     ],
     "dependencies": [
-        "collections.abc",
-        "_typeshed",
-        "sys",
-        "typing",
-        "typing_extensions",
-        "builtins"
+        "unicodedata",
+        "functools",
+        "builtins",
+        "abc",
+        "typing"
     ],
-    "hash": "a3b9c6522f0a6d3e6e4cd8febae992da12d43e37176bb3fb0909533463a529b2",
-    "id": "abc",
+    "hash": "6211374e8faf048eee74bb55e01fa0fb4e12de5f15a110f9922f77e508a99890",
+    "id": "_pytest._io.wcwidth",
     "ignore_all": true,
-    "interface_hash": "7b25b3291456b223ffbb9d4e140059673b6ec6d95b74352cd0c19a5751d1c3f2",
+    "interface_hash": "ff785b55f64db0077c07b259a0e7bd5a4b46efddfeb79e1eaebcc7226e39c7c5",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -66,13 +63,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/abc.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/_pytest/_io/wcwidth.py",
     "plugin_data": null,
-    "size": 1770,
+    "size": 1253,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/argparse.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/argparse.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/argparse.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/argparse.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/array.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/array.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/array.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/dis.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7590714840714841%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(3, 4), (4, 5)], delete: [6, 5, 4]}',*

 * * "'dep_prios'": '{insert: [(1, 10)], delete: [7, 6]}',*

 * * "'dependencies'": "{insert: [(2, 'types'), (3, 'opcode'), (7, '_typeshed')], delete: [9, 8, 7, "*

 * *                   '2]}',*

 * * "'hash'": "'0752728fe06a3c30c30280311b749ec46eee32ec08b5ec9221c552757dd04ca7'",*

 * * "'id'": "'dis'",*

 * * "'interface_hash'": "'dcde734b3f10aeb177c0cb25c530c9ce6e810fb07f1445cf96cd0352e7383b33'",*

 * * "'path'": "'/home/james/.local/share/hatch/env […]*

```diff
@@ -1,49 +1,46 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         3,
         1,
         2,
+        4,
+        5,
         6,
-        7,
-        1,
-        1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
         10,
+        10,
         5,
         5,
         5,
         5,
         30,
-        30,
-        30,
         30
     ],
     "dependencies": [
         "collections.abc",
         "sys",
-        "_typeshed",
+        "types",
+        "opcode",
         "typing",
         "typing_extensions",
         "builtins",
-        "abc",
-        "ctypes",
-        "mmap",
-        "pickle"
+        "_typeshed",
+        "abc"
     ],
-    "hash": "d0ad5e13f4193b236ba4ba6fea5d43bd8795d6f09b3a27b8ef2cfbb1b1e2d993",
-    "id": "array",
+    "hash": "0752728fe06a3c30c30280311b749ec46eee32ec08b5ec9221c552757dd04ca7",
+    "id": "dis",
     "ignore_all": true,
-    "interface_hash": "a779d356ced53b8f7703ad2eb1b6a91189882f4150adf2db87bec1cf423e8343",
+    "interface_hash": "dcde734b3f10aeb177c0cb25c530c9ce6e810fb07f1445cf96cd0352e7383b33",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -78,13 +75,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/array.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/dis.pyi",
     "plugin_data": null,
-    "size": 3679,
+    "size": 4403,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/ast.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/ast.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/ast.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/ast.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/atexit.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/atexit.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/atexit.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/atexit.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/bdb.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/bdb.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/bdb.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/bdb.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/bisect.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/bisect.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/bisect.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/bisect.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/builtins.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/builtins.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/builtins.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/pdb.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7472250639386189%*

 * *Differences: {"'data_mtime'": '1680278526',*

 * * "'dep_lines'": '{insert: [(0, 5), (5, 6), (6, 7), (7, 8), (8, 9)], delete: [9, 8, 7, 6, 5, 0]}',*

 * * "'dep_prios'": '{insert: [(8, 5), (9, 5)], delete: [10, 9, 2]}',*

 * * "'dependencies'": "{insert: [(1, 'signal'), (3, 'bdb'), (4, 'cmd'), (5, 'inspect'), (9, "*

 * *                   "'builtins'), (10, '_typeshed'), (12, 'ast'), (13, 'enum')], delete: [14, 13, "*

 * *                   '12, 11, 10, 6, 5, 2, 1]}',*

 * * "'hash'": "'f28fa38985ef2d556366b0116f8569533bca86d686aeac3663f62f8bfabf2e62'", […]*

```diff
@@ -1,64 +1,61 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680278526,
     "dep_lines": [
-        30,
+        5,
         1,
         2,
         3,
         4,
-        5,
-        31,
-        35,
-        57,
-        1,
+        6,
+        7,
+        8,
+        9,
         1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
         10,
-        5,
         10,
         5,
         5,
         5,
         5,
         5,
-        30,
-        30,
+        5,
+        5,
         30,
         30,
         30,
         30
     ],
     "dependencies": [
         "collections.abc",
-        "_ast",
-        "_typeshed",
+        "signal",
         "sys",
+        "bdb",
+        "cmd",
+        "inspect",
         "types",
-        "_collections_abc",
-        "io",
         "typing",
         "typing_extensions",
+        "builtins",
+        "_typeshed",
         "abc",
-        "array",
-        "ctypes",
-        "importlib",
-        "mmap",
-        "pickle"
+        "ast",
+        "enum"
     ],
-    "hash": "2036859bfabd3515c707a849167221d44fe91af7b10f828d2745a152a4af3fea",
-    "id": "builtins",
+    "hash": "f28fa38985ef2d556366b0116f8569533bca86d686aeac3663f62f8bfabf2e62",
+    "id": "pdb",
     "ignore_all": true,
-    "interface_hash": "4893fdbcb6f39c06f42c6743630d18bbcae1bc7cbce9edef3460bb21c8c1626c",
+    "interface_hash": "d7514e6d33ee85ec36910cd86f7b783dcb01c6727effb73c4078b2ab517a7c6e",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -93,13 +90,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/builtins.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/pdb.pyi",
     "plugin_data": null,
-    "size": 82326,
+    "size": 7379,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/cmd.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/cmd.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/cmd.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/cmd.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/codecs.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/codecs.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/codecs.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/codecs.meta.json`

 * *Files 5% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         6,
         1,
         2,
         3,
         4,
         5,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/compliance.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/compliance.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/compliance.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/compliance.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/consensus.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/consensus.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/consensus.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/consensus.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/contextlib.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/contextlib.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/contextlib.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/enum.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7562289562289561%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 7), (4, 5), (7, 9)], delete: [7, 5, 0]}',*

 * * "'dep_prios'": '{insert: [(3, 10)], delete: [3]}',*

 * * "'dependencies'": "{insert: [(2, 'sys'), (4, 'abc'), (5, 'builtins')], delete: [7, 2, 1]}",*

 * * "'hash'": "'70b30897b521ffb90251c805cd8ed4dfb35b1dd86134b06669a5dd31a90cbfa5'",*

 * * "'id'": "'enum'",*

 * * "'interface_hash'": "'19beccd3f73f5ba0f60956cad001a0f51a1925e7afa2a142a2fb60531027925d'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/ […]*

```diff
@@ -1,43 +1,43 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        5,
+        7,
         1,
         2,
         3,
+        5,
         6,
-        7,
         8,
-        1
+        9
     ],
     "dep_prios": [
         5,
         5,
         10,
-        5,
+        10,
         5,
         5,
         5,
         5
     ],
     "dependencies": [
         "collections.abc",
-        "abc",
-        "sys",
         "_typeshed",
+        "sys",
         "types",
+        "abc",
+        "builtins",
         "typing",
-        "typing_extensions",
-        "builtins"
+        "typing_extensions"
     ],
-    "hash": "e9251a3e7f59f7bd3f0883f9f7ffca34270a476e9b7afcf326492ad786b18f8a",
-    "id": "contextlib",
+    "hash": "70b30897b521ffb90251c805cd8ed4dfb35b1dd86134b06669a5dd31a90cbfa5",
+    "id": "enum",
     "ignore_all": true,
-    "interface_hash": "b2e20e8ed9d5e0c6062abf78cec3437ef856830dc1081f0183bf91e796c3041a",
+    "interface_hash": "19beccd3f73f5ba0f60956cad001a0f51a1925e7afa2a142a2fb60531027925d",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -72,13 +72,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/contextlib.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/enum.pyi",
     "plugin_data": null,
-    "size": 8764,
+    "size": 10061,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/contextvars.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/contextvars.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/contextvars.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/contextvars.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/copy.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/copy.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/copy.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/copy.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/copyreg.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/copyreg.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/copyreg.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/copyreg.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/dataclasses.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/dataclasses.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/dataclasses.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/sysconfig.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7409090909090909%*

 * *Differences: {"'data_mtime'": '1680278524',*

 * * "'dep_lines'": '{insert: [(3, 1), (4, 1)], delete: [7, 6, 5, 4, 0]}',*

 * * "'dep_prios'": '{insert: [(4, 30)], delete: [4, 3, 1, 0]}',*

 * * "'dependencies'": "{insert: [(3, 'builtins'), (4, '_typeshed')], delete: [5, 4, 3, 1, 0]}",*

 * * "'hash'": "'6b911010944cddd5dba0058e155c1c02bcc9bedde4553b1f04a9a54e46fffd68'",*

 * * "'id'": "'sysconfig'",*

 * * "'interface_hash'": "'0e44f2d044b64af2c89b0bc366a5b5d465d06eeb0f50e90def8c5f9c32e5c96a'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/pyth […]*

```diff
@@ -1,46 +1,37 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680278524,
     "dep_lines": [
-        6,
         1,
         2,
         3,
-        4,
-        5,
-        7,
-        8,
+        1,
+        1,
         1
     ],
     "dep_prios": [
-        5,
-        10,
         10,
         5,
         5,
         5,
-        5,
-        5,
+        30,
         30
     ],
     "dependencies": [
-        "collections.abc",
-        "enum",
         "sys",
-        "types",
-        "_typeshed",
-        "builtins",
         "typing",
         "typing_extensions",
+        "builtins",
+        "_typeshed",
         "abc"
     ],
-    "hash": "ffd75c9498e57a272219ee18fced3f082acfead1fef3a594524c2b81076bb215",
-    "id": "dataclasses",
+    "hash": "6b911010944cddd5dba0058e155c1c02bcc9bedde4553b1f04a9a54e46fffd68",
+    "id": "sysconfig",
     "ignore_all": true,
-    "interface_hash": "5b8dd43c6269dbf1094b7e8b564145e866fd03e7468954393c99148b059ddf68",
+    "interface_hash": "0e44f2d044b64af2c89b0bc366a5b5d465d06eeb0f50e90def8c5f9c32e5c96a",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -75,13 +66,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/dataclasses.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/sysconfig.pyi",
     "plugin_data": null,
-    "size": 8816,
+    "size": 1399,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/datetime.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/datetime.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/datetime.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/datetime.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/decimal.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/decimal.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/decimal.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/decimal.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/dev.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/__init__.data.json`

 * *Files 11% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8129783163265306%*

 * *Differences: {"'_fullname'": "'_pytest'",*

 * * "'names'": "{'__annotations__': {'node': {'fullname': '_pytest.__annotations__'}, "*

 * *            "'module_public': False}, '__doc__': {'node': {'fullname': '_pytest.__doc__'}, "*

 * *            "'module_public': False}, '__file__': {'node': {'fullname': '_pytest.__file__'}, "*

 * *            "'module_public': False}, '__name__': {'node': {'fullname': '_pytest.__name__'}, "*

 * *            "'module_public': False}, '__package__': {'node': {'fullname': '_pytest.__package__'}, "*

 * *            "' […]*

```diff
@@ -1,24 +1,46 @@
 {
     ".class": "MypyFile",
-    "_fullname": "dev",
+    "_fullname": "_pytest",
     "future_import_flags": [],
     "is_partial_stub_package": false,
     "is_stub": false,
     "names": {
         ".class": "SymbolTable",
+        "__all__": {
+            ".class": "SymbolTableNode",
+            "kind": "Gdef",
+            "module_public": false,
+            "node": {
+                ".class": "Var",
+                "flags": [
+                    "is_inferred",
+                    "has_explicit_value"
+                ],
+                "fullname": "_pytest.__all__",
+                "name": "__all__",
+                "type": {
+                    ".class": "Instance",
+                    "args": [
+                        "builtins.str"
+                    ],
+                    "type_ref": "builtins.list"
+                }
+            }
+        },
         "__annotations__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
+            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "dev.__annotations__",
+                "fullname": "_pytest.__annotations__",
                 "name": "__annotations__",
                 "type": {
                     ".class": "Instance",
                     "args": [
                         "builtins.str",
                         {
                             ".class": "AnyType",
@@ -30,114 +52,93 @@
                     "type_ref": "builtins.dict"
                 }
             }
         },
         "__doc__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
+            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "dev.__doc__",
+                "fullname": "_pytest.__doc__",
                 "name": "__doc__",
                 "type": "builtins.str"
             }
         },
         "__file__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
+            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "dev.__file__",
+                "fullname": "_pytest.__file__",
                 "name": "__file__",
                 "type": "builtins.str"
             }
         },
         "__name__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
+            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "dev.__name__",
+                "fullname": "_pytest.__name__",
                 "name": "__name__",
                 "type": "builtins.str"
             }
         },
         "__package__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
+            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "dev.__package__",
+                "fullname": "_pytest.__package__",
                 "name": "__package__",
                 "type": "builtins.str"
             }
         },
-        "data": {
+        "__path__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
+            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
-                    "is_inferred",
-                    "has_explicit_value"
+                    "is_ready"
                 ],
-                "fullname": "dev.data",
-                "name": "data",
+                "fullname": "_pytest.__path__",
+                "name": "__path__",
                 "type": {
                     ".class": "Instance",
                     "args": [
-                        "builtins.str",
-                        "builtins.object"
+                        "builtins.str"
                     ],
-                    "type_ref": "builtins.dict"
+                    "type_ref": "builtins.list"
                 }
             }
         },
-        "json": {
-            ".class": "SymbolTableNode",
-            "cross_ref": "json",
-            "kind": "Gdef",
-            "module_hidden": true,
-            "module_public": false
-        },
-        "jsonpath": {
+        "__version__": {
             ".class": "SymbolTableNode",
-            "cross_ref": "jsonpath",
-            "kind": "Gdef",
-            "module_hidden": true,
-            "module_public": false
+            "cross_ref": "_pytest._version.version",
+            "kind": "Gdef"
         },
-        "products": {
+        "version_tuple": {
             ".class": "SymbolTableNode",
-            "kind": "Gdef",
-            "node": {
-                ".class": "Var",
-                "flags": [
-                    "is_inferred",
-                    "has_explicit_value"
-                ],
-                "fullname": "dev.products",
-                "name": "products",
-                "type": {
-                    ".class": "Instance",
-                    "args": [
-                        "builtins.object"
-                    ],
-                    "type_ref": "builtins.list"
-                }
-            }
+            "cross_ref": "_pytest._version.version_tuple",
+            "kind": "Gdef"
         }
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/dev.py"
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/_pytest/__init__.py"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/dev.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/cache.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.6939393939393939%*

 * *Differences: {"'data_mtime'": '1679859772',*

 * * "'dep_lines'": '{insert: [(0, 36), (1, 38), (2, 39), (3, 41)], delete: [3, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(1, 5), (2, 5), (3, 5), (4, 5)], delete: [4, 3, 1, 0]}',*

 * * "'dependencies'": "{insert: [(0, '__future__'), (1, 'collections'), (2, 'threading'), (3, "*

 * *                   "'typing')], delete: [6, 5, 1, 0]}",*

 * * "'hash'": "'6ab0d821d4b0f6dc01be3f912198684641f3cb7366f42ddb23afae0a445fa999'",*

 * * "'id'": "'jsonpath.cache'",*

 * * "'interface_hash'": "'01b6cf90e67516f123ed7f1d42c […]*

```diff
@@ -1,41 +1,41 @@
 {
-    "data_mtime": 1680278342,
+    "data_mtime": 1679859772,
     "dep_lines": [
-        1,
-        2,
-        1,
-        1,
+        36,
+        38,
+        39,
+        41,
         1,
         1,
         1
     ],
     "dep_prios": [
-        10,
-        10,
         5,
-        30,
-        30,
+        5,
+        5,
+        5,
+        5,
         30,
         30
     ],
     "dependencies": [
-        "json",
-        "jsonpath",
+        "__future__",
+        "collections",
+        "threading",
+        "typing",
         "builtins",
         "_typeshed",
-        "abc",
-        "json.encoder",
-        "typing"
+        "abc"
     ],
-    "hash": "c450ccff29b5bc0b05dde5a4e7a166a1561b5459a76ba62be47903e80eb18211",
-    "id": "dev",
+    "hash": "6ab0d821d4b0f6dc01be3f912198684641f3cb7366f42ddb23afae0a445fa999",
+    "id": "jsonpath.cache",
     "ignore_all": false,
-    "interface_hash": "a5244e58cf9e8c0206558c0fc82abef37280425a8c0bf931a79030e0dcb8960e",
-    "mtime": 1680278387,
+    "interface_hash": "01b6cf90e67516f123ed7f1d42c84b851317dfd135ab814dd7fb3f17228a1d61",
+    "mtime": 1679859865,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -69,13 +69,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/dev.py",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/cache.py",
     "plugin_data": null,
-    "size": 1138,
+    "size": 5899,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/difflib.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/difflib.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/difflib.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/difflib.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/dis.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/dis.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/dis.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/socket.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7388017429193899%*

 * *Differences: {"'data_mtime'": '1680161756',*

 * * "'dep_lines'": '{insert: [(0, 116), (3, 115), (4, 117), (5, 118), (6, 119), (7, 120), (8, 1), (9, '*

 * *                '1), (10, 1)], delete: [5, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(1, 5), (3, 5), (4, 5), (9, 30), (10, 30), (11, 30)], delete: [1]}',*

 * * "'dependencies'": "{insert: [(1, '_socket'), (3, '_typeshed'), (4, 'enum'), (5, 'io'), (10, "*

 * *                   "'array'), (11, 'ctypes'), (12, 'mmap'), (13, 'pickle')], delete: [7, 3, 2]}",*

 * * "'hash'": "'9b55cc26e3ab1353951b904 […]*

```diff
@@ -1,46 +1,61 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680161756,
     "dep_lines": [
-        3,
-        1,
-        2,
+        116,
         4,
         5,
-        6,
+        115,
+        117,
+        118,
+        119,
+        120,
+        1,
+        1,
+        1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
+        5,
         10,
-        10,
         5,
         5,
         5,
         5,
+        5,
+        5,
+        30,
+        30,
+        30,
         30,
         30
     ],
     "dependencies": [
         "collections.abc",
+        "_socket",
         "sys",
-        "types",
-        "opcode",
+        "_typeshed",
+        "enum",
+        "io",
         "typing",
         "typing_extensions",
         "builtins",
-        "_typeshed",
-        "abc"
+        "abc",
+        "array",
+        "ctypes",
+        "mmap",
+        "pickle"
     ],
-    "hash": "0752728fe06a3c30c30280311b749ec46eee32ec08b5ec9221c552757dd04ca7",
-    "id": "dis",
+    "hash": "9b55cc26e3ab1353951b9041461f39c315fb58b9805f94327c5212f4b90c4908",
+    "id": "socket",
     "ignore_all": true,
-    "interface_hash": "dcde734b3f10aeb177c0cb25c530c9ce6e810fb07f1445cf96cd0352e7383b33",
+    "interface_hash": "e8458adedcebf163b3e1cb59307d19cca1f972c07ac38eb026a41b2a7bcfc3e9",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -75,13 +90,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/dis.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/socket.pyi",
     "plugin_data": null,
-    "size": 4403,
+    "size": 28022,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/doctest.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/doctest.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/doctest.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/doctest.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/enum.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/enum.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/enum.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/itertools.meta.json`

 * *Files 4% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7358730158730159%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(1, 1), (3, 4), (4, 7), (5, 1), (6, 1), (7, 1)], delete: [7, 6, 5, 4, '*

 * *                '1, 0]}',*

 * * "'dep_prios'": '{insert: [(6, 30), (7, 30)], delete: [2, 0]}',*

 * * "'dependencies'": "{insert: [(4, 'types'), (5, 'builtins'), (6, '_typeshed'), (7, 'abc')], "*

 * *                   'delete: [5, 4, 3, 1]}',*

 * * "'hash'": "'8d452d6d11a70ac8cf92f7f8ca2f0ec391f06ffd520b0a5e9c6083b3efe75b5d'",*

 * * "'id'": "'itertools'",*

 * * "'interface_hash'": "'2129ea33c5fac659a28848e6d0 […]*

```diff
@@ -1,43 +1,43 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        7,
-        1,
         2,
+        1,
         3,
-        5,
-        6,
-        8,
-        9
+        4,
+        7,
+        1,
+        1,
+        1
     ],
     "dep_prios": [
         5,
-        5,
-        10,
         10,
         5,
         5,
         5,
-        5
+        5,
+        30,
+        30
     ],
     "dependencies": [
         "collections.abc",
-        "_typeshed",
         "sys",
+        "typing",
+        "typing_extensions",
         "types",
-        "abc",
         "builtins",
-        "typing",
-        "typing_extensions"
+        "_typeshed",
+        "abc"
     ],
-    "hash": "70b30897b521ffb90251c805cd8ed4dfb35b1dd86134b06669a5dd31a90cbfa5",
-    "id": "enum",
+    "hash": "8d452d6d11a70ac8cf92f7f8ca2f0ec391f06ffd520b0a5e9c6083b3efe75b5d",
+    "id": "itertools",
     "ignore_all": true,
-    "interface_hash": "19beccd3f73f5ba0f60956cad001a0f51a1925e7afa2a142a2fb60531027925d",
+    "interface_hash": "2129ea33c5fac659a28848e6d094ad3a9de54391ba14d079707deae4849c0c99",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -72,13 +72,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/enum.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/itertools.pyi",
     "plugin_data": null,
-    "size": 10061,
+    "size": 10908,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/errno.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/errno.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/errno.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/errno.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/fnmatch.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/fnmatch.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/fnmatch.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/fnmatch.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/functools.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/functools.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/functools.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/functools.meta.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         4,
         1,
         2,
         3,
         5,
         6,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/gc.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/gc.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/gc.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/gc.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/genericpath.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/genericpath.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/genericpath.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/genericpath.meta.json`

 * *Files 5% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         3,
         1,
         2,
         4,
         5,
         1,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/getpass.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/getpass.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/getpass.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/getpass.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/gettext.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/gettext.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/gettext.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/gettext.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/glob.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/glob.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/glob.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/glob.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/inspect.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/inspect.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/inspect.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/inspect.meta.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         6,
         1,
         2,
         3,
         4,
         5,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/io.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/io.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/io.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/io.meta.json`

 * *Files 5% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         6,
         1,
         2,
         3,
         4,
         5,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/itertools.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/itertools.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/itertools.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/pprint.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7564814814814814%*

 * *Differences: {"'data_mtime'": '1680278525',*

 * * "'dep_lines'": '{insert: [(1, 2)], delete: [4, 3, 2, 0]}',*

 * * "'dep_prios'": '{delete: [3, 2, 0]}',*

 * * "'dependencies'": '{delete: [4, 3, 0]}',*

 * * "'hash'": "'78a47e4955ce4623d31fabbe4f6e6f0dd95985479353aea46ff2c3054f362a4f'",*

 * * "'id'": "'pprint'",*

 * * "'interface_hash'": "'4997a06a9a722d958fa08c24dc761cf2485e948dac42c187da519f5cd59cc746'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/ […]*

```diff
@@ -1,43 +1,34 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680278525,
     "dep_lines": [
-        2,
         1,
-        3,
-        4,
-        7,
+        2,
         1,
         1,
         1
     ],
     "dep_prios": [
-        5,
         10,
         5,
         5,
-        5,
-        5,
         30,
         30
     ],
     "dependencies": [
-        "collections.abc",
         "sys",
         "typing",
-        "typing_extensions",
-        "types",
         "builtins",
         "_typeshed",
         "abc"
     ],
-    "hash": "8d452d6d11a70ac8cf92f7f8ca2f0ec391f06ffd520b0a5e9c6083b3efe75b5d",
-    "id": "itertools",
+    "hash": "78a47e4955ce4623d31fabbe4f6e6f0dd95985479353aea46ff2c3054f362a4f",
+    "id": "pprint",
     "ignore_all": true,
-    "interface_hash": "2129ea33c5fac659a28848e6d094ad3a9de54391ba14d079707deae4849c0c99",
+    "interface_hash": "4997a06a9a722d958fa08c24dc761cf2485e948dac42c187da519f5cd59cc746",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -72,13 +63,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/itertools.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/pprint.pyi",
     "plugin_data": null,
-    "size": 10908,
+    "size": 3857,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/marshal.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/marshal.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/marshal.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/marshal.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/math.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/math.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/math.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/math.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/mmap.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/mmap.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/mmap.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/mmap.meta.json`

 * *Files 4% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         3,
         1,
         2,
         4,
         5,
         1,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/numbers.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/numbers.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/numbers.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/numbers.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/opcode.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/opcode.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/opcode.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/opcode.meta.json`

 * *Files 5% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
         2,
         1,
         1,
         1,
         1
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/operator.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/operator.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/operator.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/operator.meta.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
         2,
         1,
         1,
         1,
         1,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/pathlib.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/pathlib.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/pathlib.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/urllib/parse.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7413515406162465%*

 * *Differences: {"'data_mtime'": '1680278525',*

 * * "'dep_lines'": '{insert: [(2, 3), (3, 4), (4, 7)], delete: [9, 8, 7, 6, 5, 4, 3, 1, 0]}',*

 * * "'dep_prios'": '{delete: [11, 10, 9, 4, 3, 2]}',*

 * * "'dependencies'": "{insert: [(4, 'types'), (6, '_typeshed')], delete: [13, 12, 11, 10, 5, 4, 3, "*

 * *                   '2]}',*

 * * "'hash'": "'c63b9b79f7fc54b266cad001ebf899091051353c61578cd27445312e0553b969'",*

 * * "'id'": "'urllib.parse'",*

 * * "'interface_hash'": "'0821d0c5abfa0147f9ab49034b5abe71d40e92be08730c5871847440c633fef6'",*

 * * "'path'": "'/ho […]*

```diff
@@ -1,61 +1,43 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680278525,
     "dep_lines": [
-        12,
-        1,
         2,
-        13,
-        14,
-        15,
-        16,
-        17,
-        1,
-        1,
         1,
+        3,
+        4,
+        7,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
         10,
         5,
         5,
         5,
         5,
-        5,
-        5,
-        5,
-        30,
-        30,
-        30,
         30,
         30
     ],
     "dependencies": [
         "collections.abc",
         "sys",
-        "_typeshed",
-        "io",
-        "os",
-        "types",
         "typing",
         "typing_extensions",
+        "types",
         "builtins",
-        "abc",
-        "array",
-        "ctypes",
-        "mmap",
-        "pickle"
+        "_typeshed",
+        "abc"
     ],
-    "hash": "04a9e436986cd9b24089af97b33a4ce12d691429398e3de21b63d203baa68ccf",
-    "id": "pathlib",
+    "hash": "c63b9b79f7fc54b266cad001ebf899091051353c61578cd27445312e0553b969",
+    "id": "urllib.parse",
     "ignore_all": true,
-    "interface_hash": "8d6296e9f5172aca44955748a80ab51a6efdcda7f533f534c61e309b11e45c18",
+    "interface_hash": "0821d0c5abfa0147f9ab49034b5abe71d40e92be08730c5871847440c633fef6",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -90,13 +72,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/pathlib.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/urllib/parse.pyi",
     "plugin_data": null,
-    "size": 7941,
+    "size": 7050,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/pdb.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/pdb.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/pdb.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/selectors.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7532738095238095%*

 * *Differences: {"'data_mtime'": '1680161756',*

 * * "'dep_lines'": '{insert: [(0, 4), (4, 5)], delete: [8, 7, 6, 4, 0]}',*

 * * "'dep_prios'": '{delete: [4, 3, 1]}',*

 * * "'dependencies'": "{insert: [(2, '_typeshed'), (3, 'abc'), (7, 'array'), (8, 'ctypes'), (9, "*

 * *                   "'mmap'), (10, 'pickle')], delete: [13, 12, 11, 10, 6, 5, 4, 3, 1]}",*

 * * "'hash'": "'d248f792ad4a4d57dc0d4633bdb245930e838ba41ae6eea4fe53fe933521ee65'",*

 * * "'id'": "'selectors'",*

 * * "'interface_hash'": "'14d3c765b2c9cc45a24852a7f0ded97bb6d23c073bb03f2cf6498b44613 […]*

```diff
@@ -1,61 +1,52 @@
 {
-    "data_mtime": 1680278526,
+    "data_mtime": 1680161756,
     "dep_lines": [
-        5,
+        4,
         1,
         2,
         3,
-        4,
+        5,
         6,
-        7,
-        8,
-        9,
         1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
         10,
-        10,
-        5,
-        5,
         5,
         5,
         5,
         5,
         5,
         30,
         30,
         30,
         30
     ],
     "dependencies": [
         "collections.abc",
-        "signal",
         "sys",
-        "bdb",
-        "cmd",
-        "inspect",
-        "types",
+        "_typeshed",
+        "abc",
         "typing",
         "typing_extensions",
         "builtins",
-        "_typeshed",
-        "abc",
-        "ast",
-        "enum"
+        "array",
+        "ctypes",
+        "mmap",
+        "pickle"
     ],
-    "hash": "f28fa38985ef2d556366b0116f8569533bca86d686aeac3663f62f8bfabf2e62",
-    "id": "pdb",
+    "hash": "d248f792ad4a4d57dc0d4633bdb245930e838ba41ae6eea4fe53fe933521ee65",
+    "id": "selectors",
     "ignore_all": true,
-    "interface_hash": "d7514e6d33ee85ec36910cd86f7b783dcb01c6727effb73c4078b2ab517a7c6e",
+    "interface_hash": "14d3c765b2c9cc45a24852a7f0ded97bb6d23c073bb03f2cf6498b44613cba23",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -90,13 +81,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/pdb.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/selectors.pyi",
     "plugin_data": null,
-    "size": 7379,
+    "size": 3729,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/pickle.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/pickle.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/pickle.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/pickle.meta.json`

 * *Files 4% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         3,
         1,
         2,
         4,
         5,
         1,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/pkgutil.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/pkgutil.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/pkgutil.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/pkgutil.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/platform.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/platform.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/platform.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/platform.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/posixpath.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/posixpath.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/posixpath.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/posixpath.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         3,
         1,
         2,
         4,
         17,
         18,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/pprint.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/pprint.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/pprint.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/time.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7571428571428572%*

 * *Differences: {"'data_mtime'": '1680161756',*

 * * "'dep_lines'": '{insert: [(2, 3), (3, 4)], delete: [2]}',*

 * * "'dep_prios'": '{insert: [(3, 5), (4, 5)], delete: [3]}',*

 * * "'dependencies'": "{insert: [(1, '_typeshed'), (3, 'typing_extensions')], delete: [3]}",*

 * * "'hash'": "'81ee1e52c98cc1cd26d7a6aa6d5a9c23d100b4e14cdd725b405a720187e41f8c'",*

 * * "'id'": "'time'",*

 * * "'interface_hash'": "'b8990f6368b6d084c40909e654516f4ea726a64dd2f94f85baef1ee135868287'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/p […]*

```diff
@@ -1,34 +1,37 @@
 {
-    "data_mtime": 1680278525,
+    "data_mtime": 1680161756,
     "dep_lines": [
         1,
         2,
-        1,
+        3,
+        4,
         1,
         1
     ],
     "dep_prios": [
         10,
         5,
         5,
-        30,
+        5,
+        5,
         30
     ],
     "dependencies": [
         "sys",
+        "_typeshed",
         "typing",
+        "typing_extensions",
         "builtins",
-        "_typeshed",
         "abc"
     ],
-    "hash": "78a47e4955ce4623d31fabbe4f6e6f0dd95985479353aea46ff2c3054f362a4f",
-    "id": "pprint",
+    "hash": "81ee1e52c98cc1cd26d7a6aa6d5a9c23d100b4e14cdd725b405a720187e41f8c",
+    "id": "time",
     "ignore_all": true,
-    "interface_hash": "4997a06a9a722d958fa08c24dc761cf2485e948dac42c187da519f5cd59cc746",
+    "interface_hash": "b8990f6368b6d084c40909e654516f4ea726a64dd2f94f85baef1ee135868287",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -63,13 +66,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/pprint.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/time.pyi",
     "plugin_data": null,
-    "size": 3857,
+    "size": 3663,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/queue.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/queue.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/queue.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/queue.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/re.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/re.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/re.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/re.meta.json`

 * *Files 5% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         5,
         1,
         2,
         3,
         4,
         6,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/reprlib.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/reprlib.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/reprlib.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/reprlib.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/selectors.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/selectors.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/selectors.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/warnings.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7563325563325562%*

 * *Differences: {"'data_mtime'": '1680278525',*

 * * "'dep_lines'": '{insert: [(0, 3), (3, 4)], delete: [7, 6, 3, 0]}',*

 * * "'dep_prios'": '{delete: [8, 7]}',*

 * * "'dependencies'": "{insert: [(2, '_warnings'), (3, 'types'), (7, '_typeshed'), (8, 'abc')], "*

 * *                   'delete: [10, 9, 8, 7, 3, 2]}',*

 * * "'hash'": "'9a991da6c7cb550f45efd87385ec22f61a45c69511ab3af2594b6d1ce0487343'",*

 * * "'id'": "'warnings'",*

 * * "'interface_hash'": "'1c3a1b98599df08099646f61ef07ed3e591c08dff1813caa0b815a6fde82ba9a'",*

 * * "'path'": "'/home/james/.local/shar […]*

```diff
@@ -1,52 +1,46 @@
 {
-    "data_mtime": 1680161756,
+    "data_mtime": 1680278525,
     "dep_lines": [
-        4,
+        3,
         1,
         2,
-        3,
+        4,
         5,
         6,
         1,
         1,
-        1,
-        1,
         1
     ],
     "dep_prios": [
         5,
         10,
         5,
         5,
         5,
         5,
         5,
         30,
-        30,
-        30,
         30
     ],
     "dependencies": [
         "collections.abc",
         "sys",
-        "_typeshed",
-        "abc",
+        "_warnings",
+        "types",
         "typing",
         "typing_extensions",
         "builtins",
-        "array",
-        "ctypes",
-        "mmap",
-        "pickle"
+        "_typeshed",
+        "abc"
     ],
-    "hash": "d248f792ad4a4d57dc0d4633bdb245930e838ba41ae6eea4fe53fe933521ee65",
-    "id": "selectors",
+    "hash": "9a991da6c7cb550f45efd87385ec22f61a45c69511ab3af2594b6d1ce0487343",
+    "id": "warnings",
     "ignore_all": true,
-    "interface_hash": "14d3c765b2c9cc45a24852a7f0ded97bb6d23c073bb03f2cf6498b44613cba23",
+    "interface_hash": "1c3a1b98599df08099646f61ef07ed3e591c08dff1813caa0b815a6fde82ba9a",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -81,13 +75,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/selectors.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/warnings.pyi",
     "plugin_data": null,
-    "size": 3729,
+    "size": 3682,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/shlex.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/shlex.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/shlex.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/shlex.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/shutil.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/shutil.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/shutil.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/shutil.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/signal.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/signal.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/signal.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/signal.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/socket.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/socket.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/socket.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/ssl.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7846801346801348%*

 * *Differences: {"'dep_lines'": '{insert: [(1, 1), (2, 2), (3, 3), (4, 4), (5, 6), (6, 7), (7, 1), (8, 1)], '*

 * *                'delete: [7, 6, 5, 4, 3, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(2, 10), (3, 10), (8, 30), (9, 30)], delete: [4, 3, 0]}',*

 * * "'dependencies'": "{insert: [(1, 'enum'), (2, 'socket'), (8, '_socket'), (13, 'os')], delete: [5, "*

 * *                   '4, 1]}',*

 * * "'hash'": "'8af07ef5dc59da8c89212191867912df01e842128a36b021b665eb9ad14d096a'",*

 * * "'id'": "'ssl'",*

 * * "'interface_hash'": "'e6f87ca6bae07cda21f6d29401d1720 […]*

```diff
@@ -1,61 +1,64 @@
 {
     "data_mtime": 1680161756,
     "dep_lines": [
-        116,
-        4,
         5,
-        115,
-        117,
-        118,
-        119,
-        120,
+        1,
+        2,
+        3,
+        4,
+        6,
+        7,
+        1,
+        1,
         1,
         1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
-        5,
+        10,
+        10,
         10,
         5,
         5,
         5,
         5,
-        5,
-        5,
+        30,
+        30,
         30,
         30,
         30,
         30,
         30
     ],
     "dependencies": [
         "collections.abc",
-        "_socket",
+        "enum",
+        "socket",
         "sys",
         "_typeshed",
-        "enum",
-        "io",
         "typing",
         "typing_extensions",
         "builtins",
+        "_socket",
         "abc",
         "array",
         "ctypes",
         "mmap",
+        "os",
         "pickle"
     ],
-    "hash": "9b55cc26e3ab1353951b9041461f39c315fb58b9805f94327c5212f4b90c4908",
-    "id": "socket",
+    "hash": "8af07ef5dc59da8c89212191867912df01e842128a36b021b665eb9ad14d096a",
+    "id": "ssl",
     "ignore_all": true,
-    "interface_hash": "e8458adedcebf163b3e1cb59307d19cca1f972c07ac38eb026a41b2a7bcfc3e9",
+    "interface_hash": "e6f87ca6bae07cda21f6d29401d1720e8c33870594354e954d98f95ca389517f",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -90,13 +93,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/socket.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/ssl.pyi",
     "plugin_data": null,
-    "size": 28022,
+    "size": 18248,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/sre_compile.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/sre_compile.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/sre_compile.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/sre_compile.meta.json`

 * *Files 0% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
         2,
         4,
         5,
         1,
         1
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/sre_constants.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/sre_constants.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/sre_constants.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/sre_constants.meta.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
         2,
         3,
         1,
         1,
         1
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/sre_parse.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/sre_parse.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/sre_parse.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/email/charset.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7396296296296296%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{delete: [5, 4, 3, 2, 0]}',*

 * * "'dep_prios'": '{delete: [4, 3, 2, 1, 0]}',*

 * * "'dependencies'": "{insert: [(3, 'typing')], delete: [7, 5, 4, 3, 2, 1]}",*

 * * "'hash'": "'46b806f04d1179ba7b23c108135be7153f457b638c352804a5b1338d1e9347fa'",*

 * * "'id'": "'email.charset'",*

 * * "'interface_hash'": "'668ed651e7fb7b39fdc4f4003c79dbf09eb4f3802ef03607bd07f6142c8d9e19'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/sit […]*

```diff
@@ -1,46 +1,31 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        2,
         1,
-        3,
-        4,
-        6,
-        7,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
-        10,
-        5,
-        5,
-        5,
-        5,
         5,
         30,
         30
     ],
     "dependencies": [
         "collections.abc",
-        "sys",
-        "re",
-        "sre_constants",
-        "typing",
-        "typing_extensions",
         "builtins",
-        "_typeshed",
-        "abc"
+        "abc",
+        "typing"
     ],
-    "hash": "38b6a819e544b584ec71b7040293fae6a77f2447fc14e9bc70e752ec237c8022",
-    "id": "sre_parse",
+    "hash": "46b806f04d1179ba7b23c108135be7153f457b638c352804a5b1338d1e9347fa",
+    "id": "email.charset",
     "ignore_all": true,
-    "interface_hash": "2b13eb3b1350bf942354e90a97500dd0a3fe206b98e910edcb745cb1aadcff2a",
+    "interface_hash": "668ed651e7fb7b39fdc4f4003c79dbf09eb4f3802ef03607bd07f6142c8d9e19",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -75,13 +60,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/sre_parse.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/email/charset.pyi",
     "plugin_data": null,
-    "size": 4069,
+    "size": 1077,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/ssl.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/ssl.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/ssl.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tempfile.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7501225490196078%*

 * *Differences: {"'data_mtime'": '1680278525',*

 * * "'dep_lines'": '{insert: [(0, 4), (4, 5)], delete: [11, 10, 9, 8, 7, 4, 0]}',*

 * * "'dep_prios'": '{insert: [(7, 5)], delete: [12, 11, 10, 9, 8, 1]}',*

 * * "'dependencies'": "{insert: [(1, 'io'), (4, 'types')], delete: [14, 12, 11, 10, 8, 2, 1]}",*

 * * "'hash'": "'f4ec890533fa3c342a29c868f57b9e039c99856c9ef6f4df798031b93671dcc1'",*

 * * "'id'": "'tempfile'",*

 * * "'interface_hash'": "'e60018bfec73976dfa94fdaa45dd3f0407e721fa2b20e0c4672a91639e41f8b4'",*

 * * "'path'": "'/home/james/.local/share/hatch/e […]*

```diff
@@ -1,64 +1,49 @@
 {
-    "data_mtime": 1680161756,
+    "data_mtime": 1680278525,
     "dep_lines": [
-        5,
+        4,
         1,
         2,
         3,
-        4,
+        5,
         6,
         7,
         1,
         1,
-        1,
-        1,
-        1,
-        1,
-        1,
         1
     ],
     "dep_prios": [
         5,
         10,
         10,
-        10,
         5,
         5,
         5,
         5,
-        30,
-        30,
-        30,
-        30,
-        30,
+        5,
         30,
         30
     ],
     "dependencies": [
         "collections.abc",
-        "enum",
-        "socket",
+        "io",
         "sys",
         "_typeshed",
+        "types",
         "typing",
         "typing_extensions",
         "builtins",
-        "_socket",
         "abc",
-        "array",
-        "ctypes",
-        "mmap",
-        "os",
-        "pickle"
+        "os"
     ],
-    "hash": "8af07ef5dc59da8c89212191867912df01e842128a36b021b665eb9ad14d096a",
-    "id": "ssl",
+    "hash": "f4ec890533fa3c342a29c868f57b9e039c99856c9ef6f4df798031b93671dcc1",
+    "id": "tempfile",
     "ignore_all": true,
-    "interface_hash": "e6f87ca6bae07cda21f6d29401d1720e8c33870594354e954d98f95ca389517f",
+    "interface_hash": "e60018bfec73976dfa94fdaa45dd3f0407e721fa2b20e0c4672a91639e41f8b4",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -93,13 +78,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/ssl.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/tempfile.pyi",
     "plugin_data": null,
-    "size": 18248,
+    "size": 16433,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/stat.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/stat.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/stat.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/stat.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/string.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/string.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/string.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/string.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/struct.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/struct.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/struct.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/struct.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/subprocess.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/subprocess.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/subprocess.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/subprocess.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         3,
         1,
         2,
         4,
         5,
         6,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/sys.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/sys.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/sys.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/futures.meta.json`

 * *Files 10% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7371428571428571%*

 * *Differences: {"'data_mtime'": '1680161757',*

 * * "'dep_lines'": '{insert: [(1, 2), (3, 1), (4, 4), (5, 5), (6, 14), (7, 17), (8, 1), (9, 1), (10, '*

 * *                '1)], delete: [8, 7, 6, 3, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(3, 10), (9, 30), (10, 30)], delete: [0]}',*

 * * "'dependencies'": "{insert: [(0, 'concurrent.futures._base'), (2, 'asyncio.events'), (3, 'sys'), "*

 * *                   "(6, 'contextvars'), (7, 'types'), (8, 'builtins'), (9, '_typeshed'), (11, "*

 * *                   "'concurrent'), (12, 'concurrent.futures […]*

```diff
@@ -1,52 +1,58 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680161757,
     "dep_lines": [
-        4,
-        5,
-        6,
-        2,
         3,
+        2,
         7,
-        8,
-        9,
-        10,
+        1,
+        4,
+        5,
+        14,
+        17,
+        1,
+        1,
+        1,
         1,
         1
     ],
     "dep_prios": [
         5,
         5,
         5,
+        10,
         5,
         5,
         5,
         5,
         5,
-        5,
+        30,
+        30,
         30,
         30
     ],
     "dependencies": [
+        "concurrent.futures._base",
         "collections.abc",
-        "importlib.abc",
-        "importlib.machinery",
-        "_typeshed",
-        "builtins",
-        "io",
-        "types",
+        "asyncio.events",
+        "sys",
         "typing",
         "typing_extensions",
+        "contextvars",
+        "types",
+        "builtins",
+        "_typeshed",
         "abc",
-        "importlib"
+        "concurrent",
+        "concurrent.futures"
     ],
-    "hash": "41b700a469a256dbdbd61fd54c34f7da58b4b2a5d2f59b8cbe26658fc8b53151",
-    "id": "sys",
+    "hash": "05b7db98d28d7040cb68bed2bfac7f655fd484552261e885a9c9fd1888e66b18",
+    "id": "asyncio.futures",
     "ignore_all": true,
-    "interface_hash": "dd60be164d6e830e52d78afa1d413846bd0954dbda40a73b294727bcc2d666e8",
+    "interface_hash": "f0eac0683b34751b1ba0339dceabd893acdb88735989af8e6f1bdb8fd71ef64e",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -81,13 +87,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/sys.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/asyncio/futures.pyi",
     "plugin_data": null,
-    "size": 11286,
+    "size": 2644,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/sysconfig.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/sysconfig.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/sysconfig.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/_base.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7454545454545455%*

 * *Differences: {"'data_mtime'": '1680161756',*

 * * "'dep_lines'": '{insert: [(0, 4), (4, 5), (5, 6), (6, 7), (7, 8)], delete: [3]}',*

 * * "'dep_prios'": '{insert: [(0, 5), (1, 10), (6, 5), (7, 5), (8, 5)], delete: [4]}',*

 * * "'dependencies'": "{insert: [(0, 'collections.abc'), (2, 'threading'), (3, '_typeshed'), (4, "*

 * *                   "'logging'), (5, 'types')], delete: [4]}",*

 * * "'hash'": "'3f849a90b4bfad984ace2908d3926de071c8c9f62fc0af5bdbcb6e94fec4b77e'",*

 * * "'id'": "'concurrent.futures._base'",*

 * * "'interface_hash'": "'bc94ee0778697 […]*

```diff
@@ -1,37 +1,49 @@
 {
-    "data_mtime": 1680278524,
+    "data_mtime": 1680161756,
     "dep_lines": [
+        4,
         1,
         2,
         3,
-        1,
+        5,
+        6,
+        7,
+        8,
         1,
         1
     ],
     "dep_prios": [
+        5,
         10,
+        10,
+        5,
+        5,
+        5,
         5,
         5,
         5,
-        30,
         30
     ],
     "dependencies": [
+        "collections.abc",
         "sys",
+        "threading",
+        "_typeshed",
+        "logging",
+        "types",
         "typing",
         "typing_extensions",
         "builtins",
-        "_typeshed",
         "abc"
     ],
-    "hash": "6b911010944cddd5dba0058e155c1c02bcc9bedde4553b1f04a9a54e46fffd68",
-    "id": "sysconfig",
+    "hash": "3f849a90b4bfad984ace2908d3926de071c8c9f62fc0af5bdbcb6e94fec4b77e",
+    "id": "concurrent.futures._base",
     "ignore_all": true,
-    "interface_hash": "0e44f2d044b64af2c89b0bc366a5b5d465d06eeb0f50e90def8c5f9c32e5c96a",
+    "interface_hash": "bc94ee07786973308a53770091026d58c533a1904272196e7635fd416a4cfcdc",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -66,13 +78,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/sysconfig.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/concurrent/futures/_base.pyi",
     "plugin_data": null,
-    "size": 1399,
+    "size": 4187,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tempfile.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tempfile.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tempfile.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/os/__init__.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7367063492063491%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 23), (1, 30), (4, 21), (5, 22), (6, 24), (7, 25), (8, 26), (9, 27), '*

 * *                '(10, 28), (11, 33), (12, 1)], delete: [6, 5, 4, 3, 0]}',*

 * * "'dep_prios'": '{insert: [(3, 5), (4, 5), (5, 5), (6, 5), (12, 30), (13, 30)]}',*

 * * "'dependencies'": "{insert: [(1, 'os.path'), (4, 'abc'), (5, 'builtins'), (6, 'contextlib'), (7, "*

 * *                   "'io'), (8, 'subprocess'), (11, 'types'), (12, 'array'), (13, 'ctypes'), (14, "*

 * *                   "'mmap […]*

```diff
@@ -1,49 +1,67 @@
 {
-    "data_mtime": 1680278525,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        4,
+        23,
+        30,
         1,
         2,
-        3,
-        5,
-        6,
-        7,
+        21,
+        22,
+        24,
+        25,
+        26,
+        27,
+        28,
+        33,
+        1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
         10,
         10,
         5,
         5,
         5,
         5,
         5,
+        5,
+        5,
+        5,
+        5,
+        30,
+        30,
         30,
         30
     ],
     "dependencies": [
         "collections.abc",
-        "io",
+        "os.path",
         "sys",
         "_typeshed",
-        "types",
+        "abc",
+        "builtins",
+        "contextlib",
+        "io",
+        "subprocess",
         "typing",
         "typing_extensions",
-        "builtins",
-        "abc",
-        "os"
+        "types",
+        "array",
+        "ctypes",
+        "mmap",
+        "pickle"
     ],
-    "hash": "f4ec890533fa3c342a29c868f57b9e039c99856c9ef6f4df798031b93671dcc1",
-    "id": "tempfile",
+    "hash": "4a8324189926c5351fe71b5411d9eda688b9c3854e620ff2045b6970266eb079",
+    "id": "os",
     "ignore_all": true,
-    "interface_hash": "e60018bfec73976dfa94fdaa45dd3f0407e721fa2b20e0c4672a91639e41f8b4",
+    "interface_hash": "715501750e4bbbb755525e210fb27f5068a6ad84428afe83ad84d69c1016e713",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -78,13 +96,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/tempfile.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/os/__init__.pyi",
     "plugin_data": null,
-    "size": 16433,
+    "size": 36855,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/test_consensus.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/test_consensus.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/test_consensus.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/test_consensus.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/textwrap.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/textwrap.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/textwrap.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/textwrap.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/threading.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/threading.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/threading.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/threading.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/time.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/time.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/time.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unicodedata.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8%*

 * *Differences: {"'data_mtime'": '1680278525',*

 * * "'hash'": "'bc77a39d577e1923eaf5c5d56ce79bc39d415d8d5c70e4b59bca27c77b1bcdd0'",*

 * * "'id'": "'unicodedata'",*

 * * "'interface_hash'": "'3ab8f14c4520703d17ccd6c15d7b2ecfea931c6d4b77edc66ede3705e86a2886'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unicodedata.pyi'",*

 * * "'size'": '2511'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680161756,
+    "data_mtime": 1680278525,
     "dep_lines": [
         1,
         2,
         3,
         4,
         1,
         1
@@ -20,18 +20,18 @@
         "sys",
         "_typeshed",
         "typing",
         "typing_extensions",
         "builtins",
         "abc"
     ],
-    "hash": "81ee1e52c98cc1cd26d7a6aa6d5a9c23d100b4e14cdd725b405a720187e41f8c",
-    "id": "time",
+    "hash": "bc77a39d577e1923eaf5c5d56ce79bc39d415d8d5c70e4b59bca27c77b1bcdd0",
+    "id": "unicodedata",
     "ignore_all": true,
-    "interface_hash": "b8990f6368b6d084c40909e654516f4ea726a64dd2f94f85baef1ee135868287",
+    "interface_hash": "3ab8f14c4520703d17ccd6c15d7b2ecfea931c6d4b77edc66ede3705e86a2886",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -66,13 +66,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/time.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unicodedata.pyi",
     "plugin_data": null,
-    "size": 3663,
+    "size": 2511,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/token.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/token.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/token.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/token.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tokenize.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tokenize.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tokenize.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tokenize.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/traceback.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/traceback.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/traceback.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/traceback.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tracemalloc.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tracemalloc.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tracemalloc.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tracemalloc.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/types.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/types.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/types.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/types.meta.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         3,
         16,
         1,
         2,
         19,
         20,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/typing.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/typing.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/typing.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/typing.meta.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
         2,
         3,
         4,
         5,
         6,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/typing_extensions.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/typing_extensions.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/typing_extensions.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/typing_extensions.meta.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         7,
         1,
         2,
         3,
         4,
         5,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unicodedata.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unicodedata.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unicodedata.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/stash.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7833333333333333%*

 * *Differences: {"'dep_lines'": '{delete: [3, 2, 1]}',*

 * * "'dep_prios'": '{delete: [2, 1, 0]}',*

 * * "'dependencies'": '{delete: [3, 1, 0]}',*

 * * "'hash'": "'c7fcb001e4df5fce2d234bd4c9798a9820f1c1c5c8113aa70ab56439402da90f'",*

 * * "'id'": "'_pytest.stash'",*

 * * "'interface_hash'": "'bfeb62f2ff5b4b2cf529368435b38cc6bd211801bfbac4517d07a5e80bb6b025'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/_pytest/stash.py'",*

 * * "'size'": '3055'}*

```diff
@@ -1,37 +1,28 @@
 {
     "data_mtime": 1680278525,
     "dep_lines": [
         1,
-        2,
-        3,
-        4,
         1,
         1
     ],
     "dep_prios": [
-        10,
-        5,
-        5,
         5,
         5,
         30
     ],
     "dependencies": [
-        "sys",
-        "_typeshed",
         "typing",
-        "typing_extensions",
         "builtins",
         "abc"
     ],
-    "hash": "bc77a39d577e1923eaf5c5d56ce79bc39d415d8d5c70e4b59bca27c77b1bcdd0",
-    "id": "unicodedata",
+    "hash": "c7fcb001e4df5fce2d234bd4c9798a9820f1c1c5c8113aa70ab56439402da90f",
+    "id": "_pytest.stash",
     "ignore_all": true,
-    "interface_hash": "3ab8f14c4520703d17ccd6c15d7b2ecfea931c6d4b77edc66ede3705e86a2886",
+    "interface_hash": "bfeb62f2ff5b4b2cf529368435b38cc6bd211801bfbac4517d07a5e80bb6b025",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -66,13 +57,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unicodedata.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/_pytest/stash.py",
     "plugin_data": null,
-    "size": 2511,
+    "size": 3055,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/uuid.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/uuid.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/uuid.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/uuid.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/warnings.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/warnings.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/warnings.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/shared_memory.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7668518518518519%*

 * *Differences: {"'data_mtime'": '1680161756',*

 * * "'dep_lines'": '{insert: [(1, 1), (2, 3), (4, 7)], delete: [5, 4, 1, 0]}',*

 * * "'dep_prios'": '{delete: [2]}',*

 * * "'dependencies'": "{insert: [(4, 'types')], delete: [3, 2]}",*

 * * "'hash'": "'d6a72618e0f6acaa3a2f6730a43e468df406e957b6d7a5d042bba955e5dc2328'",*

 * * "'id'": "'multiprocessing.shared_memory'",*

 * * "'interface_hash'": "'82cc4bbbb75f569154f4099bbdc3ffdad4b4cd65dd1f0ca9f974f88d88aea800'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonp […]*

```diff
@@ -1,46 +1,43 @@
 {
-    "data_mtime": 1680278525,
+    "data_mtime": 1680161756,
     "dep_lines": [
-        3,
-        1,
         2,
+        1,
+        3,
         4,
-        5,
-        6,
+        7,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
         10,
         5,
         5,
         5,
         5,
-        5,
         30,
         30
     ],
     "dependencies": [
         "collections.abc",
         "sys",
-        "_warnings",
-        "types",
         "typing",
         "typing_extensions",
+        "types",
         "builtins",
         "_typeshed",
         "abc"
     ],
-    "hash": "9a991da6c7cb550f45efd87385ec22f61a45c69511ab3af2594b6d1ce0487343",
-    "id": "warnings",
+    "hash": "d6a72618e0f6acaa3a2f6730a43e468df406e957b6d7a5d042bba955e5dc2328",
+    "id": "multiprocessing.shared_memory",
     "ignore_all": true,
-    "interface_hash": "1c3a1b98599df08099646f61ef07ed3e591c08dff1813caa0b815a6fde82ba9a",
+    "interface_hash": "82cc4bbbb75f569154f4099bbdc3ffdad4b4cd65dd1f0ca9f974f88d88aea800",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -75,13 +72,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/warnings.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/multiprocessing/shared_memory.pyi",
     "plugin_data": null,
-    "size": 3682,
+    "size": 1354,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/weakref.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/weakref.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/weakref.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/weakref.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/function_extensions/length.data.json`

 * *Files 12% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8150755494505494%*

 * *Differences: {"'_fullname'": "'jsonpath.function_extensions.length'",*

 * * "'names'": "{'__annotations__': {'node': {'fullname': "*

 * *            "'jsonpath.function_extensions.length.__annotations__'}, delete: ['module_public']}, "*

 * *            "'__doc__': {'node': {'fullname': 'jsonpath.function_extensions.length.__doc__'}, "*

 * *            "delete: ['module_public']}, '__file__': {'node': {'fullname': "*

 * *            "'jsonpath.function_extensions.length.__file__'}, delete: ['module_public']}, "*

 * *            "'__name__': {'node':  […]*

```diff
@@ -1,46 +1,38 @@
 {
     ".class": "MypyFile",
-    "_fullname": "_pytest",
+    "_fullname": "jsonpath.function_extensions.length",
     "future_import_flags": [],
     "is_partial_stub_package": false,
     "is_stub": false,
     "names": {
         ".class": "SymbolTable",
-        "__all__": {
+        "Optional": {
             ".class": "SymbolTableNode",
+            "cross_ref": "typing.Optional",
             "kind": "Gdef",
-            "module_public": false,
-            "node": {
-                ".class": "Var",
-                "flags": [
-                    "is_inferred",
-                    "has_explicit_value"
-                ],
-                "fullname": "_pytest.__all__",
-                "name": "__all__",
-                "type": {
-                    ".class": "Instance",
-                    "args": [
-                        "builtins.str"
-                    ],
-                    "type_ref": "builtins.list"
-                }
-            }
+            "module_hidden": true,
+            "module_public": false
+        },
+        "Sized": {
+            ".class": "SymbolTableNode",
+            "cross_ref": "typing.Sized",
+            "kind": "Gdef",
+            "module_hidden": true,
+            "module_public": false
         },
         "__annotations__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
-            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "_pytest.__annotations__",
+                "fullname": "jsonpath.function_extensions.length.__annotations__",
                 "name": "__annotations__",
                 "type": {
                     ".class": "Instance",
                     "args": [
                         "builtins.str",
                         {
                             ".class": "AnyType",
@@ -52,93 +44,110 @@
                     "type_ref": "builtins.dict"
                 }
             }
         },
         "__doc__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
-            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "_pytest.__doc__",
+                "fullname": "jsonpath.function_extensions.length.__doc__",
                 "name": "__doc__",
                 "type": "builtins.str"
             }
         },
         "__file__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
-            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "_pytest.__file__",
+                "fullname": "jsonpath.function_extensions.length.__file__",
                 "name": "__file__",
                 "type": "builtins.str"
             }
         },
         "__name__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
-            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "_pytest.__name__",
+                "fullname": "jsonpath.function_extensions.length.__name__",
                 "name": "__name__",
                 "type": "builtins.str"
             }
         },
         "__package__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
-            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "_pytest.__package__",
+                "fullname": "jsonpath.function_extensions.length.__package__",
                 "name": "__package__",
                 "type": "builtins.str"
             }
         },
-        "__path__": {
+        "length": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
-            "module_public": false,
             "node": {
-                ".class": "Var",
-                "flags": [
-                    "is_ready"
+                ".class": "FuncDef",
+                "abstract_status": 0,
+                "arg_kinds": [
+                    0
                 ],
-                "fullname": "_pytest.__path__",
-                "name": "__path__",
+                "arg_names": [
+                    "obj"
+                ],
+                "dataclass_transform_spec": null,
+                "flags": [],
+                "fullname": "jsonpath.function_extensions.length.length",
+                "name": "length",
                 "type": {
-                    ".class": "Instance",
-                    "args": [
-                        "builtins.str"
+                    ".class": "CallableType",
+                    "arg_kinds": [
+                        0
                     ],
-                    "type_ref": "builtins.list"
+                    "arg_names": [
+                        "obj"
+                    ],
+                    "arg_types": [
+                        "typing.Sized"
+                    ],
+                    "bound_args": [],
+                    "def_extras": {
+                        "first_arg": null
+                    },
+                    "fallback": "builtins.function",
+                    "from_concatenate": false,
+                    "implicit": false,
+                    "is_ellipsis_args": false,
+                    "name": "length",
+                    "ret_type": {
+                        ".class": "UnionType",
+                        "items": [
+                            "builtins.int",
+                            {
+                                ".class": "NoneType"
+                            }
+                        ]
+                    },
+                    "type_guard": null,
+                    "unpack_kwargs": false,
+                    "variables": []
                 }
             }
-        },
-        "__version__": {
-            ".class": "SymbolTableNode",
-            "cross_ref": "_pytest._version.version",
-            "kind": "Gdef"
-        },
-        "version_tuple": {
-            ".class": "SymbolTableNode",
-            "cross_ref": "_pytest._version.version_tuple",
-            "kind": "Gdef"
         }
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/_pytest/__init__.py"
+    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/function_extensions/length.py"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_argcomplete.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_argcomplete.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_argcomplete.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_argcomplete.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_version.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_version.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_version.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_version.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/cacheprovider.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/cacheprovider.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/cacheprovider.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/cacheprovider.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/capture.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/capture.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/capture.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/capture.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/compat.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/compat.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/compat.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/compat.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/debugging.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/debugging.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/debugging.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/debugging.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/deprecated.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/deprecated.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/deprecated.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/deprecated.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/doctest.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/doctest.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/doctest.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/doctest.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/fixtures.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/fixtures.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/fixtures.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/fixtures.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/freeze_support.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/freeze_support.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/freeze_support.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/freeze_support.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/helpconfig.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/helpconfig.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/helpconfig.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/helpconfig.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/hookspec.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/hookspec.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/hookspec.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/hookspec.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/legacypath.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/legacypath.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/legacypath.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/legacypath.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/logging.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/logging.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/logging.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/logging.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/main.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/main.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/main.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/main.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/monkeypatch.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/monkeypatch.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/monkeypatch.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/monkeypatch.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/nodes.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/nodes.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/nodes.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/nodes.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/outcomes.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/outcomes.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/outcomes.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/outcomes.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/pathlib.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/pathlib.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/pathlib.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/pathlib.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/pytester.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/pytester.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/pytester.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/pytester.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/pytester_assertions.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/pytester_assertions.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/pytester_assertions.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/pytester_assertions.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/python.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/python.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/python.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/python.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/python_api.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/python_api.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/python_api.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/python_api.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/recwarn.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/recwarn.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/recwarn.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/recwarn.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/reports.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/reports.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/reports.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/reports.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/runner.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/runner.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/runner.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/runner.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/scope.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/scope.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/scope.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/scope.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/stash.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/stash.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/stash.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/_version_info.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8%*

 * *Differences: {"'dep_prios'": '{insert: [(1, 30)], delete: [0]}',*

 * * "'dependencies'": "{insert: [(2, 'typing')], delete: [0]}",*

 * * "'hash'": "'c7f3372f75ae07baff50b5c05a3c7de7db9d290e072c1f25fa1b1cd450c636f9'",*

 * * "'id'": "'attr._version_info'",*

 * * "'interface_hash'": "'28c39c5fa5238ecab4e5aceaaa1112a34d215442abad3f0cb19c2f3a7329feb6'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/attr/_version_info.pyi'",*

 * * "'size'": '209'}*

```diff
@@ -3,26 +3,26 @@
     "dep_lines": [
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
-        5,
+        30,
         30
     ],
     "dependencies": [
-        "typing",
         "builtins",
-        "abc"
+        "abc",
+        "typing"
     ],
-    "hash": "c7fcb001e4df5fce2d234bd4c9798a9820f1c1c5c8113aa70ab56439402da90f",
-    "id": "_pytest.stash",
+    "hash": "c7f3372f75ae07baff50b5c05a3c7de7db9d290e072c1f25fa1b1cd450c636f9",
+    "id": "attr._version_info",
     "ignore_all": true,
-    "interface_hash": "bfeb62f2ff5b4b2cf529368435b38cc6bd211801bfbac4517d07a5e80bb6b025",
+    "interface_hash": "28c39c5fa5238ecab4e5aceaaa1112a34d215442abad3f0cb19c2f3a7329feb6",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -57,13 +57,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/_pytest/stash.py",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/attr/_version_info.pyi",
     "plugin_data": null,
-    "size": 3055,
+    "size": 209,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/terminal.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/terminal.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/terminal.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/terminal.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/timing.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/timing.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/timing.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/timing.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/tmpdir.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/tmpdir.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/tmpdir.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/tmpdir.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/warning_types.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/warning_types.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/warning_types.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/warning_types.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/warnings.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/warnings.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/warnings.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/warnings.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_code/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_code/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_code/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_code/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_code/code.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_code/code.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_code/code.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_code/code.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_code/source.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_code/source.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_code/source.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_code/source.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/saferepr.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/saferepr.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/saferepr.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/saferepr.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/terminalwriter.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/terminalwriter.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/terminalwriter.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/terminalwriter.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/wcwidth.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/_io/wcwidth.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/_io/wcwidth.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/setters.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7761904761904762%*

 * *Differences: {"'dep_lines'": '{insert: [(1, 3)], delete: [1, 0]}',*

 * * "'dep_prios'": '{insert: [(2, 5)], delete: [3, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'typing'), (1, 'attr')], delete: [4, 1, 0]}",*

 * * "'hash'": "'a7263c4d5341bbc4d684e95dbff4711f3986bdd805407f7cd5d6fbd2bd1f9f92'",*

 * * "'id'": "'attr.setters'",*

 * * "'interface_hash'": "'abcc0572c00dcf31326035ad7a16c860b9f74c1f04ca1d9a9ea7978d324dc031'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages […]*

```diff
@@ -1,34 +1,31 @@
 {
     "data_mtime": 1680278525,
     "dep_lines": [
         1,
-        2,
-        1,
+        3,
         1,
         1
     ],
     "dep_prios": [
-        10,
         5,
         5,
-        30,
+        5,
         30
     ],
     "dependencies": [
-        "unicodedata",
-        "functools",
+        "typing",
+        "attr",
         "builtins",
-        "abc",
-        "typing"
+        "abc"
     ],
-    "hash": "6211374e8faf048eee74bb55e01fa0fb4e12de5f15a110f9922f77e508a99890",
-    "id": "_pytest._io.wcwidth",
+    "hash": "a7263c4d5341bbc4d684e95dbff4711f3986bdd805407f7cd5d6fbd2bd1f9f92",
+    "id": "attr.setters",
     "ignore_all": true,
-    "interface_hash": "ff785b55f64db0077c07b259a0e7bd5a4b46efddfeb79e1eaebcc7226e39c7c5",
+    "interface_hash": "abcc0572c00dcf31326035ad7a16c860b9f74c1f04ca1d9a9ea7978d324dc031",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -63,13 +60,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/_pytest/_io/wcwidth.py",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/attr/setters.pyi",
     "plugin_data": null,
-    "size": 1253,
+    "size": 567,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/rewrite.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/rewrite.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/rewrite.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/rewrite.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/truncate.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/truncate.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/truncate.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/truncate.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/util.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/util.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/assertion/util.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/assertion/util.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/argparsing.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/argparsing.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/argparsing.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/argparsing.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/compat.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/compat.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/compat.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/compat.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/exceptions.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/exceptions.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/exceptions.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/exceptions.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/findpaths.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/findpaths.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/config/findpaths.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/config/findpaths.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/mark/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/mark/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/mark/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/mark/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/mark/expression.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/mark/expression.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/mark/expression.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/mark/expression.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/mark/structures.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/mark/structures.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_pytest/mark/structures.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_pytest/mark/structures.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_typeshed/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_typeshed/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/_typeshed/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_typeshed/__init__.meta.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         10,
         5,
         6,
         7,
         8,
         9,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/base_events.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/base_events.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/base_events.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/base_events.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/coroutines.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/coroutines.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/coroutines.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/coroutines.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/events.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/events.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/events.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/events.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/exceptions.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/exceptions.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/exceptions.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/exceptions.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/futures.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/futures.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/futures.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/tasks.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7874074074074074%*

 * *Differences: {"'dep_lines'": '{insert: [(0, 1), (2, 8), (3, 9), (5, 2), (8, 6)], delete: [8, 7, 6, 2, 1]}',*

 * * "'dep_prios'": '{insert: [(0, 10), (4, 20)], delete: [9, 4]}',*

 * * "'dependencies'": "{insert: [(0, 'concurrent.futures'), (3, 'asyncio.futures'), (4, "*

 * *                   "'concurrent'), (6, 'types'), (12, 'concurrent.futures._base')], delete: [12, "*

 * *                   '11, 7, 6, 0]}',*

 * * "'hash'": "'91fc1fd72cd5409f8f0fe0b3078ca980324fd6a6353c1844a7a5a15446cddd96'",*

 * * "'id'": "'asyncio.tasks'",*

 * * "'interface_hash'": " […]*

```diff
@@ -1,58 +1,58 @@
 {
     "data_mtime": 1680161757,
     "dep_lines": [
+        1,
         3,
-        2,
-        7,
+        8,
+        9,
         1,
+        2,
         4,
         5,
-        14,
-        17,
-        1,
+        6,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
+        10,
         5,
         5,
         5,
+        20,
         10,
         5,
         5,
         5,
         5,
-        5,
-        30,
         30,
         30,
         30
     ],
     "dependencies": [
-        "concurrent.futures._base",
+        "concurrent.futures",
         "collections.abc",
         "asyncio.events",
+        "asyncio.futures",
+        "concurrent",
         "sys",
+        "types",
         "typing",
         "typing_extensions",
-        "contextvars",
-        "types",
         "builtins",
         "_typeshed",
         "abc",
-        "concurrent",
-        "concurrent.futures"
+        "concurrent.futures._base"
     ],
-    "hash": "05b7db98d28d7040cb68bed2bfac7f655fd484552261e885a9c9fd1888e66b18",
-    "id": "asyncio.futures",
+    "hash": "91fc1fd72cd5409f8f0fe0b3078ca980324fd6a6353c1844a7a5a15446cddd96",
+    "id": "asyncio.tasks",
     "ignore_all": true,
-    "interface_hash": "f0eac0683b34751b1ba0339dceabd893acdb88735989af8e6f1bdb8fd71ef64e",
+    "interface_hash": "0893d5fa3bf9c3338ff4b692cea504d62b37e808a48bc0aff3d9bb51f4e8853c",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -87,13 +87,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/asyncio/futures.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/asyncio/tasks.pyi",
     "plugin_data": null,
-    "size": 2644,
+    "size": 13517,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/locks.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/locks.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/locks.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/locks.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/protocols.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/protocols.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/protocols.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/protocols.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/queues.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/queues.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/queues.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/queues.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/runners.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/runners.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/runners.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/runners.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/selector_events.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/selector_events.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/selector_events.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/selector_events.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/streams.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/streams.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/streams.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/streams.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/subprocess.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/subprocess.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/subprocess.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/subprocess.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/tasks.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/tasks.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/tasks.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/sre_parse.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7501587301587302%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 2), (5, 7)], delete: [9, 7, 5, 4, 3, 2]}',*

 * * "'dep_prios'": '{insert: [(6, 5)], delete: [10, 4, 2, 1, 0]}',*

 * * "'dependencies'": "{insert: [(2, 're'), (3, 'sre_constants')], delete: [12, 6, 4, 3, 2, 0]}",*

 * * "'hash'": "'38b6a819e544b584ec71b7040293fae6a77f2447fc14e9bc70e752ec237c8022'",*

 * * "'id'": "'sre_parse'",*

 * * "'interface_hash'": "'2b13eb3b1350bf942354e90a97500dd0a3fe206b98e910edcb745cb1aadcff2a'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virt […]*

```diff
@@ -1,58 +1,46 @@
 {
-    "data_mtime": 1680161757,
+    "data_mtime": 1680779143,
     "dep_lines": [
+        2,
         1,
         3,
-        8,
-        9,
-        1,
-        2,
         4,
-        5,
         6,
-        1,
+        7,
         1,
         1,
         1
     ],
     "dep_prios": [
-        10,
-        5,
-        5,
         5,
-        20,
         10,
         5,
         5,
         5,
         5,
-        30,
+        5,
         30,
         30
     ],
     "dependencies": [
-        "concurrent.futures",
         "collections.abc",
-        "asyncio.events",
-        "asyncio.futures",
-        "concurrent",
         "sys",
-        "types",
+        "re",
+        "sre_constants",
         "typing",
         "typing_extensions",
         "builtins",
         "_typeshed",
-        "abc",
-        "concurrent.futures._base"
+        "abc"
     ],
-    "hash": "91fc1fd72cd5409f8f0fe0b3078ca980324fd6a6353c1844a7a5a15446cddd96",
-    "id": "asyncio.tasks",
+    "hash": "38b6a819e544b584ec71b7040293fae6a77f2447fc14e9bc70e752ec237c8022",
+    "id": "sre_parse",
     "ignore_all": true,
-    "interface_hash": "0893d5fa3bf9c3338ff4b692cea504d62b37e808a48bc0aff3d9bb51f4e8853c",
+    "interface_hash": "2b13eb3b1350bf942354e90a97500dd0a3fe206b98e910edcb745cb1aadcff2a",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -87,13 +75,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/asyncio/tasks.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/sre_parse.pyi",
     "plugin_data": null,
-    "size": 13517,
+    "size": 4069,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/threads.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/threads.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/threads.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/threads.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/transports.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/transports.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/transports.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/transports.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/unix_events.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/unix_events.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/asyncio/unix_events.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/asyncio/unix_events.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/_cmp.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/_cmp.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/_cmp.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/_cmp.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/_typing_compat.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/_typing_compat.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/_typing_compat.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/_typing_compat.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/_version_info.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/_version_info.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/_version_info.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/email/contentmanager.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7422222222222222%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(1, 2), (2, 3)]}',*

 * * "'dep_prios'": '{insert: [(1, 5), (2, 5), (3, 5)], delete: [1]}',*

 * * "'dependencies'": "{insert: [(0, 'collections.abc'), (1, 'email.message'), (2, 'typing')], "*

 * *                   'delete: [2]}',*

 * * "'hash'": "'53099e51c46e4530831d75440f30c0481378944b551b503d0689cd68c9afd1bf'",*

 * * "'id'": "'email.contentmanager'",*

 * * "'interface_hash'": "'f0645ac1401529463f61b7a1a1053907d0979d410fcf765c307c7a030d84f852'",*

 * * "'path'": "'/home/james/.local/ […]*

```diff
@@ -1,28 +1,34 @@
 {
-    "data_mtime": 1680278525,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
+        2,
+        3,
         1,
         1
     ],
     "dep_prios": [
         5,
-        30,
+        5,
+        5,
+        5,
         30
     ],
     "dependencies": [
+        "collections.abc",
+        "email.message",
+        "typing",
         "builtins",
-        "abc",
-        "typing"
+        "abc"
     ],
-    "hash": "c7f3372f75ae07baff50b5c05a3c7de7db9d290e072c1f25fa1b1cd450c636f9",
-    "id": "attr._version_info",
+    "hash": "53099e51c46e4530831d75440f30c0481378944b551b503d0689cd68c9afd1bf",
+    "id": "email.contentmanager",
     "ignore_all": true,
-    "interface_hash": "28c39c5fa5238ecab4e5aceaaa1112a34d215442abad3f0cb19c2f3a7329feb6",
+    "interface_hash": "f0645ac1401529463f61b7a1a1053907d0979d410fcf765c307c7a030d84f852",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -57,13 +63,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/attr/_version_info.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/email/contentmanager.pyi",
     "plugin_data": null,
-    "size": 209,
+    "size": 480,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/converters.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/converters.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/converters.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/converters.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/exceptions.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/exceptions.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/exceptions.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/exceptions.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/filters.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/filters.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/filters.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/filters.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/setters.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/setters.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/setters.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/spawn.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.77%*

 * *Differences: {"'data_mtime'": '1680161756',*

 * * "'dep_lines'": '{insert: [(1, 2)]}',*

 * * "'dep_prios'": '{insert: [(0, 5)]}',*

 * * "'dependencies'": "{insert: [(0, 'collections.abc'), (1, 'types')], delete: [1]}",*

 * * "'hash'": "'ab21af9d8e81cb2d2d1f03eccfcea5175c0000bd3607fbdbeb0bbae2f0ac80d9'",*

 * * "'id'": "'multiprocessing.spawn'",*

 * * "'interface_hash'": "'bafc1befe0857d0963d69a21ddd92d6c2f2d6489eeecc7b525696cdc47c8a27b'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/s […]*

```diff
@@ -1,31 +1,34 @@
 {
-    "data_mtime": 1680278525,
+    "data_mtime": 1680161756,
     "dep_lines": [
         1,
+        2,
         3,
         1,
         1
     ],
     "dep_prios": [
         5,
         5,
         5,
+        5,
         30
     ],
     "dependencies": [
+        "collections.abc",
+        "types",
         "typing",
-        "attr",
         "builtins",
         "abc"
     ],
-    "hash": "a7263c4d5341bbc4d684e95dbff4711f3986bdd805407f7cd5d6fbd2bd1f9f92",
-    "id": "attr.setters",
+    "hash": "ab21af9d8e81cb2d2d1f03eccfcea5175c0000bd3607fbdbeb0bbae2f0ac80d9",
+    "id": "multiprocessing.spawn",
     "ignore_all": true,
-    "interface_hash": "abcc0572c00dcf31326035ad7a16c860b9f74c1f04ca1d9a9ea7978d324dc031",
+    "interface_hash": "bafc1befe0857d0963d69a21ddd92d6c2f2d6489eeecc7b525696cdc47c8a27b",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -60,13 +63,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/attr/setters.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/multiprocessing/spawn.pyi",
     "plugin_data": null,
-    "size": 567,
+    "size": 861,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/validators.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/validators.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/attr/validators.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/attr/validators.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/collections/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/collections/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/collections/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/collections/__init__.meta.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         11,
         1,
         2,
         3,
         4,
         5,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/collections/abc.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/collections/abc.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/collections/abc.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/collections/abc.meta.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/_base.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/_base.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/_base.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/util.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7839285714285714%*

 * *Differences: {"'dep_lines'": '{insert: [(0, 3), (3, 4), (6, 1), (7, 1), (8, 1), (9, 1)], delete: [7, 6, 3, 0]}',*

 * * "'dep_prios'": '{insert: [(7, 30), (8, 30), (9, 30), (10, 30)], delete: [3, 1]}',*

 * * "'dependencies'": "{insert: [(8, 'array'), (9, 'ctypes'), (10, 'mmap'), (11, 'pickle')], delete: "*

 * *                   '[5, 1]}',*

 * * "'hash'": "'950310d7e05e3d9bcc405ce475cec4ed8bf788b7148b6ae9d96eea92ebce861b'",*

 * * "'id'": "'multiprocessing.util'",*

 * * "'interface_hash'": "'60c7732061b098c9be0068c7282d4f4c4c0bc379fc09d2306e209ba61a00 […]*

```diff
@@ -1,49 +1,55 @@
 {
     "data_mtime": 1680161756,
     "dep_lines": [
-        4,
+        3,
         1,
         2,
-        3,
+        4,
         5,
         6,
-        7,
-        8,
+        1,
+        1,
+        1,
+        1,
         1,
         1
     ],
     "dep_prios": [
         5,
         10,
-        10,
-        5,
         5,
         5,
         5,
         5,
         5,
+        30,
+        30,
+        30,
+        30,
         30
     ],
     "dependencies": [
         "collections.abc",
-        "sys",
         "threading",
         "_typeshed",
         "logging",
-        "types",
         "typing",
         "typing_extensions",
         "builtins",
-        "abc"
+        "abc",
+        "array",
+        "ctypes",
+        "mmap",
+        "pickle"
     ],
-    "hash": "3f849a90b4bfad984ace2908d3926de071c8c9f62fc0af5bdbcb6e94fec4b77e",
-    "id": "concurrent.futures._base",
+    "hash": "950310d7e05e3d9bcc405ce475cec4ed8bf788b7148b6ae9d96eea92ebce861b",
+    "id": "multiprocessing.util",
     "ignore_all": true,
-    "interface_hash": "bc94ee07786973308a53770091026d58c533a1904272196e7635fd416a4cfcdc",
+    "interface_hash": "60c7732061b098c9be0068c7282d4f4c4c0bc379fc09d2306e209ba61a00cb63",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -78,13 +84,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/concurrent/futures/_base.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/multiprocessing/util.pyi",
     "plugin_data": null,
-    "size": 4187,
+    "size": 2429,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/process.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/process.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/process.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/process.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/thread.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/thread.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/concurrent/futures/thread.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/concurrent/futures/thread.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/ctypes/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/ctypes/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/ctypes/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/ctypes/__init__.meta.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         5,
         1,
         2,
         3,
         4,
         6,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/email/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/email/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/email/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/email/__init__.meta.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
         2,
         3,
         4,
         5,
         1,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/email/charset.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/email/charset.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/email/charset.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/function_extensions/length.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7177777777777777%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 2), (1, 3)], delete: [1, 0]}',*

 * * "'dep_prios'": '{insert: [(2, 5)], delete: [2]}',*

 * * "'dependencies'": "{insert: [(1, 'typing')], delete: [3]}",*

 * * "'hash'": "'41dc242cb3536e034a588c7533cba60079dce6fc9cf5c8ccfef38373a8570cad'",*

 * * "'id'": "'jsonpath.function_extensions.length'",*

 * * "'interface_hash'": "'be352a810d23fe869f7f183e0e293b3152075f1dfc27c3cb32f5b53ee0e3d404'",*

 * * "'mtime'": '1680776687',*

 * * "'path'": "'/home/james/projects/simply_json_path/simply-j […]*

```diff
@@ -1,32 +1,32 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        1,
-        1,
+        2,
+        3,
         1,
         1
     ],
     "dep_prios": [
         5,
         5,
-        30,
+        5,
         30
     ],
     "dependencies": [
         "collections.abc",
+        "typing",
         "builtins",
-        "abc",
-        "typing"
+        "abc"
     ],
-    "hash": "46b806f04d1179ba7b23c108135be7153f457b638c352804a5b1338d1e9347fa",
-    "id": "email.charset",
+    "hash": "41dc242cb3536e034a588c7533cba60079dce6fc9cf5c8ccfef38373a8570cad",
+    "id": "jsonpath.function_extensions.length",
     "ignore_all": true,
-    "interface_hash": "668ed651e7fb7b39fdc4f4003c79dbf09eb4f3802ef03607bd07f6142c8d9e19",
-    "mtime": 1679496944,
+    "interface_hash": "be352a810d23fe869f7f183e0e293b3152075f1dfc27c3cb32f5b53ee0e3d404",
+    "mtime": 1680776687,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -60,13 +60,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/email/charset.pyi",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/function_extensions/length.py",
     "plugin_data": null,
-    "size": 1077,
+    "size": 313,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/email/contentmanager.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/email/contentmanager.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/email/contentmanager.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_structures.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7357142857142857%*

 * *Differences: {"'data_mtime'": '1680278525',*

 * * "'dep_lines'": '{insert: [(1, 1)], delete: [2, 1]}',*

 * * "'dep_prios'": '{insert: [(1, 30), (2, 30)], delete: [2, 1, 0]}',*

 * * "'dependencies'": "{insert: [(2, 'types'), (3, 'typing')], delete: [2, 1, 0]}",*

 * * "'hash'": "'ab77953666d62461bf4b40e2b7f4b7028f2a42acffe4f6135c500a0597b9cabe'",*

 * * "'id'": "'packaging._structures'",*

 * * "'interface_hash'": "'52c23dd350071a797973de4f3a72c0e994ad922b78f25c17d0dc9f355e167b63'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath […]*

```diff
@@ -1,34 +1,31 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680278525,
     "dep_lines": [
         1,
-        2,
-        3,
+        1,
         1,
         1
     ],
     "dep_prios": [
         5,
-        5,
-        5,
-        5,
+        30,
+        30,
         30
     ],
     "dependencies": [
-        "collections.abc",
-        "email.message",
-        "typing",
         "builtins",
-        "abc"
+        "abc",
+        "types",
+        "typing"
     ],
-    "hash": "53099e51c46e4530831d75440f30c0481378944b551b503d0689cd68c9afd1bf",
-    "id": "email.contentmanager",
+    "hash": "ab77953666d62461bf4b40e2b7f4b7028f2a42acffe4f6135c500a0597b9cabe",
+    "id": "packaging._structures",
     "ignore_all": true,
-    "interface_hash": "f0645ac1401529463f61b7a1a1053907d0979d410fcf765c307c7a030d84f852",
+    "interface_hash": "52c23dd350071a797973de4f3a72c0e994ad922b78f25c17d0dc9f355e167b63",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -63,13 +60,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/email/contentmanager.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/packaging/_structures.py",
     "plugin_data": null,
-    "size": 480,
+    "size": 1431,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/email/errors.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/email/errors.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/email/errors.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/email/errors.meta.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
         1,
         1,
         1,
         1
     ],
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/email/header.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/email/header.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/email/header.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/email/header.meta.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
         2,
         3,
         1,
         1
     ],
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/email/message.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/email/message.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/email/message.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/metadata/__init__.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7377053745474798%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 31), (5, 2), (6, 3), (7, 4), (8, 8), (9, 10), (10, 11), (11, 12)], '*

 * *                'delete: [7, 5, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(4, 10), (6, 10), (11, 5), (12, 5)], delete: [9]}',*

 * * "'dependencies'": "{insert: [(0, 'importlib.metadata._meta'), (2, 'email.message'), (3, "*

 * *                   "'importlib.abc'), (4, 'abc'), (5, 'pathlib'), (6, 'sys'), (7, '_typeshed'), "*

 * *                   "(8, 'os'), (9, 're')], delete: [9, 5, 4, 3, 2, 1] […]*

```diff
@@ -1,49 +1,58 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        1,
-        3,
-        4,
+        31,
         5,
         6,
-        2,
         7,
-        8,
         1,
+        2,
+        3,
+        4,
+        8,
+        10,
+        11,
+        12,
         1
     ],
     "dep_prios": [
         5,
         5,
         5,
         5,
+        10,
+        5,
+        10,
         5,
         5,
         5,
         5,
         5,
-        30
+        5
     ],
     "dependencies": [
+        "importlib.metadata._meta",
         "collections.abc",
-        "email.charset",
-        "email.contentmanager",
-        "email.errors",
-        "email.policy",
-        "email",
+        "email.message",
+        "importlib.abc",
+        "abc",
+        "pathlib",
+        "sys",
+        "_typeshed",
+        "os",
+        "re",
         "typing",
         "typing_extensions",
-        "builtins",
-        "abc"
+        "builtins"
     ],
-    "hash": "6e0993b354bdf6bbe105b3598646b27a62851aead468c8a871eb4c4baef5ed2f",
-    "id": "email.message",
+    "hash": "ae422af81eff03dc03edf2ef5f854e32c69b6b23ebb6d7415e1165121041a540",
+    "id": "importlib.metadata",
     "ignore_all": true,
-    "interface_hash": "6f33c8af615df82d6630b720bcf459b7f138ed1bc6f7714c0e1421370ea76f01",
+    "interface_hash": "1ec76ef6c11a9698d377edfab22a6b9377866f6932f02429a856c7826ea732f7",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -78,13 +87,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/email/message.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/importlib/metadata/__init__.pyi",
     "plugin_data": null,
-    "size": 6091,
+    "size": 6736,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/email/policy.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/email/policy.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/email/policy.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/email/policy.meta.json`

 * *Files 3% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         2,
         3,
         4,
         5,
         6,
         1,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_catch.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_catch.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_catch.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_catch.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_exceptions.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_exceptions.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_exceptions.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_exceptions.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_formatting.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_formatting.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_formatting.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_formatting.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_version.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_version.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/exceptiongroup/_version.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/exceptiongroup/_version.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/__init__.meta.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
         2,
         3,
         1,
         1,
         1
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/abc.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/abc.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/abc.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/machinery.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7534204793028323%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 1), (1, 5), (2, 9), (6, 4), (7, 6), (8, 1)], delete: [8, 7, 6, 5, '*

 * *                '1, 0]}',*

 * * "'dep_prios'": '{insert: [(0, 10), (3, 20), (9, 30)], delete: [6, 5, 4]}',*

 * * "'dependencies'": "{insert: [(0, 'importlib.abc'), (2, 'importlib.metadata'), (3, 'importlib'), "*

 * *                   "(9, 'abc')], delete: [8, 6, 5, 1]}",*

 * * "'hash'": "'d8d65c367ab0b794c41c101e2200e4171d0d147dfa49385be91cdd958db6fc1d'",*

 * * "'id'": "'importlib.machinery'",*

 * * "'interf […]*

```diff
@@ -1,61 +1,61 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        12,
-        13,
+        1,
+        5,
+        9,
         1,
         2,
         3,
-        11,
-        14,
-        15,
-        16,
+        4,
+        6,
+        1,
         1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
+        10,
         5,
         5,
+        20,
         10,
         10,
         5,
         5,
         5,
-        5,
-        5,
-        5,
+        30,
         30,
         30,
         30,
         30
     ],
     "dependencies": [
+        "importlib.abc",
         "collections.abc",
-        "importlib.machinery",
+        "importlib.metadata",
+        "importlib",
         "sys",
         "types",
         "_typeshed",
-        "abc",
-        "io",
         "typing",
-        "typing_extensions",
         "builtins",
+        "abc",
         "array",
         "ctypes",
         "mmap",
         "pickle"
     ],
-    "hash": "ad8ba0ae1c679f2e613913ca173b46b1a8660c6c8175a482b1c24de042d5c2f4",
-    "id": "importlib.abc",
+    "hash": "d8d65c367ab0b794c41c101e2200e4171d0d147dfa49385be91cdd958db6fc1d",
+    "id": "importlib.machinery",
     "ignore_all": true,
-    "interface_hash": "d720407de67d430cd5edc64555205895bc074be2bc58ef43ce87c0770e0ca390",
+    "interface_hash": "4f5b3eb3a4592993f46fd111538d35e9805518fe9206c9354680a269b45a7699",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -90,13 +90,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/importlib/abc.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/importlib/machinery.pyi",
     "plugin_data": null,
-    "size": 7295,
+    "size": 5621,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/machinery.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/machinery.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/machinery.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_spawn_win32.meta.json`

 * *Files 9% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7337301587301588%*

 * *Differences: {"'data_mtime'": '1680161756',*

 * * "'dep_lines'": '{insert: [(0, 2)], delete: [11, 10, 9, 8, 7, 6, 4, 2, 0]}',*

 * * "'dep_prios'": '{delete: [12, 11, 10, 9, 6, 4, 3, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'multiprocessing.process'), (1, 'multiprocessing.util')], "*

 * *                   'delete: [13, 12, 11, 10, 6, 5, 3, 2, 1, 0]}',*

 * * "'hash'": "'b7ed144a1362114a9e29f2c412deed44cf1e1758916b175a14a3ff7344d70cd7'",*

 * * "'id'": "'multiprocessing.popen_spawn_win32'",*

 * * "'interface_hash'": "'88b436318f3b0d06c0afc25e9868bb7fb83 […]*

```diff
@@ -1,61 +1,37 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680161756,
     "dep_lines": [
-        1,
+        2,
         5,
-        9,
         1,
-        2,
         3,
-        4,
-        6,
-        1,
-        1,
-        1,
-        1,
         1,
         1
     ],
     "dep_prios": [
-        10,
         5,
         5,
-        20,
         10,
-        10,
-        5,
         5,
         5,
-        30,
-        30,
-        30,
-        30,
         30
     ],
     "dependencies": [
-        "importlib.abc",
-        "collections.abc",
-        "importlib.metadata",
-        "importlib",
+        "multiprocessing.process",
+        "multiprocessing.util",
         "sys",
-        "types",
-        "_typeshed",
         "typing",
         "builtins",
-        "abc",
-        "array",
-        "ctypes",
-        "mmap",
-        "pickle"
+        "abc"
     ],
-    "hash": "d8d65c367ab0b794c41c101e2200e4171d0d147dfa49385be91cdd958db6fc1d",
-    "id": "importlib.machinery",
+    "hash": "b7ed144a1362114a9e29f2c412deed44cf1e1758916b175a14a3ff7344d70cd7",
+    "id": "multiprocessing.popen_spawn_win32",
     "ignore_all": true,
-    "interface_hash": "4f5b3eb3a4592993f46fd111538d35e9805518fe9206c9354680a269b45a7699",
+    "interface_hash": "88b436318f3b0d06c0afc25e9868bb7fb833caf641a8e0796fac5495a90a1d49",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -90,13 +66,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/importlib/machinery.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/multiprocessing/popen_spawn_win32.pyi",
     "plugin_data": null,
-    "size": 5621,
+    "size": 738,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/util.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/util.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/util.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/util.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/metadata/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/metadata/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/metadata/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/iniconfig/exceptions.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7200000000000001%*

 * *Differences: {"'data_mtime'": '1680278525',*

 * * "'dep_lines'": '{insert: [(2, 5), (3, 1)], delete: [11, 10, 9, 8, 7, 6, 3, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(2, 25), (4, 30)], delete: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]}',*

 * * "'dependencies'": "{insert: [(0, '__future__'), (4, 'abc')], delete: [9, 8, 7, 6, 5, 4, 3, 2, 1, "*

 * *                   '0]}',*

 * * "'hash'": "'dd5d894b9ae7770898521f383cd612ff5cddf07f0807e45aafcd4044003b13db'",*

 * * "'id'": "'iniconfig.exceptions'",*

 * * "'interface_hash'": "'9ea02a85884126e85bb171ae84295af9f864ddb1 […]*

```diff
@@ -1,58 +1,34 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680278525,
     "dep_lines": [
-        31,
-        5,
-        6,
-        7,
         1,
         2,
-        3,
-        4,
-        8,
-        10,
-        11,
-        12,
+        5,
+        1,
         1
     ],
     "dep_prios": [
         5,
         5,
+        25,
         5,
-        5,
-        10,
-        5,
-        10,
-        5,
-        5,
-        5,
-        5,
-        5,
-        5
+        30
     ],
     "dependencies": [
-        "importlib.metadata._meta",
-        "collections.abc",
-        "email.message",
-        "importlib.abc",
-        "abc",
-        "pathlib",
-        "sys",
-        "_typeshed",
-        "os",
-        "re",
+        "__future__",
         "typing",
         "typing_extensions",
-        "builtins"
+        "builtins",
+        "abc"
     ],
-    "hash": "ae422af81eff03dc03edf2ef5f854e32c69b6b23ebb6d7415e1165121041a540",
-    "id": "importlib.metadata",
+    "hash": "dd5d894b9ae7770898521f383cd612ff5cddf07f0807e45aafcd4044003b13db",
+    "id": "iniconfig.exceptions",
     "ignore_all": true,
-    "interface_hash": "1ec76ef6c11a9698d377edfab22a6b9377866f6932f02429a856c7826ea732f7",
+    "interface_hash": "9ea02a85884126e85bb171ae84295af9f864ddb11b857b03d76358498c285760",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -87,13 +63,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/importlib/metadata/__init__.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/iniconfig/exceptions.py",
     "plugin_data": null,
-    "size": 6736,
+    "size": 501,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/metadata/_meta.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/metadata/_meta.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/importlib/metadata/_meta.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/metadata/_meta.meta.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
         2,
         1,
         1
     ],
     "dep_prios": [
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/iniconfig/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/iniconfig/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/iniconfig/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/iniconfig/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/iniconfig/_parse.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/iniconfig/_parse.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/iniconfig/_parse.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/iniconfig/_parse.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/iniconfig/exceptions.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/iniconfig/exceptions.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/iniconfig/exceptions.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/contextlib.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.73%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(2, 2), (3, 3), (4, 6), (5, 7), (6, 8)], delete: [1, 0]}',*

 * * "'dep_prios'": '{insert: [(2, 10), (4, 5), (5, 5), (6, 5), (7, 5)], delete: [4, 2]}',*

 * * "'dependencies'": "{insert: [(0, 'collections.abc'), (1, 'abc'), (2, 'sys'), (3, '_typeshed'), "*

 * *                   "(4, 'types')], delete: [4, 0]}",*

 * * "'hash'": "'e9251a3e7f59f7bd3f0883f9f7ffca34270a476e9b7afcf326492ad786b18f8a'",*

 * * "'id'": "'contextlib'",*

 * * "'interface_hash'": "'b2e20e8ed9d5e0c6062abf78cec3 […]*

```diff
@@ -1,34 +1,43 @@
 {
-    "data_mtime": 1680278525,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        1,
-        2,
         5,
         1,
+        2,
+        3,
+        6,
+        7,
+        8,
         1
     ],
     "dep_prios": [
         5,
         5,
-        25,
+        10,
+        5,
+        5,
+        5,
         5,
-        30
+        5
     ],
     "dependencies": [
-        "__future__",
+        "collections.abc",
+        "abc",
+        "sys",
+        "_typeshed",
+        "types",
         "typing",
         "typing_extensions",
-        "builtins",
-        "abc"
+        "builtins"
     ],
-    "hash": "dd5d894b9ae7770898521f383cd612ff5cddf07f0807e45aafcd4044003b13db",
-    "id": "iniconfig.exceptions",
+    "hash": "e9251a3e7f59f7bd3f0883f9f7ffca34270a476e9b7afcf326492ad786b18f8a",
+    "id": "contextlib",
     "ignore_all": true,
-    "interface_hash": "9ea02a85884126e85bb171ae84295af9f864ddb11b857b03d76358498c285760",
+    "interface_hash": "b2e20e8ed9d5e0c6062abf78cec3437ef856830dc1081f0183bf91e796c3041a",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -63,13 +72,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/iniconfig/exceptions.py",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/contextlib.pyi",
     "plugin_data": null,
-    "size": 501,
+    "size": 8764,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/json/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/json/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/json/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/json/__init__.meta.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         2,
         5,
         6,
         1,
         3,
         1,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/json/decoder.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/json/decoder.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/json/decoder.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/parser.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.74%*

 * *Differences: {"'data_mtime'": '1680012434',*

 * * "'dep_lines'": '{insert: [(0, 3)], delete: [1]}',*

 * * "'dependencies'": "{insert: [(0, 'yaml.error')], delete: [0]}",*

 * * "'hash'": "'84278dd07d81544ddf4cc836dc52802455df327cd4a68dc98f4ad2eb3c46c1e9'",*

 * * "'id'": "'yaml.parser'",*

 * * "'interface_hash'": "'9a2c1f1e122d45c02a095f316762080131022bede90cb48b0b2e8fdd58b90eb3'",*

 * * "'mtime'": '1680012426',*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/pars […]*

```diff
@@ -1,32 +1,32 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680012434,
     "dep_lines": [
+        3,
         1,
-        2,
         1,
         1
     ],
     "dep_prios": [
         5,
         5,
         5,
         30
     ],
     "dependencies": [
-        "collections.abc",
+        "yaml.error",
         "typing",
         "builtins",
         "abc"
     ],
-    "hash": "5dd5349e16128655996d25e9c4676c82eaed3374bf9740bd98360257d4df6a29",
-    "id": "json.decoder",
+    "hash": "84278dd07d81544ddf4cc836dc52802455df327cd4a68dc98f4ad2eb3c46c1e9",
+    "id": "yaml.parser",
     "ignore_all": true,
-    "interface_hash": "fac81736281b7d1750d3212e9e738c89432738e50c50b42dc19c75f0a5cd345a",
-    "mtime": 1679496944,
+    "interface_hash": "9a2c1f1e122d45c02a095f316762080131022bede90cb48b0b2e8fdd58b90eb3",
+    "mtime": 1680012426,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -60,13 +60,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/json/decoder.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/parser.pyi",
     "plugin_data": null,
-    "size": 1117,
+    "size": 1672,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/json/encoder.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/json/encoder.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/json/encoder.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/json/encoder.meta.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         1,
         2,
         3,
         1,
         1
     ],
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/__about__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/__about__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/__about__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/tokens.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7%*

 * *Differences: {"'data_mtime'": '1680012434',*

 * * "'dep_prios'": '{insert: [(1, 5)], delete: [1]}',*

 * * "'dependencies'": "{insert: [(0, 'typing')], delete: [2]}",*

 * * "'hash'": "'9595fb62da4dff11a0bdcac9955779c3c78d1e09616ed809b69d9cdd5036330b'",*

 * * "'id'": "'yaml.tokens'",*

 * * "'ignore_all'": 'True',*

 * * "'interface_hash'": "'13eebf5e863f594f7841c4d34ff4acbecf37765bf9b34d24a4dfea98c2e01de6'",*

 * * "'mtime'": '1680012426',*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-pac […]*

```diff
@@ -1,29 +1,29 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680012434,
     "dep_lines": [
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
-        30,
+        5,
         30
     ],
     "dependencies": [
+        "typing",
         "builtins",
-        "abc",
-        "typing"
+        "abc"
     ],
-    "hash": "70e558e4b942ca8c19568a6b224d099a248d17c82d006b286f0dfeb6539f1600",
-    "id": "jsonpath.__about__",
-    "ignore_all": false,
-    "interface_hash": "f90142b97cf2ff94d7ecbc2e11ad3d707003ae2a730b8811ff45471dbc44961c",
-    "mtime": 1680254737,
+    "hash": "9595fb62da4dff11a0bdcac9955779c3c78d1e09616ed809b69d9cdd5036330b",
+    "id": "yaml.tokens",
+    "ignore_all": true,
+    "interface_hash": "13eebf5e863f594f7841c4d34ff4acbecf37765bf9b34d24a4dfea98c2e01de6",
+    "mtime": 1680012426,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -57,13 +57,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/__about__.py",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/tokens.pyi",
     "plugin_data": null,
-    "size": 132,
+    "size": 1796,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/__init__.meta.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         5,
         6,
         10,
         11,
         12,
         13,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/cache.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/cache.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/cache.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/lru_cache.meta.json`

 * *Files 3% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8666666666666667%*

 * *Differences: {"'data_mtime'": '1679860357',*

 * * "'id'": "'jsonpath.lru_cache'",*

 * * "'interface_hash'": "'0284babfdd10fbf48ee6e7e0e866f1f9a19c9d83b4ecf96cc4b5cb809512105f'",*

 * * "'path'": "'/home/james/projects/simply_json_path/simply-json-path/jsonpath/lru_cache.py'"}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1679859772,
+    "data_mtime": 1679860357,
     "dep_lines": [
         36,
         38,
         39,
         41,
         1,
         1,
@@ -24,17 +24,17 @@
         "threading",
         "typing",
         "builtins",
         "_typeshed",
         "abc"
     ],
     "hash": "6ab0d821d4b0f6dc01be3f912198684641f3cb7366f42ddb23afae0a445fa999",
-    "id": "jsonpath.cache",
+    "id": "jsonpath.lru_cache",
     "ignore_all": false,
-    "interface_hash": "01b6cf90e67516f123ed7f1d42c84b851317dfd135ab814dd7fb3f17228a1d61",
+    "interface_hash": "0284babfdd10fbf48ee6e7e0e866f1f9a19c9d83b4ecf96cc4b5cb809512105f",
     "mtime": 1679859865,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -69,13 +69,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/cache.py",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/lru_cache.py",
     "plugin_data": null,
     "size": 5899,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/env.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/env.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/env.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/env.meta.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9333333333333333%*

 * *Differences: {"'data_mtime'": '1680779143', "'mtime'": '1680778568'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         6,
         22,
         23,
         26,
         27,
         28,
@@ -96,15 +96,15 @@
         "types",
         "typing_extensions"
     ],
     "hash": "ed19f8de311df414daf97a34cb1c0873357641a20a3872a42af6727e835d299c",
     "id": "jsonpath.env",
     "ignore_all": true,
     "interface_hash": "1a753dc1fec3ea1f787dbc7c69b2e28e2d8a7e000ac7a42395c5d9c010aa0a27",
-    "mtime": 1680586364,
+    "mtime": 1680778568,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/exceptions.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/exceptions.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/exceptions.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/exceptions.meta.json`

 * *Files 9% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         8,
         2,
         4,
         1,
         1,
         1
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/filter.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/filter.data.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.998447204968944%*

 * *Differences: {"'names'": "{'json': OrderedDict([('.class', 'SymbolTableNode'), ('cross_ref', 'json'), ('kind', "*

 * *            "'Gdef'), ('module_hidden', True), ('module_public', False)])}"}*

```diff
@@ -4892,14 +4892,21 @@
         "annotations": {
             ".class": "SymbolTableNode",
             "cross_ref": "__future__.annotations",
             "kind": "Gdef",
             "module_hidden": true,
             "module_public": false
         },
+        "json": {
+            ".class": "SymbolTableNode",
+            "cross_ref": "json",
+            "kind": "Gdef",
+            "module_hidden": true,
+            "module_public": false
+        },
         "re": {
             ".class": "SymbolTableNode",
             "cross_ref": "re",
             "kind": "Gdef",
             "module_hidden": true,
             "module_public": false
         }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/filter.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/parse.meta.json`

 * *Files 9% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7257381507381507%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 14), (2, 32), (3, 33), (4, 41), (5, 90), (6, 91), (10, 6)], delete: '*

 * *                '[6, 2, 1]}',*

 * * "'dep_prios'": '{insert: [(0, 5), (1, 5), (2, 5), (3, 5), (9, 10)], delete: [5]}',*

 * * "'dependencies'": "{insert: [(1, 'jsonpath.filter'), (4, 'jsonpath.token'), (5, 'jsonpath.env'), "*

 * *                   "(6, 'jsonpath.stream'), (8, 'codecs'), (12, '_codecs'), (13, '_typeshed'), "*

 * *                   "(14, 'abc'), (20, 'typing_extensions')], delete:  […]*

```diff
@@ -1,71 +1,83 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
+        14,
         15,
-        18,
-        19,
+        32,
+        33,
+        41,
+        90,
+        91,
         2,
         4,
         5,
-        7,
+        6,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
+        5,
+        5,
+        5,
+        5,
         25,
         25,
         5,
         10,
-        5,
+        10,
         5,
         5,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
         30
     ],
     "dependencies": [
         "jsonpath.exceptions",
+        "jsonpath.filter",
         "jsonpath.path",
         "jsonpath.selectors",
+        "jsonpath.token",
+        "jsonpath.env",
+        "jsonpath.stream",
         "__future__",
+        "codecs",
         "re",
-        "abc",
         "typing",
         "builtins",
-        "_collections_abc",
+        "_codecs",
+        "_typeshed",
+        "abc",
         "array",
         "ctypes",
         "enum",
-        "jsonpath.env",
-        "jsonpath.token",
         "mmap",
         "pickle",
-        "types"
+        "typing_extensions"
     ],
-    "hash": "4c6c430016a6d78d5965523cabe6947133ab36f2336ca991c46758866f936776",
-    "id": "jsonpath.filter",
+    "hash": "bf9579b774dc35a3c96aae5845b5877b5bc36066bc823211cc482645c7f37f3c",
+    "id": "jsonpath.parse",
     "ignore_all": true,
-    "interface_hash": "c2e362fb4e45363eb3e28d0b207b0bd5bf5203af2bc47380cb388bd25de42a56",
-    "mtime": 1680541092,
+    "interface_hash": "21415cba6e58aef1b669a29046643b333e4f893c94498c17baea3e0912dd9761",
+    "mtime": 1680542050,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -99,13 +111,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/filter.py",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/parse.py",
     "plugin_data": null,
-    "size": 11518,
+    "size": 17562,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/lex.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/lex.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/lex.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/token.meta.json`

 * *Files 9% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7058802308802309%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(1, 3)], delete: [6, 5, 4, 3, 1, 0]}',*

 * * "'dep_prios'": '{delete: [6, 4, 2, 1, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'sys'), (4, 'types'), (5, 'typing_extensions')], delete: [10, 9, "*

 * *                   '6, 4, 3, 2, 1, 0]}',*

 * * "'hash'": "'052d35382ceb88e1a7f39364c86a02f7787ff7a0509fe19779e78cda4fec0cf7'",*

 * * "'id'": "'jsonpath.token'",*

 * * "'interface_hash'": "'63a23fee5b4a852b5158d5036c671baaaba2926791863a4064b6bb9da1fb23a9'",*

 * * "'mtime'": '1680542514',*

 * *  […]*

```diff
@@ -1,53 +1,38 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        10,
-        11,
         2,
-        4,
-        5,
-        6,
-        69,
+        3,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
-        5,
-        5,
-        5,
         10,
         5,
         5,
-        25,
-        5,
         30,
         30,
         30
     ],
     "dependencies": [
-        "jsonpath.exceptions",
-        "jsonpath.token",
-        "__future__",
-        "re",
-        "functools",
+        "sys",
         "typing",
-        "jsonpath",
         "builtins",
         "abc",
-        "enum",
-        "jsonpath.env"
+        "types",
+        "typing_extensions"
     ],
-    "hash": "bf482a50ebd648e0d68afd7420fa3ff3462bd5af1ce9f123a408b36366314de8",
-    "id": "jsonpath.lex",
+    "hash": "052d35382ceb88e1a7f39364c86a02f7787ff7a0509fe19779e78cda4fec0cf7",
+    "id": "jsonpath.token",
     "ignore_all": true,
-    "interface_hash": "889c44ded3efbffa61b40d47da01e2a699b2e252e49fd68b8739597dfd7cd11c",
-    "mtime": 1680277988,
+    "interface_hash": "63a23fee5b4a852b5158d5036c671baaaba2926791863a4064b6bb9da1fb23a9",
+    "mtime": 1680542514,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -81,13 +66,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/lex.py",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/token.py",
     "plugin_data": null,
-    "size": 11085,
+    "size": 3650,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/lru_cache.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/lru_cache.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/lru_cache.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_match_api.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.6868131868131868%*

 * *Differences: {"'data_mtime'": '1680333435',*

 * * "'dep_lines'": '{insert: [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)], delete: [3, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(0, 10), (2, 30), (3, 30), (4, 30), (5, 30), (6, 30)], delete: [3, 2, '*

 * *                '1, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'jsonpath'), (3, 'array'), (4, 'ctypes'), (5, 'jsonpath.match'), "*

 * *                   "(6, 'mmap'), (7, 'pickle'), (8, 'typing')], delete: [5, 3, 2, 1, 0]}",*

 * * "'hash'": "'63f0be661877d811fe9f2fc9a156745353729d0f26def0f4fc1 […]*

```diff
@@ -1,41 +1,47 @@
 {
-    "data_mtime": 1679860357,
+    "data_mtime": 1680333435,
     "dep_lines": [
-        36,
-        38,
-        39,
-        41,
+        1,
+        1,
+        1,
+        1,
+        1,
+        1,
         1,
         1,
         1
     ],
     "dep_prios": [
+        10,
         5,
-        5,
-        5,
-        5,
-        5,
+        30,
+        30,
+        30,
+        30,
+        30,
         30,
         30
     ],
     "dependencies": [
-        "__future__",
-        "collections",
-        "threading",
-        "typing",
+        "jsonpath",
         "builtins",
-        "_typeshed",
-        "abc"
+        "abc",
+        "array",
+        "ctypes",
+        "jsonpath.match",
+        "mmap",
+        "pickle",
+        "typing"
     ],
-    "hash": "6ab0d821d4b0f6dc01be3f912198684641f3cb7366f42ddb23afae0a445fa999",
-    "id": "jsonpath.lru_cache",
+    "hash": "63f0be661877d811fe9f2fc9a156745353729d0f26def0f4fc1136ac09560e8b",
+    "id": "tests.test_match_api",
     "ignore_all": false,
-    "interface_hash": "0284babfdd10fbf48ee6e7e0e866f1f9a19c9d83b4ecf96cc4b5cb809512105f",
-    "mtime": 1679859865,
+    "interface_hash": "442dc8e7ac8a90829d986bbbd96c9e456b1fe107b50f993b675c1ab8e628314a",
+    "mtime": 1680333526,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -69,13 +75,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/lru_cache.py",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/test_match_api.py",
     "plugin_data": null,
-    "size": 5899,
+    "size": 1438,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/match.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/match.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/match.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/match.meta.json`

 * *Files 5% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         2,
         4,
         1,
         1,
         1,
         1,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/parse.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/parse.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/parse.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/specifiers.meta.json`

 * *Files 11% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7135198135198135%*

 * *Differences: {"'data_mtime'": '1680278526',*

 * * "'dep_lines'": '{insert: [(0, 26), (1, 27), (2, 11), (3, 12), (4, 13)], delete: [11, 10, 9, 8, 7, '*

 * *                '6, 5, 4, 3, 2, 1]}',*

 * * "'dep_prios'": '{insert: [(2, 10)], delete: [12, 6, 5, 3, 2, 1, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'packaging.utils'), (1, 'packaging.version'), (2, 'abc'), (3, "*

 * *                   "'itertools'), (13, 'types')], delete: [14, 12, 8, 7, 6, 5, 4, 3, 2, 1, 0]}",*

 * * "'hash'": "'fb76a36790a442b8cd5b91fc34f8ef095d91060afec3dc1c60175bf248cf05f […]*

```diff
@@ -1,83 +1,65 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680278526,
     "dep_lines": [
+        26,
+        27,
+        11,
+        12,
+        13,
         14,
-        15,
-        32,
-        33,
-        41,
-        90,
-        91,
-        2,
-        4,
-        5,
-        6,
-        1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
         5,
-        5,
-        5,
-        5,
-        25,
-        25,
-        5,
+        10,
         10,
         10,
         5,
         5,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
-        30,
         30
     ],
     "dependencies": [
-        "jsonpath.exceptions",
-        "jsonpath.filter",
-        "jsonpath.path",
-        "jsonpath.selectors",
-        "jsonpath.token",
-        "jsonpath.env",
-        "jsonpath.stream",
-        "__future__",
-        "codecs",
+        "packaging.utils",
+        "packaging.version",
+        "abc",
+        "itertools",
         "re",
         "typing",
         "builtins",
-        "_codecs",
         "_typeshed",
-        "abc",
         "array",
         "ctypes",
         "enum",
         "mmap",
         "pickle",
+        "types",
         "typing_extensions"
     ],
-    "hash": "bf9579b774dc35a3c96aae5845b5877b5bc36066bc823211cc482645c7f37f3c",
-    "id": "jsonpath.parse",
+    "hash": "fb76a36790a442b8cd5b91fc34f8ef095d91060afec3dc1c60175bf248cf05f8",
+    "id": "packaging.specifiers",
     "ignore_all": true,
-    "interface_hash": "21415cba6e58aef1b669a29046643b333e4f893c94498c17baea3e0912dd9761",
-    "mtime": 1680542050,
+    "interface_hash": "9c27f50be3017562798945282cd6bf8959bd4e36a80f3c88aa5092e599ac6917",
+    "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -111,13 +93,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/parse.py",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/packaging/specifiers.py",
     "plugin_data": null,
-    "size": 17562,
+    "size": 39046,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/path.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/path.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/path.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/pathlib.meta.json`

 * *Files 10% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7028787878787879%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 12), (2, 2), (3, 13), (4, 14), (5, 15), (6, 16), (7, 17)], delete: '*

 * *                '[7, 6, 5, 4, 3, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(4, 5), (5, 5), (6, 5), (7, 5), (8, 5)], delete: [9, 8, 4, 2, 1, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'collections.abc'), (1, 'sys'), (2, '_typeshed'), (3, 'io'), (4, "*

 * *                   "'os'), (5, 'types'), (7, 'typing_extensions')], delete: [14, 11, 5, 4, 3, 2, "*

 * *                   '1, 0]}',*

 * * "'hash'" […]*

```diff
@@ -1,65 +1,62 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        19,
-        23,
-        24,
-        2,
-        4,
-        5,
-        6,
-        1,
+        12,
         1,
+        2,
+        13,
+        14,
+        15,
+        16,
+        17,
         1,
         1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
-        25,
-        25,
-        5,
-        10,
         10,
         5,
         5,
-        30,
-        30,
+        5,
+        5,
+        5,
+        5,
+        5,
         30,
         30,
         30,
         30,
         30
     ],
     "dependencies": [
-        "jsonpath.match",
-        "jsonpath.env",
-        "jsonpath.selectors",
-        "__future__",
-        "itertools",
-        "json",
+        "collections.abc",
+        "sys",
+        "_typeshed",
+        "io",
+        "os",
+        "types",
         "typing",
+        "typing_extensions",
         "builtins",
         "abc",
         "array",
         "ctypes",
-        "json.decoder",
         "mmap",
-        "pickle",
-        "types"
+        "pickle"
     ],
-    "hash": "22e01eb8b693fb0b790b42fa58a2aac47d784b81b22cdf9fc204d3e4db98c622",
-    "id": "jsonpath.path",
+    "hash": "04a9e436986cd9b24089af97b33a4ce12d691429398e3de21b63d203baa68ccf",
+    "id": "pathlib",
     "ignore_all": true,
-    "interface_hash": "422380732d80a8e80c091999bcc774072fe06c46ffd0f1046b195a5c11bebddd",
-    "mtime": 1680586565,
+    "interface_hash": "8d6296e9f5172aca44955748a80ab51a6efdcda7f533f534c61e309b11e45c18",
+    "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -93,13 +90,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/path.py",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/pathlib.pyi",
     "plugin_data": null,
-    "size": 11286,
+    "size": 7941,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/selectors.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/selectors.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/selectors.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/pool.meta.json`

 * *Files 12% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.6939259914492112%*

 * *Differences: {"'data_mtime'": '1680161756',*

 * * "'dep_lines'": '{insert: [(2, 3), (3, 4), (4, 5)], delete: [11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(1, 10)], delete: [13, 12, 11, 5, 4, 3, 2, 1, 0]}',*

 * * "'dependencies'": "{insert: [(1, 'sys'), (2, 'types'), (4, 'typing_extensions'), (6, "*

 * *                   "'_typeshed'), (7, 'abc')], delete: [15, 14, 13, 12, 11, 8, 7, 6, 5, 4, 3, 2, "*

 * *                   '1]}',*

 * * "'hash'": "'7027d3444098f13592bd486741f2f2738c0042aa57dd167f0dcdb5fde988b530'",*

 * * "'id'":  […]*

```diff
@@ -1,68 +1,44 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680161756,
     "dep_lines": [
-        6,
-        18,
-        19,
-        22,
-        23,
-        24,
         2,
-        4,
-        8,
-        9,
-        1,
-        1,
         1,
+        3,
+        4,
+        5,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
+        10,
         5,
         5,
-        25,
-        25,
-        25,
-        5,
         5,
         5,
-        5,
-        5,
-        30,
-        30,
-        30,
         30,
         30
     ],
     "dependencies": [
         "collections.abc",
-        "jsonpath.exceptions",
-        "jsonpath.match",
-        "jsonpath.env",
-        "jsonpath.filter",
-        "jsonpath.token",
-        "__future__",
-        "abc",
-        "contextlib",
+        "sys",
+        "types",
         "typing",
+        "typing_extensions",
         "builtins",
-        "array",
-        "ctypes",
-        "mmap",
-        "pickle",
-        "types"
+        "_typeshed",
+        "abc"
     ],
-    "hash": "817b849795ba3d1f5194af26097a23a272327b2ce41ec41ac21c410d14827653",
-    "id": "jsonpath.selectors",
+    "hash": "7027d3444098f13592bd486741f2f2738c0042aa57dd167f0dcdb5fde988b530",
+    "id": "multiprocessing.pool",
     "ignore_all": true,
-    "interface_hash": "122b216d07667890df21168cd598eb98af118d6205187f7caa611793963b0579",
-    "mtime": 1680587317,
+    "interface_hash": "9dbd6d35a0de07cd1d49b93bc1c5c2eb587d1b9a13a7cc4c140da6144634210c",
+    "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -96,13 +72,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/selectors.py",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/multiprocessing/pool.pyi",
     "plugin_data": null,
-    "size": 20229,
+    "size": 4757,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/stream.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/stream.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/stream.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/stream.meta.json`

 * *Files 4% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         8,
         9,
         2,
         4,
         5,
         1,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/token.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/token.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/token.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_elffile.meta.json`

 * *Files 10% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7053613053613054%*

 * *Differences: {"'data_mtime'": '1680278525',*

 * * "'dep_lines'": '{insert: [(0, 11), (1, 12), (2, 13), (3, 14), (4, 1), (5, 1), (6, 1)], delete: '*

 * *                '[1, 0]}',*

 * * "'dep_prios'": '{insert: [(0, 10), (1, 10), (5, 30), (6, 30), (7, 30)]}',*

 * * "'dependencies'": "{insert: [(0, 'enum'), (1, 'os'), (2, 'struct'), (6, 'array'), (7, 'ctypes'), "*

 * *                   "(8, 'mmap'), (9, 'pickle')], delete: [4, 0]}",*

 * * "'hash'": "'85b98af0e0fa67b7d8ea1c229c7114703d5bcbb73390688d62eed28671449369'",*

 * * "'id'": "'packaging._elffile'",*

 * * […]*

```diff
@@ -1,38 +1,53 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680278525,
     "dep_lines": [
-        2,
-        3,
+        11,
+        12,
+        13,
+        14,
+        1,
+        1,
+        1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
         10,
+        10,
+        10,
         5,
         5,
         30,
         30,
+        30,
+        30,
+        30,
         30
     ],
     "dependencies": [
-        "sys",
+        "enum",
+        "os",
+        "struct",
         "typing",
         "builtins",
         "abc",
-        "types",
+        "array",
+        "ctypes",
+        "mmap",
+        "pickle",
         "typing_extensions"
     ],
-    "hash": "052d35382ceb88e1a7f39364c86a02f7787ff7a0509fe19779e78cda4fec0cf7",
-    "id": "jsonpath.token",
+    "hash": "85b98af0e0fa67b7d8ea1c229c7114703d5bcbb73390688d62eed28671449369",
+    "id": "packaging._elffile",
     "ignore_all": true,
-    "interface_hash": "63a23fee5b4a852b5158d5036c671baaaba2926791863a4064b6bb9da1fb23a9",
-    "mtime": 1680542514,
+    "interface_hash": "6813c991ccfb7e9f770910239ac61d8881862c897a99edb34da8e82761bc69d9",
+    "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -66,13 +81,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/token.py",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/packaging/_elffile.py",
     "plugin_data": null,
-    "size": 3650,
+    "size": 3266,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/function_extensions/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/function_extensions/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/function_extensions/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/function_extensions/__init__.meta.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         2,
         3,
         1,
         1,
         1
     ],
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/function_extensions/keys.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/function_extensions/keys.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/function_extensions/keys.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/function_extensions/keys.meta.json`

 * *Files 5% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9666666666666667%*

 * *Differences: {"'data_mtime'": '1680779143'}*

```diff
@@ -1,9 +1,9 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680779143,
     "dep_lines": [
         2,
         1,
         1
     ],
     "dep_prios": [
         5,
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/function_extensions/length.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/__init__.data.json`

 * *Files 16% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8111607142857142%*

 * *Differences: {"'_fullname'": "'tomli'",*

 * * "'names'": "{'__annotations__': {'node': {'fullname': 'tomli.__annotations__'}, 'module_public': "*

 * *            "False}, '__doc__': {'node': {'fullname': 'tomli.__doc__'}, 'module_public': False}, "*

 * *            "'__file__': {'node': {'fullname': 'tomli.__file__'}, 'module_public': False}, "*

 * *            "'__name__': {'node': {'fullname': 'tomli.__name__'}, 'module_public': False}, "*

 * *            "'__package__': {'node': {'fullname': 'tomli.__package__'}, 'module_public': False}, "*

 * *  […]*

```diff
@@ -1,38 +1,65 @@
 {
     ".class": "MypyFile",
-    "_fullname": "jsonpath.function_extensions.length",
+    "_fullname": "tomli",
     "future_import_flags": [],
     "is_partial_stub_package": false,
     "is_stub": false,
     "names": {
         ".class": "SymbolTable",
-        "Optional": {
+        "TOMLDecodeError": {
             ".class": "SymbolTableNode",
-            "cross_ref": "typing.Optional",
-            "kind": "Gdef",
-            "module_hidden": true,
-            "module_public": false
+            "cross_ref": "tomli._parser.TOMLDecodeError",
+            "kind": "Gdef"
         },
-        "Sized": {
+        "__all__": {
             ".class": "SymbolTableNode",
-            "cross_ref": "typing.Sized",
             "kind": "Gdef",
-            "module_hidden": true,
-            "module_public": false
+            "module_public": false,
+            "node": {
+                ".class": "Var",
+                "flags": [
+                    "is_inferred",
+                    "has_explicit_value"
+                ],
+                "fullname": "tomli.__all__",
+                "name": "__all__",
+                "type": {
+                    ".class": "TupleType",
+                    "implicit": false,
+                    "items": [
+                        "builtins.str",
+                        "builtins.str",
+                        "builtins.str"
+                    ],
+                    "partial_fallback": {
+                        ".class": "Instance",
+                        "args": [
+                            {
+                                ".class": "AnyType",
+                                "missing_import_name": null,
+                                "source_any": null,
+                                "type_of_any": 6
+                            }
+                        ],
+                        "type_ref": "builtins.tuple"
+                    }
+                }
+            }
         },
         "__annotations__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
+            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "jsonpath.function_extensions.length.__annotations__",
+                "fullname": "tomli.__annotations__",
                 "name": "__annotations__",
                 "type": {
                     ".class": "Instance",
                     "args": [
                         "builtins.str",
                         {
                             ".class": "AnyType",
@@ -44,110 +71,109 @@
                     "type_ref": "builtins.dict"
                 }
             }
         },
         "__doc__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
+            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "jsonpath.function_extensions.length.__doc__",
+                "fullname": "tomli.__doc__",
                 "name": "__doc__",
                 "type": "builtins.str"
             }
         },
         "__file__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
+            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "jsonpath.function_extensions.length.__file__",
+                "fullname": "tomli.__file__",
                 "name": "__file__",
                 "type": "builtins.str"
             }
         },
         "__name__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
+            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "jsonpath.function_extensions.length.__name__",
+                "fullname": "tomli.__name__",
                 "name": "__name__",
                 "type": "builtins.str"
             }
         },
         "__package__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
+            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "jsonpath.function_extensions.length.__package__",
+                "fullname": "tomli.__package__",
                 "name": "__package__",
                 "type": "builtins.str"
             }
         },
-        "length": {
+        "__path__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
+            "module_public": false,
             "node": {
-                ".class": "FuncDef",
-                "abstract_status": 0,
-                "arg_kinds": [
-                    0
-                ],
-                "arg_names": [
-                    "obj"
+                ".class": "Var",
+                "flags": [
+                    "is_ready"
                 ],
-                "dataclass_transform_spec": null,
-                "flags": [],
-                "fullname": "jsonpath.function_extensions.length.length",
-                "name": "length",
+                "fullname": "tomli.__path__",
+                "name": "__path__",
                 "type": {
-                    ".class": "CallableType",
-                    "arg_kinds": [
-                        0
-                    ],
-                    "arg_names": [
-                        "obj"
-                    ],
-                    "arg_types": [
-                        "typing.Sized"
+                    ".class": "Instance",
+                    "args": [
+                        "builtins.str"
                     ],
-                    "bound_args": [],
-                    "def_extras": {
-                        "first_arg": null
-                    },
-                    "fallback": "builtins.function",
-                    "from_concatenate": false,
-                    "implicit": false,
-                    "is_ellipsis_args": false,
-                    "name": "length",
-                    "ret_type": {
-                        ".class": "UnionType",
-                        "items": [
-                            "builtins.int",
-                            {
-                                ".class": "NoneType"
-                            }
-                        ]
-                    },
-                    "type_guard": null,
-                    "unpack_kwargs": false,
-                    "variables": []
+                    "type_ref": "builtins.list"
                 }
             }
+        },
+        "__version__": {
+            ".class": "SymbolTableNode",
+            "kind": "Gdef",
+            "module_public": false,
+            "node": {
+                ".class": "Var",
+                "flags": [
+                    "is_ready",
+                    "is_inferred",
+                    "has_explicit_value"
+                ],
+                "fullname": "tomli.__version__",
+                "name": "__version__",
+                "type": "builtins.str"
+            }
+        },
+        "load": {
+            ".class": "SymbolTableNode",
+            "cross_ref": "tomli._parser.load",
+            "kind": "Gdef"
+        },
+        "loads": {
+            ".class": "SymbolTableNode",
+            "cross_ref": "tomli._parser.loads",
+            "kind": "Gdef"
         }
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/function_extensions/length.py"
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/tomli/__init__.py"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/jsonpath/function_extensions/length.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/dev.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.6606481481481481%*

 * *Differences: {"'data_mtime'": '1680767114',*

 * * "'dep_lines'": '{insert: [(0, 1), (2, 1), (3, 1), (4, 1)], delete: [1]}',*

 * * "'dep_prios'": '{insert: [(0, 10), (1, 10), (3, 30), (4, 30), (5, 30)], delete: [1, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'json'), (1, 'jsonpath'), (3, '_typeshed'), (5, 'json.encoder'), "*

 * *                   "(6, 'typing')], delete: [1, 0]}",*

 * * "'hash'": "'73e60f61fa5f9ce0a3153b28131397219676112f1700ee81b3933911be92012d'",*

 * * "'id'": "'dev'",*

 * * "'ignore_all'": 'False',*

 * * "'interface_hash'": "'8911c034d10d […]*

```diff
@@ -1,32 +1,41 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680767114,
     "dep_lines": [
+        1,
         2,
-        3,
+        1,
+        1,
+        1,
         1,
         1
     ],
     "dep_prios": [
+        10,
+        10,
         5,
-        5,
-        5,
+        30,
+        30,
+        30,
         30
     ],
     "dependencies": [
-        "collections.abc",
-        "typing",
+        "json",
+        "jsonpath",
         "builtins",
-        "abc"
+        "_typeshed",
+        "abc",
+        "json.encoder",
+        "typing"
     ],
-    "hash": "41dc242cb3536e034a588c7533cba60079dce6fc9cf5c8ccfef38373a8570cad",
-    "id": "jsonpath.function_extensions.length",
-    "ignore_all": true,
-    "interface_hash": "be352a810d23fe869f7f183e0e293b3152075f1dfc27c3cb32f5b53ee0e3d404",
-    "mtime": 1680586204,
+    "hash": "73e60f61fa5f9ce0a3153b28131397219676112f1700ee81b3933911be92012d",
+    "id": "dev",
+    "ignore_all": false,
+    "interface_hash": "8911c034d10dcee214cc5bc53ce5b6ac4d078948b8ea3da996370dbc08282e1d",
+    "mtime": 1680779670,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -60,13 +69,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/function_extensions/length.py",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/dev.py",
     "plugin_data": null,
-    "size": 313,
+    "size": 1229,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/logging/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/logging/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/logging/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/logging/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/connection.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/connection.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/connection.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/connection.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/context.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/context.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/context.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/context.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/managers.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/managers.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/managers.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/managers.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/pool.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/pool.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/pool.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/process.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8083333333333333%*

 * *Differences: {"'dep_lines'": '{delete: [4, 3]}',*

 * * "'dep_prios'": '{delete: [3, 2]}',*

 * * "'dependencies'": '{delete: [4, 2]}',*

 * * "'hash'": "'e44ea317051af09f8dfcc8fc2bf556ed7231f27d7cbaffded663ea2926d1f307'",*

 * * "'id'": "'multiprocessing.process'",*

 * * "'interface_hash'": "'a3e5d411574881d24b308809966143c632c703d92a81fa8552441fee5ab0a905'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/multiprocessing/process.pyi'",*

 * * "'size'": '1 […]*

```diff
@@ -1,43 +1,37 @@
 {
     "data_mtime": 1680161756,
     "dep_lines": [
         2,
         1,
         3,
-        4,
-        5,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
         10,
         5,
         5,
-        5,
-        5,
         30,
         30
     ],
     "dependencies": [
         "collections.abc",
         "sys",
-        "types",
         "typing",
-        "typing_extensions",
         "builtins",
         "_typeshed",
         "abc"
     ],
-    "hash": "7027d3444098f13592bd486741f2f2738c0042aa57dd167f0dcdb5fde988b530",
-    "id": "multiprocessing.pool",
+    "hash": "e44ea317051af09f8dfcc8fc2bf556ed7231f27d7cbaffded663ea2926d1f307",
+    "id": "multiprocessing.process",
     "ignore_all": true,
-    "interface_hash": "9dbd6d35a0de07cd1d49b93bc1c5c2eb587d1b9a13a7cc4c140da6144634210c",
+    "interface_hash": "a3e5d411574881d24b308809966143c632c703d92a81fa8552441fee5ab0a905",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -72,13 +66,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/multiprocessing/pool.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/multiprocessing/process.pyi",
     "plugin_data": null,
-    "size": 4757,
+    "size": 1335,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_fork.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_fork.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_fork.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_fork.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_forkserver.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_forkserver.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_forkserver.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_forkserver.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_spawn_posix.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_spawn_posix.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_spawn_posix.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_spawn_posix.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_spawn_win32.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/popen_spawn_win32.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/popen_spawn_win32.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/os/path.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.744047619047619%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(1, 7), (2, 1)], delete: [3, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(3, 30)], delete: [1, 0]}',*

 * * "'dependencies'": "{insert: [(1, 'posixpath'), (4, 'typing')], delete: [3, 1, 0]}",*

 * * "'hash'": "'1bbead25bbe51b5fe4cc577c8270aa4b8321b7780fce50b58a1201ab3babc433'",*

 * * "'id'": "'os.path'",*

 * * "'interface_hash'": "'c642066bf2d20711b1934dcdfb641b1546d6d49a6a79f30ca2f4dd67284271f3'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/p […]*

```diff
@@ -1,37 +1,34 @@
 {
-    "data_mtime": 1680161756,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        2,
-        5,
         1,
-        3,
+        7,
+        1,
         1,
         1
     ],
     "dep_prios": [
-        5,
-        5,
         10,
         5,
         5,
+        30,
         30
     ],
     "dependencies": [
-        "multiprocessing.process",
-        "multiprocessing.util",
         "sys",
-        "typing",
+        "posixpath",
         "builtins",
-        "abc"
+        "abc",
+        "typing"
     ],
-    "hash": "b7ed144a1362114a9e29f2c412deed44cf1e1758916b175a14a3ff7344d70cd7",
-    "id": "multiprocessing.popen_spawn_win32",
+    "hash": "1bbead25bbe51b5fe4cc577c8270aa4b8321b7780fce50b58a1201ab3babc433",
+    "id": "os.path",
     "ignore_all": true,
-    "interface_hash": "88b436318f3b0d06c0afc25e9868bb7fb833caf641a8e0796fac5495a90a1d49",
+    "interface_hash": "c642066bf2d20711b1934dcdfb641b1546d6d49a6a79f30ca2f4dd67284271f3",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -66,13 +63,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/multiprocessing/popen_spawn_win32.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/os/path.pyi",
     "plugin_data": null,
-    "size": 738,
+    "size": 186,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/process.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/process.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/process.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/queues.meta.json`

 * *Files 10% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7958333333333333%*

 * *Differences: {"'dep_lines'": '{insert: [(1, 2), (3, 6)], delete: [0]}',*

 * * "'dep_prios'": '{insert: [(0, 10), (2, 5)], delete: [0]}',*

 * * "'dependencies'": "{insert: [(0, 'queue'), (3, 'types')], delete: [0]}",*

 * * "'hash'": "'f170d46818dea8ca3b35995f422088d0d45d553a8ae132aa10d152aa6a274fa0'",*

 * * "'id'": "'multiprocessing.queues'",*

 * * "'interface_hash'": "'4523d82895c23258d709dbe86acb335ebca8e411d1103a63d8a66aa9822a015f'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.1 […]*

```diff
@@ -1,37 +1,40 @@
 {
     "data_mtime": 1680161756,
     "dep_lines": [
-        2,
         1,
+        2,
         3,
+        6,
         1,
         1,
         1
     ],
     "dep_prios": [
-        5,
         10,
+        10,
+        5,
         5,
         5,
         30,
         30
     ],
     "dependencies": [
-        "collections.abc",
+        "queue",
         "sys",
         "typing",
+        "types",
         "builtins",
         "_typeshed",
         "abc"
     ],
-    "hash": "e44ea317051af09f8dfcc8fc2bf556ed7231f27d7cbaffded663ea2926d1f307",
-    "id": "multiprocessing.process",
+    "hash": "f170d46818dea8ca3b35995f422088d0d45d553a8ae132aa10d152aa6a274fa0",
+    "id": "multiprocessing.queues",
     "ignore_all": true,
-    "interface_hash": "a3e5d411574881d24b308809966143c632c703d92a81fa8552441fee5ab0a905",
+    "interface_hash": "4523d82895c23258d709dbe86acb335ebca8e411d1103a63d8a66aa9822a015f",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -66,13 +69,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/multiprocessing/process.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/multiprocessing/queues.pyi",
     "plugin_data": null,
-    "size": 1335,
+    "size": 1238,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/queues.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/queues.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/queues.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/reader.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7123148148148147%*

 * *Differences: {"'data_mtime'": '1680012434',*

 * * "'dep_lines'": '{insert: [(0, 5)], delete: [4, 3]}',*

 * * "'dep_prios'": '{insert: [(3, 5), (4, 5)], delete: [5, 1, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'yaml.error'), (1, '_typeshed'), (3, 'typing_extensions')], "*

 * *                   'delete: [5, 3, 1, 0]}',*

 * * "'hash'": "'89f882e9d50aa4e9b7226e9fcbe22a26fba214fbcabd2cdf2770e6626a360983'",*

 * * "'id'": "'yaml.reader'",*

 * * "'interface_hash'": "'dc37223836df446e4c816e40b9813ed5a5c34f9391e3a63f2dd0c122ee4ba754'",*

 * * "'mtime'": '1680012426' […]*

```diff
@@ -1,41 +1,38 @@
 {
-    "data_mtime": 1680161756,
+    "data_mtime": 1680012434,
     "dep_lines": [
+        5,
         1,
         2,
         3,
-        6,
-        1,
         1,
         1
     ],
     "dep_prios": [
-        10,
-        10,
         5,
         5,
         5,
-        30,
+        5,
+        5,
         30
     ],
     "dependencies": [
-        "queue",
-        "sys",
+        "yaml.error",
+        "_typeshed",
         "typing",
-        "types",
+        "typing_extensions",
         "builtins",
-        "_typeshed",
         "abc"
     ],
-    "hash": "f170d46818dea8ca3b35995f422088d0d45d553a8ae132aa10d152aa6a274fa0",
-    "id": "multiprocessing.queues",
+    "hash": "89f882e9d50aa4e9b7226e9fcbe22a26fba214fbcabd2cdf2770e6626a360983",
+    "id": "yaml.reader",
     "ignore_all": true,
-    "interface_hash": "4523d82895c23258d709dbe86acb335ebca8e411d1103a63d8a66aa9822a015f",
-    "mtime": 1679496944,
+    "interface_hash": "dc37223836df446e4c816e40b9813ed5a5c34f9391e3a63f2dd0c122ee4ba754",
+    "mtime": 1680012426,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -69,13 +66,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/multiprocessing/queues.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/reader.pyi",
     "plugin_data": null,
-    "size": 1238,
+    "size": 1038,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/reduction.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/reduction.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/reduction.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/reduction.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/shared_memory.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/shared_memory.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/shared_memory.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/_log.meta.json`

 * *Files 10% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7610774410774411%*

 * *Differences: {"'data_mtime'": '1680278525',*

 * * "'dep_lines'": '{insert: [(0, 5), (2, 2)], delete: [4, 0]}',*

 * * "'dep_prios'": '{insert: [(2, 10)], delete: [2]}',*

 * * "'dependencies'": "{insert: [(0, 'unittest.case'), (1, 'logging'), (4, 'typing')], delete: [3, 2, "*

 * *                   '0]}',*

 * * "'hash'": "'297a51a36613ffcd84bcef772c3f0dd0fdb57a1a9acc544a72840468647d968c'",*

 * * "'id'": "'unittest._log'",*

 * * "'interface_hash'": "'f790fed9c5c66a487dd8d192db67e8fd7980e77d29df6657b41c33bacc94eb88'",*

 * * "'path'": "'/home/james/.local/share/ha […]*

```diff
@@ -1,43 +1,43 @@
 {
-    "data_mtime": 1680161756,
+    "data_mtime": 1680278525,
     "dep_lines": [
-        2,
+        5,
         1,
+        2,
         3,
         4,
-        7,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
         10,
-        5,
+        10,
         5,
         5,
         5,
         30,
         30
     ],
     "dependencies": [
-        "collections.abc",
+        "unittest.case",
+        "logging",
         "sys",
-        "typing",
-        "typing_extensions",
         "types",
+        "typing",
         "builtins",
         "_typeshed",
         "abc"
     ],
-    "hash": "d6a72618e0f6acaa3a2f6730a43e468df406e957b6d7a5d042bba955e5dc2328",
-    "id": "multiprocessing.shared_memory",
+    "hash": "297a51a36613ffcd84bcef772c3f0dd0fdb57a1a9acc544a72840468647d968c",
+    "id": "unittest._log",
     "ignore_all": true,
-    "interface_hash": "82cc4bbbb75f569154f4099bbdc3ffdad4b4cd65dd1f0ca9f974f88d88aea800",
+    "interface_hash": "f790fed9c5c66a487dd8d192db67e8fd7980e77d29df6657b41c33bacc94eb88",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -72,13 +72,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/multiprocessing/shared_memory.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unittest/_log.pyi",
     "plugin_data": null,
-    "size": 1354,
+    "size": 892,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/sharedctypes.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/sharedctypes.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/sharedctypes.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/sharedctypes.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/spawn.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/spawn.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/spawn.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/error.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7088888888888889%*

 * *Differences: {"'data_mtime'": '1680012434',*

 * * "'dep_lines'": '{delete: [2, 1]}',*

 * * "'dep_prios'": '{insert: [(1, 30)], delete: [2, 1, 0]}',*

 * * "'dependencies'": "{insert: [(2, 'typing')], delete: [2, 1, 0]}",*

 * * "'hash'": "'941a31ff4b8c7774905ca62dff8018605f6f18a20c021da72f93746e04270d68'",*

 * * "'id'": "'yaml.error'",*

 * * "'interface_hash'": "'061f95064df216e8470d9bfe7bdfaa2abec17641b45e6fb5c0f7490188be016f'",*

 * * "'mtime'": '1680012426',*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/ […]*

```diff
@@ -1,35 +1,29 @@
 {
-    "data_mtime": 1680161756,
+    "data_mtime": 1680012434,
     "dep_lines": [
         1,
-        2,
-        3,
         1,
         1
     ],
     "dep_prios": [
         5,
-        5,
-        5,
-        5,
+        30,
         30
     ],
     "dependencies": [
-        "collections.abc",
-        "types",
-        "typing",
         "builtins",
-        "abc"
+        "abc",
+        "typing"
     ],
-    "hash": "ab21af9d8e81cb2d2d1f03eccfcea5175c0000bd3607fbdbeb0bbae2f0ac80d9",
-    "id": "multiprocessing.spawn",
+    "hash": "941a31ff4b8c7774905ca62dff8018605f6f18a20c021da72f93746e04270d68",
+    "id": "yaml.error",
     "ignore_all": true,
-    "interface_hash": "bafc1befe0857d0963d69a21ddd92d6c2f2d6489eeecc7b525696cdc47c8a27b",
-    "mtime": 1679496944,
+    "interface_hash": "061f95064df216e8470d9bfe7bdfaa2abec17641b45e6fb5c0f7490188be016f",
+    "mtime": 1680012426,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -63,13 +57,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/multiprocessing/spawn.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/error.pyi",
     "plugin_data": null,
-    "size": 861,
+    "size": 749,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/synchronize.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/synchronize.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/synchronize.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/synchronize.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/util.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/multiprocessing/util.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/multiprocessing/util.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/_re.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7129166666666666%*

 * *Differences: {"'data_mtime'": '1680278525',*

 * * "'dep_lines'": '{insert: [(0, 12), (2, 7), (3, 8), (4, 9), (5, 10), (6, 1), (7, 1), (8, 1)], '*

 * *                'delete: [5, 3, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(4, 10), (7, 30), (8, 30), (9, 30)], delete: [1]}',*

 * * "'dependencies'": "{insert: [(0, 'tomli._types'), (1, '__future__'), (2, 'datetime'), (3, "*

 * *                   "'functools'), (4, 're'), (7, '_typeshed'), (11, 'enum'), (14, "*

 * *                   "'typing_extensions')], delete: [5, 3, 2, 1, 0]}",*

 * * "'hash'": "'75 […]*

```diff
@@ -1,56 +1,65 @@
 {
-    "data_mtime": 1680161756,
+    "data_mtime": 1680278525,
     "dep_lines": [
-        3,
-        1,
-        2,
-        4,
+        12,
         5,
-        6,
+        7,
+        8,
+        9,
+        10,
+        1,
+        1,
+        1,
         1,
         1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
-        10,
         5,
         5,
         5,
+        10,
         5,
         5,
         30,
         30,
         30,
         30,
+        30,
+        30,
+        30,
         30
     ],
     "dependencies": [
-        "collections.abc",
-        "threading",
-        "_typeshed",
-        "logging",
+        "tomli._types",
+        "__future__",
+        "datetime",
+        "functools",
+        "re",
         "typing",
-        "typing_extensions",
         "builtins",
+        "_typeshed",
         "abc",
         "array",
         "ctypes",
+        "enum",
         "mmap",
-        "pickle"
+        "pickle",
+        "typing_extensions"
     ],
-    "hash": "950310d7e05e3d9bcc405ce475cec4ed8bf788b7148b6ae9d96eea92ebce861b",
-    "id": "multiprocessing.util",
+    "hash": "75b8e0e428594f6dca6bdcfd0c73977ddb52a4fc147dd80c5e78fc34ea25cbec",
+    "id": "tomli._re",
     "ignore_all": true,
-    "interface_hash": "60c7732061b098c9be0068c7282d4f4c4c0bc379fc09d2306e209ba61a00cb63",
-    "mtime": 1679496944,
+    "interface_hash": "9ad2e882ddd0ddd6fae258a78ddc646427ce9843c3461e25bde4108f94b00f9a",
+    "mtime": 1679496943,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -84,13 +93,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/multiprocessing/util.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/tomli/_re.py",
     "plugin_data": null,
-    "size": 2429,
+    "size": 2943,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/os/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/os/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/os/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/_parser.meta.json`

 * *Files 10% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.6982600732600732%*

 * *Differences: {"'data_mtime'": '1680278526',*

 * * "'dep_lines'": '{insert: [(0, 7), (1, 12), (2, 20), (3, 5), (4, 8), (5, 9), (6, 10), (8, 1), (9, '*

 * *                '1), (10, 1), (11, 1), (12, 1)], delete: [11, 10, 9, 8, 7, 6, 5, 4, 3, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(4, 10), (8, 30), (9, 30), (10, 30), (11, 30), (12, 30)], delete: [4, '*

 * *                '3, 2, 1, 0]}',*

 * * "'dependencies'": "{insert: [(1, 'tomli._re'), (2, 'tomli._types'), (3, '__future__'), (4, "*

 * *                   "'string'), (5, 'types'), (6, 'typing'),  […]*

```diff
@@ -1,68 +1,71 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680278526,
     "dep_lines": [
-        23,
-        30,
+        7,
+        12,
+        20,
+        5,
+        8,
+        9,
+        10,
+        1,
+        1,
+        1,
+        1,
+        1,
         1,
-        2,
-        21,
-        22,
-        24,
-        25,
-        26,
-        27,
-        28,
-        33,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
-        10,
-        10,
-        5,
-        5,
-        5,
         5,
         5,
         5,
+        10,
         5,
         5,
         5,
         30,
         30,
         30,
+        30,
+        30,
+        30,
+        30,
+        30,
         30
     ],
     "dependencies": [
         "collections.abc",
-        "os.path",
-        "sys",
+        "tomli._re",
+        "tomli._types",
+        "__future__",
+        "string",
+        "types",
+        "typing",
+        "builtins",
         "_typeshed",
         "abc",
-        "builtins",
-        "contextlib",
-        "io",
-        "subprocess",
-        "typing",
-        "typing_extensions",
-        "types",
         "array",
         "ctypes",
+        "datetime",
         "mmap",
-        "pickle"
+        "pickle",
+        "re",
+        "typing_extensions"
     ],
-    "hash": "4a8324189926c5351fe71b5411d9eda688b9c3854e620ff2045b6970266eb079",
-    "id": "os",
+    "hash": "83df8435a00b4be07c768918a42bb35056a55a5a20ed3f922183232d9496aed3",
+    "id": "tomli._parser",
     "ignore_all": true,
-    "interface_hash": "715501750e4bbbb755525e210fb27f5068a6ad84428afe83ad84d69c1016e713",
-    "mtime": 1679496944,
+    "interface_hash": "4fe813d67b766911e29ff84c1f4d006db3fd0bfd70b2fff6044c256d77da5ff2",
+    "mtime": 1679496943,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -96,13 +99,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/os/__init__.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/tomli/_parser.py",
     "plugin_data": null,
-    "size": 36855,
+    "size": 22633,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/os/path.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/os/path.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/os/path.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/runner.meta.json`

 * *Files 9% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7322222222222223%*

 * *Differences: {"'data_mtime'": '1680278525',*

 * * "'dep_lines'": '{insert: [(1, 2), (2, 3), (3, 4), (5, 5), (6, 6)], delete: [1]}',*

 * * "'dep_prios'": '{insert: [(0, 10), (1, 10), (4, 20), (6, 5), (7, 5)], delete: [3]}',*

 * * "'dependencies'": "{insert: [(0, 'unittest.case'), (1, 'unittest.result'), (2, 'unittest.suite'), "*

 * *                   "(3, 'collections.abc'), (4, 'unittest'), (5, 'typing'), (6, "*

 * *                   "'typing_extensions')], delete: [4, 1, 0]}",*

 * * "'hash'": "'38357da7850b668627503d574cb0e5545a449f460bfbb9e8d632 […]*

```diff
@@ -1,34 +1,46 @@
 {
-    "data_mtime": 1680589460,
+    "data_mtime": 1680278525,
     "dep_lines": [
         1,
-        7,
+        2,
+        3,
+        4,
         1,
+        5,
+        6,
         1,
         1
     ],
     "dep_prios": [
         10,
+        10,
+        10,
+        5,
+        20,
+        5,
         5,
         5,
-        30,
         30
     ],
     "dependencies": [
-        "sys",
-        "posixpath",
+        "unittest.case",
+        "unittest.result",
+        "unittest.suite",
+        "collections.abc",
+        "unittest",
+        "typing",
+        "typing_extensions",
         "builtins",
-        "abc",
-        "typing"
+        "abc"
     ],
-    "hash": "1bbead25bbe51b5fe4cc577c8270aa4b8321b7780fce50b58a1201ab3babc433",
-    "id": "os.path",
+    "hash": "38357da7850b668627503d574cb0e5545a449f460bfbb9e8d6325f3820e0aeef",
+    "id": "unittest.runner",
     "ignore_all": true,
-    "interface_hash": "c642066bf2d20711b1934dcdfb641b1546d6d49a6a79f30ca2f4dd67284271f3",
+    "interface_hash": "4bb129d47b0249602c7932bde716715a821cb0f7faa751c16af9efdfed6f5cc3",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -63,13 +75,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/os/path.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unittest/runner.pyi",
     "plugin_data": null,
-    "size": 186,
+    "size": 1353,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_elffile.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_elffile.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_elffile.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/async_case.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7603769841269841%*

 * *Differences: {"'dep_lines'": '{insert: [(0, 2), (1, 6), (3, 3), (4, 4)], delete: [6, 5, 4, 3, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(0, 5), (1, 5), (5, 5)], delete: [8, 7, 6, 5, 1, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'collections.abc'), (1, 'unittest.case'), (2, 'sys'), (4, "*

 * *                   "'typing_extensions'), (6, '_typeshed')], delete: [10, 9, 8, 7, 6, 2, 1, 0]}",*

 * * "'hash'": "'ef2aa50559010d3124e9f0003c17f9cd8b959f4c73d8157fe40ab0ba3c218808'",*

 * * "'id'": "'unittest.async_case'",*

 * * "'interface_hash'": "'a339439 […]*

```diff
@@ -1,52 +1,43 @@
 {
     "data_mtime": 1680278525,
     "dep_lines": [
-        11,
-        12,
-        13,
-        14,
-        1,
-        1,
-        1,
+        2,
+        6,
         1,
+        3,
+        4,
         1,
         1,
         1
     ],
     "dep_prios": [
-        10,
-        10,
+        5,
+        5,
         10,
         5,
         5,
-        30,
-        30,
-        30,
-        30,
+        5,
         30,
         30
     ],
     "dependencies": [
-        "enum",
-        "os",
-        "struct",
+        "collections.abc",
+        "unittest.case",
+        "sys",
         "typing",
+        "typing_extensions",
         "builtins",
-        "abc",
-        "array",
-        "ctypes",
-        "mmap",
-        "pickle",
-        "typing_extensions"
+        "_typeshed",
+        "abc"
     ],
-    "hash": "85b98af0e0fa67b7d8ea1c229c7114703d5bcbb73390688d62eed28671449369",
-    "id": "packaging._elffile",
+    "hash": "ef2aa50559010d3124e9f0003c17f9cd8b959f4c73d8157fe40ab0ba3c218808",
+    "id": "unittest.async_case",
     "ignore_all": true,
-    "interface_hash": "6813c991ccfb7e9f770910239ac61d8881862c897a99edb34da8e82761bc69d9",
+    "interface_hash": "a3394397f94a7af47f9c92b60a2ab86ff45e5ef15a359b981e6e9367835e4e73",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -81,13 +72,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/packaging/_elffile.py",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unittest/async_case.pyi",
     "plugin_data": null,
-    "size": 3266,
+    "size": 663,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_manylinux.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_manylinux.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_manylinux.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_manylinux.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_musllinux.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_musllinux.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_musllinux.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_musllinux.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_parser.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_parser.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_parser.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_parser.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_structures.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_structures.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_structures.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/emitter.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7088888888888889%*

 * *Differences: {"'data_mtime'": '1680012434',*

 * * "'dep_lines'": '{insert: [(0, 3)], delete: [0]}',*

 * * "'dep_prios'": '{insert: [(1, 5), (2, 5)], delete: [2, 1]}',*

 * * "'dependencies'": "{insert: [(0, 'yaml.error'), (1, 'typing')], delete: [3, 2]}",*

 * * "'hash'": "'36c66ff5726e098a36c4b005e415a6977e6c98e5c8ee49dc6cf04afe85b0ab3f'",*

 * * "'id'": "'yaml.emitter'",*

 * * "'interface_hash'": "'2ab4289f40584fc887864664c785a9791ad4a2f6a66ca64ede9039061537b941'",*

 * * "'mtime'": '1680012426',*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/pyth […]*

```diff
@@ -1,32 +1,32 @@
 {
-    "data_mtime": 1680278525,
+    "data_mtime": 1680012434,
     "dep_lines": [
-        1,
+        3,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
-        30,
-        30,
+        5,
+        5,
         30
     ],
     "dependencies": [
+        "yaml.error",
+        "typing",
         "builtins",
-        "abc",
-        "types",
-        "typing"
+        "abc"
     ],
-    "hash": "ab77953666d62461bf4b40e2b7f4b7028f2a42acffe4f6135c500a0597b9cabe",
-    "id": "packaging._structures",
+    "hash": "36c66ff5726e098a36c4b005e415a6977e6c98e5c8ee49dc6cf04afe85b0ab3f",
+    "id": "yaml.emitter",
     "ignore_all": true,
-    "interface_hash": "52c23dd350071a797973de4f3a72c0e994ad922b78f25c17d0dc9f355e167b63",
-    "mtime": 1679496944,
+    "interface_hash": "2ab4289f40584fc887864664c785a9791ad4a2f6a66ca64ede9039061537b941",
+    "mtime": 1680012426,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -60,13 +60,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/packaging/_structures.py",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/emitter.pyi",
     "plugin_data": null,
-    "size": 1431,
+    "size": 4141,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_tokenizer.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_tokenizer.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/_tokenizer.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/_tokenizer.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/markers.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/markers.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/markers.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/markers.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/requirements.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/requirements.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/requirements.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/requirements.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/specifiers.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/specifiers.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/specifiers.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/utils.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7989460784313726%*

 * *Differences: {"'dep_lines'": '{insert: [(0, 8), (1, 9), (2, 5), (3, 6), (4, 1)], delete: [5, 4, 3, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(5, 30)], delete: [3, 2]}',*

 * * "'dependencies'": "{insert: [(0, 'packaging.tags'), (6, 'abc')], delete: [3, 2, 0]}",*

 * * "'hash'": "'7acd1c09eccab29ceb890fb757cf21df2273c73d36f1eb95dac53033ad6413ea'",*

 * * "'id'": "'packaging.utils'",*

 * * "'interface_hash'": "'3c483eccc88d2544f12386c100fcfc2f1c1dc626aa1ce6df0e24b4446fda7e62'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpat […]*

```diff
@@ -1,64 +1,61 @@
 {
     "data_mtime": 1680278526,
     "dep_lines": [
-        26,
-        27,
-        11,
-        12,
-        13,
-        14,
+        8,
+        9,
+        5,
+        6,
+        1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
         5,
         10,
-        10,
-        10,
         5,
         5,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
+        30,
         30
     ],
     "dependencies": [
-        "packaging.utils",
+        "packaging.tags",
         "packaging.version",
-        "abc",
-        "itertools",
         "re",
         "typing",
         "builtins",
         "_typeshed",
+        "abc",
         "array",
         "ctypes",
         "enum",
         "mmap",
         "pickle",
         "types",
         "typing_extensions"
     ],
-    "hash": "fb76a36790a442b8cd5b91fc34f8ef095d91060afec3dc1c60175bf248cf05f8",
-    "id": "packaging.specifiers",
+    "hash": "7acd1c09eccab29ceb890fb757cf21df2273c73d36f1eb95dac53033ad6413ea",
+    "id": "packaging.utils",
     "ignore_all": true,
-    "interface_hash": "9c27f50be3017562798945282cd6bf8959bd4e36a80f3c88aa5092e599ac6917",
+    "interface_hash": "3c483eccc88d2544f12386c100fcfc2f1c1dc626aa1ce6df0e24b4446fda7e62",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -93,13 +90,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/packaging/specifiers.py",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/packaging/utils.py",
     "plugin_data": null,
-    "size": 39046,
+    "size": 4355,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/tags.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/tags.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/tags.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/tags.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/utils.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/utils.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/utils.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/builtins.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.739672083150344%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 30), (2, 2), (3, 3), (4, 4), (5, 5), (6, 31), (7, 35), (8, 57)], '*

 * *                'delete: [6, 5, 4, 3, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(1, 10), (6, 5), (7, 5), (8, 5)], delete: [7, 6, 5]}',*

 * * "'dependencies'": "{insert: [(0, 'collections.abc'), (1, '_ast'), (3, 'sys'), (4, 'types'), (5, "*

 * *                   "'_collections_abc'), (6, 'io'), (7, 'typing'), (8, 'typing_extensions'), (12, "*

 * *                   "'importlib')], delete: [13, 12,  […]*

```diff
@@ -1,61 +1,64 @@
 {
-    "data_mtime": 1680278526,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        8,
-        9,
-        5,
-        6,
-        1,
-        1,
-        1,
+        30,
         1,
+        2,
+        3,
+        4,
+        5,
+        31,
+        35,
+        57,
         1,
         1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
+        10,
         5,
         10,
         5,
         5,
-        30,
-        30,
-        30,
+        5,
+        5,
+        5,
         30,
         30,
         30,
         30,
         30,
         30
     ],
     "dependencies": [
-        "packaging.tags",
-        "packaging.version",
-        "re",
-        "typing",
-        "builtins",
+        "collections.abc",
+        "_ast",
         "_typeshed",
+        "sys",
+        "types",
+        "_collections_abc",
+        "io",
+        "typing",
+        "typing_extensions",
         "abc",
         "array",
         "ctypes",
-        "enum",
+        "importlib",
         "mmap",
-        "pickle",
-        "types",
-        "typing_extensions"
+        "pickle"
     ],
-    "hash": "7acd1c09eccab29ceb890fb757cf21df2273c73d36f1eb95dac53033ad6413ea",
-    "id": "packaging.utils",
+    "hash": "2036859bfabd3515c707a849167221d44fe91af7b10f828d2745a152a4af3fea",
+    "id": "builtins",
     "ignore_all": true,
-    "interface_hash": "3c483eccc88d2544f12386c100fcfc2f1c1dc626aa1ce6df0e24b4446fda7e62",
+    "interface_hash": "4893fdbcb6f39c06f42c6743630d18bbcae1bc7cbce9edef3460bb21c8c1626c",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -90,13 +93,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/packaging/utils.py",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/builtins.pyi",
     "plugin_data": null,
-    "size": 4355,
+    "size": 82326,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/version.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/version.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/packaging/version.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/packaging/version.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/pytest/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/pytest/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/pytest/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/pytest/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/compliance.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/compliance.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/compliance.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_find_reference.meta.json`

 * *Files 10% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7158421825088491%*

 * *Differences: {"'data_mtime'": '1680332416',*

 * * "'dep_lines'": '{insert: [(0, 5), (1, 6), (2, 7), (3, 8), (5, 16)], delete: [10, 9, 8, 7, 6, 5, '*

 * *                '4, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(6, 5)], delete: [11, 10, 9, 8, 5, 3]}',*

 * * "'dependencies'": "{insert: [(0, 'asyncio'), (2, 'operator'), (9, '_pytest.config'), (10, "*

 * *                   "'_pytest.fixtures'), (14, 'jsonpath.env'), (15, 'jsonpath.path')], delete: "*

 * *                   '[20, 19, 18, 17, 16, 15, 13, 12, 2, 1, 0]}',*

 * * "'hash'": "'b5f1c4000ed8b9 […]*

```diff
@@ -1,21 +1,16 @@
 {
-    "data_mtime": 1680543228,
+    "data_mtime": 1680332416,
     "dep_lines": [
-        11,
-        12,
-        13,
+        5,
+        6,
+        7,
+        8,
         14,
-        15,
-        22,
-        24,
-        1,
-        1,
-        1,
-        1,
+        16,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
@@ -24,60 +19,50 @@
         1
     ],
     "dep_prios": [
         10,
         10,
         10,
         5,
-        5,
-        10,
         10,
         5,
-        30,
-        30,
-        30,
-        30,
+        5,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
         30
     ],
     "dependencies": [
-        "json",
-        "operator",
-        "unittest",
+        "asyncio",
         "dataclasses",
+        "operator",
         "typing",
         "pytest",
         "jsonpath",
         "builtins",
         "_operator",
         "_pytest",
+        "_pytest.config",
+        "_pytest.fixtures",
         "_pytest.mark",
         "_pytest.mark.structures",
-        "_pytest.outcomes",
-        "_typeshed",
         "abc",
-        "io",
-        "json.decoder",
-        "os",
-        "types",
-        "typing_extensions",
-        "unittest.case"
+        "jsonpath.env",
+        "jsonpath.path"
     ],
-    "hash": "1c2d740d29c518a16919f19474032b4d2457789f7338bd0cf6d930b5c0873204",
-    "id": "tests.compliance",
+    "hash": "b5f1c4000ed8b946b14ac6be447aad201c4281e49fb3aaa3d61e8940c7d0ba9e",
+    "id": "tests.test_find_reference",
     "ignore_all": false,
-    "interface_hash": "13cea6604cd7f8e6d223b73ea75f3a4dfba4f9fb134059d1b3a24a22ef0fdb4e",
-    "mtime": 1680543227,
+    "interface_hash": "dabe6384c4ffbc10b6ee182cd0a8d094fba6a63967b198ec6ee2af2ac265b831",
+    "mtime": 1680332415,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -111,13 +96,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/compliance.py",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/test_find_reference.py",
     "plugin_data": null,
-    "size": 2036,
+    "size": 15182,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/consensus.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/consensus.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/consensus.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_errors.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7125192012288787%*

 * *Differences: {"'data_mtime'": '1680254514',*

 * * "'dep_lines'": '{insert: [(0, 4), (1, 1), (2, 3), (3, 1), (4, 1)], delete: [6, 5, 4, 3, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(4, 30), (5, 30)], delete: [6, 2, 1, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'jsonpath.exceptions'), (5, '_pytest._code'), (6, "*

 * *                   "'_pytest._code.code'), (7, '_pytest.config'), (8, '_pytest.fixtures'), (9, "*

 * *                   "'_pytest.python_api'), (11, 'contextlib'), (12, 'jsonpath.env'), (13, "*

 * *                   "'jsonpath.path' […]*

```diff
@@ -1,77 +1,71 @@
 {
-    "data_mtime": 1680543239,
+    "data_mtime": 1680254514,
     "dep_lines": [
-        11,
-        12,
-        13,
-        14,
-        22,
-        23,
-        25,
+        4,
+        1,
+        3,
+        1,
+        1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
-        10,
-        10,
-        5,
         5,
         10,
         5,
-        10,
         5,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
+        30,
+        30,
         30
     ],
     "dependencies": [
-        "operator",
-        "unittest",
-        "dataclasses",
-        "typing",
+        "jsonpath.exceptions",
         "pytest",
-        "yaml",
         "jsonpath",
         "builtins",
-        "_collections_abc",
-        "_operator",
         "_pytest",
-        "_pytest.mark",
-        "_pytest.mark.structures",
-        "_pytest.outcomes",
-        "_typeshed",
+        "_pytest._code",
+        "_pytest._code.code",
+        "_pytest.config",
+        "_pytest.fixtures",
+        "_pytest.python_api",
         "abc",
-        "io",
-        "os",
-        "unittest.case"
+        "contextlib",
+        "jsonpath.env",
+        "jsonpath.path",
+        "jsonpath.token",
+        "re",
+        "typing"
     ],
-    "hash": "f3dfdda91bc6fe1715204713d23a86aefa815eaf2174b29c14f0589366eb6eee",
-    "id": "tests.consensus",
+    "hash": "4c26fecf53c2ec7f96beb4aca651073c2b9a2a569bac285e19f2bc4106cded3f",
+    "id": "tests.test_errors",
     "ignore_all": false,
-    "interface_hash": "19afc16497dd87468936db5d25b95be86c9e2e9822e8f3b4678e8981092ec569",
-    "mtime": 1680543246,
+    "interface_hash": "ad13861afb48bc97e363abbb7fcc2f6f97df4c51d7d1a9d710851028f7036957",
+    "mtime": 1680254515,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -105,13 +99,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/consensus.py",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/test_errors.py",
     "plugin_data": null,
-    "size": 2550,
+    "size": 747,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_async.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_async.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_async.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_async.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_compare.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_compare.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_compare.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_compare.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_compound_path.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_compound_path.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_compound_path.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_compound_path.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_concrete_path.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_concrete_path.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_concrete_path.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_concrete_path.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_env.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_env.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_env.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/lex.meta.json`

 * *Files 12% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.6711928104575163%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 10), (1, 11), (3, 4), (5, 6), (6, 69)], delete: [6, 5, 4, 3, 1]}',*

 * * "'dep_prios'": '{insert: [(0, 5), (1, 5), (6, 25), (7, 5)], delete: [7, 6, 5, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'jsonpath.exceptions'), (1, 'jsonpath.token'), (2, "*

 * *                   "'__future__'), (3, 're'), (4, 'functools'), (9, 'enum')], delete: [10, 7, 6, "*

 * *                   '5, 2, 0]}',*

 * * "'hash'": "'bf482a50ebd648e0d68afd7420fa3ff3462bd5af1ce9f123a408b36366314de8'", […]*

```diff
@@ -1,53 +1,53 @@
 {
-    "data_mtime": 1679900652,
+    "data_mtime": 1680779143,
     "dep_lines": [
+        10,
+        11,
         2,
-        3,
+        4,
         5,
-        7,
-        1,
-        1,
-        1,
+        6,
+        69,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
-        10,
+        5,
+        5,
         5,
         10,
         5,
         5,
-        30,
-        30,
-        30,
+        25,
+        5,
         30,
         30,
         30
     ],
     "dependencies": [
-        "asyncio",
+        "jsonpath.exceptions",
+        "jsonpath.token",
+        "__future__",
+        "re",
+        "functools",
         "typing",
-        "pytest",
         "jsonpath",
         "builtins",
-        "_pytest",
-        "_pytest.config",
-        "_pytest.fixtures",
         "abc",
-        "jsonpath.env",
-        "jsonpath.match"
+        "enum",
+        "jsonpath.env"
     ],
-    "hash": "1bab37bbe16aec4f96c9dfefbb9b16076e0bde52b450e82829016362575837c1",
-    "id": "tests.test_env",
-    "ignore_all": false,
-    "interface_hash": "4edff46f5ed4f8f6c7d90c0607f8e31a9a829d0caf6bce550da3974894d159a2",
-    "mtime": 1680100237,
+    "hash": "bf482a50ebd648e0d68afd7420fa3ff3462bd5af1ce9f123a408b36366314de8",
+    "id": "jsonpath.lex",
+    "ignore_all": true,
+    "interface_hash": "889c44ded3efbffa61b40d47da01e2a699b2e252e49fd68b8739597dfd7cd11c",
+    "mtime": 1680277988,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -81,13 +81,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/test_env.py",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/lex.py",
     "plugin_data": null,
-    "size": 3989,
+    "size": 11085,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_errors.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_errors.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_errors.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_ietf_comparison.meta.json`

 * *Files 11% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.717668677622911%*

 * *Differences: {"'data_mtime'": '1680099039',*

 * * "'dep_lines'": '{insert: [(0, 45), (1, 39), (2, 40), (3, 42), (4, 44)], delete: [6, 5, 4, 3, 2, '*

 * *                '1, 0]}',*

 * * "'dep_prios'": '{insert: [(1, 10), (2, 10)], delete: [7, 6, 5, 4]}',*

 * * "'dependencies'": "{insert: [(0, 'jsonpath.filter'), (1, 'dataclasses'), (2, 'operator'), (6, "*

 * *                   "'_operator'), (10, '_pytest.mark'), (11, '_pytest.mark.structures')], delete: "*

 * *                   '[15, 14, 13, 11, 9, 6, 5, 0]}',*

 * * "'hash'": "'afeb0fc3106edaffe9d77c1b […]*

```diff
@@ -1,71 +1,65 @@
 {
-    "data_mtime": 1680254514,
+    "data_mtime": 1680099039,
     "dep_lines": [
-        4,
-        1,
-        3,
-        1,
-        1,
-        1,
-        1,
+        45,
+        39,
+        40,
+        42,
+        44,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
         10,
+        10,
+        10,
         5,
         5,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
-        30,
-        30,
-        30,
-        30,
         30
     ],
     "dependencies": [
-        "jsonpath.exceptions",
+        "jsonpath.filter",
+        "dataclasses",
+        "operator",
         "pytest",
         "jsonpath",
         "builtins",
+        "_operator",
         "_pytest",
-        "_pytest._code",
-        "_pytest._code.code",
         "_pytest.config",
         "_pytest.fixtures",
-        "_pytest.python_api",
+        "_pytest.mark",
+        "_pytest.mark.structures",
         "abc",
-        "contextlib",
         "jsonpath.env",
-        "jsonpath.path",
-        "jsonpath.token",
-        "re",
         "typing"
     ],
-    "hash": "4c26fecf53c2ec7f96beb4aca651073c2b9a2a569bac285e19f2bc4106cded3f",
-    "id": "tests.test_errors",
+    "hash": "afeb0fc3106edaffe9d77c1ba95dc1533afc0e98b35502e42f7603d26b641e0f",
+    "id": "tests.test_ietf_comparison",
     "ignore_all": false,
-    "interface_hash": "ad13861afb48bc97e363abbb7fcc2f6f97df4c51d7d1a9d710851028f7036957",
-    "mtime": 1680254515,
+    "interface_hash": "c20871a0ce40467cd634f08cb99140d9f8e7aadf46c038a9c2e4f46893e1d3e5",
+    "mtime": 1680586233,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -99,13 +93,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/test_errors.py",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/test_ietf_comparison.py",
     "plugin_data": null,
-    "size": 747,
+    "size": 6415,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_find.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_find.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_find.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_find.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_find_compound_path.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_find_compound_path.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_find_compound_path.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_find_compound_path.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_find_reference.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_find_reference.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_find_reference.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_parse_compound_path.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7263888888888889%*

 * *Differences: {"'data_mtime'": '1680099093',*

 * * "'dep_lines'": '{insert: [(0, 1), (1, 2), (2, 4), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)], '*

 * *                'delete: [5, 4, 3, 2, 0]}',*

 * * "'dep_prios'": '{insert: [(5, 30), (6, 30), (7, 30), (8, 30), (9, 30)], delete: [3, 0]}',*

 * * "'dependencies'": "{insert: [(12, 'array'), (13, 'ctypes'), (16, 'mmap'), (17, 'pickle'), (18, "*

 * *                   "'typing')], delete: [3, 0]}",*

 * * "'hash'": "'454dd9750476cec98998ab05a27aba9ad30713856c57d321233ffe85189d63f5'",*

 * * "'id'": "'tests.test_p […]*

```diff
@@ -1,16 +1,19 @@
 {
-    "data_mtime": 1680332416,
+    "data_mtime": 1680099093,
     "dep_lines": [
-        5,
+        1,
+        2,
+        4,
         6,
-        7,
-        8,
-        14,
-        16,
+        1,
+        1,
+        1,
+        1,
+        1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
@@ -19,50 +22,56 @@
         1
     ],
     "dep_prios": [
         10,
         10,
         10,
         5,
-        10,
-        5,
         5,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
+        30,
+        30,
+        30,
+        30,
+        30,
         30
     ],
     "dependencies": [
-        "asyncio",
         "dataclasses",
         "operator",
-        "typing",
         "pytest",
         "jsonpath",
         "builtins",
         "_operator",
         "_pytest",
         "_pytest.config",
         "_pytest.fixtures",
         "_pytest.mark",
         "_pytest.mark.structures",
         "abc",
+        "array",
+        "ctypes",
         "jsonpath.env",
-        "jsonpath.path"
+        "jsonpath.path",
+        "mmap",
+        "pickle",
+        "typing"
     ],
-    "hash": "b5f1c4000ed8b946b14ac6be447aad201c4281e49fb3aaa3d61e8940c7d0ba9e",
-    "id": "tests.test_find_reference",
+    "hash": "454dd9750476cec98998ab05a27aba9ad30713856c57d321233ffe85189d63f5",
+    "id": "tests.test_parse_compound_path",
     "ignore_all": false,
-    "interface_hash": "dabe6384c4ffbc10b6ee182cd0a8d094fba6a63967b198ec6ee2af2ac265b831",
-    "mtime": 1680332415,
+    "interface_hash": "eb4dc9dea6b903110671fc4a44b64eb331b8bba892e6c9a94e219ba764b48b58",
+    "mtime": 1680100260,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -96,13 +105,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/test_find_reference.py",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/test_parse_compound_path.py",
     "plugin_data": null,
-    "size": 15182,
+    "size": 1109,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_ietf.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_ietf.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_ietf.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_ietf.meta.json`

 * *Files 4% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9%*

 * *Differences: {"'hash'": "'21bd5047f29d0dee9cae38aef16d2cbfd59176f95f5c6b2287c0e8585451291c'",*

 * * "'mtime'": '1680777401',*

 * * "'size'": '12342'}*

```diff
@@ -50,19 +50,19 @@
         "_pytest.fixtures",
         "_pytest.mark",
         "_pytest.mark.structures",
         "abc",
         "jsonpath.env",
         "jsonpath.path"
     ],
-    "hash": "f26f57f3176faac03183ac45d7a2af62d232efc39cef6a99ea64a60ad496211a",
+    "hash": "21bd5047f29d0dee9cae38aef16d2cbfd59176f95f5c6b2287c0e8585451291c",
     "id": "tests.test_ietf",
     "ignore_all": false,
     "interface_hash": "45be24a9e44018e2c4283b2376aef396a5b8617f998f060ec278e50076a61c68",
-    "mtime": 1680276773,
+    "mtime": 1680777401,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -98,11 +98,11 @@
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
     "path": "/home/james/projects/simply_json_path/simply-json-path/tests/test_ietf.py",
     "plugin_data": null,
-    "size": 12396,
+    "size": 12342,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_ietf_comparison.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_ietf_comparison.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_ietf_comparison.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_re.meta.json`

 * *Files 13% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7340647370059136%*

 * *Differences: {"'data_mtime'": '1680771407',*

 * * "'dep_lines'": '{insert: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 10), (5, 12)], delete: [4, 3, 2, 1, '*

 * *                '0]}',*

 * * "'dep_prios'": '{insert: [(0, 10), (3, 5)], delete: [0]}',*

 * * "'dependencies'": "{insert: [(0, 'asyncio'), (3, 'typing'), (15, 'jsonpath.path')], delete: [14, "*

 * *                   '0]}',*

 * * "'hash'": "'b14741922b5d98d5f4f372221b15357a275a2de5f5b93ca54460adc71e5430c1'",*

 * * "'id'": "'tests.test_re'",*

 * * "'interface_hash'": "'6621c953ee612d41b0097322d0f8c85aafc2c34 […]*

```diff
@@ -1,65 +1,68 @@
 {
-    "data_mtime": 1680099039,
+    "data_mtime": 1680771407,
     "dep_lines": [
-        45,
-        39,
-        40,
-        42,
-        44,
+        1,
+        2,
+        3,
+        4,
+        10,
+        12,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
-        5,
         10,
         10,
         10,
         5,
+        10,
+        5,
         5,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
         30
     ],
     "dependencies": [
-        "jsonpath.filter",
+        "asyncio",
         "dataclasses",
         "operator",
+        "typing",
         "pytest",
         "jsonpath",
         "builtins",
         "_operator",
         "_pytest",
         "_pytest.config",
         "_pytest.fixtures",
         "_pytest.mark",
         "_pytest.mark.structures",
         "abc",
         "jsonpath.env",
-        "typing"
+        "jsonpath.path"
     ],
-    "hash": "afeb0fc3106edaffe9d77c1ba95dc1533afc0e98b35502e42f7603d26b641e0f",
-    "id": "tests.test_ietf_comparison",
+    "hash": "b14741922b5d98d5f4f372221b15357a275a2de5f5b93ca54460adc71e5430c1",
+    "id": "tests.test_re",
     "ignore_all": false,
-    "interface_hash": "c20871a0ce40467cd634f08cb99140d9f8e7aadf46c038a9c2e4f46893e1d3e5",
-    "mtime": 1680586233,
+    "interface_hash": "6621c953ee612d41b0097322d0f8c85aafc2c3449f8cafe83e5f5219a93d2fba",
+    "mtime": 1680771676,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -93,13 +96,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/test_ietf_comparison.py",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/test_re.py",
     "plugin_data": null,
-    "size": 6415,
+    "size": 1615,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_lex.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_lex.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_lex.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_lex.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_match_api.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_match_api.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_match_api.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/nodes.meta.json`

 * *Files 9% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.6554545454545455%*

 * *Differences: {"'data_mtime'": '1680012434',*

 * * "'dep_lines'": '{insert: [(0, 3)], delete: [5, 4, 3, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(1, 5), (2, 5)], delete: [7, 6, 5, 4, 3, 2, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'yaml.error'), (1, 'typing')], delete: [8, 7, 6, 5, 4, 3, 0]}",*

 * * "'hash'": "'8fb0614d7b5894afcac04e11665310348b914a2e197ff395c3504b786ef37d64'",*

 * * "'id'": "'yaml.nodes'",*

 * * "'ignore_all'": 'True',*

 * * "'interface_hash'": "'8455f9774f8649c16be751cad0b31d65f4c406ee8b554a982855ef44ba92bfb4'",*

 * * "'mtime'": '16800 […]*

```diff
@@ -1,47 +1,32 @@
 {
-    "data_mtime": 1680333435,
+    "data_mtime": 1680012434,
     "dep_lines": [
-        1,
-        1,
-        1,
-        1,
-        1,
-        1,
+        3,
         1,
         1,
         1
     ],
     "dep_prios": [
-        10,
         5,
-        30,
-        30,
-        30,
-        30,
-        30,
-        30,
+        5,
+        5,
         30
     ],
     "dependencies": [
-        "jsonpath",
+        "yaml.error",
+        "typing",
         "builtins",
-        "abc",
-        "array",
-        "ctypes",
-        "jsonpath.match",
-        "mmap",
-        "pickle",
-        "typing"
+        "abc"
     ],
-    "hash": "63f0be661877d811fe9f2fc9a156745353729d0f26def0f4fc1136ac09560e8b",
-    "id": "tests.test_match_api",
-    "ignore_all": false,
-    "interface_hash": "442dc8e7ac8a90829d986bbbd96c9e456b1fe107b50f993b675c1ab8e628314a",
-    "mtime": 1680333526,
+    "hash": "8fb0614d7b5894afcac04e11665310348b914a2e197ff395c3504b786ef37d64",
+    "id": "yaml.nodes",
+    "ignore_all": true,
+    "interface_hash": "8455f9774f8649c16be751cad0b31d65f4c406ee8b554a982855ef44ba92bfb4",
+    "mtime": 1680012426,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -75,13 +60,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/test_match_api.py",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/nodes.pyi",
     "plugin_data": null,
-    "size": 1438,
+    "size": 1032,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_parse.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_parse.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_parse.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_parse.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_parse_compound_path.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_parse_compound_path.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_parse_compound_path.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_env.meta.json`

 * *Files 12% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7075757575757575%*

 * *Differences: {"'data_mtime'": '1679900652',*

 * * "'dep_lines'": '{insert: [(1, 3), (2, 5), (3, 7)], delete: [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 0]}',*

 * * "'dep_prios'": '{insert: [(1, 5)], delete: [12, 11, 10, 9, 8, 7, 6, 5, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'asyncio'), (1, 'typing'), (10, 'jsonpath.match')], delete: [18, "*

 * *                   '17, 16, 15, 13, 12, 10, 9, 5, 1, 0]}',*

 * * "'hash'": "'8acc9fee6d575e53eeea8c3c735d0ec7e8483deead74816ed909fdc4f469e57f'",*

 * * "'id'": "'tests.test_env'",*

 * * "'interface_hash'": "'4edff46f5ed […]*

```diff
@@ -1,77 +1,53 @@
 {
-    "data_mtime": 1680099093,
+    "data_mtime": 1679900652,
     "dep_lines": [
-        1,
         2,
-        4,
-        6,
-        1,
-        1,
-        1,
-        1,
-        1,
-        1,
-        1,
-        1,
+        3,
+        5,
+        7,
         1,
         1,
         1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
         10,
-        10,
+        5,
         10,
         5,
         5,
         30,
         30,
         30,
         30,
         30,
-        30,
-        30,
-        30,
-        30,
-        30,
-        30,
-        30,
-        30,
         30
     ],
     "dependencies": [
-        "dataclasses",
-        "operator",
+        "asyncio",
+        "typing",
         "pytest",
         "jsonpath",
         "builtins",
-        "_operator",
         "_pytest",
         "_pytest.config",
         "_pytest.fixtures",
-        "_pytest.mark",
-        "_pytest.mark.structures",
         "abc",
-        "array",
-        "ctypes",
         "jsonpath.env",
-        "jsonpath.path",
-        "mmap",
-        "pickle",
-        "typing"
+        "jsonpath.match"
     ],
-    "hash": "454dd9750476cec98998ab05a27aba9ad30713856c57d321233ffe85189d63f5",
-    "id": "tests.test_parse_compound_path",
+    "hash": "8acc9fee6d575e53eeea8c3c735d0ec7e8483deead74816ed909fdc4f469e57f",
+    "id": "tests.test_env",
     "ignore_all": false,
-    "interface_hash": "eb4dc9dea6b903110671fc4a44b64eb331b8bba892e6c9a94e219ba764b48b58",
-    "mtime": 1680100260,
+    "interface_hash": "4edff46f5ed4f8f6c7d90c0607f8e31a9a829d0caf6bce550da3974894d159a2",
+    "mtime": 1680771395,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -105,13 +81,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/test_parse_compound_path.py",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/test_env.py",
     "plugin_data": null,
-    "size": 1109,
+    "size": 4025,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_re.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/test_re.data.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9999999776320462%*

 * *Differences: {"'names'": "{'Case': {'node': {'metadata': {'dataclass': {'attributes': {0: {'line': 17}, 1: "*

 * *            "{'line': 18}, 2: {'line': 19}, 3: {'line': 20}}}}}}}"}*

```diff
@@ -43,37 +43,37 @@
                             {
                                 "alias": null,
                                 "column": 4,
                                 "has_default": false,
                                 "is_in_init": true,
                                 "is_init_var": false,
                                 "kw_only": false,
-                                "line": 13,
+                                "line": 17,
                                 "name": "description",
                                 "type": "builtins.str"
                             },
                             {
                                 "alias": null,
                                 "column": 4,
                                 "has_default": false,
                                 "is_in_init": true,
                                 "is_init_var": false,
                                 "kw_only": false,
-                                "line": 14,
+                                "line": 18,
                                 "name": "path",
                                 "type": "builtins.str"
                             },
                             {
                                 "alias": null,
                                 "column": 4,
                                 "has_default": false,
                                 "is_in_init": true,
                                 "is_init_var": false,
                                 "kw_only": false,
-                                "line": 15,
+                                "line": 19,
                                 "name": "data",
                                 "type": {
                                     ".class": "UnionType",
                                     "items": [
                                         {
                                             ".class": "Instance",
                                             "args": [
@@ -105,15 +105,15 @@
                             {
                                 "alias": null,
                                 "column": 4,
                                 "has_default": false,
                                 "is_in_init": true,
                                 "is_init_var": false,
                                 "kw_only": false,
-                                "line": 16,
+                                "line": 20,
                                 "name": "want",
                                 "type": {
                                     ".class": "UnionType",
                                     "items": [
                                         {
                                             ".class": "Instance",
                                             "args": [
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tests/test_re.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/compliance.meta.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7202777777777778%*

 * *Differences: {"'data_mtime'": '1680543228',*

 * * "'dep_lines'": '{insert: [(0, 11), (1, 12), (2, 13), (3, 14), (4, 15), (5, 22), (6, 24), (8, 1)], '*

 * *                'delete: [5, 4, 3, 2, 1]}',*

 * * "'dep_prios'": '{insert: [(5, 10), (6, 10), (8, 30), (9, 30)], delete: [4]}',*

 * * "'dependencies'": "{insert: [(0, 'json'), (2, 'unittest'), (3, 'dataclasses'), (12, "*

 * *                   "'_pytest.outcomes'), (13, '_typeshed'), (15, 'io'), (16, 'json.decoder'), (17, "*

 * *                   "'os'), (18, 'unittest.case')], delete: [15, 14, 1 […]*

```diff
@@ -1,16 +1,19 @@
 {
-    "data_mtime": 1680100267,
+    "data_mtime": 1680543228,
     "dep_lines": [
+        11,
+        12,
+        13,
+        14,
+        15,
+        22,
+        24,
+        1,
         1,
-        2,
-        3,
-        4,
-        6,
-        8,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
@@ -19,50 +22,56 @@
         1
     ],
     "dep_prios": [
         10,
         10,
         10,
         5,
-        10,
         5,
+        10,
+        10,
         5,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
         30,
+        30,
+        30,
         30
     ],
     "dependencies": [
-        "asyncio",
-        "dataclasses",
+        "json",
         "operator",
+        "unittest",
+        "dataclasses",
         "typing",
         "pytest",
         "jsonpath",
         "builtins",
         "_operator",
         "_pytest",
-        "_pytest.config",
-        "_pytest.fixtures",
         "_pytest.mark",
         "_pytest.mark.structures",
+        "_pytest.outcomes",
+        "_typeshed",
         "abc",
-        "jsonpath.env",
-        "jsonpath.path"
+        "io",
+        "json.decoder",
+        "os",
+        "unittest.case"
     ],
-    "hash": "d948449d48187c1ccccf9db45d37229a216aaac5e414bf81017b08b446b627f7",
-    "id": "tests.test_re",
+    "hash": "3c4f211a82a44baf8c96af03e568ac2fc9b60caedb32156bc3502465f20089d7",
+    "id": "tests.compliance",
     "ignore_all": false,
-    "interface_hash": "78da3161e9adaa77622576623696eb1eafa7c5c19d495433c3fd560e99d9b64a",
-    "mtime": 1680100269,
+    "interface_hash": "13cea6604cd7f8e6d223b73ea75f3a4dfba4f9fb134059d1b3a24a22ef0fdb4e",
+    "mtime": 1680769461,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -96,13 +105,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/test_re.py",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/compliance.py",
     "plugin_data": null,
-    "size": 1537,
+    "size": 1677,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/dev.data.json`

 * *Files 11% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8095703125%*

 * *Differences: {"'_fullname'": "'dev'",*

 * * "'names'": "{'__annotations__': {'node': {'fullname': 'dev.__annotations__'}, delete: "*

 * *            "['module_public']}, '__doc__': {'node': {'fullname': 'dev.__doc__'}, delete: "*

 * *            "['module_public']}, '__file__': {'node': {'fullname': 'dev.__file__'}, delete: "*

 * *            "['module_public']}, '__name__': {'node': {'fullname': 'dev.__name__'}, delete: "*

 * *            "['module_public']}, '__package__': {'node': {'fullname': 'dev.__package__'}, delete: "*

 * *            "['mod […]*

```diff
@@ -1,65 +1,24 @@
 {
     ".class": "MypyFile",
-    "_fullname": "tomli",
+    "_fullname": "dev",
     "future_import_flags": [],
     "is_partial_stub_package": false,
     "is_stub": false,
     "names": {
         ".class": "SymbolTable",
-        "TOMLDecodeError": {
-            ".class": "SymbolTableNode",
-            "cross_ref": "tomli._parser.TOMLDecodeError",
-            "kind": "Gdef"
-        },
-        "__all__": {
-            ".class": "SymbolTableNode",
-            "kind": "Gdef",
-            "module_public": false,
-            "node": {
-                ".class": "Var",
-                "flags": [
-                    "is_inferred",
-                    "has_explicit_value"
-                ],
-                "fullname": "tomli.__all__",
-                "name": "__all__",
-                "type": {
-                    ".class": "TupleType",
-                    "implicit": false,
-                    "items": [
-                        "builtins.str",
-                        "builtins.str",
-                        "builtins.str"
-                    ],
-                    "partial_fallback": {
-                        ".class": "Instance",
-                        "args": [
-                            {
-                                ".class": "AnyType",
-                                "missing_import_name": null,
-                                "source_any": null,
-                                "type_of_any": 6
-                            }
-                        ],
-                        "type_ref": "builtins.tuple"
-                    }
-                }
-            }
-        },
         "__annotations__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
-            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "tomli.__annotations__",
+                "fullname": "dev.__annotations__",
                 "name": "__annotations__",
                 "type": {
                     ".class": "Instance",
                     "args": [
                         "builtins.str",
                         {
                             ".class": "AnyType",
@@ -71,109 +30,114 @@
                     "type_ref": "builtins.dict"
                 }
             }
         },
         "__doc__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
-            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "tomli.__doc__",
+                "fullname": "dev.__doc__",
                 "name": "__doc__",
                 "type": "builtins.str"
             }
         },
         "__file__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
-            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "tomli.__file__",
+                "fullname": "dev.__file__",
                 "name": "__file__",
                 "type": "builtins.str"
             }
         },
         "__name__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
-            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "tomli.__name__",
+                "fullname": "dev.__name__",
                 "name": "__name__",
                 "type": "builtins.str"
             }
         },
         "__package__": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
-            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
                     "is_ready"
                 ],
-                "fullname": "tomli.__package__",
+                "fullname": "dev.__package__",
                 "name": "__package__",
                 "type": "builtins.str"
             }
         },
-        "__path__": {
+        "example_data": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
-            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
-                    "is_ready"
+                    "is_inferred",
+                    "has_explicit_value"
                 ],
-                "fullname": "tomli.__path__",
-                "name": "__path__",
+                "fullname": "dev.example_data",
+                "name": "example_data",
                 "type": {
                     ".class": "Instance",
                     "args": [
-                        "builtins.str"
+                        "builtins.str",
+                        "builtins.object"
                     ],
-                    "type_ref": "builtins.list"
+                    "type_ref": "builtins.dict"
                 }
             }
         },
-        "__version__": {
+        "json": {
+            ".class": "SymbolTableNode",
+            "cross_ref": "json",
+            "kind": "Gdef",
+            "module_hidden": true,
+            "module_public": false
+        },
+        "jsonpath": {
+            ".class": "SymbolTableNode",
+            "cross_ref": "jsonpath",
+            "kind": "Gdef",
+            "module_hidden": true,
+            "module_public": false
+        },
+        "products": {
             ".class": "SymbolTableNode",
             "kind": "Gdef",
-            "module_public": false,
             "node": {
                 ".class": "Var",
                 "flags": [
-                    "is_ready",
                     "is_inferred",
                     "has_explicit_value"
                 ],
-                "fullname": "tomli.__version__",
-                "name": "__version__",
-                "type": "builtins.str"
+                "fullname": "dev.products",
+                "name": "products",
+                "type": {
+                    ".class": "Instance",
+                    "args": [
+                        "builtins.object"
+                    ],
+                    "type_ref": "builtins.list"
+                }
             }
-        },
-        "load": {
-            ".class": "SymbolTableNode",
-            "cross_ref": "tomli._parser.load",
-            "kind": "Gdef"
-        },
-        "loads": {
-            ".class": "SymbolTableNode",
-            "cross_ref": "tomli._parser.loads",
-            "kind": "Gdef"
         }
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/tomli/__init__.py"
+    "path": "/home/james/projects/simply_json_path/simply-json-path/dev.py"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/_parser.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/_parser.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/_parser.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/__init__.meta.json`

 * *Files 11% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.697181964573269%*

 * *Differences: {"'data_mtime'": '1680278525',*

 * * "'dep_lines'": '{insert: [(0, 3), (2, 19), (4, 21), (5, 22), (6, 28), (7, 31)], delete: [11, 10, '*

 * *                '9, 8, 7, 6, 5, 4, 3, 0]}',*

 * * "'dep_prios'": '{insert: [(7, 5), (8, 10), (9, 5)], delete: [13, 12, 11, 10, 9, 8, 4]}',*

 * * "'dependencies'": "{insert: [(0, 'unittest.case'), (1, 'unittest.loader'), (2, 'unittest.main'), "*

 * *                   "(3, 'unittest.result'), (4, 'unittest.runner'), (5, 'unittest.signals'), (6, "*

 * *                   "'unittest.suite'), (7, 'unit […]*

```diff
@@ -1,71 +1,59 @@
 {
-    "data_mtime": 1680278526,
+    "data_mtime": 1680278525,
     "dep_lines": [
-        7,
+        3,
         12,
+        19,
         20,
-        5,
-        8,
-        9,
-        10,
-        1,
-        1,
-        1,
-        1,
-        1,
+        21,
+        22,
+        28,
+        31,
         1,
         1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
         5,
         5,
         5,
-        10,
         5,
         5,
         5,
-        30,
-        30,
-        30,
-        30,
-        30,
-        30,
+        5,
+        10,
+        5,
         30,
         30,
         30
     ],
     "dependencies": [
-        "collections.abc",
-        "tomli._re",
-        "tomli._types",
-        "__future__",
-        "string",
-        "types",
-        "typing",
+        "unittest.case",
+        "unittest.loader",
+        "unittest.main",
+        "unittest.result",
+        "unittest.runner",
+        "unittest.signals",
+        "unittest.suite",
+        "unittest.async_case",
+        "sys",
         "builtins",
         "_typeshed",
         "abc",
-        "array",
-        "ctypes",
-        "datetime",
-        "mmap",
-        "pickle",
-        "re",
-        "typing_extensions"
+        "typing"
     ],
-    "hash": "83df8435a00b4be07c768918a42bb35056a55a5a20ed3f922183232d9496aed3",
-    "id": "tomli._parser",
+    "hash": "dba2f84ec364f1cff90d8afc8c41c0b6815b451f2e1697c82b61c6bd75940b75",
+    "id": "unittest",
     "ignore_all": true,
-    "interface_hash": "4fe813d67b766911e29ff84c1f4d006db3fd0bfd70b2fff6044c256d77da5ff2",
-    "mtime": 1679496943,
+    "interface_hash": "2ea6f3a325c16de5d559b4a5bb228ecb34d024a52647fa3864a2e4c3ab011b03",
+    "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -99,13 +87,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/tomli/_parser.py",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unittest/__init__.pyi",
     "plugin_data": null,
-    "size": 22633,
+    "size": 1871,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/_re.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/_re.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/_re.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/result.meta.json`

 * *Files 9% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7260239651416122%*

 * *Differences: {"'dep_lines'": '{insert: [(1, 3), (3, 2), (4, 4)], delete: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(0, 10), (2, 20)], delete: [12, 11, 10, 9, 8, 7, 4, 1, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'unittest.case'), (1, 'collections.abc'), (2, 'unittest'), (3, "*

 * *                   "'_typeshed'), (7, 'types')], delete: [14, 13, 12, 11, 10, 9, 7, 4, 3, 2, 1, "*

 * *                   '0]}',*

 * * "'hash'": "'c3c84d157ab204cd3b00b3faf4d64cc85ad50fd622145a8032cde2378d31e767'",*

 * * "'id'": "'unittest.result […]*

```diff
@@ -1,65 +1,44 @@
 {
     "data_mtime": 1680278525,
     "dep_lines": [
-        12,
-        5,
-        7,
-        8,
-        9,
-        10,
-        1,
-        1,
-        1,
-        1,
         1,
+        3,
         1,
+        2,
+        4,
         1,
         1,
         1
     ],
     "dep_prios": [
+        10,
         5,
+        20,
         5,
         5,
         5,
-        10,
-        5,
-        5,
-        30,
-        30,
-        30,
-        30,
-        30,
-        30,
         30,
         30
     ],
     "dependencies": [
-        "tomli._types",
-        "__future__",
-        "datetime",
-        "functools",
-        "re",
+        "unittest.case",
+        "collections.abc",
+        "unittest",
+        "_typeshed",
         "typing",
         "builtins",
-        "_typeshed",
         "abc",
-        "array",
-        "ctypes",
-        "enum",
-        "mmap",
-        "pickle",
-        "typing_extensions"
+        "types"
     ],
-    "hash": "75b8e0e428594f6dca6bdcfd0c73977ddb52a4fc147dd80c5e78fc34ea25cbec",
-    "id": "tomli._re",
+    "hash": "c3c84d157ab204cd3b00b3faf4d64cc85ad50fd622145a8032cde2378d31e767",
+    "id": "unittest.result",
     "ignore_all": true,
-    "interface_hash": "9ad2e882ddd0ddd6fae258a78ddc646427ce9843c3461e25bde4108f94b00f9a",
-    "mtime": 1679496943,
+    "interface_hash": "2fa9c0b791f95f0c07fbe4a95d86a2d64b0848775c03b4559232f496fc27f3d9",
+    "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -93,13 +72,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/tomli/_re.py",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unittest/result.pyi",
     "plugin_data": null,
-    "size": 2943,
+    "size": 1721,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/_types.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/_types.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/tomli/_types.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tomli/_types.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/main.meta.json`

 * *Files 9% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7613748423345946%*

 * *Differences: {"'dep_lines'": '{insert: [(1, 2), (2, 3), (3, 4), (4, 5), (6, 6), (7, 7)], delete: [8, 7, 6, 5, '*

 * *                '4, 3, 2, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(0, 10), (1, 10), (2, 10), (3, 10), (5, 20)], delete: [11, 10, 8, 4, 3, '*

 * *                '2, 1, 0]}',*

 * * "'dependencies'": "{insert: [(4, 'collections.abc'), (5, 'unittest'), (6, 'types'), (7, "*

 * *                   "'typing')], delete: [12, 10, 8, 7, 5, 4, 2]}",*

 * * "'hash'": "'f150ef9438e591e3d629f0eefd7b3236c18528d8e0a103ed15774b156b554302'",*

 * * "'id'":  […]*

```diff
@@ -1,58 +1,49 @@
 {
     "data_mtime": 1680278525,
     "dep_lines": [
-        3,
-        12,
-        19,
-        20,
-        21,
-        22,
-        28,
-        31,
-        1,
         1,
+        2,
+        3,
+        4,
+        5,
         1,
+        6,
+        7,
         1,
         1
     ],
     "dep_prios": [
+        10,
+        10,
+        10,
+        10,
         5,
+        20,
         5,
         5,
         5,
-        5,
-        5,
-        5,
-        5,
-        10,
-        5,
-        30,
-        30,
         30
     ],
     "dependencies": [
         "unittest.case",
         "unittest.loader",
-        "unittest.main",
         "unittest.result",
-        "unittest.runner",
-        "unittest.signals",
         "unittest.suite",
-        "unittest.async_case",
-        "sys",
+        "collections.abc",
+        "unittest",
+        "types",
+        "typing",
         "builtins",
-        "_typeshed",
-        "abc",
-        "typing"
+        "abc"
     ],
-    "hash": "dba2f84ec364f1cff90d8afc8c41c0b6815b451f2e1697c82b61c6bd75940b75",
-    "id": "unittest",
+    "hash": "f150ef9438e591e3d629f0eefd7b3236c18528d8e0a103ed15774b156b554302",
+    "id": "unittest.main",
     "ignore_all": true,
-    "interface_hash": "2ea6f3a325c16de5d559b4a5bb228ecb34d024a52647fa3864a2e4c3ab011b03",
+    "interface_hash": "a62150bec07f45980dd67091a1254cc60f7ab89f9cc093460b35145a832d993f",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -87,13 +78,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unittest/__init__.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unittest/main.pyi",
     "plugin_data": null,
-    "size": 1871,
+    "size": 1544,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/_log.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/_log.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/_log.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/cyaml.meta.json`

 * *Files 10% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.698974358974359%*

 * *Differences: {"'data_mtime'": '1680012434',*

 * * "'dep_lines'": '{insert: [(1, 6), (2, 7), (3, 8), (4, 9), (5, 1)], delete: [5, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(4, 5), (5, 5), (6, 5), (7, 5), (8, 5)], delete: [6, 2, 1]}',*

 * * "'dependencies'": "{insert: [(0, 'collections.abc'), (1, 'yaml._yaml'), (2, 'yaml.constructor'), "*

 * *                   "(3, 'yaml.representer'), (4, 'yaml.resolver'), (5, '_typeshed'), (7, "*

 * *                   "'typing_extensions')], delete: [6, 3, 2, 1, 0]}",*

 * * "'hash'": "'ad9d86d1137af6866fc179232581e […]*

```diff
@@ -1,44 +1,50 @@
 {
-    "data_mtime": 1680278525,
+    "data_mtime": 1680012434,
     "dep_lines": [
-        5,
-        1,
         2,
+        6,
+        7,
+        8,
+        9,
+        1,
         3,
         4,
         1,
-        1,
         1
     ],
     "dep_prios": [
         5,
-        10,
-        10,
         5,
         5,
         5,
-        30,
+        5,
+        5,
+        5,
+        5,
+        5,
         30
     ],
     "dependencies": [
-        "unittest.case",
-        "logging",
-        "sys",
-        "types",
+        "collections.abc",
+        "yaml._yaml",
+        "yaml.constructor",
+        "yaml.representer",
+        "yaml.resolver",
+        "_typeshed",
         "typing",
+        "typing_extensions",
         "builtins",
-        "_typeshed",
         "abc"
     ],
-    "hash": "297a51a36613ffcd84bcef772c3f0dd0fdb57a1a9acc544a72840468647d968c",
-    "id": "unittest._log",
+    "hash": "ad9d86d1137af6866fc179232581e8308f32723a86a14607f4979b17438e00b8",
+    "id": "yaml.cyaml",
     "ignore_all": true,
-    "interface_hash": "f790fed9c5c66a487dd8d192db67e8fd7980e77d29df6657b41c33bacc94eb88",
-    "mtime": 1679496944,
+    "interface_hash": "43aefb4a7baad8fc40f3f61cfcb06ec367733dd6280ddb975179bf5a6ddcc111",
+    "mtime": 1680012426,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -72,13 +78,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unittest/_log.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/cyaml.pyi",
     "plugin_data": null,
-    "size": 892,
+    "size": 2715,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/async_case.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/async_case.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/async_case.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/sys.meta.json`

 * *Files 8% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7372222222222222%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 4), (1, 5), (3, 2), (5, 7), (6, 8), (7, 9), (8, 10)], delete: [5, '*

 * *                '4, 2, 0]}',*

 * * "'dep_prios'": '{insert: [(2, 5), (3, 5), (4, 5), (5, 5)], delete: [2]}',*

 * * "'dependencies'": "{insert: [(1, 'importlib.abc'), (2, 'importlib.machinery'), (3, '_typeshed'), "*

 * *                   "(4, 'builtins'), (5, 'io'), (6, 'types'), (10, 'importlib')], delete: [6, 5, "*

 * *                   '2, 1]}',*

 * * "'hash'": "'41b700a469a256dbdbd61fd54c34f7da58b4b […]*

```diff
@@ -1,43 +1,52 @@
 {
-    "data_mtime": 1680278525,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        2,
+        4,
+        5,
         6,
-        1,
+        2,
         3,
-        4,
-        1,
+        7,
+        8,
+        9,
+        10,
         1,
         1
     ],
     "dep_prios": [
         5,
         5,
-        10,
+        5,
+        5,
+        5,
+        5,
         5,
         5,
         5,
         30,
         30
     ],
     "dependencies": [
         "collections.abc",
-        "unittest.case",
-        "sys",
+        "importlib.abc",
+        "importlib.machinery",
+        "_typeshed",
+        "builtins",
+        "io",
+        "types",
         "typing",
         "typing_extensions",
-        "builtins",
-        "_typeshed",
-        "abc"
+        "abc",
+        "importlib"
     ],
-    "hash": "ef2aa50559010d3124e9f0003c17f9cd8b959f4c73d8157fe40ab0ba3c218808",
-    "id": "unittest.async_case",
+    "hash": "41b700a469a256dbdbd61fd54c34f7da58b4b2a5d2f59b8cbe26658fc8b53151",
+    "id": "sys",
     "ignore_all": true,
-    "interface_hash": "a3394397f94a7af47f9c92b60a2ab86ff45e5ef15a359b981e6e9367835e4e73",
+    "interface_hash": "dd60be164d6e830e52d78afa1d413846bd0954dbda40a73b294727bcc2d666e8",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -72,13 +81,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unittest/async_case.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/sys.pyi",
     "plugin_data": null,
-    "size": 663,
+    "size": 11286,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/case.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/case.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/case.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/case.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/loader.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/loader.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/loader.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/loader.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/main.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/main.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/main.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/suite.meta.json`

 * *Files 11% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7924242424242425%*

 * *Differences: {"'dep_lines'": '{insert: [(3, 1)], delete: [7, 6, 4]}',*

 * * "'dep_prios'": '{insert: [(6, 30)], delete: [6, 1, 0]}',*

 * * "'dependencies'": "{insert: [(4, 'typing_extensions'), (7, 'typing')], delete: [7, 6, 3, 1]}",*

 * * "'hash'": "'bfe23ef3990add1fa9e7e02d9f2f25fc599af4bb020dba5f216d90c2f6667c80'",*

 * * "'id'": "'unittest.suite'",*

 * * "'interface_hash'": "'bc4d97e3ca864182b1ee45d8f8963b69677b7406440b932c52d2a6c15ccfa067'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib […]*

```diff
@@ -1,49 +1,43 @@
 {
     "data_mtime": 1680278525,
     "dep_lines": [
         1,
         2,
         3,
+        1,
         4,
-        5,
         1,
-        6,
-        7,
         1,
         1
     ],
     "dep_prios": [
         10,
         10,
-        10,
-        10,
         5,
         20,
         5,
         5,
-        5,
+        30,
         30
     ],
     "dependencies": [
         "unittest.case",
-        "unittest.loader",
         "unittest.result",
-        "unittest.suite",
         "collections.abc",
         "unittest",
-        "types",
-        "typing",
+        "typing_extensions",
         "builtins",
-        "abc"
+        "abc",
+        "typing"
     ],
-    "hash": "f150ef9438e591e3d629f0eefd7b3236c18528d8e0a103ed15774b156b554302",
-    "id": "unittest.main",
+    "hash": "bfe23ef3990add1fa9e7e02d9f2f25fc599af4bb020dba5f216d90c2f6667c80",
+    "id": "unittest.suite",
     "ignore_all": true,
-    "interface_hash": "a62150bec07f45980dd67091a1254cc60f7ab89f9cc093460b35145a832d993f",
+    "interface_hash": "bc4d97e3ca864182b1ee45d8f8963b69677b7406440b932c52d2a6c15ccfa067",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -78,13 +72,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unittest/main.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unittest/suite.pyi",
     "plugin_data": null,
-    "size": 1544,
+    "size": 984,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/result.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/result.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/result.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/importlib/abc.meta.json`

 * *Files 10% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.729010989010989%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 12), (1, 13), (4, 3), (5, 11), (6, 14), (7, 15), (8, 16)], delete: '*

 * *                '[6, 5, 4, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(0, 5), (1, 5), (2, 10), (8, 5), (9, 5)], delete: [7, 6, 2]}',*

 * * "'dependencies'": "{insert: [(1, 'importlib.machinery'), (2, 'sys'), (3, 'types'), (5, 'abc'), "*

 * *                   "(6, 'io'), (8, 'typing_extensions')], delete: [7, 6, 2, 0]}",*

 * * "'hash'": "'ad8ba0ae1c679f2e613913ca173b46b1a8660c6c8175a482b1c24de042d5c2 […]*

```diff
@@ -1,43 +1,49 @@
 {
-    "data_mtime": 1680278525,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        1,
-        3,
+        12,
+        13,
         1,
         2,
-        4,
-        1,
-        1,
+        3,
+        11,
+        14,
+        15,
+        16,
         1
     ],
     "dep_prios": [
+        5,
+        5,
+        10,
         10,
         5,
-        20,
         5,
         5,
         5,
-        30,
-        30
+        5,
+        5
     ],
     "dependencies": [
-        "unittest.case",
         "collections.abc",
-        "unittest",
+        "importlib.machinery",
+        "sys",
+        "types",
         "_typeshed",
-        "typing",
-        "builtins",
         "abc",
-        "types"
+        "io",
+        "typing",
+        "typing_extensions",
+        "builtins"
     ],
-    "hash": "c3c84d157ab204cd3b00b3faf4d64cc85ad50fd622145a8032cde2378d31e767",
-    "id": "unittest.result",
+    "hash": "ad8ba0ae1c679f2e613913ca173b46b1a8660c6c8175a482b1c24de042d5c2f4",
+    "id": "importlib.abc",
     "ignore_all": true,
-    "interface_hash": "2fa9c0b791f95f0c07fbe4a95d86a2d64b0848775c03b4559232f496fc27f3d9",
+    "interface_hash": "d720407de67d430cd5edc64555205895bc074be2bc58ef43ce87c0770e0ca390",
     "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -72,13 +78,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unittest/result.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/importlib/abc.pyi",
     "plugin_data": null,
-    "size": 1721,
+    "size": 7295,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/runner.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/runner.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/runner.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/events.meta.json`

 * *Files 13% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7%*

 * *Differences: {"'data_mtime'": '1680012434',*

 * * "'dep_lines'": '{delete: [6, 5, 3, 2, 1, 0]}',*

 * * "'dep_prios'": '{delete: [5, 4, 3, 2, 1, 0]}',*

 * * "'dependencies'": '{delete: [6, 4, 3, 2, 1, 0]}',*

 * * "'hash'": "'dba8a1ce79649700cf4ddcf4a40e435b40087b706d48b03da18c50d782359b2a'",*

 * * "'id'": "'yaml.events'",*

 * * "'interface_hash'": "'4ce3a3df568d78cdb1e2e8e0c4851bcebb0a0e7ca72e7875f2737ad0cd662073'",*

 * * "'mtime'": '1680012426',*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.1 […]*

```diff
@@ -1,47 +1,29 @@
 {
-    "data_mtime": 1680278525,
+    "data_mtime": 1680012434,
     "dep_lines": [
         1,
-        2,
-        3,
-        4,
-        1,
-        5,
-        6,
         1,
         1
     ],
     "dep_prios": [
-        10,
-        10,
-        10,
-        5,
-        20,
-        5,
         5,
         5,
         30
     ],
     "dependencies": [
-        "unittest.case",
-        "unittest.result",
-        "unittest.suite",
-        "collections.abc",
-        "unittest",
         "typing",
-        "typing_extensions",
         "builtins",
         "abc"
     ],
-    "hash": "38357da7850b668627503d574cb0e5545a449f460bfbb9e8d6325f3820e0aeef",
-    "id": "unittest.runner",
+    "hash": "dba8a1ce79649700cf4ddcf4a40e435b40087b706d48b03da18c50d782359b2a",
+    "id": "yaml.events",
     "ignore_all": true,
-    "interface_hash": "4bb129d47b0249602c7932bde716715a821cb0f7faa751c16af9efdfed6f5cc3",
-    "mtime": 1679496944,
+    "interface_hash": "4ce3a3df568d78cdb1e2e8e0c4851bcebb0a0e7ca72e7875f2737ad0cd662073",
+    "mtime": 1680012426,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -75,13 +57,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unittest/runner.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/events.pyi",
     "plugin_data": null,
-    "size": 1353,
+    "size": 1683,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/signals.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/signals.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/signals.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/signals.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/suite.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/unittest/suite.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/unittest/suite.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/serializer.meta.json`

 * *Files 11% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7083754208754208%*

 * *Differences: {"'data_mtime'": '1680012434',*

 * * "'dep_lines'": '{delete: [3, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(3, 5)], delete: [6, 3, 1, 0]}',*

 * * "'dependencies'": "{insert: [(0, 'yaml.error'), (1, 'yaml.nodes'), (2, 'typing')], delete: [7, 4, "*

 * *                   '3, 2, 1, 0]}',*

 * * "'hash'": "'91f9c1fb22ce4363c11f764c27eaa5c47d72c293d1bb79a3f59c07660dda2f9f'",*

 * * "'id'": "'yaml.serializer'",*

 * * "'interface_hash'": "'3f008e3cbedf2fbce69406b2e6443fcbeffca2029aa0585effa4e407df180544'",*

 * * "'mtime'": '1680012426',*

 * * "'path'": "'/home […]*

```diff
@@ -1,44 +1,35 @@
 {
-    "data_mtime": 1680278525,
+    "data_mtime": 1680012434,
     "dep_lines": [
-        1,
-        2,
         3,
-        1,
         4,
         1,
         1,
         1
     ],
     "dep_prios": [
-        10,
-        10,
         5,
-        20,
         5,
         5,
-        30,
+        5,
         30
     ],
     "dependencies": [
-        "unittest.case",
-        "unittest.result",
-        "collections.abc",
-        "unittest",
-        "typing_extensions",
+        "yaml.error",
+        "yaml.nodes",
+        "typing",
         "builtins",
-        "abc",
-        "typing"
+        "abc"
     ],
-    "hash": "bfe23ef3990add1fa9e7e02d9f2f25fc599af4bb020dba5f216d90c2f6667c80",
-    "id": "unittest.suite",
+    "hash": "91f9c1fb22ce4363c11f764c27eaa5c47d72c293d1bb79a3f59c07660dda2f9f",
+    "id": "yaml.serializer",
     "ignore_all": true,
-    "interface_hash": "bc4d97e3ca864182b1ee45d8f8963b69677b7406440b932c52d2a6c15ccfa067",
-    "mtime": 1679496944,
+    "interface_hash": "3f008e3cbedf2fbce69406b2e6443fcbeffca2029aa0585effa4e407df180544",
+    "mtime": 1680012426,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -72,13 +63,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/unittest/suite.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/serializer.pyi",
     "plugin_data": null,
-    "size": 984,
+    "size": 729,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/urllib/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/urllib/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/urllib/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/urllib/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/urllib/parse.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/urllib/parse.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/urllib/parse.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/loader.meta.json`

 * *Files 12% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7103846153846154%*

 * *Differences: {"'data_mtime'": '1680012434',*

 * * "'dep_lines'": '{insert: [(2, 5), (3, 6), (5, 8), (6, 1), (7, 1)], delete: [1, 0]}',*

 * * "'dep_prios'": '{insert: [(1, 5), (2, 5), (3, 5), (8, 30)], delete: [1]}',*

 * * "'dependencies'": "{insert: [(0, 'yaml.composer'), (1, 'yaml.constructor'), (2, 'yaml.parser'), "*

 * *                   "(3, 'yaml.reader'), (4, 'yaml.resolver'), (5, 'yaml.scanner'), (10, "*

 * *                   "'typing')], delete: [4, 2, 1, 0]}",*

 * * "'hash'": "'95cb90a55f354b187357e7018932065982b024cf0fb4e6815aa23127be8f8 […]*

```diff
@@ -1,44 +1,53 @@
 {
-    "data_mtime": 1680278525,
+    "data_mtime": 1680012434,
     "dep_lines": [
-        2,
-        1,
         3,
         4,
+        5,
+        6,
         7,
+        8,
+        1,
+        1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
-        10,
         5,
         5,
         5,
         5,
+        5,
+        5,
+        5,
+        30,
         30,
         30
     ],
     "dependencies": [
-        "collections.abc",
-        "sys",
-        "typing",
+        "yaml.composer",
+        "yaml.constructor",
+        "yaml.parser",
+        "yaml.reader",
+        "yaml.resolver",
+        "yaml.scanner",
         "typing_extensions",
-        "types",
         "builtins",
         "_typeshed",
-        "abc"
+        "abc",
+        "typing"
     ],
-    "hash": "c63b9b79f7fc54b266cad001ebf899091051353c61578cd27445312e0553b969",
-    "id": "urllib.parse",
+    "hash": "95cb90a55f354b187357e7018932065982b024cf0fb4e6815aa23127be8f82d2",
+    "id": "yaml.loader",
     "ignore_all": true,
-    "interface_hash": "0821d0c5abfa0147f9ab49034b5abe71d40e92be08730c5871847440c633fef6",
-    "mtime": 1679496944,
+    "interface_hash": "3d3dad4698b67d88c3547e7835fb05500f17b7ed17fb250047666b1c517f7add",
+    "mtime": 1680012426,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -72,13 +81,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/urllib/parse.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/loader.pyi",
     "plugin_data": null,
-    "size": 7050,
+    "size": 1151,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/__init__.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/__init__.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/__init__.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/__init__.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/_yaml.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/_yaml.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/_yaml.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/_yaml.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/composer.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/composer.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/composer.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/composer.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/constructor.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/constructor.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/constructor.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/constructor.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/cyaml.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/cyaml.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/cyaml.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/representer.meta.json`

 * *Files 15% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7721350762527234%*

 * *Differences: {"'dep_lines'": '{insert: [(0, 3), (4, 2), (6, 5), (7, 1), (8, 1), (9, 1), (10, 1)], delete: [6, '*

 * *                '4, 1, 0]}',*

 * * "'dep_prios'": '{insert: [(3, 10), (8, 30), (9, 30), (10, 30), (11, 30)], delete: [1, 0]}',*

 * * "'dependencies'": "{insert: [(1, 'yaml.error'), (2, 'yaml.nodes'), (3, 'datetime'), (5, 'types'), "*

 * *                   "(9, 'array'), (10, 'ctypes'), (11, 'mmap'), (12, 'pickle')], delete: [7, 4, 3, "*

 * *                   '2, 1]}',*

 * * "'hash'": "'c4288565c56b1af404c4a2561387397d1a4e0c3cbeff8d3 […]*

```diff
@@ -1,49 +1,58 @@
 {
     "data_mtime": 1680012434,
     "dep_lines": [
-        2,
-        6,
+        3,
         7,
         8,
-        9,
         1,
-        3,
+        2,
         4,
+        5,
+        1,
+        1,
+        1,
+        1,
         1,
         1
     ],
     "dep_prios": [
         5,
         5,
         5,
+        10,
         5,
         5,
         5,
         5,
-        5,
-        5,
+        30,
+        30,
+        30,
+        30,
         30
     ],
     "dependencies": [
         "collections.abc",
-        "yaml._yaml",
-        "yaml.constructor",
-        "yaml.representer",
-        "yaml.resolver",
+        "yaml.error",
+        "yaml.nodes",
+        "datetime",
         "_typeshed",
+        "types",
         "typing",
-        "typing_extensions",
         "builtins",
-        "abc"
+        "abc",
+        "array",
+        "ctypes",
+        "mmap",
+        "pickle"
     ],
-    "hash": "ad9d86d1137af6866fc179232581e8308f32723a86a14607f4979b17438e00b8",
-    "id": "yaml.cyaml",
+    "hash": "c4288565c56b1af404c4a2561387397d1a4e0c3cbeff8d3ad9c33e5222b5d7aa",
+    "id": "yaml.representer",
     "ignore_all": true,
-    "interface_hash": "43aefb4a7baad8fc40f3f61cfcb06ec367733dd6280ddb975179bf5a6ddcc111",
+    "interface_hash": "979c8936641d489fc2be75110df6749a01273c74441afcfe3b052668ee9ef2dd",
     "mtime": 1680012426,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -78,13 +87,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/cyaml.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/representer.pyi",
     "plugin_data": null,
-    "size": 2715,
+    "size": 3363,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/dumper.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/dumper.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/dumper.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/dumper.meta.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/emitter.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/emitter.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/emitter.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/abc.meta.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.6976190476190477%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 4), (2, 2), (3, 5), (4, 6)], delete: [1, 0]}',*

 * * "'dep_prios'": '{insert: [(2, 10), (4, 5), (5, 5)], delete: [3]}',*

 * * "'dependencies'": "{insert: [(0, 'collections.abc'), (1, '_typeshed'), (2, 'sys'), (4, "*

 * *                   "'typing_extensions')], delete: [3, 0]}",*

 * * "'hash'": "'a3b9c6522f0a6d3e6e4cd8febae992da12d43e37176bb3fb0909533463a529b2'",*

 * * "'id'": "'abc'",*

 * * "'interface_hash'": "'7b25b3291456b223ffbb9d4e140059673b6ec6d95b74352cd0c19a5751d1c3 […]*

```diff
@@ -1,32 +1,38 @@
 {
-    "data_mtime": 1680012434,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        3,
-        1,
+        4,
         1,
+        2,
+        5,
+        6,
         1
     ],
     "dep_prios": [
         5,
         5,
+        10,
+        5,
         5,
-        30
+        5
     ],
     "dependencies": [
-        "yaml.error",
+        "collections.abc",
+        "_typeshed",
+        "sys",
         "typing",
-        "builtins",
-        "abc"
+        "typing_extensions",
+        "builtins"
     ],
-    "hash": "36c66ff5726e098a36c4b005e415a6977e6c98e5c8ee49dc6cf04afe85b0ab3f",
-    "id": "yaml.emitter",
+    "hash": "a3b9c6522f0a6d3e6e4cd8febae992da12d43e37176bb3fb0909533463a529b2",
+    "id": "abc",
     "ignore_all": true,
-    "interface_hash": "2ab4289f40584fc887864664c785a9791ad4a2f6a66ca64ede9039061537b941",
-    "mtime": 1680012426,
+    "interface_hash": "7b25b3291456b223ffbb9d4e140059673b6ec6d95b74352cd0c19a5751d1c3f2",
+    "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -60,13 +66,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/emitter.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/abc.pyi",
     "plugin_data": null,
-    "size": 4141,
+    "size": 1770,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/error.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/error.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/error.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/scanner.meta.json`

 * *Files 14% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.785%*

 * *Differences: {"'dep_lines'": '{insert: [(0, 3)]}',*

 * * "'dep_prios'": '{insert: [(1, 5), (2, 5)], delete: [1]}',*

 * * "'dependencies'": "{insert: [(0, 'yaml.error'), (1, 'typing')], delete: [2]}",*

 * * "'hash'": "'2f2d76a0f63225536b74e0c133e17d7553b51332b7862888b4c81acb48434001'",*

 * * "'id'": "'yaml.scanner'",*

 * * "'interface_hash'": "'29b730ad26a15ee1c280ce7a074a9cce2758a6dbacf57ce2be5b9971ecbdb85a'",*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs […]*

```diff
@@ -1,28 +1,31 @@
 {
     "data_mtime": 1680012434,
     "dep_lines": [
+        3,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
-        30,
+        5,
+        5,
         30
     ],
     "dependencies": [
+        "yaml.error",
+        "typing",
         "builtins",
-        "abc",
-        "typing"
+        "abc"
     ],
-    "hash": "941a31ff4b8c7774905ca62dff8018605f6f18a20c021da72f93746e04270d68",
-    "id": "yaml.error",
+    "hash": "2f2d76a0f63225536b74e0c133e17d7553b51332b7862888b4c81acb48434001",
+    "id": "yaml.scanner",
     "ignore_all": true,
-    "interface_hash": "061f95064df216e8470d9bfe7bdfaa2abec17641b45e6fb5c0f7490188be016f",
+    "interface_hash": "29b730ad26a15ee1c280ce7a074a9cce2758a6dbacf57ce2be5b9971ecbdb85a",
     "mtime": 1680012426,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
@@ -57,13 +60,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/error.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/scanner.pyi",
     "plugin_data": null,
-    "size": 749,
+    "size": 3573,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/events.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/events.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/events.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/dataclasses.meta.json`

 * *Files 12% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.6911111111111111%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 6), (2, 2), (3, 3), (4, 4), (5, 5), (6, 7), (7, 8)], delete: [0]}',*

 * * "'dep_prios'": '{insert: [(0, 5), (1, 10), (2, 10), (3, 5), (4, 5), (5, 5)]}',*

 * * "'dependencies'": "{insert: [(0, 'collections.abc'), (1, 'enum'), (2, 'sys'), (3, 'types'), (4, "*

 * *                   "'_typeshed'), (6, 'typing'), (7, 'typing_extensions')], delete: [0]}",*

 * * "'hash'": "'ffd75c9498e57a272219ee18fced3f082acfead1fef3a594524c2b81076bb215'",*

 * * "'id'": "'dataclasses'",*

 * * "'in […]*

```diff
@@ -1,29 +1,47 @@
 {
-    "data_mtime": 1680012434,
+    "data_mtime": 1680779143,
     "dep_lines": [
+        6,
         1,
-        1,
+        2,
+        3,
+        4,
+        5,
+        7,
+        8,
         1
     ],
     "dep_prios": [
         5,
+        10,
+        10,
+        5,
+        5,
+        5,
+        5,
         5,
         30
     ],
     "dependencies": [
-        "typing",
+        "collections.abc",
+        "enum",
+        "sys",
+        "types",
+        "_typeshed",
         "builtins",
+        "typing",
+        "typing_extensions",
         "abc"
     ],
-    "hash": "dba8a1ce79649700cf4ddcf4a40e435b40087b706d48b03da18c50d782359b2a",
-    "id": "yaml.events",
+    "hash": "ffd75c9498e57a272219ee18fced3f082acfead1fef3a594524c2b81076bb215",
+    "id": "dataclasses",
     "ignore_all": true,
-    "interface_hash": "4ce3a3df568d78cdb1e2e8e0c4851bcebb0a0e7ca72e7875f2737ad0cd662073",
-    "mtime": 1680012426,
+    "interface_hash": "5b8dd43c6269dbf1094b7e8b564145e866fd03e7468954393c99148b059ddf68",
+    "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -57,13 +75,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/events.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/dataclasses.pyi",
     "plugin_data": null,
-    "size": 1683,
+    "size": 8816,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/loader.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/loader.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/loader.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/email/message.meta.json`

 * *Files 22% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7177350427350427%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 1), (5, 2)], delete: [8, 7, 6]}',*

 * * "'dep_prios'": '{insert: [(8, 5)], delete: [9, 8]}',*

 * * "'dependencies'": "{insert: [(0, 'collections.abc'), (1, 'email.charset'), (2, "*

 * *                   "'email.contentmanager'), (3, 'email.errors'), (4, 'email.policy'), (5, "*

 * *                   "'email'), (6, 'typing')], delete: [10, 8, 5, 4, 3, 2, 1, 0]}",*

 * * "'hash'": "'6e0993b354bdf6bbe105b3598646b27a62851aead468c8a871eb4c4baef5ed2f'",*

 * * "'id'": "'email.messag […]*

```diff
@@ -1,53 +1,50 @@
 {
-    "data_mtime": 1680012434,
+    "data_mtime": 1680779143,
     "dep_lines": [
+        1,
         3,
         4,
         5,
         6,
+        2,
         7,
         8,
         1,
-        1,
-        1,
-        1,
         1
     ],
     "dep_prios": [
         5,
         5,
         5,
         5,
         5,
         5,
         5,
         5,
-        30,
-        30,
+        5,
         30
     ],
     "dependencies": [
-        "yaml.composer",
-        "yaml.constructor",
-        "yaml.parser",
-        "yaml.reader",
-        "yaml.resolver",
-        "yaml.scanner",
+        "collections.abc",
+        "email.charset",
+        "email.contentmanager",
+        "email.errors",
+        "email.policy",
+        "email",
+        "typing",
         "typing_extensions",
         "builtins",
-        "_typeshed",
-        "abc",
-        "typing"
+        "abc"
     ],
-    "hash": "95cb90a55f354b187357e7018932065982b024cf0fb4e6815aa23127be8f82d2",
-    "id": "yaml.loader",
+    "hash": "6e0993b354bdf6bbe105b3598646b27a62851aead468c8a871eb4c4baef5ed2f",
+    "id": "email.message",
     "ignore_all": true,
-    "interface_hash": "3d3dad4698b67d88c3547e7835fb05500f17b7ed17fb250047666b1c517f7add",
-    "mtime": 1680012426,
+    "interface_hash": "6f33c8af615df82d6630b720bcf459b7f138ed1bc6f7714c0e1421370ea76f01",
+    "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -81,13 +78,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/loader.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/email/message.pyi",
     "plugin_data": null,
-    "size": 1151,
+    "size": 6091,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/nodes.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/nodes.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/nodes.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/_ctypes.meta.json`

 * *Files 13% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7121693121693121%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 1), (1, 2), (3, 1)]}',*

 * * "'dep_prios'": '{insert: [(0, 10), (4, 30), (5, 30)]}',*

 * * "'dependencies'": "{insert: [(0, 'sys'), (1, 'ctypes'), (2, 'typing_extensions'), (4, "*

 * *                   "'_typeshed'), (6, 'typing')], delete: [1, 0]}",*

 * * "'hash'": "'f3f569576a38ac44f7351d80826ca0da2673c3895b9278a10d671615e6388fc9'",*

 * * "'id'": "'_ctypes'",*

 * * "'interface_hash'": "'a73ffbaace30e4490abd6ee944ca165a73ced1f43d6dbf8606cea4c57eed0181'",*

 * * "'mtime'": '167949 […]*

```diff
@@ -1,32 +1,41 @@
 {
-    "data_mtime": 1680012434,
+    "data_mtime": 1680779143,
     "dep_lines": [
+        1,
+        2,
         3,
         1,
         1,
+        1,
         1
     ],
     "dep_prios": [
+        10,
         5,
         5,
         5,
+        30,
+        30,
         30
     ],
     "dependencies": [
-        "yaml.error",
-        "typing",
+        "sys",
+        "ctypes",
+        "typing_extensions",
         "builtins",
-        "abc"
+        "_typeshed",
+        "abc",
+        "typing"
     ],
-    "hash": "8fb0614d7b5894afcac04e11665310348b914a2e197ff395c3504b786ef37d64",
-    "id": "yaml.nodes",
+    "hash": "f3f569576a38ac44f7351d80826ca0da2673c3895b9278a10d671615e6388fc9",
+    "id": "_ctypes",
     "ignore_all": true,
-    "interface_hash": "8455f9774f8649c16be751cad0b31d65f4c406ee8b554a982855ef44ba92bfb4",
-    "mtime": 1680012426,
+    "interface_hash": "a73ffbaace30e4490abd6ee944ca165a73ced1f43d6dbf8606cea4c57eed0181",
+    "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -60,13 +69,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/nodes.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/_ctypes.pyi",
     "plugin_data": null,
-    "size": 1032,
+    "size": 829,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/parser.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/parser.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/parser.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/selectors.meta.json`

 * *Files 13% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.6845860566448801%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 6), (1, 18), (2, 19), (3, 22), (4, 23), (5, 24), (6, 2), (7, 4), '*

 * *                '(8, 8), (9, 9), (10, 1), (11, 1), (12, 1)], delete: [0]}',*

 * * "'dep_prios'": '{insert: [(0, 5), (1, 5), (2, 5), (3, 25), (4, 25), (5, 25), (6, 5), (7, 5), (11, '*

 * *                '30), (12, 30), (13, 30), (14, 30)]}',*

 * * "'dependencies'": "{insert: [(0, 'collections.abc'), (1, 'jsonpath.exceptions'), (2, "*

 * *                   "'jsonpath.match'), (3, 'jsonpath.env'), (4, […]*

```diff
@@ -1,32 +1,68 @@
 {
-    "data_mtime": 1680012434,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        3,
+        6,
+        18,
+        19,
+        22,
+        23,
+        24,
+        2,
+        4,
+        8,
+        9,
+        1,
+        1,
+        1,
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
         5,
         5,
+        25,
+        25,
+        25,
+        5,
+        5,
+        5,
+        5,
+        5,
+        30,
+        30,
+        30,
+        30,
         30
     ],
     "dependencies": [
-        "yaml.error",
+        "collections.abc",
+        "jsonpath.exceptions",
+        "jsonpath.match",
+        "jsonpath.env",
+        "jsonpath.filter",
+        "jsonpath.token",
+        "__future__",
+        "abc",
+        "contextlib",
         "typing",
         "builtins",
-        "abc"
+        "array",
+        "ctypes",
+        "mmap",
+        "pickle",
+        "types"
     ],
-    "hash": "84278dd07d81544ddf4cc836dc52802455df327cd4a68dc98f4ad2eb3c46c1e9",
-    "id": "yaml.parser",
+    "hash": "3bab46b462dd682862f4d35aaec60d6983d20449a2094a5d9f5a728df87e2ca0",
+    "id": "jsonpath.selectors",
     "ignore_all": true,
-    "interface_hash": "9a2c1f1e122d45c02a095f316762080131022bede90cb48b0b2e8fdd58b90eb3",
-    "mtime": 1680012426,
+    "interface_hash": "122b216d07667890df21168cd598eb98af118d6205187f7caa611793963b0579",
+    "mtime": 1680778690,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -60,13 +96,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/parser.pyi",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/selectors.py",
     "plugin_data": null,
-    "size": 1672,
+    "size": 21397,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/reader.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/reader.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/reader.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/array.meta.json`

 * *Files 14% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7129292929292929%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(0, 3), (3, 6), (4, 7), (5, 1), (6, 1), (7, 1)], delete: [3, 0]}',*

 * * "'dep_prios'": '{insert: [(1, 10), (6, 30), (7, 30), (8, 30)]}',*

 * * "'dependencies'": "{insert: [(0, 'collections.abc'), (1, 'sys'), (7, 'ctypes'), (8, 'mmap'), (9, "*

 * *                   "'pickle')], delete: [0]}",*

 * * "'hash'": "'d0ad5e13f4193b236ba4ba6fea5d43bd8795d6f09b3a27b8ef2cfbb1b1e2d993'",*

 * * "'id'": "'array'",*

 * * "'interface_hash'": "'a779d356ced53b8f7703ad2eb1b6a91189882f4150adf2db87 […]*

```diff
@@ -1,38 +1,50 @@
 {
-    "data_mtime": 1680012434,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        5,
+        3,
         1,
         2,
-        3,
+        6,
+        7,
+        1,
+        1,
+        1,
         1,
         1
     ],
     "dep_prios": [
         5,
+        10,
         5,
         5,
         5,
         5,
+        30,
+        30,
+        30,
         30
     ],
     "dependencies": [
-        "yaml.error",
+        "collections.abc",
+        "sys",
         "_typeshed",
         "typing",
         "typing_extensions",
         "builtins",
-        "abc"
+        "abc",
+        "ctypes",
+        "mmap",
+        "pickle"
     ],
-    "hash": "89f882e9d50aa4e9b7226e9fcbe22a26fba214fbcabd2cdf2770e6626a360983",
-    "id": "yaml.reader",
+    "hash": "d0ad5e13f4193b236ba4ba6fea5d43bd8795d6f09b3a27b8ef2cfbb1b1e2d993",
+    "id": "array",
     "ignore_all": true,
-    "interface_hash": "dc37223836df446e4c816e40b9813ed5a5c34f9391e3a63f2dd0c122ee4ba754",
-    "mtime": 1680012426,
+    "interface_hash": "a779d356ced53b8f7703ad2eb1b6a91189882f4150adf2db87bec1cf423e8343",
+    "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -66,13 +78,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/reader.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/array.pyi",
     "plugin_data": null,
-    "size": 1038,
+    "size": 3679,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/representer.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/representer.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/resolver.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/resolver.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/resolver.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/tests/consensus.meta.json`

 * *Files 27% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.6503508771929825%*

 * *Differences: {"'data_mtime'": '1680543239',*

 * * "'dep_lines'": '{insert: [(0, 11), (1, 12), (2, 13), (3, 14), (4, 22), (5, 23), (6, 25), (7, 1), '*

 * *                '(8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1)], delete: '*

 * *                '[0]}',*

 * * "'dep_prios'": '{insert: [(0, 10), (1, 10), (2, 5), (4, 10), (6, 10), (8, 30), (9, 30), (10, 30), '*

 * *                '(11, 30), (12, 30), (13, 30), (14, 30), (15, 30), (16, 30), (17, 30)]}',*

 * * "'dependencies'": "{insert: [(0, 'operator'), (1, 'unittest'), (2,  […]*

```diff
@@ -1,32 +1,77 @@
 {
-    "data_mtime": 1680012434,
+    "data_mtime": 1680543239,
     "dep_lines": [
-        3,
+        11,
+        12,
+        13,
+        14,
+        22,
+        23,
+        25,
+        1,
+        1,
+        1,
+        1,
+        1,
+        1,
+        1,
+        1,
+        1,
         1,
         1,
         1
     ],
     "dep_prios": [
+        10,
+        10,
+        5,
         5,
+        10,
         5,
+        10,
         5,
+        30,
+        30,
+        30,
+        30,
+        30,
+        30,
+        30,
+        30,
+        30,
+        30,
         30
     ],
     "dependencies": [
-        "yaml.error",
+        "operator",
+        "unittest",
+        "dataclasses",
         "typing",
+        "pytest",
+        "yaml",
+        "jsonpath",
         "builtins",
-        "abc"
+        "_collections_abc",
+        "_operator",
+        "_pytest",
+        "_pytest.mark",
+        "_pytest.mark.structures",
+        "_pytest.outcomes",
+        "_typeshed",
+        "abc",
+        "io",
+        "os",
+        "unittest.case"
     ],
-    "hash": "6ff3245b99546e2d2707eb2d24702846303b100ada1a698bb1a7c14fd387e738",
-    "id": "yaml.resolver",
-    "ignore_all": true,
-    "interface_hash": "105e16a344e082e452f9af00235921431d09c5841ca21b6839dfffc3354cceac",
-    "mtime": 1680012426,
+    "hash": "4c225ea3a24793d45324c37a9b7a20b912f5562e50be2c5adb4a2f157a0645dc",
+    "id": "tests.consensus",
+    "ignore_all": false,
+    "interface_hash": "19afc16497dd87468936db5d25b95be86c9e2e9822e8f3b4678e8981092ec569",
+    "mtime": 1680777260,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -60,13 +105,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/resolver.pyi",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/tests/consensus.py",
     "plugin_data": null,
-    "size": 787,
+    "size": 2329,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/scanner.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/scanner.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/scanner.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/json/decoder.meta.json`

 * *Files 18% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.74%*

 * *Differences: {"'data_mtime'": '1680779143',*

 * * "'dep_lines'": '{insert: [(1, 2)], delete: [0]}',*

 * * "'dependencies'": "{insert: [(0, 'collections.abc')], delete: [0]}",*

 * * "'hash'": "'5dd5349e16128655996d25e9c4676c82eaed3374bf9740bd98360257d4df6a29'",*

 * * "'id'": "'json.decoder'",*

 * * "'interface_hash'": "'fac81736281b7d1750d3212e9e738c89432738e50c50b42dc19c75f0a5cd345a'",*

 * * "'mtime'": '1679496944',*

 * * "'path'": "'/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/type […]*

```diff
@@ -1,32 +1,32 @@
 {
-    "data_mtime": 1680012434,
+    "data_mtime": 1680779143,
     "dep_lines": [
-        3,
         1,
+        2,
         1,
         1
     ],
     "dep_prios": [
         5,
         5,
         5,
         30
     ],
     "dependencies": [
-        "yaml.error",
+        "collections.abc",
         "typing",
         "builtins",
         "abc"
     ],
-    "hash": "2f2d76a0f63225536b74e0c133e17d7553b51332b7862888b4c81acb48434001",
-    "id": "yaml.scanner",
+    "hash": "5dd5349e16128655996d25e9c4676c82eaed3374bf9740bd98360257d4df6a29",
+    "id": "json.decoder",
     "ignore_all": true,
-    "interface_hash": "29b730ad26a15ee1c280ce7a074a9cce2758a6dbacf57ce2be5b9971ecbdb85a",
-    "mtime": 1680012426,
+    "interface_hash": "fac81736281b7d1750d3212e9e738c89432738e50c50b42dc19c75f0a5cd345a",
+    "mtime": 1679496944,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -60,13 +60,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/scanner.pyi",
+    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/mypy/typeshed/stdlib/json/decoder.pyi",
     "plugin_data": null,
-    "size": 3573,
+    "size": 1117,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/serializer.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/serializer.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/tokens.data.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/yaml/tokens.data.json`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.mypy_cache/3.10/yaml/tokens.meta.json` & `python_jsonpath-0.4.0/.mypy_cache/3.10/jsonpath/__about__.meta.json`

 * *Files 25% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.7%*

 * *Differences: {"'data_mtime'": '1680785785',*

 * * "'dep_prios'": '{insert: [(1, 30)], delete: [0]}',*

 * * "'dependencies'": "{insert: [(2, 'typing')], delete: [0]}",*

 * * "'hash'": "'290a4f4bd1e747caab67b168a5e644fda120511577acc6924741656fb96f5cae'",*

 * * "'id'": "'jsonpath.__about__'",*

 * * "'ignore_all'": 'False',*

 * * "'interface_hash'": "'f90142b97cf2ff94d7ecbc2e11ad3d707003ae2a730b8811ff45471dbc44961c'",*

 * * "'mtime'": '1680785788',*

 * * "'path'": "'/home/james/projects/simply_json_path/simply-json-path/jsonpath/__about__.py'",*

 * * "'size'": '132'}*

```diff
@@ -1,29 +1,29 @@
 {
-    "data_mtime": 1680012434,
+    "data_mtime": 1680785785,
     "dep_lines": [
         1,
         1,
         1
     ],
     "dep_prios": [
         5,
-        5,
+        30,
         30
     ],
     "dependencies": [
-        "typing",
         "builtins",
-        "abc"
+        "abc",
+        "typing"
     ],
-    "hash": "9595fb62da4dff11a0bdcac9955779c3c78d1e09616ed809b69d9cdd5036330b",
-    "id": "yaml.tokens",
-    "ignore_all": true,
-    "interface_hash": "13eebf5e863f594f7841c4d34ff4acbecf37765bf9b34d24a4dfea98c2e01de6",
-    "mtime": 1680012426,
+    "hash": "290a4f4bd1e747caab67b168a5e644fda120511577acc6924741656fb96f5cae",
+    "id": "jsonpath.__about__",
+    "ignore_all": false,
+    "interface_hash": "f90142b97cf2ff94d7ecbc2e11ad3d707003ae2a730b8811ff45471dbc44961c",
+    "mtime": 1680785788,
     "options": {
         "allow_redefinition": false,
         "allow_untyped_globals": false,
         "always_false": [],
         "always_true": [],
         "bazel": false,
         "check_untyped_defs": true,
@@ -57,13 +57,13 @@
         "strict_equality": true,
         "strict_optional": true,
         "warn_no_return": true,
         "warn_return_any": true,
         "warn_unreachable": true,
         "warn_unused_ignores": false
     },
-    "path": "/home/james/.local/share/hatch/env/virtual/python-jsonpath/d-SoupV5/python-jsonpath/lib/python3.10/site-packages/yaml-stubs/tokens.pyi",
+    "path": "/home/james/projects/simply_json_path/simply-json-path/jsonpath/__about__.py",
     "plugin_data": null,
-    "size": 1796,
+    "size": 132,
     "suppressed": [],
     "version_id": "1.1.1"
 }
```

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/113169384d5668bc` & `python_jsonpath-0.4.0/.ruff_cache/content/113169384d5668bc`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/135ad1453038c1a4` & `python_jsonpath-0.4.0/.ruff_cache/content/135ad1453038c1a4`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/1398303151225940` & `python_jsonpath-0.4.0/.ruff_cache/content/1398303151225940`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/146653dc356f145a` & `python_jsonpath-0.4.0/.ruff_cache/content/146653dc356f145a`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/15a3b5713a8c7860` & `python_jsonpath-0.4.0/.ruff_cache/content/15a3b5713a8c7860`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/1627d49e057ce6ef` & `python_jsonpath-0.4.0/.ruff_cache/content/1627d49e057ce6ef`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/1acf71e60d0cb21f` & `python_jsonpath-0.4.0/.ruff_cache/content/1acf71e60d0cb21f`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/1f12aa22fe2f769c` & `python_jsonpath-0.4.0/.ruff_cache/content/1f12aa22fe2f769c`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/1f3b04ff651c8c80` & `python_jsonpath-0.4.0/.ruff_cache/content/1f3b04ff651c8c80`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/213493565c60d69e` & `python_jsonpath-0.4.0/.ruff_cache/content/213493565c60d69e`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/253e03a0e43afe2` & `python_jsonpath-0.4.0/.ruff_cache/content/253e03a0e43afe2`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/26a981bb502f16f` & `python_jsonpath-0.4.0/.ruff_cache/content/26a981bb502f16f`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/279262a136b9c91b` & `python_jsonpath-0.4.0/.ruff_cache/content/279262a136b9c91b`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/28b9e8854f3bba14` & `python_jsonpath-0.4.0/.ruff_cache/content/28b9e8854f3bba14`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/2b1ae2f56430e88e` & `python_jsonpath-0.4.0/.ruff_cache/content/2b1ae2f56430e88e`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/2b9fda870d662d61` & `python_jsonpath-0.4.0/.ruff_cache/content/2b9fda870d662d61`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/2ea0f9311fceda9f` & `python_jsonpath-0.4.0/.ruff_cache/content/2ea0f9311fceda9f`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/2f7a4bad2663cc7a` & `python_jsonpath-0.4.0/.ruff_cache/content/2f7a4bad2663cc7a`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/2f7a9dea88b592c6` & `python_jsonpath-0.4.0/.ruff_cache/content/2f7a9dea88b592c6`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/3064bcb187e4005b` & `python_jsonpath-0.4.0/.ruff_cache/content/3064bcb187e4005b`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/325e27582ba6b00b` & `python_jsonpath-0.4.0/.ruff_cache/content/325e27582ba6b00b`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/3278cae1025f408d` & `python_jsonpath-0.4.0/.ruff_cache/content/3278cae1025f408d`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/35570cbe6251c078` & `python_jsonpath-0.4.0/.ruff_cache/content/35570cbe6251c078`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/35acb2ea313c1f4f` & `python_jsonpath-0.4.0/.ruff_cache/content/35acb2ea313c1f4f`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/492ebdc8ce6d7aaa` & `python_jsonpath-0.4.0/.ruff_cache/content/492ebdc8ce6d7aaa`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/4c10a12091591533` & `python_jsonpath-0.4.0/.ruff_cache/content/4c10a12091591533`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/501fd54946953b5c` & `python_jsonpath-0.4.0/.ruff_cache/content/501fd54946953b5c`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/510acc3260e58d67` & `python_jsonpath-0.4.0/.ruff_cache/content/510acc3260e58d67`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/51a39a4ab0b9e5a` & `python_jsonpath-0.4.0/.ruff_cache/content/51a39a4ab0b9e5a`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/582fc01eaccf9d11` & `python_jsonpath-0.4.0/.ruff_cache/content/582fc01eaccf9d11`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/5f8db1660501e234` & `python_jsonpath-0.4.0/.ruff_cache/content/5f8db1660501e234`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/6164c8374827eb66` & `python_jsonpath-0.4.0/.ruff_cache/content/6164c8374827eb66`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/6576547c7f4694be` & `python_jsonpath-0.4.0/.ruff_cache/content/6576547c7f4694be`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/682188a646d78c0` & `python_jsonpath-0.4.0/.ruff_cache/content/682188a646d78c0`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/695170c6d345cb58` & `python_jsonpath-0.4.0/.ruff_cache/content/695170c6d345cb58`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/6c8242c16814d970` & `python_jsonpath-0.4.0/.ruff_cache/content/6c8242c16814d970`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/6e342654a00b5817` & `python_jsonpath-0.4.0/.ruff_cache/content/6e342654a00b5817`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/6fb452c5ea33322` & `python_jsonpath-0.4.0/.ruff_cache/content/6fb452c5ea33322`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/71373ffe75246f00` & `python_jsonpath-0.4.0/.ruff_cache/content/71373ffe75246f00`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/715499bd1eb26466` & `python_jsonpath-0.4.0/.ruff_cache/content/715499bd1eb26466`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/72499df899c54a45` & `python_jsonpath-0.4.0/.ruff_cache/content/72499df899c54a45`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/7281991b04dc372b` & `python_jsonpath-0.4.0/.ruff_cache/content/7281991b04dc372b`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/7861f5cb2966565a` & `python_jsonpath-0.4.0/.ruff_cache/content/7861f5cb2966565a`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/79d8b31a7196e404` & `python_jsonpath-0.4.0/.ruff_cache/content/79d8b31a7196e404`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/7abafe920dd77a92` & `python_jsonpath-0.4.0/.ruff_cache/content/7abafe920dd77a92`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/7bbfd8c3690b5a75` & `python_jsonpath-0.4.0/.ruff_cache/content/7bbfd8c3690b5a75`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/7d958009b81b0dd7` & `python_jsonpath-0.4.0/.ruff_cache/content/7d958009b81b0dd7`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/7e39743b5037bb34` & `python_jsonpath-0.4.0/.ruff_cache/content/7e39743b5037bb34`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/80e739b3e52c2ee9` & `python_jsonpath-0.4.0/.ruff_cache/content/80e739b3e52c2ee9`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/8377c8be88accd28` & `python_jsonpath-0.4.0/.ruff_cache/content/8377c8be88accd28`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/857ff98531f4bd4a` & `python_jsonpath-0.4.0/.ruff_cache/content/857ff98531f4bd4a`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/8880e918cb120ec7` & `python_jsonpath-0.4.0/.ruff_cache/content/8880e918cb120ec7`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/88b37c139c075c2c` & `python_jsonpath-0.4.0/.ruff_cache/content/88b37c139c075c2c`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/8a5fbc233bbd1ad6` & `python_jsonpath-0.4.0/.ruff_cache/content/8a5fbc233bbd1ad6`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/8fff743c3d8501f3` & `python_jsonpath-0.4.0/.ruff_cache/content/8fff743c3d8501f3`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/950808b1e26775ec` & `python_jsonpath-0.4.0/.ruff_cache/content/950808b1e26775ec`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/95267216d1d74c9` & `python_jsonpath-0.4.0/.ruff_cache/content/95267216d1d74c9`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/9564ef73b0f0b9bd` & `python_jsonpath-0.4.0/.ruff_cache/content/9564ef73b0f0b9bd`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/986b503a8f13eaa` & `python_jsonpath-0.4.0/.ruff_cache/content/986b503a8f13eaa`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/9dfd1a4c1d6c5611` & `python_jsonpath-0.4.0/.ruff_cache/content/9dfd1a4c1d6c5611`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/9f86a234993ab90f` & `python_jsonpath-0.4.0/.ruff_cache/content/9f86a234993ab90f`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/a09ca4d68f7f7a6d` & `python_jsonpath-0.4.0/.ruff_cache/content/a09ca4d68f7f7a6d`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/a296e558a05a4446` & `python_jsonpath-0.4.0/.ruff_cache/content/a296e558a05a4446`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/a3930f42fc0d5727` & `python_jsonpath-0.4.0/.ruff_cache/content/a3930f42fc0d5727`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/aa737b2f5fb8e71d` & `python_jsonpath-0.4.0/.ruff_cache/content/aa737b2f5fb8e71d`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/ac31423108a9860` & `python_jsonpath-0.4.0/.ruff_cache/content/ac31423108a9860`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/adfdc55c283c3c0f` & `python_jsonpath-0.4.0/.ruff_cache/content/adfdc55c283c3c0f`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/ae81d3744b93d310` & `python_jsonpath-0.4.0/.ruff_cache/content/ae81d3744b93d310`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/b2c510e6d789bae1` & `python_jsonpath-0.4.0/.ruff_cache/content/b2c510e6d789bae1`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/b34b2d8198704c68` & `python_jsonpath-0.4.0/.ruff_cache/content/b34b2d8198704c68`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/b69b1ed3056953ee` & `python_jsonpath-0.4.0/.ruff_cache/content/b69b1ed3056953ee`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/b72ce555d5fa6a8e` & `python_jsonpath-0.4.0/.ruff_cache/content/b72ce555d5fa6a8e`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/b925dc8a594b869a` & `python_jsonpath-0.4.0/.ruff_cache/content/b925dc8a594b869a`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/bfaa6c8b09ea7082` & `python_jsonpath-0.4.0/.ruff_cache/content/bfaa6c8b09ea7082`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/bfeb6ff39293ca1d` & `python_jsonpath-0.4.0/.ruff_cache/content/bfeb6ff39293ca1d`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/c467bf0cef9b03ab` & `python_jsonpath-0.4.0/.ruff_cache/content/c467bf0cef9b03ab`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/c8959c42754024d` & `python_jsonpath-0.4.0/.ruff_cache/content/c8959c42754024d`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/cd4f7faa7a866ead` & `python_jsonpath-0.4.0/.ruff_cache/content/cd4f7faa7a866ead`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/ce1f45bc791cd4ab` & `python_jsonpath-0.4.0/.ruff_cache/content/ce1f45bc791cd4ab`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/cfe8a804b0d1388d` & `python_jsonpath-0.4.0/.ruff_cache/content/cfe8a804b0d1388d`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/d17b1a6a05c0a1a` & `python_jsonpath-0.4.0/.ruff_cache/content/d17b1a6a05c0a1a`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/d42b3f28fcca5b92` & `python_jsonpath-0.4.0/.ruff_cache/content/d42b3f28fcca5b92`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/d5ff022c78ca8bdb` & `python_jsonpath-0.4.0/.ruff_cache/content/d5ff022c78ca8bdb`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/d698a764e2eee095` & `python_jsonpath-0.4.0/.ruff_cache/content/d698a764e2eee095`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/da69e5397a61483b` & `python_jsonpath-0.4.0/.ruff_cache/content/da69e5397a61483b`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/dafc0b9cca5a6ec0` & `python_jsonpath-0.4.0/.ruff_cache/content/dafc0b9cca5a6ec0`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/dff7ac6c8a6da66c` & `python_jsonpath-0.4.0/.ruff_cache/content/dff7ac6c8a6da66c`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/e4058c4aa5da08b2` & `python_jsonpath-0.4.0/.ruff_cache/content/e4058c4aa5da08b2`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/e656067c10d75580` & `python_jsonpath-0.4.0/.ruff_cache/content/e656067c10d75580`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/e8bd3b3a333c4df1` & `python_jsonpath-0.4.0/.ruff_cache/content/e8bd3b3a333c4df1`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/e985bcee084c8ec0` & `python_jsonpath-0.4.0/.ruff_cache/content/e985bcee084c8ec0`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/e9b4fe44bf585a4f` & `python_jsonpath-0.4.0/.ruff_cache/content/e9b4fe44bf585a4f`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/eaefa94a9823b2f1` & `python_jsonpath-0.4.0/.ruff_cache/content/eaefa94a9823b2f1`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/eb3d0304cfb9339f` & `python_jsonpath-0.4.0/.ruff_cache/content/eb3d0304cfb9339f`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/ec4d305e85bb4e19` & `python_jsonpath-0.4.0/.ruff_cache/content/ec4d305e85bb4e19`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/ee2d09ff4551420d` & `python_jsonpath-0.4.0/.ruff_cache/content/ee2d09ff4551420d`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/f041520f880369c3` & `python_jsonpath-0.4.0/.ruff_cache/content/f041520f880369c3`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/f22550a5656ee20f` & `python_jsonpath-0.4.0/.ruff_cache/content/f22550a5656ee20f`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/f27f3c06aa306cb3` & `python_jsonpath-0.4.0/.ruff_cache/content/f27f3c06aa306cb3`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/f387f65a58ab496e` & `python_jsonpath-0.4.0/.ruff_cache/content/f387f65a58ab496e`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/f48e1807643594f1` & `python_jsonpath-0.4.0/.ruff_cache/content/f48e1807643594f1`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/fa02e62e08abbadb` & `python_jsonpath-0.4.0/.ruff_cache/content/fa02e62e08abbadb`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/.ruff_cache/content/fa5ccd5562187a1b` & `python_jsonpath-0.4.0/.ruff_cache/content/fa5ccd5562187a1b`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/docs/index.md` & `python_jsonpath-0.4.0/docs/index.md`

 * *Files 12% similar despite different names*

```diff
@@ -97,10 +97,10 @@
     products = jsonpath.findall("$..products.*", fd)
 
 print(products)
 ```
 
 ## Next Steps
 
-Have a read through the [Quick Start](quickstart.md) and [High Level API Reference](api.md).
+Have a read through the [Quick Start](quickstart.md) and [High Level API Reference](api.md), or the default [JSONPath Syntax](syntax.md) supported by Python JSONPath.
 
 If you're interested in customizing JSONPath, take a look at [Advanced Usage](advanced.md) and the [Low Level API Reference](custom_api.md).
```

### Comparing `python_jsonpath-0.3.0/docs/css/style.css` & `python_jsonpath-0.4.0/docs/css/style.css`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/jsonpath/__init__.py` & `python_jsonpath-0.4.0/jsonpath/__init__.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/jsonpath/env.py` & `python_jsonpath-0.4.0/jsonpath/env.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/jsonpath/exceptions.py` & `python_jsonpath-0.4.0/jsonpath/exceptions.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/jsonpath/filter.py` & `python_jsonpath-0.4.0/jsonpath/filter.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,11 @@
 """Filter expression nodes."""
 from __future__ import annotations
 
+import json
 import re
 from abc import ABC
 from abc import abstractmethod
 from typing import TYPE_CHECKING
 from typing import Generic
 from typing import List
 from typing import Mapping
@@ -258,33 +259,23 @@
             and self.operator == other.operator
             and self.right == other.right
         )
 
     def evaluate(self, context: FilterContext) -> bool:
         if isinstance(self.left, Undefined) and isinstance(self.right, Undefined):
             return True
-
         left = self.left.evaluate(context)
         right = self.right.evaluate(context)
-
-        if left is UNDEFINED and right is UNDEFINED:
-            return False
-
         return context.env.compare(left, self.operator, right)
 
     async def evaluate_async(self, context: FilterContext) -> bool:
         if isinstance(self.left, Undefined) and isinstance(self.right, Undefined):
             return True
-
         left = await self.left.evaluate_async(context)
         right = await self.right.evaluate_async(context)
-
-        if left is UNDEFINED and right is UNDEFINED:
-            return False
-
         return context.env.compare(left, self.operator, right)
 
 
 class BooleanExpression(FilterExpression):
     """An expression that always evaluates to `True` or `False`."""
 
     __slots__ = ("expression",)
@@ -324,28 +315,36 @@
 
     def evaluate(self, context: FilterContext) -> object:
         if not isinstance(context.current, (Sequence, Mapping)):
             if self.path.empty():
                 return UNDEFINED
             return context.current
 
-        matches = self.path.findall(context.current)
+        try:
+            matches = self.path.findall(context.current)
+        except json.JSONDecodeError:
+            return UNDEFINED
+
         if not matches:
             return UNDEFINED
         if len(matches) == 1:
             return matches[0]
         return matches
 
     async def evaluate_async(self, context: FilterContext) -> object:
         if not isinstance(context.current, (Sequence, Mapping)):
             if self.path.empty():
                 return UNDEFINED
             return context.current
 
-        matches = await self.path.findall_async(context.current)
+        try:
+            matches = await self.path.findall_async(context.current)
+        except json.JSONDecodeError:
+            return UNDEFINED
+
         if not matches:
             return UNDEFINED
         if len(matches) == 1:
             return matches[0]
         return matches
```

### Comparing `python_jsonpath-0.3.0/jsonpath/lex.py` & `python_jsonpath-0.4.0/jsonpath/lex.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/jsonpath/match.py` & `python_jsonpath-0.4.0/jsonpath/match.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/jsonpath/parse.py` & `python_jsonpath-0.4.0/jsonpath/parse.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/jsonpath/path.py` & `python_jsonpath-0.4.0/jsonpath/path.py`

 * *Files 2% similar despite different names*

```diff
@@ -72,14 +72,15 @@
 
         Raises:
             JSONPathSyntaxError: If the path is invalid.
             JSONPathTypeError: If a filter expression attempts to use types in
                 an incompatible way.
         """
         if isinstance(data, str):
+            # TODO: catch JSONDecodeError?
             _data = json.loads(data)
         elif isinstance(data, TextIO):
             _data = json.loads(data.read())
         else:
             _data = data
         return [
             match.obj for match in self.finditer(_data, filter_context=filter_context)
@@ -136,14 +137,15 @@
         self,
         data: Union[str, TextIO, Sequence[Any], Mapping[str, Any]],
         *,
         filter_context: Optional[FilterContextVars] = None,
     ) -> List[object]:
         """An async version of `findall()`."""
         if isinstance(data, str):
+            # TODO: catch JSONDecodeError
             _data = json.loads(data)
         elif isinstance(data, TextIO):
             _data = json.loads(data.read())
         else:
             _data = data
         return [
             match.obj
```

### Comparing `python_jsonpath-0.3.0/jsonpath/selectors.py` & `python_jsonpath-0.4.0/jsonpath/selectors.py`

 * *Files 2% similar despite different names*

```diff
@@ -443,30 +443,42 @@
     ) -> None:
         super().__init__(env=env, token=token)
         self.expression = expression
 
     def __str__(self) -> str:
         return f"[?({self.expression})]"
 
-    def resolve(self, matches: Iterable[JSONPathMatch]) -> Iterable[JSONPathMatch]:
+    def resolve(  # noqa: PLR0912
+        self, matches: Iterable[JSONPathMatch]
+    ) -> Iterable[JSONPathMatch]:
         for match in matches:
             if isinstance(match.obj, Mapping):
-                context = FilterContext(
-                    env=self.env,
-                    current=match.obj,
-                    root=match.root,
-                    extra_context=match.filter_context(),
-                )
-                try:
-                    if self.expression.evaluate(context):
-                        yield match
-                except JSONPathTypeError as err:
-                    if not err.token:
-                        err.token = self.token
-                    raise
+                for key, val in match.obj.items():
+                    context = FilterContext(
+                        env=self.env,
+                        current=val,
+                        root=match.root,
+                        extra_context=match.filter_context(),
+                    )
+                    try:
+                        if self.expression.evaluate(context):
+                            _match = JSONPathMatch(
+                                filter_context=match.filter_context(),
+                                obj=val,
+                                parent=match,
+                                parts=match.parts + (key,),
+                                path=match.path + f"['{key}']",
+                                root=match.root,
+                            )
+                            match.add_child(_match)
+                            yield _match
+                    except JSONPathTypeError as err:
+                        if not err.token:
+                            err.token = self.token
+                        raise
 
             elif isinstance(match.obj, Sequence) and not isinstance(match.obj, str):
                 for i, obj in enumerate(match.obj):
                     context = FilterContext(
                         env=self.env,
                         current=obj,
                         root=match.root,
@@ -485,58 +497,72 @@
                             match.add_child(_match)
                             yield _match
                     except JSONPathTypeError as err:
                         if not err.token:
                             err.token = self.token
                         raise
 
-    async def resolve_async(
+    async def resolve_async(  # noqa: PLR0912
         self, matches: AsyncIterable[JSONPathMatch]
     ) -> AsyncIterable[JSONPathMatch]:
         async for match in matches:
             if isinstance(match.obj, Mapping):
-                context = FilterContext(
-                    env=self.env,
-                    current=match.obj,
-                    root=match.root,
-                    extra_context=match.filter_context(),
-                )
-
-                try:
-                    if await self.expression.evaluate_async(context):
-                        yield match
-                except JSONPathTypeError as err:
-                    if not err.token:
-                        err.token = self.token
-                    raise
+                for key, val in match.obj.items():
+                    context = FilterContext(
+                        env=self.env,
+                        current=val,
+                        root=match.root,
+                        extra_context=match.filter_context(),
+                    )
+
+                    try:
+                        result = await self.expression.evaluate_async(context)
+                    except JSONPathTypeError as err:
+                        if not err.token:
+                            err.token = self.token
+                        raise
+
+                    if result:
+                        _match = JSONPathMatch(
+                            filter_context=match.filter_context(),
+                            obj=val,
+                            parent=match,
+                            parts=match.parts + (key,),
+                            path=match.path + f"['{key}']",
+                            root=match.root,
+                        )
+                        match.add_child(_match)
+                        yield _match
 
             elif isinstance(match.obj, Sequence) and not isinstance(match.obj, str):
                 for i, obj in enumerate(match.obj):
                     context = FilterContext(
                         env=self.env,
                         current=obj,
                         root=match.root,
                         extra_context=match.filter_context(),
                     )
+
                     try:
-                        if await self.expression.evaluate_async(context):
-                            _match = JSONPathMatch(
-                                filter_context=match.filter_context(),
-                                obj=obj,
-                                parent=match,
-                                parts=match.parts + (i,),
-                                path=f"{match.path}[{i}]",
-                                root=match.root,
-                            )
-                            match.add_child(_match)
-                            yield _match
+                        result = await self.expression.evaluate_async(context)
                     except JSONPathTypeError as err:
                         if not err.token:
                             err.token = self.token
                         raise
+                    if result:
+                        _match = JSONPathMatch(
+                            filter_context=match.filter_context(),
+                            obj=obj,
+                            parent=match,
+                            parts=match.parts + (i,),
+                            path=f"{match.path}[{i}]",
+                            root=match.root,
+                        )
+                        match.add_child(_match)
+                        yield _match
 
 
 class FilterContext:
     """A filter expression context."""
 
     __slots__ = ("current", "env", "root", "extra_context")
```

### Comparing `python_jsonpath-0.3.0/jsonpath/stream.py` & `python_jsonpath-0.4.0/jsonpath/stream.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/jsonpath/token.py` & `python_jsonpath-0.4.0/jsonpath/token.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/tests/compliance.py` & `python_jsonpath-0.4.0/tests/compliance.py`

 * *Files 15% similar despite different names*

```diff
@@ -41,27 +41,17 @@
 def cases() -> List[Case]:
     with open("cts.json", encoding="utf8") as fd:
         data = json.load(fd)
     return [Case(**case) for case in data["tests"]]
 
 
 def valid_cases() -> List[Case]:
-    def mangle_filter(case: Case) -> Case:
-        # XXX: Insert wildcard in front of root :(
-        if (
-            case.name.startswith("filter")
-            and case.selector.startswith("$[?")
-            and isinstance(case.document, list)
-        ):
-            case.selector = case.selector.replace("$[?", "$.*[?")
-        return case
-
     # TODO: skipping filter functions. Not supported.
     return [
-        mangle_filter(case)
+        case
         for case in cases()
         if not case.invalid_selector and "function" not in case.name
     ]
 
 
 @pytest.mark.parametrize("case", valid_cases(), ids=operator.attrgetter("name"))
 def test_compliance(case: Case) -> None:
```

### Comparing `python_jsonpath-0.3.0/tests/consensus.py` & `python_jsonpath-0.4.0/tests/consensus.py`

 * *Files 24% similar despite different names*

```diff
@@ -43,19 +43,14 @@
     "scalar-consensus": "scalar_consensus",
 }
 
 SKIP = {
     "bracket_notation_with_number_on_object": "Bad consensus",
     "bracket_notation_with_number_on_string": "Invalid document",
     "dot_notation_with_number_-1": "Unexpected token",
-    "filter_expression_with_equals_on_object_with_key_matching_query": "Bad consensus",
-    (
-        "filter_expression_with_value_after_"
-        "dot_notation_with_wildcard_on_array_of_objects"
-    ): "Bad consensus",
 }
 
 
 def clean_query(query: Dict[str, Any]) -> Dict[str, Any]:
     # Replace hyphens with underscores in dict names.
     for old, new in RENAME_MAP.items():
         if old in query:
```

### Comparing `python_jsonpath-0.3.0/tests/test_async.py` & `python_jsonpath-0.4.0/tests/test_async.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/tests/test_compare.py` & `python_jsonpath-0.4.0/tests/test_compare.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/tests/test_concrete_path.py` & `python_jsonpath-0.4.0/tests/test_concrete_path.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/tests/test_env.py` & `python_jsonpath-0.4.0/tests/test_env.py`

 * *Files 2% similar despite different names*

```diff
@@ -24,15 +24,15 @@
     assert rv == [1]
 
 
 def test_find_all_with_extra_filter_context(env: JSONPathEnvironment) -> None:
     """Test that we can pass extra filter context to findall."""
     rv = env.findall(
         "$[?(@.some == #.other)]",
-        {"some": 1, "thing": 2},
+        {"foo": {"some": 1, "thing": 2}},
         filter_context={"other": 1},
     )
     assert rv == [{"some": 1, "thing": 2}]
 
 
 def test_find_iter_from_object(env: JSONPathEnvironment) -> None:
     """Test that we can pass a Python object to finditer."""
@@ -46,15 +46,15 @@
     assert [match.obj for match in matches] == [1]
 
 
 def test_find_iter_with_extra_filter_context(env: JSONPathEnvironment) -> None:
     """Test that we can pass extra filter context to finditer."""
     matches = env.finditer(
         "$[?(@.some == #.other)]",
-        {"some": 1, "thing": 2},
+        {"foo": {"some": 1, "thing": 2}},
         filter_context={"other": 1},
     )
     assert [match.obj for match in matches] == [{"some": 1, "thing": 2}]
 
 
 def test_find_all_async_from_object(env: JSONPathEnvironment) -> None:
     """Test that we can pass a Python object to findall_async."""
@@ -76,15 +76,15 @@
 
 def test_find_all_async_with_extra_filter_context(env: JSONPathEnvironment) -> None:
     """Test that we can pass extra filter context to findall_async."""
 
     async def coro() -> List[object]:
         return await env.findall_async(
             "$[?(@.some == #.other)]",
-            {"some": 1, "thing": 2},
+            {"foo": {"some": 1, "thing": 2}},
             filter_context={"other": 1},
         )
 
     assert asyncio.run(coro()) == [{"some": 1, "thing": 2}]
 
 
 def test_find_iter_async_from_object(env: JSONPathEnvironment) -> None:
@@ -109,13 +109,13 @@
 
 def test_find_iter_async_with_extra_filter_context(env: JSONPathEnvironment) -> None:
     """Test that we can pass extra filter context to finditer."""
 
     async def coro() -> List[object]:
         matches = await env.finditer_async(
             "$[?(@.some == #.other)]",
-            {"some": 1, "thing": 2},
+            {"foo": {"some": 1, "thing": 2}},
             filter_context={"other": 1},
         )
         return [match.obj async for match in matches]
 
     assert asyncio.run(coro()) == [{"some": 1, "thing": 2}]
```

### Comparing `python_jsonpath-0.3.0/tests/test_errors.py` & `python_jsonpath-0.4.0/tests/test_errors.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/tests/test_find.py` & `python_jsonpath-0.4.0/tests/test_find.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/tests/test_find_compound_path.py` & `python_jsonpath-0.4.0/tests/test_find_compound_path.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/tests/test_find_reference.py` & `python_jsonpath-0.4.0/tests/test_find_reference.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/tests/test_ietf.py` & `python_jsonpath-0.4.0/tests/test_ietf.py`

 * *Files 1% similar despite different names*

```diff
@@ -153,23 +153,23 @@
     ),
     Case(
         description="filter selector - Array value existence",
         path="$.a[?(@.b)]",
         data=FILTER_SELECTOR_DATA,
         want=[{"b": "j"}, {"b": "k"}, {"b": {}}, {"b": "kilo"}],
     ),
-    # Case(
-    #     description="filter selector - Existence of non-singular queries",
-    #     path="$[?(@.*)]",
-    #     data=FILTER_SELECTOR_DATA,
-    #     want=[
-    #         [3, 5, 1, 2, 4, 6, {"b": "j"}, {"b": "k"}, {"b": {}}, {"b": "kilo"}],
-    #         {"p": 1, "q": 2, "r": 3, "s": 5, "t": {"u": 6}},
-    #     ],
-    # ),
+    Case(
+        description="filter selector - Existence of non-singular queries",
+        path="$[?(@.*)]",
+        data=FILTER_SELECTOR_DATA,
+        want=[
+            [3, 5, 1, 2, 4, 6, {"b": "j"}, {"b": "k"}, {"b": {}}, {"b": "kilo"}],
+            {"p": 1, "q": 2, "r": 3, "s": 5, "t": {"u": 6}},
+        ],
+    ),
     # Case(
     #     description="filter selector - Nested filters",
     #     path="$[?(@[?(@.b)])]	",
     #     data=FILTER_SELECTOR_DATA,
     #     want=[[3, 5, 1, 2, 4, 6, {"b": "j"}, {"b": "k"}, {"b": {}}, {"b": "kilo"}]],
     # ),
     Case(
@@ -186,32 +186,32 @@
     # ),
     # Case(
     #     description="filter selector - Array value regular expression search",
     #     path='$.a[?search(@.b, "[jk]")]',
     #     data=FILTER_SELECTOR_DATA,
     #     want=[{"b": "j"}, {"b": "k"}, {"b": "kilo"}],
     # ),
-    # Case(
-    #     description="filter selector - Object value logical AND",
-    #     path="$.o[?(@>1 && @<4)]",
-    #     data=FILTER_SELECTOR_DATA,
-    #     want=[2, 3],
-    # ),
-    # Case(
-    #     description="filter selector - Object value logical OR",
-    #     path="$.o[?(@.u || @.x)]",
-    #     data=FILTER_SELECTOR_DATA,
-    #     want=[{"u": 6}],
-    # ),
-    # Case(
-    #     description="filter selector - Comparison of queries with no values",
-    #     path="$.a[?(@.b == $.x)]",
-    #     data=FILTER_SELECTOR_DATA,
-    #     want=[3, 5, 1, 2, 4, 6],
-    # ),
+    Case(
+        description="filter selector - Object value logical AND",
+        path="$.o[?(@>1 && @<4)]",
+        data=FILTER_SELECTOR_DATA,
+        want=[2, 3],
+    ),
+    Case(
+        description="filter selector - Object value logical OR",
+        path="$.o[?(@.u || @.x)]",
+        data=FILTER_SELECTOR_DATA,
+        want=[{"u": 6}],
+    ),
+    Case(
+        description="filter selector - Comparison of queries with no values",
+        path="$.a[?(@.b == $.x)]",
+        data=FILTER_SELECTOR_DATA,
+        want=[3, 5, 1, 2, 4, 6],
+    ),
     Case(
         description=(
             "filter selector - Comparisons of primitive and of structured values"
         ),
         path="$.a[?(@ == @)]",
         data=FILTER_SELECTOR_DATA,
         want=[3, 5, 1, 2, 4, 6, {"b": "j"}, {"b": "k"}, {"b": {}}, {"b": "kilo"}],
```

### Comparing `python_jsonpath-0.3.0/tests/test_ietf_comparison.py` & `python_jsonpath-0.4.0/tests/test_ietf_comparison.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/tests/test_lex.py` & `python_jsonpath-0.4.0/tests/test_lex.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/tests/test_match_api.py` & `python_jsonpath-0.4.0/tests/test_match_api.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/tests/test_parse.py` & `python_jsonpath-0.4.0/tests/test_parse.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/tests/test_parse_compound_path.py` & `python_jsonpath-0.4.0/tests/test_parse_compound_path.py`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/tests/test_re.py` & `python_jsonpath-0.4.0/tests/test_re.py`

 * *Files 6% similar despite different names*

```diff
@@ -20,27 +20,27 @@
     want: Union[Sequence[Any], Mapping[str, Any]]
 
 
 TEST_CASES = [
     Case(
         description="match a regex",
         path="$.some[?(@.thing =~ /fo[a-z]/)]",
-        data={"some": {"thing": "foo"}},
+        data={"some": [{"thing": "foo"}]},
         want=[{"thing": "foo"}],
     ),
     Case(
         description="regex with no match",
         path="$.some[?(@.thing =~ /fo[a-z]/)]",
-        data={"some": {"thing": "foO"}},
+        data={"some": [{"thing": "foO"}]},
         want=[],
     ),
     Case(
         description="case insensitive match",
         path="$.some[?(@.thing =~ /fo[a-z]/i)]",
-        data={"some": {"thing": "foO"}},
+        data={"some": [{"thing": "foO"}]},
         want=[{"thing": "foO"}],
     ),
 ]
 
 
 @pytest.fixture()
 def env() -> JSONPathEnvironment:
```

### Comparing `python_jsonpath-0.3.0/.gitignore` & `python_jsonpath-0.4.0/.gitignore`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/LICENSE.txt` & `python_jsonpath-0.4.0/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/README.md` & `python_jsonpath-0.4.0/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -226,31 +226,31 @@
 ```
 
 ### Filters (`[?(EXPRESSION)]`)
 
 Filters allow you to remove nodes from a selection using a Boolean expression. Within a filter, `@` refers to the current node and `$` refers to the root node in the target document. `@` and `$` can be used to select nodes as part of the expression. Since version 0.3.0, the parentheses are optional, as per the IETF JSONPath draft. These two examples are equivalent.
 
 ```text
-$..products.*[?(@.price < $.price_cap)]
+$..products[?(@.price < $.price_cap)]
 ```
 
 ```text
-$..products.*[?@.price < $.price_cap]
+$..products[?@.price < $.price_cap]
 ```
 
 Comparison operators include `==`, `!=`, `<`, `>`, `<=` and `>=`. Plus `<>` as an alias for `!=`.
 
 `in` and `contains` are membership operators. `left in right` is equivalent to `right contains left`.
 
 `&&` and `||` are logical operators, `and` and `or` work too.
 
 `=~` matches the left value with a regular expression literal. Regular expressions use a syntax similar to that found in JavaScript, where the pattern to match is surrounded by slashes, optionally followed by flags.
 
 ```text
-$..products.*[?(@.description =~ /.*trainers/i)]
+$..products[?(@.description =~ /.*trainers/i)]
 ```
 
 Filters can use [function extensions](#function-extensions) too.
 
 ### Union (`|`) and intersection (`&`)
 
 Union (`|`) and intersection (`&`) are similar to Python's set operations, but we don't dedupe the matches (matches will often contain unhashable objects).
@@ -260,15 +260,15 @@
 ```text
 $..products.*.price | $.price_cap
 ```
 
 The `&` operator produces matches that are common to both left and right paths. This example would select the list of products that are common to both the "footwear" and "headwear" categories.
 
 ```text
-$.categories.*[?(@.name == 'footwear')].products.* & $.categories.*[?(@.name == 'headwear')].products.*
+$.categories[?(@.name == 'footwear')].products.* & $.categories[?(@.name == 'headwear')].products.*
 ```
 
 Note that `|` and `&` are not allowed inside filter expressions.
 
 ## Function extensions
 
 TODO:
@@ -286,15 +286,14 @@
 
 - For now, the only built-in function extension is `length()`.
 - We don't require filters that use a function extension to include a comparison operator.
 - Whitespace is mostly insignificant unless inside quotes.
 - The root token (default `$`) is optional.
 - Paths starting with a dot (`.`) are OK. `.thing` is the same as `$.thing`, as is `thing`, `$[thing]` and `$["thing"]`.
 - Nested filters are not supported.
-- We don't treat filter expressions without a comparison as existence test, but an "is truthy" test. See the "Existence of non-singular queries" example in the IETF JSONPath draft.
 
 And this is a list of features that are uncommon or unique to Python JSONPath.
 
 - `|` is a union operator, where matches from two or more JSONPaths are combined. This is not part of the Python API, but built-in to the JSONPath syntax.
 - `&` is an intersection operator, where we exclude matches that don't exist in both left and right paths. This is not part of the Python API, but built-in to the JSONPath syntax.
 - `#` is a filter context selector. With usage similar to `$` and `@`, `#` exposes arbitrary data from the `filter_context` argument to `findall()` and `finditer()`.
```

### Comparing `python_jsonpath-0.3.0/pyproject.toml` & `python_jsonpath-0.4.0/pyproject.toml`

 * *Files identical despite different names*

### Comparing `python_jsonpath-0.3.0/PKG-INFO` & `python_jsonpath-0.4.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: python-jsonpath
-Version: 0.3.0
+Version: 0.4.0
 Summary: Another JSONPath implementation for Python.
 Project-URL: Documentation, https://jg-rp.github.io/python-jsonpath/
 Project-URL: Issues, https://github.com/jg-rp/python-jsonpath/issues
 Project-URL: Source, https://github.com/jg-rp/python-jsonpath
 Author-email: James Prior <jamesgr.prior@gmail.com>
 License-Expression: MIT
 License-File: LICENSE.txt
@@ -250,31 +250,31 @@
 ```
 
 ### Filters (`[?(EXPRESSION)]`)
 
 Filters allow you to remove nodes from a selection using a Boolean expression. Within a filter, `@` refers to the current node and `$` refers to the root node in the target document. `@` and `$` can be used to select nodes as part of the expression. Since version 0.3.0, the parentheses are optional, as per the IETF JSONPath draft. These two examples are equivalent.
 
 ```text
-$..products.*[?(@.price < $.price_cap)]
+$..products[?(@.price < $.price_cap)]
 ```
 
 ```text
-$..products.*[?@.price < $.price_cap]
+$..products[?@.price < $.price_cap]
 ```
 
 Comparison operators include `==`, `!=`, `<`, `>`, `<=` and `>=`. Plus `<>` as an alias for `!=`.
 
 `in` and `contains` are membership operators. `left in right` is equivalent to `right contains left`.
 
 `&&` and `||` are logical operators, `and` and `or` work too.
 
 `=~` matches the left value with a regular expression literal. Regular expressions use a syntax similar to that found in JavaScript, where the pattern to match is surrounded by slashes, optionally followed by flags.
 
 ```text
-$..products.*[?(@.description =~ /.*trainers/i)]
+$..products[?(@.description =~ /.*trainers/i)]
 ```
 
 Filters can use [function extensions](#function-extensions) too.
 
 ### Union (`|`) and intersection (`&`)
 
 Union (`|`) and intersection (`&`) are similar to Python's set operations, but we don't dedupe the matches (matches will often contain unhashable objects).
@@ -284,15 +284,15 @@
 ```text
 $..products.*.price | $.price_cap
 ```
 
 The `&` operator produces matches that are common to both left and right paths. This example would select the list of products that are common to both the "footwear" and "headwear" categories.
 
 ```text
-$.categories.*[?(@.name == 'footwear')].products.* & $.categories.*[?(@.name == 'headwear')].products.*
+$.categories[?(@.name == 'footwear')].products.* & $.categories[?(@.name == 'headwear')].products.*
 ```
 
 Note that `|` and `&` are not allowed inside filter expressions.
 
 ## Function extensions
 
 TODO:
@@ -310,15 +310,14 @@
 
 - For now, the only built-in function extension is `length()`.
 - We don't require filters that use a function extension to include a comparison operator.
 - Whitespace is mostly insignificant unless inside quotes.
 - The root token (default `$`) is optional.
 - Paths starting with a dot (`.`) are OK. `.thing` is the same as `$.thing`, as is `thing`, `$[thing]` and `$["thing"]`.
 - Nested filters are not supported.
-- We don't treat filter expressions without a comparison as existence test, but an "is truthy" test. See the "Existence of non-singular queries" example in the IETF JSONPath draft.
 
 And this is a list of features that are uncommon or unique to Python JSONPath.
 
 - `|` is a union operator, where matches from two or more JSONPaths are combined. This is not part of the Python API, but built-in to the JSONPath syntax.
 - `&` is an intersection operator, where we exclude matches that don't exist in both left and right paths. This is not part of the Python API, but built-in to the JSONPath syntax.
 - `#` is a filter context selector. With usage similar to `$` and `@`, `#` exposes arbitrary data from the `filter_context` argument to `findall()` and `finditer()`.
```

