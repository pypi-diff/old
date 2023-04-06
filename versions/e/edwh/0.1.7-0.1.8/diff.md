# Comparing `tmp/edwh-0.1.7.tar.gz` & `tmp/edwh-0.1.8.tar.gz`

## Comparing `edwh-0.1.7.tar` & `edwh-0.1.8.tar`

### file list

```diff
@@ -1,16 +1,122 @@
--rw-r--r--   0        0        0      176 2020-02-02 00:00:00.000000 edwh-0.1.7/.idea/.gitignore
--rw-r--r--   0        0        0      325 2020-02-02 00:00:00.000000 edwh-0.1.7/.idea/edwh.iml
--rw-r--r--   0        0        0      327 2020-02-02 00:00:00.000000 edwh-0.1.7/.idea/misc.xml
--rw-r--r--   0        0        0      260 2020-02-02 00:00:00.000000 edwh-0.1.7/.idea/modules.xml
--rw-r--r--   0        0        0      495 2020-02-02 00:00:00.000000 edwh-0.1.7/.idea/vcs.xml
--rw-r--r--   0        0        0     3383 2020-02-02 00:00:00.000000 edwh-0.1.7/.idea/workspace.xml
--rw-r--r--   0        0        0      174 2020-02-02 00:00:00.000000 edwh-0.1.7/.idea/inspectionProfiles/profiles_settings.xml
--rw-r--r--   0        0        0      139 2020-02-02 00:00:00.000000 edwh-0.1.7/src/edwh/__about__.py
--rw-r--r--   0        0        0      117 2020-02-02 00:00:00.000000 edwh-0.1.7/src/edwh/__init__.py
--rw-r--r--   0        0        0     1148 2020-02-02 00:00:00.000000 edwh-0.1.7/src/edwh/cli.py
--rw-r--r--   0        0        0      143 2020-02-02 00:00:00.000000 edwh-0.1.7/src/edwh/tasks.py
--rw-r--r--   0        0        0      117 2020-02-02 00:00:00.000000 edwh-0.1.7/tests/__init__.py
--rw-r--r--   0        0        0     1094 2020-02-02 00:00:00.000000 edwh-0.1.7/LICENSE.txt
--rw-r--r--   0        0        0      451 2020-02-02 00:00:00.000000 edwh-0.1.7/README.md
--rw-r--r--   0        0        0     3634 2020-02-02 00:00:00.000000 edwh-0.1.7/pyproject.toml
--rw-r--r--   0        0        0     1942 2020-02-02 00:00:00.000000 edwh-0.1.7/PKG-INFO
+-rw-r--r--   0        0        0     2340 2020-02-02 00:00:00.000000 edwh-0.1.8/.idea/jupyter-settings.xml
+-rw-r--r--   0        0        0      495 2020-02-02 00:00:00.000000 edwh-0.1.8/.idea/vcs.xml
+-rw-r--r--   0        0        0     4219 2020-02-02 00:00:00.000000 edwh-0.1.8/.idea/workspace.xml
+-rw-r--r--   0        0        0      390 2020-02-02 00:00:00.000000 edwh-0.1.8/.idea/shelf/Uncommitted_changes_before_Update_at_05-04-2023_11_26__Changes_.xml
+-rw-r--r--   0        0        0      392 2020-02-02 00:00:00.000000 edwh-0.1.8/.idea/shelf/Uncommitted_changes_before_Update_at_06-04-2023_13_14__Changes_.xml
+-rw-r--r--   0        0        0      392 2020-02-02 00:00:00.000000 edwh-0.1.8/.idea/shelf/Uncommitted_changes_before_Update_at_06-04-2023_13_14__Changes_1.xml
+-rw-r--r--   0        0        0     3389 2020-02-02 00:00:00.000000 edwh-0.1.8/.idea/shelf/Uncommitted_changes_before_Update_at_05-04-2023_11_26_[Changes]/shelved.patch
+-rw-r--r--   0        0        0     2242 2020-02-02 00:00:00.000000 edwh-0.1.8/.idea/shelf/Uncommitted_changes_before_Update_at_06-04-2023_13_14_[Changes]/shelved.patch
+-rw-r--r--   0        0        0      831 2020-02-02 00:00:00.000000 edwh-0.1.8/.idea/shelf/Uncommitted_changes_before_Update_at_06-04-2023_13_14_[Changes]1/shelved.patch
+-rw-r--r--   0        0        0       34 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/.gitignore
+-rw-r--r--   0        0        0      190 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/CACHEDIR.TAG
+-rw-r--r--   0        0        0        2 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/@plugins_snapshot.json
+-rw-r--r--   0        0        0   193690 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/_ast.data.json
+-rw-r--r--   0        0        0     1791 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/_ast.meta.json
+-rw-r--r--   0        0        0    57310 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/_codecs.data.json
+-rw-r--r--   0        0        0     1837 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/_codecs.meta.json
+-rw-r--r--   0        0        0    19783 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/_collections_abc.data.json
+-rw-r--r--   0        0        0     1745 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/_collections_abc.meta.json
+-rw-r--r--   0        0        0     3196 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/_ctypes.data.json
+-rw-r--r--   0        0        0     1747 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/_ctypes.meta.json
+-rw-r--r--   0        0        0    22378 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/abc.data.json
+-rw-r--r--   0        0        0     1733 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/abc.meta.json
+-rw-r--r--   0        0        0    66395 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/array.data.json
+-rw-r--r--   0        0        0     1800 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/array.meta.json
+-rw-r--r--   0        0        0  1141227 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/builtins.data.json
+-rw-r--r--   0        0        0     1897 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/builtins.meta.json
+-rw-r--r--   0        0        0   134231 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/codecs.data.json
+-rw-r--r--   0        0        0     1851 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/codecs.meta.json
+-rw-r--r--   0        0        0   113689 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/contextlib.data.json
+-rw-r--r--   0        0        0     1775 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/contextlib.meta.json
+-rw-r--r--   0        0        0    63269 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/dataclasses.data.json
+-rw-r--r--   0        0        0     1793 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/dataclasses.meta.json
+-rw-r--r--   0        0        0    66858 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/enum.data.json
+-rw-r--r--   0        0        0     1765 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/enum.meta.json
+-rw-r--r--   0        0        0    24418 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/genericpath.data.json
+-rw-r--r--   0        0        0     1762 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/genericpath.meta.json
+-rw-r--r--   0        0        0    93277 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/io.data.json
+-rw-r--r--   0        0        0     1856 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/io.meta.json
+-rw-r--r--   0        0        0    31524 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/mmap.data.json
+-rw-r--r--   0        0        0     1799 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/mmap.meta.json
+-rw-r--r--   0        0        0    96592 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/pathlib.data.json
+-rw-r--r--   0        0        0     1865 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/pathlib.meta.json
+-rw-r--r--   0        0        0    48558 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/pickle.data.json
+-rw-r--r--   0        0        0     1801 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/pickle.meta.json
+-rw-r--r--   0        0        0    82126 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/posixpath.data.json
+-rw-r--r--   0        0        0     1795 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/posixpath.meta.json
+-rw-r--r--   0        0        0   182939 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/re.data.json
+-rw-r--r--   0        0        0     1887 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/re.meta.json
+-rw-r--r--   0        0        0    15221 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/sre_compile.data.json
+-rw-r--r--   0        0        0     1731 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/sre_compile.meta.json
+-rw-r--r--   0        0        0    30275 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/sre_constants.data.json
+-rw-r--r--   0        0        0     1743 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/sre_constants.meta.json
+-rw-r--r--   0        0        0    53725 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/sre_parse.data.json
+-rw-r--r--   0        0        0     1795 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/sre_parse.meta.json
+-rw-r--r--   0        0        0   173191 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/subprocess.data.json
+-rw-r--r--   0        0        0     1855 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/subprocess.meta.json
+-rw-r--r--   0        0        0   152168 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/sys.data.json
+-rw-r--r--   0        0        0     1834 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/sys.meta.json
+-rw-r--r--   0        0        0   248525 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/types.data.json
+-rw-r--r--   0        0        0     1806 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/types.meta.json
+-rw-r--r--   0        0        0   444970 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/typing.data.json
+-rw-r--r--   0        0        0     1872 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/typing.meta.json
+-rw-r--r--   0        0        0    73973 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/typing_extensions.data.json
+-rw-r--r--   0        0        0     1796 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/typing_extensions.meta.json
+-rw-r--r--   0        0        0    96993 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/_typeshed/__init__.data.json
+-rw-r--r--   0        0        0     1869 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/_typeshed/__init__.meta.json
+-rw-r--r--   0        0        0   446284 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/collections/__init__.data.json
+-rw-r--r--   0        0        0     1880 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/collections/__init__.meta.json
+-rw-r--r--   0        0        0     4058 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/collections/abc.data.json
+-rw-r--r--   0        0        0     1711 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/collections/abc.meta.json
+-rw-r--r--   0        0        0   140957 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/ctypes/__init__.data.json
+-rw-r--r--   0        0        0     1843 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/ctypes/__init__.meta.json
+-rw-r--r--   0        0        0     1579 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/edwh/__about__.data.json
+-rw-r--r--   0        0        0     1576 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/edwh/__about__.meta.json
+-rw-r--r--   0        0        0     1525 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/edwh/__init__.data.json
+-rw-r--r--   0        0        0     1565 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/edwh/__init__.meta.json
+-rw-r--r--   0        0        0     1547 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/edwh/cli.data.json
+-rw-r--r--   0        0        0     1584 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/edwh/cli.meta.json
+-rw-r--r--   0        0        0     8144 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/email/__init__.data.json
+-rw-r--r--   0        0        0     1772 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/email/__init__.meta.json
+-rw-r--r--   0        0        0    13296 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/email/charset.data.json
+-rw-r--r--   0        0        0     1708 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/email/charset.meta.json
+-rw-r--r--   0        0        0     7918 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/email/contentmanager.data.json
+-rw-r--r--   0        0        0     1743 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/email/contentmanager.meta.json
+-rw-r--r--   0        0        0    27009 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/email/errors.data.json
+-rw-r--r--   0        0        0     1715 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/email/errors.meta.json
+-rw-r--r--   0        0        0    10010 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/email/header.data.json
+-rw-r--r--   0        0        0     1728 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/email/header.meta.json
+-rw-r--r--   0        0        0    86512 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/email/message.data.json
+-rw-r--r--   0        0        0     1846 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/email/message.meta.json
+-rw-r--r--   0        0        0    33595 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/email/policy.data.json
+-rw-r--r--   0        0        0     1801 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/email/policy.meta.json
+-rw-r--r--   0        0        0     6704 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/importlib/__init__.data.json
+-rw-r--r--   0        0        0     1746 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/importlib/__init__.meta.json
+-rw-r--r--   0        0        0    75549 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/importlib/abc.data.json
+-rw-r--r--   0        0        0     1829 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/importlib/abc.meta.json
+-rw-r--r--   0        0        0    69950 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/importlib/machinery.data.json
+-rw-r--r--   0        0        0     1905 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/importlib/machinery.meta.json
+-rw-r--r--   0        0        0    97916 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/importlib/metadata/__init__.data.json
+-rw-r--r--   0        0        0     1911 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/importlib/metadata/__init__.meta.json
+-rw-r--r--   0        0        0    12954 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/importlib/metadata/_meta.data.json
+-rw-r--r--   0        0        0     1728 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/importlib/metadata/_meta.meta.json
+-rw-r--r--   0        0        0   382607 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/os/__init__.data.json
+-rw-r--r--   0        0        0     1914 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/os/__init__.meta.json
+-rw-r--r--   0        0        0     5337 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/os/path.data.json
+-rw-r--r--   0        0        0     1703 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/os/path.meta.json
+-rw-r--r--   0        0        0     1529 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/tests/__init__.data.json
+-rw-r--r--   0        0        0     1563 2020-02-02 00:00:00.000000 edwh-0.1.8/.mypy_cache/3.10/tests/__init__.meta.json
+-rw-r--r--   0        0        0       37 2020-02-02 00:00:00.000000 edwh-0.1.8/.pytest_cache/.gitignore
+-rw-r--r--   0        0        0      191 2020-02-02 00:00:00.000000 edwh-0.1.8/.pytest_cache/CACHEDIR.TAG
+-rw-r--r--   0        0        0      302 2020-02-02 00:00:00.000000 edwh-0.1.8/.pytest_cache/README.md
+-rw-r--r--   0        0        0        2 2020-02-02 00:00:00.000000 edwh-0.1.8/.pytest_cache/v/cache/nodeids
+-rw-r--r--   0        0        0        2 2020-02-02 00:00:00.000000 edwh-0.1.8/.pytest_cache/v/cache/stepwise
+-rw-r--r--   0        0        0      139 2020-02-02 00:00:00.000000 edwh-0.1.8/src/edwh/__about__.py
+-rw-r--r--   0        0        0      117 2020-02-02 00:00:00.000000 edwh-0.1.8/src/edwh/__init__.py
+-rw-r--r--   0        0        0     1148 2020-02-02 00:00:00.000000 edwh-0.1.8/src/edwh/cli.py
+-rw-r--r--   0        0        0      143 2020-02-02 00:00:00.000000 edwh-0.1.8/src/edwh/tasks.py
+-rw-r--r--   0        0        0      117 2020-02-02 00:00:00.000000 edwh-0.1.8/tests/__init__.py
+-rw-r--r--   0        0        0     1094 2020-02-02 00:00:00.000000 edwh-0.1.8/LICENSE.txt
+-rw-r--r--   0        0        0      451 2020-02-02 00:00:00.000000 edwh-0.1.8/README.md
+-rw-r--r--   0        0        0     3658 2020-02-02 00:00:00.000000 edwh-0.1.8/pyproject.toml
+-rw-r--r--   0        0        0     1996 2020-02-02 00:00:00.000000 edwh-0.1.8/PKG-INFO
```

### Comparing `edwh-0.1.7/src/edwh/cli.py` & `edwh-0.1.8/src/edwh/cli.py`

 * *Files identical despite different names*

### Comparing `edwh-0.1.7/LICENSE.txt` & `edwh-0.1.8/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `edwh-0.1.7/pyproject.toml` & `edwh-0.1.8/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -36,14 +36,15 @@
   'humanize',
   'tabulate',
   'pyyaml',
 ]
 plugins = [
   'edwh-multipass-plugin',
   'edwh-demo-tasks-plugin',
+  'edwh-restic-plugin',
 ]
 
 [project.scripts]
 edwh = "edwh.cli:program.run"
 ew = "edwh.cli:program.run"
 
 [project.urls]
```

### Comparing `edwh-0.1.7/PKG-INFO` & `edwh-0.1.8/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: edwh
-Version: 0.1.7
+Version: 0.1.8
 Summary: Education Warehouse maintenance tools
 Project-URL: Documentation, https://github.com/educationwarehouse/edwh#readme
 Project-URL: Issues, https://github.com/educationwarehouse/edwh/issues
 Project-URL: Source, https://github.com/educationwarehouse/edwh
 Author-email: Remco Boerma <remco.b@educationwarehouse.nl>, Robin van der Noord <robin.vdn@educationwarehouse.nl>, Romy Schöller <romy.s@educationwarehouse.nl>, Sven Keimpema <sven.k@educationwarehouse.nl>
 License-Expression: MIT
 License-File: LICENSE.txt
@@ -23,14 +23,15 @@
 Provides-Extra: omgeving
 Requires-Dist: humanize; extra == 'omgeving'
 Requires-Dist: pyyaml; extra == 'omgeving'
 Requires-Dist: tabulate; extra == 'omgeving'
 Provides-Extra: plugins
 Requires-Dist: edwh-demo-tasks-plugin; extra == 'plugins'
 Requires-Dist: edwh-multipass-plugin; extra == 'plugins'
+Requires-Dist: edwh-restic-plugin; extra == 'plugins'
 Description-Content-Type: text/markdown
 
 # edwh
 
 [![PyPI - Version](https://img.shields.io/pypi/v/edwh.svg)](https://pypi.org/project/edwh)
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/edwh.svg)](https://pypi.org/project/edwh)
```

